---
layout: post
title: "C++ ve Oyun Motorlarının Kalbi: İşaretçilerle Belleği Dizginlemek"
math: true
categories: 
  - Bilgi
tags: 
  - C++
  - Oyun Motoru
  - Bellek Yönetimi
  - Fizik Motoru
---

Bir oyun motorunu devasa bir lunapark gibi düşünün: fizik simülasyonu hız trenidir, render sistemi ışıklı dönme dolaptır, yapay zekâ ise pamuk şeker kuyruğunda karar vermeye çalışan NPC’dir. Bu lunaparkın elektriği ise bellektir. C++ burada sahneye çıkar; çünkü işaretçiler, düşük seviyeli bellek kontrolü ve veri yerleşimi sayesinde üç boyutlu dünyaların milisaniyeler içinde hesaplanmasını sağlar.

``

## Neden C++ hâlâ oyun motorlarında bu kadar güçlü?

Modern oyun motorlarında her karede binlerce nesnenin konumu güncellenir, çarpışmalar çözülür, animasyonlar karıştırılır ve GPU’ya veri gönderilir. 60 FPS hedefinde bir karenin süresi yaklaşık $16.67ms$’dir. Eğer fizik, render ve oyun mantığı bu küçük zaman penceresine sığmazsa oyuncu takılma hisseder.

C++’ın avantajı, geliştiriciye belleğin nerede, ne zaman ve nasıl kullanılacağını söyleme şansı vermesidir. İşaretçiler sayesinde veriye doğrudan erişebilir, nesneleri kopyalamadan aktarabilir ve donanım önbelleğini daha verimli kullanabiliriz.

| Yaklaşım | Avantaj | Risk |
|---|---|---|
| Ham işaretçi `T*` | Çok hızlı, doğrudan erişim | Dangling pointer, bellek sızıntısı |
| `std::unique_ptr` | Tek sahiplik, otomatik temizlik | Kopyalanamaz, tasarım dikkat ister |
| `std::shared_ptr` | Paylaşımlı sahiplik | Referans sayımı maliyeti |
| Nesne havuzu | Parçalanmayı azaltır | Yönetim kodu karmaşıklaşır |

## Fizik motorunun arkasındaki basit matematik

Bir fizik motoru temelde şu soruyu her karede tekrar sorar: “Nesneler şimdi nerede olmalı?” En basit hareket güncellemesi şu formülle yapılabilir: $x_{t+dt} = x_t + v_t \cdot dt$. Burada $x$ konum, $v$ hız, $dt$ ise kareler arası zamandır.

Çarpışma tarafında iş daha eğlenceli hale gelir. Bin nesnenin birbirine çarpıp çarpmadığını saf yöntemle kontrol edersek karmaşıklık $O(n^2)$ olur. Yani 1000 nesne için yaklaşık 1 milyon karşılaştırma! Bu yüzden oyun motorları broad phase ve narrow phase gibi aşamalar kullanır.

| Aşama | Amaç | Örnek Teknik |
|---|---|---|
| Broad Phase | Olası çarpışmaları hızlı elemek | Spatial Grid, BVH, Octree |
| Narrow Phase | Gerçek temas hesaplamak | SAT, GJK, Raycast |
| Solver | Tepki kuvvetini üretmek | Impulse Resolution |

## İşaretçiler neden performans için kritik?

Oyun motorlarında en büyük düşmanlardan biri gereksiz kopyalamadır. Büyük bir `RigidBody` nesnesini her fonksiyona değer olarak göndermek pahalıdır. Bunun yerine işaretçi veya referans kullanılır. Böylece nesne bellekte tek yerde durur, sistemler aynı veriye erişir.

```cpp
struct Vec3 {
    float x, y, z;
};

struct RigidBody {
    Vec3 position;
    Vec3 velocity;
    float mass;
};

void integrate(RigidBody* body, float dt) {
    if (!body) return;

    body->position.x += body->velocity.x * dt;
    body->position.y += body->velocity.y * dt;
    body->position.z += body->velocity.z * dt;
}
```

Bu kodda `RigidBody* body`, fizik nesnesinin adresini taşır. Fonksiyon nesneyi kopyalamaz; doğrudan orijinal veriyi günceller. Bu, özellikle binlerce gövdeyi her kare güncelleyen fizik sistemlerinde ciddi fark yaratır.

## Bellek havuzları: Motorun gizli turbo modu

Bir sahnede sürekli mermi, parçacık, düşman veya geçici temas noktası oluşturup yok etmek klasik `new/delete` ile maliyetli olabilir. Çünkü işletim sisteminden sık sık bellek istemek yavaştır ve bellek parçalanmasına yol açar. Çözüm: önceden büyük bir blok ayırmak ve nesneleri bu bloktan dağıtmak.

```cpp
class BodyPool {
    RigidBody bodies[1024];
    bool used[1024] = {};

public:
    RigidBody* create() {
        for (int i = 0; i < 1024; ++i) {
            if (!used[i]) {
                used[i] = true;
                return &bodies[i];
            }
        }
        return nullptr;
    }

    void destroy(RigidBody* body) {
        int index = static_cast<int>(body - bodies);
        if (index >= 0 && index < 1024) used[index] = false;
    }
};
```

Bu yapı, nesneleri bitişik bellekte tuttuğu için CPU önbelleğine dosttur. Yani işlemci “bir sonraki veriyi” tahmin edip daha hızlı erişebilir. Karmaşık sahnelerde bu fark, teoriden çıkıp FPS grafiğinde görünür hale gelir.

## Sonuç: Güç büyük, sorumluluk da büyük

C++ ile oyun motoru geliştirmek, spor araba kullanmaya benzer: inanılmaz hızlanır ama virajı yanlış alırsanız bariyerle tanışırsınız. İşaretçiler, bellek havuzları, RAII ve veri odaklı tasarım birlikte kullanıldığında fizik motorları daha hızlı, üç boyutlu dünyalar daha akıcı hale gelir. Kısacası C++ hâlâ oyun motorlarının kalbinde atıyorsa sebebi nostalji değil; belleğe yakın durmanın verdiği ham güçtür.
