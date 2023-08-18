---
title: Python Kümeler (Sets)
author: sonsuz
date: 2023-08-18 18:57:59 +0300
categories: [Program,Python]
tags: [python,programlama,küme,set]
---




## Kümeler

Küme, birden fazla değerin yer aldığı bir yapıdır. Küme içindeki verilerin aynı veri türünden olması gerekli değildir. Elemanlar düzenli değildir ve elemanlarda değişiklik yapılamaz.

Küme oluşturmak için parantezler ({ }) veya set() fonksiyonu kullanılır.

```py
küme-adı = ("deger01", "deger02", "deger03") # { } ile küme oluşturma

küme-adı = set(("deger01", "deger02", "deger03")) # set() fonksiyonu ile kümes oluşturma


```

Kümeler aşağıda gösterilen kurallara uygun olarak oluşturulur:

* Küme, aynı veya farklı veri türünden elemanlardan oluşabilir.
* Küme elemanları sıralı değildir. Elemanların tanımlanma sırası değişebilir.
* Küme elemanlarının değerleri değiştirilemez, ancak silinebilir ve yeni eleman eklenebilir.
* Küme elemanları birbirinin aynı olamaz.
* Küme elemanlarına erişim endeksleme ile sağlanamaz, for döngüleri ile sağlanır.

Şimdi, küme oluşturulmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
# { } ile küme oluşturma
kume1 = {"aaa", "bbb", "ccc", "ddd"}
kume2 = {21, 35, 54, 82}

# set() fonksiyonu ile tuple oluşturma
kume3 = set((7, 15, 24, 43))

# Küme yazdırma
print(kume1)
print(kume2)
print(kume3)


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

{'bbb', 'aaa', 'ddd', 'ccc'}
{82, 35, 21, 54}
{24, 43, 15, 7}

```

## Küme elemanlarının tamamına sırayla erişim

Bir küme içindeki elemanlara sıra ile erişim sağlamak için döngüleri kullanabiliriz.

Şimdi, küme elemanlarına sıra ile erişim sağlamak için döngü kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
kume1 = {"aaa", "bbb", "ccc",  "ddd", "eee"}

print(kume1) # Kümeyi tek komutla yazdırma

# Küme elemanlarını for döngüsüyle tek tek yazdırma
for deg in kume1:
    print(deg, end=' ')


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

{'ddd', 'eee', 'aaa', 'bbb', 'ccc'}
ddd eee aaa bbb ccc 

```

## Kümeye bir veya birden fazla eleman ekleme

Bir kümeye bir eleman eklemek için add() fonksiyonunu ve birden fazla eleman eklemek için iki kümeyi birleştiren union ve update fonksiyonlarını kullanabiliriz. Fonksiyonların genel yapısı aşağıda gösterilmektedir:

```py
küme-adı.add(eleman-değeri) # Eleman-değeri gereklidir. Eleman varsa eklenmez.

oluşturulacak-küme = küme-adı.union(küme1, küme2, ...) # Bir veya daha fazla küme elemanından yeni bir küme oluşturma

ekleme-yapılacak-küme-adı.update(eklenecek-küme-adı) # Farklı bir kümeden eleman alarak bir kümeyi günceller.


```

union() ve update() fonksiyonları benzer elemanlardan sadece birisini alır.

Şimdi, bir kümeye bir veya birden fazla eleman ekleme işlemini bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
kume1 = {1, 2, 3, 4}
kume2 = {6, 7, 8, 9, 10}

# add() fonksiyonu ile kümeye eleman ekleme
kume1.add(5)
print(kume1) 

# union() fonksiyonu ile bir kümeye farklı kümeleri ekleme
kume3 = kume1.union(kume2)
print(kume3) 

# update() fonksiyonu ile bir kümeye birden fazla eleman ekleme
kume1.update(kume2)
print(kume1) 


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

{1, 2, 3, 4, 5}
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

```

## Bir kümeden başka bir küme oluşturma

Bir kümeden başka bir küme oluşturmak için aşağıda genel yapısı gösterilen copy() fonksiyonunu kullanabiliriz:

```py
yeni-küme-adı = küme-adı.copy() # Bir kümenin elemanlarını kopyalayarak yeni bir küme oluşturur.


```

Şimdi, bir kümeden başka bir küme oluşturma işlemini bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
kume1 = {"aaa", "bbb", "ccc", "ddd"}

# copy() fonksiyonu ile bir kümeden başka bir küme oluşturma
kume2 = kume1.copy()
print(kume2) 


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

{'ccc', 'ddd', 'bbb', 'aaa'}

```

## Kümeler arasındaki benzerlik ve farklılık işlemleri

Kümeler arasındaki benzerlik ve farklılık işlemlerini gerçekleştirmek için aşağıda genel yapıları ve açıklamaları verilen fonksiyonları kullanabiliriz:

```py
# İlk kümede olan ve ikinci kümede olmayan elemanlardan yeni bir küme oluşturur.
yeni-küme-adı = ilk-küme-adı.difference(ikinci-küme-adı) 

# Sadece ilk kümede olan ve ikinci kümede olmayan elemanlarla ilk küme içeriğini günceller. 
ilk-küme-adı.difference_update(ikinci-küme-adı) 

# İlk küme ile diğer kümeler arasındaki ortak elemanlardan yeni bir küme oluşturur.
yeni-küme-adı = ilk-küme-adı.intersection(ikinci-küme-adı, üçüncü-küme-adı, ...) 

# İlk küme ile diğer kümeler arasındaki ortak elemanlarla ilk küme içeriğini günceller.  
ilk-küme-adı.intersection_update(ikinci-küme-adı, üçüncü-küme-adı, ...) 

# Her iki kümede ortak eleman bulunmuyorsa True, bulunuyorsa False bir değer geri döndürür.
değişken-adı = ilk-küme-adı.isdisjoint(ikinci-küme-adı) 

# İlk kümenin tüm elemanları ikinci kümede bulunuyorsa True, bulunmuyorsa False bir değer geri döndürür.
değişken-adı = ilk-küme-adı.issubset(ikinci-küme-adı) 

# İlk küme ikinci kümenin tüm elemanlarını içeriyorsa True, içermiyorsa False bir değer geri döndürür.
değişken-adı = ilk-küme-adı.issuperset(ikinci-küme-adı) 

# Her iki kümede ortak olmayan elemanlardan yeni bir küme oluşturur.
yeni-küme-adı = ilk-küme-adı.symmetric_difference(ikinci-küme-adı) 

# Her iki kümede ortak olmayan elemanlarla ilk küme içeriğini günceller. 
ilk-küme-adı.symmetric_difference_update(ikinci-küme-adı)


```

Şimdi, kümeler arasındaki benzerlik ve farklılık işlemlerini bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
kume1 = {"aaa", "bbb", "ccc", "ddd", "eee", "fff", "ggg"}
kume2 = {"hhh", "bbb", "iii", "ddd", "jjj", "fff", "kkk"}

# kume1'de olan ve kume2'de olmayan elemanlardan yeni bir küme oluşturur.
kume3 = kume1.difference(kume2)
print(kume3) 

# kume1'de olan ve kume2'de olmayan elemanlarla kume1 içeriğini günceller.
kume1.difference_update(kume2)
print(kume1) 

kume1 = {"aaa", "bbb", "ccc", "ddd", "eee", "fff", "ggg"}

# kume1 ile kume2 arasındaki ortak elemanlardan yeni bir küme oluşturur.
kume3 = kume1.intersection(kume2)
print(kume3) 

# kume1 ile kume2 arasındaki ortak elemanlarla kume1 içeriğini günceller.
kume1.intersection_update(kume2)
print(kume1) 

# Her iki kümede ortak eleman bulunmuyorsa True, bulunuyorsa False bir değer geri döndürür.
print(kume1.isdisjoint(kume2))

# kume1'in tüm elemanları kume2'de bulunuyorsa True, bulunmuyorsa False bir değer geri döndürür.
print(kume1.issubset(kume2))

# kume1 kume2'nin tüm elemanlarını içeriyorsa True, içermiyorsa False bir değer geri döndürür.
print(kume1.issuperset(kume2))

# Her iki kümede ortak olmayan elemanlardan yeni bir küme oluşturur.
kume3 = kume1.symmetric_difference(kume2)
print(kume3) 
 
# Her iki kümede ortak olmayan elemanlarla kume1 içeriğini günceller. 
kume1.symmetric_difference_update(kume2)
print(kume1)


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

{'ggg', 'eee', 'ccc', 'aaa'}
{'eee', 'aaa', 'ccc', 'ggg'}
{'ddd', 'fff', 'bbb'}
{'ddd', 'fff', 'bbb'}
False
True
False
{'jjj', 'iii', 'kkk', 'hhh'}
{'hhh', 'jjj', 'iii', 'kkk'}

```

## Küme eleman silme ve içerik temizleme işlemleri

Bir kümede eleman değeri tanımlayarak eleman silmek için remove() ve discard()fonksiyonlarını, kümenin sonundaki elemanı silmek için pop() fonksiyonunu, küme içeriğini komple silmek için clear() fonksiyonunu ve kümeyi silmek için del anahtar kelimesini kullanabiliriz. Fonksiyon ve anahtar kelimenin genel yapısı aşağıda gösterilmektedir:

```py
küme-adı.remove(eleman-değeri) # Elemanı siler. Eleman-değeri gereklidir. Eleman yoksa hata verir.

küme-adı.discard(eleman-değeri) # Elemanı siler. Eleman-değeri gereklidir. Eleman yoksa hata vermez.

küme-adı.pop() # Rastgele bir eleman siler.

küme-adı.clear() # Küme içeriğini komple siler.

del küme-adı # Kümeyi komple siler.


```

Şimdi, bir küme eleman silme ve içerik temizleme işlemlerini bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
kume = {"aaa", "bbb", "ccc", "ddd", "eee", "fff", "ggg"}

# remove() fonksiyonu ile kümeden eleman silme
kume.remove("ccc")
print(kume) 

# discard() fonksiyonu ile kümeden eleman silme
kume.discard("fff")
print(kume) 

# pop() fonksiyonu ile kümeden rastgele bir eleman silme
kume.pop()
print(kume) 

# clear() fonksiyonu küme içeriğini silme
kume.clear()
print(kume) 

# del anahtar kelimesi kümeyi komple silme
del kume


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

{'fff', 'ddd', 'aaa', 'ggg', 'eee', 'bbb'}
{'ddd', 'aaa', 'ggg', 'eee', 'bbb'}
{'aaa', 'ggg', 'eee', 'bbb'}
set()

```
