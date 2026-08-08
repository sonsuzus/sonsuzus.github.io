---
layout: post
title: "Conway'in Hayat Oyunu'na Turbo Takmak: Hashlife Algoritması"
math: true
categories: 
  - Bilgi
tags: 
  - hashlife
  - conway-hayat-oyunu
  - algoritma
---

Conway'in Hayat Oyunu basit kurallardan şaşırtıcı derecede karmaşık yapılar üretir. Ancak milyonlarca hücreden oluşan bir evreni klasik yöntemle simüle etmek, her nesilde bütün ızgarayı taramak anlamına gelir. Glider filoları büyüdükçe işlemciniz de küçük bir yaşam krizi geçirebilir! Hashlife, tekrar eden uzay-zaman desenlerini tanıyıp sonuçlarını önbelleğe alarak devasa ve seyrek evrenlerde inanılmaz sıçramalar yapar.
``
## Önce oyunun matematiği

Her hücre canlı veya ölüdür. Hücrenin bir sonraki durumu, sekiz komşusundaki canlı hücre sayısına bağlıdır. $x_t(p) \in \{0,1\}$ hücrenin durumunu, $n_t(p)$ ise canlı komşu sayısını göstersin:

$$
x_{t+1}(p)=
\begin{cases}
1, & n_t(p)=3 \\
1, & x_t(p)=1 \land n_t(p)=2 \\
0, & \text{diğer durumlarda}
\end{cases}
$$

Klasik simülasyon, genişliği $W$, yüksekliği $H$ olan bir alan için her nesilde yaklaşık $O(WH)$ iş yapar. Hashlife'ın gücü ise tek bir sabit karmaşıklık formülünden değil; daha önce gördüğü alt evrenleri tekrar hesaplamamasından gelir.

| Yaklaşım | Uzay gösterimi | Zaman ilerletme | Güçlü olduğu durum |
|---|---|---|---|
| Dizi tabanlı | Tüm hücreler | Birer nesil | Küçük, yoğun alanlar |
| Seyrek küme | Yalnızca canlı hücreler | Birer nesil | Dağınık ve hareketli desenler |
| Hashlife | Paylaşılan dört ağaç | Üstel sıçramalar | Büyük, tekrarlı ve seyrek evrenler |

## Izgara yerine dört ağaç

Hashlife, evreni kenar uzunluğu $2^k$ olan karelere böler. Her kare; kuzeybatı, kuzeydoğu, güneybatı ve güneydoğu çocuklarından oluşan bir **quadtree** düğümüdür. Aynı dört çocuğa sahip düğümler yalnızca bir kez saklanır. Buna hash-consing denir.

```python
class Node:
    def __init__(self, level, nw, ne, sw, se):
        self.level = level
        self.children = (nw, ne, sw, se)
        self.population = sum(c.population for c in self.children)
        self.result = None

node_cache = {}

def make_node(level, nw, ne, sw, se):
    key = (level, id(nw), id(ne), id(sw), id(se))
    if key not in node_cache:
        node_cache[key] = Node(level, nw, ne, sw, se)
    return node_cache[key]
```

Bu fabrika fonksiyonu eşdeğer bölgelerin aynı nesneyi paylaşmasını sağlar. Gerçek uygulamada `id` yerine çocuk düğümlerin kararlı kimlikleri veya doğrudan nesne referansları kullanılabilir. `population == 0` kontrolüyle tamamen boş bölgeler anında atlanır.

## Zamanı neden katlayabiliyoruz?

Bir seviyedeki düğümün merkez bölgesinin $2^{k-2}$ nesil sonraki sonucu hesaplanıp düğümde saklanır. Bunun mümkün olmasının nedeni bilgi yayılım hızıdır: Bir hücrenin etkisi her nesilde en fazla bir hücre uzaklaşabilir. Dış kenarlardan yeterince uzak merkez bölge, belirlenen süre boyunca düğüm dışındaki hücrelerden etkilenmez.

Algoritma, çakışan dokuz alt bölge oluşturur; bunların sonuçlarını özyinelemeli hesaplar ve merkezdeki dört sonucu birleştirir. Aynı alt desen yeniden görüldüğünde simülasyon yapmak yerine önbellekteki gelecek doğrudan döndürülür.

```python
def advance(node):
    if node.result is not None:
        return node.result
    if node.population == 0:
        node.result = empty_node(node.level - 1)
        return node.result
    if node.level == 2:
        node.result = evolve_base_case(node)
        return node.result

    regions = overlapping_subnodes(node)
    futures = [advance(region) for region in regions]
    node.result = combine_center(futures)
    return node.result
```

Kod, Hashlife'ın temel fikrini gösterir: sonucu biliyorsan kullan, bölge boşsa kısa devre yap, küçükse doğrudan hesapla, büyükse parçalayıp birleştir.

## Pratik mühendislik notları

Evren kökünün çevresine boşluk eklemek önemlidir; desen sınıra yaklaşırsa kök iki kat büyütülmelidir. Ayrıca bellek önbelleği sınırsız bırakılmamalı, erişilmeyen düğümler çöp toplama veya yaş tabanlı temizleme ile kaldırılmalıdır.

Hashlife her durumda sihirli değildir. Rastgele gürültülü desenlerde tekrar az olduğundan hash tabloları ek maliyet yaratabilir. Buna karşılık durağan yapılar, osilatörler ve uzun mesafe yol alan glider'lar bol tekrar üretir. Doğru evrende Hashlife yalnızca daha hızlı koşmaz; milyonlarca nesli tek tek yaşamadan geleceğe adeta ışınlanır.
