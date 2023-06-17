---
title:  Bilimsel Programlamaya Kolay Başlangıç – 2
author: sonsuz
date: 2023-06-18 01:15:12 +0300
categories: [Program,Python,Bilim]
tags: [bilim,fizik,eğit atış,euler yöntemi,matplotlib,python,programlama]
math: true
---







Bilimsel Programlamaya Kolay Başlangıç serisinin ilk yazısında sadece grafikler için `matplotlib` kütüphanesini kullanarak serbest düşüş problemini modellemiş ve sonuçları grafiklerle görselleştirmiştik. Vesileyle, “fonksiyonları ne zaman nerede kullanmak gerekir” sorusuna da bir başlangıç yapmıştık.

İlk yazıda Bilimsel Programlama 3 adımdan oluşur dedik, ama aslında birçok problemde dört adımdan bahsetmek mümkün:

1. Hazırlık (Sabitleri başlatma, gerekirse veri yapılarını oluşturma vb.)
2. Hesaplama
3. Veri Analizi (Hesaplama sonuçlarını gerçek veriler ya da başka bir modelle karşılaştırma, diğer bir deyişle Hata ya da Fark Analizi)
4. Sonuçları Görselleştirme

Bu yazıda öncelikle eğik atış problemini çözeceğiz ve sayısal yöntemlerin ne kadar başarılı olduğuna bakacağız. Elimiz değmişken sınıf (class) yapılarının nasıl kullanıldığına dair de basit bir örnek yapmış olacağız.

Eğik atış problemi iki eksende çözülüyor, yatay eksen x ve düşey eksen y.

İki eksendeki konum değişimi şu şekilde gösterilebilir:  

$t$ anında yatay eksendeki konum: $ r_x(t) = r_x(0) + v_x(0) t $  

$t$ anında düşey eksendeki konum: $ r_y(t) = r_y(0) + v_y(0) t – \frac{1}{2} g t^2 $

İki eksendeki hız değişimi ise şu şekilde gösterilebilir:  

$t$ anında yatay eksendeki hız: $ v_x(t) = v_x(0) $  

$t$ anında düşey eksendeki hız: $ v_y(t) = v_y(0) – g t $

Parametreler ise şöyle:  

$r_x(t), r_y(t) = $ x ve y ekseninde konum vektörü bileşenleri ($m$)  

$v_x(t), v_x(t) = $ x ve y ekseninde hız vektörü bileşenleri ($m/s$)  

$g = $ yerçekimi sabiti (9.81 $m/s^2$)  

$t = $ zaman ($s$)

Formüllerin bize anlatmak istediği şey şu:

1. Cisim yatay eksende başlanıç hızında gitmeye devam eder
2. Cisim düşey eksende başlangıç hızında başlar, hızı yerçekimi ivmesiyle orantılı olarak düşey yönde değişir ve sonuçta düşmeye başlar.

“Bu kadar matematik yeter” diyorsanız, kodlama işine başlayalım o zaman. Öncelikle basit bir vektör sınıfı oluşturalım. Bu sınıf zaman, yatay ve düşey konum ile yatay ve düşey hız bileşenlerinden oluşuyor.

In [1]:

```py
class zamanKonumHız:

   'Zaman, 2D konum ve 2D hız değerlerini içeren vektör sınıfı'

   t = 0

   rx, ry = 0, 0

   vx, vy = 0, 0



   def __init__(self, t0, rx0, ry0, vx0, vy0):

      self.t  = t0

      self.rx = rx0

      self.ry = ry0

      self.vx = vx0

      self.vy = vy0


```

Bundan sonra belirli bir zamana ait konum ve hız bilgilerimizi bir arada tutmak için bu yapıyı kullanacağız.

Bu sınıfın sadece bir metodu var, o da `__init__()`. Adından da anlaşılacağı üzere bu sınıfın parametrelerini doldurmak için kullanılıyor. Herhangi bir parametre için varsayılan değer yok, çünkü konum ve hızı içeren bir vektörün başlangıç değerinin ne olduğunu tahmin etmemiz mümkün değil.

