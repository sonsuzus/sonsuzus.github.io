---
title: Python yield kullanımı nasıldır? yield nerede kullanılır?
author: sonsuz
date: 2023-09-13 18:16:41 +0300
categories: [Program,Python]
tags: [python,programlama,iter,iterator,yield,generator]
---

## Python yield kullanımı

### Python iter deyimi

Python dilindeki yield deyimini anlamak için, generator'ları bilmek gerekiyor, generator'ları anlamak için de, iterator ve iterable kavramlarını anlamak gerekiyor. İngilizcede "iterate" kelimesi, tekrar tekrar uygulanmak veya işlenmek anlamına geliyor. Python'daki iterable ve iterator kavramları bu kelimeden türetilmiş. Python'da `iter()` yerleşik fonksiyona argüman olarak verebildiğimiz objelere iterable diyoruz. iter() fonksiyonu bize bir iterator döndürüyor. Iterator, objenin elemanları ne şekilde tanımlanırsa tanımlansın, bir koleksiyon içindeki tüm elemanlara sırasıyla erişebilmemiz için ortak bir arayüz oluşturan bir mekanizma. Kısacası, elemanları üzerinde sırasıyla gezinebildiğimiz, listeler ve demetler gibi objelere iterable diyoruz. Bu objeler, `iter()` fonksiyonu ile çağrıldığında, birer iterator döndürüyor, ve bu iterator'lar bir koleksiyondan sırasıyla eleman almak için kullanılıyor.

```py
a = [1,2,3,4,5]
for k in a:
    print(k)
```

Bu örnekte, sıradan bir liste ve for döngüsü görüyoruz. Buradaki liste, for döngüsünde kullandığımız herşey gibi, bir iterable. Python'da for döngüsü, önce iterable olarak verilen objeden, döngü sırasında kullanmak için bir iterator elde ediyor. Biz bu aşamayı görmüyoruz, bu aşama, Python'daki for döngülerinin çalışma yapısının bir parçası. Daha sonra, bu iterator elemanlar tükendi sinyali verene kadar, k değişkenini bir sonraki elemana atayıp, döngünün gövdesini çalıştırılıyor. Yani, yukarıdaki for döngüsü ile aşağıdaki kod parçacığı tamamen aynı çalışıyor.

```py
a = [1,2,3,4,5]
b = iter(a)
while True:
    try:
        k = next(b)
    except StopIteration:
       break
   print(k)
```

Yukarıdaki örnekte, ikinci satırda listenin elemanlarını sırasıyla elde etmek için bir iterator oluşturup, bunu b değişkenine atadık. Yukarıdaki for döngüsünde, bu işlem for döngüsü tarafından kendiğinden yapılıyordu. Daha sonra, 5. satırda, k'yı iterator'dan gelen bir sonraki elemana atadık. Eğer iterator yeni eleman veremiyorsa, StopIteration durumu oluşturuyor. Bu durumu catch ile yakalayıp, döngüden çıkıyoruz. Iterator'larla ilgili son bir şey;iteratorlar tek kullanımlıktır, bir kere tükendikten sonra, aynı  objenin elemanları içinde tekrar gezinmek için, yeni bir iterator'a ihtiyacımız var.

### Bir generator yaratma

Python’da en kolay şekilde bir generator oluşturma return yerine yield ifadesini kullanmaktır. Eğer bir fonksiyon yield ifadesi içeriyorsa bir generator fonksiyonu haline dönüşür. Aslında bir fonksiyonda yield ve return ifadesi aynı değeri döndürür. Ancak, return ifadesi bir fonksiyonu sonlandırırken, yield ifadesi değeri döndürür, saklar ve fonksiyonu çağırma devam eder.

Bir örnek yapmadan önce normal bir fonksiyona göre farklılıkları sıralayalım:

- Bir generator fonksiyonu bir veya birden fazla yield ifadesi içerebilir.
- Çağrıldığı zaman, bir iterator nesnesi döndürür, ama işlemi hemen çalıştırma başlamaz.
- __iter__() ve __next__() metotları otomatik olarak uygulanabilir.
- Yield işlemi çağrıldığında kontrol duraklar ve çağrıya aktarılır.
- Yerel değişkenler ve durumları ardışık çağrılarda unutulmaz.
- Fonksiyon bittiğinde, StopIteration durumu tetiklenir.

