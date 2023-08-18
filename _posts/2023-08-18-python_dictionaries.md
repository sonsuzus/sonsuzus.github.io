---
title: Python Sözlükler
author: sonsuz
date: 2023-08-18 19:01:11 +0300
categories: [Program,Python]
tags: [python,programlama,sözlük]
---




## Sözlükler

Anahtar ve değer ikililerinden oluşan sıralanmamış verilerdir. Değere ulaşmak için anahtar adı kullanılır.

Sözlük içindeki verilerin aynı veri türünden olması gerekli değildir. Elemanlar düzenlidir ve elemanlarda değişiklik yapılabilir.

Sözlük oluşturmak için parantezler ({ }) içinde anahtar ve değerler ikilisi şeklinde veriler tanımlanır.

```py
değişken-adı = {
	anahtar1:değer1,
	anahtar2:değer2,
	anahtar3:değer3,
	.
	.
	.
} 


```

Sözlükler aşağıda gösterilen kurallara uygun olarak oluşturulur:

* Sözlük, aynı veya farklı veri türünden elemanlardan oluşabilir.
* Sözlük elemanları sıralıdır. İkililerin tanımlanma sırası değişmez.
* Sözlük verileri değiştirilebilir, silinebilir ve yeni eleman eklenebilir.
* Sözlük elemanları birbirinin aynı olamaz.
* Sözlük elemanlarına anahtar adı yoluyla anahtara karşılık gelen değere erişim sağlanır.

Şimdi, sözlük oluşturulmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
# Sözlük oluşturma
sozluk = {
	1:"aaa",
	2:"bbb",
	3:"ccc",
	"dort":"ddd",
	5:"eee"
} 

print(sozluk) # Sözlüğün tamamını yazdırma


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

{1: 'aaa', 2: 'bbb', 3: 'ccc', 'dort': 'ddd', 5: 'eee'}

```

Sözlükleri aşağıda genel yapısı gösterilen fromkeys fonksiyonu ile de oluşturabiliriz:

```py
sözlük-adı.fromkeys(anahtar-adı, değer) # Değer isteğe bağlı olarak tanımlanır.


```

Anahtar-adı mutlak tanımlanmalıdır. Değer isteğe bağlı olarak tanımlanır ve ön tanımlı değeri None'dır.

Örnek

```py
deg1 = (1, 2, 3, 4, 5)
deg2 = ("aaa")

sozluk = dict.fromkeys(deg1, deg2)

print(sozluk) # Sözlüğün tamamını yazdırma


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

{1: 'aaa', 2: 'aaa', 3: 'aaa', 4: 'aaa', 5: 'aaa'}

```

## Sözlük elemanlarına erişim

Sözlük elemanlarının değer bölümlerine erişim sağlamak için, [ ] işaretleri ile birlikte anahtar değerini veya get() fonksiyonunu kullanabiliriz.

```py
sözlük-adı[eleman-değeri]

sözlük-adı.get(anahtar-adı, değer) # Değer isteğe bağlı olarak tanımlanır.


```

Şimdi, sözlük elemanlarına erişim sağlama işlemini bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
sozluk = {
	1:"aaa",
	2:"bbb",
	3:"ccc",
	4:"ddd",
	5:"eee"
} 

print(sozluk[3]) # Sözlüğün 3 anahtar değerine karşılık gelen değeri yazdırma 
print(sozluk.get(5)) # Sözlüğün 5 anahtar değerine karşılık gelen değeri yazdırma 


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

ccc
eee

```

## Sözlük elemanlarını değiştirme ve sözlüğe eleman ekleme işlemleri

Sözlük elemanlarını değiştirme ve sözlüğe eleman ekleme işlemleri için, [ ] işaretleri ile birlikte anahtar değerini veya update() fonksiyonunu kullanabiliriz.

```py
sözlük-adı[eleman-değeri] = yeni-değer

sözlük-adı.update({anahtar-adı1:değer1, anahtar-adı2:değer2, ...}) 


```

Şimdi, sözlük elemanlarını değiştirme ve sözlüğe eleman ekleme işlemlerini bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
sozluk = {
	1:"aaa",
	2:"bbb",
	3:"ccc",
	4:"ddd",
	5:"eee"
} 

sozluk[4]= "ggg" # Sözlüğün 4 anahtar değerine karşılık gelen değeri değiştirme 
# Sözlüğün 1 ve 2 anahtar değerlerine karşılık gelen değerleri değiştirme
sozluk.update({1:"ttt", 2:"uuu"})

print(sozluk) # Sözlüğü komple yazdırma

sozluk[6]= "fff" # Sözlüğe 6 ve "fff" ikilisini ekleme
sozluk.update({7:"ggg", 2:"hhh"}) # Sözlüğe 2 adet ikili değer ekleme

print(sozluk) # Sözlüğü komple yazdırma


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

{1: 'ttt', 2: 'uuu', 3: 'ccc', 4: 'ggg', 5: 'eee'}
{1: 'ttt', 2: 'hhh', 3: 'ccc', 4: 'ggg', 5: 'eee', 6: 'fff', 7: 'ggg'}

