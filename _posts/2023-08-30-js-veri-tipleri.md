---
title: Javascript Veri Tipleri
author: sonsuz
date: 2023-08-30 00:06:16 +0300
categories: [Program,Javascript]
tags: [javascript,programlama,veri,tip]
---


Javascript' de veri tutmak için kullandığımız javascript veri tiplerini **2 ayrı grupta** ele alabiliriz.

**Basit Veri Tipleri:** String, Number, Boolean ve undefined.

**Referans Tipler:** **Dizi**, **Nesne, Fonksiyon**ve **null** veri tipleridir. 

Javascript' de değişken tiplerini belirtmek için her veri tipine özel bir komut yoktur. Her veri tipi var komutu ile tanımlanır ancak değişkene attığımız veri tipine göre değişken farklı veri tipinde değerlendirilir.

**typeof operatörü** ile bir değişkenin veri tipini öğrenebiliriz.

## Javascript String

Javascript' de karakter dizilerini string veri tipiyle saklarız.  

```js
var firstName = 'Çınar';

console.log(typeof firstName) // string
```

Değişkenin tipine typeof ile baktığımızda **"string"** olduğunu görürüz.

String bir değişken tanımlarken tek tırnak ya da çift tırnak kullanabiliriz.

String bir veri türü karakter dizisi olarak anılır yani bir string ifadeyi karakterler topluluğu oluşturur. (dizi ile benzer)

```js
var carName1 = "Volvo XC60";    // çift tırnak

var carName2 = 'Volvo XC60';    // tek tırnak
```

Tek ve çift tırnak iç içe kullanıldığında gereklidir.

Örneğin;

```js
var str = "It's alright";    // çift tırnak içinde tek tırnak kullanımı
```

## Javascript Number

Javascript' de sayısal verileri number veri tiplerinde tutarız.

```js
var age = 20; 

console.log(typeof age)  // number
```

number türündeki değerler **tırnak kullanılmadan** oluşturulması gerekiyor. typeof operatörü ile değişkenin tipine baktığımızda **"number"** olduğunu görürüz.

```js
var money = 100.5;

console.log(typeof money)  // number
```

Ondalıklı bir sayıyı nokta ile tanımlarız ve veri tipine baktığımızda gene number türünde bir veri olduğunu görürüz.

## Javascript Boolean

Javascript' de true yada false verileri boolean veri tipinde tutarız. 

```js
var isActive = false;

console.log(isActive) // boolean
```

boolean türündeki bir veri tipi **true** ya da **false** bir değer alır. Örneğin **isActive** ismindeki boolean değişkeni içine false değerini atadık ve typeof operatörü ile bakarsak boolean tipinde olduğunu görürüz.

boolean veri tipini bir durumun doğru ya da yanlış, var ya da yok şeklinde bilgisini tutmak için kullanırız. Örneğin uygulama aktif mi; true ise **evet**, false ise **hayır**. Ya da cinsiyet bilgisini boolean veri tipinde saklayabiliriz. 

```js
var cinsiyet = true; // erkek 

var cinsiyet = false; // kadın 
```

## Javascript Undefined

Tanımlanan ancak içerisine değer atılmayan tipler için **undefined** tipi kullanılır.

```js
var car;

console.log(typeof car) // undefined
```

## Javascript Diziler

String veri türünde karakter grubu saklayabildiğimiz gibi diziler içerisinde de string bir veri ya da number türünde bir veri grubunu saklayabiliriz. Örneğin isim listesi, şehir listesi vb.

```js
var names = ['Ali','Ahmet','Can']

console.log(typeof names) // object
```

names ismindeki dizi **3** elemanlıdır. Her bir dizi elemanına atanan bir index numarası vardır ve ilk eleman 0. indeksten başlar. Dolayısıyla dizi elemanlarına ulaşmak için;

```js
console.log(names[0]) // Ali

console.log(names[1]) // Ahmet

console.log(names[2]) // Can
```

Dizinin eleman sayısını öğrenmek için **length** özelliğini kullanmamız gerekiyor. Javascript diziler için kullanabileceğimiz özellikler ve metotlar mevcuttur. Dizileri daha detaylı olarak diziler dersinde öğreneceğiz.

```js
console.log(names.length) // 3
```

## Javascript Nesne

Javascript' de bir nesne tanımlayarak bir gruba ait bilgileri ayrı ayrı değişken tanımlamamıza gerek kalmadan saklayabiliriz Örneğin bir kullanıcının bilgileri ya da bir araç bilgisi.

```js
var kullanici = {

     ad: 'Sadık',

     soyad: 'Turan',

     yas: 38

};


```

Nesne tanımlamasını tek satırda da yapabiliriz.

```js
var kullanici = { ad: 'Sadık',  soyad: 'Turan', yas: 38 };



console.log(typeof kullanici) // object
```

Nesne üzerinden bilgilere ulaşmak için nesneden sonra **'.'** operatörünü kullanabiliriz.

```js
console.log(kullanici.ad)      // Sadık

console.log(kullanici.soyad)   // Turan

console.log(kullanici.yas)     // 38
```

Alternatif olarak nesne özelliklerine ulaşmak için **[ ]** operatörünü de kullanabiliriz.

```js
console.log(kullanici["ad"])      // Sadık

console.log(kullanici["soyad"])   // Turan

console.log(kullanici["yas"])     // 38
```

## Javascript Fonksiyon

```js
var calculateAge = function(){

   return 0;

}



console.log(typeof calculateAge) // function
```

Javascript' de fonksiyonlar da bir nesne olarak nitelendirilir. Fonksiyonları ayrı bir ders içerisinde göreceğiz.

## Javascript Null

Javascript' de null bir nesne olarak algılanır. Yani tanımladığınız bir veri içine null değer attığınızda bellekte bir alan tahsis edilir ancak içerisinde bir değer olmadığını söylemiş oluruz.

```js
var person = {firstName:"Ahmet", lastName:"Turan", age:20 };

person = null;   
```

burada null değer atayarak adresi belli olan nesnenin içerisindeki değeri silmiş oluyoruz. Tanımlanan nesnenin bellek üzerindeki adresi silmiş olmayız.

Bellekteki adres kavramını anlayabilmek için nesnenin bellekte nasıl saklandığını iyi anlamak gerekiyor. Referans tipler konusunda öğreneceğiz.
