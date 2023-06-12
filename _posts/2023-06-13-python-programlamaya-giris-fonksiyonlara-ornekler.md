---
title:  Python Programlamaya Giriş 9 – Fonksiyonlara Örnekler
author: sonsuz
date: 2023-06-13 01:33:03 +0300
categories: [Program,Python]
tags: [python,fonksiyon]
math: true
---




Önceki yazılarda verdiğimiz basit örneklerin ötesine geçip biraz daha elle tutulur fonksiyon örnekleri verelim.

* Asallık testi
* Asal çarpanlar
* Standart sapma
* Collatz dizisi uzunluğu
* Taylor serisiyle üstel fonksiyon

## Asallık testi

[Döngülerden bahsederken](https://sonsuzus.github.io/posts/python-programlamaya-giris-donguler/), bir sayının asal olup olmadığını belirleyen bir program yazmıştık. Şimdi bunu bir fonksiyon haline getirelim. Parametre değeri bir asal sayıysa fonksiyonumuz `True` verecek, değilse `False` verecek.

In [1]:

```python
def asal_mı(x):

    i = 2

    while i*i <= x:

        if x % i == 0:

            return False

        i += 1

    else:

        return True


```

In [2]:

```
asal_mı(8)


```

Out[2]:

```
False
```

In [3]:

```
asal_mı(79)


```

Out[3]:

```
True
```

## Asal çarpanlar

[Önceki bir bölümde](https://sonsuzus.github.io/posts/python-programlamaya-giris-dongulerle-problem-cozme/) bir sayının asal çarpanlarını ekrana basan bir döngü yazmıştık. O döngüyü bir fonksiyon içine koyalım ve verilen sayının asal çarpanları bir liste olarak geri verilsin.

In [4]:

```python
def asalçarpanlar(N):

    çarpanlar = []  # boş liste 

    x = 2

    while N > 1:

        # x asal mı?

        asal = True

        i = 2

        while i*i <= x:

            if x % i == 0:

                asal = False

                break

            i += 1



        if asal and N % x == 0:  # x asalsa ve N'yi bölüyorsa...

            çarpanlar.append(x)  # x'i listenin sonuna ekle

            while N % x == 0 :   # N x'e bölünebildiği sürece...

                N = N / x        # N'yi x'e böl, x çarpanı kalmasın.

        x += 1

    return çarpanlar


```

In [5]:

```
asalçarpanlar(600851475143)


```

Out[5]:

```
[71, 839, 1471, 6857]
```

Bu fonksiyonu, yukarıda tanımladığımız `asal_mı()` fonksiyonunu kullanarak kısaltabiliriz.

In [6]:

```python
def asalçarpanlar(N):

    çarpanlar = []  # boş liste 

    x = 2

    while N > 1:

        if asal_mı(x) and N % x == 0:   # x asalsa ve N'yi bölüyorsa...

            çarpanlar.append(x)         # x'i listenin sonuna ekle.

            while N % x == 0 :          # N x'e bölünebildiği sürece...

                N = N / x               # N'yi x'e böl, x çarpanı kalmasın.

        x += 1

    return çarpanlar



asalçarpanlar(600851475143)


```

Out[6]:

```
[71, 839, 1471, 6857]
```

## Standart sapma

Elimizde $N$ tane $x_1, x_2,\ldots,x_N$ sayısı olsun. Sayıların ortalamasına $\bar{x}$ diyelim. Bu sayıların standart sapması şöyle tanımlanır:

$$ \sigma = \sqrt{ \frac{1}{N-1} \left[ (x_1-\bar{x})^2 + (x_2-\bar{x})^2 + \ldots + (x_N-\bar{x})^2\right]}$$

Belirsiz sayıda parametre alan ve bu parametrelerin standart sapmasını veren `stdsap()` isimli bir fonksiyon yazalım. Standart sapmanın tanımlanabilmesi için fonksiyon en az iki parametre almalı. Bunun dışında parametre sayısında bir kısıtlama olmayacak. Bu şartı sağlamak için fonksiyon arayüzünü `stdsap(x1, x2, *y)` şeklinde yazmamız gerekir.

In [7]:

```python
import math   # karekök için



def stsapma(x1, x2, *y):

    N = len(y) + 2 # Fonksiyona verilen parametre sayısı



    # ortalamayı hesapla

    toplam = x1 + x2

    for z in y:

        toplam += z

    ort = toplam / N



    karetoplam = (x1-ort)**2 + (x2-ort)**2

    for z in y:

        karetoplam += (z-ort)**2

    stsap = math.sqrt(karetoplam / (N-1))



    return stsap


```

In [8]:

```
print(stsapma(1,2))

print(stsapma(1,2,2,3,3,3,3,4,4,5,5))


```

```
0.7071067811865476

1.250454462839956


```

Tipik bir uygulamada, verileri önceden kullanıcıdan veya bir dosyadan tek tek almış ve bir listeye yazmış olabilirsiniz. O durumda parametre çözme (link) kullanarak listeyi bu fonksiyona parametre olarak verebilirsiniz.

In [9]:

```
data = [1,2,2,3,3,3,3,4,4,5,5]

stsapma( *data )


```

Out[9]:

```
1.250454462839956
```

## Collatz dizisi uzunluğu

Collatz dizisini [önceki bölümlerde görmüştük](https://sonsuzus.github.io/posts/python-programlamaya-giris-dongulerle-problem-cozme/). Bir dizide belli bir $n_0$ sayısından başlayıp $n_1$’i buluruz, $n_1$ ile $n_2$’yi buluruz, ve böyle gider. Collatz dizisinde bir sonraki sayıyı bulma kuralı şöyledir:

* $n_i$ çift sayıysa: $n_{i+1} = n_i/2$
* $n_i$ tek sayıysa: $n_{i+1} = 3n_i+1$
* $n_i = 1$ ise dur.

Söz gelişi, 13 ile başlayan bir dizi aşağıdaki gibi olur.

```
13, 40, 20, 10, 5, 16, 8, 4, 2, 1




```

Collatz dizisi, bildiğimiz kadarıyla, hangi sayıyla başlarsak başlayalım hep 1’e gelir ve durur (ama bunun her zaman böyle olacağı ispat edilememiştir). Öyle bir fonksiyon yazalım ki, verilen bir başlangıç değeriyle Collatz dizisini üretsin ve 1’e kaç adımda ulaşıldığını saysın. Bunu yaparken dizinin en fazla kaça çıktığını da kaydetsin ve bu iki değeri geri versin.

In [10]:

```py
def collatz_uzunluk(n):

    enbüyük = n

    uzunluk = 0

    while n > 1:

        if n % 2==0:

            n = n/2

        else:

            n = 3*n + 1



        uzunluk += 1

        if n > enbüyük:

            enbüyük = n

    return uzunluk, enbüyük


```

In [11]:

```py
for n0 in [11, 79]:

    u, m = collatz_uzunluk(n0)

    print("Başlangıç = {}, dizi uzunluğu = {}, en büyük değer = {}".format(n0, u, m))


```

```
Başlangıç = 11, dizi uzunluğu = 14, en büyük değer = 52.0

Başlangıç = 79, dizi uzunluğu = 35, en büyük değer = 808.0


```

11 ile başlayan Collatz dizisi 14 adım sonra 1’e ulaşıyor ve arada aldığı en büyük değer 52. Diziyi 79 ile başlatırsak 1’e ulaşana kadar 35 adım atıyor; ara değerler 808’e kadar çıkıyor.

## Taylor serisiyle üstel fonksiyon

[Döngü alıştırmaları bölümünde](https://sonsuzus.github.io/posts/python-programlamaya-giris-dongu-alistirmalari/) üstel fonksiyon $e^x$ değerini Taylor serisi ile bulmaktan bahsetmiştik.

$$ e^x = \sum_{n=0}^{\infty} \frac {x^n}{n!} = 1 + x + \frac{1}{2}x^2 + \frac{1}{6}x^3 + \cdots$$

Bu açılımı kullanarak, üstel fonksiyonu bir Python fonksiyonu olarak yazalım.

Bu serinin sonsuz terimi olduğu için bir yerde kesmek zorundayız. Bu kesme bir hataya yol açacak, ve biz ne kadarlık bir hataya göz yumabileceğimizi (toleransımızı) önceden belirleyeceğiz. Her yeni terim bir öncekinden küçük olduğu için, yeni terim toleranstan küçükse hesabı durduracağız.

Ayrıca, kaç tane terim kullanabileceğimizin katı bir sınırı da olacak. Belki öyle bir $x$ sayısı ile başlarız ki, seriye ne kadar terim eklersek ekleyelim bir türlü toleransın altına inemeyiz. Tabii bu serinin her $x$ değeri için yakınsak olduğunu biliyoruz, ama bu ek emniyet tedbiri bu tür iteratif algoritmalarda genelde faydalıdır. Eğer azami terim sayısına ulaşılmasına rağmen terimler toleransın altına inmediyse ekrana bir uyarı mesajı basılsın ve fonksiyon elde ettiği sonucu geri versin.

Tolerans ve azami terim sayısı için makul varsayılan değerler verelim, böylece fonksiyonu kullanırken her seferinde yazmak zorunda kalmayalım. Sadece deney yapmak istediğimizde değiştirelim.

In [12]:

```py
def üstel(x, hata = 1e-8, maxterim = 20):

    n = 1

    sonterim = 1 # serideki ilk terimimiz

    toplam = sonterim

    while sonterim >= hata:

        if n > maxterim :

            print("{} terimde yakınsama sağlanamadı".format(maxterim))

            break

        sonterim = sonterim * x/n # yeni terim bir öncekini x ile çarpıp terim sıra numarasına bölerek bulunuyor.

        toplam += sonterim

        n += 1

    return toplam


```

Fonksiyonumuzu standart kütüphanedeki üstel fonksiyonla karşılaştıralım:

In [13]:

```py
import math

print(math.exp(2))

print(üstel(2))


```

```
7.38905609893065

7.389056098516415


```

Virgülden sonra dokuz basamağa kadar uyum sağlanıyor. Daha iyi uyum için toleransı küçültebiliriz. Ama çok küçültürsek yirmi terim yeterli olmayacaktır.

In [14]:

```
üstel(2, hata=1e-15)


```

```
20 terimde yakınsama sağlanamadı


```

Out[14]:

```
7.389056098930604
```

Bu sınıra takılmadan daha yüksek hassasiyet sağlamak için `maxterim` değerini artırabiliriz.

In [15]:

```
print(math.exp(2))

print(üstel(2, hata=1e-15, maxterim=30))


```

```
7.38905609893065

7.389056098930649


```

Büyük $x$ değerleri kullanmak da varsayılan terim sayısının yetmemesine sebep olabilir.

In [16]:

```
üstel(10)


```

```
20 terimde yakınsama sağlanamadı


```

Out[16]:

```
21991.482025665064
```

In [17]:

```py
print(math.exp(10))

print(üstel(10, maxterim=50))


```

```
22026.465794806718

22026.46579480579


```

Burada bir örnek olsun diye üstel fonksiyon için kod yazdık, ama pratik uygulamalarda bu kodu kullanmamalısınız. Matematiksel işlemler için Python’un matematik kütüphanesini kullanmanız daha iyi olur. Bu kütüphane C dilinde yazılmış ve derlenerek makine diline çevrilmiş kod kullandığı için çok daha hızlıdır. Tek çalıştırmada bu hız farkı çok belli olmasa da çok sayıda işlem yapıldığında ciddi bir fark görülür.

In [18]:

```
%timeit üstel(2)


```

```
3.11 µs ± 584 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)


```

In [19]:

```py
%timeit math.exp(2)


```

```
138 ns ± 6.25 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)


```

Görüldüğü gibi `math.exp` fonksiyonu işlemi 140 nanosaniyede yaparken, bizim yazdığımız `üstel` fonksiyonuyla yapılan işlem yaklaşık 3 mikrosaniye sürüyor, yirmi kat yavaş. Üstelik `math.exp` daha yüksek hassasiyette sonuç veriyor ve fazladan kontroller içeriyor.

Meraklısı için: `math.exp` içinde üstel fonksiyon Taylor serisiyle hesaplanmaz. Python matematik işlemlerinde C dilinin standart matematik kütüphanesini kullanır. Bu kütüphanede üstel fonksiyon hızlı ve isabetli hesaplanabilecek şekilde özel olarak düzenlenmiştir. C’de üstel fonksiyonun tanımı [şurada](http://www.netlib.org/fdlibm/e_exp.c) görülebilir. Özetle, önce öyle bir tamsayı $k$ ve $|r|<0.5\ln 2$ sağlayan reel sayı $r$ bulunur ki, parametremiz $x = k\ln 2 + r$ biçiminde olsun. O zaman $e^x = 2^k + e^r$ şeklinde yazılabilir. Bunun avantajı şudur: Bilgisayarda 2’nin tamsayı kuvvetini almak kolaydır (sayı bitlerini sola kaydırmak yeter). Kalan $r$ sayısı küçük olduğu için $e^r$ içinse yüksek hassasiyetli özel bir formül kullanılabilir. Ara hesaplar, bayt seviyesi işlemler kullanılarak mümkün olduğunca hızlandırılır.
