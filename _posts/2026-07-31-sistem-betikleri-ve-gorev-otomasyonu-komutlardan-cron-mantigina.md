---
layout: post
title: "Sistem Betikleri ve Görev Otomasyonu: Komutlardan Cron Mantığına"
math: true
categories: 
  - Program
tags: 
  - Python
  - Cron
  - Otomasyon
---

Bir geliştiricinin aynı komutu her sabah elle çalıştırması, kahve makinesinin başında suyun kaynamasını izlemek kadar gereksizdir. Sistem betikleri; dosya yedekleme, günlük temizleme, servis denetleme ve rapor üretme gibi işleri kodla yönetmemizi sağlar. Bu işleri belirli aralıklarla kendiliğinden çalıştırdığımızda ise küçük ama yorulmayan bir dijital asistana sahip oluruz.
``
## İşletim sistemi komutu çalıştırmanın mantığı

Bir terminale `ls`, `ipconfig` veya `mkdir` yazdığımızda kabuk, komutu yorumlayarak işletim sisteminden ilgili programı başlatmasını ister. Kod içerisinden komut çalıştırırken de benzer bir süreç gerçekleşir:

1. Ana program bir alt süreç oluşturur.
2. İşletim sistemi komutu ayrı bir süreçte yürütür.
3. Standart çıktı, hata çıktısı ve dönüş kodu ana programa iletilir.

Komutun başarılı olup olmadığını anlamak için **çıkış kodu** kullanılır. Genel kabul şöyledir: $E = 0$ başarıyı, $E \neq 0$ ise hata veya olağan dışı durumu temsil eder.

Python'da bunun için `subprocess` modülü tercih edilir:

```python
import subprocess

komut = ["ping", "-c", "2", "example.com"]

try:
    sonuc = subprocess.run(
        komut,
        capture_output=True,
        text=True,
        timeout=10,
        check=True
    )
    print("Komut başarılı:")
    print(sonuc.stdout)
except subprocess.TimeoutExpired:
    print("Komut zaman aşımına uğradı.")
except subprocess.CalledProcessError as hata:
    print("Çıkış kodu:", hata.returncode)
    print("Hata mesajı:", hata.stderr)
```

Bu kod, hedef sunucuya iki ping gönderir; çıktıyı yakalar, on saniyelik sınır uygular ve başarısız dönüş kodunu istisnaya dönüştürür. Windows kullanılıyorsa parametreler `ping -n 2 example.com` biçiminde değiştirilmelidir.

## `shell=True` neden dikkat ister?

Kullanıcıdan gelen metni doğrudan kabuğa göndermek komut enjeksiyonuna yol açabilir. Örneğin dosya adına eklenen `; rm -rf ...` benzeri bir ifade ikinci bir komut olarak yorumlanabilir. Bu nedenle komutları liste halinde vermek ve varsayılan `shell=False` davranışını korumak daha güvenlidir.

| Yaklaşım | Avantaj | Risk veya sınırlama |
|---|---|---|
| `subprocess.run([...])` | Güvenli ve kontrol edilebilir | Kabuk özellikleri doğrudan kullanılamaz |
| `shell=True` | Boru ve yönlendirme işlemleri kolaydır | Enjeksiyon riski oluşturur |
| Python kütüphaneleri | Platformlar arası çalışabilir | Her sistem işlemini kapsamayabilir |

Örneğin dosya silmek için `rm` çağırmak yerine `pathlib.Path.unlink()` kullanmak çoğu zaman daha taşınabilir ve güvenlidir.

## Cron mantığı ve periyodik çalışma

Periyodik görevlerde temel fikir, mevcut zamanın belirlenen kuralla eşleşip eşleşmediğini denetlemektir. Bir görev her $T$ dakikada çalışıyorsa, yaklaşık çalışma sayısı $N = \frac{D}{T}$ ile hesaplanabilir. Burada $D$, toplam dakika sayısıdır. Örneğin bir günde her 15 dakikada çalışan görev $1440 / 15 = 96$ kez tetiklenir.

Linux cron ifadesi beş zaman alanından oluşur:

```text
* * * * *
│ │ │ │ └── Haftanın günü
│ │ │ └──── Ay
│ │ └────── Ayın günü
│ └──────── Saat
└────────── Dakika
```

Her gece 02.30'da yedek alan bir betik şöyle planlanabilir:

```cron
30 2 * * * /usr/bin/python3 /opt/scripts/yedekle.py >> /var/log/yedekle.log 2>&1
```

Buradaki yönlendirme, normal ve hata çıktılarını günlük dosyasına ekler. Betiğin elle çalışırken başarılı olması cron altında da başarılı olacağı anlamına gelmez; cron daha sınırlı bir ortam değişkeni ve `PATH` değeriyle çalışabilir. Bu yüzden mutlak dosya yolları kullanılmalıdır.

| Araç | Uygun kullanım | Öne çıkan özellik |
|---|---|---|
| Cron | Basit Linux görevleri | Hafif ve yerleşik |
| systemd timer | Servis odaklı Linux işleri | Günlükleme ve bağımlılık yönetimi |
| Windows Task Scheduler | Windows otomasyonu | Grafik arayüz ve tetikleyiciler |
| APScheduler | Uygulama içi Python görevleri | Dinamik zamanlama |

## Sağlam bir otomasyonun kontrol listesi

İyi bir görev tekrar çalıştırıldığında veriyi bozmamalı, yani mümkün olduğunca **idempotent** olmalıdır. Hataları dosyaya veya merkezi günlük sistemine yazmalı, çalışma süresini sınırlamalı ve gizli bilgileri kaynak koda gömmemelidir. Aynı görevin iki kopyasının eşzamanlı başlamasını önlemek için kilit dosyası da kullanılabilir.

Kısacası başarılı otomasyon yalnızca “komutu zamanında çalıştırmak” değildir. Güvenli süreç yönetimi, doğru zamanlama, gözlemlenebilir günlükler ve hata sonrası toparlanma birlikte tasarlandığında betikler gerçekten güvenilir birer sistem çalışanına dönüşür.
