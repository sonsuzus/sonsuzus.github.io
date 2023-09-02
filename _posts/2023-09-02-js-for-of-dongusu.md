---
title: Javascript For/Of Döngüsü
author: sonsuz
date: 2023-09-02 12:38:31 +0300
categories: [Program,Javascript]
tags: [javascript,programlama,döngü,for,of]
---




## Javascript For/Of Döngüsü Kullanımı

Javascript for/of döngüsü ile iterable bir nesnenin tüm elemanlarına ulaşabiliriz.

Iterable nesneler yapı itibariyle elemanları üzerinde döngüler ile gezilebilir nesnelerdir. Örneğin array, set, map, string gibi javascript nesneleri iterable nesnelerdir.

Kullanım şekli;

```js
for (element of iterable) {

    // kod bloğu

}
```

**iterable** nesnenin her biri sırasıyla element değişkeni içerisine kopyalanır.

**iterable** array, set, map, string olabilir.

**element** const, let ve var ile tanımlanabilir.

## For/Of Döngüsünün Dizi ile Kullanımı

For/Of döngüsü ile diziler üzerindeki tüm elemanlara kolaylıkla ulaşabiliriz.

Örnek:

```js
// array

const ogrenciler = ['Ali', 'Ahmet', 'Yasemin'];



for ( let ogrenci of ogrenciler ) {

    console.log(ogrenci);

}



// Ali

// Ahmet

// Yasemin
```

iterable bir nesne olan ogrenciler dizisi üzerindeki tüm elemanlar sırasıyla ogrenci değişkeni içerisine kopyalanır ve ekrana yazdırılır.

## For/Of Döngüsünün String ile Kullanımı

For/Of döngüsü ile string bir verideki tüm karakterlere kolaylıkla ulaşabiliriz.

Örnek:

```js
// string

const string = 'hey';



for (let i of string) {

    console.log(i);

}



// h

// e

// y
```

iterable bir nesne olan string verideki tüm karakterlere sırasıyla ulaşıp ekrana yazdırıyoruz.

## For/Of Döngüsünün Set ile Kullanımı

For/Of döngüsü ile javascript set nesnesi üzerindeki tüm elemanlara ulaşabiliriz.

\*\* set nesnesinde elemanlar tekrarlanmadan saklanır. Örneğin; iki tane 5 sayısı yerine tek 5 sayısı saklanır.

Örnek:

```js
const set = new Set([1, 2, 3]);

for (let i of set) {

    console.log(i);

}



// 1

// 2

// 3
```

## For/Of Döngüsünün Map ile Kullanımı

For/Of döngüsü ile javascript map nesnesi üzerindeki tüm elemanlara ulaşabiliriz.

\*\* map nesnesinde elemanlar key-value şeklinde saklanır. Örneğin; plaka ve şehir bilgisi.

```js
// boş bir map tanımlaması

let map = new Map();



// map nesnesine eleman ekleme

map.set('sehir', 'Kocaeli');

map.set('plaka', '41');



for (let [key, value] of map) {

    console.log(key + '- ' + value);

}



// sehir- kocaeli

// plaka- 41


```
