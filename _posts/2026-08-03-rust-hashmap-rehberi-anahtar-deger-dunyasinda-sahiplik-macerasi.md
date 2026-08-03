---
layout: post
title: "Rust HashMap Rehberi: Anahtar-Değer Dünyasında Sahiplik Macerası"
math: true
categories: 
  - Bilgi
tags: 
  - Rust
  - HashMap
  - Sahiplik
---

Bir telefon rehberinde kişileri sayfa sayfa aramak yerine isimlerini doğrudan yazarak numaralarına ulaştığınızı düşünün. Hash haritaları tam olarak bu fikri programlama dünyasına taşır: Veriler, anahtar ve değer çiftleri hâlinde saklanır. Rust’ın `HashMap` koleksiyonu ise bu pratik yapıyı dilin sahiplik, ödünç alma ve yaşam süresi kurallarıyla birleştirerek hem hızlı hem de güvenli veri yönetimi sunar.
``
## Hash haritasının çalışma mantığı

Bir hash haritasındaki her anahtar, hash fonksiyonu tarafından sayısal bir özete dönüştürülür. Basitleştirilmiş biçimiyle yerleşim işlemi şöyle gösterilebilir:

$$indeks = hash(anahtar) \bmod kapasite$$

Bu indeks, değerin bellekte hangi kovaya yerleştirileceğini belirler. İki farklı anahtar aynı indeksi üretirse **çakışma** oluşur. Hash haritası uygulamaları bu durumu zincirleme veya açık adresleme gibi yöntemlerle çözer.

İyi dağılım sağlayan bir hash fonksiyonunda ekleme, arama ve silme işlemlerinin ortalama zaman karmaşıklığı $O(1)$ kabul edilir. Ancak çok sayıda çakışmanın yaşandığı kötü durumda karmaşıklık $O(n)$ seviyesine çıkabilir.

| Koleksiyon | Erişim yöntemi | Ortalama arama | Sıralama |
|---|---|---:|---|
| `Vec<T>` | Sayısal indeks | $O(n)$ | Ekleme sırasını korur |
| `HashMap<K, V>` | Benzersiz anahtar | $O(1)$ | Garanti edilmez |
| `BTreeMap<K, V>` | Sıralı anahtar | $O(\log n)$ | Anahtara göre sıralıdır |

## Rust ile HashMap oluşturmak

`HashMap`, standart kütüphanenin ön hazırlık modülünde otomatik olarak bulunmaz; önce içe aktarılmalıdır. Aşağıdaki kod, ürün adlarını fiyatlarla eşleştirir:

```rust
use std::collections::HashMap;

fn main() {
    let mut fiyatlar = HashMap::new();

    fiyatlar.insert(String::from("Klavye"), 1250);
    fiyatlar.insert(String::from("Fare"), 700);
    fiyatlar.insert(String::from("Monitör"), 8200);

    if let Some(fiyat) = fiyatlar.get("Klavye") {
        println!("Klavye fiyatı: {fiyat} TL");
    }
}
```

`insert`, haritayı değiştirdiği için değişken `mut` olarak tanımlanmıştır. `get` metodu ise anahtar bulunamayabileceğinden `Option<&V>` döndürür. Böylece Rust, “olmayan değeri kullandın, program çöktü” sürprizini kontrollü bir seçime dönüştürür.

## Sahiplik kuralları haritayı nasıl etkiler?

`i32` gibi `Copy` özelliğine sahip türler haritaya kopyalanır. `String` gibi kopyalanmayan türlerde ise sahiplik varsayılan olarak `HashMap` yapısına taşınır:

```rust
use std::collections::HashMap;

fn main() {
    let anahtar = String::from("tema");
    let deger = String::from("karanlik");
    let mut ayarlar = HashMap::new();

    ayarlar.insert(anahtar, deger);

    // println!("{anahtar}"); // Hata: sahiplik taşındı.
    println!("{:?}", ayarlar.get("tema"));
}
```

Eklemeden sonra `anahtar` ve `deger` artık kullanılamaz; onların yeni sahibi `ayarlar` değişkenidir. Harita kapsam dışına çıktığında içindeki veriler de güvenli biçimde temizlenir. Verilerin sahipliğini taşımak istemiyorsak referans saklayabiliriz; ancak bu kez referansların haritadan daha uzun yaşaması gerekir.

| Ekleme biçimi | Sonuç | Dikkat edilmesi gereken |
|---|---|---|
| Sahip olunan `String` | Sahiplik haritaya taşınır | Eski değişken kullanılamaz |
| `i32`, `bool` gibi `Copy` türü | Değer kopyalanır | Kaynak değişken kullanılabilir |
| `&str` veya başka referans | Yalnızca ödünç alınır | Yaşam süresi geçerli kalmalıdır |
| `clone()` ile ekleme | Bağımsız kopya üretilir | Ek bellek ve işlem maliyeti doğurur |

## Değerleri güncelleme stratejileri

Aynı anahtarla tekrar `insert` çağrılırsa eski değer yenisiyle değiştirilir. Anahtar yalnızca yoksa değer eklemek için `entry` API’si kullanılır. Bu API, kelime sayacı gibi senaryolarda oldukça zariftir:

```rust
use std::collections::HashMap;

fn main() {
    let metin = "rust guvenli rust hizli rust eglenceli";
    let mut sayac = HashMap::new();

    for kelime in metin.split_whitespace() {
        let adet = sayac.entry(kelime).or_insert(0);
        *adet += 1;
    }

    println!("{sayac:?}");
}
```

`or_insert(0)`, ilgili değere değiştirilebilir bir referans verir. `*adet += 1` ifadesi bu referansın gösterdiği sayıyı artırır. Ödünç alma kuralları nedeniyle aynı anda harita üzerinde çakışan değiştirilebilir erişimler oluşturulamaz; böylece iterator geçersizliği ve veri yarışı gibi hatalar daha derleme aşamasında engellenir.

Sonuç olarak `HashMap`, hızlı anahtar tabanlı erişim sağlarken Rust’ın sahiplik modeli verilerin kime ait olduğunu açıkça belirler. Ayarlar, önbellekler, sayaçlar ve kullanıcı kayıtları için güçlü bir seçimdir; fakat sıralama gerekiyorsa `BTreeMap`, yalnızca ardışık veriler tutulacaksa `Vec` daha uygun olabilir.
