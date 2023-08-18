---
title: Python Sınıflar
author: sonsuz
date: 2023-08-18 19:18:05 +0300
categories: [Program,Python]
tags: [python,programlama,sınıf,class]
---


Python nesneye yönelik bir programlama dilidir. Nesneye yönelik programlama dilinin esasını nesne oluşturur. Bir nesne oluşturmadan önce, nesnenin özelliklerini (değişkenler) ve metodlarını (fonksiyonlar) belirleyecek olan bir sınıf bildirimi yapılarak yeni bir veri türü oluşturulur. Daha sonra, bu sınıf türünden nesneler oluşturularak, sadece bu nesne yoluyla sınıf kopyası içinde yer alan değişken ve fonksiyonlara erişim sağlanır.

## Sınıf bildirimi

Python'da bir sınıf bildirimi class anahtar kelimesi ile aşağıda gösterildiği şekilde yapılır:

```py
class sınıf-adı:
   # Sınıf dışından erişim sağlanabilen değişken bildirimleri
   ortak-değişken1 = ön-tanımlı-değer1
   ortak-değişken2 = ön-tanımlı-değer2
   .
   .

   # Sınıf dışından erişilemeyen değişken bildirimleri (çift alt çizgi ile başlar.)
   \_\_özel-değişken1
   \_\_özel-değişken2
   .
   .
   
   # Başlangıç değer atama fonksiyonu
   def \_\_init\_\_(sınıf-kopya-değişkeni, param1, param2, ...):
         sınıf-kopya-değişkeni.param1 = ...
         sınıf-kopya-değişkeni.param2 = ...
         .
         .	   
		 
   # Normal sınıf fonksiyon bildirimleri 
   def fonksiyon-adı1(param1, param2, ...)
   def fonksiyon-adı2(param1, param2, ...)
   .
   .   

```

* Ortak değişkenler sınıf dışından erişim sağlanabilen değişkenlerdir.
* Çift alt çizgi ( \_\_ ) ile başlayan özel değişkenler sınıf dışından erişilemeyen değişkenlerdir.
* Bir sınıftan bir nesne oluşturulduğunda, \_\_init\_\_() fonksiyonu otomatik olarak çağrılır ve başlıcası nesnenin değişkenlerine ilk değer atamak olan işlemleri gerçekleştirir.
* sınıf-kopya-değişkeni sınıfın aktif kopyasını gösteren ve \_\_init\_\_() fonksiyonunun ilk parametresi olarak tanımlanan değişken olup, sınıf içindeki değişken ve fonksiyonlara erişim sağlamak için kullanılır.
* \_\_init\_\_() fonksiyonunun ilk parametresinden sonra yer alan parametrelere, nesne oluşturulurken değer atanır.

Şimdi, sınıf bildiriminin yapılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
class sinif_kitap:
   # Sınıf dışından erişim sağlanabilen değişken bildirimleri
   grup = "Kitap"

   # Sınıf dışından erişilemeyen değişken bildirimleri (çift alt çizgi ile başlar.)
   __yazar = 1
   
   # Başlangıç değer atama fonksiyonu
   def __init__(self, kategori, adi):
       self.kategori = kategori
       self.adi = adi
		 
   # Normal sınıf fonksiyon bildirimleri 
   def nesne_yazdir(self):
       print(self.grup + ' ' + self.kategori + ' ' + self.adi)
	   
print(sinif_kitap)	   


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

<class '__main__.sinif_kitap'>

```

Program, grup adlı bir adet ortak değişken, \_\_yazar adlı bir adet özel değişken, iki parametreli bir \_\_init\_\_() fonksiyonu ve nesne değişken değerlerini ekrana yazan nesne\_yazdir() adlı bir fonksiyon içeren sinif\_kitap adlı bir sınıf bildirimi yapar. Sınıfı ekrana yazdırır.

## Nesne oluşturma

Python'da bir sınıf bildirimi yapıldıktan sonra, aşağıdaki gösterilen genel yapıyı kullanarak bu sınıftan nesneler oluşturabiliriz. Nesneyi oluşturduktan sonra, nesne adını nokta (.) karakteri ile birlikte kullanarak sınıf içinde yer alan değişken ve fonksiyonlara erişim sağlayabiliriz.

```py
nesne-adı = sınıf-adı(param1, param2, ...) # Nesne oluşturma (Parametre tanımlanması isteğe bağlıdır.)

# Nesne elemanlarına erişim 
print(nesne-adı.değişken-adı) # Nesne değişkenlerine erişim
nesne-adı.fonksiyon-adı() # Nesne fonksiyonlarına erişim


