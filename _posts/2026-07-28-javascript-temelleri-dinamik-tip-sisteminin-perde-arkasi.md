---
layout: post
title: "JavaScript Temelleri: Dinamik Tip Sisteminin Perde Arkası"
math: true
categories: 
  - Bilgi
tags: 
  - JavaScript
  - dinamik tipleme
  - programlama temelleri
---

JavaScript’e C veya C++ dünyasından gelenlerin ilk şaşkınlığı genellikle şudur: Bir değişken nasıl olur da önce sayı, birkaç satır sonra metin olabilir? Bunun nedeni JavaScript’in **dinamik tipli** bir dil olmasıdır. Tür bilgisi değişken adına değil, çalışma zamanındaki değere bağlıdır. Bu esneklik hızlı geliştirme sağlarken bazı sürprizleri de beraberinde getirir.
``
## Statik ve dinamik tipleme nedir?

C++ gibi statik tipli dillerde değişkenin türü derleme aşamasında belirlenir. Örneğin `int` olarak tanımlanmış bir değişkene metin atamak derleme hatası üretir. JavaScript’te ise değişkenler belirli türlerde değerleri saklayan sabit kutular değil, farklı değerlere yöneltilebilen etiketler gibidir.

Teorik olarak bir değişkeni zamana bağlı bir eşleme şeklinde düşünebiliriz:

$$V(t) \rightarrow (değer, tür)$$

Burada $t$ çalışma zamanındaki anı temsil eder. JavaScript motoru, işlemi gerçekleştirirken değerin güncel türünü inceler.

| Özellik | Statik tip sistemi | Dinamik tip sistemi |
|---|---|---|
| Tür kontrolü | Genellikle derleme zamanında | Çalışma zamanında |
| Değişkenin türü | Önceden belirlenir | Tutulan değere göre değişir |
| Hata yakalama | Daha erken | Program çalışırken olabilir |
| Esneklik | Daha sınırlı | Daha yüksek |
| Tipik örnekler | C, C++, Rust | JavaScript, Python, Ruby |

## Değişken değil, değer tür taşır

Aşağıdaki kodda `veri` değişkeninin kendisine kalıcı bir tür verilmez:

```js
let veri = 42;
console.log(typeof veri); // number

veri = "Merhaba";
console.log(typeof veri); // string

veri = true;
console.log(typeof veri); // boolean
```

Kod geçerlidir çünkü `let`, yeniden atamaya izin verir. `const` ise türü sabitlemez; yalnızca değişkenin başka bir değere yeniden bağlanmasını engeller. Örneğin `const liste = []` ile oluşturulan dizinin içeriği değiştirilebilir.

JavaScript’in temel değer türleri `string`, `number`, `bigint`, `boolean`, `undefined`, `symbol` ve `null` olarak sıralanır. Nesneler, diziler ve fonksiyonlar ise referans davranışı gösteren yapılardır. İlginç bir tarihsel ayrıntı olarak `typeof null` sonucu `"object"` döner. Bu, dilin ilk sürümlerinden kalan ve uyumluluk nedeniyle düzeltilemeyen ünlü bir tuzaktır.

## Tip dönüşümü ve zorlaması

JavaScript bazı işlemlerde türleri otomatik olarak dönüştürür. Buna **type coercion**, yani tip zorlama denir:

```js
console.log("5" + 2); // "52"
console.log("5" - 2); // 3
console.log(Number("5") + 2); // 7
```

İlk işlemde `+` operatörü metin birleştirmeyi seçer. İkinci işlemde `-` yalnızca sayısal anlam taşıdığı için `"5"` sayıya çevrilir. Genel fikir, işlemin uygulanabilmesi için değerlerin ortak bir alana dönüştürülmesidir:

$$op(a, b) = op(convert(a), convert(b))$$

Ancak dönüşüm kuralları her operatörde aynı değildir. Bu nedenle örtük dönüşüme güvenmek yerine `Number()`, `String()` ve `Boolean()` gibi açık dönüşümler kullanmak kodun niyetini anlaşılır kılar.

## Eşitlik: `==` mı, `===` mi?

| Operatör | Tür dönüşümü | Örnek |
|---|---|---|
| `==` | Uygulayabilir | `5 == "5"` → `true` |
| `===` | Uygulamaz | `5 === "5"` → `false` |

Sıkı eşitlik operatörü `===`, hem türü hem değeri karşılaştırır. Beklenmeyen dönüşümleri azaltmak için modern JavaScript kodunda genellikle `===` ve `!==` tercih edilir.

## Dinamik yapı kontrolsüzlük değildir

Dinamik tipleme, kuralların bulunmadığı anlamına gelmez; kontrollerin farklı bir zamanda yapıldığı anlamına gelir. Güvenilir kod için girişleri doğrulamak, `typeof`, `Array.isArray()` ve null kontrollerini kullanmak önemlidir. Daha büyük projelerde TypeScript, JavaScript’in üzerine statik analiz katmanı ekleyerek hataları çalıştırmadan önce gösterebilir.

Sonuç olarak JavaScript’in tip sistemi bir sihirbaz değil, çalışma zamanında karar veren hızlı bir hakemdir. Kurallarını öğrendiğinizde esneklik avantaja dönüşür; öğrenmediğinizde ise `"5" + 2` size küçük ama unutulmaz bir şaka yapabilir.
