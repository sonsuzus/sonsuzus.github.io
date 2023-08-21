---
title:  Python Basit Kod Örnekleri 
author: sonsuz
date: 2023-08-21 15:43:35 +0300
categories: [Program,Python]
tags: [python,algoritma,programlama,kod,örnek]
---



Bir programlama dilini öğrenmenin en iyi yöntemi örnekler üzerinden kodları inceleyerek çalışmaktır. Python dilinde de aynı yöntemleri izleyerek kodlama deneyiminizi arttırabilirsiniz. 

Bu sayfa Python’un temel kavramlarına ve tkinter GUI arayüzüne ilişkin örnekler içerir. **Çözüme bakmadan önce bu örnekleri kendi başınıza denemenizi öneririm.**

**Örnek 1:** Ekranda “Merhaba Dünya” yazdıran Python Örneği

```py
print("Merhaba Dünya")
```

**Örnek 2:** Kullanıcının İsmini Alarak Merhaba (kullanıcı ismi) Yazdıran Python Örneği

```py
isim = input('İsminizi Girin : ')
print("Merhaba "+isim)
```

**Örnek 3:** Girilen 2 Sayıyı Toplayan Python Örneği

```py
sayi1 = input('1. Sayı : ')
sayi2 = input('1. Sayı : ')
toplam=float(sayi1)+float(sayi2)
print("Toplam :{0} ".format(toplam))
```

**Örnek 4:** Girilen 2 Sayının Ortalamasını Bulan Python Örneği

```py
sayi1 = input('1. Sayı : ')
sayi2 = input('1. Sayı : ')
ortalama=(int(sayi1)+int(sayi2))/2
print("Ortalama :{0} ".format(ortalama))
```

**Örnek 5:** Girilen Vize ve Final Notu Ortalaması Hesaplayan Python Örneği

```py
vize = input('Vize Notunuz : ')
final = input('Final Notunuz : ')
ortalama=(float(vize)*0.3)+(float(final)*0.7)
print("Ortalama :{0} ".format(ortalama))
```

**Örnek 6:** Girilen 3 Yazılı Notunun Ortalamasını Bulan Python Örneği

```py
y1 = input('1. Yazılı : ')
y2 = input('2. Yazılı : ')
y3 = input('3. Yazılı : ')
ortalama=(float(y1)+float(y2)+float(y3))/3
print("Ortalama :{0} ".format(ortalama))
```

**Örnek 7:** Yazılı Ortalaması Girilen Öğrencinin Sınıf Geçme Durumunu (GEÇTİ – KALDI) Gösteren Python Örneği

```py
ort = input('Ortalamanızı Girin : ')
if(int(ort)>=50):
 print("Geçtiniz")
else:
 print("Kaldınız")
```

**Örnek 8: Girilen Sayının Tek mi Çift mi Olduğunu Bulan Python Örneği.**

```py
sayi = input('Sayı : ')
if(int(sayi)%2==0):
 print("Sayı Çift")
else:
 print("Sayı Tek")

```

**Örnek 9:** Girilen Sayının Pozitif, Negatif, ya da 0 Olduğunu Bulan Python Örneği

```py
sayi = input('Sayı : ')
if(int(sayi)<0):
 print("Sayı Negatif")
elif(int(sayi)>0):
 print("Sayı Pozitif")
else:
 print("Sayı Sıfır")

```

**Örnek 10:** Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle indeksini (VKİ=ağırlık/(boy*boy), boymetre cinsinden verilmeli) hesaplayınız. 

VKİ 18 ile < 25 aralığındaysa normal, VKİ 25 ile <30 aralığındaysa kilolu, VKİ 30 ve daha yüksekse obez, VKİ 35 ve daha fazlaysa ciddi obez olarak kabul edilir. VKİ’ni hesaplayarak kişinin durumunu yazdırınız

```py
print("VÜCUT KİTLE ENDEKSİ HESAPLAMA PROGRAMI 💪")
boy = float(input("Boy (m):"))
kilo = int(input("Kilo (kg):"))
 
endeks = kilo/(boy*boy)
 
if endeks <=18:
 print("\n zayıf VKİ:{}".format(endeks))
elif endeks > 18 and endeks <=25 :
 print("\n kilolu VKİ:{}".format(endeks))
elif endeks > 25 and endeks <=30:
 print("\n obez VKİ:{}".format(endeks))
elif endeks > 30:
 print("\n ciddi obez VKİ:{}".format(endeks))

```

**Örnek 11:** Yaşı Girilen Kişinin Ehliyet Alıp Alamayacağını Gösteren Python Örneği

```py
yas = input('Yaşınız : ')
if(int(yas)&lt;18):
 print("Yaşınız Ehliyet almak İçin Uygun Değil")
else:
 print("Yaşınız Ehliyet almak İçin Uygun")

```

