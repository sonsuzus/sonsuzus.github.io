---
title: Javascript Diziler
author: sonsuz
date: 2023-08-31 23:52:39 +0300
categories: [Program,Javascript]
tags: [programlama,js,javascript,dizi]
---






**Javascript array** ile birden fazla veriyi bir değişken içinde saklayabiliriz.

```js
var names = ['çınar','sena','ada','yiğit'];

var years = [2017,1970,1990,1998];



var result = "Benim adım " + names[0] + " ve yaşım " + (2020- years[0]);

console.log(result); // Benim adım çınar ve yaşım 3


```

## Neden Javascipt Dizi Kullanırız

**Javascript dizi**olmadan isimleri bir string değişken içinde saklayabiliriz.

```js
var names = 'çınar,sena,ada,yiğit';
```

Bu şekilde bir string değişken tanımlaması yapabiliriz. Ancak her bir isme ulaşma ihtiyacı duyduğumuzda zorlanırız.

Daha önceki [javascript string ve string metotları](https://sonsuzus.github.io/posts/js-string-metotlari/) dersinde öğrendiğimiz split() metodunu kullanarak string bilgiyi virgülden ayırarak elemanlara teker teker ulaşabiliriz.

```js
var names = 'çınar,sena,ada,yiğit';

var result = names.split(",");



// result[0] => çınar

// result[1] => sena

// result[2] => ada

// result[3] => yiğit
```

Zaten burada dikkat edersek **split(",")** dediğimizde string bilgiyi virgülden ayırarak bir **diziye çevirir.** Dolayısıyla dizi elemanlarına da indeks numaraları ile ulaşabiliriz.

Ancak bu işin tabi ki kolay yolu en başta bir dizi tanımlamaktır.

## Javascript Dizi Tanımlama

**Javascript dizi**tanımlamak için köşeli parantezler içinde her bir elemanı virgül ile ayırmamız gerekir.

```js
var names = ['çınar','sena','ada','yiğit'];

var years = [2017,1970,1990,1998];
```

Ayrıca **javascript dizi**tanımlaması için new komutunu da kullanabiliriz.

```js
var names = new Array('çınar','sena','ada','yiğit');

var years = new Array(2017,1970,1990,1998);
```

**Javascipt dizi**içerisine aynı tipte eleman ekleyebileceğimiz gibi farklı tipte veri de eklebiliriz.

```js
var mix = ['sadık','turan',1983,null,undefined,['sinema','kitap']];


```

## Javascript Dizi Elemanlarına Erişim

**Javascript dizi**elemanlarına erişmek için indeks numarasını kullanırız. Javascript array 'in ilk elemanı 0 indeks numarasına sahiptir.

```js
console.log(names[0]) // çınar

console.log(names[1]) // sena

console.log(names[2]) // ada

console.log(names[3]) // yiğit
```

Eğer **javascipt dizi**bilgisine olduğu gibi ulaşmak istersek;

```js
var names = ['çınar','sena','ada','yiğit'];

print(names)  // çınar,sena,ada,yiğit'
```

Peki dizinin son elemanına ulaşmak istersek?

```js
var names = ['çınar','sena','ada','yiğit'];

var soneklenen = names[names.length - 1];
```

Dizinin son elemanının indeks numarası indeks 0' dan başladığı için "eleman sayısı - 1" olur. Dolayısıyla eleman sayısını bulmak için **names.length** özelliğini kullanabiliriz.

Peki **javascript dizi**içerisine bir başka array varsa bu durumda, ulaştığımız array üzerinden diğer array 'e gene indeks numarası ile geçiş yapabiliriz.

```js
var profile = ['sadık','turan',1983,['sinema','kitap']];

console.log(profile[3][0]) // sinema
```

## Javascript Dizi Elemanlarına Döngü ile Erişim

Tanımlanan javascript array' ine tek tek indeks numaraları ile ulaşmak mümkün ancak bazen tüm elemanlara ulaşmak isteriz. Bu durumda dizi üzerinde döngü yardımıyla tek tek dolaşabiliriz.

```js
var names = ['çınar','sena','ada','yiğit'];

for (var i=0; i<names.length;i++){

    console.log(names[i]);

}



// çınar

// sena

// ada

// yiğit


```

## Javascript Dizi Elemanlarını Güncelleme

**Javascript dizi** elemanına indeks numarası ile ulaşıp yeni bir değer ataması yapabiliriz.

```js
var cars = ['mazda','opel','toyota','bmw'];

cars[1] = "audi";

console.log(cars[1]) // audi
```

## Javascript Dizi Üzerine Yeni Eleman Ekleme

Dizi üzerine eleman eklemek için kullanabileceğimiz array metotları var ve bu metotları bir sonraki dersimizde göreceğiz.

Dizi metotlarından başka bir de length özelliğini kullanarak eleman ekleme yapabiliriz.

```js
var cars = ['mazda','opel','toyota','bmw'];

cars[cars.length] = "mercedes";
```

cars.length bize 5 sayısını verir ve olmayan bir indeks olduğundan son eleman olarak yeni bir değeri dizi üzerine eklemiş oluruz.
