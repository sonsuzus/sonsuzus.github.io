---
title: Python Programlama Ders 3. Fonksiyonlar
author: sonsuz
date: 2023-06-23 12:23:39 +0300
categories: [Program,Python]
tags: [python,fonksiyon,parametre,işlem,ders]
---



## 3.1 Tanımlar ve kullanım

Programlama bağlamın, bir **fonksiyon (işlev)** belli bir işlemi gerçekleştirmek üzere isimlendirilmiş cümle (komut) serisidir. Bu işlem **fonksiyon tanımında** belirlenmiştir. Python'da, fonksiyon tanımı için sözdizimi şu şekildedir:

```py

def ISIM( PARAMETRE LISTESI ):
    CUMLELER

```

Fonksiyonlar için dilediğiniz ismi kullanabilirsiniz, ancak değişkenlerde de olduğu gibi Python anahtar kelimelerini kullanamazsınız. Parametre listesi fonksiyon tarafından kullanılması gereken, varsa, bilgileri belirtmek için kullanılır.

Fonksiyon içerisinde herhangi sayıda cümle bulunabilir, ancak `def`'e göre daha içerden başlamaları gerekiyor. Bu kitaptaki örneklerde standart içeriden başlama (indentation - girinti) olan dört boşluk kullanılacaktır. Fonksiyon tanımlamaları **bileşik cümlelerin** ilk örneğidir, ileride de anlaşılacağı gibi hepsinin kalıbı aynıdır:

1. Bir **başlık**, bir anahtar kelime ile başlar ve iki nokta üst üste ile biter
2. Bir **gövde**, bir veya daha fazla Python cümlesi içerir ve herbiri başlığa göre eşit oranda içeriden - *Python standartı 4 boşluk karakteridir* - başlar.

Bir fonksiyon tanımlamasında, başlıktaki anahtar kelime `def`tir, bu ifade daha sonra fonksiyon ismi ve parantezlerle sınırlanmış parametrelerle izlenir. Tanımın sonunda iki nokta üst üste vardır. Parametre listesi boş olabilir veya herhangi bir sayıda parametre içerebilir. Her iki durumda da parantezler olmazsa olmazdır. 

Yazacağımız ilk fonksiyon örnekleri parametre içermeyecektir, bu yüzden sözdizimi şu şekildedir:

```py

def yeni_satir():
    print()          # herhangi bir arguman almayan print cumlesi yeni bir satir yazar

```

Bu fonksiyon `yeni_satir` ismindedir. Boş parantezler parametre almadığını gösterir. Gövdesinde sadece bir cümle vardır, bu cümle yeni satır karakterini ekranda göstermektedir (bunun anlamı bir boş satır bırakılmasıdır, boş bir print cümlesi kullanıldığında oluşan durumdur).

Yeni bir fonksiyon tanımlamak o fonksiyonun çalışmasını sağlamaz. Fonksiyonu çalıştırabilmemiz için bir **fonksiyon çağrısı** yapmamız gerekir. Fonksiyon çağrıları, çalıştırılacak fonksiyonun ismi ve onu takip eden parantez içerisindeki fonksiyona aktarılacak olan değer listesinden - bunlara *argüman* adı verilir - oluşur. Bu argümanlar fonksiyon tanımındaki parametrelere eşlenir. İlk örneklerimiz, boş parametre listesine sahip olduğu için, çağrılarımızda argüman göndermeyeceğiz. Ancak yine de parantezleri - içi boş olsa da - yazmaya devam edeceğiz:

```py

print("İlk satır.")
yeni_satir()
print("İkinci satır.")

```

Programın çıktısı:

```py

İlk satır.

İkinci satır.

```

İki satır arasındaki ek boşluk, `yeni_satir()` fonksiyon çağrısının bir sonucudur. Eğer satırlar arasında daha fazla boşluk isteseydik ne yapacaktık? Aynı fonksiyonu tekrar tekrar çağıracaktık:

```py

print("İlk satır.")
yeni_satir()
yeni_satir()
yeni_satir()
print("İkinci satır.")

```

Veya üç yeni satır yazan `uc_satir` isminde yeni bir fonksiyon yazabilirdik:

```py

def uc_satir():
    yeni_satir()
    yeni_satir()
    yeni_satir()

print("İlk satır.")
uc_satir()
print("İkinci satır.")

```

Bu fonksiyon üç cümle içermektedir, ve herbir cümle dört boşluk karakteri içeriden başlamaktadır. Sonraki satır içeriden başlamadığı için Python onun fonksiyonun bir parçası olmadığını anlayacaktır.

