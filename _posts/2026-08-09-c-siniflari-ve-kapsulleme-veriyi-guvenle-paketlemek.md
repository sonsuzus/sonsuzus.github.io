---
layout: post
title: "C++ Sınıfları ve Kapsülleme: Veriyi Güvenle Paketlemek"
math: true
categories: 
  - Bilgi
tags: 
  - C++
  - Nesne Yönelimli Programlama
  - Sınıflar
  - Kapsülleme
---

C dilinde bir program büyüdükçe, birbirleriyle ilişkili verileri ve bu veriler üzerinde çalışan fonksiyonları takip etmek zorlaşabilir. Örneğin bir banka hesabının bakiye, hesap numarası ve para yatırma fonksiyonu farklı yerlerde durabilir. C++ sınıfları ise bu dağınıklığı toplar: Veri ile o veriyi yöneten davranışlar aynı güvenli kutuda yaşar. Bu yaklaşım, nesne yönelimli programlamanın temel taşlarından olan **kapsülleme**dir.

``

C tarafındaki `struct`, farklı alanları tek bir çatı altında gruplamak için harikadır; ancak üyeleri varsayılan olarak dışarıya açıktır. Herhangi bir kod parçası bakiyeyi doğrudan değiştirebilir. C++ içindeki `class` ise yalnızca veri grubu değil, aynı zamanda davranış tanımıdır. Sınıfın içindeki fonksiyonlara **üye fonksiyon** veya **metot** denir.

| Özellik | C `struct` yaklaşımı | C++ `class` yaklaşımı |
|---|---|---|
| Veri organizasyonu | Alanlar bir arada tutulur | Alanlar ve davranışlar bir aradadır |
| Varsayılan erişim | Genellikle açık kullanım | `class` için `private` |
| Doğrulama | Çağıran kodun sorumluluğu | Metotlar içinde merkezi doğrulama |
| Bakım | Kurallar birçok yere yayılabilir | Kurallar sınıf içinde toplanır |

Kapsüllemenin ana fikri şudur: Bir nesnenin iç durumu, her isteyen tarafından rastgele değiştirilememelidir. Matematiksel olarak bir hesabın bakiyesi için şu değişmezi korumak isteyelim:

$$bakiye \geq 0$$

Eğer `bakiye` alanı herkese açık olursa, birisi `bakiye = -500;` yazabilir. Oysa para çekme işlemini bir metot üzerinden geçirirsek, sınıf bu kuralı her çağrıda denetler. Böylece nesnenin **geçerli durumunu** korumak tek bir noktadan yönetilir.

Aşağıdaki örnek, bir `BankaHesabi` sınıfının temel hâlidir:

```cpp
#include <iostream>
#include <string>

class BankaHesabi {
private:
    std::string hesapSahibi;
    double bakiye;

public:
    BankaHesabi(const std::string& sahip, double ilkBakiye)
        : hesapSahibi(sahip), bakiye(ilkBakiye >= 0 ? ilkBakiye : 0) {}

    void paraYatir(double miktar) {
        if (miktar > 0) {
            bakiye += miktar;
        }
    }

    bool paraCek(double miktar) {
        if (miktar > 0 && miktar <= bakiye) {
            bakiye -= miktar;
            return true;
        }
        return false;
    }

    double bakiyeGetir() const {
        return bakiye;
    }
};

int main() {
    BankaHesabi hesap("Ada", 1000);
    hesap.paraYatir(250);

    if (!hesap.paraCek(2000)) {
        std::cout << "Yetersiz bakiye!\n";
    }

    std::cout << hesap.bakiyeGetir() << " TL\n";
}
```

Burada `private` altındaki `hesapSahibi` ve `bakiye`, sınıfın dışından erişilemez. Yani `hesap.bakiye = -10;` derleme hatası üretir. `public` bölümündeki metotlar ise sınıfın kontrollü arayüzüdür. Kullanıcı bakiyeyi okuyabilir veya değiştirmeyi talep edebilir; fakat kuralları sınıf belirler.

`const` anahtar sözcüğü de küçük ama güçlü bir sözleşmedir. `bakiyeGetir() const`, bu metodun nesnenin durumunu değiştirmeyeceğini söyler. Derleyici bu sözü denetler; böylece salt-okunur metotlara yanlışlıkla değişiklik eklemek zorlaşır.

| Erişim belirleyicisi | Kim erişebilir? | Tipik kullanım |
|---|---|---|
| `public` | Sınıfın dışındaki herkes | Kullanıcıya sunulan metotlar |
| `private` | Yalnızca sınıfın kendi metotları | İç veri ve yardımcı ayrıntılar |
| `protected` | Sınıf ve türetilmiş sınıflar | Kalıtım senaryoları |

İyi tasarlanmış bir sınıf, kullanıcıya “nasıl sakladığımı düşünme, ne yapabildiğimi kullan” der. Bugün bakiye `double` ile tutulabilir; yarın hassas para işlemleri için kuruş cinsinden `long long` kullanılabilir. Arayüz aynı kaldığı sürece sınıfı kullanan kodların çoğu etkilenmez. İşte kapsülleme, yalnızca erişim engeli değil; değişime dayanıklı, kuralları net ve daha güvenilir yazılım tasarlama sanatıdır.
