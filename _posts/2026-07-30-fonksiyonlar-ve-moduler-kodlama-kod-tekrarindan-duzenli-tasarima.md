---
layout: post
title: "Fonksiyonlar ve Modüler Kodlama: Kod Tekrarından Düzenli Tasarıma"
math: true
categories: 
  - Bilgi
tags: 
  - fonksiyonlar
  - modüler programlama
  - temiz kod
---

Bir program büyüdükçe aynı işlemleri yapan kod satırları farklı yerlerde tekrar belirmeye başlar. Başlangıçta masum görünen bu kopyalar, değişiklik zamanı geldiğinde küçük birer baş ağrısı fabrikasına dönüşür. Fonksiyonlar, belirli bir görevi yerine getiren kod bloklarını isimlendirip ihtiyaç duyduğumuzda çağırmamızı sağlar. Böylece program, devasa bir komut yığını yerine anlaşılır ve yeniden kullanılabilir parçalardan oluşur.

``

## Fonksiyon Nedir?

Fonksiyon; girdi alabilen, bir işlem gerçekleştiren ve gerektiğinde çıktı üreten alt programdır. Matematikteki fonksiyon kavramıyla benzer şekilde düşünülebilir:

$$f(x) = 2x + 3$$

Burada $x$ fonksiyonun girdisi, $2x+3$ işlemi fonksiyonun davranışı, elde edilen değer ise çıktıdır. Programlamada aynı fikir şu biçimde ifade edilebilir:

```python
def hesapla(x):
    return 2 * x + 3

sonuc = hesapla(5)
print(sonuc)  # 13
```

`hesapla` fonksiyonu işlemin nasıl yapıldığını tek bir yerde tanımlar. Programın diğer bölümleri ayrıntılarla uğraşmadan yalnızca fonksiyonun adını kullanır. Bu yaklaşım **soyutlama** olarak adlandırılır.

## Parametre ve Argüman Arasındaki Fark

Bu iki kavram sıklıkla birbirinin yerine kullanılsa da teknik olarak farklıdır:

| Kavram | Nerede bulunur? | Örnek |
|---|---|---|
| Parametre | Fonksiyon tanımında | `def topla(a, b)` içindeki `a` ve `b` |
| Argüman | Fonksiyon çağrısında | `topla(4, 7)` içindeki `4` ve `7` |
| Dönüş değeri | Fonksiyonun ürettiği sonuçta | `return a + b` |

Parametreler birer boş kutu, argümanlar ise çağrı sırasında bu kutulara yerleştirilen değerler gibi düşünülebilir.

```python
def indirimli_fiyat(fiyat, indirim_orani=10):
    indirim = fiyat * indirim_orani / 100
    return fiyat - indirim

standart = indirimli_fiyat(500)
ozel = indirimli_fiyat(500, 25)
```

Bu örnekte `indirim_orani` varsayılan bir parametredir. İlk çağrı yüzde 10, ikinci çağrı yüzde 25 indirim uygular. Tek fonksiyon, farklı argümanlarla farklı durumlara uyarlanmıştır.

## Modülerlik Neden Önemlidir?

Modüler kodlama, büyük bir problemi küçük ve bağımsız görevlere ayırma yaklaşımıdır. Bir e-ticaret uygulamasında fiyat hesaplama, vergi ekleme, stok kontrolü ve bildirim gönderme ayrı fonksiyonlar olabilir.

| Tekrarlı yaklaşım | Modüler yaklaşım |
|---|---|
| Aynı kod birçok yerde kopyalanır | İşlem bir kez tanımlanır |
| Değişiklikler risklidir | Güncelleme tek noktadan yapılır |
| Test etmek zordur | Her parça ayrı test edilir |
| Okunabilirlik düşüktür | Fonksiyon adları amacı açıklar |

Örneğin toplam tutar matematiksel olarak

$$T = \sum_{i=1}^{n} f_i \times a_i$$

şeklinde ifade edilebilir. Burada $f_i$ ürün fiyatını, $a_i$ ise ürün adedini temsil eder:

```python
def sepet_toplami(urunler):
    """Fiyat ve adet bilgilerini kullanarak toplam tutarı hesaplar."""
    toplam = 0
    for urun in urunler:
        toplam += urun["fiyat"] * urun["adet"]
    return toplam

sepet = [
    {"fiyat": 120, "adet": 2},
    {"fiyat": 75, "adet": 3}
]

print(sepet_toplami(sepet))  # 465
```

Fonksiyon yalnızca toplam hesaplama sorumluluğunu üstlenir. Ekrana yazdırma, veritabanına kaydetme veya ödeme alma gibi işler başka modüllere bırakılmalıdır. Bu ilkeye **tek sorumluluk ilkesi** denir.

## Daha Sağlam Fonksiyonlar Yazmak

İyi bir fonksiyon kısa, anlamlı isimli ve tahmin edilebilir olmalıdır. `islem()` yerine `vergi_hesapla()` gibi niyeti açıklayan adlar seçilmelidir. Fonksiyon mümkünse dışarıdaki değişkenleri değiştirmemeli; girdiden çıktı üretmelidir. Böyle fonksiyonlara saf fonksiyon denir ve test edilmeleri çok daha kolaydır.

Kısacası fonksiyonlar yalnızca satır sayısını azaltmaz; kodun düşünce yapısını düzenler. Tekrar eden bir blok gördüğünüzde kendinize şu soruyu sorun: “Bu davranışın bir adı olsaydı ne olurdu?” Cevap büyük ihtimalle yeni fonksiyonunuzun adıdır.