```py
# Basit bir generator
def my_gen():
    i = 1
    print('Birinci')
    yield i
 
    i += 1
    print('İkinci')
    yield i
 
    i += 1
    print('Üçüncü')
    yield i
 
a = my_gen()
print(next(a))
print(next(a))
print(next(a))
```

Python'daki generator'lar ise, farklı bir çeşit iterable'dır. Bunların diğer iterable'lardan farklarından biri, bunların tek kullanımlık olmasıdır. Örneğin, bir listeyi istediğiniz kadar for döngüsünde kullanabilirsiniz, ancak, bir generator'u yalnız bir kere for döngüsünde kullanabilirsiniz. Bunların bir diğer önemli farkı ise, tüm elemanların hafızada tutulmaması. Generatorlar, sırası gelen elemanı üretip döndürür, daha sonra da bu elemanı unuturlar. Örneğin;

```py
generator = (x*x*x for x in range(5))
for k in generator:
   print(k)
"""
Ekrana şunu basar:
0
1
8
27
64
"""
for k in generator:
   print(k)
"""
Ekrana hiçbir şey basılmaz, çünkü generator'u bir kere kullandık ve bitti.
"""
```

Yukarıdaki örnekte, ilk satırda bir generator oluşturup, bunu generator isimli bir değişkene atadık. Şimdi bunu, istediğimiz gibi for döngüsünde kullanabiliriz. Burada dikkat edilmesi gereken nokta, 0,1,8 gibi değerlerin, ilk satırda oluşturulmamış olması. Bu değerler, for döngüsünde sıraları geldiklerinde oluşup, işleri bittikten sonra hafızadan siliniyorlar.

```py
def nextSquare():
    i = 1
 
    # kare alan sonsuz döngü yaratıyoruz
    while True:
        yield i*i
        i += 1  # sonraki sayı için arttırıyor
        # yield ifadesinde duruyor
 
 
# test edelim
# fonksiyonu çağırarak
for num in nextSquare():
    if num > 100:
        break
    print(num)
```

Bir stringin tersini alan generator:

```py
def rev_str(my_str):
    'Döngülü yield'
    length = len(my_str)
    for i in range(length - 1,-1,-1):
        yield my_str[i] 
 
for char in rev_str("merhaba"):
     print(char)
```

### Generator ifadesi

Generator ifadesi kullanarak genaratorler oluşturulabilir. Lambda ile isimsiz fonksiyonlar oluşturabildiği gibi generator ifadesi ile anonim bir generator fonksiyonu oluşturur. Generator sözdizimi list ifadesinin sözdizimine çok benzer, ama köşeli parantez yerine normal parantezler kullanılır. Bir list ifadesi ile bir generator ifadesi arasındaki hem önemli fark bir list ifadesi tam bir liste oluştururken genarator ifadesi bir seferde bir öğe oluşturur.  Bir generator ifadesi sadece istenildiğinde öğeyi oluşturur. Bu sebepten dolayı bir generator ifadesinin list ifadesine göre belleği çok daha etkin kullandığı söylenebilir.

Artık yield deyimini anlamak için, yeterli altyapıya sahibiz. yield deyimi, return deyimi gibi fonksiyonlarda kullanılır, ancak, fonksiyon bir generator döndürür. Şu örneğe bakalım;

```py
def creategeneratorSquare(l):
    for x in l:
     yield x * x

generator = creategeneratorSquare([1,2,3,4,5])
for k in generator:
   print(k)
"""
Ekrana şunu basar:    
1
4
9
16
25
"""
```

