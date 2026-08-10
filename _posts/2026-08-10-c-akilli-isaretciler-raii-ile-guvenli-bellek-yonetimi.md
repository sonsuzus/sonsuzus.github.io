---
layout: post
title: "C++ Akıllı İşaretçiler: RAII ile Güvenli Bellek Yönetimi"
math: true
categories: 
  - Bilgi
tags: 
  - C++
  - Smart Pointers
  - RAII
---

C++’ta `new` ile bellek ayırmak kolay, onu her yürütme yolunda doğru zamanda `delete` etmek ise şaşırtıcı derecede zordur. Erken `return`, fırlatılan bir istisna veya sahipliği belirsiz bir işaretçi; bellek sızıntısı, çift silme ve geçersiz belleğe erişim gibi klasik hatalara davetiye çıkarır. Modern C++’ın cevabı akıllı işaretçilerdir: Kaynağın ömrünü nesnenin ömrüne bağlayan, RAII tabanlı küçük ama güçlü sınıflar.
``

## Sorunun kökü: sahiplik

Ham işaretçi (`T*`) bir adres taşır; fakat bu adresin **kime ait olduğunu** söylemez. İşaretçi nesneyi mi yönetiyor, yalnızca ödünç mü alıyor, yoksa başka bir yerde silinmiş mi? Bu belirsizlik, özellikle büyük kod tabanlarında maliyetlidir.

RAII (Resource Acquisition Is Initialization) yaklaşımında kaynak edinimi kurucuda, bırakılması ise yıkıcıda gerçekleşir. Bir nesne kapsam dışına çıktığında yıkıcısı otomatik çağrılır. Böylece kaynak ömrü deterministik olur:

$$\text{Kaynak ömrü} = \text{RAII nesnesinin kapsam ömrü}$$

İstisna fırlatılsa bile C++ kapsam temizliği yapar. Akıllı işaretçi de sahip olduğu nesne için uygun zamanda `delete` çağıran bir RAII sarmalayıcısıdır. Bu, çöp toplayıcı değildir: temizlik zamanı tahmin edilebilir ve çoğunlukla ek çalışma zamanı maliyeti yoktur.

| Araç | Sahiplik modeli | Kopyalanabilir mi? | Tipik kullanım |
|---|---|---:|---|
| `T*` | Belirsiz / gözlemci | Evet | Sahip olmayan erişim |
| `std::unique_ptr<T>` | Tek sahip | Hayır, taşınabilir | Varsayılan sahiplik tercihi |
| `std::shared_ptr<T>` | Ortak sahiplik | Evet | Gerçekten paylaşılan yaşam süresi |
| `std::weak_ptr<T>` | Sahip olmayan zayıf referans | Evet | Döngü kırma, güvenli gözlem |

## `unique_ptr`: tek kaptan, sıfır drama

`std::unique_ptr`, bir nesnenin yalnızca bir sahibi olmasını garanti eder. Kopyalama yasaktır; sahiplik `std::move` ile açıkça devredilir. Bu kural, “Bu nesneyi kim silecek?” sorusunu derleme zamanında cevaplar. Nesne, `unique_ptr` yok edildiğinde otomatik silinir.

```cpp
#include <memory>
#include <string>

class Dosya {
public:
    explicit Dosya(std::string ad) : ad_(std::move(ad)) {}
    void yaz() const { /* dosyaya veri yaz */ }
private:
    std::string ad_;
};

std::unique_ptr<Dosya> dosyaAc() {
    auto dosya = std::make_unique<Dosya>("rapor.txt");
    dosya->yaz();
    return dosya; // sahiplik taşınır; kopyalama yoktur
}
```

`make_unique`, C++14 ile geldi ve `new` yazma ihtiyacını büyük ölçüde kaldırdı. İstisna güvenliği açısından da üstündür: nesne oluşturma ve sahipliğe alma tek ifadede tamamlanır. Diziler için `std::make_unique<int[]>(10)` kullanılabilir; ancak çoğu durumda boyut bilgisini de taşıdığı için `std::vector` daha anlamlıdır.

## `shared_ptr`: paylaşım gerekli olduğunda

`std::shared_ptr`, aynı nesnenin birden fazla sahibi olduğunda kullanılır. Bir kontrol bloğu referans sayısını tutar. Sahip sayısı $n$ iken nesne yaşar; $n = 0$ olduğunda silinir. Kopyalama sayacı artırır, yok etme ise azaltır:

$$n_{yeni} = n_{eski} + 1 \quad \text{veya} \quad n_{yeni} = n_{eski} - 1$$

```cpp
#include <memory>
#include <iostream>

struct Oturum {
    void baglan() { std::cout << "Baglandi\n"; }
};

void kullan(std::shared_ptr<Oturum> oturum) {
    oturum->baglan(); // fonksiyon boyunca ortak sahiplik sürer
}

int main() {
    auto oturum = std::make_shared<Oturum>();
    kullan(oturum);
} // son shared_ptr burada yok olursa Oturum temizlenir
```

Ancak `shared_ptr`, varsayılan seçim olmamalıdır. Kontrol bloğu, atomik sayaç işlemleri ve belirsiz sahiplik mimari maliyet yaratabilir. Daha önemlisi, iki nesne birbirini `shared_ptr` ile tutarsa sayaçlar sıfıra inmez: döngüsel sızıntı oluşur. Bu senaryoda bir yön `weak_ptr` olmalıdır.

| Durum | Doğru tercih | Neden |
|---|---|---|
| Nesnenin tek, açık sahibi var | `unique_ptr` | Basit ve düşük maliyetli |
| Birden çok bileşen yaşam süresini paylaşır | `shared_ptr` | Ortak sahiplik modeli |
| Nesneyi yalnızca gözlemliyorsunuz | `T*` veya `T&` | Sahiplik iddiası yok |
| Geri referans / ebeveyn bağlantısı | `weak_ptr` | Döngüsel sahipliği önler |

Özet kural nettir: Önce `unique_ptr` düşünün, zorunlu ortak sahiplik varsa `shared_ptr` seçin ve ham `new`/`delete` ikilisini uygulama kodundan uzak tutun. Akıllı işaretçiler yalnızca belleği temizlemez; sahiplik niyetini kodun bir parçası hâline getirerek hataları daha oluşmadan görünür kılar.
