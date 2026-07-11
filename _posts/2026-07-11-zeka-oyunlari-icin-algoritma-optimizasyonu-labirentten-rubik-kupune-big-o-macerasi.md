---
layout: post
title: "Zekâ Oyunları İçin Algoritma Optimizasyonu: Labirentten Rubik Küpüne Big O Macerası"
math: true
categories: 
  - Bilgi
tags: 
  - algoritma
  - big-o
  - yapay-zeka
  - optimizasyon
---

Zekâ oyunları, bilgisayara sadece çözüm buldurduğumuz oyuncaklar değil; algoritmaların kas geliştirdiği küçük spor salonlarıdır. Bir labirent çözücü ya da Rubik Küp algoritması yazarken asıl soru şudur: Çözümü bulabilir miyiz? Evet. Peki çözümü makul sürede ve belleği yakmadan bulabilir miyiz? İşte eğlence burada başlar.
``
Bir problemde olası durum sayısı büyüdükçe kaba kuvvet yaklaşımı hızla kontrolden çıkar. Labirentte her kavşakta ortalama $b$ seçenek varsa ve çözüm derinliği $d$ ise, saf arama için yaklaşık karmaşıklık $O(b^d)$ olur. Rubik Küp tarafında durum uzayı yaklaşık $4.3 \times 10^{19}$ olduğu için her hamleyi denemek, evrendeki çay molalarını tüketebilir.

Temel fikir, arama ağacını küçültmektir. Bunun için üç ana silahımız var: daha iyi veri yapısı, daha iyi sezgisel fonksiyon ve tekrarları engelleyen bellek yönetimi.

| Yöntem | Zaman Karmaşıklığı | Uzay Karmaşıklığı | Ne Zaman Güzel? |
|---|---:|---:|---|
| DFS | $O(b^d)$ | $O(d)$ | Bellek azsa, çözüm derinliği belirsizse |
| BFS | $O(b^d)$ | $O(b^d)$ | En kısa yol kesin lazımsa |
| A* | $O(b^d)$, pratikte daha iyi | $O(b^d)$ | İyi sezgisel varsa |
| IDA* | $O(b^d)$ | $O(d)$ | Rubik gibi dev durum uzaylarında |

Labirent için A* genellikle yıldız oyuncudur. Çünkü hedefe olan Manhattan mesafesi gibi basit bir sezgisel, algoritmanın boş koridorlarda kaybolmasını engeller. A* şu puanı kullanır: $f(n)=g(n)+h(n)$. Burada $g(n)$ başlangıçtan gelinen maliyet, $h(n)$ ise hedefe tahmini uzaklıktır. Eğer $h(n)$ asla gerçek maliyeti aşmıyorsa, yani kabul edilebilir ise, A* en kısa yolu bulur.

```python
from heapq import heappush, heappop

def astar(start, goal, neighbors, heuristic):
    pq = []
    heappush(pq, (0, start))
    cost = {start: 0}
    parent = {start: None}

    while pq:
        _, node = heappop(pq)
        if node == goal:
            return parent

        for nxt, step_cost in neighbors(node):
            new_cost = cost[node] + step_cost
            if nxt not in cost or new_cost < cost[nxt]:
                cost[nxt] = new_cost
                priority = new_cost + heuristic(nxt, goal)
                heappush(pq, (priority, nxt))
                parent[nxt] = node
    return None
```

Bu kodda öncelik kuyruğu, en umut verici düğümü öne alır. Böylece algoritma her yeri eşit merakla gezmez; hedefe doğru kibarca burnunu uzatır. Labirentte `neighbors` fonksiyonu geçilebilir hücreleri döndürür, `heuristic` ise örneğin $|x_1-x_2|+|y_1-y_2|$ hesaplar.

Rubik Küp tarafında mesele daha serttir. Her durumda 18 temel hamle düşünürsek dallanma faktörü yüksektir. Burada IDA* öne çıkar: A* mantığını derinlik sınırıyla birleştirir, ancak devasa öncelik kuyruğu tutmaz. Özellikle desen veritabanları, yani pattern database, sezgisel değeri önceden hesaplayarak büyük hız kazandırır. Bunun bedeli bellektir; klasik takas: zaman mı, RAM mi?

| Dil | Güçlü Yanı | Zayıf Yanı | Uygun Kullanım |
|---|---|---|---|
| Python | Hızlı prototipleme | Yorumlayıcı maliyeti | Heuristik deneme, eğitim |
| C++ | Çok hızlı, bellek kontrolü | Geliştirmesi daha zahmetli | Yarışma, üretim çözücü |
| Rust | Güvenli bellek, yüksek hız | Öğrenme eğrisi | Güvenilir performans kodu |
| JavaScript | Görselleştirme kolay | CPU yoğun işte sınırlı | Web tabanlı labirent demo |

Optimizasyonda dil seçimi kadar temsil biçimi de önemlidir. Labirenti karakter matrisi yerine bitset ile saklamak belleği azaltır. Rubik Küp için yüz renklerini uzun dizilerde tutmak yerine permütasyon ve yönelim dizileri kullanmak hem hızlı karşılaştırma hem de daha küçük hash üretir. Ziyaret edilen durumları `set` içinde tutmak tekrarları keser; fakat uzay karmaşıklığını artırır. Bu yüzden IDA* gibi yöntemler bazen bilinçli olarak daha az hatırlar, daha çok tekrar hesaplar.

Pratik reçete şöyle: Önce doğru algoritmayı seç, sonra sezgisel fonksiyonu iyileştir, ardından profil çıkar. Çünkü tahminle optimizasyon yapmak, gözleri kapalı labirent çözmeye benzer. Labirentte A*, Rubik Küpünde IDA* ve desen veritabanları çoğu zaman iyi başlangıçtır. Big O bize haritanın ölçeğini verir; gerçek performansı ise veri yapıları, önbellek davranışı ve dilin çalışma modeli belirler. Kısacası hızlı çözücü yazmak, sadece kodlamak değil, arama uzayını ikna sanatıdır.
