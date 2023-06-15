---
title:  Python Programlamaya Giriş 20 – Dosya Okuma ve Yazma
author: sonsuz
date: 2023-06-15 15:45:40 +0300
categories: [Program,Python]
tags: [python,dosya,okuma,yazma]
---






Yazı dizimizin bu bölümünde, dosya okuma ve yazma yöntemlerinden bahsedeceğiz. Önce herhangi bir özel şekilde yapılanmamış olan düz metin dosyalarını işlemeyi göreceğiz. Ardından *csv* modülüyle CSV biçiminde yapılanmış dosyaları okuyup yazmayı inceleyeceğiz. JSON, ZIP, PDF, Word, Excel, HTML dosyalarının işlenmesine kısaca değineceğiz. Son olarak, Python oturumunda yarattığımız nesneleri ikili (binary) formda dosyaya kaydetmemizi ve sonra dosyadan tekrar yüklememizi sağlayan *pickle* modülünün kullanımını özetleyeceğiz.

Dizinin bütün yazılarına erişmek için [*Python Programlamaya Giriş*](https://sonsuzus.github.io/categories/python) kategorimize bakabilirsiniz. 

## Genel dosya okuma/yazma

### Dosya okumak

Öncelikle, IPython sihirleriyle *deneme.txt* isimli bir dosya yaratalım (Jupyter kullanmıyorsanız aşağıdaki metni bir metin editörüne kopyalayıp *deneme.txt* ismiyle çalışma dizininize kaydedebilirsiniz).

In [1]:

```py
%%writefile deneme.txt

Ey Türk Gençliği!

Birinci vazifen, 

Türk istiklâlini, Türk Cumhuriyeti'ni, 

ilelebet muhafaza ve müdafaa etmektir.


```

```
Overwriting deneme.txt


```

Bir dosyayı açmak için `open()` fonksiyonunu kullanırız. En basit halinde `open()` mevcut bir metin dosyasını okumak için açar ve bir dosya nesnesi döndürür.

In [2]:

```py
f = open("deneme.txt")


```

Dosya nesnesinin `read()` metodu dosya içeriğini tek bir dize halinde döndürür.

In [3]:

```py
f.read()


```

Out[3]:

```
"Ey Türk Gençliği!\nBirinci vazifen, \nTürk istiklâlini, Türk Cumhuriyeti'ni, \nilelebet muhafaza ve müdafaa etmektir."
```

Açılmış dosyalarla işimiz bittiğinde kapatmamız gerekir, yoksa bellekte birikip yer işgal edebilirler.

In [4]:

```
f.close()


```

`readlines()` metodu, satırlardan oluşan bir liste döndürür:

In [5]:

```py
f = open("deneme.txt")

f.readlines()


```

Out[5]:

```py
['Ey Türk Gençliği!\n',

 'Birinci vazifen, \n',

 "Türk istiklâlini, Türk Cumhuriyeti'ni, \n",

 'ilelebet muhafaza ve müdafaa etmektir.']
```

In [6]:

```
f.close()


```

Bir dosya nesnesi bir *iteratördür*; bütün dosyayı bir kerede belleğe yüklemez, ama talep geldikçe satırları birer birer verir. `readline()` metodu dosyadaki mevcut satırı okumak için kullanılır. Her yeni `readline()` çağrısı bir sonraki satırı getirir.

In [7]:

```py
f = open("deneme.txt")

f.readline()


```

Out[7]:

```
'Ey Türk Gençliği!\n'
```

In [8]:

```
f.readline()


```

Out[8]:

```
'Birinci vazifen, \n'
```

Dosya nesnesi bir iteratör olduğu için `for` döngüsünde kullanılabilir. Bir dosyayı satır satır işlemek için şöyle bir döngü kurulur.

In [9]:

```py
for satır in f:

    print(satır.upper(),end="")

f.close()


```

```
TÜRK ISTIKLÂLINI, TÜRK CUMHURIYETI'NI, 

ILELEBET MUHAFAZA VE MÜDAFAA ETMEKTIR.
```

### with … as

Yukarıda, dosyayı `open()` ile açtıktan sonra `close()` metoduyla kapatmak gerektiğini söyledik. Bu basit bir kural olsa da, karmaşık programlar içinde gözden kaçabiliyor. Dosya açma/kapama işlemini daha düzenli hale getirmek için Python programcıları *context manager* denen bir yapı kullanırlar. Bir context manager oluşturmak için `with` komutu kullanılır.

In [10]:

```py
with open("deneme.txt") as f:

    print(f.read())


```

```
Ey Türk Gençliği!

Birinci vazifen, 

Türk istiklâlini, Türk Cumhuriyeti'ni, 

ilelebet muhafaza ve müdafaa etmektir.


```

Context manager ayrı ve geniş bir konudur, ayrıntısı için [Python belgelerine](https://docs.python.org/3/reference/compound_stmts.html#with) bakabilirsiniz. Bizim açımızdan önemli olan, burada `with` bloku bitince dosyanın otomatik olarak kapatılmasıdır. Dosyanın kapanmış olduğunu, dosya nesnesinin `closed` değişkeninin durumuyla kontrol edebiliriz.

In [11]:

```
f.closed


```

Out[11]:

```
True
```

### Dosyaya yazmak

Bir dosyaya yazmak için `open()` fonksiyonunda `"w"` (write) modunu kullanırız.

In [12]:

```py
f = open("deneme2.txt", "w")


```

Bu komutla, mevcut dizinde *deneme2.txt* dosyası yoksa yaratılır, varsa mevcut içeriği silinip üstüne yeni veri yazılır. Açılan dosyaya bir dize yazmak için `write()` metodu kullanılır.

In [13]:

```py
f.write("ABCDE\n")

f.write("123456\n")

f.write("wxyz\n")

f.close()


```

Dosyayı açarak, veya `%cat` sihirini kullanarak içeriğine bakabiliriz.

In [14]:

```py
%cat deneme2.txt


```

```
ABCDE

123456

wxyz


```

Aynısını bir context manager ile de yapabiliriz:

In [15]:

```py
with open("deneme2.txt", "w") as f:

    f.write("ABCDE\n")

    f.write("123456\n")

    f.write("wxyz\n")


```

Dosyada mevcut bulunan verileri silmeden, yeni verilerin dosyanın altına eklenmesini istersek dosyayı `"a"` (append) modunda açmalıyız.

In [16]:

```py
with open("deneme2.txt", "a") as f:

    f.write("Yeni satır 1\n")

    f.write("Yeni satır 2\n")


```

In [17]:

```
%cat deneme2.txt


```

```
ABCDE

123456

wxyz

Yeni satır 1

Yeni satır 2


```

## CSV dosya biçimi

Bir çok veri dosyasında veriler tablo halinde, her satırda bir *kayıt* ve her sütunda o kayda ait bir *alan* olacak şekilde düzenlenmişlerdir. Alanlar birbirlerinden boşlukla, virgülle, veya başka bir karakterle ayrılabilir. Bu tür bir dosya düzenine CSV (comma-separated values, virgülle ayrılmış değerler) adı verilir. CSV biçimindeki dosyaları okumak için yukarıda açıkladığımız genel yöntemleri kullanmak mümkünse de, Python’un `csv` modülü işleri basitleştirir. Sözgelişi MS Excel ve benzeri bir hesap tablosunu CSV biçiminde kaydedip, verileri Python ile okuyabilirsiniz; veya Python’la üretilen verileri CSV dosyası olarak kaydedip hesap tablosu uygulamasıyla açabilirsiniz.

### CSV okuma

Önce bir örnek veri dosyası hazırlayalım.

In [18]:

```py
%%writefile ornek.csv

"Potter, H",37,"Londra, İngiltere"

"Granger, H",36,"Sydney, Avustralya"

"Weasley, Bill",45,"Bükreş, Romanya"


```

```
Overwriting ornek.csv


```

Bu örnekte isim ve adres alanı değerlerinin tırnak içinde yazıldığına dikkat edin. Eğer tırnak kullanılmasaydı, alanları virgülle ayırma kuralı bize `"Potter"`, `"H"`, `37`, `"Londra"`, `"İngiltere"` gibi beş ayrı alan verirdi.

Bir CSV dosyasını açtıktan sonra, `csv` modülündeki `reader()` fonksiyonunu kullanarak onu satır satır okuyacak bir iteratör nesnesi yaratırız. Sonra bu iteratör nesnesi üzerinde bir döngüyle dosyayı tarayabiliriz.

In [19]:

```py
import csv

with open("ornek.csv") as f:

    okur = csv.reader(f)

    for satır in okur:

        print(satır)


```

```py
['Potter, H', '37', 'Londra, İngiltere']

['Granger, H', '36', 'Sydney, Avustralya']

['Weasley, Bill', '45', 'Bükreş, Romanya']


```

Veya dosyamızda alan ayırıcı olarak boşluk karakteri, alan gruplama için bölü işareti (`/`) kullanılmış olabilir. Bu durumda `reader()` fonksiyonundaki `delimiter` ve `quotechar` parametrelerini değiştirerek dosyayı doğru şekilde alabiliriz.

In [20]:

```py
%%writefile ornek2.csv

/Potter, H/ 37 /Londra, İngiltere/

/Granger, H/ 36 /Sydney, Avustralya/

/Weasley, Bill/ 45 /Bükreş, Romanya/


```

```
Overwriting ornek2.csv


```

In [21]:

```py
with open("ornek2.csv") as f:

    okur = csv.reader(f, delimiter=" ", quotechar="/")

    for satır in okur:

        print(satır)


```

```py
['Potter, H', '37', 'Londra, İngiltere']

['Granger, H', '36', 'Sydney, Avustralya']

['Weasley, Bill', '45', 'Bükreş, Romanya']


```

Görüldüğü gibi, bir CSV dosyasında alan ayırma, gruplama, satır sonu karakterleri için farklı tercihler olabilir. Her bir tercih kümesine bir *lehçe* (dialect) adı veriliyor. `csv.reader()` için varsayılan lehçe olan `"excel"`, MS Excel ile üretilen CSV dosyalarını okumaya ayarlıdır. Ancak yukarıda gördüğümüz gibi bu tercihler kolaylıkla değiştirilebilir.

Eğer özel bir CSV biçimini sık sık kullanıyorsanız, o lehçeye özel bir `Dialect` nesnesi oluşturup `reader()` ile birlikte kullanabilirsiniz. Bunun ayrıntılarını [Python belgelerinden](https://docs.python.org/3/library/csv.html) öğrenebilirsiniz.

### CSV yazma

Elimizdeki verileri bir CSV dosyasına yazmak için önce `csv` modülünün `writer()` fonksiyonuyla bir yazıcı nesnesi yaratırız. Yazıcı nesnesi verilen veriyi kullanılan “lehçe”ye uygun şekilde bir dizeye dönüştürür ve dosyaya yazar. Yazılacak dosyayı `open()` ile açarken `newline=""` parametresi vermemiz gerekir.

Yazıcı nesnesinin `writerow()` metodu yazılacak satırı bir liste olarak alır.

In [22]:

```py
with open("ornek3.csv", "w", newline="") as f:

    yazıcı = csv.writer(f)

    yazıcı.writerow(['Potter, H', '37', 'Londra, İngiltere'])

    yazıcı.writerow(['Granger, H', '36', 'Sydney, Avustralya'])


```

Dosyanın içeriğine bakarak doğru yazılıp yazılmadığını kontrol edelim:

In [23]:

```
%cat ornek3.csv


```

```
"Potter, H",37,"Londra, İngiltere"

"Granger, H",36,"Sydney, Avustralya"


```

### Pandas ile CSV okuma

CSV dosyalarını veri analizi paketi *pandas* ile de okumak ve yazmak mümkündür. Pandas ile CSV okumak hem daha basittir, hem de `csv` modülünde bulunmayan sözgelişi veri içindeki yorumları elemek, sadece istenen sütunları almak gibi ince ayarlara da imkan verir.

Pandas’ın `read_csv()` fonksiyonu dosyanın içeriğini bir veri çerçevesi olarak okur; ardından bu veri çerçevesinden çeşitli satırlar veya sütunlar alınabilir. Pandas kullanımı bu notların kapsamı dışında olduğu için ayrıntıya girmiyorum.

## Diğer dosya formatları

Birçok dosya biçimi için Python’da özelleşmiş kütüphaneler vardır. Bunların bazılarına değinelim.

### JSON

Birçok internet hizmeti API’si, sorgulama sonuçlarını JSON biçiminde bir dosya olarak verir. Python standart kütüphanesindeki `json` modülü, JSON biçimli bir dosyayı okuyup bir Python sözlük veya listesine dönüştüren, ve Python nesnelerinden JSON biçimli bir dosya oluşturan fonksiyonları içerir.

[Mockaroo](https://www.mockaroo.com/) sitesini kullanarak yalancı veri içeren küçük bir JSON dosyası üretelim.

In [24]:

```py
%%writefile yalanci_veri.json

[{

  "id": 1,

  "first_name": "Fredia",

  "last_name": "Waith",

  "email": "fwaith0@tamu.edu"

}, {

  "id": 2,

  "first_name": "Rafaello",

  "last_name": "Rowthorn",

  "email": "rrowthorn1@stanford.edu"

}, {

  "id": 3,

  "first_name": "Harriette",

  "last_name": "Patters",

  "email": "hpatters2@samsung.com"

}]


```

```
Overwriting yalanci_veri.json


```

Şimdi bu dosyayı açıp, içeriğini yorumlayalım ve bir Python nesnesine aktaralım.

In [25]:

```py
import json

with open("yalanci_veri.json") as f:

    yalanciveriler = json.load(f)


```

Bu işlem sonucunda bir sözlükler listesi elde etmiş oluruz. Bilindik indeksleme işlemleriyle tek tek elemanlara ulaşabiliriz.

In [26]:

```py
yalanciveriler[1]["first_name"], yalanciveriler[1]["email"]


```

Out[26]:

```py
('Rafaello', 'rrowthorn1@stanford.edu')
```

Şimdi JSON dosyası yazmayı görelim. Elimizdeki veriye bir satır daha ekleyelim ve nesnenin yeni halini `json.dump()` ile dosyaya yazalım.

In [27]:

```py
yalanciveriler.append(

{

  "id": 4,

  "first_name": "Giffer",

  "last_name": "Dur",

  "email": "gdur2@cnbc.com"

})



with open("yalanci_veri.json", "w") as f:

    json.dump(yalanciveriler,f)


```

Dosyanın içeriğine bakarak beklediğimiz şekilde yazıldığını görebiliyoruz.

In [28]:

```
%cat yalanci_veri.json


```

```py
[{"id": 1, "first_name": "Fredia", "last_name": "Waith", "email": "fwaith0@tamu.edu"}, {"id": 2, "first_name": "Rafaello", "last_name": "Rowthorn", "email": "rrowthorn1@stanford.edu"}, {"id": 3, "first_name": "Harriette", "last_name": "Patters", "email": "hpatters2@samsung.com"}, {"id": 4, "first_name": "Giffer", "last_name": "Dur", "email": "gdur2@cnbc.com"}]
```

### HTML

HTML dosyaları zaten düz metinden oluştuğu için onları okumakta teknik bir zorluk yok. HTML işlemede asıl istenen şey *parsing*, yani çeşitli HTML elemanlarına erişebilmektir. Söz gelişi, bir HTML’deki bağlantıları almak, tablo veriyi okumak gibi işlemler yapmamız gerekebilir. Bu tür işlemler bu yazı dizisinin kapsamını aşıyor. İlgilenenler, en çok kullanılan araçlardan biri olan [*Beautiful Soup* modülüyle](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) denemeler yapabilirler.

### Excel

MS Excel dosyalarını CSV olarak kaydederseniz *CSV okuma/yazma* kısmındaki yöntemleri kullanabilirsiniz. Bunu istemiyorsanız, veya tablodaki verileriniz bu işleme uygun değilse, veya birden fazla yapraktan oluşuyorsa, Excel dosyasını doğrudan açmak için [*xlrd* modülünü](http://xlrd.readthedocs.io/en/latest/) kullanabilirsiniz.

Daha geniş özelliklere sahip bir paket olan [*pyexcel*](http://pyexcel.readthedocs.io/en/latest/) ile hem okuma hem de yazmayı daha kolay işlemlerle yapabilirsiniz.

*Pandas* paketinin `read_excel()` fonksiyonu ile bir Excel dosyasını doğrudan okuyarak bir veri çerçevesi haline getirebilirsiniz. 

### Word

MS Word belgelerinin içinden metin almak, belge yaratmak ve varolan belgeye içerik eklemek için [*python-docx*](https://python-docx.readthedocs.io/en/latest/index.html) modülü kullanılabilir. Örnekler için Al Sweigart’ın *Automate The Boring Stuff with Python* [kitabına](https://automatetheboringstuff.com/chapter13/) bakabilirsiniz.

### PDF

PDF dosyalarından bilgi almak, PDF dosyası yaratmak, mevcut dosyada değişiklik yapmak gibi işler için [*pyPDF2*](https://pythonhosted.org/PyPDF2/) modülünü kullanabilirsiniz. Sweigart’ın *Automate The Boring Stuff with Python* [kitabında](https://automatetheboringstuff.com/chapter13/) bu modülün kullanımına dair açıklayıcı örnekler bulabilirsiniz.

### ZIP

Python standart kütüphanesindeki [*zipfile* modülü](https://docs.python.org/3/library/zipfile.html), ZIP formatında sıkıştırma ve açma fonksiyonları sağlar.  

Basit bir örnek olarak, yukarıda kullandığımız *deneme.txt* ve *yalanci_veri.json* dosyalarını sıkıştırarak bir arşiv dosyası oluşturalım.

In [29]:

```py
import zipfile

with zipfile.ZipFile("arsiv.zip","w") as z:

    z.write("deneme.txt")

    z.write("yalanci_veri.json")


```

Mevcut bir arşive bir dosya eklemek istiyorsak, `ZipFile()` fonksiyonunun açılma modunu `"w"` yerine `"a"` yaparız.

`ZipFile()` fonksiyonu, yukarıda gördüğümüz `open()` gibi çalışır. Arşivi açmak için `ZipFile()` fonksiyonunu okuma modunda kullanırız, ve arşiv dosyası nesnesine ait `open()` metoduyla dosyayı açarız. Açılan dosyanın içeriği `read()`, `readline()` veya `readlines()` metodlarıyla okunabilir. Bu metodlar kodlanmış dizeler döndürdüğü için `decode()` dize metoduyla Unicode’a çevrilmelidir.

In [30]:

```py
with zipfile.ZipFile('arsiv.zip') as z:

    with z.open('deneme.txt') as f:

        print(f.read().decode("utf-8"))


```

```py
Ey Türk Gençliği!

Birinci vazifen, 

Türk istiklâlini, Türk Cumhuriyeti'ni, 

ilelebet muhafaza ve müdafaa etmektir.


```

Bir ZIP arşivindeki bir dosyayı açarak diske kaydetmek için `extract()`, arşivdeki bütün dosyaları açmak için `extractall()` fonksiyonları kullanabiliriz.

## Değişkenlerimizi kaydetmek: pickle

Bir oturumda hazırladığınız değişkenleri, oturumu kapattığınızda kaybetmemek isterseniz bunları ikili (binary) bir veri yapısı haline getirip diske kaydetmeniz gerekir. Bu işi standart kütüphanedeki [*pickle* modülü](https://docs.python.org/3/library/pickle.html) ile yapabilirsiniz. Neredeyse bütün Python nesnelerini (kendi tanımladığımız nesne sınıfları dahil) dosyaya kaydetmeniz ve sonra tekrar okumanız mümkündür. Bu işleme *serialization* adı verilir.

Birkaç değişken tanımlayalım.

In [34]:

```py
x = 3.14159

L = [1,3,2,5,4]

D = {"abc": 123, "def": 456}

def fon(x):

    return x*x


```

Verileri kaydetmek istediğimiz dosyayı ikili yazma modunda açalım ve *pickle* modülündeki `dump()` fonksiyonuyla değişkenleri dosyaya ekleyelim.

In [35]:

```py
import pickle

with open("data.p", "wb") as f:

    pickle.dump(x,f)

    pickle.dump(L,f)

    pickle.dump(D,f)

    pickle.dump(fon,f)


```

Değişkenleri dosyadan okumak için `load()` fonksiyonunu kullanırız. Nesneler dosyaya kondukları sırayla geri alınırlar. Değişkenlerin orijinal adını kullanmamız gerekmez.

In [36]:

```py
with open("data.p", "rb") as f:

    y = pickle.load(f)

    print(y)

    J = pickle.load(f)

    print(J)

    F = pickle.load(f)

    print(F)

    G = pickle.load(f)

    print(G(y))


```

```py
3.14159

[1, 3, 2, 5, 4]

{'abc': 123, 'def': 456}

9.869587728099999


```

Bazı nesneler *pickle* ile kaydedilemezler; ağ bağlantıları, veri tabanı bağlantıları, açık dosya nesneleri gibi.

Dikkat: *pickle* işlemleri herhangi bir emniyet tedbiri içermez. Pickle dosyasının içindeki nesne `load()` ile doğrudan doğruya çalıştırılır. Bu nesnenin içinde kötü amaçlı bir kod parçası varsa sisteminize zarar gelebilir. Bu yüzden bilmediğiniz bir yerden gelen pickle dosyalarını açmayın.
