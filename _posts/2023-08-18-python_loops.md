---
title: Python Döngüler
author: sonsuz
date: 2023-08-18 19:10:17 +0300
categories: [Program,Python]
tags: [python,programlama,döngü,for,while]
---




## Döngüler

Python'da, tek bir işlem satırını veya kod bloğunu bir defadan fazla çalıştırmak için tekrar yazmak yerine, döngü kavramını kullanabiliriz. Bir veya birden fazla işlem satırını, bir koşula bağlı olarak, belirli sayıda veya bir koşul sağlandığı sürece tekrarlayarak çalıştıran kalıplara döngü adı verilir.

Döngüleri kullanarak liste, tuple, küme, sözlük veya bir karakter dizisinin elemanlarına birer birer erişim sağlayabiliriz.

Python'da, for ve while olmak üzere 2 farklı döngü kullanılmaktadır.

Bir döngü yapısında döngü içinde yer alan işlem satırları for veya while döngü satırının başlangıç sütunundan en az bir karakter ileriden başlamalıdır.

## for döngüsü

```

for değişken-adı in işlem-yapılacak-dizi-adı: 
      işlem-satırı
      .
      .

```

İşlem-yapılacak-dizi-adı, bir liste, tuple, küme, sözlük veya karakter dizisi olabilir.

Şimdi, for döngüsünün listelerle kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
liste = ["aaa", "bbb", "ccc", "ddd"]

# Liste elemanlarını for döngüsüyle tek tek yazdırma
for deg in liste:
    print(deg, end=' ')
	
print() # Satır aralığı verme	

# Liste elemanlarını for döngüsü ve endeksleme yöntemiyle yazdırma	
len = len(liste)
for deg in range(len):
    print(liste[deg], end=' ')


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

aaa bbb ccc ddd 
aaa bbb ccc ddd 

```

Şimdi, sözlük elemanlarına sıra ile erişim sağlamak için for döngüsü kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
sozluk = {
	1:"aaa",
	2:"bbb",
	3:"ccc",
	4:"ddd",
	5:"eee"
} 

print(sozluk) # Sözlüğü tek komutla yazdırma

# Sözlük anahtar değerlerini for döngüsüyle tek tek yazdırma
for deg in sozluk:
    print(deg, end=' ')
	
print()	# satır aralığı

# Sözlük değerlerini for döngüsüyle tek tek yazdırma
for deg in sozluk:
    print(sozluk[deg], end=' ') 

print()	# satır aralığı
	
# Sözlük anahtar değerlerini for döngüsüyle tek tek yazdırma
for deg in sozluk.keys():
    print(deg, end=' ') 

print()	# satır aralığı
	
# Sözlük değerlerini for döngüsüyle tek tek yazdırma
for deg in sozluk.values():
    print(deg, end=' ') 

print()	# satır aralığı
	
# Sözlük anahtar ve değerlerini for döngüsüyle tek tek yazdırma
for deg1, deg2 in sozluk.items():
    print(deg1, deg2, end=' ') 


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

{1: 'aaa', 2: 'bbb', 3: 'ccc', 4: 'ddd', 5: 'eee'}
1 2 3 4 5 
aaa bbb ccc ddd eee 
1 2 3 4 5 
aaa bbb ccc ddd eee 
1 aaa 2 bbb 3 ccc 4 ddd 5 eee 

```

Şimdi, for döngüsünün karakter dizileriyle kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
dizi = "Bilgisayar"

# Diziyi tek komutla yazdırma
print(dizi)

# Karakter dizisindeki karakterleri for döngüsüyle tek tek yazdırma
for deg in dizi:
    print(deg, end='')	


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Bilgisayar
Bilgisayar

```

Şimdi, for döngüsünün range veri türü ile kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
# range(başlangıç sayısı, son sayı, aralık)
# Başlangıç sayısı (ön tanımlı 0) ve aralık değerinin (ön tanımlı 1) tanımlanması isteğe bağlıdır.  

ran = range(4, 12) # Aralık değeri 1
print("Range içinde yer alan sayılar: ", end=': ')
for deg in ran:
    print(deg, end=' ')

print()

ran = range(-5, 12, 3) # Aralık değeri 3
print("Range içinde yer alan sayılar: ", end=': ')
for deg in ran:
    print(deg, end=' ')


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Range içinde yer alan sayılar: : 4 5 6 7 8 9 10 11 
Range içinde yer alan sayılar: : -5 -2 1 4 7 10 

```