Bu program hakkında bir kaç şey dikkatinizi çekmiş olmalı:

* Aynı yordamı tekrar tekrar çağırabilirsiniz. Gerçekte, bu çok olağandır ve yapmanız yararlıdır.

* Bir fonksiyon çağrısının, bir başka fonksiyonu çağırmasını sağlayabilirsiniz; bu durumda `uc_satir` fonksiyonu `yeni_satir` fonksiyonunu çağırmıştır.

Şimdiye kadar bu yeni fonksiyonları yazmak için neden bu kadar zahmete katlandığımızı anlamamış olabilirsiniz. Aslında oldukça fazla neden vardır, aşağıdaki örnek iki nedeni gösterecektir:

1. Yeni bir fonksiyon yaratma, size cümle gruplarına bir isim verme şansı verir. Fonksiyonlar karmaşık hesaplamaları tek bir komutun arkasına saklayarak ve adı karışık komutlar yerine anlamlı isimlere (Türkçe, İngilizce) sahip komutlar kullanmanızı sağlayarak programı basitleştirirler.

2. Yeni fonksiyonlar yaratmak programınızı küçültebilir. Fonksiyonlar tekrar eden kodların elenmesini sağlar. Örneğin, dokuz kere ekrana boş satır yazacak komut yerine `uc_satir` fonksiyonunu üç kere çağırarak daha az kod yazmış olursunuz.

Önceki kod parçalarını biraraya getirip `tryme1.py` isimli bir betik içerisine yazdığımızda, tüm program aşağıdaki gibi gözükecektir:

```py

def yeni_satir():
    print()

def uc_satir():
    yeni_satir()
    yeni_satir()
    yeni_satir()

print("İlk satır.")
uc_satir()
print("İkinci satır.")

```

Bu program iki fonksiyon tanımlaması içermektedir:

`yeni_satir` ve `uc_satir`. Fonksiyon tanımlamaları diğer cümleler gibi çalıştırılırlar. Bu etkisi yeni bir fonksiyon yaratılması şeklindedir. Fonksiyon içerisindeki cümleler fonksiyon çağrımı yapmadan işletilmezler ve fonksiyon tanımlaması herhangi bir çıktı üretmez.

Tahmin edebileceğiniz gibi, bir fonksiyonu çalıştırmadan önce yaratmanız gerekir. Başka bir şekilde açıklayacak olursak, fonksiyon tanımlaması fonksiyonun ilk çağrısından önce çalışmalıdır.

## 3.2 Yürütme akışı

Fonksiyonun ilk kullanımından önce tanımlandığından emin olmak için, cümlelerin yürütülme sırasını bilmeniz gerekir, bu sıraya **yürütme akışı (flow of execution)** adı verilmektedir.

Yürütme her zaman programın ilk satırıyla başlar. Cümleler her seferinde biri olmak üzere yukarıdan aşağıya doğru sırayla çalıştırılır.

Fonksiyon tanımlamaları programın yürütme akışını değiştirmezler, ancak fonksiyon içerisindeki cümlelerin fonksiyon çağrılana kadar yürütülmediğini unutmayın. Her ne kadar sıklıkla kullanılan bir yöntem olmasa da, bir fonksiyon içerisinde başka bir fonksiyon tanımlayabilirsiniz. Bu durumda içerideki fonksiyon tanımı, içerisinde tanımlandığı fonksiyon çağrılana kadar yürütülmeyecektir.

Fonksiyon çağrımları yürütme akışındaki sapmalar gibidir. Sonraki cümleye gitmek yerine, akış çağrılan fonksiyon içerisindeki ilk cümleye atlar, fonksiyondaki tüm cümleleri çalıştırır daha sonra bıraktığı yere (fonksiyonun çağrıldığı satır) döner.

Bu her ne kadar kolaymış gibi görünse de, bir fonksiyonun başka bir fonksiyonu çağırabildiğini düşündüğünüzde bu sapmaların bir süre sonra takibi zorlaşabilir. Düşünün ki, bir fonksiyonun ortasındayken bir başka fonksiyon çağrılabilir. Ayrıca bu yeni çağrılan fonksiyon içerisinde de bir başka fonksiyon içerisindeki cümlelerin yürütülmesine ihtiyaç duyulabilir. Bu böyle gider!

Şansımız var ki, Python nerede kaldığını tutmada oldukça beceriklidir, böylece her fonksiyon yürütülmesi bittiğinde, program kaldığı yere geri döner. Programın sonuna geldiğinde programı sonlandırır.

