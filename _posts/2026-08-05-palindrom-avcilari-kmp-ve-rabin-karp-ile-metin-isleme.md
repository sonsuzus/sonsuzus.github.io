---
layout: post
title: "Palindrom Avcıları: KMP ve Rabin-Karp ile Metin İşleme"
math: true
categories: 
  - Bilgi
tags: 
  - KMP
  - Rabin-Karp
  - palindrom
---

Bir kelimeyi ters çevirdiğinizde aynı sonucu görüyorsanız karşınızda bir palindrom vardır: “kabak”, “level” ve “ada” gibi. Ancak metin milyonlarca karakterden oluştuğunda palindromları tek tek kontrol etmek pek eğlenceli değildir. Neyse ki KMP ve Rabin-Karp, örüntü arama yeteneklerini palindrom sorularına uyarlayarak bizi iç içe döngülerin karanlık dünyasından kurtarabilir.
``

## Palindrom probleminin temeli

Bir $S$ dizisinin palindrom olması için şu koşul sağlanmalıdır:

$$S[i] = S[n-1-i] \quad \text{tüm } 0 \le i < n$$

Doğrudan kontrolde dizinin yalnızca yarısını karşılaştırmak yeterlidir ve süre karmaşıklığı $O(n)$ olur. Fakat “en uzun palindromik önek nedir?”, “şu aralık palindrom mu?” veya “metinde belirli bir palindrom kaç kez geçiyor?” gibi sorular geldiğinde daha güçlü araçlara ihtiyaç duyarız.

| Yöntem | Temel fikir | Ön işleme | Sorgu maliyeti | Risk |
|---|---|---:|---:|---|
| Doğrudan karşılaştırma | İki uçtan ilerleme | $O(1)$ | $O(n)$ | Yok |
| KMP | Önek ve sonek eşleşmesi | $O(n)$ | Probleme göre $O(1)$ veya $O(n)$ | Yok |
| Rabin-Karp | Hash değerlerini karşılaştırma | $O(n)$ | $O(1)$ | Hash çakışması |

## KMP ile en uzun palindromik önek

KMP yalnızca bir örüntüyü metinde aramaz; oluşturduğu **LPS** dizisi, her konumda aynı zamanda sonek olan en uzun uygun önekin uzunluğunu saklar. Bir metnin en uzun palindromik önekini bulmak için metni tersiyle birleştirebiliriz:

$$T = S + \# + reverse(S)$$

Buradaki `#`, metinde bulunmayan ayırıcıdır. `T` için hesaplanan son LPS değeri, `S` içindeki en uzun palindromik önekin uzunluğunu verir. Çünkü normal metnin öneki ile ters metnin soneki arasındaki eşleşme, iki yönde aynı okunan bölümü temsil eder.

```python
def en_uzun_palindromik_onek(s):
    t = s + "#" + s[::-1]
    lps = [0] * len(t)

    for i in range(1, len(t)):
        j = lps[i - 1]
        while j > 0 and t[i] != t[j]:
            j = lps[j - 1]
        if t[i] == t[j]:
            j += 1
        lps[i] = j

    uzunluk = lps[-1]
    return s[:uzunluk]

print(en_uzun_palindromik_onek("abacabaXYZ"))  # abacaba
```

Bu yaklaşım $O(n)$ zamanda ve $O(n)$ ek bellekte çalışır. Özellikle bir metnin başına en az kaç karakter eklenerek palindrom yapılacağını bulmada kullanışlıdır. Gerekli karakter sayısı $n-L$ olur; burada $L$, en uzun palindromik önekin uzunluğudur.

## Rabin-Karp ile hızlı palindrom sorguları

Rabin-Karp, karakterleri sayılara dönüştürüp polinom hash üretir. Bir alt dizinin palindrom olup olmadığını anlamak için orijinal metindeki hash ile ters metindeki karşılık gelen aralığın hash’i karşılaştırılır.

Bir önek hash’i şu şekilde kurulabilir:

$$H[i+1] = (H[i]\cdot b + code(S[i])) \bmod m$$

`S[l:r]` aralığının hash’i ise önceden hesaplanan kuvvetlerle $O(1)$ zamanda çıkarılır.

```python
class PalindromHash:
    def __init__(self, s, base=911, mod=1_000_000_007):
        self.s = s
        self.n = len(s)
        self.base, self.mod = base, mod
        self.power = [1] * (self.n + 1)

        for i in range(self.n):
            self.power[i + 1] = self.power[i] * base % mod

        self.forward = self._build(s)
        self.backward = self._build(s[::-1])

    def _build(self, text):
        h = [0]
        for ch in text:
            h.append((h[-1] * self.base + ord(ch)) % self.mod)
        return h

    def _hash(self, h, left, right):
        return (h[right] - h[left] * self.power[right-left]) % self.mod

    def palindrom_mu(self, left, right):
        # Aralık [left, right) biçimindedir.
        ters_sol = self.n - right
        ters_sag = self.n - left
        return self._hash(self.forward, left, right) == \
               self._hash(self.backward, ters_sol, ters_sag)
```

Hash yaklaşımı çok sayıda aralık sorgusunda parıldar. Yine de farklı metinlerin aynı hash’i üretme ihtimali vardır. Yarışma sorularında çift mod kullanmak bu olasılığı ciddi biçimde azaltır.

## Hangisini seçmeli?

Tek bir palindrom kontrolü için iki uçlu karşılaştırma yeterlidir. En uzun palindromik önek veya sonek aranıyorsa KMP deterministik ve güvenlidir. Çok sayıda alt dizi sorgusu varsa Rabin-Karp daha esnektir. Kısacası KMP eşleşme yapısını, Rabin-Karp ise sayısal parmak izlerini kullanır; palindromlar da aynaya bakarken bu iki avcıdan kolay kolay kaçamaz.
