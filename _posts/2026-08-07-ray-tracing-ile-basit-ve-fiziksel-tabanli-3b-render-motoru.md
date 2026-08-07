---
layout: post
title: "Ray Tracing ile Basit ve Fiziksel Tabanlı 3B Render Motoru"
math: true
categories: 
  - Proje
tags: 
  - ray-tracing
  - 3B-render
  - Python
---

Bir ışık ışınının kameradan çıkıp sahnedeki nesnelere çarptığını, oradan ışık kaynaklarına ve aynalara doğru sekerek yolculuğunu sürdürdüğünü hayal edin. Ray tracing, gerçek dünyadaki optik davranışları ters yönde izleyerek yansıma, aydınlatma ve gölgeleri hesaplar. Bu projede kürelerden oluşan küçük bir sahneyi render eden, gölge ışınları ve yansımalar kullanan basit bir Python motoru kuracağız.

``

## Ray tracing nasıl çalışır?

Gerçek dünyada fotonlar ışık kaynağından çıkar ve kameraya ulaşır. Ancak milyarlarca fotonu rastgele takip etmek verimsizdir. Klasik ray tracing bunun tersini yapar: Her piksel için kameradan sahneye bir **birincil ışın** gönderir. Işın bir yüzeye çarparsa en yakın kesişim noktası bulunur; ardından ışık, gölge ve yansıma hesaplanır.

Bir ışın parametrik olarak şöyle gösterilir:

$$R(t) = O + tD$$

Burada $O$ ışının başlangıç noktası, $D$ normalize edilmiş yönü, $t$ ise ışın üzerindeki mesafedir. $t > 0$ koşulunu sağlayan en küçük değer, kameraya en yakın görünür yüzeyi verir.

| Işın türü | Başlangıç | Amaç |
|---|---|---|
| Birincil ışın | Kamera | Görünen yüzeyi bulmak |
| Gölge ışını | Kesişim noktası | Işığın engellenip engellenmediğini ölçmek |
| Yansıma ışını | Yüzey | Aynadaki görüntüyü hesaplamak |

## Küreyle kesişim

Merkezi $C$, yarıçapı $r$ olan kürenin denklemi $\lVert P-C\rVert^2=r^2$ biçimindedir. $P=R(t)$ yerleştirildiğinde ikinci dereceden denklem elde edilir:

$$at^2+bt+c=0$$

$$a=D\cdot D,\quad b=2D\cdot(O-C),\quad c=(O-C)\cdot(O-C)-r^2$$

Diskriminant $\Delta=b^2-4ac$ negatifse kesişim yoktur. Pozitifse iki çözümden en küçük pozitif olanı seçilir.

```python
import numpy as np

def normalize(v):
    return v / np.linalg.norm(v)

def hit_sphere(origin, direction, center, radius):
    oc = origin - center
    a = np.dot(direction, direction)
    b = 2.0 * np.dot(oc, direction)
    c = np.dot(oc, oc) - radius * radius
    delta = b * b - 4 * a * c
    if delta < 0:
        return None

    roots = [(-b - np.sqrt(delta)) / (2 * a),
             (-b + np.sqrt(delta)) / (2 * a)]
    valid = [t for t in roots if t > 1e-4]
    return min(valid) if valid else None
```

Küçük `1e-4` eşiği, ışının çıktığı yüzeye yeniden çarpmasını önler. Bu sorun render dünyasında **shadow acne** olarak bilinir; görüntünüz sivilce çıkarırsa matematiği suçlayabilirsiniz.

## Aydınlatma, gölge ve yansıma

Mat Lambert yüzeylerde parlaklık, normal $N$ ile ışık yönü $L$ arasındaki açıya bağlıdır:

$$I_d = k_d I_L \max(0,N\cdot L)$$

Noktasal ışığın şiddeti ayrıca uzaklığın karesiyle azalır: $I_L=P/(4\pi d^2)$. Böylece uzaktaki nesneler fiziksel olarak daha az aydınlanır. Kesişim noktasından ışığa gönderilen gölge ışını başka bir nesneye çarparsa doğrudan aydınlatma sıfırlanır.

Mükemmel ayna yansımasının yönü ise şöyledir:

$$R = D - 2(D\cdot N)N$$

```python
def reflect(direction, normal):
    return normalize(direction - 2 * np.dot(direction, normal) * normal)

def shade(point, normal, light_pos, light_power, blocked):
    to_light = light_pos - point
    distance = np.linalg.norm(to_light)
    light_dir = normalize(to_light)
    if blocked or np.dot(normal, light_dir) <= 0:
        return 0.0
    return light_power * np.dot(normal, light_dir) / (4 * np.pi * distance**2)
```

`blocked` değeri, gölge ışınının ışığa ulaşmadan önce nesne bulup bulmadığını belirtir. Yansıma için `reflect` yönünde yeni bir ışın gönderilir ve dönen renk yüzeyin yansıtıcılığıyla çarpılır.

| Özellik | Hız etkisi | Görsel katkı |
|---|---:|---|
| Gölge ışını | Orta | Nesneleri zemine oturtur |
| Yansıma | Yüksek | Ayna ve metal hissi verir |
| Yüksek çözünürlük | Çok yüksek | Kenar ayrıntısını artırır |
| Çoklu örnekleme | Çok yüksek | Tırtıklı kenarları azaltır |

Render döngüsünde her pikseli kamera düzlemindeki bir koordinata dönüştürün, ışını normalize edin ve `trace(ray, depth)` fonksiyonunu çağırın. Fonksiyon en yakın nesneyi bulmalı, yerel rengi hesaplamalı ve derinlik sınırı aşılmadıysa yansıma ışınını özyinelemeli izlemelidir. Üç veya dört sekme başlangıç için yeterlidir.

Bu temel motor; üçgen kesişimi, BVH hızlandırma yapısı, kırılma, Fresnel etkisi ve Monte Carlo örneklemesi eklenerek gerçek bir path tracer'a dönüştürülebilir. İlk görüntü yavaş üretilebilir, fakat kendi yazdığınız aynalı kürenin başka bir küreyi yansıttığını görmek beklemeye kesinlikle değer.
