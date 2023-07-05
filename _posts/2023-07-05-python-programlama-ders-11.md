---
title: Python Programlama Ders 11. Özyineleme (Rekürsif) ve istisnalar
author: sonsuz
date: 2023-07-05 16:25:56 +0300
categories: [Program,Python]
tags: [python,programlama,ders,döngü,çokuz,liste,tuple,fonksiyon,istisna,hata,özyineleme,rekürsif,rekürsiyon]
---



## 11.1 Tuplelar ve değişebilirlik

Şimdiye kadar iki bileşik tip gördünüz: karakter dizileri, karakterlerden oluşmaktadır; ve listeler, herhangi bir tipte öğelerden oluşmaktadır. Bu iki bileşik tip arasındaki farklardan biri listenin öğelerinin değiştirilebilir olduğu, karakter dizisindeki karakterlerin değiştirilemez olduğuydu. Başka bir deyişle, karakter dizileri **değiştirilemez (immutable)** ve listeler **değiştirilebilir (mutable)** tiplerdir.

**Tuple**, liste gibi herhangi bir tipteki öğelerin ardışıklığıdır. Ancak listelerden farklı olarak tuplelar değiştirilemez. Sözdizim olarak tuplelar virgül ile ayrılmış değerlerin sıralanmasıdır:

```py
>>> tup = 2, 4, 6, 8, 10
```

Her ne kadar gerekmese de, tupleları parantezlerin arasına yazmak gelenekselleşmiştir:

```py
>>> tup = (2, 4, 6, 8, 10)
```

Tek öğeli bir tuple yaratmak için son virgülü yazmamız gerekmektedir:

```py
>>> tup = (5,)
>>> type(tup)
<type 'tuple'>

```

Virgülsüz Python `(5)` ifadesine parantezler içerisinde yer alan bir tamsayı olarak davranır:

```py
>>> tup = (5)
>>> type(tup)
<type 'int'>
```

Sözdizim farklarını bir kenara bırakırsak, tuplelar karakter dizileri ve listelerdeki aynı dizi işlemlerini desteklerler. İndis işleci tupledan belirli bir öğeyi seçmek için kullanılır.

```py
>>> tup = ('a', 'b', 'c', 'd', 'e')
>>> tup[0]
'a'
```

Dilim işleci de belirli bir aralıktaki öğeleri seçer.

```py
>>> tup[1:3]
('b', 'c')
```

Ancak eğer atamayla bir öğeyi değiştirmek istersek, bir hatayla karşılaşırız:

```py
>>> tup[0] = 'X'
TypeError: 'tuple' object does not support item assignment
```

Elbette, tuple öğelerini değiştiremesek te, tupleı başka bir tuple ile değiştirebiliriz:

```py
>>> tup = ('X',) + tup[1:]
>>> tup
('X', 'b', 'c', 'd', 'e')
```

Alternatif olarak, ilk önce listeye çevirip, değiştirip, tekrar bir tuplea dönüştürebiliriz:

```py
>>> tup = ('X', 'b', 'c', 'd', 'e')
>>> tup = list(tup)
>>> tup
['X', 'b', 'c', 'd', 'e']
>>> tup[0] = 'a'
>>> tup = tuple(tup)
>>> tup
('a', 'b', 'c', 'd', 'e')
```

## 11.2 Tuple ataması

Arada sırada, iki değişkenin değerlerini karşılıklı olarak aktarmak yararlıdır. Geleneksel atama cümleleriyle, bir geçici değişken kullanmamız gerekir. Örneğin, `a` ve `b`'yi karşılıklı değiştirmek için:

```py
gecici = a
a = b
b = gecici
```

Eğer bunu sıkça yapmamız gerekirse, bu işlem yorucu olacaktır. Python **tuple ataması**nın bir biçimini bu sorunu çözmek üzere sağlamaktadır:

```py
a, b = b, a
```

Sol taraf değişkenlerin tupleıdır, sağ taraf ise değerlerin. Her bir değer ilgili değişkene atanmaktadır. Sağ taraftaki tüm deyimler herhangi bir atama olmadan önce işlenmektedir. Bu özellik tuple atamasını çok amaçlı kılmaktadır. Ve bu harika bir özelliktir.

Doğal olarak soldaki değişkenlerin ve sağdaki değerlerin sayısı aynı olmalıdır:

```py
>>> a, b, c, d = 1, 2, 3
ValueError: need more than 3 values to unpack 
```

## 11.3 Geri dönüş değerleri olarak Tuplelar

Fonksiyonlar tupleları geri dönüş değeri olarak döndürebilirler. Örneğin, iki parametreyi birbiriyle değiştiren bir fonksiyon yazabiliriz:

```py
def swap(x, y):
    return y, x
```

Daha sonra geri dönüş değerini iki değişkenli bir tuplea atayabiliriz:

```py
a, b = swap(a, b)
```

