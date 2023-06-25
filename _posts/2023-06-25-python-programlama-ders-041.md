---
title: Python Programlama Ders 4.1 Turtle Modülü ve Kullanımı
author: sonsuz
date: 2023-06-25 20:08:23 +0300
categories: [Program,Python]
tags: [python,ders,modül,turtle,grafik,çizim,döngü,for]
image: python-turtle.jpg
---

Kendi programlarımız içinde kullanabileceğimiz Python modülleri, oldukça
fazladır ve birçok önemli özellikler sunar. E-posta veya bir ev
sayfasının içeriğini indirmek gibi. Bu bölümde bakacağımız modül, bize
ekranda kaplumbağalar yaratmamamızı; bu kaplumbağaları kullanarak
ekranda şekiller ve desenler çizmemizi sağlayacak.

Kaplumbağalar oldukça eğlendiricidir, fakat bu bölümün gerçek amacı:
Biraz daha Python öğrenmek, hesaplamalı düşünmeyi geliştirmek veya "bir
bilgisayar bilimcisi gibi düşünmeyi" öğrenmektir. Bu bölümde işlenen
Python'un büyük bir kısmı daha sonra derinlemesine tekrar
incelenecektir.

## İlk kaplumbağa programımız

Bir kaplumbağa yaratan ve bununla bir dikdörtgen çizen birkaç satırlık
Python programı yazalım. (İlk yarattığımız kaplumbağaya atayacağımız
değişkeni `ahmet` olarak adlandıracağız. Daha önceki bölümdeki değişken
isimlendirme kurallarını kullanarak eğer istersek farklı bir isimde
seçebiliriz.)

```py
import turtle             # Kaplumbağalar yaratmamazı sağlar.
wn = turtle.Screen()      # Kaplumbağalar için bir pencere aç (oyun alanı) yaratır. 
ahmet = turtle.Turtle()    # Bir tane kaplumbağa yarat ve bunu  ahmet'e ata

ahmet.forward(50)          # ahmet'e 50 birim ilerlemesini söyle
ahmet.left(90)             # ahmet'in 90 derece dönmesini söyle
ahmet.forward(30)          # Dikdörtgenin ikinci kenarını tamamla.

wn.mainloop()             # Kullanıcının pencereyi kapatmasını bekle. 
```

Bu programı çalıştırdığınızda, aşağıdaki gibi yeni bir pencere
çıkacaktır:

![image](illustrations/tess01.png)

Bu progamı anlayabilmemiz için birkaç şeyi açıklayalım:

İlk satır bize `turtle` isimli modülü Python'a yüklememizi söyler. Bu
modül bize iki yeni farklı yeni tür kullanmamıza izin verir: `Turtle` ve
`Screen` type. `turtle.Turtle` içindeki nokta bize, *"Turtle türü
turtle modülü içinde tanımlanmıştır"* anlamını verir. ( Unutmayınız ki
Python büyük harf ve küçük harf ayrımı yapar; bu yüzden, küçük harfle
(turtle) başlayan modül ismi , büyük harfle başlayan
[Turtle] sınıf isminden farklıdır. Şansımıza
[Turtle] isimli bir modül Python'da yoktur.)

Eğer screen (ekran) denilen şeyi yaratır ve bunu açarsak (ekran yerine,
pencere demeyi tercih edeceğim), bu pencereye `wn` değişkenini atar. Her
pencerenin içinde çizim yapabileceğimiz alana **kanvas** (tuval) denir.

3'üncü satırda bir kaplumbağa oluştururuz. `ahmet` değişkeni bu
kaplumbağaya işaret eder.

Bu üç satırı halllettikten sonra, kaplumbağımıza kanvas üzerinde çizim
yaptırabiliriz.

5-7 satırlar arasında, `ahmet` **nesne**sini hareket ettiriyoruz ve
döndürüyoruz. Biz bunu yaparken `ahmet`'in **yöntem**lerini
çalıştırıyoruz (C.n: yöntemi bir fonksiyon gibi düşünebilirsiniz.) ya da
etkinleştiriyoruz. Bütün kaplumbağalar bütün bu komutlara nasıl cevap
vereceğini biliyor.

