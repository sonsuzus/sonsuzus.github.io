---
title:  Python Programlamaya Giriş 7 – Fonksiyonlar
author: sonsuz
date: 2023-06-13 00:50:42 +0300
categories: [Program,Python]
tags: [python,fonksiyon,kütüphane]
---




Python Programlamaya Giriş yazı dizimize Python fonksiyonlarının temelleriyle devam ediyoruz.

Yazı dizimizin şimdiye kadarki bölümlerinde bir programı inşa etmek için gereken bütün yapı taşlarını gördük. *Prosedürel programlama* denen paradigma içinde programlar birbiri arkasından işlenir, bir karar verilmesi gerektiğinde program akışı iki yoldan birini seçer, veya bir döngü içindeki bir kod parçası tekrarlanır.

Teorik olarak, her türlü programı yazmak için bu yapılar yeterli. Ancak, Yogi Berra’nın dediği gibi: Teoride teori ve pratik arasında fark yoktur, ama pratikte vardır.

Kod yazarken işlemleri sık sık farklı yerlerde tekrarlamamız gerekir. Söz gelişi, bir yatırımın belli bir dönem sonunda bileşik faizle ne miktara ulaştığını yazmak için bir döngü yazabiliriz. Bu tür bir işlemi büyük bir program içinde değişik yerlerde (mesela farklı yatırım araçları için) kullanmamız gerekebilir. Programcılar böyle tekrarlanan işler için aynı kodu tekrar tekrar yazmaktansa, bunları bir *fonksiyon* (prosedür veya yordam olarak da bilinir) olarak paketleyip kullanmayı tercih ederler. Fonksiyon kullanmak sayesinde:

* Aynı kodu defalarca yazmak gerekmez.
* Tekrarlama yüzünden doğacak hatalar ortadan kalkar.
* Bellek (RAM) gereksiz yere dolmaz. Kod parçası onlarca kere tekrarlanmak yerine bir kere yazılır.
* Programcı küçük ayrıntılara tekrar tekrar kafa yormak zorunda kalmaz.
* İşleri küçük birimlere bölmek, programlama hatalarını bulmayı kolaylaştırır.
* Programlama dilinin çekirdek tanımında bulunmayan üst seviye işlemleri tek komutla yapmayı sağlar.
* Fonksiyon kütüphaneleri, uzmanlaşmış programcılar tarafından hızlı ve verimli hale getirilebilir.

Bu faydalar sadece Python değil, her türlü programlama dili için geçerlidir tabii.

Bir fonksiyon bir kara kutu gibi düşünülebilir: Aldığı *parametre*ler onun girdisi, verdiği (“döndürdüğü”) değer ise çıktısıdır. Fonksiyonlara istediğiniz sayıda parametre verebilirsiniz. Parametre almayan ve/veya geriye bir değer vermeyen fonksiyonlar da olabilir.

## Kütüphane fonksiyonları kullanma

Bir *kütüphane* belli bir işlev için hazırlanan fonksiyonların topluluğudur. Bir kütüphane matematik fonksiyonlarını toplarken, başka bir kütüphane kelime işleme, bir başkası ağ iletişimi, bir başkası oyun modülleri barındırıyor olabilir. Kütüphaneler bir dilin resmi tanımına dahil olabilir ve kurulumda beraber gelebilir (bu durumda onlara *standart kütüphane* denir), veya üçüncü kişiler tarafından hazırlanmış olabilir.

