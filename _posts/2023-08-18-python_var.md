---
title: Python Değişkenler
author: sonsuz
date: 2023-08-18 15:56:33 +0300
categories: [Program,Python]
tags: [python,programlama,değişken]
---



## Değişken tanımlama

Python'da değişken farklı türdeki verileri yerleştirmek için kullanılan bellek bölgesidir.

Python'da bir değişkene ilk değer atanırken değişken adından önce herhangi bir veri türü tanımlaması yapılmaz. Değişkene atanan değerin veri türüne bağlı olarak, değişkenin veri türü otomatik olarak belirlenir.

Bir değişken oluşturmak için, değişken adını tanımlamak ve tanımlarken değişkene değişkenin veri türünü belirleyecek olan bir veri atamak gerekir. Belirli bir veri türünden değişken tanımladıktan sonra, aynı değişkene farklı veri türünden bir değer atadığımızda, değişken veri türü otomatik olarak yeni atanan verinin türüne dönüşür.

Değişken adı aşağıdaki kurallara uygun olarak verilmelidir:

* Sadece harf, rakam ve alt çizgi karakteri (\_) kullanılabilir.
* İlk karakteri rakam olamaz.
* Büyük ve küçük harfler farklı kabul edilir (Deg ve deg ifadeleri farklıdır).

Değişken tanımlama işlemini bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
deg = 35 # deg veri türü int olur. 
print(deg)

deg = 'Murat' # deg veri türü string olur.
print(deg)

deg = 457.25 # deg veri türü float olur.
print(deg)


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

35
Murat
457.25

```

Programda, deg değişkenine ilk olarak bir tamsayı değer atandığından değişken veri türü int olarak belirlenir. İkinci safhada, string bir sabit atandığından deg değişkeninin veri türü string olarak, üçüncü safhada ondalık bir sayı atandığından deg değişken veri türü float olarak belirlenir.

## Tek değişkene değer atama

Python'da bir satırda tek bir değişkene ilk değer atanırken, değişkene atanan değerin veri türüne bağlı olarak, değişkenin veri türü otomatik olarak belirlenir. Tek değişken değer atama işlemini bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
deg1 = 21      # deg1 veri türü int olur. 
deg2 = 'Nedim' # deg2 veri türü string olur.
deg3 = 1725.42 # deg3 veri türü float olur.

print(deg1)
print(deg2)
print(deg3)


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

21
Nedim
1725.42

```

Program, deg1 değişkenine bir tamsayı değer atandığından, deg1 değişkeninin veri türü otomatik olarak int, deg2 değişkenine bir karakter dizisi atadığından deg2 değişken veri türü string ve deg3 değişkenine kayan noktalı bir sayı atandığıdan deg3 değişken veri türü float olarak belirlenir.

## Birden fazla değişkene değer atama

Python'da birden fazla değişkene tek bir komutla ilk değer atayabiliriz.

Aşağıdaki komut satırları ile, deg1, deg2 ve deg3 değişkenlerine bir tamsayı değer atandığından, değişkenlerin veri türü otomatik olarak int olarak belirlenir.

Örnek

```py
deg1 = deg2 = deg3 = 21

print(deg1)
print(deg2)
print(deg3)


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

21
21
21

```

Eğer aynı komut satırında birden fazla değişkene tek bir komutla farklı değer atamak istersek aşağıdaki komut yapısını kullanabiliriz:

Örnek

```py
deg1, deg2, deg3 = 21, 42, 175

print(deg1)
print(deg2)
print(deg3)


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

21
42
175

```

## Geçici veri türü değiştirme (casting)

Bir değişkene değer atarken, atanacak değerin veri türünü geçici olarak değiştirerek değişkenin veri türünü belirleyebiliriz. Bu amaçla, int(), float() ve str() fonksiyonlarını kullanabiliriz. Bu özelliği bir örnek üzerinde incelemeye çalışalım

Örnek

```py
deg1 = 21     # değişken veri türü int olarak belirlenir.   
deg2 = "1784" # değişken veri türü string olarak belirlenir.

deg3 = int(deg2)   # deg3 değişken veri türü int olarak belirlenir. 
deg4 = float(deg2) # deg4 değişken veri türü int olarak belirlenir.
deg5 = str(deg1)   # deg5 değişken veri türü string olarak belirlenir.

print(deg1)
print(deg2)
print(deg3)
print(deg4)
print(deg5)


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

21
1784
1784
1784.0
21

```

Program, deg1 adlı değişkene 21 değerini atayarak değişkeninin veri türünü int olarak ve deg2 adlı değişkene "1784" değerini atayarak değişkeninin veri türünü string olarak belirler. deg3 değişkenine deg2 değişken değerini ilk değer atarken int() fonksiyonunu kullandığından, deg3 değişken veri türü int olarak belirlenir. deg4 değişkenine deg2 değişken değerini ilk değer atarken float() fonksiyonunu kullandığından, deg4 değişken veri türü float olarak belirlenir. deg5 değişkenine deg1 değişken değerini ilk değer atarken str() fonksiyonunu kullandığından, deg5 değişken veri türü string olarak belirlenir.

deg1 ve deg2 değişkenlerinin veri türleri int(), float() ve str() fonksiyonları ile geçici olarak değiştirildiğinden, değişken veri türleri aynı kalır.

## Değişken veri türünü alma

