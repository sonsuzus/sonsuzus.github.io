---
title:  Python Yazım kuralları
author: sonsuz
date: 2023-08-18 15:51:39 +0300
categories: [Program,Python]
tags: [python,programlama,syntax,yazım]
---


Python'da, bir kod satırının başındaki boşluklar (indentation) bir kod bloğunu belirtmek için girinti kullanılır. Diğer programlama dillerinde bu boşluklar kodların daha düzenli bir şekilde yazılması ve kolayca anlaşılması için kullanılır.

Python'da kod satır başındaki boşluklar programın yapısını belirlediğinden, düzgün kullanılmadığı takdirde program hata verir.

Bir kod bloğu içinde yer alan tüm satırların başındaki boşluklar aynı olmalıdır.

Örnek

```py
deg1 = 21
deg2 = 17

if deg1>deg2:
   print("deg1 değişken deg2 değişken değerinden büyüktür!")

if deg1>deg2:
   print("deg1 değişken deg2 değişken değerinden büyüktür!")
   print("deg1 değişken deg2 değişken değerinden büyüktür!")


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

deg1 değişken deg2 değişken değerinden büyüktür!
deg1 değişken deg2 değişken değerinden büyüktür!
deg1 değişken deg2 değişken değerinden büyüktür!

```