Hazırlık kısmına devam edelim. Öncelikle kullanacağımız paketleri ekliyoruz ve yerçekimi sabitini dolduruyoruz. Başlangıç zamanı, bitiş zamanı ve adım büyüklüğünü de burada dolduruyoruz. Tüm bu parametreleri en başta tanımlıyourz ki, sonradan başka değerler kullanmak istersek hepsini derli toplu burada bulabilelim.

Yaptığımız birkaç eğlenceli iş daha var; başlangıç hızının büyüklüğünü ve ilk atış açısını veriyoruz, sonra da `pvt0` başlangıç vektörünü bu değerlerle dolduruyoruz. Bu aşamada birimlere dikkat, Python `math.sin` ve `math.cos` fonksiyonları derece değil radyan cinsinden parametrelerle çalışıyor. Emin olun dalgınlıkla bunu gözden kaçırmak çok kolay.

En son yaptığımız iş ise `zamanKonumHız` adlı, zaman, konum ve hız bilgisini paketleyen yapılardan oluşan boş bir liste oluşturmak. Her zaman adımında yaptığımız hesaplamalarla oluşturduğumuz bu veri paketlerini buraya istifleyeceğiz.

In [2]:

```py
# sonradan gerekecek kütüphanelerini çağır

import matplotlib.pyplot as plt

import math



# Kütleçekimi Sabiti [m/s^2]

gDünya = 9.81



# başlangıç zamanı

t0 = 0

# bitiş zamanı (sn)

tSon = 100

# adım büyüklüğü (sn)

tAdım = 0.5



# başlangıç hızı (m/sn) ve atış açısı (derece)

v0 = 100 

yükselmeAçısı = 50 



# başlangıç konum ve hız

pvt0 = zamanKonumHız(t0, 0, 0, v0*math.cos(math.radians(yükselmeAçısı)), v0*math.sin(math.radians(yükselmeAçısı)))



# Zaman, yükseklik ve hız bilgilerini içeren vektör listelerini oluştur

pvtList = []


```

Uzun hazırlık evreleri bilimsel programlamacılığın doğasında vardır. Varsayılan değerler, bilimsel sabitler, seçenekler, konfigürasyonlar gibi birçok parametre ve bilgi genellikle ilk adım olarak oluşturulur. Ayrıca gerekli bilgileri tutacak veri yapıları, sınıflar ve o sınıfların alt metodları ya da işlevleri de yine en başta oluşturulur. Bilimsel Programlama işlerinde pek de dile getirilmeyen bir sırrı artık biliyorsunuz: Zamanın önemli bir kısmı bu tür göze gözükmeyen ama mecburi işlerle geçer. Bununla birlikte, bu adımı ne kadar özenli yaparsanız Hesaplama ve sonrasındaki Veri Analizi aşamalarında başınız o kadar az ağrır.

Sonunda Hesaplama adımına ulaşmayı başardık. Bu adım, verilen bir $t$ zamanı için, başlangıç değerlerinden(`pvt0`) nereye varılacağını hesaplayan bir fonksiyondan ibaret. Fonksiyonun içindeki matematiği yazının başında açıklamıştık zaten – zamana bağlı olarak yatayda ve düşeyde konum ve hız hesaplanıyor. Yeni konum, zaman ve hızdan oluşan bu veri paketi fonksiyon tarafından döndürülüyor, ancak başlangıç değerleri değiştirilmiyor.

In [3]:

```py
def tAnındaZamanKonumHız(t, pvt0, g=gDünya):

    """Verilen bir t zamanı için yeni konum ve hızı döndürür"""

    tYeni  = pvt0.t + t

    rxYeni = pvt0.rx + pvt0.vx * t

    ryYeni = pvt0.ry + pvt0.vy * t + (-1/2 * g * t**2)

    vxYeni = pvt0.vx 

    vyYeni = pvt0.vy + (-g) * t

    return zamanKonumHız(tYeni, rxYeni, ryYeni, vxYeni, vyYeni)


```

