---
title: Python Sayılar
author: sonsuz
date: 2023-08-18 16:13:00 +0300
categories: [Program,Python]
tags: [python,programlama,sayılar]
---



## Sayılar

Python'da int, float ve complex olmak üzere üç farklı sayı verisi kullanılmaktadır. Ayrıca, 0 ve 1 değeri alabilen bool verisi de bu kapsamda değerlendirilebilir.

Bir değişkene sayısal bir sabit değer atadığımızda, değişken veri türü tanımlanarak oluşturulur.

Şimdi, değişkenlere sabit sayısal değerler atayarak, sayısal değişkenlerin tanımlanmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
# int sayı
deg = 21 
print(deg, "değişkeninin veri türü:", type(deg))

# float sayı
deg = 35.75 
print(deg, "değişkeninin veri türü:", type(deg))

# complex sayı
deg = 1+2j 
print(deg, "değişkeninin veri türü:", type(deg))

# bool veri türü
deg = True 
print(deg, "değişkeninin veri türü:", type(deg))


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

21 değişkeninin veri türü: <class 'int'>
35.75 değişkeninin veri türü: <class 'float'>
(1+2j) değişkeninin veri türü: <class 'complex'>
True değişkeninin veri türü: <class 'bool'>

```

Program, deg adlı değişkene sırasıyla int, float, complex ve bool değerler atayarak, değişken değerini ve değişken veri türünü ekrana yazar. Değişkenin veri türünü yazarken type() fonksiyonunu kullanır.

## int sayılar

Python'da, int sayılar pozitif veya negatif tamsayıları temsil eder. Sayıların basamak sayısı ile ilgili bir sınırlama yoktur.

Şimdi, int sayıların kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
deg = 21 
print(deg)

deg = 176235489753
print(deg)

deg = -9123658745296524
print(deg)


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

21
176235489753
-9123658745296524

```

## float sayılar

Python'da, float sayılar pozitif veya negatif ondalık sayıları temsil eder. Sayıların basamak sayısı ile ilgili bir sınırlama yoktur.

Şimdi, float sayıların kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
deg = 21.75 
print(deg)

deg = 176.354
print(deg)

deg = -512.87
print(deg)


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

21.75
176.354
-512.87

```

## complex sayılar

Python'da, complex sayılar karmaşık sayıları temsil eder. Karmaşık sayılar, gerçel ve sanal sayılardan oluşur. Karmaşık bir sayının içinde hem gerçel sayı ve hem de sanal sayı vardır. Sanal kısımda j ile ifade edilen bir değer yer alır.

Şimdi, complex sayıların kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
deg = 2+3j 
print(deg)

deg = 3-4j
print(deg)

deg = -3-3j
print(deg)

deg = -5+2j
print(deg)


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

(2+3j)
(3-4j)
(-3-3j)
(-5+2j)

```

## bool veri türü

Python'da bool veri türü True ve False olmak üzere iki adet değer içerir.

Değişken, sabit ve işlemcilerden oluşan ifade sonuçları True veya False olarak alınan bool veri türü ile değerlendirilir.

Şimdi, bool veri türünün kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
# Sabit değer ve işlemci kullanımı
print(21>14)
print(21<14)

# Değişken, sabit değer ve işlemci kullanımı
deg = 21 
print(deg>7)
print(deg<7)

# Koşula bağlı değerlendirme
if(deg>7) print("Değişken değeri 7 sayısından büyüktür!")


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

True
False
True
False
Değişken değeri 7 sayısından büyüktür!

```

Program, sadece sabit değer ve işlemcinin kullanıldığı ilk iki satırda, 21>14 ifadesi doğru sonuç verdiği için ekrana True değerini, 21<14 ifadesi yanlış sonuç verdiği için False değerini, değişken, sabit değer ve işlemcinin kullanıldığı sonraki iki satırda deg>14 ifadesi doğru sonuç verdiği için ekrana True değerini, deg<14 ifadesi yanlış sonuç verdiği için False değerini ekrana yazar. Son satırda ise, deg>7 ifadesi doğru sonuç verdiği için karakter dizisini ekrana yazar.

Fonksiyonlar bool değer geri döndürebilir.

Şimdi, bool veri türünün fonksiyonlar tarafından geri döndürülmesini bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
def ispositive(deg):
    if(deg>0): 
      return True
    else:
      return False

deg = ispositive(21)
print(deg)

deg = ispositive(-21)
print(deg)


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

True
False

```

Program, sadece sabit değer ve işlemcinin kullanıldığı ilk iki satırda, 21>14 ifadesi doğru sonuç verdiği için ekrana True değerini, 21<14 ifadesi yanlış sonuç verdiği için False değerini, değişken, sabit değer ve işlemcinin kullanıldığı sonraki iki satırda deg>14 ifadesi doğru sonuç verdiği için ekrana True değerini, deg<14 ifadesi yanlış sonuç verdiği için False değerini ekrana yazar. Son satırda ise, deg>7 ifadesi doğru sonuç verdiği için karakter dizisini ekrana yazar.

## Sayısal değerlerin veri türünü geçici olarak değiştirme (casting)

Bir değişkene değer atarken, atanacak değerin veri türünü geçici olarak değiştirerek değişkenin veri türünü belirleyebiliriz. Bu amaçla, int(), float() ve complex() fonksiyonlarını kullanabiliriz. Bu özelliği bir örnek üzerinde incelemeye çalışalım

Örnek

```py
deg1 = 21     # değişken veri türü int olarak belirlenir.   
deg2 = 174.25 # değişken veri türü float olarak belirlenir.
deg3 = 2+3j   # değişken veri türü complex olarak belirlenir. 

deg4 = float(deg1)   # deg4 değişken veri türü float olarak belirlenir.
deg5 = complex(deg1) # deg5 değişken veri türü complex olarak belirlenir.
deg6 = int(deg2)     # deg6 değişken veri türü int olarak belirlenir.

print(deg1, type(deg1))
print(deg2, type(deg2))
print(deg3, type(deg3))
print(deg4, type(deg4))
print(deg5, type(deg5))
print(deg6, type(deg6))


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

21 
174.25 
(2+3j) 
21.0 
(21+0j) 
174 

```

Program, deg1 adlı değişkene 21 değerini atayarak değişkeninin veri türünü int olarak, deg2 adlı değişkene 174.25 değerini atayarak değişkeninin veri türünü float olarak ve deg3 adlı değişkene 2+3j değerini atayarak değişkeninin veri türünü complex olarak belirler. deg4 değişkenine deg1 değişken değerini ilk değer atarken float() fonksiyonunu kullandığından, deg4 değişken veri türü float olarak belirlenir. deg5 değişkenine deg1 değişken değerini ilk değer atarken complex() fonksiyonunu kullandığından, deg5 değişken veri türü complex olarak belirlenir. deg6 değişkenine deg2 değişken değerini ilk değer atarken int() fonksiyonunu kullandığından, deg6 değişken veri türü int olarak belirlenir.

deg1, deg2 ve deg3 değişkenlerinin veri türleri int(), float() ve complex() fonksiyonları ile geçici olarak değiştirildiğinden, değişken veri türleri aynı kalır.
