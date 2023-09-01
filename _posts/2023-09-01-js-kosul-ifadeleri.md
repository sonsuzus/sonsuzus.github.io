---
title: Javascript Koşul İfadeleri
author: sonsuz
date: 2023-09-01 15:20:13 +0300
categories: [Program,Javascript]
tags: [javascript,programlama,js,koşul,karşılaştırma,if,else]
---




Javascript uygulamalarında belli bir duruma bağlı olan farklı kod bloklarını çalıştırmak istediğimizde if-else ve else-if bloklarını kullanırız.

## if Bloğu

if bloğu ile tanımladığımız koşul eğer doğru yani true bilgi üretiyorsa if bloğu kapsamındaki kodlar işletilir eğer false üretirse işletilmez.

```js
if (koşul) {

  //  koşul true ürettiğinde çalışacak kodlar burada tanımlanır.

}
```

Örnek

```js
var saat = 10;

if (saat < 11) {

   console.log("günaydın");

}
```

saat değişkeni 11' den az olduğu sürece (saat<11) karşılaştırması bize true getireceğinden dolayı console' da günaydın yazısını görürüz.

## else Bloğu

if bloğunun true değer üretmediği durumda da bazı kodları çalıştırmak isteyebiliriz bu durumda else bloğunu kullanmalıyız.

```js
if (koşul) {

  //  koşul true ürettiğinde çalışacak kodlar burada tanımlanır.

} else {

  //  koşul false ürettiğinde çalışacak kodlar burada tanımlanır.

}
```

Örnek

```js
var saat = 13;

if (saat < 11) {

   console.log("günaydın");

} else {

   console.log("iyi günler")

}
```

saat değeri 11' den az olmadığı için koşul bize false üretir ve console' da iyi günler yazısını görürüz.

## else if Bloğu

Bazen de bir koşula bağlı olarak farklı farklı koşullar üretmek isteyebiliriz. Bu durumda else-if bloğunu kullanarak ekstra sorular sorma imkanına sahip oluruz.

```js
if (kosul1) {

  //  koşul 1 true ürettiğinde çalışır.

} else if (kosul2) {

  // kosul1 false olduğunda koşul2 ' e bakılır. koşul2 true ise çalışır.

} else {

  //  koşul1 ve koşul2 false ürettiğinde çalışır.

}
```

Örnek

```js
var saat = 10;

if (saat < 11) {

   console.log("günaydın");

} else if (saat < 18) {

  console.log("iyi günler.");

} else {

  console.log("iyi akşamlar.");

}
```

Eğer saat 11' den küçükse ilk koşul çalışır ve ekrana günaydın yazar.

Eğer saat 18' den küçük ancak 11' den büyükse ekrana iyi günler yazar.

İki koşulun gerçekleşmediği durumlarda ise else bloğu çalışır.

\*\* else if bloğunu aşağıya doğru arttırabiliriz.
