---
layout: post
title: "Eşzamanlılık ve İş Parçacıkları: Çok Çekirdeği Akıllıca Kullanmak"
math: true
categories: 
  - Bilgi
tags: 
  - multithreading
  - eşzamanlılık
  - thread
  - senkronizasyon
  - çok çekirdekli
---

Modern işlemciler artık saat hızını sınırsız artırmak yerine birden fazla çekirdekle güçleniyor. Bir uygulamanın bu gücü kullanabilmesi için işleri bağımsız parçalara bölmesi, bu parçaları iş parçacıklarında (thread) çalıştırması ve ortak belleğe erişimi dikkatle düzenlemesi gerekir. Ancak multithreading, uygulamayı otomatik olarak hızlandıran sihirli bir değnek değildir; doğru tasarlanmadığında yarış koşulları, kilitlenmeler ve zor tekrarlanan hatalar üretir.
``

## Thread, süreç ve eşzamanlılık

**Süreç** (process), kendi bellek alanına sahip çalışan program örneğidir. Aynı süreçteki thread'ler ise kodu, heap alanını ve açık kaynakları paylaşır; yalnızca çağrı yığını ve register durumları özeldir. Bu paylaşım, thread oluşturmayı hafifletir ve veri alışverişini hızlandırır. Bedeli ise ortak verinin korunmasıdır.

| Kavram | Bellek modeli | Güçlü yanı | Temel risk |
|---|---|---|---|
| Process | İzole bellek | Hata yalıtımı | IPC maliyeti |
| Thread | Ortak bellek | Hızlı iletişim | Data race |
| Async I/O | Genellikle tek/az thread | I/O verimliliği | Akış karmaşıklığı |

Eşzamanlılık (concurrency), birden çok işin zaman içinde ilerlemesidir. Paralellik (parallelism) ise işlerin gerçekten aynı anda, ayrı çekirdeklerde yürütülmesidir. Tek çekirdekli bir makine eşzamanlı davranabilir; fakat gerçek paralellik için birden fazla yürütme kaynağı gerekir.

## Hızlanmanın matematiği: Amdahl kanunu

Programın yalnızca paralelleştirilebilen kısmı hızlanır. Amdahl kanunu, teorik üst sınırı şöyle verir:

$$S(N) = \frac{1}{(1-P) + \frac{P}{N}}$$

Burada $P$ paralelleştirilebilir oran, $N$ çekirdek sayısıdır. Örneğin işin %90'ı paralelse ve 8 çekirdek kullanılıyorsa, $S(8) \approx 4.7$ olur; yani sekiz kat değil. Seri bölüm, thread oluşturma maliyeti, cache etkileri ve senkronizasyon bu sonucu daha da düşürebilir. Bu nedenle önce profil çıkarın: darboğaz CPU mu, disk mi, ağ mı, yoksa kilit bekleme süresi mi?

## Ortak belleğin tehlikesi: yarış koşulu

Aşağıdaki sayaç artırma işlemi masum görünür; fakat `counter++` tek ve bölünemez bir işlem değildir. Okuma, artırma ve yazma adımlarına ayrılabilir.

```cpp
#include <thread>
#include <mutex>

int counter = 0;
std::mutex counterMutex;

void increment() {
    for (int i = 0; i < 100000; ++i) {
        std::lock_guard<std::mutex> lock(counterMutex);
        ++counter;
    }
}

int main() {
    std::thread a(increment), b(increment);
    a.join();
    b.join();
}
```

`std::lock_guard`, mutex'i kapsam boyunca kilitler ve kapsam bitince otomatik serbest bırakır. Böylece iki thread aynı anda sayaç güncelleyemez. Basit sayaçlar için `std::atomic<int>` çoğu zaman daha uygun ve daha düşük maliyetli bir seçenektir.

| Araç | Ne zaman tercih edilir? | Dikkat edilmesi gereken |
|---|---|---|
| Mutex | Birden çok veriyi tutarlı güncelleme | Uzun kritik bölge performansı düşürür |
| Atomic | Sayaç, bayrak, tekil atomik durum | Karmaşık invariant'ları korumaz |
| Condition variable | Bir olayın oluşmasını bekleme | Her zaman koşulla birlikte kullanılmalı |
| Semaphore | Sınırlı kaynak havuzu | İzin sayısı doğru yönetilmeli |

## Sağlam mimari için pratik ilkeler

Kritik bölgeleri kısa tutun; kilit altındayken ağ isteği, dosya işlemi veya ağır hesaplama yapmayın. Kilitleri birden fazlaysa her yerde aynı sırayla alın; bu, iki thread'in birbirini sonsuza dek beklediği deadlock riskini azaltır. Paylaşılan değişken sayısını azaltmak için mesaj kuyruğu, immutable veri ve iş kuyruğu (thread pool) gibi yaklaşımları değerlendirin.

Son olarak thread sayısını çekirdek sayısının rastgele katı yapmayın. CPU ağırlıklı işler için çekirdek sayısına yakın bir havuz, I/O ağırlıklı işler için ise bekleme sürelerini tolere eden daha geniş bir havuz mantıklıdır. Başarılı multithreading tasarımı, en çok thread'i açmak değil; en az paylaşım ve en net senkronizasyonla doğru işi paralelleştirmektir.
