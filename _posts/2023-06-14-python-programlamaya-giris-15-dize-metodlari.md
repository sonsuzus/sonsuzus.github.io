---
title:  Python Programlamaya Giriş 15 – Dize metodları
author: sonsuz
date: 2023-06-14 01:11:25 +0300
categories: [Program,Python]
tags: [python,dize,metod]
---






Python programlamaya giriş yazı dizimizin bu bölümünde dizelerin kullanımını daha ayrıntılı inceleyeceğiz ve dize veri tipine ait olan metodların bazılarına örneklerle göz atacağız. Dizinin bütün yazılarına erişmek için [*Python Programlamaya Giriş*](http://www.veridefteri.com/categories/python-giris/) kategorimize bakabilirsiniz.

**Dize**, bir veya daha fazla karakterden bir araya gelmiş bir sıralı veri tipidir. Dizelerle düz metin halindeki veriler alınıp işlenebilir. Veriler pek çok zaman düz metin dosyaları halinde bulunur. HTML, XML, JSON veya CSV gibi standartlardaki veriler de düz metinden oluşur. Bir metin verisini dize halinde aldığımızda, dize metodlarını kullanarak bu verileri işleyebilir, biçimlerini değiştirebilir, parçalayabilir, birleştirebilir, sıralayabilir, değişiklik yapabiliriz.

## Temel işlemler

Sıralı nesnelerle kullanılan `len`, `in`, `not in`, `+`, `*` gibi işlemler dizelerde de aynı şekilde çalışır:

In [1]:

```py
print( "Def" in "Abcç Defg" )

print( "def" in "ABcç Defg" )

print( "def" not in "ABcç Defg" )


```

```py
True

False

True


```

In [2]:

```py
len("Abcç Defg")


```

Out[2]:

```
9
```

In [3]:

```py
"Abcç" + "Defg"


```

Out[3]:

```py
'AbcçDefg'
```

In [4]:

```py
"Abcç" * 5


```

Out[4]:

```py
'AbcçAbcçAbcçAbcçAbcç'
```

Bir nesnenin dize biçimini elde etmek için `str` fonksiyonu kullanılabilir.

In [5]:

```
str(12345)


```

Out[5]:

```
'12345'
```

In [6]:

```
str([1,2,3])


```

Out[6]:

```
'[1, 2, 3]'
```

## Tek tırnak, çift tırnak, üçlü tırnak

Python’da diziler istenirse tek tırnakla, istenirse çift tırnakla sınırlandırarak kullanılabilirler. İkisi de aynı nesneyi üretir; yani `"abc"` ile `'abc'` aynı dizedir.

Bu esneklik, dizenin içinde bir çeşit tırnak varsa, dizenin çevresinde öbür çeşit tırnağı kullanma imkânı verir.

In [7]:

```py
print("Ali'nin kalemini ver.")


```

```
Ali'nin kalemini ver.


```

In [8]:

```py
print( 'Dedim ki: "Gel!"' )


```

```
Dedim ki: "Gel!"


```

Eğer dizenin içindeki metinde her iki tırnak çeşidine de ihtiyaç duyarsak, *kaçış karakterleri* `\’` ve `\"` kullanabiliriz.

In [9]:

```py
print("Ali'ye dedim ki: \"Gel!\"")


```

```
Ali'ye dedim ki: "Gel!"


```

Üç tırnak (`"""` veya `'''`) kullanarak birkaç satıra yayılan bir dize yaratabiliriz. Yaptığımız kaydırmalar, satırbaşları, boş satırlar dizenin parçası olarak kaydedilir. Bu tür dizeler özellikle fonksiyonlardaki belge dizelerinde (docstring) çok kullanılır.

In [10]:

```py
s = """abcç

 def

gğhıi"""

print(s)


```

```py
abcç

    def

gğhıi


```

## Dize metodları

Dize sınıfı içinde tanımlanmış pek çok metod mevcut. Bunların tam bir listesini görmek için `dir(str)` komutunu verebilirsiniz.

In [11]:

```
dir(str)


```

Out[11]:

```py
['__add__',

 '__class__',

 '__contains__',

 '__delattr__',

 '__dir__',

 '__doc__',

 '__eq__',

 '__format__',

 '__ge__',

 '__getattribute__',

 '__getitem__',

 '__getnewargs__',

 '__gt__',

 '__hash__',

 '__init__',

 '__init_subclass__',

 '__iter__',

 '__le__',

 '__len__',

 '__lt__',

 '__mod__',

 '__mul__',

 '__ne__',

 '__new__',

 '__reduce__',

 '__reduce_ex__',

 '__repr__',

 '__rmod__',

 '__rmul__',

 '__setattr__',

 '__sizeof__',

 '__str__',

 '__subclasshook__',

 'capitalize',

 'casefold',

 'center',

 'count',

 'encode',

 'endswith',

 'expandtabs',

 'find',

 'format',

 'format_map',

 'index',

 'isalnum',

 'isalpha',

 'isdecimal',

 'isdigit',

 'isidentifier',

 'islower',

 'isnumeric',

 'isprintable',

 'isspace',

 'istitle',

 'isupper',

 'join',

 'ljust',

 'lower',

 'lstrip',

 'maketrans',

 'partition',

 'replace',

 'rfind',

 'rindex',

 'rjust',

 'rpartition',

 'rsplit',

 'rstrip',

 'split',

 'splitlines',

 'startswith',

 'strip',

 'swapcase',

 'title',

 'translate',

 'upper',

 'zfill']
```

Her bir metodun kısa bir açıklaması için `help()` komutunu kullanabilirsiniz.

In [12]:

```py
help(str.capitalize)


```

```py
Help on method_descriptor:



capitalize(...)

    S.capitalize() -> str

    

    Return a capitalized version of S, i.e. make the first character

    have upper case and the rest lower case.




```

Burada bu metodların belli başlılarının kullanımlarını örnekleyerek açıklayacağız. Özellikle, metin şeklindeki verilerin analizinde kullanılabilecek metodları seçtik. Tam bir liste için [Python yardım belgelerine](https://docs.python.org/3.6/library/stdtypes.html#string-methods) bakabilirsiniz.

## startswith, endswith

Bir dizenin başlangıcında veya sonunda belli bir alt dizenin bulunması halinde `True` verirler.

In [13]:

```py
s = "Python Programlamaya Giriş"

s.startswith("Pyth"), s.startswith("python")


```

Out[13]:

```
(True, False)
```

In [14]:

```
s.endswith("iriş"), s.endswith("xyz")


```

Out[14]:

```
(True, False)
```

## Büyük-küçük harf değişiklikleri

Dizeleri tamamen küçük veya büyük harfe çevirmek, cümlenin ilk harfinin büyük olmasını sağlamak, veya bir başlıktaki gibi her kelimenin büyük harfle başlamasını sağlamak için çeşitli dize metodları vardır.

In [15]:

```py
s = "Pijamalı hasta yağız şoföre çabucak güvendi."



print("s.upper():", s.upper())   # Hepsini büyük harfe çevir.

print("s.lower():", s.lower())   # Hepsini küçük harfe çevir.

print("s.capitalize():", s.capitalize())   # Sadece cümlelerin ilk harfini büyük yap. 

print("s.swapcase():", s.swapcase())   # Büyük harfleri küçüğe, küçükleri büyüğe çevir.

print("s.title():", s.title())   # Her kelimenin ilk harfini büyük yap.


```

```py
s.upper(): PIJAMALI HASTA YAĞIZ ŞOFÖRE ÇABUCAK GÜVENDI.

s.lower(): pijamalı hasta yağız şoföre çabucak güvendi.

s.capitalize(): Pijamalı hasta yağız şoföre çabucak güvendi.

s.swapcase(): pIJAMALI HASTA YAĞIZ ŞOFÖRE ÇABUCAK GÜVENDI.

s.title(): Pijamalı Hasta Yağız Şoföre Çabucak Güvendi.


```

Görüldüğü gibi bu fonksiyonlar Türkçedeki i ve I harflerini doğru şekilde işleyemiyorlar. Küçük i harfi büyük I harfine (ve tersine) dönüştürülüyor. Bu yüzden Python’un dize metodları, yazılımda Türkiye testi olarak bilinen testi geçemiyor.

In [16]:

```py
"I İ".lower(), "ı i".upper()


```

Out[16]:

```
('i i̇', 'I I')
```

Bu problemin çevresinden dolaşmak için kullanılacak bir yöntemi [şuradan](https://stackoverflow.com/a/41316018) öğrenebilirsiniz.

## Alt dizeleri saymak: count

Bir dize içinde bir alt dizenin kaç kere geçtiğinin sayısını verir.

In [17]:

```py
"ABCDABCAAABC".count("ABC")


```

Out[17]:

```
3
```

Sadece örtüşmeyen alt dizeler sayılır. Sözgelişi, `"AAAAA"` dizesinin içinde, örtüşmeleri sayarsak `"AA"` altdizesi 5 kere mevcuttur, ama `count` 2 sonucunu verir.

In [18]:

```py
"AAAAA".count("AA")


```

Out[18]:

```
2
```

## Bir alt dizenin yerini bulmak: find, rfind, index, rindex

`find` metodu, bir dizenin içinde bir alt dizenin ilk bulunduğu konumu verir. Aranan alt dize mevcut değilse -1 döndürür.

In [19]:

```py
s = "ABRAKADABRA"

s.find("RA")


```

Out[19]:

```
2
```

In [20]:

```py
s.find("XYZ")


```

Out[20]:

```
-1
```

Konum saymanın sıfır ile başladığını hatırlayın; o yüzden `"RA"` dizesi üçüncü harfte başlıyor, ama konum indeksi 2.

Dikkat: Amacınız belli bir alt dizenin yerini bulmak değil, sadece mevcut olup olmadığını anlamaksa `find` yerine `in` kullanın.

In [21]:

```py
"RA" in s, "XYZ" in s


```

Out[21]:

```
(True, False)
```

Aramaya sağdan başlamak isterseniz `rfind` metodunu kullanın.

In [22]:

```py
s.rfind("RA")


```

Out[22]:

```
9
```

`index` ile `find` aynı işi yapar. Tek farkları, aranan alt dize bulunamayınca `index`‘in bir hata işareti (`"ValueError"`) vermesidir. Hata yakalamaya dayalı programlarda tercih edilir.

In [23]:

```
s.index("RA")


```

Out[23]:

```
2
```

In [24]:

```py
s.index("XYZ")


```

```py
---------------------------------------------------------------------------

ValueError                                Traceback (most recent call last)

<ipython-input-24-de36660908dd> in <module>()

----> 1 s.index("XYZ")



ValueError: substring not found
```

Aramaya sağdan başlamak isterseniz `rindex` komutunu kullanabilirsiniz.

## Dizeleri birleştirmek: join

Bir sıralı nesnenin (liste, çokuz, dize, vs.) dize tipi elemanlarını birleştirerek yeni bir dize üretir.

In [25]:

```py
"".join(["A","67","B","0.15"])    # yanyana yapıştırır


```

Out[25]:

```
'A67B0.15'
```

In [26]:

```py
" ".join(["A","67","B","0.15"])   # araya bir boşluk koyarak yapıştırır


```

Out[26]:

```
'A 67 B 0.15'
```

In [27]:

```py
"-*-".join(["A","67","B","0.15"]) # araya -*- koyarak yapıştır


```

Out[27]:

```
'A-*-67-*-B-*-0.15'
```

## Boşlukları atmak: lstrip, rstrip, strip

Bu metodlar bir dizenin sol ve/veya sağ tarafındaki boş karakterleri (boşluk, kaydırma `\t`, satırbaşı `\n`) kaldırır. `lstrip` soldaki, `rstrip` sağdaki, `strip` ise her iki yandaki boşlukları temizler. Bu metodlar özellikle bir dosya satır satır okunurken yararlı olur.

In [28]:

```py
s = """

 ferah ferah 

"""

s


```

Out[28]:

```py
'\n        ferah  ferah   \n'
```

In [29]:

```py
s.lstrip()


```

Out[29]:

```
'ferah  ferah   \n'
```

In [30]:

```py
s.rstrip()


```

Out[30]:

```py
'\n        ferah  ferah'
```

In [31]:

```py
s.strip()


```

Out[31]:

```
'ferah  ferah'
```

## Değiştirme: replace

Dizede belli bir alt dizenin ortaya çıktığı her yeri başka bir alt dizeyle değiştirir.

In [32]:

```py
s = "eskişehir'de eski bir evde eski bir kapı"

s.replace("eski", "yeni")


```

Out[32]:

```py
"yenişehir'de yeni bir evde yeni bir kapı"
```

Tercihe bağlı olarak, soldan itibaren sadece belli sayıda değiştirme de yapılabilir:

In [33]:

```py
s.replace("eski", "yeni", 2)


```

Out[33]:

```py
"yenişehir'de yeni bir evde eski bir kapı"
```

## Bölme: split, rsplit, splitlines

`split` metodu bir dizedeki kelimeleri belli yerlerden (varsayılan olarak boşluk karakterlerinden) böler ve ortaya çıkan bölümlerden oluşan bir dize listesi verir. Fazlalık boşluklar hesaba katılmaz.

In [34]:

```py
" kedi köpek balık kuş ".split()


```

Out[34]:

```py
['kedi', 'köpek', 'balık', 'kuş']
```

Boşluk yerine başka bir ayırıcı kullanılabilir. Ayrıcı istenilen sayıda karakterden oluşabilir.

In [35]:

```py
"1,2,3,4,5,6".split(",")


```

Out[35]:

```py
['1', '2', '3', '4', '5', '6']
```

In [36]:

```py
"a<>b<>c<>d<>e".split("<>")


```

Out[36]:

```py
['a', 'b', 'c', 'd', 'e']
```

Sadece belli sayıda bölme yapmak da mümkündür. Arta kalan kısım tek bir dizede toplanır.

In [37]:

```py
" kedi köpek balık kuş ".split(maxsplit=2)


```

Out[37]:

```py
['kedi', 'köpek', 'balık    kuş   ']
```

Soldan değil sağdan başlayarak ayırmamız gerekirse `rsplit` metodunu kullanırız.

In [38]:

```py
" kedi köpek balık kuş ".rsplit(maxsplit=2)


```

Out[38]:

```py
['   kedi köpek', 'balık', 'kuş']
```

Birden fazla satır barındıran bir dizeyi satır sınırlarından bölmek için `splitlines` metodu kullanılabilir.

In [39]:

```py
s = """abcç

defgğ

hıi

jkl"""



s.splitlines()


```

Out[39]:

```py
['abcç', 'defgğ', 'hıi', 'jkl']
```

`splitlines` metodu sadece satırbaşı (`"\n"`) ile değil, `"\r"`, `"\v"`, `"\f"`, ve satır sonu sayılan başka birkaç karakter ile de böler. Ayrıca, `split`‘ten farklı olarak dize sonundaki `"\n"` karakterini de göz ardı eder. Bir dosyanın içeriğini bütün olarak bir dizeye yüklediyseniz, onu satırlara bölmek için en uygunu `splitlines` kullanmaktır.
