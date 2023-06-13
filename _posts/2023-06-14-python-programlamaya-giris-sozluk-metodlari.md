---
title:  Python Programlamaya Giriş 14 – Sözlük Metodları
author: sonsuz
date: 2023-06-14 00:17:13 +0300
categories: [Program,Python]
tags: [python,sözlük,metod]
---






Python’daki [veri tiplerini daha önce](https://sonsuzus.github.io/posts/python-programlamaya-giris-sayilar-aritmetik-temel-veri-yapilari) kısaca ele almıştık; bir önceki bölümde de [liste tipine ait metodların kullanımını](https://sonsuzus.github.io/posts/python-programlamaya-giris-liste-metodlari) örneklerle incelemiştik. Bu yazıda sözlük tipine ait olan metodları örneklerle açıklıyoruz. Bundan sonraki bölümlerde dize ve küme tiplerine ait metodları inceleyeceğiz.

**Sözlükler**, listeler gibi, birden fazla elemanı bir araya toplayan yapılardır. Listelerden farkları *sıralı nesne* olmamalarıdır. Bir listenin indeksleri üzerinden doğal bir sırası varken, sözlüklerin elemanlarında doğal bir sıralama mevcut değildir.

Bir sözlük *birleşmeli dizi* (associative array) olarak anılan bir veri yapısıdır. Bu yapıdaki her eleman bir *anahtar-değer* (key-value) çiftinden oluşur. Belli bir *değere* ulaşmak için o değere ait tekil *anahtarı* kullanmak gerekir. Bu anahtar bir sayı, dize veya çokuz olabilir.

```py
telefon["kaan"] == "216 123 4567"

sıcaklık[(24.345, 41.243)] == 21.2




```

Listelerde elemanlar sıfırdan başlayarak tamsayılarla indekslenirken, sözlük elemanlarını anahtarlarla indekslenir. Bu anlamda sözlükler listelerden daha geneldirler.

## Sözlük yaratma

Diyelim bir kişinin ismini ve yaşını barındıran bir sözlük oluşturacaksınız. Bu sözlüğü Python’da oluşturmanın dört değişik yolu vardır.

(1) Doğrudan bir sözlük nesnesi yaratmak

In [1]:

```py
D = {"isim" : "Ali", "yaş" : 45}

D


```

Out[1]:

```py
{'isim': 'Ali', 'yaş': 45}
```

(2) Boş bir sözlük yarattıktan sonra anahtar ve değerleri tek tek eklemek:

In [2]:

```py
D = {}

D["isim"] = "Ali"

D["yaş"] = 45

D


```

Out[2]:

```py
{'isim': 'Ali', 'yaş': 45}
```

(3) `dict` fonksiyonunu isimli parametrelerle kullanmak:

In [3]:

```py
D = dict(isim="Ali", yaş=45)

D


```

Out[3]:

```py
{'isim': 'Ali', 'yaş': 45}
```

(4) `dict` fonksiyonuna (anahtar, değer) çiftleri dizisi vermek:

In [4]:

```py
D = dict([("isim","Ali"),("yaş",45)])

D


```

Out[4]:

```py
{'isim': 'Ali', 'yaş': 45}
```

Bu sonuncu yöntem genellikle, anahtarlar ve değerler ayrı ayrı listelerde verilmişse, onları `zip` fonksiyonuyla birleştirilerek kullanılır.

In [5]:

```py
anahtarlar = ['isim', 'yaş']

degerler = ['Ali', 45]

D = dict( zip(anahtarlar, degerler) )

D


```

Out[5]:

```py
{'isim': 'Ali', 'yaş': 45}
```

## len, del, in

Bir nesnenin içindeki eleman sayısını veren `len` fonksiyonu, bir nesneyi veya elemanını silen `del` komutu, belirli bir elemanın mevcut olup olmadığını veren `in` işlemi sözlüklerde de kullanılabilir.

In [6]:

```py
D = {'bir': 1, 'iki': 2.0, 'pi': 3.14159}


```

In [7]:

```
len(D)


```

Out[7]:

```
3
```

In [8]:

```
"bir" in D


```

Out[8]:

```
True
```

`in` komutu sadece anahtarlar üzerinde tarama yapar. Değerler arasında belli bir değer bulunup bulunmadığını bulmakta kullanılmaz.

In [9]:

```
1 in D


```

Out[9]:

```
False
```

In [10]:

```py
del D["bir"]

D


```

Out[10]:

```py
{'iki': 2.0, 'pi': 3.14159}
```

## Sözlük metodları

Bir sözlük nesnesine ait metodları `dir` fonksiyonuyla görebiliriz.

In [11]:

```
dir(dict)


```

Out[11]:

```py
['__class__',

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

 '__init__',

 '__init_subclass__',

 '__iter__',

 '__le__',

 '__len__',

 '__lt__',

 '__ne__',

 '__new__',

 '__reduce__',

 '__reduce_ex__',

 '__repr__',

 '__setattr__',

 '__setitem__',

 '__sizeof__',

 '__str__',

 '__subclasshook__',

 'clear',

 'copy',

 'fromkeys',

 'get',

 'items',

 'keys',

 'pop',

 'popitem',

 'setdefault',

 'update',

 'values']
```

Başında ve sonunda altçizgi olan metodlar nesne içi kullanım içindir.

## Sözlükteki bütün maddeleri silmek

`clear` metodu ile bir sözlükteki bütün anahtar-değer çiftleri silinebilir.

In [12]:

```py
D = {'bir': 1, 'iki': 2.0, 'pi': 3.14159}

D.clear()

D


```

Out[12]:

```
{}
```

## Sözlüğün kopyasını çıkarmak

Bazen bir sözlükteki orijinal bilgileri değiştirmeden, bir kopya üzerinde işlemler yapmanız gerekebilir. Bir sözlüğün kopyasını `copy` metoduyla elde edebilirsiniz.

In [13]:

```py
D = {'bir': 1, 'iki': 2.0, 'pi': 3.14159}

D2 = D.copy()

D2


```

Out[13]:

```py
{'bir': 1, 'iki': 2.0, 'pi': 3.14159}
```

Bundan sonra `D2`‘de yapacağımız değişiklikler `D`‘yi etkilemez.

In [14]:

```py
D2["bir"] = "uno"

print("D =",D)

print("D2 =",D2)


```

```py
D = {'bir': 1, 'iki': 2.0, 'pi': 3.14159}

D2 = {'bir': 'uno', 'iki': 2.0, 'pi': 3.14159}


```

## İki sözlüğü birleştirmek

Sözlüklerin `update` metodu ile varolan bir sözlüğe yeni bir sözlükten anahtar-değer çiftleri ekleyebilirsiniz. Aynı anahtara sahip iki değer varsa, eskisi yenisiyle değiştirilir. Bu metod nesne içi (in-place) değişiklik yapar.

In [15]:

```py
telefonlar = {"Ali": 3762, "Zeynep": 8249, "Mehmet": 2652}

telf_2 = {"Fatma": 9212, "Deniz": 1129, "Mehmet": 1212}

telefonlar.update(telf_2)

telefonlar


```

Out[15]:

```py
{'Ali': 3762, 'Deniz': 1129, 'Fatma': 9212, 'Mehmet': 1212, 'Zeynep': 8249}
```

## Sözlüklerden liste üretmek

Bazen bir sözlükteki elemanları teker teker işlemek için bir döngü kurmak isteyebilirsiniz. Ancak sözlükler sıralı nesne olmadıkları için `for` döngüsü ile kullanılamazlar. Bir sözlüğün içeriğini iterasyona uygun bir biçime getirmek için `dict.items` metodunu kullanmalıyız.

In [16]:

```py
telefonlar = {"Ali": 3762, "Zeynep": 8249, "Mehmet": 2652}

for isim,tel in telefonlar.items():

    print("Adı: {}, İç Hat: {}".format(isim,tel))


```

```py
Adı: Ali, İç Hat: 3762

Adı: Zeynep, İç Hat: 8249

Adı: Mehmet, İç Hat: 2652


```

In [17]:

```py
list(telefonlar.items())


```

Out[17]:

```py
[('Ali', 3762), ('Zeynep', 8249), ('Mehmet', 2652)]
```

Dikkat: Yazdığımız döngüde elemanları sözlüğe verdiğimiz orijinal sırada geri aldık. Ama bunun her zaman böyle olacağının garantisi yok. Sözlüklerde herhangi bir varsayılan sıra olmaz. Yapacağınız işlem belli bir sıralama gerektiriyorsa, işlemden önce elemanlar listesinde açık komutla sıralama yapın.

In [18]:

```py
telefonlar = {"Ali": 3762, "Zeynep": 8249, "Mehmet": 2652}

for isim,tel in sorted(telefonlar.items()):

    print("Adı: {}, İç Hat: {}".format(isim,tel))


```

```py
Adı: Ali, İç Hat: 3762

Adı: Mehmet, İç Hat: 2652

Adı: Zeynep, İç Hat: 8249


```

Sadece anahtarlardan oluşan bir liste elde etmek için `dict.keys` metodunu kullanırız.

In [19]:

```py
list(telefonlar.keys())


```

Out[19]:

```
['Ali', 'Zeynep', 'Mehmet']
```

Sadece değerlerden oluşan bir liste için `dict.values` metodu kullanılır.

In [20]:

```
list(telefonlar.values())


```

Out[20]:

```
[3762, 8249, 2652]
```

Eğer iki çağrı arasında sözlükte bir değişiklik yapılmadıysa, `keys` ve `values` metodlarıyla elde ettiğimiz listelerin elemanları karşılıklı olarak sözlükteki mevcut anahtar-değer çiftlerine denk gelir. Böylece `zip` ile bu listeleri birleştirerek orijinal sözlüğü elde edebiliriz.

In [21]:

```py
isimler = list(telefonlar.keys())

telnolar = list(telefonlar.values())

dict(zip(isimler,telnolar))


```

Out[21]:

```py
{'Ali': 3762, 'Mehmet': 2652, 'Zeynep': 8249}
```

## Elemanlara erişmek

Bir `D` sözlüğünde saklanan bir değere erişmenin en basit yolu `D[anahtar]` komutunu kullanmak. Fakat `anahtar` referansı sözlükte tanımlı değilse bir hata mesajı çıkar, bu da programınızın akışınızı bozabilir.

In [22]:

```py
telefonlar = {"Ali": 3762, "Zeynep": 8249, "Mehmet": 2652}

telefonlar["Ali"]


```

Out[22]:

```
3762
```

In [23]:

```py
telefonlar["Kaan"]


```

```py
---------------------------------------------------------------------------

KeyError                                  Traceback (most recent call last)

<ipython-input-23-e5c66bc1aadc> in <module>()

----> 1 telefonlar["Kaan"]



KeyError: 'Kaan'
```

Verilen anahtarın sözlükte bulunmaması durumunda varsayılan bir değer döndürülmesini istiyorsanız, `get` metodunu kullanabilirsiniz. `D.get(k, d)` ifadesi, `k` anahtarı sözlükte varsa `D[k]` değerini, yoksa varsayılan `d` değerini geri verir.

In [24]:

```py
for isim in ["Ali","Kaan"]:

    print("{} telefonu {}".format(isim, telefonlar.get(isim, "mevcut değil")))


```

```py
Ali telefonu 3762

Kaan telefonu mevcut değil


```

## Sözlüğe yeni anahtarlar eklemek

Bir `D` sözlüğüne yeni bir anahtar-değer çiftini dinamik olarak kolayca ekleyebiliriz.

In [25]:

```py
D = {}

D["abc"] = 3

D


```

Out[25]:

```
{'abc': 3}
```

Bunun başka bir yolu da `setdefault` metodunu kullanmaktır. Bu metod, `get` gibi çalışır, mevcut olmayan bir anahtar verildiğinde bir varsayılan değer döndürür. Ama `get`‘ten farklı olarak, verilen yeni anahtarı sözlüğe ekler.

In [26]:

```py
print(D.get("def",42))

print(D) # sözlük eski halinde kalır.


```

```py
42

{'abc': 3}


```

In [27]:

```py
print(D.setdefault("def",42))

print(D) # sözlüğe "def" anahtarı eklendi.


```

```py
42

{'abc': 3, 'def': 42}


```
