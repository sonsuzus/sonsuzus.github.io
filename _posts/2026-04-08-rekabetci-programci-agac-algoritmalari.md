---
layout: post
title: Rekabetçi Programcı Ağaç Algoritmaları
math: true
categories:
  - Program
tags:
  - çizge
  - graph
  - ağaç
  - tree
  - dfs
  - dinamik-programlama
  - çap
  - ikili-ağaç
  - c
  - programlama
  - algoritma
  - olimpiyat
  - yarışma
  - kodlama
  - matematik
  - kitap
---

Bir **ağaç** (tree), $n$ düğüm ve $n - 1$ kenardan oluşan bağlı ve asiklik (döngüsüz) bir çizgedir. Ağaçtan herhangi bir kenarı çıkarmak onu iki parçaya böler; herhangi bir kenar eklemek ise bir döngü oluşturur. Her iki düğüm arasında tam olarak bir yol bulunur.

Örneğin 8 düğüm ve 7 kenardan oluşan bir ağaçta **yapraklar** (leaves), derecesi 1 olan yani tek komşusu bulunan düğümlerdir. **Köklü bir ağaçta** düğümlerden biri kök seçilir ve diğer tüm düğümler onun altına yerleştirilir. Köklü ağaçta bir düğümün **çocukları** (children) onun alt komşuları, **ebeveyni** (parent) ise üst komşusudur. Her düğümün kök hariç tam bir ebeveyni vardır.

Köklü ağacın yapısı **özyinelemelidir**: her düğüm, kendisini ve tüm torunlarını kapsayan bir alt ağacın kökü gibi davranır.

## 14.1 Ağaç Dolaşımı

Genel çizge dolaşım algoritmaları ağaçlarda da kullanılabilir. Ancak ağaçlar döngü içermediğinden ve bir düğüme birden fazla yoldan ulaşılamadığından implementasyon genel çizgelere kıyasla çok daha sadedir.

Ağacı dolaşmanın klasik yolu herhangi bir düğümden DFS başlatmaktır:

```cpp
void dfs(int s, int e) {
    // s düğümü ile bir şeyler yap
    for (auto u : adj[s]) {
        if (u != e) dfs(u, s);
    }
}
```

Fonksiyon iki parametre alır: mevcut düğüm `s` ve onun ebeveyni `e`. Ebeveyn parametresi, aramanın geri dönüp sonsuz döngüye girmesini önler. Arama `x` düğümünden şöyle başlatılır:

```cpp
dfs(x, 0);
```

İlk çağrıda `e = 0` verilir çünkü kökün ebeveyni yoktur.

### Dinamik Programlama ile Alt Ağaç Hesapları

Ağaç dolaşımı sırasında dinamik programlama kullanarak her düğüm için yararlı bilgiler $O(n)$ zamanda hesaplanabilir; örneğin alt ağacındaki düğüm sayısı ya da bir düğümden yaprağa olan en uzun mesafe.

Her `s` düğümü için alt ağacındaki toplam düğüm sayısını veren `count[s]` değeri şöyle hesaplanır:

```cpp
void dfs(int s, int e) {
    count[s] = 1;
    for (auto u : adj[s]) {
        if (u == e) continue;
        dfs(u, s);
        count[s] += count[u];
    }
}
```

Alt ağaç, düğümün kendisini ve tüm çocuklarının alt ağaçlarını içerir; dolayısıyla `count[s]`, çocukların `count` değerlerinin toplamına 1 eklenerek bulunur.

## 14.2 Çap

Bir ağacın **çapı** (diameter), ağaçtaki herhangi iki düğüm arasındaki en uzun mesafedir. Aynı uzunlukta birden fazla en uzun yol bulunabilir.

Çapı bulmak için $O(n)$ zamanda çalışan iki farklı algoritma vardır.

### 1. Algoritma: Dinamik Programlama

Ağacı köklendirip her alt ağaç için çapı ayrı ayrı hesaplayan bir yaklaşımdır. Köklü ağaçtaki her yolun bir **en yüksek noktası** (tepesi) vardır; yani yolda geçilen en üstteki düğüm. Bu gözlemden yola çıkarak her düğüm için iki değer hesaplanır:

- $\text{toLeaf}(x)$: $x$ düğümünden herhangi bir yaprağa olan en uzun mesafe.
- $\text{maxLength}(x)$: tepe noktası $x$ olan en uzun yolun uzunluğu.

Örneğin 1. düğümün kök olduğu bir ağaçta $\text{toLeaf}(1) = 2$ ise ($1 \to 2 \to 6$ yoluyla) ve $\text{maxLength}(1) = 4$ ise ($6 \to 2 \to 1 \to 4 \to 7$ yoluyla) ağacın çapı $\text{maxLength}(\text{kök})$'e eşittir.

Hesaplama adımları:

- $\text{toLeaf}(x)$: $x$'in çocukları arasında $\text{toLeaf}(c)$ değeri en büyük olan $c$ seçilir ve $\text{toLeaf}(x) = \text{toLeaf}(c) + 1$ olur.
- $\text{maxLength}(x)$: En büyük $\text{toLeaf}$ değerine sahip iki farklı $a, b$ çocuğu seçilir; $\text{maxLength}(x) = \text{toLeaf}(a) + \text{toLeaf}(b) + 2$ olur.

