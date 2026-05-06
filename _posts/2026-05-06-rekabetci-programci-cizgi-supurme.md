---
layout: post
title: Rekabetçi Programcı Çizgi Süpürme Algoritmaları
math: true
excerpt_separator: "``"
categories:
  - Program
tags:
  - çizgi-süpürme
  - sweep-line
  - kesişim-noktaları
  - en-yakın-çift
  - convex-hull
  - andrew-algoritması
  - segment-ağacı
  - ikili-indeksli-ağaç
  - geometri
  - olay-tabanlı
  - c
  - programlama
  - algoritma
  - olimpiyat
  - yarışma
  - kodlama
  - matematik
  - kitap
---

**Çizgi süpürme algoritmaları**, geometrik problemleri düzlemdeki noktaları temsil eden **olaylar** kümesine dönüştürerek çözer. Olaylar $x$ veya $y$ koordinatına göre sıralanır ve soldan sağa (ya da aşağıdan yukarıya) sırayla işlenir; böylece iki boyutlu problem tek boyutlu bir taramaya indirgenir.

**Motivasyon örneği:** $n$ çalışanı olan bir ofiste her çalışanın giriş ve çıkış saatleri bilinmektedir. Herhangi bir anda ofiste bulunan en fazla çalışan sayısını bul.

Her çalışan iki olay üretir: **giriş (+1)** ve **çıkış (−1)**. Olaylar zamana göre sıralanır ve bir sayaç tutulur:
``

| Kişi | Giriş | Çıkış |
|---|---|---|
| John | 10 | 15 |
| Maria | 6 | 12 |
| Peter | 14 | 16 |
| Lisa | 5 | 13 |

Olaylar soldan sağa işlendiğinde sayaç değerleri:

$$+\ +\quad +\quad -\ -\ +\ -\ -$$
$$1\ \ 2\quad 3\quad 2\ \ 1\ \ 2\ \ 1\ \ 0$$

Maksimum değer **3** olup John'un gelişi ile Maria'nın çıkışı arasındaki aralıktır.

**Karmaşıklık:** Olayları sıralamak $O(n \log n)$, tarama $O(n)$ → **toplam $O(n \log n)$**.

## 30.1 Kesişim Noktaları

$n$ yatay veya dikey çizginin toplam kesişim noktası sayısını bul.

Kaba kuvvetle tüm çift çiftler $O(n^2)$'de incelenebilir. Çizgi süpürme + aralık sorgu veri yapısıyla bu **$O(n \log n)$**'e iner.

### Olay Türleri

Her çizgi en fazla iki olay üretir:

| Olay | Açıklama |
|---|---|
| **(1) Yatay çizgi başlıyor** | Bu çizginin $y$ koordinatını aktif kümeye **ekle** |
| **(2) Yatay çizgi bitiyor** | Bu çizginin $y$ koordinatını aktif kümeden **çıkar** |
| **(3) Dikey çizgi** | Aktif kümede $[y_1, y_2]$ aralığında kaç $y$ koordinatı var? → bu sayı kesişim sayısına eklenir |

### Algoritmanın İşleyişi

Olaylar $x$ koordinatına göre soldan sağa sıralanır. Aktif yatay çizgilerin $y$ koordinatları **sıralı bir veri yapısında** (ikili indeksli ağaç veya segment ağacı) tutulur.

```
Dikey çizgi geldiğinde:
  → [y1, y2] aralığındaki aktif y koordinatlarını say
  → Bu sayıyı toplam kesişim sayısına ekle
```

**İndis sıkıştırması:** $y$ koordinatları $[0, m]$ aralığına eşlenerek segment ağacı verimli kullanılır.

Her olayı işlemek $O(\log n)$ → **toplam $O(n \log n)$**.

**Görsel örnek:**

```
      |          |
------+----------+------   ← yatay çizgi 1
      |          |
      |    ------+------   ← yatay çizgi 2
      |          |
  dikey 1    dikey 2
```

- Dikey 1 geldiğinde aktif kümede yatay çizgi 1 var → 1 kesişim
- Dikey 2 geldiğinde aktif kümede yatay çizgi 1 ve 2 var → 2 kesişim
- **Toplam: 3 kesişim** ✓

## 30.2 En Yakın Çift Problemi

$n$ nokta arasında **Öklid uzaklığı en küçük** olan iki noktayı bul.

Kaba kuvvetle tüm çiftler $O(n^2)$'de incelenebilir. Çizgi süpürme ile **$O(n \log n)$** mümkündür (böl ve yönet yöntemi de aynı karmaşıklığı verir).

### Algoritma

