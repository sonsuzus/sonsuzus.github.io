---
title:  Python Programlamaya Giriş 5 – Döngülerle Problem Çözme
author: sonsuz
date: 2023-06-12 19:58:52 +0300
categories: [Program,Python]
tags: [python,döngü,problem]
math: true
---





## Asal sayıları listelemek

Verilen bir (N) sayısından küçükeşit bütün asalları listeleyen bir program yazalım.

Bir önceki yazıda, belli bir sayının asal olup olmadığını tespit eden bir program yazmıştık. Burada, o programı 2 ile $N$ arasındaki her tamsayı için çalıştıracağız.

In [1]:

```python
N = int(input("Bir pozitif tamsayı girin: "))

x = 2

while x <= N:

    i = 2

    while i*i <= x:

        if x % i == 0:

            break

        i += 1

    else:

        print(x)

    x += 1


```

```python
Bir pozitif tamsayı girin: 20

2

3

5

7

11

13

17

19


```

Gördüğünüz gibi, verilen bir sayının asallığını tespit etmek için kullandığımız döngünün etrafına bir döngü daha sararak $N$’ye kadar olan bütün sayıları yokluyoruz.

**Alıştırma.** Yukarıdaki programı değiştirerek ilk $k$ asal sayıyı basmasını sağlayın. Yani, meselâ 6 girildiğinde 2, 3, 5, 7, 11, 13 sayılarını çıkarsın.

## Verilen bir sayının asal çarpanlarını listelemek

Bu öncekine göre biraz daha zahmetli bir iş, ama ilkokulda öğrendiğimiz yöntemi uyarlamak yeterli.

Verilen sayıya $N$ diyelim. Bir $x$ değişkenine başta 2 atayalım. Eğer $x$ asal sayıysa, ve $N$ sayısı $x$’e bölünüyorsa, $x$’i ekrana basalım. Ardından $N$’yi $x$’e bölebildiğimiz kadar bölelim, böylece içinde $x$ çarpanı kalmasın. $N$ birden büyük olduğu sürece, $x$’i bir artırıp tekrarlayalım.

In [2]:

```python
N = int(input("Bir pozitif tamsayı girin: "))

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



    if asal and N % x == 0:

        print(x, end=" ")

        while N % x == 0 :

            N = N / x

    x += 1


```

```python
Bir pozitif tamsayı girin: 13860

2 3 5 7 11
```

Bu programdaki döngüde `else` kullanmadık.

## Fibonacci dizisi

Temel programlama derslerinin olmazsa olmazı Fibonacci dizisi şöyle tanımlanır:

$$\begin{array}{rcl} F_0 &=& 1 \\ F_1 &=& 1 \\ F_n &=& F_{n-1} + F_{n-2}\end{array}$$

Yani, dizideki her terim, önceki iki terimin toplamıdır. Dizideki sayılar şöyle gider: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, …

Fibonacci dizisinin ilk elli terimini ekrana yazacak bir program yazalım.

In [3]:

```python
a, b = 1, 1

print(a)

print(b)

i = 2

while i<=50:

    a,b = b, a+b

    print(b)

    i += 1


```

```
1

1

2

3

5

8

13

21

34

55

89

144

233

377

610

987

1597

2584

4181

6765

10946

17711

28657

46368

75025

121393

196418

317811

514229

832040

1346269

2178309

3524578

5702887

9227465

14930352

24157817

39088169

63245986

102334155

165580141

267914296

433494437

701408733

1134903170

1836311903

2971215073

4807526976

7778742049

12586269025

20365011074


```

Döngüde, Python’a özgü bir çokuz ataması yaptığımıza dikkat edin:

```python
a,b = b, a+b


```

Bu işlemin sonunda `b`‘nin eski değeri `a`‘ya, `a+b` toplamının eski değeri de `b`‘ye atanır. Başka dillerde çokuz ataması bulunmayabilir. Aynı işi başka türlü nasıl yaparız? İlk akla gelen şey şu olabilir:

```python
a = b

b = a + b   # yanlış


```

Bu yanlış, çünkü ikinci atamada eşitliğin sağ tarafında `a`‘nın yeni değeri kullanılıyor. Bir önceki ifadede `a`‘ya `b`‘nin değerini atamıştık. Böylece atamanın sonunda sadece `b`‘yi iki katına çıkarmış oluruz.