Hesaplama adımında yapmamız gereken tek şey bu fonksiyonu her bir zaman adımı için tekrar tekrar çağırmak. Diğer bir deyişle döngü $t \le t_{Son}$ olana dek çalışıyor. Ancak ikinci bir kontrol daha var, cismimiz yerin altına düşmesin diye hesaplanan irtifa değeri sıfırın altına inerse de döngüden çıkılıyor.

In [4]:

```py
t = pvt0.t

h = pvt0.ry 

while t<=tSon and h>=0:

    pvtList.append( tAnındaZamanKonumHız(t, pvt0) )

    h = pvtList[-1].ry

    t += tAdım


```

Şimdilik bir Veri Analizi adımımız yok, bir sonraki örnekte karşımıza çıkacak. Bu nedenle Görselleştirme adımına geçebiliriz. Bu kez zamana karşı değil yatay ve düşey eksenlerdeki konum ve hızı göstereceğiz.

In [5]:

```py
# konum grafiği 

plt.plot( [pvt.rx for pvt in pvtList], [pvt.ry for pvt in pvtList])



plt.title("Konum")

plt.xlabel("x konum (m)")

plt.ylabel('y konum (m)')



plt.show()



# hız grafiği

plt.plot( [pvt.vx for pvt in pvtList], [pvt.vy for pvt in pvtList])



plt.title("Hız")

plt.xlabel("x hız (m/sn)")

plt.ylabel('y hız (m/sn)')



plt.show()


```

![](data:image/png;base64,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)

![](data:image/png;base64,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)

Konum grafiği beklediğimiz gibi çıktı, ama hız grafiği biraz tuhaf. Aslında hız grafiğinin bize anlatmaya çalıştığı, yatay hızın hiç değişmediği, düşey hızınsa yaklaşık 80 m/s’den başlayıp -80 m/s civarında sonlandığı.

İlginç bir nokta daha var: son konum 0’ın altında çıktı. Bunun da sebebi şu; `while` döngüsü, irtifanın 0’ın altında olduğu bir değer hesaplanıp listeye eklendikten *sonra* irtifa kontrolünü yapıyor ve döngüden çıkıyor, haliyle 0’ın altında kalan son değer de grafiğe giriyor. İrtifanın tam olarak sıfıra denk geldiği yerde grafiği sonlandırmak isteseydik işler epey karışacaktı, zira bu sefer hangi zamanda irtifanın sıfıra eşit olduğunu bulmak için aradaki değeri tahmin etmemiz (İngilizcesiyle *interpolation*) ya da benzer başka bir yöntem kullanmamız gerekecekti. Şimdilik yazılımı karmaşıklaştıracak bu işlere girmiyoruz, zira bizi başka konular bekliyor.

Yazının başında Veri Analizi adımından bahsetmiştim, artık buna dair bir örnek yapmanın da zamanı geldi. Sayısal integrasyon ya da sayısal diferansiyel çözümü metodları diye afili isimler verilen, ama aslında “ben tembel adamım, ben çalışacağıma bilgisayar çalışsın” diyenlerin şaşmaz tercihi olan metodların en basitiyle eğik atış problemini çözeceğiz. Sonra da bunu şimdiye dek hesapladığımız “gerçek” değerlerle karşılaştırarak yaptığımız hatayı ölçeceğiz.

Öncelikle her zaman olduğu gibi işin Hazırlık adımına bakalım. Bu adımda yapılan işler artık tanıdık, ama ufak bir ek yaptık ve `konumBüyüklüğü()` ile `hızBüyüklüğü()` metodlarını ekledik. Sınıf yapılarının iki temel özelliği var: *bilgi depolamak* ve bu sınıfa ait bir *işlevi* yerine getirmek. Bizim vektör sınıfı da zaman, konum ve hız gibi bilgileri depoluyor ve artık konum ve hız vektörlerinin büyüklüğünü hesaplama işlevini yerine getiriyor. Bu işlevlere daha sonra ihtiyacımız olacak.

