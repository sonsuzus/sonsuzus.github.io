---
title: Python Listeler
author: sonsuz
date: 2023-08-18 18:46:06 +0300
categories: [Program,Python]
tags: [python,programlama,liste,eleman,dizi]
---





## Listeler

Liste, birden fazla değerin yer aldığı bir yapıdır. Listede yer alan verilerin aynı veri türünden olması gerekli değildir. Elemanlarda değişiklik yapılabilir.

Liste oluşturmak için köşeli parantezler ([ ]) veya list() fonksiyonu kullanılır.

```py
liste-adı = ["deger01", "deger02", "deger03"] # [ ] ile liste oluşturma

liste-adı = list(("deger01", "deger02", "deger03")) # list() ile liste oluşturma


```

Listeler aşağıda gösterilen kurallara uygun olarak oluşturulur:

* Liste, aynı veya farklı veri türünden elemanlardan oluşabilir.
* Liste elemanları sıralıdır. Eleman tanımlanma sırası değişmez. Yeni elemanlar listenin sonuna eklenir.
* Liste elemanları değiştirilebilir, silinebilir ve listeye yeni eleman eklenebilir.
* Liste elemanları birbirinin aynı olabilir.
* Liste elemanlarına 0'dan başlamak üzere endeksleme ile erişim sağlanır.

Şimdi, liste oluşturulmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
# [ ] ile liste oluşturma
liste1 = ["Bilgisayar", "Programlama", "Yazılım"]
liste2 = [21, 35, 54, 82, 117]

# list() ile liste oluşturma
liste3 = [7, 15, 24, 43] 

# Listeleri yazdırma
print(liste1)
print(liste2)
print(liste3)


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

['Bilgisayar', 'Programlama', 'Yazılım']
[21, 35, 54, 82, 117]
[7, 15, 24, 43, 57]

```

## Liste elemanlarına erişim

Liste elemanlarına birer birer erişmek için, [ ] işaretleri ile birlikte 0'dan başlayan endeks yöntemini kullanabiliriz. Bir sıra dahilindeki birden fazla liste elemanına erişim sağlamak için, [ ] işaretleri ile : işaretini kullanabiliriz.

Şimdi, liste elemanlarına erişim sağlama işlemini bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
liste = ["aaa", "bbb", "ccc",  "ddd", "eee"]

print(liste[0])   # Listenin ilk elemanını yazdırma 
print(liste[1])   # Listenin ikinci elemanını yazdırma 
print(liste[-1])  # Listenin son elemanını yazdırma 
print(liste[-2])  # Listenin sondan ikinci elemanını yazdırma 

print(liste[:3])  # Listenin 1.elemanından 4.elemanına kadar yazdırma
print(liste[2:])  # Listenin 3.elemanından itibaren yazdırma
print(liste[1:4]) # Listenin 2.elemanından 5.elemanına kadar yazdırma


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

aaa
bbb
eee
ddd
['aaa', 'bbb', 'ccc']
['ccc', 'ddd', 'eee']
['bbb', 'ccc', 'ddd']

```

## Liste elemanlarında değişiklik yapma

Liste elemanlarını değiştirebilir ve listeye yeni eleman ekleyebiliriz. Liste elemanlarında bu işlemleri yapmak için, [ ] işaretleri ile birlikte 0'dan başlayan endeks yöntemini, bir sıra dahilindeki birden fazla liste elemanına erişim sağlamak için, [ ] işaretleri ile : işaretini veya append(), insert() ve extend() fonksiyonlarını kullanabiliriz. Bu fonksiyonların genel yapısı aşağıda gösterilmektedir:

```py
liste-adı.append(eleman-değeri) # Listenin sonuna bir eleman ekler.

liste-adı.insert(endeks, eleman-değeri) # Listede belirli bir endekse bir eleman ekler.

liste-adı.extend(eklenecek-liste) # Bir listenin sonuna diğer bir listeyi ekler.


```

Şimdi, liste elemanlarını değiştirme ve listeye yeni eleman ekleme işlemlerinin [ ] ve : işaretleri ile yapılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
liste = ["aaa", "bbb", "ccc",  "ddd", "eee"]

liste[2] = "Program" # 3.elemanı değiştirme
print(liste) # Liste elemanlarını yazdırma 

liste[0:2] = [21, 35.17] # İlk iki elemanı değiştirme
print(liste) # Liste elemanlarını yazdırma 

liste[2:3] = ["kkk", "mmm"] # Listenin 3.elemanı yerine 2 eleman yerleştirme 
print(liste) # Liste elemanlarını yazdırma 

liste[4:] = ["ppp"] # Listenin son iki elmanı yerine tek bir eleman ekleme
print(liste) # Liste elemanlarını yazdırma


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

['aaa', 'bbb', 'Program', 'ddd', 'eee']
[21, 35.17, 'Program', 'ddd', 'eee']
[21, 35.17, 'kkk', 'mmm', 'ddd', 'eee']
[21, 35.17, 'kkk', 'mmm', 'ppp']

