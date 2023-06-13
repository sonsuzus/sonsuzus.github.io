---
title:  Python Programlamaya Giriş 12 – Sıralı nesnelerle işlemler
author: sonsuz
date: 2023-06-13 17:10:05 +0300
categories: [Program,Python]
tags: [python,nesne,sıralı,işlem,dizi,liste]
---






[Daha önceki bir bölümde](https://sonsuzus.github.io/posts/python-programlamaya-giris-sayilar-aritmetik-temel-veri-yapilari) Python’daki liste, çokuz, dize ve sözlük tiplerinin nasıl kullanıldığını kısaca özetlemiştik. Bu ve bunu izleyen üç yazıda liste, sözlük, dize ve küme veri tiplerine dair daha fazla ayrıntı işleyeceğiz. Dizinin bütün yazılarına erişmek için [*Python Programlamaya Giriş*](https://sonsuzus.github.io/categories/python-giris/) kategorimize bakabilirsiniz. 

Bu yazının konusu *sıralı nesne* (sequential object) olarak anılan liste, çokuz ve dize tipleriyle ilgili bazı işlemlerdir. Bunlara sıralı nesne denmesinin sebebi, içlerinde barındırdıkları nesnelerin sırasının önemli oluşu. Söz gelişi, `"merhaba"` dizesi ile `"baharem"` dizesi farklıdır, aynı harfleri barındırmalarına rağmen. Buna karşılık bir sözlük sıralı nesne değildir, çünkü `{"ahmet":123, "ayşe":456}` ile `{"ayşe":456, "ahmet":123}` aynı sözlüğü tanımlarlar.

Bu yazıda göreceklerimiz:

* Dilimleme (slicing)
* Öntanımlı fonksiyonlar: `range, len, del, list, tuple, join, all, any, enumerate, max, min, sorted, sum, zip`
* Türkçe alfabeye göre sıralama

## Dilimleme

Daha önce, bir `L` sıralı nesnesinin `i` indeksli bir elemanına `L[i]` işlemi ile ulaşabildiğimizi görmüştük. Python’da indeksler sıfırdan başladığı için `L[i]` listenin `i+1`‘inci elemanını verir.

In [1]:

```py
L = [3,4,5,6,7,8]

L[0] # birinci eleman


```

Out[1]:

```
3
```

In [2]:

```
L[1] # ikinci eleman


```

Out[2]:

```
4
```

Bazen sonuncu, sondan ikinci vs. elemanları elde etmek isteriz. Genellikle listenin kaç elemanlı olduğunu tam olarak bilmediğimiz için bunu genel bir ifadeyle yazmamız gerekir. Bunun bir yolu, listenin kaç elemanlı olduğunu veren `len` fonksiyonunu kullanmaktır.

In [3]:

```py
len(L)


```

Out[3]:

```
6
```

Liste indeksleri sıfırdan başlayıp `len(L)`-1 değerine kadar gider. O zaman sonuncu elemanı `L[len(L)-1]` ile elde edebiliriz.

In [4]:

```py
L = [3,4,5,6,7,8]

print( L[len(L)-1] ) # sonuncu eleman

print( L[len(L)-2] ) # sondan bir önceki eleman


```

```
8

7


```

Python bu zahmetli yazım yerine doğrudan negatif indeks kullanmaya izin verir. Negatif indeks kullanmak sondan itibaren saymak anlamına gelir. `L[-i]` ifadesi, sondan `i`‘inci elemanı verir.

In [5]:

```py
print( L[-1] ) # sonuncu eleman

print( L[-2] ) # sondan bir önceki eleman


```

```
8

7


```

Dizinin belli bir alt kümesini almak için `L[a:b]` ifadesini kullanırız. Bu *dilimleme* işlemi `L[a]` elemanından `L[b-1]` elemanına kadar bir alt dizi verir. Dikkat: Bu alt diziye `L[b]` dahil değildir.

In [6]:

```py
L[1:4] # ikinci elemandan dördüncü elemana kadar alır.


```

Out[6]:

```
[4, 5, 6]
```

Dilimleme işleminde başlangıç indeksini vermezsek, ilk elemandan başlanır.

In [7]:

```py
L[:4]  # birinci elemandan dördüncü elemana kadar alır.


```

Out[7]:

```py
[3, 4, 5, 6]
```

Bitiş indeksini vermezsek, son elemana kadar gider.

In [8]:

```py
L[4:]  # beşinci elemandan sonuncuya kadar.


```

Out[8]:

```
[7, 8]
```

Bitiş indeksi olarak negatif bir sayı verirsek, o negatif sayıyla belirtilen indeksin bir öncesine kadar gider.

In [9]:

```
L[4:-1] # beşinciden, sondan ikinciye kadar dilim


```

Out[9]:

```
[7]
```

Ne başlangıç ne de bitiş indeksi verirsek dizinin aynısı geri verilir. Bu ilk başta faydasız görünse de, listenin bir kopyasını çıkarma amacıyla sık kullanılan bir kalıptır.

In [10]:

```
L[:]   # baştan sona dilim. Listenin bir kopyasını çıkarmakta kullanılabilir.


```

Out[10]:

```
[3, 4, 5, 6, 7, 8]
```

Dilimleme yaparken elemanları atlamamız da mümkündür.

In [11]:

```
L[1:6:2]  # Birinciden altıncıya kadar iki atlayarak


```

Out[11]:

```
[4, 6, 8]
```

In [12]:

```
L[::2]    # baştan sona kadar iki atlayarak


```

Out[12]:

```
[3, 5, 7]
```

Negatif adım vererek diziyi sondan başa tarayabiliriz.

In [13]:

```
L[::-2]   # sondan başa iki atlayarak


```

Out[13]:

```
[8, 6, 4]
```

In [14]:

```
L[::-1]   # listeyi tersten yaz


```

Out[14]:

```
[8, 7, 6, 5, 4, 3]
```

Liste dilimlerine atama yaparak listeyi değiştirmemiz mümkün olur.

In [15]:

```
L = [3,4,5,6,7,8]

L[1:4] = [-1,-2,-3]   # birinciden dördüncüye kadar elemanları değiştir

L


```

Out[15]:

```
[3, -1, -2, -3, 7, 8]
```

In [16]:

```py
L[::2] = [0,0,0]      # baştan sona kadar birer atlayarak elemanları sıfıra ata.

L


```

Out[16]:

```py
[0, -1, 0, -3, 0, 8]
```

## Dize ve çokuzlarla dilimleme

Yukarıda gösterdiğimiz indeksleme ve dilimleme kuralları, sıralı nesne olan dize (string) ve çokuz (tuple) tiplerinde de aynen geçerlidir.

In [17]:

```py
s = "abcçdefgğ"

t = (3,4,5,6,7,8)


```

In [18]:

```
s[::-1]


```

Out[18]:

```py
'ğgfedçcba'
```

In [19]:

```
t[2:5]


```

Out[19]:

```
(5, 6, 7)
```

Tek fark, dize ve çokuzlar *değiştirilemez* (immutable) veri tipleri oldukları için elemanlarında dilimleme ile değişiklik yapılamaz.

In [21]:

```
t[2:5] = (-1,-2,-3)


```

```py
---------------------------------------------------------------------------

TypeError                                 Traceback (most recent call last)

<ipython-input-21-9ffe2cc1beca> in <module>()

----> 1 t[2:5] = (-1,-2,-3)



TypeError: 'tuple' object does not support item assignment
```

Eğer amacımız ortadaki bazı elemanları değiştirilmiş olan bir çokuz elde etmekse, bunu dilimleri birleştirerek sağlayabiliriz.

In [22]:

```py
t = (3,4,5,6,7,8)

t = t[:2] + (-1,-2,-3) + t[5:]

t


```

Out[22]:

```py
(3, 4, -1, -2, -3, 8)
```

Aynı yöntem tabii dizelerde de geçerli olur.

In [23]:

```py
s = "abcçdefgğ"

s = s[:2] + "XYZ" + s[5:]

s


```

Out[23]:

```py
'abXYZefgğ'
```

## Temel fonksiyonlar

Python’un öntanımlı fonksiyonlarının bir kısmı sıralı nesneler üretmekte veya sıralı nesneler hakkında bilgi edinmekte kullanılırlar. Bunların en yaygınlarının nasıl kullanıldığına bakalım şimdi. Python’daki öntanımlı fonksiyonların tam listesini [Python belgelerinde](https://docs.python.org/3/library/functions.html) bulabilirsiniz.

### range

Tamsayılardan oluşan bir liste üretmek için `range(baş, son, adım)` işlemini kullanabilirsiniz. Aslında `range` bir fonksiyon değil, bir veri tipi döndürür. Onu bir listeye çevirmek için ayrıca `list` işlemi gerekir.

In [24]:

```py
range(10)


```

Out[24]:

```py
range(0, 10)
```

In [25]:

```py
list(range(10))


```

Out[25]:

```py
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

In [26]:

```py
list(range(2,10))


```

Out[26]:

```
[2, 3, 4, 5, 6, 7, 8, 9]
```

In [27]:

```py
list(range(2,10,2))


```

Out[27]:

```
[2, 4, 6, 8]
```

`range` işlemi bir liste değil, dizinin başlangıç, bitiş ve adım bilgilerini barındıran bir nesne geri verir sadece. Bu sayede, `range(1000000)` gibi çok uzun görünen bir dizi bile bellekte ancak `range(10)` kadar yer kaplar. Elemanlar ve alt aralıklar gerektiğinde aritmetik olarak hesaplanır.

In [28]:

```py
r = range(0,20,2)

r


```

Out[28]:

```
range(0, 20, 2)
```

In [29]:

```
11 in r


```

Out[29]:

```
False
```

In [30]:

```
10 in r


```

Out[30]:

```
True
```

In [31]:

```
r[:5]


```

Out[31]:

```
range(0, 10, 2)
```

In [32]:

```
r[-1]


```

Out[32]:

```
18
```

Bir `range` nesnesi `for` döngüsünde doğrudan kullanılabilir.

In [33]:

```
for i in range(0,20,2):

    print(i,end=" ")


```

```
0 2 4 6 8 10 12 14 16 18
```

### len

Kapsayıcı bir nesnenin kaç nesne barındırdığını verir. Sıralı olmayan tiplerle de kullanılabilir.

In [34]:

```
len([1,2,3])


```

Out[34]:

```
3
```

In [35]:

```
len("Hello")


```

Out[35]:

```
5
```

In [36]:

```
len({"a": 45, "b": 5.4})


```

Out[36]:

```
2
```

In [37]:

```
len([])


```

Out[37]:

```
0
```

In [38]:

```
len(range(0, 20, 2))


```

Out[38]:

```
10
```

### del

Genel olarak, belli bir isme bağlı bir nesneyi bellekten kaldırır. Sıralı nesnelerde, bir dilimi silmek için de kullanılabilir.

In [39]:

```
a = 23

del a

a


```

```
---------------------------------------------------------------------------

NameError                                 Traceback (most recent call last)

<ipython-input-39-281c77bb7324> in <module>()

 1 a = 23

 2 del a

----> 3 a



NameError: name 'a' is not defined
```

In [40]:

```
L = [1,2,3,4,5,6]

del L[1]   # ikinci elemanı siler

L


```

Out[40]:

```
[1, 3, 4, 5, 6]
```

In [41]:

```
del L[2:4]    # üçüncüden dördüncüye kadar olan elemanları siler

L


```

Out[41]:

```
[1, 3, 6]
```

In [42]:

```
del L[:]      # bütün elemanları siler, ama L listesini silmez.

L


```

Out[42]:

```
[]
```

In [43]:

```
del L         # L listesini siler

L


```

```
---------------------------------------------------------------------------

NameError                                 Traceback (most recent call last)

<ipython-input-43-c66d86760815> in <module>()

 1 del L         # L listesini siler

----> 2 L



NameError: name 'L' is not defined
```

### list, tuple, join

`list` fonksiyonu herhangi bir sıralı nesneyi bir liste nesnesine4 çevirmek için kullanılır.

In [44]:

```py
s = "merhaba"

list(s)  # dizeyi listeye çevirir.


```

Out[44]:

```py
['m', 'e', 'r', 'h', 'a', 'b', 'a']
```

In [45]:

```py
t = (1,2,3,4)

list(t)  # çokuzu listeye çevirir.


```

Out[45]:

```py
[1, 2, 3, 4]
```

`tuple` fonksiyonu ise bir sıralı diziyi çokuza çevirir.

In [46]:

```
s = "merhaba"

tuple(s)


```

Out[46]:

```py
('m', 'e', 'r', 'h', 'a', 'b', 'a')
```

In [47]:

```
L = [1,2,3,4]

tuple(L)


```

Out[47]:

```py
(1, 2, 3, 4)
```

Bir dizenin harflerinden oluşan bir liste veya çokuz oluşturmak kolay olsa da, bunun tersi, yani harf listesini dizeye çevirmek için tek bir komut yok. Bu işlem için kabul edilen kalıp, dizelerin `join` metodunu kullanmaktır (bir *metod*, bir nesnenin içinde tanımlanmış bir fonksiyondur).

In [48]:

```py
L = ['m', 'e', 'r', 'h', 'a', 'b', 'a']

"".join(L)


```

Out[48]:

```
'merhaba'
```

Genel olarak `s.join(L)` işlemi `L` listesinin her elemanını aralarına `s` dizesini koyarak birleştirir. Yukarıdaki örnekte `s` bir boş dizeydi, o yüzden `L`‘nin elemanları yanyana yazıldı. Eğer istersek, araya başka karakterler de koyabiliriz.

In [49]:

```py
L = ['m', 'e', 'r', 'h', 'a', 'b', 'a']

"-*-".join(L)


```

Out[49]:

```
'm-*-e-*-r-*-h-*-a-*-b-*-a'
```

Dize birleştirmeyi aşağıdaki gibi bir `for` döngüsüyle de yapabiliriz.

In [50]:

```py
s = ""

for ls in L:

    s = s + ls

s


```

Out[50]:

```
'merhaba'
```

### all

Bir sıralı nesne içindeki *bütün elemanlar* mantıksal doğruya denkse `True` verir, yoksa `False` verir. Python’da sıfır, boş liste `[]`, boş dize `""` gibi yapıların da `False` sayıldığını; sıfır olmayan sayıların ve boş olmayan nesnelerin de `True` sayıldığını hatırlayın.

In [51]:

```
all( [1, 2, 3, 4] )


```

Out[51]:

```
True
```

In [52]:

```
all( (0, 1, 2, 3) )


```

Out[52]:

```
False
```

In [53]:

```
all( "abc" )


```

Out[53]:

```
True
```

In [54]:

```
all( [1, 2, ()] )


```

Out[54]:

```
False
```

### any

Bir liste içinde *en az bir eleman* mantıksal doğruya denkse `True` verir, yoksa `False` verir. Python’da sıfır, boş liste `[]`, boş dize `""` gibi yapıların da `False` sayıldığını; sıfır olmayan sayıların ve boş olmayan nesnelerin de `True` sayıldığını hatırlayın.

In [55]:

```
any( [0, '', True] )


```

Out[55]:

```
True
```

In [56]:

```
any( [0, '', False] )


```

Out[56]:

```
False
```

In [57]:

```
any( [0, 'abc', False] )


```

Out[57]:

```
True
```

### enumerate

Bir sıralı nesnenin elemanlarına sıra numarası atamak için kullanılır. Özellikle döngülerde, bir nesne üzerinden iterasyon yaparken yararlı olur.

In [58]:

```
list(enumerate("abcd"))


```

Out[58]:

```
[(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]
```

In [59]:

```py
for i,c in enumerate("abcçdefgğ"):

    print(i,c)


```

```
0 a

1 b

2 c

3 ç

4 d

5 e

6 f

7 g

8 ğ


```

Bazı problemlerde, bir veri listesini tararken o verinin bulunduğu konuma dair bilgiye de ihtiyaç duyarız. Basit bir örnek olarak, bir isim listesinde Z ile başlayan isimlerin listedeki konumunu görmek isteyebiliriz. Bu amaçla yazdığımız bir `for` döngüsünde `enumerate` kullanabiliriz.

In [60]:

```py
isimler = ["Kaan","Meral","Ziya","Fındık"]

for i, isim in enumerate( isimler ):

    if "Z" in isim:

        print(i,isim)


```

```
2 Ziya


```

Python dışındaki dillere alışık olan programcılar bu işlemi bir `while` döngüsüyle ve bir sayaçla yapmaya çalışırlar, örneğin şöyle bir kodla:

In [61]:

```py
isimler = ["Kaan","Meral","Ziya","Fındık"]

i = 0

while i < len(isimler):

    if "Z" in isimler[i]:

        print(i,isimler[i])

    i += 1

    


```

```
2 Ziya


```

Ancak `enumerate` ile `for` kullanmak sadeliği ve okunaklılığı açısından tercih edilir.

### max, min

`max` fonksiyonu bir sıralı nesne veya bir dizi parametre alır, aralarından en büyük değerli olanını geri verir.

In [62]:

```py
max(4,2,8,3,1,7)


```

Out[62]:

```
8
```

In [63]:

```py
L = [4,2,8,3,1,7]

max(L)


```

Out[63]:

```
8
```

Dizelerden oluşan bir sıralı nesne verildiğinde `max` alfabetik sırada en ileride olanını döndürür.

In [64]:

```py
max(["dfg","zxy","abc"])


```

Out[64]:

```py
'zxy'
```

In [65]:

```
max("merhaba")


```

Out[65]:

```
'r'
```

`key` parametresi ile her elemana önceden uygulanacak bir fonksiyon belirleyebilirsiniz ve maksimum bu fonksiyonun sonucuna göre tespit edilir. Söz gelişi, mutlak değer olarak en büyük elemanı bulmak için `key=abs` verebilirsiniz.

In [66]:

```py
L = [-1,-3, 4, -5, 2]

max(L, key=abs)


```

Out[66]:

```
-5
```

`min` fonksiyonu verilen bir dizinin içinde, veya parametreler içinde en küçük olanını döndürür. Kullanımı `max` ile aynıdır.

In [67]:

```
min(L, key=abs)


```

Out[67]:

```
-1
```

In [68]:

```
min("merhaba")


```

Out[68]:

```
'a'
```

### sorted

Bir dizi nesnesi alır ve nesne elemanlarının düzgün sıralanmış olduğu bir liste döndürür.

In [69]:

```
sorted([1, 3, -1, 4, -3, 6, 4])


```

Out[69]:

```
[-3, -1, 1, 3, 4, 4, 6]
```

`reverse` parametresiyle sıralama ters çevrilir.

In [70]:

```py
 sorted([1, 3, -1, 4, -3, 6, 4], reverse=True)      # ters sıralama


```

Out[70]:

```py
[6, 4, 4, 3, 1, -1, -3]
```

Dizeler alfabetik sıraya konur.

In [71]:

```
sorted("merhaba")


```

Out[71]:

```
['a', 'a', 'b', 'e', 'h', 'm', 'r']
```

In [72]:

```py
sorted(("Ziya","Meral","Kaan","Fındık"))


```

Out[72]:

```
['Fındık', 'Kaan', 'Meral', 'Ziya']
```

`key` parametresine verilen bir fonksiyon sıralamadan önce her elemana uygulanır; sonuç sıralaması bu fonksiyona göre belirlenir.

In [73]:

```py
sorted([1, 3, -2, 4, -5, 6, 4], key=abs)    # mutlak değere göre sıralar


```

Out[73]:

```
[1, -2, 3, 4, 4, -5, 6]
```

In [74]:

```py
sorted( [(1,2), (0,2), (3,4), (2,-1)] , key=sum)  # çokuz elemanların toplamına göre sıralar


```

Out[74]:

```
[(2, -1), (0, 2), (1, 2), (3, 4)]
```

In [75]:

```py
sorted( [(1,2), (0,2), (3,4), (2,-1)], key=lambda x:x[1]) # ikinci elemana göre sıralar


```

Out[75]:

```
[(2, -1), (1, 2), (0, 2), (3, 4)]
```

### Türkçe sıralama

Python 3 Unicode kullandığı için İngilizce dışı harfleri kullanırken zorluk çıkarmaz. Ama alfabetik sıralama yapmaya çalıştığımızda doğru cevabı alamayabiliriz.

In [76]:

```
sorted(("Ahmet","Şebnem","Mehmet","Ziya","İsmail","Ümit"))


```

Out[76]:

```
['Ahmet', 'Mehmet', 'Ziya', 'Ümit', 'İsmail', 'Şebnem']
```

Türkçe alfabeye göre sıralama yapmak için yerellik ayarı yapmalıyız. Bunun için `locale` modülünü yüklemeli, ardından da `sorted` fonksiyonuna `key` parametresi olarak `locale.strxfrm` fonksiyonunu vermeliyiz.

In [77]:

```py
import locale

locale.setlocale(locale.LC\_ALL, ("tr", 'UTF-8'))

sorted(("Ahmet","Şebnem","Mehmet","Ziya","İsmail","Ümit"), key=locale.strxfrm)


```

Out[77]:

```py
['Ahmet', 'İsmail', 'Mehmet', 'Şebnem', 'Ümit', 'Ziya']
```

### sum

Bir sıralı nesnenin elemanlarının toplamını verir. Elemanlar sayısal değere sahip olmalıdır.

In [78]:

```py
sum([1,2,3])


```

Out[78]:

```
6
```

In [79]:

```py
sum(range(1,101))


```

Out[79]:

```
5050
```

### zip

Aynı uzunlukta iki veya daha çok listenin aynı konumdaki elemanlarını sırayla alır, bu elemanlardan çokuzlar oluşturur ve bu çokuzların listesini verir.

In [80]:

```
L1 = [4, 5, 9]

L2 = ['a', 'b', 'c']

list(zip(L1, L2))


```

Out[80]:

```py
[(4, 'a'), (5, 'b'), (9, 'c')]
```

`zip` ile farklı verileri birleştirerek bir `for` döngüsünde işlemek mümkün olur. Tıpkı `enumerate` gibi `zip` de bizi elemanları bir sayaç değişkeniyle takip etme mecburiyetinden kurtarır.

In [81]:

```py
yaşlar = [19, 25, 32, 27]

boylar = [170, 180, 175, 169]

ağırlık = [75, 78, 81, 71]

for y, b, a in zip(yaşlar, boylar, ağırlık):

    print("Yaş:", y, "Boy:", b, "Ağırlık:",a)


```

```py
Yaş: 19 Boy: 170 Ağırlık: 75

Yaş: 25 Boy: 180 Ağırlık: 78

Yaş: 32 Boy: 175 Ağırlık: 81

Yaş: 27 Boy: 169 Ağırlık: 71


```
