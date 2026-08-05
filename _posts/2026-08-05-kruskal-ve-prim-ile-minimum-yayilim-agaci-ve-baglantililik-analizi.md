---
layout: post
title: "Kruskal ve Prim ile Minimum Yayılım Ağacı ve Bağlantılılık Analizi"
math: true
categories: 
  - Bilgi
tags: 
  - graf teorisi
  - Kruskal algoritması
  - Prim algoritması
---

Şehirleri en düşük maliyetle birbirine bağlayan yolları, bilgisayarları buluşturan kabloları veya enerji hatlarını tasarladığımızı düşünelim. Gereksiz döngüler oluşturmadan bütün noktaları birbirine ulaştırmak istiyorsak karşımıza **minimum yayılım ağacı** problemi çıkar. Bu problemin iki meşhur kahramanı Kruskal ve Prim algoritmalarıdır; ancak işe başlamadan önce grafın gerçekten bağlantılı olup olmadığını da sorgulamamız gerekir.

``

## Minimum yayılım ağacı nedir?

Ağırlıklı ve yönsüz bir grafı $G=(V,E)$ biçiminde gösterelim. Burada $V$ düğümleri, $E$ kenarları temsil eder. Bir **yayılım ağacı**, grafın bütün düğümlerini kapsayan, bağlantılı ve döngüsüz alt graftır. $|V|=n$ olan her yayılım ağacında tam olarak $n-1$ kenar bulunur.

Minimum yayılım ağacı (MST), kenar ağırlıkları toplamı en küçük olan yayılım ağacıdır:

$$T^* = \operatorname{argmin}_{T} \sum_{e \in T} w(e)$$

Graf bağlantılı değilse bütün düğümleri kapsayan tek bir ağaç kurulamaz. Bu durumda algoritmalar bir **minimum yayılım ormanı** üretir. Dolayısıyla bağlantılılık, yalnızca teorik bir ayrıntı değil, sonucun anlamını belirleyen temel kontroldür.

## Kruskal: En ucuz kenardan başla

Kruskal algoritması bütün kenarları ağırlıklarına göre sıralar. Ardından en ucuzdan başlayarak, döngü oluşturmayan kenarları seçer. Döngü kontrolü için çoğunlukla **Disjoint Set Union (DSU)** kullanılır. DSU, düğümlerin aynı bağlantılı bileşende bulunup bulunmadığını hızlıca söyler.

```python
def kruskal(vertices, edges):
    parent = {v: v for v in vertices}

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        parent[rb] = ra
        return True

    tree = []
    for weight, u, v in sorted(edges):
        if union(u, v):
            tree.append((u, v, weight))
    return tree
```

Burada `union` işleminin başarısız olması, iki ucun zaten bağlı olduğunu ve kenarın döngü yaratacağını gösterir. Sonuçta `len(tree) == len(vertices) - 1` ise graf bağlantılıdır. Daha az kenar seçilmişse sonuç tek ağaç değil, ormandır.

## Prim: Ağacı adım adım büyüt

Prim algoritması rastgele bir başlangıç düğümü seçer ve mevcut ağacı, dışarıdaki bir düğüme bağlayan en ucuz kenarla genişletir. En uygun kenarı hızlı seçmek için öncelik kuyruğu kullanılır.

```python
import heapq

def prim(graph, start):
    visited = set()
    heap = [(0, start, None)]
    tree = []

    while heap:
        weight, node, previous = heapq.heappop(heap)
        if node in visited:
            continue
        visited.add(node)
        if previous is not None:
            tree.append((previous, node, weight))

        for neighbor, cost in graph[node]:
            if neighbor not in visited:
                heapq.heappush(heap, (cost, neighbor, node))

    return tree, visited
```

Prim tamamlandığında `visited` kümesinin boyutu $|V|$ değerine eşitse graf bağlantılıdır. Eşit değilse algoritma yalnızca başlangıç düğümünün bulunduğu bileşeni dolaşmıştır. Tüm bileşenleri bulmak için ziyaret edilmemiş her düğümden Prim, DFS veya BFS yeniden başlatılabilir.

## Kruskal mı, Prim mi?

| Özellik | Kruskal | Prim |
|---|---|---|
| Temel yaklaşım | Kenarları küresel olarak seçer | Tek ağacı büyütür |
| Ana veri yapısı | DSU | Öncelik kuyruğu |
| Seyrek graflar | Genellikle çok uygundur | Uygundur |
| Yoğun graflar | Sıralama maliyetli olabilir | Çoğunlukla avantajlıdır |
| Bağlantısız graf | Doğrudan orman üretir | Yalnızca bir bileşeni kapsar |
| Karmaşıklık | $O(E \log E)$ | $O(E \log V)$ |

Her iki algoritma da açgözlüdür; yani her adımda o an için en iyi görünen seçimi yapar. Doğrulukları **kesim özelliğine** dayanır: Bir kesiti geçen en hafif kenar, uygun koşullarda bir minimum yayılım ağacına güvenle eklenebilir.

Sonuç olarak Kruskal, bağlantılı bileşenleri doğal biçimde gözlemlemek ve seyrek graflarla çalışmak için güçlüdür. Prim ise belirli bir düğümden başlayarak yoğun bir ağı büyütmekte pratiktir. Fakat hangi kahramanı seçerseniz seçin, önce bağlantılılığı kontrol etmek algoritmik emniyet kemerinizi takmak gibidir.
