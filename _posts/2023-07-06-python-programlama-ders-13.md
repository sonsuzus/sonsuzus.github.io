---
title: Python Programlama Ders 13. Sınıflar ve nesneler
author: sonsuz
date: 2023-07-06 16:26:44 +0300
categories: [Program,Python]
tags: [nesne,sınıf,class,oop,ders,python,programlama]
---



## 13.1 Nesne yönelimli programlama

Python **nesne yönelimli programlama dilidir**, bunun anlamı **nesne yönelimli programlamanın** (Object Oriented Programming - OOP) desteklediği özellikleri sağlar.

Nesne yönelimli programlama 1960larda ortaya çıkmasına rağmen 1980lerin ortasına kadar yeni yazılım üretmede ana **programlama paradigması** haline gelmedi. Hızlı bir şekilde büyüyen ve karmaşıklaşan yazılım sistemlerini kotarmak ve bu büyük ve karmaşık sistemleri zaman içerisinde daha kolay değiştirmek için geliştirilmiştir.

Şu ana kadar programları **yordamsal (procedural) programlama** paradigmasını kullanarak yazdık. Yordamsal programlamada fonksiyonları veya *yordamları* yazmaya odaklanma sözkonusudur. Fonksiyonlar/yordamlar veri üzerinde işlem yaparlar. Nesne yönelimli programlamada odak **nesnelerin** yaratılmasındadır, nesneler hem veriyi hem de işlevselliği birlikte barındırır.

## 13.2 Kullanıcı tanımlı bileşik tipler

Sınıf esas olarak yeni bir **veri tipi** tanımlar. Şu ana kadar kitapta Python'un içinde tanımlı tipleri kullandık, şimdi kendi kullanıcı tanımlı tiplerimizi yaratmaya başlayabiliriz: `Nokta`.

Matematiksel nokta kavramını düşünelim. İki boyutlu bir uzayda, nokta iki sayıdan (koordinatlar) oluşan ve birlikte tek bir nesne olarak ele alınır. Matematiksel gösterimde, noktalar genellikle parantez içerisinde virgül ile ayrılmış iki sayı şeklinde gösterilir. Örneğin `(0,0)` başlangıç (origin) noktasını, `(x,y)` ise başlangıçtan `x` birim kadar sağdaki ve `y` birim kadar yukarıdaki bir noktayı gösterir.

Python'da bir noktayı doğal olarak temsil etmenin bir yolu iki nümerik kullanmaktır. Soru, bu iki nümerik değeri nasıl gruplayacağız sorusudur. Hızlı ve kötü bir çözüm bir liste veya tuple kullanmaktır ve bazı uygulamalar için en iyi çözüm olabilir.

Bir alternatif yöntem ise kullanıcı tanımlı bileşik tip tanımlamaktır, bu bileşik tipe **sınıf** adı verilmektedir. Bu yaklaşım biraz çaba gerektirir, ancak avantajları ortaya çıkacaktır.

Bir sınıf tanımı aşağıdaki gibidir:

```py
class Nokta:
    pass
```

Sınıf tanımları programın içerisinde herhangi bir yerde bulunabilir, ancak genellikle başlangıçta kullanılırlar (`import` cümlelerinden sonra). Sınıf tanımı için sözdizimi kuralları bileşik cümleler için olanlarla aynıdır. Bir başlık vardır, `class` anahtar kelimesiyle tanımlı, sonrasında sınıfın ismi bulunur ve cümle iki nokta üstüste ile bitirilir.

Yukarıdaki tanımlama `Nokta` olarak çağrılan bir yeni sınıf yaratır. `pass` cümlesi etkisizdir; sadece bileşik cümlenin gövdesinde bir şey olması gerektiği için yazılmıştır.

`Nokta`sınıfını yaratarak, Nokta isminde yeni bir tip oluşturmuş olduk. Bu tipin üyeleri, tipin **örnekleri** veya **nesneler** adını almaktadır. Yeni bir örnek yaratma işlemine **örnekleme (instantiation)** denilir. Bir `Nokta` nesnesini örneklemek için Nokta isminde (tahmin ettiğiniz gibi) bir fonksiyon çağırırız:

```py
>>> type(Nokta)
<type 'classobj'>
>>> p = Nokta()
>>> type(p)
<type 'instance'>
```

`p` değişkeni yeni `Nokta` nesnesine bir referans olarak atanmıştır. Yeni nesneler yaratan `Nokta` şeklindeki fonksiyon **yapıcı (constructor)**dır.

## 13.3 Özellikler

Gerçek dünya nesneleri gibi, nesne örnekleri de biçim ve işlevlere sahiptir. Biçim örnek içinde yer alan veri öğelerinden oluşur.

