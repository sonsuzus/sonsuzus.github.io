---
layout: post
title: "Değişkenler ve Bellek Yönetimi: Tipler Baytlara Dönüşürken"
math: true
categories: 
  - Bilgi
tags: 
  - statik tip sistemi
  - bellek yönetimi
  - değişkenler
---

Bir değişkeni yalnızca `x = 42` diye düşünmek, buzdağının görünen kısmına bakmaktır. Statik tipli dillerde değişken; adı, tipi, yaşam süresi ve bellekte temsil edilme biçimi olan bir sözleşmedir. Derleyici bu sözleşmeyi program çalışmadan önce denetler: `int` bekleyen yere metin, belirli aralıkta sayı bekleyen yere taşacak bir değer koymaya çalışırsanız alarm çalar. Bu katılık ilk anda sınırlayıcı görünse de bellek düzenini öngörülebilir, hataları erken yakalanabilir ve performansı daha hesaplanabilir yapar.
``

Statik tip sisteminin ana fikri şudur: Her ifadenin bir tipi vardır ve işlemler yalnızca uyumlu tipler arasında gerçekleşir. Örneğin `int32` ile `float64` aynı sayısal dünyada yaşasa da bit düzeyindeki anlamları farklıdır. Birincisi tam sayıyı ikinin tümleyeniyle, ikincisi yaklaşık reel sayıyı işaret, üs ve kesir alanlarıyla saklar. Bu nedenle tip dönüşümü sadece etiketi değiştirmek değildir; çoğu zaman bitlerin yeniden yorumlanması veya yeni bir temsile dönüştürülmesidir.

Bir veri türünün teorik kapasitesi, bit sayısıyla doğrudan ilişkilidir. İşaretsiz $n$ bitlik bir tamsayı için olası değer sayısı $2^n$ ve aralık $[0, 2^n-1]$ olur. İşaretli, ikinin tümleyeni kullanan bir tamsayıda ise aralık genellikle $[-2^{n-1}, 2^{n-1}-1]$ şeklindedir. Sekiz bitlik `uint8` bu yüzden 256 farklı değer taşır; 255'ten sonra ne olacağı ise dilin taşma kurallarına bağlıdır.

| Tür | Tipik boyut | Temsil yaklaşımı | Kritik sınır |
|---|---:|---|---|
| `bool` | 1 bayt* | Doğru/yanlış | Mantıksal değerler |
| `int32` | 4 bayt | İkinin tümleyeni | $-2^{31}$ ile $2^{31}-1$ |
| `uint8` | 1 bayt | İşaretsiz ikili sayı | 0 ile 255 |
| `float64` | 8 bayt | IEEE 754 kayan nokta | Hassasiyet ve yuvarlama |
| `char` | Dile bağlı | Karakter kodu | Kodlama standardı |

\*Donanım ve dil uygulamasına göre yerleşim değişebilir. Özellikle `bool`, yapılar içinde hizalama nedeniyle beklenenden fazla alan etkisi yaratabilir.

Bellek, byte byte adreslenen büyük bir dizi gibi düşünülebilir. Ancak işlemci bazı verilerin belirli adres sınırlarında başlamasını tercih eder; buna **hizalama** denir. Dört baytlık bir `int32` çoğunlukla 4'ün katı bir adreste, sekiz baytlık bir `float64` ise 8'in katında konumlanır. Yapıların içinde derleyicinin eklediği görünmez boşluklar, yani padding, bu yüzden ortaya çıkar. Küçük bir alan tasarrufu umarken bellekte fazladan baytlarla karşılaşmak oldukça klasik bir programcı sürprizidir.

```c
#include <stdint.h>

struct SensorA {
    uint8_t active;
    int32_t reading;
    uint16_t id;
};

struct SensorB {
    int32_t reading;
    uint16_t id;
    uint8_t active;
};
```

Bu C örneğinde iki yapı aynı mantıksal alanları taşır, fakat alan sırası bellek boyutunu değiştirebilir. `SensorA` içinde `active` sonrasında `int32_t` hizalamak için boşluk eklenebilir. `SensorB`, geniş alanları önce yerleştirerek padding'i azaltma şansına sahiptir. Kesin sonuç derleyiciye, mimariye ve ABI kurallarına bağlıdır; `sizeof` ile ölçmek en güvenli yoldur.

| Bellek bölgesi | Genellikle ne tutar? | Yaşam süresi |
|---|---|---|
| Stack (yığın) | Yerel değişkenler, çağrı bilgileri | Fonksiyon çağrısı boyunca |
| Heap (öbek) | Dinamik oluşturulan nesneler | Açıkça serbest bırakılana veya çöp toplanana kadar |
| Static/Data | Global ve statik veriler | Programın tamamı boyunca |

Statik tip, belleğin sahibini tek başına belirlemez. Örneğin Rust'ta tip sistemi sahiplik ve ödünç alma kurallarıyla bellek güvenliğine güçlü katkı sunar; C++'ta RAII nesnenin ömrünü kapsamla ilişkilendirir; Java ve C# ise çöp toplayıcıyla erişilemeyen heap nesnelerini geri kazanır. Buna karşılık C'de `malloc` ile alınan alanın `free` edilmesi programcının sorumluluğundadır.

Sonuçta değişken tanımı, derleyiciye verilmiş bir niyet beyanıdır: Kaç bayt gerektiğini, bitlerin nasıl yorumlanacağını ve hangi işlemlerin anlamlı olduğunu söyler. Tip sınırlarını, taşmayı, hizalamayı ve yaşam süresini anlayan geliştirici; hem daha güvenli kod yazar hem de “Neden bu yapı 12 değil 16 bayt?” sorusuna paniklemeden cevap verir.
