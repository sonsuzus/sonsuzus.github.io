---
title:  Python Programlamaya Giriş 18 – Python referans modeli, sığ ve derin kopyalama
author: sonsuz
date: 2023-06-14 18:09:22 +0300
categories: [Program,Python]
tags: [python,nesne,referans,kopyalama]
---






Python Programlamaya Giriş yazı dizimizin bu bölümünün konusu, Python’da isimler ve nesnelerin eşleştirilmesinin ayrıntıları, ve bu ayrıntıların bazen nasıl bizi şaşırtabileceği. Dizinin bütün yazılarına erişmek için [*Python Programlamaya Giriş*](https://sonsuzus.github.io/categories/python) kategorimize bakabilirsiniz. 

## Nesneler ve referanslar

Elimizde `a` isimli bir liste olsun. Diyelim bu listeyi kopyalayıp `b` isimli ikinci ve eş bir liste yaratmak istiyoruz. İlk aklımıza gelen şeyi yapalım ve basit bir atama yapalım.

In [1]:

```py
a = [1,2,3]

b = a

b


```

Out[1]:

```py
[1, 2, 3]
```

Şimdi `a`‘yı bir kenara bırakalım ve `b` ile çalışalım. Sözgelişi, `b`‘nin ikinci elemanını değiştirelim.

In [2]:

```
b[1] = "abc"

b


```

Out[2]:

```py
[1, 'abc', 3]
```

Ancak, bu değişiklik `b` ile sınırlı kalmaz, `a`‘yı da etkiler.

In [3]:

```
a


```

Out[3]:

```py
[1, 'abc', 3]
```

Birçok başka programlama dilinde görülmeyen bu davranışın nedenini anlamak için Python’un atamaları nasıl yaptığına bakmamız gerekiyor.

Basit bir atamayla başlayalım. Yorumlayıcı `a = 42` gibi bir atama ifadesi gördüğünde iki şey yapar: 42 değerini taşıyan bir tamsayı nesnesi yaratır, ayrıca bir `a` ismi yaratır, ve bu ismi 42 nesnesine bağlar. İsim ve işaret ettiği nesne birbirlerinden bağımsız varlıklardır.

![](p18-1.png)

İsimlerle nesneler birbirinden ayrıldığı için, Python’da değişkenlerin ne tipte olduğunu (tamsayı, karakter, vs) deklare etmeniz gerekmez. Aynı isim çok farklı tipte nesnelere aktarılabilir. Mesela hemen ardından `a = "merhaba"` komutu verirsek yorumlayıcı `"merhaba"` dizesini barındıran bir nesne yaratır, ve `a` ismini bu yeni dizeye bağlar.

![](p18-2.png)

Bu değişiklikten sonra olunca 42’ye ne olur? Eğer ona referans veren başka bir isim varsa yerinde kalır, yoksa silinir. Her nesneyle beraber ona kaç referans verildiğinin sayısı tutulur. Bu sayı sıfıra indiğinde “çöp toplayıcı” o nesneyi bellekten kaldırır.

`a` değişkenini `"merhaba"`ya bağladıktan sonra `b = a` gibi bir atama yapıldığında `"merhaba"`ya bir de `b` ismi bağlanır. Şimdi aynı nesnenin iki farklı ismi vardır.

In [7]:

```py
a = "merhaba"

b = a

b is a


```

Out[7]:

```
True
```

Burada kullandığımız `is` işleminin `True` vermesi iki ismin aynı nesneye işaret ettiğini gösterir. Yani `a` ve `b`‘deki değerler eşit olmakla kalmıyorlar, aynılar.  

![](p18-3.png)

Şimdi yukarıdaki davranışı daha iyi anlayabiliyoruz. Yaptığımız atamalar sonucunda `a` ve `b` aynı listeye işaret ettiğinden, `b` ismi aracılığıyla yapılan bir değişiklik `a` ismine de yansır.

In [9]:

```py
a = [1,2,3]

b = a

a is b, a[0] is b[0]


```

Out[9]:

```
(True, True)
```

Bunu daha iyi görmek için [Python Tutor](http://pythontutor.com/) sitesinden, Python kodunun işletilme aşamalarını görsel olarak sunan bir programcığı kullanabiliriz (internet bağlantısı gerektirir).  

Aynı davranış fonksiyonlarda da görülür. Bir fonksiyon parametre olarak bir liste alır ve listeyi kendi içinde değiştirirse, orijinal liste de değişir.

In [12]:

```py
def f(x,L):

    L[0] = x  # L'nin ilk elemanına x'i ata.



a = [1,2,3]

f("merhaba",a)

a


```

Out[12]:

```
['merhaba', 2, 3]
```

## Sığ ve derin kopyalama

Peki ne yapmalıyız? Doğrudan atama yapmak yerine, listenin `copy()` metodunu kullanmamız gerekir. Bu metod ile elde ettiğimiz kopyayı yeni bir isme atadığımızda, artık iki isim aynı nesneye işaret etmez, ve birinde yapılan değişiklik öbürüne aktarılmaz.

In [13]:

```py
a = [1,2,3]

b = a.copy()

print("a is b?", a is b)

print("a == b?", a == b)


```

```py
a is b? False

a == b? True


```

Burada `a` ve `b` aynı değerleri taşıyan ama birbirinden ayrı iki liste oldu. Artık birini değiştirmek öbürünün de değişmesine sebep olmayacak.

![](p18-4.png)

In [15]:

```py
b[0] = "abc"

b


```

Out[15]:

```py
['abc', 2, 3]
```

In [16]:

```
a


```

Out[16]:

```
[1, 2, 3]
```

`copy()` metodu listelerin yanı sıra sözlükler ve kümelerde de mevcuttur. Çokuz ve dizelerde bulunmazlar, ama zaten onlar değiştirilemez (immutable) nesneler oldukları için elemanlarına atama yapılamaz.

Sıralı nesnelerde (liste, çokuz, dize, vs.) dilimleme işlemi de bir kopya üretmek için kullanılabilir. Böylece bir `a` nesnesini kopyalamak için `a[:]` yazımı kullanılabilir.

In [17]:

```py
a = [1,2,3]

b = a[:]

a is b


```

Out[17]:

```
False
```

Ancak, gerek `copy()` metodu gerekse de `a[:]` işlemi *sığ bir kopya* üretir. Başka bir deyişle, liste elemanlarını birebir kopyalarlar. Ama ya liste elemanının kendisi bir listeyse? O zaman aynı problem daha derin bir seviyede karşımıza çıkar.

In [18]:

```py
a = [5, [4,9,3], 7.1]

b = a.copy()

b[0] = 8                # a'yı değiştirmez

print("a =",a)

print("b =",b)


```

```
a = [5, [4, 9, 3], 7.1]

b = [8, [4, 9, 3], 7.1]


```

In [19]:

```py
b[1][0] = "merhaba"     # a'yı değiştirir

print("a =",a)

print("b =",b)


```

```py
a = [5, ['merhaba', 9, 3], 7.1]

b = [8, ['merhaba', 9, 3], 7.1]


```

Aynı sorunla karşılaşmamızın sebebi, `a`‘nın ikinci elemanının bir referans barındırmasıdır. `copy()` metoduyla kopyalanan da bu referanstır, listenin kendisi değil.

![](p18-5.png)

Derin seviyelerde kusursuz kopyalama yapabilmek için `copy` modülü içindeki `deepcopy()` fonksiyonunu kullanmak gerekir.

In [21]:

```py
import copy



a = [5, [4,9,3], 7.1]

b = copy.deepcopy(a)



b[1][0] = "merhaba"

print("a =",a)

print("b =",b)


```

```py
a = [5, [4, 9, 3], 7.1]

b = [5, ['merhaba', 9, 3], 7.1]


```

Bu sefer derin kopyalama yaptığımız için, `b`‘de yaptığımız hiç bir değişiklik artık `a`‘ya yansımıyor.

## Liste-sayı çarpımı referansları kopyalar

Son bir örnek olarak, çarpma işlemiyle çoğaltılmış bir listeler listesini ele alalım.

In [22]:

```py
L = [[1,2,3]]*4

L


```

Out[22]:

```py
[[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]
```

Bildiğimiz gibi bir listeyle bir sayıyı çarpmak, o listenin elemanlarının o sayı kadar tekrarlandığı yeni bir liste yaratır. Burada da beş tane listeden oluşan bir listemiz var. Bu listenin birinci elemanındaki elemanlardan birine bir atama yapalım.

In [23]:

```py
L[0][0] = "abc"

L


```

Out[23]:

```py
[['abc', 2, 3], ['abc', 2, 3], ['abc', 2, 3], ['abc', 2, 3]]
```

Bu davranışın sebebi liste elemanlarının kendilerinin değil referanslarının kopyalanarak listeye konması. Nitekim `is` işlemi ile kontrol ettiğimizde elemanların aynı nesne olduğunu görüyoruz.

In [24]:

```
L[0] is L[1]


```

Out[24]:

```
True
```

![](p18-6.png)

Çarpımla çoğaltılan listelerde elemanların değil referansların kopyalanması genel olarak verimlilik sağlayan bir özellik. Aynı nesneleri dört kere değil bir milyon kere çoğalttığımızı düşünün; kopyalamakla gereksiz yere bellek işgal etmiş oluruz. Yine de eğer gerçek kopyalama istiyorsak, `deepcopy()` fonksiyonunu liste kurma işlemi ile beraber şu şekilde kullanabiliriz.

In [26]:

```py
L = [copy.deepcopy(i) for i in [[1,2,3]]*4]

L


```

Out[26]:

```py
[[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]
```

Böylece elemanlar aynı nesne olmaktan çıkar ve birine yapılan atama diğerlerini etkilemez.

In [27]:

```
L[0] is L[1]


```

Out[27]:

```
False
```

In [28]:

```py
L[0][0]="abc"

L


```

Out[28]:

```py
[['abc', 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]
```