Bu sefil hikayenin anafikri nedir? Bir programı okuduğunuzda, ne yukarıdan aşağıya doğru ne aşağıdan yukarıya doğru okumayın. Bunun yerine, yürütme akışını takip edin.

## 3.3 Parametreler, argümanlar, ve `import` cümlesi

Çoğu fonksiyon argümanlara gereksinimi duyar, bu değerler fonksiyonun görevini yaparken kullandığı ve bir bakıma bu görevi nasıl yapacağını belirlerler. Örneğin, bir sayının mutlak değerini bulmak istiyorsanız, hangi sayının mutlak değerini bulmak istediğinizi belirtmeniz gerekir. Python bu iş için içerisinde mutlak değer hesaplayan bir fonksiyon barındırır:

```py

>>> abs(5)
5
>>> abs(-5)
5

```

Bu örnekte, `abs` fonksiyonuna gönderdiğimiz argümanlar 5 ve -5'tir.

Bazı fonksiyonlar birden fazla argüman alabilir. Örneğin Python içerisinde tanımlı `pow` fonksiyonu iki argüman alır, taban ve üs. Fonksiyonun içerisinde bu değerler **parametre** adı verilen değişkenlere atanırlar.

```py

>>> pow(2, 3)
8
>>> pow(7, 4)
2401

```

Birden fazla argüman alan bir başka varolan fonksiyon `max`'tır.

```py

>>> max(7, 11)
11
>>> max(4, 1, 17, 2, 12)
17
>>> max(3*11, 5**3, 512-9, 1024**0)
503

```

`max` fonksiyonuna virgüllerle ayrılmış dilediğiniz sayıda argüman gönderebilirsiniz. Gönderilen argümanlar arasından en büyük sayıyı bulup geri döndürecektir. Argümanlar basit değerler olabildiği gibi deyim de olabilirler. Son örnekte 503 döndürüldü, çünkü 33, 125 ve 1'den daha büyüktür (deyimler değerlendirilerek sonuçlar fonksiyona geçiyor).

Kullanıcı tanımlı ve tek parametre içeren bir fonksiyon örneği:

```py

def iki_kere_yaz(bruce):
    print(bruce, bruce)

```

Bu fonksiyon tek bir **argüman** alır ve onu `bruce` isimli parametreye atar. Parametrenin değeri (bu noktada ne olduğuna dair bir fikrimiz yok) iki kere yazılır, sonrasında bir yeni satır ekranda gösterilir. `bruce` isminin seçilmesinin nedeni parametrelere dilediğiniz ismi verebileceğinizi göstermek içindir. Elbette `bruce` isminden daha yaratıcı ve anlamlı isimler seçmeniz kaynak kodun okunabilirliği açısından önemlidir.

Etkileşimli Python kabuğu bize fonksiyonlarımızı sınamak için elverişli bir yol sağlarlar. **import cümlesini** bir betik içerisinde tanımladığımız fonksiyonları yorumlayıcı oturumuna getirmek için kullanabiliriz. Bunun nasıl çalıştığını anlamak için, `iki_kere_yaz` fonksiyonunun `ders03.py` isimli bir betik içerisinde tanımlı olduğunu varsayalım. Etkileşimli olarak sınamak için betiği kendi Python kabuk oturumumuza *aktarırız*::

```py

>>> from ders03 import *
>>> iki_kere_yaz('Spam')
Spam Spam
>>> iki_kere_yaz(5)
5 5
>>> iki_kere_yaz(3.14159)
3.14159 3.14159

```

Bir fonksiyon çağrımında, argümanın değeri ilgili parametreye fonksiyon tanımlamasında atanmaktadır. Gerçekte `bruce = 'Spam'` ataması `iki_kere_yaz('Spam')` çağrımı yapılınca, `bruce = 5` `iki_kere_yaz(5)` ve `bruce = 3.14159` `iki_kere_yaz(3.14159)` çağrımı yapıldığında gerçekleşir.

Yazılabilir herhangi bir argüman `iki_kere_yaz` fonksiyonuna gönderilebilir. İlk fonksiyon çağrımında, argüman bir karakter dizisidir. İkinci çağrımda tamsayı, üçüncü çağrımda kayan `float` tipindedir.

İçsel (varolan) fonksiyonlar gibi `iki_kere_yaz` argümanı yerine deyim de kullanabiliriz:

```py

>>> iki_kere_yaz('Spam'*4)
SpamSpamSpamSpam SpamSpamSpamSpam

```

`'Spam'*4` deyimi ilk önce değerlendirilip `'SpamSpamSpamSpam'` şeklinde `iki_kere_yaz` fonksiyonuna argüman olarak geçirilmektedir.

## 3.4 Kompozisyon

Matematiksel fonksiyonlarda olduğu gibi, Python fonksiyonları da **dizilebilir**, bunun anlamı bir fonksiyonun sonucu bir başka fonksiyona girdi olarak verilebilir.

```py

>>> iki_kere_yaz(abs(-7))
7 7
>>> iki_kere_yaz(max(3, 1, abs(-11), 7))
11 11

```

İlk örnekte, `abs(-7)` deyimi 7 şeklinde değerlendirilir ve `iki_kere_yaz` fonksiyonuna argüman olarak verilir. İkinci örnekte iki seviyeli bir dizme sözkonusudur. İlk olarak `abs(-11)` ifadesi 11 sonucunu ürettiği için `max(3,1,11,7)` fonksiyonu 11 değerini üretir. Sonrasında bu 11 değeri `iki_kere_yaz(11)` fonksiyonuna argüman olarak geçirilir ve sonuç ekranda görüntülenir.

Ayrıca değişkenleri de argüman olarak kullanabiliriz:

```py

>>> michael = 'Erik, yarım arı.'
>>> iki_kere_yaz(michael)
Erik, yarım arı. Erik, yarım arı.

```

Burada dikkat etmeniz gereken önemli bir nokta var. Argüman olarak geçirdiğimiz değişkenin isminin (`michael`) parametre ismi (`bruce`) ile bir ilgisi yok. Çağrıldığı yerde o değişkenin isminin ne olduğunun bir önemi yok, fonksiyon içerisinde (`iki_kere_yaz`) parametre ismi (`bruce`) kullanılmaktadır, herkesi bu isim (`bruce`) ile sesleniriz.

## 3.5 Değişkenler ve parametreler yereldir

Bir fonksiyon içerisinde bir **yerel değişken** yarattığınızda, o değişken sadece o fonksiyon içerisinde varolur, fonksiyon dışında o değişkeni kullanamazsınız. Örneğin:

```py

def iki_kere_birlestir(part1, part2):
    cat = part1 + part2
    iki_kere_yaz(cat)

```

Bu fonksiyon iki argüman alır, bu argümanları birleştirir ve sonucu iki kere ekranda görüntüler. Bu fonksiyonu iki karakter dizisi ile çağırabiliriz:

```py

>>> chant1 = "Pie Jesu domine, "
>>> chant2 = "Dona eis requiem."
>>> iki_kere_birlestir(chant1, chant2)
Pie Jesu domine, Dona eis requiem. Pie Jesu domine, Dona eis requiem.

```

When `iki_kere_birlestir` bittiğinde, `cat` değişkeni yokedilir. Onu yazdırmaya kalkışırsak bir hata ile karşılaşırız:

```

>>> print cat
NameError: name 'cat' is not defined

```

Parametreler de yereldir. Örneğin, `iki_kere_yaz` fonksiyonu dışında `bruce` ismiyle tanımlı bir değişken yoktur. Kullanmaya kalkışırsanız, Python yine şikayet edecektir.

## 3.6 Yığıt diyagramları

Hangi değişkenlerin nerede kullanıldığını takip edebilmek için, **yığıt diyagramları** çizmek faydalı olabilir. Durum diyagramları gibi, yığıt diyagramları da her değişkenin değerini gösterir, ancak ayrıca her değişkenin ait olduğu fonksiyonu da gösterirler.

Her fonksiyon bir **çerçeve** ile temsil edilir. Bir çerçeve yan tarafında fonksiyonun ismi ve içerisinde parametre ve değişkenlerin bulunduğu bir kutudur. Önceki kod örneğinin yığıt diyagramı aşağıdaki gibidir:

![](illustrations/stack.png)

Yığıtın sırası yürütme akışını gösterir. `iki_kere_yaz` `iki_kere_birlestir` tarafından çağrılmıştır ve `iki_kere_birlestir` `__main__` (en üstteki fonksiyonun özel ismidir) tarafından çağrılmıştır. Herhangi bir fonksiyonun dışında tanımladığınız değişkenler `__main__`'e aittir.

Her parametre ilgili argümanıyla aynı değeri gösterir. Bu yüzden, `part1` `chant1` ile aynı değere, `part2` `chant2` ile aynı değere ve `bruce` `cat` ile aynı değere sahiptir.

