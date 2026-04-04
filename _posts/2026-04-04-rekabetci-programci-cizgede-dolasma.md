---
layout: post
title: Rekabetçi Programcı Çizgede Dolaşma
math: true
categories:
  - Program
tags:
  - çizge
  - graph
  - dfs
  - bfs
  - derinlik-öncelikli-arama
  - genişlik-öncelikli-arama
  - c
  - programlama
  - algoritma
  - olimpiyat
  - yarışma
  - veri-yapisi
  - kodlama
  - kitap
---

Bu bölümde iki temel çizge dolaşma algoritması ele alınacaktır: **derinlik öncelikli arama** (DFS) ve **genişlik öncelikli arama** (BFS). Her ikisinin de bir başlangıç noktası vardır ve başlangıç düğümünden ulaşılabilen tüm düğümleri gezerler. İki algoritma arasındaki fark, düğümleri dolaşma sırasıdır.

## 12.1 Derinlik Öncelikli Arama (DFS)

**Derinlik öncelikli arama** (Depth-First Search — DFS), sezgisel bir çizge dolaşma tekniğidir. Algoritma başlangıç düğümünden hareket ederek çizgenin kenarlarını kullanır ve ulaşılabilir tüm düğümleri ziyaret eder. DFS, yeni bir düğüm buldukça tek bir yolu izlemeye devam eder; çıkmaza girdiğinde ise geri dönerek çizgenin diğer bölgelerini keşfeder. Her düğüm yalnızca bir kez ziyaret edilip işlenir.

Algoritmanın zaman karmaşıklığı $O(n + m)$'dir; burada $n$ düğüm sayısı, $m$ ise kenar sayısıdır. Bu, algoritmanın her düğümü ve kenarı tam bir kez işlemesinden kaynaklanır.

### Örnek

Aşağıdaki beş düğümlü çizgede DFS'in 1. düğümden nasıl ilerlediğini izleyelim:

```
1 — 2
|   |
4   3
 \ /
  5
```

DFS 1. düğümden başlar ve önce 2. düğüme geçer. Oradan 3, ardından 5. düğüm ziyaret edilir. 5. düğümün komşuları olan 2 ve 3 zaten ziyaret edildiği için geri dönülür. 3 ve 2. düğümlerin tüm kenarları da işlendiğinden 1. düğüme dönülür ve oradan 4. düğüme gidilir. Tüm düğümler ziyaret edildiğinde arama sona erer.

Ziyaret sırası: $1 \to 2 \to 3 \to 5 \to 4$

### İmplementasyon

DFS, özyineleme (recursion) ile kolayca kodlanabilir. `dfs` fonksiyonu belirtilen düğümden aramaya başlar. Çizge komşuluk listelerinde, ziyaret edilen düğümler ise `visited` dizisinde tutulur:

```cpp
vector<int> adj[N];
bool visited[N];

void dfs(int s) {
    if (visited[s]) return;
    visited[s] = true;
    // s düğümüyle bir şeyler yap
    for (auto u : adj[s]) {
        dfs(u);
    }
}
```

Başta `visited` dizisinin tüm elemanları `false`'tur. Arama `s` düğümüne geldiğinde `visited[s]` değeri `true` olarak işaretlenir ve o düğüm bir daha işlenmez.

## 12.2 Genişlik Öncelikli Arama (BFS)

**Genişlik öncelikli arama** (Breadth-First Search — BFS), düğümleri başlangıç düğümüne olan mesafeye göre artan sırada ziyaret eder. Bu özelliği sayesinde BFS, tüm düğümlerin başlangıç düğümüne olan **en kısa mesafelerini** hesaplamak için doğal bir araçtır. Bununla birlikte DFS'e kıyasla koda geçirilmesi biraz daha karmaşıktır.

BFS düğümleri katman katman (level by level) dolaşır: önce başlangıç düğümüne 1 uzaklıktaki düğümler, ardından 2 uzaklıktakiler ve böyle devam eder. Tüm düğümler ziyaret edilene kadar sürer. Zaman karmaşıklığı DFS ile aynıdır: $O(n + m)$.

### Örnek

Altı düğümlü çizgede BFS'in 1. düğümden nasıl ilerlediğini izleyelim:

```
1 — 2 — 3
|       |
4   5 — 6
```

