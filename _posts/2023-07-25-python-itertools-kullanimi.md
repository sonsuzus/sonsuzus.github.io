---
title:  Python itertools kullanımı
author: sonsuz
date: 2023-07-25 01:19:51 +0300
categories: [Program,Python]
tags: [python,programlama,veri,döngü,itertools,count,cycle,repeat,kombinasyon,permütasyon]
---

Python'un Itertool'u, karmaşık döngüler üretmek için döngüler ve listeler üzerinde çalışan çeşitli işlevler sağlayan bir modüldür .

Bu modül, yineleyici cebiri oluşturmak için kendi başına veya kombinasyon halinde kullanılan hızlı, belleği verimli kullanan bir araç olarak çalışır . 

Örneğin, iki liste olduğunu ve bunların öğelerini çarpmak istediğinizi varsayalım. Bunu başarmanın birkaç yolu olabilir. Naif yaklaşım, yani her iki listenin öğelerini aynı anda yineleyerek ve bunları çarparak kullanılabilir . Başka bir yaklaşım da, map fonksiyonunu kullanmak, yani mul operatörünü harita fonksiyonuna birinci parametre olarak ve Lists'i bu fonksiyona ikinci ve üçüncü parametre olarak iletmek olabilir. Her yaklaşımın aldığı zamanı görelim.

```python
# Python program demosu
# iterator modul

import operator
import time

# Listeleri tanımlayalım
L1 = [1, 2, 3]
L2 = [2, 3, 4]

# map fonksiyonu için zamanı başlatalım
t1 = time.time()

# sonucu hesaplayalım
a, b, c = map(operator.mul, L1, L2)

# map fonksiyonu için zamanı bitiriyoruz
t2 = time.time()

# Sonuçları ve zamanı yazdıralım
print("Sonuç:", a, b, c)
print("Geçen zaman: %.6f" % (t2 - t1))

# Normal işlem için zamanı başlatalım
t1 = time.time()

# Döngü kurarak hesaplayalım
print("Sonuç:", end=" ")
for i in range(3):
    print(L1[i] * L2[i], end=" ")

# Normaldöngü için zamanı durduralım
t2 = time.time()
print("\nDöngüde geçen zaman: %.6f" % (t2 - t1))
```

```
Sonuç: 2 6 12
Geçen zaman: 0.000005
Sonuç: 2 6 12 
Döngüde geçen zaman: 0.000014
```

## Sonsuz Döngüler

Python'daki döngülerde, `for` kullanılır genelde. Bu döngü türü Python listeleri, demetler , sözlükler ve kümelerin tümü üzerinde aktif olarak çalışır . Ancak bazen bir yineleyici nesnenin tükenmesi gerekli değildir , bazen sonsuz olabilir. Bu tür döngüler, Sonsuz döngüler olarak bilinir.

Python itertools modülü, üç tür sonsuz döngü sağlar: 

**count(start, step)**: Bu yineleyici, "başlangıç" sayısından itibaren yazdırmaya başlar ve sonsuz sayıda yazdırır . Adımlardan bahsediliyorsa, sayılar parametre şeklinde atlanır, aksi takdirde adım varsayılan olarak 1'dir. for döngüsünde kullanımı için aşağıdaki örneğe bakın.

Örnek:
```py
# Python program sonsuz döngüler

import itertools

# for döngüsü
for i in itertools.count(5, 5):
	if i == 35:
		break
	else:
		print(i, end=" ")
```

Çıktı:

`5 10 15 20 25 30`

Eğer i değeri 35 olduğunda döngüyü bitirmeseydik sonsuza kadar sürerdi.

**cycle(liste)**: Bu yineleyici, geçirilen listeden gelen tüm değerleri sırayla yazdırır. Tüm öğeler döngüsel olarak yazdırıldığında yazdırmayı yeniden baştan başlatır.

```py
# Python program sonsuz döngüler

import itertools

count = 0

for i in itertools.cycle('AB'):
	if count > 7:
		break
	else:
		print(i, end=" ")
		count += 1
```

Çıktı:

`A B A B A B A B `

AB döngüsü bittikçe baştan devam ediyor.

Yeni bir örnek,

```py
# Python program sonsuz döngüler

import itertools

l = ['Sonsuz', 'Us', 'Sonsuza']

# yineleyici tanımlıyoruz
iterators = itertools.cycle(l)

# for döngüsü
for i in range(6):
	# next fonksiyonunu kullanıyoruz
	print(next(iterators), end=" ")
```

Çıktı:

`Sonsuz Us Sonsuza Sonsuz Us Sonsuza`

Burada next eğer döngünün sonuna gelmişse tekrar başa dönüyor.

**repeat(val, num)**: Bu yineleyici, geçirilen değeri (val) sonsuz sayıda tekrar tekrar yazdırır. İsteğe bağlı num parametresi alırsa, art arda num sayısı kadar val değerini yazdırır.