## while döngüsü

```

değişken-adı
while değişken-adı karşılaştırma-işlemi: 
      işlem-satırı
      .
      .
	  değişken-artırma-azaltma	  

```

İşlem-yapılacak-dizi-adı, bir liste, tuple, küme, sözlük veya karakter dizisi olabilir.

Şimdi, while döngüsünün listelerle kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
liste = ["aaa", "bbb", "ccc", "ddd"]

# Liste elemanlarını while döngüsü ve endeksleme yöntemiyle yazdırma	  
len = len(liste)
deg = 0
while deg<len:
  print(liste[deg], end=' ')
  deg += 1  


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

aaa bbb ccc ddd 

```

Şimdi, sözlük elemanlarına sıra ile erişim sağlamak için while döngüsü kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
sozluk = {
	1:"aaa",
	2:"bbb",
	3:"ccc",
	4:"ddd",
	5:"eee"
} 

print(sozluk) # Sözlüğü tek komutla yazdırma

len = len(sozluk)

# Sözlük anahtar değerlerini while döngüsüyle tek tek yazdırma
keys = list(sozluk)
deg = 0
while deg<len:
  print(keys[deg], end=' ')
  deg += 1  

print()	# satır aralığı
  
# Sözlük değerlerini while döngüsüyle tek tek yazdırma
values = list(sozluk.values())
deg = 0
while deg<len:
  print(values[deg], end=' ')
  deg += 1   

print()	# satır aralığı
  
# Sözlük anahtar ve değerlerini while döngüsüyle tek tek yazdırma
items = list(sozluk.items())
deg = 0
while deg<len:
  print(items[deg], end=' ')
  deg += 1    


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

{1: 'aaa', 2: 'bbb', 3: 'ccc', 4: 'ddd', 5: 'eee'}
1 2 3 4 5 
aaa bbb ccc ddd eee 
(1, 'aaa') (2, 'bbb') (3, 'ccc') (4, 'ddd') (5, 'eee')  

```

Şimdi, while döngüsünün karakter dizileriyle kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
dizi = "Bilgisayar"

# Karakter dizisindeki karakterleri while döngüsü ve endeksleme yöntemiyle yazdırma	  
len = len(dizi)
deg = 0
while deg < len:
  print(dizi[deg], end='')
  deg += 1  	


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Bilgisayar

```

Şimdi, while döngüsünün range veri türü ile kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
# range(başlangıç sayısı, son sayı, aralık)
# Başlangıç sayısı (ön tanımlı 0) ve aralık değerinin (ön tanımlı 1) tanımlanması isteğe bağlıdır.  

ran = range(7, 15) # Aralık değeri 1
print("Range içinde yer alan sayılar: ", end=': ')
deg = 0
while deg < len(ran):
  print(ran[deg], end=' ')
  deg += 1	
	
print()

ran = range(-6, 18, 4) # Aralık değeri 4
print("Range içinde yer alan sayılar: ", end=': ')
deg = 0
while deg < len(ran):
  print(ran[deg], end=' ')
  deg += 1	


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Range içinde yer alan sayılar: : 7 8 9 10 11 12 13 14 
Range içinde yer alan sayılar: : -6 -2 2 6 10 14

```

## break ifadesi

Bir döngü içinde, bir koşula bağlı olarak kullanılan break ifadesi tanımlanırsa, koşul gerçekleştiğinde, while satırında tanımlanan koşula veya for satırındaki sıraya göre işlem devam etse bile, döngü sona erer.

Şimdi, break ifadesinin kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
liste = ["aaa", "bbb", "ccc", "ddd", "eee"]

# Liste elemanlarını for döngüsüyle tek tek yazdırma
for deg in liste:
    if deg=="ccc":
       break
    print(deg, end=' ')
	
print() # Satır aralığı verme	

# Liste elemanlarını while döngüsü ve endeksleme yöntemiyle yazdırma	  
len = len(liste)
deg = 0
while deg<len:
  if liste[deg]=="ddd":
     break
  print(liste[deg], end=' ')
  deg += 1


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

aaa bbb 
aaa bbb ccc 