Bir örneğe nokta işaretini kullanarak yeni veri öğeleri ekleyebiliriz:

```py
>>> p.x = 3
>>> p.y = 4
```

Bu sözdizimi, bir modülden değişken seçme işine yarayan, örneğin `math.pi` veya `string.uppercase` gibi, sözdizimi ile benzerdir. Hem modüller hem de örnekler kendi isim alanlarını (namespace) oluştururlar, ve bu içerdikleri isimlere, bunlara **özellik** adı verilmektedir, erişmek için kullanılan sözdizimleri aynıdır. Sınıflar için geçerli olan durumda, özellik bir örnekten seçtiğimiz veriyi kastetmektedir.

Aşağıdaki durum diyagramları yukarıdaki atamaların sonuçlarını göstermektedir:

![](illustrations/point.png)

`p` değişkeni bir Nokta nesnesini referans etmekte, bu nesnede iki özellik içermektedir. Her özellik bir sayıya işaret etmektedir.

Bir özelliğin değerini aynı sözdizimini kullanarak okuyabiliriz:

```py
>>> print(p.y)
4
>>> x = p.x
>>> print(x)
3
```

`p.x` ifadesinin anlamı, `p`'nin referans ettiği nesneye git ve `x`'in değerini getirdir. `x=p.x` ifadesinde, `x` isimli değişkene `p.x` değerini atıyoruz. `x` değişkeni ve `x` özelliği arasında herhangi bir çakışma yoktur. Nokta gösteriminin amacı hangi değişkeni kullandığımızı belirsizlik yaratmadan tanımlamaktır.

Nokta gösterimini herhangi bir deyimin parçası olarak kullanabilirsiniz, bu yüzden aşağıdaki cümlelerin hepsi geçerlidir:

```py
print('(%d, %d)' % (p.x, p.y))
uzaklıkKare = p.x * p.x + p.y * p.y
```

İlk satır `(3, 4)` çıktısını gösterir; ikinci satır 25 değerini hesaplar.

## 13.4 **İlkleme (initialization) metotu** ve `self`

`Nokta` sınıfımız iki boyutlu bir matematiksel noktayı temsil edeceğine göre, *tüm* nokta örnekleri `x` ve `y` özelliklerine sahip olmalıdır, ancak bu henüz bizim `Nokta` nesneleri için geçerli değildir.

```py
>>> p2 = Nokta()
>>> p2.x
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
AttributeError: Nokta instance has no attribute 'x'
>>>

```

Bu sorunu çözmek için sınıfımıza bir **ilkleme metotu** ekleriz

```py
class Nokta:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

```

## 13.5 Parametreler şeklinde örnekler

Bir örneği (burada kastedilen sınıf örneğidir-instance) olağan şekilde parametre olarak geçirebilirsiniz. Örneğin:

```py
def noktayi_yaz(p):
    print('(%s, %s)' % (str(p.x), str(p.y)))
```

`noktayi_yaz` bir noktayı argüman olarak alır ve standart bir biçimde ekranda değerini görüntüler. Eğer `noktayi_yaz(blank)` şeklinde çağrılırsa, çıktı `(3, 4)` olacaktır.

## 13.6 Aynılık

Aynı kelimesinin anlamı, üzerinde biraz düşünene kadar yeterince açıktır. Ancak bir süre sonra daha fazlasının olması gerektiğini düşünmeye başlamanız gerekiyor. 

Örneğin, Mustafa ve ben aynı arabaya sahibiz dediğinizde, bunun anlamı sizin ve Mustafa'nın arabasının aynı model ve üretim olduğu, ancak farklı iki araç olduğudur. Eğer Mustafa ve ben aynı anneye sahibiz dediğinizde, bunun anlamı ikinizin annesinin aynı kişi olduğudur.

Nesneler hakkında konuşurken, benzer bir belirsizlik sözkonusudur. Örneğin, eğer iki `Nokta` aynı ise, bunun anlamı aynı veriye (koordinatlar) sahip olmaları mı yoksa ikisinin gerçekten aynı nesne olması mıdır?

İki referansın aynı nesneyi gösterip göstermediğini anlamak için, `==` işleci kullanılır. Örneğin:

```py
>>> p1 = Nokta()
>>> p1.x = 3
>>> p1.y = 4
>>> p2 = Nokta()
>>> p2.x = 3
>>> p2.y = 4
>>> p1 == p2
False
```

`p1` ve `p2` her ne kadar aynı koordinatlara sahip olsa da, ikisi aynı nesne değildir. Eğer `p1`'i `p2`'ye atarsak, o zaman iki değişken aynı nesneyi gösterecektir:

```py
>>> p2 = p1
>>> p1 == p2
True
```