Bir değişkenin veri türünü almak için type() fonksiyonunu kullanabiliriz. Bu özelliği bir örnek üzerinde incelemeye çalışalım

Örnek

```py
deg1 = 135          # değişken veri türü int olarak belirlenir.   
deg2 = "Bilgisayar" # değişken veri türü string olarak belirlenir.

print(type(deg1))
print(type(deg2))
print(deg1)
print(deg2)


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

<class 'int'>
<class 'str'>
135
Bilgisayar

```

Program, deg1 adlı değişkene 135 değerini atayarak değişkeninin veri türünü int olarak ve deg2 adlı değişkene "Bilgisayar" değerini atayarak değişkeninin veri türünü string olarak belirler. Sonra, değişkenlerin veri türlerini ve değerlerini ekrana yazar.

## Lokal değişkenler

Python'da, bir fonksiyonun içinde tanımlanan değişkenlere lokal değişken adı verilir.

Lokal değişkenler aşağıdaki kurallara uygun olarak işlem görür:

* Lokal değişkenlere sadece içinde tanımlandığı fonksiyon kod bloğu tarafından erişim sağlanabilir.
* Birden fazla fonksiyon içinde tanımlanan aynı ada sahip lokal değişkenler birbirinden tamamen farklıdır.
* Aynı ada sahip lokal ve global değişkenler birbirinden tamamen farklıdır.

Lokal değişkenlerin kullanımını bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
deg_g = "Bilgisayar" # Global değişken bildirimi

def fonk1():
    deg1 = "Yazılımı" # Lokal değişken bildirimi
    print("fonk1(): " + deg_g + " " + deg1) # Lokal ve global değişkenlere erişim

def fonk2():
    deg2 = "Programı" # Lokal değişken bildirimi
    print("fonk2(): " + deg_g + " " + deg2) # Lokal ve global değişkenlere erişim
	
print(deg_g) # Global değişkene erişim	
fonk1()
fonk2()


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Bilgisayar
fonk1(): Bilgisayar Yazılımı
fonk2(): Bilgisayar Programı

```

Program, global olarak deg\_g adlı, lokal olarak fonk1() fonksiyonu içinde deg1 adlı ve fonk2() fonksiyonu içinde deg2 adlı olmak üzere, string veri türünden üç adet değişken tanımlar. Tüm değişkenler birbirinden tamamen farklı olup, fonksiyonların içinde tanımlanan değişkenlere sadece içinde tanımlandıkları fonksiyon kodları ile global değişkene ise programın her satırından erişim sağlanabilir.

Aynı ada sahip lokal ve global değişkenlerin kullanımını bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
deg = "Bilgisayar"

def fonk1():
    deg = "Yazılım"
    print("fonk1(): " + deg)

def fonk2():
    deg = "Geliştirme"
    print("fonk2(): " + deg)
	
print(deg)	
fonk1()
fonk2()


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Bilgisayar
fonk1(): Yazılım
fonk2(): Geliştirme

```

Programda, birisi global, birisi fonk1() fonksiyonu içinde ve birisi de fonk2() fonksiyonu içinde olmak üzere, string veri türünden üç adet deg adlı değişken tanımlar. Tüm değişkenler birbirinden tamamen farklı olup, tüm fonksiyonların dışından değişkene yapılan erişim global değişken ile işlem yapılmasını sağlar. Fonksiyonların içinden değişkene yapılan erişim fonksiyon içindeki lokal değişken ile işlem yapılmasını sağlar.

## Global değişkenler

Python'da, tüm fonksiyonların dışında tanımlanan değişkenlere global değişken adı verilir.

GLobal değişkenler aşağıdaki kurallara uygun olarak işlem görür:

* Global değişkenlere tüm fonksiyonlardan ve diğer kod satırlarından erişim sağlanabilir.
* Bir fonksiyon içinde tanımlanan değişken adından önce global anahtar kelimesini kullanarak, global bir değişkeni fonksiyon içinde tanımlayabiliriz.

Global değişkenlerin kullanımını bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
deg_g1 = "Bilgisayar" # Global değişken bildirimi

def fonk1():
    global deg_g2 # Global değişken bildirimi
    print("fonk1(): " + deg_g1 + " " + deg_g2 + " " + deg_g3) # Global değişkenlere erişim

def fonk2():
    global deg_g3 # Global değişken bildirimi
    print("fonk2(): " + deg_g1 + " " + deg_g2 + " " + deg_g3) # Global değişkenlere erişim
	
deg_g2 = "Yazılım"    # Global değişkene değer atama
deg_g3 = "Geliştirme" # Global değişkene değer atama

print(deg_g1 + " " + deg_g2 + " " + deg_g3) # Global değişkenlere erişim	

fonk1()
fonk2()


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Bilgisayar Yazılım Geliştirme
fonk1(): Bilgisayar Yazılım Geliştirme
fonk2(): Bilgisayar Yazılım Geliştirme

```

Program, tüm fonksiyonların dışında deg\_g1 adlı, fonk1() fonksiyonu içinde deg\_g2 adlı ve fonk2() fonksiyonu içinde deg\_g3 adlı global değişken bildirimleri yapar. deg\_g2 ve deg\_g3 değişkenlerine değer atar. Önce, tüm fonksiyonların dışından sonra fonksiyonların içinden tüm global değişkenlere erişim sağlayarak, değişken değerlerini ekrana yazar.
