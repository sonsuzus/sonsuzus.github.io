---
title: Javascript Veri Tipi Dönüşümü
author: sonsuz
date: 2023-08-30 20:39:48 +0300
categories: [Program,Javascript]
tags: [javascript,programlama,js,veri tipi]
---





```js
var a = 10;

var b = "20";

var sonuc = a + b;
```

dediğimizde sonucun **1020** olduğunu görürüz. Çünkü b değişkeni string bir değer ve içindeki karakterlerin rakam olması önemli değildir burada tırnak kullanıldığından dolayı b bir string değer taşıyor. Dolayısıyla matematiksel bir ifadeye girmeden önce tüm değişkenlerin number türünde olması gerekiyor.

```js
var a = 10;

var b = "20";

var sonuc = a + Number(b);
```

şeklinde b değerini **Number()** metodu ile number veri tipine dönüştürmeniz gerekiyor.

```js
var val = String(10)  // Number - String Tür Dönüşümü

console.log(val)

console.log(typeof val)
```

10 sayısal değerini string' e çeviriyoruz.

```js
var val = String(true)  // Boolean - String Tür Dönüşümü

console.log(val)

console.log(typeof val)
```

Boolean tipindeki true değerini string 'true' değerine çeviriyoruz.

```js
val = String(new Date())  // Date to String

console.log(val) 

console.log(typeof val)  // Tue Sep 17 2019 14:52:53 GMT+0300 (GMT+03:00)



Date objesini string bir veriye çeviriyoruz. 

```

```js
val = String([1,2,3,4])  // Array to String



console.log(val)   //  1,2,3,4

console.log(typeof val)
```

Dizi elemanları artık string bir değere dönüşür. Gördüğümüz değer "1,2,3,4" şeklindedir.

Tür dönüşümü için ayrıca **toString()** metodunu da kullanabiliriz.

```js
val = (10).toString()

val = (false).toString()




```

```js
val = Number(true)  // Boolean to Number

console.log(val) 

console.log(typeof val)
```

Boolean true değerinin sayısal karşılığı 1 ve false değerinin karşılığı ise 0' dır.

```js
val = Number(null)  // Null to Number



console.log(val) 

console.log(typeof val)
```

null değerinin sayısal karşılığı 0' dır.

```js
val = Number('A')  // String to Number



console.log(val) 

console.log(typeof val)
```

String bir değerin sayısal karşılığı NaN (Not a number) olarak karşımıza çıkar.

```js
val = Number([1,2,3,4])  // Array to Number



console.log(val) 

console.log(typeof val)
```

Array bir değerin sayısal karşılığı NaN (Not a number) olarak karşımıza çıkar.

Sayısal tür dönüşümü için ayrıca **parseInt()** ve **parseFloat()**metotlarını kullanabiliriz.

```js
val = parseInt('10')

val = parseInt('10.5')

val = parseFloat('10.5')


```
