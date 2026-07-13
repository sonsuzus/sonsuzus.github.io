---
layout: post
title: Kurbağanın Talihsiz Zıplamaları Kırık Basamak ve Olasılıkların Dansı
categories:
  - Program
tags:
  - program
  - oyun
  - random
  - montecarlo
  - olasılık
  - simülasyon
math: true
redirect_from:
  - /posts/ziplayan-kurbaga-problemi/
---

Bir [kurbağa](https://sonsuzus.github.io/search.html?q=kurba%C4%9Fa) düşünelim: her sıçrayışında ya bir ya da iki [basamak](https://sonsuzus.github.io/search.html?q=basamak) yukarı çıkıyor. Amacı 75. basamağa ulaşmak. Ancak ortada bir tehlike var: 38. basamak **[kırık](https://sonsuzus.github.io/search.html?q=k%C4%B1r%C4%B1k)** ve kurbağa o basamağa basarsa düşüyor. Bu yazıda, bu eğlenceli ama çetin problemi hem simülasyonla hem de matematiksel yöntemlerle ele alacağız.

## 🎯 Problemin Özeti

* Kurbağa 1. basamaktan başlıyor.
* Her adımda %50 olasılıkla 1 veya 2 basamak yukarı çıkıyor.
* Ve 38. basamak kırık: kurbağa oraya basarsa oyun biter.
* Amacı 75. basamağa ulaşmak.

### Cevaplamak istediğimiz iki soru:

1. **Kurbağanın 38. basamağa basma olasılığı nedir?**
2. **Kurbağa 38. basamağa hiç basmadan 75. basamağa basabilir mi? Olasılığı nedir?**

---

## 🎲 Monte Carlo Simülasyonu ile Yaklaşım

Simülasyon yöntemiyle bu soruları yaklaşık olarak cevaplayabiliriz. Aşağıdaki Python kodu bu yaklaşımı uygular:

```python
import random

def monte_carlo(N=1_000_000):
    temas38_sayisi = 0
    hedefe_ulasma_sayisi = 0

    for _ in range(N):
        konum = 1
        temas38 = False
        while konum < 75:
            adim = 1 if random.random() < 0.5 else 2
            konum += adim
            if konum == 38:
                temas38 = True
                break

        if temas38:
            temas38_sayisi += 1
        elif konum == 75:
            hedefe_ulasma_sayisi += 1

    p38 = temas38_sayisi / N
    p75 = hedefe_ulasma_sayisi / N
    return p38, p75

p38, p75 = monte_carlo()
print(p38, p75)
```

## 📊 Grafiksel Gösterim

Simülasyonun farklı hedef basamaklar için nasıl sonuç verdiğini de aşağıdaki gibi görselleştirebiliriz:

```python
import matplotlib.pyplot as plt

def grafik_ciz():
    temas_oranlari = []
    ulasma_oranlari = []
    N = 100_000

    for hedef in range(1, 76):
        temas38_sayisi = 0
        hedefe_ulasma_sayisi = 0

        for _ in range(N):
            konum = 1
            temas38 = False

            while konum < hedef:
                adim = 1 if random.random() < 0.5 else 2
                konum += adim
                if konum == 38:
                    temas38 = True
                    break

            if temas38:
                temas38_sayisi += 1
            elif konum == hedef:
                hedefe_ulasma_sayisi += 1

        temas_oranlari.append(temas38_sayisi / N)
        ulasma_oranlari.append(hedefe_ulasma_sayisi / N)

    plt.plot(range(1, 76), temas_oranlari, label="38'e basma")
    plt.plot(range(1, 76), ulasma_oranlari, label="Hedefe ulaşma (38'e basmadan)")
    plt.xlabel("Hedef Basamak")
    plt.ylabel("Olasılık")
    plt.legend()
    plt.title("Kurbağa Zıplama Simülasyonu")
    plt.grid(True)
    plt.show()

grafik_ciz()
```

Grafikte açıkça görüyoruz ki:

* Kurbağanın 38. basamağa basma olasılığı yaklaşık **%66.6**
* Kurbağanın 75. basamağa ulaşırken 38’e hiç basmama olasılığı ise **%22.2** civarında

---

## 📐 Matematiksel (Analitik) Yaklaşım

Bu problem aslında Fibonacci benzeri bir yapı oluşturur:

Kurbağa her adımda 1 veya 2 basamak atlayabildiği için,
$F(n) = F(n-1) + F(n-2)$ şeklinde bir yapı vardır.

Bu durumda 75. basamağa toplam kaç farklı yolla çıkılabileceğini hesaplayabiliriz. Ardından, 38. basamağa uğrayan ve uğramayan yollar ayrıştırılabilir.

```python
def count_paths(n, broken=None):
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        if i == broken:
            dp[i] = 0
        else:
            dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

# Tüm yollar (38 dahil)
total_paths = count_paths(75)

# 38. basamağa basan yollar (38'e kadar gidip oradan 75'e gidenler)
paths_through_38 = count_paths(38) * count_paths(75 - 38)

p_hit_38 = paths_through_38 / total_paths
p_avoid_38 = 1 - p_hit_38

print(f"38'e basma olasılığı: {p_hit_38:.6f}")
print(f"38'e basmadan 75'e ulaşma olasılığı: {p_avoid_38:.6f}")
```

### 📌 Sonuçlar

* **38. basamağa basma olasılığı:** $\frac{2}{3}$
* **38'e basmadan 75'e ulaşma olasılığı:** $\frac{2}{9}$

Bu değerler teorik olarak da doğrulanabilir. Simülasyon sonuçlarıyla oldukça uyumludur.

---

## 🧠 Sonuç ve Yorum

Bu basit gibi görünen soru, hem simülasyon hem de matematiksel analiz gerektiriyor. Gerçek hayatta da "kırık basamaklar" önümüze çıkabiliyor. Kurbağa bazen yanlış yere basıyor. Ama yeterince denersek, doğru yola ulaşma ihtimalimiz hep var.

Kodlayan kurbağalara selam olsun! 🐸💻

---

### 🔧 Kaynaklar ve Araştırma Önerisi

* Bu tür problemler "random walk" ve "Markov zincirleri" içinde yer alır.
* Benzer yapıdaki klasik problem: "1 ya da 2 adımda merdiveni çıkma yolları"
* Teorik olarak çözmek isterseniz dinamik programlama önerilir.
