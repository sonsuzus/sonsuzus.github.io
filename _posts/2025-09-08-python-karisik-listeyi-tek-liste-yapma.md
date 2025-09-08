---
layout: post
title: Python karışık listeyi tek liste yapma
categories:
  - Program
tags:
  - program
  - python
  - liste
  - karışık
  - fonksiyon
---

Elimizde şöyle bir liste olsun;

```python
liste=[1,2,3,[4,5,[6,7]],[8,9],[10,11,[100],12,(1,1),{5,6},{'a':[200,100],'b':100},13,14,[15,[16,17]]]]
```

Bu listede bulunan sayılardan tek bir liste yapmak isteyelim.

Bunun için şöyle bir fonksiyon yazabiliriz;

```python
def listele(x):
    sonuc=[]
    if isinstance(x,int):
        sonuc.append(x)
    elif isinstance(x,(list,tuple,set)):
        for k in x:
            sonuc.extend(listele(k))
    elif isinstance(x,dict):
        for k in x.values():
            sonuc.extend(listele(k))
    return sonuc
```
