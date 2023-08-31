---
title: Javascript String Metotları
author: sonsuz
date: 2023-08-31 23:22:43 +0300
categories: [Program,Javascript]
tags: [javascript,js,string,metot]
---



## Javascript String Metotları Kullanımı

Javascript string nesnesi ile hazır olarak gelen bir çok kullanışlı string metodu vardır.

**Javascript string metotları**na tanımladığımız string karakter dizisi üzerinden ulaşırız.

Aşağıdaki javascript string metotlarını sırasıyla öğrenelim;

* String concat()
* String indexof() ve lastindexof()
* String search()
* String toUpperCase() ve toLowerCase()
* String trim()
* String slice()
* String substring()
* String substr()
* String replace()
* String split()

## String concat()

**Javascript concat()** metodu ile string concatenation yani string birleştirme yapabiliriz.

```js
var adsoyad = ad.concat(' ',soyad);  //Sadık Turan
```

Orginal string verisi üzerinde bir güncelleme yapılmaz çünkü javascript' de string veriler immutable yani değiştirilemez. Concat örneğimizde ad ile soyad değişkenini birleştirip yeni bir string verinin içerisine kopyalıyoruz.

## String indexof() ve lastindexof() Metodu

String **indexof()** metodunu karakter dizisinde arama yapmak için kullanıyoruz.

string indexof() metodu parametre olarak gönderdiğimiz karakterin ilgili string dizisi içinde ilk geçtiği index bilgisini gönderir.

Eğer aranan ifade bulunamazsa -1 değeri gelir.

Karakter dizilerinin ilk karakteri 0' dan başlar.

```js
var kurs = "Modern Javascript Dersleri: Baştan Sona Javascript Programlama";

var result = kurs.indexOf("Javascript"); // result: 7


```

Javascript, karakter dizisi içerisinde ilk olarak 7.indeks de bulunur.

\*\* **lastindexof()** metodu ise son bulunan karakterin indeks numarasını gönderir.

```js
var kurs = "Modern Javascript Dersleri: Baştan Sona Javascript Programlama";

var result = kurs.lastindexOf("Javascript"); // result: 40
```

Javascript, karakter dizisi içerisinde 2 defa bulunur ve lastindexof() en son bulduğunun indeks numarasını gönderir.

\*\* indexof() ve lastindexof() metotları ikinci parametre olarak aramanın başlanmak istediği indeks numarasını alabilirler.

```js
var kurs = "Modern Javascript Dersleri: Baştan Sona Javascript Programlama";

var result = kurs.indexof("Javascript",10); // result: 40
```

indexof() metoduna gönderilen 10 parametresi ile 10.indeks den itibaren arama yapılır dolayısıyla ilk Javascript bulunmaz ikinci bulunur.

## String search()

String search() metodu da indexof() metodu gibi karakter dizisi içinde arama yapıp bulduğu karakterin indeks numarasını döndürür.

```js
var kurs = "Modern Javascript Dersleri: Baştan Sona Javascript Programlama";

var result = kurs.search("Javascript"); // result: 7
```

\*\* search() ile indexof() metodunun **farkı ise;**

* search(), indexof() metodunda olduğu gibi aramaya başlanacak olan indeks numarasını almaz.
* indexof() metodu regular expression ifadelerini almaz.

## String toUpperCase() ve toLowerCase()

Javascript transform metotlarından **toUpperCase()** metodu ile karakter dizisini büyük harfe, **toLowerCase()** ile küçük harfe çevirebiliriz.

```js
var str1 = "Hello World!"; 

var str2 = str1.toUpperCase();  // HELLO WORLD!

var str3 = str1.toLowerCase();  // hello world!
```

## String trim()

trim() metodu ile karakter dizisinin başındaki ve sonundaki boşluk karakterlerini sileriz.

```js
var greeting="   Hello World!    ";

alert(greeting.trim()); // Hello World!
```

## String Parçalama Metotları

Javascript' de bir karakter dizisi içinde belli aralıktaki karakterleri alabiliriz. String parçamak için kullanabileceğimiz 3 tane string metodu vardır.

* String slice()
* String substring()
* String substr()

String parçalama metotların sırasıyla öğrenelim.

## String slice()

