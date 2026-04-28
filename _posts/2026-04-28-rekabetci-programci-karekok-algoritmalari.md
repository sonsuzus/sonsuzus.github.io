---
layout: post
title: Rekabetçi Programcı Karekök Algoritmaları
math: true
excerpt_separator: "``"
categories:
  - Program
tags:
  - karekök-algoritmaları
  - square-root
  - mo-algoritması
  - blok-ayrıştırma
  - aralık-sorgusu
  - knapsack
  - tam-sayı-bölmesi
  - yazı-oluşturma
  - durum-işleme
  - grup-işleme
  - c
  - programlama
  - algoritma
  - olimpiyat
  - yarışma
  - kodlama
  - matematik
  - kitap
---

**Karekök algoritmaları**, zaman karmaşıklığı $O(\sqrt{n})$ bileşeni içeren algoritmalardır. Karekök, "fakir adamın logaritması" olarak nitelendirilebilir:

$$O(\log n) \;<\; O(\sqrt{n}) \;<\; O(n)$$

Pratikte karekök algoritmaları hem yeterince hızlı hem de uygulaması görece basittir. Temel fikir, bir diziyi $\sqrt{n}$ büyüklüğündeki **bloklara** ayırmaktır.
``

## Temel Yapı: Blok Ayrıştırma

$n$ elemanlı bir dizi üzerinde iki işlem desteklenmek istensin:

- **Güncelleme:** Belirli bir pozisyondaki elemanı değiştir.
- **Toplam sorgusu:** $[a, b]$ aralığındaki elemanların toplamını bul.

Dizi $\sqrt{n}$ büyüklüğünde bloklara ayrılır; her blok kendi toplamını tutar.

```
5 | 8 | 20 | 17 ||  6 | 3 | 2 | 7 || 13 | 1 | 5 | 6 || 3 | 2 | 2 | ?
       50          ||      18        ||       25        ||       7
```

- **Güncelleme:** Elemanı değiştir, yalnızca o bloğun toplamını güncelle → $O(1)$
- **Toplam sorgusu:** Aralığı üç parçaya böl — sol kenardaki tek elemanlar + tam kaplanan bloklar + sağ kenardaki tek elemanlar → $O(\sqrt{n})$

Blok büyüklüğü $k$ seçilirse güncelleme $O(1)$, sorgu $O(k + n/k)$ zaman alır. $k = \sqrt{n}$ bu ikisini dengeler. Pratikte tam $\sqrt{n}$ yerine dengelemeye göre farklı $k$ değerleri kullanılabilir.

## 27.1 Algoritmaları Birleştirme

Karekök eşiği iki farklı algoritmayı birleştirir: küçük durumlar için biri, büyük durumlar için diğeri. Her iki algoritma da tek başına $O(n^2)$ iken birleşince $O(n\sqrt{n})$'e iner.

### Durum İşleme (Case Processing)

$n$ hücreli iki boyutlu bir yapıda her hücrede bir harf var. Aynı harfe sahip, aralarındaki **Manhattan mesafesi** en kısa iki hücreyi bul.

İki algoritma:

1. **1. Algoritma:** $c$ harfine sahip $k$ hücrenin tüm çiftlerini tara → $O(k^2)$
2. **2. Algoritma:** $c$ harfine sahip tüm hücrelerden aynı anda BFS başlat → $O(n)$

**Karekök birleştirmesi:**

$$\text{Eğer } k \leq \sqrt{n}: \text{ 1. Algoritma} \quad\mid\quad \text{Eğer } k > \sqrt{n}: \text{ 2. Algoritma}$$

- $k \leq \sqrt{n}$ olan harfler: her hücre en fazla $\sqrt{n}$ kez karşılaştırılır → toplam $O(n\sqrt{n})$
- $k > \sqrt{n}$ olan harfler: en fazla $\sqrt{n}$ çeşit böyle harf olabilir → toplam $O(n\sqrt{n})$

**Genel toplam:** $O(n\sqrt{n})$

### Grup İşleme (Batch Processing)

$n$ hücreli yapıda başta bir hücre siyah, geri kalanı beyaz. $n-1$ işlem yapılır: her işlemde beyaz bir hücreden en yakın siyah hücreye mesafe bulunur, ardından o hücre siyaha boyanır.

İki algoritma:

1. **1. Algoritma:** Tüm siyah hücrelerden BFS yap → $O(n)$; ardından herhangi bir hücreden en yakın siyah hücreye mesafe $O(1)$'de bulunur.
2. **2. Algoritma:** Siyah hücreleri listede tut; her işlemde listeden geç → $O(k)$ ($k$: liste uzunluğu)

**Karekök birleştirmesi:** İşlemleri $\sqrt{n}$ büyüklüğünde gruplara böl.

- Her grubun başında **1. Algoritma** uygulanır → $O(n)$, toplam $O(n\sqrt{n})$
- Grup içinde **2. Algoritma** kullanılır; liste $\sqrt{n}$'den büyümez (her grup başında temizlenir) → her işlem $O(\sqrt{n})$, toplam $O(n\sqrt{n})$

**Genel toplam:** $O(n\sqrt{n})$

## 27.2 Tamsayı Bölmesi

