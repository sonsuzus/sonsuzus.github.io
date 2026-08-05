---
layout: post
title: "Asal Sayılardan Hızlı Üs Almaya: Matematiğin Programlama Motoru"
math: true
categories: 
  - Bilgi
tags: 
  - asal sayılar
  - modüler aritmetik
  - hızlı üs alma
---

Bilgisayarlar matematik konusunda hızlıdır; ancak sonsuz sabırlı değillerdir. Sayılar büyüdükçe sıradan yöntemler yavaşlar, bellek tüketimi artar ve taşma sorunları ortaya çıkar. Asal sayılar, modüler aritmetik ve hızlı üs alma teknikleri; kriptografiden algoritma yarışmalarına kadar bu sorunları çözmemizi sağlayan güçlü araçlardır.
``
## Asal Sayılar: Aritmetiğin Atomları

Yalnızca $1$ ve kendisine tam bölünebilen, $1$'den büyük doğal sayılara **asal sayı** denir. Örneğin $2, 3, 5, 7$ asaldır; $12$ ise $2 \times 2 \times 3$ biçiminde ayrılabildiği için bileşiktir.

Aritmetiğin Temel Teoremi'ne göre $1$'den büyük her tam sayı, asal sayıların çarpımı olarak tek bir biçimde yazılabilir. Çarpanların sırası sonucu değiştirmez:

$$360 = 2^3 \times 3^2 \times 5$$

Bu özellik, asal sayıları doğal sayıların yapı taşları hâline getirir. Bir sayının asal olup olmadığını kontrol etmek için $2$'den başlayıp sayının kendisine kadar ilerlemek gereksizdir. Eğer $n$ bileşikse çarpanlarından en az biri $\sqrt{n}$ değerinden küçük veya ona eşittir. Dolayısıyla kontrol sınırı $\sqrt{n}$ olabilir.

```python
from math import isqrt

def asal_mi(n):
    if n < 2:
        return False
    for bolen in range(2, isqrt(n) + 1):
        if n % bolen == 0:
            return False
    return True
```

Bu fonksiyonun zaman karmaşıklığı yaklaşık $O(\sqrt{n})$ olur. Belirli bir sınıra kadarki bütün asalları bulmak gerektiğinde ise Eratosthenes Eleği daha uygundur.

## Modüler Aritmetik: Sayıların Saat Hâli

Modüler aritmetik, bölme işleminden kalanlarla ilgilenir. Saat 10'a üç saat ekleyince 13 değil, 1 denmesi bunun günlük hayattaki örneğidir. Matematiksel olarak:

$$13 \equiv 1 \pmod{12}$$

Bu ifade, $13$ ve $1$ sayılarının 12 ile bölündüğünde aynı kalanı verdiğini söyler. Modüler işlemler büyük değerleri kontrol altında tutar:

$$10^{100} \bmod 9 = 1$$

Çünkü $10 \equiv 1 \pmod 9$ olduğundan $10^{100} \equiv 1^{100} \equiv 1 \pmod 9$ elde edilir.

| Normal işlem | Modüler karşılığı | Avantajı |
|---|---|---|
| $a+b$ | $(a \bmod m+b \bmod m)\bmod m$ | Sayıları küçük tutar |
| $a\times b$ | $((a\bmod m)(b\bmod m))\bmod m$ | Dev çarpımları sınırlar |
| $a^b$ | $a^b\bmod m$ | Kriptografide kullanılır |
| $a-b$ | $(a-b+m)\bmod m$ | Negatif kalanı önler |

Programlama dillerinin negatif sayılarda kalan davranışı farklı olabileceği için güvenli normalleştirme genellikle `((x % m) + m) % m` biçimindedir.

## Büyük Sayılarla İşlemler

Python tam sayıları ihtiyaç oldukça büyüyebilir. C, C++ ve Java gibi dillerdeyse sabit genişlikli türler taşabilir. Örneğin işaretli 64 bit bir tam sayının üst sınırı $2^{63}-1$ değeridir.

| Yaklaşım | Kullanım alanı | Dezavantajı |
|---|---|---|
| 64 bit tam sayı | Hızlı genel hesaplama | Taşma riski |
| BigInteger | Kesin ve dev değerler | Daha yavaş çalışma |
| Modüler hesaplama | Yalnızca kalan gerekiyorsa | Asıl sayı korunmaz |

Sonuç yalnızca belirli bir modüle göre isteniyorsa dev sayıyı üretmek yerine her adımda mod almak en verimli çözümdür.

## Hızlı Üs Alma: Üssü İkiye Böl

$a^b$ değerini $b$ kez çarpmak $O(b)$ işlem gerektirir. **Binary exponentiation**, üssü sürekli ikiye bölerek bunu $O(\log b)$ seviyesine indirir. Temel fikir şudur:

$$a^{2k}=(a^k)^2, \qquad a^{2k+1}=a(a^k)^2$$

```python
def hizli_us(taban, us, mod):
    sonuc = 1
    taban %= mod

    while us > 0:
        if us % 2 == 1:
            sonuc = (sonuc * taban) % mod
        taban = (taban * taban) % mod
        us //= 2

    return sonuc
```

Kod, üssün ikilik gösterimindeki her biti işler. Bit 1 olduğunda mevcut taban sonuca katılır; ardından taban karesine yükseltilir. Böylece örneğin $3^{1\,000\,000}\bmod 1\,000\,000\,007$ saniyeler beklemeden hesaplanabilir.

Bu kavramlar birlikte düşünüldüğünde güçlü bir algoritmik araç kutusu oluşur: asal sayılar çarpan yapısını açıklar, modüler aritmetik değerleri dizginler, büyük sayı stratejileri taşmayı önler ve hızlı üs alma astronomik görünen hesapları birkaç adıma indirir. Matematiğin programlamadaki süper gücü tam olarak budur.