**Örnek 12:** 1-100 Arası Sayıları Ekranda Listeleyen Python Örneği.

```py
for i in range(1,101):
 print(i)

```

**Örnek 13:** 1-100 arası Çift Sayıları Listeleyen Python Örneği.

```py
for i in range(1,101):
 if i%2==0:
 print(i)

```

**Örnek 14:** 1-100 Arası Tek Sayıları Listeleyen Python Örneği

```py
for i in range(1,101):
 if i%2!=0:
 print(i)

```

**Örnek 15:** 1-100 Arası 3′ e ve 5′ e tam bölünen sayıları bulan Python Örneği

```py
for i in range(1,101):
 if i%3==0 or i%5==0:
 print(i)

```

**Örnek 16:** 1 den Kullanıcının Girdiği Sayıya Kadar Sayıları Listeleyen Python Örneği

```py
sayi=input('Sayıyı Gir : ')
for i in range(1,int(sayi)+1):
 print(i)

```

**Örnek 17:** Kenarları Girilen Dikdörtgenin Alanı ve Çevresini Bulan Python Örneği

```py
kisa=input('Kısa Kenar : ')
uzun=input('Uzun Kenar : ')
alan=int(kisa)*int(uzun)
cevre=2*(int(kisa)+int(uzun))
print("Alan : {0}".format(alan))
print("Çevre : {0}".format(cevre))

```

**Örnek 18:** Girilen metnin harflerini alt alta yazdıran Python Örneği

```py
isim=input("Adınızı Girin ")
sayac=0
while sayac < len(isim):
 print(isim[sayac])
 sayac += 1
else:
 print("Adının harflerini listeledim.")

```

**Örnek 19:** Kullanıcın girdiği iki sayı arasındaki sayıların toplamını gösteren Python Örneği.

```py
toplam=0;
sayi1=input('1. Sayı: ')
sayi2=input('2. Sayı: ')
for i in range(int(sayi1)+1,int(sayi2)):
 toplam+=i
print("{0} ile {1} arasındaki sayıların toplamı : {2}".format(sayi1,sayi2,toplam))

```

**Örnek 20:** Kullanıcıya sinema ya da tiyatro tercihi sorulsun. Sinema izlemek için 15 TL, tiyatro için 10 TL ödenmesi gerekmedir. Öğrencilere %50 indirim yapıldığı düşünülerek öğrenci ise indirim yapılan; öğrenci değilse indirimsiz tutarı hesaplayarak ekrana yazdıran kodu yazınız.

```py

secim = input("Sinema için (1), Tiyatro için (2) tuşlayınız : ")
ogrenci = input("Öğrenci misiniz(E/H) : ")
ucret = 0

#indirimsiz ücret hesaplama
if secim == '1':
 ucret = 15 #sinema
elif secim == '2':
 ucret = 10 #tiyatro

#öğrenci indirimi
if ogrenci =='E' or ogrenci =='e':
 ucret=ucret / 2 #%50

print("Ödemeniz gereken ücret :{}".format(ucret))

```

**Örnek 21:** Girilen Sayının Asal Sayı mı Değil mi olduğunu bulan Python Örneği

```py
sayac=0
sayi=input('Sayı: ')
for i in range(2,int(sayi)):
 if(int(sayi)%i==0):
 sayac+=1
 break
if(sayac!=0):
 print("Sayı Asal Değil")
else:
 print("Sayı Asal")

```

**Örnek 22:** 1 den kullanıcının girmiş olduğu sayıya kadar olan tek ve çift sayıların toplamını ayrı ayrı bulan ve sonucu ekranda gösteren Python Örneği

```py
sayi = input('Sayıyı Girin : ')
tekToplam=0
ciftToplam=0
for i in range(1,int(sayi)):
 if(i%2==0):
 ciftToplam+=i
 else:
 tekToplam+=i
print("Tek Sayıların Toplamı : {0}".format(tekToplam))
print("Çift Sayıların Toplamı : {0}".format(ciftToplam))

```

**Örnek 23:** Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda gösteren Python örneği:

```py
yeniMaas=0
maas=input("Maaşı Gir : ")
zam=input("Zam Oranı(%) : ")
yeniMaas=int(maas)+(int(maas)*int(zam)/100)
print("Zamlı Maaş :",yeniMaas)

```

**Örnek 24**: Fonksiyon kullanarak yarıçapı girilen dairenin alanını hesaplayan Python örneği:

```py
def daireAlan(yaricap):
 alan = float(yaricap) * float(yaricap)*3.14
 print ("Alan :",alan)
 return alan

r = input("Yarıçapı Gir :")

daireAlan(r)

```

