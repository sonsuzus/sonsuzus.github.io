---
title:  Numpy Kütüphanesi Nedir? Nasıl Kullanılır?
author: sonsuz
date: 2023-06-20 00:51:34 +0300
categories: [Program,Python]
tags: [python,numpy,veri,veri bilimi,veri analizi,modül,kütüphane]
---



NumPy, [Python](https://sonsuzus.github.io/tags/python) programlama diline ait çok boyutlu dizilerle ve matrislerle çalışmamıza yardım eden ileri düzey matematiksel işlemler yapabileceğimiz bir kütüphanedir. Günümüzde özellikle [veri bilimi](https://sonsuzus.github.io/tags/veri) üzerine çalışanlar başta olmak üzere Numpy, Python programlayanlar tarafından çok sık kullanılan bir **kütüphanedir.**

## Numpy Nedir?

* Açık Kaynak ve numerik bir Python kütüphanesidir.
* Çok boyutlu dizin ve matris veri yapılarını içerir
* Numeric ve Numarray öğelerinin uzantısıdır.
* Rastgele sayı üreteçlerine sahiptir.
* Pandas nesneleri büyük ölçüde Numpy ile bağlantılıdır. Buna Pandas Numpy’i genişletir diyebiliriz.
* Dizinler üzerinde matematiksel, cebirsel ve istatistiksel operasyonlar uygulamak için kullanılır.

## Numpy Kullanımı

Öncelikle eğer bilgisayarınızda Numpy kütüphanesi kurulu değilse terminalden bu komut ile Numpy’ı indiriyoruz.

```py
>>> pip install numpy
```

Artık sistemimizde Numpy kütüphanesine sahibiz. Eğer Numpy kullanacaksak kodumuzu yazmaya başlamadan önce kütüphaneyi çağırmamız gerekmekte. Import ile kütüphaneyi çağıracağız ve çoğu kişinin kullandığı “np” aliasını (takma adını) kullanacağız.

```py
import numpy as np
```

### ***Boş Array Oluşturma***

Şimdi sıra Numpy kütüphanesini en çok ilgilendiren veri tipinde: **Diziler.** Numpy ile boş bir dizi oluşturmanın birden fazla yolu vardır.

#### **np.array() :**

![numpy-array](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20774%20180'%3E%3C/svg%3E)

![numpy-array](https://d9v7j6n3.rocketcdn.me/wp-content/uploads/2020/06/np_array.jpg)

np.array() kullanımı
**np.array()**, Numpy’da basit bir şekilde bir dizin oluşturmanızı sağlar. np.array() metodu hakkında [daha fazla bilgiye ve aldığı parametrelere buradan ulaşabilirsiniz.](https://numpy.org/doc/1.18/reference/generated/numpy.array.html)

#### **np.arange():**

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20771%20133'%3E%3C/svg%3E)

![](https://d9v7j6n3.rocketcdn.me/wp-content/uploads/2020/06/np_arange.jpg)

np.arange() kullanımı
: np.arange() fonksiyonu 4 parametre alır. Bunlar başlangıç değeri, bitiş değeri, değişim miktarı ve veri tipidir. Fonksiyon başlangıç noktasından bitiş noktasına kadar değişim miktarı kadar artarak girilen veri tipinde değerler üretir. Yukarıdaki örnekte başlangıç 0, son ise 12’ydi. Değişim miktarımızda 3 olduğundan np.arange() fonksiyonu 0’dan üçer üçer artarak bize bir dizin üretti.

np.arange() fonksiyonu n-boyutlu dizinler oluşturmak için oldukça uygundur. Fonksiyon ilk olarak tek boyutlu bir dizin oluştursa da np.reshape() metodu ile dizininizin boyutlarını istediğiniz gibi ayarlayabilirsiniz.

#### **np.linspace():**

![numpy-linspace](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20771%20131'%3E%3C/svg%3E)

![numpy-linspace](https://d9v7j6n3.rocketcdn.me/wp-content/uploads/2020/06/np_linspace.jpg)

np.linspace() kullanımı
: np.linspace() metodu başlıca 3 parametre alır. Başlangıç, dizinin hangi sayıdan başlayacağıdır. Bitiş, dizinin hangi sayıya geldiğinde son bulacağıdır. Bir de **num**, dizinin kaç elemana sahip olacağıdır. np.linspace() metodu başlangıçtan sona num tane sayıyı birbiri arası uzaklık eşit olacak şekilde böler. [Metot hakkında daha fazla bilgiyi burada bulabilirsiniz.](https://numpy.org/doc/1.18/reference/generated/numpy.linspace.html?highlight=nump%20linspace#numpy.linspace)

#### **np.zeros():**

![numpy-zeros](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20758%20205'%3E%3C/svg%3E)

![numpy-zeros](https://d9v7j6n3.rocketcdn.me/wp-content/uploads/2020/06/np_zeros-1.jpg)

np.zeros() kullanımı
: np.zeros() bir tuple (demet) değeri alır. Bu tuple değeri, oluşturmak istediğimiz dizinin boyutlarının değerleridir. Örnekte girilen (4,4) dizinin 4 satır ve 4 sütundan oluşacağını belirtmek içindir. np.zeros() ise bu boyutlarda ve sıfırlardan oluşan bir dizin üretir.

#### **np.ones():**

![numpy-ones](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20769%20163'%3E%3C/svg%3E)

![numpy-ones](https://d9v7j6n3.rocketcdn.me/wp-content/uploads/2020/06/np_ones.jpg)

np.ones() kullanımı
: np.ones() fonksiyonu da np.zeros() mantığında çalışır ve girilen boyutlarda oluşturduğu dizini 1’lerle doldurur.

#### **np.full():**

![numpy-full](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20768%20165'%3E%3C/svg%3E)

![numpy-full](https://d9v7j6n3.rocketcdn.me/wp-content/uploads/2020/06/np_full.jpg)

np.full() kullanımı
: np.full() metodu başlıca 2 parametre alır. İlki istenilen dizinin boyutu, ikincisi ise dizinin hangi sayıdan oluşacağı. Yukarıdaki örnekte oluşturduğumuz (2,3)’lük bir matrisin sadece 8 değerini içermesini istedik ve np.full() metotu bunu bizim için yaptı.

#### **np.random():**

![numpy-random](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20768%20184'%3E%3C/svg%3E)

![numpy-random](https://d9v7j6n3.rocketcdn.me/wp-content/uploads/2020/06/np_random.jpg)

np.random() kullanımı
: np.random() istenilen boyutta bir dizin oluşturur ve bu dizini 0 ve 1 aralığında üretilmiş rastgele ondalık sayılar ile doldurur. [Buradaki dökümantasyondan np.random() hakkında daha fazla bilgi alabilirsiniz.](https://numpy.org/doc/1.18/reference/random/index.html?highlight=numpy%20random#module-numpy.random)

### ***Lineer Cebir***

Numpy’ın bize sağladığı en büyük kolaylıklardan birisi de cebirsel işlemleri halletmemiz için sahip olduğu fonksiyonlar. İsterseniz 2 farklı Numpy dizini oluşturalım ve örneklerden devam edelim.

```py
dizin1 = np.array((1,2,3))
dizin2 = np.array((2,3,1))
```

#### **np.dot():**

![numpy-dot](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20770%20118'%3E%3C/svg%3E)

![numpy-dot](https://d9v7j6n3.rocketcdn.me/wp-content/uploads/2020/06/np_dot.jpg)

np.dot() kullanımı
: np.dot() metodu sonuç olarak aldığı iki Numpy dizininin nokta çarpımı ya da bir diğer adıyla skaler çarpımını döndürür. 

#### **np.matmul():**

![python-matmul](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20769%20117'%3E%3C/svg%3E)

![python-matmul](https://d9v7j6n3.rocketcdn.me/wp-content/uploads/2020/06/np_matmul.jpg)

np.matmul() kullanımı
: np.matmul() fonksiyonu çıktı olarak bize, girilen 2 dizinin matris çarpımı sonucunu verir. 

#### **np.T:**

![python-transpoz](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20771%20185'%3E%3C/svg%3E)

![python-transpoz](https://d9v7j6n3.rocketcdn.me/wp-content/uploads/2020/06/np_t-1.jpg)

Bir matrisin transpozunu alma
: Cebirde bir matrisin transpozunu bulmak için matrisin sütunları satırlar, satırlarını ise sütunların yerine koyarız. Numpy sayesinde np.T ile matrisin transpozunu rahatlıkla bulabilmekteyiz.

Determinant, identitiy(birim) matris, logaritmik değerler gibi bir çok şeyi Numpy ile bulabilmekteyiz. Bu yazıda az sayıda örnek verdiysek de [buradan](https://docs.scipy.org/doc/scipy/reference/tutorial/linalg.html) diğer fonksiyonlara ulaşabilirsiniz.

### ***İstatistik***

İstatistik her ne kadar zevkli bir alan olsa da karmaşıklığıyla bazen bizleri oldukça zorlamakta. Numpy kütüphanesi sayesinde çok büyük veri setlerinde rahatlıkla istatistiksel analizler yapabilmekteyiz. Şimdi verdiğimiz diğer örneklere kıyasla biraz daha uzun bir dizin üzerinden gidelim.

```py
boy_olculeri_cm = np.random.randint(low = 150,high = 200,size = 20,dtype = int)
```

Yukarıdaki kod parçacığı ile 150 ve 200 arasında tam 20 integer (*tam sayı*) elemana sahip bir Numpy dizini oluşturduk. Bu dizini oluşturan bir sınıftaki öğrencilerin santimetre(cm) cinsinden boy ölçüleri olduğunu varsayalım. Dizinimizin içerdiği elemanlar aşağıdaki şekilde olacaktır. Bu değerler sizde farklılık gösterebilir çünkü bu elemanları Numpy ile rastgele olacak bir biçimde ürettik.

```
[171, 187, 155, 191, 174, 184, 159, 175, 193, 174, 156, 167, 187,158, 158, 190, 157, 168, 153, 169]
```

#### **np.median():**

![python-median](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20749%20118'%3E%3C/svg%3E)

![python-median](https://d9v7j6n3.rocketcdn.me/wp-content/uploads/2020/06/np_median.jpg)

np.median() kullanımı
: Bir dizinin medyanı o dizini sıraladığımızda tam ortasına denk gelen elemana denir. Bizim bu sınıfımızdaki boy ölçülerinin medyanını np.median() fonksiyonu ile rahatlıkla bulabiliriz. Yukarıdaki örnekte görüldüğü üzere sınıfımızın boylarının medyanı 170’dir.

#### **np.mean():**

![python-mean](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20770%20121'%3E%3C/svg%3E)

![python-mean](https://d9v7j6n3.rocketcdn.me/wp-content/uploads/2020/06/np_mean.jpg)

np.mean() kullanımı
: np.mean() ise verilen dizinin değerlerinin ortalamasını bulmak için kullanılır. Yine örneğimiz üzerinden gidersek sınıfın boylarının ortalaması 171.3 cm’dir.

#### **np.std()**:

![standart-sapma](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20759%20121'%3E%3C/svg%3E)

![standart-sapma](https://d9v7j6n3.rocketcdn.me/wp-content/uploads/2020/06/np_std.jpg)

standstanp.std() kullanımı
: Standart sapma bir dizindeki verilerin ortalamaya göre dağılımının sayısal olarak gösterimidir. Normal şartlarda standart sapmayı bulmak için :

* Sayıların artimetik ortalaması bulunur,
* Her bir sayı aritmetik ortalamadan çıkarılır ve sonucun karesi alınır,
* Bu kareler toplanır ve toplam serinin eleman sayısının 1 eksiğine bölünür,
* Bu sonucun karekökü alınır.

Standart sapmayı bulmak için bu işlemleri yapmamız gerekir fakat Numpy kütüphanesi np.std() fonksiyonuyla arka planda bu işlemleri yapar ve sonucu bize getirir.

Numpy görüldüğü üzere çok fazla matematiksel hesaplamalarda kullanılabilir. Az sayıda örnekler üzerinden gittik fakat [Numpy’ın kendi dökümantasyonlarından](https://numpy.org/doc/stable/index.html) istediğiniz metoda bakabilirsiniz.

## Numpy’ın Dizinleri vs. Python’un Kendi Dizinleri

Aslında bakacak olursak Numpy’ın da Python’un da dizileri birbiriyle çok fazla benzerlikler göstermekte. İki türde de veri saklarsınız, indeklersiniz ve iterate (yenilemek) edebilirsiniz.

Fakat Numpy ile oluşturacağınız dizinler hem çok daha az boyutta yer kaplar hem de Python dizinlerine kıyasla oldukça hızlı çalışırlar. Ayrıca Python dizinlerinde çoğu matematiksel işlemi doğrudan yapamazsınız. Bunlara örnek vermek gerekirse toplama, çıkarma, çarpma, bölme ve kuvvet alma. Fakat Numpy sayesinde bunu rahatlıkla yapabiliriz.

```py
# Python Dizini
In [0]: yeni_dizin = [2,4,5,2,1,4]
In [1]: print((yeni_dizin) * 2)
Out[1]: [2, 4, 5, 2, 1, 4, 2, 4, 5, 2, 1, 4]

# Numpy Dizini
In [2]: yeni_dizin = np.array([2,4,5,2,1,4])
In [3]: print((yeni_dizin) * 2)
Out[3]: [ 4  8 10  4  2  8]
```

Örnekte görüldüğü üzere ilk dizini 2 ile çarptığımızda **Python** dizinden bir tane daha oluşturup diğerinin sonuna ekledi fakat **Numpy** tüm değerleri 2 ile çarptı.

## Numpy Veri Tipleri

Numpy Python’a göre çok daha fazla ve farklı veri tiplerini destekler. Aşağıdaki tabloda Numpy’ın içerdiği veri tiplerini bulabilirsiniz.

![veri-tipleri](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20674%20580'%3E%3C/svg%3E)

![veri-tipleri](https://d9v7j6n3.rocketcdn.me/wp-content/uploads/2020/06/data_types.png)

Numpy Veri Tipleri
: Sonuç olarak Numpy bize gerek matematiksel işlemler gerekse dizinler üzerinde yapacağımız komplike işlemlerde oldukça kolaylık tanımaktadır. Eğer Python ile kodlama yapmaya ilgili iseniz Numpy’a bir göz gezdirmenizi tavsiye ederiz. 
