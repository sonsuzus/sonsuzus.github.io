---
title:  Python Programlamaya Giriş 19 – Liste kurma, sözlük kurma, üreteç ifadeler
author: sonsuz
date: 2023-06-14 18:42:37 +0300
categories: [Program,Python]
tags: [python,sözlük,liste,üreteç ifade]
math: true
---






Diyelim mevcut bir listedeki her elemanı tek tek işleyip, işlemin sonuçlarını yeni bir listede toplamak istiyorsunuz. Bunun için boş bir listeyle başlayıp, [bir döngü içinde](https://sonsuzus.github.io/posts/python-programlamaya-giris-donguler) `append()` metoduyla listeyi adım adım büyütebiliriz. Bu yazıda Python’da bu işlemi daha hızlı verimli olarak yapmamızı sağlayan özel *liste kurma* yazımını göreceğiz. Liste kurma, genel olarak bir *üreteç ifadesi* örneğidir. Liste kurma gibi sözlük ve kümeleri de hızlıca kurmak için benzer bir yazım kullanırız.

Yazı dizimizin bütün yazılarına erişmek için [*Python Programlamaya Giriş*](https://sonsuzus.github.io/categories/python) kategorimize bakabilirsiniz.

## Basit liste kurma

Basit bir örnekle başlayalım: Bir sayı listesi alalım, ve liste elemanlarının karelerinden oluşan yeni bir liste oluşturalım.

Şimdiye kadar gördüğümüz yöntemlerle bu işi yapmak için önce boş bir liste yaratırız, sonra bir `for` döngüsü içinde sayıları tek tek alırız, karelerini teker teker boş listeye ekleriz.

In [1]:

```py
sayılar = [1,2,3,4,5]

kareler = []

for x in sayılar:

    kareler.append(x*x)



kareler


```

Out[1]:

```
[1, 4, 9, 16, 25]
```

Aynı işi daha kısa yoldan ve daha hızlı yapmak için Python’da *liste kurma* (list comprehensions) denen bir yapı vardır.

In [2]:

```py
kareler = [x*x for x in sayılar]

kareler


```

Out[2]:

```
[1, 4, 9, 16, 25]
```

En basit halinde, liste kurma yapısının genel hali şöyledir:

```py
[ <ifade> for <değişken> in <sıralı nesne> ]




```

Bu yapıda, `<sıralı nesne>`‘deki değerler tek tek `<değişken>`‘e atanır, ve `<ifade>`‘nin değeri hesaplanarak listeye eklenir.

Yukarıdaki liste kurma ifadesi aşağıdaki kod parçasına denktir:

```py
L = []

for <değişken> in <sıralı nesne>:

    L.append(<ifade>)




```

Birkaç örnek vererek açıklayalım. İkinin ilk on kuvvetinin listesi:

In [3]:

```py
[2**i for i in range(1,11)]


```

Out[3]:

```py
[2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
```

Bir dizedeki karakterleri tek tek almak:

In [4]:

```py
[c+"*" for c in "merhaba"]


```

Out[4]:

```py
['m*', 'e*', 'r*', 'h*', 'a*', 'b*', 'a*']
```

Çokuzlardaki elemanların toplamlarının listesi:

In [5]:

```py
[ x[0] + x[1] for x in [(1,2), (2,-1), (4,2), (3,7)] ]


```

Out[5]:

```
[3, 1, 6, 10]
```

Yukarıdaki örnek, *çokuz ataması* özelliği sayesinde şöyle de yazılabilir:

In [6]:

```py
[ x+y for x,y in [(1,2), (2,-1), (4,2), (3,7)] ]


```

Out[6]:

```
[3, 1, 6, 10]
```

Aradaki fark şöyle: Birinci durumda `x` değişkenine sırayla çokuzlar atanıyor, sonra indeksleme ile tek tek elemanlarını alıyoruz. İkinci durumda ise çokuzun birinci ve ikinci elemanı sırasıyla `x` ve `y` değişkenlerine atanıyor.

İfade olarak bir fonksiyon da kullanılabilir.

In [7]:

```py
def kare(x): return x*x

[kare(x) for x in range(1,11)]


```

Out[7]:

```py
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

In [8]:

```py
def topla(a,b): return a+b

[topla(x,y) for x,y in [(1,2), (2,-1), (4,2), (3,7)] ]


```

Out[8]:

```
[3, 1, 6, 10]
```

Liste kurma ifadelerinin döngülerden bir farkı da, döngü değişkeninin kalıcı olmamasıdır.

In [9]:

```py
[i*i for i in range(10)]


```

Out[9]:

```py
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

In [10]:

```
i


```

```py
---------------------------------------------------------------------------

NameError                                 Traceback (most recent call last)

<ipython-input-10-372e25f23b5a> in <module>()

----> 1 i



NameError: name 'i' is not defined
```

Oysa bir döngü kullandığımızda iç değişkenler döngüden sonra da erişilebilir olurlar.

In [11]:

```py
L = []

for i in range(10):

    L.append(i*i)



i


```

Out[11]:

```
9
```

## Hız farkı

Liste kurma ile, bir döngü içinde bir listeye `append()` ile eleman ekleme aynı işi yapıyorsa, neden liste kurmayı kullanalım? Birincisi, daha sade bir yapı olduğu için. Daha da önemlisi, liste kurma işlemi daha hızlı çalışır.

Hız farkının iki sebebi vardır: Birincisi Python gibi yorumlanan dillerde döngülerin nispeten yavaş çalışmasıdır (C gibi derlenen dillere göre). Bir liste kurma ifadesi yine de örtük bir döngü içeriyor elbette, ama bu döngü alt seviyededir ve Python yorumlayıcısı tarafından yüksek hızda işletilir. İkinci sebep ise her iterasyonda listenin `append()` metodunun çağırılması gereğidir – fonksiyon çağrıları uzun zaman alan işlemlerdir ve programı yavaşlatırlar.

Bunu daha somut olarak görmek için 1 ile 1000 arasındaki sayıların karelerini alan bir liste kurma ve bir döngü oluşturalım ve %%timeit komutuyla iki yaklaşım arasındaki zaman farkına  bakalım.

In [12]:

```py
%%timeit

[x*x for x in range(1000)]


```

```py
79.8 µs ± 9.52 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)


```

In [13]:

```py
%%timeit

L = []

for x in range(1000):

    L.append(x*x)


```

```py
150 µs ± 13.2 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)


```

## Şartlı liste kurma

Liste kurma işleminde her elemanı eklemek zorunda değiliz; bir şartı sağlayanları da eklememiz mümkün. Sözgelişi, bir sayı listesi içinde, sadece beşten büyük olanların karesini barındıran bir liste oluşturalım.

In [14]:

```py
[x*x for x in [1,3,5,7,9,11] if x>5 ]


```

Out[14]:

```py
[49, 81, 121]
```

Bu ifade, aşağıdaki döngüye denktir:

```py
L = []

for x in [1,3,5,7,9,11]:

    if x>5:

        L.append(x*x)




```

Çeşitli karşılaştırma işlemleri ve mantıksal işlemler de birleştirilebilir. Örnek olarak, 1900 ile 2100 arasındaki artık yılların listesini oluşturalım. Bilindiği gibi bir yıl 4’e bölünebiliyorsa artık yıldır; 100’e bölünen ama 400’e bölünemeyen yıllar hariç. Yani 1600 ve 2000 yılları artık yıl iken, 1700, 1800, 1900, 2100 yılları artık değildir.

In [15]:

```py
[ y for y in range(1900, 2101) if (y%4 == 0 and y%100 != 0) or y%400 == 0 ]


```

Out[15]:

```py
[1904,

 1908,

 1912,

 1916,

 1920,

 1924,

 1928,

 1932,

 1936,

 1940,

 1944,

 1948,

 1952,

 1956,

 1960,

 1964,

 1968,

 1972,

 1976,

 1980,

 1984,

 1988,

 1992,

 1996,

 2000,

 2004,

 2008,

 2012,

 2016,

 2020,

 2024,

 2028,

 2032,

 2036,

 2040,

 2044,

 2048,

 2052,

 2056,

 2060,

 2064,

 2068,

 2072,

 2076,

 2080,

 2084,

 2088,

 2092,

 2096]
```

Şartlı liste kurmanın genel ifadesi şöyledir:

```py
[<ifade> for <değişken> in <sıralı nesne> if <şart>]




```

Bu yapıda, sadece şartın doğru olduğu değişken değerleri için listeye eleman eklenir. Şart yanlışsa eklenmez. Eğer şart yanlış olduğunda da listeye belli değerler eklenmesini istiyorsak, daha önce gördüğümüz *üçlü if-else* ifadesini kullanabiliriz.

Söz gelişi, girdi listesindeki sayı beşten büyükse o sayının karesini, değilse sıfırı barındıran bir liste kuralım.

In [16]:

```py
[x*x if x>5 else 0 for x in [1,3,5,7,9,11] ]


```

Out[16]:

```py
[0, 0, 0, 49, 81, 121]
```

Buradaki `if-else` komutunun asıl ifadeye ait olduğuna dikkat edin; liste kurma şartı olarak kullanılmamıştır.

## İç içe döngülerle liste kurma

Diyelim iki ayrı listeden elemanları birleştirerek mümkün bütün çiftleri kurmak istiyoruz, (a,1), (a,2),.., (b,1), (b,2),… gibi. Bunun için birinci listedeki her bir eleman için ikinci listedeki elemanlar üzerinde döngü kurmamız gerek. Yani döngü içinde döngü kurmalıyız. Bunu alışıldık yöntemle şöyle yapabiliriz:

In [17]:

```py
liste = []

for c in "abcd":

    for b in [1,2,3]:

        liste.append((c,b))

liste


```

Out[17]:

```py
[('a', 1),

 ('a', 2),

 ('a', 3),

 ('b', 1),

 ('b', 2),

 ('b', 3),

 ('c', 1),

 ('c', 2),

 ('c', 3),

 ('d', 1),

 ('d', 2),

 ('d', 3)]
```

Aynı işi liste kurma işlemiyle yapmak da mümkündür:

In [18]:

```py
[(c,b) for b in (1,2,3) for c in "abcd"]


```

Out[18]:

```py
[('a', 1),

 ('b', 1),

 ('c', 1),

 ('d', 1),

 ('a', 2),

 ('b', 2),

 ('c', 2),

 ('d', 2),

 ('a', 3),

 ('b', 3),

 ('c', 3),

 ('d', 3)]
```

Başka bir örnek olarak, iki ayrı listeden alınan sayılar ve onların toplamlarından oluşan çokuzlarla bir liste kurabiliriz.

In [19]:

```py
[(a,b,a+b) for b in (1,2,3) for a in (4,5,6)]


```

Out[19]:

```py
[(4, 1, 5),

 (5, 1, 6),

 (6, 1, 7),

 (4, 2, 6),

 (5, 2, 7),

 (6, 2, 8),

 (4, 3, 7),

 (5, 3, 8),

 (6, 3, 9)]
```

Kullanabileceğimiz iç içe döngülerin sınırı yok, istediğimiz kadar derine inebiliriz.

In [20]:

```py
[(a,b,c,a+b+c) for c in (1,2) for b in (3,4) for a in (5,6,7)]


```

Out[20]:

```py
[(5, 3, 1, 9),

 (6, 3, 1, 10),

 (7, 3, 1, 11),

 (5, 4, 1, 10),

 (6, 4, 1, 11),

 (7, 4, 1, 12),

 (5, 3, 2, 10),

 (6, 3, 2, 11),

 (7, 3, 2, 12),

 (5, 4, 2, 11),

 (6, 4, 2, 12),

 (7, 4, 2, 13)]
```

Her `for` ile beraber bir şart ekleyebiliriz.

In [21]:

```py
[(a,b,a+b) for a in (1,2,3,4) if a>2 for b in (5,6,7)]


```

Out[21]:

```py
[(3, 5, 8), (3, 6, 9), (3, 7, 10), (4, 5, 9), (4, 6, 10), (4, 7, 11)]
```

In [22]:

```py
[(a,b,a+b) for a in (1,2,3,4) if a>2 for b in (5,6,7) if b<7]


```

Out[22]:

```py
[(3, 5, 8), (3, 6, 9), (4, 5, 9), (4, 6, 10)]
```

Şartlarımız değişkenlerin hepsini birleştiren bir ifade halinde de olabilir. Örnek olarak, `a+b+c==10` şartını sağlayan bütün üçlüleri bulalım. Tekrarlardan kaçınmak için `b>=a` ve `c>=b` şartlarını da koyalım.

In [23]:

```py
[ (a,b,c) for a in range(1,10) for b in range(a, 10) for c in range(b,10) if a+b+c==10 ]


```

Out[23]:

```py
[(1, 1, 8),

 (1, 2, 7),

 (1, 3, 6),

 (1, 4, 5),

 (2, 2, 6),

 (2, 3, 5),

 (2, 4, 4),

 (3, 3, 4)]
```

Liste kurma ifadesinde solda kalan değişken sağ tarafta tanınır, ama tersi doğru değildir. Aşağıdaki kod yanlış olur:

In [24]:

```py
[ (a,b,c) for b in range(a,10) for a in range(1, 10) for c in range(b,10) if a+b+c==10 ]


```

```py
---------------------------------------------------------------------------

NameError                                 Traceback (most recent call last)

<ipython-input-24-bd9badefae47> in <module>()

----> 1 [ (a,b,c) for b in range(a,10) for a in range(1, 10) for c in range(b,10) if a+b+c==10 ]



NameError: name 'a' is not defined
```

Liste kurmanın yorumlanması sol taraftan başladığı için, yukarıdaki örnekte `a` henüz tanımlanmamış oluyor ve yorumlayıcı hata mesajı veriyor. Bu davranışı anlamak için yukarıda bir önceki örneği döngülerle yazalım:

```py
L = []

for a in range(1,10):

    for b in range(a,10):

        for c in range(b,10):

            if (a+b+c==10):

                L.append((a,b,c))




```

Buradan da görülebileceği gibi, `for b in range(a,10):` satırı önce gelirse, `a`‘nın değeri tanımsız oluyor.

## Genel liste kurma ifadesi ve dengi olan döngüler

Liste kurma ifadesinin en genel hali şöyle yazılabilir:

```py
[ <ifade> for <değişken_1> in <sıralı_1> if <şart_1>

for <değişken_2> in <sıralı_2> if <şart_2>

...

for <değişken_N> in <sıralı_N> if <şart_N> ]




```

Burada `if` kısımları mecburi değil. Bu yapı ilk bakışta yadırgatıcı geliyorsa, aynısının döngü karşılığını göz önünde tutmak faydalı olabilir.

```py
liste = []

for <değişken_1> in <sıralı_1>:

    if <şart_1>:

        for <değişken_2> in <sıralı_2>:

            if <şart_2>:

            ....

                      for <değişken_N> in <sıralı_N>:

                          if <şart_N>:

                              liste.append(<ifade>)
```

## İç içe listeler ve matrisler kurma

Bir önceki bölümde gördüğümüz iç içe `for` döngülerinin tek seviyeli bir liste kurduğuna dikkat edin. Listeye yeni eleman eklemek ancak en içteki döngüde gerçekleşiyor. Eğer bir *listeler listesi* oluşturmak istiyorsak başka bir yaklaşım kullanacağız, yani bir liste kurma işlemini başka birinin içine yerleştireceğiz.

In [25]:

```py
[ [a+b for a in "abc"] for b in "xyz"]


```

Out[25]:

```py
[['ax', 'bx', 'cx'], ['ay', 'by', 'cy'], ['az', 'bz', 'cz']]
```

Bir matris bir listeler listesi olarak yazılabilir. Listenin her elemanı (satır) bir listedir. Sözgelişi, $\left[\begin{array}{ccc}1&2&3\\\\ 4&5&6\\\\7&8&9\end{array}\right]$ matrisini bu şekilde temsil etmek için aşağıdaki yapıyı kullanabiliriz.

In [26]:

```py
[ [3*sütun + satır for satır in [1,2,3] ] for sütun in [0,1,2] ]


```

Out[26]:

```
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

Daha karmaşık bir örnek olarak, *Kronecker delta* $\delta_{i,j}$ matrisi, yani diyagonal elemanları 1, diğer elemanları 0 olan matris bir üçlü if-else ifadesiyle yazılabilir:

In [27]:

```
[ [ 1 if satır==sütun else 0 for sütun in range(5)] for satır in range(5)]


```

Out[27]:

```py
[[1, 0, 0, 0, 0],

 [0, 1, 0, 0, 0],

 [0, 0, 1, 0, 0],

 [0, 0, 0, 1, 0],

 [0, 0, 0, 0, 1]]
```

## Üreteç ifadeler

Yukarıda gördüğümüz liste kurma yapısı, aslında daha genel ve daha verimli olan *üreteç ifadeleri* nin (generator expressions) özel bir durumudur. İlk örneğimizi, bir üreteç olarak şöyle yazabiliriz:

In [28]:

```py
(x*x for x in [1,2,3,4,5])


```

Out[28]:

```
<generator object <genexpr> at 0x7f26157b7a98>
```

Somut bir listeye çevirmek için bu üreteç ifadesini çıplak halde (çevresinde parantezler olmadan) bir `list()` fonksiyonuna verebiliriz. Bu, liste kurma ifadesiyle birebir aynı sonucu verir.

In [29]:

```py
list(x*x for x in [1,2,3,4,5])


```

Out[29]:

```
[1, 4, 9, 16, 25]
```

Üreteçler, sıralı nesneler gibi iterasyonlarda kullanılabilirler. Önemli bir farkları vardır: Bütün elemanları bir seferde yaratılıp bellekte saklanmaz. Bunun yerine, her eleman sırası geldikçe üretilir. Üreteç en son kaldığı yeri aklında tutar.

In [30]:

```py
g = (x*x for x in [1,2,3,4,5])

next(g), next(g), next(g)


```

Out[30]:

```
(1, 4, 9)
```

Üreteci bir döngüde kullanabiliriz:

In [31]:

```py
for i in g:

    print(i)


```

```
16

25


```

Üreteç ifadelerinin listelere göre avantajı daha az yer kaplamalarıdır. Bir listede bütün elemanlar baştan sonra üretilip bellekte saklanırken, bir üreteçte her eleman sadece ihtiyaç duyulduğu anda (söz gelişi, döngüde sırası geldiği zaman) dinamik olarak üretilirler. Özellikle çok elemanlı dizilerde bu önemli miktarda bellek tasarrufu sağlayabilir.

Üreteç ifadeleri, dizili nesne alan fonksiyonlara parametre olarak verilebilir:

In [32]:

```py
sum(1/(x*x) for x in range(1,1001))


```

Out[32]:

```
1.6439345666815615
```

Bir de kendi tanımladığımız fonksiyonla kullanalım.

In [33]:

```py
def çarpım(L):

    """Liste elemanlarının çarpımını döndürür."""

    p = 1

    for x in L:

        p *= x

    return p



çarpım(x+2 for x in range(1,6))


```

Out[33]:

```
2520
```

## Çokuz ve küme kurma

Liste yerine küme kurmak için köşeli parantez `[]` yerine küme parantezi `{}` kullanmak yeterlidir. Aynı kurallar geçerlidir.

In [34]:

```py
{i for i in range(10) if i%3 > 0}


```

Out[34]:

```
{1, 2, 4, 5, 7, 8}
```

Ancak, yuvarlak parantez `()` üreteç kurma için kullanıldığından, çokuz üretmek için üreteci `tuple()` fonksiyonuna vermek gerekir.

In [35]:

```py
tuple( (i,i**2, i**3) for i in range(10) )


```

Out[35]:

```py
((0, 0, 0),

 (1, 1, 1),

 (2, 4, 8),

 (3, 9, 27),

 (4, 16, 64),

 (5, 25, 125),

 (6, 36, 216),

 (7, 49, 343),

 (8, 64, 512),

 (9, 81, 729))
```

## Sözlük kurma

Liste kurma yapısını sözlük kurmaya adapte etmek mümkündür. Sözlük kurma yapısında, ikililerden oluan bir sıralı nesne üzerinden iterasyon yapılır. İkililerin birinci elemanı sözlüğe anahtar, ikinci elemanı ise o anahtara ait değer olarak atanır.

In [36]:

```py
{k:v for k,v in (("a",1),("b",2),("c",6))}


```

Out[36]:

```py
{'a': 1, 'b': 2, 'c': 6}
```

Anahtarlar ve değerler ayrı nesnelerde sıralanmışlarsa, bunlar `zip()` fonksiyonuyla istenen biçime sokulabilir.

In [37]:

```py
anahtarlar = ("a","b","c")

değerler = (1,2,3)

{k:v for k,v in zip(anahtarlar,değerler)}


```

Out[37]:

```py
{'a': 1, 'b': 2, 'c': 3}
```

Bir sözlüğün `items()` metodu anahtar-değer ikililerinden oluşan bir dizi verir. Bu dizi üzerinden iterasyon yaparsak, mevcut bir sözlükteki verilerle yeni bir sözlük oluşturabiliriz.

Söz gelişi, `d` sözlüğündeki değerlerin karesini barındıran yeni bir sözlük oluşturalım:

In [38]:

```py
d = {'a': 1, 'b': 2, 'c': 3}

{k*2:v*v for k,v in d.items()}


```

Out[38]:

```
{'aa': 1, 'bb': 4, 'cc': 9}
```

Bu yöntemle bir sözlüğün anahtar ve değerlerini ters çevirmek çok kolaydır:

In [39]:

```py
{v:k for k,v in d.items()}


```

Out[39]:

```
{1: 'a', 2: 'b', 3: 'c'}
```

Bu son örnekte, iki ayrı anahtarda aynı değer varsa, sonra gelenin öncekini sileceğine dikkat edin.

In [40]:

```py
d = {'a': 1, 'b': 2, 'c': 3, 'd':2}

{v:k for k,v in d.items()}


```

Out[40]:

```py
{1: 'a', 2: 'd', 3: 'c'}
```
