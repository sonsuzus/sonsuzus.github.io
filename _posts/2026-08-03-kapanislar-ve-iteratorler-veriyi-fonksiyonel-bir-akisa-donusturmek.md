---
layout: post
title: "Kapanışlar ve İteratörler: Veriyi Fonksiyonel Bir Akışa Dönüştürmek"
math: true
categories: 
  - Bilgi
tags: 
  - closures
  - iteratörler
  - fonksiyonel programlama
---

Kapanışlar (closures) ve iteratörler, veriyi “nasıl dolaşacağımızı” adım adım anlatmak yerine “hangi dönüşümleri istediğimizi” ifade etmemizi sağlar. Kapanışlar çevrelerindeki değişkenleri hatırlayan isimsiz fonksiyonlardır; iteratörler ise koleksiyon elemanlarını sırayla üreten soyutlamalardır. Birlikte kullanıldıklarında kısa, okunabilir ve yeniden kullanılabilir veri işleme zincirleri ortaya çıkar.

``

## Kapanış neden sıradan bir fonksiyondan farklıdır?

Normal bir fonksiyon çoğunlukla yalnızca parametrelerine ve erişebildiği genel değerlere bağlıdır. Kapanış ise tanımlandığı kapsamın değişkenlerini **yakalayabilir**. Matematiksel açıdan sıradan bir fonksiyonu

$$f(x)=x^2$$

şeklinde düşünürsek, dışarıdaki $a$ değerini yakalayan kapanış şu aileyi temsil eder:

$$f_a(x)=ax^2$$

Burada $a$, açıkça parametre olarak verilmemesine rağmen hesaplamanın parçasıdır. Kapanışın yanında taşıdığı bu çevresel bilgilere bazen **closure environment** denir.

| Özellik | Normal fonksiyon | Kapanış |
|---|---|---|
| İsme ihtiyaç duyar mı? | Genellikle evet | Hayır |
| Dış değişken yakalar mı? | Genellikle hayır | Evet |
| Kısa işlemlerde kullanım | Daha törensel | Oldukça pratik |
| Durum taşıyabilir mi? | Ek yapı gerekir | Yakalanan değerlerle taşıyabilir |

Rust’ta bir kapanış çevresindeki değeri referansla ödünç alabilir, değiştirilebilir biçimde ödünç alabilir veya sahipliğini üstlenebilir. Derleyici buna göre kapanışı `Fn`, `FnMut` ya da `FnOnce` davranışlarından biriyle ilişkilendirir.

```rust
fn main() {
    let katsayi = 3;
    let carp = |sayi: i32| sayi * katsayi;

    println!("{}", carp(5)); // 15
}
```

Buradaki `carp`, `katsayi` değişkenini çevresinden yakalar. Böylece her çağrıda katsayıyı ayrıca göndermemiz gerekmez.

## İteratör: Koleksiyon değil, üretim süreci

İteratör bir koleksiyonun kendisi değildir; sıradaki elemanın nasıl elde edileceğini tanımlayan bir mekanizmadır. Temel fikir, her adımda ya yeni bir değer ya da akışın bittiğini bildiren sonuç üretmektir.

$n$ elemanlı bir koleksiyon tek kez dolaşılıyorsa zaman karmaşıklığı çoğunlukla

$$T(n)=O(n)$$

olur. `map`, `filter` ve `take` gibi işlemlerin zincirlenmesi mutlaka her aşamada yeni bir koleksiyon oluşturmaz. Birçok dilde, özellikle Rust’ta, iteratörler **tembeldir**: Sonuç tüketilene kadar hesaplama başlamaz.

| İşlem | Görevi | Sonuç türü |
|---|---|---|
| `map` | Her elemanı dönüştürür | Yeni iteratör |
| `filter` | Koşula uyanları geçirir | Yeni iteratör |
| `take` | İlk belirli sayıda değeri alır | Sınırlı iteratör |
| `fold` | Değerleri tek sonuçta birleştirir | Tek değer |
| `collect` | Akışı koleksiyona dönüştürür | Koleksiyon |

## İkisini birlikte kullanalım

Aşağıdaki örnek çift sayıları seçer, dışarıdan yakalanan katsayıyla çarpar ve sonuçları toplar:

```rust
fn main() {
    let sayilar = vec![1, 2, 3, 4, 5, 6];
    let katsayi = 10;

    let toplam: i32 = sayilar
        .iter()
        .filter(|sayi| *sayi % 2 == 0)
        .map(|sayi| sayi * katsayi)
        .sum();

    println!("Toplam: {}", toplam); // 120
}
```

`filter` içindeki kapanış yalnızca çift değerleri geçirir. `map` kapanışı ise `katsayi` değişkenini yakalayarak değerleri dönüştürür. `sum`, tembel zinciri tüketen **terminal işlem** olduğu için gerçek hesaplama bu noktada gerçekleşir.

Aynı yaklaşım klasik bir döngüyle de yazılabilir; ancak iteratör zinciri “indeksi artır, elemana eriş, sonucu geçici değişkende tut” ayrıntılarını gizler. Böylece kod, mekanizmadan çok niyeti anlatır.

## Ne zaman dikkatli olmalıyız?

Uzun ve iç içe kapanış zincirleri okunabilirliği azaltabilir. Yan etkiler, karmaşık hata yönetimi veya çok sayıda koşul varsa işlemleri isimlendirilmiş fonksiyonlara ayırmak daha sağlıklıdır. Ayrıca sahiplik kullanan dillerde `move` ile yakalanan bir değerin artık önceki kapsamda kullanılamayabileceği unutulmamalıdır.

Özetle kapanışlar davranışı veri gibi taşır, iteratörler ise veriyi kontrollü bir akışa dönüştürür. Birlikte kullanıldıklarında döngü yazmaktan fazlasını yaparız: Dönüşümleri birbirine bağlayan küçük ve güçlü bir işlem hattı kurarız.
