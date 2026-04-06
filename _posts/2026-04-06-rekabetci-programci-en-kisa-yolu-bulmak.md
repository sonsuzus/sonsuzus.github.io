---
layout: post
title: Rekabetçi Programcı En Kısa Yolu Bulmak
math: true
categories:
  - Program
tags:
  - çizge
  - graph
  - en-kısa-yol
  - shortest-path
  - bellman-ford
  - dijkstra
  - floyd-warshall
  - c
  - programlama
  - algoritma
  - olimpiyat
  - yarışma
  - kodlama
  - matematik
  - kitap
---

Bir çizgede iki düğüm arasındaki en kısa yolu bulmak, pek çok pratik uygulamaya sahip temel bir problemdir. Klasik bir örnek, yol uzunlukları bilinen bir ağda iki şehir arasındaki en kısa rotayı hesaplamaktır. Ağırlıksız çizgelerde yol uzunluğu kenar sayısına eşit olduğundan BFS ile çözülebilir; bu bölümde ise ağırlıklı çizgeler için geliştirilmiş algoritmalara bakacağız.

## 13.1 Bellman–Ford Algoritması

**Bellman–Ford algoritması**[^1], başlangıç düğümünden çizgedeki tüm düğümlere en kısa mesafeyi bulur. Negatif döngü içermeyen her türlü çizgede çalışır; üstelik çizgede negatif döngü varsa bunu tespit edebilir.

Algoritma, başlangıç düğümüne 0, diğer tüm düğümlere sonsuz mesafe atayarak başlar. Her turda tüm kenarlar incelenerek mesafeler kısaltılmaya çalışılır. Hiçbir mesafe artık kısalımıyorsa algoritma durur.

### Örnek

Aşağıdaki 5 düğümlü ağırlıklı çizgede 1. düğümden başlayan Bellman–Ford adımları:

**Başlangıç:** Mesafeler $[0, \infty, \infty, \infty, \infty]$

**1. tur** — 1. düğümden çıkan tüm kenarlar mesafeleri azaltır:

$$[0,\ 5,\ 3,\ 7,\ \infty]$$

**2. tur** — $2 \to 5$ ve $3 \to 4$ kenarları devreye girer:

$$[0,\ 5,\ 3,\ 4,\ 7]$$

**3. tur** — Son bir güncelleme daha:

$$[0,\ 5,\ 3,\ 4,\ 6]$$

Artık hiçbir kenar mesafeyi azaltamaz; başlangıç düğümünden tüm düğümlere en kısa mesafeler bulunmuştur. Örneğin 1. düğümden 5. düğüme en kısa mesafe 3'tür.

### İmplementasyon

```cpp
// distance[i]: x düğümünden i düğümüne en kısa mesafe
// edges: (a, b, w) formatında kenar listesi

for (int i = 1; i <= n; i++) distance[i] = INF;
distance[x] = 0;

for (int i = 1; i <= n - 1; i++) {
    for (auto e : edges) {
        int a, b, w;
        tie(a, b, w) = e;
        distance[b] = min(distance[b], distance[a] + w);
    }
}
```

Algoritma $n - 1$ tur çalışır; her turda $m$ kenarı işler. Zaman karmaşıklığı $O(nm)$'dir. En kısa her yol en fazla $n - 1$ kenar içerdiğinden $n - 1$ tur sonunda tüm mesafeler kesinleşir. Pratikte son mesafeler çoğu zaman $n - 1$ turdan önce bulunur; bir tur boyunca hiçbir mesafe değişmezse algoritma erken sonlandırılabilir.

### Negatif Döngüler

Bellman–Ford algoritması çizgede negatif döngü bulunup bulunmadığını da kontrol eder. Örneğin $2 \to 3 \to 4 \to 2$ döngüsünün toplam ağırlığı $-4$ ise bu döngüyü içeren yolları sınırsız kısaltmak mümkün olur; bu durumda "en kısa yol" tanımsızlaşır.

Negatif döngüyü tespit etmek için $n$. bir tur daha koşulur. Bu turda herhangi bir mesafe hâlâ azalıyorsa çizgede negatif döngü vardır. Bu yöntem, başlangıç düğümünden bağımsız olarak çizgenin herhangi bir yerindeki negatif döngüyü yakalar.

