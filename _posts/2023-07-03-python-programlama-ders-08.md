---
title: Python Programlama Ders 8. Karakter dizileri Metodları, Formatları
author: sonsuz
date: 2023-07-03 16:03:18 +0300
categories: [Program,Python]
tags: [python,ders,programlama,karakter,dizi,dize,string,veri,döngü,len,for,format,metod]
---



## 8.1 Karakter Dizilerinin Metotları

Geçen bölümde karakter dizilerinin genel özelliklerinden söz ettik. Bu bölümde ise karakter dizilerini biraz daha ayrıntılı bir şekilde incelemeye ve karakter dizilerinin yepyeni özelliklerini görmeye başlayacağız.

**Metotlar** Python’da nesnelerin niteliklerini değiştirmemizi, sorgulamamızı veya bu nesnelere yeni özellikler katmamızı sağlayan araçlardır. Metotlar sayesinde karakter dizilerini istediğimiz gibi eğip bükebileceğiz.

### replace()

Karakter dizisi metotları arasında inceleyeceğimiz ilk metot `replace()` metodu olacak. replace kelimesi Türkçede *‘değiştirmek, yerine koymak’* gibi anlamlar taşır. İşte bu metodun yerine getirdiği görev de tam olarak budur. Yani bu metodu kullanarak bir karakter dizisi içindeki karakterleri başka karakterlerle değiştirebileceğiz.

Peki bu metodu nasıl kullanacağız? Hemen bir örnek verelim:

`kardiz = "elma"`

Burada “elma” değerini taşıyan kardiz adlı bir karakter dizisi tanımladık. Şimdi bu karakter dizisinin içinde geçen “e” harfini “E” ile değiştirelim. Dikkatlice bakın:

```py
kardiz.replace("e", "E")
'Elma'
```

Gördüğünüz gibi, `replace()` son derece yararlı ve kullanımı oldukça kolay bir metot. Bu arada bu ilk metodumuz sayesinde Python’daki metotların nasıl kullanılacağı konusunda da bilgi edinmiş olduk. Yukarıdaki örneklerin bize gösterdiği gibi şöyle bir formülle karşı karşıyayız:

`karakter_dizisi.metot(parametre)`

Metotlar karakter dizilerinden nokta ile ayrılır. Python’da bu yönteme *‘noktalı gösterim’ (dot notation)* adı verilir.

Bu arada metotların görünüş ve kullanım olarak fonksiyonlara ne kadar benzediğine dikkat edin. Tıpkı fonksiyonlarda olduğu gibi, metotlar da birtakım parametreler alabiliyor.

Yukarıdaki örnekte, `replace()` metodunun iki farklı parametre aldığını görüyoruz. Bu metoda verdiğimiz ilk parametre değiştirmek istediğimiz karakter dizisini gösteriyor. İkinci parametre ise birinci parametrede belirlediğimiz karakter dizisinin yerine ne koyacağımızı belirtiyor. Yani replace() metodu şöyle bir formüle sahiptir:

`karakter_dizisi.replace(eski_karakter_dizisi, yeni_karakter_dizisi)`

Gelin isterseniz elimizin alışması için replace() metoduyla birkaç örnek daha verelim:

```py
kardiz = "memleket"
kardiz.replace("ket", "KET")

'memleKET'
```

Burada gördüğünüz gibi, replace() metodu aynı anda birden fazla karakteri değiştirme yeteneğine de sahip.

> replace() metodunun iki parametreden oluştuğunu, ilk parametrenin değiştirilecek karakter dizisini, ikinci parametrenin ise ilk karakter dizisinin yerine geçecek yeni karakter dizisini gösterdiğini söylemiştik. Aslında replace() metodu üçüncü bir parametre daha alır. Bu parametre ise bir karakter dizisi içindeki karakterlerin kaç tanesinin değiştirileceğini gösterir. Eğer bu parametreyi belirtmezsek replace() metodu ilgili karakterlerin tamamını değiştirir. Yani:
{: .prompt-info }

```py
kardiz = "memleket"

kardiz.replace("e", "")

'mmlkt'
```

Gördüğünüz gibi, replace() metodunu iki parametre ile kullanıp üçüncü parametreyi belirtmediğimizde, *“memleket”* kelimesi içindeki bütün “e” harfleri boş karakter dizisi ile **değiştiriliyor** (yani bir anlamda siliniyor).

Şimdi şu örneğe bakalım:

```py
kardiz.replace("e", "", 1)

'mmleket'
```

Burada replace() metodunu üçüncü bir parametre ile birlikte kullandık. Üçüncü parametre olarak 1 sayısını verdiğimiz için replace() metodu sadece tek bir “e” harfini sildi.

Bu üçüncü parametreyi, silmek istediğiniz harf sayısı kadar artırabilirsiniz. Mesela:

```py
kardiz.replace("e", "", 2)

'mmlket'

kardiz.replace("e", "", 3)

'mmlkt'
```

Burada ilk örnekte üçüncü parametre olarak 2 sayısını kullandığımız için, ‘replace’ işleminden karakter dizisi içindeki 2 adet “e” harfi etkilendi. Üçüncü örnekte ise “memleket” adlı karakter dizisi içinde geçen üç adet “e” harfi değişiklikten etkilendi.

Karakter dizileri konusunun ilk bölümünde ‘değiştirilebilirlik’ (mutability) üzerine söylediğimiz şeylerin burada da geçerli olduğunu unutmayın. Orada da söylediğimiz gibi, karakter dizileri değiştirilemeyen veri tipleridir. Dolayısıyla eğer bir karakter dizisi üzerinde değişiklik yapmak istiyorsanız, o karakter dizisini baştan tanımlamalısınız. Örneğin:

```py
meyve = "elma"
meyve = meyve.replace("e", "E")
meyve

'Elma'
```

Böylece `replace()` metodunu incelemiş olduk. Sırada üç önemli metot var.

### split(), rsplit(), splitlines()

Şimdi size şöyle bir soru sorduğumu düşünün: Acaba aşağıdaki karakter dizisinde yer alan bütün kelimelerin **ilk harfini** nasıl alırız?

`kardiz = "İstanbul Büyükşehir Belediyesi"`

Yani diyorum ki burada “İBB” gibi bir çıktıyı nasıl elde ederiz?

Sadece bu karakter dizisi söz konusu ise, elbette karakter dizilerinin dilimlenme özelliğinden yararlanarak, kardiz değişkeni içindeki “İ”, “B”, ve “B” harflerini tek tek alabiliriz:

```py
print(kardiz[0], kardiz[9], kardiz[20], sep="")

İBB
```

Ancak bu yöntemin ne kadar kullanışsız olduğu ortada. Çünkü bu metot yalnızca “İstanbul Büyükşehir Belediyesi” adlı karakter dizisi için geçerlidir. Eğer karakter dizisi değişirse bu yöntem de çöpe gider. Bu soruna genel bir çözüm üretebilsek ne güzel olurdu, değil mi?

