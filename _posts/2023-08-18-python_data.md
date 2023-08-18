---
title: Python Veri türleri
author: sonsuz
date: 2023-08-18 16:00:34 +0300
categories: [Program,Python]
tags: [python,programlama,data,veri,tür]
---


Python'da 14 adet ön tanımlı veri türü kullanılmaktadır. Bu veri türlerini 6 farklı grup altında sınıflandırabiliriz:

Python veri türleri

| Grup | Veri türü | Açıklama |
| Sayısal | |
| int | Pozitif ve negatif tamsayıları temsil eder. Sayıların basamak sayısı ile ilgili bir sınırlama yoktur. |
| float | Ondalıklı sayıları temsil eder. |
| complex | Kompleks sayıları temsil eder. |
| bool | True veya False değerinden oluşan ikili bir değerdir. |
| None | Boş bir nesneyi temsil eder. Bir değer geri döndürmeyen fonksiyonlar tarafından geri döndürülür. |
| Metin | |
| str | Unicode karakterleri temsil eden karakterlerden oluşan karakter dizisidir. Tek, çift veya üçlü tırnak karakterleri arasında kullanılır. Karakter veri türü olmadığından, tek bir karakter bir değer uzunluğunda karakter dizisidir. |
| list | Verilerin sıralı olarak yer aldığı bir yapıdır. Listede yer alan verilerin aynı veri türünden olması gerekli değildir. Elemanlarda değişiklik yapılabilir. |
| Sıralama | |
| tuple | Verilerin sıralı olarak yer aldığı bir yapıdır. Listede yer alan verilerin aynı veri türünden olması gerekli değildir. Elemanlarda değişiklik yapılamaz. |
| range | Ön tanımlı olarak 0'dan başlamak ve birer birer artırılmak üzere belirlenen sayıdan önce sona eren bir dizi sayı geri döndürür. |
| Mapping | |
| dict | Anahtar ve değer ikililerinden oluşan sıralanmamış verilerdir. Değere ulaşmak için anahtar adı kullanılır. |
| Set | set | Arası virgülle ayrılan ve { } işaretleri arasında yer alan eşsiz elemanlardan oluşan sıralanmamış veri grubudur. |
| frozenset | Arası virgülle ayrılan ve { } işaretleri arasında yer alan eşsiz ve değiştirilemeyen elemanlardan oluşan sıralanmamış veri grubudur. |
| İkili sistem | |
| bytes | 0-255 aralığındaki tamsayılardan oluşan değerlerdir. |
| bytearray | 0-255 aralığındaki tamsayılardan oluşan ve değiştirilebilen değerlerdir. |
| memoryview |  |

Değişken tanımlanırken, değişkenlere atanan farklı türdeki veriler değişkenin veri türünü belirler.

Şimdi, tüm veri türlerinin kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
# int veri türü
deg = 21 
print(deg, "değişkeninin veri türü:", type(deg))

# float veri türü
deg = 35.75 
print(deg, "değişkeninin veri türü:", type(deg))

# complex sayı veri türü
deg = 1+2j 
print(deg, "değişkeninin veri türü:", type(deg))

# bool veri türü
deg = True 
print(deg, "değişkeninin veri türü:", type(deg))

# string veri türü
deg = "Bilgisayar"
print(deg, "değişkeninin veri türü:", type(deg))
print("string değerinin 6.karakteri", deg[5]) # string değerinin 6.karakteri

# list veri türü
deg = [21, 'Bilgisayar', 45.87, 'Yazılım', 75] 
print(deg, "değişkeninin veri türü:", type(deg))
print("İlk eleman değeri:", deg[0]) # list'in ilk elemanına erişim
print("4.eleman değeri:", deg[3]) # list'in 4.elemanına erişim
print("İlk 2 eleman değeri:", deg[0:2]) # list'in ilk 2 elemanına erişim
print("4.elemandan itibaren eleman değerleri:", deg[3:]) # list elemanlarını 4.elemandan itibaren yazdırma
deg[2] = 86 # list'in 3.elemanını değiştirme
print("list eleman değerleri:", deg) # list eleman değerleri

# tuple veri türü
deg = (21, 'Bilgisayar', 45.87, 'Yazılım', 75) 
print(deg, "değişkeninin veri türü:", type(deg))
print("İlk eleman değeri:", deg[0]) # list'in ilk elemanına erişim
print("4.eleman değeri:", deg[3]) # list'in 4.elemanına erişim
print("İlk 2 eleman değeri:", deg[0:2]) # list'in ilk 2 elemanına erişim
print("4.elemandan itibaren eleman değerleri:", deg[3:]) # list elemanlarını 4.elemandan itibaren yazdırma

