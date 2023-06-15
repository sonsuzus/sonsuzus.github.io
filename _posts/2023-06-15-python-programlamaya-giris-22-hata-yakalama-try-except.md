---
title:  Python Programlamaya Giriş 22 – Hata yakalama, try/except
author: sonsuz
date: 2023-06-15 17:01:00 +0300
categories: [Program,Python]
tags: [python,try,except,hata yakalama]
---






**Hata yakalama** (exception handling) beklenmedik durumlarda programınızın bir hata mesajı vermesi ve çalışmayı durdurması yerine, hataya kendi istediğimiz şekilde cevap vermesini sağlamanın bir yoludur. Hata yakalama Python programcılığının önemli bir parçasıdır, kaynak kodunu çok karışık hale getirmeden programınızın güvenilir bir şekilde çalışmasını sağlar.

Dizinin bütün yazılarına erişmek için [*Python Programlamaya Giriş*](https://sonsuzus.github.io/categories/python) kategorimize bakabilirsiniz. 

## Hatalı girdiyi yakalamak

Bir örnekle başlayalım: Etkileşimli çalışarak kullanıcıdan sayılar alan ve aldığı sayıların karesini ekrana basan bir program yazalım. Boş satır okuduğunda program sonlansın.

In [ ]:

```py
while True:

    x = input("Bir sayı girin: ")

    if not x:

        break

    print(float(x)**2)


```

Örnek olarak, programımız şöyle çalışabilir.

```py
Bir sayı girin: 1

1.0

Bir sayı girin: -45.5

2070.25

Bir sayı girin: abc

    ---------------------------------------------------------------------------

ValueError                                Traceback (most recent call last)

<ipython-input-1-297c961843d7> in <module>()

      3     if not x:

      4         break

----> 5     print(float(x)**2)



ValueError: could not convert string to float: 'abc'




```

Son girdimiz `"abc"` sayıya dönüştürülemediği için `float()` fonksiyonu bir `ValueError` hatası (Python terimiyle “exception”) verdi. Böyle hatalar programımızın çalışmasını durdurur. Oysa, bir hata yakalama (exception handling) yapısı kullanırsak bu tür sorunları programımızı durdurmadan halletmemiz mümkün olur. Söz gelişi:

In [ ]:

```py
while True:

    x = input("Bir sayı girin: ")

    if not x:

        break

    try:

        y = float(x)

    except ValueError:

        print("Geçersiz sayı")

        continue

    print(y**2)


```

Bu program hatalı girdi verdiğimizde ekrana bir uyarı yazar ve tekrar girdi alır:

```py
Bir sayı girin: 3

9.0

Bir sayı girin: -2

4.0

Bir sayı girin: abc

Geçersiz sayı

Bir sayı girin: 1.5

2.25

Bir sayı girin: 




```

Bu programda, hata mesajı çıkarabilecek bölümü `try:` blokunun içine aldık. Eğer `float(x)` işlemi `valueError` hatası verirse `except ValueError` bloku çalıştırılır, ve kullanıcıya bir uyarı verilerek tekrar döngünün başına dönülür. Bu sayede program durmadan hatayı yakalayıp sorunu gidermiş oluruz.

## Hata tipleri

Yukarıdaki örnekte `ValueError` hatasını yakaladık, ama başka durumlardaki hata isimlerini nereden bileceğiz?

Öncelikle, yazdığınız her kod satırında neler olabileceğini düşünün. Hata durumu (exception) yaratan bir çok durum olabilir: Çağırdığınız fonksiyonda bir sayıyı sıfıra bölüyor olmanız mümkün mü? Bir matematiksel fonksiyona verdiğiniz değişken sayısal olmazsa ne olur? Üçüncü elemanını almaya çalıştığınız listede sadece iki eleman varsa? Açmak istediğiniz dosya diskte mevcut değilse?

Bu hata durumlarının ne olduğunu anlamak için komutları çalıştırıp ne tip hata aldığınıza bakabilirsiniz ve sonra buna göre *try/except* blokları yazabilirsiniz. Yardım belgelerinde de fonksiyonun hangi durumlarda hangi hataları yayınlayacağına dair bilgi mevcuttur.

**Çalışma.** Yukarıdaki hata durumlarını yaratan Python kodları yazın ve hangi hataların yayınlandığına bakın. Bu hataları bir *try/except* yapısı içine koyup uygun bulduğunuz şekilde düzenleyin.

**Çalışma.** `open()` fonksiyonunun yardım belgelerine bakarak hangi durumda hangi hataların yayınlandığını inceleyin.

Python dilindeki ön tanımlı hataların tam listesini ve hangi durumlarda yayınlandıklarını [resmi Python dökümanlarından](https://docs.python.org/3/library/exceptions.html) okuyabilirsiniz.

## Birden fazla hata durumu

Yukarıdaki örneğimizde, `float()` fonksiyonuna yanlış parametre vermekle ortaya çıkan `ValueError` hatasını yakalamıştık. Alternatif olarak şu kodu da kullanabilirdik:

In [ ]:

```py
while True:

    x = input("Bir sayı girin: ")

    if not x:

        break

    try:

        y = 1/float(x)

    except:

        print("Geçersiz sayı")

        continue

    print(y)


```

```py
Bir sayı girin: 0

Geçersiz sayı

Bir sayı girin: abc

Geçersiz sayı

Bir sayı girin: 2

0.5

Bir sayı girin: 
```

Bu değişiklikle `try` bloku içindeki *herhangi* bir hata ile `except` bloku çalıştırılır. Ancak, bu yaklaşımda farklı hataların hepsi aynı `except` blokuna yönlendirilir. Söz gelişi, yukarıda girdi olarak 0 verdiğimizde de ekrana `"Geçersiz sayı"` yazılır. Oysa bu iki ayrı hata durumunun ayrı şekilde düzenlenmesini isteyebiliriz. O zaman iki farklı `except` bloku kullanırız:

In [ ]:

```py
while True:

    x = input("Bir sayı girin: ")

    if not x:

        break

    try:

        y = 1/float(x)

    except ValueError:

        print("Geçersiz sayı")

        continue

    except ZeroDivisionError:

        print("Sıfıra bölme")

        continue

    print(y)


```

Bu program farklı hatalar için farklı uyarılar gösterir:

```py
Bir sayı girin: abc

Geçersiz sayı

Bir sayı girin: 0

Sıfıra bölme

Bir sayı girin: 4

0.25

Bir sayı girin: 
```

## Hata durumu hiyerarşisi

Hata durumları bir nesne hiyerarşisi içinde tanımlanır. Bunların en geneli `BaseException` sınıfıdır; diğer daha özelleşmiş hata durumları bunlardan türetilir.

Hata durumları hiyerarşisinin bir bölümü şöyledir (tam bir listeyi [Python belgelerinde](https://docs.python.org/3/library/exceptions.html#exception-hierarchy) bulabilirsiniz):

```py
BaseException

 +-- SystemExit

 +-- KeyboardInterrupt

 +-- Exception

      +-- StopIteration

      +-- StopAsyncIteration

      +-- ArithmeticError

      |    +-- FloatingPointError

      |    +-- OverflowError

      |    +-- ZeroDivisionError

      +-- ImportError

      |    +-- ModuleNotFoundError

      +-- LookupError

      |    +-- IndexError

      |    +-- KeyError

      +-- OSError

      +-- ValueError
```

Bu hiyerarşi sebebiyle, alt seviye bir hatayı yayınlayan bir kod, onun üstündeki hataları da yayınlar. Söz gelişi, `1/0` işlemi `ZeroDivisionError`, `ArithmeticError`, `Exception` ve `BaseException` hatalarının hepsine uyar.

Bir try/except yapısında bir hata durumu belirtmezsek en genel durum olan `BaseException` yayınlanır.

In [1]:

```py
try:

    1/0

except:

    print("Bir hata oldu.")


```

```
Bir hata oldu.


```

Ama böyle bir kullanım, okunaklı yazılım geliştirme açısından doğru değildir. Eğer `try` blokumuz genişse ve birden fazla farklı hata olması ihtimali varsa, hepsi birden bu mesajı verir, ve hangi hatanın gerçekleştiğini tespit etmemiz mümkün olmaz.

In [2]:

```py
try:

    int("abc")

except:

    print("Bir hata oldu.")


```

```
Bir hata oldu.


```

Belirsizliği azaltmak için en iyi yol, hiyerarşide en alt noktadaki (en dar kapsamlı) hata durumunu yakalamak ve ona göre ayrı `except` blokları içinde sorunu gidermektir.

In [3]:

```py
try:

    2.5**1000

except OverflowError:

    print("İşlem çok büyük.")

except ZeroDivisionError:

    print("Sıfıra bölme.")


```

```
İşlem çok büyük.


```

Hatta, yaptığınız işlemin yeni bir hata durumu olmasını da sağlayabilirsiniz. Öntanımlı hata durumlarından yeni hatalar türetmeyi aşağıda göreceğiz.

## Fonksiyonlarımızda hata durumu yayınlamak

Gördüğümüz gibi birçok Python fonksiyonu normal işleyişe uymayan durumlarda bir hata durumu yayınlıyor, ve programımızda bu hata durumunu yakalayarak işlem yapıyoruz. Kendi yazdığımız fonksiyonların içinde `raise` komutu kullanarak bir hata durumu yayınlanmasını sağlayabiliriz. Örnek olarak, negatif argüman aldığında `ValueError` yayınlayan bir faktöriyel fonksiyonu yazalım. Hata mesajını değiştirmemiz de mümkündür:

In [4]:

```py
def faktöryel(x):

    x = int(x)    

    if x<0:

        raise ValueError("Negatif değer")

    p = 1

    for i in range(1,x+1):

        p *= i

    return p


```

Şimdi bu fonksiyonu bir try/except bloku içinde kullanalım.

In [5]:

```py
for x in [5, -5, "abc", 5]:

    try:

        y = faktöryel(x)

    except ValueError as e:

        print(x,": ", e)

        continue

    print(y)


```

```
120

-5 :  Negatif değer

abc :  invalid literal for int() with base 10: 'abc'

120


```

Bu koddaki `except ValueError as e:` komutu ile hata durumu `e` isimli bir yerel değişkende saklanabilir ve blok içinde kullanılabilir. Yukarıdaki gibi `print()` içinde kullanıldığında hata mesajını ekrana basarız. Negatif girdi ve harf girdisi durumlarında farklı hata mesajları çıktığına dikkat edin.

## Yeni hata durumları yaratmak

Python’un standart hata durumlarına ek olarak, kendi hata durumlarımızı da yaratabiliriz. Yukarıda gördüğümüz hata durumu hiyerarşisi, aslında bir nesne hiyerarşisidir. Nesne sınıfları tanımlamayı sonraki bölümlerde göreceğiz, ama buradaki örneği nesne programlama bilmeden de uygulayabilirsiniz.

Yeni bir hata tanımlarken varolan bir hatayı temel alırız. Söz gelişi, genel `Exception` nesne sınıfından türetilmiş bir `VektörBoyuHatası` tanımlayalım.

In [6]:

```py
class VektörBoyuHatası(Exception):

    pass


```

Buradaki `pass` kelimesi etkisiz bir komuttur. Python sözdizimi gereğince doldurulması gereken bir yere herhangi bir kod koymak istemediğimizde kullanırız.

Şimdi iki sayı listesinin iç çarpımını veren bir fonksiyon yazalım. Listeler aynı uzunlukta değilse iç çarpım tanımlı olmaz; bu durumda `VektörBoyuHatası` yayınlayalım.

In [7]:

```py
def iç_çarpım(L1, L2):

    if len(L1)!=len(L2):

        raise VektörBoyuHatası("Parametreler aynı sayıda elemandan oluşmalı.")

    return sum( [a*b for (a,b) in zip(L1,L2)] )


```

In [8]:

```
iç_çarpım([1,2,3], [-1,0,1])


```

Out[8]:

```
2
```

In [9]:

```
iç_çarpım([1,2,3,4], [-1,0,1])


```

```py
---------------------------------------------------------------------------

VektörBoyuHatası                          Traceback (most recent call last)

<ipython-input-9-5f70170b4bfa> in <module>()

----> 1 iç_çarpım([1,2,3,4], [-1,0,1])



<ipython-input-7-ec326e885a8f> in iç_çarpım(L1, L2)

 1 def iç_çarpım(L1, L2):

 2     if len(L1)!=len(L2):

----> 3         raise VektörBoyuHatası("Parametreler aynı sayıda elemandan oluşmalı.")

 4     return sum( [a*b for (a,b) in zip(L1,L2)] )



VektörBoyuHatası: Parametreler aynı sayıda elemandan oluşmalı.
```

Bu fonksiyonu bir try/except yapısı içinde kullanabiliriz:

In [10]:

```py
try:

    iç_çarpım([1,2,3,4], [-1,0,1])

except VektörBoyuHatası as e:

    print(e)


```

```
Parametreler aynı sayıda elemandan oluşmalı.


```
