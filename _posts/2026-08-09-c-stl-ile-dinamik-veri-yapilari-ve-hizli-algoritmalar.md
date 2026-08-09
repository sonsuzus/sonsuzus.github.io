---
layout: post
title: "C++ STL ile Dinamik Veri Yapıları ve Hızlı Algoritmalar"
math: true
categories: 
  - Bilgi
tags: 
  - C++
  - STL
  - Veri Yapıları
  - Algoritmalar
  - Performans
---

C++ Standart Şablon Kütüphanesi, yani STL (Standard Template Library), tekerleği yeniden icat etmek yerine güvenilir parçalarla hızlı yazılım üretmenin yoludur. Dinamik diziler, bağlı listeler, yığınlar ve hazır algoritmalar sayesinde hem kod miktarı azalır hem de yıllardır test edilmiş uygulamalardan yararlanılır. Asıl güç, veri yapısını doğru probleme; algoritmayı da doğru veri düzenine eşleştirmekte yatar.

<!--more-->

STL üç ana fikrin birleşimidir: **container** (veriyi tutar), **iterator** (veri üzerinde dolaşır) ve **algorithm** (veriye işlem uygular). Bu ayrım oldukça değerlidir: `std::sort`, hangi sınıftan geldiğini umursamadan rastgele erişim sunan bir aralık üzerinde çalışır. Böylece veri ile işlem birbirine sıkı sıkıya bağlanmaz.

En sık kullanılan container'lar aşağıdaki gibi karşılaştırılabilir:

| Yapı | Güçlü yanı | Zayıf yanı | Tipik kullanım |
|---|---|---|---|
| `std::vector` | Sonda ekleme ve indeksle erişim çok hızlıdır | Ortaya ekleme/kaldırma maliyetlidir | Dinamik dizi, sonuç listesi |
| `std::list` | Bilinen konuma ekleme ve silme hızlıdır | İndeksle erişim yoktur; önbellek dostu değildir | Sık düğüm silinen zincirler |
| `std::deque` | Başta ve sonda ekleme hızlıdır | Bellek düzeni `vector` kadar sade değildir | Çift uçlu kuyruk |
| `std::stack` | LIFO işlemlerini sadeleştirir | Sadece üst elemana erişilir | Geri alma, parantez kontrolü |

Bir `vector` fiziksel olarak çoğunlukla bitişik bellekte yaşar. Bu nedenle `v[i]` erişimi $O(1)$ zamanlıdır ve işlemci önbelleğinden iyi yararlanır. Sona ekleme (`push_back`) normalde $O(1)$, kapasite dolduğunda ise yeni alan ayırma nedeniyle $O(n)$ maliyetli olabilir. Buna rağmen büyümenin seyrek gerçekleşmesi sebebiyle amortize maliyet şöyledir:

$$T_{amortize}(push\_back)=O(1)$$

Aşağıdaki örnek, sayıları sıralar, tekrarları temizler ve ikili arama yapar. Buradaki kritik nokta, `binary_search` fonksiyonunun doğru sonuç vermesi için aralığın önceden sıralı olmasıdır.

```cpp
#include <algorithm>
#include <iostream>
#include <vector>

int main() {
    std::vector<int> puanlar{42, 17, 42, 99, 8, 17};

    std::sort(puanlar.begin(), puanlar.end());
    auto yeniSon = std::unique(puanlar.begin(), puanlar.end());
    puanlar.erase(yeniSon, puanlar.end());

    int aranan = 42;
    bool bulundu = std::binary_search(
        puanlar.begin(), puanlar.end(), aranan);

    std::cout << (bulundu ? "Puan bulundu" : "Puan yok") << '\n';
}
```

`unique` doğrudan eleman silmez; tekrar edenleri sona taşıyıp yeni mantıksal sonu döndürür. Bu yüzden silme işlemi için `erase` ile birlikte kullanılır. Bu kalıp, STL öğrenirken önemli olan iterator mantığını da gösterir.

Algoritma seçimi performansı dramatik biçimde değiştirir:

| İşlem | Yaklaşım | Zaman karmaşıklığı |
|---|---|---|
| Sıralama | `std::sort` | $O(n \log n)$ |
| Sıralı dizide arama | `std::binary_search` | $O(\log n)$ |
| Sırasız dizide arama | `std::find` | $O(n)$ |
| Yığının üstüne ekleme/çıkarma | `push` / `pop` | $O(1)$ |

Örneğin 1 milyon eleman içinde doğrusal arama en kötü durumda yaklaşık $10^6$ karşılaştırma isterken, ikili arama yaklaşık $\log_2(10^6) \approx 20$ adımda sonuca ulaşabilir. Elbette sıralamanın da bir bedeli vardır; veri yalnızca bir kez aranacaksa `sort` her zaman kazanç sağlamaz. Çok sayıda sorgu yapılacaksa ise sıralama maliyeti kısa sürede kendini öder.

Pratik kural basittir: İndeksleme ve yoğun dolaşma için önce `vector` düşünün; yalnızca gerçekten gerekli olduğunda `list` seçin. LIFO davranışı için `stack`, iki uçtan işlem için `deque` kullanın. Ardından el yazımı döngülere geçmeden `sort`, `find`, `count`, `transform` ve `lower_bound` gibi algoritmaları inceleyin. STL, yalnızca daha kısa kod değil; karmaşıklığı görünür, niyeti açık ve bakımı kolay C++ kodu demektir.
