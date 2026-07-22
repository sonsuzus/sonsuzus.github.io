---
layout: post
title: "Raspberry Pi Device Tree Sorgulayıcı: GPIO, I2C ve SPI Fiziksel Adreslerini Avlamak"
math: true
categories: 
  - Proje
tags: 
  - raspberry-pi
  - device-tree
  - linux
  - gpio
  - python
---

Raspberry Pi üzerinde GPIO, I2C, SPI ya da UART gibi çevre birimlerinin fiziksel adreslerini öğrenmek istiyorsan genelde datasheet, forum ve kernel kaynak kodu üçgeninde kaybolursun. Oysa Linux zaten bu bilgilerin büyük kısmını Device Tree üzerinden çekirdeğe sunar. Bu yazıda /proc/device-tree dosyalarını okuyarak çevre birimlerini ve adres aralıklarını listeleyen küçük ama güçlü bir sorgu aracı tasarlayacağız.
``

Device Tree, donanıma ait hiyerarşik bir tarif dosyasıdır. Kernel açılırken “şu adreste GPIO var”, “bu I2C kontrolcüsü şu kesmeyi kullanıyor” gibi bilgileri buradan okur. Raspberry Pi’de bu ağaç genellikle `/proc/device-tree` altında sanal dosya sistemi olarak görünür. Her klasör bir düğüm, her dosya ise bir özelliktir. Örneğin `compatible`, `status`, `reg` ve `ranges` en sık karşımıza çıkan özelliklerdir.

Buradaki asıl sihir `reg` alanındadır. Ancak `reg` düz bir sayı değildir; kaç hücreden oluşacağı üst düğümdeki `#address-cells` ve `#size-cells` değerlerine bağlıdır. Basitçe düşünürsek:

$$reg = address_{cells} + size_{cells}$$

Eğer `#address-cells = 1` ve `#size-cells = 1` ise `reg` içinde önce başlangıç adresi, ardından boyut gelir. Raspberry Pi SoC çevre birimleri çoğunlukla bellek eşlemeli I/O kullandığından, bu adresler CPU’nun fiziksel adres haritasına bağlanır. Yani GPIO’ya yazmak aslında belirli bir bellek adresine yazmaktır. Eğlenceli tarafı şu: LED yakmak, teoride RAM’e mektup bırakmak gibidir; sadece mektubu alan kişi bir GPIO kontrolcüsüdür.

| Kavram | Ne Anlama Gelir? | Örnek |
|---|---|---|
| Node | Donanım bileşeni | `gpio@7e200000` |
| Property | Düğüm bilgisi | `compatible`, `reg` |
| `reg` | Adres ve boyut | `0x7e200000 0xb4` |
| `ranges` | Bus adresini CPU adresine çevirir | `0x7e000000 -> 0xfe000000` |
| `status` | Aygıt aktif mi? | `okay`, `disabled` |

Adres yorumlarken önemli bir ayrım vardır: Device Tree’de görülen bus adresi her zaman CPU fiziksel adresi olmayabilir. Özellikle Raspberry Pi modellerinde peripheral base adresi modele göre değişebilir. Örneğin eski modellerde `0x20000000`, Pi 2/3 tarafında `0x3f000000`, Pi 4 tarafında `0xfe000000` sık görülür. Device Tree’deki `ranges` alanı bu dönüşümün ipucunu verir.

| Raspberry Pi Nesli | Yaygın Peripheral Base | Not |
|---|---:|---|
| Pi 1 / Zero | `0x20000000` | BCM2835 |
| Pi 2 / Pi 3 | `0x3f000000` | BCM2836/2837 |
| Pi 4 | `0xfe000000` | BCM2711 |

Şimdi Python ile bir tarayıcı yazalım. Amaç: `/proc/device-tree` altında gezmek, `compatible` veya düğüm adına göre GPIO/I2C/SPI adaylarını bulmak, `reg` alanını okuyup adresleri hesaplamak.

```python
from pathlib import Path
import struct

DT = Path('/proc/device-tree')
KEYWORDS = ('gpio', 'i2c', 'spi')

def read_prop(path):
    try:
        return path.read_bytes()
    except FileNotFoundError:
        return None

def read_u32_cells(prop):
    if not prop:
        return []
    count = len(prop) // 4
    return list(struct.unpack('>' + 'I' * count, prop[:count * 4]))

def read_text(prop):
    if not prop:
        return ''
    return prop.replace(b'\x00', b',').decode(errors='ignore').strip(',')

def get_cells(node, name, default):
    current = node
    while current != current.parent:
        value = read_prop(current / name)
        if value:
            cells = read_u32_cells(value)
            return cells[0] if cells else default
        current = current.parent
    return default

def parse_reg(node):
    reg = read_u32_cells(read_prop(node / 'reg'))
    if not reg:
        return []

    parent = node.parent
    addr_cells = get_cells(parent, '#address-cells', 1)
    size_cells = get_cells(parent, '#size-cells', 1)
    step = addr_cells + size_cells
    results = []

    for i in range(0, len(reg), step):
        addr = 0
        size = 0
        for cell in reg[i:i + addr_cells]:
            addr = (addr << 32) | cell
        for cell in reg[i + addr_cells:i + step]:
            size = (size << 32) | cell
        results.append((addr, size))
    return results

def scan():
    for node in DT.rglob('*'):
        if not node.is_dir():
            continue
        name = node.name.lower()
        compatible = read_text(read_prop(node / 'compatible')).lower()
        if any(k in name or k in compatible for k in KEYWORDS):
            regs = parse_reg(node)
            status = read_text(read_prop(node / 'status')) or 'okay?'
            if regs:
                print(f'[{status}] {node.relative_to(DT)}')
                print(f'  compatible: {compatible}')
                for addr, size in regs:
                    print(f'  reg: 0x{addr:08x} size=0x{size:x}')

if __name__ == '__main__':
    scan()
```

Kodun yaptığı şey oldukça mekanik: dosyaları byte olarak okuyor, Device Tree hücreleri big-endian olduğu için `struct.unpack('>I')` kullanıyor ve `reg` alanını üst düğümdeki hücre sayılarına göre parçalıyor. Burada dikkat edilmesi gereken nokta, çıktıdaki adresin her zaman nihai CPU fiziksel adresi olmayabileceğidir. Daha ileri sürümde `ranges` ayrıştırması ekleyerek bus adresinden fiziksel adrese dönüşüm yapabiliriz.

Mini aracın örnek çıktısı şöyle görünebilir:

```text
[okay] soc/gpio@7e200000
  compatible: brcm,bcm2711-gpio
  reg: 0x7e200000 size=0xb4

[okay] soc/i2c@7e804000
  compatible: brcm,bcm2711-i2c
  reg: 0x7e804000 size=0x1000
```

Bu proje bize iki önemli şey öğretir: Linux altında donanım bilgisi çoğu zaman zaten elimizin altındadır ve “adres” dediğimiz şey bağlama göre değişir. Device Tree okuma aracı, gömülü Linux dünyasında debugging için İsviçre çakısı gibidir. Bir sonraki adımda çıktıyı JSON’a çevirip web arayüzü ekleyebilir, hatta `devmem` ile güvenli salt-okunur register inceleme modülü yazabilirsin.