**Değişkenler:**
- Noktalar $x$ koordinatına göre soldan sağa sıralanır.
- $d$: şu ana kadar bulunan minimum mesafe.
- Aktif küme: $x$ koordinatı $[x - d, x]$ aralığında olan noktalar (y'ye göre sıralı tutulur).

**Her yeni $p = (x, y)$ noktası için:**

1. Aktif kümeden $x$ koordinatı $x - d$'den küçük olanları çıkar.
2. Aktif kümede $y$ koordinatı $[y - d,\ y + d]$ aralığındaki noktaları tara; hepsine uzaklığı hesapla.
3. $d$ güncellendi mi? Güncellendiyse aktif küme yeniden ayarlanır.
4. $p$'yi aktif kümeye ekle.

### Neden Verimli?

Kilit gözlem: Taranan $d \times 2d$'lik dikdörtgen bölge her zaman **$O(1)$ nokta** içerir.

```
     2d
   ┌────────────┐
 d │            │
   │    p →     │
 d │            │
   └────────────┘
       ← d →
```

Bu bölgede $d$ eşiği nedeniyle noktalar birbirinden en az $d$ uzaklıktadır; dolayısıyla $2d \times d$'lik alana sığabilecek maksimum nokta sayısı sabittir (yaklaşık 6–8).

Noktalar $y$'ye göre sıralı kümede tutulduğundan $[y-d, y+d]$ aralığı $O(\log n)$'de sorgulanır.

**Toplam karmaşıklık:** $n$ nokta × $O(\log n)$ sorgu = **$O(n \log n)$**

### C++ İskeleti

```cpp
set<pair<long long,long long>> active; // {y, x} sıralı küme
sort(points.begin(), points.end());    // x'e göre sırala
long long d = INF;
int left = 0;

for (auto [x, y] : points) {
    // Sola çok uzaklaşanları çıkar
    while (points[left].x < x - d) {
        active.erase({points[left].y, points[left].x});
        left++;
    }
    // [y-d, y+d] aralığını tara
    for (auto it  = active.lower_bound({y - d, LLONG_MIN});
              it != active.end() && it->first <= y + d; ++it) {
        d = min(d, dist({x, y}, {it->second, it->first}));
    }
    active.insert({y, x});
}
```

## 30.3 Convex Hull

**Convex hull** (dışbükey zarf), bir nokta kümesindeki tüm noktaları kapsayan **en küçük dışbükey çokgendir**. Dışbükeylik: çokgendeki herhangi iki nokta arasındaki doğru parçası tamamen çokgenin içinde kalır.

**Andrew'in Algoritması** $O(n \log n)$'de convex hull oluşturur.

### Fikir: İki Yarı

Convex hull **üst hull** ve **alt hull** olmak üzere iki parçaya ayrılır. Her iki parça da benzer şekilde hesaplanır; burada yalnızca **üst hull** ele alınır.

### Algoritma Adımları

1. Noktaları önce $x$'e göre, eşit $x$'lerde $y$'ye göre **sırala**.
2. Sıralı noktalardan geçerek her noktayı hull'a ekle.
3. Her eklemede **son üç nokta sola mı dönüyor?** Kontrol et:
   - Sola dönüş varsa → ortadaki noktayı hull'dan **sil** (dışbükey değil).
   - Ta ki sola dönüş kalmayana dek tekrarla.

**Yön kontrolü:** Vektörel çarpımla yapılır. $A$, $B$, $C$ üç noktasında:

$$(B - A) \times (C - A) > 0 \implies \text{sola dönüş (hull'a almama)}$$

### Adım Adım Görselleştirme

```
Başlangıç noktaları (x'e göre sıralı):
  1   2   3   4   5   6   7
  ·   ·   ·   ·   ·   ·   ·

Üst hull oluşturma (sola dönen noktalar elenir):
  Adım 1: [1]
  Adım 2: [1, 2]
  Adım 3: [1, 2, 3]  → 2 sola dönüş yaratıyor mu? Evet → sil
           [1, 3]
  Adım 4: [1, 3, 4]  → kontrol et...
  ...
  Son: [1, 5, 7]  (üst hull)
```

### Karmaşıklık

| Adım | Süre |
|---|---|
| Sıralama | $O(n \log n)$ |
| Hull oluşturma | $O(n)$ (her nokta en fazla bir kez eklenir/çıkarılır) |
| **Toplam** | **$O(n \log n)$** |

### C++ Kodu (Üst Hull)

```cpp
// Noktalar x'e göre sıralanmış varsayılır
vector<P> upper_hull(vector<P>& pts) {
    vector<P> h;
    for (auto p : pts) {
        // Son iki nokta ile p sola dönüyor mu?
        while (h.size() >= 2) {
            P a = h[h.size()-2], b = h[h.size()-1];
            // Vektörel çarpım: (b-a) × (p-a)
            if ((conj(b-a) * (p-a)).Y <= 0)
                h.pop_back();  // sola dönüş yok → sil
            else break;
        }
        h.push_back(p);
    }
    return h;
}
```

Alt hull için noktaları ters sırada işle; iki hull birleştirilince tam convex hull elde edilir.

---

> **Özet Tablo**

| Problem | Kaba Kuvvet | Çizgi Süpürme |
|---|---|---|
| Maks. eş zamanlı çalışan | $O(n^2)$ | $O(n \log n)$ |
| Çizgi kesişim sayısı | $O(n^2)$ | $O(n \log n)$ |
| En yakın çift | $O(n^2)$ | $O(n \log n)$ |
| Convex hull | $O(n^2)$ | $O(n \log n)$ |

Tüm problemlerde ortak yapı aynıdır: **olayları sırala, veri yapısıyla tara**.

---

> **Kaynak:** *Rekabetçi Programcı* (Competitive Programmer's Handbook — Antti Laaksonen), Bölüm 30.
