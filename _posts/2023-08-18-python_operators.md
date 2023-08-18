---
title: Python İşlemciler
author: sonsuz
date: 2023-08-18 16:29:23 +0300
categories: [Program,Python]
tags: [python,programlama,işlemci,operatör,işlem,mantıksal,atama]
---


## İşlemciler

Python'da işlemciler ile değişkenler ve sabitler üzerinde işlem yapılır. Python'da, aşağıda gösterilen 7 kategori içinde sınıflandırılan toplam 27 adet işlemci kullanılır.

* Aritmetik işlemciler: + - \* / % \*\* //
* Atama işlemcisi: =
* Karşılaştırma işlemcileri: == != > < >= <=
* Mantıksal işlemciler: and or not
* Tanımlama işlemcileri: is, is not
* Üyelik işlemcileri: in, not in
* Bit işlemcileri: & \| ^ ~ \<< \>>

Ayrıca, aritmetik işlemciler ile bit işlemcilerinin 5 tanesi (~ hariç) atama işlemcisi ile kullanılarak 12 adet ek işlemci oluşturulur.

## Aritmetik işlemciler

| Değişken sembolü | Değişken adı | Açıklama |
| --- | --- | --- |
| + | Toplama | Değişken ve sabitlerle toplama işlemi yapar. |
| - | Çıkarma | Değişken ve sabitlerle çıkarma işlemi yapar. |
| \* | Çarpma | Değişken ve sabitlerle çarpma işlemi yapar. |
| / | Bölme | Değişken ve sabitlerle bölme işlemi yapar. |
| % | Kalan (Modulus) işlemcisi | Bölme işleminde kalan değeri verir. |
| // | Bölüm işlemcisi | Bölme işleminde sonucun sadece tamsayı kısmını verir. |
| \*\* | Üs alma işlemcisi | Bir sayının üs değerini alma |

Şimdi, aritmetik işlemcilerin kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
deg1 = 84
deg2 = 21
deg3 = 42

# Toplama işlemleri
print(17+8) # Sabit değerleri toplama
print(deg1+deg2) # Değişken değerlerini toplama
deg3 = 57 + 75 # Sabit değer toplama işlemi sonucunu değişkene atama
print(deg3) # Değişken değerini yazdırma

print()

# Çıkarma işlemleri
print(17-8) # Sabit değerleri çıkarma
print(deg1-deg2) # Değişken değerlerini birbirinden çıkarma
deg3 = 121 - 65 # Sabit değer çıkarma işlemi sonucunu değişkene atama
print(deg3) # Değişken değerini yazdırma

print()

# Çarpma işlemleri
print(9*28) # Sabit değerleri çarpma
print(deg1*deg2) # Değişken değerlerini çarpma
deg3 = 8 * 16 # Sabit değer çarpma işlemi sonucunu değişkene atama
print(deg3) # Değişken değerini yazdırma

print()

# Bölme işlemleri
print(60/12) # Sabit değerleri bölme
print(deg1/deg2) # Değişken değerlerini bölme
deg3 = 17 / 5 # Sabit değer bölme işlemi sonucunu değişkene atama
print(deg3) # Değişken değerini yazdırma

print()

# Kalan işlemleri
print(63%12) # Sabit değer bölme işlemi sonucunda kalan değer
print(deg1%deg2) # Değişken değerlerini bölme işlemi sonucunda kalan değer
deg3 = 24 % 7 # Sabit değer bölme işlemi sonucunda kalan değeri değişkene atama
print(deg3) # Değişken değerini yazdırma

print()