Son satırında bir amacı vardır: `wn` değişkeni yukarıda gösterilen
pencereye işaret eder. `mainloop` yöntemini etkinleştirdiğimizde,
pencere bir kullanıcıdan bir eylem bekleyen konuma girer ( bu bir
düğmeye basma, fareyi hareket ettirip, düğmeye basmak olabilir.)
Kullanıcı pencereyi kapattığında program sona erecektir.

Bir nesne farklı yöntemlere \-\-- birşey yapabilen şeyler\-\-- ve
**nitelik**lere (bazen özellik diye de isimlendirilir.) Örneğin, her
kaplumbağa bir *renk* özelliğine sahiptir. `ahmet.color("red")` ise bir
yöntem etkinleştirmesi ile, `ahmet`i ve çizimleri kırmızı yapacaktır.
(Dikkat ediniz ki [color]'un hecelenmesi Amerikan
İngilizcesi gibidir. Ç.n: İngiliz İngilizcesinde [color] ,
[colour] diye yazılır.)

Kaplumbağa'nın rengi. pencere içindeki yeri, hangi yöne baktığı ve
diğer özellikleri; kalemin çizgi genişliği gibi parçalar
kaplumbağa'nın anlık **durumu**dur. Benzer olarak, pencere nesnesinin
bir rengi, başlık çubuğunda bir ismi, büyüklüğü ve ekran üzerinde bir
yeri vardır. Bunlar, pencere nesnesinin durumunun bölümleridir.

Kaplumbağa ve pencere nesnesini değiştirmeye yarayan epeyce yöntem
vardır. Biz şimdilik birkaçını göstereceğiz. Diğer önceki örnekten
farklı olan satırları aşağıdaki programda yorumladık ( ve bu kaplumbağa
için farklı bir değişken ismi kullandık.)

```py
import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")      # Pencerenin rengini ayarla
wn.title("Hello, tamer!")      # Pencerenin başlığını ayarla

tamer = turtle.Turtle()
tamer.color("blue")            # tamer'a rengini değiştirmesini söyle
tamer.pensize(3)               # tamer'a kalem genişliğini ayarlamasını söyle

tamer.forward(50)
tamer.left(120)
tamer.forward(50)

wn.mainloop()
```

Bu programı çalıştırdığımızda yeni bir pencere ortaya çıkar ve bu
pencereyi kapatana kadar ekranda kalmaya devam eder.

![image](illustrations/tess02.png)


Bu programı genişletelim...

1. Komut satırından kullanıcıya pencerenin rengini soracak şekilde
    programı değiştirin. Kullanıcının cevabının bir değişken içinde
    saklamalı ve kullanıcının isteğine göre pencerenin rengini
    değiştirebilmelidir. (İpucu: İzin verilen renklerin isimlerini
    <http://www.tcl.tk/man/tcl8.4/TkCmd/colors.htm> adresinden
    bulabilirsiniz. Bu sayfa bazı garip isimler ile renkleri
    isimlendirmektedir. Sıcak pembe "HotPink" ve şeftali esintisi
    "peach puff")
2. Kullanıcının, ali'nin rengini değiştirebilmesine izin verecek
    benzer değişiklikleri yapın.
3. tamer'ın kaleminin genişliği için benzer değişikleri yapın.
    *Yardım:* diyalog ekranınız kullanıcıdan aldığı cevabı karakter
    dizisi olacak döndürecektir, fakat `tamer`'in `pensize` (genişlik)
    yöntemi kullanıcıdan int (tamsayı) bir değişken bekler. Bu yüzden,
    `pensize`'ın değerini kullanmadan önce onu string'den int'e
    çevirmeniz gerekecek.


## Örneklemeler - Kaplumbağa sürüleri