Yukarıdaki kod parçacığında, creategeneratorSquare isimli bir fonksiyon oluşturduk. Bu fonksiyonun, normal fonksiyonlardan farkı, bir generator döndürmesi. Bu fonksiyonu çağrıdığımızda, normal fonksiyonlardan beklediğimiz gibi, fonksiyonun gövdesi çalışmıyor, bunun yerine fonksiyon bir generator döndürüyor. Bu generator for döngüsü içinde kullanıldığında, fonksiyon içinde yazdığımız kod, yield görene kadar çalışıyor. Burada, yield deyimi `x * x` döndürüyor ve beklemeye başlıyor. Daha sonra, 6. satırdaki döngü, bir sonraki elemanı istedikçe, beklemedeki kod bloğu tekrar yield görene kadar çalışıp, yield gördüğünde sıradaki elemanı döndürüyor. Böylece, bu kod bloğu tamamlanıncaya kadar, 6. satırdaki for döngüsü k'ya farklı değerler atayıp, bunları ekrana bastırıyor.

Bir örneğe daha bakalım;

```py
def fibogenerator():
  a,b = 1,1
   while True:
     yield b
     a,b = b, a + b

for k in fibogenerator():
   if k > 10000000:
     print(k)
     break
"""
Ekrana şunu basar:  
14930352
"""
```

Bu örnekte, biz istedikçe bir sonraki fibonacci sayısını veren bir generator kullanmak istedik. Bunun için, fibogenerator isimli bir fonksiyon yazdık. Bir önceki örnekten farklı olarak, bu sefer generator'u bir ara değişkende tutmaktansa, doğrudan for döngüsü içinde kullandık. Generator zaten tek kullanımlık olduğu için, bunları bir değişkene atamak çoğu zaman gereksiz. For döngüsünde ise, k 10 milyon'dan büyük olduğunda, k'yı ekrana bas ve döngüden çık dedik. Eğer döngüden çıkmak için herhangi birşey kullanmazsak, bu for döngüsü sonsuza kadar çalışırdı, çünkü, yazdığımız generator doğal yollardan sonlanmıyor.

> yield deyimi ilk görüldüğünde kafa karıştırıcı olabilir. Buna rağmen, yield deyimini anlamaya çalışmakta yarar var, çünkü yeri geldiğinde bunu bilmek, diğer yollardan çözemeyeceğiniz problemleri bir çırpıda çözmenize olanak sağlıyor.
{: .prompt-tip }

## yield nasıl çalışır.

Sade bir dille anlatmak gerekirse;

Bir dizi sayı üzerinde işlem yapmak istiyorum, ancak bu dizinin yaratılmasıyla uğraşmak istemiyorum. Sadece yapmak istediğim işleme odaklanmak istiyorum. Bu yüzden aşağıdakileri yapıyorum:

Sizi arayıp belirli bir şekilde üretilmiş bir dizi sayı istediğimi söylüyorum ve algoritmanın ne olduğunu da söylüyorum.
Bu adım, generator fonksiyonunun, yani yield içeren fonksiyonun tanımlanmasına karşılık geldi.

Bir süre sonra sana “Tamam, bana sayıların sırasını anlatmaya hazır ol” diyorum.

Bu adım, bir generator nesnesi döndüren generator fonksiyonu çağırmaya karşılık geldi. Henüz bana bir sayı söylemediniz; sadece kağıt ve kaleminizi aldınız.

Şimdi size, “bana bir sonraki numarayı söyleyin” diyorum ve siz bana ilk numarayı söylüyorsunuz. Ondan sonra, benden bir sonraki numarayı sormamı bekliyorsunuz. Nerede olduğunuzu, hangi sayıları söylediğinizi ve bir sonraki sayının ne olduğunu hatırlamak sizin işiniz. Detaylar benim için önemli değil.

Bu adım, generator nesnesinde .next()‘i çağırmaya karşılık geldi.
Buraya kadar önceki adımları tekrar ettik ve sona geldik. Burada artık bana “başka sayı yok!” diyorsunuz.

Bu adım, generator nesnenin işini bitirmesine ve bir StopIteration istisnasının fırlatılmasına karşılık geldi. Generator fonksiyonunun istisnayı oluşturması gerekmez. Fonksiyon sona erdiğinde veya bir dönüt verdiğinde otomatik olarak fırlatılır.