```

## Sözlük silme işlemleri

Bir sözlükte yer alan elemanları birer birer silmek için pop(), popitem() fonksiyonları ile del anahtar kelimesini, sözlük içeriğini komple silmek için clear() fonksiyonunu ve sözlüğü tamamen silmek için del anahtar kelimesini kullanabiliriz. Fonksiyonların ve anahtar kelimenin genel yapısı aşağıda gösterilmektedir:

```py
sözlük-adı.pop(anahtar-değeri) # Anahtar değeri verilen eleman sözlükten silinir. 

sözlük-adı.popitem(anahtar-değeri) # Anahtar değeri verilen eleman sözlükten silinir. 

sözlük-adı.clear() # Sözlük içeriği tamamen silinir. 

del sözlük-adı # Sözlüğü komple siler.
del sözlük-adı[anahtar-değeri] # Anahtar değeri verilen eleman sözlükten silinir.


```

Şimdi, sözlük elemanlarını değiştirme ve sözlüğe eleman ekleme işlemlerini bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
sozluk = {
	1:"aaa",
	2:"bbb",
	3:"ccc",
	4:"ddd",
	5:"eee"
} 

sozluk.pop(3) # Anahtar adı verilen elemanı siler.
del sozluk[1] # Anahtar adı verilen elemanı siler.
sozluk.popitem() # Sözlüğün son elemanını siler.
print(sozluk)

sozluk.clear() # Sözlük içeriğini temizler.
print(sozluk)

del sozluk # Sözlüğü tamamen siler.


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

{2: 'bbb', 4: 'ddd'}
{}

```

## Sözlük anahtar ve değer ikililerini birlikte ve ayrı ayrı okuma

Bir sözlükte yer alan anahtar ve değer ikililerini birlikte okumak için item() fonksiyonunu, sadece anahtar değerlerini okumak için keys() fonksiyonunu ve sadece değerleri okumak için values() fonksiyonunu kullanabiliriz. Fonksiyonların genel yapıları aşağıda gösterilmektedir:

```py
sözlük-adı.items() # Sözlükteki anahtar-değer ikililerinin tamamını alır.

sözlük-adı.keys() # Sadece sözlükteki anahtar değerlerini alır.

sözlük-adı.values() # Sadece sözlükteki değerleri alır.


```

Şimdi, sözlük elemanlarını değiştirme ve sözlüğe eleman ekleme işlemlerini bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
sozluk = {
	1:"aaa",
	2:"bbb",
	3:"ccc",
	4:"ddd",
	5:"eee"
} 

print(sozluk.items())  # Anahtar-değer ikililerinin tamamını yazar.
print(sozluk.keys())   # Sadece anahtar değerlerini yazar.
print(sozluk.values()) # Sadece değerleri yazar.


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```py
dict_items([(1, 'aaa'), (2, 'bbb'), (3, 'ccc'), (4, 'ddd'), (5, 'eee')])
dict_keys([1, 2, 3, 4, 5])
dict_values(['aaa', 'bbb', 'ccc', 'ddd', 'eee'])

```

## Sözlük elemanlarının tamamına sırayla erişim

Bir sözlükte yer alan elemanlara sıra ile erişim sağlamak için döngüleri kullanabiliriz.

Şimdi, sözlük elemanlarına sıra ile erişim sağlamak için döngü kullanılmasını bir örnek üzerinde incelemeye çalışalım:

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

## Sözlükleri kopyalarak yeni bir sözlük oluşturma

Bir sözlüğü kopyalarak yeni bir sözlük oluşturmak için copy() ve dict() fonksiyonlarını kullanabiliriz. Fonksiyonların genel yapıları aşağıda gösterilmektedir:

```py
yeni-sözlük-adı = sözlük-adı.copy()

yeni-sözlük-adı = sözlük-adı.dict()


```

Şimdi, bir sözlüğü kopyalarak yeni bir sözlük oluşturulmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
sozluk = {
	1:"aaa",
	2:"bbb",
	3:"ccc",
	4:"ddd",
	5:"eee"
} 

sozluk2 = sozluk.copy()
print(sozluk2)

sozluk3 = dict(sozluk)
print(sozluk3) 


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

{1: 'aaa', 2: 'bbb', 3: 'ccc', 4: 'ddd', 5: 'eee'}
{1: 'aaa', 2: 'bbb', 3: 'ccc', 4: 'ddd', 5: 'eee'}

```

## İç içe sözlük oluşturma

Sözlükler içinde, aşağıda gösterildiği şekilde, sözlükler tanımlayarak iç içe sözlükler oluşturabiliriz.

```py
sozluk-ana = {
  "sozluk-alt1" : {
      anahtar1:değer-1,
	  anahtar2:değer-2,
	  .
	  .
	  .
  },
  "sozluk-alt2" : {
      anahtar1:değer-1,
	  anahtar2:değer-2,
	  .
	  .
	  .
  },
  .
  .
  .
} 


```

Şimdi, bir sözlüğü kopyalarak yeni bir sözlük oluşturulmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
sozlukana = {
  "sozlukalt1" : {
      1:"aaa",
      2:"bbb",
      3:"ccc"
  },
  "sozlukalt2" : {
      1:"aaa",
      2:"bbb",
      3:"ccc"
  },
  "sozlukalt3" : {
      1:"aaa",
      2:"bbb",
      3:"ccc"
  }
} 

print(sozlukana["sozlukalt1"][1])
print(sozlukana["sozlukalt3"][2])


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

aaa
bbb

```
