---
layout: post
title: "Sistem Programlama Felsefesi: C’nin Çıplak Gerçekliği ve C++’ın Mimari Gücü"
math: true
categories: 
  - Bilgi
tags: 
  - C
  - C++
  - Sistem Programlama
---

Sistem programlama, bilgisayarın yalnızca ne yaptığını değil, bunu **hangi maliyetle** yaptığını da önemser. Bellek adresleri, işlemci önbelleği, kesmeler, dosya tanıtıcıları ve eşzamanlılık burada günlük araçlardır. C ile C++ arasındaki seçim de basitçe “eski mi yeni mi?” sorusu değildir: C doğrudanlık ve evrensel uyumluluk sunarken, C++ aynı donanım düzeyinde daha sağlam soyutlamalar kurmayı hedefler.
``
## Temel ayrım: kontrol mü, ifade gücü mü?

C, işletim sistemi arayüzlerinin doğal dilidir. Linux çekirdeğinin C ile yazılması tesadüf değildir: dilin çalışma zamanı yükü çok küçüktür, bellek düzeni öngörülebilirdir ve üretilen makine koduna yaklaşmak kolaydır. Bir `struct`, bellekteki verinin açık bir tarifidir; bir işaretçi ise doğrudan adresle konuşur.

C++ ise C’nin düşük seviyeli alanını terk etmeden, kaynak yönetimi ve büyük ölçekli tasarım için araçlar ekler. Sınıflar, şablonlar, RAII ve tür güvenliği doğru kullanıldığında “sıfır maliyetli soyutlama” hedefler. İdeal durumda kullanılmayan özelliğin bedeli yoktur; kullanılan soyutlama da elle yazılmış C koduna yakın maliyet üretir.

Bu yaklaşım kabaca şöyle modellenebilir:

$$T_{toplam} = T_{hesaplama} + T_{bellek} + T_{senkronizasyon} + T_{soyutlama}$$

C’de geliştirici son terimi elle azaltır. C++’ta ise iyi tasarlanmış bir soyutlama ile $T_{soyutlama} \approx 0$ olmaya çalışır. Ancak sanal fonksiyonlar, kontrolsüz dinamik tahsis ve istisnalar bazı senaryolarda bu maliyeti görünür hâle getirebilir.

| Başlık | C | C++ |
|---|---|---|
| Kaynak yönetimi | `malloc/free` disiplini | RAII, akıllı işaretçiler |
| Soyutlama | Fonksiyonlar ve `struct` | Sınıflar, şablonlar, kavramlar |
| ABI ve uyumluluk | Çok kararlı, C API’leri yaygın | Ad karmaşası ve ABI ayrıntıları daha karmaşık |
| Hata modeli | Hata kodları, `errno` | Hata kodları veya istisnalar |
| Tipik alan | Çekirdek, sürücü, gömülü sistem | Oyun motoru, tarayıcı, yüksek performanslı servis |

## C: donanımla pazarlıksız konuşmak

Bir sürücü, önyükleyici veya mikrodenetleyici kodunda başlangıç maliyeti, ikili boyut ve davranışın kesinliği kritiktir. C burada güçlüdür. Aşağıdaki örnek, bir bellek eşlemeli yazmacı temsil eder:

```c
#include <stdint.h>

#define GPIO_OUT (*(volatile uint32_t *)0x40020014u)

void led_yak(void) {
    GPIO_OUT |= (1u << 5);
}
```

`volatile`, derleyiciye bu belleğin donanım tarafından değişebileceğini söyler; bu yüzden okuma veya yazma işlemini “gereksiz” diye silemez. Bu kodun etkisi nettir: belirli adresteki yazmacın beşinci biti etkinleşir. Fakat bu güç sorumluluk getirir: yanlış adres, taşan dizi veya unutulan `free`, doğrudan hata üretir.

## C++: kaynakları nesne ömrüne bağlamak

İşletim sistemi seviyesinde her şey sınıf olmak zorunda değildir. Fakat dosya tanıtıcısı, kilit veya soket gibi **sahipliği olan kaynaklar**, C++ için çok uygundur. RAII’nin fikri basittir: kaynak kurucuda alınır, nesne yok edilirken bırakılır.

```cpp
#include <unistd.h>
#include <stdexcept>

class DosyaTanıtıcısı {
    int fd_ = -1;
public:
    explicit DosyaTanıtıcısı(int fd) : fd_(fd) {
        if (fd_ < 0) throw std::runtime_error("dosya acilamadi");
    }
    ~DosyaTanıtıcısı() { if (fd_ >= 0) close(fd_); }
    DosyaTanıtıcısı(const DosyaTanıtıcısı&) = delete;
};
```

Bu sınıfın amacı dosya okumak değil, `close` çağrısının unutulmasını zorlaştırmaktır. Kopyalamayı kapatması da aynı tanıtıcının iki kez kapatılmasını önler. Gerçek zamanlı veya çekirdek kodunda istisnalar tercih edilmeyebilir; yine de RAII, istisnasız bir C++ tarzında da değerlidir.

## Karar rehberi

| Senaryo | Daha doğal tercih | Gerekçe |
|---|---|---|
| Çekirdek modülü, bootloader | C | Küçük çalışma zamanı ve yerleşik ekosistem |
| Donanım sürücüsü | C, bazen kısıtlı C++ | Kesin kontrol ve platform kuralları |
| Yüksek performanslı ağ sunucusu | C++ | RAII, şablonlar ve güçlü tür modeli |
| C ile sunulan kütüphane API’si | C arayüzü | Farklı dillerle kolay bağlanabilirlik |
| Büyük motor veya altyapı | C++ | Karmaşıklığı modüllere ayırma avantajı |

Sonuçta C “her ayrıntıyı ben yönetirim” felsefesidir; C++ ise “ayrıntıyı yönetirim, ama tekrar eden hataları dile devrederim” yaklaşımıdır. İyi sistem yazılımı dil savaşından değil, gecikme bütçesi, hata toleransı, ekip deneyimi ve hedef platformun gerçeklerinden doğar.
