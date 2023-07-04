---
title: Python Programlama Ders 10. Modüller ve dosyalar
author: sonsuz
date: 2023-07-04 01:41:05 +0300
categories: [Program,Python]
tags: [python,ders,programlama,modül,dosya]
---



## 10.1 Modüller

**Modül**, diğer Python programları tarafından kullanılmak üzere Python tanımlamaları ve cümlelerini içeren bir dosyadır. Python'la birlikte **standart kütüphane**nin parçası olarak gelen bir çok Python modülü vardır. Bunlardan iki tanesini daha önce gördük, `doctest` ve `string` modülleri.

## 10.2 pydoc

**pydoc** modülünü sistemde kurulu olan Python kütüphanelerini içerisinde arama yapmak için kullanabilirsiniz. **Komut satırı**nda aşağıdakini yazın:

```
$ pydoc -g
```

ve aşağıdaki görüntülenecektir:

![](illustrations/pydoc_tk.png)

(*not*: bir hata ile karşılaşırsanız 2. alıştırmaya bakın)

`pydoc` ile üretilmiş belgeleri ağ tarayıcı penceresinde görüntülemek için open browser düğmesine basın:

![](illustrations/pydoc_firefox.png)

Bu sistemdeki Python tarafından bulunan bütün python kütüphanelerinin bir listesidir. Bir modül ismine tıkladığınızda, o modülün belgelemesi açılacaktır. Bir `keyword`e tıkladığınızda, örneğin, aşağıdaki pencere açılacaktır:

![](illustrations/pydoc_keyword_firefox.png)

Çoğu modülün belgeleri üç renkli kod kısımları içermektedir:

* *Sınıflar* pembe
* *Fonksiyonlar* turuncu
* *Veri* yeşil

Sınıflar daha sonraki bölümlerde anlatılacaktır, ama şimdi pydocu modüller içerisindeki fonksiyonları ve verileri görmek için kullanabiliriz.

`keyword` modülü tek bir fonksiyon içermektedir, `iskeyword`, isminden de anlaşılacağı gibi parametre olarak aldığı karakter dizisi bir anahtar kelime ise `True` değerini döndüren boolean bir fonksiyondur:

```py
>>> from keyword import *
>>> iskeyword('for')
True
>>> iskeyword('all')
False
>>>

```

Veri öğesi, `kwlist` Python'da yer alan tüm anahtar kelimelerin bir listesini içerir:

```py
>>> from keyword import *
>>> print (kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>>
```

Sizi `pydoc`'u Python ile birlikte gelen kapsamlı kütüphaneleri araştırmanız için kullanmaya teşvik ediyoruz. Keşfedilecek bir çok hazine var!

## 10.3 Modül yaratma

Modül yaratmak için bütün yapılması gereken uzantısı `.py` olan bir metin dosyasıdır:

```py
# seqtools.py
#
def remove_at(pos, seq):
    return seq[:pos] + seq[pos+1:]

```

Modülümüzü hem betiklerde hem de Python kabuğunda kullanabiliriz. Bunu yapabilmek için öncelikle modülümüzü *içe aktarmak (import)* gerekmektedir. Bunu yapmanın iki yolu vardır:

```py
>>> from seqtools import remove_at
>>> s = "A string!"
>>> remove_at(4, s)
'A sting!'

```

ve:

```py
>>> import seqtools
>>> s = "A string!"
>>> seqtools.remove_at(4, s)
'A sting!'

```

İlk örnekte, `remove_at` daha önce gördüğümüz fonksiyonlar gibi çağrıldı. İkinci örnekte modülün ismi ve bir nokta (.) fonksiyon isminden önce yazıldı.

İki durumda da dosyayı içe aktarırkan `.py` uzantısını yazmadığımıza dikkat edin. Python, Python modüllerinin `.py` uzantısı ile bitmesini beklemektedir, bu nedenle dosya uzantısı **içe aktarma cümlesi** yer almaz.

Modül kullanımı çok büyük programları yönetilebilir büyüklükte parçalara bölmemize ve ilişkili parçaları birlikte tutmamıza yaramaktadır.

## 10.4 İsim uzayları

**İsim uzayı** sözdizimsel bir kaptır. Sayesinde aynı ismin farklı modül veya fonksiyonlarda (yakında göreceğimiz gibi sınıf ve metotlarda) kullanılmasına izin verir.

Her modül kendi isim uzayını belirler, böylece aynı ismi farklı modüllerde bir tanımlama problemiyle karşılaşmadan kullanabiliriz.

```py
# module1.py

question = "What is the meaning of life, the Universe, and everything?"
answer = 42
```

```py
# module2.py

question = "What is your quest?"
answer = "To seek the holy grail."
```

Şimdi her iki modülü de içe aktarıp içerilerindeki `question` ve `answer` erişebiliriz:

```

>>> import module1
>>> import module2
>>> print module1.question
What is the meaning of life, the Universe, and everything?
>>> print module2.question
What is your quest?
>>> print module1.answer
42
>>> print module2.answer
To seek the holy grail.
>>>

```

Eğer `from module1 import *` ve
`from module2 import *` kullansaydık bir **isimlendirme çakışması**yla karşılaşabilirdik ve `module1`deki `question` ve `answer`'a erişemezdik.

