---
title: Javascript Sayılar
author: sonsuz
date: 2023-08-31 20:12:38 +0300
categories: [Program,Javascript]
tags: [javascript,programlama,js,sayı]
---




## Javascript Sayılar

Javascript 'de bir sayı veri türü vardır. Tanımladığımız her sayısal veri tam sayı ya da ondalıklı sayı olabilir. 

Sayısal bir veri tanımlarken tırnak kullanmamalıyız.

```js
var x = 10;    // Ondalıklı sayı 

var y = 10.5;  // Tam sayı
```

## Javascript Toplama

Javascript' de sayısal verileri+ operatörü ile toplayabiliriz.

```js
var x = 10;

var y = 20;

var z = x + y;   // 30
```

Peki **Javascript string** türündeki verileri + operatörü ile toplamak istersek?

```js
var x = "10";

var y = 20;

var z = x + y;   // 1020
```

x değişkenine atanan veri tırnak ile tanımlandığından dolayı string olarak kabul edilir ve sayı veri türünde olmaz dolayısıyla string toplama işlemi yapılır ve z değişkeni 1020 değerine eşitlenir.

**Aynı şekilde x gibi y değişkeni de tırnaklar içinde tanımlanmış olsaydı sonuç gene aynı olurdu.**

Peki toplama işlemine bir değişken daha eklersek?

```js
var x = 10;

var y = 20;

var z = "30";

var result = x + y + z;  // 3030
```

x ve y değişkeni **javascript sayı**veri türünde olduğundan dolayı x+y sonucu 30 değerini verir. 30+z işlemi ise z değişkeninin string veri türünde olmasından dolayı string birleştirme işlemi ile işlem 3030 olarak sonuçlanır.

> Önemli olan + operatörünün sağ ve solundaki değişkenin javascript sayı veritüründe olup olmamasıdır. Bir değişken string ise string toplama işlemi yapılır.
{: .prompt-tip }

## Javascript Matematiksel İşlemler

"+" operatörünün dışında diğer matematiksel operatörlere gelen string veri türleri javascript number türüne çevrilmeye çalışılırlar.

```js
var x = "10";

var y = "2";

var z = x / y;   // 5
```

x ve y değişkeni string olmasına rağmen bölme işleminde string veri türleri **javascript sayı**veri türüne çevrilir.

**Aynı işlemi bölme yerine çarpma ve çıkarma işleminde de test edebilirsiniz.**

## Javascript NaN (Not a Number)

Javascript NaN, bir değerin sayı olmadığı anlamını taşır. 

```js
var x = 10 / "2a";  // NaN
```

Normalde bölme işlemine giren string bir değer **javascript sayı**türüne çevrilmek istenir ancak **2a** değeri **javascript sayı**türüne çevrilemediğinden dolayı sayısal bir sonuç vermesi gereken bölme işlemi **NaN** sonucunu verir. Eğer ki 2a yerine string "2" değeri gelseydi bölme işlemi yapılabilirdi.

Peki bölme işlemine girmeden önce gelen **javascript input value**değerinin javascript number türüne çevirilip çevrilmeyeceğini önceden öğrenemez miyiz? Tabi ki öğrenebiliriz.

## Javascript isNan() Metodu

isNan() metoduna parametre olarak gönderdiğimiz değer eğer NaN yani sayısal olmayan bir değer ise bu durumda true sonucunu gönderir.

```js
isNaN("2a")  // true

isNaN("2")   // false
```

Dolayısıyla kullanıcıdan aldığınız **javascript input value** değerinin gerçekten sayı olup olmadığını kontrol edebilirsiniz.

```js
var sayi = input('sayı: ');

if (isNaN(sayi)){

   console.log('girilen değer sayı değil');

}
```