**Gözlem:** $n$ pozitif tamsayısı, farklı pozitif tamsayıların toplamı olarak yazılırsa bu toplam en fazla $O(\sqrt{n})$ terim içerir.

**Kanıt:** En fazla terim sayısı için $1 + 2 + \cdots + k = \frac{k(k+1)}{2} \leq n$ olmalı, buradan $k = O(\sqrt{n})$.

Bu gözlem bazı algoritmalarda $O(n\sqrt{n})$ sınırı elde etmek için kullanılır.

### Sırt Çantası (Knapsack)

Toplamları $n$ olan tamsayı ağırlıklar verilsin; bu ağırlıklarla oluşturulabilecek tüm toplamları bul.

- **Klasik DP yaklaşımı:** $O(n^2)$
- **Karekök iyileştirmesi:** Aynı ağırlıktan en fazla $O(\sqrt{n})$ farklı değer olduğu bilindiğinden, aynı ağırlıklıları gruplar hâlinde işle. Her grup $O(n)$'de, toplam $O(n\sqrt{n})$'de çözülür.

Fikir: $n$ elemanlık bir "ulaşılabilir toplam" dizisi tutulur (1: ulaşılabilir, 0: ulaşılamaz). Grupları soldan sağa işlerken yeni ulaşılabilir değerler kaydedilir.

### Yazı Oluşturma (String Construction)

$n$ uzunluğundaki $s$ yazısı ile toplam uzunluğu $m$ olan $D$ yazı kümesi verilsin. $D$'deki yazıları birleştirerek $s$'yi kaç farklı şekilde oluşturabiliriz?

**DP tanımı:** $\text{count}(k)$ = $s[0 \ldots k]$'yı $D$'den yazılarla oluşturma yolu sayısı.

- **Trie ile:** $O(n^2)$
- **Hash + karekök:** $D$'de en fazla $O(\sqrt{m})$ farklı yazı uzunluğu vardır. Her $\text{count}(k)$ hesaplanırken bu uzunluklar taranır; her adım $O(\sqrt{m})$, toplam $O(n\sqrt{m})$.

## 27.3 Mo'nun Algoritması

**Mo'nun Algoritması**, **sabit** (sorgu sırasında değişmeyen) diziler üzerindeki aralık sorgularını verimli işler. Her sorgu $[a, b]$ aralığındaki elemanlardan bir değer ister.

Dizi sabit olduğu için sorgular **istenen sırada** işlenebilir; Mo'nun Algoritması bu sırayı akıllıca seçerek toplam işlem sayısını minimize eder.

### Temel Fikir

Algoritma bir **aktif aralık** $[l, r]$ tutar. Her sorgu için bu aralığın sınırları eleman ekleyerek veya çıkararak kaydırılır. Her kaydırma adımı $O(f(n))$ zaman alırsa toplam karmaşıklık:

$$O\!\left(n\sqrt{n}\cdot f(n)\right)$$

### Sıralama Stratejisi

Dizi $k = O(\sqrt{n})$ büyüklüğünde bloklara ayrılır. $[a_1, b_1]$ sorgusu $[a_2, b_2]$'den **önce** işlenir; eğer:

$$\lfloor a_1 / k \rfloor < \lfloor a_2 / k \rfloor \qquad\text{veya}$$
$$\lfloor a_1 / k \rfloor = \lfloor a_2 / k \rfloor \text{ ve } b_1 < b_2$$

Yani: **Aynı blokta** olanlar sağ bitiş noktasına göre artan sırada; farklı bloklar soldan sağa işlenir.

### Hareket Analizi

Bu sıralama ile:

- **Sol bitiş noktası:** Her blok geçişinde en fazla $O(\sqrt{n})$ hareket eder. $O(\sqrt{n})$ blok vardır → toplam $O(n\sqrt{n})$ hareket.
- **Sağ bitiş noktası:** Her blok içinde monoton artar, o blok bitince sıfırlanır. Her blok $O(n)$ hareket → toplam $O(n\sqrt{n})$ hareket.

**Her iki bitiş noktası toplamda $O(n\sqrt{n})$ adım atar.**

### Örnek: Aralıkta Farklı Eleman Sayısı

Her $[a, b]$ sorgusunda aralıkta kaç farklı eleman olduğu bulunacak.

**Veri yapısı:** `count[x]` → $x$ elemanının aktif aralıkta kaç kez geçtiği.

- **Eleman ekle ($x$):** `count[x]++`; eğer `count[x] == 1` oldu ise cevabı 1 artır.
- **Eleman çıkar ($x$):** `count[x]--`; eğer `count[x] == 0` oldu ise cevabı 1 azalt.

Her adım $O(1)$ → toplam $O(n\sqrt{n})$.

**Örnek geçiş:**

| Aktif aralık | Sonraki aralık | Sol kayma | Sağ kayma |
|---|---|---|---|
| $[3, 7]$ | $[4, 9]$ | 1 adım sağ | 2 adım sağ |

```
4  2  5  4  2  4  3  3  4
         [3..7]
            [4..9]
```

---

> **Kaynak:** *Rekabetçi Programcı* (Competitive Programmer's Handbook — Antti Laaksonen), Bölüm 27.
