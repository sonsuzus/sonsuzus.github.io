---
title: Riya'nın Doğum Günü Sorusu Algoritması
author: sonsuz
date: 2023-08-20 22:01:41 +0300
categories: [Program,Algoritma]
tags: [algoritma,problem,soru,python,liste]
---

## Riya'nın Doğum Günü Sorusu

### Problem

Madhav Riya’nın Doğum Günü Partisine gider. O bir inek olduğundan, bu yüzden hangi hediye hoşuna gideceği konusunda hiçbir fikri yoktur. Bu yüzden bir dizi tamsayıyı yanına alır. Dizi belirli bir düzene uyar. Dizinin ilk elemanı 1’dir. Dizinin ikinci elemanı 6 dır.

Dizinin diğer elemanları, kendisinden önce ve sonra gelen sayıların aritmetik ortalamasının iki eksiği olarak belirleniyordu. Açıkça görüleceği gibi, Riya bu fikrin aptalca olduğunu düşündü ve bu yüzden Madhav’ı cezalandırmak istedi. Madhav’ın bu utanç verici durumdan kaçmasına yardım et.

### Girdi

- Girdi, T, Test Durumlarının sayısı ile başlar. (Kaç N gönderileceği)
- Sonraki T satırda tamsayı N ler verilir.

### Çıktı

Her test durumu için, dizinin N’inci üyesini bir tamsayı çıktısı olarak verin. Cevap çok büyük olabileceğinden, sonucu 10 ^ 9 + 7’e göre modulo alarak çıktı verin.

### Kısıtlamalar:

- 1 ≤ T ≤ 10^5
- 1 ≤ N ≤ 10^18

### Örnek Giriş

```
2
1
3
```

### Örnek Çıktı

```
1
15
```

Kısacası dizimiz `a[n] = (a[n-1]+a[n+1])/2 - 2` olarak ilerliyor. Buradan `a[n+1]` i bulaabilmek için `a[n+1] = 2*a[n] - a[n-1] + 4` formülünü uygulayabiliriz. Elimizde ilk iki eleman 1 ve 6 olduğuna göre dizinin 3. elemanı 15 olarak buluruz.

Yani sonuç olarak dizimiz `[1, 6, 15, 28, 45, 66, 91, 120, 153, 190, 231, 276, 325, 378, 435, ...]` olarak gidiyor.

## Olası çözüm algoritmaları

Aşağıdaki kod liste kullanımı ile çözümüdür. 

```py
dizi = [1,6]
N = []
T = int(input())
for _ in range(T):
    N.append(int(input()))

ma = max(N)
for i in range(2,ma):
    dizi.append(2*dizi[i-1]-dizi[i-2]+4)

for i in N:
    print(dizi[i-1])
```

Girilen sayıların en  büyüğüne kadar diziyi doldurmak üzere tasarlanmıştır.

Fonksiyon kullanarak şöyle bir çözüm de üretilebilir.

```py
def bul(eleman):
    if eleman == 1:
        return 1
    tp=0
    for n in range(0,eleman-1):
        tp += n       

    return 1+5*(eleman-1)+4*(tp)

T = int(input())
for _ in range(T):
    print(bul(int(input())))
```

Daha kısa kod kullanarak çözümü de sayılar arasındaki bağıntıyı kullanarak olabilir.

```py
T = int(input())
for s in range(T):
    N = int(input())
    to = 1
    for i in range(N-1):
        to = to +5+ i*4
    print(to)
```

Bu kodlar doğru sonuçları verse de daha güzel ve hızlı çalışan algoritmalar üretilebilir. Konu güncellenecektir.