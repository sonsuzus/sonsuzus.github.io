---
layout: post
title: "En Kısa Yol Arenası: Dijkstra, Bellman-Ford ve Floyd-Warshall"
math: true
categories: 
  - Bilgi
tags: 
  - graf algoritmaları
  - en kısa yol
  - Python
---

Bir şehir haritasında en yakın kafeyi aramak, ağ paketlerini yönlendirmek veya bir oyundaki karaktere güvenli rota çizmek aynı temel soruya dayanır: Bir noktadan diğerine en düşük maliyetle nasıl gideriz? Dijkstra, Bellman-Ford ve Floyd-Warshall bu soruya farklı koşullarda cevap veren üç klasik algoritmadır. Ancak yanlış algoritmayı seçmek, navigasyon uygulamasını macera oyununa çevirebilir!

``

## Problemin matematiksel modeli

Bir ağırlıklı grafı $G=(V,E)$ biçiminde tanımlayalım. Burada $V$ düğümleri, $E$ kenarları ve $w(u,v)$ ise $u$ ile $v$ arasındaki geçiş maliyetini gösterir. Bir $P$ yolunun toplam maliyeti:

$$W(P)=\sum_{(u,v)\in P} w(u,v)$$

şeklindedir. Amaç, kaynak $s$ ile hedef $t$ arasındaki yollar içinde maliyeti en küçük olanı bulmaktır:

$$d(s,t)=\min_{P:s\leadsto t} W(P)$$

Kenar ağırlıkları mesafe, süre, ücret veya enerji tüketimi olabilir. Kritik ayrım, negatif ağırlıkların bulunup bulunmamasıdır. Örneğin bir finans modelinde kazanç, negatif maliyet olarak temsil edilebilir.

## Üç algoritma, üç farklı yaklaşım

| Özellik | Dijkstra | Bellman-Ford | Floyd-Warshall |
|---|---|---|---|
| Hesaplanan yollar | Tek kaynaktan tüm düğümlere | Tek kaynaktan tüm düğümlere | Her düğüm çifti arasında |
| Negatif kenar | Desteklemez | Destekler | Destekler |
| Negatif döngü tespiti | Hayır | Evet | Evet |
| Zaman karmaşıklığı | $O((V+E)\log V)$ | $O(VE)$ | $O(V^3)$ |
| İdeal kullanım | Büyük ve seyrek graflar | Negatif maliyetli graflar | Küçük veya yoğun graflar |

### Dijkstra: Hızlı ama seçici

Dijkstra, başlangıç düğümünden erişilebilen en düşük geçici mesafeye sahip düğümü sürekli seçer. Açgözlü çalışır: Kesinleştirilen bir mesafeye tekrar dönmez. Bu karar yalnızca tüm ağırlıklar $w(u,v)\geq 0$ olduğunda güvenlidir.

```python
import heapq

def dijkstra(graph, source):
    dist = {node: float('inf') for node in graph}
    dist[source] = 0
    queue = [(0, source)]

    while queue:
        current, node = heapq.heappop(queue)
        if current != dist[node]:
            continue
        for neighbor, weight in graph[node]:
            candidate = current + weight
            if candidate < dist[neighbor]:
                dist[neighbor] = candidate
                heapq.heappush(queue, (candidate, neighbor))
    return dist
```

Öncelik kuyruğu, sıradaki en yakın düğümü verimli biçimde seçer. Yol ağları ve internet yönlendirme senaryoları için genellikle en pratik tercihtir.

### Bellman-Ford: Yavaş ama kuşkucu

Bellman-Ford bütün kenarları en fazla $|V|-1$ tur gevşetir. Gevşetme işlemi şu eşitsizliği kontrol eder:

$$d(v)>d(u)+w(u,v)$$

Koşul doğruysa $d(v)$ güncellenir. Bir tur daha yapıldığında hâlâ güncelleme gerçekleşiyorsa erişilebilir bir negatif döngü vardır.

```python
def bellman_ford(vertices, edges, source):
    dist = {v: float('inf') for v in vertices}
    dist[source] = 0

    for _ in range(len(vertices) - 1):
        changed = False
        for u, v, weight in edges:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                changed = True
        if not changed:
            break

    for u, v, weight in edges:
        if dist[u] + weight < dist[v]:
            raise ValueError('Negatif döngü bulundu')
    return dist
```

Döviz arbitrajı ve maliyetlerin negatif olabildiği modeller, ek işlem süresine rağmen Bellman-Ford için uygundur.

### Floyd-Warshall: Herkes herkese karşı

Floyd-Warshall, dinamik programlama kullanır. $k$ ara düğümüne izin verildiğinde güncelleme kuralı şöyledir:

$$D_{ij}=\min(D_{ij},D_{ik}+D_{kj})$$

```python
def floyd_warshall(dist):
    n = len(dist)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist
```

Sonuç matrisindeki herhangi bir $D_{ii}<0$ değeri negatif döngüyü gösterir. Bellek maliyeti $O(V^2)$ olduğundan devasa graflarda pahalıdır; fakat tüm çiftlerin sorgulanacağı küçük ulaşım veya ilişki ağlarında son derece kullanışlıdır.

## Hangisini seçmeliyiz?

Negatif ağırlık yoksa ve tek kaynak önemliyse **Dijkstra**, negatif kenarlar varsa **Bellman-Ford**, bütün düğüm çiftleri gerekiyorsa **Floyd-Warshall** seçilmelidir. Özetle Dijkstra sprinter, Bellman-Ford temkinli denetçi, Floyd-Warshall ise herkesin rotasını önceden çıkaran takıntılı haritacıdır.
