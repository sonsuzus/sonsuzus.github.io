---
title: Python Programlama Ders 7. Karakter dizileri
author: sonsuz
date: 2023-07-03 13:03:18 +0300
categories: [Program,Python]
tags: [python,ders,programlama,karakter,dizi,dize,string,veri,döngü,len,for]
image: python-string.jpg
---



## 7.1 Bileşik veri tipi

Şimdiye kadar beş tip gördük:`int`, `float`, `bool`, `NoneType` ve `str`. Karakter dizileri (str) diğer dört tipten nitelik olarak farklıdır çünkü daha küçük parçalardan (karakterler) oluşmuştur.

Daha küçük parçalardan oluşan tiplere **bileşik veri tipleri** adı verilir. Ne yaptığımıza bağlı olarak, bileşik veri tipine tek bir şeymiş gibi davranabilir veya parçalarına erişmek isteyebiliriz. Bu belirsizlik yararlıdır.

Köşeli parantez işleci bir karakter dizisinden tek bir karakter seçmeye yarar:

```py
>>> fruit = "banana"
>>> letter = fruit[1]
>>> print(letter)
```

`fruit[1]` deyimi fruit değişkeninden 1 numaralı karakteri seçer.  değişkeni sonucu referans eder. `letter` değişkenini ekranda görüntülediğimizde, bir sürprizle karşılaşırız:

```
a
```

`"banana"` kelimesinin ilk harfi `a` değildir, eğer bilgisayar bilimcisi değilseniz. Sapkın nedenlerden dolayı, bilgisayar bilimcileri saymaya her zaman sıfırdan başlarlar. `"banana"` kelimesinin Sıfırıncı (0.) harfi `b`'dir. Birinci (1.)harfi `a` ve ikinci (2.) harfi `n`'dir.

Bir karakter dizisinin sıfırıncı karakterini istiyorsanız, köşeli parantezler içerisine 0 veya sonucu 0 olan bir deyim koyarsınız:

```py
>>> letter = fruit[0]
>>> print(letter)
b
```

Köşeli parantezler içerisindeki deyim **indis (index)** adını alır. Bir dizin sıralı bir kümedeki belli bir öğeyi tanımlar, bizim durumumuzda karakter dizisi içerisindeki karakterlerin kümesini hedeflemektedir. İndis, isimden de anlaşılacağı gibi hangi öğeyi istediğinizi *belirtir*. Herhangi bir tamsayı ifade olabilir.

## 7.2 Uzunluk

`len` fonksiyonu bir karakter dizisindeki karakterlerin sayısını döndürür:

```py
>>> fruit = "banana"
>>> len(fruit)
6
```

Bir karakter dizisinin son harfine ulaşmak için, aşağıdaki gibi bir şeyi kullanmak isteyebilirsiniz:

```py
length = len(fruit)
last = fruit[length]       # ERROR!
```

Bu çalışmaz, çalışma zamanı hatası üretir `IndexError: string index out of range`. Bunun nedeni sıfırdan saymaya başladığımız için, altı tane harf 0 ve 5 arasında numaralanacaktır. Son karakteri seçmek için, `uzunluk`tan bir çıkarmamız gerekir:

```py
length = len(fruit)
last = fruit[length-1]
```

Alternatif olarak, negatif indisleri de kullanabiliriz, bunlar karakter dizisinin sonundan itibaren saymaya başlarlar. `fruit[-1]` deyimi son harfi getirir, `fruit[-2]` sondan ikinci harfi getirir ve böyle devam eder.

## 7.3 Gezinme ve `for` döngüsü

Bir çok hesaplama bir karakter dizisinin bir anda tek bir karakterini işlemeyi barındırır. Genellikle baştan başlar ve sona kadar devam edr. Bu şekildeki işleme yöntemine **gezinme (traversal)** adı verilir. Bir gezinmeyi kodlamanın bir yolu `while` cümlesi kullanmaktır:

```py
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index += 1
```

Bu döngü karakter dizisini dolaşır ve her seferinde bir harfi ekranda görüntüler. Döngü koşulu `index < len(fruit)`, böylece `index` karakter dizisinin uzunluğuna eriştiğinde koşul yanlışlanacak ve döngünün gövdesi yürütülmeyecektir. En son erişilen karakter indisi `len(fruit) - 1` olan karakter olacaktır, bu da karakter dizisindeki son karakterdir.

