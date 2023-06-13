---
title:  Python Programlamaya Giriş 16 – Dize biçimlendirme
author: sonsuz
date: 2023-06-14 01:25:37 +0300
categories: [Program,Python]
tags: [python,dize,biçim,metod]
---






*Python Programlamaya Giriş* dizimizin [bir önceki bölümünde](https://sonsuzus.github.io/posts/python-programlamaya-giris-15-dize-metodlari) dizelerle yapılabilecek işlemleri ve yaygın dize metodlarını özetledik. Bu yazıda dize metodlarından biri olan `format()` ile dize biçimlendirmeyi daha ayrıntılı işleyeceğiz. Dizinin bütün yazılarına erişmek için [*Python Programlamaya Giriş*](https://sonsuzus.github.io/categories/python) kategorimize bakabilirsiniz. 

Birçok durumda bir değişkende barındırılan bir değeri uygun bir biçimde düzenleyerek ekrana basmamız gerekir. Bu düzenlemeler ve biçimlendirmeler örneğin şöyle olabilirler:

* Bir kalıp dize içindeki boşlukları doldurmak, `İsim:...., Yaş:....` gibi.
* Sayıları ondalıktan sonra sabit sayıda basamakla vermek: `9.340, -18.731` gibi.
* Sayıları sıfırlarla doldurmak: `099.45, 001.12` gibi.
* Tablo halinde basılan listeleri hizalı olarak, belli boşluklar ayırarak basmak.
* Tablo içeriklerini sağa veya sola yaslamak, ortalamak.

Bu tür düzenlemeler için Python’da kapsamlı bir mini-dil mevcut. Bu tür düzenlemeler, `format()` metoduyla beraber şu şekilde kullanılır:

```py
"<kalıp dizesi>".format(<değerler>)




```

Dize biçimlendirmenin bütün ayrıntıları için [Python belgelerine](https://docs.python.org/3/library/string.html#formatstrings) bakabilirsiniz.

## Konumla yerleştirme ve isimle yerleştirme

En basit kullanımda, `format()`‘a verilen değerler, kalıp dizesinin içinde küme parantezleri (`{}`) ile bırakılan boşluklara sırayla yerleştirilir.

In [1]:

```py
"İsim: {}, Telefon: {}, Boy: {} m".format("Kaan", "5555", 1.80)


```

Out[1]:

```py
'İsim: Kaan, Telefon: 5555, Boy: 1.8 m'
```

Yukarıdaki örnekte birinci boşluğa birinci değer (`"Kaan"`), ikinci boşluğa ikinci değer (`"5555"`), üçüncü boşluğa da üçüncü değer (1.80) yerleştirildi. Bu sırayı değiştirmek için, küme parantezlerinin içine arzu ettiğimiz konum numaralarını koyabiliriz.

In [2]:

```py
"İsim: {0}, Boy: {2} m, Telefon: {1}".format("Kaan", "5555", 1.80)


```

Out[2]:

```py
'İsim: Kaan, Boy: 1.8 m, Telefon: 5555'
```

Başka bir yol da, yer tutuculara isim vermek ve `format()`‘a bu isimlerle parametreler vermektir.

In [3]:

```py
"Alıcı Adı: {isim}, Yaşı: {yaş}, Şehir: {şehir}".format(yaş=32, isim="Fatma", şehir="Tekirdağ")


```

Out[3]:

```py
'Alıcı Adı: Fatma, Yaşı: 32, Şehir: Tekirdağ'
```

Örneklerden gördüğümüz gibi, `format()` fonksiyonu kalıp dizesindeki boşluklarla değerleri eşleştirirken, fonksiyonlardaki [parametre eşleştirme](https://sonsuzus.github.io/posts/python-programlamaya-giris-fonksiyon-parametreleri) kurallarını kullanıyor. İlk gördüğümüz örnek *konumla eşleştirmeye* denk iken, son örneğimiz *isimle eşleştirme* yapıyor.

Bu sebepten, fonksiyon çağrılarındaki *parametre çözme* kuralları da aynen uygulanabilir. Mesela:

In [4]:

```py
p = ("Kaan","5555",1.80)

"İsim: {}, Telefon: {}, Boy: {} m".format(*p)


```

Out[4]:

```py
'İsim: Kaan, Telefon: 5555, Boy: 1.8 m'
```

Biraz daha gelişkin bir örnek olarak, önceden hazırlanmış bir veri listesi üzerinden döngü çalıştıralım.

In [5]:

```py
liste = [

("Kaan","5555",1.80),

("Meral","5628",1.50),

("Ziya","9879",1.40)]

for p in liste:

    print("İsim: {0}, Boy: {2} m, Telefon: {1}".format(*p))


```

```py
İsim: Kaan, Boy: 1.8 m, Telefon: 5555

İsim: Meral, Boy: 1.5 m, Telefon: 5628

İsim: Ziya, Boy: 1.4 m, Telefon: 9879


```

Verileri çokuzlar olarak değil de sözlük olarak saklıyor olabiliriz. O zaman sözlüklerde kullandığımız parametre çözme yöntemi geçerli olur.

In [6]:

```py
D = dict(isim="Filiz", yaş=55, şehir="İstanbul")

"Alıcı Adı: {isim}, Yaşı: {yaş}, Şehir: {şehir}".format(**D)


```

Out[6]:

```py
'Alıcı Adı: Filiz, Yaşı: 55, Şehir: İstanbul'
```

In [7]:

```py
liste = [

{"isim": "Filiz", "yaş":"55", "şehir":"İstanbul"},

{"isim": "Meral", "yaş":"40", "şehir":"Ankara"},

{"isim": "Ziya", "yaş":"10", "şehir":"Bursa"}

]

for D in liste:

    print("Alıcı Adı: {isim}, Yaşı: {yaş}, Şehir: {şehir}".format(**D))


```

```py
Alıcı Adı: Filiz, Yaşı: 55, Şehir: İstanbul

Alıcı Adı: Meral, Yaşı: 40, Şehir: Ankara

Alıcı Adı: Ziya, Yaşı: 10, Şehir: Bursa


```

`format()`‘a verilen parametre bir liste veya sözlük ise, kalıp dizesinde indeksleme uygulanabilir.

In [8]:

```py
listem = [3,6,7,9]

"İlk eleman: {0[0]}, son eleman: {0[3]}".format(listem)


```

Out[8]:

```py
'İlk eleman: 3, son eleman: 9'
```

In [9]:

```py
kayıt = {"isim":"Kaan", "boy":1.80, "telefon":"5555"}

"İsim: {D[isim]}, Tel: {D[telefon]}, Boy: {D[boy]}".format(D=kayıt)


```

Out[9]:

```py
'İsim: Kaan, Tel: 5555, Boy: 1.8'
```

## Yana yaslama ve ortalama

Dizeleri biçimlendirirken, alt alta olan dizelerin belli bir hizada olmasını sağlamak isteyebiliriz. Bunun için, dizenin basılacağı yerde kaç karakterlik alan ayrılacağını belirlememiz, sağa veya sola yaslamamız, veya ortalamamız mümkündür.

Önce hizalama yapılmayan bir örnek görelim:

In [10]:

```py
isimler = ["Ziya", "Meral", "Hüsamettin", "Zebercet"]

yaşlar = [9, 32, 45, 28]

şehirler = ["İstanbul", "Ankara", "Van", "Diyarbakır"]



for i, y, ş in zip(isimler, yaşlar, şehirler):

    print("Alıcı Adı: {}, Yaşı: {}, Şehir: {}".format(i, y, ş))


```

```py
Alıcı Adı: Ziya, Yaşı: 9, Şehir: İstanbul

Alıcı Adı: Meral, Yaşı: 32, Şehir: Ankara

Alıcı Adı: Hüsamettin, Yaşı: 45, Şehir: Van

Alıcı Adı: Zebercet, Yaşı: 28, Şehir: Diyarbakır


```

Kalıp dizesinde yer tutucuları (mesela) `{:10}` biçiminde yazmakla 10 karakter genişlikte bir alan ayırmış oluruz. Aksi belirtilmedikçe dizeler sola, sayılar ise sağa yaslanır.

In [11]:

```py
for i, y, ş in zip(isimler, yaşlar, şehirler):

print("Alıcı Adı: {:11} Yaşı: {:3} Şehir: {:10}".format(i, y, ş))


```

```py
Alıcı Adı: Ziya        Yaşı:  9 Şehir: İstanbul

Alıcı Adı: Meral       Yaşı: 32 Şehir: Ankara

Alıcı Adı: Hüsamettin  Yaşı: 45 Şehir: Van

Alıcı Adı: Zebercet    Yaşı: 28 Şehir: Diyarbakır


```

Sola yaslanmış olarak basmak için `{:<10}`, sağa yaslanmış olarak basmak için `{:>10}`, ortalanmış olarak basmak içinse `{:^10}` yazımı kullanırız.

In [12]:

```py
for i, y, ş in zip(isimler, yaşlar, şehirler):

    print("Alıcı Adı: {:>11} Yaşı: {:<3} Şehir: {:^10}".format(i, y, ş))


```

```py
Alıcı Adı:        Ziya Yaşı: 9  Şehir:  İstanbul

Alıcı Adı:       Meral Yaşı: 32 Şehir:   Ankara

Alıcı Adı:  Hüsamettin Yaşı: 45 Şehir:    Van

Alıcı Adı:    Zebercet Yaşı: 28 Şehir: Diyarbakır


```

Boş bırakılan yerleri bir karakterle doldurmak istiyorsak, bu karakteri `:` işaretinden hemen sonra koyarız. Mesela, `*` işaretiyle doldurmak için:

In [13]:

```py
for i in isimler:

     print("{:*>11}".format(i))


```

```py
*******Ziya

******Meral

*Hüsamettin

***Zebercet


```

Yer tutucuları indeksle veya isimle eşleştirmek istediğimizde, iki nokta üstüste işaretinden önce indeksi veya ismi yazarız; `{0:10}` veya `{isim:10}` gibi.

In [14]:

```py
for i, y, ş in zip(isimler, yaşlar, şehirler):

     print("{1:3} yaşındaki {0:11} isimli alıcı {2:10} şehrinde oturuyor.".format(i, y, ş))


```

```py
 9 yaşındaki Ziya        isimli alıcı İstanbul   şehrinde oturuyor.

32 yaşındaki Meral       isimli alıcı Ankara     şehrinde oturuyor.

45 yaşındaki Hüsamettin  isimli alıcı Van        şehrinde oturuyor.

28 yaşındaki Zebercet    isimli alıcı Diyarbakır şehrinde oturuyor.


```

In [15]:

```py
for i, y, ş in zip(isimler, yaşlar, şehirler):

    print("{yaş:3} yaşındaki {isim:11} isimli alıcı {şehir:10} şehrinde oturuyor.".format(isim=i, yaş=y, şehir=ş))


```

```py
 9 yaşındaki Ziya        isimli alıcı İstanbul   şehrinde oturuyor.

32 yaşındaki Meral       isimli alıcı Ankara     şehrinde oturuyor.

45 yaşındaki Hüsamettin  isimli alıcı Van        şehrinde oturuyor.

28 yaşındaki Zebercet    isimli alıcı Diyarbakır şehrinde oturuyor.


```

Genel olarak, kalıp dizesindeki yer tutucunun içinde `:` işaretinin solunda eşleştirme bilgisi (indeks veya isim) yer alır; sağında ise o değerin nasıl biçimlendirileceğinin bilgisi bulunur.

## Sayı biçimlendirme

Yer tutucu içine bir sayı koyacağımız zaman, tamsayılarda `{:d}`, ondalıklı sayılarda ise `{:f}` kodlarını kullanırız.

In [16]:

```py
"Yaş: {:d}, Boy: {:f}".format(42, 1.76)


```

Out[16]:

```py
'Yaş: 42, Boy: 1.760000'
```

Belli miktarda, söz gelişi 5 karakterlik yer ayırmak için `{:5d}` yazımını kullanabiliriz. Ondalıklı sayılar için `{:5.2f}` yazımı, noktadan sonra 2 basamak olmak üzere en az 5 karakterlik yer ayrılmasını sağlar (ondalık noktası dahil). Türkçeye uygun olarak virgüllerle ayırma yöntemi için bir sonraki bölüme bakın.

In [17]:

```py
"Yaş: {:5d}, Boy: {:5.3f}".format(42, 1.76)


```

Out[17]:

```py
'Yaş: 42, Boy: 1.760'
```

Ayırdığımız alanda, sayının değerini değiştirmeden boşlukların sıfırlarla doldurulmasını istiyorsak `{:05d}` veya `{05.3f}` gibi yazımlar kullanırız.

In [18]:

```py
"Yaş: {:05d}, Boy: {:06.3f}".format(42, 1.76)


```

Out[18]:

```py
'Yaş: 00042, Boy: 01.760'
```

Negatif sayıların başına her zaman eksi gelir; pozitif sayıların da her zaman artı ile başlaması için `{:+d}` yazımını kullanırız.

In [19]:

```py
"{:+d}, {:+d}".format(42, -45)


```

Out[19]:

```
'+42, -45'
```

Bir sayıyı ikili, sekizli, onaltılı tabanda göstermek için sırasıyla `b`, `o`, `x` kullanırız.

In [20]:

```py
print("Onluk tabanda {:d}\nİkili tabanda {:b}\nSekizli tabanda {:o}\nOnaltılı tabanda {:x}".format(42,42,42,42))


```

```
Onluk tabanda 42

İkili tabanda 101010

Sekizli tabanda 52

Onaltılı tabanda 2a


```

Bu dönüşümleri yapınca sayının tabanının da belli olmasını istersek `#b`, `#o`, `#x` kullanırız. Bu kodlar sayının başına sırasıyla `"0b"`, `"0o"`, `"0x"` konmasını sağlar.

In [21]:

```py
print("Onluk tabanda {:d}\nİkili tabanda {:#b}\nSekizli tabanda {:#o}\nOnaltılı tabanda {:#x}".format(42,42,42,42))


```

```py
Onluk tabanda 42

İkili tabanda 0b101010

Sekizli tabanda 0o52

Onaltılı tabanda 0x2a


```

Büyük sayıları virgülle üçer basamaklı ayırmak için `{:,}` kullanırız (Türkçeye uygun olarak noktalarla ayırmak için sonraki bölüme bakın).

In [22]:

```py
"{:,}".format(123456789)


```

Out[22]:

```py
'123,456,789'
```

Ondalıklı sayıları göstermek için şu kodlar kullanılabilir:

* `{:f}` veya `{:F}` (fixed): Ondalıktan sonra sabit sayıda basamak (varsayılan 6).
* `{:e}` veya `{:E}` (exponential): Sayıyı bilimsel notasyonda gösterir; üsteli `"e"` veya `"E"` harfinden sonra koyar.
* `{:g}` veya `{:G}` (genel): Yerine göre `f` veya `e`. Belirli bir basamak sayısını (varsayılan 6) verecek şekilde yuvarlar; sayının büyüklüğüne göre `f` veya `e` biçimine getirir.
* `{:%}`: Sayıyı 100 ile çarpar ve sonuna yüzde işareti koyar.

In [23]:

```py
x = 12345.6789

print("Sabit biçim: {:f}, {:F}".format(x,x))

print("Üstel biçim: {:e}, {:E}".format(x,x))

print("Genel biçim: {:g}, {:G}".format(x,x))


```

```py
Sabit biçim: 12345.678900, 12345.678900

Üstel biçim: 1.234568e+04, 1.234568E+04

Genel biçim: 12345.7, 12345.7


```

In [24]:

```py
x = 12345.6789

print("Sabit biçim: {:4.2f}, {:4.4F}".format(x,x))

print("Üstel biçim: {:1.3e}, {:1.4E}".format(x,x))

print("Genel biçim: {:.10g}, {:.2G}".format(x,x))


```

```py
Sabit biçim: 12345.68, 12345.6789

Üstel biçim: 1.235e+04, 1.2346E+04

Genel biçim: 12345.6789, 1.2E+04


```

Yüzdeleri gösterirken `%` kodunu kullanabiliriz.

In [25]:

```py
geçen = 57

başvuran = 245

"Başarı oranı {:.2%}".format(geçen/başvuran)


```

Out[25]:

```py
'Başarı oranı 23.27%'
```

## Sayıları Türk standartlarında biçimlendirmek

Yukarıdaki örneklerde, Amerikan standardına uygun olarak, sayı grupları virgülle ayrıldı ve ondalık için nokta kullanıldı. Oysa Türkiye’deki sayı yazma standartlarında sayı grupları noktayla ayrılır, ondalık için ise virgül kullanılır. Türk standartlarına uygun biçimlendirme yapmak için biraz dolaylı bir yoldan gidip, yerelleştirme işlemleri için kullanılan `locale` kütüphanesini kullanmamız gerekir.

In [26]:

```py
import locale

loc = locale.getlocale()

locale.setlocale(locale.LC_ALL,"tr_TR.UTF-8")


```

Out[26]:

```
'tr_TR.UTF-8'
```

Yerelleştirme ayarlarını yapsak da, bu ayarlar `str.format` metodunu etkilemeyecektir. Bunun yerine, `locale.format` fonksiyonunu kullanmalıyız. Bu fonksiyonun dize biçimleme sintaksı [eski usül](https://docs.python.org/2/library/stdtypes.html#string-formatting) olarak bilinir. Basit bir örnek olarak:

In [27]:

```py
locale.format("%f", 1234567.89, grouping=True)


```

Out[27]:

```
'1.234.567,890000'
```

Şimdi de virgülden sonra 3 hane olmak üzere toplam 13 karakterlik yer ayırarak biçimlendirelim.

In [28]:

```py
locale.format("%013.3f", 1234567.89, grouping=True)


```

Out[28]:

```
'001.234.567,890'
```

`locale.format()` sadece bir tek biçim dizesi alır (`%f` veya `%d` gibi). Daha geniş bir kalıp kullanmak için `locale.format_string()` fonksiyonunu kullanmamız gerekir.

In [29]:

```py
isimler = ["Ziya", "Meral", "Hüsamettin", "Zebercet"]

boylar = [1.42, 1.50, 1.74, 1.81]

maaşlar = [100.73, 5555.62, 12446.43, 2300.12]



for i, b, m in zip(isimler, boylar, maaşlar):

    print(locale.format_string("İsim: %-12s Boy: %6.2f Maaş: %10.2f", (i,b,m), grouping=True))


```

```py
İsim: Ziya Boy: 1,42 Maaş: 100,73

İsim: Meral Boy: 1,50 Maaş: 5.555,62

İsim: Hüsamettin Boy: 1,74 Maaş: 12.446,43

İsim: Zebercet Boy: 1,81 Maaş: 2.300,12


```

Ne yazık ki `locale.format_string()` sadece daha sınırlı olan eski usül biçimlendirme sintaksıyla çalışıyor. Yine de, ileri Python sürümlerinde yeni usule geçilmesi muhtemeldir.

Sayıların biçimlerini yerelleştirmeyi, son kullanıma yönelik raporlar üretme amacıyla sınırlı tutmanız iyi olur. Bu amaç dışında, mesela veriler bir dosyaya yazıp sonradan okumayı hedefliyorsanız yerel ayarları değil varsayılan ayarları (Amerikan standardını) kullanın. Dosyadaki verilerde, söz gelişi, ondalıklar virgülle ayrılmışsa, sonradan veri dosyasını okumakta sorunlar yaşayabilirsiniz. Yazılım paketlerindeki otomatik araçların çoğu Amerikan tarzı sayı yazımını temel alır. Bunun etrafından dolaşmak mümkündür ama hem dolambaçlıdır hem de sorunlara gebedir.

## Nesne içi değişkenleri kullanmak

Nesnelerin iç değişkenleri (“attributes”) kalıp dizede kullanılabilir. Örneğin, karmaşık sayıların gerçek kısımları `real`, sanal kısımları `imag` isimli iç değişkenlerde saklanır.

In [30]:

```py
z = 3+2j

z.real, z.imag


```

Out[30]:

```py
(3.0, 2.0)
```

Dize biçimlendirmede bu iç değişkenlerin isimlerini doğrudan kullanabiliriz.

In [31]:

```py
"Gerçek kısım {0.real}, sanal kısım {0.imag}".format(3+2j)


```

Out[31]:

```py
'Gerçek kısım 3.0, sanal kısım 2.0'
```