Doğru yöntem, eski değerler için ayrı değişkenler kullanmaktır. Yukarıdaki programı bu yaklaşımla tekrar yazalım:

In [ ]:

```python
a = 1

b = 1

print(a)

print(b)

i = 2

while i<=50:

    a_eski = a

    b_eski = b

    a = b_eski

    b = a_eski + b_eski

    print(b)

    i += 1


```

İki programı karşılaştırınca, çoklu atama kullanan programın daha sade ve okunaklı olduğunu görebiliyoruz.

## Collatz dizisi

Collatz dizisi pozitif tamsayılardan oluşur. Diziyi oluşturma kuralı şöyledir:

$$n_i$$ çift sayıysa: $$n_{i+1} = n_i/2$$

$$n_i$$ tek sayıysa: $$n_{i+1} = 3n_i+1$$

Dizi 1’e ulaştığında durur. Sözgelişi, diziye 13 ile başlarsak

13, 40,20, 10, 5, 16, 8, 4, 2,1

elde ederiz. [Collatz dizisi](http://en.wikipedia.org/wiki/Collatz_conjecture) adı verilen bu diziyi basit bir Python programıyla üretebiliriz:

In [4]:

```python
n = int(input("Başlangıç değeri: "))

while n > 1:

    if n % 2 == 0:  # n çift sayıysa

        n = n/2

    else:   # n tek sayıysa

        n = 3*n + 1

    print(int(n), end=" ")


```

```
Başlangıç değeri: 11

34 17 52 26 13 40 20 10 5 16 8 4 2 1
```

## Seriler

Terimleri belli bir formüle göre değişen serileri hesaplamak için döngüleri kullanabiliriz. Sözgelişi, $\pi$ sayısını Leibniz formülü ile hesaplayalım.

$$\frac{\pi}{4} = \sum_{i=0}^{\infty} (-1)^i \frac{1}{2i+1} = 1 – \frac{1}{3} + \frac{1}{5} – \frac{1}{7} + \ldots$$

Bu eşitlik sonsuz sayıda terim kullandığımızda tam doğru olur. Pratikte bu mümkün olmadığından toplamayı bir yerde bitirmek gerekir, bu da *kesme hatası* (truncation error) denen hataya yol açacaktır. Buna ek olarak, bilgisayarın içinde sayıları tam olarak temsil edememekten kaynaklanan *yuvarlama hatası* (roundoff error) da vardır.

Bu toplamı nerede kesmeliyiz? Önce, serinin yavaş yakınsadığına dikkat edin. Her yeni terim, büyüklük olarak bir öncekine yakın. O yüzden çok sayıda toplama yapmak gerekecek ($\pi$ sayısını hesaplamak için daha iyi formüller vardır. Bazılarını alıştırmalarda kullanacağız). Diyelim $\pi$’yi virgülden sonra dört basamak doğrulukta belirlemek istiyoruz. O zaman hata payının $10^{-5}$ kadar olmasını isteriz. Terimlerin mutlak değeri tekdüze olarak azaldığından, mutlak değeri $10^{-5}$’den küçük terimlere geldiğimizde döngüyü durdururuz.

Başka bir deyişle, döngüyü durdurmak için $1/(2i+1) \leq 10^{-5}$, veya, $2i+1 \geq 10^5$ şartı geçerlidir. Böylece yaklaşık 50 000 terim toplamak gerektiğini görürüz.

In [5]:

```python
toplam = 0.0 # ara toplam

isaret = 1 # +1 veya -1 olarak dönüşümlü olarak değişecek

payda = 1.0  # 1,3,5,7,...

terim = isaret / payda

sayac = 1

while abs(terim) > 0.00001:

    toplam += terim

    payda += 2

    isaret *= -1

    terim = isaret / payda

    sayac += 1



print("pi ~", 4*toplam)

print(sayac,"terim toplandı.")


```

```python
pi ~ 3.1415726535897814

50001 terim toplandı.


```

## Fonksiyon tablolama

Aşağıdaki program, $x$ değişkenini 0 ile 1 arasında 0.1 adımlarla artırarak, $x$ ve $\sin(x)$ değerlerini bir tablo olarak yazar.

Bu programda *matematik modülünü* kullanıyoruz. Matematiksel fonksiyon ve sabitlerin bulunduğu `math` modülü Python standart kütüphanesine dahildir. Bu modülden daha sonra bahsedeceğiz. Ayrıntılı bilgi için Python [başvuru belgelerine](http://docs.python.org/2/library/math.html) bakabilirsiniz.

In [6]:

```python
import math

x = 0.0

dx = 0.1

print("x", "sin x")

while x <= 1.0:

    print(x, math.sin(x))

    x += dx


```

```python
x sin x

0.0 0.0

0.1 0.09983341664682815

0.2 0.19866933079506122

0.30000000000000004 0.2955202066613396

0.4 0.3894183423086505

0.5 0.479425538604203

0.6 0.5646424733950354

0.7 0.644217687237691

0.7999999999999999 0.7173560908995227

0.8999999999999999 0.7833269096274833

0.9999999999999999 0.8414709848078964


```

Bu çıktı pek göze hitap etmiyor, hizalanma iyi değil. Daha iyi bir görünüm için *dize biçimlendirme* (string formatting) uygulayabiliriz.

In [7]:

```python
import math

x = 0.0

dx = 0.1

print("{:6s} {:6s}".format("x", "sin x"))

while x <= 1.0:

    print("{:1.4f} {:1.4f}".format(x, math.sin(x)))

    x += dx


```

```python
x      sin x 

0.0000 0.0000

0.1000 0.0998

0.2000 0.1987

0.3000 0.2955

0.4000 0.3894

0.5000 0.4794

0.6000 0.5646

0.7000 0.6442

0.8000 0.7174

0.9000 0.7833

1.0000 0.8415


```

Dize biçimlendirme, belli kurallara göre hazırlanmış bir kalıp dizesine işlem yapar. Bu kalıp içinde `{` ve `}` işaretleri bir *yer tutucu* görevi görür. Bu örnekte `{:6s}` yer tutucusu 6 karakterlik yer içine bir dize (“s”) geleceğini belirtiyoruz. Daha sonraki `{:1.4f}` yer tutucusu ise bir reel sayının (“f”) ondalık noktadan önce bir basamak, noktadan sonra ise dört basamak olarak gösterileceğini düzenliyor.

Dize biçimlendirme kalıplarını oluşturma kuralları çok zengindir. Buradaki amaçlarımız için daha fazla derine girmemiz gerekmiyor. Meraklısı için daha ayrıntılı bilgi [şurada bulunabilir](https://pyformat.info/).

---

Başka bir örnek olarak, sinüs fonksiyonunun değişik derecelerdeki Taylor yaklaştırımını veren bir tablo üretelim. Bilindiği gibi, $\sin$ fonksiyonunun 0 çevresindeki Taylor açılımı şu şekildedir:

$$\sin x = x – \frac{x^3}{6} + \frac{x^5}{120} – \frac{x^7}{5040} + \ldots$$

Artan derecelerdeki yaklaştırım fonksiyonlarını şöyle tanımlayabiliriz:

$$\begin{eqnarray}  

f_1(x) &=& x – \frac{x^3}{6} \\  

f_2(x) &=& x – \frac{x^3}{6} + \frac{x^5}{120}\\  

f_3(x) &=& x – \frac{x^3}{6} + \frac{x^5}{120} – \frac{x^7}{5040}  

\end{eqnarray}$$

ve 0 ile 1 arasında değişen $x$ değerleri için, her satıra $x$, $f_1(x)$, $f_2(x)$, $f_3(x)$, $\sin x$ değerlerini ekrana yazalım.

In [8]:

```python
import math

x = 0.0

dx = 0.1

print("{:6s} {:6s} {:6s} {:6s} {:6s}".format("x", "f1", "f2", "f3", "sin x"))

while x <= 1.0:

    f1 = x - x**3 /6

    f2 = f1 + x**5/120

    f3 = f2 + x**7/5040

    print("{:1.4f} {:1.4f} {:1.4f} {:1.4f} {:1.4f}".format(x, f1, f2, f3, math.sin(x)))

    x += dx


```

```python
x      f1     f2     f3     sin x 

0.0000 0.0000 0.0000 0.0000 0.0000

0.1000 0.0998 0.0998 0.0998 0.0998

0.2000 0.1987 0.1987 0.1987 0.1987

0.3000 0.2955 0.2955 0.2955 0.2955

0.4000 0.3893 0.3894 0.3894 0.3894

0.5000 0.4792 0.4794 0.4794 0.4794

0.6000 0.5640 0.5646 0.5647 0.5646

0.7000 0.6428 0.6442 0.6443 0.6442

0.8000 0.7147 0.7174 0.7174 0.7174

0.9000 0.7785 0.7834 0.7835 0.7833

1.0000 0.8333 0.8417 0.8419 0.8415


```

## İteratif denklem sistemleri

Diyelim, radyoaktif bir $A$ izotopu bozunuyor ve yine radyoaktif olan $B$ izotopunu üretiyor, o da bozunarak kararlı (radyoaktif olmayan) $C$ izotopunu üretiyor. $A$’nın bozunma sabiti (birim zamanda bozunan atomların oranı) $\lambda_A$, $B$’ninki ise $\lambda_B$ olsun. Düzenli zaman aralıklarında $A$, $B,$ ve $C$ atomlarının sayılarını veren bir program yazalım.

Denklemler şöyle olur:

$$\begin{eqnarray}  

a_{t+1} &=& a_t – a_t \lambda_A \Delta t\\  

b_{t+1} &=& b_t – b_t \lambda_B \Delta t + a_t \lambda_A \Delta t  

\end{eqnarray}$$

Burada $a_t$ ve $b_t$, $t$ adımında $A$ ve $B$ atomlarının sayısı, $\Delta t$ ise zaman adımı. Birinci denklemde her adımda bir miktar $A$ atomu kaybediliyor. İkinci denklemde ise her adımda bir miktar $B$ atomu kaybediliyor, buna karşılık kaybedilen $A$ atomu kadar yeni $B$ atomu ekleniyor. Toplam atom sayısı $N$ sabit olduğundan $C $  

atomları için ayrı bir denklem yazmaya lüzum yok, $c_t =N-a_t-b_t$ ile bulunabilir.

Somut bir örnek olarak, $^{135} \mathrm{I} \rightarrow ^{135}\mathrm{Xe} \rightarrow ^{135} \mathrm{Cs}$ [zincirini ele alalım](https://en.wikipedia.org/wiki/Decay_chain#Beta_decay_chains_in_uranium_.26_plutonium_fission_products). İyot-135’in yarılanma ömrü 6.57 saat, Ksenon-135’in ise 9.14 saattir. Sezyum-135 kararlı izotop olmasa da, yarılanma ömrü 2.3 milyon yıl olduğundan, diğerlerine göre sabit sayılır. Yarılanma ömrü $\tau$ ise, bozunma sabiti $\lambda = \ln 2 / \tau$ [olur](https://en.wikipedia.org/wiki/Radioactive_decay#Radioactive_decay_rates).

In [9]:

```python
import math



a,b,c = 1000, 0, 0

N = a+b+c



lam_a = math.log(2) / 6.57 # I-135, 1/saat biriminde

lam_b = math.log(2) / 9.14 # Xe-135, 1/saat biriminde

t = 0



# Sütun başlıkları sağa yaslansın.

print("{:>6s} {:>6s} {:>6s} {:>6s}".format("saat", "I","Xe","Cs"))



# Bir saatlik aralıklarla a,b,c miktarını ekrana bas.

while t <= 20:

    print("{:6d} {:6d} {:6d} {:6d}".format(t, int(a), int(b), int(c)))

    a = (1-lam_a)*a

    b = (1-lam_b)*b + lam_a*a

    c = N-a-b

    t += 1


```

```python
  saat      I     Xe     Cs

     0   1000      0      0

     1    894     94     11

     2    800    171     28

     3    715    234     50

     4    640    283     75

     5    572    322    104

     6    512    352    135

     7    458    373    167

     8    409    388    201

     9    366    398    235

    10    327    402    269

    11    293    402    303

    12    262    400    337

    13    234    394    370

    14    209    386    403

    15    187    377    435

    16    167    366    465

    17    150    354    495

    18    134    341    523

    19    120    328    551

    20    107    314    577


```

Görüyoruz ki $^{135} \mathrm{I}$ miktarı sürekli azalıyor ve $ ^{135} \mathrm{Cs}$ sürekli artıyor. Geçiş izotopu $^{135}\mathrm{Xe}$ ise önce artıyor, onuncu saatte zirveye ulaşıyor, ve sonra sürekli azalıyor.