---
layout: post
title: Rekabetçi Programcı Ağaç Sorguları
math: true
excerpt_separator: "``"
categories:
  - Program
tags:
  - ağaç
  - tree
  - köklü-ağaç
  - ata
  - ancestor
  - lca
  - en-yakın-ortak-ata
  - lowest-common-ancestor
  - euler-turu
  - ağaç-dolaşma-dizisi
  - binary-lifting
  - union-find
  - segment-tree
  - dfs
  - c
  - programlama
  - algoritma
  - olimpiyat
  - yarışma
  - kodlama
  - matematik
  - kitap
---

Bu bölümde köklü ağaçların alt ağaçları ve yolları üzerinde yapılan sorguları çözme yöntemlerini inceliyoruz. Ele alınan sorgu türleri şunlardır:

- Bir düğümün $k$. atası hangi düğümdür?
- Bir alt ağaçtaki değerlerin toplamı kaçtır?
- İki düğüm arasındaki yolda bulunan değerlerin toplamı kaçtır?
- İki düğümün en yakın ortak atası hangisidir?
``

## 18.1 Ataları Bulmak

Köklü bir ağaçta $x$ düğümünün **$k$. atası**, $x$'ten $k$ defa yukarı çıkıldığında ulaşılan düğümdür. $\text{ancestor}(x, k)$ ile gösterilir; eğer bu ata yoksa değer $0$ kabul edilir. Örneğin bir ağaçta $\text{ancestor}(2, 1) = 1$ ve $\text{ancestor}(8, 2) = 4$ olabilir.

Naif yöntemle $\text{ancestor}(x, k)$, ağaçta $k$ adım yukarı çıkılarak bulunur; ancak bu $O(k)$ zaman alır ve $n$ düğümlü bir zincir şeklindeki ağaçta oldukça yavaş kalabilir.

**İkili kaldırma (binary lifting)** ile Bölüm 16.3'teki ardıl yol tekniğine benzer biçimde $\text{ancestor}(x, k)$ değeri $O(\log k)$ zamanda hesaplanabilir. Her düğüm için $2$'nin kuvvetlerine karşılık gelen atalar önceden hesaplanır:

| $x$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|:---:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| $\text{ancestor}(x, 1)$ | 0 | 1 | 4 | 1 | 1 | 2 | 4 | 7 |
| $\text{ancestor}(x, 2)$ | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 4 |
| $\text{ancestor}(x, 4)$ | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

Ön işleme $O(n \log n)$ zaman alır; her düğüm için $O(\log n)$ değer hesaplanır. Ardından herhangi bir $\text{ancestor}(x, k)$ değeri, $k$'yı $2$'nin kuvvetlerinin toplamı olarak ifade ederek $O(\log k)$ zamanda bulunabilir.

## 18.2 Alt Ağaçlar ve Yollar

**Ağaç dolaşma dizisi** (tree traversal array), köklü bir ağacın düğümlerini kök düğümünden başlayan DFS ziyaret sırasına göre sıralar. Örneğin aşağıdaki ağaçta:

```
        1
      / | \ \
     2  3  4  5
     |     |\ 
     6     7 8
             |
             9
```

DFS sırası ve ağaç dolaşma dizisi şöyle olur:

$$[1,\ 2,\ 6,\ 3,\ 4,\ 7,\ 8,\ 9,\ 5]$$

### Alt Ağaç Sorguları

Bir ağaçtaki her alt ağaç, dolaşma dizisinin **ardışık bir alt dizisine** karşılık gelir. Bu alt dizinin ilk elemanı alt ağacın kök düğümüdür. Örneğin 4. düğümün alt ağacı aşağıdaki vurgulanan bölüme denk gelir:

$$[1,\ 2,\ 6,\ 3,\ \mathbf{4,\ 7,\ 8,\ 9},\ 5]$$

Bu yapıyı kullanarak şu iki sorguyu verimli biçimde çözebiliriz:

- Bir düğümün değerini güncelle.
- Bir düğümün alt ağacındaki değerlerin toplamını hesapla.

Her düğüm için üç değer tutan bir dolaşma dizisi oluşturulur: düğüm kimliği, alt ağaç büyüklüğü ve düğümün değeri. Örnek ağaç için:

| düğüm              | 1 | 2 | 6 | 3 | 4 | 7 | 8 | 9 | 5 |
|:------------------:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| alt ağaç büyüklüğü | 9 | 2 | 1 | 1 | 4 | 1 | 1 | 1 | 1 |
| düğümün değeri     | 2 | 3 | 4 | 5 | 3 | 4 | 3 | 1 | 1 |

