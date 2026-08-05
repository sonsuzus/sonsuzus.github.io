---
layout: post
title: "Topolojik Sıralama ile Görevleri Rayına Oturtmak"
math: true
categories: 
  - Bilgi
tags: 
  - topolojik sıralama
  - graf algoritmaları
  - görev planlama
---

Bir projedeki görevleri gelişigüzel sıraya koymak, çatıyı temelden önce inşa etmeye benzeyebilir. Bazı işler ancak başka işler tamamlandıktan sonra başlayabilir. Topolojik sıralama, bu bağımlılıkları bozmadan geçerli bir çalışma sırası üretir; döngü tespiti ise planın kendi kuyruğunu kovalayan bir yılana dönüşüp dönüşmediğini gösterir.
``

## Problemi graf olarak düşünmek

Görev planlama problemi, **yönlü graf** ile modellenebilir. Her düğüm bir görevi, $u \rightarrow v$ kenarı ise “$u$ tamamlanmadan $v$ başlayamaz” ilişkisini temsil eder. Örneğin tasarım tamamlanmadan arayüz geliştirilemiyorsa `Tasarım → Arayüz` kenarı eklenir.

Topolojik sıralama, her kenar için $u$ düğümünün $v$ düğümünden önce geldiği doğrusal bir sıralamadır:

$$
(u,v) \in E \Rightarrow sıra(u) < sıra(v)
$$

Böyle bir sıralama yalnızca **yönlendirilmiş döngüsüz graflarda**, yani DAG yapılarında bulunur. Ayrıca sonuç her zaman benzersiz değildir. Birbirinden bağımsız iki görev farklı sıralarda yürütülebilir.

| Kavram | Anlamı | Planlamadaki karşılığı |
|---|---|---|
| Düğüm | Grafın bir elemanı | Görev veya iş paketi |
| Yönlü kenar | Tek yönlü ilişki | Ön koşul bağımlılığı |
| Giriş derecesi | Düğüme gelen kenar sayısı | Beklenen görev sayısı |
| Döngü | Başlangıca dönen yol | Çözülemeyen bağımlılık |
| Topolojik sıra | Bağımlılıklara uygun dizilim | Geçerli yürütme planı |

## Kahn algoritması

Kahn algoritması, giriş derecesi sıfır olan görevlerden başlar. Bunların beklediği hiçbir iş yoktur; dolayısıyla hemen yapılabilirler. Bir görev sıraya alındığında ona ait giden kenarlar kaldırılmış gibi düşünülür ve komşuların giriş dereceleri azaltılır.

```python
from collections import deque

def planla(graf):
    derece = {gorev: 0 for gorev in graf}

    for komsular in graf.values():
        for komsu in komsular:
            derece[komsu] += 1

    hazir = deque(g for g, d in derece.items() if d == 0)
    plan = []

    while hazir:
        gorev = hazir.popleft()
        plan.append(gorev)

        for sonraki in graf[gorev]:
            derece[sonraki] -= 1
            if derece[sonraki] == 0:
                hazir.append(sonraki)

    if len(plan) != len(graf):
        raise ValueError('Döngü var: geçerli plan üretilemedi!')

    return plan
```

Burada `hazir` kuyruğu, bütün ön koşulları tamamlanan görevleri tutar. Algoritma sonunda plana eklenen düğüm sayısı toplam düğüm sayısından küçükse bazı görevlerin giriş derecesi sıfıra inmemiştir. Bu durum bir döngü bulunduğunu kanıtlar.

Zaman karmaşıklığı $O(V+E)$, bellek karmaşıklığı da $O(V)$ düzeyindedir. Çünkü her düğüm ve kenar en fazla birkaç kez işlenir.

## DFS ile döngü tespiti

Alternatif yöntemde derinlik öncelikli arama kullanılır. Düğümler üç durumda tutulur: ziyaret edilmemiş, işleniyor ve tamamlandı. Arama sırasında “işleniyor” durumundaki bir düğüme geri dönülürse bir geri kenar, dolayısıyla döngü vardır.

| Yöntem | Güçlü yanı | Döngü sinyali |
|---|---|---|
| Kahn | Hazır görev kuyruğunu doğal biçimde üretir | Tüm düğümler işlenemez |
| DFS | Bağımlılık zincirlerini incelemek kolaydır | Aktif düğüme geri dönülür |

## Gerçek görev planlamasına uygulama

Diyelim ki görevler `Analiz`, `Tasarım`, `API`, `Arayüz` ve `Test` olsun. Analizden sonra tasarım; tasarımdan sonra API ve arayüz; ikisi tamamlandıktan sonra test yapılabilir. Geçerli sıralardan biri şöyledir:

```text
Analiz → Tasarım → API → Arayüz → Test
```

API ile arayüz arasında doğrudan bağımlılık bulunmadığı için sıraları değişebilir, hatta yeterli ekip varsa paralel yürütülebilirler. Topolojik sıralama tek başına süre veya kaynak optimizasyonu yapmaz; yalnızca bağımlılıklara uygunluğu garanti eder. Süreler eklenirse kritik yol, çalışan kapasiteleri eklenirse kaynak kısıtlı planlama gibi daha gelişmiş problemlere geçilir.

Kısacası topolojik sıralama “önce ne yapılmalı?” sorusunu, döngü tespiti ise “bu planın yapılması mümkün mü?” sorusunu yanıtlar. İyi bir görev yöneticisi ikisini birlikte kullanarak hem uygulanabilir plan üretir hem de daha işe başlamadan bağımlılık düğümlerini yakalar.