```

Program, her iki döngü ile de listenin tamamını yazdırması gerekirken, for döngüsü içinde liste eleman değeri "ccc" olduğunda ve while döngüsü içinde liste eleman değeri "ddd" olduğunda break ifadesi ile döngü sona erer. Böylece, liste elemanları break ifadesi koşulunda belirtilen eleman değerine kadar ekrana yazılır.

## continue ifadesi

Bir döngü içinde, bir koşula bağlı olarak kullanılan continue ifadesi tanımlanırsa, koşul gerçekleştiğinde, while satırında tanımlanan koşula veya for satırındaki sıraya göre işlem devam etse bile, döngünün o tekrarı devre dışı bırakılır ve bir sonraki tekrardan devam edilir.

Şimdi, continue ifadesinin kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
liste = ["aaa", "bbb", "ccc", "ddd", "eee"]

# Liste elemanlarını for döngüsüyle tek tek yazdırma
for deg in liste:
    if deg=="ccc":
       continue
    print(deg, end=' ')
	
print() # Satır aralığı verme	

# Liste elemanlarını while döngüsü ve endeksleme yöntemiyle yazdırma	  
len = len(liste)
deg = 0
while deg<len:
  if liste[deg]=="ddd":
     deg += 1
     continue
  print(liste[deg], end=' ')
  deg += 1


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

aaa bbb ddd eee 
aaa bbb ccc eee 

```

Program, her iki döngü ile de listenin tamamını yazdırması gerekirken, for döngüsü içinde liste eleman değeri "ccc" olduğunda ve while döngüsü içinde liste eleman değeri "ddd" olduğunda continue ifadesi ile aktif tekrar devre dışı kalır ve eleman değeri ekrana yazılmaz.

## Döngülerde else kullanımı

Bir for döngüsü sona erdiğinde ve bir while döngüsü koşulu doğru sonuç vermediğinde, döngüler içinde break ifadesi kullanılmamışsa, çalışmasını istediğimiz işlem satırı veya kod bloğunu içerir.

Şimdi, döngüler ile else else ifadesinin kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
liste = ["aaa", "bbb", "ccc", "ddd", "eee"]

# Liste elemanlarını for döngüsüyle tek tek yazdırma
for deg in liste:
    print(deg, end=' ')
else:
    print() # Satır aralığı verme
    print("Liste içeriği ekrana yazıldı!") 	
	
print() # Satır aralığı verme	

# Liste elemanlarını while döngüsü ve endeksleme yöntemiyle yazdırma	  
len = len(liste)
deg = 0
while deg<len:
  print(liste[deg], end=' ')
  deg += 1
else:
  print() # Satır aralığı verme
  print("Döngü koşulu artık sağlanmıyor!")   


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

aaa bbb ccc ddd eee 
Liste içeriği ekrana yazıldı!

aaa bbb ccc ddd eee 
Döngü koşulu artık sağlanmıyor!

```

Program, for ve while döngüleri sona erdiğinde döngülere bağlı else satırları ile birer karakter dizisinin ekrana yazar.

## İç içe döngü tanımlama

Bir for döngüsü sona erdiğinde ve bir while döngüsü koşulu doğru sonuç vermediğinde, döngüler içinde break ifadesi kullanılmamışsa, çalışmasını istediğimiz işlem satırı veya kod bloğunu içerir.

Şimdi, döngüler ile else else ifadesinin kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
liste = ["aaa", "bbb", "ccc", "ddd", "eee"]

# Liste elemanlarını for döngüsüyle tek tek yazdırma
for deg1 in liste:
    print(deg1, end=' ')
    for deg2 in deg1:
        print(deg2, end='')
    print()		
	
print() # Satır aralığı verme	

# Liste elemanlarını while döngüsü ve endeksleme yöntemiyle yazdırma	  
len1 = len(liste)
deg1 = 0
while deg1<len1:
  print(liste[deg1], end=' ')
  len2 = len(liste[deg1])
  deg2=0  
  while deg2<len2:
    print(liste[deg1][deg2], end='')
    deg2 += 1
  print()	
  deg1 += 1


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

aaa aaa
bbb bbb
ccc ccc
ddd ddd
eee eee

aaa aaa
bbb bbb
ccc ccc
ddd ddd
eee eee

```

Program, içi içe for ve while döngüleri ile liste elemanlarını önce tek komutla sonra birer birer ekrana yazar.
