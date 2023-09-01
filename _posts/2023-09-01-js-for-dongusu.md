---
title: Javascript For Döngüsü
author: sonsuz
date: 2023-09-01 15:57:49 +0300
categories: [Program,Javascript]
tags: [javascript,js,programlama,döngü,for]
---





## Javascript Döngüler

Javascript 'de döngü yardımıyla bir kod parçasını bir koşula bağlı olarak tekrar tekrar çalıştırabiliriz.

Örneğin bir isim listesindeki her bir ismi ekrana tekrar tekrar yazmak yerine döngü kullanımı işimizi oldukça kolaylaştırır.

```js
var isimler = ["ali", "ahmet", "can", "canan"];

console.log(isimler[0]);  // ali

console.log(isimler[1]);  // ahmet

console.log(isimler[2]);  // can

console.log(isimler[3]);  // canan



for (i = 0; i < isimler.length; i++) {

  console.log(isimler[i]);

}
```

## Javascript Döngü Tipleri

Javascript ile döngü oluşturmak için aşağıdaki alternatifleri kullanabilirsiniz.

* for
* for / in
* for / of
* while
* do / while

## Javascript For Döngüsü

For döngüsünün kullanımı şu şekildedir;

```js
for (bölüm 1; bölüm 2; bölüm 3) {

  // tekrarlanacak kod bloğu

}
```

bölüm 1: Kontrol değişkenin tanımlandığı kısımdır. Döngü başladığında sadece bir kez işletilir. 

bölüm 2: Koşulun tanımlandığı kısımdır. Koşul true getirdiği sürece döngü bloğundaki kodlar işletilir.

bölüm 3: Kod blokları her işletildikten sonra koşul durumuna bakılmadan bu kısım işletilir.

Örnek: Javascript ile 1 den 10 a kadar sayıların yazdırılması

```js
for (i = 1; i <= 10; i++) {

  console.log(i);

}
```

Örneğimizde 1-10 arasındaki sayıları yazdırmak istiyoruz. Bu durumda bölüm 1' de "i" değişkeni tanımlayıp 1 değerinden başlatalım ve i değerinin 10 dan (i<=10) küçük ya da eşit olup olmadığını bölüm 2 de kontrol edelim. Eğer true getiriyorsa bu durumda kod bloklarını işletip i değerini ekrana yazalım. Kod blokları her işletildikten sonra bölüm 3 işletilir ve i değeri 1 arttırılır aksi halde sonsuz döngüye gireriz çünkü döngü başında 1 değerine sahip olan i değeri her zaman 1' dan küçük olur.

## Dizi Elemanlarının For ile Yazdırılması

Dizi elemanlarına tek tek indeks değerleri ile ulaşabiliriz ancak dizi çok fazla eleman içerdiğinde bu oldukça zor olur dolayısıyla dizi elemanlarına döngü ile ulaşmak işimizi kolaylaştırır.

Örnek: Javascript ile dizi elemanlarını yazdırma

```js
var markalar = ["mazda","opel","bmw","toyota"];

for (i = 0; i < markalar.length; i++) {

  console.log(markalar[i]);

}
```

markalar.length bize dizinin kaç eleman içerdiğini getirir. Dolayısıyla dizi eleman sayısı değiştiğinde de döngü çalışmaya devam eder.

Örnek: Javascript sözlük döngü kullanımı

```js
let people =[

   {firstName:'Ada',lastName:'Bilgi'},

   {firstName:'Yiğit',lastName:'Bilgi'},

   {firstName:'Çınar',lastName:'Turan'}

];



for (let i=0; i<people.length;i++){

     console.log(people[i].firstName + ' ' + people[i].lastName);

}
```

Döngü ile ulaştığımız her bir nesne içinde firstName ve lastName özellikleri mevcuttur dolayısıyla döngü yardımıyla ad soyad arasına bir boşluk ekleyerek kolaylıkla yazdırabiliriz.