Bir fonksiyon çağrımı esnasında bir hata oluşursa Python fonksiyon ismini ve o fonksiyonu çağıran fonksiyonun ismini yazar, o fonksiyonu da çağıran fonksiyon ismini, .... en üstteki fonksiyona ulaşana kadar tüm çağrım yapan fonksiyonları yazar.

Bunun nasıl çalıştığını görmek için `tryme2.py` isminde ve içeriği aşağıdaki gibi olan bir betik yaratalım:

```py

def iki_kere_yaz(bruce):
    print(bruce, bruce)
    print(cat)

def iki_kere_birlestir(part1, part2):
    cat = part1 + part2
    iki_kere_yaz(cat)

chant1 = "Pie Jesu domine, "
chant2 = "Dona eis requim."
iki_kere_birlestir(chant1, chant2)

```

`iki_kere_yaz` fonksiyonu içerisine `print cat` cümlesini ekledik, ancak `cat` değişkeni orada tanımlı olmadığı için bu betik hata üretecektir:

```py

Traceback (innermost last):
  File "tryme2.py", line 11, in <module>
    cat_twice(chant1, chant2)
  File "tryme2.py", line 7, in cat_twice
    print_twice(cat)
  File "tryme2.py", line 3, in print_twice
    print(cat)
NameError: global name 'cat' is not defined

```

Bu fonksiyon listesine **geri izleme (traceback)** adı verilmektedir. Hangi program dosyasında, hangi satırda ve hangi fonksiyonları işletirken hatanın oluştuğuna dair bilgi verir. Ayrıca hataya neden olan kod satırını da gösterir.

Geri izleme ile yığıt diyagramı arasındaki benzerliğe dikkat edin. Bu bir rastlantı değil. Gerçekte geri izlemenin bir başka ismi de *yığıt izleme*dir.

## 3.7 Sözlük

fonksiyon (işlev):
: Bazı faydalı işler başarabilen isimlendirilmiş cümle dizisidir. Fonksiyonlar parametre alabilir veya almayabilir, sonuç üretebilir veya üretmeyebilir.

fonksiyon tanımı:
: Yeni bir fonksiyon yaratan cümledir, fonksiyonun ismini, parametrelerini ve yürüteceği cümleleri belirtir.

bileşik cümle:
: İki parçadan oluşan cümledir:

1. başlık - cümlenin tipini belirleyen bir anahtar kelimeyle başlar ve iki nokta üstüste ile biter.

2. gövde - başlıktan eşit oranda içeride yazılmış olan bir veya daha fazla cümledir

Bileşik cümlenin sözdizimi aşağıdaki gibidir:

```py

anahtar_kelime deyim :
    cümle
    cümle ...

```

başlık:
: Bileşik cümlenin ilk kısmıdır. Bir anahtar kelime ile başlar ve iki nokta üst üste (:) ile biter.

gövde:
: Bileşik cümlenin ikinci kısmıdır. Gövde başlıktan eşit derecede içeride başlayan cümle dizilerinden oluşur. Python topluluğu tarafından kullanılan standart girinti 4 boşluktur.

fonksiyon çağrımı:
: Fonksiyonu yürütmeye başlatan cümledir. Fonksiyonun ismiyle başlar ve parantezler içerisindeki argümanlar (eğer varsa) ile devam eder.

yürütme akışı:
: Bir programın çalışması sırasında cümlelerin yürütülmesi sırasıdır.

parametre:
: Bir fonksiyon içerisinde kullanılan ve fonksiyona geçirilen argümanı referans eden isim.

içeri aktarma (import):
: Bir Python betiği içerisinde tanımlanmış fonksiyon ve değişkenlerin başka bir betik ortamına veya Python kabuğuna getirilmesi için kullanılan cümledir.

Örneğin, aşağıdaki kodun `tryme.py` isimli bir betik içerisinde bulunduğunu düşünelim:

```py

def print_thrice(thing):
    print(thing, thing, thing)

n = 42
s = "And now for something completely different..."

```

Şimdi `tryme.py` dosyasının bulunduğu dizin içerisinde bir Python kabuğu başlatalım:

```py

$ ls
tryme.py  <ve diğer şeyler...>
$ python
>>>

```

`tryme.py` içerisinde üç isim tanımlanmıştır:
`print_thrice`, `n`, and `s`.
Eğer içe aktarmadan (import) bu isimleri kullanmaya çalışırsak, bir hata oluşur:

