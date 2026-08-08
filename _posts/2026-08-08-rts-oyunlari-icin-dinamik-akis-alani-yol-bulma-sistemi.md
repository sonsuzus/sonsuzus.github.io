---
layout: post
title: "RTS Oyunları İçin Dinamik Akış Alanı Yol Bulma Sistemi"
math: true
categories: 
  - Proje
tags: 
  - oyun geliştirme
  - akış alanı
  - yol bulma
---

Yüzlerce askerin aynı hedefe koştuğu bir gerçek zamanlı strateji oyununda her birim için ayrı ayrı A* çalıştırmak, işlemciyi kısa sürede savaş alanına çevirebilir. Akış alanı yol bulma, tek bir ortak yön haritası üreterek bütün birimlerin hedefe akmasını sağlar. Üstelik hareketli engeller ve değişen arazi maliyetleri hesaba katıldığında sistem hem performanslı hem de oldukça doğal sonuçlar verir.
``

## Akış alanının temel mantığı

Oyun haritasını karelerden oluşan bir ızgara olarak düşünelim. Sistem üç katman üretir:

1. **Maliyet alanı:** Her karenin geçiş maliyetini tutar. Yolun maliyeti 1, çamurun 5, duvarın ise sonsuz olabilir.
2. **Entegrasyon alanı:** Her hücreden hedefe ulaşmanın toplam maliyetini gösterir.
3. **Akış alanı:** Her hücre için en düşük maliyetli komşuya bakan yön vektörünü saklar.

Bir hücrenin entegrasyon değeri kabaca şu bağıntıyla hesaplanır:

$$I(x) = \min_{n \in N(x)} \left(I(n) + C(x,n)\right)$$

Burada $I(x)$ hücrenin hedefe toplam maliyeti, $N(x)$ komşuları ve $C(x,n)$ geçiş maliyetidir. Hedef hücrenin değeri $0$ olarak başlatılır. Ardından Dijkstra algoritmasına benzeyen bir yayılma gerçekleştirilir.

| Yöntem | Hesaplama yaklaşımı | Çok sayıda birim | Dinamik hedefler |
|---|---|---:|---:|
| A* | Her birim için yol üretir | Pahalı | Orta |
| NavMesh | Geometrik rota üretir | İyi | İyi |
| Akış alanı | Grup için yön haritası üretir | Çok iyi | Yeniden hesaplama gerekir |

## Alanların oluşturulması

Aşağıdaki C# sınıfı, entegrasyon alanını kuyruk tabanlı biçimde hesaplar. Örneği sade tutmak için dört yönlü komşuluk kullanıyoruz:

```csharp
public class FlowField
{
    public int Width, Height;
    public int[,] Cost;
    public int[,] Integration;
    public Vector2[,] Direction;

    public void Build(Vector2Int target)
    {
        const int INF = int.MaxValue;

        for (int x = 0; x < Width; x++)
            for (int y = 0; y < Height; y++)
                Integration[x, y] = INF;

        var frontier = new PriorityQueue<Vector2Int, int>();
        Integration[target.x, target.y] = 0;
        frontier.Enqueue(target, 0);

        while (frontier.Count > 0)
        {
            Vector2Int current = frontier.Dequeue();

            foreach (Vector2Int next in GetNeighbours(current))
            {
                if (Cost[next.x, next.y] < 0) continue;

                int value = Integration[current.x, current.y]
                          + Cost[next.x, next.y];

                if (value < Integration[next.x, next.y])
                {
                    Integration[next.x, next.y] = value;
                    frontier.Enqueue(next, value);
                }
            }
        }

        BuildDirections();
    }
}
```

`Cost` değeri negatif olan hücreler geçilemez kabul edilir. `PriorityQueue`, en düşük toplam maliyetli hücreyi önce işleyerek ağırlıklı arazilerde doğru sonuç üretir.

## Yön vektörlerini çıkarmak

Her hücre, entegrasyon değeri en düşük komşusunu seçer. Birimin hedef hızı bu yönle hesaplanabilir:

$$v_{istenen} = \hat{d} \cdot v_{maksimum}$$

```csharp
private void BuildDirections()
{
    for (int x = 0; x < Width; x++)
    for (int y = 0; y < Height; y++)
    {
        var cell = new Vector2Int(x, y);
        Vector2Int best = cell;

        foreach (var neighbour in GetNeighbours(cell))
            if (Integration[neighbour.x, neighbour.y] <
                Integration[best.x, best.y])
                best = neighbour;

        Direction[x, y] = ((Vector2)(best - cell)).normalized;
    }
}
```

Birimin dünya konumu ızgara koordinatına çevrilir ve ilgili `Direction` değeri okunur. Hareketin robotik görünmemesi için bu vektör; komşulardan kaçınma, hizalanma ve çarpışma önleme kuvvetleriyle harmanlanmalıdır.

## Dinamik engelleri yönetmek

Yeni bir bina yerleştirildiğinde tüm haritayı yeniden hesaplamak kolaydır fakat büyük haritalarda pahalı olabilir. Bunun yerine değişen hücreleri “kirli” olarak işaretleyip yalnızca etkilenen bölgeyi güncellemek daha verimlidir.

| Değişiklik | Önerilen çözüm |
|---|---|
| Hedef değişti | Alanı tamamen yeniden oluştur |
| Tek bina eklendi | Yerel bölgeyi kirli işaretle |
| Geçici birim kalabalığı | Kaçınma kuvveti kullan |
| Köprü yıkıldı | Bağlantılı alanı yeniden hesapla |

Ayrıca haritayı sektörlere ayırarak yalnızca birimlerin bulunduğu veya hedefe bağlanan sektörler için akış alanı üretilebilir. Böylece yüzlerce asker aynı hesaplamayı paylaşır; ordunuz disiplinle ilerlerken işlemciniz de beyaz bayrak çekmez.
