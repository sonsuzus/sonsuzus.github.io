---
layout: post
title: "Rust’ta Akıllı İşaretçiler: Box, Rc ve RefCell Nasıl Çalışır?"
math: true
categories: 
  - Bilgi
tags: 
  - Rust
  - Akıllı İşaretçiler
  - Bellek Yönetimi
---

Rust, çöp toplayıcı kullanmadan bellek güvenliği sağlamasıyla ünlüdür. Ancak boyutu derleme anında bilinmeyen veriler, birden fazla sahip gerektiren nesneler veya çalışma zamanında değişebilirlik isteyen yapılar, temel sahiplik kurallarının ötesine geçmemizi gerektirir. İşte `Box`, `Rc` ve `RefCell`, heap belleğin karanlık koridorlarında el feneri görevi görür.

``

## Stack ve heap neden ayrılır?

Stack üzerindeki bir değerin kapladığı alan derleme anında bilinmelidir. Çünkü fonksiyon çağrılırken stack çerçevesinin ne kadar büyüyeceği önceden hesaplanır. Heap ise çalışma zamanında ayrılan, boyutu dinamik olabilen veriler için kullanılır.

Bir koleksiyonun eleman sayısını $n$, her elemanın boyutunu $s$ kabul edersek gereken yaklaşık alan:

$$M = n \times s$$

şeklindedir. $n$ çalışma zamanına kadar bilinmiyorsa verinin tamamını doğrudan stack üzerinde saklamak mümkün değildir. Akıllı işaretçi stack üzerinde sabit boyutlu bir adres tutarken gerçek veri heap üzerinde bulunur.

| Araç | Temel amacı | Kontrol zamanı | Sahip sayısı |
|---|---|---|---|
| `Box<T>` | Veriyi heap üzerinde saklamak | Derleme zamanı | Tek |
| `Rc<T>` | Aynı veriyi paylaşmak | Çalışma zamanı sayaç takibi | Birden fazla |
| `RefCell<T>` | İçsel değişebilirlik sağlamak | Çalışma zamanı | Genellikle tek kapsayıcı |

## `Box<T>`: Heap’e açılan en sade kapı

`Box<T>`, `T` değerini heap’e yerleştirir ve stack üzerinde bu değerin adresini saklar. İşaretçinin boyutu sabit olduğundan özyinelemeli veri yapıları kurulabilir.

```rust
enum Liste {
    Dugum(i32, Box<Liste>),
    Son,
}

fn main() {
    let liste = Liste::Dugum(
        10,
        Box::new(Liste::Dugum(20, Box::new(Liste::Son))),
    );
}
```

Burada `Liste` doğrudan kendisini içerseydi boyutu sonsuz biçimde tanımlanırdı. `Box<Liste>` ise yalnızca sabit boyutlu bir adres tuttuğu için bu döngüyü kırar. `Box` kapsamdan çıktığında hem işaretçi hem de heap’teki veri otomatik olarak temizlenir.

## `Rc<T>`: Bir verinin birden fazla sahibi

Bazen bir düğümün veya yapılandırmanın birden fazla nesne tarafından paylaşılması gerekir. `Rc`, yani reference counting, güçlü referansların sayısını izler. Sayaç $r$ olsun. Her klonlamada $r = r + 1$, her sahip kapsamdan çıktığında $r = r - 1$ olur. $r = 0$ olduğunda veri silinir.

```rust
use std::rc::Rc;

fn main() {
    let veri = Rc::new(vec![10, 20, 30]);
    let okuyucu_a = Rc::clone(&veri);
    let okuyucu_b = Rc::clone(&veri);

    let sahip_sayisi = Rc::strong_count(&veri);
    assert_eq!(sahip_sayisi, 3);
    assert_eq!(okuyucu_a[0], okuyucu_b[0]);
}
```

`Rc::clone`, içeriğin tamamını kopyalamaz; yalnızca referans sayacını artırır. Bu işlem genellikle $O(1)$ maliyetlidir. Ancak `Rc` atomik sayaç kullanmadığından yalnızca tek iş parçacıklı senaryolara uygundur. Çok iş parçacıklı programlarda karşılığı `Arc<T>` olur.

## `RefCell<T>`: Kuralları çalışma zamanında denetlemek

Rust normalde aynı anda ya bir değiştirilebilir referansa ya da birden fazla salt okunur referansa izin verir:

$$N_{mutable} \leq 1, \qquad N_{mutable} > 0 \Rightarrow N_{shared} = 0$$

`RefCell<T>` bu kuralları kaldırmaz; kontrolü derleme zamanından çalışma zamanına taşır. `borrow()` salt okunur, `borrow_mut()` değiştirilebilir ödünç alma oluşturur. Kurallar ihlal edilirse program `panic` üretir.

```rust
use std::cell::RefCell;
use std::rc::Rc;

fn main() {
    let puan = Rc::new(RefCell::new(10));
    let oyuncu = Rc::clone(&puan);

    *oyuncu.borrow_mut() += 5;
    assert_eq!(*puan.borrow(), 15);
}
```

`Rc<RefCell<T>>` birleşimi, paylaşılan ve değiştirilebilen veri sağlar. Güçlüdür; fakat borçlar kısa tutulmalı ve döngüsel `Rc` bağlantılarından kaçınılmalıdır. Aksi hâlde sayaç hiçbir zaman sıfıra düşmez. Ebeveyn bağlantıları gibi sahiplik gerektirmeyen ilişkilerde `Weak<T>` kullanmak bu bellek sızıntısını önler.

Kısacası `Box` tek sahipli heap verisi, `Rc` ortak sahiplik, `RefCell` ise çalışma zamanında denetlenen içsel değişebilirlik sunar. Doğru seçim, verinin nerede duracağından çok ona kimin, ne zaman ve hangi yetkiyle erişeceğini belirlemektir.