Bu tip eşitliğe **yüzeysel eşitlik (shallow equality)** denir, çünkü sadece referansları karşılaştırır, içeriği değil.

Nesnelerin içeriğini karşılaştırmak için -- **derin eşitlik** -- `ayni_nokta` isminde bir fonksiyon yazabiliriz:

```py
def ayni_nokta(p1, p2):
    return (p1.x == p2.x) and (p1.y == p2.y)
```

Eğer şimdi içeriği aynı olan iki farklı nesne yaratırsak, `ayni_nokta` metotunu kullanarak aynı noktayı temsil edip etmediklerini kontrol edebiliriz.

```py
>>> p1 = Nokta()
>>> p1.x = 3
>>> p1.y = 4
>>> p2 = Nokta()
>>> p2.x = 3
>>> p2.y = 4
>>> ayni_nokta(p1, p2)
True
```

Elbette, iki değişken de aynı nesneyi gösteriyorsa, her ikisi de hem yüzeysel hem de derin eşitliğe sahiptir.

## 13.7 Dikdörtgenler

Varsayalım ki dikdörtgeni temsil eden bir sınıf istiyoruz. Soru, bir dikdörtgeni temsil etmek için ne tür bilgiye ihtiyacımız vardır? İşi kolay tutmak için, farzedelim ki dikdörtgen sadece dikey veya yatay, açısız bir şekilde olsun.

Birkaç olasılık mevcuttur: dikdörtgenin merkezini (iki koordinat) ve boyutlarını (genişlik, yükseklik) belirtebiliriz; veya köşelerden birini ve boyutlarını belirtebiliriz; veya iki çapraz köşeyi belirtebiliriz. Geleneksel yöntem sol üst köşeyi ve boyutları belirtmektir.

Tekrar, yeni bir sınıf tanımlarız:

```py
class Dikdortgen:
    pass
```

Ve örnekleriz:

```py
box = Dikdortgen()
box.genislik = 100.0
box.yukseklik = 200.0
```

Yukarıdaki kod, iki kayan noktalı özelliğe sahip yeni bir `Dikdortgen` nesnesi yaratır. Sol üst köşeyi tanımlamak için nesne içerisine nesne gömebiliriz!

```py
box.kose = Nokta()
box.kose.x = 0.0;
box.kose.y = 0.0;
```

Nokta işareti düzeni sağlar. `box.kose.x` ifadesi `box` değişkeninin gösterdiği nesnenin `kose` isimli özelliğiyle tanımlı nesnenin `x` isimli özelliğinin değerini seç anlamına gelir.

Aşağıdaki şekilde bu nesnenin durumunu görebilirsiniz:

![](illustrations/rectangle.png)

## 13.8 Dönüş değeri olarak örnekler

Fonksiyonlar örnekleri döndürebilir. Örneğin, `merkezi_bul` bir `Dikdortgen` argümanı alır ve bu argümanın tanımladığı dikdörtgenin merkezinin koordinatlarını `Nokta` örneği olarak döndürür:

```py
def merkezi_bul(box):
    p = Nokta()
    p.x = box.kose.x + box.genislik/2.0
    p.y = box.kose.y - box.yukseklik/2.0
    return p
```

Bu fonksiyonu çağırmak için `box` değişkenini argüman olarak geçirip, sonucu bir değişkene atarız::

```py
>>> merkez = merkezi_bul(box)
>>> noktayi_yaz(merkez)
(50.0, 100.0)
```

## 13.9 Nesneler değiştirilebilir

Bir nesnenin durumunu özelliklerinden birine atama yaparak değiştirebiliriz. Örneğin bir dikdörtgenin konumunu değiştirmeden boyutlarını değiştirmek istersek, `genislik` ve `yukseklik` özelliklerini değiştirebiliriz. :

```py
box.genislik = box.genislik + 50
box.yukseklik = box.yukseklik + 100
```

## 13.10 Kopyalama

İsim takma (aliasing) programın okunabilirliğini zorlaştırabilir, çünkü bir yerde yapılan bir değişiklik başka bir yeri etkileyebilir. Bir nesneye referans veren tüm değişkenleri takip etmek zordur.

Kopyalama işlemi isim takmanın bir alternatifidir. `copy` modülü `copy` isminde bir fonksiyon içerir ve bu fonksiyon herhangi bir nesnenin kopyasını oluşturur:

```py
>>> import copy
>>> p1 = Nokta()
>>> p1.x = 3
>>> p1.y = 4
>>> p2 = copy.copy(p1)
>>> p1 == p2
False
>>> ayni_nokta(p1, p2)
True
```

`copy` modülünü içeri aktardıktan sonra, `copy` fonksiyonunu yeni `Nokta`lar üretmek için kullanabiliriz. `p1` ve `p2` aynı noktalar değildir, ancak aynı veriyi içerirler.