**Örnek 25**: Fonksiyon kullanarak genişliği ve yüksekliği girilen dikdörtgenin alanını hesaplayan Python örneği:

```py
def dikdortgenAlan(genislik, yukseklik):
 alan = float(genislik) * float(yukseklik)
 print ("Alan :",alan)
 return alan
 
gen = input("Genişlik :")
 
yuk = input("Yükseklik : ")
 
dikdortgenAlan(gen, yuk)

```

**Örnek 26**: Python ile Sayı Tahmin Oyunu Yapımı.

```py
from random import randint
 
rand=randint(1, 100)
sayac=0
 
while True:
 sayac+=1
 sayi=int(input("1 ile 100 arasında değer girin (0 çıkış):"))
 if(sayi==0):
 print("Oyunu İptal Ettiniz")
 break
 elif sayi < rand:
 print("Daha Yüksek Bir Sayı Girin.")
 continue
 elif sayi > rand:
 print("Daha Düşük Bir Sayı Girin.")
 continue
 else:
 print("Rastele seçilen sayı {0}!".format(rand))
 print("Tahmin sayınız {0}".format(sayac))

```

**Örnek 27**: Verilen bir tarihin yılın kaçıncı günü olduğunu bulan Python Örneği.

```py
def ArtıkYıl(yıl):
 artık=False
 if yıl%400==0 or (yıl%4==0 and yıl%100!=0): artık=True
 return artık
 
def YılınGünü(Ay,Gün,Yıl):
 günler=[31,28,31,30,31,30,31,31,30,31,30,31]
 if ArtıkYıl(Yıl):
 günler[1]=29
 sıra=0
 for a in range(Ay-1):
 sıra+=günler[a]
 sıra+=Gün
 return sıra

print(YılınGünü(4,9,2023))

```

**Örnek 28**: Python ile bir liste içinde 5’in katları olan sayıları listeleme.

```py
sayilar = [18,22,15,85,65,30,10,20,32,34,28,101,5,4,32]
sayac=0 
for sayi in sayilar:
 if sayi%5 == 0:
 print (str(sayi)+ (" : 5'in katıdır."))
 sayac=sayac+1
else:
 print ('Döngü Bitti')
print("5'in katı olan sayı adeti : "+str(sayac))

```

**Örnek 29:** Bir string içerisinde belirlenen bir karakterin olup olmadığını kontrol eden Python programı kodları. Kontrol etme işlemi fonksiyon içinde yapılmıştır.

```py
def kontrol(str):
 sayac = 0
 for ch in str:
 if ch == 'ğ':
 sayac = sayac + 1
 return True
 break
 
 
metin=input('Metin : ')
if(kontrol(metin)==True):
 print('ğ karakteri metin içinde var')
else:
 print('ğ karakteri metin içinde yok')

```

**Örnek 30:** Kullanıcının girdiği 2 sayı arasındaki çift sayıların ortalamasını bulan Python örneği. Sayının çift olup olmadığı fonksiyon ile kontrol ediliyor.

```py
def ciftMi(x): 
 return x % 2 == 0

toplam=0
sayac=0
baslangic = input("Başlangıç Sayısı :")
bitis = input("Bitiş Sayısı :")
for sayi in range (int(baslangic), int(bitis)+1):
 if(ciftMi(int(sayi))):
 toplam=toplam+sayi
 sayac=sayac+1
print('Ortalama',(toplam/sayac))

```

**Örnek 31:**  Python 3 Veri tabanından kayıt okuma

```py
import pymysql.cursors

# Veritabanı bağlantı cümlesi
connection = pymysql.connect(host='localhost',
 user='root',
 password='',
 db='ogrenciler',
 charset='utf8mb4',
 cursorclass=pymysql.cursors.DictCursor)
try:
 with connection.cursor() as cursor:
 # tek satır okuma
 sql = "SELECT `id`, `firstname`,`lastname` FROM `users`"
 cursor.execute(sql)
 
 for row in cursor.fetchall():
 #tüm satırları okuma
 firstname = str(row["firstname"])
 lastname = str(row["lastname"])

 #ekrana yazdırma
 print("İsim : " + firstname)
 print("Soyisim : " + lastname)

finally:
 connection.close()


```

**Örnek 32:** Python Tkinter  Form Kullanımı

```py
import tkinter

nesne = tkinter.Tk()
nesne.mainloop()

```

**Örnek  33:** Python Form Entry Kullanımı

```py
from tkinter import *

from tkinter import messagebox

pencere = Tk()

pencere.title("sonsuzus")
pencere.geometry("400x300")

#grid form çizdirme
uygulama = Frame(pencere)
uygulama.grid()


L1 = Label(uygulama, text="Adınızı Girin")
L1.grid(padx=110, pady=10)

E1 = Entry(uygulama, bd =2)
E1.grid(padx=110, pady=3)

#formu çiz
pencere.mainloop()

```