Dolayısıyla generatorun yaptığı şey şöyledir; yürütmeye başlar, bir ürün verdiğinde duraklar ve bir .next() değeri sorulduğunda son noktadan devam eder. Python’un yineleyici protokolü ile de tasarımı gereği mükemmel uyum sağlar.

## yield from deyimi kullanımı

Genellikle from sözcüğünü, bir kütüphaneyi import sözcüğü ile programa yüklerken kullanıyoruz. Ancak from sözcüğünün kullanıldığı başka bir yer daha var. Bu başlıkta bundan bahsetmek isterim.

Diyelim aşağıdaki gibi bir fonksiyonumuz var. Bu aşağıdaki fonksiyon ne yapıyor bilmeyenler için anlatayım, izninizle.

`def f(*args): pass`

`f(*args)` ifadesi, f fonksiyonunun -255’e kadar- bir sürü argüman alabileceğini gösteriyor. Ana konudan sapmadan, isterseniz, 255 tane argüman alabileceğini nasıl öğrenebiliriz bulmaya çalışalım.

Yukarıdaki fonksiyona 255 tane argüman vererek çağırmaya çalışalım.

`exec(f"f({', '.join(map(str, range(255)))})")`

Bir de 256 tane argüman vererek çağırmaya çalışalım.

`exec(f"f({', '.join(map(str, range(256)))})")`

Şöyle bir hata almış olmamız lazım.

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<string>", line 1
SyntaxError: more than 255 arguments
```

Gördüğünüz gibi bir fonksiyona en fazla 255 tane argüman verilebiliyor.

Şimdi izninizle from sözcüğünün farklı kullanımını sizlere anlatmaya çalışmak isterim.

Örneğin, aşağıdaki gibi bir fonksiyonumuz olsun.

```py
def f(*args):
    for i in args:
        yield i

```
Yukarıdaki fonksiyonun ne yaptığını henüz bilmeyen arkadaşlar için kısaca bir açıklamada bulunayım.

Öncelikle yield deyimi tıpkı return gibi bir fonksiyondan değer döndürmeye yarar ancak burada bir değerden çok bir çok değer içeren bir üreteç elde edersiniz. Yukarıdaki fonksiyonda yield yerine return kullanılmış olsaydı, ilk i değeri geri döndürülecekti, oysa yield sözcüğü burada bütün i'lere ulaşma imkanı tanıyor.

Şimdi basit bir tane dizi tanımlayalım.

`dizi = ["elma", "armut", "çilek", "karpuz"]`

dizi'yi `f(*args)` fonksiyonuna argüman olarak verelim. Ve aşağıdaki gibi ekrana yazdıralım.

`print(*f(dizi))`

Yukarıdaki print fonksiyonunun ekrana bastıracağı çıktı aşağıdaki gibi olacaktır.

`['elma', 'armut', 'çilek', 'karpuz']`

`f()` fonksiyonunun argümanı dizi değil de `*dizi` olsun bu sefer.

`print(*f(*dizi))`

Bu kez alacağımız çıktı aşağıdaki gibi olacaktır.

`elma, armut, çilek, karpuz`

Şimdi gelin yukarıdaki fonksiyonu biraz değiştirelim:

```py
def f(*args):
    yield from args    
    
print(*f(dizi))
```

f fonksiyonunun argümanına dizi'yi yazalım ve bakalım nasıl bir sonuç elde ediyoruz.

`['elma', 'armut', 'çilek', 'karpuz']`

Gördüğünüz gibi bu fonksiyon da ilk `f(dizi)` fonksiyonuna benzer bir çıktı verdi. f fonksiyonuna argüman olarak bir de `*dizi`'yi verelim.

`print(*f(*dizi))`

Şöyle bir çıktı almamız gerekir.

`elma, armut, çilek, karpuz`

Yine diğer fonksiyonun ürettiği sonuca benzer bir sonuç üretildi. Peki bu her zaman böyle mi olur? Gelin fonksiyonu biraz daha değiştirelim ve bu sorunun cevabını bulmaya çalışalım.

```py
def f(*args):
    for i in args:
        yield i.upper() if isinstance(i, str) else i
