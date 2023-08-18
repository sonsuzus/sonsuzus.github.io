---
title: Python Tanımlayıcılar
author: sonsuz
date: 2023-08-18 16:11:03 +0300
categories: [Program,Python]
tags: [python,programlama,tanımlayıcı]
---


Tanımlayıcılar, değişken, fonksiyon, sınıf veya nesne tanımlamak için kullanılır.

Tanımlayıcılar içini aşağıdaki kurallar geçerlidir:

* Tanımlayıcılarda sadece harf, rakam ve alt çizgi karakteri (\_) kullanılabilir.
* Python'da kullanılan ifadeler harf duyarlı olduğundan, tanımlayıcılarda büyük ve küçük harfler farklı kabul edilir (Deg ve deg ifadeleri farklıdır).
* Anahtar kelimeler tanımlayıcılarda kullanılmaz.
* Tanımlayıcıların ilk karakteri rakam olamaz.

Şimdi, bu özellikleri bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
deg1 = 21  # deg1 veri türü int olur. 
deg_2 = 36 # _ karakteri kullanımı
deg3 = 17  # Alttaki değişken ile tamamen farklıdır.
Deg3 = 25  # Yukarıdaki değişken ile tamamen farklıdır.

# for = 42 anahtar kelime olduğundan hata verir.
# 1deg = 75 Rakam ile başladığından hata verir.

print(deg1)
print(deg_2)
print(deg3)
print(Deg3)


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

21
36
17
25

```
