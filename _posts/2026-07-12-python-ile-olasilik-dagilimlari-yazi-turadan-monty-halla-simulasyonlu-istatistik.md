---
layout: post
title: "Python ile Olasılık Dağılımları: Yazı-Turadan Monty Hall’a Simülasyonlu İstatistik"
math: true
categories: 
  - Program
tags: 
  - python
  - olasılık
  - simülasyon
  - istatistik
---

Olasılık teorisi ilk bakışta zarlar, paralar ve renkli toplarla oynanan masum bir oyun gibi görünür; fakat arka planda belirsizliği ölçmeye yarayan güçlü bir matematik dili vardır. Python ise bu dili deney masasına yatırmak için harika bir laboratuvardır. Yazı-tura simülasyonlarıyla büyük sayılar yasasını gözlemleyebilir, koşullu olasılık paradokslarıyla sezgilerimizin nasıl tökezlediğini görebiliriz.
``

## Olasılık dağılımı nedir?

Bir rassal değişkenin alabileceği değerleri ve bu değerlerin gerçekleşme olasılıklarını tarif eden yapıya **olasılık dağılımı** denir. Örneğin adil bir para için sonuç kümesi $S=\{Yazı, Tura\}$ ve her sonuç için olasılık $P(Yazı)=P(Tura)=0.5$ olur.

Eğer $X$, 10 atışta gelen yazı sayısını temsil ederse, $X$ artık binom dağılımına uyar:

$$P(X=k)=\binom{n}{k}p^k(1-p)^{n-k}$$

Burada $n$ deneme sayısı, $k$ başarı sayısı, $p$ ise tek denemedeki başarı olasılığıdır. Para adilse $p=0.5$.

| Kavram | Anlamı | Python’da karşılığı |
|---|---|---|
| Deney | Tekrarlanabilir süreç | Döngü, fonksiyon |
| Olay | İstenen sonuç kümesi | Koşul ifadesi |
| Olasılık | Olayın gerçekleşme oranı | Başarı / toplam |
| Dağılım | Olasılıkların deseni | Liste, sözlük, NumPy dizisi |

## Yazı-tura simülasyonu

Teorik olarak adil parada yazı oranı $0.5$ olmalıdır. Ama 10 atışta 8 yazı gelmesi şaşırtıcı değildir. Deneme sayısı büyüdükçe oran teorik değere yaklaşır. Buna **büyük sayılar yasası** denir.

```python
import random

def coin_flip_simulation(n):
    heads = 0
    ratios = []

    for i in range(1, n + 1):
        flip = random.choice(['Yazı', 'Tura'])
        if flip == 'Yazı':
            heads += 1
        ratios.append(heads / i)

    return heads, ratios

heads, ratios = coin_flip_simulation(10000)
print('Yazı sayısı:', heads)
print('Son oran:', ratios[-1])
```

Bu kodda her atış bağımsızdır; yani önceki sonucun sonraki sonucu etkilemediğini varsayarız. İşte bu nokta önemlidir: Art arda 5 kez tura gelmesi, bir sonraki atışta yazı olasılığını artırmaz. Hâlâ $P(Yazı)=0.5$.

## Dağılımı sayarak görmek

10 kez para atıp kaç yazı geldiğini bir kez hesaplamak yerine, bu deneyi binlerce kez tekrar edebiliriz. Böylece deneysel binom dağılımını elde ederiz.

```python
from collections import Counter
import random

def count_heads_in_trial(n):
    return sum(random.choice([0, 1]) for _ in range(n))

def binomial_experiment(trials, flips_per_trial):
    results = []
    for _ in range(trials):
        results.append(count_heads_in_trial(flips_per_trial))
    return Counter(results)

dist = binomial_experiment(20000, 10)
for heads_count in sorted(dist):
    print(heads_count, dist[heads_count] / 20000)
```

Burada 0’dan 10’a kadar yazı sayılarının göreli frekanslarını görürüz. Teorik olarak en yüksek değerler 5 civarında toplanır; çünkü 10 atışta 5 yazı gelme olasılığı uç değerlere göre daha fazladır.

| Yazı sayısı | Yorum |
|---|---|
| 0 veya 10 | Çok nadir, uç durum |
| 4, 5, 6 | En olası bölge |
| 1, 2, 8, 9 | Mümkün ama daha seyrek |

## Koşullu olasılık: Monty Hall paradoksu

Koşullu olasılık, bir olayın gerçekleştiğini bildiğimizde başka bir olayın olasılığını günceller. Formül şöyledir:

$$P(A|B)=\frac{P(A\cap B)}{P(B)}$$

Monty Hall probleminde 3 kapı vardır. Birinde araba, ikisinde keçi bulunur. Oyuncu bir kapı seçer. Sunucu, arabanın olmadığı bir kapıyı açar. Oyuncuya seçim değiştirme hakkı verilir. Sezgisel cevap “fark etmez, olasılık yarı yarıya” olabilir; ama doğru strateji değiştirmektir.

```python
import random

def monty_hall(change=True, trials=10000):
    wins = 0
    doors = [0, 1, 2]

    for _ in range(trials):
        car = random.choice(doors)
        choice = random.choice(doors)

        possible_opens = [d for d in doors if d != choice and d != car]
        opened = random.choice(possible_opens)

        if change:
            choice = [d for d in doors if d != choice and d != opened][0]

        if choice == car:
            wins += 1

    return wins / trials

print('Değiştirirse:', monty_hall(True))
print('Değiştirmezse:', monty_hall(False))
```

Sonuçlar genellikle değiştirme stratejisinin yaklaşık $\frac{2}{3}$, değiştirmeme stratejisinin ise yaklaşık $\frac{1}{3}$ kazandırdığını gösterir.

| Strateji | Kazanma olasılığı | Sezgisel mi? |
|---|---:|---|
| Kapıyı değiştirme | $1/3$ | Evet |
| Kapıyı değiştir | $2/3$ | Hayır, ama doğru |

## Sonuç

Python ile olasılık dağılımlarını modellemek, formülleri ezberlemekten daha kalıcı bir öğrenme sağlar. Simülasyonlar bize şunu öğretir: Kısa vadede rastgelelik gürültülüdür, uzun vadede ise matematik kendini belli eder. Yazı-tura örneği büyük sayılar yasasını, Monty Hall ise koşullu olasılığın sezgilerimize karşı nasıl galip geldiğini gösterir. Kısacası Python, istatistiği kuru bir konu olmaktan çıkarıp deney yapılabilir bir oyun alanına dönüştürür.
