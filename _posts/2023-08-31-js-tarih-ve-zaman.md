---
title: Javascript Tarih ve Zaman
author: sonsuz
date: 2023-08-31 23:29:45 +0300
categories: [Program,Javascript]
tags: [javascript,js,programlama,tarih,zaman,fonksiyon]
---

 


## Js Tarih ve Zaman kullanımı

**Javascript date** nesnesi ile tarayıcının o anki tarih ve saat bilgisini alabiliriz.

```js
var dt = new Date();

console.log(dt); // **Fri Jan 03 2020 10:35:38 GMT+0300 (GMT+03:00)**
```

Sayfayı ziyaret ettiğimizde **Javascript date** objesi bize tam olarak o anki tarih ve saat bilgisini verir.  

**Javascript date** objesinin bize getirdiği bir çok avantaj var. Örneğin; tarih objesinin üstüne belirli bir zamanı ekleyebiliriz ya da tüm tarih bilgisi yerine sadece yıl bilgisini ya da sadece saat bilgisini de alabiliriz.

## Javascript Tarih Nesnesi Tanımlama

**new Date()** dediğimizde bize tarayıcının o anki zaman bilgisi gelir ancak **javascript date** objesini belirli bir zamanı gösterecek şekilde de üretebiliriz. 

**Javascript date** objesini farklı parametre türleri ile tanımlayabiliriz. Date()' e vereceğiniz parametre,

* **String** bir bilgi olabilir. **8/24/2010 14:50:10**
* Yıl,ay,gün,saat,dakika,saniye,salise şeklinde **7 sayısal parametre** olabilir. **2010,7,24,14,50,10,123**
* 7 parametrenin hepsini vermemiz gerekmez. Sadece yıl, ay ve gün bilgisi de verebiliriz.

```js
var dtA = new Date('8/24/2010 14:50:10');

var dtB = new Date(2010,7,24,14,50,10)



console.log(dtA); // Tue Aug 24 2010 14:50:10 GMT+0300 (GMT+03:00)

console.log(dtB); // Tue Aug 24 2010 14:50:10 GMT+0300 (GMT+03:00)
```

Gördüğünüz gibi 2 farklı şekilde **javascript date** objesini türettik peki **javascript date** objeleri ile nasıl çalışabiliriz?

## Javascript Date Objesinden Bilgi Alma

Türetilen bir **javascript date** objesi içinden istediğimiz bir bilgiyi alabiliriz. Kullanabileceğimiz metotlar;

```js
var dt = new Date();
```

|  |  |  |  |
| --- | --- | --- | --- |
| **Method** | **Açıklama** | **Örnek** |  |
| **getFullYear()** | Yıl bilgisini alır. (yyyy) | dt.getFullYear() | 2020 |
| **getMonth()** | Ay bilgisini 0 ile 11 arasında rakam şeklinde getirir. 0: Ocak 11: Aralık | dt.getMonth()      | 0 |
| **getDate()** | Gün bilgisini 1 ile 31 arasında rakam şeklinde getirir. | dt.getDate()     | 24 |
| **getHours()** | Saat bilgisini 0 ile 23 arasında getirir. | dt.getHours()      | 14 |
| **getMinutes(**) | Dakika bilgisini 0 ile 59 arasında getirir. | dt.getMinutes()  | 50 |
| **getSeconds()** | Saniye bilgisini 0 ile 59 arasında getirir. | dt.getSeconds() | 10 |
| **getMilliseconds()** | Salise bilgisini 0 ile 999 arasında getirir. | dt.getMilliseconds()  | 125 |
| **getTime()** | Zaman bilgisini 1-1-1970 tarihinden itibaren salise cinsinden getirir. | dt.getTime() | 1578039816947 |
| **getDay()** | Haftanın kaçıncı gününde (0-6) olduğumuzu verir. 0.gün Pazar | dt.getDay() | 5 |
| **Date.now()** | Şimdiki zaman bilgisini verir. |  |  |

> **Javascript date** objesi **1-1-1970** tarihini başlangıç olarak kabul eder. Yani **new Date()** diyerek tanımladığınız bir **javascript date** objesi içerisinde bulunan o anki tarih bilgisi aslında 1-1-1970 tarihinden o ana kadar olan zamanın **salise (miliseconds)**cinsinden karşılığıdır.
{: .prompt-tip }