### 2. Algoritma: İki DFS

Çapı bulmanın daha şık bir yolu iki DFS çalıştırmaktır:

1. Ağaçta rastgele bir $a$ düğümü seç.
2. $a$'dan en uzaktaki $b$ düğümünü bul (BFS veya DFS ile).
3. $b$'den en uzaktaki $c$ düğümünü bul.
4. $b$ ile $c$ arasındaki mesafe ağacın çapıdır.

Bu yöntemin neden doğru çalıştığını anlamak için ağacı çap yatay olacak şekilde düşünmek yeterlidir. Rastgele seçilen $a$ düğümü çapın dışında olsa bile, $a$'dan en uzak düğüm olan $b$ her zaman çap yolunun bir ucu olur. Çünkü $b$, çap uçlarından en az $a$'nın çapla kesişim noktasına olan mesafesi kadar uzakta olmak zorundadır ve bu da onu daima çapın bir ucuna karşılık getirir.

## 14.3 Bütün En Uzun Yollar

Her düğüm için o düğümden başlayan en uzun yolun uzunluğunu $\text{maxLength}(x)$ olarak hesaplamak istiyoruz. Bu, çap probleminin genelleştirilmiş halidir; sonuçların en büyüğü ağacın çapına eşit olur.

Örneğin aşağıdaki tablo 6 düğümlü bir ağaç için sonuçları gösterir:

| Düğüm $x$ | 1 | 2 | 3 | 4 | 5 | 6 |
|:---------:|:-:|:-:|:-:|:-:|:-:|:-:|
| $\text{maxLength}(x)$ | 2 | 2 | 3 | 3 | 3 | 3 |

Problem $O(n)$ zamanda iki aşamada çözülür.

**Aşama 1:** Her $x$ düğümü için çocuklarından geçen en uzun yol dinamik programlamayla hesaplanır (Bölüm 14.2'deki yaklaşımla aynıdır).

**Aşama 2:** Her $x$ düğümü için ebeveyninden $p$'den geçen en uzun yol bulunur. Burada dikkat edilmesi gereken bir incelik vardır: $p$'den geçen en uzun yol bazen $x$ üzerinden geçebilir. Bu durumda $x$'e ait olmayan yönde bir çözüm gerekir.

Bu sorunu çözmek için her $x$ düğümüne ait **iki** maksimum değer saklanır:

- $\text{maxLength}_1(x)$: $x$ düğümünden geçen en uzun yolun uzunluğu.
- $\text{maxLength}_2(x)$: $x$ düğümünden farklı bir yönde geçen ikinci en uzun yolun uzunluğu.

Son adımda: eğer $p$'nin $\text{maxLength}_1$ değerini sağlayan yol $x$ üzerinden geçiyorsa cevap $\text{maxLength}_2(p) + 1$, geçmiyorsa $\text{maxLength}_1(p) + 1$ olur.

## 14.4 İkili Ağaç

**İkili ağaç** (binary tree), her düğümün **sol** ve **sağ** olmak üzere en fazla iki çocuğu bulunan köklü bir ağaçtır. Bir çocuk olmayabilir; dolayısıyla her düğümün 0, 1 veya 2 çocuğu olabilir.

### Dolaşım Sıraları

İkili ağacın düğümleri dolaşım biçimine göre üç farklı sırayla listelenebilir:

- **Önce kök (pre-order):** Kök → Sol alt ağaç → Sağ alt ağaç
- **Kök ortada (in-order):** Sol alt ağaç → Kök → Sağ alt ağaç
- **Kök sonda (post-order):** Sol alt ağaç → Sağ alt ağaç → Kök

Örneğin aşağıdaki ikili ağaç için:

```
      1
     / \
    2   3
   / \   \
  4   5   7
     /
    6
```

| Dolaşım | Sıra |
|:-------:|:----:|
| Önce kök | $[1, 2, 4, 5, 6, 3, 7]$ |
| Kök ortada | $[4, 2, 6, 5, 1, 3, 7]$ |
| Kök sonda | $[4, 6, 5, 2, 7, 3, 1]$ |

### Ağacı Yeniden Oluşturmak

İki dolaşım sırasından ağacın tam yapısını çıkarmak mümkündür; ancak hangi iki sıranın yeterli olduğu önemlidir:

- **Önce kök + Kök ortada** → Ağaç yapısı **benzersiz** biçimde belirlenir.
- **Kök sonda + Kök ortada** → Ağaç yapısı **benzersiz** biçimde belirlenir.
- **Önce kök + Kök sonda** → Ağaç yapısı **benzersiz belirlenemez**; birden fazla ağaç bu iki sırayla uyuşabilir.

Örneğin önce kök sırası $[1, 2]$ ve kök sonda sırası $[2, 1]$ olan iki farklı ağaç yapısı mevcuttur: birinde 2, kökün sol çocuğu; diğerinde ise sağ çocuğudur.
