---
layout: post
title: "Diziler ve Demetler: Bellekte Düzen, Hız ve Esneklik"
math: true
categories: 
  - Bilgi
tags: 
  - arrays
  - tuples
  - bellek yönetimi
---

Bir alışveriş sepetinde aynı türden ürünleri yan yana dizmek kolaydır; fakat ürünün adı, fiyatı ve stok durumu gibi farklı bilgileri tek paket hâlinde taşımak başka bir düzen gerektirir. Programlamada dinamik diziler aynı türdeki elemanları büyüyebilen bir koleksiyonda saklarken demetler, farklı türdeki belirli sayıda değeri sıralı bir bütün olarak tutar. Aralarındaki asıl fark yalnızca sözdiziminde değil, belleğin nasıl ayrıldığı ve veriye nasıl erişildiğindedir.

``

## Dinamik dizilerin bellek düzeni

Klasik bir dizi, aynı veri türündeki elemanları çoğunlukla bellekte **ardışık** olarak saklar. İlk elemanın adresi $A$, her elemanın boyutu $s$ ise $i$ indisli elemanın adresi yaklaşık olarak şöyle hesaplanır:

$$Adres(i) = A + i \times s$$

Bu basit formül sayesinde indisle erişim $O(1)$ zaman karmaşıklığına sahiptir. İşlemci önbelleği de komşu elemanları birlikte getirebildiği için diziler üzerinde sırayla dolaşmak oldukça hızlıdır.

Dinamik diziler ise çalışma sırasında büyüyebilir. C++ dilindeki `std::vector`, bunun yaygın bir örneğidir. Vector genellikle üç bilgiyi yönetir: veri bloğunun adresi, mevcut eleman sayısı ve ayrılmış kapasite.

```cpp
#include <iostream>
#include <vector>

int main() {
    std::vector<int> puanlar;
    puanlar.reserve(4); // Dört elemanlık belleği önceden ayırır.

    puanlar.push_back(70);
    puanlar.push_back(85);
    puanlar.push_back(92);

    std::cout << "Boyut: " << puanlar.size() << '\n';
    std::cout << "Kapasite: " << puanlar.capacity() << '\n';
}
```

`size`, gerçekten bulunan eleman sayısını; `capacity` ise yeniden bellek ayırmadan saklanabilecek eleman sayısını gösterir. Kapasite dolduğunda daha büyük bir blok ayrılır, eski elemanlar yeni alana taşınır ve eski blok serbest bırakılır. Bu işlem tek seferde $O(n)$ maliyetlidir. Ancak kapasite geometrik olarak büyütüldüğünden `push_back` işleminin amortize maliyeti $O(1)$ kabul edilir.

## Demetler neden farklıdır?

Demet, farklı türdeki değerleri belirli bir sırada ve sabit sayıda tutar. Örneğin bir öğrenciyi kimlik numarası, isim ve not ile temsil edebiliriz:

```cpp
#include <iostream>
#include <string>
#include <tuple>

int main() {
    std::tuple<int, std::string, double> ogrenci{42, "Ada", 91.5};

    auto& [numara, ad, notu] = ogrenci;
    std::cout << numara << " - " << ad << " - " << notu;
}
```

Buradaki elemanların türleri derleme zamanında bellidir ve sonradan dördüncü bir alan eklenemez. Yapısal bağlama, indis yerine anlamlı değişken adlarıyla çalışmayı kolaylaştırır. Bununla birlikte `std::tuple` elemanlarının fiziksel sıralaması ve yerleşimi uygulamaya bağlı olabilir; ardışık bir ham dizi gibi yorumlanmamalıdır.

Farklı türlerin hizalama gereksinimleri nedeniyle demet içinde **padding** adı verilen kullanılmayan baytlar oluşabilir. Yaklaşık toplam boyut şu düşünceyle modellenebilir:

$$Toplam\ Boyut \geq \sum_{k=1}^{n} sizeof(T_k)$$

Eşitsizliğin nedeni hizalama boşlukları ve kütüphane uygulamasının tercih ettiği yerleşimdir.

| Özellik | Dinamik dizi | Demet |
|---|---|---|
| Eleman türleri | Genellikle aynı | Farklı olabilir |
| Eleman sayısı | Çalışma zamanında değişebilir | Derleme zamanında sabittir |
| Bellek | Ayrı, ardışık veri bloğu | Nesnenin kendi yerleşimi |
| Erişim | Çalışma zamanı indisi | Derleme zamanı konumu |
| Büyüme maliyeti | Yeniden ayırma ve taşıma | Büyüme desteklenmez |
| Kullanım amacı | Liste ve koleksiyon | Sabit yapılı kayıt veya dönüş değeri |

## Hangisini seçmeliyiz?

Aynı türden, sayısı değişebilen verileri işleyecekseniz dinamik dizi doğal seçimdir. Sensör ölçümleri, puan listeleri ve oyun nesneleri buna örnektir. Bir fonksiyondan farklı türde birkaç değeri birlikte döndürmek veya küçük, sabit bir kayıt oluşturmak istiyorsanız demet daha uygundur.

Yine de alanların özel anlamları varsa `tuple` yerine adlandırılmış bir `struct` kullanmak okunabilirliği artırır. Kısacası dizi, büyüyebilen düzenli bir raf; demet ise bölmeleri önceden belirlenmiş bir araç çantasıdır. Doğru seçim, hem bellek davranışını hem de kodun anlaşılabilirliğini doğrudan etkiler.