In [6]:

```py
class zamanKonumHız:

   'Zaman, 2D konum ve 2D hız değerlerini içeren vektör sınıfı'

   t = 0

   rx, ry = 0, 0

   vx, vy = 0, 0



   def __init__(self, t0, rx0, ry0, vx0, vy0):

      self.t  = t0

      self.rx = rx0

      self.ry = ry0

      self.vx = vx0

      self.vy = vy0



      

   def konumBüyüklüğü(self):

       """Konum vektörünün büyüklüğünü döndürür"""

       return math.sqrt(self.rx*self.rx+self.ry*self.ry)



   def hızBüyüklüğü(self):

       """Hız vektörünün büyüklüğünü döndürür"""

       return math.sqrt(self.vx*self.vx+self.vy*self.vy)


```

Hazırlık işlerinin kalanı da tanıdık. Ama bu kez hata vektörünü de hazırlayıp başlangıç değerlerini 0 olarak giriyoruz. Gerçek değer ile sayısal metodlarla hesaplanan değer arasındaki farkı her adımda bu yapıya kaydedeceğiz.

Bunun yanı sıra sayısal hesaplama ve gerçek vektörleri taşıyacak yapıların da ilk değerlerini dolduruyoruz. Bunu yapma amacımız, hesaplamanın ilk değerlerini bildiğimiz için hesaplama döngüsüne girmelerini engellemek. Daha sonra döngüyü kurarken bu ilk zaman adımını atlayacağız.

In [7]:

```py
# sonradan gerekecek kütüphanelerini çağır

import matplotlib.pyplot as plt

import math



# Yerçekimi sabiti [m/s^2]

gEarth = 9.81



# başlangıç zamanı

t0 = 0

# bitiş zamanı (sn)

tSon = 100 

# adım büyüklüğü (sn)

tAdım = 0.5



# başlangıç hızı (m/sn) ve atış açısı (derece)

v0 = 100 

yükselmeAçısı = 50 



# başlangıç konum ve hız

pvt0 = zamanKonumHız(t0, 0, 0, v0*math.cos(math.radians(yükselmeAçısı)), v0*math.sin(math.radians(yükselmeAçısı)))



# ilk değerleri doldur

gerçekPvtList = [pvt0]

numPvtList    = [pvt0]

hataPvtList   = [zamanKonumHız(t0, 0, 0, 0, 0)]


```