Bir değer kümesini gezinmede indis kullanımı çok yaygın kullanılan bir yöntem olduğu için Python bir alternatif sağlamaktadır, daha kolay sözdizimine sahip `for` döngüsü:

```py
for char in fruit:
    print(char)
```

Döngüde her anda, karakter dizisindeki bir sonraki karakter `char` değişkenine atanıyor. Döngü hiç karakter kalmayana kadar devam eder.

Aşağıdaki örnek birleştirme işlemi ve `for` döngüsünü kullanarak abecedarian serisi üretmeyi göstermektedir. Abecedarian öğelerin alfabetik bir şekilde sıralanmış seri veya listeyi temsil eder. Örneğin, Robert McCloskey'in kitabı *Make Way for Ducklings*, ördek yavrularının isimleri Jack, Kack, Lack, Mack, Nack, Ouack, Pack ve Quack'tır. Aşağıdaki döngü bu isimleri sıralı olarak ekranda görüntüler:

```py
prefixes = "JKLMNOPQ"
suffix = "ack"
   
for letter in prefixes:
    print(letter + suffix)
```

Programın çıktısı:

```py
Jack
Kack
Lack
Mack
Nack
Oack
Pack
Qack
```

Elbete, bu o kadar doğru değildir çünkü Ouack ve Quack yanlış yazılmıştır. Bunu aşağıdaki alıştırmaların birinde düzelteceksiniz.

## 7.4 Karakter dizisi dilimleri

Bir karakter dizisinin her bir parçasına (alt karakter dizisi - substring) **dilim** adı verilmektedir. Bir dilimi seçmek bir karakteri seçmeye benzer:

```py
>>> s = "Peter, Paul, and Mary"
>>> print(s[0:5])
Peter
>>> print(s[7:11])
Paul
>>> print(s[17:21])
Mary
```

`[n:m]` işleci bir karakter dizisinin n. ve m. karakterleri arasındaki parçasını, (ilk karakteri içerir ancak son karakteri içermez,) döndürür. Bu davranış düşülenin aksine bir davranıştır; eğer indisleri aşağıdaki resimdeki gibi *karakter ara*larını işaret ediyor diye düşünürseniz daha anlamlı gelecektir:

![](illustrations/banana.png)

Eğer ilk indisi yazmazsanız (iki nokta üstüsteden önceki), dilim karakter dizisinin başından başlar. Eğer ikinci indisi yazmazsanız, dilim karakter dizisinin sonuna kadar gider. Böylece:

```py
>>> fruit = "banana"
>>> fruit[:3]
'ban'
>>> fruit[3:]
'ana'
```

Bu durumda `s[:]` ifadesinin ne olduğunu düşünüyorsunuz?

## 7.5 Karakter dizisi karşılaştırma

Karşılaştırma işlecleri karakter dizileri için de çalışır. İki karakter dizisinin eşit olup olmadığını kontrol etmek için:

```py
if word == "muz":
    print("Evet, iki muzumuz var!")
```

Diğer karşılaştırma işleçleri kelimeleri alfabetik sıraya koymak için yararlıdır:

```py
if word < "muz":
    print("Kelimeniz," + word + ", muzdan önce gelir.")
elif word > "muz":
    print("Kelimeniz," + word + ", muzdan sonra gelir.")
else:
    print("Evet, hiç muzumuz yok!")
```

Python'un küçük ve büyük harflere insanların davrandığı gibi davranmadığını unutmamalısınız. Tüm büyük harfler küçük harflerden önce gelir. Bu yüzden:

```
Kelimeniz, Zebra, muzdan önce gelir.
```

Bu probleme yönelik yaygın bir kullanım karakter dizilerini standart bir biçime dönüştürmektir. Örneğin herhangi bir karşılaştırma yapmadan önce hepsini küçük harfe çevirebilirsiniz. Daha büyük problem ise programın zebranın bir meyve olmadığını anlamamasıdır.

## 7.6 Karakter dizileri değişmez

Sadece bir karakteri değiştirmek amacıyla `[]` işlecini atamanın solunda kullanmak isteyebilirsiniz. Örneğin:

```py
greeting = "Merhaba, dünya!"
greeting[0] = 'N'            # ERROR!
print(greeting)
```

`Nerhaba, dünya!` çıktısını üretmek yerine yukarıdaki kod bir çalışma zamanı hatası `TypeError: 'str' object doesn't support item assignment` üretmektedir.

