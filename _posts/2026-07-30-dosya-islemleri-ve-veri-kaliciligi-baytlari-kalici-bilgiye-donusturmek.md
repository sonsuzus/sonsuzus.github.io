---
layout: post
title: "Dosya İşlemleri ve Veri Kalıcılığı: Baytları Kalıcı Bilgiye Dönüştürmek"
math: true
categories: 
  - Bilgi
tags: 
  - dosya işlemleri
  - veri kalıcılığı
  - python
---

Bir program çalışırken üretilen değişkenler çoğunlukla RAM üzerinde yaşar; program kapanınca da küçük bir vedalaşma töreni bile yapmadan kaybolur. Dosya işlemleri, dışarıdaki ham veriyi belleğe almayı ve işlenmiş sonuçları kalıcı depolamaya yazmayı sağlar. Böylece uygulamamız yalnızca “anı yaşayan” bir süreç olmaktan çıkar, geçmişini hatırlayan bir sisteme dönüşür.
``
## Bellek ve kalıcı depolama arasındaki fark

Bellek hızlı fakat geçicidir. SSD, sabit disk veya ağ üzerindeki depolama ise daha yavaş olmasına rağmen veriyi program sona erdikten sonra da korur. Dosya I/O, yani **Input/Output**, bu iki dünya arasındaki köprüdür.

| Özellik | RAM | Dosya sistemi |
|---|---|---|
| Hız | Çok yüksek | Görece düşük |
| Kalıcılık | Program kapanınca veri kaybolur | Veri açıkça silinene kadar korunur |
| Kullanım amacı | Aktif hesaplamalar | Kayıtlar, raporlar ve yapılandırmalar |
| Erişim biçimi | Değişkenler ve adresler | Dosya yolları ve akışlar |

Bir metin dosyasını okumak kavramsal olarak üç adımdan oluşur: dosyayı açmak, içeriği almak ve kaynağı kapatmak. Modern dillerde kaynak yönetimi yapıları, kapatma işlemini otomatikleştirir. Bu önemlidir; çünkü açık bırakılan dosyalar işletim sistemi kaynaklarını tüketebilir veya verinin diske tam yazılmasını engelleyebilir.

## Metni belleğe okumak

Python’da `with` bloğu, işlem başarıyla tamamlansa da hata oluşsa da dosyanın kapatılmasını sağlar:

```python
from pathlib import Path

kaynak = Path("ham_veri.txt")

with kaynak.open("r", encoding="utf-8") as dosya:
    metin = dosya.read()

satirlar = [satir.strip() for satir in metin.splitlines() if satir.strip()]
print(f"İşlenecek {len(satirlar)} satır bulundu.")
```

Burada `read()` içeriğin tamamını belleğe yükler. Küçük ve orta büyüklükteki belgelerde kullanışlıdır; ancak devasa bir günlük dosyasında RAM’i zorlayabilir. Yaklaşık bellek gereksinimini $M ≈ N + O$ şeklinde düşünebiliriz. Burada $N$ dosyanın boyutu, $O$ ise karakter nesneleri ve veri yapılarının ek yüküdür.

Büyük dosyalarda satır satır okuma daha güvenlidir:

```python
with open("ham_veri.txt", "r", encoding="utf-8") as dosya:
    for satir_no, satir in enumerate(dosya, start=1):
        temiz = satir.strip()
        if temiz:
            print(satir_no, temiz.lower())
```

Bu yaklaşımda bellek tüketimi yaklaşık olarak $M ≈ L$ olur; $L$, aynı anda işlenen satırın boyutudur. Dosya yüzlerce megabayt olsa bile program bütün içeriği tek seferde taşımak zorunda kalmaz.

## İşlenmiş veriyi kalıcılaştırmak

Okunan metin temizlenebilir, dönüştürülebilir veya analiz edilebilir. Sonuç yalnızca ekrana yazdırılırsa program kapandığında pratik değerini kaybedebilir. Çıktıyı belgeye yazmak için `w` ve `a` kipleri kullanılabilir.

| Kip | Davranış | Uygun kullanım |
|---|---|---|
| `r` | Dosyayı okur | Ham veriyi almak |
| `w` | İçeriği sıfırlayıp yeniden yazar | Güncel rapor üretmek |
| `a` | Dosyanın sonuna ekler | Günlük ve işlem geçmişi tutmak |
| `x` | Yalnızca yeni dosya oluşturur | Yanlışlıkla ezmeyi önlemek |

```python
sonuclar = [satir.upper() for satir in satirlar]

with open("rapor.txt", "w", encoding="utf-8") as dosya:
    dosya.write("İŞLENMİŞ VERİLER\n")
    dosya.write("-" * 20 + "\n")
    dosya.writelines(f"{deger}\n" for deger in sonuclar)
```

`w` kipi mevcut içeriği siler. Bu nedenle değerli bir dosyanın üzerine yazmadan önce hedef yol doğrulanmalı veya yedek oluşturulmalıdır. Ayrıca `encoding="utf-8"` belirtmek, Türkçe karakterlerin farklı sistemlerde anlamsız sembollere dönüşmesini önler.

## Güvenli ve dayanıklı I/O

Dosya bulunamayabilir, erişim izni reddedilebilir ya da disk dolabilir. Sağlam bir program bu durumları yakalamalıdır:

```python
try:
    with open("rapor.txt", "a", encoding="utf-8") as dosya:
        dosya.write("İşlem başarıyla tamamlandı.\n")
except OSError as hata:
    print(f"Dosya işlemi başarısız: {hata}")
```

Daha kritik uygulamalarda sonuç önce geçici bir dosyaya yazılır, ardından hedef dosyanın yerine atomik olarak taşınır. Böylece işlem yarıda kesilirse eski sağlam belge korunur. Kısacası iyi dosya yönetimi; doğru kip, uygun kodlama, kontrollü bellek kullanımı ve hata yönetiminin birleşimidir. Veri kalıcılığı tesadüf değil, bilinçli bir tasarım kararıdır.
