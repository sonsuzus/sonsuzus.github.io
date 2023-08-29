---
title: Python Lambda Fonksiyonu
author: sonsuz
date: 2023-08-29 13:38:02 +0300
categories: [Program,Python]
tags: [python,programlama,lambda,filter]
---



Pythonda lambda fonksiyonu nasıl tanımlanır ve hangi amaçla kullanılır? Map ve Filter metodu lambda fonksiyonlarında nasıl kullanılır?

## Pythonda Lambda Fonksiyonu

Pythonda isimsiz olarak tanımladığımız fonksiyonlara lambda fonksiyonları denir.

İlk olarak lambda fonksiyonları nasıl tanımlanır öğrenelim sonrasında neden python lambda fonksiyonlarına ihtiyaç duyarız görelim.

## Lambda Fonksiyonu Tanımlama

Square isminde normal bir fonksiyon tanımlayalım.

```py
def square(num): 

    return num ** 2



print(square(4)) # 16 
```

Kendisine gönderilen sayının karesini geriye gönderir.Peki aynı fonksiyonu lambda fonksiyonu olarak hazırlayalım.

```py
square =  lambda num: num ** 2

print(square(4)) # 16 
```

```py
a = lambda a, b, c : a + b + c

print(a(2, 3, 4))
```

Kendisine gönderilen 3 sayıyı toplayan bir lambda fonksiyonu.

## Lambda Fonksiyonu Neden Kullanılır?

Lambda fonksiyonu bir başka fonksiyon içinde kullanıldığında anlam kazanır.

Örneğin bir sayının karesini mi kübünü mü almak istediğinizden emin değilsiniz bu durumda bir fonksiyon içerisinde lambda tanımlaması yaparak istediğimiz bir aşamada geriye çalıştırılabilir bir fonksiyon döndürebilirsiniz.

```py
def math(n):

  return lambda a : a ** n



square = math(2)

cube = math(3)



print(square(3)) # 8

print(cube(3))    # 27
```

## Python Map Fonksiyonu

Pythonda map fonksiyonu aracılığıyla referansı belirtilen bir fonksiyona belirtilen bir listenin tüm elemanları sırayla gönderilip liste üzerinde istenilen yapılandırılma yapılır.

```py
numbers = [1,3,5,9,10,4]



def square(num): 

       return num ** 2



result = list(map(square, numbers)) # [1,9,25,81,100,16]
```

Gördüğünüz gibi map metoduna hazırladığımız fonksiyonun sadece ismini veriyoruz (referans) ve ikinci parametre olarak sayı listesi veriyoruz ve liste üzerindeki her eleman sırasıyla square metoduna gönderililip bir map objesi oluşturuluyor ve son olarak list ile objeyi sayı listesine çeviriyoruz.

Peki sadece kendisine gelen sayının karesini alan bir fonksiyonu dışarıda tanımlamaya gerek var mı ? eğer ki square metodu sadece bir kere kullanılacaksa bence hiç gerek yok bu işlemi daha kısa şekilde yapabiliriz.

```py
numbers = [1,3,5,9,10,4]

result = list(map(lambda num: num ** 2, numbers)) # [1,9,25,81,100,16]


```

Gene aynı şekilde listedeki her sayının karesi bir liste içerisinde geri gelir. Bir fonksiyon referansı vermek yerine bir lambda fonksiyonu tanımladık.

## Python Filter Fonksiyonu

Map fonksiyonunda liste içerisindeki her bir sayı fonksiyona gönderilip bir işlem görüyor ve geriye gönderiliyor ancak filter metodu ile geriye dönecek sayılara bir filtre uygulayabiliriz.

```py
numbers = [1,3,5,9,10,4]

result = list(filter(lambda num: num%2==0,numbers)) # [10,4]
```

Listedeki her bir sayı check\_even metoduna gönderilir ve hangi sayı True değer döndürüyorsa ki çift olanlar True döndürür bu durumda o sayı geri dönecek listenin bir elemanı oluyor. Yani gönderdiğimiz listedeki çift sayıları almış oluyoruz.

Peki tek bir sayının çift olup olmadığına bakarsak ?

```py
check_even = lambda num: num%2==0

result = check_even(numbers[2])

print(result) # False
```

numbers[2], 5 rakamına karşılık gelen tek sayı olduğundan False değer döner ki; False bilgisini gören filter fonksiyonu bu değeri listeden çıkarır.