Karakter dizileri **değişmez (immutable)**, bunun anlamı var olan bir karakter dizisini değiştiremezsiniz. En iyi yapabileceğiniz şey var olan karakter dizisi üzerinde bir değişiklik yapıp yeni bir karakter dizisi yaratmaktır:

```py
greeting = "Merhaba, dünya!"
newGreeting = 'N' + greeting[1:]
print (newGreeting)
```

Buradaki çözüm değiştirmek istediğimiz ilk karakterin yeni halini, `greeting` değişkeninde değişmemesi gereken kısımla birleştirmedir. Bu işlemin özgün karakter dizisi üzerinde bir etkisi yoktur.

## 7.7 `in` işleci

`in` işleci bir karakter dizisinin başka bir karakter dizisinde alt karakter dizisi olarak varolup olmadığını sınar:

```py
>>> 'p' in 'apple'
True
>>> 'i' in 'apple'
False
>>> 'ap' in 'apple'
True
>>> 'pa' in 'apple'
False
```

Karakter dizisinin kendisinin de bir alt karakter dizisi olduğunu unutmamak gerekir:

```py
>>> 'a' in 'a'
True
>>> 'apple' in 'apple'
True
```

`in` işlecini karakter dizisi birleştirme (`+` işleci) ile bir araya getirdiğimizde, bir karakter dizisinden tüm sesli harfleri çıkaran bir fonksiyon yazabiliriz:

```py
def remove_vowels(s):
    vowels = "aeıioöuüAEIİOÖUÜ"
    s_without_vowels = ""
    for letter in s:
        if letter not in vowels:
            s_without_vowels += letter
    return s_without_vowels
```

Bu fonksiyonu istediğimizi yapıp yapmadığına dair bir sınamadan geçirin.

## 7.8 Bir karakter indisi bulma (`find`) fonksiyonu

Aşağıdaki fonksiyon ne yapar?

```py
def find(strng, ch):
    index = 0
    while index < len(strng):
        if strng[index] == ch:
            return index
        index += 1
    return -1

```

Bir bakıma, `find` `[]` işlecinin karşıtıdır. İndisi alıp bu indise karşılık gelen karakter yerine, bir karakter alıp o karakterin bulunduğu indisi döndürmektedir. Eğer karakter yok ise, `-1` değerini döndürür.

Bu `return` cümlesini bir döngü içerisinde gördüğünüz ilk örnektir. Eğer `strng[index] == ch` ise, fonksiyon hemen dönecektir, döngü erken bir şekilde sonlandırılmış olacaktır.

Eğer karakter, karakter dizisinin içerisinde bulunamazsa döngü normal bir şekilde tamamlanacak ve fonksiyon `-1` değerini döndürecektir.

Bu tarz hesaplama şablonuna **euraka gezinimi** denilmektedir çünkü sonucu bulur bulmaz, Euraka! diye bağırıp aramayı bırakabiliriz.

## 7.9 Döngü ve sayma