# Bölüm işlemleri
print(60//12) # Sabit değerleri bölme işlemi sonucunun tamsayı bölümü
print(deg1//deg2) # Değişken değerlerini bölme işlemi sonucunun tamsayı bölümü
deg3 = 17 // 5 # Sabit değer bölme işlemi sonucunun tamsayı bölümünü değişkene atama
print(deg3) # Değişken değerini yazdırma

print()

# Üs alma işlemleri
print(5**4) # Sabit değerin 4.üs değerini alma
deg1 = 4
deg2 = 3
print(deg1**deg2) # Değişken değerinin üs değerin ialma
deg3 = 5**4 # Sabit değerin üs değerini değişkene atama
print(deg3) # Değişken değerini yazdırma


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

25
105
132

9
63
56

252
1764
128

5.0
4.0
3.4

3
0
3

5
4
3

625
64
625

```

## Atama işlemcisi

Python'da, atama işlemcisini bir değişkene sabit değer atamak için kulanabiliriz. Ayrıca, aritmetik işlemciler ile bit işlemcilerinin 5 tanesi (~ hariç) atama işlemcisi ile kullanarak 12 adet ek işlemci oluşturabiliriz.

Şimdi, atama işlemcisi ve atama işlemcisinin aritmetik ve bit işlemcileri ile kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
# Atama işlemcisinin tek başına kullanılması
deg1 = 21 # Atama işlemcisinin int veri türü ile kullanılması
deg2 = 15.47 # Atama işlemcisinin float veri türü ile kullanılması
deg3 = "Bilgisayar" # Atama işlemcisinin string veri türü ile kullanılması

print(deg1)
print(deg2)
print(deg3)

print()

# Atama işlemcisinin aritmetik işlemcilerle kullanılması
deg1 += 7 # Sabit bir değeri değişken değerine ekleyip sonucu değişkene atama
print(deg1) # 28

deg1 -= 10 # Değişken değerinden sabit bir değeri çıkarıp sonucu değişkene atama
print(deg1) # 18

deg1 *= 3 # Değişken değeri ile sabit bir değeri çarpıp sonucu değişkene atama
print(deg1) # 54

deg1 /= 2 # Değişken değerini sabit bir değere bölüp sonucu değişkene atama
print(deg1) # 27.0

deg1 %= 7 # Değişken değerinin sabit değere bölüm işleminde kalan değeri değişkene atama
print(deg1) # 6.0

deg1 //= 2 # Değişken değerinin sabit değere bölüm işlemi sonucunun tamsayı bölümünü değişkene atama
print(deg1) # 3.0

deg1 **= 4 # Değişken değerinin sabit değer kadar üs değerini değişkene atama
print(deg1) # 81.0

# Atama işlemcisinin bit işlemcileri ile kullanılması
deg1 = 81;
deg1 &= 21 # Değişken değeri ile sabit bir değere & (AND) işlemi yapıp sonucu değişkene atama
print(deg1) # 17 (81 = 1010001 21 = 0010101 sonuç = 17 = 0010001)

deg1 |= 45 # Değişken değeri ile sabit bir değere | (OR) işlemi yapıp sonucu değişkene atama
print(deg1) # 61 (17 = 010001 45 = 101101 sonuç = 61 = 111101)

deg1 ^= 42 # Değişken değeri ile sabit bir değere ^ (XOR) işlemi yapıp sonucu değişkene atama
print(deg1) # 23 (61 = 111101 42 = 101010 sonuç = 23 = 010111)

deg1 >>= 2 # Değişken değeri ile sabit bir değere >> işlemi yapıp sonucu değişkene atama
print(deg1) # 5 (23 = 010111 sonuç = 5 = 000101)

deg1 <<= 3 # Değişken değeri ile sabit bir değere << işlemi yapıp sonucu değişkene atama
print(deg1) # 40 (5 = 000101 sonuç = 40 = 101000)


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

21
15.47
Bilgisayar

28
18
54
27.0
6.0
3.0
81.0
17
61
23
5
40

```

## Karşılaştırma işlemcileri

Python'da kullanılan 6 adet karşılaştırma işlemcisi 2 değerin karşılaştırılması için kullanılır.

| Değişken sembolü | Değişken adı | Açıklama |
| --- | --- | --- |
| == | Eşitlik | Değişken ve/veya sabitlerden oluşan 2 adet değerin eşit olup olmadığını belirler. |
| != | Eşitsizlik | Değişken ve/veya sabitlerden oluşan 2 adet değerin farklı olup olmadığını belirler. |
| > | Büyüklük | Değişken ve/veya sabitlerden oluşan bir değerin diğerinden büyük olup olmadığını belirler. |
| < | Küçüklük | Değişken ve/veya sabitlerden oluşan bir değerin diğerinden küçük olup olmadığını belirler. |
| >= | Büyük ve eşitlik | Değişken ve/veya sabitlerden oluşan bir değerin diğerinden büyük veya eşit olup olmadığını belirler. |
| <= | Küçük ve eşitlik | Değişken ve/veya sabitlerden oluşan bir değerin diğerinden küçük veya eşit olup olmadığını belirler. |

Şimdi, karşılaştırma işlemcilerinin kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
deg1 = 21
deg2 = 15

# Eşitlik işlemcisinin (==) kullanılması
if(deg1==deg2):
   print("Değişken değerleri eşittir!")
else:
   print("Değişken değerleri farklıdır!")

# Eşitsizlik işlemcisinin (!=) kullanılması
if(deg1!=deg2):
   print("Değişken değerleri farklıdır!")
else:
   print("Değişken değerleri eşittir!")
   
# Büyüklük işlemcisinin (>) kullanılması
if(deg1>deg2):
   print("deg1 değişken değeri deg2 değişken değerinden büyüktür!")
else:
   print("deg1 değişken değeri deg2 değişken değerinden büyük değildir!")   
   
# Küçüklük işlemcisinin (<) kullanılması
if(deg1<deg2):
   print("deg1 değişken değeri deg2 değişken değerinden küçüktür!")
else:
   print("deg1 değişken değeri deg2 değişken değerinden küçük değildir!")   
   
# Büyük ve eşitlik işlemcisinin (>=) kullanılması
if(deg1>=deg2):
   print("deg1 değişken değeri deg2 değişken değerinden büyük veya eşittir!")
else:
   print("deg1 değişken değeri deg2 değişken değerinden büyük veya eşit değildir!")   
   
# Küçük ve eşitlik işlemcisinin (<=) kullanılması
if(deg1<=deg2):
   print("deg1 değişken değeri deg2 değişken değerinden küçük veya eşittir!")
else:
   print("deg1 değişken değeri deg2 değişken değerinden küçük veya eşit değildir!")  


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Değişken değerleri farklıdır!
Değişken değerleri farklıdır!
deg1 değişken değeri deg2 değişken değerinden büyüktür!
deg1 değişken değeri deg2 değişken değerinden küçük değildir!
deg1 değişken değeri deg2 değişken değerinden büyük veya eşittir!
deg1 değişken değeri deg2 değişken değerinden küçük veya eşit değildir!

```

## Mantıksal işlemciler

Python'da kullanılan 3 adet mantıksal işlemci, karşılaştırma işlemcileri ile yapılan iki veya daha fazla işlemin birlikte değerlendirilmesi için kullanılır.

Mantıksal işlemciler, karşılaştırma işlemcileri ile yapılan işlemlerde elde edilen True veya False değerlere işlem yaparlar.

| Değişken sembolü | Değişken adı | Açıklama |
| --- | --- | --- |
| and | Ve | Her iki ifade doğru ise doğru bir değer geri döndürür. |
| or | Veya | İki ifadeden sadece biri doğru ise doğru bir değer geri döndürür. |
| not | Değil | İfade sonucunun tersini geri döndürür. |

Şimdi, mantıksal işlemcilerin kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
deg1 = 21
deg2 = 15

# Ve işlemcisinin (and) kullanılması
print(deg1>deg2 and deg1<100)
if(deg1>deg2 and deg1<100):
   print("deg1 değişken değeri 0-100 arasındadır!")

# Veya işlemcisinin (or) kullanılması
print(deg1>0 or deg1>10)
if(deg1>0 or deg1>10):
   print("deg1 değişken değeri 0'dan veya 10'dan büyüktür!")
   
# Değil işlemcisinin (not) kullanılması
print(not(deg1>0 and deg1<100))


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

True
deg1 değişken değeri 1-100 arasındadır!
True
deg1 değişken değeri 0'dan veya 10'dan büyüktür!
False

```

## Tanımlama işlemcileri

Python'da, tanımlama işlemcileri nesneleri karşılaştırmak için kullanılır.

| Değişken sembolü | Değişken adı | Açıklama |
| --- | --- | --- |
| is | Aynı mı | Her iki değişken aynı nesne ise True bir değer geri döndürür. |
| is not | Aynı değil mi | Her iki değişken aynı nesne değil ise True bir değer geri döndürür. |

Şimdi, tanımlama işlemcilerin kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
nes1 = ["Bilgisayar", "Yazılım", "Programlama"]
nes2 = ["Bilgisayar", "Yazılım", "Programlama"]
nes3 = nes1

print(nes1 is nes3) # nes1 ve nes2 aynı nesne olduğundan True değeri verir. 

print(nes1 is nes2) # nes1 ve nes2 aynı nesne olmadığından False değeri verir (İçerikleri aynı olsa bile). 

print(nes1 is not nes3) # nes1 ve nes2 aynı nesne olduğundan False değeri verir. 

print(nes1 is not nes2) # nes1 ve nes2 aynı nesne olmadığından True değeri verir (İçerikleri aynı olsa bile). 


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

True
False
False
True

```

## Üyelik işlemcileri

Python'da, üyelik işlemcileri bir değerin bir nesne içinde bulunup bulunmadığını belirlemek için kullanılır.

| Değişken sembolü | Değişken adı | Açıklama |
| --- | --- | --- |
| in | İçinde mi | Bir değer bir nesne içinde varsa, True bir değer geri döndürür. |
| not in | İçinde değil mi | Bir değer bir nesne içinde yoksa, True bir değer geri döndürür. |

Şimdi, tanımlama işlemcilerin kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
nes = ["Bilgisayar", "Yazılım", "Programlama"]

print("Bilgisayar" in nes) # "Bilgisayar" karakter dizisi nes nesnesi içinde olduğundan True değeri verir. 

print("Yazılım" not in nes) # "Yazılım" karakter dizisi nes nesnesi içinde olduğundan False değeri verir. 


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

True
False

```

## Bit işlemcileri

Python'da, bit işlemcileri sayıları ikili sistem esasına göre değerlendirmek için kullanılır. İki sayının aynı basamakta yer alan karşılıklı değerleri işlem yapıldıktan sonra elde edilen ikili sistem değeri sonuç sayısının basamağına yazılır.

| Değişken sembolü | Değişken adı | Açıklama |
| --- | --- | --- |
| & | AND | Her iki sayıda karşılıklı bit değeri 1 ise, sonuç değerinin bit değerini 1 yapar. |
| \| | OR | Sayıların karşılıklı bit değerinin herhangi biri 1 ise, sonuç değerinin bit değerini 1 yapar. |
| ^ | XOR | Sayıların karşılıklı bit değerinden sadece birisi 1 ise, sonuç değerinin bit değerini 1 yapar. |
| ~ | NOT | Bir sayının bit değerlerinin tamamını tersine çevirir. |
| `<<` | Sola kaydırma | Bir sayının basamak bit değerlerini sola doğru kaydırır. |
| `>>` | Sağa kaydırma | Bir sayının basamak bit değerlerini sağa doğru kaydırır. |

`<<` işlemlerinde en soldan kaydırılan bit değerleri kaybolmaz, `>>` işlemlerinde ise en sağdan kaydırılan bit değerleri kaybolur.

Şimdi, bit işlemcilerinin kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
# & işlemcisinin kullanılması
deg = 81 & 21
print(deg) # 17 (81 = 1010001 21 = 0010101 sonuç = 17 = 0010001)

# | işlemcisinin kullanılması
deg = 17 | 45
print(deg) # 61 (17 = 010001 45 = 101101 sonuç = 61 = 111101)

# ^ işlemcisinin kullanılması
deg = 61 ^ 42
print(deg) # 23 (61 = 111101 42 = 101010 sonuç = 23 = 010111)

# ~ işlemcisinin kullanılması
deg = ~23
print(deg) # -24 (23 = 010111 sonuç = -24 = 11111111111111111111111111101000)

# << işlemcisinin kullanılması
deg = 138 << 3
print(deg) # 1104 (138 = 10001010 sonuç = 1104 = 10001010000)

# >> işlemcisinin kullanılması
deg = 175 >> 2
print(deg) # 43 (175 = 10101111 sonuç = 43 = 00101011)


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

17
61
23
-24
1104
43

```