İşte Python’da bu sorunu çözmemizi sağlayacak çok güzel bir metot bulunur. Bu metodun adı `split()`.

Bu metodun görevi karakter dizilerini belli noktalardan bölmektir. Zaten split kelimesi Türkçede *‘bölmek, ayırmak’* gibi anlamlara gelir. İşte bu metot, üzerine uygulandığı karakter dizilerini parçalarına ayırır. Örneğin:

```py
kardiz = "İstanbul Büyükşehir Belediyesi"
kardiz.split()

['İstanbul', 'Büyükşehir', 'Belediyesi']
```

Gördüğünüz gibi bu metot sayesinde “İstanbul Büyükşehir Belediyesi” adlı karakter dizisini kelimelere bölmeyi başardık. Eğer bu çıktı üzerine bir for döngüsü uygularsak şöyle bir sonuç elde ederiz:

```py
for i in kardiz.split():
    print(i)

İstanbul
Büyükşehir
Belediyesi
```

Artık bu bilgiyi kullanarak şöyle bir program yazabiliriz:

```py
kardiz = input("Kısaltmasını öğrenmek istediğiniz kurum adını girin: ")

for i in kardiz.split():
    print(i[0], end="")
```

Burada kullanıcı hangi kurum adını girerse girsin, bu kurum adının her kelimesinin ilk harfi ekrana dökülecektir. Örneğin kullanıcı burada “Türkiye Büyük Millet Meclisi” ifadesini girmişse split() metodu öncelikle bu ifadeyi alıp şu şekle dönüştürür:

`['Türkiye', 'Büyük', 'Millet', 'Meclisi']`

Daha sonra biz bu çıktı üzerinde bir for döngüsü kurarsak bu kelime grubunun her bir öğesine tek tek müdahale etme imkanına erişiriz. Örneğin yukarıdaki programda bu kelime grubunun her bir öğesinin ilk harfini tek tek ekrana döktük ve “TBMM” çıktısını elde ettik.

Yukarıdaki örneklerde `split()` metodunu herhangi bir parametre içermeyecek şekilde kullandık. Yani metodun parantezleri içine herhangi bir şey eklemedik. `split()` metodunu bu şekilde parametresiz olarak kullandığımızda bu metot karakter dizilerini bölerken boşluk karakterini ölçüt alacaktır. Yani karakter dizisi içinde karşılaştığı her boşluk karakterinde bir bölme işlemi uygulayacaktır. Ama bazen istediğimiz şey, bir karakter dizisini boşluklardan bölmek değildir. Mesela şu örneğe bakalım:

`kardiz = "Bolvadin, Kilis, Siverek, İskenderun, İstanbul"`

Eğer bu karakter dizisi üzerine `split()` metodunu parametresiz olarak uygularsak şöyle bir çıktı elde ederiz:

`['Bolvadin,', 'Kilis,', 'Siverek,', 'İskenderun,', 'İstanbul']`

split() metoduna herhangi bir parametre vermediğimiz için bu metot karakter dizisi içindeki kelimeleri boşluklardan böldü. Bu yüzden karakter dizisi içindeki virgül işaretleri de bölünen kelimeler içinde görünüyor:

```py
kardiz = kardiz.split()
for i in kardiz:
    print(i)

Bolvadin,
Kilis,
Siverek,
İskenderun,
İstanbul
```

Bu arada tıpkı `replace()` metodunu anlatırken gösterdiğimiz gibi, `kardiz.split()` ifadesini de yine kardiz adını taşıyan bir değişkene atadık. Böylece `kardiz.split()` komutu ile elde ettiğimiz değişiklik kaybolmamış oldu. Karakter dizilerinin değiştirilemeyen bir veri tipi olduğunu biliyorsunuz. Dolayısıyla yukarıdaki karakter dizisi üzerine `split()` metodunu uyguladığımızda aslında orijinal karakter dizisi üzerinde herhangi bir değişiklik yapmış olmuyoruz. Çıktıda görünen değişikliğin orijinal karakter dizisini etkileyebilmesi için eski karakter dizisini silip, yerine yeni değerleri yazmamız gerekiyor. Bunu da `kardiz = kardiz.split()` gibi bir komutla hallediyoruz.

Nerede kalmıştık? Gördüğünüz gibi `split()` metodu parametresiz olarak kullanıldığında karakter dizisini boşluklardan bölüyor. Ama yukarıdaki örnekte karakter dizisini boşluklardan değil de virgüllerden bölsek çok daha anlamlı bir çıktı elde edebiliriz.

Dikkatlice inceleyin:

```py
kardiz = "Bolvadin, Kilis, Siverek, İskenderun, İstanbul"
kardiz = kardiz.split(",")
print(kardiz)

['Bolvadin', ' Kilis', ' Siverek', ' İskenderun', ' İstanbul']

for i in kardiz:
    print(i)

Bolvadin
Kilis
Siverek
İskenderun
İstanbul
```

Gördüğünüz gibi, split() metodu tam da istediğimiz gibi, karakter dizisini bu kez boşluklardan değil virgüllerden böldü. Peki bunu nasıl başardı? Aslında bu sorunun cevabı gayet net bir şekilde görünüyor. Dikkat ederseniz yukarıdaki örnekte `split()` metoduna parametre olarak virgül karakter dizisini verdik. Yani şöyle bir şey yazdık:

`kardiz.split(",")`

Bu sayede split() metodu karakter dizisini virgüllerden bölmeyi başardı. Tahmin edebileceğiniz gibi, split() metoduna hangi parametreyi verirseniz bu metot ilgili karakter dizisini o karakterin geçtiği yerlerden bölecektir. Yani mesela siz bu metoda “l” parametresini verirseniz, bu metot da ‘l’ harfi geçen yerden karakter dizisini bölecektir:

```py
kardiz.split("l")

['Bo', 'vadin, Ki', 'is, Siverek, İskenderun, İstanbu', '']

for i in kardiz.split("l"):
    print(i)

Bo
vadin, Ki
is, Siverek, İskenderun, İstanbu
```

> Eğer parametre olarak verdiğiniz değer karakter dizisi içinde hiç geçmiyorsa karakter dizisi üzerinde herhangi bir değişiklik yapılmaz:
{: .prompt-tip }

```py
kardiz.split("z")

['Bolvadin, Kilis, Siverek, İskenderun, İstanbul']
```

Aynı şey, split() metodundan önce öğrendiğimiz replace() metodu için de geçerlidir. Yani eğer değiştirilmek istenen karakter, karakter dizisi içinde yer almıyorsa herhangi bir işlem yapılmaz.

split() metodu çoğunlukla, yukarıda anlattığımız şekilde parametresiz olarak veya tek parametre ile kullanılır. Ama aslında bu metot ikinci bir parametre daha alır. Bu ikinci parametre, karakter dizisinin kaç kez bölüneceğini belirler:

```py
kardiz = "Ankara Büyükşehir Belediyesi"

kardiz.split(" ", 1)

['Ankara', 'Büyükşehir Belediyesi']

kardiz.split(" ", 2)

['Ankara', 'Büyükşehir', 'Belediyesi']
```

Gördüğünüz gibi, ilk örnekte kullandığımız 1 sayısı sayesinde bölme işlemi karakter dizisi üzerine bir kez uygulandı. İkinci örnekte ise 2 sayısının etkisiyle karakter dizimiz iki kez bölme işlemine maruz kaldı.

Böylece split() metodunu öğrenmiş olduk. Gelelim rsplit() metoduna…

rsplit() metodu her yönüyle split() metoduna benzer. split() ile rsplit() arasındaki tek fark, split() metodunun karakter dizisini soldan sağa, rsplit() metodunun ise sağdan sola doğru okumasıdır. Şu örnekleri dikkatlice inceleyerek bu iki metot arasındaki farkı bariz bir şekilde görebilirsiniz:

```py
kardiz.split(" ", 1)

['Ankara', 'Büyükşehir Belediyesi']

kardiz.rsplit(" ", 1)

['Ankara Büyükşehir', 'Belediyesi']
```

Gördüğünüz gibi, `split()` metodu karakter dizisini soldan sağa doğru okuduğu için bölme işlemini “Ankara” karakter dizisine uyguladı. rsplit() metodu ise karakter dizisini sağdan sola soğru okuduğu için bölme işlemini “Belediyesi” adlı karakter dizisine uyguladı.

rsplit() metodunun pek yaygın kullanılan bir metot olmadığını belirterek splitlines() metoduna geçelim.

Bildiğiniz gibi, split() metodunu bir karakter dizisini kelime kelime ayırabilmek için kullanabiliyoruz. splitlines() metodunu ise bir karakter dizisini satır satır ayırmak için kullanabiliriz. Mesela elinizde uzun bir metin olduğunu ve amacınızın bu metin içindeki herbir satırı ayrı ayrı almak olduğunu düşünün. İşte splitlines() metoduyla bu amacınızı gerçekleştirebilirsiniz. Hemen bir örnek verelim:

```py
metin = """Python programlama dili Guido Van Rossum adlı Hollandalı bir programcı
tarafından 90'lı yılların başında geliştirilmeye başlanmıştır. Çoğu insan, isminin
Python olmasına bakarak, bu programlama dilinin, adını piton yılanından aldığını
düşünür. Ancak zannedildiğinin aksine bu programlama dilinin adı piton yılanından
gelmez. Guido Van Rossum bu programlama dilini, The Monty Python adlı bir İngiliz
komedi grubunun, Monty Python's Flying Circus adlı gösterisinden esinlenerek
adlandırmıştır. Ancak her ne kadar gerçek böyle olsa da, Python programlama
dilinin pek çok yerde bir yılan figürü ile temsil edilmesi neredeyse bir gelenek
halini almıştır diyebiliriz."""

print(metin.splitlines())
```

Bu programı çalıştırdığınızda şöyle bir çıktı alırsınız:

```py
['Python programlama dili Guido Van Rossum adlı Hollandalı bir programcı ',
"tarafından 90'lı yılların başında geliştirilmeye başlanmıştır. Çoğu insan,
isminin", 'Python olmasına bakarak, bu programlama dilinin, adını piton
yılanından aldığını ', 'düşünür. Ancak zannedildiğinin aksine bu programlama
dilinin adı piton yılanından ', 'gelmez. Guido Van Rossum bu programlama
dilini, The Monty Python adlı bir İngiliz ', "komedi grubunun, Monty Python's
Flying Circus adlı gösterisinden esinlenerek ", 'adlandırmıştır. Ancak her ne
kadar gerçek böyle olsa da, Python programlama ', 'dilinin pek çok yerde bir
yılan figürü ile temsil edilmesi neredeyse bir gelenek ', 'halini almıştır
diyebiliriz.']
```

Gördüğünüz gibi, metnimiz Enter tuşuna bastığımız noktalardan bölündü.

### lower()

Mutlaka karşılaşmışsınızdır. Bazı programlarda kullanıcıdan istenen veriler büyük-küçük harfe duyarlıdır. Yani mesela kullanıcıdan bir parola isteniyorsa, kullanıcının bu parolayı büyük-küçük harfe dikkat ederek yazması gerekir. Bu programlar açısından, örneğin ‘parola’ ve ‘Parola’ aynı kelimeler değildir. Mesela kullanıcının parolası ‘parola’ ise, bu kullanıcı programa ‘Parola’ yazarak giremez.

> Bazı başka programlarda ise bu durumun tam tersi söz konusudur. Yani büyük-küçük harfe duyarlı programların aksine bazı programlar da kullanıcıdan gelen verinin büyük harfli mi yoksa küçük harfli mi olduğunu önemsemez. Kullanıcı doğru kelimeyi büyük harfle de yazsa, küçük harfle de yazsa program istenen işlemi gerçekleştirir. Mesela Google’da yapılan aramalar bu mantık üzerine çalışır. Örneğin ‘kitap’ kelimesini Google’da aratıyorsanız, bu kelimeyi büyük harfle de yazsanız, küçük harfle de yazsanız Google size aynı sonuçları gösterecektir. Google açısından, aradığınız kelimeyi büyük ya da küçük harfle yazmanızın bir önemi yoktur.
{: .prompt-tip }

Şimdi şöyle bir program yazdığımızı düşünün:

```py
kişi = input("Aradığınız kişinin adı ve soyadı: ")

if kişi == "Ahmet Öz":
    print("email: aoz@hmail.com")
    print("tel  : 02121231212")
    print("şehir: istanbul")

elif kişi == "Mehmet Söz":
    print("email: msoz@zmail.com")
    print("tel  : 03121231212")
    print("şehir: ankara")

elif kişi == "Mahmut Göz":
    print("email: mgoz@jmail.com")
    print("tel  : 02161231212")
    print("şehir: istanbul")

else:
    print("Aradığınız kişi veritabanında yok!")
```

> Bu programın doğru çalışabilmesi için kullanıcının, örneğin, Ahmet Öz adlı kişiyi ararken büyük-küçük harfe dikkat etmesi gerekir. Eğer kullanıcı Ahmet Öz yazarsa o kişiyle ilgili bilgileri alabilir, ama eğer mesela Ahmet öz yazarsa bilgileri alamaz. Peki acaba biz bu sorunun üstesinden nasıl gelebiliriz? Yani programımızın büyük-küçük harfe duyarlı olmamasını nasıl sağlayabiliriz?

Bu işi yapmanın iki yolu var: Birincisi if bloklarını her türlü ihtimali düşünerek yazabiliriz. Mesela:

```py
if kişi == "Ahmet Öz" or kişi == "Ahmet öz" or kişi == "ahmet öz":
    ...
```