Bir program içinde birçok farklı tamsayı olabileceği gibi, birçok
kaplumbağa'da olabilir. Bunlardan herbirine **örnek** (instance)
denir. Her örnek'in kendine ait nitelikleri (özellikleri ) ye
yöntemleri vardır. Böylece, `ahmet` siyah ince bir kalem ile çizebilir
ve kanvas üzerinde bir konum üzerinde olabilir, bunun gibi `tamer`'de
kalın bir pembe ile kendi yönünde gidebilir.

```py
import turtle
wn = turtle.Screen()         # Pencereyi ve özelliklerini oluştur.
wn.bgcolor("lightgreen")
wn.title("Ahmet ve Tamer")

tamer = turtle.Turtle()       # tamer'i ve ona ait özellikleri oluştur.
tamer.color("hotpink")
tamer.pensize(5)

ahmet = turtle.Turtle()       # ahmet'i oluştur. 

tamer.forward(80)             # tamer'e eşkenarlı üçgen çizdir.
tamer.left(120)
tamer.forward(80)
tamer.left(120)
tamer.forward(80)
tamer.left(120)               # üçgen'i tamamla.

tamer.right(180)              # tamer'i kendi çevresinde 180 derece döndür.  
tamer.forward(80)             # onu origin'den uzaklaştır. 

ahmet.forward(50)             # ahmet'e kare çizdir. 
ahmet.left(90)
ahmet.forward(50)
ahmet.left(90)
ahmet.forward(50)
ahmet.left(90)
ahmet.forward(50)
ahmet.left(90)

wn.mainloop()
```

Aşağıdaki şekil, `ahmet`'in dikdörtgeni tamamladığında ve `tamer`'ın
da üçgeni tamamladığındaki resmi göstermektedir.

![image](illustrations/tess03.png)

Burda bazı *Bir bilgisayar bilimcisi gibi nasıl düşünülür* gözlemleri:

- Bir tam çemberde 360 derece vardır. Bir kaplumbağ'nın yaptığı
    bütün dönüşleri bir araya getirirsek, *dönüşler sırasında hangi
    adımlar olmuşsa olsun*, biz kolayca bunların 360 derecenin katları
    olup olmadığını anlayabiliriz. `ahmet` ilk anda yaratıldığında hangi
    yöne işareti ediyorsa, en son halinin de aynı yöne işaret ettiğini
    bize gösterir. Geometri'nin geleneklerine göre, oluşturulan
    kaplumbağaların yönleri doğuya 0 derece yönlenir.
- `ahmet`'in son dönüşünü yapmayabilirdik, fakat bu pek tatmin edici
    olmayabilirdi. Eğer bize kare veya dikdörtgen gibi kapalı şekiller
    çizilmesi sorulursa, başladığı ilk durumdaki yöne bakması ve bütün
    dönüşlerini tamamlamış olması iyi bir fikirdir. Bu, küçük
    programların büyük programlara çevrilmesinı ve bu programların
    insanlar tarafından daha kolay anlaşılmasını sağlar.
