---
layout: post
title: "C++ Constructor ve Destructor: Nesnelerin Yaşam Döngüsünü Yönetmek"
math: true
categories: 
  - Bilgi
tags: 
  - C++
  - OOP
  - Constructor
  - Destructor
  - Bellek Yönetimi
---

C++'ta bir nesne yalnızca değişken tanımlandığında ortaya çıkan basit bir veri paketi değildir; doğar, kullanılır ve zamanı gelince yok olur. Bu yaşam döngüsünün iki başrol oyuncusu **yapıcı metotlar** (constructor) ile **yıkıcı metotlardır** (destructor). Constructor, nesne bellekte oluşturulurken başlangıç durumunu güvenle kurar; destructor ise nesne kapsam dışına çıkarken sahne arkasında kalan kaynakları toplar. Özellikle dosya, ağ bağlantısı, dinamik bellek ve kilit gibi kaynaklarda bu otomasyon, C++'ın en güçlü fikirlerinden biri olan RAII yaklaşımının temelidir.
``

Bir sınıftan nesne üretildiğinde, o nesnenin üyeleri için bellekte yer ayrılır ve ardından constructor çalışır. Constructor'ın adı sınıf adıyla aynıdır, dönüş tipi yoktur ve parametre alabilir. Amaç, nesneyi geçerli bir durumda başlatmaktır. Örneğin bir banka hesabının bakiyesi rastgele bir değerle değil, açıkça belirlenmiş bir başlangıç değeriyle yaşama başlamalıdır.

```cpp
#include <iostream>
#include <string>

class BankaHesabi {
private:
    std::string sahip;
    double bakiye;

public:
    BankaHesabi(const std::string& isim, double ilkBakiye)
        : sahip(isim), bakiye(ilkBakiye) {
        std::cout << sahip << " için hesap açıldı.\n";
    }

    void paraYatir(double miktar) {
        if (miktar > 0) bakiye += miktar;
    }

    ~BankaHesabi() {
        std::cout << sahip << " nesnesi kapatılıyor.\n";
    }
};
```

Buradaki `: sahip(isim), bakiye(ilkBakiye)` bölümü **üye başlatma listesi**dir. Atama işleminden daha doğrudan ve çoğu durumda daha verimlidir. Ayrıca `const` üyeler ve referans üyeler için tercih değil, zorunluluktur. Constructor çalıştıktan sonra nesnenin temel koşulu, yani **sınıf değişmezi** korunmuş olur. Örneğin bakiyenin negatif olmaması isteniyorsa bu kural daha ilk anda denetlenmelidir.

| Özellik | Constructor | Destructor |
|---|---|---|
| Çalışma zamanı | Nesne oluşturulurken | Nesne yok edilirken |
| Adlandırma | Sınıf adıyla aynı | Sınıf adı + `~` işareti |
| Parametre | Alabilir, aşırı yüklenebilir | Parametre almaz, tek tanedir |
| Temel görev | Geçerli başlangıç durumu kurmak | Kaynakları serbest bırakmak |
| Çağrılma biçimi | Genellikle otomatik | Genellikle otomatik |

Destructor'ın önemi, nesnenin sahip olduğu kaynağın türü arttıkça büyür. Sadece `int` gibi basit üyeler için özel destructor yazmak gerekmez; derleyici zaten yeterli temizliği üretir. Ancak sınıf `new` ile bellek ayırıyor, dosya açıyor veya bir sistem kaynağını kilitliyorsa, bu kaynak mutlaka bırakılmalıdır. Kapsamdan çıkış normal bir `return` ile de olsa, hata nedeniyle exception fırlatılmasıyla da olsa destructor çağrılır.

```cpp
#include <fstream>
#include <string>

class GunlukDosyasi {
private:
    std::ofstream dosya;

public:
    explicit GunlukDosyasi(const std::string& yol) : dosya(yol) {
        if (!dosya) throw std::runtime_error("Dosya açılamadı");
    }

    void yaz(const std::string& mesaj) {
        dosya << mesaj << '\n';
    }

    ~GunlukDosyasi() {
        // ofstream zaten kapanır; flush çağrısı niyeti görünür kılar.
        if (dosya.is_open()) dosya.flush();
    }
};
```

Bu desenin teorik adı **RAII**'dır: *Resource Acquisition Is Initialization*. Kaynağın edinilmesi constructor'a, bırakılması destructor'a bağlanır. Böylece kaynak ömrü nesne ömrüne eşitlenir. Bir nesnenin yaşadığı süreyi kabaca $t_{yaşam} = t_{yıkım} - t_{oluşum}$ ile ifade edersek, RAII'da kaynak için de $t_{kaynak} = t_{yaşam}$ hedeflenir. Manuel `delete` veya `close` çağrısını unutma riski ciddi biçimde azalır.

Dinamik bellek gerekiyorsa ham işaretçiler yerine `std::unique_ptr` ve `std::vector` gibi RAII uyumlu standart araçları tercih edin. Böylece çoğu zaman destructor yazmanız bile gerekmez: buna **Rule of Zero** denir. Kalıtım kullanılan sınıflarda ise taban sınıf işaretçisi üzerinden silme ihtimali varsa destructor `virtual` olmalıdır. Kısacası iyi bir constructor nesneyi güvenilir biçimde başlatır; iyi tasarlanmış bir destructor da ayrılırken arkasında bellek sızıntısı ve açık kaynak bırakmaz.