Ama burada bazı problemler var. Birincisi, kullanıcının kaç türlü veri girebileceğini kestiremeyebilirsiniz. İkincisi, kestirebilseniz bile, her kişi için olasılıkları girmeye çalışmak eziyetten başka bir şey değildir…

İşte burada imdadımıza lower() metodu yetişecek. Dikkatlice inceleyin:

```py
kişi = input("Aradığınız kişinin adı ve soyadı: ")
kişi = kişi.lower()

if kişi == "ahmet öz":
    print("email: aoz@hmail.com")
    print("tel  : 02121231212")
    print("şehir: istanbul")

elif kişi == "mehmet söz":
    print("email: msoz@zmail.com")
    print("tel  : 03121231212")
    print("şehir: ankara")

elif kişi == "mahmut göz":
    print("email: mgoz@jmail.com")
    print("tel  : 02161231212")
    print("şehir: istanbul")

else:
    print("Aradığınız kişi veritabanında yok!")
```

Artık kullanıcı ‘ahmet öz’ de yazsa, ‘Ahmet Öz’ de yazsa, hatta ‘AhMeT öZ’ de yazsa programımız doğru çalışacaktır. Peki bu nasıl oluyor? Elbette `lower()` metodu sayesinde…

Yukarıdaki örneklerin de bize gösterdiği gibi, lower() metodu, karakter dizisindeki bütün harfleri küçük harfe çeviriyor. Örneğin:

```py
kardiz = "ELMA"
kardiz.lower()

'elma'

kardiz = "arMuT"
kardiz.lower()

'armut'

kardiz = "PYTHON PROGRAMLAMA"
kardiz.lower()

'python programlama'
```

Eğer karakter dizisi zaten tamamen küçük harflerden oluşuyorsa bu metot hiçbir işlem yapmaz:

### upper()

Bu metot biraz önce öğrendiğimiz lower() metodunun yaptığı işin tam tersini yapar. Hatırlarsanız lower() metodu yardımıyla karakter dizileri içindeki harfleri küçültüyorduk. upper() metodu ise bu harfleri büyütmemizi sağlar.

Örneğin:

```py
kardiz = "kalem"
kardiz.upper()

'KALEM'
```

lower() metodunu anlatırken, kullanıcıdan gelen verileri belli bir düzene sokmak konusunda bu metodun oldukça faydalı olduğunu söylemiştik. Kullanıcıdan gelen verilerin lower() metodu yardımıyla standart bir hale getirilmesi sayesinde, kullanıcının girdiği kelimelerin büyük-küçük harfli olmasının önemli olmadığı programlar yazabiliyoruz. Elbette eğer isterseniz kullanıcıdan gelen bütün verileri lower() metoduyla küçük harfe çevirmek yerine, upper() metoduyla büyük harfe çevirmeyi de tercih edebilirsiniz. Python programcıları genellikle kullanıcı verilerini standart bir hale getirmek için bütün harfleri küçültmeyi tercih eder, ama tabii ki sizin bunun tersini yapmak istemenizin önünde hiçbir engel yok.

### islower(), isupper()

Yukarıda öğrendiğimiz lower() ve upper() adlı metotlar karakter dizileri üzerinde bazı değişiklikler yapmamıza yardımcı oluyor. Karakter dizileri üzerinde birtakım değişiklikler yapmamızı sağlayan bu tür metotlara ‘değiştirici metotlar’ adı verilir. Bu tür metotların dışında bir de ‘sorgulayıcı metotlar’dan söz edebiliriz. Sorgulayıcı metotlar, değiştirici metotların aksine, bir karakter dizisi üzerinde değişiklik yapmamızı sağlamaz. Bu tür metotların görevi karakter dizilerinin durumunu sorgulamaktır. Sorgulayıcı metotlara örnek olarak islower() ve isupper() metotlarını verebiliriz.

Bildiğiniz gibi, lower() metodu bir karakter dizisini tamamen küçük harflerden oluşacak şekle getiriyordu. islower() metodu ise bir karakter dizisinin tamamen küçük harflerden oluşup oluşmadığını sorguluyor.

Hemen bir örnek verelim:

```py
kardiz = "istihza"
kardiz.islower()

True
```

“istihza” tamamen küçük harflerden oluşan bir karakter dizisi olduğu için islower() sorgusu True çıktısı veriyor. 

isupper() metodu da islower() metodunun yaptığı işin tam tersini yapar. Bildiğiniz gibi, upper() metodu bir karakter dizisini tamamen büyük harflerden oluşacak şekle getiriyordu. isupper() metodu ise bir karakter dizisinin tamamen büyük harflerden oluşup oluşmadığını sorguluyor:

```py
kardiz = "İSTİHZA"
kardiz.isupper()

True

kardiz = "python"
kardiz.isupper()

False
```

> Tıpkı islower() metodunda olduğu gibi, isupper() metodunu da kullanıcıdan gelen verinin büyük harfli mi yoksa küçük harfli mi olduğunu denetlemek için kullanabilirsiniz.
{: .prompt-tip }

### endswith()

Tıpkı isupper() ve islower() metotları gibi, endswith() metodu da sorgulayıcı metotlardan biridir. endswith() metodu karakter dizileri üzerinde herhangi bir değişiklik yapmamızı sağlamaz. Bu metodun görevi karakter dizisinin durumunu sorgulamaktır.

Bu metot yardımıyla bir karakter dizisinin hangi karakter dizisi ile bittiğini sorgulayabiliyoruz. Yani örneğin:

```py
kardiz = "istihza"
kardiz.endswith("a")

True
```

### startswith()

Bu metot, biraz önce gördüğümüz endswith() metodunun yaptığı işin tam tersini yapar. Hatırlarsanız endswith() metodu bir karakter dizisinin hangi karakter veya karakterlerle bittiğini denetliyordu. startswith() metodu ise bir karakter dizisinin hangi karakter veya karakterlerle başladığını denetler:

### capitalize()

Hatırlarsanız, bir önceki bölümde öğrendiğimiz startswith() ve endswith() metotları karakter dizileri üzerinde herhangi bir değişiklik yapmıyordu. Bu iki metodun görevi, karakter dizilerini sorgulamamızı sağlamaktı. Şimdi göreceğimiz capitalize() metodu ise karakter dizileri üzerinde değişiklik yapmamızı sağlayacak. Dolayısıyla bu capitalize() metodu da ‘değiştirici metotlar’dan biridir diyebiliriz.

Hatırlarsanız, upper() ve lower() metotları bir karakter dizisi içindeki bütün karakterleri etkiliyordu. Yani mesela upper() metodunu bir karakter dizisine uygularsak, o karakter dizisi içindeki bütün karakterler büyük harfe dönecektir. Aynı şekilde lower() metodu da bir karakter dizisi içindeki bütün karakterleri küçük harfe çevirir.

Şimdi göreceğimiz capitalize() metodu da upper() ve lower() metotlarına benzemekle birlikte onlardan biraz daha farklı davranır: capitalize() metodunun görevi karakter dizilerinin yalnızca ilk harfini büyütmektir. Örneğin:

```py
a = "python"
a.capitalize()

'Python'
```

> Bu metodu kullanırken dikkat etmemiz gereken bir nokta var: Bu metot bir karakter dizisinin yalnızca ilk harfini büyütür. Yani birden fazla kelimeden oluşan karakter dizilerine bu metodu uyguladığımızda bütün kelimelerin ilk harfi büyümez. Yalnızca ilk kelimenin ilk harfi büyür. Yani:
{: .prompt-warning }

```py
a = "python programlama dili"
a.capitalize()

'Python programlama dili'
```

“python programlama dili” üç kelimeden oluşan bir karakter dizisidir. Bu karakter dizisi üzerine capitalize() metodunu uyguladığımızda bu üç kelimenin tamamının ilk harfleri büyümüyor. Yalnızca ilk ‘python’ kelimesinin ilk harfi bu metottan etkileniyor.

### title()

Bu metot biraz önce öğrendiğimiz capitalize() metoduna benzer. Bildiğiniz gibi capitalize() metodu bir karakter dizisinin yalnızca ilk harfini büyütüyordu. `title()` metodu da karakter dizilerinin ilk harfini büyütür. Ama capitalize() metodundan farklı olarak bu metot, birden fazla kelimeden oluşan karakter dizilerinin **her kelimesinin ilk harflerini büyütür**.

Bunu bir örnek üzerinde anlatsak sanırım daha iyi olacak:

```py
a = "python programlama dili"
a.capitalize()

'Python programlama dili'

a.title()

'Python Programlama Dili'
```

`capitalize()` metodu ile `title()` metodu arasındaki fark bariz bir biçimde görünüyor. Dediğimiz gibi, capitalize() metodu yalnızca ilk kelimenin ilk harfini büyütmekle yetinirken, title() metodu karakter dizisi içindeki bütün kelimelerin ilk harflerini büyütüyor.

### swapcase()

swapcase() metodu da büyük-küçük harfle ilgili bir metottur. Bu metot bir karakter dizisi içindeki büyük harfleri küçük harfe; küçük harfleri de büyük harfe dönüştürür. Örneğin:

```py
kardiz = "python"
kardiz.swapcase()

'PYTHON'

kardiz = "PYTHON"
kardiz.swapcase()

'python'

kardiz = "Python"
kardiz.swapcase()

'pYTHON'
```

### join()

Hatırlarsanız şimdiye kadar öğrendiğimiz metotlar arasında `split()` adlı bir metot vardı. Bu metodun ne işe yaradığını ve nasıl kullanıldığını biliyorsunuz:

```py
kardiz = "Beşiktaş Jimnastik Kulübü"
bölünmüş = kardiz.split()
print(bölünmüş)

['Beşiktaş', 'Jimnastik', 'Kulübü']
```

Gördüğünüz gibi split() metodu bir karakter dizisini belli yerlerden bölerek parçalara ayırıyor. Bu noktada insanın aklına şöyle bir soru geliyor: Diyelim ki elimizde böyle bölünmüş bir karakter dizisi grubu var. Biz bu grup içindeki karakter dizilerini tekrar birleştirmek istersek ne yapacağız?

Şimdi şu kodlara çok dikkatlice bakın:

```py
" ".join(bölünmüş)

'Beşiktaş Jimnastik Kulübü'
```

Gördüğünüz gibi, “Beşiktaş Jimnastik Kulübü” adlı karakter dizisinin ilk halini tekrar elde ettik. Yani bu karakter dizisine ait, bölünmüş parçaları tekrar bir araya getirdik. Ancak bu işi yapan kod gözünüzüne biraz tuhaf ve anlaşılmaz görünmüş olabilir.

İlk başta dikkatimizi çeken şey, bu metodun öbür metotlara göre biraz daha farklı bir yapıya sahipmiş gibi görünmesi. Ama belki yukarıdaki örneği şöyle yazarsak bu örnek biraz daha anlaşılır gelebilir gözünüze:

```py
birleştirme_karakteri = " "
birleştirme_karakteri.join(bölünmüş)
```

Burada da tıpkı öteki metotlarda olduğu gibi, `join()` metodunu bir karakter dizisi üzerine uyguladık.

### count()

Tıpkı daha önce öğrendiğimiz sorgulayıcı metotlar gibi, count() metodu da bir karakter dizisi üzerinde herhangi bir değişiklik yapmamızı sağlamaz. Bu metodun görevi *bir karakter dizisi içinde belli bir karakterin kaç kez geçtiğini sorgulamaktır*. Bununla ilgili hemen bir örnek verelim:

```py
şehir = "Kahramanmaraş"
şehir.count("a")

5
```

Buradan anlıyoruz ki, “Kahramanmaraş” adlı karakter dizisi içinde toplam 5 adet “a” karakteri geçiyor.

### index(), rindex()

Bu bölümün başında karakter dizilerinin dilimlenme özelliğinden söz ederken, karakter dizisi içindeki her harfin bir sırası olduğunu söylemiştik. Örneğin “python” adlı karakter dizisinde ‘p’ harfinin sırası 0’dır. Aynı şekilde ‘n’ harfinin sırası ise 5’tir. Karakterlerin, bir karakter dizisi içinde hangi sırada bulunduğunu öğrenmek için `index()` adlı bir metottan yararlanabiliriz. Örneğin:

```py
kardiz = "python"
kardiz.index("p")

0

kardiz.index("n")

5
```

Eğer sırasını sorguladığımız karakter, o karakter dizisi içinde bulunmuyorsa, bu durumda Python bize bir hata mesajı gösterir:

### find, rfind()

find() ve rfind() metotları tamamen index() ve rindex() metotlarına benzer. find() ve rfind() metotlarının görevi de bir karakter dizisi içindeki bir karakterin konumunu sorgulamaktır:

```py
kardiz = "adana"
kardiz.find("a")

0

kardiz.rfind("a")

4
```

Peki index() / rindex() ve find() / rfind() metotları arasında ne fark var?

`index()` ve `rindex()` metotları karakter dizisi içindeki karakteri sorgularken, eğer o karakteri bulamazsa bir **ValueError hatası** verir:

```py
kardiz = "adana"
kardiz.index("z")

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: substring not found
```

Ama `find()` ve `rfind()` metotları böyle bir durumda -1 çıktısı verir:

```py
kardiz = "adana"
kardiz.find("z")

-1
```

Bu iki metot çifti arasındaki tek fark budur.

### partition(), rpartition()

Bu metot yardımıyla bir karakter dizisini belli bir ölçüte göre üçe bölüyoruz. Örneğin:

```py
a = "istanbul"
a.partition("an")

('ist', 'an', 'bul')
```

Eğer partition() metoduna parantez içinde verdiğimiz ölçüt karakter dizisi içinde bulunmuyorsa şu sonuçla karşılaşırız:

```py
a = "istanbul"
a.partition("h")

('istanbul', '', '')
```

Gelelim rpartition() metoduna… Bu metot da partition() metodu ile aynı işi yapar, ama yöntemi biraz farklıdır. partition() metodu karakter dizilerini soldan sağa doğru okur. rpartition() metodu ise sağdan sola doğru. 

### str.maketrans(), translate()

Bu iki metot birbiriyle bağlantılı olduğu ve genellikle birlikte kullanıldığı için, bunları bir arada göreceğiz.

Dilerseniz bu iki metodun ne işe yaradığını anlatmaya çalışmak yerine bir örnek üzerinden bu metotların görevini anlamayı deneyelim.

Şöyle bir vaka hayal edin: Bildiğiniz gibi, internet üzerinde bazen Türkçe karakterleri kullanamıyoruz. Böyle durumlarda, elimizdeki bir metni, cümleyi veya kelimeyi Türkçe karakter içermeyecek bir hale getirmemiz gerekebiliyor. Örneğin şu cümleyi ele alalım:

> Bildiğiniz gibi, internet üzerinde bazen Türkçe karakterleri kullanamıyoruz.

İşte buna benzer bir cümleyi kimi zaman Türkçe karakterlerinden arındırmak zorunda kalabiliyoruz. Eğer elinizde Türkçe yazılmış bir metin varsa ve sizin amacınız bu metin içinde geçen Türkçeye özgü karakterleri noktasız benzerleriyle değiştirmek ise str.maketrans() ve translate() metotlarından yararlanabilirsiniz.

Örneğimiz şu cümle idi:

**Bildiğiniz gibi, internet üzerinde bazen Türkçe karakterleri kullanamıyoruz.**

Amacımız bu cümleyi şu şekilde değiştirmek:

**Bildiginiz gibi, internet uzerinde bazen Turkce karakterleri kullanamiyoruz.**

Bunun için şöyle bir kod yazabilirsiniz:

```py
kaynak = "şçöğüıŞÇÖĞÜİ"
hedef  = "scoguiSCOGUI"

çeviri_tablosu = str.maketrans(kaynak, hedef)

metin = "Bildiğiniz gibi, internet üzerinde bazen Türkçe karakterleri kullanamıyoruz."

print(metin.translate(çeviri_tablosu))
```

Bu kodları çalıştırdığımızda şöyle bir çıktı elde ederiz:

`Bildiginiz gibi, internet uzerinde bazen Turkce karakterleri kullanamiyoruz.`

Gördüğünüz gibi, “kaynak” adlı karakter dizisi içinde belirttiğimiz bütün harfler “hedef” adlı karakter dizisi içindeki harflerle tek tek değiştirildi. Böylece Türkçeye özgü karakterleri (‘şçöğüıŞÇÖĞÜİ’) en yakın noktasız benzerleriyle (‘scoguiSCOGUI’) değiştirmiş olduk.

### isalpha()

Bu metot yardımıyla bir karakter dizisinin ‘alfabetik’ olup olmadığını denetleyeceğiz. Peki ‘alfabetik’ ne demek?

Eğer bir karakter dizisi içinde yalnızca alfabe harfleri (‘a’, ‘b’, ‘c’ gibi…) varsa o karakter dizisi için ‘alfabetik’ diyoruz. Bir örnekle bunu doğrulayalım:

```py
a = "kezban"
a.isalpha()

True
```

Ama:

```py
b = "k3zb6n"
b.isalpha()

False
```

### isdigit()

Bu metot da isalpha() metoduna benzer. Bunun yardımıyla bir karakter dizisinin sayısal olup olmadığını denetleyebiliriz. Sayılardan oluşan karakter dizilerine *‘sayı değerli karakter dizileri’* adı verilir. Örneğin şu bir *‘sayı değerli karakter dizisi’*dir:

`a = "12345"`

Metodumuz yardımıyla bunu doğrulayabiliriz:

`a.isdigit()`

True

Ama şu karakter dizisi sayısal değildir:

`b = "123445b"`

Hemen kontrol edelim:

`b.isdigit()`

False

### isalnum()

Bu metot, bir karakter dizisinin ‘alfanümerik’ olup olmadığını denetlememizi sağlar. Peki ‘alfanümerik’ nedir?

Daha önce bahsettiğimiz metotlardan hatırlayacaksınız:

Alfabetik karakter dizileri, alfabe harflerinden oluşan karakter dizileridir.

Sayısal karakter dizileri, sayılardan oluşan karakter dizileridir.

Alfanümerik karakter dizileri ise bunun birleşimidir. Yani sayı ve/veya harflerden oluşan karakter dizilerine alfanümerik karakter dizileri adı verilir. Örneğin şu karakter dizisi alfanümerik bir karakter dizisidir:

`a = "123abc"`

İsterseniz hemen bu yeni metodumuz yardımıyla bunu doğrulayalım:

`a.isalnum()`

True

### isdecimal()

Bu metot yardımıyla bir karakter dizisinin ondalık sayı cinsinden olup olmadığını denetliyoruz. Mesela aşağıdaki örnek ondalık sayı cinsinden bir karakter dizisidir:

`a = "123"`

`a.isdecimal()`

True

Ama şu ise kayan noktalı (floating-point) sayı cinsinden bir karakter dizisidir:

`a = "123.3"`

`a.isdecimal()`

False

Dolayısıyla a.isdecimal() komutu False çıktısı verir…

## 8.2 Karakter Dizilerini Biçimlendirmek

Bu bölüme gelinceye kadar, Python’da karakter dizilerinin biçimlendirilmesine ilişkin epey söz söyledik. Ancak bu konu ile ilgili bilgilerimiz hem çok dağınık, hem de çok yüzeysel. İşte bu bölümde amacımız, daha önce farklı yerlerde dile getirdiğimiz bu önemli konuya ait bilgi kırıntılarını bir araya toplayıp, karakter dizisi biçimlendirme konusunu, Python bilgimiz elverdiği ölçüde ayrıntılı bir şekilde ele almak olacak.

Şu ana kadar yaptığımız örneklere bakarak, programlama maceranız boyunca karakter dizileriyle bol bol haşır neşir olacağınızı anlamış olmalısınız. Bundan sonra yazdığınız programlarda da karakter dizilerinin size pek çok farklı biçimlerde geldiğine tanık olacaksınız. Farklı farklı biçimlerde elinize ulaşan bu karakter dizilerini, muhtemelen, sadece alt alta ve rastgele bir şekilde ekrana yazdırmakla yetinmeyeceksiniz. Bu karakter dizilerini, yazdığınız programlarda kullanabilmek için, programınıza **uygun şekillerde biçimlendirmeniz** gerekecek.

### format() Metodu ile Biçimlendirme

