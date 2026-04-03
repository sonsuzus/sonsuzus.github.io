---
layout: post
title: Rekabetçi Programcı Çizgenin Temelleri
math: true
categories:
  - Program
tags:
  - çizge
  - graph
  - c
  - programlama
  - algoritma
  - olimpiyat
  - yarışma
  - veri-yapisi
  - komşuluk-listesi
  - komşuluk-matrisi
  - kenar-listesi
  - kodlama
  - matematik
  - kitap
---

Çoğu kodlama sorusu bir çizge problemi olarak modellenip uygun bir çizge algoritmasıyla çözülebilir. Tipik bir örnek, bir ülkedeki yolları ve şehirleri temsil eden ağdır. Bazen çizge sorunun içinde gizli olduğundan fark edilmesi güçleşir. Bu bölümde çizgelerle ilgili temel kavramları ele alıp algoritmalarda çizgeleri göstermenin farklı yollarını inceleyeceğiz.

## 11.1 Çizge Terminolojisi

Bir **çizge** (graph), **düğümlerden** (nodes) ve **kenarlardan** (edges) oluşur. Bu yazıda $n$ çizgedeki toplam düğüm sayısını, $m$ ise toplam kenar sayısını belirtecektir. Düğümler $1, 2, \ldots, n$ tamsayılarıyla numaralandırılır.

### Yol ve Döngü

**Yol** (path), $a$ düğümünden $b$ düğümüne kenarlar kullanılarak ulaşılmasını sağlar. Yolun uzunluğu, yolda geçilen kenar sayısına eşittir. Örneğin $1 \to 3 \to 4 \to 5$ yolu, 1. düğümden 5. düğüme 3 uzunluğunda bir yoldur.

Başlangıç ve son düğümün aynı olduğu yola **döngü** (cycle) denir. Bir yolda her düğüm en fazla bir kez geçiyorsa bu yol **basittir** (simple).

### Bağlılık

Her iki düğümü arasında bir yol bulunan çizge **bağlıdır** (connected). Bir çizgenin bağlı alt gruplarına **parça** (component) denir. Örneğin $\{1,2,3\}$, $\{4,5,6,7\}$ ve $\{8\}$ olmak üzere üç parçalı bir çizge bağlı değildir.

Bir çizge bağlıysa ve $n$ düğüm ile $n-1$ kenardan oluşuyorsa bu çizge bir **ağaçtır** (tree). Ağaçta her iki düğüm arasında tam olarak bir yol vardır.

### Kenar Yönleri

Kenarların tek yönlü olduğu çizge **yönlüdür** (directed). Yönlü bir çizgede $3 \to 1 \to 2 \to 5$ yolu olabilirken $5$'ten $3$'e giden herhangi bir yol olmayabilir.

### Kenar Ağırlıkları

**Ağırlıklı** (weighted) bir çizgede her kenarın bir ağırlığı vardır; bu ağırlık genellikle uzunluk olarak yorumlanır. Ağırlıklı bir çizgedeki yolun uzunluğu, yoldaki kenarların ağırlıklarının toplamıdır. Örneğin $1 \to 2 \to 5$ yolunun uzunluğu 12, $1 \to 3 \to 4 \to 5$ yolunun uzunluğu 11 olabilir; burada ikinci yol daha kısadır.

### Komşular ve Dereceler

İki düğüm arasında kenar varsa bunlar **komşu** (neighbor) düğümlerdir. Bir düğümün **derecesi** (degree), komşu sayısına eşittir.

$m$ kenarlı bir çizgenin toplam derece sayısı her zaman $2m$'dir; çünkü her kenar iki düğümün derecesini birer artırır. Bu nedenle derece toplamı daima çifttir.

Yönlü çizgelerde bir düğümün **iç derecesi** (indegree) o düğüme gelen kenar sayısını, **dış derecesi** (outdegree) ise o düğümden çıkan kenar sayısını verir.

Her düğümün derecesi $d$ ise çizge **sıradan** (regular), her düğüm birbirine bağlıysa (derece $n-1$) çizge **tam** (complete) olarak adlandırılır.

### Boyamalar

Çizgeyi boyarken komşu düğümlerin farklı renk almasına dikkat edilir. Yalnızca iki renkle boyanabilen çizge **iki parçalıdır** (bipartite). Bir çizgenin iki parçalı olabilmesi için tek sayıda kenarlı herhangi bir döngü içermemesi gerekir.

Örneğin altı düğümlü bir çizge iki parçalıysa düğümler iki gruba ayrılıp her kenar gruplar arasında geçer; iki renkle boyanabilir. Ama tek sayıda kenarlı bir döngü içeriyorsa boyama mümkün olmaz.

Genel durumda bir çizgenin $k$ renkle boyanıp boyanamayacağını bulmak zordur. $k = 3$ için dahi bilinen verimli bir algoritma yoktur — bu problem **NP-hard**'dır.

### Basitlik

