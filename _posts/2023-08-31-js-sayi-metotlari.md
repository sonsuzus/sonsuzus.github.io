---
title: Javascript Sayı Metotları
author: sonsuz
date: 2023-08-31 20:17:40 +0300
categories: [Program,Javascript]
tags: [javascript,programlama,sayı,metot,js]
---




## Javascript Sayı Metotları

Javascript' de metotlara nesne üzerinden ulaşabiliriz ayrıca kullanabileceğimiz global seviyede de metotlar da mevcuttur. Javascript metotlarını sırasıyla öğrenelim.

Javascript' de number nesnesini Number() metodu ile tanımlayabiliriz. Ancak tanımladığımız primitive tipteki (x=10) veriler de nesne olarak tanımlanırlar. Dolayısıyla;

```js
var x = 10;             

var y = new Number(10);
```

x ve y değişkenlerinin ikiside birer nesnedir ve iki satırda da yaptığımız iş aynıdır.

\*\* Nesne kavramını ileride öğreneceğiz.

### Javascript toString() Metodu

Number türündeki veriyi string veri türüne çevirir.

```js
var x = 10;

var y = 20;

var z = x.toString() + y.toString()  // 1020
```

### Javascript toFixed() Metodu

toFixed() metodu verilen parametreye göre veriyi yuvarlar.

```js
var x = 10.439;

x.toFixed(0);           // 10

x.toFixed(2);           // 10.44

x.toFixed(4);           // 10.4390

x.toFixed(5);           // 10.43900
```

Ondalıklı kısım hangi sayıya yakınsa o sayıya yuvarlanır. Örneğin 10.439 yerine 10.501 değeri kullanılmış olsaydı ilk örnekte sonuç 11 olurdu.

Parametre olarak gönderdiğimiz sayı ondalıklı kısımdaki basamak sayısını belirtiyor.

### Javascript toPrecision() Metodu

toPrecision() metodu toFixed() metodu ile aynı iş için kullanılıyor ancak farkı toFixed() metodunda verilen parametre ondalıklı kısımdaki basamak sayısını belirtirken toPrecision() metodunda tam ve ondalıklı kısmın toplamındaki basamak sayısını belirtir.

```js
var x = 10.439;

x.toPrecision(0);           // 10.439

x.toPrecision(2);           // 10

x.toPrecision(4);           // 10.44

x.toPrecision(5);           // 10.439
```

## Global JavaScript Metotları

Global javascript metotları her veri türleri için kullanılabilir sadece javascript number veri türü ile çalışırken kullanmayız.

### Javascript Number() Metodu

Javascript 'de her hangi bir veri türünü number veri türüne çevirirken Number() metodunu kullanırız.

```js
Number(true);          // 1

Number(false);         // 0

Number("10");          // 10

Number("  10");        // 10

Number("10  ");        // 10

Number("10.55");       // 10.55

Number("10,55");       // NaN

Number("10 55");       // NaN

Number("10a");         // NaN
```

### Javascript parseInt() Metodu

parseInt() metoduna gönderdiğimiz parametreyi tam sayıya çevirir.

```js
parseInt("10");         // 10

parseInt("10.33");      // 10

parseInt("10 20 30");   // 10

parseInt("10 a");       // 10

parseInt("a10");        // NaN 
```

Gördüğünüz gibi boşluk ve string değerlerini görmezden gelir ve mümkün olduğunca tamsayıya çevirmeye çalışır.

### Javascript parseFloat() Metodu

parseInt() metodundan farklı olarak geriye ondalıklı kısmıda döndürür.

```js
parseFloat("10");         // 10

parseFloat("10.33");      // 10.33

parseFloat("10 20 30");   // 10

parseFloat("10 a");       // 10

parseFloat("a10");        // NaN 
```

## Javascript Math

Nesneye özel metotlar ve global metotlar dışında matematiksel işlemlerde kullanabilceğimiz Javascript Math objesi mevcut. 

Javascript Math objesi sayısal işlemlerde işimizi kolaylaştıracak oldukça güzel metot ve özelliklere sahiptir.

Örneğin, Math.PI dediğimizde bize pi sayısı gelir. (3.141592653589793)

### Math.round()

round() metodu ile en yakın sayıya yuvarlama yapabiliriz.

```js
Math.round(2.4);  // 2

Math.round(2.7);  // 3
```

### Math.ceil()

ceil() metodu ile en yakın tam sayıya **yukarı** yuvarlama yaparız.

```js
Math.ceil(2.4);  // 3

Math.ceil(2.6);  // 3 
```

### Math.floor()

floor() metodu ile en yakın tam sayıya **aşağı**yuvarlama yaparız.

```js
Math.floor(2.4); // 2

Math.floor(2.7); // 2
```

### Math.abs()

abs() metoduna gönderilen sayı pozitif olarak geri gönderilir.

```js
Math.abs(-10.5)  // 10.5
```

### Math.min() ve Math.max()

min() metodu kendisine gönderilen sayıların en küçüğünü bulur. max() metodu ise en büyüğünü bulur.

```js
Math.min(-5,5,-43,10)  // -43

Math.max(-5,5,-43,10)  // 10 
```

### Math.random()

random() metodu 0 ile 1 arasında rastgele bir sayı üretir.

```js
Math.random()  // 0.4273523063470368
```

> random() metodunu daha detaylı bir şekilde inceleyeceğiz.
