---
layout: post
title: "C++ Şablonları ve Jenerik Programlama: Tek Algoritma, Birçok Tür"
math: true
categories: 
  - Bilgi
tags: 
  - C++
  - Templates
  - Jenerik Programlama
---

C++'ta aynı algoritmayı `int`, `double`, `std::string` ya da kendi sınıflarımız için tekrar tekrar yazmak, kodun bakım maliyetini hızla artırır. Şablonlar (templates), algoritmayı türden ayırarak bu sorunu çözer: Bir kez kuralları tanımlar, tür seçimini derleyiciye bırakırsınız. Sonuç, çalışma anında tür kontrolü yapan yapılardan farklı olarak, derleme anında üretilen hızlı ve tür güvenli koddur.
``

Jenerik programlamanın temel fikri şudur: Algoritma, belirli bir sınıf adına değil, ihtiyaç duyduğu **davranışlara** bağımlı olmalıdır. Örneğin bir sıralama algoritması, elemanların `int` olmasını istemez; yalnızca karşılaştırılabilir olmalarını ister. Bu yaklaşımın basit maliyet modeli şöyle özetlenebilir:

$$T(n) = T_{algoritma}(n) + T_{tür\,işlemleri}$$

Şablon kullanmak algoritmanın asimptotik karmaşıklığını değiştirmez. Örneğin sıralama hâlâ çoğu durumda $O(n \log n)$'dir. Ancak derleyici türü bildiği için çağrıları satır içine alma (inlining) ve özel optimizasyonlar yapabilir.

## Fonksiyon şablonu: Türü derleyici bulsun

En tanıdık örnek, iki değerden büyüğünü döndüren bir fonksiyon şablonudur:

```cpp
#include <iostream>
#include <string>

template <typename T>
const T& maksimum(const T& a, const T& b) {
    return (a > b) ? a : b;
}

int main() {
    std::cout << maksimum(12, 8) << "\n";
    std::cout << maksimum(3.14, 6.28) << "\n";
    std::cout << maksimum(std::string{"Ada"}, std::string{"Zeynep"});
}
```

`typename T` yerine `class T` da yazılabilir; bu bağlamda anlamları aynıdır. Derleyici ilk çağrıda `T = int`, ikinci çağrıda `T = double` ve son çağrıda `T = std::string` olacak şekilde gerekli sürümleri üretir. Fakat burada görünmez bir sözleşme vardır: `T` için `>` operatörü tanımlı olmalıdır. Jenerik kodun gücü kadar sorumluluğu da bu sözleşmeleri doğru kurmaktır.

| Yaklaşım | Tür kontrolü | Performans maliyeti | Yeni tür ekleme |
|---|---|---|---|
| Fonksiyon aşırı yükleme | Derleme anı | Düşük | Her tür için kod gerekir |
| Sanal fonksiyon/polimorfizm | Çalışma anı | Dolaylı çağrı olabilir | Ortak taban sınıf ister |
| Template | Derleme anı | Genellikle sıfır ek maliyet | Uygun işlemleri sağlayan tür yeterlidir |

## Sınıf şablonları ve tür parametreleri

Şablonlar yalnızca fonksiyonlar için değildir. Aşağıdaki `Kutu`, içinde hangi değer saklanacağını kullanıcıya bırakır:

```cpp
#include <utility>

template <typename T>
class Kutu {
public:
    explicit Kutu(T deger) : deger_(std::move(deger)) {}

    const T& al() const { return deger_; }
    void ayarla(T yeniDeger) { deger_ = std::move(yeniDeger); }

private:
    T deger_;
};
```

`Kutu<int>` ve `Kutu<std::string>` birbirinden farklı türlerdir. Bu önemli ayrım, yanlış türde atamaları daha program çalışmadan yakalar. Ayrıca modern C++'ta şablon parametreleri yalnızca tür olmak zorunda değildir: `std::array<int, 10>` örneğindeki `10`, derleme zamanı değer parametresidir.

## Kısıtlar: Her T gerçekten uygun mu?

Eski C++ tarzında hatalar, şablonun gövdesi örneklendiğinde uzun derleyici mesajlarıyla ortaya çıkabilirdi. C++20 `concept` yapısı, beklentiyi açıkça ifade eder:

```cpp
#include <concepts>

template <std::totally_ordered T>
const T& maksimumGuvenli(const T& a, const T& b) {
    return a > b ? a : b;
}
```

Buradaki `std::totally_ordered`, türün anlamlı karşılaştırma işlemlerine sahip olmasını ister. Böylece hata mesajı “`>` bulunamadı” ayrıntısına boğulmak yerine, fonksiyonun beklediği kavramı anlatır.

Şablonları kullanırken iki dengeyi koruyun: Arayüzü mümkün olduğunca genel tutun, ancak belirsiz davranışa izin verecek kadar da gevşetmeyin. Standart kütüphanedeki `std::vector`, `std::sort` ve `std::optional` bu felsefenin güçlü örnekleridir. İyi tasarlanmış jenerik kod, türleri değil yetenekleri hedefler; C++ derleyicisi de bu soyut fikri somut, hızlı makine koduna dönüştürür.
