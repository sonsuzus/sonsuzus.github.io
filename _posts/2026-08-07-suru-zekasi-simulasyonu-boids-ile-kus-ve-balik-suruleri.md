---
layout: post
title: "Sürü Zekâsı Simülasyonu: Boids ile Kuş ve Balık Sürüleri"
math: true
categories: 
  - Proje
tags: 
  - sürü zekâsı
  - boids
  - simülasyon
---

Gökyüzünde aynı anda yön değiştiren kuşlar veya suda tek bir canlıymış gibi ilerleyen balıklar merkezi bir komut sistemine sahip değildir. Buna rağmen ortaya son derece düzenli ve karmaşık hareketler çıkar. Sürü zekâsı simülasyonu, her bireye birkaç basit kural vererek bu şaşırtıcı davranışları bilgisayar ortamında yeniden üretmemizi sağlar.
``

## Sürü zekâsı nedir?

Sürü zekâsı, merkezi yönetim olmadan çalışan çok sayıda basit ajanın yerel etkileşimlerinden doğan kolektif davranıştır. Bir kuş, bütün sürünün konumunu hesaplamaz; yalnızca yakınındaki komşularını gözlemler. Bu yaklaşım robot koordinasyonu, trafik modelleme, oyun yapay zekâsı ve optimizasyon gibi alanlarda kullanılır.

Craig Reynolds tarafından geliştirilen **Boids** modeli, her kuşu bağımsız bir ajan olarak ele alır. Ajanın konumu $p_i$, hızı ise $v_i$ olsun. Her simülasyon adımında hareket yaklaşık olarak şöyle güncellenir:

$$v_i(t+1) = v_i(t) + w_s S_i + w_a A_i + w_c C_i$$

$$p_i(t+1) = p_i(t) + v_i(t+1)$$

Buradaki $S_i$ ayrılma, $A_i$ hizalanma ve $C_i$ bütünleşme kuvvetidir. $w_s$, $w_a$ ve $w_c$ katsayıları davranışların etkisini belirler.

| Kural | Ajanın yaptığı | Ortaya çıkan etki |
|---|---|---|
| Ayrılma | Çok yakın komşulardan uzaklaşır | Çarpışmalar azalır |
| Hizalanma | Komşuların ortalama yönüne döner | Sürü ortak yönde ilerler |
| Bütünleşme | Komşuların merkezine yaklaşır | Grup dağılmaz |

Bu kuralların hiçbiri tek başına gerçekçi bir sürü oluşturmaz. Ayrılma fazla güçlü olursa ajanlar birbirinden kaçar; bütünleşme baskın olursa ekranın ortasında sıkışmış bir top oluşur. Eğlence, katsayılarla oynayıp düzen ile kaos arasındaki dengeyi bulmaktadır.

## Python ile hareket çekirdeği

Aşağıdaki sınıf, bir ajanın komşularına bakarak üç temel kuvveti hesaplar. NumPy vektör işlemlerini kolaylaştırır:

```python
import numpy as np

class Boid:
    def __init__(self, position, velocity):
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)

    def update(self, flock, radius=60):
        neighbors = [b for b in flock
                     if b is not self and
                     np.linalg.norm(b.position - self.position) < radius]

        if not neighbors:
            self.position += self.velocity
            return

        center = np.mean([b.position for b in neighbors], axis=0)
        average_velocity = np.mean([b.velocity for b in neighbors], axis=0)

        cohesion = (center - self.position) * 0.002
        alignment = (average_velocity - self.velocity) * 0.05
        separation = np.zeros(2)

        for other in neighbors:
            difference = self.position - other.position
            distance = np.linalg.norm(difference)
            if 0 < distance < 20:
                separation += difference / distance

        self.velocity += cohesion + alignment + separation * 0.08

        speed = np.linalg.norm(self.velocity)
        if speed > 4:
            self.velocity = self.velocity / speed * 4

        self.position += self.velocity
```

`neighbors` listesi algı yarıçapındaki ajanları seçer. Bütünleşme komşuların geometrik merkezini, hizalanma ortalama hızını hedefler. Ayrılma ise mesafe azaldıkça ajanı ters yönde iter. Hız sınırı koymak önemlidir; aksi hâlde kuvvetler birikerek kuşları roket hızına ulaştırabilir.

## Simülasyonu canlandırmak

Pygame, ajanları ekranda göstermek için kullanılabilir. Her karede tüm ajanlar güncellenir, ekran sınırını aşanlar karşı taraftan çıkarılır ve küçük daireler çizilir:

```python
for boid in flock:
    boid.update(flock)
    boid.position %= [width, height]
    pygame.draw.circle(screen, (80, 210, 255),
                       boid.position.astype(int), 4)
```

Kuş görünümü için hız yönünde dönen üçgenler, balık görünümü için kuyruk animasyonu eklenebilir. Fare imlecini bir avcı olarak tanımlayıp yakındaki ajanlara kaçış kuvveti uygulamak da sürünün aniden yarılması gibi etkileyici davranışlar üretir.

## Deney fikirleri

Ajan sayısını, algı yarıçapını ve kural ağırlıklarını çalışma sırasında değiştirin. Sonuçları yalnızca görsel olarak değil, ortalama komşu mesafesi ve yön uyumu gibi ölçülerle de inceleyin. Örneğin yön uyumu, normalize edilmiş hızların ortalamasıyla $0$ ile $1$ arasında ölçülebilir. Basit yerel kararların küresel düzeyde nasıl örgütlendiğini görmek, bu projeyi hem öğretici hem de hipnotik derecede eğlenceli yapar.