Python dili çok zengin bir [standart kütüphaneye](https://docs.python.org/3/library/index.html) sahiptir. Matematik işlemleri, istatistik işlemleri, gün ve saat işlemleri, dosya sıkıştırma, internet protokolleri, HTML, işletim sistemi yönetimi, grafik arayüz oluşturma, ve daha bir çok işlem için gereken hazır fonksiyonlar Python ile birlikte gelir. Bunların dışında yüzlerce başka kütüphane de mevcuttur, istediğinizde bunları sisteminize kurup kullanabilirsiniz. Daha sonraki yazılarda kendi kütüphanelerimizi nasıl oluşturacağımızı da göreceğiz. Bu yazıda sadece matematik fonksiyonları kütüphanesini örnek olarak kullanacağız.

Kütüphaneler diskimize kurulu olarak hazır bekliyor olsalar da, onları kullanmak için önce `import` komutuyla yorumlayıcıya yüklememiz gerekir.

In [1]:

```python
import math

print( math.sqrt(2) )

print( math.sin(math.pi/2) )


```

```
1.4142135623730951

1.0


```

Burada `math.sqrt(2)` ifadesi bir fonksiyon çağrısıdır. Matematik modülü `math` içindeki karekök fonksiyonu `sqrt` çağrılır ve 2 argümanı verilir. Aradaki nokta bir *üyelik* belirtir; `sqrt` fonksiyonu `math` modülünün altındadır. Keza `math.sin` aynı modülün altındaki sinüs fonksiyonudur, `math.pi` ise $\pi$ sayısıdır.

Siz ayrıca `pi` veya `sqrt` isimli değişkenler veya fonksiyonlar tanımlamış olsanız da, onlar ile bu isimler karışmaz; `pi` ile `math.pi` farklıdır. Burada `math` bir *isim alanı* (namespace) oluşturur; kendi tanımlarını ayrı tutar.

Yükleme sırasında modülün adını değiştirebiliriz. Özellikle uzun isimli modülleri daha kısa isimle kullanmak için bu özellik faydalı olur.

In [2]:

```python
import math as m

print( m.sqrt(2) )

print( m.sin(m.pi/2) )


```

```
1.4142135623730951

1.0


```

Veya, modüldeki bütün isimlere ihtiyacınız yoksa, onları mevcut isim alanınıza tek tek belirleyerek alabilirsiniz. İsim değiştirme burada da geçerlidir. Modül içindeki isimleri değiştirerek alabilirsiniz.

In [3]:

```python
from math import sqrt, sin

from math import pi as π

print( sqrt(2) )

print( sin(π/2) )


```

```
1.4142135623730951

1.0


```


Başka bir alternatif, modüldeki bütün isimleri mevcut isim alanına yüklemektir.

In [4]:

```python
from math import *

cos(pi), tan(pi/4)


```

Out[4]:

```
(-1.0, 0.9999999999999999)
```

Ancak bu usül Python programcıları tarafından tavsiye edilmez. Bir modül adı kullanmak, ister `math` ister kısaca `m`, bir isim alanı yaratır ve isim çatışmalarını engeller. Varsayalım ki `pi` veya `tan` değişkenlerini kodunuzda bir yerlerde önceden başka bir anlamda tanımladınız. Modülü `import *` ile yüklemekle önceki tanımları silersiniz, ve kodunuz biraz karmaşık ise bunu farketmeyebilirsiniz bile. Özellikle büyük modüllerde pek çok değişik isim gizli olabilir ve neyi sildiğinizi farketmeyebilirsiniz bile. En doğrusu, birazcık daha fazla yazmayı göze alıp bir modül ismi kullanmaktır.

Bir modülde tanımlı bütün isimlere `dir` fonksiyonuyla erişilebilir.

In [5]:

```python
import math

dir(math)


```

Out[5]:

```python
['__doc__',

 '__file__',

 '__loader__',

 '__name__',

 '__package__',

 '__spec__',

 'acos',

 'acosh',

 'asin',

 'asinh',

 'atan',

 'atan2',

 'atanh',

 'ceil',

 'copysign',

 'cos',

 'cosh',

 'degrees',

 'e',

 'erf',

 'erfc',

 'exp',

 'expm1',

 'fabs',

 'factorial',

 'floor',

 'fmod',

 'frexp',

 'fsum',

 'gamma',

 'gcd',

 'hypot',

 'inf',

 'isclose',

 'isfinite',

 'isinf',

 'isnan',

 'ldexp',

 'lgamma',

 'log',

 'log10',

 'log1p',

 'log2',

 'modf',

 'nan',

 'pi',

 'pow',

 'radians',

 'sin',

 'sinh',

 'sqrt',

 'tan',

 'tanh',

 'tau',

 'trunc']
```

Modüldeki belli bir fonksiyonun nasıl kullanıldığını hatırlamanız gerektiğinde `help` fonksiyonunu kullanabilirsiniz. Bu işlemle, fonksiyonun içine gömülü *belgeleme dizesi* (docstring) ekrana yazılır. Belgeleme dizelerinin nasıl oluşturulacağını bu yazının sonunda okuyabilirsiniz.

In [6]:

```
help(math.sin)


```

```
Help on built-in function sin in module math:



sin(...)

    sin(x)

    

    Return the sine of x (measured in radians).




```

## Fonksiyon tanımlama

Şimdi kendimiz nasıl fonksiyon yaratabileceğimizi görelim. Python’da fonksiyonlar `def` kelimesiyle tanımlanır. Mesela:

In [7]:

```python
def f1(x):

    print(x)



f1(3)


```

```
3


```

In [8]:

```python
f1("merhaba"), f1(3.0*4.25), f1( (2,37) )


```

```
merhaba

12.75

(2, 37)


```

Out[8]:

```
(None, None, None)
```

Bu fonksiyon basit bir iş yapıyor, aldığı parametreyi olduğu gibi ekrana basıyor. Herhangi bir nesne alabildiğine dikkat edin. Fonksiyonun geri verdiği bir değer yok. Bu yüzden yukarıdaki komutta çıktı hücresinde `(None, None, None)` görüyoruz.

Fonksiyonların bir değer geri vermesi istiyorsak `return` komutunu kullanırız. Bu komut, arkasından gelen ifadenin değerinin, fonksiyonu çağıran programa bildirilmesini sağlar ve fonksiyonun çalışmasını bitirir.

Aşağıdaki fonksiyon aldığı iki parametreye çarpma işlemini uygular ve sonucu geri verir:

In [9]:

```
def carp(a,b):

    return a*b



carp(2,-7)


```

Out[9]:

```
-14
```

Geri verilen değeri daha sonraki bir işlemde kullanmak için bir değişkene atayabilirsiniz.

In [10]:

```
y = carp(2, -7)

y + 3


```

Out[10]:

```
-11
```

C, C++, Fortran, Java gibi daha katı dillerden farklı olarak, Python’da fonksiyon tanımlarken, parametrelerin ne tipte (tamsayı, kayan noktalı sayı, dize, liste, vs.) olduğu belirtilmez. Bu özellik sayesinde Python programları farklı veri tipleriyle işlem yapma kolaylığı sağlar. Mesela `carp` bir dize ile bir tamsayı almaya itiraz etmez. Çarpma işlemini bu iki tiple tanımlandığı gibi yapıp sonucu geri verir.

In [11]:

```
carp("merhaba",3)


```

Out[11]:

```
'merhabamerhabamerhaba'
```

Ama bu kolaylığın bir bedeli vardır: Fonksiyonun içinde, kullandığınız veri tipleri ile ilgili işlemlerin uyumlu olması gereklidir. Sözgelişi, iki dizeyi “çarpmak” bir hata mesajına yol açar, çünkü dizeler arasında `*` işlemi tanımlı değildir.

In [12]:

```
carp("merhaba","dunya")


```

```
---------------------------------------------------------------------------

TypeError                                 Traceback (most recent call last)

<ipython-input-12-5dfbcca2560b> in <module>()

----> 1 carp("merhaba","dunya")



<ipython-input-9-c813e8533fc7> in carp(a, b)

 1 def carp(a,b):

----> 2     return a*b

 3 

 4 carp(2,-7)



TypeError: can't multiply sequence by non-int of type 'str'
```

Böyle hatalardan kaçınmak için birkaç yol vardır. Bunlardan biri `assert` komutu ile belli şartların sağlanıp sağlanmadığını önceden yoklamak, bir diğer ise fonksiyonun içinde *istisna işlemi* (“exception handling”) yapmaktır. Böylece belli bir hata (meselâ yukarıdaki gibi *TypeError*) oluştuğunda, programı durdurmadan akışı düzenlemek mümkün olur. Bu konulara sonraki bölümlerde yer vereceğiz.

## Birkaç tane değer geri verme

Fonksiyonlar her tipte nesne geri verebilirler. Bir çokuz nesnesi veren bir fonksiyon kullanarak, birden fazla değer çıkarma davranışı taklit edilebilir:

In [13]:

```python
def f(x, y):

    return x+y, x-y



toplam, fark = f(3,5)

print("Toplam = {}, Fark = {}".format(toplam,fark))


```

```
Toplam = 8, Fark = -2


```

## Fonksiyon veren fonksiyonlar

Python dinamik bir dildir: Programın işleyişi sırasında komutlar yeni nesnelerin üretilmesini ve işlenmesini sağlar. Fonksiyonlar da dinamik olarak `def` komutuyla yaratılır. Buna karşılık, C gibi derlenen diller böyle davranmaz. Bu tür dillerde fonksiyonlar, program henüz çalıştırılmadan, derleme aşamasında yaratılır ve işletilebilir ikili koda gömülür. Python gibi dillerin dinamik yapısı sayesinde, fonksiyonların başka komutlar ve bloklar içinde, mesela sadece bir şart doğru olduğunda tanımlanmasını sağlayabiliriz.

In [14]:

```
test = True

if test:

    def f1(): print(5)

else:

    def f2(): print(10)


```

In [15]:

```
f1()


```

```
5


```

In [16]:

```
f2()


```

```
---------------------------------------------------------------------------

NameError                                 Traceback (most recent call last)

<ipython-input-16-fdec4c1c071f> in <module>()

----> 1 f2()



NameError: name 'f2' is not defined
```

Bir fonksiyon tanımlanmasında, önce belirttiğimiz kod parçasını içeren bir *fonksiyon nesnesi* yaratılır, sonra bu nesne ona verdiğimiz isme bağlanır. Bu anlamda `def` komutu atama (`=`) işlemi gibi çalışır. Bunun bir yan faydası, varolan bir fonksiyona başka isimler verebilme imkânıdır.

In [17]:

```
yenifonk = f1

yenifonk()


```

```
5


```

İki ismin de aynı nesneye işaret ettiğini `is` komutuyla doğrulayabiliriz.

In [18]:

```
yenifonk is f1


```

Out[18]:

```
True
```

Yine aynı dinamik özellik sayesinde, *fonksiyon veren fonksiyonlar* (“fonksiyon fabrikaları”) tanımlanabilir.

In [19]:

```python
def kuvvetfonk(n):

    def fonk(x):

        return x**n

    return fonk


```

Buradaki `kuvvetfonk` fonksiyonu, aldığı parametreyi kullanarak yarattığı bir fonksiyon nesnesini verir. Bu fonksiyon nesnesine bir isim atayıp bu isimle çalıştırabiliriz.

In [20]:

```python
kare = kuvvetfonk(2)

kup = kuvvetfonk(3)

kare(5), kup(5)


```

Out[20]:

```
(25, 125)
```

Aslında bu fonksiyon nesneleri bir isme atamadan da çağrılabilir, ama her seferinde bu fonksiyonlar baştan yaratılacağı için hesaplama açısından verimsiz olur.

In [21]:

```
kuvvetfonk(2)(5), kuvvetfonk(3)(5)


```

Out[21]:

```
(25, 125)
```

## Fonksiyon alan fonksiyonlar

Fonksiyonlar, başka fonksiyonları parametre olarak alabilirler. Basit bir örnek olarak, \(\sum\_{i=a}^{b} f(i)\) toplamını veren bir fonksiyon yazalım.

In [22]:

```python
def fntoplam(f, a, b):

    i = a

    toplam = 0

    while i<=b:

        toplam += f(i)

        i += 1

    return toplam



def f1(x):

    return 1.0/x



def f2(x):

    return 2.0**-x


```

In [23]:

```
fntoplam(f1, 1, 10)


```

Out[23]:

```
2.9289682539682538
```

In [24]:

```
fntoplam(f2, 1, 10)


```

Out[24]:

```
0.9990234375
```

## Değiştirilebilir parametreler

Fonksiyonlara, listeler gibi değiştirilebilir (mutable) parametreler veriyorsanız, ve bunlar fonksiyon içinde değiştiriliyorsa, bu değişiklik kalıcı olur.

In [25]:

```python
def f(x):

    x[0] = -10

    print(x)



x = [1,2,3]

f(x)


```

```
[-10, 2, 3]


```

In [26]:

```
x


```

Out[26]:

```
[-10, 2, 3]
```

## Değişken görünürlüğü, yerel ve global değişkenler

Bir fonksiyon blokunun dışında ve içinde aynı isimde değişkenler kullanırsanız, içeride olanın değeri kullanılır olur. Fonksiyon, dıştaki değişkenin değerini değiştirmez.

In [27]:

```python
x = 10

def f():

    x = 20

    print(x)



f()


```

```
20


```

In [28]:

```
x


```

Out[28]:

```
10
```

Python bu iki `x` ismini farklı değişkenler olarak görür. İkinci `x` bir *yerel* değişkendir ve sadece `f` fonksiyonu içinde tanımlıdır. Birincisi ise *global* görünürlüğe sahiptir; aşağısında tanımlanan bütün fonksiyonlarda kullanılabilir. Yukarıdaki örnekte `f` fonksiyonu tanımı altında `x=20` satırını silersek fonksiyon ekrana global `x` değeri olan 10’u basacaktır.

Bir seviye daha karmaşık bir örnek olarak, `f` fonksiyonu içinde başka bir fonksiyon tanımlayalım.

In [29]:

```python
x = 10

print("x =",x)

def f():

    x = 20

    print("f içinde x =",x)

    def g():

        x = 30

        print("g içinde x =", x)

    g()

f()


```

```
x = 10

f içinde x = 20

g içinde x = 30


```

Bir değişken ismine atanmış değerin tespit edilmesi için genel kural şöyledir: Önce program akışının bulunduğu blok içinde bir tanım yapılmış mı diye bakılır. Eğer en içteki blokta bir tanım bulunmazsa, onu çevreleyen dış bloka, yoksa onun da dış blokuna bakılır. En dış bloka gelindiğinde *global* değişkenler içinde olup olmadığına bakılır. En son olarak öntanımlı (“built-in”) isimler kontrol edilir.

Peki, diyelim ki tam tersini istiyoruz. Yani, bir fonksiyon içinde, fonksiyonun dışında tanımlanmış bir değişkene yeni bir değer atamak istiyoruz. Somut olarak, iki önceki örnekte, fonksiyon çalıştıktan sonra `x`‘in 20 olmasını istiyoruz. Bunu, fonksiyon içinde `global` komutuyla sağlarız.

In [30]:

```
x = 10

def f():

    global x

    x = 20



f()

print("x =",x)


```

```
x = 20


```

Ancak, global değişkenlerden mümkün olduğunca kaçınmak gerekir. Fonksiyonlara giriş bilgisini parametrelerle sağlamak ve çıkış değerini `return` komutu aracılığıyla almak daha iyidir. Böylece fonksiyonların düzgün bir akış içinde çalışmasını, bileşenlerin birbirine kolayca bağlanan modüler bir yapıda olmasını, “aldığı belli verdiği belli” olmasını sağlarız. Bu şekilde programlar daha okunaklı ve anlaşılır olur. Global değişkenler ise hem giriş hem çıkış kanalı oldukları için bu akışı bozarlar. Globallerin fazla kullanıldığı programları hem okumak zordur, hem de bilgi akışının karışık bir yumak haline gelmesi mümkündür, hata yapma ihtimali artar. Fonksiyonlara veriyi her zaman fonksiyon parametreleriyle vermeye çalışın.

## Belgeleme dizeleri

Fonksiyon tanımına bir belgeleme dizesi (docstring) eklemek mümkündür. Bir belgeleme dizesi, fonksiyon başlığının hemen altında başlayıp biten bir açıklama metnidir. Normal bir Python dizesinden hiç bir farkı yoktur, ama genellikle üç tırnak (`"""`) ile sınırlandırılırlar, böylece birkaç satıra yayılabilirler. Fonksiyonun çalışmasını etkilemezler. Birçok Python aracı, sözgelişi etkileşimli *help* fonksiyonu bu dizeleri otomatik olarak alıp kullanabilir.

In [31]:

```python
def fntoplam(f, a, b):

    """f(a) + f(a+1) + ... + f(b) toplamını döndürür."""

    i = a

    toplam = 0

    while i<=b:

        toplam += f(i)

        i += 1

    return toplam


```

In [32]:

```
help(fntoplam)


```

```
Help on function fntoplam in module __main__:



fntoplam(f, a, b)

    f(a) + f(a+1) + ... + f(b) toplamını döndürür.




```

Bütünleşik geliştirme ortamlarında (IDE’lerde) çalışırken, fonksiyonu yazdığınız sırada bu belgeleme dizesine ulaşabilirsiniz. Sözgelişi Jupyter defterinde `Shift-Tab` basarsanız bir yardım penceresi açılır.