### SPFA Algoritması

**SPFA** ("Shortest Path Faster Algorithm"), Bellman–Ford'un optimize edilmiş bir varyantıdır. Her turda tüm kenarları değil, yalnızca mesafesi azalan düğümlere bağlı kenarları inceler. Bunun için mesafesi azalabilen düğümleri bir kuyrukta tutar. Ortalama durumda Bellman–Ford'dan hızlıdır; ancak en kötü durumda zaman karmaşıklığı yine $O(nm)$'dir.

## 13.2 Dijkstra'nın Algoritması

**Dijkstra'nın algoritması**[^2], Bellman–Ford gibi başlangıç düğümünden tüm düğümlere en kısa mesafeleri bulur; fakat çok daha verimlidir ve daha büyük çizgelerde kullanılabilir. Tek koşul: **çizgede negatif ağırlıklı kenar bulunmamalıdır.**

Bellman–Ford'dan farklı olarak Dijkstra her kenarı yalnızca bir kez işler. Bu verimliliği, negatif ağırlıklı kenar bulunmaması garantisiyle sağlanır.

### Örnek

1. düğümden başlayarak 5 düğümlü ağırlıklı çizgede Dijkstra'nın adımları:

**Başlangıç:** $[0,\ \infty,\ \infty,\ \infty,\ \infty]$

**Adım 1** — 0 mesafeli 1. düğüm seçilir; komşularının mesafeleri güncellenir:

$$[0,\ 5,\ \infty,\ 9,\ 1]$$

**Adım 2** — 1 mesafeli 5. düğüm seçilir; 4. düğümün mesafesi 9'dan 3'e iner:

$$[0,\ 5,\ \infty,\ 3,\ 1]$$

**Adım 3** — 3 mesafeli 4. düğüm seçilir; 3. düğümün mesafesi 9 olur:

$$[0,\ 5,\ 9,\ 3,\ 1]$$

Dijkstra'nın önemli özelliği: bir düğüm seçildiğinde onun mesafesi **artık değişmez**. Örneğin bu aşamada 1, 5 ve 4. düğümlerin mesafeleri kesinleşmiştir.

**Son durum:**

$$[0,\ 5,\ 7,\ 3,\ 1]$$

### Negatif Kenarlar

Dijkstra, negatif kenarlarda hatalı sonuç üretebilir. Örneğin $-5$ ağırlıklı bir kenar varsa algoritma bu kenarın öncesindeki yüksek maliyeti geç fark eder ve yanlış en kısa yolu seçebilir. Bu durumda Bellman–Ford kullanılmalıdır.

### İmplementasyon

Verimli Dijkstra implementasyonu için işlenmemiş düğümler arasından mesafesi en küçük olanı hızla bulmak gerekir. Bunun için **öncelikli kuyruk** (priority queue) kullanılır.

C++'ın varsayılan öncelikli kuyruğu maksimum elemana öncelik verdiğinden, mesafeleri negatif tutarak minimum elemanın başa gelmesi sağlanır:

```cpp
// adj[a] = {b, w}: a'dan b'ye w ağırlığında kenar

priority_queue<pair<int,int>> q;
bool processed[N];

for (int i = 1; i <= n; i++) distance[i] = INF;
distance[x] = 0;
q.push({0, x});

while (!q.empty()) {
    int a = q.top().second; q.pop();
    if (processed[a]) continue;
    processed[a] = true;
    for (auto u : adj[a]) {
        int b = u.first, w = u.second;
        if (distance[a] + w < distance[b]) {
            distance[b] = distance[a] + w;
            q.push({-distance[b], b});
        }
    }
}
```

Öncelikli kuyrukta aynı düğüme ait birden fazla eleman bulunabilir; ancak yalnızca en kısa mesafeli olan işlenir (`processed` kontrolü sayesinde). Zaman karmaşıklığı $O(n + m \log m)$'dir: tüm düğümler işlenir ve her kenar için kuyruğa en fazla bir eleman eklenir[^3].

## 13.3 Floyd–Warshall Algoritması