```

Bir nesne oluşturulduğunda, nesnenin oluşturulduğu sınıfın bir kopyası oluşturulmuş olur. Böylece, nesne yoluyla sınıf kopyası üzerinde yapılan değişiklikler esas sınıf içeriğini etkilemez.

Şimdi, sınıf bildiriminin yapılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
class sinif_kitap:
   # Sınıf dışından erişim sağlanabilen değişken bildirimleri
   grup = 'Kitap'

   # Sınıf dışından erişilemeyen değişken bildirimleri (çift alt çizgi ile başlar.)
   __yazar = ''
   
   # Başlangıç değer atama fonksiyonu
   def __init__(self, kategori, adi, yazar):
       self.kategori = kategori
       self.adi = adi
       self.__yazar = yazar
		 
   # Normal sınıf fonksiyon bildirimleri 
   def nesne_yazdir(self):
       print(self.grup + ', ' + self.kategori + ', ' + self.adi + ', ' + self.__yazar)
	   
nes1 = sinif_kitap('Roman', 'Çalıkuşu', 'Reşat Nuri Güntekin')
nes1.nesne_yazdir()

nes2 = sinif_kitap('Hikaye', 'Perili köşk', 'Ömer Seyfettin')
nes2.nesne_yazdir()


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Kitap, Roman, Çalıkuşu, Reşat Nuri Güntekin
Kitap, Hikaye, Perili köşk, Ömer Seyfettin

```

Program, grup adlı bir adet ortak değişken, \_\_yazar adlı bir adet özel değişken, iki parametreli bir \_\_init\_\_() fonksiyonu ve nesne değişken değerlerini ekrana yazan nesne\_yazdir() adlı bir fonksiyon içeren sinif\_kitap adlı bir sınıf bildirimi yapar. Bu sınıftan iki adet nesne oluşturur ve nesne fonksiyonu yoluyla nesne değişken değerlerini ekrana yazdırır.

## Nesne değişkenlerinde değişiklik yapma

Bir sınıftan bir nesne oluşturduktan sonra, nesne adını nokta (.) karakteri ve değişken adı ile birlikte kullanarak nesne değişken değerlerinde değişiklik yapabiliriz.

```


nesne-adı.değişken-adı = yeni-değer


```

Şimdi, nesne değişkenlerinde değişiklik yapma işlemini bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
class sinif_kitap:
   # Sınıf dışından erişim sağlanabilen değişken bildirimleri
   grup = 'Kitap'

   # Sınıf dışından erişilemeyen değişken bildirimleri (çift alt çizgi ile başlar.)
   __yazar = ''
   
   # Başlangıç değer atama fonksiyonu
   def __init__(self, kategori, adi, yazar):
       self.kategori = kategori
       self.adi = adi
       self.__yazar = yazar
		 
   # Normal sınıf fonksiyon bildirimleri 
   def nesne_yazdir(self):
       print(self.grup + ', ' + self.kategori + ', ' + self.adi + ', ' + self.__yazar)

   def yazar_degistir(self, yazar):
       self.__yazar = yazar	   
	   
nes1 = sinif_kitap('Roman', 'Çalıkuşu', 'Reşat Nuri Güntekin')
nes1.nesne_yazdir()

# nes1.__yazar = 'Ömer Seyfettin' # Değişken özel olduğundan erişim sağlayamaz.
nes1.yazar_degistir('Ömer Seyfettin') # Değişken özel olduğundan sadece sınıf fonksiyonu erişim sağlar.
nes1.kategori = 'Hikaye'
nes1.adi = 'Perili köşk'

nes1.nesne_yazdir()


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Kitap, Roman, Çalıkuşu, Reşat Nuri Güntekin
Kitap, Hikaye, Perili köşk, Ömer Seyfettin

```

Program, grup adlı bir adet ortak değişken, \_\_yazar adlı bir adet özel değişken, iki parametreli bir \_\_init\_\_() fonksiyonu ve nesne değişken değerlerini ekrana yazan nesne\_yazdir() adlı bir fonksiyon içeren sinif\_kitap adlı bir sınıf bildirimi yapar. Bu sınıftan bir adet nesne oluştururken nesne değişkenlerine birer değer atar ve bu değerleri nesne\_yazdir() fonksiyonu ile ekrana yazar. Nesne içindeki kategori ve adi değişken değerlerini nesne adı ve nokta (.) karakteri kullanarak, \_\_yazar1 değişken değerini ise nesne adı ve yazar\_degistir() fonksiyonunu kullanarak değiştirir. Yeni değişken değerlerini nesne\_yazdir() fonksiyonu ile ekrana yazar.

\_\_prideg1 değişken özel bir değişen olduğundan nesne yoluyla doğrudan erişim sağlanamaz. Özel değişkenlere erişm sağlamak için sınıf içinde yer alan fonksiyonlar kullanılır.

## Nesne değişkenlerini ve nesneleri silme

Bir sınıftan bir nesne oluşturduktan sonra, del anahtar kelimesini nesne adı, nokta (.) karakteri ve değişken adı ile birlikte kullanarak nesne değişken değerlerini, nesne adı ile kullanarak nesneyi silebiliriz.

```

