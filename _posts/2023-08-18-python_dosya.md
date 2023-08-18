---
title: Python Dosya işlemleri
author: sonsuz
date: 2023-08-18 19:33:18 +0300
categories: [Program,Python]
tags: [python,programlama,dosya]
---





## Dosya açma ve kapama

Şimdi, dosya açma ve kapama işlemlerini incelemeye çalışacağız.

Bir dosya ile işlem yapmak istediğimizde, önce dosyayı açmamız, gerekli yazma ve/veya okuma işlemlerini gerçekleştirdikten sonra dosyayı kapatmamız gerekir. Dosya açma işlemi için aşağıda genel yapısı verilen open() fonksiyonu kullanılır.

```


dosya-nesnesi open(dosya-adı, mod);


```

dosya-adı
: Açılacak dosya adını gösterir. Tanımlanması zorunludur.

mod
: Dosyanın açılma şeklini gösterir. Tanımlanması isteğe bağlıdır. Tanımlanmadığında, ön tanımlı değer olan ve dosyanın sadece okuma amaçlı açılacağını gösteren 'r' değeri kullanılır.

dosya-nesnesi
: Dosya işlemlerinde kullanılacak olan dosya nesnesidir.

mod değerleri

| Mod | Anlamı |
| --- | --- |
| 'r' | Okuma için bir metin dosyası açar. Dosya mevcut olmalıdır. |
| 'w' | Yazma için bir metin dosyası oluşturur. Aynı isimde bir dosya zaten mevcut ise, içeriği silinir. |
| 'x' | Yazma için bir metin dosyası oluşturur. Aynı isimde bir dosya zaten mevcut ise, işlem gerçekleşmez. |
| 'a' | Bir metin dosyasını ekleme yapmak için açar. Dosya yok ise oluşturulur. |
| 'r+' | Okuma ve yazma için bir metin dosyası açar. Dosya mevcut olmalıdır. |
| 'w+' | Okuma ve yazma için bir metin dosyası oluşturur. |
| 'x+' | Okuma ve yazma için bir metin dosyası oluşturur. Aynı isimde bir dosya varsa, işlem gerçekleşmez. |
| 'a+' | Okuma ve ekleme için bir metin dosyası açar. |
| 'rb' | Okuma için bir ikili sistem dosyası açar. Dosya mevcut olmalıdır. |
| 'wb' | Yazma için bir ikili sistem dosyası oluşturur. Aynı isimde bir dosya zaten mevcut ise, içeriği silinir. |
| 'xb' | Yazma için bir ikili sistem dosyası oluşturur. Aynı isimde bir dosya zaten mevcut ise, işlem gerçekleşmez. |
| 'ab' | Bir ikili sistem dosyasını ekleme yapmak için açar. Dosya yok ise oluşturulur. |
| 'r+b' | Okuma ve yazma için bir ikili sistem dosyası açar. Dosya mevcut olmalıdır. |
| 'w+b' | Okuma ve yazma için bir ikili sistem dosyası oluşturur. |
| 'x+b' | Okuma ve yazma için bir ikili sistem dosyası oluşturur. Aynı isimde bir dosya varsa, işlem gerçekleşmez. |
| 'a+b' | Okuma ve ekleme için bir ikili sistem dosyası açar. |

w, x ve a modları kullanıldığında, mevcut olmayan dosya otomatik olarak oluşturulur.

Dosya kapatma işlemi için aşağıda genel yapısı verilen close() fonksiyonu kullanılır.

```py
dosya-nesnesi.close()


```

dosya-nesnesi: Daha önce dosya açma işleminde geri döndürülen dosya nesnesidir.

Bir dosyayı kapatma işleminin uygun bir şekilde yapılmasını sağlamak için, close() fonksiyonunu try-except-finally yapısı içinde kullanmak veya close() fonksiyonunun kullanılmasına gerek olmayan with yapısını kullanmak tercih edilmelidir.

Şimdi, open() ve close() fonksiyonlarının doğrudan kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
file = open("deneme.txt", "w")

file.close()


```

Yukarıdaki programı çalıştırdığımızda, open() fonksiyonu ile "deneme.txt" adlı bir metin dosyası oluşturur ve open() fonksiyonunun geri döndürdüğü file dosya nesnesi yoluyla close() fonksiyonunu kullanarak dosyayı kapatır.

Şimdi, open() ve close() fonksiyonlarının try-except-finally yapısı içinde kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
try:
    file = open("deneme.txt", "w")
    # Dosya işlemleri
except IOError:
    print("Dosya işlem hatası!")
finally:
    file.close()


```