**Floyd–Warshall algoritması**[^4], tek bir kaynaktan değil, **tüm düğüm çiftleri** arasındaki en kısa mesafeleri tek bir koşuda bulur. Diğer iki algoritmadan farklı olarak hem negatif kenarlarda hem de negatif döngü tespitinde kullanılabilir.

Algoritma, iki boyutlu bir mesafe matrisi tutar. Başlangıçta matris yalnızca doğrudan kenarlarla doldurulur. Sonra her düğüm sırayla **ara düğüm** olarak denenerek mevcut mesafeler kısaltılmaya çalışılır.

### Örnek

5 düğümlü ağırlıklı çizge için başlangıç matrisi (∞ = sonsuz):

|   | 1 | 2 | 3 | 4 | 5 |
|:-:|:-:|:-:|:-:|:-:|:-:|
| **1** | 0 | 5 | 1 | 9 | 1 |
| **2** | 5 | 0 | 2 | 1 | ∞ |
| **3** | 1 | 2 | 0 | 7 | ∞ |
| **4** | 9 | 1 | 7 | 0 | 2 |
| **5** | 1 | ∞ | ∞ | 2 | 0 |

**1. tur** (ara düğüm: 1) — 2 ile 4 arasında ve 2 ile 5 arasında yeni yollar keşfedilir.

**2. tur** (ara düğüm: 2) — 1–3 ve 3–5 arasında yeni yollar bulunur.

**3. tur** (ara düğüm: 3) — 2–4 arasındaki mesafe kısalır.

Tüm turlar bittikten sonra matris her iki düğüm arasındaki minimum mesafeleri tutar:

|   | 1 | 2 | 3 | 4 | 5 |
|:-:|:-:|:-:|:-:|:-:|:-:|
| **1** | 0 | 5 | 7 | 3 | 1 |
| **2** | 5 | 0 | 2 | 8 | 6 |
| **3** | 7 | 2 | 0 | 7 | 8 |
| **4** | 3 | 8 | 7 | 0 | 2 |
| **5** | 1 | 6 | 8 | 2 | 0 |

Örneğin 2 ile 4. düğüm arasındaki en kısa mesafe 8 olup $2 \to 3 \to 1 \to 5 \to 4$ yoluna karşılık gelir.

### İmplementasyon

Floyd–Warshall'ın en büyük avantajı son derece sade bir koda sahip olmasıdır:

```cpp
// Başlatma
for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= n; j++) {
        if (i == j) distance[i][j] = 0;
        else if (adj[i][j]) distance[i][j] = adj[i][j];
        else distance[i][j] = INF;
    }
}

// En kısa mesafeleri bulma
for (int k = 1; k <= n; k++) {
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            distance[i][j] = min(distance[i][j],
                                 distance[i][k] + distance[k][j]);
        }
    }
}
```

Üç iç içe döngü nedeniyle zaman karmaşıklığı $O(n^3)$'tür. Kodu sade olduğundan, tek bir en kısa yol bulmak gerekse bile çizge yeterince küçükse kullanılabilir.

## Algoritmaların Karşılaştırması

| Algoritma | Kaynak | Negatif kenar | Zaman karmaşıklığı |
|:---:|:---:|:---:|:---:|
| Bellman–Ford | Tek kaynak | ✓ (döngü tespiti de yapar) | $O(nm)$ |
| SPFA | Tek kaynak | ✓ | $O(nm)$ (ortalama daha hızlı) |
| Dijkstra | Tek kaynak | ✗ | $O(n + m \log m)$ |
| Floyd–Warshall | Tüm çiftler | ✓ | $O(n^3)$ |

[^1]: Algoritma R. E. Bellman ve L. R. Ford tarafından birbirinden habersiz biçimde sırasıyla 1958 ve 1956 yıllarında yayınlanmıştır.
[^2]: E. W. Dijkstra algoritmayı 1959 yılında yayınlamıştır; ancak orijinal makalesinde verimli bir implementasyondan bahsetmemiştir.
[^3]: Kendi öncelikli kuyruk yapısı tanımlanarak pozitif değerler de kullanılabilir; ancak implementasyon biraz daha uzun olur.
[^4]: Algoritma R. W. Floyd ve S. Warshall tarafından birbirinden habersiz biçimde 1962 yılında yayınlanmıştır.