İlk adımda 1'den tek bir kenarla ulaşılan 2 ve 4 ziyaret edilir. Sonra 2'nin komşusu 3 ve bağlantılı yoldan 5 ziyaret edilir. En sonda 6 ziyaret edilir.

Hesaplanan mesafeler:

| Düğüm | Mesafe |
|:-----:|:------:|
| 1 | 0 |
| 2 | 1 |
| 3 | 2 |
| 4 | 1 |
| 5 | 2 |
| 6 | 3 |

### İmplementasyon

BFS bir **kuyruk** (queue) veri yapısıyla koda dökülür. Her adımda kuyruğun başındaki düğüm işlenir; yeni keşfedilen düğümler kuyruğun sonuna eklenir. Böylece düğümler her zaman mesafe sırasına göre işlenir.

```cpp
queue<int> q;
bool visited[N];
int distance[N];

// x: başlangıç düğümü
visited[x] = true;
distance[x] = 0;
q.push(x);

while (!q.empty()) {
    int s = q.front(); q.pop();
    // s düğümüyle bir şeyler yap
    for (auto u : adj[s]) {
        if (visited[u]) continue;
        visited[u] = true;
        distance[u] = distance[s] + 1;
        q.push(u);
    }
}
```

`visited` dizisi ziyaret edilen düğümleri, `distance` dizisi ise başlangıç düğümünden her düğüme olan en kısa mesafeyi tutar.

## 12.3 Uygulamalar

Çizge dolaşma algoritmaları, çizgenin çeşitli özelliklerini tespit etmek için kullanılabilir. Genellikle DFS de BFS de işe yarar; ancak DFS özyinelemeli yapısıyla daha sade yazıldığından pratikte daha sık tercih edilir. Aşağıdaki uygulamalar çizgenin yönsüz olduğunu varsayar.

### Bağlılık Kontrolü

Bir çizge, her iki düğümü arasında yol varsa **bağlıdır**. Bağlılığı kontrol etmek için herhangi bir düğümden dolaşma başlatılır ve tüm düğümlerin ziyaret edilip edilmediğine bakılır. Ziyaret edilmemiş düğüm varsa çizge bağlı değildir.

Çizgenin tüm bağlı **parçalarını** (components) bulmak için ziyaret edilmemiş her düğümden yeni bir dolaşma başlatmak yeterlidir:

```cpp
for (int i = 1; i <= n; i++) {
    if (!visited[i]) dfs(i); // yeni bir parça başlıyor
}
```

### Döngü Bulmak

Dolaşma sırasında daha önce ziyaret edilmiş bir komşuya ulaşılırsa — bir önceki düğüm hariç — çizgede **döngü** (cycle) vardır.

Örneğin 2. düğümden 5. düğüme geçerken 5'in komşusu olan 3'ün zaten ziyaret edildiği görülürse $3 \to 2 \to 5 \to 3$ döngüsü tespit edilmiş olur.

Alternatif bir yöntem: her parçanın düğüm ve kenar sayısını karşılaştırmak. Parça $c$ düğüm içeriyorsa ve döngüsüzse tam $c - 1$ kenar içerir (yani bir ağaçtır). $c$ veya daha fazla kenar içeriyorsa o parça en az bir döngü barındırıyordur.

### İki Parçalılık Kontrolü

Komşu düğümlerin asla aynı renge sahip olmayacağı şekilde yalnızca iki renkle boyanabilen çizge **iki parçalıdır** (bipartite). Bunu çizge dolaşmayla kontrol etmek oldukça kolaydır.

Başlangıç düğümü maviye boyanır, tüm komşuları kırmızıya, ardından o komşuların komşuları tekrar maviye boyama şeklinde alternatif renkler atanır. Eğer dolaşma sırasında iki komşu düğüm aynı renge boyanmışsa çizge iki parçalı **değildir**. Böyle bir çelişki oluşmazsa çizge iki parçalıdır ve elde edilen boyama geçerli bir çözümdür.

Örneğin tek sayıda kenara sahip bir döngü içeren çizgede bu boyama mutlaka bir çelişkiyle sonuçlanır. Başlangıç düğümüne hangi rengin atandığının önemi yoktur; seçilen renk otomatik olarak diğer tüm düğümlerin rengini belirler.

Genel durumda bir çizgeyi $k$ renkle boyamak ise çok daha zordur. $k = 3$ için dahi bilinen verimli bir algoritma yoktur; bu problem **NP-hard**'dır.