```py

>>> n
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'n' is not defined
>>> print_thrice("ouch!")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'print_thrice' is not defined

```

`tryme.py` betiğinden herşeyi içe aktarırsak, içerisinde tanımlı herşeyi kullanabiliriz:

```py

>>> from tryme import *
>>> n
42
>>> s
'And now for something completely different...'
>>> print_thrice("Yipee!")
Yipee! Yipee! Yipee!
>>>

```

Dikkat etmeniz gereken nokta `import` cümlesinde `.py` uzantısını kullanmıyorsunuz.

argüman:
: Bir fonksiyon çağrıldığında, bu fonksiyona aktarılan değerdir. Bu değer fonksiyonda ilgili parametreye atanır.

fonksiyon dizilimi (kompozisyon):
: Bir fonksiyon çıktısını bir başka fonksiyona girdi olarak kullanmaktır.

yerel değişken:
: Bir fonksiyon içerisinde tanımlı değişkendir. Yerel değişken sadece kendi fonksiyonu içerisinde kullanılabilir.

yığıt diyagramı:
: Fonksiyonların, değişkenlerinin ve değişkenlerin gösterdiği değerlerin grafiksel gösterimidir.

çerçeve:
: Yığıt diyagramında bir fonksiyon çağrısını temsil eden çerçevedir. Fonksiyonun yerel değişkenleri ve parametrelerini içerir.

geri izleme:
: Bir çalışma zamanı hatası oluştuğunda çalışan fonksiyonların bir listesidir. Geri izleme ayrıca *yığıt izleme* olarak ta adlandırılır. Bu listede fonksiyonlar [çalışma zamanı yığıtı](https://en.wikipedia.org/wiki/Runtime_stack) içerisindeki sıraya göre bulunurlar.

## 3.8 Alıştırmalar

1. Bir metin düzenleyici veya python editörü kullanarak `tryme3.py` bir Python betiği yazın. Bu dosya içerisinde `three_lines` fonksiyonunu kullanarak dokuz boş satır üreten `nine_lines` isimli bir fonksiyon yazın. Daha sonra `clear_screen` isimli, ekrana 25 adet boş satır yazıp, ekranı temizleyen fonksiyonu yazın. Programınızın son satırında `clear_screen` fonksiyonuna bir çağrı yapmanız gerekiyor.

2. `tryme3.py` programının son satırını en üste taşıyın, `clear_screen` fonksiyonuna yapılan *fonksiyon çağrısı* böylece *fonksiyon tanımlamasından* önce yapılmış olacak. Programı çalıştırın ve ortaya çıkan hata mesajını kaydedin. *Fonksiyon tanımlamaları* ve *fonksiyon çağrıları* ile ilgili birbirlerine bağlı olarak kod içerisinde nerede bulunabileceklerine dair bir kural oluşturabilir misiniz?

3. Hatasız çalışan bir `tryme3.py` kullanarak, `new_line` fonksiyon tanımlamasını `three_lines` tanımlamasından sonraya taşıyın. Bu programı çalıştırdığınızda ne olduğunu gözlemleyin. Şimdi `new_line` tanımlamasını `three_lines()` çağrısının altına taşıyalım ve çalıştıralım. Ortaya çıkan sonucu bir önceki örnekte tanımladığınız kural açısından değerlendirin.

4. s karakter dizisini n kere yazacak şekilde `cat_n_times` *fonksiyon tanımlaması*nın *gövdesini* doldurun:

```py

def cat_n_times(s, n):
    <kodu buraya yazın>

```

Bu kodu `import_test.py` betiği içerisine kaydedin. Şimdi sistemde bu betik ile aynı dizinde olduğunuzdan emin olduktan sonra Bir Python kabuğu başlatın ve aşağıdakileri deneyin:

```py

>>> from import_test import *
>>> cat_n_times('Spam', 7)
SpamSpamSpamSpamSpamSpamSpam

```

Eğer herşey düzgünse sizin oturumunuz da yukarıdaki gibi çalışacaktır. `cat_n_times` fonksiyonuna farklı çağrıları deneyerek nasıl çalıştığını iyice anlamaya çalışın.

- Kullanıcıya çap sorulur ve dairenin çevresi ve alanı hesaplanır. (alan = pi r^2) (cevre = 2pi r) (r = R/2) Bunun için alan ve çevre isimli iki fonksiyon tanımlayıp içinde hesaplayın. Parametre olarak R (Çap) alsın.