Aşağıdaki program `a` harfinin bir karakter dizisinde kaç kere gözüktüğünü sayar, ve [6. bölümde](https://sonsuzus.github.io/posts/python-programlama-ders-06/) anlattığımız sayma şablonunun bir başka örneğidir:

```py
fruit = "banana"
count = 0
for char in fruit:
    if char == 'a':
        count += 1
print (count)
```

## 7.10 İsteğe bağlı parametreler

Bir karakterin bir karakter dizisinde ikinci veya üçüncü konumlarını bulmak istersek, `find` fonksiyonunu bir üçüncü parametre -- aramanın yapıldığı karakter dizisinde aramaya başlama indisi -- ekleyerek değiştirebiliriz:

```py
def find2(strng, ch, start):
    index = start 
    while index < len(strng):
        if strng[index] == ch:
            return index
        index += 1
    return -1
```

`find2('banana','a',2)` şimdi `3` değerini döndürmektedir, bu değer 'a' karakterinin 2. indisten sonraki ilk bulunduğu yerin indisidir. `find2('banana','n',3)` ne döndürecektir? Eğer, 4 dediyseniz `find2`'nin nasıl çalıştığına dair bir fikriniz oluşmuş demektir.

Daha iyisi, `find` ve `find2` fonksiyonlarını **isteğe bağlı (optional) parametre** kullanarak birleştirebiliriz:

```py
def find(strng, ch, start=0):
    index = start 
    while index < len(strng):
        if strng[index] == ch:
            return index
        index += 1
    return -1
```

Fonksiyonunun bu sürümüne yapılan `find('banana', 'a', 2)` çağrımı aynen `find2` gibi davranacaktır, `find('banana','a')` çağrımında ise `start` **varsayılan (default) değer**e yani 0'a değerine sahip olacaktır.

`find` fonksiyonuna yeni bir isteğe bağlı parametre ekleyerek kodumuzun her iki yönde (ileri, geri) arama yapmasını sağlayabiliriz:

```py
def find(strng, ch, start=0, step=1):
    index = start 
    while 0 <= index < len(strng):
        if strng[index] == ch:
            return index
        index += step 
    return -1

```

`step` için `-1` değeri geçirmemiz karakter dizisinin sonu yerine başından arama yapmamızı sağlayacaktır. Unutulmaması gereken, `index` değişkenini alabileceği en yüksek değer olduğu kadar bu değişikliği karşılayabilmek için en düşük değerler için de kontrol etmemiz gerekmektedir.

## 7.11 `string` modülü

`string` modülü karakter dizileri üzerinde işlemler yapmamız için gereken yararlı fonksiyonlar içermektedir. Her modül için olduğu gibi kullanmadan önce bu modülü de içe aktarmamız gerekmektedir:

```py
>>> import string
```

Bu modülün içerdiklerini görmek için, `dir` fonksiyonunu argüman olarak modül ismini vererek kullanabiliriz.

```py
>>> dir(string)
```

bu deyim `string` modülü içerisindeki öğelerin listesini döndürecektir:  

`['Template', '_TemplateMetaclass', '__builtins__', '__doc__',
'__file__', '__name__', '_float', '_idmap', '_idmapL', '_int',
'_long', '_multimap', '_re', 'ascii_letters', 'ascii_lower()',
'ascii_upper()', 'atof', 'atof_error', 'atoi', 'atoi_error',
'atol', 'atol_error', 'capitalize', 'capwords', 'center', 'count',
'digits', 'expandtabs', 'find', 'hexdigits', 'index',
'index_error', 'join', 'joinfields', 'letters', 'ljust', 'lower',
'lower()', 'lstrip', 'maketrans', 'octdigits', 'printable',
'punctuation', 'replace', 'rfind', 'rindex', 'rjust', 'rsplit',
'rstrip', 'split', 'splitfields', 'strip', 'swapcase', 'translate',
'upper', 'upper()', 'whitespace', 'zfill']`

Bu listedeki herhangi bir öğe hakkında daha fazla bilgi almak istersek, `type` komutunu kullanabiliriz. Modül ismini ve **nokta işareti**nden sonra da öğe ismini yazarak sonucu inceleyebiliriz. Python 3 den itibaren string modülündeki fonksiyonları modülü eklemeden de kullanabiliyoruz.

```py
>>> type(string.digits)
<type 'str'>
>>> type(string.find)
<type 'function'>

```

`string.digits` bir karakter dizisi olduğuna göre, içeriğini ekranda görüntüleyebiliriz:

```py
>>> print (string.digits)
0123456789
```

Şaşırtmayacak şekilde, onluk sistemdeki rakamları içeriyor.

`string.find` bizim yazdığımız fonksiyonla neredeyse aynı şeyi yapan bir fonksiyon. Hakkında daha fazla bilgi almak için **docstring**'ini (`__doc__`) -- fonksiyonun belgelendirilmesidir -- ekranda görüntüleyebiliriz:

```py
>>> print (string.find.__doc__)
find(s, sub [,start [,end]]) -> in

    Return the lowest index in s where substring sub is found,
    such that sub is contained within s[start,end].  Optional
    arguments start and end are interpreted as in slice notation.

    Return -1 on failure.
```

Köşeli parantez içerisindeki parametreler isteğe bağlı parametrelerdir. `string.find` fonksiyonunu bizim yazdığımız `find` fonksiyonu ile aynı şekilde kullanabiliriz:

```py
>>> fruit = "banana"
>>> index = string.find(fruit, "a")
>>> print (index)
1

```

Bu örnek, modüllerin bir yararını göstermektedir, var olan (built-in) fonksiyonlar ile kullanıcı tanımlı fonksiyonların isimden dolayı karışmasını önler. Nokta işaretini kullanarak hangi `find` sürümünü kullanmak istediğimizi belirtebiliriz.

Aslında, `string.find` bizim fonksiyondan daha genel bir sürümdür. Sadece karakterleri değil, alt karakter dizilerini de bulabilir:

```py
>>> string.find("banana", "na")
2
```

Bizimki gibi, başlaması gereken indisi bir ek argüman olarak alabilir:

```py
>>> string.find("banana", "na", 3)
4
```

Bizimkinden farklı olarak ikinci isteğe bağlı parametresi, aramayı bitirmesi gereken indisi vermek için:

```py
>>> string.find("bob", "b", 1, 2)
-1
```

Bu örnekte arama başarısız olur çünkü *b* harfi verdiğimiz indis aralığında (`1`'den `2`'ye - `2` dahil değil) yoktur.

## 7.12 Karakter sınıflandırma

Bir karakteri incelemek ve büyük-küçük olduğunu kontrol etmek veya harf mi rakam mı olduğunu belirlemek genellikle yararlıdır. `string` modülü bu iş için bir çok sabit sağlamaktadır. Bu sabitlerden biri, `string.digits()`, daha önce içeriğini gördüğümüz bir sabittir.

`string.lower()` sistemin küçük harf olarak tanımladığı tüm harfleri içerir. Benzer bir şekilde `string.upper()` bütün büyük harfleri içerir. Aşağıdakini deneyip sonucunu inceleyebilirsiniz:

```py
print (string.lower())
print (string.upper())
print (string.digits)
```

Bu sabitleri ve `find` fonksiyonunu karakterleri sınıflandırmak için kullanabiliriz. Örneğin, eğer `find(lower(),ch)` fonksiyon çağrımı `-1`'den farklı bir değer döndürürse, `ch` küçük harf olmalıdır:

```py
def is_lower(ch):
    return string.find(string.lower(), ch) != -1
```

Bir alternatif olarak, `in` işlecinin avantajını kullanabiliriz:

```py
def is_lower(ch):
    return ch in string.lower()
```

Başka bir alternatif olarak, karşılaştırma işlecini kullanabiliriz:

```py
def is_lower(ch):
    return 'a' <= ch <= 'z'
```

Eğer `ch` *a* ve *z* arasında ise, küçük harf olmak zorundadır.

`string` modülünde bulunan başka bir sabit ekranda görüntülediğiniz zaman sizi şaşırtabilir:

```py
>>> print string.whitespace

```

**Boş karakterler (whitespace)** imleci herhangi bir şey görüntülemeden hareket ettiren karakterlerdir. Görünür karakterler arasında beyaz boşluklar (en azından beyaz kağıt üstünde) yaratırlar. `string.whitespace` sabiti tüm boş karakterleri -- boşluk, tab (\t) ve yeni satır (\n) -- içerir:

`string` modülü içerisinde bir sürü başka yararlı fonksiyon vardır, ancak bu kitap referans el kitabı amacı gütmediği için tüm bu yararlı fonksiyonları burada anlatmayacağız. *Python Kütüphane Referansı (Python Library Reference)*, referans kitabıdır. Diğer bir çok yararlı belgeyle birlikte Python web sitesinden erişilebilir, [http://www.python.org](http://www.python.org/)

## 7.13 Karakter dizisi biçimlendirme

Python programlamada bir karakter dizisini biçimlendirmenin en kesin ve güçlü yolu *karakter dizisi biçimlendirme işleci*ni, `%`, Python'un karakter dizisi biçimlendirme işlemleriyle birlikte kullanmaktır. Bunun nasıl çalıştığını görmek için, aşağıdaki bir kaç örnekle başlayalım:

```py
>>> "His name is %s."  % "Arthur"
'His name is Arthur.'
>>> name = "Alice"
>>> age = 10
>>> "I am %s and I am %d years old." % (name, age)
'I am Alice and I am 10 years old.'
>>> n1 = 4
>>> n2 = 5
>>> "2**10 = %d and %d * %d = %f" % (2**10, n1, n2, n1 * n2)
'2**10 = 1024 and 4 * 5 = 20.000000'
>>>
```

Karakter dizisi biçimlendirme işleminin sözdizimi şu şekildedir:

```py
"<BICIM>" % (<DEGERLER>)
```

Peşpeşe gelen karakterler ve *dönüştürme belirtimlerinden* oluşan *biçim* ile başlar. Dönüştürme belirtimleri `%` işleci ile başlar. Biçim karakter dizisini tek bir `%` işareti ve *her bir dönüşüm belirtimi* için peşpeşe gelen değerler izler, değerler virgül ile ayrılmıştır ve parantez içerisine alınmıştır. Tek bir değer olması durumunda parantezler isteğe bağlıdır.

Yukarıdaki ilk örnekte, tek bir dönüştürme değeri vardır, `%s`, bu bir karakter dizisini gösterir. Ve tek bir değer, `"Arthur"` bu işaretten etkilenir, dikkat edilirse parantez kullanılmamıştır.

İkinci örnekte, `name` karakter dizisi değerine sahiptir, `"Alice"`; `age` tamsayı değerine sahiptir, `10`. Bu iki dönüştürme belirtimine eşlenir, `%s` ve `%d`. İkinci dönüştürme belirtimindeki `d` karakteri değerin bir onluk tamsayı olduğunu belirtir.

Üçüncü örnekte `n1` ve `n2` değişkenleri `4` ve `5` tamsayı değerlerine sahipler. Biçim karakter dizisinde dört dönüştürme belirtimi var: üç `%d` ve bir `%f`. `f` karakteri değerin kayan noktalı sayı olarak temsil edilmesi gerektiğini belirtir. Dört dönüştürme belirtimine eşlenen dört değer ise: `2**10`, `n1`, `n2` ve `n1 * n2`'dir.

`s`, `d`, ve `f` karakterlerinin hepsi bu kitap için gereksinim duyacağımız dönüştürme tipleridir. Dönüştürme karakterlerinin tüm listesini incelemek için Python Library Reference kitabının [String Formatting Operations (Karakter Dizisi Biçimlendirme İşlemleri)](https://docs.python.org/tr/3/library/string.html) bölümüne bakabilirsiniz.

## 7.14 Sözlük

bileşik veri tipi:
: Değerleri kendileri de bir değer olan bileşenlerden veya öğelerden üretilmiş olan veri tipidir.

indis:
: Sıralı bir kümenin (karakter dizisindeki karakterler) bir üyesini seçmek için kullanılan değer veya değişkendir.

gezinme:
: Bir kümenin öğeleri arasında sırayla dolaşma ve her bir öğe üzerinde benzer işlemleri gerçekleştirmedir.

dilim:
: Bir karakter dizisinin indis aralığıyla belirlenmiş bir parçasıdır. Daha genel olarak, Pyton içerisinde bulunan herhangi bir dizinin dilim işleci ile (`dizi[başlangıç:bitiş]`) alt dizisidir.

değişmez (immutable):
: Öğelerine ayrı ayrı yeni bir değer atanamayan bileşik veri tipidir.

isteğe bağlı parametre:
: Fonksiyon başlığında kendisine varsayılan değerin atandığı ve eğer fonksiyon çağrımında ilgili parametre için bir argüman verilmezse bu varsayılan değeri kullanacak olan parametredir.

varsayılan (default) değer:
: İsteğe bağlı bir parametreye verilen ve fonksiyon çağrımında argüman verilmemesi durumunda kullanılacak olan değerdir.

nokta gösterimi:
: Bir modül içerisindeki fonksiyonlara erişmek için **nokta işlecinin** (`.`) kullanılmasıdır.

docstring:
: Bir fonksiyon veya modül tanımlamasındaki ilk satırda bulunan karakter dizisi şeklindeki sabittir (ileride göreceğimiz gibi sınıf ve metot tanımlamalarında da bulunacak). Docstringler kod ile belgelendirmeyi birleştirmek için kullanılan geleneksel bir yöntemdir. Docstringler ayrıca `doctest` modülü tarafından otomatik sınama için kullanılmaktadır.

boş karakterler (whitespace):
: İmleci bir şey görüntülemeden hareket ettiren herhangi bir karakterdir. `string.whitespace` sabiti tüm boş karakterleri içerir.

## 7.15 Alıştırmalar

- Aşağıdaki kodu `Ouack` ve `Quack` kelimeleri doğru bir şekilde yazılacak şekilde düzeltin:

```py
prefixes = "JKLMNOPQ"
suffix = "ack"
   
for letter in prefixes:
    print (letter + suffix)
```

- Aşağıdaki fonksiyonu `count_letters` isminde ve karakter dizisi ile karakteri argüman alacak şekilde genelleştirip bir fonksiyon şekline getirin:

```py
fruit = "banana"
count = 0
for char in fruit:
    if char == 'a':
        count += 1
print (count)
```

- `count_letters` fonksiyonunu tekrar yazarak, karakter dizisini gezinmesi yerine `find` fonksiyonunu (8.10 bölümündeki sürümü) sayılan harfin yeni bulunuşları için kullanılacak isteğe bağlı bir parametre ile tekrar tekrar çağırsın.

- `is_lower` fonksiyonunun hangi sürümünün daha hızlı olduğunu düşünüyorsunuz? Bir sürümü diğerine tercih etmek için hızdan başka nedenler düşünebiliyor musunuz?

- `stringtools.py` isminde bir dosya yaratıp aşağıdakiler içerisine koyun:

```py
def reverse(s):
    """
 >>> reverse('happy')
 'yppah'
 >>> reverse('Python')
 'nohtyP'
 >>> reverse("")
 ''
 >>> reverse("P")
 'P'
 """

if __name__ == '__main__':
    import doctest
    doctest.testmod()

```

Doctestlerin başarılı olması için `reverse` fonksiyon gövdesini yazın.

- `stringtools.py` içerisine `mirror` kodunu koyun.

```py
def mirror(s):
    """
 >>> mirror("good")
 'gooddoog'
 >>> mirror("yes")
 'yessey'
 >>> mirror('Python')
 'PythonnohtyP'
 >>> mirror("")
 ''
 >>> mirror("a")
 'aa'
 """
```

Doctestler ile tanımlanmış işlemi yapabilmesi için fonksiyon gövdesini yazın.

- `stringtools.py` içerisine `remove_letter` fonksiyonunu ekleyin.

```py
def remove_letter(letter, strng):
    """
 >>> remove_letter('a', 'apple')
 'pple'
 >>> remove_letter('a', 'banana')
 'bnn'
 >>> remove_letter('z', 'banana')
 'banana'
 >>> remove_letter('i', 'Mississippi')
 'Msssspp'
 """
```

Doctestler ile tanımlanmış görevi yapabilmesi için fonksiyon gövdesini yazın.

- Son olarak, aşağıdaki fonksiyonların gövdesini her seferinde biri olacak şekilde doldurun.

```py
def is_palindrome(s):
    """
 >>> is_palindrome('abba')
 True
 >>> is_palindrome('abab')
 False
 >>> is_palindrome('tenet')
 True
 >>> is_palindrome('banana')
 False
 >>> is_palindrome('straw warts')
 True
 """

def count(sub, s):
    """
 >>> count('is', 'Mississippi')
 2
 >>> count('an', 'banana')
 2
 >>> count('ana', 'banana')
 2
 >>> count('nana', 'banana')
 1
 >>> count('nanan', 'banana')
 0
 """

def remove(sub, s):
    """
 >>> remove('an', 'banana')
 'bana'
 >>> remove('cyc', 'bicycle')
 'bile'
 >>> remove('iss', 'Mississippi')
 'Missippi'
 >>> remove('egg', 'bicycle')
 'bicycle'
 """

def remove_all(sub, s):
    """
 >>> remove_all('an', 'banana')
 'ba'
 >>> remove_all('cyc', 'bicycle')
 'bile'
 >>> remove_all('iss', 'Mississippi')
 'Mippi'
 >>> remove_all('eggs', 'bicycle')
 'bicycle'
 """

```

Tüm doctestlerin başarılı olması gerektiğini unutmayın.

- Aşağıdaki biçimlendirilmiş karakter dizilerin Python kabuğunda sınayıp sonuçları inceleyin:

	1. "%s %d %f" % (5, 5, 5)

	2. "%-.2f" % 3

	3. "%-10.2f%-10.2f" % (7, 1.0/2)

	4. print " $%5.2f\n $%5.2f\n $%5.2f" % (3, 4.5, 11.2)

- Aşağıdaki biçimlendirilmiş karakter dizilerinde hata var, hataları düzeltin:

	1. "%s %s %s %s" % ('this', 'that', 'something')

	2. "%s %s %s" % ('yes', 'no', 'up', 'down')

	3. "%d %f %f" % (3, 3, 'three')
