---
layout: post
title: Rekabetçi Programcı Kapsayan Ağaç (Spanning Trees)
math: true
categories:
  - Program
tags:
  - çizge
  - graph
  - ağaç
  - tree
  - kapsayan-ağaç
  - spanning-tree
  - kruskal
  - prim
  - union-find
  - açgözlü
  - greedy
  - c
  - programlama
  - algoritma
  - olimpiyat
  - yarışma
  - kodlama
  - matematik
  - kitap
---

**Kapsayan ağaç** (spanning tree), bir çizgenin bütün düğümlerini bağlı olacak şekilde birleştiren, çizgenin bazı kenarlarını içeren bir ağaçtır. Ağaçlardaki gibi, kapsayan ağaçlar da bağlı ve asikliktir. Genelde, kapsayan ağaç oluşturmanın birkaç yolu vardır.

**Kapsayan ağacın ağırlığı** kenar ağırlıklarının toplamıdır. **En küçük kapsayan ağaç** (minimum spanning tree), ağırlığı en küçük olan kapsayan ağaçtır. Benzer şekilde **en büyük kapsayan ağaç**, en büyük ağırlığa sahip kapsayan ağaçtır.

Bir çizgenin birkaç tane en küçük ve en büyük kapsayan ağacı olabilir; yani bu ağaçlardan sadece bir tane olmak zorunda değildir.

En küçük ve en büyük kapsayan ağaçları bazı açgözlü yöntemler kullanarak oluşturabiliriz. Bu bölümde kenarların ağırlıklarına göre sıralayarak yapılan iki algoritmadan bahsedeceğiz. Her ne kadar bölümde en küçük kapsayan ağaçları bulmaya odaklanacak olsak bile, en büyük kapsayan ağaç da kenarları ters sırada işleyerek bulunabilir.

## 15.1 Kruskal'ın Algoritması

Kruskal'ın Algoritması'nda başlangıçtaki kapsayan ağaçta sadece çizgenin düğümleri bulunur ve herhangi bir kenar içermemektedir. Sonrasında algoritma kenarlara ağırlıklarına göre bakar ve eğer kenar döngü oluşturmuyorsa kenarı kapsayan ağaca ekler.

Algoritma, ağacın parçalarını tutar. İlk başta çizgenin her düğümü ayrı bir parçadır. Her seferinde ağaca bir kenar eklendiği zaman iki parça birleşir. Sonunda bütün düğümler aynı parçaya ait olur ve en küçük kapsayan ağaç bulunur.

### Örnek

Algoritmanın ilk adımında kenarlar, ağırlıklarına göre küçükten büyüğe doğru sıralanır:

| Kenar | Ağırlık |
|:-----:|:-------:|
| 5–6   | 2       |
| 1–2   | 3       |
| 3–6   | 3       |
| 1–5   | 5       |
| 2–3   | 5       |
| 2–5   | 6       |
| 4–6   | 7       |
| 3–4   | 9       |

Bundan sonra algoritma listeden geçer ve kenar iki ayrı parçayı bağlıyorsa kenarı ağaca ekler. Başta her düğüm kendisine ait parçadadır. Ağaca ilk eklenen kenar **5–6** kenarıdır; bu kenar $\{5\}$ ve $\{6\}$ parçalarını $\{5, 6\}$ şeklinde birleştirir. Ardından **1–2**, **3–6** ve **1–5** kenarları benzer şekilde eklenir.

Bu adımlardan sonra ağaçta iki parça kalmıştır: $\{1, 2, 3, 5, 6\}$ ve $\{4\}$. Listedeki sonraki kenar **2–3**'tür, ancak 2 ve 3 düğümleri aynı parçaya ait olduğundan bu kenar ağaca eklenmez. Aynı nedenden dolayı **2–5** kenarı da eklenmez. En sonunda **4–6** kenarı ağaca eklenir ve algoritma tamamlanır. Oluşan en küçük kapsayan ağacın ağırlığı $2 + 3 + 3 + 5 + 7 = 20$ olur.

### Bu Neden Çalışır?

Çizgedeki minimum ağırlıklı kenarı eklemediğimizi varsayalım. Bu durumda mevcut kapsayan ağaçtan bir kenarı çıkartıp yerine minimum ağırlıklı kenarı eklediğimizde daha küçük ağırlığa sahip bir kapsayan ağaç elde ederiz. Bu çelişki, en küçük ağırlığa sahip kenarı eklemenin her zaman optimal olduğunu gösterir. Benzer mantık sonraki kenarlar için de geçerlidir; dolayısıyla Kruskal'ın Algoritması her zaman doğru sonucu verir.

### İmplementasyon

Kruskal'ın Algoritması'nı koda geçirirken çizgeyi bir kenar listesinde tutmak daha rahat olur. Algoritmanın ilk aşamasında listedeki kenarlar $O(m \log m)$ zamanda sıralanır. Bundan sonra algoritma en küçük kapsayan ağacı şu şekilde oluşturur:

```cpp
for (...) {
    if (!same(a, b)) unite(a, b);
}
```

Döngü listedeki bütün kenarlardan geçer ve her seferinde $a$–$b$ kenarını işler. İki fonksiyon gereklidir:

- `same(a, b)`: $a$ ve $b$ düğümlerinin aynı parçaya ait olup olmadığını belirler.
- `unite(a, b)`: $a$ ve $b$ düğümlerini içeren parçaları birleştirir.

