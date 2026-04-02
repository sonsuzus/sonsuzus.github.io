---
layout: post
title: Pythonda Karmaşık ve İç İçe Listeleri Düzleştirmek (Flatten)
categories:
  - Program
tags:
  - python
  - program
  - liste
  - flatten
  - özyineleme
  - fonksiyon
  - itertools
redirect_from:
  - /posts/python-karisik-listeyi-tek-liste-yapma/
---

Python'da programlama yaparken, bazen karşımıza iç içe geçmiş listeler, demetler (tuple), kümeler (set) ve hatta sözlükler (dictionary) gibi farklı veri tiplerini bir arada barındıran karmaşık veri yapıları çıkabilir. Bu tür bir yapıyı analiz etmek veya üzerinde işlem yapmak için genellikle onu "düzleştirmek", yani tek bir liste haline getirmek isteriz.

Bu yazıda, karmaşık bir listedeki tüm sayısal değerleri ayıklayıp tek ve düz bir liste oluşturmanın farklı yollarını inceleyeceğiz.

### Zorlu Bir Örnek: Karışık Veri Yapısı

İşe, üzerinde çalışacağımız karmaşık listeyi tanımlayarak başlayalım. Bu liste, içinde tam sayılar, listeler, demetler, kümeler ve sözlükler barındırıyor.

```python
karmaşık_liste = [1, 2, 3, [4, 5, [6, 7]], [8, 9], [10, 11, [100], 12, (1, 1), {5, 6}, {'a': [200, 100], 'b': 100}, 13, 14, [15, [16, 17]]]]
```

Amacımız, bu yapı içindeki tüm sayıları ayıklayarak `[1, 2, 3, 4, 5, ...]` şeklinde tek bir liste elde etmek.

### Çözüm 1: Özyinelemeli (Recursive) Fonksiyon

Bu tür derin ve karmaşık yapıları çözmenin en esnek yollarından biri özyinelemeli, yani kendi kendini çağıran bir fonksiyon yazmaktır.

Fonksiyonumuz, kendisine verilen verinin tipini kontrol edecek:
- Eğer veri bir sayı ise doğrudan sonuç listesine ekleyecek (temel durum).
- Eğer veri bir liste, demet veya küme ise içindeki her bir eleman için fonksiyonu tekrar çağıracak (özyinelemeli durum).
- Eğer veri bir sözlük ise sadece değerleri (values) için aynı işlemi tekrarlayacak.

```python
def düzleştir(veri):
    sonuç = []
    if isinstance(veri, int):
        sonuç.append(veri)
    elif isinstance(veri, (list, tuple, set)):
        for eleman in veri:
            sonuç.extend(düzleştir(eleman))
    elif isinstance(veri, dict):
        for değer in veri.values():
            sonuç.extend(düzleştir(değer))
    return sonuç

# Fonksiyonu çağıralım ve sonucu görelim
düz_liste = düzleştir(karmaşık_liste)
print(düz_liste)
```

**Çıktı:**

```
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 100, 12, 1, 1, 5, 6, 200, 100, 100, 13, 14, 15, 16, 17]
```

Bu fonksiyon, `isinstance()` ile tip kontrolü yaparak her veri türüne uygun şekilde davranır ve `extend()` metodu ile bulduğu listeleri ana sonuç listesine ekler.

### Çözüm 2: `yield` ile Daha Pythonic Bir Yaklaşım (Generator)

Özyinelemeli fonksiyonlar, büyük veri setlerinde hafıza kullanımını artırabilir. `yield` anahtar kelimesini kullanarak bir "generator" fonksiyonu oluşturmak, daha hafıza dostu ve "Pythonic" bir çözümdür. Bu fonksiyon, değerleri bir listede biriktirmek yerine, bulduğu anda teker teker döndürür.

```python
def düzleştir_generator(veri):
    if isinstance(veri, int):
        yield veri
    elif isinstance(veri, (list, tuple, set)):
        for eleman in veri:
            yield from düzleştir_generator(eleman)
    elif isinstance(veri, dict):
        for değer in veri.values():
            yield from düzleştir_generator(değer)

# Generator'ı kullanarak listeyi oluşturalım
düz_liste_gen = list(düzleştir_generator(karmaşık_liste))
print(düz_liste_gen)
```

`yield from` ifadesi, başka bir generator'dan gelen tüm değerleri sanki bu fonksiyondan geliyormuş gibi aktarır ve kodu daha temiz hale getirir.

### Çözüm 3: Basit Durumlar İçin `itertools`

Eğer listemiz sadece bir seviye derinliğe sahipse (örneğin `[[1, 2], [3, 4]]` gibi), Python'un standart `itertools` kütüphanesi en hızlı ve etkili çözümü sunar.

```python
import itertools

basit_liste = [[1, 2, 3], [4, 5], [6, 7, 8]]

# itertools.chain.from_iterable ile düzleştirme
düz_liste_itertools = list(itertools.chain.from_iterable(basit_liste))
print(düz_liste_itertools)
```

**Çıktı:**

```
[1, 2, 3, 4, 5, 6, 7, 8]
```

Ancak bu yöntem, bizim karmaşık örneğimizdeki gibi çok katmanlı ve farklı tipler içeren yapılar için tek başına yeterli değildir.

### Sonuç

- **Karmaşık, derin ve karışık tipli yapılar için:** Özyinelemeli bir fonksiyon (`yield` ile veya olmadan) en esnek ve güvenilir çözümdür.
- **Sadece bir seviye iç içe geçmiş listeler için:** `itertools.chain.from_iterable()` en performanslı ve okunabilir yöntemdir.

Doğru aracı seçmek, hem kodunuzun daha temiz olmasını sağlar hem de verimliliği artırır.