Gelelim Hesaplama adımına. Kullanacağımız sayısal integrasyon yöntemi [Euler Metodu](https://en.0wikipedia.org/wiki/Euler_method). Yöntemin detaylarına girmeyeceğim ama eğik atış problemi için yapılan iş özetle şöyle:

1. Başlangıç zamanındaki hız ve ivmenin çok kısa bir süre için sabit olduğunu varsayarak, bir sonraki adım için yeni hızı ve yeni konumu hesapla
2. İlk adımda hesaplanan hız ve ivmenin çok kısa bir süre için sabit olduğunu varsayarak, bir sonraki adım için yeni hızı ve yeni konumu hesapla
3. İkinci adımda hesaplanan hız ve ivmenin çok kısa bir süre için sabit olduğunu varsayarak, bir sonraki adım için yeni hızı ve yeni konumu hesapla
4. …

Elbette ivme bizim problemde sabit, ama sabit olmasaydı (örneğin Dünya’dan çok uzaklaşıyor olsaydık) ivmeyi tekrar tekrar hesaplamamız gerekecekti.

Eğik atış probleminde Euler Metodu’nun bir adımının matematiksel ifadesi ise şöyle:

$t_n$ anında yatay eksendeki konum: $ r_x(t_n) = r_x(t_{n-1}) + v_x(t_{n-1}) dt$  

$t_n$ anında düşey eksendeki konum: $ r_y(t_n) = r_y(t_{n-1}) + v_y(t_{n-1}) dt$

$t_n$ anında yatay eksendeki hız: $ v_x(t_n) = v_x(t_{n-1}) $  

$t_n$ anında düşey eksendeki hız: $ v_y(t_n) = v_y(t_{n-1}) + g dt $

Yani $t_n$ anındaki konum ve hız, $t_{n-1}$ anındaki konum ve hız ile $dt$ ile ifade edilen adım büyüklüğüne bağlı. Yatay eksende hız değişmiyor, çünkü bunu sağlayacak bir kuvvet ya da ivme yok. Düşey hız ise sabit ivmeye bağlı.

`tAnındaZamanKonumHız()` metodu bu yazıda verilen bir önceki örnekle aynı ve bize her hesaplama zamanı için “gerçek” konum ve hız değerlerini veriyor. `eulerZamanKonumHız()` ise, yukarıda bahsettiğimiz matematiksel modelle *yaklaşık* değerleri her adım için hesaplıyor.

In [8]:

```py
def tAnındaZamanKonumHız(t, pvt0, g=gDünya):

    """Verilen bir t zamanı için yeni konum ve hızı döndürür"""

    tYeni  = pvt0.t + t

    rxYeni = pvt0.rx + pvt0.vx * t

    ryYeni = pvt0.ry + pvt0.vy * t + (-1/2 * g * t**2)

    vxYeni = pvt0.vx 

    vyYeni = pvt0.vy + (-g) * t

    return zamanKonumHız(tYeni, rxYeni, ryYeni, vxYeni, vyYeni)



def eulerZamanKonumHız(dt, pvt, g=gDünya):

    """Verilen bir dt adım büyüklüğü için yeni konum ve hızı döndürür"""

    tYeni  = pvt.t  + dt

    rxYeni = pvt.rx + pvt.vx * dt

    ryYeni = pvt.ry + pvt.vy * dt 

    vxYeni = pvt.vx + 0 * dt

    vyYeni = pvt.vy + (-g) * dt

    return zamanKonumHız(tYeni, rxYeni, ryYeni, vxYeni, vyYeni)


```

Hesaplama mekanizmamızı da kurduk, artık hesaplama döngüsüne geçelim. İlk iş, irtifayı gerçek listenin ilk adımına ayarlamak oldu. İlk zaman adımını başta doldurduğumuz için döngüde hesaplanacak hedef zaman adımını da adım büyüklüğü kadar ilerlettik. Sonra da döngüye girdik. Döngüde önce gerçek zaman, konum hız vektörünü, sonra sayısal hesaplamayı, en sonda da bu ikisinin farkına karşılık gelen hata vektörünü doldurduk. Hazırlık adımını detaylı bir şekilde yaptığımız için döngü bu kadar basit oldu.

In [9]:

```py
# Döngüyü çalıştır

t = gerçekPvtList[0].t + tAdım

h = gerçekPvtList[0].ry 

while t<=tSon and h>=0:

    pvtGerçek = tAnındaZamanKonumHız(t, pvt0)

    gerçekPvtList.append( pvtGerçek )

    

    pvtNum = eulerZamanKonumHız(tAdım, numPvtList[-1])

    numPvtList.append( pvtNum )

    

    hataPvt = zamanKonumHız(t, pvtNum.rx-pvtGerçek.rx, pvtNum.ry-pvtGerçek.ry, pvtNum.vx-pvtGerçek.vx, pvtNum.vy-pvtGerçek.vy)

    hataPvtList.append(hataPvt)

    

    h = gerçekPvtList[-1].ry

    t += tAdım


```

O halde sonuçları görelim. Bu kez aynı grafiğe hem gerçek hem de sayısal yöntemlerle hesaplanan yaklaşık konum ve hızı basacağız. Sonra da hata grafiklerini çizdireceğiz. Grafik başlıklarına ve veri etiketlerine adım büyüklüğünü yazdırıyoruz ki sonradan bu grafiklere baktığımızda hatırlayabilelim.

In [10]:

```py
# konum grafiği 

plt.plot( [pvt.rx for pvt in gerçekPvtList], [pvt.ry for pvt in gerçekPvtList], label="gerçek")

plt.plot( [pvt.rx for pvt in numPvtList], [pvt.ry for pvt in numPvtList], label="Euler (" + str(tAdım) + " s)")



plt.title(r"Konum")

plt.xlabel("x konum (m)")

plt.ylabel('y konum (m)')

plt.legend(loc=3)



plt.show()



# hiz grafiği

plt.plot( [pvt.vx for pvt in gerçekPvtList], [pvt.vy for pvt in gerçekPvtList], label="gerçek")

plt.plot( [pvt.vx for pvt in numPvtList], [pvt.vy for pvt in numPvtList], label="Euler (" + str(tAdım) + " s)")



plt.title(r"Hız")

plt.xlabel("x hız (m/s)")

plt.ylabel('y hız (m/s)')

plt.legend(loc=3)



plt.show()



# hata grafikleri 

plt.subplot(211)

plt.plot( [pvt.t for pvt in hataPvtList], [pvt.konumBüyüklüğü() for pvt in hataPvtList])



plt.title(r"Konum ve Hız Hatası Değişimi (" + str(tAdım) + " s)")

plt.xlabel("zaman (s)")

plt.ylabel('konum hatası (m)')



plt.subplot(212)

plt.plot( [pvt.t for pvt in hataPvtList], [pvt.hızBüyüklüğü() for pvt in hataPvtList])



# plt.title(r"Hız Değişimi ($ v = gt $)")

plt.xlabel("zaman (s)")

plt.ylabel('hız hatası (m/s)')



plt.show()


```

![](data:image/png;base64,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)

![](data:image/png;base64,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Fr761a+2yM9oZq1fmyiKrOQOu3zemjVr6NatG7Nnzy74mq5du6a+PiIYMWIE48aN22Be+/btGTRoEI8//riLwsyajW8KWEYHH3wwv/3tb1mxYgUffvghjz32GFtssQW9e/fmN7/5DZD7xf/CCy8UfP2RRx7Jbbfdtm65d999lyFDhvDQQw/xzju5i9n/8Y9/8MYbbwC5rY577rmH+fPnc91117XAT2hmbYGLoowGDx7M0KFD2XfffTnppJOoqalh6623ZsKECdx9993su+++7L333kyZMqXg6y+//HKWLVvGzjvvzF577cUzzzxD3759GTt2LEceeST9+/fniCOOYOnSpete065dOyZOnMj06dO59dZbW+pHNbNWTIV2b2xuampqora29nPT5s2bx1577ZVRos98+OGHbLnllnz00UcceuihjB8/noEDB27UeyxZsoQ77riDq6++ukwpy6NS/gyyNOfagwHY+4dPZ5zEbEOS6iKiprHlvEVRZqNHj2bAgAEMHDiQb3zjGxtdEk899RSHHXaYr6kws8z4t0+ZPfDAA016/de+9jXmz5/fTGnMzDaetyjMzCyVi8LMzFK5KMzMLJWLwszMUrkoyqhdu3YMGDBg3VdjF8Hde++9nHvuuU1a59KlSzn++OPXPR83bhy77bYbe+yxB48//njB14wcOZLevXuvy1nsqvH1rVq1ikMPPZTVq1c3KbOZVTaf9VRGXbp0KfmX7qYodCvyn/3sZ5x55pkAzJ07l4kTJzJnzhyWLFnC4YcfziuvvPK5O82udcMNN3DyySdv1Po7duzIkCFDmDRpEqeffvqm/yBmVtHaRlH8/hJ466Xmfc/t94FjNu02GdXV1dTW1tKjRw9qa2u58MILeeqppz63TENDA2eddRZvvvkmAD//+c856KCDuOqqq1iyZAkLFy6kR48eG5x+O3nyZMaOHQvAlClTOO200+jUqRO9e/dmt91247nnnuPAAw/c6Mxz5sxh1KhRrFq1ijVr1jB58mT69OnD8OHDufTSS10UZq2Ydz2V0ccff/y5XU9r7wRbijFjxnDBBRcwc+ZMJk+ezPe+97118+rq6pgyZcoGJfH666/TvXt3OnXqBMDixYvp1euzkWWrqqpYvHhxwfVddtll9O/fnwsuuOBzd7Nd6/bbb2fMmDHMnj2b2tpaqqqqAOjXrx8zZ84s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)

![](data:image/png;base64,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)

Hiç fena değil, değil mi? Konum değerlerinde gerçek değerden ne kadar saptığımızı görüyoruz. Hız grafiğinde ise pek bir fark göremiyoruz. Hata analizi için özel olarak ürettiğimiz grafiklere bakarak daha fazla bilgi edinebiliriz elbette. Buna göre konum hatası lineer olarak artıyor ve 16 saniyede 40 metreye ulaşıyor. E zaten 1000 m yol gitmiştik, pek iyi bir performans gösterdiğimiz söylenemez; hatamız %4 nispetinde. Oysa hız konusunda gayet iyiyiz, altı üstü 0.00000000000002 m/s hata yapmışız – grafikte y eksenindeki değerlerin üstündeki “*1e-14*” ifadesine dikkat.

Konum ve hızdaki bu kadar farklı hata davranışının sebebi gerçek dinamiğin matematiğinde ve Euler Metodu’nda gizli. Konum değişimi zamanın karesiyle orantılı, hız değişimi ise zamanla doğru orantılı. Euler Metodu lineer sistemleri hatasız olarak modelleyebilirken, lineer olmayan sistemleri hatalı bir şekilde modelleyebiliyor. “Madem lineer sistemler hatasız, hızda niye küçük de olsa bir hata var?” diye soranlar olabilir. Soruyu Orhan Gencebay’dan ilhamla, “hatasız makine olmaz” diye yanıtlayabiliriz; bilgisayarlar çalışma prensipleri gereği gerçel bir sayıyı sınırsız uzunlukta depolayamazlar. Yani bir sayıyı defalarca 1.2345678 ile çarpıp bölerseniz neticede başladığınız yere dönmeyi beklersiniz, ama bilgisayarda bunu yaparsanız küçük de olsa bir hata görürsünüz. İnanmayanlar deneyebilir! Bu örnekte gördüğümüz 10-14 seviyesindeki bu hata “kayan nokta” (*İng. floating point*) hataları için normal kabul edilebilecek bir seviye.

Sayısal metodların doğruluğu genellikle seçilen adım büyüklüğüne bağlıdır. Konum hatasından memnun olmayanlar hesaplamayı 0.1 saniye adım büyüklüğü için tekrar edebilirler. Spoiler vermiş gibi olacağım ama hata 40 metreden 7.5 metreye düşüyor, lakin bilgisayar 5 kat daha fazla sayıda döngü hesaplamak zorunda kalıyor. Çoğumuzun bilgisayarında bu kadar basit bir problem için sorun olmayacaktır, ama eğik atıştan daha karmaşık problemler için bunun bir sorun teşkil edeceğini size garanti edebilirim.

Adım büyüklüğü küçüldükçe modeldeki hata azalır, ama daha fazla sayıda işlem yapıldığı için yukarıda kayan nokta meselesinde birazcık bahsettiğimiz, bilgisayarın hesaplama hataları diyeceğimiz hatalar artar. Nitekim 0.1 saniye adım büyüklüğünde hız hatası 10-13 seviyesine yükseliyor.

Bu örneğimizde de saf Python kullandık, *hâlâ* `numpy` gibi daha eğlenceli ve yetenekli yapılara giremedik; bir sonraki aşama için sözüm olsun. En azından, hem eğik atış problemini karmaşıklaştırıp sayısal metodlara giriş yaptık, hem de sınıf yapılarına değindik.