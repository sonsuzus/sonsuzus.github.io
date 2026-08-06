---
layout: post
title: "Fonksiyonlar ve Modüler Kodlama: Kopyala-Yapıştır Döngüsünden Kurtulun"
math: true
categories: 
  - Bilgi
tags: 
  - fonksiyonlar
  - modüler programlama
  - temiz kod
---

Bir program büyüdükçe aynı işlemleri farklı yerlerde tekrar tekrar yazmak, başlangıçta masum görünen bir alışkanlıktan ciddi bir bakım sorununa dönüşür. Fonksiyonlar ve modüler kodlama, bu tekrarları anlamlı parçalara ayırarak kodu daha okunabilir, test edilebilir ve yeniden kullanılabilir hâle getirir. Kısacası amaç, bilgisayara yalnızca ne yapacağını söylemek değil, bunu düzenli ve sürdürülebilir bir biçimde söylemektir.
``
## Fonksiyon Nedir?

Fonksiyon, belirli bir görevi gerçekleştiren ve gerektiğinde çağrılabilen isimlendirilmiş kod bloğudur. Bir fonksiyon girdiler alabilir, bu girdileri işleyebilir ve sonuç döndürebilir. Matematikteki fonksiyon fikriyle programlamadaki kullanım oldukça benzerdir:

$$f(x) = x^2 + 2x + 1$$

Burada $x$ girdi, $f(x)$ ise çıktıdır. Programlamada aynı yapı şöyle ifade edilebilir:

```python
def hesapla(x):
    """x² + 2x + 1 işleminin sonucunu döndürür."""
    return x ** 2 + 2 * x + 1

sonuc = hesapla(4)
print(sonuc)  # 25
```

Bu örnekte `hesapla` fonksiyonu işlemin nasıl yapıldığını tek bir yerde saklar. Formül değişirse fonksiyonun kullanıldığı her satırı değil, yalnızca fonksiyon gövdesini güncellemek yeterlidir.

## Tekrar Neden Tehlikelidir?

Aynı kodun birden fazla yerde bulunması, hata düzeltmelerini zorlaştırır. Örneğin indirim hesaplayan formülü beş farklı noktaya kopyaladıysanız oran değiştiğinde beş yeri de bulmanız gerekir. Birini unutursanız program farklı sonuçlar üretmeye başlar.

Tekrarlı kod miktarını kabaca şöyle düşünebiliriz:

$$T = n \times m$$

Burada $n$ tekrar sayısını, $m$ ise işlemin satır sayısını temsil eder. İşlem 8 satırsa ve 6 kez tekrarlanıyorsa toplam $48$ satır yönetilir. Fonksiyon kullanıldığında mantık yalnızca 8 satırda tutulur; diğer yerlerde kısa fonksiyon çağrıları bulunur.

| Yaklaşım | Okunabilirlik | Değişiklik Maliyeti | Yeniden Kullanım | Hata Riski |
|---|---:|---:|---:|---:|
| Kopyala-yapıştır | Düşük | Yüksek | Düşük | Yüksek |
| Tek fonksiyon | Yüksek | Düşük | Yüksek | Düşük |
| Modüllere ayrılmış yapı | Çok yüksek | Düşük | Çok yüksek | Düşük |

## Parametreler ve Dönüş Değerleri

İyi tasarlanmış fonksiyonlar dışarıdan parametre alır ve sonucu `return` ile döndürür. Böylece belirli değerlere bağımlı kalmazlar.

```python
def indirimli_fiyat(fiyat, indirim_orani=0.10):
    """Fiyata belirtilen oranda indirim uygular."""
    if fiyat < 0:
        raise ValueError("Fiyat negatif olamaz.")

    indirim = fiyat * indirim_orani
    return fiyat - indirim

urunler = [250, 400, 750]
sonuclar = [indirimli_fiyat(urun, 0.20) for urun in urunler]
print(sonuclar)
```

Fonksiyon hem farklı ürünlerde kullanılabilir hem de varsayılan indirim oranı sayesinde esnekliğini korur. Değer doğrulamasının fonksiyon içinde yapılması, hatalı verilerin sisteme sessizce yayılmasını da önler.

## Modüler Kodlama Nedir?

Fonksiyonlar tek tek görevleri düzenlerken modüler kodlama, ilişkili fonksiyonları ayrı dosyalarda toplar. Örneğin bir e-ticaret uygulamasında fiyat işlemleri `fiyat.py`, kullanıcı işlemleri `kullanici.py`, veritabanı işlemleri ise `veritabani.py` modülünde tutulabilir.

```python
# fiyat.py
def vergi_ekle(fiyat, oran=0.20):
    return fiyat * (1 + oran)


def indirim_uygula(fiyat, oran):
    return fiyat * (1 - oran)
```

Başka bir dosyada bu modül şöyle kullanılır:

```python
from fiyat import vergi_ekle, indirim_uygula

ara_toplam = indirim_uygula(1000, 0.15)
toplam = vergi_ekle(ara_toplam)
print(toplam)
```

Bu ayrım, ana programın ayrıntılara boğulmasını engeller. Kod, uzun bir yapılacaklar listesi yerine anlamlı görevlerin orkestrasyonu gibi görünür.

## İyi Fonksiyon Yazmanın Altın Kuralları

- Her fonksiyon mümkünse **tek bir sorumluluğa** sahip olmalıdır.
- `islem1` yerine `siparis_toplamini_hesapla` gibi açıklayıcı isimler kullanılmalıdır.
- Gereksiz küresel değişkenlerden kaçınılmalıdır.
- Çok fazla parametre alan fonksiyonlar yeniden tasarlanmalıdır.
- Tekrarlanan mantık ortak bir fonksiyona taşınmalıdır.
- Fonksiyonlar küçük ve bağımsız testlerle doğrulanmalıdır.

Fonksiyonlara ayırmak yalnızca satır sayısını azaltmaz; programın düşünce yapısını görünür kılar. Kodunuzda sık sık kopyala-yapıştır yapıyorsanız küçük bir alarm çalmalıdır: Orada muhtemelen keşfedilmeyi bekleyen bir fonksiyon vardır!
