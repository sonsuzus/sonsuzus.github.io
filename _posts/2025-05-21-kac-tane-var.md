---
layout: post
title: Kaç Tane Var
categories:
  - Program
tags:
  - python
  - algoritma
  - soru
  - sayılar
  - zeka
---

Elimizde bir problem var. Bir sayı dizisi. Öncelikle bu bir ilişki bulma sorusu. Ama bu soruyu bir programlama veya algoritma sorusuna da çevirebiliriz. Soru aşağıdaki gibi.

1
11
21
1211
111221
Sırada ki sayı kaçtır?

Sorunun çözümünü size bırakıyorum. Ben sırayla yapılan programları örnek olarak ekliyorum. Zamanla daha gelişmiş örneklerini ve farklı dillerde yapımlarını da ekleyeceğim.

## Python

En ilkel ve anlaşılır haliyle yapılan program.

```python
def grupla(text):
    if not text:
        return []
    
    result = []
    grup = text[0]
    
    for char in text[1:]:
        if char == grup[-1]:
            grup += char
        else:
            result.append(grup)
            grup = char
    result.append(grup)
    
    return result

def yaz(gruplar):
    result = ""
    for grup in gruplar:
        result += str(len(grup))+grup[0]
    return result

string = "1"
for _ in range(10):
    print(string)
    gruplar = grupla(string)
    string = yaz(gruplar
```

Daha sonra bir rekürsif denemesi.

```python
def say(sonuc = [], dize = []):
    if dize == []:
        return "".join(map(str, sonuc))
    if sonuc == [] or dize[0] != sonuc[-1]:
        sonuc.append(1)
        sonuc.append(dize[0])
    elif dize[0] == sonuc[-1]:
        sonuc[-2] += 1
    return say(sonuc, dize[1:])

liste = "1"
for _ in range(10):
    print(liste)
    liste = (say([], list(liste)))
```

Daha da sadesi ve rekürsifsiz hali.

```python
def say(dize):
    sonuc = []
    for i in dize:
        if sonuc == [] or i != sonuc[-1]:
            sonuc.append(1)
            sonuc.append(i)
        else:
            sonuc[-2] += 1
    return "".join(map(str, sonuc))

liste = "1"
for _ in range(10):
    print(liste)
    liste = say(liste)
```

Bu konu güncellenecektir.