```

Şimdi, listeye yeni eleman ekleme işlemlerinin append(), insert() ve extend() fonksiyonları ile yapılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
liste = ["aaa", "bbb", "ccc",  "ddd", "eee"]

liste.append("kkk") # Listenin sonuna eleman ekleme
print(liste) # Liste elemanlarını yazdırma 

liste.insert(2, "ppp") # Listenin 3.elemanı olarak eleman ekleme
print(liste) # Liste elemanlarını yazdırma 

liste2 = ["ttt", "uuu", "vvv"]
liste.extend(liste2) # liste2 elemanlarını list sonuna ekleme
print(liste) # Liste elemanlarını yazdırma 


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'kkk']
['aaa', 'bbb', 'ppp', 'ccc', 'ddd', 'eee', 'kkk']
['aaa', 'bbb', 'ppp', 'ccc', 'ddd', 'eee', 'kkk', 'ttt', 'uuu', 'vvv']

```

## Liste elemanlarını silme

Bir listede yer alan elemanları silmek için remove() ve pop() fonksiyonları ile del anahtar kelimesini, liste içeriğini komple silmek için clear() fonksiyonunu ve listeyi tamamen silmek için del anahtar kelimesini kullanabiliriz. Fonksiyonların ve anahtar kelimenin genel yapısı aşağıda gösterilmektedir:

```py
liste-adı.pop(endeks) # Endeks sıra numarasındaki eleman silinir. 

liste-adı.remove(eleman-değeri) # Değeri verilen eleman listeden silinir.

liste-adı.clear() # Liste içeriği komple silinir.

del liste-adı # Listeyi komple siler.
del liste-adı[endeks] # Endeks ile gösterilen elemanı siler.


```

Şimdi, liste elemanlarını değiştirme ve listeye yeni eleman ekleme işlemlerinin [ ] ve : işaretleri ile yapılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
liste = ["aaa", "bbb", "ccc",  "ddd", "eee", "fff"]

liste.remove("ccc") # "ccc" değeri içeren elemanı listeden silme
print(liste) # Liste elemanlarını yazdırma 

liste.pop(2) # 3.elemanı silme
print(liste) # Liste elemanlarını yazdırma 

del liste[1] # Listenin 2.elemanını silme 
print(liste) # Liste elemanlarını yazdırma 

liste.clear() # Liste içeriğini silme
print(liste) # Liste elemanlarını yazdırma

del liste # Listeyi tamamen silme


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

['aaa', 'bbb', 'ddd', 'eee', 'fff']
['aaa', 'bbb', 'eee', 'fff']
['aaa', 'eee', 'fff']
[]

```

## Liste elemanlarının tamamına sırayla erişim

Bir listede yer alan elemanlara sıra ile erişim sağlamak için döngüleri kullanabiliriz.

Şimdi, liste elemanlarına sıra ile erişim sağlamak için döngü kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
liste = ["aaa", "bbb", "ccc",  "ddd", "eee"]

print(liste) # Listeyi tek komutla yazdırma

# Liste elemanlarını for döngüsüyle tek tek yazdırma
for deg in liste:
    print(deg, end=' ')
	
print() # Satır aralığı verme	

# Liste elemanlarını for döngüsü ve endeksleme yöntemiyle yazdırma	
len = len(liste)
for deg in range(len):
  print(liste[deg], end=' ')
  
print() # Satır aralığı verme  
  
# Liste elemanlarını while döngüsü ve endeksleme yöntemiyle yazdırma	  
deg = 0
while deg < len:
  print(liste[deg], end=' ')
  deg += 1  


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

['aaa', 'bbb', 'ccc', 'ddd', 'eee']
aaa bbb ccc ddd eee 
aaa bbb ccc ddd eee 
aaa bbb ccc ddd eee 

```

## Bir Listeden yeni bir liste oluşturma

Bir listede yeni bir liste oluşturmak için, for döngüsü ve kapsam yöntemi ile aşağıda genel yapısı gösterilen copy() ve list() fonksiyonlarını kullanabiliriz.

```py
yeni-liste-adı = liste-adı.copy() # Bir listenin tamamı diğer bir listeye aktarılır. 

yeni-liste-adı = list(liste-adı) # # Bir listenin tamamı diğer bir listeye aktarılır.


```

* for döngüsü: Bir liste içeriğinin tamamı veya koşula bağlı olarak bir kısmı aktarılarak yeni bir liste oluşturulur.
* Kapsam yöntemi: Bir liste içeriğinin tamamı veya koşula bağlı olarak bir kısmı aktarılarak yeni bir liste oluşturulur.
* copy() fonksiyonu: Bir liste elemanlarının tamamı kopya edilerek yeni bir liste oluşturulur.
* list() fonksiyonu: Bir liste elemanlarının tamamından yeni bir liste oluşturulur.

Kapsam yöntemi ile bir listeden yeni bir liste oluşturmak için kullanılan genel yapı aşağıda gösterilmektedir. Bu yapıda, if koşulunun tanımlanması isteğe bağlıdır.

```py
yeni-liste-adı = [ifade for liste-eleman-değişkeni in önceki-liste-adı if koşul]


```