`Nokta` gibi basit bir nesneyi, herhangi bir gömülü nesneye sahip olmayan, kopyalamak için `copy` fonksiyonu yeterlidir. Bu **yüzeysel kopyalama**dır. 

`Dikdortgen` benzeri, içerisinde `Nokta` nesnesine referans içermektedir, sınıfları kopyalamak için `copy` bekleneni yapmayacaktır. Sadece `Point` nesnesinin referansını kopyalayacaktır, böylece eski ve yeni `Dikdortgen` nesneleri aynı `Nokta` nesnesini gösterecektir.

Eğer olağan şekilde bir `b1` kutu nesnesi oluşturup, `copy` fonksiyonu ile kopyasını oluşturursak, oluşan durum diyagramı aşağıdaki gibi olacaktır:

![](illustrations/rectangle2.png)

Bu kesinlikle bizim istediğimiz sonuç değil. Bu durumda, herhangi bir dikdörtgen nesnesinde çağırdığımız `kareyi_genislet` fonksiyonu diğer nesneyi etkileyemeyecek, ancak `konum_degistir` fonksiyonu her iki nesneyi de etkileyecektir! Bu davranış kafa karıştırıcı ve hatalara müsaittir.

Şanslıyız ki, `copy` modülü `deepcopy` isminde bir fonksiyon içermektedir. Bu fonksiyon sadece nesneyi değil, ayrıca gömülü tüm nesneleri de kopyalayacaktır. Bu işleme **derin kopyalama** denmesi sizi şaşırtmayacaktır.

```py
>>> b2 = copy.deepcopy(b1)
```

Şimdi `b1` ve `b2` tamamen farklı nesnelerdir.

`deepcopy` fonksiyonunu `kareyi_genislet` ve `konum_degistir` fonksiyonlarını değiştirmek için kullanabiliriz. Böylece bu fonksiyonlar varolan bir `Dikdortgen`i değiştirmek yerine, aynı konuma sahip fakat yeni boyutlarda yeni bir `Dikdortgen` oluşturacaktır:

```py
def kareyi_genislet(box, dwidth, dheight):
    import copy
    new_box = copy.deepcopy(box)
    new_box.width = new_box.width + dwidth
    new_box.height = new_box.height + dheight
    return new_box
```

## 13.11 Sözlük

sınıf:
: Kullanıcı tanımlı bileşik tiptir. Bir sınıf ayrıca, kendisinden oluşturulan örnekler için nesnelerin bir şablonu gibi de düşünülebilir.

örnekleme:
: Bir sınıfın bir örneğini yaratma.

örnek:
: Bir sınıfa ait olan bir nesne.

nesne:
: Gerçek dünyadaki bir şeyi veya kavramı modellemek için kullanılan bileşik veri tipidir.

yapıcı:
: Yeni nesneler yaratmak için kullanılan bir metot.

özellik:
: Bir örneği oluşturan isimlendirilmiş veri öğelerinden biri.

yüzeysel eşitlik:
: Referansların eşitliği, veya iki referansın aynı nesneyi işaret etmesidir.

derin eşitlik:
: Değerlerin eşitliği, veya iki referansın aynı değerlere sahip nesneleri işaret etmesidir.

yüzeysel kopyalama:
: Bir nesnenin içeriklerini, içerdiği gömülü nesne referansları da dahil olmak üzere, kopyalamak. `copy` modülündeki `copy` fonksiyonunda gerçekleştirilmiştir.

derin kopyalama:
: Bir nesnenin içeriklerini, içeridği gömülü nesnelerin içerikleri de olmak üzere, kopyalanmasıdır. `copy` modülündeki `deepcopy` fonksiyonunda gerçekleştirilmiştir.

## 13.12 Alıştırmalar

- Bir `Nokta` nesnesi yaratıp ekrana yazdırın, daha sonra `id` kullanarak nesnenin tekil belirtecini ekranda gösterin. Onaltılık biçimi onluk biçime çevirip ikisinin uyuştuğunu doğrulayın.

- 5. bölümdeki `uzaklik` fonksiyonunu dört sayı yerine iki `Nokta` parametresi alacak şekilde tekrar yazın.

- `kareyi_yurut` isminde ve `dx` ile `dy` isminde iki parametre alan fonksiyon yazınız. Bu fonksiyon konum değiştirmeyi, dikdörtgenin köşesinin ilgili özelliğine bu aldığı parametreleri (x'e dx, y'e dy) ekleyerek gerçekleştirmelidir.

- `konum_degistir` fonksiyonunu varolan dikdörtgeni değiştirmek yerine yeni bir `Rectangle` nesnesi oluşturup döndürecek şekilde tekrar yazın.
