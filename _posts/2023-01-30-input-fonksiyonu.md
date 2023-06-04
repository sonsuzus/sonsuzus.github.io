---
title: Python input fonksiyonu
author: sonsuz
date: 2023-01-30 22:00:00 +0300
categories: [Python]
tags: [programlama,input,python,fonksiyon]
---

``input()`` bir fonksiyondur dedik. Henüz fonksiyon kavramının ayrıntılarını
öğrenmemiş olsak da, şimdiye kadar pek çok fonksiyon gördüğümüz için artık bir
fonksiyonla karşılaştığımızda bunun nasıl kullanılacağını az çok tahmin
edebiliyoruz. Tıpkı düşündüğünüz ve yukarıdaki örnekten de gördüğünüz gibi,
birer fonksiyon olan ``type()``, ``print()``, ``len()`` ve ``open()``
fonksiyonlarını nasıl kullanıyorsak ``input()`` fonksiyonunu da öyle
kullanacağız.

Dilerseniz lafı daha fazla uzatmadan örnek bir program yazalım::

    isim = input("İsminiz nedir? ")

    print("Merhaba", isim, end="!\n")

Bu programı kaydedip çalıştırdığınızda, sorulan soruya verdiğiniz cevaba göre
çıktı farklı olacaktır. Örneğin eğer bu soruya 'Niyazi' cevabını vermişseniz
çıktınız `Merhaba Niyazi!` şeklinde olacaktır.

Görüyorsunuz ya, tıpkı daha önce gördüğümüz fonksiyonlarda olduğu gibi,
``input()`` fonksiyonunda da parantez içine bir parametre yazıyoruz. Bu
fonksiyona verilen parametre, kullanıcıdan veri alınırken kullanıcıya sorulacak
soruyu gösteriyor. Gelin isterseniz bir örnek daha yapalım elimizin alışması
için::

    yaş = input("Yaşınız: ")

    print("Demek", yaş, "yaşındasın.")
    print("Genç mi yoksa yaşlı mı olduğuna karar veremedim.")

``input()`` fonksiyonunun ne kadar kullanışlı bir araç olduğu ortada. Bu
fonksiyon sayesinde, şimdiye kadar tek sesli bir şekilde yürüttüğümüz
programcılık faaliyetlerimizi çok sesli bir hale getirebileceğiz. Mesela önceki
bölümlerden birinde yazdığımız, daire alanı hesaplayan programı hatırlarsınız. O
zaman henüz dosyalarımızı kaydetmeyi ve ``input()`` fonksiyonunu öğrenmediğimiz
için o programı etkileşimli kabukta şu şekilde yazmıştık::

    >>> çap = 16
    >>> yarıçap = çap / 2
    >>> pi = 3.14159
    >>> alan = pi * (yarıçap * yarıçap)
    >>> alan

    201.06176

Ama artık hem dosyalarımızı kaydetmeyi biliyoruz, hem de ``input()``
fonksiyonunu öğrendik. Dolayısıyla yukarıdaki programı şu şekilde yazabiliriz::

    #Kullanıcıdan dairenin çapını girmesini istiyoruz.
    çap = input("Dairenin çapı: ")

    #Kullanıcının verdiği çap bilgisini kullanarak
    #yarıçapı hesaplayalım. Buradaki int() fonksiyonunu
    #ilk kez görüyoruz. Biraz sonra bunu açıklayacağız
    yarıçap = int(çap) / 2

    #pi sayımız sabit
    pi = 3.14159

    #Yukarıdaki bilgileri kullanarak artık
    #dairenin alanını hesaplayabiliriz
    alan = pi * (yarıçap * yarıçap)

    #Son olarak, hesapladığımız alanı yazdırıyoruz
    print("Çapı", çap, "cm olan dairenin alanı: ", alan, "cm2'dir")

Gördüğünüz gibi, ``input()`` fonksiyonunu öğrenmemiz sayesinde artık yavaş yavaş
işe yarar programlar yazabiliyoruz.

Ancak burada, daha önce öğrenmediğimiz bir fonksiyon dikkatinizi çekmiş olmalı.
Bu fonksiyonun adı ``int()``. Bu yeni fonksiyon dışında, yukarıdaki bütün
kodları anlayabilecek kadar Python bilgisine sahibiz.

``int()`` fonksiyonunun ne işe yaradığını anlamak için isterseniz ilgili satırı
``yarıçap = çap / 2`` şeklinde yazarak çalıştırmayı deneyin bu programı.

Dediğim gibi, eğer o satırdaki ``int()`` fonksiyonunu kaldırarak programı
çalıştırdıysanız şuna benzer bir hata mesajı almış olmalısınız::

    Traceback (most recent call last):
      File "deneme.py", line 8, in <module>
        yarıçap = çap / 2
    TypeError: unsupported operand type(s) for /: 'str' and 'int'

Gördüğünüz gibi programımız bölme işlemini yapamadı. Buradan anlıyoruz ki, bu
``int()`` fonksiyonu programımızdaki aritmetik işlemin düzgün bir şekilde
yapılabilmesini sağlıyor. Gelelim bu fonksiyonun bu işlevi nasıl yerine
getirdiğini incelemeye.

## Tip Dönüşümleri


Bir önceki bölümün sonunda verdiğimiz örnek programda ``int()`` adlı bir
fonksiyon görmüş, bu fonksiyonu anlatmayı o zaman ertelemiştik. Çok gecikmeden,
bu önemli fonksiyonun ne işe yaradığını öğrenmemiz gerekiyor. İsterseniz bir
örnek üzerinden gidelim.

