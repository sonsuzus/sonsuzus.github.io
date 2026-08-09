---
layout: post
title: "C++ Kalıtım ile Kod Yeniden Kullanımı: Nesne Hiyerarşileri Kurmak"
math: true
categories: 
  - Bilgi
tags: 
  - C++
  - Nesne Yönelimli Programlama
  - Kalıtım
---

Büyük bir C++ projesinde her nesneyi sıfırdan tanımlamak, kısa sürede kopyala-yapıştır bataklığına dönüşür. Bir aracın, çalışanın ya da oyun karakterinin ortak özellikleri varken bunları tekrar tekrar yazmak yerine kalıtım (inheritance) kullanırız. Kalıtım, bir temel sınıfın (base class) veri ve davranışlarını türetilmiş sınıflara (derived class) aktaran; böylece hem kod tekrarını azaltan hem de anlamlı nesne hiyerarşileri kuran nesne yönelimli programlama mekanizmasıdır.

``

Kalıtımın ana fikri **"bir türüdür"** (*is-a*) ilişkisidir. Örneğin bir `Araba` bir `Arac` türüdür; dolayısıyla aracın marka, hız ve hareket etme gibi genel niteliklerini miras alabilir. Buna karşılık, bir arabanın motoru olması **"sahiptir"** (*has-a*) ilişkisidir ve genellikle composition ile modellenmelidir. Bu ayrımı doğru yapmak, sürdürülebilir tasarımın ilk savunma hattıdır.

| İlişki | Anlamı | Uygun yaklaşım | Örnek |
|---|---|---|---|
| Is-a | Bir nesne, diğerinin özel türüdür | Kalıtım | `Araba`, `Arac`tır |
| Has-a | Bir nesne başka bir nesneyi içerir | Bileşim | `Araba` bir `Motor`a sahiptir |
| Uses-a | Geçici kullanım ilişkisi vardır | Bağımlılık | `Servis`, `Arac` kullanır |

C++'ta türetilmiş sınıf, temel sınıfın `public` üyelerine doğrudan erişebilir; `private` üyeler ise miras alınmış olsalar bile doğrudan erişilemez. Bu kural kapsüllemeyi korur. Temel sınıfın kontrollü erişim için sunduğu `protected` alanlar vardır, fakat veri üyelerini çoğunlukla `private` tutup metotlarla yönetmek daha güvenlidir.

```cpp
#include <iostream>
#include <string>

class Arac {
private:
    std::string marka;
    int hiz;

public:
    Arac(const std::string& marka) : marka(marka), hiz(0) {}

    void hizlan(int miktar) {
        hiz += miktar;
    }

    void bilgileriYazdir() const {
        std::cout << marka << " - " << hiz << " km/s\n";
    }
};

class ElektrikliAraba : public Arac {
private:
    int bataryaYuzdesi;

public:
    ElektrikliAraba(const std::string& marka, int batarya)
        : Arac(marka), bataryaYuzdesi(batarya) {}

    void sarjDurumunuYazdir() const {
        std::cout << "Batarya: %" << bataryaYuzdesi << "\n";
    }
};
```

Burada `ElektrikliAraba : public Arac` ifadesi, herkese açık kalıtımı anlatır. `ElektrikliAraba` nesnesi, `Arac`ın açık arayüzünü korur; yani `hizlan()` ve `bilgileriYazdir()` çağrılabilir. Kurucu listesinde yer alan `Arac(marka)` çağrısı da önemlidir: Önce temel sınıf bölümü, ardından türetilmiş sınıf bölümü oluşturulur.

Kalıtımın gerçek gücü, çok biçimlilikle (polymorphism) birleştiğinde görünür. Temel sınıftaki bir metodu `virtual` yaparsak, temel sınıf işaretçisi üzerinden doğru türetilmiş sınıf davranışı çalışma zamanında seçilir. Mantıksal olarak bu seçim $O(1)$ düzeyinde bir sanal tablo yönlendirmesiyle gerçekleşir; getirisi ise farklı türleri ortak bir arayüzde işleyebilmektir.

| Kavram | Amaç | Anahtar sözcük |
|---|---|---|
| Metot ezme | Alt sınıfa özel davranış | `override` |
| Dinamik bağlama | Çalışma anında doğru metodu seçme | `virtual` |
| Güvenli yıkım | Taban işaretçisinden silme | `virtual ~Sinif()` |

```cpp
class Bildirim {
public:
    virtual void gonder() const {
        std::cout << "Genel bildirim\n";
    }
    virtual ~Bildirim() = default;
};

class EpostaBildirimi : public Bildirim {
public:
    void gonder() const override {
        std::cout << "E-posta gönderildi.\n";
    }
};

void bildir(const Bildirim& kanal) {
    kanal.gonder();
}
```

`bildir()` fonksiyonu hangi bildirim türüyle çalıştığını bilmek zorunda değildir. Bu, açık/kapalı ilkesini destekler: Mevcut kodu değiştirmeden yeni `SMSBildirimi` sınıfları ekleyebilirsiniz. Ancak her ortak alan için kalıtım kullanmayın. Derin hiyerarşiler, sıkı bağımlılık ve kırılgan taban sınıf sorunları doğurabilir. Sağlam bir kural şudur: Gerçek bir *is-a* ilişkisi yoksa bileşimi tercih edin; varsa küçük, anlaşılır ve sanal yıkıcısı olan arayüz tabanlı sınıflar tasarlayın.
