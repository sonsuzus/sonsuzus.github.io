---
title:  Python Programlamaya Giriş 11 – İsimsiz Fonksiyonlar
author: sonsuz
date: 2023-06-13 16:30:37 +0300
categories: [Program,Python]
tags: [python,fonksiyon,lambda]
math: true
---






Python Programlamaya Giriş yazı dizimizde [Python fonksiyonlarının nasıl tanımlandığını](https://sonsuzus.github.ip/posts/python-programlamaya-giris-fonksiyonlar), parametre eşleştirmenin ve varsayılan parametrelerin [nasıl işlediğini gördük](https://sonsuzus.github.io/posts/python-programlamaya-giris-fonksiyon-parametreleri), çeşitli örnekler ve alıştırmalar işledik. Dizinin bütün yazılarına erişmek için [*Python Programlamaya Giriş*](http://sonsuzus.github.io/categories/python) kategorimize bakabilirsiniz.

Fonksiyonların her zaman `def` komutuyla tanımlanması gerekmez. Başka bir yol, `lambda` komutunu kullanarak isimsiz (“anonymous” – belli bir isme bağlı olmayan) fonksiyonlar yaratmaktır. İsimsiz fonksiyonlar, `def` komutuyla üretilen fonksiyonlara göre daha kısıtlıdırlar. Buna karşılık, bir fonksiyon nesnesi gereken yerlerde bazı kolaylıklar sağlarlar.

Fonksiyonların `lambda` komutuyla üretilmesine basit bir örnek olarak, aşağıdaki ifadeyi ele alalım. Burada, aldığı parametrenin karesini döndüren bir fonksiyon yaratıyoruz ve buna `f` ismini atıyoruz.

In [1]:

```python
f = lambda x: x*x


```

Bundan sonra `f` alıştığımız şekilde bir fonksiyon olarak kullanılabilir.

In [2]:

```
f(1.2), f(4), f(f(4))


```

Out[2]:

```
(1.44, 16, 256)
```

Nitekim aynı `f` fonksiyonunu `def` ile de tanımlayabilirdik.

In [3]:

```python
def f(x): return x*x


```

In [4]:

```python
f(1.2), f(4), f(f(4))


```

Out[4]:

```
(1.44, 16, 256)
```

Python dinamik bir dildir. Bunun anlamı, verdiğimiz komutların anında işlenmesi, ve gerekli nesnelerin bellekte o anda yaratılıyor olmasıdır. Python’daki her şey gibi fonksiyonlar da (yazılım geliştirmedeki anlamıyla) birer nesnedir. Yukarıdaki `lambda x: x*x` ifadesi bellekte bir *fonksiyon nesnesi* yaratır, ve bu nesne ile `f` ismi birbirine bağlanır. Öz olarak bunun `s = "merhaba"` komutundan farkı yok; burada da önce bellekte `"merhaba"` değerini tutan bir dize nesnesi yaratılır, sonra bu nesne `s` ismi ile eşleştirilir.

Elbette `lambda` ile yaratılan fonksiyon nesnesi tek başına da kullanılabilir.

In [5]:

```python
(lambda x: x*x)(1.2)


```

Out[5]:

```
1.44
```

Ama böyle bir kullanımda fonksiyon her seferinde baştan oluşturulacağından programın verimi azalır.

İsimsiz fonksiyonlar, `def` ile tanımladığımız genel amaçlı fonksiyonlardan daha kısıtlıdırlar. Genel amaçlı fonksiyonlarda Python’da tanımlı olan her türlü işlemi kullanabiliriz. İsimsiz fonksiyonlarda ise komut (“statement”) bulunamaz, yani mesela atama yapamayız veya `if-else`, `while`, `for` yapılarını kullanamayız. Sadece bir ifade (“expression”, geriye bir değer veren bir işlem) bulunabilir.

O zaman isimsiz fonksiyonların faydası ne? Bunlar, özellikle **fonksiyon alan fonksiyonlara verilen parametreler** olarak kullanışlıdırlar.

İlk okuyuşta çok egzotik bir kullanım gibi görünebilir ama değil. İsimsiz fonksiyonların kullanılabildiği yerlere birkaç örnek verelim.

**Örnek: Seriler**

[Önceki bir bölümde](http://sonsuzus.github.io/posts/python-programlamaya-giris-fonksiyonlar) fonksiyon alan bir fonksiyon tanımlamıştık. Özel olarak, $f$ reel sayı alıp reel sayı veren herhangi bir fonksiyon olmak üzere, $f(a) + f(a+1) + f(a+2) +\cdots + f(b)$ toplamını hesaplayan bir fonksiyon yazdık. Bu fonksiyon sadece başlangıç ve bitiş değerleri olan `a` ve `b`‘yi değil, aynı zamanda `f` fonksiyonunu da parametre olarak alıyor. Böylece herhangi bir fonksiyon için bu toplamı hesaplayabiliyoruz.

Bu toplamı veren fonksiyonu şöyle tanımlayabiliriz:

In [6]:

```python
def seritoplam(f, a, b):

    toplam = 0

    x = a

    while x<=b:

        toplam += f(x)

        x += 1

    return toplam


```

Tanımladığımız `seritoplam` fonksiyonu, matematiksel terimle bir “fonksiyonel”dir, yani fonksiyon alıp sayı veren bir fonksiyon. Bunu kullanarak, $\sum_{x=a}^b 2^{-x}$ değerini hesaplayalım. Bu toplam için `f` parametresine $2^{-x}$ olarak tanımlanmış bir fonksiyon verilmeli.

In [7]:

```python
def g(x): return 2.0**(-x)

seritoplam(g, 0, 10)
```

Out[7]:

```
1.9990234375
```

Aynısını bir isimsiz fonksiyonla şöyle yapabiliriz:

In [8]:

```py
seritoplam( lambda x: 2.0**(-x), 0, 10 )


```

Out[8]:

```
1.9990234375
```

Burada `lambda` ifadesini doğrudan doğruya `seritoplam`‘a bir parametre olarak verdiğimize dikkat edin. Bunu doğrudan `def` ile yapamayız, yani

```
seritoplam( def f(x): 2.0**(-x), 0, 10 )


```

yazmak hatalıdır, çünkü `def` yapısı bir fonksiyon nesnesi döndürmez. Buna karşılık `lambda` bir ifadedir (“expression”); konduğu yerde bir fonksiyon nesnesi yaratır.

`seritoplam` fonksiyonunu birçok farklı fonksiyon parametresi vererek denemek istiyor olabilirsiniz. Mesela $ 1+ 1/2 + 1/3 + \cdots + 1/10$ toplamını bulalım:

In [9]:

```py
seritoplam( lambda x: 1/x, 1, 10 )


```

Out[9]:

```
2.9289682539682538
```

Elbette deneyeceğiniz her türlü fonksiyonu `def` ile tanımlayarak da aynı sonuca ulaşabilirsiniz. Ama `lambda` kullanmak burada daha fazla kolaylık sağlıyor.

**Örnek: Sıralama**

Listelere kısaca değinmiştik. Bir listenin elemanlarını sıralamak için `sorted` fonksiyonu kullanılabilir. Söz gelişi:

In [10]:

```
L = [ 6.1, 2.3, -5.6, 8.5, 4.0, -1.2, -3.4, 7.8]

sorted(L)


```

Out[10]:

```
[-5.6, -3.4, -1.2, 2.3, 4.0, 6.1, 7.8, 8.5]
```

Bazen alışılageldik sırayla değil de, başka bir düzene göre sıralamak isteyebilirsiniz. `sorted` fonksiyonunun `key` parametresine bir fonksiyon verirseniz, bu fonksiyon bütün elemanlara tek tek uygulanır ve sıralama bu sonuçlara göre yapılır. Söz gelişi, yukarıdaki listeyi sayıların *mutlak değerlerine* göre sıralamak için `key` parametresine `abs` fonksiyonunu verebilirsiniz.

In [11]:

```py
sorted(L, key=abs)


```

Out[11]:

```
[-1.2, 2.3, -3.4, 4.0, -5.6, 6.1, 7.8, 8.5]
```

Gördüğünüz gibi burada da fonksiyon alan bir fonksiyonumuz var. Aynı sıralamayı bir isimsiz fonksiyonla şöyle elde ederdik.

In [12]:

```py
sorted(L, key=lambda x: x if x>0 else -x)


```

Out[12]:

```
[-1.2, 2.3, -3.4, 4.0, -5.6, 6.1, 7.8, 8.5]
```

Üçlü if-else yapısını [başka bir bölümde](http://sonsuzus.github.io/posts/python-programlamaya-giris-secim-yapma-mantik-islemleri-karsilastirmalar) daha ayrıntılı işlemiştik.

Başka bir örnek olarak, listelerden oluşan bir listeyi sıralamayı ele alalım. `key` parametresini kullanmadan `sorted` ilk elemana göre sıralama yapar.

In [13]:

```py
L = [ [1, "merhaba"], [6, "hello"], [-2, "guten tag"] ]

sorted(L)


```

Out[13]:

```py
[[-2, 'guten tag'], [1, 'merhaba'], [6, 'hello']]
```

Eğer ikinci elemana göre sıralama yapmak istiyorsak, `key` parametresine listenin ikinci elemanını (1 indeksli) veren bir fonksiyon koyarız.

In [14]:

```py
sorted(L, key = lambda i: i[1])


```

Out[14]:

```
[[-2, 'guten tag'], [6, 'hello'], [1, 'merhaba']]
```

**Örnek: Sayısal integral hesaplama**

Bir *belirli integral* $\int_a^b f(x)\mathrm{d}x$ matematiksel olarak bir “fonksiyonel”dir: Bir fonksiyon alır ve bir sayı verir. Bir fonksiyonun integralini alırken de isimsiz fonksiyonlar kullanabiliriz.

Bir belirli integrali sayısal olarak hesaplamanın pek çok yöntemi vardır. Bunlara şimdilik hiç girmeden, SciPy paketi içindeki integral alma modülünü kullanalım ve $\int_{-2}^4 6x^3 – 4x^2\, \mathrm{d}x$ integralini hesaplayalım.

In [15]:

```py
import scipy.integrate



scipy.integrate.quad(lambda x: 6*x**3 - 4*x**2, -2, 4)


```

Out[15]:

```
(264.00000000000006, 3.703317987014864e-12)
```

İlk sayı belirli integralin değeri, ikinci sayı ise tahmini hata miktarıdır.

---

Örnekler çoğaltılabilir: Bir fonksiyonun optimal noktalarını bulan bir fonksiyon, türev alan bir fonksiyon, veya bir fonksiyonun grafiğini çizen bir fonksiyon, isimsiz fonksiyonlar alarak daha kolay şekilde işlenebilirler. Ayrıca grafik arayüz oluştururken de isimsiz fonksiyonlar kolaylık sağlar.

İsimsiz fonksiyonların iyi ve kötü taraflarını şöyle özetleyebiliriz:

* `lambda` bir fonksiyon nesnesi döndürür, `def` ise bir komuttur, bir değer döndürmez. Bu yüzden `lambda` ile tanımlanan isimsiz fonksiyonları başka ifadelerin içine, söz gelişi atamalara veya fonksiyon parametrelerine yerleştirebiliriz.
* İsimsiz fonksiyonlarla karmaşık işlemler yapılamaz. Kısa, bir seferlik kullan-at fonksiyonlar tanımlamak için daha uygundurlar.
* İsimsiz fonksiyonlarla kodunuz daha okunaklı olabilir. Sıralama vb. işlemlerde `def` ile farklı fonksiyonlar tanımlamak isim alanının bir sürü tek kullanımlık fonksiyon ismiyle dolmasına sebep olur. Dahası, kaynak kodunuz uzunsa, fonksiyonun tanımlandığı yer ile kullanıldığı yer arasında kalan mesafe yüzünden, kodda ne yapıldığını anlamak için yukarı aşağı kaydırmak gerekebilir. Bu tür küçük işlerde `lambda` ifadeleri kullanmak, fonksiyonun yapısını açıkça gösterdiği için kodun anlaşılırlığını artırır.

İsimsiz fonksiyonlarda parametre kullanımı kuralları isimli fonksiyonlardakilerle aynıdır. Örneğin birden fazla parametre alabilirler.

In [16]:

```py
f = lambda x, y: x+y

f(4,5)


```

Out[16]:

```
9
```

In [17]:

```py
f("hello","world")


```

Out[17]:

```
'helloworld'
```

Parametre paketleme / parametre çözme kuralları isimsiz fonksiyonlarda da aynen geçerlidir.

In [18]:

```py
g = lambda *p : sum(p)

g(0.25, 2, 13)


```

Out[18]:

```
15.25
```

Parametrelere varsayılan değerler atanabilir.

In [19]:

```py
h = lambda x, n=2: x**n  # üst alma. Varsayılan kuvvet 2.

print(h(3)) # 3**2

print(h(3,5)) # 3**5


```

```
9

243