4. düğümün alt ağaç toplamı alt ağaç büyüklüğü sayesinde doğrudan tespit edilir: $3 + 4 + 3 + 1 = 11$. Bu sorguları $O(\log n)$ sürede çözmek için değerleri bir **ikili indeksli ağaç** (binary indexed tree / Fenwick tree) ya da **bölüm ağacı** (segment tree) üzerinde tutmak yeterlidir.

### Yol Sorguları

Ağaç dolaşma dizisi, kök düğümden herhangi bir düğüme uzanan yoldaki değerlerin toplamını bulmak için de kullanılabilir. Çözülmek istenen sorgular:

- Bir düğümün değerini değiştir.
- Kökten bir düğüme uzanan yoldaki değerlerin toplamını hesapla.

Bu kez dolaşma dizisinin son satırında her düğüm için köke olan **yol toplamı** tutulur:

| düğüm              | 1 | 2 |  6 | 3 | 4 |  7 |  8 |  9 | 5 |
|:------------------:|:-:|:-:|:--:|:-:|:-:|:--:|:--:|:--:|:-:|
| alt ağaç büyüklüğü | 9 | 2 |  1 | 1 | 4 |  1 |  1 |  1 | 1 |
| yol toplamı        | 4 | 9 | 12 | 7 | 9 | 14 | 12 | 10 | 6 |

Bir düğümün değeri $x$ arttırıldığında, onun alt ağacındaki tüm düğümlerin yol toplamı $x$ kadar artar. Örneğin 4. düğümün değeri 1 arttırılırsa:

| düğüm              | 1 | 2 |  6 | 3 |  4 |  7 |  8 |  9 | 5 |
|:------------------:|:-:|:-:|:--:|:-:|:--:|:--:|:--:|:--:|:-:|
| alt ağaç büyüklüğü | 9 | 2 |  1 | 1 |  4 |  1 |  1 |  1 | 1 |
| yol toplamı        | 4 | 9 | 12 | 7 | 10 | 15 | 13 | 11 | 6 |

Bu işlem bir aralıktaki tüm değerleri artırma ve tekil bir değeri okuma sorgusuna dönüşür; her ikisi de ikili indeksli ağaç veya bölüm ağacı ile $O(\log n)$ zamanda yapılabilir (bkz. Bölüm 9.4).

## 18.3 En Yakın Ortak Ata (LCA)

İki düğümün **en yakın ortak atası** (Lowest Common Ancestor, LCA), köklü ağaçta her iki düğümü de alt ağacında barındıran en alttaki düğümdür. Örneğin 5 ve 8. düğümünün LCA'sı 2. düğümdür.

### 1. Yöntem: İkili Kaldırma

Bu yöntem, $k$. atayı verimli bulan ön işlemeye (18.1) dayanır. İki adımdan oluşur:

**Adım 1 — Aynı derinliğe getir:** İki düğümü gösteren işaretçiler tutulur. Daha derinde olan işaretçi, diğeriyle aynı derinliğe gelene kadar yukarı taşınır. Örneğin 8. düğümü gösteren işaretçi bir seviye yukarı çıkıp 6. düğümü gösterince 5. düğümle aynı seviyeye ulaşır.

**Adım 2 — Birlikte yukarı çık:** İki işaretçi aynı düğüme ulaşana kadar gereken minimum adım sayısı ikili kaldırmayla hesaplanır; her iki işaretçi bu kadar yukarı taşınır. İşaretçilerin buluştuğu düğüm LCA'dır.

Her iki adım da $O(\log n)$ zamanda çalışır.

### 2. Yöntem: Euler Turu

Bu yöntemde DFS sırasında her düğüm yalnızca ilk ziyarette değil, **her ziyarette** diziye eklenir. $k$ çocuğu olan bir düğüm dizide $k + 1$ kez yer alır; dolayısıyla toplam dizi uzunluğu $2n - 1$ olur.

Dizi iki değer tutar: düğüm kimliği ve derinlik. Örnek ağaç için dizi:

| indeks | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
|:------:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:--:|:--:|:--:|:--:|:--:|
| düğüm  | 1 | 2 | 5 | 2 | 6 | 8 | 6 | 2 | 1 | 3 |  1 |  4 |  7 |  4 |  1 |
| derinlik | 1 | 2 | 3 | 2 | 3 | 4 | 3 | 2 | 1 | 2 |  1 |  2 |  3 |  2 |  1 |

$a$ ve $b$ düğümlerinin LCA'sı, dizide $a$ ile $b$'nin konumları arasındaki **minimum derinlikli** düğüme karşılık gelir. Örneğin 5. düğüm dizinin 2. indeksinde, 8. düğüm ise 5. indeksindedir. $[2, 5]$ aralığında minimum derinlik 2 olup bu 3. indeksteki 2. düğüme karşılık gelir; dolayısıyla LCA = 2.

