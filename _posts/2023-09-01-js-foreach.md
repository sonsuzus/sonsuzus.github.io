---
title: Javascript ForEach Döngüsü
author: sonsuz
date: 2023-09-01 16:17:58 +0300
categories: [Program,Javascript]
tags: [javascript,foreach,döngü,js,programlama]
---


## Javascript ForEach Döngüsü Kullanımı

**Js forEach()** fonksiyonu ile bir dizideki tüm elemanlara kolaylıkla dolaşabiliriz.

**Js forEach()** fonksiyonu Array nesnesi yani bir dizi üzerinden çağrılmalıdır.

**Js forEach()** fonksiyonuna gönderdiğimiz callback fonksiyonu dizideki her bir elemana ulaşıldığında çağrılır.

Örnek:

```js
const sayilar = [1, 2, 3];

sayilar.forEach(myFunction);

function myFunction(sayi) {

  console.log(sayi);

}



// 1

// 2

// 3
```

Sayilar dizisi üzerindeki her bir elemana ulaşıldığında myFunction fonksiyonu çağrılır ve fonksiyona gelen dizi elemanı ekrana yazdırılır.

Her bir dizi elemanı için çağrılan fonksiyona **callback fonksiyonu** denir.

Fonksiyonu isimsiz bir şekilde forEach fonksiyonu içinde tanımlayabiliriz. İsimsiz tanımlanan bu fonksiyonlara ise **anonymous fonksiyonlar** denir.

Örnek:

```js
const sayilar = [1, 2, 3];

sayilar.forEach(function(sayi) {

    console.log(sayi);

});



// 1

// 2

// 3
```

Kodlarımızı biraz daha sadeleştirmek için ES6 ile birlikte gelen **arrow function** tanımlamasını da kullanabilirsiniz.

Örnek:

```js
const sayilar = [1, 2, 3];

sayilar.forEach(sayi => console.log(sayi));



// 1

// 2

// 3
```

sayilar dizisindeki her bir eleman sırasıyla sayi içerisine kopyalanarak ekrana yazdırılabilir.

**forEach()** fonksiyonunun her bir dizi elemanı için çağırmış olduğu fonksiyona dizi elemanı haricinde dizi elemanının konum bilgisinide (indeks) gönderebiliriz.

Örnek:

```js
const sayilar = [1, 2, 3];

sayilar.forEach((sayi, index) => {

    console.log(index + ' => ' + sayi);

});



// 0 => 1

// 1 => 2

// 2 => 3


```