del nesne-adı.değişken-adı
   
del nesne-adı   

```

Şimdi, nesne değişkenlerini ve nesneleri silme işlemini bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
class sinif_kitap:
   # Sınıf dışından erişim sağlanabilen değişken bildirimleri
   grup = 'Kitap'

   # Sınıf dışından erişilemeyen değişken bildirimleri (çift alt çizgi ile başlar.)
   __yazar = ''
   
   # Başlangıç değer atama fonksiyonu
   def __init__(self, kategori, adi, yazar):
       self.kategori = kategori
       self.adi = adi
       self.__yazar = yazar
		 
   # Normal sınıf fonksiyon bildirimleri 
   def nesne_yazdir(self):
       print(self.grup + ', ' + self.kategori + ', ' + self.adi + ', ' + self.__yazar)

   def yazar_degistir(self, yazar):
       self.__yazar = yazar
	   
nes = sinif_kitap('Roman', 'Çalıkuşu', 'Reşat Nuri Güntekin')
nes.nesne_yazdir()

del nes.adi # Nesne değişkenini silme

# nes.nesne_yazdir() # adi fonksiyon parametresi silindiğinden hata verir.

del nes # Nesneyi komple silme


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Kitap, Roman, Çalıkuşu, Reşat Nuri Güntekin

```

Program, grup adlı bir adet ortak değişken, \_\_yazar adlı bir adet özel değişken, iki parametreli bir \_\_init\_\_() fonksiyonu ve nesne değişken değerlerini ekrana yazan nesne\_yazdir() adlı bir fonksiyon içeren sinif\_kitap adlı bir sınıf bildirimi yapar. Bu sınıftan bir adet nesne oluştururken nesne değişkenlerine birer değer atar ve bu değerleri nesne\_yazdir() fonksiyonu ile ekrana yazar. Sonra, del anahtar kelimesini kullanarak nesne içindeki adi değişkenini siler. Silinen değişken nesne\_yazdir() fonksiyonunun bir parametresi olduğundan, nesne\_yazdir() fonksiyonu çağrıldığında hata verir. Tekrar del anahtar kelimesini kullanarak nesneyi tamamen sildiğimizde nesne yok olduğundan nesneye erişim sağlanamaz.

## Kalıtım işlemleri

Bir ana sınıftan türetilmiş bir sınıf oluşturarak, ana sınıfın tüm değişken ve fonksiyonlarının türetilmiş sınıf içinde kullanılmasına kalıtım adı verilir.

Kalıtım bir nesneden türetilen bir nesnenin türetildiği nesnenin tüm özelliklerine sahip olmasıdır. Kalıtım, nesneye yönelik programlamada mevcut bir sınıf içinde bulunan veri ve metotların bu sınıftan türetilen alt sınıflar içinde kullanılması olarak tanımlanabilir.

Bir ana sınıftan bir sınıf türetildiğinde, ana sınıfta yer alan tüm veri ve metotlar türetilen sınıf tarafından kullanılabileceği gibi, türetilen sınıf içinde de yeni veri ve metotlar tanımlanabilir. Eğer ihtiyaç duyulursa, ana sınıftan devralınan metotlar yeniden tanımlanır ve aynı isim altında farklı kodlar yazılır.

Öncelikle bir ana sınıf tanımlaması yapılmalıdır. Ana sınıf tanımlaması yapılırken, bu sınıftan üretilecek olan sınıfların ortak olarak sahip olacağı ve birlikte kullanacağı özellikleri gösteren değişkenlerin tamamının bildirimi ana sınıf içinde yapılmalıdır. Ana sınıftan türetilen alt sınıfların sadece kendileri tarafından kullanılacak özellikleri gösteren değişkenlerin bildirimi ise türetilen alt sınıfların içinde yapılmalıdır.

Bir ana sınıftan türetilmiş bir sınıf oluşturmak için aşağıda gösterilen yapı kullanılır:

```

class türetilen-sınıf-adı(ana-sınıf-adı):
   # Sınıf dışından erişim sağlanabilen değişken bildirimleri
   ortak-değişken1 = ön-tanımlı-değer1
   ortak-değişken2 = ön-tanımlı-değer2
   .
   .

   # Sınıf dışından erişilemeyen değişken bildirimleri (çift alt çizgi ile başlar.)
   __özel-değişken1
   __özel-değişken2
   .
   .
   
   # Başlangıç değer atama fonksiyonu
   def __init__(sınıf-kopya-değişkeni, param1, param2, ...):
         sınıf-kopya-değişkeni.param1 = ...
         sınıf-kopya-değişkeni.param2 = ...
         .
         .	   
		 
   # Normal sınıf fonksiyon bildirimleri 
   def fonksiyon-adı1(param1, param2, ...)
   def fonksiyon-adı2(param1, param2, ...)
   .
   .

```

* Türetilen sınıf içinde \_\_init\_\_() fonksiyonu tanımlandığında, ana sınıf \_\_init\_\_() fonksiyonunun yerini alarak bu fonksiyonu devre dışı bırakır. Ancak, ihtiyaç duyulursa ana sınıf \_\_init\_\_() fonksiyonu, ana sınıf adı ile birlikte nokta (.) karakteri kullanılarak, türetilen sınıf \_\_init\_\_() fonksiyonu içinden çağrılabilir.
* class satırından sonra tanımlanan değişken ve fonksiyonların yerine sadece pass anahtar kelimesi kullanıldığında, türetilen sınıf için herhangi bir değişken ve fonksiyon tanımlanmamış olur.

Şimdi, bir ana sınıftan türetilmiş bir sınıf oluşturulmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
class sinif_kitap:
   # Sınıf dışından erişim sağlanabilen değişken bildirimleri
   grup = 'Kitap'

   # Başlangıç değer atama fonksiyonu
   def __init__(self, kategori, adi, yazar):
       self.kategori = kategori
       self.adi = adi
       self.yazar = yazar
		 
   # Normal sınıf fonksiyon bildirimleri 
   def nesne_yazdir(self):
       print(self.grup + ', ' + self.kategori + ', ' + self.adi + ', ' + self.yazar)

class sinif_kitap_tur(sinif_kitap):
   
   # Başlangıç değer atama fonksiyonu
   def __init__(self, kategori, adi, yazar, yil, sayfa):
       super().__init__(kategori, adi, yazar)
       self.yil = yil
       self.sayfa = sayfa
		 
   # Normal sınıf fonksiyon bildirimleri 
   def kitap_yazdir(self):
       print(self.grup + ', ' + self.kategori + ', ' + self.adi + ', ' + self.yazar + ', ' + self.yil + ', ' + self.sayfa)

# Ana sınıf nesnesi oluşturma	   
nes = sinif_kitap('Roman', 'Çalıkuşu', 'Reşat Nuri Güntekin')
nes.nesne_yazdir()

# Türetilmiş sınıf nesnesi oluşturma
nes_tur = sinif_kitap_tur('Hikaye', 'Perili köşk', 'Ömer Seyfettin', '2016', '96')
nes_tur.nesne_yazdir() # Türetilmiş sınıf nesnesi yoluyla ana sınıf fonksiyonu çağırma
nes_tur.kitap_yazdir() # Ana sınıf ve türetilen sınıf içindeki değişkenleri yazdırma 


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Kitap, Roman, Çalıkuşu, Reşat Nuri Güntekin
Kitap, Hikaye, Perili köşk, Ömer Seyfettin
Kitap, Hikaye, Perili köşk, Ömer Seyfettin, 2016, 96

```

Program, grup adlı bir adet ortak değişken, üç parametreli bir \_\_init\_\_() fonksiyonu ve nesne değişken değerlerini ekrana yazan nesne\_yazdir() adlı bir fonksiyon içeren sinif\_kitap adlı bir sınıf bildirimi yapar. Sonra, sinif\_kitap sınıfından sinif\_kitap\_tur adlı bir sınıf oluşturur. Bu sınıf içinde, ana sınıf \_\_init\_\_() fonksiyonunu super() fonksiyonu ile çağıran ve yil ve sayfa adlı iki değişkene değer atayan bir \_\_init\_\_() fonksiyonu ile ana sınıf ve türetilen sınıf içindeki değişken değerlerini ekrana yazan kitap\_yazdir() adlı bir fonksiyon tanımlar.

Ana sınıftan nes adlı bir nesne oluştururken nesne değişkenlerine birer değer atar ve bu değerleri nesne\_yazdir() fonksiyonu ile ekrana yazar. Sonra, türetilmiş sınıftan nes\_tur adlı bir nesne oluştururken, ana sınıf ve türetilmiş sınıf değişkenlerine birer değer atar. Ana sınıf içinde yer alan değişkenleri nesne\_yazdir() fonksiyonu ile, ana sınıf ve türetilen sınıf içindeki değişkenlerin tamamını kitap\_yazdir() fonksiyonuyla ekrana yazar.
