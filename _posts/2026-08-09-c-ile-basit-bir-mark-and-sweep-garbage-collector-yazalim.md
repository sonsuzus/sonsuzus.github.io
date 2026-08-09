---
layout: post
title: "C ile Basit Bir Mark-and-Sweep Garbage Collector Yazalım"
math: true
categories: 
  - Proje
tags: 
  - C
  - Bellek Yönetimi
  - Garbage Collector
---

Bellek yönetimi, programlamanın “ışıkları kapattım mı?” sorusudur: Bir nesneyi ayırdığımızı hatırlarız ama serbest bırakıp bırakmadığımızdan asla tam emin olamayız. Bu projede C ile küçük bir **mark-and-sweep garbage collector** geliştirerek manuel bellek yönetimini, nesne erişilebilirliğini ve sanal belleğin süreçteki rolünü birlikte inceleyeceğiz.

``

## Önce bellek haritasını anlayalım

Bir süreç çalıştırıldığında işletim sistemi ona geniş ve kesintisiz görünen bir **sanal adres alanı** sunar. Programın kullandığı adresler doğrudan fiziksel RAM adresleri değildir. Sayfa tabloları, sanal sayfaları fiziksel çerçevelere eşler.

Bir adres alanı kabaca kod, global veriler, stack ve heap bölgelerinden oluşur. `malloc` ile istediğimiz alan heap üzerinde yönetilir; ancak her `malloc` çağrısının anında yeni bir fiziksel sayfa ayırması gerekmez. İşletim sistemi sayfaları ihtiyaç anında eşleyebilir.

Bellek kullanımını basitleştirerek şöyle ifade edebiliriz:

$$M_{etkin} = M_{ayrılan} - M_{erişilemeyen}$$

Garbage collector’ın amacı, artık kök nesnelerden erişilemeyen $M_{erişilemeyen}$ bölümünü bulup yeniden kullanılabilir hâle getirmektir.

| Kavram | Manuel yönetim | Garbage collector |
|---|---|---|
| Ayırma | `malloc` | GC tarafından izlenen ayırma |
| Serbest bırakma | `free` çağrısı | Erişilebilirlik analizinden sonra |
| Temel risk | Sızıntı, çift `free` | Duraklama, ek metadata |
| Kontrol | Programcıda | Çalışma zamanı sisteminde |
| Sanal bellek ilişkisi | Heap sayfalarını kullanır | Aynı heap içinde canlı nesneleri belirler |

## Mark-and-sweep nasıl çalışır?

Algoritma iki temel aşamadan oluşur:

1. **Mark:** Stack, global değişkenler veya çalışma zamanı tarafından tutulan köklerden başlanır. Ulaşılabilen bütün nesneler işaretlenir.
2. **Sweep:** Ayrılmış nesneler taranır. İşaretlenmemiş olanlar erişilemez kabul edilerek serbest bırakılır.

Bu örnekte gerçek stack taraması yapmayacağız. Bunun yerine kökleri açıkça kaydedeceğiz. Böylece algoritmanın özü, platforma özgü ayrıntılar arasında kaybolmayacak.

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct Object {
    int marked;
    int value;
    struct Object *ref;
    struct Object *next;
} Object;

static Object *heap = NULL;

Object *gc_alloc(int value) {
    Object *obj = malloc(sizeof(Object));
    if (!obj) {
        perror("malloc");
        exit(EXIT_FAILURE);
    }

    obj->marked = 0;
    obj->value = value;
    obj->ref = NULL;
    obj->next = heap;
    heap = obj;
    return obj;
}

void mark(Object *obj) {
    if (obj == NULL || obj->marked)
        return;

    obj->marked = 1;
    mark(obj->ref);
}

void sweep(void) {
    Object **cursor = &heap;

    while (*cursor) {
        Object *obj = *cursor;
        if (!obj->marked) {
            *cursor = obj->next;
            printf("Silindi: %d\n", obj->value);
            free(obj);
        } else {
            obj->marked = 0;
            cursor = &obj->next;
        }
    }
}

void collect(Object **roots, size_t count) {
    for (size_t i = 0; i < count; i++)
        mark(roots[i]);
    sweep();
}
```

`heap` listesi ayrılan tüm nesnelerin envanteridir. `ref`, bir nesneden diğerine referans oluşturarak küçük bir nesne grafiği kurar. `mark` fonksiyonu bu grafiği derinlik öncelikli dolaşır. Döngüsel referanslarda sonsuz özyinelemeyi `marked` kontrolü engeller.

## Collector’ı deneyelim

```c
int main(void) {
    Object *a = gc_alloc(10);
    Object *b = gc_alloc(20);
    Object *orphan = gc_alloc(99);

    a->ref = b;

    Object *roots[] = { a };
    collect(roots, 1);

    roots[0] = NULL;
    collect(roots, 1);
    return 0;
}
```

İlk koleksiyonda `a` köktür; `b` nesnesine `a->ref` üzerinden ulaşılır. `orphan` ise hiçbir kökten erişilemediği için silinir. İkinci koleksiyonda kök kaldırıldığından hem `a` hem `b` temizlenir. Referans döngüsü kurulsa bile kökten ulaşılamayan nesneler toplanabilir; bu, referans sayımına göre önemli bir avantajdır.

## Gerçek sistemlerden farkı

Bu oyuncak collector thread güvenliği, bellek sıkıştırma, nesil tabanlı toplama ve stack taraması sunmaz. Ayrıca özyinelemeli `mark`, çok derin grafiklerde stack taşmasına yol açabilir. Üretim sistemleri iş listesinden yararlanan yinelemeli tarama, tri-color marking ve eşzamanlı toplama gibi yöntemler kullanır.

Yine de proje kritik fikri gösterir: `free` işlemini otomatikleştirmek yalnızca adresleri takip etmek değildir; programın canlı nesne grafiğini anlamaktır. Sanal bellek bize adres alanını sağlar, allocator blokları dağıtır, garbage collector ise bu bloklardan hangilerinin artık hikâyede rolü kalmadığına karar verir.