# range veri türü
# range(başlangıç sayısı, son sayı, aralık)
deg = range(-5, 12, 3) # Başlangıç sayısı (ön tanımlı 0) ve aralık değerinin (ön tanımlı 1) tanımlanması isteğe bağlıdır.  
print(deg, "değişkeninin veri türü:", type(deg))
print("Range içinde yer alan sayılar: ", end=': ')
for n in deg:
    print(n, end=' ')
print()
	
# dict veri türü
deg = {1:'Bilgisayar', 2:'Yazılım', 'Geliştirme':4, 7:'Veriler'}
print(deg, "değişkeninin veri türü:", type(deg))
print("1 anahtarına karşılık gelen değer:", deg[1]) # 1 anahtarına karşılık gelen değeri yazdırma 
print("Geliştirme anahtarına karşılık gelen değer:", deg['Geliştirme']) # 'Geliştirme' anahtarına karşılık gelen değeri yazdırma

# set veri türü
deg = {21, 57, 43, 17, 25}
print(deg, "değişkeninin veri türü:", type(deg))
for n in deg: # set elemanlarını birer yazdırma
    print(n, end=' ')  
print()	

# frozenset veri türü
deg = frozenset({21, 57, 43, 17, 25})
print(deg, "değişkeninin veri türü:", type(deg))
for n in deg: # frozenset elemanlarını birer yazdırma
    print(n, end=' ')
print()

# byte veri türü
deg = b"Bilgisayar"
print(deg, "değişkeninin veri türü:", type(deg))
print("4.karakterin unicode değeri:", deg[3]) # 4.karakterin unicode değeri

# bytearray veri türü
deg = bytearray(b"Bilgisayar")
print(deg, "değişkeninin veri türü:", type(deg))
print("6.karakterin unicode değeri:", deg[5]) # 6.karakterin unicode değeri

# memoryview veri türü
deg = memoryview(b"Bilgisayar")
print(deg, "değişkeninin veri türü:", type(deg))
print("8.karakterin unicode değeri:", deg[7]) # 8.karakterin unicode değeri 


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

21 değişkeninin veri türü: <class 'int'>
35.75 değişkeninin veri türü: <class 'float'>
(1+2j) değişkeninin veri türü: <class 'complex'>
True değişkeninin veri türü: <class 'bool'>
Bilgisayar değişkeninin veri türü: <class 'str'>
string değerinin 6.karakteri s
[21, 'Bilgisayar', 45.87, 'Yazılım', 75] değişkeninin veri türü: <class 'list'>
İlk eleman değeri: 21
4.eleman değeri: Yazılım
İlk 2 eleman değeri: [21, 'Bilgisayar']
4.elemandan itibaren eleman değerleri: ['Yazılım', 75]
list eleman değerleri: [21, 'Bilgisayar', 86, 'Yazılım', 75]
(21, 'Bilgisayar', 45.87, 'Yazılım', 75) değişkeninin veri türü: <class 'tuple'>
İlk eleman değeri: 21
4.eleman değeri: Yazılım
İlk 2 eleman değeri: (21, 'Bilgisayar')
4.elemandan itibaren eleman değerleri: ('Yazılım', 75)
range(-5, 12, 3) değişkeninin veri türü: <class 'range'>
Range içinde yer alan sayılar: : -5 -2 1 4 7 10 
{1: 'Bilgisayar', 2: 'Yazılım', 'Geliştirme': 4, 7: 'Veriler'} değişkeninin veri türü: <class 'dict'>
1 anahtarına karşılık gelen değer: Bilgisayar
Geliştirme anahtarına karşılık gelen değer: 4
{17, 21, 25, 43, 57} değişkeninin veri türü: <class 'set'>
17 21 25 43 57 
frozenset({17, 21, 25, 43, 57}) değişkeninin veri türü: <class 'frozenset'>
17 21 25 43 57 
b'Bilgisayar' değişkeninin veri türü: <class 'bytes'>
4.karakterin unicode değeri: 103
bytearray(b'Bilgisayar') değişkeninin veri türü: <class 'bytearray'>
6.karakterin unicode değeri: 115
<memory at 0x000001425F9B5E80> değişkeninin veri türü: <class 'memoryview'>
8.karakterin unicode değeri: 121

```
