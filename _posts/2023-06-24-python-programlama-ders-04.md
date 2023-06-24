---
title: Python Programlama Ders 4. Koşul ifadeleri ve Karşılaştırmalar
author: sonsuz
date: 2023-06-24 20:08:23 +0300
categories: [Program,Python]
tags: [python,koşul,karşılaştırma,modül,turtle,ders,modül,boolean,mantık]
---



## 4.1 Modül (Kalan) işleci

**Modül işleci** tamsayılarla (ve tamsayı deyimlerle) çalışan ve ilk işlenen ikinci işlenene bölünmesiyle oluşan kalanı veren bir işleçtir. Python'da, modül işleci yüzde işareti(`%`)'dir. Sözdizimi diğer işleçlerle aynıdır:

```py
>>> bolum = 7 // 3
>>> print(bolum)
2
>>> kalan = 7 % 3
>>> print(kalan)
1
```

7'yi 3 ile tam böldüğümüzde sonuç 2, ve kalan 1'dir.

Modül işlecinin faydalı olduğunu görebilirsiniz. Örneğin bir sayının bir başka sayı ile bölünebilir olup olmadığını -- `x % y` sıfıra eşit ise `x` `y` ile bölünebilirdir-- sınayabilirsiniz.

Ayrıca sayının en sağ basamağındaki rakam veya rakamları elde edebilirsiniz. Örneğin, `x % 10` deyimi `x` sayısının en sağındaki rakamı (onluk sisteme göre) üretir. Benzer olarak `x % 100` en sağdaki iki rakamı döndürür.

## 4.2 Boolean değerler ve deyimler

Python'da doğru ve yanlış değerleri saklamak için kullanılan tipe `bool` adı verilmektedir, bu isim (tüm dillerde olduğu gibi) *Boolean Cebir*ini yaratan İngiliz matematikçi George Boole'dan dolayı verilmiştir. Boole cebiri tüm modern bilgisayar aritmetiğinin temelidir.

Sadece iki **boolean değer** vardır: `True`(doğru) ve `False`(yanlış). Python açısından büyük harfle başlamaları önemlidir. `true` ve `false` boolean değerler değildir.

```py
>>> type(True)
<type 'bool'>
>>> type(true)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'true' is not defined
```

**Boolean deyim**i, boolean değer şeklinde değerlendirilen (sonucu boolean değer olan) bir deyimdir. `==` işleci iki değeri karşılaştırıp boolean değer üretir:

```py
>>> 5 == 5
True
>>> 5 == 6
False
```

İlk cümlede, iki işlenen eşittir, bu yüzden deyim `True` sonucunu üretir; ikinci cümlede ise 5, 6'ya eşit değil, bu yüzden `False` sonucu elde ederiz. `==` işleci **karşılaştırma işleçleri**nden biridir; diğerleri şunlardır:

```py
x != y               # x, y'e eşit değil
x > y                # x, y'den büyük
x < y                # x, y'den küçük
x >= y               # x, y'den büyük veya eşit
x <= y               # x, y'den küçük veya eşit
```

Her ne kadar bu işlemler size tanıdık gelse de, Python tarafından kullanılan işaretler matematiksel işaretlerden farklıdır. En çok karşılaşılan hata çift eşit işareti (`==`) yerine tek eşit (`=`) işaretini kullanmaktır. Unutulmaması gereken `=` işareti atama işlecidir ve `==` karşılaştırma işlecidir. Ayrıca `=<` ve `=>` işaretleri tanımlı değildir.

## 4.3 Mantıksal işleçler

Üç adet **mantıksal işleç** vardır: `and` (ve), `or` (veya), ve `not` (değil). Bu işleçlerin anlamları, parantez içinde yazılmış olan Türkçe anlamlarıyla benzerdir. Örneğin `x > 0 and x < 10` ifadesi sadece `x` 0'dan büyük *ve* `x` 10'dan küçük olduğunda doğrudur.

