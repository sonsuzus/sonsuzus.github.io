---
layout: post
title: "JavaScript Veri Tipleri, Bellek ve Otomatik Tip Dönüşümleri"
math: true
categories: 
  - Bilgi
tags: 
  - JavaScript
  - Veri Tipleri
  - Type Coercion
---

JavaScript’te `"5" + 2` işleminin `"52"`, `"5" - 2` işleminin ise `3` üretmesi ilk bakışta motorun zar attığını düşündürebilir. Oysa bu davranışların arkasında belirli dönüşüm kuralları bulunur. İlkel ve referans tiplerinin bellekte nasıl temsil edildiğini, değerlerin nasıl kopyalandığını ve otomatik tip dönüşümünün hangi adımlarla gerçekleştiğini anlamak; şaşırtıcı hataları önlemenin en etkili yollarından biridir.

``

## İlkel ve referans tipleri

JavaScript’in ilkel veri tipleri `string`, `number`, `bigint`, `boolean`, `undefined`, `symbol` ve `null` değerleridir. Bunlar değiştirilemez, yani **immutable** değerlerdir. Örneğin bir metni büyük harfe çevirdiğimizde mevcut metin değişmez; yeni bir değer oluşturulur.

Nesneler, diziler ve fonksiyonlar ise referans tipleri olarak anılır. Teknik olarak JavaScript standardı “stack” ve “heap” kullanımını zorunlu kılmaz; bu ayrıntı motora bağlıdır. Bununla birlikte zihinsel model olarak ilkel değerlerin doğrudan, nesnelerin ise bellekteki bir nesneye erişim sağlayan referans üzerinden işlendiğini düşünebiliriz.

| Özellik | İlkel değer | Referans değer |
|---|---|---|
| Örnek | `42`, `true`, `"merhaba"` | `{}`, `[]`, `function(){}` |
| Değiştirilebilirlik | Immutable | İçeriği değiştirilebilir |
| Atama sonucu | Değer kopyalanır | Referans kopyalanır |
| Karşılaştırma | Değere göre | Nesne kimliğine göre |

```js
let puanA = 10;
let puanB = puanA;
puanB = 20;

console.log(puanA); // 10

const kullaniciA = { ad: "Ada" };
const kullaniciB = kullaniciA;
kullaniciB.ad = "Ece";

console.log(kullaniciA.ad); // "Ece"
```

İlk bölümde `puanB`, sayısal değerin bağımsız bir kopyasını alır. İkinci bölümde iki değişken aynı nesneye erişir. Kabaca $A \rightarrow O$ ve $B \rightarrow O$ şeklinde gösterebileceğimiz bu durumda nesne `O` üzerinde yapılan değişiklik her iki değişkenden de görülebilir.

## Coercion nasıl çalışır?

**Type coercion**, bir değerin işlem sırasında başka bir tipe otomatik dönüştürülmesidir. JavaScript motoru operatörün beklentisine göre `ToPrimitive`, `ToString`, `ToNumber` ve `ToBoolean` gibi soyut işlemler uygular.

`+` operatörü özel davranır: Operandlardan biri primitive dönüşümden sonra metinse birleştirme yapar. `-`, `*` ve `/` ise değerleri genellikle sayıya dönüştürür.

| İfade | Sonuç | Temel neden |
|---|---:|---|
| `"5" + 2` | `"52"` | Sayı metne dönüşür |
| `"5" - 2` | `3` | Metin sayıya dönüşür |
| `true + 1` | `2` | $ToNumber(true)=1$ |
| `null + 1` | `1` | $ToNumber(null)=0$ |
| `undefined + 1` | `NaN` | Sayısal dönüşüm başarısızdır |

```js
console.log("10" + 5);       // "105"
console.log("10" * 2);       // 20
console.log(Number("10"));   // 10
console.log(String(false));   // "false"
console.log(Boolean([]));     // true
```

Son üç satır **açık dönüşüm** yapar. Niyet görünür olduğu için üretim kodunda otomatik dönüşüme güvenmek yerine `Number`, `String` ve `Boolean` kullanmak çoğunlukla daha güvenlidir.

## Truthy ve falsy değerler

Koşullarda değerler boolean tipe dönüştürülür. `false`, `0`, `-0`, `0n`, `""`, `null`, `undefined` ve `NaN` falsy’dir; diğer değerler truthy kabul edilir. Boş dizi ve boş nesnenin de truthy olması sık karşılaşılan bir sürprizdir.

```js
if ([]) {
  console.log("Boş dizi bile truthy!");
}

console.log(Boolean("0")); // true
console.log(Boolean(0));   // false
```

## Eşitlik tuzağı

Gevşek eşitlik operatörü `==`, karşılaştırmadan önce dönüşüm yapabilir. Sıkı eşitlik `===` ise tipler farklıysa doğrudan `false` döndürür.

```js
console.log(0 == false);  // true
console.log(0 === false); // false
console.log(null == undefined);  // true
console.log(null === undefined); // false
```

Özetle, referans paylaşımını anlamak beklenmedik nesne değişikliklerini; coercion kurallarını bilmek ise garip görünen işlem sonuçlarını açıklar. Varsayılan tercihi `===` yapmak ve dönüşümleri açıkça belirtmek, JavaScript motoruyla tahmin oyunu oynamaktan çok daha huzurludur.
