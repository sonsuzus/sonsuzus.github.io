---
layout: post
title: "Graflar ve Ağaçlarda DFS ve BFS: Derine mi, Genişe mi?"
math: true
categories: 
  - Bilgi
tags: 
  - DFS
  - BFS
  - graf algoritmaları
---

Bir labirentte çıkış aradığınızı düşünün: Bir yolu sonuna kadar takip edip çıkmazda geri mi dönersiniz, yoksa önce size bir adım uzaklıktaki bütün yolları mı incelersiniz? İlk yaklaşım **derinlik öncelikli arama (DFS)**, ikincisi ise **genişlik öncelikli arama (BFS)** mantığıdır. Bu iki kapsamlı arama tekniği; ağaçların, grafların ve birçok yapay zekâ probleminin temel araçlarıdır.
``
## Önce yapıyı tanıyalım

Bir **graf**, düğümlerden ve bu düğümleri bağlayan kenarlardan oluşur: $G=(V,E)$. Burada $V$ düğüm, $E$ ise kenar kümesidir. Ağaç da çevrim içermeyen, bağlantılı özel bir graftır. Bir ağaçta iki düğüm arasında yalnızca tek bir basit yol bulunurken genel bir grafta birden fazla yol ve çevrim olabilir.

Bu ayrım uygulamada önemlidir. Ağaç üzerinde aşağı doğru ilerlemek çoğunlukla güvenlidir; ancak çevrimli bir grafta ziyaret edilen düğümler kaydedilmezse algoritma `A → B → A → B` döngüsünde sonsuza kadar kalabilir.

## Derinlik öncelikli arama: Yolun sonunu gör

DFS, başlangıç düğümünden hareket ederek erişebildiği en derin noktaya ilerler. Gidecek yeni komşu kalmadığında geri izleme yapar. Bu davranış doğal olarak bir **yığın (stack)** ile modellenir. Özyinelemeli fonksiyonlarda çağrı yığını aynı görevi üstlenir.

```python
def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node in visited:
            continue

        visited.add(node)
        print(node)  # Düğüm burada işlenir.

        # Ters ekleme, soldaki komşunun önce gezilmesini sağlar.
        for neighbor in reversed(graph[node]):
            if neighbor not in visited:
                stack.append(neighbor)

    return visited
```

Kod, sıradaki düğümü yığının sonundan alır. Komşular yığına eklendiği için algoritma diğer seçeneklere geçmeden önce bir dal boyunca derinleşir. DFS; çevrim tespiti, topolojik sıralama, bağlı bileşen bulma ve labirent çözme gibi problemlerde kullanışlıdır.

## Genişlik öncelikli arama: Katman katman ilerle

BFS, önce başlangıç düğümüne bir kenar uzaklıktaki düğümleri, ardından iki kenar uzaklıktakileri inceler. Bu nedenle **kuyruk (queue)** kullanır. Ağırlıksız bir grafta en kısa yolu bulabilmesinin nedeni de düğümleri artan uzaklık sırasıyla ziyaret etmesidir.

```python
from collections import deque

def bfs(graph, start):
    visited = {start}
    queue = deque([(start, 0)])

    while queue:
        node, distance = queue.popleft()
        print(node, distance)  # Başlangıca olan uzaklık.

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))

    return visited
```

Bir düğüm kuyruğa eklenirken ziyaret edilmiş sayılır. Böylece aynı düğümün farklı komşular tarafından kuyruğa defalarca eklenmesi önlenir.

## DFS ve BFS karşılaştırması

| Özellik | DFS | BFS |
|---|---|---|
| Temel veri yapısı | Yığın | Kuyruk |
| İlerleme biçimi | Dal boyunca derine | Seviye seviye |
| Ağırlıksız en kısa yol | Garanti etmez | Garanti eder |
| Bellek davranışı | Derinliğe bağlıdır | Geniş seviyelerde büyür |
| Tipik kullanım | Çevrim, bileşen, topolojik sıralama | En kısa yol, seviye analizi |
| Tamlık | Sonsuz derinlikte sorun yaşayabilir | Sonlu dallanmada çözümü bulur |

Komşuluk listesi kullanılan bir grafta her düğüm ve kenar en fazla sabit sayıda işlendiği için iki algoritmanın zaman karmaşıklığı da $O(|V|+|E|)$ olur. Bellek karmaşıklığı genel durumda $O(|V|)$ düzeyindedir.

Arama ağacının dallanma katsayısı $b$, çözüm derinliği $d$ ise BFS yaklaşık $1+b+b^2+...+b^d$ düğüm üretir; baskın terim nedeniyle bu miktar $O(b^d)$ kabul edilir. DFS ise aynı anda çoğunlukla tek yol ile alternatifleri tuttuğundan bellekte daha tutumlu olabilir.

## Hangisini seçmeliyiz?

Hedefin başlangıca yakın olduğu veya ağırlıksız en kısa yolun istendiği durumlarda BFS güçlü seçimdir. Arama alanı çok genişse, çözümün derinde olduğu düşünülüyorsa ya da bütün yapısal ilişkiler araştırılacaksa DFS daha uygun olabilir. Ancak kenarlar farklı ağırlıklara sahipse BFS yerine Dijkstra gibi algoritmalar gerekir.

Özetle DFS meraklı bir mağara kâşifi gibi tek tünele dalar; BFS ise düzenli bir arama ekibi gibi bütün katmanı tarar. Doğru algoritma, yalnızca grafın biçimine değil, aradığınız cevabın türüne ve kullanabileceğiniz belleğe de bağlıdır.
