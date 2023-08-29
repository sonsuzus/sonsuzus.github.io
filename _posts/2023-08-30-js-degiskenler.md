---
title: Javascript Değişkenler
author: sonsuz
date: 2023-08-30 00:00:30 +0300
categories: [Program,Javascript]
tags: [javascript,programlama,değişken]
---


Geçici olarak **veri saklamak** için oluşturduğumuz veri yapılarına **değişken** denir.

Örneğin bir öğrencinin not ortalamasını hesaplamak istediğimizde hesaplama işlemine gelmeden önce öğrencinin notlarını geçici olarak bir yerde saklamamız gerekir.

```js
var not1 = 50;

var not2 = 60;

var ortalama = (not1+not2)/2;
```

Burada bir değişken kullanıyoruz çünkü not bilgilerini her kullanıcı için tekrar tekrar alabiliriz ve değişken içerisinde hangi değer varsa ona göre bir hesaplama sonucu gelecektir.

## Javascript Değişken Tanımlama

Javascript de değişken tanımlamak için var ya da let komutu kullanılır. 

```js
var x = 10;

var y = 20;

var z = x + y;

var k;



consolo.log(x);  // 10

consolo.log(y);  // 20

consolo.log(z);  // 30

consolo.log(k);  // undefined
```

Tanımlamış olduğumuz **x**,**y**,**z** ve **k** değişkenleri **bellekte tanımlanan geçici alan**lardır. Uygulama her çalıştığında bellek üzerinde tanımlanan değerler silinir.

**k değişkenine** bir değer ataması yapmadığımızdan dolayı **undefined** değere sahip olur.

```js
var name;
```

Değişkenleri var komutuyla tanımladıktan sonra içlerine değer ataması yapıyoruz ve en sona **;** (noktalı virgül) eklememiz gerekiyor.

Örneğin;

```js
var name = "Çınar";
```

Değişkenlere karakter ataması (string) yaparken **tek tırnak** ya da **çift tırnak** kullanmamız gerekir.

```js
var name = "Çınar";

var surname = 'Turan';
```

Değişkenlere sayısal bir atama yaparken tırnak kullanmamamız gerekiyor. Aksi halde string bir değişken tanımlaması yapmış oluruz.

```js
var a = 50;   // sayısal olarak 50 değeri tanımladık

var b = "50"; // karakter (string) olarak 50 değeri tanımladık.

var toplam = a + b; // a + b' nin sonucu 5050 olur.
```

eğer ki; a + b' nin sonucunun 100 olmasını istiyorsak bu durumda b değişkenini de sayısal olarak tanımlamamız gerekiyor. Yani tırnak kullanmadan değişken tanımlamamız lazım.

```js
var a = 50; 

var b = 50;

var toplam = a + b; 
```

Bu durumda toplam değişkeninin içeriği 100 olur.

Değişken içerisinde var olan bir değeri yeni bir atamayla değiştirebiliriz.

```js
var x = 10; // x içinde 10 değeri var.

var y = 20; // y içinde 20 değeri var.

x = 30; // x içinde bulunan 10 değeri silinir ve 30 değeri aktarılır.


```

## Javascript Değişken Tanımlama Kuralları

Javascript' de değişken isimlerini seçerken bazı kurallara uymamız gerekiyor.

- Değişken isimleri rakam ile başlayamaz.

```js
 var 1yas; => hatalı

 var yas1; => geçerli

 var _yas; => geçerli
```

- Komut isimleriyle tanımlama yapılamaz.

Örneğin if ya da switch kelimesi değişken ismi olamaz.

- Büyük küçük harf duyarlılığı vardır.

```js
var firstName = 'Sadık';

var FirstName = 'Çınar';
```

Burada tanımlanan 2 farklı değişken vardır.

- Değişken isimlerinde türkçe karakter kullanmamalıyız. "ı" karakteri yerine "i" karakteri kullanmalıyız.

```js
var kullaniciAdi = "sadikturan";


```
