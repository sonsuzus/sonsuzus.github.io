---
title: Javascript Operatörler
author: sonsuz
date: 2023-08-30 20:49:15 +0300
categories: [Program,Javascript]
tags: [javascript,programlama,operatör]
---




**Javascript Operatörler**i aritmetik operatörler, atama operatörleri, karşılaştırma operatörleri ve mantıksal operatörler olmak üzere 4 grup altında ele alabiliriz.

## Aritmetik Operatörler

Javascript' de matematiksel işlemleri yapmak için **aritmetik operatörler** kullanılır.

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | x = 20; y = 5; | sonuc |
| + | Toplama | sonuc = x + y | 25 |
| - | Çıkarma | sonuc = x - y | 15 |
| \* | Çarpma | sonuc = x \* y; | 100 |
| / | Bölme | sonuc = x / y; | 4 |
| % | Mod Alma | sonuc = y % x; | 0 |
| ++ | Arttırma | sonuc = x++; | 21 |
| -- | Eksiltme | sonuc = x--; | 19 |
| \*\* | Üs alma | sonuc = 2 \*\* 3; | 8 |

### Toplama Operatörü (+)

```js
var x = 100 + 50;
```

Toplama operatörüne göre 100 ve 50 sayısı toplanır ve sonuç soldaki x değişkeni içerisine aktarılır.

### Çıkarma Operatörü (-)

```js
var a = 5;

var x = (100 + 50) - a;
```

Parantez içindeki 100 + 50 işleminden sonra a değişkeni 150 'den çıkartılır ve sonuç 145 olur.

### Çarpma Operatörü (\*)

```js
var x = 5;

var y = 3;

var z = (x + y) * (y - x);
```

Parantez içlerindeki (x+y)' nin değeri 8 ile (y-x)' nin değeri -2 çarpılır ve sonuç z değişkenine -16 olarak eşitlenir.

### Bölme Operatörü (/)

```js
var x = 5;

var y = 2;

var z = (x * y) / y;
```

Parantez içindeki (x\*y)' nin değeri 10 sayısı y' nin değeri olan 2' e bölünür ve sonuç 5 olarak z değişkenine aktarılır.

### Mod Alma Operatörü (%)

```js
var x = 1001;

var y = 2;

var z = x % y;
```

x değişkeninin değeri olan 1001 sayısının 2' e kalansız bölümünden elde edilen sayı 1' dir. 

### Arttırma Operatörü (++)

```js
x = 10;

y = x++;
```

x' değişkeninin değerini 1 arttırıp y değişkenine eşitliyoruz. Aynı işlemi aşağıdaki şekilde yapabilirsiniz.

```js
x = 10; 

y = x + 1;
```

### Azaltma Operatörü (--)

```js
x = 10;

y = x--;
```

x' değişkeninin değerini 1 azaltıp y değişkenine eşitliyoruz. Aynı işlemi aşağıdaki şekilde yapabilirsiniz.

```js
x = 10; 

y = x - 1;
```

### Üs Alma Operatörü (\*\*)

```js
var x = 5;

var z = x ** 2;    
```

x değişkeninin değeri olan 5' in 2 sayısı ile üssünü almış oluyoruz. Dolayısıyla 5' in yan yana 2 kere çarpımı 25 sonucunu verir.

##  Atama Operatörleri

**Javascript** 'de değişkenlere değer ataması yapabilmek için **atama operatörleri** kullanılır.

|  |  |  |
| --- | --- | --- |
| Operatör | Kısa kullanım | Uzun kullanım |
| = | x = y | x = y |
| += | x += y | x = x + y |
| -= | x -= y | x = x - y |
| \*= | x \*= y | x = x \* y |
| /= | x /= y | x = x / y |
| %= | x %= y  | x = x % y |
| \*\*= | x \*\*= y | x = x \*\* y |

```js
var x = 4;

x *= 5;
```

x değişkeni ile 5 değeri çarp ve sonucu x değişkenine eşitle yani sonuç 4 \* 5 'den 20 olur.

```js
var x = 2;

var y = 4;

x **= y;
```