Aynı düğümde başlayıp biten kenar (öz-döngü) veya iki düğüm arasında birden fazla kenar içeren çizge **basit değildir** (not simple). Genellikle çizgelerin basit olduğu kabul edilir.

## 11.2 Çizge Gösterimi

Algoritmalarda çizgeleri göstermenin birkaç yaygın yolu vardır. Veri yapısının seçimi çizgenin büyüklüğüne ve algoritmanın çizgeyi işleme biçimine göre değişir.

### Komşuluk Listesi Gösterimi

**Komşuluk listesi** (adjacency list) gösteriminde her $x$ düğümüne bir liste atanır; bu liste $x$'ten çıkan kenarların ulaştığı düğümleri içerir. Komşuluk listeleri çizgeleri göstermenin en popüler yoludur ve çoğu algoritma bu yöntemle verimli biçimde kodlanabilir.

Komşuluk listesini oluşturmanın pratik yolu vektörlerden oluşan bir dizi kullanmaktır:

```cpp
vector<int> adj[N];
```

Örneğin aşağıdaki çizge için:

```cpp
adj[1].push_back(2);
adj[2].push_back(3);
adj[2].push_back(4);
adj[3].push_back(4);
adj[4].push_back(1);
```

Yönsüz (undirected) çizgelerde her kenar her iki yöne de eklenir. Ağırlıklı bir çizge için yapı şöyle güncellenir:

```cpp
vector<pair<int,int>> adj[N];
```

Bu durumda $a$ düğümünden $b$ düğümüne $w$ ağırlığında kenar varsa $a$'nın listesi $(b, w)$ çiftini içerir:

```cpp
adj[1].push_back({2, 5});
adj[2].push_back({3, 7});
adj[2].push_back({4, 6});
adj[3].push_back({4, 5});
adj[4].push_back({1, 2});
```

Komşuluk listesinin en büyük avantajı, bir düğümden ulaşılabilecek düğümlerin hızlıca dolaşılabilmesidir:

```cpp
for (auto u : adj[s]) {
    // u düğümünü işle
}
```

### Komşuluk Matrisi Gösterimi

**Komşuluk matrisi** (adjacency matrix) gösterimi, çizgedeki kenarları iki boyutlu bir dizide tutar ve iki düğüm arasında kenar olup olmadığını $O(1)$ zamanda sorgular:

```cpp
int adj[N][N];
```

`adj[a][b] = 1` ise $a$'dan $b$'ye kenar vardır, `adj[a][b] = 0` ise yoktur. Ağırlıklı çizgelerde kenar ağırlığı da bu matriste tutulabilir.

Dezavantajı, $n^2$ elemanlık bir dizi gerektirmesidir. Büyük çizgeler için bellek açısından pratik değildir; özellikle matrisin büyük bölümü sıfırdan oluştuğunda (seyrek çizgeler).

### Kenar Listesi Gösterimi

**Kenar listesi** (edge list) gösterimi, çizgenin tüm kenarlarını rastgele bir sırada bir vektörde tutar. Algoritma tüm kenarları işliyorsa ve belirli bir düğümden başlayan kenarları bulmaya gerek yoksa bu gösterim uygundur.

```cpp
vector<pair<int,int>> edges;
```

Her $(a, b)$ çifti, $a$ düğümünden $b$ düğümüne bir kenar olduğunu gösterir:

```cpp
edges.push_back({1, 2});
edges.push_back({2, 3});
edges.push_back({2, 4});
edges.push_back({3, 4});
edges.push_back({4, 1});
```

Ağırlıklı çizgeler için yapı üçlü demet olarak genişletilir:

```cpp
vector<tuple<int,int,int>> edges;
```

Her $(a, b, w)$ demeti, $a$'dan $b$'ye $w$ ağırlığında kenar olduğunu belirtir[^1]:

```cpp
edges.push_back({1, 2, 5});
edges.push_back({2, 3, 7});
edges.push_back({2, 4, 6});
edges.push_back({3, 4, 5});
edges.push_back({4, 1, 2});
```

### Gösterimler Arasında Karşılaştırma

| Gösterim | Bellek | Kenar var mı? | Düğümün komşuları |
|---|---|---|---|
| Komşuluk listesi | $O(n + m)$ | $O(\text{derece})$ | $O(\text{derece})$ |
| Komşuluk matrisi | $O(n^2)$ | $O(1)$ | $O(n)$ |
| Kenar listesi | $O(m)$ | $O(m)$ | $O(m)$ |

Seyrek çizgelerde ($m \ll n^2$) komşuluk listesi tercih edilir. Yoğun çizgelerde ($m \approx n^2$) komşuluk matrisi pratik olabilir. Bellman-Ford gibi tüm kenarları tek tek işleyen algoritmalar için kenar listesi doğal bir seçimdir.

[^1]: Bazı eski derleyicilerde süslü parantez yerine `make_tuple` fonksiyonu kullanılmalıdır. Örneğin `{1, 2, 5}` yerine `make_tuple(1, 2, 5)` yazılır.
