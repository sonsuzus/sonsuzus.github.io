---
layout: post
title: "Korkusuz Eşzamanlılık: Rust ile Veri Yarışlarına Derleme Zamanında Fren"
math: true
categories: 
  - Bilgi
tags: 
  - Rust
  - eşzamanlılık
  - veri güvenliği
---

Eşzamanlı programlama, performans kapısını açarken içeri veri yarışları, kilitlenmeler ve gizemli üretim hataları da sokabilir. Rust’ın “korkusuz eşzamanlılık” yaklaşımı ise sahiplik kurallarını ve tip sistemini bir güvenlik görevlisi gibi kullanır. Böylece birçok tehlikeli thread senaryosu, program çalıştırılmadan önce derleyici tarafından reddedilir. Kısacası Rust, “Önce çalıştıralım, sonra ne patlıyor bakarız” geleneğine pek sıcak bakmaz.

``

## Veri yarışı tam olarak nedir?

Bir veri yarışı oluşması için şu üç koşulun aynı anda gerçekleşmesi gerekir:

1. En az iki thread aynı belleğe erişir.
2. Erişimlerden en az biri yazma işlemidir.
3. Erişimler arasında güvenilir bir senkronizasyon yoktur.

Örneğin iki thread aynı sayacı eşzamanlı artırırsa sonuç beklenenden küçük olabilir. Çünkü `sayac += 1` tek ve bölünemez bir işlem değildir; kabaca okuma, artırma ve yazma aşamalarından oluşur.

Rust’ın temel sahiplik ilkesi bunu şu kuralla sınırlar: Aynı anda ya birden fazla değişmez referans (`&T`) ya da yalnızca bir değişebilir referans (`&mut T`) bulunabilir. Sembolik olarak:

$$N(&T) \ge 0 \quad \text{ve} \quad N(&mut T)=0$$

veya

$$N(&T)=0 \quad \text{ve} \quad N(&mut T)=1$$

Bu kural thread sınırlarında da uygulandığı için güvensiz ortak yazma işlemleri daha doğmadan yakalanır.

## Klasik yaklaşım ile Rust yaklaşımı

| Konu | Klasik dillerde yaygın durum | Rust yaklaşımı |
|---|---|---|
| Bellek paylaşımı | Referanslar serbestçe paylaşılabilir | Sahiplik aktarılır veya güvenli biçimde paylaşılır |
| Veri yarışı | Genellikle çalışma zamanında fark edilir | Çoğunlukla derleme anında engellenir |
| Thread güvenliği | Programcının disiplinine bağlıdır | `Send` ve `Sync` tip özellikleriyle denetlenir |
| Ortak değişken | Kilitleme unutulabilir | `Mutex<T>` veriye erişimi kilit korumasına bağlar |
| Mesajlaşma | Harici araçlar gerekebilir | Standart kanallar doğrudan kullanılabilir |

`Send`, bir değerin sahipliğinin başka bir thread’e aktarılabileceğini; `Sync` ise `&T` referansının thread’ler arasında güvenle paylaşılabileceğini belirtir. Bu özelliklerin çoğunu Rust uygun tipler için otomatik belirler.

## Sahipliği thread’e taşımak

`move` anahtar sözcüğü, closure’ın kullandığı değerin sahipliğini yeni thread’e aktarır:

```rust
use std::thread;

fn main() {
    let mesajlar = vec!["derle", "test et", "yayınla"];

    let worker = thread::spawn(move || {
        for mesaj in mesajlar {
            println!("Görev: {mesaj}");
        }
    });

    worker.join().expect("Thread başarısız oldu");
}
```

Burada `mesajlar`, worker thread’ine taşınır. Ana thread daha sonra bu vektörü kullanmaya çalışırsa derleyici itiraz eder. Böylece bir thread veriyi yok ederken diğerinin okumaya devam etmesi engellenir. `join` ise ana thread’in worker tamamlanana kadar beklemesini sağlar.

## Paylaşılan sayaç: `Arc<Mutex<T>>`

Birden fazla thread’in aynı veriyi değiştirmesi gerektiğinde `Arc`, thread güvenli ortak sahiplik; `Mutex` ise kontrollü değişim sağlar:

```rust
use std::sync::{Arc, Mutex};
use std::thread;

fn main() {
    let sayac = Arc::new(Mutex::new(0));
    let mut handles = Vec::new();

    for _ in 0..4 {
        let sayac = Arc::clone(&sayac);
        handles.push(thread::spawn(move || {
            for _ in 0..1_000 {
                let mut deger = sayac.lock().unwrap();
                *deger += 1;
            }
        }));
    }

    for handle in handles {
        handle.join().unwrap();
    }

    println!("Sonuç: {}", *sayac.lock().unwrap());
}
```

Beklenen sonuç $4 \times 1000 = 4000$ olur. `lock()` bir koruma nesnesi döndürür; bu nesne kapsamdan çıktığında kilit otomatik bırakılır. Böylece kilit açmayı unutma riski azalır.

## Hızlanma ücretsiz değildir

Paralel çalışmanın ideal hızlanması $S(p)=p$ olsa da pratikte seri işler sınır koyar. Amdahl yasası bunu şöyle ifade eder:

$$S(p)=\frac{1}{(1-f)+\frac{f}{p}}$$

Burada $f$ paralelleştirilebilir oran, $p$ ise thread sayısıdır. Ayrıca çok sık kilit almak, thread’leri hızlandırmak yerine sıraya sokabilir. Bu nedenle mesaj kanalları, küçük kilit kapsamları ve değişmez veri tercih edilmelidir.

Korkusuz eşzamanlılık bütün mantık hatalarını engellemez; deadlock veya yanlış işlem sırası hâlâ mümkündür. Ancak Rust, veri yarışlarını tip hatasına dönüştürerek en sinsi hata sınıflarından birini çalışma zamanından derleme zamanına taşır. Derleyici bazen huysuz görünür, fakat amacı hafta sonu üretim alarmı almamanızdır.
