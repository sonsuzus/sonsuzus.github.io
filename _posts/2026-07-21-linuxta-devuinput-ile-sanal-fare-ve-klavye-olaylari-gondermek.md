---
layout: post
title: "Linux’ta /dev/uinput ile Sanal Fare ve Klavye Olayları Göndermek"
math: true
categories: 
  - Program
tags: 
  - linux
  - uinput
  - input-simulation
  - python
  - evdev
---

Bazen fiziksel bir fareye ya da klavyeye dokunmadan sisteme giriş olayı göndermek isteriz: test otomasyonu, erişilebilirlik araçları, kiosk sistemleri, oyun botu prototipleri veya uzaktan kontrol yazılımları buna örnektir. Linux tarafında bu işin en temiz yollarından biri `/dev/uinput` aygıtıdır. Kısaca uinput, kullanıcı alanındaki bir programın çekirdeğe “Ben bir input aygıtıyım” demesini ve gerçek donanım gibi olay üretmesini sağlar.
``
Linux input mimarisinde olaylar genellikle `/dev/input/eventX` dosyaları üzerinden okunur. Gerçek klavye, fare, gamepad gibi donanımlar çekirdeğe olay üretir; masaüstü ortamı da bunları tüketir. `/dev/uinput` ise bu akışı tersine çevirir: kullanıcı alanındaki program çekirdeğe sanal cihaz kaydeder ve olayları içeri enjekte eder.

Teorik olarak bir giriş olayı şu üçlüyle düşünülebilir:

$$Olay = (tip, kod, değer)$$

Örneğin klavyede A tuşuna basmak için tip `EV_KEY`, kod `KEY_A`, değer `1` gönderilir. Tuşu bırakmak için değer `0` kullanılır. Fare hareketi ise `EV_REL`, `REL_X`, `REL_Y` gibi göreli eksen olaylarıyla temsil edilir. Her olay grubundan sonra `EV_SYN` gönderilerek “bu paket tamamlandı” denir.

| Kavram | Anlamı | Örnek |
|---|---|---|
| `EV_KEY` | Tuş veya buton olayı | `KEY_ENTER`, `BTN_LEFT` |
| `EV_REL` | Göreli hareket | `REL_X`, `REL_Y` |
| `EV_ABS` | Mutlak koordinat | Dokunmatik ekran ekseni |
| `EV_SYN` | Olayları senkronize eder | `SYN_REPORT` |

Bu yapı fiziksel donanımla sanal donanım arasında hoş bir soyutlama sağlar. Masaüstü ortamı çoğu zaman olayın gerçek fareden mi yoksa sanal aygıttan mı geldiğini umursamaz. Matematiksel olarak fare imlecinin göreli hareketini şöyle düşünebiliriz:

$$x_{yeni} = x_{eski} + \Delta x, \quad y_{yeni} = y_{eski} + \Delta y$$

Yani sanal fare `REL_X = 30`, `REL_Y = 10` gönderirse imleç mevcut konumdan sağa 30, aşağı 10 birim hareket eder.

Pratik tarafta Python için `evdev` kütüphanesi işleri oldukça kolaylaştırır. Önce kurulum yapalım:

```bash
sudo apt install python3-evdev
```

Ayrıca `/dev/uinput` erişimi gerekir. Çoğu sistemde root yetkisiyle çalıştırmak yeterlidir:

```bash
sudo python3 virtual_input.py
```

Aşağıdaki örnek hem sanal klavye hem de sanal fare özellikleri olan bir cihaz oluşturur. Önce A tuşuna basıp bırakır, ardından fareyi hareket ettirip sol tık gönderir.

```python
from evdev import UInput, ecodes as e
import time

capabilities = {
    e.EV_KEY: [
        e.KEY_A,
        e.KEY_ENTER,
        e.BTN_LEFT
    ],
    e.EV_REL: [
        e.REL_X,
        e.REL_Y
    ]
}

with UInput(capabilities, name='blog-virtual-keyboard-mouse') as ui:
    time.sleep(1)

    # A tuşuna bas ve bırak
    ui.write(e.EV_KEY, e.KEY_A, 1)
    ui.write(e.EV_SYN, e.SYN_REPORT, 0)
    time.sleep(0.1)
    ui.write(e.EV_KEY, e.KEY_A, 0)
    ui.write(e.EV_SYN, e.SYN_REPORT, 0)

    # Fareyi sağa ve aşağı hareket ettir
    ui.write(e.EV_REL, e.REL_X, 80)
    ui.write(e.EV_REL, e.REL_Y, 40)
    ui.write(e.EV_SYN, e.SYN_REPORT, 0)

    # Sol tık
    ui.write(e.EV_KEY, e.BTN_LEFT, 1)
    ui.write(e.EV_SYN, e.SYN_REPORT, 0)
    time.sleep(0.05)
    ui.write(e.EV_KEY, e.BTN_LEFT, 0)
    ui.write(e.EV_SYN, e.SYN_REPORT, 0)
```

Buradaki `capabilities` sözlüğü sanal cihazın hangi olayları üretebileceğini bildirir. Eğer `KEY_A` tanımlamazsanız sonradan A tuşu göndermeye çalışmak anlamlı olmaz; çünkü çekirdek bu aygıtın böyle bir yeteneği olduğunu bilmez.

| Yaklaşım | Avantaj | Dezavantaj |
|---|---|---|
| X11 araçları | Kolay kullanım | Wayland ve konsolda sınırlı |
| `/dev/uinput` | Çekirdek seviyesinde genel çözüm | Yetki ve aygıt tanımı gerekir |
| Donanım emülatörü | Çok gerçekçi | Ek cihaz veya firmware ister |

Güvenlik tarafı önemlidir. Sanal klavye oluşturabilen bir program parola alanına da yazı yazabilir. Bu yüzden `/dev/uinput` erişimi herkese verilmemelidir. Geliştirme ortamında root kullanmak pratik olsa da üretimde özel grup, udev kuralı ve minimum yetki prensibi tercih edilmelidir.

Sonuç olarak `/dev/uinput`, Linux’ta fiziksel donanım olmadan giriş simülasyonu yapmak için güçlü ve esnek bir kapıdır. Mantığı kavradığınızda olay tipleri, kodlar ve değerlerden oluşan küçük paketlerle sisteme “gerçekmiş gibi” davranan sanal aygıtlar tanımlayabilirsiniz. Bu da test otomasyonundan erişilebilirlik çözümlerine kadar oldukça geniş ve eğlenceli bir oyun alanı açar.
