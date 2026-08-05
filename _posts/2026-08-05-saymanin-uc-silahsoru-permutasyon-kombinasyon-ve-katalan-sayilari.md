---
layout: post
title: "Saymanın Üç Silahşörü: Permütasyon, Kombinasyon ve Katalan Sayıları"
math: true
categories: 
  - Bilgi
tags: 
  - kombinatorik
  - olasılık
  - katalan-sayıları
---

Bir kart destesini karıştırırken, takım kurarken veya parantezleri hatasız biçimde dizerken aslında aynı matematiksel soruyla karşılaşırız: Kaç farklı sonuç mümkündür? Kombinatorik bu soruyu sistematik biçimde yanıtlar; olasılık ise mümkün sonuçların içinden ilgilendiğimiz olayların payını hesaplar. Permütasyon, kombinasyon ve Katalan sayıları bu dünyada farklı kapıları açan üç güçlü anahtardır.
``

## Önce temel ilke: Çarpma kuralı

Bir süreç art arda gelen bağımsız seçimlerden oluşuyorsa seçenek sayılarını çarparız. İlk adımda $m$, ikinci adımda $n$ seçenek bulunuyorsa toplam $m \cdot n$ farklı sonuç vardır. Örneğin üç gömlek ve iki pantolon arasından birer parça seçerek $3 \cdot 2=6$ kıyafet oluşturabiliriz.

Bu fikir faktöriyele uzanır. $n$ farklı nesneyi sıralarken ilk konum için $n$, sonraki için $n-1$ seçenek bulunur:

$$n!=n(n-1)(n-2)\cdots 1$$

Ayrıca boş düzenlemenin tek bir biçimi bulunduğu kabul edilerek $0!=1$ tanımlanır.

## Permütasyon: Sıra önemliyse

Permütasyon, nesnelerin sıralanmasını inceler. $n$ farklı nesnenin tamamının sıralanma sayısı $n!$ olur. Yalnızca $r$ tanesi seçilip sıralanacaksa:

$$P(n,r)=\frac{n!}{(n-r)!}$$

Örneğin sekiz koşucudan altın, gümüş ve bronz madalya alacak kişileri belirlerken sıra önemlidir. Sonuç sayısı:

$$P(8,3)=8\cdot7\cdot6=336$$

Aynı elemanlar tekrar ediyorsa fazla sayımları temizlemeliyiz. “KAKAO” kelimesinde iki K ve iki A bulunduğundan farklı diziliş sayısı:

$$\frac{5!}{2!2!}=30$$

## Kombinasyon: Ekipte sıra aranmaz

Kombinasyonda yalnızca hangi elemanların seçildiği önemlidir. $n$ elemandan $r$ eleman seçmenin sayısı:

$$\binom{n}{r}=\frac{n!}{r!(n-r)!}$$

Sekiz kişiden üç kişilik bir ekip seçersek $inom{8}{3}=56$ sonuç elde ederiz. Permütasyondaki 336 sonucun her ekip için $3!=6$ farklı sıralama içermesi, $336/6=56$ ilişkisini açıklar.

| Araç | Sıra önemli mi? | Tipik örnek | Formül |
|---|---:|---|---|
| Permütasyon | Evet | Yarış dereceleri | $P(n,r)$ |
| Kombinasyon | Hayır | Komite seçimi | $\binom{n}{r}$ |
| Katalan sayısı | Yapısal koşul var | Dengeli parantezler | $C_n$ |

## Olasılığa geçiş

Sonuçların eş olasılıklı olduğu sonlu bir deneyde bir $A$ olayının olasılığı:

$$P(A)=\frac{|A|}{|\Omega|}$$

Örneğin 52 karttan seçilen beş kartın tamamının kupa olma olasılığında sıralama önemli değildir:

$$P(A)=\frac{\binom{13}{5}}{\binom{52}{5}}$$

Buradaki kritik nokta, pay ve paydada aynı sayma modelini kullanmaktır. Pay kombinasyonla, payda permütasyonla hesaplanırsa matematik elmalarla sıralanmış armutları karşılaştırmaya başlar.

## Katalan sayıları: Her seçim serbest değilse

Bazı problemlerde nesneleri seçmek yetmez; oluşan yapı belirli kurallara da uymalıdır. Katalan sayıları dengeli parantez dizilerini, ikili ağaçları ve bir çokgenin üçgenlere ayrılma biçimlerini sayar:

$$C_n=\frac{1}{n+1}\binom{2n}{n}$$

Örneğin üç çift parantezin doğru diziliş sayısı $C_3=5$ olur. `()()()`, `(())()` ve `((()))` bunlardan bazılarıdır. Her açılış parantezini $+1$, kapanışı $-1$ sayarsak toplam sıfır olmalı ve hiçbir ara toplam negatif olmamalıdır. Katalan sayılarının gizli kahramanı bu “yol boyunca dengenin bozulmaması” koşuludur.

Aşağıdaki Python kodu ilk Katalan sayılarını hesaplar:

```python
from math import comb

def catalan(n):
    # 2n elemandan n tanesini seçer, geçersiz yapıları ayıklar.
    return comb(2 * n, n) // (n + 1)

for n in range(6):
    print(n, catalan(n))
```

Çıktı `1, 1, 2, 5, 14, 42` biçiminde büyür. Özetle önce “Sıra önemli mi?”, ardından “Tekrar var mı?” ve son olarak “Yapısal bir kısıt bulunuyor mu?” sorularını sorun. Doğru sayma aracını seçtiğinizde olasılık hesabının geri kalanı çoğu zaman yalnızca zarif bir bölme işlemidir.
