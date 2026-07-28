---
layout: post
title: "Modern JavaScript’te var, let ve const: Kapsamın Görünmeyen Sınırları"
math: true
categories: 
  - Bilgi
tags: 
  - JavaScript
  - Scope
  - Değişkenler
---

JavaScript’te değişken tanımlamak kolay görünür: Bir anahtar kelime seçer, isim verir ve değeri atarsınız. Ancak `var`, `let` ve `const` arasındaki seçim yalnızca sözdizimsel bir tercih değildir. Bu kelimeler; değişkenin nerede erişilebilir olduğunu, ne zaman oluşturulduğunu ve yeniden atanıp atanamayacağını belirler. Yanlış seçim, özellikle iç içe bloklarda oldukça şaşırtıcı hatalar doğurabilir.

``

## Kısa bir tarih yolculuğu

JavaScript’in ilk sürümlerinde değişken tanımlamak için yalnızca `var` bulunuyordu. Dil başlangıçta küçük tarayıcı betikleri için tasarlandığından blok kapsamı önemli bir ihtiyaç sayılmamıştı. Uygulamalar büyüyünce `var` davranışları hata kaynağına dönüştü. ECMAScript 2015, yani ES6 ile `let` ve `const` eklenerek modern kapsam modeli güçlendirildi.

| Özellik | `var` | `let` | `const` |
|---|---|---|---|
| Kapsam | Fonksiyon | Blok | Blok |
| Yeniden atama | Evet | Evet | Hayır |
| Aynı kapsamda yeniden tanımlama | Evet | Hayır | Hayır |
| Hoisting | `undefined` ile erişilebilir | TDZ içinde | TDZ içinde |
| İlk değer zorunlu mu? | Hayır | Hayır | Evet |

## Fonksiyon ve blok kapsamı

Fonksiyon kapsamı, bir değişkenin tanımlandığı fonksiyonun tamamında erişilebilir olmasıdır. Blok kapsamı ise erişimi `{` ve `}` arasındaki bölgeyle sınırlar. `if`, `for` ve `while` gövdeleri birer blok oluşturur.

```javascript
function kapsamTesti() {
  if (true) {
    var eskiDegisken = "var dışarı çıkabilir";
    let modernDegisken = "let blokta kalır";
    const sabitDegisken = "const da blokta kalır";
  }

  console.log(eskiDegisken); // Çalışır
  // console.log(modernDegisken); // ReferenceError
  // console.log(sabitDegisken);  // ReferenceError
}
```

Burada `var`, `if` bloğunu önemsemez ve `kapsamTesti` fonksiyonuna bağlanır. `let` ile `const` ise yalnızca tanımlandıkları blokta yaşar. Bu sınır, aynı değişken adının yanlışlıkla başka bir değeri ezmesini önler.

Kapsamları iç içe halkalar gibi düşünebiliriz. JavaScript bir ismi önce mevcut kapsamda, ardından dış kapsamlarda arar. İç içe kapsam sayısı $n$ ise en kötü durumda kavramsal olarak $n$ ortam kontrol edilir:

$$T(n) = O(n)$$

Bu ifade çoğunlukla performans hesabından ziyade sözcüksel kapsam zincirini anlamak için yararlıdır.

## Hoisting ve geçici ölü bölge

Üç anahtar kelimeyle oluşturulan bildirimler de kapsamın başında kayda alınır; fakat erişim davranışları aynı değildir. `var`, bildirim satırından önce `undefined` değerini verir. `let` ve `const` ise bildirim çalıştırılana kadar **Temporal Dead Zone**, yani geçici ölü bölge içindedir.

```javascript
console.log(puan); // undefined
var puan = 10;

// console.log(seviye); // ReferenceError
let seviye = 2;
```

Bu nedenle “`let` hoist edilmez” sözü teknik olarak eksiktir. Bildirim bilinir, fakat erken erişime izin verilmez. Böylece değer oluşturulmadan önce kullanma hataları sessizce ilerlemek yerine görünür hâle gelir.

## `const` gerçekten sabit mi?

`const`, değerin tamamen değişmez olduğunu değil, değişken bağının yeniden atanamayacağını söyler. Bir nesnenin içeriği hâlâ değiştirilebilir.

```javascript
const kullanici = { ad: "Ada", puan: 10 };
kullanici.puan += 5; // Geçerli: nesnenin alanı değişiyor

// kullanici = {}; // TypeError: bağ yeniden atanamaz
```

Gerçek değişmezlik gerekiyorsa `Object.freeze()` gibi ek yöntemler kullanılmalıdır. Ancak bu yöntem varsayılan olarak yalnızca yüzeysel dondurma yapar.

## Hangisini seçmeliyiz?

Modern JavaScript’te güvenli başlangıç noktası `const` kullanmaktır. Değer daha sonra yeniden atanacaksa `let` tercih edilir. `var` ise eski kodları anlamak veya özel uyumluluk ihtiyaçları dışında genellikle kullanılmamalıdır.

```javascript
const maksimum = 100;
let toplam = 0;

for (let i = 0; i < maksimum; i++) {
  toplam += i;
}
```

Bu yaklaşım niyeti açıkça gösterir: `maksimum` değişmeyecek, `toplam` ve sayaç ise güncellenecektir. Kısacası `const` varsayılanınız, `let` bilinçli alternatifiniz, `var` ise JavaScript tarih müzesindeki dikkatle incelenmesi gereken eseriniz olsun.
