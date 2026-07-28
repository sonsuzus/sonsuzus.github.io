---
layout: post
title: "JavaScript Dizileri ve Yüksek Mertebe Metotlarla Veriyi Dönüştürme"
math: true
categories: 
  - Bilgi
tags: 
  - JavaScript
  - Diziler
  - Fonksiyonel Programlama
---

Bir alışveriş sepetindeki ürünlerden sınav notlarına kadar pek çok veri, yazılım dünyasında listeler hâlinde karşımıza çıkar. JavaScript dizileri bu verileri tek bir değişkende düzenli biçimde saklarken `map`, `filter` ve `reduce` gibi yüksek mertebe metotlar, döngü karmaşasına kapılmadan verileri dönüştürmemizi sağlar.
``
## Dizi nedir?

Dizi, birden fazla değeri sıralı biçimde saklayan veri yapısıdır. JavaScript'te köşeli parantezlerle oluşturulur ve her elemanın sıfırdan başlayan bir indeksi vardır.

```javascript
const diller = ["JavaScript", "Python", "Go"];

console.log(diller[0]); // JavaScript
console.log(diller.length); // 3
```

Bir dizide $n$ eleman varsa geçerli indeksler $0$ ile $n-1$ arasındadır. Örneğin üç elemanlı bir dizinin son elemanı `diller[2]` olur. Son elemana daha okunaklı biçimde `diller.at(-1)` kullanılarak da erişilebilir.

Diziler yalnızca metin değil; sayı, nesne ve hatta başka diziler barındırabilir. Yine de uygulamada aynı amaca hizmet eden verileri bir arada tutmak kodun anlaşılmasını kolaylaştırır.

## Yüksek mertebe metot nedir?

Yüksek mertebe fonksiyon, başka bir fonksiyonu parametre olarak alabilen veya sonuç olarak fonksiyon döndürebilen fonksiyondur. Dizi metotları, her eleman için çalıştırılacak bir geri çağırma fonksiyonu alır.

| Metot | Temel amaç | Sonuç |
|---|---|---|
| `map` | Her elemanı dönüştürmek | Aynı uzunlukta yeni dizi |
| `filter` | Koşula uyanları seçmek | Yeni ve çoğunlukla daha kısa dizi |
| `reduce` | Elemanları tek sonuçta birleştirmek | Sayı, nesne, dizi veya başka bir değer |
| `forEach` | Her eleman için işlem yapmak | `undefined` |

Bu metotlar kaynak diziyi doğrudan değiştirmez. Böylece beklenmedik yan etkiler azalır ve veri akışı daha kolay takip edilir.

## `map`: Her elemanı dönüştür

`map`, dizideki her elemanı verilen fonksiyondan geçirir. Matematiksel olarak bir $f$ fonksiyonunun tüm elemanlara uygulanması gibi düşünülebilir:

$$[x_1,x_2,\ldots,x_n] \rightarrow [f(x_1),f(x_2),\ldots,f(x_n)]$$

```javascript
const fiyatlar = [100, 250, 80];
const kdvliFiyatlar = fiyatlar.map((fiyat) => fiyat * 1.20);

console.log(kdvliFiyatlar); // [120, 300, 96]
```

Burada her fiyat yüzde 20 KDV eklenerek dönüştürülür. Orijinal `fiyatlar` dizisi değişmez.

## `filter`: İstenmeyenleri ele

`filter`, geri çağırma fonksiyonu `true` döndüren elemanları yeni diziye taşır. Bir sınıftaki başarılı notları seçelim:

```javascript
const notlar = [45, 82, 67, 30, 91];
const basariliNotlar = notlar.filter((not) => not >= 50);

console.log(basariliNotlar); // [82, 67, 91]
```

Koşul bir süzgeç gibi çalışır. En kötü durumda bütün elemanlar incelendiği için zaman karmaşıklığı $O(n)$ olur.

## `reduce`: Diziyi tek sonuca indir

`reduce`, biriktirici ve mevcut eleman üzerinden ilerler. İkinci argüman başlangıç değeridir; verilmesi, özellikle boş dizilerde hata riskini azaltır.

```javascript
const sepet = [
  { ad: "Klavye", fiyat: 900 },
  { ad: "Fare", fiyat: 500 },
  { ad: "Kulaklık", fiyat: 1200 }
];

const toplam = sepet.reduce(
  (biriken, urun) => biriken + urun.fiyat,
  0
);

console.log(toplam); // 2600
```

Toplam, matematiksel olarak $\sum_{i=1}^{n} fiyat_i$ işlemidir. Biriktirici başlangıçta `0` değerini alır ve her ürünün fiyatıyla güncellenir.

## Metotları zincirlemek

Asıl eğlence metotlar birleştiğinde başlar. Önce pahalı ürünleri seçip sonra adlarını dönüştürebiliriz:

```javascript
const pahaliUrunAdlari = sepet
  .filter((urun) => urun.fiyat >= 800)
  .map((urun) => urun.ad.toUpperCase());

console.log(pahaliUrunAdlari); // ["KLAVYE", "KULAKLIK"]
```

Her zincir halkası yeni bir sonuç üretir. Ancak her metot diziyi ayrı dolaştığından devasa veri kümelerinde gereksiz zincirler maliyet yaratabilir. Günlük uygulamalarda ise okunabilirlik kazancı çoğunlukla daha değerlidir.

Kısacası `map` dönüştürür, `filter` seçer, `reduce` biriktirir. Hangi metodu kullanacağınıza karar verirken “Yeni bir liste mi, seçilmiş elemanlar mı, yoksa tek bir sonuç mu istiyorum?” sorusunu sormanız yeterlidir.
