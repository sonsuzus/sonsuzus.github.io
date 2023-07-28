---
title:  Türkçe Sator Kareleri
author: sonsuz
date: 2023-07-28 19:09:53 +0300
categories: [Program,Algoritma]
tags: [python,program,döngü,liste,veri,türkçe,palindrom]
---

Sator kareleri meşhur bir kelime dizilimi programıdır. Örneği şu şekildedir.

![](sator-karesi.jpg)

Kurallardan anlaşılacağa üzere her satır ve sütunda anlamlı kelimeler bulunuyor ve bunlar bazen birbirinin tersi olabiliyor. Anlamlı sator karelerini bulabilmek için öncelikle elimizde bir kelime veri tabanı olması gerekiyor. 60bin anlamlı kelimelerden oluşan veri tabanını indirmek için: [Türkçe Sözcük veritabanı](https://sonsuzus.github.io/dosya/words.py) na tıklayabilirsiniz. Ben doğrudan import ettiğim için .py dosyası haline getirdim, siz elinizdeki başka veritabanlarını da kullanabilirsiniz.

Bundan sonra kodumuz bir kaç aşamadan geçiyor. Aşağıda kodlarla sator karelerini bulma girişimlerimiz olmuştur.

```python
import words

besli = []

toplam = 0
kelimeler = words.kelime
for k in kelimeler:
    if len(k)==5 and k[::-1] in kelimeler:
        besli.append(k)

for k1 in besli:
    if k1==k1[::-1]:
        continue
    for k2 in besli:
        if k2==k2[::-1]:
            continue
        if k1[1]!=k2[0] or k1[3]!=k2[4]:
            continue
        for k3 in besli:
            if k3!=k3[::-1] or k3[0]!=k1[2] or k3[1]!=k2[2]:
                continue
            k4 = k2[::-1]
            k5 = k1[::-1]
            print(k1,k2,k3,k4,k5,sep="\n")
            print()
            toplam += 1

print(toplam)
```

Sonuç olarak yukarıdaki program hem hızlı hem de doğru bulduğu 22 (ayna görüntüleri hariç) sator karesinden bir kaç örnek.

```
SAKAT
AKALA
KAÇAK
ALAKA
TAKAS

KİNİŞ
İVESİ
NEDEN
İSEVİ
ŞİNİK
```

Programın daha geliştirilmiş ve kaçlı sator karesi aradığınıza da yönelik kodu aşağıdadır.

```python
import json
from itertools import permutations, product


def read_json(filename):
    with open(filename, encoding="utf-8") as f:
        return json.load(f)


def filter_words(words, length):
    data = [x for i in words if len(x := i["word"]) == length]
    return [i for i in data if i[::-1] in data]


def possible_sator_words(x, y, index=(1, -2)):
    cases = [i for i in x if y[index[0]] == i[0] and y[index[1]] == i[-1]]
    if sum(map(abs, index)) == (len(y) if len(y) % 2 else len(y) - 1):
        return cases
    else:
        return [cases, possible_sator_words(x, y, (index[0] + 1, index[1] - 1))]


def is_sator_square(lst):
    return all(lst[m] == "".join([j[m] for j in lst]) for m in range(len(lst)))


def find_sator_squares(words, length):
    words = filter_words(words, length)
    array = []
    for word in words:
        if all(possibilities := possible_sator_words(words, word)) and len(possibilities) >= 1:
            sator_group = [[word]] + (possibilities if length % 2 else [possibilities])
            for p in product(*sator_group):
                for perm in permutations(p, length - 2):
                    perm += tuple(j[::-1] for j in perm[:2])[::-1]
                    if (
                        is_sator_square(perm) 
                        and 
                        sorted(perm) not in array 
                        and all(perm.count(i) == 1 for i in perm)
                    ):
                        array += [sorted(perm)]
    return array
```

Siz de sator kareleri ile ilgili kodu, yorumlar kısmına ekleyebilirsiniz.
