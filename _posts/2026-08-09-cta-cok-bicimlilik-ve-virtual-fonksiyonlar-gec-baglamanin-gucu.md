---
layout: post
title: "C++'ta Çok Biçimlilik ve Virtual Fonksiyonlar: Geç Bağlamanın Gücü"
math: true
categories: 
  - Bilgi
tags: 
  - C++
  - Nesne Yönelimli Programlama
  - Polymorphism
  - Virtual Fonksiyonlar
---

C++ nesne yönelimli programlamanın en etkileyici fikirlerinden biri, aynı arayüzün farklı nesnelerde farklı sonuçlar üretmesidir. Buna **çok biçimlilik** (*polymorphism*) denir. Bir `Animal*` işaretçisiyle hem kediye hem köpeğe ses çıkarttırabilmek, kodun her somut sınıfı tek tek tanımasına gerek kalmadan genişlemesini sağlar. Bu esneklik, özellikle oyun motorları, ödeme sistemleri ve eklenti mimarilerinde hayat kurtarır.

``

## Bağlama zamanı neden önemlidir?

Bir fonksiyon çağrısının hangi fonksiyona gideceğine karar verilmesine **bağlama** (*binding*) denir. Normal üye fonksiyonlarda karar derleme zamanında verilir; bu, **erken bağlama**dır. `virtual` anahtar sözcüğü ise kararı çalışma zamanına bırakır: **geç bağlama** (*late binding*).

Teorik olarak, temel sınıf işaretçisinin türü $B$ ve işaret ettiği gerçek nesnenin türü $D$ olsun. Virtual bir çağrının seçimi işaretçinin statik türüne değil, nesnenin dinamik türüne bağlıdır:

$$f(B^*) \rightarrow f(D)$$

Bu küçük görünen fark, kalıtım zincirinin gerçek gücünü açığa çıkarır. Aşağıdaki tabloda iki yaklaşımın özeti bulunuyor:

| Özellik | Normal fonksiyon | `virtual` fonksiyon |
|---|---|---|
| Karar zamanı | Derleme zamanı | Çalışma zamanı |
| Seçim ölçütü | İşaretçinin/referansın türü | Gerçek nesne türü |
| Performans | Çok az daha doğrudan | Dolaylı çağrı maliyeti olabilir |
| Esneklik | Düşük | Yüksek |
| Kullanım alanı | Sabit davranış | Genişletilebilir hiyerarşiler |

## Kedi mi konuşuyor, hayvan mı?

Önce temel sınıfın ortak sözleşmeyi tanımladığını düşünelim. `speak()` tüm hayvanlar için anlamlıdır, fakat ürettiği ses her hayvanda farklıdır. Saf sanal fonksiyon kullanmak, `Animal` sınıfının doğrudan nesne üretmek yerine bir soyutlama olduğunu açıkça söyler.

```cpp
#include <iostream>
#include <memory>
#include <vector>

class Animal {
public:
    virtual void speak() const = 0;
    virtual ~Animal() = default;
};

class Cat : public Animal {
public:
    void speak() const override {
        std::cout << "Miyav!\n";
    }
};

class Dog : public Animal {
public:
    void speak() const override {
        std::cout << "Hav hav!\n";
    }
};

int main() {
    std::vector<std::unique_ptr<Animal>> animals;
    animals.push_back(std::make_unique<Cat>());
    animals.push_back(std::make_unique<Dog>());

    for (const auto& animal : animals) {
        animal->speak();
    }
}
```

Burada `animals` vektörü yalnızca `Animal` arayüzünü bilir. Buna rağmen ilk çağrı `Cat::speak()`, ikinci çağrı `Dog::speak()` olur. Derleyici bu davranışı çoğu uygulamada **vtable** adı verilen fonksiyon işaretçisi tablosu üzerinden gerçekleştirir. Standart, vtable'ın tam uygulama ayrıntısını zorunlu kılmaz; ancak zihinsel model olarak oldukça faydalıdır.

## `override` ve sanal yıkıcı: İki önemli emniyet kemeri

Türetilmiş sınıfta `override` kullanmak zorunlu değildir, ama güçlü biçimde önerilir. Örneğin yanlışlıkla `void speak()` yerine `void speak(int)` yazarsanız, derleyici bunun üst sınıftaki fonksiyonu ezmediğini hemen bildirir. Böylece sessiz ve pahalı hatalar önlenir.

Bir diğer kritik ayrıntı, temel sınıfın yıkıcısının `virtual` olmasıdır. Aksi halde `Animal*` üzerinden silinen bir `Cat` nesnesinde türetilmiş sınıfın yıkıcısı çalışmayabilir. Kaynak yöneten sınıflarda bu durum bellek sızıntısı veya eksik temizlik demektir.

| Tercih | Sonuç |
|---|---|
| `virtual void speak()` | Davranış dinamik türe göre seçilir |
| `void speak()` | Temel işaretçi üzerinden temel sürüm çağrılabilir |
| `void speak() override` | Ezme niyeti derleyici tarafından doğrulanır |
| `virtual ~Animal()` | Temel işaretçiyle güvenli yok etme sağlar |

Sonuç olarak çok biçimlilik, `if` ve `switch` zincirleriyle tür kontrolü yapma ihtiyacını azaltır. Sisteme yeni bir `Bird` sınıfı eklediğinizde mevcut döngüyü değiştirmek yerine yalnızca `speak()` davranışını tanımlarsınız. İşte geç bağlama, C++ kodunu hem daha okunur hem de değişime daha dayanıklı yapan mekanizmadır.
