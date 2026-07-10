---
layout: post
title: "C++ Sınıf Mirasları: Kodun Aile Ağacı"
math: true
excerpt_separator: "<!-- more -->"
categories: 
  - Bilgi
tags: 
  - c++
  - oop
  - miras
  - nesne yönelimli programlama
---

C++’ta sınıf mirası, bir sınıfın başka bir sınıftan özellik ve davranış devralmasını sağlayan güçlü bir nesne yönelimli programlama mekanizmasıdır. Kısaca: “Zaten yazdığım kodu neden tekrar yazayım?” sorusuna C++’ın verdiği cevaptır. Bir oyun düşün: tüm karakterlerin adı, canı ve hareket etme davranışı var; ama büyücü ayrıca büyü yapıyor, savaşçı kılıç sallıyor. İşte miras, bu ortak ve özel tarafları düzenli biçimde ayırmamıza yardım eder.
<!-- more -->

Mirasın temelinde **is-a** ilişkisi vardır. Yani “Büyücü bir Karakterdir” diyebiliyorsak, `Wizard` sınıfı `Character` sınıfından türeyebilir. Matematiksel olarak bunu kümeler gibi düşünebiliriz: `Wizard \subset Character` değil, daha doğru ifadeyle `Wizard` nesneleri `Character` arayüzünü de taşır. Bir taban sınıfın özellik kümesi $B$, türetilmiş sınıfın eklediği özellikler $E$ ise, türetilmiş sınıfın toplam yeteneği yaklaşık olarak $D = B \cup E$ şeklinde düşünülebilir.

## Temel Miras Söz Dizimi

C++’ta miras şu şekilde tanımlanır:

```cpp
class Character {
public:
    string name;
    int health;

    void move() {
        cout << name << " hareket ediyor." << endl;
    }
};

class Wizard : public Character {
public:
    void castSpell() {
        cout << name << " büyü yapıyor!" << endl;
    }
};
```

Burada `Wizard`, `Character` sınıfından **public miras** alır. Bu sayede `Wizard` nesnesi hem `name`, `health`, `move()` üyelerine hem de kendi `castSpell()` fonksiyonuna sahip olur.

```cpp
int main() {
    Wizard merlin;
    merlin.name = "Merlin";
    merlin.health = 100;
    merlin.move();
    merlin.castSpell();
}
```

Bu kodda `move()` fonksiyonu `Wizard` içinde yazılmadığı halde çalışır; çünkü taban sınıftan devralınmıştır. Bu, mirasın en pratik tarafıdır: ortak davranışları merkezileştirmek.

## Public, Protected ve Private Miras

C++’ta miras türü, taban sınıftaki erişim seviyelerinin türetilmiş sınıfa nasıl aktarılacağını belirler.

| Miras Türü | Taban `public` üyeler | Taban `protected` üyeler | Ne zaman kullanılır? |
|---|---|---|---|
| `public` | `public` kalır | `protected` kalır | Gerçek “is-a” ilişkisi varsa |
| `protected` | `protected` olur | `protected` kalır | Dışarıya arayüz kapatılmak istenirse |
| `private` | `private` olur | `private` olur | Uygulama detayı olarak devralma gerektiğinde |

Günlük kullanımda en sık `public` miras tercih edilir. Çünkü nesne yönelimli tasarımda türetilmiş sınıfın taban sınıf yerine geçebilmesi beklenir. Buna **Liskov Yerine Geçme Prensibi** denir: Eğer `Wizard` bir `Character` ise, `Character*` bekleyen bir fonksiyona `Wizard*` gönderebilmeliyiz.

## Protected: Aile Sırrı

`private` üyeler sadece sınıfın kendisi tarafından erişilebilir. Ancak bazen türetilmiş sınıfların da bazı verilere erişmesi gerekir. Bu durumda `protected` kullanılır.

```cpp
class Character {
protected:
    int health;

public:
    Character(int h) : health(h) {}

    void showHealth() {
        cout << "Can: " << health << endl;
    }
};

class Warrior : public Character {
public:
    Warrior() : Character(150) {}

    void takeDamage(int amount) {
        health -= amount;
    }
};
```

Burada `health`, dış dünyaya kapalıdır ama `Warrior` tarafından erişilebilir. Bu, kapsüllemeyi tamamen bozmadan esneklik sağlar.

## Fonksiyon Ezme ve Sanal Fonksiyonlar

Mirasın asıl yıldızı **polimorfizm** ile parlar. Taban sınıftaki bir davranışı türetilmiş sınıfta farklılaştırmak için `virtual` kullanılır.

```cpp
class Character {
public:
    virtual void attack() {
        cout << "Karakter saldırıyor." << endl;
    }
};

class Archer : public Character {
public:
    void attack() override {
        cout << "Okçu ok fırlatıyor!" << endl;
    }
};
```

`virtual`, çalışma zamanında doğru fonksiyonun seçilmesini sağlar. Bu mekanizma dinamik bağlama olarak bilinir. Basitçe maliyetini şöyle düşünebiliriz: normal fonksiyon çağrısı $O(1)$ iken sanal çağrı da pratikte $O(1)$ kabul edilir, fakat küçük bir yönlendirme maliyeti vardır.

| Kavram | Amaç | Örnek |
|---|---|---|
| Miras | Ortak kodu paylaşmak | `Wizard : public Character` |
| Ezme | Davranışı özelleştirmek | `attack() override` |
| Polimorfizm | Aynı arayüzle farklı davranış | `Character* c = new Archer()` |
| Kapsülleme | Veriyi kontrollü saklamak | `private`, `protected` |

## Yapıcı ve Yıkıcı Fonksiyonlara Dikkat

Türetilmiş sınıf oluşturulurken önce taban sınıfın yapıcısı, sonra türetilmiş sınıfın yapıcısı çalışır. Yıkımda ise sıra tersinedir. Eğer taban sınıf üzerinden türetilmiş nesneleri sileceksen, yıkıcı fonksiyon `virtual` olmalıdır.

```cpp
class Character {
public:
    virtual ~Character() {
        cout << "Character yok edildi." << endl;
    }
};
```

Aksi halde bellek sızıntısı veya eksik temizlik gibi tatsız sürprizlerle karşılaşabilirsin.

## Ne Zaman Miras Kullanılmalı?

Miras her derde deva değildir. Eğer ilişki “bir şeydir” değil de “bir şeye sahiptir” şeklindeyse, kompozisyon daha iyi olabilir. Örneğin `Car` sınıfı `Engine` sınıfından miras almamalı; onun yerine bir `Engine` nesnesine sahip olmalıdır.

Sonuç olarak C++ sınıf mirası, doğru kullanıldığında kod tekrarını azaltır, tasarımı anlaşılır kılar ve polimorfizmle güçlü mimariler kurmanı sağlar. Ama unutma: Miras aile bağı gibidir; doğru akrabayı seçersen huzur, yanlış akrabayı seçersen sonsuz refactoring getirir!
