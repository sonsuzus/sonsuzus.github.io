---
title:  Python Programlamaya Giriş 13 – Liste metodları
author: sonsuz
date: 2023-06-13 23:48:29 +0300
categories: [Program,Python]
tags: [python,liste,metod]
---






Yazı dizimizin önceki bir bölümünde [Python’un öntanımlı veri tiplerini](https://sonsuzus.github.io/posts/python-programlamaya-giris-sayilar-aritmetik-temel-veri-yapilari/) yüzeysel bir şekilde işlemiştik. Bu yazıda ve takip eden birkaç yazıda liste, dize, sözlük ve küme veri tiplerini daha ayrıntılı işleyeceğiz ve bu tip verilerle yapılabilecek işlemleri sıralayacağız. Dizinin bütün yazılarına erişmek için [*Python Programlamaya Giriş*](https://sonsuzus.github.io/categories/python) kategorimize bakabilirsiniz.

## Nesneler ve metodlar

Temel kullanım için bunu bilmek çok gerekmese de, Python nesneye yönelik (object-oriented) bir dildir. Python’da tanımladığınız her şey bir *nesnedir*. Nesneler özel veri yapılarıdır; içlerinde verilerin yanı sıra, o verilerle yapılabilecek işlemleri tanımlayan fonksiyonlar barındırırlar. Söz gelişi, bir liste nesnesinin içinde elemanların değerleri, elemanların ne tipte olduğu, kaç eleman bulunduğu gibi veriler bulunur. Ayrıca listeye eleman ekleme, eleman çıkarma, sıralama gibi işlemler yapan fonksiyonlar da listeyi tanımlayan kodun içindedir. Veri tipinin (sınıfın) tanımı içinde bulunan fonksiyonlara o nesnenin *metodları* denir.

Herhangi bir veri tipi içinde tanımlanmış isimleri (veri veya metod) `dir` fonksiyonuyla görebilirsiniz.

In [1]:

```py
dir(list)


```

Out[1]:

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

Burada altçizgilerle başlayıp biten isimler `list` sınıfının (class) özel metodlarıdır. Bunlar kullanıcı tarafından doğrudan çağrılmamalıdır. Bu tür özel metodların bazıları, asıl metodlar için yardımcı işlemler olabilir. Bazıları ise `in, +, *, <, ==` vs. gibi işlemlerin tanımlanmasında kullanılır. Söz gelişi, iki listenin eşit olup olmadığını anlamak için `L1 == L2` ifadesini kullandığımızda bu `L1.__eq__(L2)` biçimine getirilir.

Özel metodların nasıl kullanılıp tanımlanacağını ileride nesneye yönelik programlama konusunda göreceğiz. Şimdilik ilgimiz sadece “kamuya açık” (public) metodlarla, yani çevresinde altçizgiyle tanımlanmamış olan metodlarla sınırlı.

İlgili sınıfların ve metodların belge dizelerine (docstring) ulaşmak için `help` fonksiyonunu kullanabilirsiniz.

In [2]:

```py
help(list)


```

```py
Help on class list in module builtins:



class list(object)

 |  list() -> new empty list

 |  list(iterable) -> new list initialized from iterable's items

 |  

 |  Methods defined here:

 |  

 |  __add__(self, value, /)

 |      Return self+value.

 |  

 |  __contains__(self, key, /)

 |      Return key in self.

 |  

 |  __delitem__(self, key, /)

 |      Delete self[key].

 |  

 |  __eq__(self, value, /)

 |      Return self==value.

 |  

 |  __ge__(self, value, /)

 |      Return self>=value.

 |  

 |  __getattribute__(self, name, /)

 |      Return getattr(self, name).

 |  

 |  __getitem__(...)

 |      x.__getitem__(y) <==> x[y]

 |  

 |  __gt__(self, value, /)

 |      Return self>value.

 |  

 |  __iadd__(self, value, /)

 |      Implement self+=value.

 |  

 |  __imul__(self, value, /)

 |      Implement self*=value.

 |  

 |  __init__(self, /, *args, **kwargs)

 |      Initialize self.  See help(type(self)) for accurate signature.

 |  

 |  __iter__(self, /)

 |      Implement iter(self).

 |  

 |  __le__(self, value, /)

 |      Return self<=value.

 |  

 |  __len__(self, /)

 |      Return len(self).

 |  

 |  __lt__(self, value, /)

 |      Return self<value.

 |  

 |  __mul__(self, value, /)

 |      Return self*value.n

 |  

 |  __ne__(self, value, /)

 |      Return self!=value.

 |  

 |  __new__(*args, **kwargs) from builtins.type

 |      Create and return a new object.  See help(type) for accurate signature.

 |  

 |  __repr__(self, /)

 |      Return repr(self).

 |  

 |  __reversed__(...)

 |      L.__reversed__() -- return a reverse iterator over the list

 |  

 |  __rmul__(self, value, /)

 |      Return self*value.

 |  

 |  __setitem__(self, key, value, /)

 |      Set self[key] to value.

 |  

 |  __sizeof__(...)

 |      L.__sizeof__() -- size of L in memory, in bytes

 |  

 |  append(...)

 |      L.append(object) -> None -- append object to end

 |  

 |  clear(...)

 |      L.clear() -> None -- remove all items from L

 |  

 |  copy(...)

 |      L.copy() -> list -- a shallow copy of L

 |  

 |  count(...)

 |      L.count(value) -> integer -- return number of occurrences of value

 |  

 |  extend(...)

 |      L.extend(iterable) -> None -- extend list by appending elements from the iterable

 |  

 |  index(...)

 |      L.index(value, [start, [stop]]) -> integer -- return first index of value.

 |      Raises ValueError if the value is not present.

 |  

 |  insert(...)

 |      L.insert(index, object) -- insert object before index

 |  

 |  pop(...)

 |      L.pop([index]) -> item -- remove and return item at index (default last).

 |      Raises IndexError if list is empty or index is out of range.

 |  

 |  remove(...)

 |      L.remove(value) -> None -- remove first occurrence of value.

 |      Raises ValueError if the value is not present.

 |  

 |  reverse(...)

 |      L.reverse() -- reverse *IN PLACE*

 |  

 |  sort(...)

 |      L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*

 |  

 |  ----------------------------------------------------------------------

 |  Data and other attributes defined here:

 |  

 |  __hash__ = None




```

In [3]:

```py
help(list.append)


```

```
Help on method_descriptor:



append(...)

    L.append(object) -> None -- append object to end




```

Bu metodları örneklerle görelim.

## Liste metodları

### append

Listenin sonuna bir eleman ekler.

In [4]:

```py
L = [1,"abc",3]

L.append("xyz")

L


```

Out[4]:

```py
[1, 'abc', 3, 'xyz']
```

### clear

Listeyi siler, bütün elemanları kaldırır.

In [5]:

```py
L = [1,2,5,3,5]

L.clear()

L


```

Out[5]:

```
[]
```

Aynısını `del` ve dilimleme ile de yapabiliriz.

In [6]:

```py
L = [1,2,5,3,5]

del L[:]

L


```

Out[6]:

```
[]
```

### copy

Listenin bir kopyasını çıkarır.

In [7]:

```py
L = [1,5,1,6,4]

L2 = L.copy()

L2


```

Out[7]:

```
[1, 5, 1, 6, 4]
```

Böyle bir kopya, `reverse` veya `sort` gibi nesne içinde (in-place) değişiklik yapan metodlar kullanırken orijinal listenin değiştirilmemesini sağlar.

Aynı kopyalamayı dilimleme işlemi ile de yapabiliriz.

In [8]:

```py
L3 = L[:]

L3


```

Out[8]:

```
[1, 5, 1, 6, 4]
```

### count

Listede belli bir değere sahip kaç eleman olduğunu verir.

In [9]:

```py
L = [1,2,1,2,2,2,3,3,1,1]

L.count(1)


```

Out[9]:

```
4
```

In [10]:

```py
L = [(1,2), (1,2), (3,2), (2,1)]

L.count((1,2))


```

Out[10]:

```
2
```

### extend

Listenin sonuna bir liste ekleyerek genişletir.

In [11]:

```py
L1 = [1, "abc", 3]

L2 = ["xyz", 5]

L1.extend(L2)

L1


```

Out[11]:

```
[1, 'abc', 3, 'xyz', 5]
```

Bunun `append`‘den farklı olduğuna dikkat edin. Aynı işlemi `append` ile yaparsak `L2` listesi kendi başına `L1`‘in son elemanı olur.

In [12]:

```py
L1 = [1, "abc", 3]

L2 = ["xyz", 5]

L1.append(L2)

L1


```

Out[12]:

```
[1, 'abc', 3, ['xyz', 5]]
```

Listelerde toplama (`+`) işlemi ve artırma (`+=`) işlemi arka planda `extend` ile yapılır.

In [13]:

```py
L1 = [1, "abc", 3]

L2 = ["xyz", 5]

L1 += L2

L1


```

Out[13]:

```
[1, 'abc', 3, 'xyz', 5]
```

### index

Belli bir değerin ilk olarak hangi konumda olduğunu verir. Değer bulunamazsa `ValueError` hatası çıkarır.

In [14]:

```py
L = [12, "abc", -4, 11, "abc", 0.25, 64]

L.index("abc")


```

Out[14]:

```
1
```

In [15]:

```py
L.index("xyz")


```

```py
---------------------------------------------------------------------------

ValueError                                Traceback (most recent call last)

<ipython-input-15-40978ea17492> in <module>()

----> 1 L.index("xyz")



ValueError: 'xyz' is not in list
```

Aradığımız değere sahip sonraki elemanları da bulmak istiyorsak, bulunan ilk konumu saklayıp, `index`‘e sonraki konumdan başlayarak aramasını söyleyebiliriz.

In [16]:

```py
L = [12, "abc", -4, 11, "abc", 0.25, 64]

yer = L.index("abc")

L.index("abc",yer+1)


```

Out[16]:

```
4
```

In [17]:

```py
[i for i,el in enumerate(L) if el=="abc"]


```

Out[17]:

```
[1, 4]
```

### insert

Listede verilen konuma bir eleman sokar, sonraki elemanları kaydırır.

In [18]:

```py
L = [1, 2, "abc", -45]

L.insert(3, "xyz")            # Şimdi L[3] "xyz" oldu, -45 kaydı.

L


```

Out[18]:

```py
[1, 2, 'abc', 'xyz', -45]
```

In [19]:

```py
L.insert(0, -10)              # en başa sokar.

L


```

Out[19]:

```py
[-10, 1, 2, 'abc', 'xyz', -45]
```

In [20]:

```py
L.insert(len(L), [3,1,4])     # en sona sokar. L.append([3,1,4]) ile aynı

L


```

Out[20]:

```py
[-10, 1, 2, 'abc', 'xyz', -45, [3, 1, 4]]
```

### pop

Belli bir konumdaki elemanın değerini verir ve listeden siler. Parametre almazsa son elemanı siler.

In [21]:

```py
L = [1,2,"abc",4,5,"xyz"]

L.pop()


```

Out[21]:

```py
'xyz'
```

In [22]:

```
L


```

Out[22]:

```
[1, 2, 'abc', 4, 5]
```

In [23]:

```py
L.pop(2)


```

Out[23]:

```
'abc'
```

In [24]:

```
L


```

Out[24]:

```
[1, 2, 4, 5]
```

### remove

Verilen bir değere sahip olan ilk elemanı bulur ve onu listeden siler. Değer listede yoksa `ValueError` hatası verir.

In [25]:

```py
L = [2,1,5,2,"abc",1,"abc",1]

L.remove("abc")

L


```

Out[25]:

```py
[2, 1, 5, 2, 1, 'abc', 1]
```

In [26]:

```py
L.remove("abc")

L


```

Out[26]:

```
[2, 1, 5, 2, 1, 1]
```

In [27]:

```py
L.remove("abc")

L


```

```
---------------------------------------------------------------------------

ValueError                                Traceback (most recent call last)

<ipython-input-27-610eed97e25e> in <module>()

----> 1 L.remove("abc")

 2 L



ValueError: list.remove(x): x not in list
```

### reverse

Liste elemanlarının sırasını kendi içinde (in-place) ters çevirir. *DİKKAT*: Yeni bir liste döndürmez, mevcut listeyi değiştirir. Eğer orijinal listeyi bozmak istemiyorsanız bir kopya çıkarmalısınız.

In [28]:

```py
L = [3, 1, 4, 1, 5, 9]

L.reverse()

L


```

Out[28]:

```py
[9, 5, 1, 4, 1, 3]
```

Görüldüğü gibi `L` listesi değişmiş. Bunu istemiyorsanız, bir kopya çıkarıp onu ters çevirmelisiniz.

In [29]:

```py
L = [3, 1, 4, 1, 5, 9]

L2 = L.copy()

L2.reverse()

print("L =",L)

print("L2 =",L2)


```

```py
L = [3, 1, 4, 1, 5, 9]

L2 = [9, 5, 1, 4, 1, 3]


```

Tabii daha kestirme olarak, sondan başa adımlarla dilimleme de yapabiliriz. Bu da orijinal listeyi değiştirmez

In [30]:

```
L[::-1]


```

Out[30]:

```
[9, 5, 1, 4, 1, 3]
```

### sort

Listeyi kendi içinde (in-place) sıralar. Sıralamadan sonra orijinal liste değişir.

In [31]:

```py
L = [-4, -8, 1, 2, 1, 5, 9, 7]

L.sort()

L


```

Out[31]:

```
[-8, -4, 1, 1, 2, 5, 7, 9]
```

Sırayı ters çevirmek için `reverse=True` parametresi verilebilir.

In [32]:

```py
L = [-4, -8, 1, 2, 1, 5, 9, 7]

L.sort(reverse=True)

L


```

Out[32]:

```
[9, 7, 5, 2, 1, 1, -4, -8]
```

`key` parametresine bir fonksiyon verildiğinde bu fonksiyon önce her elemana uygulanır, sonuçlara göre sıralama yapılır. Sözgelişi, mutlak değerlere göre sıralama yapmak için:

In [33]:

```
L = [-4, -8, 1, 2, 1, 5, 9, 7]

L.sort(key=abs)

L


```

Out[33]:

```
[1, 1, 2, -4, 5, 7, -8, 9]
```

`sort` metodu orijinal listede değişiklik yapar. Bu tür nesne içi (in-place) değişiklikler performansı biraz artırsa da, bazen orijinal listeyi bozmamak isteyebiliriz. O zaman iki seçeneğimiz var: Orijinal listenin bir kopyasını çıkarıp onu sıralarız:

In [34]:

```
L = [-4, -8, 1, 2, 1, 5, 9, 7]

L2 = L.copy()

L2.sort()

print("L =",L)

print("L2 =",L2)


```

```
L = [-4, -8, 1, 2, 1, 5, 9, 7]

L2 = [-8, -4, 1, 1, 2, 5, 7, 9]


```

Veya, daha önce gördüğümüz öntanımlı `sorted` fonksiyonunu kullanırız:

In [35]:

```
sorted(L)


```

Out[35]:

```
[-8, -4, 1, 1, 2, 5, 7, 9]
```

## Hataya dikkat: Nesne içi değişiklik yapan metodlar

Yukarıda gördüğümüz `sort` ve `reverse` gibi metodlar, bağlı oldukları listenin verisini doğrudan doğruya değiştirirler. Buna nesne içi (in place) değiştirme denir. Geriye döndürdükleri bir değer yoktur.

In [36]:

```py
L = [1,4,2,5]

print(L.sort())


```

```
None


```

Yeni başlayan programcıların yaptıkları yaygın bir hata `L.sort()` çağrısını bir atamanın sağ tarafında kullanmaktır.

In [37]:

```py
L2 = L.sort()


```

Programcı burada `L2`‘nin `L`‘nin sıralanmış hali olduğunu ummaktadır (aslında `L2 = sorted(L)` yazması gerekirdi). Python bu atamayı sessizce yapar, ama aslında `L2`‘yi bir listeye değil `None` değerine atamıştır.

In [38]:

```
L2 is None


```

Out[38]:

```
True
```

Programın içinde daha sonra `L2`‘yi kullanmak isteyen programcı şaşırtıcı hata mesajlarıyla karşılaşabilir.

In [39]:

```
L2[0]


```

```py
---------------------------------------------------------------------------

TypeError                                 Traceback (most recent call last)

<ipython-input-39-8b477b9c426d> in <module>()

----> 1 L2[0]



TypeError: 'NoneType' object is not subscriptable
```

Bu sorunlardan kaçınmak için metodun çevrimiçi yardımına bakarak nesne içi değişiklik yapıp yapmadığını yoklamak gerekir.