Yukarıdaki programı çalıştırdığımızda, try bloğu içindeki open() fonksiyonu ile "deneme.txt" adlı bir metin dosyası oluşturur. Dosya ile ilgili işlemler tamamlandıktan sonra, finally bloğu içindeki open() fonksiyonunun geri döndürdüğü file dosya nesnesi yoluyla close() fonksiyonunu kullanarak dosyayı kapatır.

Mevcut olmayan bir dosyayı "r" modu ile açmak istersek, dosya açılmadığından, except bloğu içindeki karakter dizi ekrana yazılır ve finally bloğu içindeki file nesnesi oluşturulmamış olduğundan program hata verir. Eğer dosya işlemleri esnasında bir hata meydana gelirse, finally bloğu içindeki dosya kapatma işlemi normal çalışır.

Şimdi, open() fonksiyonunun with yapısı içinde kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
with open("deneme.txt", "w") as file:
     print("Dosya işlemleri")


```

Yukarıdaki programı çalıştırdığımızda, with bloğu içindeki open() fonksiyonu ile "deneme.txt" adlı bir metin dosyası oluşturur. Dosya ile ilgili işlemler tamamlandıktan sonra, dosya otomatik olarak kapatılır.

Bir dosya açma işlemi with yapısı içinde yapıldığında, dosya işlemleri sona erdiğinde, dosya otomatik olarak kapatılacağından, close() fonksiyonu kullanılmaz.

## Dosyaya veri yazma

Python'da dosyaya veri yazmak için iki farklı fonksiyon kullanılır:

```py
dosya-nesnesi.write(karakter-dizisi) # Dosyaya karakter dizisi yazar.

dosya-nesnesi.writelines(liste) # Dosyaya liste verileri yazar.


```

Şimdi, write() fonksiyonunu kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
with open("deneme.txt", "w") as file:
     file.write("Bir numaralı satır bilgileri")
     file.write("İki numaralı satır bilgileri")
     file.write("Üç numaralı satır bilgileri")	 


```

Yukarıdaki programı derleyip çalıştırdığımızda, içeriği aşağıdaki şekilde olan deneme.txt adlı bir dosya oluşturur:

```

Bir numaralı satır bilgileriİki numaralı satır bilgileriÜç numaralı satır bilgileri

```

Program çalıştığında, deneme.txt adlı bir metin dosyası oluşturur. Sonra, write() fonksiyonu ile üç karakter dizisini dosyaya yazar. Ancak, karakter dizilerinin sonuna yeni satır karakteri eklenmediğinden, karakter dizileri peşpeşe yazılır.

Şimdi, write() fonksiyonunu kullanılmasını, karakter dizilerinin sonuna yeni satır karakteri ekleyerek, bir örnek üzerinde yeniden incelemeye çalışalım:

Örnek

```py
with open("deneme.txt", "w") as file:
     file.write("Bir numaralı satır bilgileri\n")
     file.write("İki numaralı satır bilgileri\n")
     file.write("Üç numaralı satır bilgileri\n")	 


```

Yukarıdaki programı derleyip çalıştırdığımızda, içeriği aşağıdaki şekilde olan deneme.txt adlı bir dosya oluşturur:

```

Bir numaralı satır bilgileri
İki numaralı satır bilgileri
Üç numaralı satır bilgileri

```

Program çalıştığında, deneme.txt adlı bir metin dosyası oluşturur. Sonra, write() fonksiyonu ile üç karakter dizisini her biri bir satıra gelecek şekilde dosyaya yazar.

Şimdi, writelines() ve write() fonksiyonlarının kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
liste = ["aaaaa\n", "bbbbb\n", "ccccc\n",  "ddddd\n", "eeeee\n"]

# writelines() fonksiyonu ile listeyi dosyaya yazdırma 
with open("deneme01.txt", "w") as file:
     file.writelines(liste)

# write() fonksiyonu ile listeyi dosyaya yazdırma	 
with open("deneme02.txt", "w") as file:
     for deg in liste:
         file.write(deg) 


