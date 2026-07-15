---
layout: post
title: "C ile Gömülü Sistemlerde Bellek Yönetimi: Her Byte’ın Hesabını Tutmak"
math: true
categories: 
  - Bilgi
tags: 
  - C
  - Gömülü Sistemler
  - Bellek Yönetimi
  - Mikrodenetleyici
---

Gömülü sistemlerde bellek yönetimi, masaüstü programlamadaki konforlu dünyadan biraz farklıdır: burada RAM bazen birkaç kilobayttır, heap kullanmak riskli olabilir ve yanlış boyutlandırılmış bir dizi tüm kontrol döngüsünü sabote edebilir. C dili bu dünyada hâlâ kraldır; çünkü donanıma yakın çalışır, maliyeti düşüktür ve geliştiriciye her byte üzerinde doğrudan kontrol verir.
``
Bir mikrodenetleyicide bellek genellikle üç ana bölge gibi düşünülür: Flash, RAM ve çevresel register alanları. Flash program kodunu ve sabit verileri tutar; RAM ise çalışma zamanındaki değişkenler, stack ve varsa heap için kullanılır. Kısıtlı sistemlerde temel denklem şudur: $RAM_{kalan} = RAM_{toplam} - (global + stack + heap + buffer)$. Bu denklem basit görünür ama gerçek hayatta her kesme rutini, her geçici değişken ve her iletişim tamponu bu hesabı değiştirir.

| Bellek Alanı | Ne İçin Kullanılır? | Avantaj | Risk |
|---|---|---|---|
| Flash | Kod, sabit tablolar | RAM tüketmez | Yazma yavaştır, sınırlı ömür |
| Global/Static RAM | Kalıcı değişkenler | Öngörülebilir | Fazla kullanılırsa RAM biter |
| Stack | Fonksiyon çağrıları, yerel değişkenler | Hızlı | Taşma tespiti zordur |
| Heap | Dinamik ayırma | Esnek | Parçalanma ve belirsizlik |

Kontrol döngülerinde hedef yalnızca az bellek kullanmak değildir; aynı zamanda zamanlamayı da garanti etmektir. Örneğin bir motor kontrol döngüsünde örnekleme süresi $T_s = 1ms$ ise, bellek ayırma yüzünden oluşan rastgele gecikmeler kabul edilemez. Bu yüzden gömülü C projelerinde `malloc` ve `free` çoğu zaman yasaklı kelimeler gibidir. Heap parçalanması, başlangıçta çalışıp saatler sonra çöken cihazların klasik sebeplerindendir.

Dinamik ayırma gerekiyorsa, genel amaçlı heap yerine sabit bloklu bir bellek havuzu daha güvenlidir. Aşağıdaki örnek, 16 adet sabit boyutlu mesaj bloğunu yönetir. Böylece ayırma süresi yaklaşık sabittir ve parçalanma oluşmaz.

```c
#include <stdint.h>
#include <stddef.h>

#define BLOCK_SIZE 32
#define BLOCK_COUNT 16

typedef struct {
    uint8_t data[BLOCK_SIZE];
    uint8_t used;
} Block;

static Block pool[BLOCK_COUNT];

void *pool_alloc(void) {
    for (uint8_t i = 0; i < BLOCK_COUNT; i++) {
        if (!pool[i].used) {
            pool[i].used = 1;
            return pool[i].data;
        }
    }
    return NULL;
}

void pool_free(void *ptr) {
    for (uint8_t i = 0; i < BLOCK_COUNT; i++) {
        if (pool[i].data == ptr) {
            pool[i].used = 0;
            return;
        }
    }
}
```

Bu kodda belleğin tamamı derleme zamanında ayrılır. `pool_alloc`, boş bir blok bulur ve işaretçi döndürür. `pool_free` ise bloğu tekrar kullanılabilir hâle getirir. Dezavantajı, her bloğun aynı boyutta olmasıdır; 5 byte veriye de 32 byte ayrılır. Ancak gömülü sistemlerde öngörülebilirlik çoğu zaman maksimum verimden daha değerlidir.

Stack kullanımı da ayrıca izlenmelidir. Büyük dizileri fonksiyon içinde tanımlamak cazip görünür ama tehlikelidir. Örneğin `uint8_t buffer[1024];` satırı, 2 KB RAM bulunan bir mikrodenetleyicide felaketin yarısı olabilir. Büyük tamponlar global veya static tanımlanmalı, mümkünse boyutları hesaplanmalıdır: $$Buffer_{toplam}=N_{paket}\times Boyut_{paket}$$. Eğer UART üzerinden 8 paket tutulacak ve her paket 32 byte olacaksa toplam tampon 256 byte eder; kulağa az gelir ama 2 KB RAM içinde yüzde 12.5 demektir.

| Yaklaşım | Ne Zaman Tercih Edilir? | Bellek Davranışı |
|---|---|---|
| Yerel küçük değişken | Kısa hesaplamalar | Stack üzerinde hızlı |
| Static tampon | Sürekli kullanılan veri | Sabit RAM tüketimi |
| Ring buffer | UART, ADC, sensör akışı | Verimli ve tahmin edilebilir |
| Heap | Nadiren önerilir | Esnek ama riskli |

Veri tipi seçimi de byte avcılığının eğlenceli kısmıdır. Sıcaklık 0-100 arasıysa `uint8_t` yeterli olabilir; sayaç 100000 değerine çıkacaksa `uint32_t` gerekir. Ancak işlemci 8 bit ise 32 bit aritmetik daha yavaş olabilir. Yani bellek optimizasyonu ile CPU maliyeti birlikte düşünülmelidir.

Pratikte iyi bir strateji şudur: önce bellek haritasını çıkar, global değişkenleri say, maksimum stack derinliğini tahmin et, kesme rutinlerinde büyük işlem yapma ve iletişim tamponlarını matematiksel olarak boyutlandır. Derleyicinin map dosyası bu noktada hazine haritasıdır; hangi sembolün kaç byte tuttuğunu gösterir.

Sonuç olarak C ile gömülü sistemlerde bellek yönetimi, biraz muhasebe biraz da mühendislik sezgisidir. Her byte’ın bir görevi olmalı, her tamponun nedeni bilinmeli ve her kontrol döngüsü zamanında bitmelidir. Kaynak kısıtlı olabilir; ama iyi tasarlanmış bir bellek düzeniyle küçük bir mikrodenetleyici bile şaşırtıcı derecede kararlı ve güçlü çalışabilir.