slice() metoduna başlangıç ve bitiş indeksi vererek aralıktaki karakter dizisini alabiliriz.

```js
var str = "Mazda,Opel,Toyota";

var result = str.slice(6, 10); // Opel
```

7.indeksten başlar ve 10' e kadar alır. Son indeks numarası dahil olmaz.

\*\* Başlangıç ve bitiş indekslerini negatif olarak da verebiliriz. En sağdaki karakter -1 ile başlar.

```js
var str = "Mazda,Opel,Toyota";

var result = str.slice(-11,-7); // Opel


```

slice() metoduna bitiş indeksini vermezsek sona kadar alır.

```js
var str = "Mazda,Opel,Toyota";

var result = str.slice(6); // Opel,Toyota
```

## String substring()

slice() metodun olduğu gibi substring() metoduyla başlangıç ve bitiş indeksi vererek aralıktaki karakter dizisini alabiliriz.

\*\* slice() metodu ile substring() metodunun farkı; substring()'^da negatif indeks kullanamıyoruz.

```js
var str = "Mazda,Opel,Toyota";

var result = str.slice(6, 10); // Opel
```

\*\* slice() metodunda olduğu gibi bitiş indeksini vermezsek sona kadar alır.

## String substr()

substr(), slice() ve substring() gibi string parçalama işlemlerinde kullanılır ancak diğer metotlardan farkı ikinci parametre başlangıçtan itibaren alınacak karakter sayısını temsil eder.

```js
var str = "Mazda,Opel,Toyota";

var result = str.substr(6,4); // Opel
```

\*\* ikinci parametre göndermezsek karakter dizisinin sonuna kadar alır.

## String replace()

replace() metodu ile belirtilen bir string bilgiyi başka bir string bilgi ile güncelleyebiliriz.

```js
var str = "Mazda,Opel,Toyota";

var result = str.replace("Mazda","Renault"); // Renault,Opel,Toyota
```

\*\* replace() metodu bulduğu ilk karakteri istenen karakter ile günceller.

## String split()

Karakter dizisini belirtilen karakterden parçalara ayırarak bir dizi oluşturur.

```js
var adsoyad= "Sadık Turan";

result = adsoyad.split(" "); 
```

Boşluk karakterinden böler ve geriye bir dizi gönderir.

**result[0]** dediğimizde "**Sadık"**,

**result[1]** dediğimizde ise, "**Turan"**bilgisi gelir.

```js
var str = "Mazda,Opel,Toyota";

result = str.split(",");



// result[0]  => Mazda

// result[1]  => Opel

// result[2]  => Toyota
```

## String Metot Örnekleri

Aşağıdaki string metot örneklerini yapınız.

```js
var sentence = " Template Literals or template strings is the ability Have multi-line strings without any funny business. ";

var url = "http://sadikturan.com/Modern Javascipt KURSU sıfırdan ileri seviye ü ö ş";
```

1- Cümle kaç karakterlidir ?

```js
console.log(sentence.length);
```

2- Kaç kelimeden oluşuyor ?

```js
console.log(sentence.trim().split(' ').length);
```

3- Tüm cümleyi küçük harfe çevirin.

```js
console.log(sentence.toLowerCase());

console.log(sentence.toUpperCase());
```

4-Cümlenin başındaki ve sonundaki boşlukları siliniz.

```js
console.log(sentence.trim());
```

5- '-' karakterini silin.

```js
console.log(sentence.replace('-',''));
```

6- url'nin içinden str kısmını çıkarınız.

```js
var str = 'http://';

console.log(url.substr(str.length));

console.log(url.slice(str.length));
```

7- Url hangi protocol'u kullanmaktadır ? (http,https)

```js
console.log(url.startsWith('http'));

console.log(url.startsWith('https'));
```

8- url, '.com' ifadesini içeriyor mu?

```js
console.log(url.indexOf('.com'));

console.log(url.includes('.com'));
```

9- url string ifadesini geçerli bir url olarak düzenleyiniz.

```js
console.log(url.toLowerCase()

  .replace(/ /g,'-')

  .replace(/ı/g,'i')

  .replace(/ü/g,'u')

  .replace(/ö/g,'o')

  .replace(/ş/g,'s')

  .replace(/ç/g,'c'));


```
