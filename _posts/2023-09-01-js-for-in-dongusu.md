---
title: Javascript For/In Döngüsü
author: sonsuz
date: 2023-09-01 16:13:46 +0300
categories: [Program,Javascript]
tags: [javascript,js,for,in,döngü,programlama]
---


## Javascript For/In Döngüsü Kullanımı

Javascript **for/in** döngüsü ile bir javascript nesnesinin tüm özelliklerine ulaşabiliriz. 

Kullanım şekli;

```js
for (key in nesne) {

   // çalıştırılacak kod blokları.

}
```

Nesne içerisindeki tüm key bilgilerine sırayla ulaşarak key 'e karşılık gelen value bilgisini alıyoruz.

Örnek:

```js
var user = { username:"sadikturan", name:"Sadık Turan", age:38 };

var x;

for (x in user) {

  console.log(user[x]);

}



// sadikturan

// Sadık Turan

// 38
```

* For in döngüsü ile user nesnesi üzerindeki her bir özelliğe ulaşabiliriz.
* Her döngü turunda user nesnesindeki key bilgilerine sırayla ulaşırız. (username, name, age)
* Ulaştığımız key bilgisiyle key' e karşılık gelen değer yani value bilgisini alabiliriz. (user[x] => user["username"], user["name"], user["age"])

## For/In Döngüsünün Diziler ile Kullanımı

Javascript for/in döngüsünü diziler üzerinde de kolaylıkla kullanabilirsiniz.

Kullanım şekli;

```js
for (index in array) {

  // kod satırları

}
```

Dizi içerisindeki tüm indeks bilgilerine sırayla ulaşarak indeks 'e karşılık gelen value bilgisini alıyoruz.

```js
var sayilar = [12, 40, 2];

var x;

for (x in sayilar) {

  console.log(sayilar[x]); 

}



// 12

// 40

// 2
```

* Gene aynı şekilde dizi elemanlarının indeks değerlerine (x => 0, 1, 2) teker teker ulaşırız.
* X değerlerine göre dizinin her bir değerini alabiliriz. (console.log(sayilar[x]) => sayilar[0], sayilar[1],sayilar[2])
* Key bilgilerini almak için console.log(x) yazabilirsiniz.