```

Yukarıdaki programı derleyip çalıştırdığımızda, içeriği aşağıdaki şekilde olan deneme01.txt ve deneme02.txt adlı iki dosya oluşturur:

```

aaaaa
bbbbb
ccccc
ddddd
eeeee

```

Program çalıştığında, deneme01.txt adlı bir metin dosyası oluşturur ve writelines() fonksiyonu ile listeyi dosyaya yazar. Sonra, deneme02.txt adlı bir metin dosyası oluşturur ve bir for döngüsü içinde write() fonksiyonunu kullanarak listeyi dosyaya yazar.

## Dosyadan veri okuma

Python'da dosyadan veri okumak için iki farklı fonksiyon kullanılır:

```py
dosya-nesnesi.read(boyut=-1) # Boyut parametre değeri kadar byte değeri dosyadan okur. Boyut parametresi tanımlanmaz veya -1 değeri alırsa tüm dosya okunur.

dosya-nesnesi.readline(boyut=-1) # Boyut parametre değeri kadar byte değeri satırdan okur. Boyut parametresi tanımlanmaz veya -1 değeri alırsa tüm satır okunur.

dosya-nesnesi.readlines() # Dosyadan okuduğu verileri liste olarak geri döndürür.


```

Şimdi, read() fonksiyonunun kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
# Dosya oluşturma
with open("deneme.txt", "w") as file:
     file.write("Bir numaralı satır bilgileri\n")
     file.write("İki numaralı satır bilgileri\n")
     file.write("Üç numaralı satır bilgileri\n")	
	 
# read() fonksiyonu ile dosya içeriğinin tamamını bir defada okuma	 
with open("deneme.txt", "r") as file:
     print(file.read())


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Bir numaralı satır bilgileri
İki numaralı satır bilgileri
Üç numaralı satır bilgileri

```

Program çalıştığında, deneme.txt adlı bir metin dosyası oluşturur ve write() fonksiyonu ile üç karakter dizisini her biri bir satıra gelecek şekilde dosyaya yazar. Program with yapısı dışına çıkar ve dosya otomatik olarak kapanır. Sonra, deneme.txt dosyası okuma modunda açılır ve dosya içeriğinin tamamı read() fonksiyonu okunarak ekrana yazılır.

Şimdi, readline() fonksiyonunun kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
# Dosya oluşturma
with open("deneme.txt", "w") as file:
     file.write("Bir numaralı satır bilgileri\n")
     file.write("İki numaralı satır bilgileri\n")
     file.write("Üç numaralı satır bilgileri\n")	
	 
# readline() fonksiyonu ile dosya içeriğini satır satır okuma
with open("deneme.txt", "r") as file:
     while True:
           line = file.readline()
           if not line:
              break
           print(line.strip())
		   
print()		   
		   
# Dosya içeriğini for döngüsü ile satır satır okuma
with open("deneme.txt", "r") as file:
     for line in file:
         print(line.strip()) 


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Bir numaralı satır bilgileri
İki numaralı satır bilgileri
Üç numaralı satır bilgileri

Bir numaralı satır bilgileri
İki numaralı satır bilgileri
Üç numaralı satır bilgileri

```

Program çalıştığında, deneme.txt adlı bir metin dosyası oluşturur ve write() fonksiyonu ile üç karakter dizisini her biri bir satıra gelecek şekilde dosyaya yazar. Program with yapısı dışına çıkar ve dosya otomatik olarak kapanır. Sonra, deneme.txt dosyası okuma modunda açılır ve readline() fonksiyonu ile dosya içeriği satır satır okunarak ekrana yazılır. Program with yapısı dışına çıkar ve dosya otomatik olarak kapanır. Daha sonra, deneme.txt dosyası okuma modunda tekrar açılır ve for döngüsü ile dosya içeriği satır satır okunarak ekrana yazılır.

Dosyadan okunan her bir satırın sonunda yer alan '\n' karakteri strip()  fonksiyonu ile silinir.

Şimdi, readlines() fonksiyonunun kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
liste = ["aaaaa\n", "bbbbb\n", "ccccc\n",  "ddddd\n", "eeeee\n"]

# writelines() fonksiyonu ile listeyi dosyaya yazdırma 
with open("deneme.txt", "w") as file:
     file.writelines(liste)

# readlines() fonksiyonu ile listeyi dosyadan okuyup ekrana yazdırma 
with open("deneme.txt", "r") as file:
     lines = file.readlines()
     print(lines) # Listenin tamamını ekrana yazdırma
     # Listeyi birer birer yazdırma
     for line in lines:
         print(line.strip())


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

['aaaaa\n', 'bbbbb\n', 'ccccc\n', 'ddddd\n', 'eeeee\n']
aaaaa
bbbbb
ccccc
ddddd
eeeee

```