`n % 2 == 0 or n % 3 == 0` ifadesi iki koşuldan biri doğru olduğunda (veya'dan dolayı)doğrudur. Bunun anlamı sayı 2 ile bölünebilir *veya* 3 ile bölünebildiğinde doğrudur.

Son olarak, `not` işleci bir boolean deyimin zıttını (negatifi) üretmede kullanılır. Böylece `not(x > y)` ifadesi `(x > y)` ifadesi yanlış olduğunda doğru olacaktır. Bu ifade `x` `y`'den daha küçük veya eşit olduğunda doğrudur.

## 4.4 Koşullu yürütme (if)

Yararlı programlar yazabilmek için, neredeyse her zaman koşulları sınamamız ve programın davranışlarını bu sınamaların sonucuna göre değiştirebilmemiz gerekir. **Koşul cümleleri** bize bu yeteneği kazandırır. En basit örneği **`if` cümlesidir**:

```py
if x > 0:
    print("x pozitiftir")
```

`if` cümlesinden sonra yazılmış olan boolean deyim'e **koşul** adı verilir. Eğer bu koşul doğru ise alttaki cümle çalışır. Eğer değilse, herhangi bir şey olmaz.

`if` cümlesinin sözdizimi şu şekildedir:

```py
if BOOLEAN DEYIM:
    CUMLELER
```

Bir önceki bölümde gördüğümüz fonksiyon tanımlaması ve diğer bileşik cümleler gibi, `if` cümlesi bir başlık ve gövdeden oluşur. Başlık `if` anahtar kelimesi ile başlar ve bir *boolean deyim*le devam eder. Sonu yine iki nokta üstüste (:) ile belirlenmiştir.

Takip eden girintili cümlelere **blok** adı verilir. İlk girintisiz cümle bloğun sonunu belirler. Bileşik cümlelerdeki cümle bloğuna cümlenin **gövde**si adı verilir.

Gövdedeki her bir cümle eğer boolean deyim doğruysa (`True`) sırasıyla yürütülür. Eğer boolean deyim yanlışsa (`False`) bütün blok yoksayılır ve çalıştırılmaz.

`if` cümlesinin gövdesinde bulunabilecek cümle sayısında bir sınır yoktur, ama en azından bir cümlenin olması gerekir. Bazen boş if cümlesi yazmak (mesela daha sonra yazmak üzere alanı ayırmak için) gerekebilir. Bu durumda `pass` cümlesini - ki bu cümle hiç bir şey yapmaz - kullanabilirsiniz.

```py
if True:          # Bu her zaman dogrudur
    pass          # bu cumle her zaman yurutulecektir,ancak bir sey yapmamaktadir
```

## 4.5 Alternatif yürütme (if, else)

`if` cümlesinin bir biçimi de alternatif yürütmeye imkan sağlayan, iki yürütme olasılığı sağlayan ve buna koşulun sonucuyla karar veren cümledir. Sözdizimi şu şekildedir:

```py
if x % 2 == 0:
    print(x, "çifttir")
else:
    print(x, "tektir")
```

Eğer `x` sayısının 2 ile bölünmesinden kalan 0 ise, `x`'in çift olduğunu biliriz, ve program bunu bize bildiren bir mesaj yazar. Eğer koşul yanlış ise (x'in 2'ye bölümünden kalan 0 değil ise) `else`'in altındaki cümleler çalışacaktır. Her halükarda boolean deyimi doğru veya yanlış olabileceğine göre bu iki alternatif yürütmeden biri mutlaka çalışacaktır. Bu alternatiflere **dal**(yol - branch) adı verilmektedir, çünkü yürütme akışındaki farklı dalları temsil ederler.

Şu ana kadar söylediklerimizi bir kenara bırakırsak, eğer sayıların çift veya tek olduğunu kontrol etmek isterseniz, yukarıdaki kodu bir fonksiyon içerisine koymak(wrap) isteyebilirsiniz:

```py
def print_parity(x):
    if x % 2 == 0:
        print(x, "çifttir")
    else:
        print(x, "tektir")
```

`x`'in herhangi bir değeri için `print_parity` fonksiyonu uygun mesajı gösterecektir. Fonksiyonu çağırdığınızda, argüman olarak herhangi bir tamsayı değer gönderebilirsiniz.

```py
>>> print_parity(17)
17 tektir.
>>> y = 41
>>> print_parity(y+1)
42 çifttir.
```

## 4.6 Zincirleme koşul ifadeleri (if, elif, else)

Bazen ikiden fazla olasılık vardır ve iki dallanmadan fazlasına gereksinim duyarız. Bunun gibi bir hesaplamayı ifade etmek için **zincirleme koşul ifadeleri**ni kullanırız:

```py
if x < y:
    print(x, "küçüktür", y)
elif x > y:
    print(x, "büyüktür", y)
else:
    print(x, "ve", y, "eşittir")
```

`elif` else if'in bir kısaltmasıdır. Daha öncede olduğu gibi sadece bir dal (yol) yürütülecektir. `elif` cümlelerinin sayısında bir sınırlama yoktur ancak sadece bir adet (isteğe bağlı olmak üzere) `else` cümlesine izin vardır ve bunun son cümle (son dal) olması gereklidir:

```py
if choice == 'a':
    function_a()
elif choice == 'b':
    function_b()
elif choice == 'c':
    function_c()
else:
    print("Yanlış seçim.")
```

Her koşul sırasıyla sınanır. Eğer ilki yanlış ise, sonraki kontrol edilir, ve bu böyle gider. Eğer koşullardan biri doğru ise, ilgili dal yürütülür ve cümlenin işlevi biter. Eğer birden fazla koşul doğru olsa bile, sadece ilk karşılaşılan doğru dal çalışır.

## 4.7 İçiçe koşul deyimleri

Bir koşul deyimi bir başka koşul deyimiyle **içiçe** olabilir. Üç kısma bölünen örneğimizi aşağıdaki gibi yazabilirdik:

```py
if x == y:
    print(x, "ve", y, "eşittir")
else:
    if x < y:
        print(x, "küçüktür", y)
    else:
        print(x, "büyüktür", y)
```

Dışarıdaki koşul deyimi iki dal içermektedir. İlk dal bir adet basit bir görüntüleme cümlesi içerir. İkinci dal başka bir `if` cümlesi içerir ve bu cümle iki dal barındırır. Bu iki dalda basit görüntüleme cümleleridir, bunlar ayrı koşul cümleleri de olabilirlerdi.

Her ne kadar cümlelerin girintisi yapıyı düzgün bir şekilde gösterse de, içiçe koşul deyimleri hızlı bir şekilde okunması zor deyimlerdir. Genellikle bu tür deyimlerden mümkün olduğunca kaçınmak gerekir.

Mantıksal işleçler içiçe koşul cümlelerini basitleştirmek için bir yöntem sağlarlar. Örneğin aşağıdaki kodu tek bir koşul cümlesiyle yazabilirsiniz:

```py
if 0 < x:
    if x < 10:
        print("x pozitif ve tek basamaklıdır.")
```

`print` cümlesi sadece iki koşulu da geçersek çalışır, bu yüzden bu örnekte `and` işlecini kullanabiliriz:

```py
if 0 < x and x < 10:
    print("x pozitif ve tek basamaklıdır.")

```

Bu tip koşullar sık kullanılır ve Python bunlar için matematiksel gösterime benzeyen alternatif biz sözdizimi sağlar:

```py
if 0 < x < 10:
    print ("x pozitif ve tek basamaklıdır.")
```

Bu koşul cümlesi yukarıdaki bileşik boolean deyimi ve içiçe koşul cümlesiyle aynı anlambilimine sahiptir.

## 4.8 Geri dönüş (`return`) cümlesi

`return` cümlesi bir fonksiyonun sona ulaşmadan bitirilmesini sağlar. Bu cümleyi kullanmanın bir nedeni bir hata durumuyla karşılaşmanız olabilir:

```py
def print_square_root(x):
    if x <= 0:
        print("Sadece pozitif sayılar lütfen.")
        return

    result = x**0.5
    print("x'in kare kökü", result)
```

`print_square_root` fonksiyonu `x` isimli bir parametreye sahiptir. İlk yaptığı işlem bu parametrenin (`x`) 0'dan küçük veya eşit olduğunu sınamaktır. Eğer 0 veya daha küçük ise (negatif) bir hata mesajı verip fonksiyonu sonlandırıp ve çağrıldığı yere dönmektedir, bunu `return` cümlesi ile yapmaktadır. Yürütme akışı hemen çağıran yere geri döner ve fonksiyonun geri kalan satırları çalıştırılmaz.

Fonksiyonların geriye değer döndürmesi kısmında return daha da detaylı anlatılacaktır.

## 4.9 Klavye girdisi

[2.](python-programlama-ders-02) Bölümde Python tarafından sağlanan ve klavyeden girdi almamızı sağlayan fonksiyonlarını görmüştük: `input()` Şimdi bu fonksiyonu ve kullanımlarını derinlemesine inceleyeceğiz.

Bu fonksiyonun herhhangi birisi çağrıldığında, program durup kullanıcının klavyeden bir şey girmesini bekler. Kullanıcı Giriş (Enter) tuşuna bastığında program çalışmasına devam eder ve `input()` kullanıcının girdiğini `karakter dizisi (string)` olarak döndürür:

```py
>>> my_input = input()
Ne için bekliyorsun?
>>> print(my_input)
Ne için bekliyorsun?
```

`input()` fonksiyonunu çağırmadan önce, kullanıcıya ne girmesi gerektiğini açıklayan bir mesaj göstermek faydalıdır. Bu mesaja **bilgi istemi (prompt)** adı verilir. `input()` fonksiyonuna bilgi istemini argüman olarak aktarabiliriz:

```py
>>> name = input("İsmin nedir? ")
İsmin nedir? Arthur, İngilizlerin kralı!
>>> print(name)
Arthur, İngilizlerin kralı!
```

Farkettiğiniz üzere bilgi istemi bir karakter dizisidir, bu yüzden tırnak işaretleri arasında alınmalıdır.

Eğer kullanıcının yanıtının tamsayı olmasını istiyorsak, yanıtı Python deyimi olarak değerlendiren `input()` fonksiyonun önünde `int()` ifadesi ile kullanabiliriz:

```py
prompt = "Yüksüz bir kırlangıcın havadaki hızı nedir?\n"
speed = int(input(prompt))
```

Eğer kullanıcı rakamlardan oluşan bir karakter dizisi girdiğinde, bu girdi bir tamsayıya dönüştürülüp `speed` değişkenine atanacaktır. Ancak eğer kullanıcı geçerli bir Python deyimi girmezse program hata verecektir:

```py
>>> speed = int(input(prompt))
Yüksüz bir kırlangıcın havadaki hızı nedir?
Neyi kastediyorsun, Afrika mı yoksa Avrupa kırlangıcı mı?
...
ERROR!
Traceback (most recent call last):
  File "<string>", line 3, in <module>
ValueError: invalid literal for int() with base 10: 'Neyi kastediyorsun, Afrika mı yoksa Avrupa kırlangıcı mı?'
```

Son örnekte kullanıcı eğer bir tam sayı ifade girseydi hata oluşmayacaktı.

```py
>>> speed = int(input(prompt))
Yüksüz bir kırlangıcın havadaki hızı nedir?
45
>>> speed
45
```

Bu tür hatalardan uzak durmak için karakter dizisini almak üzere `input()` fonksiyonunu kullanmak ve diğer tiplere dönüşümü komutları kullanarak yapmak daha uygun bir yöntemdir.

## 4.10 Tip dönüşümü

Her Python tipi için tanımlı bu tipi diğer tiplere dönüştürmeye yarayan bir yerleşik komut vardır. Örneğin `int(ARGUMAN)` komutu, herhangi bir değeri alıp eğer yapılabiliyorsa tamsayıya (int) dönüştürür veya hata mesajı üretir:

```py
>>> int("32")
32
>>> int("Merhaba")
ValueError: invalid literal for int() with base 10: 'Merhaba'
```

`int` ayrıca kayan noktalı değerleri tamsayılara çevirebilir, fakat unutulmaması gereken bu çevirme işleminde kesir kısmını kaldıracağıdır:

```py
>>> int(-2.3)
-2
>>> int(3.99999)
3
>>> int("42")
42
>>> int(1.0)1

```

`float(ARGUMAN)` komutu tamsayı ve karakter dizilerini kayan noktalı sayılara çevirir:

```py
>>> float(32)
32.0
>>> float("3.14159")
3.14159
>>> float(1)
1.0
```

Python'un tamsayı olan `1` ve kayan noktalı sayı olan `1.0`'ı birbirinden farklı değerlendirmesi garip gelebilir. İkisi aynı değeri temsil edebilir ama farklı tiptedirler. Bunun nedeni bilgisayarda farklı şekillerde temsil edilmeleridir.

`str(ARGUMAN)` herhangi bir argümanı karakter dizisine (`string`) çevirir:

```py
>>> str(32)
'32'
>>> str(3.14149)
'3.14149'
>>> str(True)
'True'
>>> str(true)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'true' is not defined
```

`str(ARGUMAN)` herhangi bir değerle çalışabilir ve o değeri karakter dizisine çevirir. Daha önce de bahsedildiği gibi `True` boolean bir değerdir, ancak `true` değildir.

Boolean değerler için durum özellikle ilgi çekicidir:

```py
>>> bool(1)
True
>>> bool(0)
False
>>> bool("Ni!")
True
>>> bool("")
False
>>> bool(3.14159)
True
>>> bool(0.0)
False
```

Python boolean değerleri diğer tiplerin değerlerine atar. Sayısal değerler için (tamsayı ve kayan noktalı sayılar) sıfır değerler yanlıştır ve diğer değerler doğrudur. Karakter dizileri için boş diziler yanlıştır, diğerleri ise doğrudur.

## 4.11 Turtle

Öncelikle Turtle kütüphanesini projemize import turtle yazarak dahil etmemiz gerekir. Daha sonra `turtle.Turtle()` fonksiyonu çağırılarak, grafiksel ekran karşımıza çıkacaktır.

Örnek;

```py
import turtle

tosbaga = turtle.Turtle()
tosbaga.forward(100)
```

Yukarıdaki kodları yazdıktan sonra aşağıda vereceğim Turtle Kütüphanesini fonksiyonlarını kullanarak çalışmalar oluşturabilirsiniz.

### 4.111 Turtle da kullanılan bazı fonksiyonlar

Fonksiyon adı-kullanımı Açıklaması

forward(100)
: 100 birim ileri çizgi çiz

backward(50)
: 50 birim geri çizgi çiz

left(60)
: 60 derece sola dön

right(90)
: 90 derece sağa dön

pensize(10)
: Kalem ucu kalınlığını 10 birim yap

color(“red”,”yellow”)
: Çizgi rengini kırmızı, dolgu rengini sarı yap

begin_fill()
: Boyamayı başlat

end_fill()
: Boyamayı bitir

circle(50) : 50 birimlik daire çiz
speed(1)
: turtle hızını ayarla(1 yavaş-10 hızlı)

penup()
: kalemi kaldır

pendown()
: kalemi bastır

goto(100,200)
: pencere de x =100 ,y =200 koordinatına git

clear()
: ekranı temizle

shape()
: Çiziciyi değiştirir. Seçenekler “arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”.

Turtle modülünü bilgisayar programlama kavramlarını görselleştirmek ve öğrenirken eğlenmek için kullanacağız.

## 4.12 Sözlük

modül işleci:
: Yüzde işaretiyle temsil edilen (`%`) ve tamsayılar üzerinde çalışıp, birbirine bölünen iki sayının bölmede kalanını üreten işleçtir.

boolean değer:
: Sadece iki adet boolean değer vardır: `True` ve `False`. Boolean değerler Python yorumlayıcısı tarafından değerlendirilen bir boolean deyim sonucunda oluşurlar. `bool` tipindedirler.

boolean deyim:
: Sonucu doğru veya yanlış olan deyim

karşılaştırma işleci:
: İki değeri karşılaştıran işleçlerdir: `==`, `!=`, `>`, `<`, `>=`, ve `<=`.

mantıksal işleç:
: Boolean deyimleri birleştiren işleçlerdir: `and`, `or`, ve `not`.

koşul cümlesi:
: Koşullara göre yürütme akışını kontrol eden cümlelerdir. Python'da `if`, `elif`, ve `else` anahtar kelimeleri koşul cümleleri için kullanılmaktadır.

koşul:
: Koşul cümlesindeki boolean deyimdir, ve hangi dalın (yolun) yürütüleceğine karar verir.

blok:
: Aynı girintiye sahip ardışık cümleler grubudur.

gövde:
: Bileşik cümledeki başlığı takip eden cümle bloğudur.

dal:
: Koşul cümlesi sonucu belirlenen yürütme akışındaki olası yollardan biridir.

zincirleme koşul ifadesi:
: İkiden fazla yürütme akışı olasılığına sahip koşul dallanmasıdır. Python'da zincirleme koşul ifadeleri `if ... elif ... else` cümleleri şeklinde yazılmaktadır.

içiçe geçme:
: Bir program yapısının bir başka program yapısı içerisinde bulunmasıdır, örnek olarak bir koşul cümlesinin bir başka koşul cümlesi dallanması içerisinde bulunmasını verebiliriz.

bilgi istemi:
: Kullanıcıya veri girmesini söyleyen görsel ipuçu

tip dönüşümü:
: Bir tipteki değeri alıp başka bir tip değerine dönüştüren cümle.

## 4.13 Alıştırmalar

- Aşağıdaki nümerik ifadeleri kafanızdan değerlendirmeye çalışın, daha sonra Python yorumlayıcısı yardımıyla bulduğunuz sonuçları karşılaştırın:

1. `>>> 5 % 2`

2. `>>> 9 % 5`

3. `>>> 15 % 12`

4. `>>> 12 % 15`

5. `>>> 6 % 6`

6. `>>> 0 % 7`

7. `>>> 7 % 0`

Son örnekte ne oldu? Neden? Bilgisayarın yanıtı sizi tatmin ettiyse ve anlayabildiyeseniz ilerleyebilirsiniz. Eğer böyle bir şey sözkonusu değilse kendi kendinize örnekleri yapmanız gerekir. Modül işlecini anladığınıza emin olana kadar araştırmaya devam etmelisiniz.

- Fonksiyon yardımıyla karşılaştırma

```py

if x < y:
    print(x, "küçüktür", y)
elif x > y:
    print(x, "büyüktür", y)
else:
    print(x, "ve", y, "eşittir")

```

Bu kodu `compare(x,y)` fonksiyonu içine *koyun*(wrap). `compare` fonksiyonunu üç kere, ilk argümanın küçük olduğu, ilk argümanın büyük olduğu ve iki argümanın eşit olduğu, çağırın.

- Boolean deyimleri daha iyi anlamak için, doğruluk tabloları üretmek yararlıdır. İki boolean deyim ancak ama ancak aynı doğruluk tablosuna sahipse *mantıksal olarak eşit*tir.


Aşağıdaki Python betiği p ve q değişkenlerine sahip herhangi bir boolean ifadesinin doğruluk tablosunu görüntüler:

```py
print(" p \t q \t p and q")
print("="*24)
for p in True, False:
    for q in True, False:
        print(" {}\t {} \t".format(p,q),p and q )

print("\n p \t q \t p or q")
print("="*24)
for p in True, False:
    for q in True, False:
        print(" {}\t {} \t".format(p,q),p or q )
```

Bu betiğin nasıl çalıştığını ileriki bölümlerde öğreneceksiniz. Şimdilik bu betiği boolean ifadeleri anlamak için kullanacağız. Bu programı `p_and_q.py` isimli bir dosyaya yazıp kaydedelim, daha sonra komut satırından çalıştıralım ve `p or q` ifadesini bilgi isteminde bulunduğu zaman verelim. Aşağıdaki gibi bir çıktıyla karşılaşmanız gerekiyor:

```py
 p       q       p and q
========================
 True    True    True
 True    False   False
 False   True    False
 False   False   False

p        q       p or q
========================
 True    True    True
 True    False   True
 False   True    True
 False   False   False

```

- Aşağıdaki deyimleri Python kabuğuna giriniz:

```py
True or False
True and False
not(False) and True
True or 7
False or 7
True and 0
False or 8
"mutlu" and "üzgün"
"mutlu" or "üzgün"
"" and "üzgün"
"mutlu" and ""

```

Sonuçları çözümleyin. Farklı tiplerin değerleri ve mantıksal işleçler ile ilgili olarak ne tür gözlemleriniz var? Bu gözlemleri basit `and` ve `or` deyimleri şeklindeki *kurallar* halinde yazabilir misiniz?

- Karşılaştırmalar için fonksiyon çağırmalı alıştırma

```py
if choice == 'a':
    function_a()
elif choice == 'b':
    function_b()
elif choice == 'c':
    function_c()
else:
    print("Hatalı seçim.")

```

Bu kodu `dispatch(choice)` fonksiyonu içerisine yerleştirelim. Daha sonra `function_a`, `function_b` ve `function_c` fonksiyonlarını yazarak bu fonksiyonların çağrıldığını ekranda gösterelim. Örneğin:

```py
def function_a():
    print("function_a() çağrıldı...")

```

Fonksiyonları (`dispatch`,
`function_a`, `function_b`, ve
`function_c`) `ch4prob4.py` isimli bir betik içerisine koyun. Bu betiğin en altına `dispatch('b')` çağrısını ekleyin. Programı çağırdığınızda çıktınız şu şekilde olmalıdır:

```py

function_b çağrıldı...

```

Son olarak betiği değiştirerek kullanıcının 'a', 'b', veya 'c' girebileceği şekile getirin. Python kabuğunda içe aktararak betiği sınayın.

- `is_divisible_by_3` fonksiyonu yazın. Bu fonksiyon tek bir tamsayı argüman alsın ve eğer argüman üç ile bölünebiliyorsa "Bu sayı üç ile bölünebilir" mesajını ekranda göstersin. Eğer bölünemeyen bir sayı ise "Bu sayı üç ile bölünemez" mesajını ekranda göstersin. 

Benzer şekilde `is_divisible_by_5` fonksiyonunu yazın.

- Bir önceki alıştırmada yazdığınız fonksiyonları `is_divisible_by_n(x,n)` şeklinde iki tamsayı argüman alan ve ilk argümanın ikinci argüman tarafından bölünüp bölünemediğini sınamak üzere genelleştirin.


- Aşağıdakinin çıktısı ne olacaktır?

```py

if "Ni!":
    print('We are the Knights who say, "Ni!"')
else:
    print("Stop it! No more of this!")

if 0:
    print("And now for something completely different...")
else:
    print("What's all this, then?")

```

Ne olduğunu ve neden olduğunu açıklayın.

- turtle modülünü kullanarak bir ev çizin

- Kullanıcıdan üç sayı isteyin ve büyükten küçüğe yazdırın.

- Kullanıcıya notunu sorun. 50 den büyükse geçtin, 50 den küçükse kaldın yazdırın.

- Suyun sıcaklığını sorun, 0 dan küçükse katı, 0-100 arasında sıvı, 100 den büyükse gaz yazdırın.

- Kullanıcıdan bir sayı girmesini isteyin. Bu sayı tek mi çift mi yazdırın.

- Kullanıcıya 3 adet tamsayı kenar girmesini isteyin. Girilen kenarlara göre üçgen olup olmadığı, üçgense ne tür bir üçgen olduğu yazdırın. (eşkenar, ikizkenar, dikkenar, çeşitkenar) (üçgen olma kuralı, her hangi iki kenarın toplamı diğer kenardan büyük olmalı, bütün kenarlar için geçerli, dik kenar üçgen olması için de iki kenarın kareleri toplamı diğer kenarın karesine eşit olmalı, bir durum sağlansa yeterli)