```

Şimdi `f(*args)` fonksiyonununa önce dizi sonra *dizi'yi argüman olarak verip, döndürdüğü değerleri ekrana yazdırmaya çalışalım…

`print(*f(dizi))`

Aşağıdaki gibi bir çıktı almamız gerekiyor:

`['elma', 'armut', 'çilek', 'karpuz']`

Argümanı \*dizi olduğunda nasıl bir çıktı veriyor ona bakalım.

```py
print(*f(*dizi))
ELMA ARMUT ÇILEK KARPUZ
```

Yazdığımız `i.upper() if isinstance(i, str) else i` deyimi sayesinde, tipi str olan argüman büyük harflerle ekrana yazdırıldı.
Bu son f fonksiyonumuzu from yield deyimiyle birlikte tekrar yazalım.

```py
def f(*args):
    yield from args.upper() if isinstance(args, str) else args
```

Fonksiyona önce dizi'yi argüman olarak verelim ve nasıl bir çıktı aldığımıza bakalım.

```py
print(*f(dizi))
['elma', 'armut', 'çilek', 'karpuz']
```

Gördüğünüz gibi diğer fonksiyon ile benzer bir sonuç aldık. Peki argümana \*dizi'yi yazsak, o da benzer bir sonuç üretiyor mu bakalım.

```py
print(*f(*dizi))
elma armut çilek karpuz
```

Bakın bu sefer farklı bir sonuç aldık. Yani ilk örnekte her iki argüman için de benzer sonuçlar almıştık ama bu örnekte son sonuç farklı çıktı. Acaba from yield kullandığımız fonksiyonda nasıl bir değişiklik yapılmalı ki `print(*f(*dizi))` fonksiyonu string değerlerini büyük harflerle ekrana bastırsın?

Şöyle yapabilirdik herhalde:

```py
def f(*args):
    yield from [i.upper() for i in args] \
        if isinstance(args, tuple) else args
    

print(*f(*dizi))
```


Yukarıdaki kodları çalıştırdığımızda alacağımız çıktı şöyle olacaktır.

`ELMA ARMUT ÇILEK KARPUZ`

Peki, aynı fonksiyon `print(*f(dizi))` şeklinde çağrılabilir miydi?

`print(*f(dizi))`

Bu kodları çalıştırdığımızda aşağıdaki gibi bir çıktı almamız gerekiyor:

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in f
  File "<stdin>", line 2, in <listcomp>
AttributeError: 'list' object has no attribute 'upper'
```

Peki, nasıl bir f fonksiyonu yazılmalı ki, fonksiyonu `print(*f(dizi))` şeklinde çağırdığımızda, bir önceki `print(*f(*dizi))` fonksiyonunun ürettiği çıktı olan ELMA ARMUT ÇILEK KARPUZ ile benzer olsun? Aşağıdakini bir deneyelim.

```py
def f(*args):
    yield from [i.upper() for i in args[0]] \
        if isinstance(args, tuple) else arg
        
print(*f(dizi))
```

Bu kodları çalıştırdığımızda alacağımız çıktı aşağıdaki gibi olacaktır.

`ELMA ARMUT ÇILEK KARPUZ`

Son f fonksiyonunun argümanı \*dizi şeklinde olursa alacağımız çıktı da şöyle olacaktır:

`E L M A`

Örneği bu kadar uzatmamın nedeni kafa karışıklığı yaratmak değildi, eğer bir kafa karışıklığına yol açtıysam şimdiden özür dilerim. Hatırlıyorsanız yukarıda şöyle bir şey yazmıştım:

Yine diğer fonksiyonun ürettiği sonuca benzer bir sonuç üretildi. Peki bu her zaman böyle mi olur? Gelin fonksiyonu biraz daha değiştirelim ve bu sorunun cevabını bulmaya çalışalım.

İşte bu soruya cevap aramaya çalıştım ve gördüğüm kadarıyla,

```py
def f(*args):
    yield from args

# ile

def f(*args):
    for i in args:
        yield args
```

