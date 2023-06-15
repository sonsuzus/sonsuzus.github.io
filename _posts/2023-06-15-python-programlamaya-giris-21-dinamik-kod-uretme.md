---
title:  Python Programlamaya Giriş 21 – Dinamik kod üretme
author: sonsuz
date: 2023-06-15 16:25:04 +0300
categories: [Program,Python]
tags: [python,kod,dinamik]
---




Python *dinamik* tabir edilen dillerden biridir; programdaki nesneleri önceden bildirmeniz gerekmez, program çalıştıkça işlenen komutlar o anda yeni nesneler üretir. Bu dinamiklik sayesinde, dize olarak verilmiş Python komutlarını da işleyebilir, hatta program yazan programlar yazabiliriz.

Bu işlemi yapmak için iki Python fonksiyonu vardır: `eval()` ve `exec()`

Dizinin bütün yazılarına erişmek için [*Python Programlamaya Giriş*](https://sonsuzus.github.io/categories/python) kategorimize bakabilirsiniz. 

## eval

Bu fonksiyon, Python komutları içeren bir dizeyi yorumlayıcıya gönderir ve sonucu geri verir.

In [1]:

```py
eval("2**3 + 4*5")


```

Out[1]:

```
28
```

Çalıştırma anında isim alanında bulunan değişkenler de kod dizesi içinde kullanılabilir.

In [2]:

```py
x = 5

eval("2*x+4")


```

Out[2]:

```
14
```

Komut dizesi içindeki değişkeni başka bir değerle kullanmak isterseniz, değişkenleri bir sözlük ile verebilirsiniz.

In [3]:

```py
eval("2*x+4",{"x":10})


```

Out[3]:

```
24
```

### Örnek: Basit hesap makinesi

Kullanıcıdan tek tek matematiksel ifadeler alıp sonucu yazan bir programcık yazalım. Kullanıcı “dur” yazdığında program sona ersin.

In [4]:

```py
while(True):

    işlem = input("Bir işlem yazın: ")

    if işlem.strip().lower()=="dur": break

    print(eval(işlem))


```

```py
3.142857142857143

1267650600228229401496703205376


```


### Örnek: Yardım belgeleri özetleri

Nesnelerin yardım belgelerini daha önce kullanmıştık. Bir metodla ilgili bilgi almak için `help()` komutunu kullandığımızda o metodun (bir fonksiyon nesnesidir) `__doc__` isimli özelliği ekrana basılır. Buna doğrudan da erişebiliriz.

In [5]:

```py
list.append.__doc__


```

Out[5]:

```py
'L.append(object) -> None -- append object to end'
```

Diyelim bir nesne sınıfı altında tanımlanmış bütün metodların kısa tarifini (belge dizesini) ekrana dökmek istiyoruz. Ama bir sınıf altında, daha özel amaçlı metodlar da bulunur. Bunlar başlarında ve sonlarında bir çift altçizgi kullanırlar.

In [6]:

```
dir(list)


```

Out[6]:

```py
['__add__',

 '__class__',

 '__contains__',

 ....

 'remove',

 'reverse',

 'sort']
```

Altçizgili metodları hariç tutmak istiyoruz, çünkü onlar doğrudan kullanılmaz. Bu amaçla `eval`‘i bir döngü içinde kullanabiliriz.

In [7]:

```py
for metod in dir(list):

    if "__" not in metod:

        print(eval("list."+metod+".__doc__"))


```

```py
L.append(object) -> None -- append object to end

L.clear() -> None -- remove all items from L

L.copy() -> list -- a shallow copy of L

L.count(value) -> integer -- return number of occurrences of value

L.extend(iterable) -> None -- extend list by appending elements from the iterable

L.index(value, [start, [stop]]) -> integer -- return first index of value.

Raises ValueError if the value is not present.

L.insert(index, object) -- insert object before index

L.pop([index]) -> item -- remove and return item at index (default last).

Raises IndexError if list is empty or index is out of range.

L.remove(value) -> None -- remove first occurrence of value.

Raises ValueError if the value is not present.

L.reverse() -- reverse *IN PLACE*

L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*


```

## exec

Değer döndüren ifadeleri `eval()` ile işletebiliriz, ama bir ifade (expression) olmayan, yani değer döndürmeyen komutları (söz gelişi fonksiyon tanımları, döngüler, atamalar vb.) çalıştırmak için `exec()` fonksiyonuna ihtiyacımız var.

Örnek olarak, bir değişken ataması yapalım:

In [8]:

```py
exec("x=3.1415")

x


```

Out[8]:

```
3.1415
```

Bir formülde değişkene 0-9 arası değerler vererek bir tablo oluşturan bir kod yazalım. Formülü kullanıcıdan alalım.

In [9]:

```py
değişken = "x" # Formülde kullanılacak değişken.

formül = input("Bir matematiksel formül yazın: ")

kod = """

for {0} in range(10):

 print({0}, {1})""".format(değişken, formül)

print(kod)


```

```py
for x in range(10):

    print(x, 2*x**3-10)


```

In [10]:

```
exec(kod)


```

```
0 -10

1 -8

2 6

3 44

4 118

5 240

6 422

7 676

8 1014

9 1448


```

Farkedeceğiniz gibi, `değişken`‘in değeri `"x"` olduğu için formülde de `x` karakterini kullanmamız gerekiyor. Ama `değişken`‘e farklı bir değer atayarak formülde farklı bir değişken adı kullanmamız mümkün olur.

## Global ve yerel değişkenler

`eval`/`exec` fonksiyonları, işletilecek kodu barındıran dizenin yanı sıra iki parametre daha alırlar: *globals* ve *locals*. Bu parametreler özellikle belirtilmezse, `eval`/`exec` kodunda yorumlayıcının o andaki durumunda tanımlanmış olan bütün isimler kullanılabilir.

*Yerel* değişkenler bir fonksiyon içinden tanımlı olan, o fonksiyonun dışında tanınmayan isimlerdir. *Global* değişkenler ise bütün fonksiyonların erişebileceği değişkenlerdir. Yerel isimlere `locals()`, global isimlere ise `globals()` komutlarıyla ulaşılabilir. Bu komutlar değişken isimleriyle değerlerini eşleştiren birer sözlük döndürür.

In [11]:

```
globals()


```

Out[11]:

```py
{'In': ['',

  'eval("2**3 + 4*5")',

  'x = 5\neval("2*x+4")',

 ...

 'formül': '2*x**3-10',

 'get_ipython': <bound method InteractiveShell.get_ipython of <ipykernel.zmqshell.ZMQInteractiveShell object at 0x7f9d822f7b70>>,

 'işlem': 'dur',

 'kod': '\nfor x in range(10):\n    print(x, 2*x**3-10)',

 'metod': 'sort',

 'quit': <IPython.core.autocall.ZMQExitAutocall at 0x7f9d80260630>,

 'x': 9}
```

In [12]:

```py
def f(x):

    a = 10

    print(locals())



f(3)


```

```py
{'a': 10, 'x': 3}


```

`eval`/`exec` ile bir kod parçası çalıştırırken bu global ve yerel değişkenleri sınırlandırabiliriz. Bu fonksiyonların genel kullanımı şöyledir:

```
eval(source, globals=None, locals=None)

exec(source, globals=None, locals=None)




```

Burada `globals` ve `locals` parametreleri olarak global ve yerel değişkenleri tutan birer sözlük koyabiliriz.

In [13]:

```py
exec("print(locals())", None, {"abc": 17, "xyz": "Mehmet"})


```

```
{'abc': 17, 'xyz': 'Mehmet'}


```

In [14]:

```
exec("print(globals())", None, {"abc": 17, "xyz": "Mehmet"})


```

```py
{'__name__': '__main__', ... '__builtins__': <module 'builtins' (built-in)>, ... '_i14': 'exec("print(globals())", None, {"abc": 17, "xyz": "Mehmet"})'}


```

*globals* yerine boş bir sözlük koyarsak sadece Python dilinin parçası olarak tanımlanmış isimlere erişilebilir.

In [15]:

```
exec("print(globals())", {}, {"abc": 17, "xyz": "Mehmet"})


```

```py
{'__builtins__': {'__name__': 'builtins', ... 'abs': <built-in function abs>, 'all': <built-in function all>, 'any': <built-in function any>, ...}


```

Bunlara bile erişimi kapatmamız mümkündür, aşağıdaki bölümde göreceğimiz gibi.

## Güvenlik

Dışarıdan alınan bir kodu çalıştırmak her zaman risklidir. `exec()` ve `eval()` fonksiyonlarının bilgisayarınıza bir kapı açtığını unutmayın.

Tehlikeyi örneklemek için, yukarıdaki örneği tekrar ele alalım. Siz bir formül beklerken, kötü niyetli bir kullanıcı işletim sisteminizi yönetecek bir komutu bu formülle beraber verebilir. Meselâ, formül sorulduğunda

```py
'x); import os; os.system("touch hello.world");(0,


```

dizesinin verildiğini varsayalım.

In [16]:

```py
değişken = "x" # Formülde kullanılacak değişken.

formül = 'x); import os; os.system("touch hello.world");(0,'

kod = """

for {0} in range(10):

 print({0}, {1})""".format(değişken, formül)


```

Bu girdi sonucunda çalıştırılacak kod şöyle olur:

In [17]:

```
print(kod)


```

```py
for x in range(10):

    print(x, x); import os; os.system("touch hello.world");(0,)


```

Burada kötü niyetli kullanıcı beklenen formülü verdikten sonra parantezi kapatmış ve işletim sistemine yönelik komutlar eklemiş. (Sondaki `(0,` kısmı, kalıpta bulunan sağ parantezin sentaks hatası vermemesi için, onu etkisiz eleman haline dönüştürüyor.)

Bu kodu `exec(kod)` ile çalıştırdığınızda ekrana sayılar tablosu çıkmasının yanı sıra, bu programı çalıştırdığınız dizinin altında *hello.world* isimli boş bir dosya yaratıldığını göreceksiniz (Linux kullanıyorsanız). Yani program işletim sisteminize erişebildi. Kötü niyetli bir saldırgan aynı yöntemle diskinizi silebilir, şifrelerinizi çalabilir, virüs yerleştirebilir.

Bu risklere karşı alınabilecek kısmi tedbirler vardır. En yaygın olanı, `exec`‘in çalıştığı sanal ortamdaki değişkenleri, *globals* ve *locals* parametreleri kullanarak düzenlemektir. Sözgelişi aşağıda, *globals* parametresi olarak `{"__builtins__":None}` vermekle Python’un öntanımlı fonksiyonlarını kapatırız. Böylelikle `import` ile bir modül yüklenmesini ve işletim sistemine ulaşılmasını engelleriz. Bu işlem `range` ve `print` fonksiyonlarını da kapatır, o yüzden *locals* parametresine bunların tanımlarını içeren bir sözlük veririz.

In [18]:

```py
exec(kod, {"__builtins__":None}, {"range":range, "print":print})


```

```
0 0


```

```py
---------------------------------------------------------------------------

ImportError                               Traceback (most recent call last)

<ipython-input-18-d4573d593261> in <module>()

----> 1 exec(kod, {"__builtins__":None}, {"range":range, "print":print})



<string> in <module>()



ImportError: __import__ not found
```

Bu yeni düzende `import` fonksiyonu tanınmadığı için `exec()` çağrısı bir hata verdi ve sızma engellendi. Aynı kodu beklenen şekilde bir girdiyle çalıştırdığınızda ise sorun yaşamazsınız.

Matematik kütüphanesindeki fonksiyonları kullanan işlemler yapmak istiyorsanız, gereken fonksiyonlardan oluşan bir “beyaz liste” oluşturabilirsiniz.

In [19]:

```py
değişken = "x" # Formülde kullanılacak değişken.

formül = "x * sqrt(x+1)/log(x+2)"

kod = """

for {0} in range(10):

 print({0}, {1})""".format(değişken, formül)


```

In [20]:

```py
import math

exec(kod, {"__builtins__":None}, {"range":range, "print":print, "sqrt":math.sqrt, "log":math.log})


```

```
0 0.0

1 1.2872726592996706

2 2.4988211106473432

3 3.728009607357671

4 4.991893199734352

5 6.293943592339911

6 7.6340245917967176

7 9.010908615097694

8 10.423067565678043

9 11.868949934707404


```

Kendi kullanacağınız programlar veya bir masaüstü uygulaması için fazla tedbir almak gerekmeyebilir. Yanlış veya kötü niyetli bir kullanım sadece kullanıcıya zarar verecektir. Ama bir web uygulaması yazıyorsanız güvenliğe çok daha fazla dikkat etmelisiniz. Web güvenliğinde uzmanlaşan kaynaklardan daha ayrıntılı bilgi edinebilirsiniz.

---

Özetle, dinamik olarak üretilen bir kodu işletmek için `exec`/`eval` kullanabilirsiniz. Bunun yararlı, hatta elzem olduğu çeşitli durumlar vardır. Söz gelişi

* Python sözdizimiyle yazılmış bir ifadeyi doğrudan alıp işlemek,
* Bir konfigürasyon dosyasını herhangi bir “parsing” işlemine tabi tutmadan yorumlamak,
* Bir programın kaynak koduna dokunmadan ek modüller yüklemek.

`exec`/`eval` ilk bakışta çok hoş görünseler de çok sık kullanılmamalıdırlar, bazı sakıncaları vardır.

* Kodu okumayı zorlaştırır. Programı anlamak istiyorsak kaynak koduna ek olarak, çalıştırılmak üzere alınacak kodun ne olduğunu da bilmeliyiz.
* Kodu test etmeyi, hataları bulmayı zorlaştırır.
* Güvenlik açığı oluşturur.

`exec`/`eval` fonksiyonlarının işe yaradığı durumlar vardır, ama probleminizi önce normal kod kullanarak çözmeye çalışın.