`same` fonksiyonunu bir çizge dolaşım algoritmasıyla $O(n + m)$ zamanda implement etmek mümkündür; ancak bu fonksiyon her kenar için çağrıldığından algoritma yavaş kalır. **Union-find yapısı** ile her iki fonksiyon da $O(\log n)$ zamanda çalışır ve Kruskal'ın Algoritması, sıralama adımından sonra $O(m \log n)$ zamanda tamamlanır.

## 15.2 Union-find Yapısı

Union-find yapısı, parçalardan oluşan bir koleksiyonu tutar. Her eleman sadece bir parçaya aittir; yani parçalar ayrıktır. İki temel $O(\log n)$ işlemi vardır:

- **unite**: İki parçayı birleştirir.
- **find**: Verilen elemanın bulunduğu parçanın temsilcisini döndürür.

### Yapı

Union-find yapısında her parçadaki bir eleman o parçanın **temsilcisi** (representative) olur ve parçadaki diğer tüm elemanlardan temsilciye bir bağ vardır. Örneğin $\{1, 4, 7\}$, $\{5\}$ ve $\{2, 3, 6, 8\}$ gibi parçalarımız olduğunu düşünelim; bu durumda temsilciler sırasıyla 4, 5 ve 2 olur.

Her elemanın temsilcisi, o elemandan başlayan bağı takip ederek bulunur. Örneğin 6. elemanın temsilcisi 2'dir çünkü $6 \to 3 \to 2$ bağı mevcuttur. İki elemanın temsilcisi aynıysa bu elemanlar aynı parçadadır.

İki parça, parçaların temsilcilerini birbirine bağlayarak birleştirilir. **Verimlilik için** her zaman küçük olan parçanın temsilcisini büyük olan parçanın temsilcisine bağlarız; eğer iki parça da aynı büyüklükteyse aralarından birini seçeriz. Bu teknikle herhangi bir bağın uzunluğu $O(\log n)$ olur.

### İmplementasyon

Union-find yapısı dizilerle implement edilir. `link` dizisi her elemanın bağdaki sonraki elemanını (eleman temsilciyse kendisini) tutar. `size` dizisi ise her temsilcinin bulunduğu parçanın büyüklüğünü verir.

Başlangıçta her eleman ayrı bir parçadadır:

```cpp
for (int i = 1; i <= n; i++) link[i] = i;
for (int i = 1; i <= n; i++) size[i] = 1;
```

`find` fonksiyonu herhangi bir $x$ elemanının temsilcisini bulur:

```cpp
int find(int x) {
    while (x != link[x]) x = link[x];
    return x;
}
```

`same` fonksiyonu $a$ ve $b$ düğümlerinin aynı parçaya ait olup olmadığını kontrol eder:

```cpp
bool same(int a, int b) {
    return find(a) == find(b);
}
```

`unite` fonksiyonu ise $a$ ve $b$ elemanlarını içeren parçaları birleştirir. Fonksiyon önce parçaların temsilcilerini bulur, ardından küçük parçayı büyük parçaya bağlar:

```cpp
void unite(int a, int b) {
    a = find(a);
    b = find(b);
    if (size[a] < size[b]) swap(a, b);
    size[a] += size[b];
    link[b] = a;
}
```

`find` fonksiyonu her bağın uzunluğunun $O(\log n)$ olduğu varsayımıyla $O(\log n)$ zamanda çalışır. `unite` fonksiyonunun küçük parçayı büyük parçaya bağlaması, bağ uzunluğunun $O(\log n)$ sınırını korumasını sağlar.

## 15.3 Prim'in Algoritması

Prim'in Algoritması, en küçük kapsayan ağacı bulmak için alternatif bir yöntemdir. Algoritma ilk başta çizgeden herhangi bir düğümü ağaca ekler. Sonra her adımda, ağaca yeni bir düğüm ekleyen en kısa kenarı seçer. En sonunda bütün düğümler ağaca eklenir ve en küçük kapsayan ağaç bulunmuş olur.

Prim'in Algoritması **Dijkstra'nın Algoritması**'nı anımsatır. Aralarındaki fark şudur: Dijkstra'nın Algoritması her zaman başlangıç düğümünden en kısa mesafede olan kenarı seçerken, Prim'in Algoritması ağaca eklenmiş herhangi bir düğümden çıkan en kısa kenarı seçer.

### Örnek

Başlangıç düğümü olarak 1. düğümü seçelim. İlk adımda 3 uzunluğundaki kenar eklenerek 2. düğüm ağaca katılır. Bundan sonra 5 uzunluğunda iki seçenek olduğunda önce 3. düğüm eklenir. İşlem, bütün düğümler ağaca eklenene kadar devam eder. Oluşan en küçük kapsayan ağacın ağırlığı yine $2 + 3 + 3 + 5 + 7 = 20$ olur.

### İmplementasyon

Dijkstra'nın Algoritması gibi Prim'in Algoritması da **öncelikli kuyruk** ile verimli biçimde yazılabilir. Öncelikli kuyruk, tek kenarla eklenebilen bütün düğümleri, kenar ağırlıklarının artan sırasına göre tutar.

Prim'in Algoritması'nın zaman karmaşıklığı $O(n + m \log m)$ olup Dijkstra'nın Algoritması'nın zaman karmaşıklığıyla aynıdır. Pratikte hem Prim'in hem de Kruskal'ın Algoritmaları verimlidir; hangisinin kullanılacağı kişiden kişiye göre değişir. Yine de çoğu olimpiyatçı Kruskal'ın Algoritması'nı tercih eder.