- `tamer` ile aynısını yaptık: O, bir üçgen çizdi ve 360 derece tam
    dönüş yaptı. Daha sonra kendi çevresinde 180 derece döndürdük ve onu
    kenera çektik. 18'inci satır bile programcının akıl yürütmesi
    hakkında bir verir. Daha geniş anlamda, `tamer`'in üçgen çizme
    eylemi (12-17 satırlar) ve başlangıç noktasından uzaklaşması ( 19 ve
    20'inci satırlar ) biraraya toplanmıştır.
- Programdaki yorumlar kullanılmasının başlıca nedeni düşünce yapımızı
    ve büyük fikirlerimizi kaydetmektir. Bunlar her zaman kodun içinde
    açık olmayabilir.
- Sürünüz için iki kaplumbağa yeterli olmayabilir. Burdaki önemli
    fikir: İhtiyacınız olduğu kadar kaplumbağ yaratabilmeniz için,
    turtle modülü size bir fabrika verir. Her örneklemenin kendisine ait
    durum ve davranışları vardır.

## *for* döngüsü

Bir kare çizmek bile, oldukça sıkıcıydı. Hareket etme ve dönme
adımlarını dörtkere açıkça tekrar etmek zorunda kaldık. Eğer bir
altıgen, sekizgen veya 42 kenarı olan bir poligon çizmek isteseydik, bu
çok daha kötü olurdu.

Bir kodu alıp onu tekrar ettirmek (döngüye koymak) programların temel
yapı taşıdır.

Python'un **for** döngüsü bunu bizim için çözer. Örneğin,
arkadaşlarımızın herbirini partimize davet edecek bir e-posta göndermek
istiyoruz. Henüz nasıl e-posta göndereceğimizi bilmiyoruz, şimdilik
herbir arkadaşımız için bir mesajı ekranda yazacağız.

```py
for f in ["Ahmet","Aysun","Burak","Ayşe","Zeki","Temel","Perihan"]:
    davet = "Merhaba " + f + ".  lütfen Cumartesi günü partime gelin."
    print(davet)
# daha fazla kod buraya eklenebilir. 
```

Bu kodu çalıştırdığımızda, aşağıdaki çıktı gibi olur:

```py
Merhaba Ahmet.  lütfen Cumartesi günü partime gelin.
Merhaba Aysun.  lütfen Cumartesi günü partime gelin.
Merhaba Burak.  lütfen Cumartesi günü partime gelin.
Merhaba Ayşe.  lütfen Cumartesi günü partime gelin.
Merhaba Zeki.  lütfen Cumartesi günü partime gelin.
Merhaba Temel.  lütfen Cumartesi günü partime gelin.
Merhaba Perihan.  lütfen Cumartesi günü partime gelin. 
```

- 1'inci satırdaki `for`'un önündeki `f` değişkenine **döngü
    değişkeni** denir. Biz burada değişken olarak `f` harfini kullandık,
    siz isterseniz bir başka harf veya kelime de kullanabilirsiniz.
- 2\. ve 3. satırlar **döngü gövdesini** oluşturur. Döngü gövdesi her
    zaman girintili yazılır. Herbir girinti, gövde içindeki her bir
    satırı tam olarak belirler.
- Herbir *tekrar*'da veya döngüyü her *geciş*'te ilk yapılan şey,
    işlenecek madde kalıp kalmadığını kontrol etmektir. Eğer işlenecek
    hiçbir madde kalmamış ise (bu **sonlandırma koşulu** olarak
    isimlendirilir) döngü sonlandırılır. Program yürümeye gövde
    bitiminden sonraki satırlardan devem eder( bu durumda, 4'üncü
    satırdaki yorumdan sonraki satır.)
- Eğer daha işlenecek maddeler varsa, listede sonra gelen maddeye
    işaret edecek şekilde döngü değişkeni güncellenir. Bu durum şu
    anlama gelir: Döngü gövdesi üzerinden 7 kez yürü ve her yürümede `f`
    değişkeni farklı bir arkadaşa atamasını yap.
- Döngünün içindeki gövde üzerinden her yürüme sonunda, Python `for`
    deyimine geri döner. Daha fazla madde kalıp kalmadığı kontrol
    edilir; eğer listenin içinde işlenecek daha madde varsa, f değişkeni
    sonraki maddeye işaret eder.

## For döngüsünün yürütme akışı

Program çalışırken, Python hangi çümlenin işleneceğini takip eder. Biz
buna programın **yürütme akışı**nın **kontrol akışı** diyeceğiz.
insanlar programı çalıştırdıklarında, sıradaki her bir cümleye
parmağıyla işaret eder. Kontrol akışını, "Python'un hareket eden
parmağı" olarak düşünebilirsiniz.

Şimdiye kadar program akışının yukarıdan aşağıya doğru satır satır
olduğunu görmüştük. `For` döngüsü bunu değiştirir.

### *for* döngüsünün akış diyagramı

Eğer bir akış diyagramı çizersek, kontrol akışını gözünde canlandırmak
ve anlamak daha kolay olur. Bu şekil, `for` deyiminin kesin
basamaklarını ve nasıl yürüdüğünü göstermektedir.

![image](illustrations/flowchart_for.png)

### Döngü bizim kaplumbağa programımızı basitleştirir

Bir kare çizmek için, aynı şeyi dört kere yapmamız
gerekebilir, kaplumbağayı hareket ettir ve döndür. `ahmet`'in bir
karenin dört kenarını çizmesini sağlamak için 8 satır yazdık. Yalnızca 3
satır kullanarak, aynı şeyi yapabiliriz.

```py
for i in [0,1,2,3]
    ahmet.forward(50)
    ahmet.left(90)
```

Bazı gözlemler:

- Bazı satırlardan tasarruf etmemiz kolaylık olmasına rağmen, bu çok
    önemli değildir. Bundan çok daha önemlisi, kendini tekrarlayan bir
    kalıp bulduk ve kalıbı tekrar kullanmak için programımızı yeniden
    düzenledik. Bu kalıpları bulmak ve bu kalıplar etrafında
    programımızı düzenlemek hesaplamalı düşünmede can alıcı yetenektir.

- \[0,1,2,3\] değerleri döngü gövdesinin 4 kere yürütülmesi için
    verilmiştir. Biz herhangi dört değerde kullanabilirdik, fakat bunlar
    genelde kullanılan değerlerdir. Gerçekte o kadar yaygındırlar ki,
    Python'un kendine ait `range` fonksiyonu vardır.

    ```py
    for i in range(4):
        # i=0, sonra 1, sonra 2 ve 3 için gövde yürütülür (çalıştırılır.) 
    for x in range(10):
        #  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]'ın herbir değerini x'e atar. 
    ```

- Bilgisayar programcıları saymaya 0'dan başlamayı severler.

- `range` fonksiyonu, `for` içideki döngü değişkeni için bir değerler
    dizisi oluşturur. Her zaman 0'dan başlarlar ve yurakıdaki durumlar
    için 4 ve 10'u bu diziye dahil etmezler.

- `ahmet`'in en son dünüşünde 360 dereceyi tamamlaması için
    yaptığımız küçük kurnazlık bize şimdi karşılığını verdi. Eğer bunu
    yapmamış olsaydık, karenin dördüncü kenarı için döngüyü kullanamamış
    olacaktık. Diğer kenarlardan farklı bir durum oluşacaktı. Mümkün
    olduğunca kodumuzu özel bir durum için değil, genel bir motife
    uyacak şekilde yazmaya çalışmalıyız.

Birşeyi dört kere tekrar etmek için, iyi bir Python programcısı şunu
yapacaktı:

```py
for i in range(4):
    ahmet.forward(50)
    ahmet.left(90)
```

`tamer'in` de eşkenar üçgen çizmesi için `for` döngüsünü de
kullanabilir. Bu programda hangi değişikleri yapmanız gerektiğini
görebilmeniz gerekir.

Fakat şimdilik, eğer aşağıdaki değişikliği yapsaydanız, ne görürdünüz.

```py
for c in ["yellow", "red", "purple", "blue"]:
    ahmet.color(c)
    forward(50)
    ahmet.left(90)
```

Değişken listeye de atanabilir. Böylece listeler yalnızca `for` döngüsü
için değil, daha genel durumlar için kullanılabilir. Yukarıdaki kode şu
şekilde yazılabilir:

```py
# değişken atanmış listelerde çalışma
clrs = ["yellow", "red", "purple", "blue"]   
for c in clrs:
    ahmet.color(c)
    ahmet.forward(50)
    ahmet.left(90)
```

## Birkaç tane daha kaplumbağa yöntemleri (fonksiyonları)

Kaplumbağa yöntemleri negatif açı veya uzaklık kullanabilir. Örneğin,
`tamer.forward(-100)` tamer'i geriye doğru hareket ettirecek ve
`tamer.left(-30)` ise tamer'i sağ döndürecektir. Ayrıca, bir çemberde
360 derece olduğundan, onu 30 derece sola döndürmek, `tamer`'i aynı
yöne çevirecek ve bu sanki onu 330 derece sağ'a çevirmek ile aynı
anlama gelecektir (Ekrandaki canlandırmayı kullanarak, `tamer`'in saat
yönününde mi yoksa saat yönünün tersin de mi hareket ettiğini
söyleyebileceksiniz.)

Bu size, hem sağa hem de sola dönme yöntemlerinin ikisine birden
ihtiyacınız olmadığını aklınıza getirir. Aynı zamand `backward` yöntemi
de vardır (Eğer biraz uçuk iseniz, `ahmet.backward(-100)` komutunu
`ahmet`'i ileriye hareket ettirmek için kullanabilirsiniz).

Bizim konumuzda yapıyı ve aralarındaki bağlantıları daha iyi anlamak,
*Bilgisayar bilimcisi gibi düşünmenin* bir parçasıdır. Eğer
kaplumbağalar ile oynayacaksak, geometri ve sayı düzlemi hakkında basit
temel konulara bir göz atmak; sol, sağ, ileri, geri, negatif ve pozitif
açılar arasındaki bağlantıları farketmek iyi bir başlangıç olabilir.

Kaplumbağ kalemi çizgi çizmek için kullanabileceği gibi( pendown: kalem
aşağı) , isterse kullanmayabilir de (penup: kalem yukarı) . Bu,
kaplumbağanın çizgi çizmeden başka yerlere hareket etmesine olanak
verir. Bu yöntemler:

```py
ahmet.penup()          # kalem kaldırıldı.
ahmet.forward(100)     # Çizgi çizilmeden ahmet'i hareket ettirir.
ahmet.pendown()        # kalem yeniden konuldu. 
```

Her kaplumbağaya farklı bir şekil verebiliriz. Halihazırda tanımlanmış
yöntemler: `arrow`, `blank`, `circle`, `classic`, `square`, `triangle`,
`turtle` bunlardan birkaçıdır.

```py
ahmet.shape("turtle")           
```

![image](illustrations/alex06.png)

Kaplumbağanın canlandırmasını (animasyon) hızlandırabilir veya
yavaşlatabiliriz ( Canlandırma, kaplumbağanın ne kadar hızlı döneceğini
veya ileri hareket edeceğini kontrol eder.) Hızlandırma ayarlamaları 1
(en yavaş) ve 10 (en hızlı) arasında ayarlanabilir. Eğer biz hızı 0'a
ayarlarsak, bunun özel bir anlamı vardır: Canlandırma yapma ve en hızlı
gidebileceğin kadar hızlı git.

```py
ahmet.speed(10)
```

Kaplumbağa kendi ayakizini kanvas üzerinde oluşturabilir ve başka bir
yere hareket ettiğinde bu ayakizi kalacaktır. Kalem yukarı (penup) olsa
bile, iz bırakma çalışır.

Bu yeni özellikleri gösteren bir örnek yapalım:

```py
import turtle
wn = turtle.Screen()             
wn.bgcolor("lightgreen")
tess = turtle.Turtle()            
tess.shape("turtle")
tess.color("blue")

tess.penup()                # kalem kaldırma özelliği
size = 20
for i in range(30):
   tess.stamp()             # tuvalde izlenim bırak
   size = size + 3          # her döngüde arttır
   tess.forward(size)       # tessle hareket et 
   tess.right(24)           #  ...  ve döndür

wn.mainloop()  
```

![image](illustrations/tess07.png)

Dikkatli olun! Kaçkere döngü gövdesi yürütüldü? Ekranda kaç tane
kaplumbağa resmi görüyorsunuz. Bir tanesi hariç bütün ekranda
gördüğünüz kaplumbağa izleri `stamp` yönergesi tarafından
oluşturulmuştur. Fakat program yalnızca bir tane kaplumbağa örneklemesi
içerir. Hangisinin gerçek `tess` olduğunu bulabilir misiniz? (İpucu:
Eğer emin değilseniz, `for` döngüsünden sonra `tess`'in rengini
değiştiren bir satırlık kod yazın; veya kalemi aşağıya indiren ve çizgi
çizen, veya onun şeklini değiştiren bir kod yazın.)

## Sözlük

nitelik, özellik (attribute)
:   Belirli bir nesneye ait olan durum veya özellik. Örneğin, `tamer`
    bir renge sahiptir. Renk burda `tamer` nesnesinin bir özelliğidir.

kanvas (tuval)
:   Çizimin gerçekleştiği pencere yüzeyi

kontrol akışı
:   Sonraki bölümdeki *yürütme akışına* bakınız.

for döngüsü
:   Döngü içindeki gövdede bulunan ifadeleri tekrarlamayı kolaylaştıran
    Python deyimi.

döngü gövdesi
:   Döngü içinde içeriye girintilenmiş ifadeler. Döngü içindeki
    ifadelerin içeriye doğru girintilenmesi, bir gruplandırmayı ifade
    eder.

döngü değişkeni
:   `for` döngüsü içinde kullanılan değişken. Döngü'nün herbir
    tekrarında farlı bir değere işaret eder.

örnek
:   Bir sınıfa ait olan nesne. `ahmet` ve `tamer` kaplumbağa sınıfının
    farklı örnekleridir.

yöntem
:   Bir nesne ile ilişiklendirilen fonksiyon. Bir yöntemi çağırıldığında
    veya etkinleştirildiğinde, nesne buna karşılık verir. Örneğin,
    `tess.forward(100)` dediğimizde, `forward` bir yöntemdir.

çağırmak
:   Bir nesneye ait yöntemler vardır. [Çağırmak] fiilini
    kullanarak, bu yöntemi etkinleştirdiğimizi ifade ederiz. Bir yöntemi
    çağırmak için, yöntemden sonra, içinde bir komut içeriği olan bir
    çift parantez [()] koyarız. Örneğin `tamer.forward()`,
    `forward` yönteminin çağırılmasıdır.

modül
:   Diğer Python programları içinde kullanılmak amacıyla Python
    tanımlamaları ve komutlarını tutan dosya. `import` deyimi
    kullanarak, modül'ün içeriği diğer programlara açık hale getirilir.

nesne
:   Bir değişkenin işaret edebileceği `şey.` Bu bir ekran penceresi veya
    yarattığımız bir kaplumbağa olabilir.

range (aralık)
:   Bir tamsayı dizisi yaratmak için Python'da tanımlanmış fonksiyon.
    Bir ifadeyi belirli bir sayıda yürütmek istediğimizde, yazdığımız
    `for döngüsü` için yararlı bir fonksiyondur.

sonlandırma koşulu
:   Bir döngü içindeki gövdedeki ifadelerin yürütmesini durduran
    koşuldur. Örneğin bu koşul; Bu bölümde gördüğümüz `for döngüsü`
    içinde, döngü değişkenine artık atayacağımız daha fazla madde
    kalmadığında oluşur.

## Alıştırmalar

1. `Biz Python'un kaplumbağlarından hoşlanırız` cümlesini 1000 kere
    yazan program yazınız.

2. Cep telefonunuza ait 3 tane özellik ve 3 tane yöntem veriniz.

3.  

    Aşağıdaki çıktıyı yazan `for döngüsü` yazın:

    :   | `Ocak yılın bir ayıdır.`
        | `Şubat yılın bir ayıdır.`
        | \...

4. `tamer` kaplumbağınız yüzünü doğuya doğru 0 derecee ile çevirmiş
    olsun. Eğer `tamer.left(3645)` komutu verirsek, `tamer` ne yapar ve
    hangi yöne doğru bakar?

5. `xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]` şeklinde bir atama
    yaptığınızı düşünelim.

    a.  Herbir sayıyı yeni bir satırda ekrana yazdıran bir döngü yazın.
    b.  Herbir sayıyı ve onun karesini yeni bir satırda ekrana yazdıran
        bir döngü yazınız.
    c.  Listedeki bütün sayıları toplayıp, sonucu `toplam`
        değişkenine atayan bir döngü yazınız. Bu sayıları toplamadan
        önce `toplam` değişkenini 0 sayısına atayın. Döngü
        tamamlandıktan sonra, `toplam`'ı yazdırın.
    d.  Listedeki bütün sayıların çarpımlarını yazdırın.

6. Aşağıdaki düzgün çokgenleri `for` döngüsü kullanarak kaplumbağaya
    çizdiriniz ( düzgün çokgen her kenarı ve her açısı aynı olan
    demektir.)

    - Eşkenar üçgen
    - Kare
    - Altıgen
    - Sekizgen

7.  #### Sarhoş Korsan Problemi
    Bir sarhoş korsan rastgele bir dönüş yapıyor ve 100 adım atıyor;
    daha sonra yeniden rastgele dönüş yapıyor ve 100 adım atıyor; ve bu
    böyle devam ediyor. Bir sosyal bilim öğrencisi, 100 adım alınmadan
    herbir dönüş öncesi bu açıları kaydediyor. Onun deneysel veriler:
    `[160, -43, 270, -97, -43, 200, -940, 17, -86]`. Kaplumbağayı
    kullanarak sarhoş arkadaş tarafından alınan yolu çiziniz.
    

8. Yukarıdaki programı zenginleştirin: Sarhoş korsan etrafta
    gezindikten sonra, yöneldiği yönü söyleyen bir program yazınız (
    Onun 0 dereceden başladığını farzedin.)

9. Eğer 18 kenarı olan bir düzgün çokgen çizerseniz, kaplumbağa her
    köşede kaç derecelik bir açıyla dönmelidir?

10. Aşağıdaki herbir satırı, Python'un etkileşimli komut satırından
    girerek ne yapacağını tahmin ediniz ve sonucu kaydediniz:

    ``` python3
    import turtle
    wn = turtle.Screen()
    tess = turtle.Turtle()
    tess.right(90)
    tess.left(3600)
    tess.right(-90)
    tess.speed(10)
    tess.left(3600)
    tess.speed(0)
    tess.left(3645)
    tess.forward(-100)
    ```

11. Aşağıdaki şekli çizen bir Python programı yazınız:

    ![image](illustrations/star.png)

    İpucu:

    - Cep telefonunuzu sanki bir kaplumbağaymış gibi bir kağıt
        parçası üzerinde hareket ettirip, döndürün. Yıldızı tamamlamadan
        önce, telefonunuzun kaçkere tam dönüş yaptığını gözlemleyiniz.
        Herbir tam dönüş 360 derece olduğundan, cep telefonunuzun kaç
        derece döndürüldüğünü bulabilirsiniz. Yıldızda 5 köşe
        olduğündan, bunu beşe bölerseniz kaplumbağanızı her köşede kaç
        derece döndürdüğünüzü bulabilirsiniz.
    - Eğer kaplumbağanızın görünmesini istemiyorsanız onu görünmez
        yapabilirsiniz. Eğer kalem aşağıda ise hala çizim yapmaya devam
        edecek. Bu yöntem `tamer.hideturtle()` ile çağrılır.
        Kaplumbağayı yeniden görünür yapmak istiyorsanız,
        `tamer.showturtle()`'ı kullanın.

12. Yukarıdaki programı genişletin. Beş tane yıldız çizin. Herbir
    yıldızdan sonra; kalemi yukarı kaldırın ( kalemi etkisizleştirin),
    kalemi 144 derece sağa döndürün ve 350 birim ileri götürün, kalemi
    aşağıya koyun, yeniden bir yıldız çizin. Şekliniz aşağıdaki gibi
    olsun:

    ![image](illustrations/five_stars.png)

13. Aşağıdaki şekle benzer bir yüz çizecek program yazınız.

    ![image](illustrations/tess_clock1.png)

14. Bir kaplumbağa yaratınız ve bu kaplumbağayı bir değişkene
    atayınız. Bu değişkenin tipini komut satırından sorunuz. Ne cevap
    alıyorsunuz?