**Örnek 34:** Python Tkinter ListBox Kullanımı

```py
from tkinter import *

from tkinter import messagebox

pencere = Tk()

pencere.title("sonsuzus")
pencere.geometry("400x300")

#grid form çizdirme
uygulama = Frame(pencere)
uygulama.grid()

Lb1 = Listbox(uygulama)
Lb1.insert(1, "Python")
Lb1.insert(2, "C#")
Lb1.insert(3, "JAVA")
Lb1.insert(4, "JAVASCRIPT")
Lb1.grid(padx=110, pady=10)

#formu çiz
pencere.mainloop()

```

**Örnek 35:** Python Fonksiyon Kullanarak Dikdörtgen Alanı Hesaplama Python Kodları:

```py
def dikdortgenAlan(genislik, yukseklik):
 alan = float(genislik) * float(yukseklik)
 print ("Alan :",alan)
 return alan

gen = input("Genişlik :")

yuk = input("Yükseklik : ")

dikdortgenAlan(gen, yuk)

```

**Örnek 36:** Kullanıcının tuttuğu sayıyı tahmin eden python örneği

```py
from random import randint
 
rand=randint(1, 100)
sayac=0
 
while True:
 sayac+=1
 sayi=int(input("1 ile 100 arasında değer girin (0 Çıkış):"))
 if(sayi==0):
 print("Oyunu İptal Ettiniz")
 break
 elif sayi < rand:
 print("Daha Yüksek Bir Sayı Girin.")
 continue
 elif sayi > rand:
 print("Daha Düşük Bir Sayı Girin.")
 continue
 else:
 print("Rastele seçilen sayı {0}!".format(rand))
 print("Tahmin sayınız {0}".format(sayac))

```

**Örnek 37:** Kullanıcının girdiği n adet sayıdan tek ve çift olanların ayrı ayrı ortalamasını hesaplayan ve ekranda gösteren Python Kodları:

```py
tekAdet=0
ciftAdet=0
tekToplam=0
ciftToplam=0

n=int(input("Kaç Adet Sayı Girilecek : "))
for i in range(n):
 sayi=int(input("Sayı : "))
 if(sayi%2==0):
 tekAdet+=1
 tekToplam+=sayi
 else:
 ciftAdet+=1
 ciftToplam+=sayi
if(tekAdet!=0):#Eğer hiç tek sayı girilmemişse 0'a bölme hatası verecektir.
 print("Tek Sayıların Ortalaması : ",tekToplam/tekAdet)
if(ciftAdet!=0):#Eğer hiç çift sayı girilmemişse 0'a bölme hatası verecektir.
 print("Çift Sayıların Ortalaması : ",ciftToplam/ciftAdet)

```

**Örnek 38:** En sevdiğiniz 3 meyveyi liste hâline getirerek ekrana yazdırınız.

```py
meyveler=["Elma","Armut","Portakal"]

print("En Sevdiğim Meyveler {}".format(meyveler))

```

**Örnek 39:** Sırasıyla pi sayısı, inç biriminin cm olarak karşılığı, mikroişlemcilerin kısaltması, kullandığınız işletim sisteminin adı ve 48 bitin byte olarak karşılığını bir liste hâline getirerek ekrana yazdırınız.

```py
# Sırasıyla pi sayısı, inç biriminin cm olarak karşılığı, mikroişlemcilerin kısaltması, kullandığınız işletim sisteminin adı ve 48 bitin byte olarak karşılığını bir liste hâline getirerek ekrana yazdırınız. 
liste=[3.14,2.54,"CPU","WINDOWS 10",6]

print(liste)

```

**Örnek 40:** Haftanın günlerinden Pazartesi ile başlayan ve Cuma ile biten bir liste oluşturunuz. Oluşturduğunuz listenin indeksi 4 olan elemanını ekrana yazdırınız.

```py
#Haftanın günlerinden Pazartesi ile başlayan ve Cuma ile biten bir liste oluşturunuz. Oluşturduğunuz listenin indeksi 4 olan elemanını ekrana yazdırınız.

liste=["Pazartesi","Salı","Çarşamba","Perşembe","Cuma"]
print(liste[4])

```

**Örnek 41: Aşağıdaki kodun çıktısını yazınız (Python’da tek karakterden oluşan değerleri tek tırnak (‘) içinde tanımlayabilirsiniz.).** ders=[‘K’,’O’,’D’,’L’,’A’,’M’,’A’]

```py
ders=['K','O','D','L','A','M','A']
print(ders)

```