Bu sayede LCA sorgusu bir **aralık minimum sorgusuna** dönüşür. Dizi statik olduğundan $O(n \log n)$ ön işlemeyle sonraki her sorgu $O(1)$ zamanda yanıtlanabilir.

### Düğümler Arası Mesafe

$a$ ile $b$ arasındaki mesafe, LCA bulunduktan sonra şu formülle hesaplanır:

$$\text{dist}(a, b) = \text{depth}(a) + \text{depth}(b) - 2 \cdot \text{depth}(\text{lca}(a, b))$$

Örneğin 5 ve 8. düğümler için LCA = 2, $\text{depth}(5) = 3$, $\text{depth}(8) = 4$, $\text{depth}(2) = 2$ olduğundan:

$$\text{dist}(5, 8) = 3 + 4 - 2 \cdot 2 = 3$$

## 18.4 Çevrimdışı Algoritmalar

Şimdiye kadar incelenen algoritmalar **çevrimiçi**dir; yani her sorguyu bir sonraki gelmeden yanıtlayabilirler. Ancak pek çok problemde bu özellik zorunlu değildir. **Çevrimdışı** algoritmalarda tüm sorgular önceden bilinir ve herhangi bir sırayla yanıtlanabilir; bu da genellikle daha kolay implementasyona olanak tanır.

### Veri Yapılarını Birleştirmek

Çevrimdışı yaklaşımın bir yolu, DFS sırasında her düğümde bir veri yapısı $d[s]$ oluşturmak ve çocukların veri yapılarını bu yapıyla birleştirmektir.

Örneğin şu problemi düşünelim: her düğümde bir değer bulunan ağaçta, "$s$ düğümünün alt ağacında $x$ değerine sahip kaç düğüm var?" sorgularını yanıtlamak istiyoruz. Çözüm için `map` veri yapısı kullanılabilir.

Naif yaklaşımda her düğüm için baştan bir map oluşturmak çok yavaş olur. Bunun yerine her $s$ düğümü için yalnızca kendi değerini içeren bir başlangıç $d[s]$ oluşturulur; ardından her çocuk $u$ için $d[u]$ ile $d[s]$ birleştirilir. Birleştirme sırasında $d[s]$, $d[u]$'dan küçükse önce yer değiştirme yapılır:

```cpp
swap(a, b);
```

Bu fonksiyon, C++ standart kütüphanesi veri yapıları için sabit zamanda çalışır. Bu strateji sayesinde her değer ağaç dolaşımı boyunca en fazla $O(\log n)$ kez kopyalanır ve algoritma verimli kalır.

### Çevrimdışı LCA: Tarjan'ın Algoritması

En yakın ortak ataları çevrimdışı bulmak için Tarjan'ın Algoritması kullanılabilir. Bu algoritma, **union-find** yapısı üzerine kurulu olup (bkz. Bölüm 15.2) bölümün başında anlatılan çevrimiçi yöntemlere kıyasla daha kolay koda dökülebilir.

Girdi olarak düğüm çiftleri alınır ve her çift için LCA hesaplanır. Algoritma DFS ile ağacı dolaşırken ayrık gruplar tutar; başlangıçta her düğüm ayrı bir gruptadır. Her grup için o gruptaki en üstteki düğüm kaydedilir.

Algoritma bir $x$ düğümünü ziyaret ettiğinde, LCA'sı $x$ ile birlikte sorgulanacak tüm $y$ düğümleri incelenir. Eğer $y$ önceden ziyaret edildiyse, $x$ ve $y$'nin LCA'sı $y$'nin grubundaki en üst düğümdür. $x$ düğümü tamamen işlendikten sonra $x$ ile ebeveyninin grupları birleştirilir.

Örneğin $(5, 8)$ ve $(2, 7)$ çiftlerinin LCA'larını bulmak istediğimiz bir ağaçta:

- Algoritma 8. düğümü ziyaret ettiğinde 5. düğümün önceden ziyaret edildiğini görür; 5'in grubundaki en üst düğüm 2'dir. Dolayısıyla $\text{lca}(5, 8) = 2$.
- Algoritma 7. düğümü ziyaret ettiğinde 2. düğümün önceden ziyaret edildiğini görür; 2'nin grubundaki en üst düğüm 1'dir. Dolayısıyla $\text{lca}(2, 7) = 1$.

Algoritmanın zaman karmaşıklığı, union-find işlemleriyle birlikte pratikte neredeyse lineer olan $O(n \alpha(n))$'dir.