Örneğin; 1/1/2020 tarihi ile bir **javascript date** objesi tanımladığınızda **1/1/2020** - **1/1/1970** arasında olan **toplam miliseconds** cinsinden veri türetmiş oluyorsunuz. Farkı temsil edecek olan **miliseconds** türündeki veriyi istediğimiz bilgiye çevirebiliriz. Örneğin yıl, ay, gün.

## Javascript Date Objesini Güncelleme

Türetilen bir **javascript date** objesinin istediğimiz bir parçasını güncellebiliriz. 

```js
var dt = new Date();
```

|  |  |  |
| --- | --- | --- |
| **Method** | **Açıklama** | **Örnek** |
| **setDate()** | Gün bilgisini günceller. (1-31) | dt.setDate(5) |
| **setFullYear()** | Yıl bilgisini günceller.  | dt.setFullYear(2019)      |
| **setHours()** | Saat bilgisini günceller. | dt.setHours(15)     |
| **setMilliseconds()** | Salise bilgisini günceller. | dt.setMilliseconds(1378039816947)      |
| **setMinutes()** | Dakika bilgisini günceller. | dt.setMinutes(20)  |
| **setMonth()** | Ay bilgisini günceller. | dt.setMonth(5) |
| **setSeconds()** | Saniye bilgisini günceller. | dt.setSeconds(30)  |
| **setTime()** | Zaman bilgisini 1-1-1970 tarihinden itibaren salise cinsinden günceller. | dt.setTime() |

Peki tablodaki set metotları ile **javascipt date** objesi içindeki her hangi bir zaman ve tarih bilgisini güncelleyebiliyoruz. Peki bir güncelleme yapmak yerine bilgi ekleyemez miyiz ? Örneğin bugünü gösteren bir **javascript date** objesi üzerine 10 gün eklemek ya da 2 yıl çıkarmak gibi.

```js
var dt = new Date();

console.log(dt);

console.log(dt.getMonth()+1);

console.log(dt.getFullYear()-2);
```

Gördüğünüz gibi 1 ay sonrasına ya da 2 yıl öncesini gösteren tarih objelerini türetebiliriz. Bu sayede 2 tarih arasını gösteren yeni bir javascript date objesi türetmemiz kolaylaşır ve türetilen objeden istediğimiz bilgiyi de get metotları ile alabiliriz.

1/1/1990 tarihinden bir gün öncesini gösteriniz.

```js
var dtC = new Date('1/1/1990');

var dayOfMonth = dtC.getDate();

dtC.setDate(dayOfMonth-1);

console.log(dtC);
```

## İki Tarih Arasındaki Süreyi Hesaplama

İki tarih arasındaki fark bilgisi bize miliseconds cinsinde değer getirir ve miliseconds değerini istediğimiz bilgiye çevirebiliriz. 

\*\* Javascript date objesi 1/1/1970 tarihinden itibaren miliseconds türünden bilgi tutar.

```js
var start = new Date('1/1/1990');

var end = new Date('2/10/1992');



var milisecond = end - start;

var saniye = milisecond / 1000;

var dakika = saniye / 60;

var saat = dakika / 60;

var gun = saat / 24;



console.log('milisecond :'+milisecond)

console.log('saniye : '+ saniye);

console.log('dakika :'+ dakika);

console.log('saat :' + saat);

console.log('gun : '+gun);
```

Yaş hesaplama uygulaması yapalım.

```js
var birthday = new Date('8/1/1985');

var ageDifMs = Date.now() - birthday.getTime();

var ageDate = new Date(ageDifMs);


console.log(ageDate.getFullYear() - 1970);

```

İlk olarak birthday isminde bir **javascript date** objesi türetelim. Date objesinin 1970 yılından itibaren salise cinsinden bilgi tuttuğunu zaten biliyorum. Dolayısıyla şimdiki zamanı tutan salise cinsinden veri ile birthday objesinin tuttuğu bilgi salise bilgisinin farkını alalım ve çıkan salise ile yeni bir **javascript date** objesi tanımlayalım ve içerisinde 1970 bilgisini çıkaralım. Bize kullanıcının yaş bilgisi gelir.

Her yıl mayıs ayının **2.haftası pazar günü** kutlanan anneler günü 2019 yılında ne zaman kutlanacaktır ?

```js
var annelerGunu = new Date();

annelerGunu.setHours(0,0,0,0);

annelerGunu.setFullYear(2019);

annelerGunu.setDate(1);

annelerGunu.setMonth(4);



while(annelerGunu.getDay() != 0){

    annelerGunu.setDate(annelerGunu.getDate()+1)

}



annelerGunu.setDate(annelerGunu.getDate()+7);

console.log(annelerGunu);

```
