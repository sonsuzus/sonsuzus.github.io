---
title: Python içiçe listeleri tek liste yapmak
author: sonsuz
date: 2024-01-30 00:16:41 +0300
categories: [Program,Python]
tags: [python,programlama,liste,rekürsif,fonksiyon,metod]
---

Python programlamada iç içe listeleri tek ve düz bir liste haline getirmek için aşağıdaki fonksiyonu kullanabilirsiniz. Fonksiyon kısaca listedeki sırası gelen eleman bir liste değilse appendle ekleniyor, eğer bir listeyse tekrar fonksiyonun kendisine gönderiliyor ve yine parçalara bölünerek geri dönüşleri listeye ekliyor. Son olarak oluşan yeni listeyi geri döndürüyor.

Daha hızlı ve güzel metodlar veya modüllerde kullanılan hazır fonksiyonlar mutlaka vardır. Eğer bildiğiniz varsa yorum olarak ekleyebilirsiniz konuyu güncellerim.

```py
def liste_yap(liste):
  tek_liste = []
  for eleman in liste:
    if isinstance(eleman, list):
      tek_liste.extend(liste_yap(eleman))
    else:
      tek_liste.append(eleman)
  return tek_liste

liste = [[1,2],3,4,[8,5],[0,6,[9,7]]]

print(liste)
print(liste_yap(liste))
```
