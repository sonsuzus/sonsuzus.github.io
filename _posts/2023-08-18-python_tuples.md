---
title: Python Tuples
author: sonsuz
date: 2023-08-18 18:51:30 +0300
categories: [Program,Python]
tags: [python,programlama,tuple,çokuz]
---



## Tuple

Tuple, birden fazla değerin yer aldığı bir yapıdır. Tuple içindeki verilerin aynı veri türünden olması gerekli değildir. Elemanlarda değişiklik yapılamaz.

Tuple oluşturmak için parantezler (( )) veya tuple() fonksiyonu kullanılır.

```py
tuple-adı = ("deger01", "deger02", "deger03") # ( ) ile tuple oluşturma

tuple-adı = tuple(("deger01", "deger02", "deger03")) # tuple() fonksiyonu ile tuple oluşturma


```

Tuple aşağıda gösterilen kurallara uygun olarak oluşturulur:

* Tuple, aynı veya farklı veri türünden elemanlardan oluşabilir.
* Tuple elemanları sıralıdır. Elemanların tanımlanma sırası değişmez.
* Tuple elemanları değiştirilemez, silinemez ve yeni eleman eklenemez.
* Tuple elemanları birbirinin aynı olabilir.
* Tuple elemanlarına 0'dan başlamak üzere endeksleme ile erişim sağlanır.

Şimdi, tuple oluşturulmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
# ( ) ile tuple oluşturma
tuple1 = ("aaa", "bbb", "ccc", "ddd")
tuple2 = (21, 35, 54, 82)

# tuple() fonksiyonu ile tuple oluşturma
tuple3 = tuple((7, 15, 24, 43))

# Tuple yazdırma
print(tuple1)
print(tuple2)
print(tuple3)


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

('aaa', 'bbb', 'ccc', 'ddd')
(21, 35, 54, 82)
(7, 15, 24, 43)

```

## Tuple elemanlarına erişim

Tuple elemanlarına birer birer erişmek için, [ ] işaretleri ile birlikte 0'dan başlayan endeks yöntemini kullanabiliriz. Bir sıra dahilindeki birden fazla liste elemanına erişim sağlamak için, [ ] işaretleri ile : işaretini kullanabiliriz.

Şimdi, liste elemanlarına erişim sağlama işlemini bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
tuple = ("aaa", "bbb", "ccc",  "ddd", "eee")

print(tuple[0])   # Tuple'ın ilk elemanını yazdırma 
print(tuple[1])   # Tuple'ın ikinci elemanını yazdırma 
print(tuple[-1])  # Tuple'ın son elemanını yazdırma 
print(tuple[-2])  # Tuple'ın sondan ikinci elemanını yazdırma 

print(tuple[:3])  # Tuple'ın 1.elemanından 4.elemanına kadar yazdırma
print(tuple[2:])  # Tuple'ın 3.elemanından itibaren yazdırma
print(tuple[1:4]) # Tuple'ın 2.elemanından 5.elemanına kadar yazdırma


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

aaa
bbb
eee
ddd
('aaa', 'bbb', 'ccc')
('ccc', 'ddd', 'eee')
('bbb', 'ccc', 'ddd')

```

## Tuple elemanlarının tamamına sırayla erişim

Bir tuple içindeki elemanlara sıra ile erişim sağlamak için döngüleri kullanabiliriz.

Şimdi, tuple elemanlarına sıra ile erişim sağlamak için döngü kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
tuple = ("aaa", "bbb", "ccc",  "ddd", "eee")

print(tuple) # Tuple'ı tek komutla yazdırma

# Tuple elemanlarını for döngüsüyle tek tek yazdırma
for deg in tuple:
    print(deg, end=' ')
	
print() # Satır aralığı verme	

# Tuple elemanlarını for döngüsü ve endeksleme yöntemiyle yazdırma	
len = len(tuple)
for deg in range(len):
  print(tuple[deg], end=' ')
  
print() # Satır aralığı verme  
  
# Tuple elemanlarını while döngüsü ve endeksleme yöntemiyle yazdırma	  
deg = 0
while deg < len:
  print(tuple[deg], end=' ')
  deg += 1  


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

('aaa', 'bbb', 'ccc', 'ddd', 'eee')
aaa bbb ccc ddd eee 
aaa bbb ccc ddd eee 
aaa bbb ccc ddd eee 

```

## Tuple birleştirme

İki tuple'ı birleştirmek için, + işlemcisini kullanabiliriz.

Şimdi, iki listeyi birleştirme işlemini bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (6, 7, 8, 9, 10)

# + işlemcisi ile tuple'ları birleştirme
tuple3 = tuple1 + tuple2
print(tuple3) 


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

```

## Tuple içindeki bir eleman değerinin endeksini ve sayısını alma

Bir tuple eleman değerinin endeksini almak için index() fonksiyonunu ve kaç adet olduğunu belirlemek için count() fonksiyonunu kullanabiliriz. Bu fonksiyonların genel yapısı aşağıda gösterilmektedir:

```py
liste-adı.index(eleman-değeri) 

liste-adı.count(eleman-değeri) 


```

Şimdi, bir tuple içindeki eleman değerinin endeksini almak ve kaç adet olduğunu belirlemek için yapılan işlemleri bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
tuple = (1, "aaa", 2, "bbb", 3, "ccc", 4, "ddd", 3)

# Elemanların endeksini alma
print(tuple.index("bbb"))
print(tuple.index(4))

# Tuple içinde kaç adet 3 değeri olduğunu belirleme
print(tuple.count(3))


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

3
6
2

```

## Tuple elemanlarını değişkenlere atama

Bir tuple içindeki eleman değerlerini değişkenlere atamak için aşağıda genel yapıyı kullanabiliriz:

```py
(degişken-adı1, degişken-adı2, ...) = tuple-adı 


```

Değişken sayısı ile tuple eleman sayısı aynı olmalıdır. Eğer değişken sayısı tuple eleman sayısından az tanımlanırsa, değişkenlerden bir tanesinin önüne mutlaka \* işareti konulmalıdır. Bu durumda, fazla olan tuple eleman değerleri adı \* ile başlayan değişkene liste olarak atanır.

Şimdi, tuple elemanlarının değişkenlere atanmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
tuple = ("aaa", "bbb", "ccc", "ddd", "eee")

# Tuple eleman sayısı kadar değişken tanımlama
(deg1, deg2, deg3, deg4, deg5) = tuple

print(deg1, end=' ')
print(deg2, end=' ')
print(deg3, end=' ')
print(deg4, end=' ')
print(deg5)

# Tuple eleman sayısı kadar değişken tanımlama
(deg6, deg7, *deg8) = tuple

print(deg6, end=' ')
print(deg7, end=' ')
print(deg8)


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

aaa bbb ccc ddd eee
aaa bbb ['ccc', 'ddd', 'eee']

```