işleminin uzun kullanımına göre x = x \*\* y; olmalıdır. Yani x 'in y kadar yan yana çarpımından gelen sonuç 2' nin yan yana 4 kere çarpımı olan 16 sayısıdır. 

## Karşılaştırma Operatörleri

**Javascript** 'de değerleri karşılaştırmak için (büyüklük, küçüklük, eşitlik vb.) **karşılaştırma operatörleri** kullanılır.

|  |  |  |  |
| --- | --- | --- | --- |
| Operatör | Açıklama | Kullanım | Sonuç |
| == | eşit mi ? | 10 == 10 | true |
| | | 5 == 4 | false |
| | | x = 5; y = 5; x == y | true |
| === | tip ve değer eşit mi ? | 5 === 5 | true |
| |  | 10 === '10' | false |
| != | eşit değil mi? | 10 != 9 | true |
| | | 10 != 10 | false |
| > | Büyük mü ? | 10 > 5 | true |
| < | Küçük mü ? | 10 < 5 | false |
| >= | Büyük eşit mi ? | 5 >= 5 | true |
| <= | Küçük eşit mi ? | 5 <= 5 | true |

Doğum yılına göre yaşı 18 ve üstü alan bir kişi ehliyet alabilir. Dolayısıyla yaşını hesapladığımız bir kişinin ehliyet alıp alamayacağını (>=) büyük eşit operatörü ile kontrol edebiliriz.

```js
var dogumYili = 1999;

var yas = 2020 - dogumYili;

var ehliyet = (yas >= 18)
```

ehliyet değişkeninin değeri true olacağından dolayı kişi ehliyet alabilir. Çünkü (2020 - 1999) bize 21 yaşını verir ve (21>=18) karşılaştırması bize true değerini döndürür.

## Mantıksal Operatörler

**Javascript** 'de birden fazla koşul ifadesini aynı anda değerlendirmek için javascript ***mantıksal operatörlerini*** kullanırız.

3 tane javascript mantıksal operatör türü vardır. Bunlar; `and (&&)`, `or (||)` ve `değil (!)` operatörleridir.

Örneğin a değişkeninin 0' dan büyük ayrıca 100' den küçük olma durumu için oluşturmamız gereken (a>0) koşulu ile (a<100) koşulunu aynı anda değerlendirmek için koşulları javascript mantıksal operatörü ile birleştirmemiz gerekiyor.

|  |  |  |  |
| --- | --- | --- | --- |
| Operatör | Açıklama | Kullanım | Sonuç |
| && | and operatörü | (8 < 10) && (6 > 5) | true |
| \|\| | or operatörü | (5 == 5) || (6 == 5) | true |
| ! | değil operatörü | !(5 == 5) | false |

## Mantıksal And (&&) Operatörü

Javascript mantıksal and operatörü ile birden fazla koşulun her birinin true döndürmesiyle sonuç true olur. En az bir koşulun false olması sonucu false yapar.

```js
x = 5;

y = 10;

z = 5;

result = (x>y) && (x>=z)
```

(x>y) sonucu false olduğundan dolayı diğer ifadelerin ne döndürdüğü önemli değil çünkü ifadede tek bir koşulun false dönmesi sonucu false yapar.

```js
yas = 20

egitim = 'lise'

result = (yas > 18) && (egitim=='lise')
```

yas 18' den büyük ve egitim lise olduğundan dolayı ehliyet alabilir. Yani her koşul bize true döndürüyor.

## Mantıksal Or (\|\|) Operatörü

Javascript mantıksal or operatörü ile birden fazla koşulun en az birinin true döndürmesiyle sonuç true olur. Sonucun false olması için her koşulun false olması gerekiyor.

Bir öğrencinin dönem sonu ortalaması en az 50 ya da final notu dönem sonu ortalamasına bakılmaksızın en az 80 ise geçer diyorsak bu durumda or operatörü kullanmamız gerekir.

```js
ortalama = 40

final= 80

result = (ortalama > 50) || (final>=80) 


```

## Mantıksal Değil (!) Operatörü

Javascript mantıksal değil operatörü ile koşulun tersini almak için kullanılır. Örneğin (10>5) ifadesi true değeri döndürürken eğer !(10>5) ifadesinin değilini alırsak bu durumda false değeri döndürür.
