---
layout: post
title: "Alt Dizilerin Dedektifliği: LIS, LCS ve Metin Benzerliği"
math: true
categories: 
  - Bilgi
tags: 
  - dinamik programlama
  - alt dizi
  - metin işleme
---

Bir sayı dizisindeki yükselişleri bulmakla iki metnin ne kadar benzediğini ölçmek ilk bakışta ayrı dünyaların işi gibi görünebilir. Oysa En Uzun Artan Alt Dizi (LIS) ve En Uzun Ortak Alt Dizi (LCS), aynı temel sorunun akrabalarıdır: Sırayı bozmadan hangi elemanları seçebiliriz? Bu yaklaşım; sürüm karşılaştırma, intihal tespiti, DNA analizi ve yazım düzeltme gibi birçok alanda karşımıza çıkar.
``

## Alt dizi tam olarak nedir?

Bir **alt dizi (subsequence)** oluştururken eleman silebiliriz ancak kalan elemanların sırasını değiştiremeyiz. Elemanların yan yana bulunması gerekmez. Buna karşılık **alt metin veya alt dizi parçası (substring/subarray)** kesintisiz olmalıdır.

| Kavram | Elemanlar bitişik mi? | Sıra korunur mu? | Örnek |
|---|---:|---:|---|
| Alt dizi | Hayır | Evet | `ABCDEF → ACE` |
| Alt metin | Evet | Evet | `ABCDEF → BCD` |
| Alt küme | Hayır | Hayır | `{A,B,C} → {C,A}` |

Bu ayrım önemlidir; yanlış kavramı seçmek, çalışan ama bambaşka bir problemi çözen algoritmalar yazmamıza yol açar.

## En Uzun Artan Alt Dizi (LIS)

LIS, sayılar arasından sırası korunacak biçimde seçilebilen en uzun artan diziyi arar. Örneğin `[3, 1, 5, 2, 6, 4, 9]` için `[1, 2, 4, 9]` geçerli bir sonuçtur.

Klasik dinamik programlama yaklaşımında $dp[i]$, `i` konumunda biten en uzun artan alt dizinin uzunluğudur:

$$dp[i] = 1 + \max(dp[j]) \quad \text{öyle ki } j<i \text{ ve } a[j]<a[i]$$

Uygun bir $j$ yoksa $dp[i]=1$ olur. İki iç içe döngü nedeniyle zaman karmaşıklığı $O(n^2)$, bellek karmaşıklığı ise $O(n)$ seviyesindedir.

```python
def lis_length(numbers):
    # dp[i], i. elemanda biten en uzun artan alt diziyi tutar.
    dp = [1] * len(numbers)

    for i in range(len(numbers)):
        for j in range(i):
            if numbers[j] < numbers[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp, default=0)
```

Daha büyük girdilerde ikili arama kullanan “sabır sıralaması” yaklaşımı süreyi $O(n\log n)$ düzeyine indirir. Ancak bu yöntemde tutulan yardımcı dizi, her zaman LIS’in kendisi değildir; öncelikle mümkün olan en küçük kuyruk değerlerini temsil eder.

## En Uzun Ortak Alt Dizi (LCS)

LCS, iki dizide veya metinde sırayı bozmadan ortak kalan en uzun yapıyı bulur. `KODLAMA` ve `KAPLAMA` sözcükleri karşılaştırıldığında ortak karakterlerin sırası, benzerliğin iskeletini oluşturur.

$dp[i][j]$, ilk metnin ilk $i$, ikinci metnin ilk $j$ karakteri için LCS uzunluğu olsun:

$$dp[i][j] = \begin{cases}dp[i-1][j-1]+1, & x_i=y_j \\ \max(dp[i-1][j],dp[i][j-1]), & x_i\ne y_j\end{cases}$$

```python
def lcs_length(first, second):
    # Tablo, metin önekleri arasındaki en iyi ortak uzunlukları saklar.
    dp = [[0] * (len(second) + 1) for _ in range(len(first) + 1)]

    for i, left in enumerate(first, 1):
        for j, right in enumerate(second, 1):
            if left == right:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[-1][-1]
```

Bu çözümün zaman ve bellek maliyeti $O(nm)$’dir. Yalnızca uzunluk gerekiyorsa iki satır tutularak bellek $O(\min(n,m))$ seviyesine düşürülebilir.

## LCS ile dizi benzerliği

Ham LCS değeri uzun metinleri doğal olarak avantajlı kılar. Bu nedenle normalize edilmiş bir skor kullanabiliriz:

$$S(A,B)=\frac{2\cdot LCS(A,B)}{|A|+|B|}$$

Skor $0$ ile $1$ arasındadır; $1$, dizilerin tamamen aynı olduğunu gösterir.

| Yöntem | Sıraya duyarlı mı? | Güçlü olduğu alan |
|---|---:|---|
| LCS benzerliği | Evet | Sürüm ve değişiklik analizi |
| Jaccard | Genellikle hayır | Kelime veya etiket kümeleri |
| Levenshtein | Evet | Yazım hataları ve düzenleme maliyeti |
| Kosinüs benzerliği | Hayır | Büyük belgelerde konu benzerliği |

Gerçek metinlerde karşılaştırmadan önce küçük harfe dönüştürme, noktalama temizleme ve kelimelere ayırma yapılabilir. Karakter tabanlı LCS küçük yazım değişikliklerini, kelime tabanlı LCS ise cümle yapısını daha iyi yakalar. Kısacası LIS yükselişleri, LCS ortak düzeni bulur; benzerlik skoru da bu düzeni yorumlanabilir bir sayıya dönüştürür.
