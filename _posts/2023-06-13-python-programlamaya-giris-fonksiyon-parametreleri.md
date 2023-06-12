---
title:  Python Programlamaya Giriş 8 – Fonksiyon Parametreleri
author: sonsuz
date: 2023-06-13 01:25:48 +0300
categories: [Program,Python]
tags: [fonksiyon,python,parametre]
---







Python Programlamaya Giriş yazı dizimize Python fonksiyonlarının temelleriyle devam ediyoruz. 

Bir önceki bölümde Python’da fonksiyonların nasıl yaratıldığından ve nasıl çağrıldığından bahsettik. Bir fonksiyon kapalı bir kutu gibidir: İçinde ne olup bittiğini görmeyiz, parametreler yoluyla bilgi veririz ve cevabı bir değer olarak geri alırız. Bu yazıda parametreleri nasıl kullandığımızı inceleyeceğiz.

## Parametre eşleştirme

Aldığı parametreleri ekrana yazan basit bir fonksiyonu ele alalım:

In [1]:

```python
def f(a,b,c):

    print("a = {}, b = {}, c = {}".format(a,b,c))


```

Bu fonksiyonu çağırırken üç tane parametre değeri vermemiz gerekir:

In [2]:

```
f(1,2,3)


```

```python
a = 1, b = 2, c = 3


```

Fonksiyon, parametre olarak 1,2,3 sayılarını aldı ve bunları sırasıyla kendi içinde tanımlanan `a`, `b`, `c` değişkenlerine atadı. Sonuç olarak ekrana basılanlar da bu atamayla belirlendi.

Buna *konumla eşleştirme* deniyor: Fonksiyon tanımında isimler hangi sırada verildiyse, fonksiyon çağrısında verilen parametreler de aynı sırayla atanır.

In [3]:

```
f(3,2,1)


```

```python
a = 3, b = 2, c = 1


```

Konumla eşleştirmede fonksiyona lüzumundan az veya fazla sayıda parametre vermek bir hata mesajına yol açar.

In [4]:

```
f(1,2)


```

```
---------------------------------------------------------------------------

TypeError                                 Traceback (most recent call last)

<ipython-input-4-c0c95413393f> in <module>()

----> 1 f(1,2)



TypeError: f() missing 1 required positional argument: 'c'
```

In [5]:

```
f(1,2,3,4)


```

```
---------------------------------------------------------------------------

TypeError                                 Traceback (most recent call last)

<ipython-input-5-525f5b13dc35> in <module>()

----> 1 f(1,2,3,4)



TypeError: f() takes 3 positional arguments but 4 were given
```

Parametreleri eşleştirmenin başka bir yolu fonksiyon çağrısında parametre isimlerini kullanmaktır. O zaman tanımlanma sırasına sadık kalmak gerekli olmaz. Bu yönteme *isimle eşleştirme* denir.

In [6]:

```
f(c=4, b=1, a="asdf")


```

```python
a = asdf, b = 1, c = 4


```

Konuma göre ve isme göre eşleştirmeler karıştırılabilir de. Bu durumda, öncelikle soldan sağa doğru konumsal eşleştirmeler yapılır, ardından isim eşleştirmeleri yapılır.

In [7]:

```
f(1, c=3, b=2)


```

```
a = 1, b = 2, c = 3


```

Bir parametre konumla eşleştirilmişse, ardından ayrıca isimle eşleştirmek hata oluşturur.

In [8]:

```
f(1, 2, b=9)


```

```
---------------------------------------------------------------------------

TypeError                                 Traceback (most recent call last)

<ipython-input-8-ac46997206a4> in <module>()

----> 1 f(1, 2, b=9)



TypeError: f() got multiple values for argument 'b'
```

Öncelikli olarak konum eşleştirmesi yapıldığı için, isim eşleştirmelerinden sonra isimsiz bir parametre verilemez.

In [9]:

```
f(1, b=2, 3)


```

```
 File "<ipython-input-9-a17b662ec26d>", line 1

 f(1, b=2, 3)

             ^

SyntaxError: positional argument follows keyword argument


```