ifadeleri benzer sonuçlar üretiyor üretmesine ancak yukarıdaki diğer fonksiyon örneklerini bu yapıya uydurarak çağırmaya çalıştığımızda farklı sonuçlar alabildiğimizi gördük ve benzer sonuçlar almak için fonksiyonları değiştirmek zorunda kaldık.

## yield ile büyük dosyaları okuma

Oluşturucuların (generator) yaygın bir kullanım durumu, veri akışlarıyla veya CSV dosyaları gibi büyük dosyalarla çalışmaktır. Bu metin dosyaları verileri virgül kullanarak sütunlara ayırır. Bu biçim, verileri paylaşmanın yaygın bir yoludur. Peki ya bir CSV dosyasındaki satır sayısını saymak isterseniz? Aşağıdaki kod bloğu bu satırları saymanın bir yolunu gösterir:

```py
csv_gen = csv_reader("some_csv.txt")
row_count = 0

for row in csv_gen:
    row_count += 1

print(f"Row count is {row_count}")
```

Bu örneğe baktığınızda csv_gen'in bir liste olmasını bekleyebilirsiniz. Bu listeyi doldurmak için `csv_reader()` bir dosya açar ve içeriğini csv_gen'e yükler. Daha sonra program liste üzerinde yinelenir ve her satır için satır_sayımı değerini artırır.

Bu makul bir açıklama, ancak dosya çok büyük olsa bile bu tasarım yine de çalışır mı? Dosya, mevcut bellekten daha büyükse ne olur? Bu soruyu cevaplamak için `csv_reader()` fonksiyonunun dosyayı açtığını ve onu bir diziye okuduğunu varsayalım:

```py
def csv_reader(file_name):
    file = open(file_name)
    result = file.read().split("\n")
    return result
```

Bu işlev belirli bir dosyayı açar ve her satırı bir listeye ayrı bir öğe olarak eklemek için `file.read()` işlevini `.split()` ile birlikte kullanır. Daha yukarıda gördüğünüz satır sayma kod bloğunda `csv_reader()` işlevinin bu sürümünü kullanırsanız aşağıdaki çıktıyı alırsınız:

```
Traceback (most recent call last):
  File "ex1_naive.py", line 22, in <module>
    main()
  File "ex1_naive.py", line 13, in main
    csv_gen = csv_reader("file.txt")
  File "ex1_naive.py", line 6, in csv_reader
    result = file.read().split("\n")
MemoryError
```

Bu durumda, `open()` tembel bir şekilde satır satır yineleyebileceğiniz bir oluşturucu nesnesi döndürür. Ancak `file.read().split()` her şeyi belleğe aynı anda yükleyerek `MemoryError` hatasına neden olur.

Bu gerçekleşmeden önce muhtemelen bilgisayarınızın taramanın yavaşladığını fark edeceksiniz. Programı `KeyboardInterrupt` ile durdurmanız bile gerekebilir. Peki bu devasa veri dosyalarını nasıl yönetebilirsiniz? `csv_reader()`'ın yeni haline bir göz atalım:

```py
def csv_reader(file_name):
    for row in open(file_name, "r"):
        yield row
```

Bu haliyle dosyayı açarsınız, yinelersiniz ve bir sonuç sayısı elde edersiniz. Bu kod, hiçbir bellek hatası olmadan aşağıdaki çıktıyı üretmelidir:

`Row count is 64186394`

Burada neler oldu? Aslında `csv_reader()` işlevini bir generatör işlevine dönüştürdünüz. Bu sürüm bir dosyayı açar, her satırda döngü yapar ve onu döndürmek yerine her satırı verir.

Ayrıca, liste kavramalarına çok benzer bir sözdizimine sahip olan bir oluşturucu ifadesi (oluşturucu kavrama olarak da adlandırılır) da tanımlayabilirsiniz. Bu şekilde generatörü bir işlevi çağırmadan kullanabilirsiniz:

```py
csv_gen = (row for row in open(file_name))
```

Bu, csv_gen demetini oluşturmanın daha kısa ve öz bir yoludur.

- yield kullanılması bir generatör nesnesi döndürür.
- yield yerine return kullanılması dosyanın yalnızca ilk satırını döndürür.