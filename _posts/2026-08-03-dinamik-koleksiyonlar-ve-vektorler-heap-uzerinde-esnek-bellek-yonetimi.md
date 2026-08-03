---
layout: post
title: "Dinamik Koleksiyonlar ve Vektörler: Heap Üzerinde Esnek Bellek Yönetimi"
math: true
categories: 
  - Bilgi
tags: 
  - veri yapıları
  - bellek yönetimi
  - C++ vector
---

Sabit boyutlu bir dizi, kaç misafir geleceğini aylar öncesinden bilerek masa hazırlamaya benzer. Dinamik koleksiyon ise kapı çaldıkça masaya yeni sandalye ekler; gerektiğinde sandalyeleri kaldırır. Vektörler bu esnekliği sunarken arka planda heap belleği, kapasite hesaplarını ve eleman taşıma işlemlerini yönetir.

``

## Sabit Dizi ile Dinamik Vektör Arasındaki Fark

Sabit bir dizinin boyutu oluşturulurken belirlenir ve sonradan değiştirilemez. Daha fazla elemana ihtiyaç duyulursa daha büyük bir alan ayırmak, eski elemanları kopyalamak ve önceki alanı serbest bırakmak gerekir. Vektör bütün bu işleri otomatikleştiren bir soyutlamadır.

| Özellik | Sabit boyutlu dizi | Dinamik vektör |
|---|---|---|
| Boyut | Başlangıçta belirlenir | Çalışma zamanında değişir |
| Bellek | Stack veya heap olabilir | Eleman deposu genellikle heap üzerindedir |
| Ekleme | Boş yer yoksa mümkün değildir | Kapasite artırılarak yapılabilir |
| Yönetim | Çoğunlukla geliştiriciye aittir | Koleksiyon sınıfı tarafından gerçekleştirilir |
| Erişim | İndeksle hızlıdır | İndeksle hızlıdır |

Vektör nesnesinin kendisi stack üzerinde bulunabilir; ancak elemanların tutulduğu büyük ve bitişik bellek bloğu heap üzerinde ayrılır. Nesne genellikle üç önemli bilgi taşır: veri bloğunun adresi, mevcut eleman sayısı ve ayrılmış toplam kapasite.

## Boyut ve Kapasite Aynı Şey Değildir

Vektörün **size** değeri gerçekten kullanılan eleman sayısını, **capacity** değeri ise yeniden bellek ayırmadan saklayabileceği eleman sayısını gösterir. Her eklemede bellek istemek pahalı olacağı için kapasite çoğunlukla ihtiyaçtan büyük tutulur.

$$0 \leq size \leq capacity$$

Kapasite dolduğunda daha büyük bir blok ayrılır. Yaygın büyüme stratejilerinden biri kapasiteyi yaklaşık iki katına çıkarmaktır:

$$C_{yeni} = 2C_{eski}$$

Ardından mevcut elemanlar yeni alana kopyalanır veya taşınır, eski heap bloğu serbest bırakılır ve yeni eleman eklenir. Bu yeniden yerleştirme tek seferde $O(n)$ maliyetli olsa da her eklemede gerçekleşmez. Bu nedenle sona ekleme işleminin amortize edilmiş zaman karmaşıklığı $O(1)$ kabul edilir.

## C++ ile Vektörü Gözlemlemek

Aşağıdaki örnek, eleman eklendikçe boyut ve kapasitenin nasıl değiştiğini gösterir:

```cpp
#include <iostream>
#include <vector>

int main() {
    std::vector<int> sayilar;

    for (int i = 1; i <= 10; ++i) {
        sayilar.push_back(i * 10);
        std::cout << "Boyut: " << sayilar.size()
                  << ", Kapasite: " << sayilar.capacity()
                  << '\n';
    }
}
```

`push_back`, elemanı sona ekler. Kapasite yeterliyse işlem doğrudan yapılır. Yeterli değilse yeni heap alanı ayrılır ve elemanlar taşınır. Kapasitenin büyüme oranı C++ standardında kesin olarak belirtilmediğinden sonuç kullanılan kütüphane uygulamasına göre değişebilir.

## Önceden Yer Ayırmak

Kaç eleman ekleneceği yaklaşık olarak biliniyorsa `reserve` kullanmak gereksiz yeniden ayırmaları önler:

```cpp
std::vector<int> puanlar;
puanlar.reserve(1000); // En az 1000 elemanlık kapasite hazırlar.

for (int i = 0; i < 1000; ++i) {
    puanlar.push_back(i);
}
```

`reserve`, vektörün boyutunu değiştirmez; yalnızca kapasite ayırır. Buna karşılık `resize`, eleman sayısını değiştirir ve gerekirse yeni elemanlar oluşturur.

| İşlem | Boyutu değiştirir mi? | Kapasiteyi değiştirebilir mi? |
|---|---:|---:|
| `reserve(n)` | Hayır | Evet |
| `resize(n)` | Evet | Evet |
| `clear()` | Evet | Genellikle hayır |
| `shrink_to_fit()` | Hayır | Azaltmayı deneyebilir |

## Dikkat: İşaretçiler Geçersizleşebilir

Yeniden bellek ayırma gerçekleştiğinde eski bloğu gösteren işaretçiler, referanslar ve iterator’lar geçersiz hale gelebilir. Artık tahliye edilmiş bir evin adresine kargo göndermek gibi düşünün: adres tanıdık görünür, fakat içeride kimse yoktur.

Vektörler hız, bitişik bellek düzeni ve esneklik arasında güçlü bir denge kurar. Yine de bu rahatlığın arkasında kapasite fazlası, taşıma maliyeti ve referans geçersizleşmesi bulunur. `size`, `capacity`, `reserve` ve yeniden ayırma mantığını bilmek, dinamik koleksiyonları yalnızca kullanmayı değil, verimli ve güvenli kullanmayı sağlar.
