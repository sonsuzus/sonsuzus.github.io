---
title:  Python itertools kullanımı
author: sonsuz
date: 2023-07-25 01:19:51 +0300
categories: [Program,Python]
tags: [python,programlama,veri,döngü,itertools]
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