Bu durumda, `swap`i bir fonksiyon yapmanın çok bir avantajı yoktur. Gerçekte, `swap`i sarmanın (encapsulate) bir tehlikesi vardır, aşağıdaki cezbedici bir yanlıştır:

```py
def swap(x, y):      # yanlis surum
     x, y = y, x
```

Eğer fonksiyonu şu şekilde çağırırsak:

```py
swap(a, b)
```

`a` ve `x` aynı değerin rumuzudur. `x`'i `swap` içerisinde değiştirmek `x`'in başka bir değeri göstermesini, ancak `a`'nın `__main__` içinde etkilenmemesini sağlar. Benzer olarak `y`'i değiştirmenin de `b` üzerinde etkisi olmayacaktır.

Bu fonksiyon hata mesajı üretmeden çalışacaktır, ama yapmak istediğimizi yapmayacaktır. Bu tipik bir anlambilim hatasıdır.

## 11.4 Saf fonksiyonlar ve değiştiriciler - gözden geçirme

[9. bölümde](https://sonsuzus.github.io/posts/python-programlama-ders-09/) listelerle ilişkili olarak *saf fonksiyonları* ve *değiştiricileri (modifier)* tartışmıştık. Tuplelar değiştirilemez olduklarına göre üzerlerine bir değiştirici yazamayız.

Burada değiştirici listenin ortasına yeni bir değer eklemektedir:

```py
#
# seqtools.py
#

def insert_in_middle(val, lst):
    middle = len(lst)/2
    lst[middle:middle] = [val]

```

Nasıl çalıştığını görmek için yürütelim:

```py
>>> from seqtools import *
>>> my_list = ['a', 'b', 'd', 'e']
>>> insert_in_middle('c', my_list)
>>> my_list
['a', 'b', 'c', 'd', 'e']
```

Tuple ile kullanmak istersek, bir hatayla karşılaşırız:

```py
>>> my_tuple = ('a', 'b', 'd', 'e')
>>> insert_in_middle('c', my_tuple)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "seqtools.py", line 7, in insert_in_middle
    lst[middle:middle] = [val]
TypeError: 'tuple' object does not support item assignment
>>> 
```

Problem tupleların değiştirilemez olması ve dilim atamasını desteklememesidir. `insert_in_middle` fonksiyonunu saf fonksiyon yapmanın basit bir yöntemi şudur:

```py
def insert_in_middle(val, tup):
    middle = len(tup)/2
    return tup[:middle] + (val,) + tup[middle:]
```

Bu sürüm tuplelar için şimdi çalışacaktır, ama liste veya karakter dizileri için çalışmayacaktır. Eğer tüm dizi tipleri için çalışan bir sürüm istiyorsak, kendi değerimizi uygun dizi tipine saran bir yol bulmalıyız. Basit bir yardımcı fonksiyon işimizi görecektir:

```py
def encapsulate(val, seq):
    if type(seq) == type(""):
        return str(val)
    if type(seq) == type([]):
        return [val]
    return (val,)
```

Şimdi `insert_in_middle` fonksiyonunu tüm yerleşik dizi tipleriyle çalışacak şekilde yazabiliriz:

```py
def insert_in_middle(val, seq):
    middle = len(seq)/2
    return seq[:middle] + encapsulate(val, seq) + seq[middle:]
```

`insert_in_middle` fonksiyonunun son iki sürümü saf fonksiyondur. Herhangi bir yan etkileri yoktur. `encapsulate` ve `insert_in_middle`'ı `seqtools.py` modülüne ekleyerek, sınayabiliriz:

```py
>>> from seqtools import *
>>> my_string = 'abde'
>>> my_list = ['a', 'b', 'd', 'e']
>>> my_tuple = ('a', 'b', 'd', 'e')
>>> insert_in_middle('c', my_string)
'abcde'
>>> insert_in_middle('c', my_list)
['a', 'b', 'c', 'd', 'e']
>>> insert_in_middle('c', my_tuple)
('a', 'b', 'c', 'd', 'e')
>>> my_string
'abde'

```

`my_string`, `my_list`, ve `my_tuple` değerleri değişmedi. `insert_in_middle` fonksiyonunun onları değiştirmesini istiyorsak, ürettiğimiz değeri geri dönüş değeri olarak fonksiyondan döndürmeliyiz:

```py
>>> my_string = insert_in_middle('c', my_string)
>>> my_string
'abcde' 

```

## 11.5 Özyineli (rekürsif) veri yapıları

Şu ana kadar gördüğümüz tüm Python veri tipleri listelerde ve tuplelarda değişik yollarla gruplanabilir. Listeler ve tuplelar da içiçe yerleştirilebilir, verinin düzenlenmesi için sayısız olasılık sunar. Kullanımını kolaylaştırmak için verinin düzenlenmesine **veri yapısı** adı verilir.

Seçim zamanı ve biz de oylar geldikçe hesaplanmasına yardımcı oluyoruz. Oylar farklı şehir, köy, kasaba, ilçe ve illerden geliyor. Bazen toplu oylar, bazen de alt toplamlardan oluşan listeler şeklinde gönderiliyor. Sayımların en iyi ne şekilde saklanacağına dair kafa patlattıktan sonra *içiçe sayı listesi* kullanmaya karar veriyoruz. İçiçe sayı listesini şu şekilde tanımlıyoruz:

*içiçe sayı listesi* aşağıdakilerden herhangi biri öğesi olan bir listedir:

1. sayılar
2. içiçe sayı listesi

Terimin, içiçe sayı listesi kendi tanımını barındırdığına dikkat edin. Bunun gibi **özyineli (rekürsif) tanımlamalar** matematik ve bilgisayar bilimlerinde yaygındır. **Özyineli veri yapıları**nı tanımlamak için öz ve güçlü bir yol sağlarlar. Özyineli veri yapıları kendilerinin daha küçük ve basit örneklerinden oluşmaktadır. Tanım döngüsel değildir, eninde sonunda öğesi olarak herhangi bir liste içermeyen bir listeye erişeceğiz.

Şimdi içiçe sayı listesindeki tüm değerleri toplayan bir fonksiyon yazmamız gerektiğini varsayalım. Python bir dizideki sayıların toplamını bulmaya yarayan yerleşik bir fonksiyona sahiptir:

```py
>>> sum([1, 2, 8])
11
>>> sum((3, 5, 8.5))
16.5
>>>
```

Ancak bizim *içiçe sayı listemiz* için `sum` çalışmayacaktır:

```py
>>> sum([1, 2, [11, 13], 8])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'list'
>>> 
```

Problem şu ki, listenin üçüncü öğesi, `[11, 13]`, bir listedir ve `1`, `2` ve `8` değerlerine eklenemez.

## 11.6 Özyineleme (rekürsiyon)

Özyineli içiçe sayı listemizdeki tüm sayıları toplamak için listeyi dolaşmak, ve içiçe geçmiş yapısındaki tüm öğeleri dolaşmak, karşılaştığımız her nümerik sayıyı toplamımıza eklemek ve herhangi bir liste öğesi için *bu süreci tekrarlamak* gerekmektedir.

Modern programlama dilleri genellikle **özyineleme**yi desteklemektedir, özyineleme fonksiyonların kendi tanımlarında *kendilerini çağırması*dır. Özyineleme sayesinde, içiçe sayı listesindeki değerlerin toplamını bulacağımız Python kodu şaşırtıcı derecede kısadır:

```py
def recursive_sum(nested_num_list):
    sum = 0
    for element in nested_num_list:
        if type(element) == type([]):
            sum = sum + recursive_sum(element)
        else:
            sum = sum + element
    return sum
```

`recursive_sum` fonksiyonunun gövdesi ağırlıklı olarak `nested_num_list`'i dolaşan bir `for` döngüsünden oluşmaktadır. Eğer `element` nümerik bir sayı ise (`else` dalı), basitçe değeri `sum`'a eklenmektedir. Eğer `element` liste ise, `recursive_sum` fonksiyonu `element` argümanı ile tekrar çağrılmaktadır. Fonksiyon tanımlaması içerisindeki kendisini çağıran cümle **özyineli çağrı** olarak bilinir.

Özyineleme gerçekten bilgisayar bilimlerindeki en güzel ve en şık araçlardan biridir.

Biraz daha karmaşık bir problem olan içiçe sayı listesindeki en büyük değeri bulmak:

```py
def recursive_max(nested_num_list):
    """
 >>> recursive_max([2, 9, [1, 13], 8, 6])
 13
 >>> recursive_max([2, [[100, 7], 90], [1, 13], 8, 6])
 100
 >>> recursive_max([2, [[13, 7], 90], [1, 100], 8, 6])
 100
 >>> recursive_max([[[13, 7], 90], 2, [1, 100], 8, 6])
 100
 """
    largest = nested_num_list[0]
    while type(largest) == type([]):
        largest = largest[0]

    for element in nested_num_list:
        if type(element) == type([]):
            max_of_elem = recursive_max(element)
            if largest < max_of_elem:
                largest = max_of_elem
        else:                           # element liste değilse
            if largest < element:
                largest = element

    return largest

```

Doctestler `recursive_max` çalışmasının örneklerini sağlamak için verilmiştir.

Bu probleme nümerik bir değeri bulmak için eklenmiş olan kıvırma `largest`'in ilklenmesidir. `nested_num_list[0]`'ı kullanamayız, çünkü bu değer sayı da olabilir, bir liste de. Bu sorunu çözmek için `largest`'a hangi derinliğe inerse insin ilk nümerik değeri atayan bir while döngüsü kullanırız.

Yukarıdaki iki örnekte özyineli çağrıya neden olmayan bir **temel durum**a sahiptir: öğenin bir sayı olduğu, liste olmadığı durum. Temel durum olmadan, **sonsuz özyineleme**ye girersiniz ve programınız çalışmaz. Python belirli bir maksimum özyineleme derinliğine ulaştığında çalışmayı durdurup, bir çalışma zamanı hatası döndürür.

Aşağıdaki kodu `infinite_recursion.py` isimli bir dosyaya yazın:

```py
#
# infinite_recursion.py
#
def recursion_depth(number):
    print ("Recursion depth number %d." % number)
    recursion_depth(number + 1)

recursion_depth(0)
```

Programı kaydettiğiniz dizinde komut satırında aşağıdaki komutu çalıştırın:

```py
python infinite_recursion.py
```

Mesajları geçişini izledikten sonra, uzun bir mesaj sonrasında aşağıdakiyle karşılaşacaksınız:

```py
  ...
  File "infinite_recursion.py", line 3, in recursion_depth
    recursion_depth(number + 1)
RuntimeError: maximum recursion depth exceeded
```

Bunun gibi bir durumun programlarımızdan birinde oluşmasını hiç bir zaman istemeyiz. Özyinelemeyi anlatmayı bitirmeden önce, Python'da hataların nasıl kotarıldığını öğrenelim.

## 11.7 İstisnalar (Exceptions)

Her ne zaman bir çalışma zamanı hatası oluşursa, bir **istisna** ortaya çıkar. Program bu noktada çalışmasını durdurur ve hatanın dökümünü verir, bu döküm ortaya çıkan istisnayla biter.

Örneğin sıfırla bölme aşağıdaki istisnayı yaratır:

```py
>>> print (55/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: integer division or modulo by zero
>>>

```

Var olmayan bir liste öğesine erişmeye çalışmak:

```py
>>> a = []
>>> print (a[5])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>>

```

Veya tupleda öğe ataması yapmaya çalışmak:

```py
>>> tup = ('a', 'b', 'd', 'd')
>>> tup[2] = 'c' 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>>

```

Her bir durumda, sondaki hata mesajları iki parçadır: iki nokta üstüsteden önce hatanın tipi, ve iki nokta üstüstüden sonra hatanın ayrıntıları.

Bazı durumlarda istisna yaratabilecek işlemler yapmak isteyebiliriz, ancak programın çalışmasını durdurmasını istemeyiz. Bu gibi durumlarda **istisna işleme (kotarma, handling)** yapmamız gerekir. Bunu da `try` ve `except` cümleleriyle yaparız.

Örneğin, kullanıcıdan bir dosya ismi sorarız ve daha sonra bu dosyayı açmaya çalışırız. Eğer dosya yoksa, programın çökmesini değil, istisnayı işlemeyi isteriz:

```py
filename = input('Enter a file name: ')
try:
    f = open (filename, "r")
except:
    print 'There is no file named', filename
```

`try` cümlesi ilk bloktaki cümleleri işletir. Eğer istisna oluşmazsa, `except` bloğunu yoksayar. Eğer herhangi bir istisna oluşursa, `except` dalı içerisindeki cümleleri çalıştırır ve devam eder.

Bu yeteneği bir fonksiyon içerisine sarabiliriz: `exists` fonksiyonu bir dosya ismi alır ve eğer dosya varsa doğru, yoksa yanlış döndürür:

```py
def exists(filename):
    try:
        f = open(filename)
        f.close()
        return True 
    except:
        return False
```

Farklı istisnaları işlemek için birden fazla `except` kullanabilirsiniz (istisnalar hakkında ayrıntılı bilgi için Python'u yaratan Guido Van Rossum'un [Python Öğrencesi](https://docs.python.org/3.8/tutorial/index.html)ndeki [Hatalar ve İstisnalar](https://docs.python.org/3.8/tutorial/errors.html) dersini inceleyebilirsiniz).

Eğer programınız hata durumunu tespit ederse, bir istisna **tetikleyebilirsiniz**. Aşağıda kullanıcıdan girdi alan ve sayının negatif olmadığını kontrol eden bir örnek görebilirsiniz:

```py
#
# learn_exceptions.py
#
def get_age():
    age = int(input('Please enter your age: '))
    if age < 0:
        raise ValueError, '%s is not a valid age' % age
    return age

```

`raise` cümlesi iki argüman alır: istisna tipi, ve hata hakkında ayrıntılı bilgi. `ValueError` tetiklemek istediğimiz istisnaya en yakın yerleşik istisnadır. Yerleşik istisnaların bütün listesine [Python kütüphane referansı](http://docs.python.org/lib/)nın [2.3 bölümünden](https://docs.python.org/3/library/exceptions.html) ulaşabilirsiniz (yine Guido Van Rossum'un yazdığı).

Eğer çağırdığı fonksiyon `get_age` hatayı kotarırsa, program çalışmaya devam edecektir, diğer durumda Python hata dökümünü yapıp çıkacaktır:

```py
>>> get_age()
Please enter your age: 42
42 
>>> get_age()
Please enter your age: -2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "learn_exceptions.py", line 4, in get_age
    raise ValueError, '%s is not a valid age' % age
ValueError: -2 is not a valid age
>>>
```

Hata mesajı bizim sağladığımız istisna tipini ve ek bilgiyi içermektedir.

İstisna işlemeyi kullanarak, `infinite_recursion.py`'yi değiştirip, izin verilen maksimum özyineleme derinliğine ulaştığında durmasını sağlayabiliriz:

```py
#
# infinite_recursion.py
#
def recursion_depth(number):
    print ("Recursion depth number %d." % number)
    try:
        recursion_depth(number + 1)
    except:
        print "Maximum recursion depth exceeded."

recursion_depth(0)
```

Bu sürümü çalıştırıp, sonuçları gözlemleyin.

## 11.8 Kuyruk özyineleme

Fonksiyon tanımlamasının sonunda bir özyineli çağrı oluşursa, buna **kuyruk özyineleme** adı verilir.

Aşağıda 6. bölümde yazdığımız `gerisayim` fonksiyonunun kuyruk özyineleme ile tekrar yazılmış sürümünü görebilirsiniz:

```py
def gerisayim(n):
    if n == 0:
        print ("Defol!")
    else:
        print (n)
        gerisayim(n-1)
```

Yineleme ile yapılan herhangi bir hesaplama, özyineleme ile de yapılabilir.

Bir çok bilinen matematiksel fonksiyon özyineli olarak tanımlanmıştır. [Faktöriyel](http://en.wikipedia.org/wiki/Factorial), örneğin, özel bir işleçe, `!`, sahiptir ve şu şekilde tanımlanmıştır:

```py
0! = 1
n! = n*(n-1)!
```

Bunu Pythonda kolayca kodlayabiliriz:

```py
def faktoryel(n):
    if n == 0:
        return 1
    else:
        return n * faktoryel(n-1)
```

Matematikte çok bilinen diğer bir özyineli ilişki [fibonacci serisi](http://en.wikipedia.org/wiki/Fibonacci_number)dir, şu şekilde tanımlanmıştır:

```py
fibonacci(0) = 1
fibonacci(1) = 1
fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)
```

Bu da Pythonda kolayca yazılabilir:

```py
def fibonacci (n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
```

Hem `factorial` hem de `fibonacci` kuyruk özyinelemenin örnekleridir.

Kuyruk özyineleme Python gibi dillerde kötü bir alışkanlık olarak kabul edilir, çünkü eşlenik yinelemeli çözüme göre daha fazla sistem kaynağı kullanmaktadır.

`faktoryel(1000)`i çalıştırmak maksimum özyineleme derinliğini aşacaktır. Ve `fibonacci(35)` çalıştırmayı deneyin, ve hesaplamanın ne kadar uzun sürdüğünü gözlemleyin (sabırla bekleyin, hesaplama bitecektir).

`faktoryel`in yinelemeli bir sürümünü yazmanız alıştırma olarak sorulacak, ve bir sonraki bölümde `fibonacci`yi daha iyi bir yolla çözeceğiz.

## 11.9 Liste kavraması

**Liste kavraması** kısa, matematiksel bir sözdizimi kullanarak diğer listelerden yeni listeler yaratmaya yarayan sözdizimsel bir yapıdır:

```py
>>> sayilar = [1, 2, 3, 4]
>>> [x**2 for x in sayilar]
[1, 4, 9, 16]
>>> [x**2 for x in sayilar if x**2 > 8]
[9, 16] 
>>> [(x, x**2, x**3) for x in sayilar]
[(1, 1, 1), (2, 4, 8), (3, 9, 27), (4, 16, 64)]
>>> dosyalar = ['bin', 'Data', 'Desktop', '.bashrc', '.ssh', '.vimrc']
>>> [isim for isim in dosyalar if isim[0] != '.']
['bin', 'Data', 'Desktop']
>>> harfler = ['a', 'b', 'c']
>>> [n*harf for n in sayilar for harf in harfler]
['a', 'b', 'c', 'aa', 'bb', 'cc', 'aaa', 'bbb', 'ccc', 'aaaa', 'bbbb', 'cccc']
>>>
```

Liste kavraması için genel sözdizimi şu şekildedir:

```py
[expr for item1 in seq1 for item2 in seq2 ... for itemx in seqx if condition]
```

Bu liste deyimi aşağıdakiyle aynı etkiye sahiptir:

```py
output_sequence = []
for item1 in seq1:
    for item2 in seq2:
        ...
            for itemx in seqx:
                if condition:
                    output_sequence.append(expr)

```

Gördüğünüz gibi, liste kavraması çok daha kısa ve özdür.

## 11.10 Mini örnek çalışma: tree

Aşağıdaki program Unix'teki [tree](http://en.wikipedia.org/wiki/Tree_(Unix)) programının davranışının bir alt kümesini gerçekleştirmektedir.

```py
#!/usr/bin/env python

import os
import sys


def getroot():
    if len(sys.argv) == 1:
        path = ''
    else:
        path = sys.argv[1]

    if os.path.isabs(path):
        tree_root = path
    else:
        tree_root = os.path.join(os.getcwd(), path)

    return tree_root


def getdirlist(path):
    dirlist = os.listdir(path)
    dirlist = [name for name in dirlist if name[0] != '.']
    dirlist.sort()
    return dirlist


def traverse(path, prefix='|--', s='.\n', f=0, d=0):
    dirlist = getdirlist(path)

    for num, file in enumerate(dirlist):
        lastprefix = prefix[:-3] + '`--'
        dirsize = len(dirlist)

        if num < dirsize - 1:
            s += '%s %s\n' % (prefix, file)
        else:
            s += '%s %s\n' % (lastprefix, file)
        path2file = os.path.join(path, file)

        if os.path.isdir(path2file):
            d += 1
            if getdirlist(path2file):
                s, f, d = traverse(path2file, '| ' + prefix, s, f, d)
        else:
            f += 1

    return s, f, d


if __name__ == '__main__':
    root =  getroot()
    tree_str, files, dirs = traverse(root)

    if dirs == 1:
        dirstring = 'directory'
    else:
        dirstring = 'directories'
    if files == 1:
        filestring = 'file'
    else:
        filestring = 'files'

    print (tree_str)
    print ('%d %s, %d %s' % (dirs, dirstring, files, filestring))
```

Alıştırmaların bir çoğunda bu programı incelemeniz istenecek.

## 11.11 Sözlük

değiştirilemez veri tipi
: Değiştirilemeyen veri tipidir. Değiştirilemez tiplerin öğelerine veya dilimlerine yapılan atamalar çalışma zamanı hatası yaratır.

değiştirilebilir veri tipi
: Değiştirilebilen veri tipleridir. Tüm değiştirilebilen tipler bileşik tiplerdir. Listeler ve sözlükler değiştirilebilir veri tipidir; karakter dizileri ve tuplelar değildir.

tuple
: Herhangi bir tipte öğe dizisi içeren veri tipidir. Liste gibidir ama değiştirilemez. Tuplelar değiştirilemeyen tiplerin gerektirdiği durumlarda kullanılabilir, örneğin sözlükte (sonraki bölüme bakınız) bir anahtar gibi.

tuple ataması
: Tek bir atama ifadesiyle tupledaki tüm öğelere atamadır. Tuple ataması sıralı yerine paralel bir şekilde gerçekleşir, değerlerin birbirleriyle değiştirilmesi için yararlıdır.

veri yapısı
: Kullanımı kolaylaştırmak amacıyla verinin düzenlenmesidir.

özyineli tanımlama
: Kendisini kendi terimleriyle tanımlayan ifadedir. Yararlı olabilmesi için özyineli olmayan *temel durumları* içermelidir. Bu şekilde *döngüsel tanımlama*dan farklıdır. Özyineli tanımlamalar karmaşık veri yapılarını ifade etmenin şık bir yoludur.

özyineleme
: Hali hazırda çalışan fonksiyonun kendisini çağırmasıdır.

özyineli çağrı
: Özyineli bir fonksiyonda kendisini çağıran ifade.

temel durum
: Özyineli fonksiyondaki koşul cümlesinin özyineli çağrı şeklinde sonuçlanmayan bir dalı.

sonsuz özyineleme
: Temel duruma ulaşmadan sürekli olarak kendisini çağıran fonksiyon. Sonsuz özyineleme çalışma zamanı hatası üretir.

istisna
: Çalışma zamanında oluşan hata.

istisna işleme
: Bir istisnanın programın çalışmasını durdurmasını `try` ve `except` cümleleriyle önlemek.

tetikleme
: Bir istisnayı `raise` cümlesiyle üretmek.

kuyruk özyineleme
: Fonksiyon tanımlamasının son cümlesi olarak (kuyrukta) yer alan özyineli çağrı. Kuyruk özyineleme Python programlarında kötü alışkanlık olarak değerlendirilir. Çünkü mantıksal olarak eş fonksiyonlar *yineleme* kullanılarak daha etkin bir şekilde yazılabilir (ayrıntılı bilgi için [tail recursion](http://en.wikipedia.org/wiki/Tail_recursion)).

liste kavrama
: Başka listelerden liste yaratmaya yarayan, matematiksel [küme yapım gösterimine](http://en.wikipedia.org/wiki/Set-builder_notation) benzer sözdizimsel yapı.

## 11.12 Alıştırmalar

- Örnek program

```py

def swap(x, y):      # yanlis surum
     print  ("before swap statement: id(x):", id(x), "id(y):", id(y))
     x, y = y, x
     print  ("after swap statement: id(x):", id(x), "id(y):", id(y))

a, b = 0, 1
print  ("before swap function call: id(a):", id(a), "id(b):", id(b))
swap(a, b)
print  ("after swap function call: id(a):", id(a), "id(b):", id(b))
```

Bu programı çalıştırın ve sonuçları tanımlayın. Sonuçları neden bu `swap` sürümünün istendiği gibi çalışmadığını açıklamak için kullanın. `swap` çağrımından sonra `a` ve `b`'nin değerleri ne olacaktır?

- `seqtools.py` bir modül yaratın. Bu bölümden `encapsulate` ve `insert_in_middle` fonksiyonlarını ekleyin.Her üç dizi tipi için doğru çalışıp çalışmadığını sınayan doctestleri ekleyin.

- Aşağıdaki fonksiyonların herbirini `seqtools.py` dosyasına ekleyin:

```py
def make_empty(seq):
    """
 >>> make_empty([1, 2, 3, 4])
 []
 >>> make_empty(('a', 'b', 'c'))
 ()
 >>> make_empty("No, not me!")
 ''
 """

def insert_at_end(val, seq):
    """
 >>> insert_at_end(5, [1, 3, 4, 6])
 [1, 3, 4, 6, 5]
 >>> insert_at_end('x', 'abc')
 'abcx'
 >>> insert_at_end(5, (1, 3, 4, 6))
 (1, 3, 4, 6, 5)
 """

def insert_in_front(val, seq):
    """
 >>> insert_in_front(5, [1, 3, 4, 6])
 [5, 1, 3, 4, 6]
 >>> insert_in_front(5, (1, 3, 4, 6))
 (5, 1, 3, 4, 6)
 >>> insert_in_front('x', 'abc')
 'xabc'
 """

def index_of(val, seq, start=0):
    """
 >>> index_of(9, [1, 7, 11, 9, 10])
 3
 >>> index_of(5, (1, 2, 4, 5, 6, 10, 5, 5))
 3
 >>> index_of(5, (1, 2, 4, 5, 6, 10, 5, 5), 4)
 6
 >>> index_of('y', 'happy birthday')
 4
 >>> index_of('banana', ['apple', 'banana', 'cherry', 'date'])
 1
 >>> index_of(5, [2, 3, 4])
 -1
 >>> index_of('b', ['apple', 'banana', 'cherry', 'date'])
 -1
 """

def remove_at(index, seq):
    """
 >>> remove_at(3, [1, 7, 11, 9, 10])
 [1, 7, 11, 10]
 >>> remove_at(5, (1, 4, 6, 7, 0, 9, 3, 5))
 (1, 4, 6, 7, 0, 3, 5)
 >>> remove_at(2, "Yomrktown")
 'Yorktown'
 """

def remove_val(val, seq):
    """
 >>> remove_val(11, [1, 7, 11, 9, 10])
 [1, 7, 9, 10]
 >>> remove_val(15, (1, 15, 11, 4, 9))
 (1, 11, 4, 9)
 >>> remove_val('what', ('who', 'what', 'when', 'where', 'why', 'how'))
 ('who', 'when', 'where', 'why', 'how')
 """

def remove_all(val, seq):
    """
 >>> remove_all(11, [1, 7, 11, 9, 11, 10, 2, 11])
 [1, 7, 9, 10, 2]
 >>> remove_all('i', 'Mississippi')
 'Msssspp'
 """

def count(val, seq):
    """
 >>> count(5, (1, 5, 3, 7, 5, 8, 5))
 3
 >>> count('s', 'Mississippi')
 4
 >>> count((1, 2), [1, 5, (1, 2), 7, (1, 2), 8, 5])
 2
 """

def reverse(seq):
    """
 >>> reverse([1, 2, 3, 4, 5])
 [5, 4, 3, 2, 1]
 >>> reverse(('shoe', 'my', 'buckle', 2, 1))
 (1, 2, 'buckle', 'my', 'shoe')
 >>> reverse('Python')
 'nohtyP'
 """

def sort_sequence(seq):
    """
 >>> sort_sequence([3, 4, 6, 7, 8, 2])
 [2, 3, 4, 6, 7, 8]
 >>> sort_sequence((3, 4, 6, 7, 8, 2))
 (2, 3, 4, 6, 7, 8)
 >>> sort_sequence("nothappy")
 'ahnoppty'
 """

if __name__ == "__main__":
    import doctest
    doctest.testmod()
```

Her zamanki gibi, bu fonksiyonları doctestlerin hepsini geçecek şekilde düzeltin.

- Bir fonksiyon yazın, `recursive_min`, içiçe sayı listesindeki en küçük değeri döndürsün:

```py
def recursive_min(nested_num_list):
    """
 >>> recursive_min([2, 9, [1, 13], 8, 6])
 1
 >>> recursive_min([2, [[100, 1], 90], [10, 13], 8, 6])
 1
 >>> recursive_min([2, [[13, -7], 90], [1, 100], 8, 6])
 -7
 >>> recursive_min([[[-13, 7], 90], 2, [1, 100], 8, 6])
 -13
 """
```

Fonksiyonunuz doctestleri geçmelidir.

- Bir fonksiyon yazın, `recursive_count`, `nested_number_list` içerisinde `target` sayısını döndürsün: 

```py
def recursive_count(target, nested_num_list):
    """
 >>> recursive_count(2, [2, 9, [2, 1, 13, 2], 8, [2, 6]])
 4
 >>> recursive_count(7, [[9, [7, 1, 13, 2], 8], [7, 6]])
 2
 >>> recursive_count(15, [[9, [7, 1, 13, 2], 8], [2, 6]])
 0
 >>> recursive_count(5, [[5, [5, [1, 5], 5], 5], [5, 6]])
 6
 """
```

Yine fonksiyonunuz tüm doctestleri geçmelidir.

- Bir fonksiyon yazın, `flatten`, `nested_number_list` içerisindeki tüm değerleri barındıran basit bir sayı listesi döndürsün: 

```py
def flatten(nested_num_list):
    """
 >>> flatten([2, 9, [2, 1, 13, 2], 8, [2, 6]])
 [2, 9, 2, 1, 13, 2, 8, 2, 6]
 >>> flatten([[9, [7, 1, 13, 2], 8], [7, 6]])
 [9, 7, 1, 13, 2, 8, 7, 6]
 >>> flatten([[9, [7, 1, 13, 2], 8], [2, 6]])
 [9, 7, 1, 13, 2, 8, 2, 6]
 >>> flatten([[5, [5, [1, 5], 5], 5], [5, 6]])
 [5, 5, 1, 5, 5, 5, 5, 6]
 """
```

Doctestleri geçtiğini doğrulamak için fonksiyonunuzu çalıştırın.

- `readposint` isminde bir fonksiyon yazın. Fonksiyon kullanıcıdan bir pozitif tamsayı alsın ve girdiyi gereksinimleri karşılayıp karşılamadığına göre sınasın. Örnek bir oturum aşağıdaki gibi olacaktır: 

```py
>>> num = readposint()
Please enter a positive integer: yes
yes is not a positive integer.  Try again.
Please enter a positive integer: 3.14
3.14 is not a positive integer.  Try again.
Please enter a positive integer: -6
-6 is not a positive integer.  Try again.
Please enter a positive integer: 42
>>> num
42
>>> num2 = readposint("Now enter another one: ")
Now enter another one: 31
>>> num2
31
>>>
```

Kullanıcının girdisinin yanlış olduğunu doğrulamak için Python'un istisna işleme düzeneklerini kullanın.

- Aşağıdakilerin herbiri için Python yorumlayıcının üreteceği sonuçları yazın:

	1. Liste doldurma 1
    
    ```py	
	>>> nums = [1, 2, 3, 4]
	>>> [x**3 for x in nums]
	
	```

	2. Liste doldurma 2
    
    ```py	
	>>> nums = [1, 2, 3, 4]
	>>> [x**2 for x in nums if x**2 != 4]
	
	```

	3. Liste doldurma 3
    
    ```py	
	>>> nums = [1, 2, 3, 4]
	>>> [(x, y) for x in nums for y in nums]	
	```

	4. Liste doldurma 4
    
    ```py	
	>>> nums = [1, 2, 3, 4]
	>>> [(x, y) for x in nums for y in nums if x != y]	
	```

Yorumlayıcıda denemeden *önce* sonuçları kavramanız gerekir.

- `pydoc` veya [http://pydoc.org](http://pydoc.org/) adresindeki çevrimiçi belgeleri kullanarak `sys.getrecursionlimit()` ve `sys.setrecursionlimit(n)` fonksiyonlarının ne iş yaptığını öğrenin. Bu modül fonksiyonlarının nasıl çalıştığını iyice anlamak için `infinite_recursion.py`de olduğu gibi bir çok *deney* yaratın.

- `faktoryel` fonksiyonunu özyineleme yerine yineleme (iteration) kullanarak tekrar yazın. Fonksiyonunuzu 1000 argümanıyla çağırın ve ne kadar sürede sonucu ürettiğini not edin.

- İsmi `litter.py` olan bir program yazın, argüman olarak verilen ağacın kökündeki (veya varsayılan olarak verilen o anki dizin) her bir altdizinde `trash.txt` isminde boş bir dosya yaratsın.

Şimdi de `cleanup.py` isminde bir program yazın, bütün bu dosyaları (dikkat edin, `trash.txt` dosyalarını sadece) silsin.
  
  
*İpucu:* Mini örnek çalışmada verdiğimiz `tree` programını bu iki özyineli program için temel olarak kullanın.