En başta da söylediğimiz gibi, % işaretini kullanarak karakter dizisi biçimlendirme eskide kalmış bir yöntemdir. Bu yöntem ağırlıklı olarak Python’ın 2.x sürümlerinde kullanılıyordu. Her ne kadar bu yöntemi Python’ın 3.x sürümlerinde de kullanmak mümkün olsa da yeni yazılan kodlarda bu yöntem yerine biraz sonra göreceğimiz format() metodunu kullanmak çok daha akıllıca olacaktır. Çünkü muhtemelen % ile biçimlendirme yöntemi, ileriki bir Python sürümünde dilden *tamamen kaldırılacak*. Bu yüzden bu eski metoda fazla bel bağlamamak gerekiyor.

Daha önceki derslerimizde verdiğimiz örnekler sayesinde format() metodunun temel olarak nasıl kullanılacağını biliyoruz. Ama isterseniz biz yine de bütünlük açısından `format()` metodunun temel kullanımını burada tekrar ele alalım.

`format()` metodunu en basit şekilde şöyle kullanıyoruz:

`print("{} ve {} iyi bir ikilidir!".format("Django", "Python"))`

> Django ve Python iyi bir ikilidir!

Gördüğünüz gibi, eski yöntemdeki % işaretine karşılık, yeni yöntemde {} işaretini kullanıyoruz.

Çok basit bir örnek daha verelim:

```py
isim = input("İsminiz: ")
print("Merhaba {}. Nasılsın?".format(isim))

# Elbette bu örneği şu şekilde de yazabilirdik:

isim = input("İsminiz: ")
print("Merhaba", isim + ".", "Nasılsın?")
```

> Burada format() metodunu ve biçim düzenleyicileri hiç kullanmadan, sadece karakter dizilerini birleştirerek istediğimiz çıktıyı elde ettik. Ama siz de görüyorsunuz; karakter dizilerini birleştirmekle uğraşacağımıza format() metodunu kullanmak hem daha pratiktir, hem de bu şekilde yazdığımız kodlar daha okunaklı olur.
{: .prompt-info }

Yukarıdaki örnekte format() metodunu tek bir parametre ile birlikte kullandık (isim). Bu parametre (tıpkı eski % işaretinde olduğu gibi), karakter dizisi içindeki {} işaretine karşılık geliyor.

Bu konuyu daha iyi anlayabilmek için bir örnek daha verelim:

```py
kalkış       = input("Kalkış yeri: ")
varış        = input("Varış yeri: ")
isim_soyisim = input("İsim ve soyisim: ")
bilet_sayısı = input("Bilet sayısı: ")

print("""{} noktasından {} noktasına, 14:30 hareket saatli sefer için {} adına {} adet bilet ayrılmıştır!""".format(kalkış, varış,isim_soyisim,bilet_sayısı))
```

Gördüğünüz gibi, {} işaretleri karakter dizisi içinde bir ‘yer tutma’ görevi görüyor. Tutulan bu yerlere nelerin geleceğini format() metodunun parametreleri vasıtasıyla belirliyoruz.

Elbette eğer isterseniz yukarıdaki örneği şu şekilde de yazabilirsiniz:

```py
kalkış       = input("Kalkış yeri: ")
varış        = input("Varış yeri: ")
isim_soyisim = input("İsim ve soyisim: ")
bilet_sayısı = input("Bilet sayısı: ")

metin = "{} noktasından {} noktasına, 14:30 hareket saatli sefer için {} adına {} adet bilet ayrılmıştır!"

print(metin.format(kalkış, varış, isim_soyisim, bilet_sayısı))
```

Ancak **yaygın olarak kullanılan yöntem**, karakter dizisini herhangi bir değişkene atamadan, doğrudan format() metoduna bağlamaktır. Elbette hangi yöntem kolayınıza geliyorsa onu tercih etmekte özgürsünüz. Ama özellikle biçimlendirilecek karakter dizisinin çok uzun olduğu durumlarda, yukarıdaki gibi, karakter dizisini önce bir değişkene atayıp, sonra da bu değişken üzerine format() metodunu uygulamak daha mantıklı olabilir.

Küme parantezlerini, yukarıdaki örneklerde görüldüğü şekilde içi boş olarak kullanabilirsiniz. Böyle bir durumda Python, karakter dizisi içindeki küme parantezleriyle, karakter dizisi dışındaki değerleri teker teker ve sırasıyla eşleştirecektir. Ama isterseniz küme parantezleri içine birer sayı yazarak, karakter dizisi dışındaki değerlerin hangi sırayla kullanılacağını belirleyebilirsiniz. Örneğin:

"{0} {1}".format("Sonsuz", "Us")

'Sonsuz Us'

Küme parantezleri içinde sayı kullanabilme imkanı sayesinde değerlerin sırasını istediğiniz gibi düzenleyebilirsiniz:

"{1} {0}".format("Sonsuz", "Us")

'Us Sonsuz'

Hatta bu özellik sayesinde değerleri bir kez yazıp, birden fazla sayıda tekrar edebilirsiniz:

"{0} {1} ({1} {0})".format("Sonsuz", "Us")

'Sonsuz Us (Us Sonsuz)'

Yukarıdaki örnekler bize, format() metodunun parametrelerine sıra numarasına göre erişebileceğimizi gösteriyor. Biz aynı zamanda bu metodun parametrelerine isme göre de erişebiliriz. Çok basit bir örnek:

`print("{dil} dersleri".format(dil="python"))`

Bu yöntemi kullanarak, aynı değişkeni birkaç farklı yerde kullanabilirsiniz:

```py
sayfa = """
<html>

<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>{konu}</title>
</head>

<body>
    <h1>Sonsuz.Us web sitesine hoş geldiniz!</h1>
    <p><b>{konu}</b> için bir Türkçe eğitim projesi...</p>
</body>

</html>
"""

print(sayfa.format(konu="Python Programlama Dili"))
```

format() metodunun yetenekleri yukarıda gösterdiğimiz şeylerle sınırlı değildir. Tıpkı eski biçimlendirme yönteminde olduğu gibi, {} işaretleri arasında bazı sayılar kullanarak, karakter dizileri üzerinde hizalama işlemleri de yapabiliriz.

Dikkatlice bakın:

```py
print("{:>15}".format("istihza"))

         istihza
```

Bu gösterim gözünüze oldukça yabancı ve karışık gelmiş olabilir. Ama aslında hiç de öyle anlaşılmaz bir yanı yoktur bu kodların. Gördüğünüz gibi, burada öncelikle `:` adlı bir işaretten yararlanıyoruz. Bu işaretin ardından `>` adlı başka bir işaret görüyoruz. Son olarak da 15 sayısını kullanıyoruz.

`:` işareti, bir biçimlendirme işlemi yapacağımızı gösteriyor. `>` işareti ise bu biçimlendirmenin bir hizalama işlemi olacağını haber veriyor. En sondaki 15 sayısı ise bu hizalama işleminin 15 karakterlik bir alan ile ilgili olduğunu söylüyor. Bu şekilde karakter dizisini 15 karakterlik bir alan içine yerleştirip karakter dizisini sağa yasladık. Yukarıdaki çıktıyı daha iyi anlayabilmek için kodları şöyle de yazabilirsiniz:

```py
print("|{:>15}|".format("istihza"))

|       istihza|
```

Gördüğünüz gibi, karakter dizimiz, kendisine ayrılan 15 karakterlik alan içinde sağa yaslanmış vaziyette duruyor.

Eğer aynı karakter dizisini sola yaslamak isterseniz şöyle bir şey yazabilirsiniz:

```py
print("|{:<15}|".format("istihza"))

|istihza        |
```

Bu defa < adlı işaretten yararlandığımıza dikkat edin.

Yukarıdaki yöntemi kullanarak, karakter dizilerini sola veya sağa yaslamanın yanısıra, kendilerine ayrılan alan içinde ortalayabilirsiniz de:

```py
print("|{:^15}|".format("istihza"))

|    istihza    |
```

Gördüğünüz gibi, python3 ile gelen format() metodunu hizalama işlemleri için kullanırken üç farklı işaretten yararlanıyoruz:

`>`

*sağa yaslama*

`<`

*sola yaslama*

`^`

*ortalama*

Yukarıdaki işaretler, yaptıkları işi çağrıştırdıkları için, bunları akılda tutmak çok zor olmasa gerek. Mesela örnek olması açısından, eski biçimlendirme yönteminin son kısmında verdiğimiz şu örneği:

```py
for sıra, karakter in enumerate(dir(str)):
    if sıra % 3 == 0:
        print("\n", end="")
    print("%-20s" %karakter, end="")
```

… bir de yeni format() metoduyla yazalım:

```py
for sıra, karakter in enumerate(dir(str)):
    if sıra % 3 == 0:
        print("\n", end="")
    print("{:<20}".format(karakter), end="")
```

Bu örneği inceleyerek, eski ile yeni yöntem arasında nelerin değiştiğini, neyin neye karşılık geldiğini görebilirsiniz.

### Biçimlendirme Karakterleri

Hatırlarsanız Python2’de geçerli olan eski biçimlendirme yönteminde % karakteri ile bazı harfleri birlikte kullanarak karakter dizileri üzerinde biçimlendirme ve dönüştürme işlemleri yapabiliyorduk. Aynı şey Python3 ile birlikte gelen bu format() metodu için de geçerlidir. Yani benzer harfleri kullanarak format() metodu ile de karakter dizileri üzerinde biçimlendirme ve dönüştürme işlemleri yapabiliriz.

format() metodu ile birlikte şu harfleri kullanabiliyoruz:

s
: Bu harf karakter dizilerini temsil eder.

Yalnız bu biçimlendirici karakterlerin {} işaretleri içindeki kullanımı ilk bakışta gözünüze biraz karışık gelebilir:

`print("{:s}".format("karakter dizisi"))`

karakter dizisi
: Bu arada, harfleri {} yapısının içinde nasıl kullandığımıza dikkat edin. Gördüğünüz gibi biçimlendirme karakterini kullanırken, karakterin sol tarafına bir adet : işareti de yerleştiriyoruz. Bir örnek verelim:

`print("{:s} ve {:s} iyi bir ikilidir!".format("Python", "Django"))`

Yalnız, s harfi karakter dizilerini temsil ettiği için, {} işaretleri arasında bu harfi kullandığımızda, format() metodunun alabileceği parametreyi karakter dizisiyle sınırlandırmış oluruz. Dolayısıyla bu harfi kullandıktan sonra format() metodu içinde sadece karakter dizilerini kullanabiliriz. 

d
: Bu harf sayıları temsil eder:

```py
print("{:d}".format(65))

65
```

Eğer sayı dışında bir değer kullanırsanız Python size bir hata mesajı gösterir:

```py
print("{:d}".format("65"))

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: Unknown format code 'd' for object of type 'str'
```

o
: Bu harf onlu düzendeki sayıları sekizli düzendeki karşılıklarına çevirir:

```py
print("{:o}".format(65))

101
```

x
: Bu harf onlu düzendeki sayıları onaltılı düzendeki karşılıklarına çevirir:

```py
print("{:x}".format(65))

41
```

X
: Tıpkı x harfinde olduğu gibi, bu harf de onlu düzendeki sayıları onaltılı düzendeki karşılıklarına çevirir:

```py
"{:X}".format(65)

'41'
```

Peki x ile X harfi arasında ne fark var? Fark şudur: x; onaltılı düzende harfle gösterilen sayıları küçük harf şeklinde temsil eder. X işareti bu sayıları büyük harf şeklinde temsil eder. Bu ikisi arasındaki farkı daha net görmek için şöyle bir kod yazabilirsiniz:

```py
for i in range(20):
    print("{:x}{:10X}".format(i, i))

0         0
1         1
2         2
3         3
4         4
5         5
6         6
7         7
8         8
9         9
a         A
b         B
c         C
d         D
e         E
f         F
10        10
11        11
12        12
13        13
```

Gördüğünüz gibi gerçekten de x harfi onaltılı düzende harflerle gösterilen sayıları küçük harf olarak; X harfi ise büyük harf olarak temsil ediyor.

b
: Bu işaret, onlu düzendeki sayıları ikili düzendeki karşılıklarına çevirir:

```py
"{:b}".format(2)

'10'
```

f
: Bu işaret, eski biçimlendirme yöntemini anlatırken gösterdiğimiz f işaretiyle benzer bir işleve sahiptir:

```py
print("{:.2f}".format(50))

50.00
```

,
: \: işaretini , işareti (basamak ayracı) ile birlikte kullanarak, sayıları basamaklarına ayırabilirsiniz:

```py
"{:,}".format(1234567890)

'1,234,567,890'
```

Böylece Python’da karakter dizisi biçimlendirmenin hem eski hem de yeni yöntemini, şu ana kadarki Python bilgimiz elverdiği ölçüde ayrıntılı bir şekilde incelemiş olduk. Buradaki bilgileri kullanarak bol bol örnek yapmak bu konuyu daha iyi anlamanıza yardımcı olacaktır.

## 8.3 Alıştırmalar

- Kullanıcıdan mail adresini isteyin ve kullanıcı adı domain olacak şekilde ikiye bölün. Örnek deneme@gmail.com, ['deneme','gmail.com']

- Kullanıcının gireceği ad soyad bilgilerini küçük harfe çevirin.

- Kullanıcının girdiği metindeki tüm harfleri sayıp, her harften kaç tane olduğunu yazdırın.

- Kullanıcının girdiği metni türkçe harflerden arındırarak yazınız.

- Kullanıcıdan telefon numarasını isteyin ve içinde harf varsa tamamı sayı girene kadar istemeye devam edin.

- Kullanıcının girdiği sayıyı para formatında yazınız. (binlik ayraçlar "," ile kuruş ayracı "." ile olacak şekilde)

- maketrans ve translate metodları ile bir şifreleme programı yazınız.