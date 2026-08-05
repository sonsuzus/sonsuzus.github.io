---
layout: post
title: "Kesirli ve 0-1 Sırt Çantası: Açgözlü Algoritma mı, Dinamik Programlama mı?"
math: true
categories: 
  - Bilgi
tags: 
  - algoritmalar
  - dinamik programlama
  - açgözlü yaklaşım
---

Bir kamp çantanızın kapasitesi sınırlı, önünüzdeki eşyaların ise ağırlıkları ve değerleri farklı olsun. Amaç, çantanın taşıma sınırını aşmadan mümkün olan en yüksek toplam değeri elde etmektir. Bilgisayar bilimindeki **sırt çantası problemi**, bu basit senaryo üzerinden algoritma tasarımının önemli bir dersini gösterir: Aynı görünen problemlerde küçük bir kural değişikliği, doğru çözüm yaklaşımını tamamen değiştirebilir.

``

## Problemin matematiksel modeli

Her eşyanın ağırlığını $w_i$, değerini $v_i$, çantanın kapasitesini ise $W$ ile gösterelim. Seçim miktarı $x_i$ olduğunda amaç fonksiyonumuz şöyledir:

$$\max \sum_{i=1}^{n} v_i x_i$$

Kapasite kısıtı ise:

$$\sum_{i=1}^{n} w_i x_i \leq W$$

İki problem arasındaki kritik fark, $x_i$ değişkeninin alabileceği değerlerdir:

| Özellik | Kesirli sırt çantası | 0-1 sırt çantası |
|---|---|---|
| Seçim değeri | $0 \leq x_i \leq 1$ | $x_i \in \{0,1\}$ |
| Eşya bölünebilir mi? | Evet | Hayır |
| Uygun yaklaşım | Açgözlü algoritma | Dinamik programlama |
| Tipik zaman karmaşıklığı | $O(n \log n)$ | $O(nW)$ |
| Yerel en iyi seçim yeterli mi? | Evet | Her zaman değil |

Kesirli modelde bir eşyanın yüzde 40’ını almak mümkündür. Altın, yakıt veya tahıl gibi bölünebilen ürünler buna uygundur. 0-1 modelinde ise dizüstü bilgisayarın yarısını çantaya koymak pek işe yaramaz; eşya ya tamamen alınır ya da bırakılır.

## Kesirli problemde açgözlü seçim

Açgözlü yaklaşım, her adımda o an en avantajlı seçimi yapar. Kesirli sırt çantasında avantajı ölçmek için değer-ağırlık oranı kullanılır:

$$r_i = \frac{v_i}{w_i}$$

Eşyalar bu orana göre büyükten küçüğe sıralanır. Çantaya sığanlar tamamen, son kalan boşluğa sığmayan eşya ise kesirli olarak alınır.

```python
def fractional_knapsack(items, capacity):
    # Her öğe (değer, ağırlık) biçimindedir.
    items.sort(key=lambda item: item[0] / item[1], reverse=True)
    total_value = 0

    for value, weight in items:
        if weight <= capacity:
            total_value += value
            capacity -= weight
        else:
            total_value += value * (capacity / weight)
            break

    return total_value
```

Bu algoritma neden doğrudur? Çünkü yüksek oranlı bir eşya yerine daha düşük oranlı bir eşyanın aynı ağırlıktaki parçasını seçmek toplam değeri artıramaz. Bölünebilirlik, yerel olarak en iyi seçimi küresel olarak da güvenli hâle getirir.

## Açgözlü yöntem 0-1 probleminde neden tökezler?

Kapasite $50$ olsun. Eşyalar sırasıyla $(değer, ağırlık)$ olarak $(60,10)$, $(100,20)$ ve $(120,30)$ olsun. Oranlar $6$, $5$ ve $4$ olur. Açgözlü yöntem ilk iki eşyayı seçerek $160$ değer elde eder. Oysa ikinci ve üçüncü eşyalar birlikte tam kapasiteyi doldurur ve $220$ değer sağlar.

Sorun, bir eşyanın parçasını alamamamızdır. Başlangıçta parlak görünen bir seçim, ileride daha iyi bir kombinasyonu engelleyebilir. Bu nedenle olası alt problemlerin sonuçlarını saklayan dinamik programlamaya ihtiyaç duyarız.

## 0-1 probleminde dinamik programlama

$dp[c]$, kapasitesi $c$ olan bir çantayla ulaşılabilecek en yüksek değeri temsil etsin. Her eşya için geçiş formülü şöyledir:

$$dp[c] = \max(dp[c],\ dp[c-w_i] + v_i)$$

```python
def zero_one_knapsack(items, capacity):
    dp = [0] * (capacity + 1)

    for value, weight in items:
        # Geriye doğru ilerlemek aynı eşyayı tekrar seçmeyi önler.
        for c in range(capacity, weight - 1, -1):
            dp[c] = max(dp[c], dp[c - weight] + value)

    return dp[capacity]
```

Kapasitelerin geriye doğru taranması kritik bir ayrıntıdır. İleri gidilseydi aynı eşyanın güncellenmiş sonucu tekrar kullanılabilir, böylece problem yanlışlıkla sınırsız sırt çantasına dönüşebilirdi.

## Hangisini ne zaman seçmeliyiz?

Eşyalar bölünebiliyorsa oranlara dayalı açgözlü çözüm hızlı, sade ve optimaldir. Eşyalar bölünemiyorsa seçimler birbirini etkiler; dinamik programlama kombinasyonları sistematik biçimde değerlendirir. Kısacası mesele yalnızca hızlı bir algoritma seçmek değil, problemin **açgözlü seçim özelliğine** sahip olup olmadığını anlamaktır. Algoritmalar dünyasında en cazip görünen eşya, her zaman çantaya ilk atılması gereken eşya değildir!