İsim eşleştirmeleri kodu daha okunaklı ve anlaşılır kılar. Bir fonksiyon çağrısının ne yaptığını anlamak kolaylaşır. Ayrıca parametrelerin ne sırada verildiğini hatırlamamıza gerek kalmaz. Parametre isimleri de dikkatli şekilde seçilmişse, fonksiyon çağrısının kendisi bir belgeleme gibi iş görür. Meselâ, aşağıdaki fonksiyon çağrısının ne yaptığı hemen anlaşılabilir:

```python
gezegen_ekle( isim="Mars", kutle=0.7, yaricap=0.6, uydu=("Phobos","Deimos") )




```

## Varsayılan değerler

Fonksiyonu tanımlarken, parametrelerine varsayılan değerler atamak mümkündür. Fonksiyon çağrısında bir parametreye değer verilmezse, varsayılan değer kullanılır.

In [10]:

```python
def f(a, b=2, c=3):

    print("a = {}, b = {}, c = {}".format(a,b,c))


```

Bu fonksiyonu çağırırken `a` için bir değer vermek zorundayız, ama `b` ve `c` için varsayılan değerler kullanılabilir. Yani en az bir, en fazla üç parametre değeri verebiliriz. Bu parametreler konuma göre veya isme göre verilebilir.

In [11]:

```python
f(1)    # b ve c varsayılan değerde

f(a = 4)  # b ve c varsayılan değerde

f(1,7)  # c varsayılan değerde

f(1,"hede",6)    # hepsine yeni değer

f(1,c=8)   # b varsayılan değerde


```

```
a = 1, b = 2, c = 3

a = 4, b = 2, c = 3

a = 1, b = 7, c = 3

a = 1, b = hede, c = 6

a = 1, b = 2, c = 8


```

## Belirsiz sayıda parametreler

Bir fonksiyonun kaç tane parametre alacağını önceden belirtmek zorunda da değilsiniz. Fonksiyon tanımını aşağıdaki gibi yaparak bütün konumsal parametrelerin bir çokuza toplanmasını sağlayabilirsiniz.

In [12]:

```python
def f(*par):

    print("Parametreler:", par)


```

In [13]:

```python
f()      # hiç parametre yok, boş çokuz.

f(3)     # tek parametre, tekli çokuz.

f(45, 3-4j, "merhaba", [1,2,3])   # dörtlü çokuz


```

```
Parametreler: ()

Parametreler: (3,)

Parametreler: (45, (3-4j), 'merhaba', [1, 2, 3])


```

Fonksiyonun tanımında `*par` kullanmakla bütün parametrelerin `par` isimli bir çokuza toplanmasını sağladık. Bu çokuzun elementlerini tek tek alarak bütün parametrelere sırayla ulaşabiliriz. Bu şekilde aynı fonksiyonda istediğimiz kadar çok parametre kulanabiliriz. Bu yönteme *parametre paketleme* (argument packing) diyoruz.

Fakat isimle eşleştirme yapmak istersek yukarıdaki tanımıyla fonksiyon doğru çalışmaz, çünkü parametrelere tek tek isim vermedik.

In [14]:

```
f(a=4)


```

```
---------------------------------------------------------------------------

TypeError                                 Traceback (most recent call last)

<ipython-input-14-251e036e5708> in <module>()

----> 1 f(a=4)



TypeError: f() got an unexpected keyword argument 'a'
```

In [15]:

```
f(**{"a":4})


```

```
---------------------------------------------------------------------------

TypeError                                 Traceback (most recent call last)

<ipython-input-15-bb907f52501b> in <module>()

----> 1 f(**{"a":4})



TypeError: f() got an unexpected keyword argument 'a'
```

Böyle bir durumda, parametre paketleme işleminde *çift yıldız* (`**`) kullanırız. O zaman, isimlerle verilmiş bir parametre listesinin bir sözlüğe toplanmasını sağlayabiliriz.

In [16]:

```python
def g(**par):

    print("Parametreler:",par)


```

In [17]:

```
g()

g(a=1, b=4)


```

```
Parametreler: {}

Parametreler: {'a': 1, 'b': 4}


```