Fonksiyonlar da kendi isim uzaylarına sahiptir:

```py
def f():
    n = 7
    print ("printing n inside of f: %d"  % n)

def g():
    n = 42
    print ("printing n inside of g: %d"  % n)

n = 11
print ("printing n before calling f: %d"  % n)
f()
print ("printing n after calling f: %d"  % n)
g()
print ("printing n after calling g: %d"  % n)
```

Bu programı çalıştırmak aşağıdaki çıktıyı üretir:

```
printing n before calling f: 11
printing n inside of f: 7
printing n after calling f: 11
printing n inside of g: 42
printing n after calling g: 11
```

Üç `n` burada çakışmaz çünkü her biri ayrı isim uzayındadır.

İsim uzayları birden fazla programcının aynı projede isim çakışmalarıyla karşılaşmadan birlikte çalışmasına olanak sağlar.

## 10.5 Özellikler ve nokta işleci

Modül içerisinde tanımlanmış olan değişkenlere modülün **özellikler**i denir. Bu özelliklere **nokta işleci** (`.`) ile erişilir. `module1` ve `module2`'nin `question` özelliklerine `module1.question` ve `module2.question` şeklinde erişilmektedir.

Modüller özellikler gibi, fonksiyonlar da içermektedir ve nokta işleci aynı şekilde fonksiyonlara erişmek için de kullanılmaktadır. `seqtools.remove_at` ifadesi `seqtools` modülünün `remove_at` fonksiyonunu temsil etmektedir.

Bölüm 7'de `string` modülünün `find` fonksiyonunu tanıtmıştık. `string` modülü daha başka bir çok yararlı fonksiyon içermektedir:

```py
>>> import string
>>> string.capitalize('maryland')
'Maryland'
>>> string.capwords("what's all this, then, amen?")
"What's All This, Then, Amen?"
>>> string.center('How to Center Text Using Python', 70)
'                   How to Center Text Using Python                    '
>>> string.upper('angola')
'ANGOLA'
>>> 

```

string modülündeki diğer fonksiyon ve özellikleri öğrenmek için pydoc'u kullanmalısınız. Fakat Python 3 ile birlikte string ifade kullanımı değişmiştir. Bu yüzden yukarıdaki program çalışmayacaktır. 

## 10.6 Karakter dizisi ve liste metotları

Python dili geliştikçe, `string` modülündeki fonksiyonların bir çoğu ayrıca karakter dizisi nesnesi **metotları** olarak eklendi. Metot bir fonksiyona oldukça benzer, ama çağırma sözdizimi biraz farklıdır:

```py
>>> 'maryland'.capitalize()
'Maryland'
>>> "what's all this, then, amen?".title()
"What'S All This, Then, Amen?"
>>> 'How to Center Text Using Python'.center(70)
'                   How to Center Text Using Python                    '
>>> 'angola'.upper()
'ANGOLA'
>>>

```

Karakter dizisi metotları string nesneleri içerisinde yer alırlar, ve nesneden sonra nokta işleci, sonrasında metot ismiyle *çağrılırlar (invoke)*.

Kendi nesnelerimizi, kendi metotlarımızla nasıl oluşturacağımızı ileriki bölümlerde öğreneceğiz. Şimdilik Python'un yerleşik nesneleriyle gelen metotları nasıl kullanacağımızı göreceğiz.

Nokta işleci liste nesnelerinin yerleşik metotlarına erişmek için de kullanılmaktadır:

```py
>>> mylist = []
>>> mylist.append(5)
>>> mylist.append(27)
>>> mylist.append(3)
>>> mylist.append(12)
>>> mylist
[5, 27, 3, 12]
>>>
```

`append` verilen parametreyi listenin sonuna ekleyen bir liste metotudur. Bu örnekle devam edecek olursak, bir çok diğer liste metotu şunlardır:

```py
>>> mylist.insert(1, 12)
>>> mylist
[5, 12, 27, 3, 12]
>>> mylist.count(12)
2
>>> mylist.extend([5, 9, 5, 11])
>>> mylist
[5, 12, 27, 3, 12, 5, 9, 5, 11])
>>> mylist.index(9)
6
>>> mylist.count(5)
3
>>> mylist.reverse()
>>> mylist
[11, 5, 9, 5, 12, 3, 27, 12, 5]
>>> mylist.sort()
>>> mylist
[3, 5, 5, 5, 9, 11, 12, 12, 27]
>>> mylist.remove(12)
>>> mylist
[3, 5, 5, 5, 9, 11, 12, 27]
>>>
```

Bu örnekteki liste metotlarıyla denemeler yapmaya, nasıl çalıştıklarını gerçekten anladığınıza güvenene kadar devam edin.

## 10.7 Metin dosyalarını okuma ve yazma

Bir program çalışırken, verisi *rastgele erişimli bellek*te (RAM) saklanmaktadır, ancak bu bellek **geçici** (volatile)dir, bunun anlamı programın çalışması sonlandığında, veya bilgisayar kapandığında, RAM'deki veri kaybolur. Bilgisayarı açtığınızda ve programınızı çalıştırdığınızda bu veriye tekrar ulaşmak istiyorsanız, veriyi **kalıcı** (non volatile) bir depo ortamına - sabit disk, usb disk, yazılabilir CD, vb. - yazmanız gerekir.