Diyelim ki kullanıcıdan aldığı sayının karesini hesaplayan bir program yazmak
istiyoruz. Öncelikle şöyle bir şey deneyelim::

    sayı = input("Lütfen bir sayı girin: ")

    #Girilen sayının karesini bulmak için sayı değişkeninin 2.
    #kuvvetini alıyoruz. Aynı şeyi pow() fonksiyonu ile de
    #yapabileceğimizi biliyorsunuz. Örn.: pow(sayı, 2)
    print("Girdiğiniz sayının karesi: ", sayı ** 2)

Bu kodları çalıştırdığımız zaman, programımız kullanıcıdan bir sayı girmesini
isteyecek, ancak kullanıcı bir sayı girip `Enter` tuşuna bastığında şöyle bir
hata mesajıyla karşılaşacaktır::

    Traceback (most recent call last):
      File "test.py", line 5, in <module>
        print("Girdiğiniz sayının karesi: ", sayı ** 2)
    TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'

Hata mesajına baktığınızda, 'TypeError' ifadesinden, bunun veri tipine ilişkin
bir hata olduğunu tahmin edebilirsiniz. Eğer İngilizce biliyorsanız yukarıdaki
hata mesajının anlamını rahatlıkla çıkarabilirsiniz. İngilizce bilmeseniz de en
sondaki 'str' ve 'int' kelimeleri size karakter dizisi ve sayı adlı veri
tiplerini hatırlatacaktır. Demek ki ortada veri tiplerini ilgilendiren bir sorun
var...

Peki burada tam olarak neler dönüyor?

Hatırlayacaksınız, geçen derslerden birinde ``len()`` fonksiyonunu anlatırken
şöyle bir şey söylemiştik:

    Biz henüz kullanıcıdan nasıl veri alacağımızı bilmiyoruz. Ama şimdilik şunu
    söyleyebiliriz: Python'da kullanıcıdan herhangi bir veri aldığımızda, bu
    veri bize bir karakter dizisi olarak gelecektir.

Gelin isterseniz yukarıda anlattığımız durumu teyit eden bir program yazalım::

    #Kullanıcıdan herhangi bir veri girmesini istiyoruz
    sayı = input("Herhangi bir veri girin: ")

    #Kullanıcının girdiği verinin tipini bir
    #değişkene atıyoruz
    tip = type(sayı)

    #Son olarak kullanıcının girdiği verinin tipini
    #ekrana basıyoruz.
    print("Girdiğiniz verinin tipi: ", tip)

Bu programı çalıştırdığımızda ne tür bir veri girersek girelim, girdiğimiz
verinin tipi `str`, yani karakter dizisi olacaktır. Demek ki gerçekten de,
kullanıcıdan veri almak için kullandığımız ``input()`` fonksiyonu bize her
koşulda bir karakter dizisi veriyormuş.

Geçen derslerde şöyle bir şey daha söylemiştik:

    Python'da, o anda elinizde bulunan bir verinin hangi tipte olduğunu bilmek
    son derece önemlidir. Çünkü bir verinin ait olduğu tip, o veriyle neler
    yapıp neler yapamayacağınızı belirler.

Şu anda karşı karşıya olduğumuz durum da buna çok güzel bir örnektir. Eğer o
anda elimizde bulunan verinin tipini bilmezsek tıpkı yukarıda olduğu gibi, o
veriyi programımızda kullanmaya çalışırken programımız hata verir ve çöker.

Her zaman üstüne basa basa söylediğimiz gibi, aritmetik işlemler yalnızca
sayılarla yapılır. Karakter dizileri ile herhangi bir aritmetik işlem yapılamaz.
Dolayısıyla, ``input()`` fonksiyonundan gelen veri bir karakter dizisi olduğu
için ve biz de programımızda girilen sayının karesini hesaplamak amacıyla bu
fonksiyondan gelen verinin `2.` kuvvetini, yani karesini hesaplamaya
çalıştığımız için programımız hata verecektir.

Yukarıdaki programda neler olup bittiğini daha iyi anlayabilmek için Python'ın
etkileşimli kabuğunda şu işlemleri yapabiliriz::

    >>> "23" ** 2

    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'

Gördüğünüz gibi, programımızdan aldığımız hata ile yukarıdaki hata tamamen aynı
(hata mesajlarında bizi ilgilendiren kısım en son satırdır). Tıpkı burada olduğu
gibi, hata veren programda da 'Lütfen bir sayı girin: ' sorusuna örneğin `23`
cevabını verdiğimizde programımız aslında ``"23" ** 2`` gibi bir işlem yapmaya
çalışıyor. Bir karakter dizisinin kuvvetini hesaplamak mümkün olmadığı, kuvvet
alma işlemi yalnızca sayılarla yapılabileceği için de hata vermekten başka
çaresi kalmıyor.

Ancak bazen öyle durumlarla karşılaşırsınız ki, programınız hiçbir hata vermez,
ama elde edilen sonuç aslında tamamen beklentinizin dışındadır. Mesela şu basit
örneği inceleyelim::

    sayı1 = input("Toplama işlemi için ilk sayıyı girin: ")
    sayı2 = input("Toplama işlemi için ikinci sayıyı girin: ")

    print(sayı1, "+", sayı2, "=", sayı1 + sayı2)
