---
layout: post
title: "Heap Macerası: C’de malloc/free, C++’ta new/delete ve Bellek Sızıntılarını Önleme"
math: true
categories: 
  - Bilgi
tags: 
  - C
  - C++
  - Dinamik Bellek
  - Heap
  - Memory Leak
---

Programlar çalışırken tüm veri boyutları baştan bilinmez: Kullanıcının gireceği metnin uzunluğu, dosyadaki kayıt sayısı veya oluşturulacak nesne miktarı değişkendir. İşte bu noktada **heap (öbek)** alanı devreye girer. Heap, çalışma zamanında bellek talep etmemizi sağlayan bölgedir. Bu bellek çağıran fonksiyon bittiğinde kendiliğinden kaybolmaz; programcı onu bilinçli biçimde iade etmelidir. Güç büyük, sorumluluk daha da büyüktür.
``

## Stack ve heap neden farklıdır?

Yerel değişkenler çoğunlukla **stack** üzerinde tutulur. Fonksiyon sona erdiğinde stack çerçevesi otomatik temizlenir. Heap ise daha uzun ömürlü veriler için uygundur: Belleği bir fonksiyonda ayırıp başka bir yerde kullanabiliriz. Ancak bu esneklik, yaşam döngüsünü yönetme zorunluluğu getirir.

| Özellik | Stack | Heap |
|---|---|---|
| Tahsis yöntemi | Otomatik | Programcının isteğiyle |
| Yaşam süresi | Kapsam sonuna kadar | Serbest bırakılana kadar |
| Hız | Genellikle çok hızlı | Yönetim maliyeti daha yüksek |
| Tipik risk | Stack overflow | Leak, dangling pointer, fragmentation |

Bir programın heap tüketimini kabaca şöyle düşünebiliriz: $H(t) = A(t) - F(t)$; burada $A(t)$ toplam ayrılan, $F(t)$ ise toplam serbest bırakılan bellek miktarıdır. Program artık kullanmadığı verileri bırakmıyorsa $H(t)$ sürekli büyür. Bu durum **memory leak** olarak bilinir.

## C dünyası: `malloc` ve `free`

C’de `malloc`, istenen bayt sayısında ham bellek ayırır ve başlangıç adresini `void*` olarak döndürür. Tahsis başarısızsa sonuç `NULL` olur. Bu nedenle dönüş değeri mutlaka kontrol edilmelidir. `calloc` ise ayrıca alanı sıfırlarla başlatır; `realloc` mevcut bloğun boyutunu değiştirmeye çalışır.

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    size_t adet = 5;
    int *sayilar = malloc(adet * sizeof *sayilar);

    if (sayilar == NULL) {
        fprintf(stderr, "Bellek tahsisi basarisiz!\n");
        return 1;
    }

    for (size_t i = 0; i < adet; i++) {
        sayilar[i] = (int)(i * i);
        printf("%d ", sayilar[i]);
    }

    free(sayilar);
    sayilar = NULL;
    return 0;
}
```

Burada `sizeof *sayilar` yazımı, işaretçinin hedef türü değişirse boyut hesabının da doğru kalmasını sağlar. `free` sonrasında işaretçiye `NULL` atamak, yanlışlıkla tekrar kullanımı görünür kılar. Fakat `NULL` yapmak, başka kopyalanmış işaretçileri güvenli hâle getirmez.

## C++ dünyası: `new` ve `delete`

C++’ta `new`, belleği ayırmanın yanında nesnenin kurucusunu da çağırır; `delete` ise yıkıcıyı çalıştırıp alanı geri verir. Tek nesne ile dizi tahsisi için karşılık gelen silme işlemi farklıdır:

| Tahsis | Doğru iade | Hatalı eşleşme |
|---|---|---|
| `new T` | `delete ptr` | `delete[] ptr` |
| `new T[n]` | `delete[] ptr` | `delete ptr` |
| `malloc(...)` | `free(ptr)` | `delete ptr` |

```cpp
#include <iostream>

int main() {
    int* notlar = new int[3]{70, 85, 95};

    for (int i = 0; i < 3; ++i)
        std::cout << notlar[i] << ' ';

    delete[] notlar;
    notlar = nullptr;
}
```

`malloc/free` ile `new/delete` karıştırılmamalıdır. İlki kurucu-yıkıcı çağırmaz; ikincisi C++ nesne yaşam döngüsünü yönetir. Eşleşmeyen çiftler tanımsız davranışa, yani bazen çalışan ama en beklenmedik anda çöken kodlara davetiye çıkarır.

## Sızıntıya karşı modern yaklaşım: sahiplik

C++’ta ham işaretçiyle `new` kullanmak çoğu zaman son çaredir. **RAII** ilkesi, kaynağın nesneyle birlikte edinilip nesne yok edilirken otomatik bırakılmasını söyler. `std::vector` ve `std::unique_ptr` bu fikri uygular:

```cpp
#include <memory>

int main() {
    auto veri = std::make_unique<int[]>(100);
    veri[0] = 42;
} // unique_ptr kapsam bitince delete[] otomatik çağrılır
```

Bu yaklaşım özellikle erken `return`, istisna (`exception`) veya karmaşık kontrol akışlarında sızıntıları azaltır. C projelerinde ise her başarılı `malloc` için tek ve belirgin bir `free` yolu tasarlamak; C++ projelerinde de mümkün olduğunca standart kapları ve akıllı işaretçileri tercih etmek en sağlam savunmadır. Heap’i özgürce kullanın, ama her tahsisin dönüş biletini unutmayın.