Kalıcı depo ortamındaki veri **dosyalar** adı verilen isimlendirilmiş konumlarda saklanmaktadır. Dosyaları okuyarak ve yazarak, programlar çalıştırmalar arasında bilgi saklayabilir.

Dosyalarla çalışmak not defterleriyle çalışmaya benzer. Bir not defteri kullanabilmek için öncelikle açmanız gerekir. İşiniz bittikten sonra da kapatmanız gerekir. Not defteri açıkken yazabilir veya okuyabilirsiniz. Her iki durumda da not defterinde nerede kaldığınızı bilirsiniz. Not defterinin hepsini doğal sırasında okuyabilirsiniz veya bazı kısımları atlayabilirsiniz.

Bütün bunlar dosyalar için de geçerlidir. Bir dosyayı açmak için ismini belirtir ve hangi amaçla - okuma veya yazma - açtığınızı söylersiniz. 

Bir dosya açmak bir `file` nesnesi yaratır. Aşağıdaki örnekte `myfile` yeni dosya nesnesini göstermektedir.

```py
>>> myfile = open('test.dat', 'w')
>>> print (myfile)
<open file 'test.dat', mode 'w' at 0x2aaaaab80cd8>

```

open fonksiyonu iki argüman almaktadır. İlk argüman dosyanın ismidir, ikinci argümanda **mod**tur. `'w'` modunun anlamı dosyayı yazmak için açtığımızdır.

Eğer `test.dat` isminde bir dosya yoksa, yaratılacaktır. Eğer hali hazırda bir tane varsa, yeni yazacağımız dosyayla değiştirilerecektir.

Dosya nesnesini yazarken, dosyanın ismini, modunu, ve nesnenin konumunu görürüz.

Dosyaya veri koymak için dosya nesnesindeki `write` metotunu çalıştırırız:

```py
>>> myfile.write("Now is the time")
>>> myfile.write("to close the file")
```

Dosyayı kapatmak sisteme yazma işimizin bittiğini söyler, böylece dosyamız okumak için elverişli hale gelir:

```py
>>> myfile.close()
```

Şimdi dosyayı tekrar açabiliriz, ancak bu sefer okumak için, ve içeriği bir karakter dizisine okuruz. Okumak için mod argümanı `'r'`dir:

```py
>>> myfile = open('test.dat', 'r')
```

Eğer olmayan bir dosyayı açmaya çalışırsak, bir hatayla karşılaşırız:

```py
>>> myfile = open('test.cat', 'r')
IOError: [Errno 2] No such file or directory: 'test.cat'
```

Tahmin edebileceğiniz gibi, `read` metotu dosyadaki tüm veriyi okumaktadır. Argümansız işletilirse, dosyanın tüm içeriğini tek bir karakter dizisine okuyacaktır:

```py
>>> text = myfile.read()
>>> print (text)
Now is the timeto close the file

```

Gördüğünüz üzere time ve to arasında boşluk yok, çünkü dosyaya yazarken karakter dizileri arasına boşluk koymadık.

`read` ayrıca okunacak karakter sayısını belirleyen bir argüman da alabilir:

```py
>>> myfile = open('test.dat', 'r')
>>> print (myfile.read(5))
Now i
```

Eğer dosyada yeterince karakter kalmazsa, `read` kalan karakterleri döndürecektir. Dosyanın sonuna geldiğimizde `read` boş bir karakter dizisi okuyacaktır:

```py
>>> print (myfile.read(1000006))
s the timeto close the file
>>> print (myfile.read())
   
>>>
```

Aşağıdaki fonksiyon bir dosyayı kopyalar, tek bir seferde elli karakter okuyup yazarak kopyalamayı gerçekleştirir. İlk argüman kaynak olan asıl dosyamızın, ikinci argüman da yeni yaratılacak olan hedef dosyamızın ismidir.

```py
def copy_file(oldfile, newfile):
    infile = open(oldfile, 'r')
    outfile = open(newfile, 'w')
    while True:
        text = infile.read(50)
        if text == "":
            break
        outfile.write(text)
    infile.close()
    outfile.close()
    return
```

Bu fonksiyon `infile`'dan 50 karakter okur ve `outfile`'a 50 karakter yazar, döngüye `infile`'ın sonuna erişene kadar devam eder, sonuna eriştiğimizde `text` boştur ve `break` cümlesi işletilir.

## 10.8 Metin dosyaları

**Metin dosyası** yazdırılabilir karakterler ve beyaz boşluklar içeren, satırlar şeklinde düzenlenmiş, satırlar birbirinden yeni satır karakterleriyle ayrılmış dosyadır. Python özellikle metin dosyalarını işlemek için tasarlandığı için, bu işi kolaylaştırmak için metotlar sunar.

Gösterim için, yeni satır karakteriyle ayrılmış üç satır metinden oluşan bir metin dosyası yaratacağız:

```py
>>> outfile = open("test.dat","w")
>>> outfile.write("line one\nline two\nline three\n")
>>> outfile.close()
```

`readline` metotu bütün karakterleri, yeni satır karakteri de dahil olmak üzere, okur:

```py
>>> infile = open("test.dat","r")
>>> print (infile.readline())
line one
   
>>>
```

`readlines` kalan bütün satırları karakter dizisi listesi olarak döndürür:

```py
>>> print (infile.readlines())
['line two\012', 'line three\012']
```

Bu durumda, çıktı liste biçimindedir, yani dizeler tırnak işaretleri içinde görünür ve yeni satır karakteri kaçış olarak görünür `\\012`.

Dosyanın sonunda, "okuma satırı" boş dizeyi döndürür ve "readlines" boş listeyi döndürür:

```py
>>> print (infile.readline())
   
>>> print (infile.readlines())
[]
```

Aşağıdaki satır-işleme programı örneğidir. `filter` metotu `oldfile`'ın `#` ile başlayan satırları olmayacak şekilde yeni bir kopyasını yaratır:

```py
def filter(oldfile, newfile):
    infile = open(oldfile, 'r')
    outfile = open(newfile, 'w')
    while True:
        text = infile.readline()
        if text == "":
           break
        if text[0] == '#':
           continue
        outfile.write(text)
    infile.close()
    outfile.close()
    return

```

**continue cümlesi** döngünün o anki adımını bitirir ama döngüye devam eder. İşleme akışı döngünün başına gider, koşulu kontrol eder ve uygun şekilde süreç devam eder.

Böylece, eğer `text` boşsa döngüden çıkılır. Ama eğer `text`'in ilk karakteri diyez işareti ise, işlem akışı döngünün başına gider. Her iki koşul da geçersiz olursa `text`'i yeni dosyaya yazarız.

## 10.9 Dizinler

Kalıcı depo ortamındaki dosyalar **dosya sistemi** adı verilen kural kümeleriyle düzenlenmiştir. Dosya sistemleri dosyalardan ve **dizinlerden** oluşmaktadır, dizinler hem dosyalar hem de diğer dizinler için bir kap görevi görürler.

Bir dosyayı açıp ve yazarak yeni bir dosya yarattığınızda, yeni dosya o an ki dizinde (programı çalıştırdığınız dizin) yer alır. Benzer olarak bir dosyayı okumak için açtığınızda, Python o an ki dizinde dosyayı arar.

Eğer başka bir yerdeki bir dosyayı açmak istiyorsanız, o dosyanın **konumunu** (path), hangi dizinde bulunduğunu belirtmeniz gerekmektedir:

```py
>>> wordsfile = open('/usr/share/dict/words', 'r')
>>> wordlist = wordsfile.readlines()
>>> print (wordlist[:5])
['\n', 'A\n', "A's\n", 'AOL\n', "AOL's\n", 'Aachen\n']
```

Bu örnek, `/` adı verilen sistemin en üst dizini altındaki `usr` dizini altındaki `share` dizini altındaki `dict` dizini içerisindeki `words` isminde bir dosyayı açmaktadır. Daha sonra tüm satırları karakter dizisi listesine `readlines` ile okumakta ve listenin ilk 5 öğesini ekranda görüntülemektedir.

`/` karakterini dosya isminin bir parçası olarak kullanamazsınız; çünkü dizin ve dosya isimleri arasında **ayırıcı** (delimiter) karakter olarak rezerve edilmiştir.

`/usr/share/dict/words` dosyası Unix tabanlı sistemlerde var olmalıdır ve alfabetik sıralı kelime listesi içerir.

## 10.10 Counting Letters

`ord` fonksiyonu bir karakterin tamsayı temsilini döndürmektedir:

```py
>>> ord('a')
97
>>> ord('A')
65
>>>
```

Bu örnek neden `'Apple' < 'apple'` ifadesi `True` döndürür açıklamaktadır.

`chr` fonksiyonu `ord` fonksiyonunun tersidir. Bir tamsayı argüman alır ve bu argümanın karakter temsilini döndürür:

```py
>>> for i in range(65, 71):
...     print (chr(i))
...
A
B
C
D
E
F
>>>
```

