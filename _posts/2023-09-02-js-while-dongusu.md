---
title: Javascript While Döngüsü
author: sonsuz
date: 2023-09-02 12:42:17 +0300
categories: [Program,Javascript]
tags: [javascript,js,döngü,while]
---




## Javascript While Döngüsü Kullanımı

Bir duruma bağlı olarak tekrarlayan işlemleri gerçekleştirmek için js while döngüsünü kullanırız.

Kullanım şekli;

```js
while (koşul) {

  // çalıştırılacak kodlar.

}
```

While döngüsünde belirtilen koşul doğru (true) olduğu sürece blok içerisindeki kodlar işletilir eğer koşul false değer üretirse while döngüsünden çıkılır.

Örnek:

```js
let i = 1;

while (i <= 5) {

    console.log(i);

    i += 1;

}



// 1

// 2

// 3

// 4

// 5
```

i değerini başlangıçta 1 ' den başlatarak 5' e eşit ya da küçük olup olmadığını kontrol ediyoruz. Eğer i değeri 6 değerine gelirse while döngüsünün koşulu false değer getireceğinden dolayı döngü biter. Her döngü bloğu çalıştırıldığında i değerinin 1 arttırıldığına dikkat ediniz aksi halde sonsuz döngüye gireriz ve uygulama hata ile sonlanır.

Örnek:

```js
let toplam = 0;



// kullanıcıdan sayı alınır.

let sayi = parseInt(prompt('sayı giriniz: '));



// girilen sayı pozitif olduğu sürece döngü çalışır.

while(sayi > 0) {

    

    toplam += sayi;



    // sayı pozitif olduğu için tekrar kullanıcıdan sayı alalım.

    sayi = parseInt(prompt('sayı giriniz: '));

}



// toplamı göster.

console.log(`toplam: ${toplam}.`);



// sayı giriniz: 4

// sayı giriniz: 4

// sayı giriniz: -5

// toplam: 8
```

Döngüye girmeden önce toplam 0 değerine eşitlenir.

Kullanıcıdan alınan sayı int veriye çevrilir çünkü sayısal bir karşılaştırma yapacağız.

Girilen sayı 0' dan büyük olduğu sürece while(true) olacağından dolayı while kod blokları işletilir.

Her girilen sayi değeri toplam içerisine eklenir ve kullanıcıdan yeni bir sayı istenir.

Kullanıcı ne zaman negatif bir değer girerese while(false) olacağından dolayı while döngüsü sonlandırılır ve ekrana toplam değer yazdırılır.

## Javascript Do-While Döngüsü

While döngüsünde döngü bloklarının en az bir kere çalıştırılması için while koşulunun true getirmesi gerekir ancak do-while döngüsünde koşul false getirecek olsa bile while döngüsünün kod blokları en az bir kere işletilir çünkü koşul durumunun kontrolü sonda yapılır.

Kullanım şekli;

```js
do {

  // çalıştırılacak kodlar.

}

while (koşul);
```

Kodlar yukarıdan aşağı doğru işletilir dolayısıyla while(koşul) false değer getirecek olsa bile döngü bunu bilemez ve blok içindeki kodları en az 1 kere çalıştırır.

Örnek:

```js
let i = 1;

do {

    console.log(i);

    i++;

} while(i <= 5);



// 1

// 2

// 3

// 4

// 5
```

Başlangıçta tanımlanan i değeri hemen ekrana yazdırılır sonrasında 5' e eşit ya da küçük olup olmadığı kontrol edilir. while i değişkenin 5 e kadar true değeri getiremesinden dolayı işletilir ve ekrana 1-5 arasındaki sayılar yazdırılır. 

Örnek:

```js
let toplam = 0;

let sayi = 0;



do {

    toplam += sayi;

    sayi = parseInt(prompt('sayı giriniz: '));

} while(sayi >= 0)



console.log(`toplam: ${toplam}.`);



// sayı giriniz: 4

// sayı giriniz: 4

// sayı giriniz: -5

// toplam: 8
```

sayi başlangıçta 0 değerine eşitleniyor çünkü kullanıcı sayı girmeden önce etkisiz eleman ile toplam içeriği toplanması gerekiyor.

Kullanıcı sayi girdikten sonra while bloğunda girilen sayının pozitif kontrolü yapılıyor ve pozitif olduğu sürece toplam hesaplanıyor.

Kullanıcı negatif değer girerse döngüden çıkılıyor.
