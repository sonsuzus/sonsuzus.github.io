---
title:  Python Programlamaya Giriş 23 – Modüller ve paketler
author: sonsuz
date: 2023-06-15 17:47:58 +0300
categories: [Program,Python]
tags: [python,modül,paket,kütüphane]
---







Her programlama dilinde olduğu gibi Python’da da tekrar tekrar kullanılabilen fonksiyon ve sınıfların bir kütüphane şeklinde ayrı dosyalarda saklanması ve yeni yazılan programlara entegre edilmesi için bir mekanizma vardır. Standart kütüphaneler, SciPy ve benzeri paketler, veya kendi kişisel fonksiyon kütüphaneniz bu modül sistemiyle inşa edilir.

Dizinin bütün yazılarına erişmek için [*Python Programlamaya Giriş*](https://sonsuzus.github.io/categories/python) kategorimize bakabilirsiniz. 

## Modüller

Python’da bir modül yaratmak için özel bir işleme gerek yoktur. Python kodu içeren, `.py` uzantılı herhangi bir dosya bir modül olabilir. Sözgelişi, aşağıdaki kodu `basitmodul.py` isimli bir dosyaya yazıp kaydettiğinizde, bir modül yaratmış olursunuz.

In [1]:

```py
%%writefile basitmodul.py

print("basitmodul çalıştırıldı.")

x = 5

def f(x):

    return x**2

def g():

    print("Merhaba")


```

```py
Writing basitmodul.py


```

Komut satırında veya başka bir program içinde `import basitmodul` komutunu vererek (sonunda .py olmayacak) bu modülün içindeki bütün komutların işletilmesini sağlarsınız.

In [2]:

```py
import basitmodul


```

```
basitmodul çalıştırıldı.


```

Elbette `basitmodul.py` dosyasını nereye kaydettiğiniz önemli. Bu örnekte, dosyanın mevcut çalışma dizininde bulunduğunu varsaydım. Bir `import` komutunda yorumlayıcı önce çalışma dizinine, sonra `PYTHONPATH` kabuk değişkeninde yazan dizinlere, sonra da kurulum sırasında belirlenmiş dizinlere bakar. İkincisini Linux bash kabuğunda `echo $PYTHONPATH` komutu ile görebilirsiniz.

Diyelim yazdığınız modülleri `modullerim` isimli bir dizin altında tutmak istiyorsunuz. Python yorumlayıcısı içindeki `sys.path` değişkeni bakılacak dizinlerin listesini tutar (önce import sys yazmayı unutmayın). Bu listeye `sys.path.append("<ev dizininiz>/modullerim")` komutuyla bir ekleme yaparak, ev dizininizin altındaki `modullerim` dizinine bakmasını sağlayabilirsiniz.

Modülü `import` etmekle yeni bir *isim alanı* yaratmış oldunuz. Bir isim alanı bir nesnedir; dolayısıyla modülde tanımlanan değişken ve fonksiyonlara erişmek için nokta notasyonu kullanılır.

In [3]:

```py
basitmodul.x, basitmodul.f(5)


```

Out[3]:

```
(5, 25)
```

In [4]:

```py
basitmodul.g()


```

```
Merhaba


```

Modülden sadece belli isimleri almak istiyorsak `from ... import` komutunu kullanabiliriz. O zaman bu değişkenler ana isim alanına aktarılmış olurlar ve onlara nokta işlemi olmadan doğrudan erişebiliriz.

In [5]:

```py
from basitmodul import x,f

basitmodul.x, basitmodul.f(5)


```

Out[5]:

```
(5, 25)
```

Yukarıdaki işlemde `g` fonksiyonunu ana isim alanına aktarmadığımız için doğrudan kullanmaya kalktığımızda hata mesajı alırız.

In [6]:

```
g()


```

```py
---------------------------------------------------------------------------

NameError                                 Traceback (most recent call last)

<ipython-input-6-5fd69ddb5074> in <module>()

----> 1 g()



NameError: name 'g' is not defined
```

Modüldeki bütün isimleri ana isim alanına aktarmak için `from basitmodul import *` komutu verilebilir. Ancak, böyle yaptığınızda modüldeki isimler daha önce tanımlanmış isimlerin yerine geçebilir. Söz gelişi, yeni bir `g()` fonksiyonu tanımlamış olalım.

In [7]:

```py
def g(): print("Hasta la vista")

g()


```

```
Hasta la vista


```

Bu tanımdan sonra, `basitmodul`‘deki bütün isimleri aşağıdaki komutla alırsak, bu fonksiyon yerine `basitmodul`‘deki `g()` geçecektir.

In [8]:

```
from basitmodul import *

g()


```

```
Merhaba


```

Bu tür çatışmalara meydan vermemek için, modülleri `import *` ile yüklemek tavsiye edilmez. Modüldeki değişkenlere modül ismi aracılığıyla (meselâ `basitmodul.g()` ile) ulaşmak daha emniyetlidir.

Ancak her seferinde modül ismini uzun uzun yazmak epeyce zahmetli olabilir ve kodun okunaklılığını azaltır. Modüle daha kısa bir isim atamak için `import ... as` komutunu kullanabiliriz.

In [9]:

```py
import basitmodul as bm


```

In [10]:

```
bm.x, bm.f(3)


```

Out[10]:

```
(5, 9)
```

`from ... import ... as` komutuyla modülden belli bir nesne (değişken, fonksiyon, vs.) alabilir ve onu yeni bir isimle kullanabilirsiniz.

In [11]:

```py
from basitmodul import g as selamlama

selamlama()


```

```
Merhaba


```

## dir() fonksiyonu

Bir modülde tanımlanmış isimlerin (değişken ve fonksiyon) tam listesini görmek isterseniz `dir()` fonksiyonunu kullanabilirsiniz.

In [12]:

```
dir(bm)


```

Out[12]:

```py
['__builtins__',

 '__cached__',

 '__doc__',

 '__file__',

 '__loader__',

 '__name__',

 '__package__',

 '__spec__',

 'f',

 'g',

 'x']
```

`dir()` fonksiyonu sadece modüllerde değil, bir sınıf (class) içindeki isimleri almak için de kullanılabilir. Örneğin, bir liste nesnesindeki metodları listelemek için `dir(list)` komutu verebiliriz.

In [13]:

```
dir(list)


```

Out[13]:

```py
['__add__',

 '__class__',

 '__contains__',

 '__delattr__',

 '__delitem__',

 '__dir__',

 '__doc__',

 '__eq__',

 '__format__',

 '__ge__',

 '__getattribute__',

 '__getitem__',

 '__gt__',

 '__hash__',

 '__iadd__',

 '__imul__',

 '__init__',

 '__init_subclass__',

 '__iter__',

 '__le__',

 '__len__',

 '__lt__',

 '__mul__',

 '__ne__',

 '__new__',

 '__reduce__',

 '__reduce_ex__',

 '__repr__',

 '__reversed__',

 '__rmul__',

 '__setattr__',

 '__setitem__',

 '__sizeof__',

 '__str__',

 '__subclasshook__',

 'append',

 'clear',

 'copy',

 'count',

 'extend',

 'index',

 'insert',

 'pop',

 'remove',

 'reverse',

 'sort']
```

## Modülleri tekrar yüklemek

Bir `import` işlemi bir modül dosyasını baştan sona bir kere işletir, ama ikinci bir `import` komutu dosyayı baştan çalıştırmaz. Dolayısıyla, etkileşimli çalışırken (sözgelişi Spyder gibi bir IDE ile veya Jupyter defteri ile) modül dosyasında bir değişiklik yaptıysanız, tekrar `import` yapmak bu değişikliklerin görülmesini sağlamaz.

Söz gelişi, `basitmodul.py` dosyasında `g()` fonksiyonunun tanımını değiştirelim:

In [14]:

```py
%%writefile basitmodul.py

print("basitmodul çalıştırıldı.")

x = 5

def f(x):

    return x**2

def g():

    print("Namaste")


```

```
Overwriting basitmodul.py


```

Bu yeni modül dosyasını `import` ile işletmeye çalışalım:

In [15]:

```
import basitmodul

basitmodul.g()


```

```
Merhaba


```

Görüldüğü gibi `g()`‘nin eski tanımını kullanıyor. Zaten başta `"basitmodul çalıştırıldı"` mesajının çıkmaması da modülün işletilmediğine işaret ediyor.

Modülünüzün güncellenmiş olarak yeniden işletilmesini istiyorsanız ya Python yorumlayıcınızı kapatıp açmalısınız (Jupyter’de kernel restart), ya da `importlib.reload()` fonksiyonunu kullanmalısınız. Bu fonksiyon bir *modül nesnesi* döndürür.

In [16]:

```py
from importlib import reload

bm = reload(basitmodul)


```

```
basitmodul çalıştırıldı.


```

In [17]:

```
bm.g()


```

```
Namaste


```

Tabii bir modül aslında dinamik bir nesne olduğu için, böyle bir değişiklik yapmak için her zaman dosyayı değiştirip tekrar yüklemek gerekmez; çalışma sırasında bir komutla da değişiklik yapılabilir.

In [18]:

```py
bm.g = lambda: print("Guten Tag")


```

In [19]:

```
bm.g()


```

```
Guten Tag


```

## Paketler

Bir *modül* belli bir işe dair fonksiyonların ve sınıfların tanımlandığı bir dosyadır. İşlev olarak ilişkili, ama birbirinden ayrı birkaç modülünüz varsa bunları ortak bir dizinde tutmak mantıklı olur. Bunlar bir Python *paketi* oluşturur.

Python’da bir *paket* bir dizindir; bu dizinde modüller ve `__init__.py` isimli bir dosya mevcut olmalıdır. Paket yüklenirken `__init__.py` dosyasının içindeki komutlar çalıştırılır. Paket yüklemesinde ilk olarak yapılmasını istediğimiz işlemleri bu dosyaya koyabiliriz. Paket dizininde mutlaka `__init__.py` isimli bir dosya bulunmalıdır; bu boş bir dosya olabilir.

Örnek olarak, çalıştığımız dizinin altında *modullerim* isimli bir dizin, ve içinde *modul_A.py*, *modul_B.py* ve *__init__.py* isimli üç tane dosya yaratalım.

```py
modullerim/

    __init__.py

    modul_A.py

    modul_B.py
```

In [20]:

```py
%%writefile modullerim/__init__.py

print("modullerim yüklendi")


```

```py
Writing modullerim/__init__.py


```

In [21]:

```py
%%writefile modullerim/modul_A.py    

print("Modül A yüklendi")

pi = 3.14159

def çevre(yarıçap):

    return 2*pi*yarıçap


```

```
Writing modullerim/modul_A.py


```

In [22]:

```py
%%writefile modullerim/modul_B.py

print("Modül B yüklendi")

def fib(n):

    """Fibonacci dizisinin n terimi."""

    a,b=1,1

    L = [1,1]

    for i in range(n-2):

        a,b = b,a+b

        L += [b]

    return L


```

```
Writing modullerim/modul_B.py


```

In [23]:

```
import modullerim.modul_A


```

```
modullerim yüklendi

Modül A yüklendi


```

In [24]:

```
modullerim.modul_A.pi


```

Out[24]:

```
3.14159
```

`from ... import` komutu ile doğrudan `modul_A` isim alanını yaratabiliriz.

In [25]:

```py
from modullerim import modul_A

modul_A.pi, modul_A.çevre(2)


```

Out[25]:

```
(3.14159, 12.56636)
```

Bu ikinci import ile `"Modul A yüklendi"` mesajının çıkmadığına dikkat edin. Bir oturumda modül içeriği sadece ilk import komutunda çalıştırılır. Sonraki import işlemlerinde modül tekrar çalıştırılmaz; yine de yukarıda görüldüğü gibi bu modülle yeni bir isim alanı oluşturmak mümkündür.

Yazma zahmetini kısaltmak için `as` kelimesiyle modüle daha kısa bir isim alanı adı verebiliriz.

In [26]:

```py
from modullerim import modul_A as A

A.pi, A.çevre(5)


```

Out[26]:

```
(3.14159, 31.4159)
```

*modul_B* içindeki bütün değişken isimlerini mevcut isim alanına ekleyebiliriz. Ama yukarıda açıkladığımız gibi bu pek tavsiye edilmez.

In [27]:

```
from modullerim.modul_B import *


```

```
Modül B yüklendi


```

In [28]:

```
fib(10)


```

Out[28]:

```
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
```

Yukarıdaki örneklerde `çevre()` fonksiyonunu bir modülden, `fib()` fonksiyonunu başka bir modülden aldık; bunun için de modülleri ayrıca import etme gibi bir adım atmamız icap etti. Bunun yerine bu isimleri doğrudan *__init__.py* içinde import edersek, modülleri ayrıca yüklememize gerek kalmaz. Bunun için *__init__.py* dosyasını aşağıdaki gibi değiştirelim:

In [29]:

```py
%%writefile modullerim/__init__.py

from .modul_A import çevre

from .modul_B import fib


```

```
Overwriting modullerim/__init__.py


```

Modül adının başındaki noktalar, dosyanın mevcut dizinde bulunduğunu gösterir. Değişikliğin görülebilmesi için yorumlayıcıyı tekrar başlatmak (Jupyter’de “Restart Kernel”), veya yukarıda gördüğümüz gibi `reload()` kullanmak gerekir.

In [30]:

```py
from importlib import reload

m = reload(modullerim)


```

Şimdi `çevre()` ve `fib()` fonksiyonlarını, tanımlandıkları modülleri import etmeye gerek kalmadan doğrudan doğruya kullanabiliriz.

In [31]:

```py
print(m.çevre(5))

print(m.fib(10))


```

```
31.4159

[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


```

## Paketlerde alt dizinler

Bir paketin altında başka dizinler de bulunabilir. Bu durumda her bir dizinin altında kendi *__init__.py* dosyası bulunmalıdır.

İç içe dizinler şeklinde düzenlemiş bir pakete örnek olarak *SciPy* paketini ele alalım. Bu paketin altındaki dizinlerin bir kısmı şöyledir:

```
scipy/

    integrate/

        __init__.py

        ...

    linalg/

        __init__.py

        ...

    stats/

        __init__.py

        distributions.py

        ...




```

Alt paketlerdeki fonksiyonları import ederken nokta (.) işlemini kullanabiliriz.

In [32]:

```
from scipy.integrate import quad

quad(lambda x: x**3, 1, 2)  # x^3 fonksiyonunun 1'den 2'ye kadar integrali


```

Out[32]:

```
(3.7500000000000004, 4.1633363423443377e-14)
```

In [33]:

```
import scipy

scipy.integrate.quad(lambda x: x**3, 1, 2)


```

Out[33]:

```
(3.7500000000000004, 4.1633363423443377e-14)
```

In [34]:

```
import scipy.integrate as intg

intg.quad(lambda x: x**3, 1, 2 )


```

Out[34]:

```
(3.7500000000000004, 4.1633363423443377e-14)
```

In [35]:

```py
from scipy.stats.distributions import norm

norm.pdf((-2,-1,0, 1, 2))  # Normal dağılımın -2, -1, 0, 1, 2 için değerleri


```

Out[35]:

```py
array([0.05399097, 0.24197072, 0.39894228, 0.24197072, 0.05399097])
```
