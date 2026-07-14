---
layout: post
title: "C ile Donanım İletişimi: Eski Disklerden Adaptörlere Sürücü Mantığı"
math: true
categories: 
  - Program
tags: 
  - C
  - donanım
  - sürücü-geliştirme
---

Eski bir IDE disk, USB-SATA dönüştürücü ya da seri port adaptörü elinize geçtiğinde ilk soru genelde şudur: “Bunu işletim sistemiyle nasıl konuştururum?” C dili burada hâlâ sahnenin başrol oyuncusudur; çünkü donanıma yakın, bellek düzenini tahmin edilebilir kılan ve kesme, DMA, I/O portu gibi düşük seviye kavramları açıkça modelleyebilen bir araçtır.
``
Donanım iletişimini sürücü seviyesinde düşünürken üç katmanı ayırmak gerekir: fiziksel aygıt, denetleyici protokolü ve işletim sistemi arayüzü. Örneğin eski bir ATA disk doğrudan “dosya” bilmez; sektör okur, sektör yazar. Dosya sistemi ise bu ham blokların üzerine kurulan daha üst seviye bir soyutlamadır. Sürücü algoritmanızın görevi, işletim sisteminden gelen “şu blokları oku” isteğini aygıtın anlayacağı komutlara çevirmektir.

Teorik olarak blok tabanlı aygıtlarda en küçük adreslenebilir birim genellikle sektördür. Klasik disklerde sektör boyutu çoğunlukla 512 bayt, yeni disklerde ise 4096 bayt olabilir. Bir okuma işleminin yaklaşık maliyeti şu şekilde düşünülebilir:

$$T_{okuma} = T_{arama} + T_{gecikme} + \frac{B}{R}$$

Burada $B$ okunan bayt miktarı, $R$ aktarım hızı, $T_{arama}$ mekanik kafanın konumlanma süresi, $T_{gecikme}$ ise dönüş gecikmesidir. SSD ve USB adaptörlerde mekanik süreler yoktur ama komut kuyruğu, veri yolu gecikmesi ve köprü yongasının davranışı hâlâ önemlidir.

| Yaklaşım | Kullanım Alanı | Avantaj | Risk |
|---|---|---|---|
| Port I/O | Eski x86 ATA, seri port | Basit ve doğrudan | Mimariye bağımlı |
| MMIO | PCI/PCIe aygıtlar | Bellek gibi erişim | Yanlış adres sistemi kilitleyebilir |
| DMA | Yüksek hızlı disk, ağ kartı | CPU yükü az | Bellek eşleme hataları tehlikeli |
| USB sınıf sürücüsü | Harici adaptörler | Standart protokoller | Köprü yongası farklı davranabilir |

C tarafında en temel fikir, donanım kayıtlarını temsil eden kesin boyutlu veri tipleri kullanmaktır. `uint8_t`, `uint16_t` ve `uint32_t` bu yüzden önemlidir. Ayrıca derleyicinin optimizasyon sırasında donanım erişimini “gereksiz” sanıp silmemesi için `volatile` kullanılır.

```c
#include <stdint.h>

#define ATA_DATA       0x1F0
#define ATA_SECTOR_CNT 0x1F2
#define ATA_LBA_LOW    0x1F3
#define ATA_COMMAND    0x1F7

static inline void outb(uint16_t port, uint8_t value) {
    __asm__ volatile ("outb %0, %1" : : "a"(value), "Nd"(port));
}

static inline uint8_t inb(uint16_t port) {
    uint8_t value;
    __asm__ volatile ("inb %1, %0" : "=a"(value) : "Nd"(port));
    return value;
}
```

Bu örnekte x86 üzerinde I/O portlarına erişen küçük yardımcı fonksiyonlar var. `outb` donanıma komut veya parametre gönderir, `inb` ise durum bayrağı okur. Gerçek bir çekirdek sürücüsünde bunlar doğrudan kullanıcı programından çağrılamaz; ayrıcalıklı kip gerekir. Linux’ta bu iş çekirdek modülü, Windows’ta ise WDM/KMDF sürücüsü üzerinden yapılır.

Bir sürücü algoritmasının kalbi genellikle durum makinesidir. Aygıta komut verilir, aygıt meşgul olur, sonra hazır bayrağı beklenir. Basitleştirilmiş akış şöyledir:

```c
enum disk_state {
    DISK_IDLE,
    DISK_SEND_CMD,
    DISK_WAIT_READY,
    DISK_TRANSFER,
    DISK_ERROR
};

int wait_ready(void) {
    for (int i = 0; i < 100000; i++) {
        uint8_t status = inb(ATA_COMMAND);
        if ((status & 0x80) == 0 && (status & 0x08))
            return 0;
    }
    return -1;
}
```

Burada `0x80` meşgul bayrağını, `0x08` veri hazır bayrağını temsil eder. Döngü sonsuza kadar beklemek yerine zaman aşımı uygular; çünkü donanım dünyasında “cevap gelmedi” de geçerli bir cevaptır. Sağlam sürücü yazmanın sırrı, mutlu yoldan çok hata yollarını ciddiye almaktır.

Harici adaptörlerde tablo biraz değişir. USB-SATA köprüleri çoğunlukla Mass Storage Class ya da UASP kullanır. Siz doğrudan ATA portuna yazmazsınız; SCSI benzeri komut paketleri gönderirsiniz. Yani algoritma yine blok okuma/yazma yapar ama alttaki taşıma protokolü farklıdır. Bu yüzden iyi tasarımda “blok aygıt arayüzü” ile “taşıma katmanı” ayrılır.

Son olarak güvenlik notu: Gerçek disklere deneme sürücüsüyle yazmak veri kaybına yol açabilir. Önce QEMU, Bochs, loop device veya sahte blok aygıtlarıyla test yapmak en sağlıklı yoldur. C ile donanım konuşmak, biraz arkeoloji biraz da elektrikli ejderha terbiyeciliğidir: protokolü okur, bayrakları izler, zaman aşımını koyar ve asla donanıma körü körüne güvenmezsiniz.