Aşağıdaki `countletters.py` programı [Alice in Wonderland](https://sonsuzus.github.io/dosya/alice_in_wonderland.txt) kitabındaki her bir karakterin kaç kere geçtiğini sayar:

```py
#
# countletters.py
#

def display(i):
    if i == 10: return 'LF'
    if i == 13: return 'CR' 
    if i == 32: return 'SPACE' 
    return chr(i)

infile = open('alice_in_wonderland.txt', 'r')
text = infile.read()
infile.close()

counts = 128 * [0]

for letter in text:
    counts[ord(letter)] += 1

outfile = open('alice_counts.dat', 'w')
outfile.write("%-12s%s\n" % ("Character", "Count"))
outfile.write("=================\n")

for i in range(len(counts)):
    if counts[i]:
        outfile.write("%-12s%d\n" % (display(i), counts[i]))

outfile.close()

```

Bu programı çalıştırıp ürettiği çıktı dosyasını bir metin düzenleyici ile inceleyin. Sondaki alıştırmalarda bu programı çözümlemeniz istenecek.

## 10.11 `sys` modülü ve `argv`

`sys` modülü python yorumlayıcının çalıştığı *ortam*a erişmek için fonksiyonlar ve değişkenler içermektedir.

Aşağıda örnek bizim sistemdeki bazı değişkenlerin değerini görüntülemektedir:

```py
>>> import sys
>>> sys.platform
'win32'
>>> sys.path
['', 'C:\\Users\\sonsu\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\idlelib', 'C:\\Users\\sonsu\\AppData\\Local\\Programs\\Python\\Python39\\python39.zip', 'C:\\Users\\sonsu\\AppData\\Local\\Programs\\Python\\Python39\\DLLs', 'C:\\Users\\sonsu\\AppData\\Local\\Programs\\Python\\Python39\\lib', 'C:\\Users\\sonsu\\AppData\\Local\\Programs\\Python\\Python39', 'C:\\Users\\sonsu\\AppData\\Roaming\\Python\\Python39\\site-packages', 'C:\\Users\\sonsu\\AppData\\Local\\Programs\\Python\\Python39\\lib\\site-packages']
>>> sys.version
'3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)]'
>>> 
```

Aynı makinede **Jython** başlatmak aynı değişkenler için farklı değerleri üretir:

```py
>>> import sys
>>> sys.platform
'java1.6.0_03'
>>> sys.path
['', '/home/jelkner/.', '/usr/share/jython/Lib', '/usr/share/jython/Lib-cpython']
>>> sys.version
'2.1'
>>> 
```

Sizin makinenizdeki sonuçlar da farklı olacaktır elbette.

`argv` değişkeni Python betiği çalıştırıldığında **komut satırı**ndan okunan karakter dizilerinin listesini tutmaktadır. Bu **komut satırı argümanları** program başlarken programa bilgi geçirmeye yardımcı olur.

```py
#
# demo_argv.py
#
import sys

print (sys.argv)

```

Bu programı unix komut satırından çalıştırmanız `sys.argv`'nin nasıl çalıştığını gösterecektir:

```bash
$ python demo_argv.py this and that 1 2 3
['demo_argv.py', 'this', 'and', 'that', '1', '2', '3']
$ 
```

`argv` karakter dizisi listesidir. İlk öğenin programın ismi olduğuna dikkat edin. Argümanlar beyaz boşluklarla liste şeklinde ayrılmıştır, aynı `string.split` fonksiyonun işlemesi gibi. Eğer bir argümanın beyaz boşluk içermesini istiyorsanız, o argümanın etrafına tırnak işaretleri koyun:

```bash
$ python demo_argv.py "this and" that "1 2" 3
['demo_argv.py', 'this and', 'that', '1 2', '3']
$ 
```

`argv` ile girdilerini doğrudan komut satırından alan yararlı programlar yazabiliriz. Örneğin aşağıdaki bir sayı dizisinin toplamını alan bir programdır:

```py
#
# sum.py
#
from sys import argv

nums = argv[1:]

for index, value in enumerate(nums):
    nums[index] = float(value)

print (sum(nums))

```

Bu programda `from <module> import <attribute>` şeklinde içe aktarmayı kullanmaktayız, böylece `argv` modülün isim uzayına alınmış oluyor.

Şimdi programı komut satırından aşağıdaki şekilde çalıştırabiliriz:

```bash
$ python sum.py 3 4 5 11
23
$ python sum.py 3.5 5 11 100
119.5

```

Alıştırma olarak benzer programlar yazmanız istenmektedir.

## 10.12 Sözlük

modül
: Başka Python programlarında kullanılmak üzere Python tanımlama ve cümleleri içeren bir dosyadır. Modülün içerikleri başka programlarda kullanılmak üzere `import` cümlesiyle içe aktarılmaktadır.

standart kütüphane
: Kütüphane başka yazılımların geliştirilmesinde kullanılmak üzere araçlar içeren yazılım kolleksiyonudur. Bir programlama dilinin standart kütüphanesi bu tür araçların çekirdek programlama diliyle dağıtılanlarıdır. Python geniş bir standart kütüphaneyle birlikte gelir.

pydoc
: Python standart kütüphanesiyle birlikte gelen bir belge üreticidir.

komut istemi
: [Komut satırı arayüzü](http://en.wikipedia.org/wiki/Command_line) tarafından görüntülen bir karakter dizisidir, komutların girilebileceğini belirtir.

import cümlesi
: Bir modül içerisindeki nesnelerin kullanıma uygun hale gelmesini sağlayan cümledir. İki biçimi vardır. `mymod` modül ismi, içerdiği fonksiyonlar `f1` ve `f2`, içerdiği değişkenler `v1` ve `v2` olsun, iki biçimin örnekleri şunlardır:

```py
import mymod
```

İlk biçim

```py
from mymod import f1, f2, v1, v2
```

Tüm nesneleri içe aktar.

isim uzayı
: Aynı isimin farklı isim uzaylarında karışıklık olmadan yer almasına olanak sağlayan sözdizimsel kaptır. Python'da, modüller, sınıflar, fonksiyonlar, metotların hepsi bir isim uzayı oluşturur.

isim çakışması
: Bir isim uzayında iki veya daha fazla ismin karışması durumudur.

```py
from string import *
```

yerine 

```py
import string
```

kullanımı isim çakışmasını önleyecektir.

özellik
: Bir modül içerisinde tanımlanmış (veya sınıf veya örnek -- daha sonra göreceğimiz gibi) değişkendir. Modül özelliklerine **nokta işleci** kullanılarak erişilmektedir.(`.`).

nokta işleci
: Nokta işleci (`.`) bir modülün özellik ve fonksiyonlarına (veya sınıf - örneğin özellik ve metotlarına) erişmeyi sağlar.

metot
: Bir nesnenin fonksiyon benzeri özelliğidir. Metotlar nesne üzerinde nokta işleci kullanılarak *çağrılırlar (invoke)*.

Örneğin:

```py
>>> s = "this is a string."
>>> s.upper()
'THIS IS A STRING.'
>>>
```

Deriz ki, s karakter dizisinin `upper` metotu çağrıldı. `s` `upper` metotunun ilk argümanıdır.

geçici bellek
: Durumunu korumak için elektrik akımına ihtiyaç duyan bellektir. Bilgisayarın Ana bellek veya RAMi geçicidir. RAMde saklanan bilgi bilgisayar kapandığında kaybolur.

kalıcı bellek
: Güç olmadan da durumunu koruyan hafızadır. Sabit diskler, flash sürücüler, tekrar yazılabilir CDlerin her biri kalıcı belleğin örnekleridir.

dosya
: Genellikle sabit disk, floppy disk veya CD-ROM'da saklanan isimli varlıklardır, karakter dizileri, akımları içerir.

mod
: Bilgisayar programında ayrı işlem metotlarıdır. Python'da dosyalar üç modta açılabilirler: okuma ('r'), yazma ('w') ve ekleme ('a').

yol (konum) (path)
: Bir dosyanın gerçek konumunu belirten dizin isimleri serisidir.

metin dosyası
: Yazdırılabilir karakterler içeren ve yeni satır karakterleriyle ayrılmış satırlar içeren dosyadır.

continue cümlesi
: Döngünün adımını sonlandıran cümledir. Akış döngünün başına gider, koşulu değerlendirir, ve uygun şekilde döngüye devam eder.

dosya sistemi
: İçerdikleri veriyi ve dosyaları isimlendirmek, erişmek ve düzenlemek için bir yöntem.

dizin
: Dosyaların isimlendirilmiş kolleksiyonudur. Dizinler başka dizinleri - dizinin *alt dizinler*i adını alır - ve dosyaları barındırırlar.

yol (konum) (path)
: Bir dosya sisteminde bir dosyanın isim konumudur. Örneğin:

```bash
/usr/share/dict/words
```

`/` kök dizini altındaki `usr` altdizininin `share` altdizininin `dict` altdizini altındaki `words` dosyasını belirtmektedir.

ayırıcı
: Bir metinin farklı parçaları arasındaki sınırı belirleyen tek veya daha fazla karakter serisidir.

komut satırı
: *Komut satırı arayüzünde* *komut yorumlayıcı*ya yazılacak karakter serisidir (Ayrıntılı bilgi için [komut satırı](http://en.wikipedia.org/wiki/Command_line).

komut satırı argümanı
: Program başlatılırken programa komut satırı arayüzünün *komut istemi*nden geçirilen değerdir.

Jython
: Python programlama dilinin Java'da yazılmış bir gerçekleştirimidir.(Daha fazla bilgi için Jython ana sayfası [http://www.jython.org](http://www.jython.org/) adresini tıklayın)

`argv`
: `argv` *argüman vektörü*nün kısaltmasıdır ve `sys` modülü içerisinde komut satırı argümanlarının listesini tutan bir değişkendir.

## 10.13 Alıştırmalar

- Aşağıdakileri yapın:

	* pydoc sunucusunu komut satırında `pydoc -g` yazarak başlatın.

	* pydoc tk penceresinde open browser düğmesine tıklayın

	* `calendar` modülünü bulup tıklayın

	* *Functions* bölümüne bakarken, aşağıdakileri Python kabuğunda deneyin:
	 
	```py	
	  >>> import calendar
	  >>> year = calendar.calendar(2008)
	  >>> print (year)                      # Burada ne olur?	  
	```

	* `calendar.isleap` ile deneyler yapın. Argüman olarak ne almaktadır? Sonuç olarak ne döndürmektedir? Bu ne tür bir fonksiyondur?

Bu alıştırmadan öğrendiklerinize dair ayrıntılı notlar oluşturun.

- Eğer bilgisayarınızda `Tkinter` kurulu değilse, `pydoc -g` hata döndürecektir. Çünkü grafik penceresi `Tkinter`'e ihtiyaç duymaktadır. Bir alternatif çözüm web sunucusu ile başlatmaktır:

```bash
$ pydoc -p 7464
```

Bu pydoc web sunucusunu 7464 portunda başlatır. Ağ tarayıcınızda aşağıdaki adresi giriniz:

```
http://localhost:7464
```

bu adresle sisteminizde kurulu Python kütüphanelerini gezebilirsiniz.

Bu yaklaşımı kullanarak `pydoc`'u başlatın ve `math` modülünü gözden geçirin.

	1. `math` modülünde kaç fonksiyon vardır?

	
	2. `math.ceil` ne yapar? Peki `math.floor`?(*ipucu:* hem `floor` hem de `ceil` kayan noktalı argüman kabul etmektedir)
	
	3. `math` modülünü kullanmadan `math.sqrt` ile aynı değeri nasıl hesaplayabileceğimizi açıklayın?
	
	4. `math` modülündeki iki veri sabiti nedir?

Bu alıştırmadaki keşiflerinizin ayrıntılı notlarını tutun.

- `pydoc` ile `copy` mdülünü inceleyin. `deepcopy` ne işe yaramaktadır? Önceki bölümdeki hangi alıştırmada `deepcopy` işimize yarar?

- `mymodule1.py` isminde bir modül yaratın. Modüle şu anki yaşınızı tutan `myage` ve şu anki yılı tutan `year` özelliklerini ekleyin. `mymodule2` isminde başka bir modül yaratın, bu modüle de 0'a eşit `myage` ve doğduğunuz yıla eşit `year` özelliklerini ekleyin.
  
Şimdi `namespace_test.py` isminde bir dosya yaratın. İki modülü de içe aktarın ve aşağıdaki cümleleri yazın:

```py
print (mymodule2.myage - mymodule1.myage) == (mymodule2.year - mymodule1.year)

```

`namespace_test.py`'i çalıştırdığınızda, bu yıl doğum gününüzü kutlayıp kutlamadığınıza bağlı olarak `True` veya `False` değerlerinden birini göreceksiniz.

- Aşağıdaki cümleyi `mymodule1.py`, `mymodule2.py`, ve `namespace_test.py` dosyalarına ekleyin:

```py
print ("My name is %s" % __name__)
```

`namespace_test.py`'ı çalıştırın. Ne oldu? Neden? Şimdi aşağıdakini `mymodule1.py`'nin en altına ekleyin:

```py
if __name__ == '__main__':
    print ("This won't run if I'm imported.")

```

`mymodule1.py` ve `namespace_test.py`'i tekrar çalıştırın. Hangi durumda print cümlesinin yazdırdığını görüyoruz?

- Bir Python kabuğunda aşağıdakileri deneyin:

```py
>>> import this
```

İsim uzayları hakkında Tim Peter bize ne söylüyor?

- `pydoc`'u kullanarak `string` modülündeki diğer üç fonksiyonu bulup, sınayın. Bulgularınızı kaydedin.

- Önceki bölümdeki `matrix_mult` fonksiyonunu öğrendiğiniz liste metotlarıyla tekrar yazın.

- `dir` fonksiyonu, daha önce 7. bölümde görmüştük, argüman olarak aktarılan nesnenin *özellikler*inin listesini ekranda görüntülemektedir. Başka bir deyişle, `dir` argümanının *isim uzayının* içeriğini döndürmektedir.
  
`dir(str)` ve `dir(list)` komutlarını kullanarak bu bölümde anlatılmamış olan en az üç tane metot bulun. İki alt çizgi ile başlayan (__) herşeyi şimdilik görmezden gelin. Bulgularınızın isimleri ve kullanım örnekleriyle birlikte ayrıntılı notlarını oluşturmayı unutmayın.
  
(*ipucu:* incelemek istediğini fonksiyonunun docstring'ini yazdırın. Örneğin `str.join`'un nasıl çalıştığını görmek için `print str.join.__doc__` cümlesini kullanın.)

- Bir yorumlayıcı oturumunda aşağıdaki komutların ne çıktı vereceğini yazınız:

	1. ```py	
	  >>> s = "If we took the bones out, it wouldn't be crunchy, would it?"
	  >>> s.split()	  
	```
	
	2. ```py	
	  >>> type(s.split())	  
	```
	
	3. ```py	
	  >>> s.split('o')	  
	```
	
	4. ```py	
	  >>> s.split('i')	  
	```
	
	5. ```py	
	  >>> '0'.join(s.split('o'))	  
	```

Her sonucu neden aldığınızı mutlaka anlayın. Aşağıdaki fonksiyonun gövdesini doldurmak için `str` nesnelerinin `split` ve `join` metotlarını kullanarak öğrendiklerinizi uygulayın:

```py
def myreplace(old, new, s):
    """
 Replace all occurances of old with new in the string s.

 >>> myreplace(',', ';', 'this, that, and, some, other, thing')
 'this; that; and; some; other; thing'
 >>> myreplace(' ', '\*\*', 'Words will now be separated by stars.')
 'Words\*\*will\*\*now\*\*be\*\*separated\*\*by\*\*stars.'
 """

```

Çözümünüz tüm doctestleri geçmelidir.

- En altında aşağıdakileri içeren `wordtools.py` isminde bir modül yaratın:

```py
if __name__ == '__main__':
    import doctest
    doctest.testmod()
```

Bu cümlenin nasıl hem sınamak hem de kullanmak için kullanılabildiğini açıklayınız. Eğer `wordtools.py` başka bir modülde içe aktarılırsa `__name__`'in değeri ne olur? Ana program olarak çalışırsa ne olur? Hangi durumda doctestler çalışır?
  
Şimdi aşağıdaki fonksiyonları doctestlerin geçmesi için ekleyin ve içlerini doldurun:

```py
def cleanword(word):
    """
 >>> cleanword('what?')
 'what'
 >>> cleanword('"now!"')
 'now'
 >>> cleanword('?+="word!,@$()"')
 'word'
 """

def has_dashdash(s):
    """
 >>> has_dashdash('distance--but')
 True
 >>> has_dashdash('several')
 False
 >>> has_dashdash('critters')
 False
 >>> has_dashdash('spoke--fancy')
 True
 >>> has_dashdash('yo-yo')
 False
 """

def extract_words(s):
    """
 >>> extract_words('Now is the time! "Now", is the time? Yes, now.')
 ['now', 'is', 'the', 'time', 'now', 'is', 'the', 'time', 'yes', 'now']
 >>> extract_words('she tried to curtsey as she spoke--fancy')
 ['she', 'tried', 'to', 'curtsey', 'as', 'she', 'spoke', 'fancy']
 """

def wordcount(word, wordlist):
    """
 >>> wordcount('now', ['now', 'is', 'time', 'is', 'now', 'is', 'is'])
 ['now', 2]
 >>> wordcount('is', ['now', 'is', 'time', 'is', 'now', 'is', 'the', 'is'])
 ['is', 4]
 >>> wordcount('time', ['now', 'is', 'time', 'is', 'now', 'is', 'is'])
 ['time', 1]
 >>> wordcount('frog', ['now', 'is', 'time', 'is', 'now', 'is', 'is'])
 ['frog', 0]
 """

def wordset(wordlist):
    """
 >>> wordset(['now', 'is', 'time', 'is', 'now', 'is', 'is'])
 ['is', 'now', 'time']
 >>> wordset(['I', 'a', 'a', 'is', 'a', 'is', 'I', 'am'])
 ['I', 'a', 'am', 'is']
 >>> wordset(['or', 'a', 'am', 'is', 'are', 'be', 'but', 'am'])
 ['a', 'am', 'are', 'be', 'but', 'is', 'or']
 """

def longestword(wordset):
    """
 >>> longestword(['a', 'apple', 'pear', 'grape'])
 5
 >>> longestword(['a', 'am', 'I', 'be'])
 2
 >>> longestword(['this', 'that', 'supercalifragilisticexpialidocious'])
 34
 """

```

Bu modülü kaydedin, daha sonra programlarınızda bu araçları kullanabilirsiniz.

- [unsorted_fruits.txt](https://sonsuzus.github.io/dosya/unsorted_fruits.txt) dosyası her biri farklı bir karakterle başlayan 26 tane meyve içermektedir.
  
Bu dosyayı (`unsorted_fruits.txt`) okuyan ve içerisindeki meyveleri alfabetik olarak sıralı bir şekilde `sorted_fruits.txt` dosyasına yazan `sort_fruits.py` isminde bir program yazın.

- `countletters.py` hakkındaki aşağıdaki soruları yanıtlayın:

	1. Aşağıdaki üç satırın ne yaptığını ayrıntılı olarak açıklayın:
	 
	```py	
	infile = open('alice_in_wonderland.txt', 'r')
	text = infile.read()
	infile.close()	
	```
	
	Bu satırlar çalıştırıldıktan sonra `type(text)` ne döndürür?

	2. `128 * [0]` ifadesinin sonucu ne olur? [ASCII](http://en.wikipedia.org/wiki/ASCII) hakkında Wikipedia'dan bilgi alın ve neden `counts` değişkenine neden `128 * [0]` atanmıştır açıklayın.

	3. Aşağıdaki ifade
	 
	```py	
	for letter in text:
	    counts[ord(letter)] += 1	
	```
	
	`counts`'a ne yapar?

	4. `display` fonksiyonunun amacını açıklayın. Neden `10`, `13`, ve `32` değerlerini sınar? Bu değerler neden özeldir?
	
	5. Aşağıdaki satırların ne yaptığını ayrıntılı olarak anlatın
	 
	```py	
	outfile = open('alice_counts.dat', 'w')
	outfile.write("%-12s%s\n" % ("Character", "Count"))
	outfile.write("=================\n")	
	```
	
	Çalışma tamamlandığında `alice_counts.dat`'da ne olur?

	6. Son olarak, aşağıdakileri ayrıntılı olarak açıklayın
	 
	```py	
	for i in range(len(counts)):
	    if counts[i]:
	        outfile.write("%-12s%d\n" % (display(i), counts[i]))	
	```
	
	`if counts[i]`'in amacı nedir?

- Write a program named `mean.py` that takes a sequence of numbers on the command line and returns the mean of their values.

```bash
$ python mean.py 3 4
3.5
$ python mean.py 3 4 5
4.0
$ python mean.py 11 15 94.5 22
35.625
```

Programınızın aynı girdi üzerinde çalışan bir oturumu aynı çıktıyı üretmelidir. yukarıdaki örnekte çıktıları baz alınız.

- Komut satırından verilmiş olan sayıların medyan değerini bulan `median.py` isminde bir program yazınız.

```bash
$ python median.py 3 7 11
7
$ python median.py 19 85 121
85
$ python median.py 11 15 16 22
15.5
```

Programınızın bir oturumunda verilen aynı girdiler için aynı çıktılar üretilmelidir, yukarıdaki örnekte görüldüğü gibi çalışmalı.

- `countletters.py` programını dosyayı komut satırı argümanı olarak alacak şekilde değiştirin. Çıktı dosyasını isimlendirmeyi nasıl çözersiniz?
