---
layout: post
title: "Fonksiyonlar Sahneye Çıkıyor: Birinci Sınıf Vatandaşlık ve Arrow Function’lar"
math: true
categories: 
  - Bilgi
tags: 
  - JavaScript
  - Fonksiyonel Programlama
  - Arrow Functions
---

Programlamada fonksiyonları yalnızca çağrıldığında çalışan kod paketleri olarak düşünmek eksik kalır. JavaScript gibi dillerde fonksiyonlar aynı zamanda değişkenlere atanabilir, başka fonksiyonlara gönderilebilir ve sonuç olarak döndürülebilir. Kısacası fonksiyonlar, dilin ayrıcalıklı üyeleri değil; diğer değerlerle aynı haklara sahip **birinci sınıf vatandaşlarıdır**.

``

## Birinci sınıf vatandaş ne demektir?

Bir programlama dilinde bir değer aşağıdaki işlemleri destekliyorsa genellikle birinci sınıf kabul edilir:

- Bir değişkene atanabilir.
- Veri yapılarında saklanabilir.
- Fonksiyonlara parametre olarak geçirilebilir.
- Başka bir fonksiyondan döndürülebilir.

JavaScript fonksiyonları bu koşulların tamamını karşılar. Matematiksel açıdan bir fonksiyonu $f: A \rightarrow B$ biçiminde gösteririz. Bu ifade, $f$ fonksiyonunun $A$ kümesindeki bir girdiyi $B$ kümesindeki bir çıktıya dönüştürdüğünü söyler. Programlamadaki önemli fark, $f$ değerinin kendisini de taşıyabilmemizdir.

```javascript
const topla = function (a, b) {
  return a + b;
};

const hesapla = topla;
console.log(hesapla(4, 6)); // 10
```

Burada `topla` fonksiyonu çalıştırılmadan `hesapla` değişkenine atanır. Parantez kullanılmaması kritiktir: `topla` fonksiyonun kendisini, `topla()` ise fonksiyon çağrısının sonucunu ifade eder.

## Fonksiyonları parametre olarak geçirmek

Bir fonksiyona başka bir fonksiyon verilmesine **callback** yaklaşımı denir. Callback alan fonksiyon ise yüksek dereceli fonksiyondur. Bu yapı, davranışı veriden ayırarak tekrar kullanılabilir kod üretmemizi sağlar.

```javascript
function uygula(sayi, islem) {
  return islem(sayi);
}

const ikiyleCarp = x => x * 2;
const karesiniAl = x => x ** 2;

console.log(uygula(5, ikiyleCarp)); // 10
console.log(uygula(5, karesiniAl)); // 25
```

`uygula`, hangi hesabın yapılacağını bilmez; yalnızca aldığı davranışı çalıştırır. Matematiksel olarak bunu $uygula(x, f) = f(x)$ şeklinde düşünebiliriz. Böylece aynı mekanizma, farklı fonksiyonlarla farklı sonuçlar üretir.

## Fonksiyondan fonksiyon döndürmek

Fonksiyonlar sonuç olarak da üretilebilir. Bu teknik yapılandırılabilir ve özelleştirilebilir işlemler oluşturmak için kullanışlıdır.

```javascript
function carpaniOlustur(carpan) {
  return sayi => sayi * carpan;
}

const ucleCarp = carpaniOlustur(3);
console.log(ucleCarp(7)); // 21
```

Döndürülen fonksiyon, dış fonksiyon tamamlandıktan sonra bile `carpan` değerini hatırlar. Bu davranışa **closure** denir. Adeta fonksiyon küçük bir sırt çantası taşır ve doğduğu kapsamın değişkenlerini yanında götürür.

## Arrow function avantajları

Arrow function sözdizimi özellikle kısa callback ifadelerinde kodu sadeleştirir.

| Özellik | Klasik fonksiyon | Arrow function |
|---|---|---|
| Yazım | `function (x) { return x * 2; }` | `x => x * 2` |
| `this` davranışı | Çağrılma biçimine göre belirlenir | Dış kapsamdaki `this` değerini kullanır |
| `arguments` nesnesi | Bulunur | Bulunmaz |
| Constructor kullanımı | `new` ile kullanılabilir | `new` ile kullanılamaz |
| Kısa callback uygunluğu | Daha uzun | Genellikle daha okunaklı |

Tek ifadeli arrow function’larda `return` ve süslü parantezler çıkarılabilir:

```javascript
const fiyatlar = [100, 200, 300];
const kdvliFiyatlar = fiyatlar.map(fiyat => fiyat * 1.20);
```

Ancak arrow function her durumda daha iyi değildir. Nesne metotlarında dinamik `this` gerekiyorsa klasik fonksiyon tercih edilmelidir.

```javascript
const kullanici = {
  ad: "Ada",
  selamla() {
    console.log(`Merhaba, ${this.ad}!`);
  }
};
```

Sonuç olarak birinci sınıf fonksiyonlar; callback, closure, olay yönetimi ve fonksiyonel programlama gibi pek çok yaklaşımın temelidir. Arrow function’lar bu gücü kısa bir sözdizimiyle sunar, fakat `this` ve constructor farklılıkları unutulmamalıdır. Fonksiyonları yalnızca çalışan bloklar değil, taşınabilen ve birleştirilebilen değerler olarak gördüğünüzde JavaScript çok daha esnek bir oyun alanına dönüşür.