Şimdi, bir listeden yeni bir liste oluşturma işlemlerini bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
liste1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
liste2 = []

# liste1 içeriğinin tamamını list2 içine aktarma
for deg in liste1:
    liste2.append(deg)
print(liste2)	

liste2.clear() # liste2 elemanlarını silme

# liste1 içeriğinden 5'den büyük olanları list2 içine aktarma
for deg in liste1:
    if deg > 5:
       liste2.append(deg)
print(liste2)

# Kapsam yöntemiyle liste oluşturma
liste2 = [deg for deg in liste1]
print(liste2) 

# Kapsam yöntemiyle koşul tanımlayarak liste oluşturma
liste2 = [deg for deg in liste1 if deg > 5]
print(liste2) 

# copy() fonksiyonu ile liste oluşturma
liste2 = liste1.copy()
print(liste2)

# list() fonksiyonu ile liste oluşturma
liste2 = list(liste1)
print(liste2)


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

[1, 2, 3, 4, 5, 6, 7, 8, 9]
[6, 7, 8, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[6, 7, 8, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 9]

```

## Listeleri birleştirme

İki listeyi birleştirmek için, + işlemcisi, for döngüsü veya aşağıda genel yapısı verilen extend() fonksiyonunu kullanabiliriz.

```py
ekleme-yapılacak-liste-adı.extend(eklenecek-liste-adı) # Bir listenin tamamı diğer bir listeye eklenir. 


```

Şimdi, iki listeyi birleştirme işlemlerini bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
liste1 = [1, 2, 3, 4, 5]
liste2 = [6, 7, 8, 9, 10]

# + işlemcisi ile listeleri birleştirme
liste3 = liste1 + liste2
print(liste3) 

# for döngüsü ile listeleri birleştirme
for deg in liste2:
    liste1.append(deg)
print(liste1) 

# extend() fonksiyonu ile listeleri birleştirme
liste1.extend(liste2)
print(liste1)


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 6, 7, 8, 9, 10]

```

## Listeleri sıralama

Bir listeyi sıralamak için, aşağıda genel yapısı verilen sort() fonksiyonunu kullanabiliriz.

```py
liste-adı.sort(reverse=True|False, key=sıralama-fonksiyonu)


```

Her iki parametre isteğe bağlı olarak tanımlanır. reverse parametresinin ön tanımlı değeri False olup artan değerde sıralama yapar. True değeri verildiğinde ise, azalan değerde sıralama yapar. key parametresi sıralama fonksiyonu tanımlar.

Şimdi, iki listeyi birleştirme işlemlerini bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
liste1 = [4, 2, 5, 1, 3]
liste2 = ["ddd", "aaa", "eee", "ccc", "bbb"]

# Sayılardan oluşan listeyi sıralama
liste1.sort()
print(liste1)

# Harflerden oluşan listeyi sıralama
liste2.sort()
print(liste2)

# Sayılardan oluşan listeyi tersten sıralama
liste1.sort(reverse = True)
print(liste1)

# Harflerden oluşan listeyi tersten sıralama
liste2.sort(reverse = True)
print(liste2)


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

[1, 2, 3, 4, 5]
['aaa', 'bbb', 'ccc', 'ddd', 'eee']
[5, 4, 3, 2, 1]
['eee', 'ddd', 'ccc', 'bbb', 'aaa']

```

## Listeyi tersine çevirme

Bir listedeki elemanları tersine çevirmek için aşağıda genel yapısı verilen reverse() fonksiyonunu kullanabiliriz.

```py
liste-adı.reverse()


```

Şimdi, bir listedeki elemanları tersine çevirme işlemlerini bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
liste1 = [1, 2, 3, 4, 5]
liste2 = ["aaa", "bbb", "ccc", "ddd", "eee"]

# Sayılardan oluşan listeyi reverse() fonksiyonu ile tersine çevirme
liste1.reverse()
print(liste1)

# Harflerden oluşan listeyi reverse() fonksiyonu tersine çevirme
liste2.reverse()
print(liste2)


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

[1, 2, 3, 4, 5]
['aaa', 'bbb', 'ccc', 'ddd', 'eee']
[5, 4, 3, 2, 1]
['eee', 'ddd', 'ccc', 'bbb', 'aaa']

```

## Listedeki bir eleman değerinin endeksini ve sayısını alma

Bir listedeki eleman değerinin endeksini almak için index() fonksiyonunu ve kaç adet olduğunu belirlemek için count() fonksiyonunu kullanabiliriz. Bu fonksiyonların genel yapısı aşağıda gösterilmektedir:

```py
liste-adı.index(eleman-değeri) 

liste-adı.count(eleman-değeri) 


```

Şimdi, bir listedeki eleman değerinin endeksini almak ve kaç adet olduğunu belirlemek için yapılan işlemleri bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
liste = [1, "aaa", 2, "bbb", 3, "ccc", 4, "ddd", 3]

# Elemanların endeksini alma
print(liste.index("bbb"))
print(liste.index(4))

# Listede kaç adet 3 değeri olduğunu belirleme
print(liste.count(3))


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

3
6
2

```