```py
# Python repeat() kullanımı

# import "itertools" ediyoruz
import itertools

# repeat() fonksiyonunu kullanıyoruz
print(list(itertools.repeat(25, 4)))
```

Çıktı:

`[25, 25, 25, 25]`

## Kombinatorik yineleyiciler

Permütasyonlar, kombinasyonlar ve Kartezyen çarpımlar gibi kombinatoryal yapıları basitleştirmek için kullanılan özyinelemeli üreteçlere kombinatoryal yineleyiciler denir.

Python'da 4 kombinatorik yineleyici vardır: 

**Product()**: Bu araç, girdi yinelenebilirlerinin kartezyen çarpımını hesaplar. Bir yinelenebilirin kendisiyle çarpımını hesaplamak için, tekrar sayısını belirtmek üzere isteğe bağlı repeat anahtar kelime argümanını kullanırız. Bu fonksiyonun çıktısı sıralanmış tuple'lardır.

```python
from itertools import product

print("repeat kullanarak kartezyan:")
print(list(product([1, 2], repeat=2)))
print()

print("konteynar kullanarak kartezyan:")
print(list(product(['sonsuz', 'us', 'github'], '2')))
print()

print("konteynar kullanarak kardezyan:")
print(list(product('AB', [3, 4])))
```

```
repeat kullanarak kartezyan:
[(1, 1), (1, 2), (2, 1), (2, 2)]

konteynar kullanarak kartezyan:
[('sonsuz', '2'), ('us', '2'), ('github', '2')]

konteynar kullanarak kardezyan:
[('A', 3), ('A', 4), ('B', 3), ('B', 4)]
```

**Permutations()**: Permutations(), adından da anlaşılacağı gibi, bir yinelenebilirin tüm olası permütasyonlarını oluşturmak için kullanılır. Tüm öğeler değerlerine göre değil, konumlarına göre benzersiz olarak değerlendirilir. Bu fonksiyon bir iterable ve group_size alır, group_size değeri belirtilmezse veya None'a eşitse group_size değeri iterable'ın uzunluğu olur.

```py
from itertools import permutations

print("Listedeki tüm permitasyonlar:")
print(list(permutations([1, 'sonsuz'], 2)))
print()

print("Stringteki tüm permütasyonlar:")
print(list(permutations('AB')))
print()

print("Konteynırdaki tüm permütasyonlar:")
print(list(permutations(range(3), 2)))
```

```
Listedeki tüm permitasyonlar:
[(1, 'sonsuz'), ('sonsuz', 1)]

Stringteki tüm permütasyonlar:
[('A', 'B'), ('B', 'A')]

Konteynırdaki tüm permütasyonlar:
[(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]
```

**Combinations()**: Bu yineleyici, belirtilen grup boyutundaki argümanlarda aktarılan kabın tüm olası kombinasyonlarını (değiştirmeden) sıralı olarak yazdırır.

```py
from itertools import combinations

print ("Listeden Tüm kombiyasyonlar sıralı olarak (değiştirmeden):")
print(list(combinations(['A', 2], 2)))
print()

print ("Stringten tüm kombinasyonlar sıralı olarak (değiştirmeden):")
print(list(combinations('AB', 2)))
print()

print ("Konteynarlardan tüm kombinasyonlar sıralı olarak (değiştirmeden):")
print(list(combinations(range(2), 1)))
```

```
Listeden Tüm kombiyasyonlar sıralı olarak (değiştirmeden):
[('A', 2)]

Stringten tüm kombinasyonlar sıralı olarak (değiştirmeden):
[('A', 'B')]

Konteynarlardan tüm kombinasyonlar sıralı olarak (değiştirmeden):
[(0,), (1,)]
```

**Combinations_with_replacement()**: Bu fonksiyon yinelenebilir dosyanın elemanlarından n uzunluğunda bir alt dizi döndürür; burada n, fonksiyonun aldığı ve fonksiyon tarafından oluşturulan alt dizilerin uzunluğunu belirleyen argümandır. Combinations_with_replacement() fonksiyonunda her bir eleman kendini tekrar edebilir.

```py
from itertools import combinations_with_replacement

print("Stringlerde tüm kombinasyonlar sıralı olarak (değiştirilerek):")
print(list(combinations_with_replacement("AB", 2)))
print()

print("Listelerde tüm kombinasyonlar sıralı olarak (değiştirilerek):")
print(list(combinations_with_replacement([1, 2], 2)))
print()

print("Konteynırlarda tüm kombinasyonlar sıralı olarak (değiştirilerek):")
print(list(combinations_with_replacement(range(2), 1)))
```

```
Stringlerde tüm kombinasyonlar sıralı olarak (değiştirilerek):
[('A', 'A'), ('A', 'B'), ('B', 'B')]

Listelerde tüm kombinasyonlar sıralı olarak (değiştirilerek):
[(1, 1), (1, 2), (2, 2)]

Konteynırlarda tüm kombinasyonlar sıralı olarak (değiştirilerek):
[(0,), (1,)]
```