Böylece değişken isimlerine ve değerlerine, yukarıdaki tanımda `par` adını verdiğimiz bir sözlük aracılığıyla erişebiliriz. (Elbette `par` ismini kullanmak zorunda değilsiniz). Buradaki dinamik tanıma dikkat edin: `a` ve `b` parametreleri fonksiyonun orijinal tanımında yoktu; bu özel fonksiyon çağrısıyla beraber tanımlandılar.

Ama bu `g()` fonksiyonu da mükemmel değil. Sadece isimlendirilmiş parametrelerle çalışır, isimsiz (konuma dayalı) parametrelerde hata mesajı verir.

In [18]:

```
g(1,2,3)


```

```
---------------------------------------------------------------------------

TypeError                                 Traceback (most recent call last)

<ipython-input-18-c686b5a0ef51> in <module>()

----> 1 g(1,2,3)



TypeError: g() takes 0 positional arguments but 3 were given
```

Daha genel bir fonksiyon arayüzü şöyle yazılabilir.

In [19]:

```
def f( *pargs, **kwargs ):

    print(pargs)    # Konum eşleştirmeli parametreler çokuzu

    print(kwargs)   # İsim eşleştirmeli parametreler sözlüğü


```

In [20]:

```
f()


```

```
()

{}


```

In [21]:

```
f(1, 2, a = "xyz", b = 3.14)


```

```
(1, 2)

{'a': 'xyz', 'b': 3.14}


```

Böyle tanımlanmış bir fonksiyon hem konum hem de isim eşleştirmeli parametrelerle çalışabilir. Birçok hazır kütüphanede, böyle genel bir arayüzle tanımlanmış fonksiyonlar bulunur.

## Parametre çözme

Yukarıda, bir parametre listesini nasıl bir çokuz haline getirebileceğimizi gördük. Tersini de yapmak mümkün: Fonksiyonu çağırırken bir çokuzdan parametreler çıkartabiliriz.

Verilen argümanları ters sırada basan basit bir fonksiyon yazalım ve vereceğimizi parametreleri bir çokuza yazarak fonksiyona verelim.

In [22]:

```python
def f(a,b,c,d):

    print(d,c,b,a)



f(1,5,9,13)


```

```
13 9 5 1


```

In [23]:

```
x = (1,5,9,13)

f(x)


```

```
---------------------------------------------------------------------------

TypeError                                 Traceback (most recent call last)

<ipython-input-23-3a2b3f8aa072> in <module>()

 1 x = (1,5,9,13)

----> 2 f(x)



TypeError: f() missing 3 required positional arguments: 'b', 'c', and 'd'
```

Dört parametre isteyen bir fonksiyonumuz var. Vereceğimiz parametreler `x` isimli bir çokuzda toplanmış. Fonksiyon çağrısını `f(x)` biçiminde yapmanın hataya yol açacağı bariz, çünkü dört parametre bekleyen bir fonksiyona bir tek parametre veriyoruz.

Eğer fonksiyon çağrısını `f(*x)` şeklinde yazarsak `x`‘in elemanları tek tek alınıp parametre olarak `f`‘ye verilir ve sorunsuzca çalışır. Bu işleme *parametre çözme* (argument unpacking) deniyor.

In [24]:

```
f(*x)


```

```
13 9 5 1


```

Parametreler başka bir sıralı veri tipinde (liste, dize) saklanıyorsa da aynı işlem geçerli olur.

In [25]:

```
f(*[1,2,3,4])

f(*"xyzt")


```

```
4 3 2 1

t z y x


```

Fonksiyonda parametre isimlerini `a, b, c, d` olarak tanımlamıştık. Bu isimleri kullanarak isim eşleştirmesi yapmak isteyebiliriz. Burada parametre çözme işlemi uygularken çokuz kullanamayız çünkü çokuzda parametre isimleri mevcut değil, sadece değerler mevcut. Bu durumda parametre çözmeyi `**` notasyonu kullanarak, parametre isimlerini ve değerlerini içeren bir sözlükle yapmalıyız.

In [26]:

```python
D = {'b':2, 'd':4, 'a':1, 'c':3}

f(**D)


```

```
4 3 2 1


```

İki yaklaşımı birleştirmek de mümkün:

In [27]:

```python
f( *(1,2), **{'c':"merhaba", 'd':[5,6]} )


```

```
[5, 6] merhaba 2 1


```