Program çalıştığında, bir liste oluşturur. Oluşturduğu listeyi writelines() fonksiyonu ile deneme.txt adlı bir dosyaya yazar. Program with yapısı dışına çıkar ve dosya otomatik olarak kapanır. Sonra, deneme.txt dosyası okuma modunda açılır ve readlines() fonksiyonu ile okunan dosya içeriği line adlı listeye aktarılır. Önce, liste içeriğinin tamamı bir defada, sonra bir for döngüsü ile liste elemanları birer birer ekrana yazılır.

Dosyadan okunan her bir satırın sonunda yer alan '\n' karakteri strip() fonksiyonu ile silinir.

## Dosya kapatmadan veri okuma

Python'da bir dosyaya veri yazdıktan sonra, dosyayı kapatmadan yazılan verileri okumak için, dosyanın aktif konumu değiştirerek okuduğumuz verilerin bulunduğu konuma getirmemiz gerekir. Bu işlemleri yapmak için aşağıda genel yapıları verilen seek ve tell fonksiyonları kullanılır:

```py
dosya-nesnesi.seek(boyut [, yer])


```

Seek() fonksiyonu, dosya konumunu, yer parametresinin gösterdiği değerin belirlediği dosya konumuna göre, boyut parametresi kadar uzağa getirir.

İsteğe bağlı olarak tanımlanan yer parametresi aşağıdaki değerleri gösterilen alır:

0: Aramayı dosya başından başlatır (ön tanımlı değer).

1: Aramayı aktif konumdan başlatır.

2: Aramayı dosya sonundan başlatır.

```py
dosya-nesnesi.tell()


```

Tell() fonksiyonu dosyanın aktif konumunu geri döndürür.

Şimdi, dosya kapatmadan veri okuma işleminin seek() fonksiyonu kullanılarak yapılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
with open("deneme.txt", "w+") as file:
     file.write("Bir numaralı satır bilgileri\n")
     file.write("İki numaralı satır bilgileri\n")
     file.write("Üç numaralı satır bilgileri")	 

     print('Dosya konumu:', file.tell()) # Dosya konumunu alma	 
     # Bu fonksiyon kullanılmadığında dosya sonu olduğundan okuma işlemi yapılamaz.
     file.seek(0) # Dosyayı başa sarma 
     print('Dosya konumu:', file.tell()) # Dosya konumu	alma 
     print(file.read()) # Dosyanın tamamını okuma
     print('Dosya konumu:', file.tell()) # Dosya konumu	alma 


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Dosya konumu: 87
Dosya konumu: 0
Bir numaralı satır bilgileri
İki numaralı satır bilgileri
Üç numaralı satır bilgileri
Dosya konumu: 87

```

Program çalıştığında, deneme.txt adlı bir metin dosyası oluşturur ve write() fonksiyonu ile üç karakter dizisini her biri bir satıra gelecek şekilde dosyaya yazar. Sonra, tell() fonksiyonu ile dosya konumunu alıp ekrana yazar. Okuma işlemi yapabilmek için, seek() fonksiyonu ile dosyanın aktif konumunu başa alır. Dosya konumunu tekrar alarak ekrana yazar. Sonra, read() fonksiyonu dosyanın tamamını okur ve ekrana yazar. Dosya konumunu tekrar alarak ekrana yazar.

## Dosya silme

Python'da dosya silmek için os modülünde bulunan fonksiyonlar kullanılır.

Şimdi, dosya silme işlemini bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
import os

if os.path.exists("deneme.txt"): # Dosyanın mevcut olup olmadığını kontrol etme
   os.remove("deneme.txt") # Dosya silme
   print("Dosya silindi!")    
else:
   print("Dosya mevcut değil!") 


```

Yukarıdaki programı derleyip çalıştırdığımızda, programın bulunduğu dizinde "deneme.txt" adlı bir dosya varsa silinir, yoksa dosyanın mevcut olmadığını bildiren bir karakter dizisi ekrana yazılır.
