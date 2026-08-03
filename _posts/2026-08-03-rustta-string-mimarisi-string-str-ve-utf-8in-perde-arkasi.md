---
layout: post
title: "Rust’ta String Mimarisi: String, &str ve UTF-8’in Perde Arkası"
math: true
categories: 
  - Bilgi
tags: 
  - Rust
  - String
  - UTF-8
---

Rust’ta metinlerle çalışmaya başlayanların karşısına kısa sürede iki oyuncu çıkar: `String` ve `&str`. İlk bakışta ikisi de yazı tutuyor gibi görünür; ancak bellek yönetimi, sahiplik ve boyut açısından aralarında önemli farklar vardır. Bu ayrımı anlamak, hem gereksiz kopyalamaları önler hem de Rust’ın ödünç alma sistemini çok daha anlaşılır hâle getirir.
``
## İki Farklı Metin Görünümü

`String`, UTF-8 kodlanmış metni heap üzerinde saklayan, büyüyüp küçülebilen ve verisinin sahibi olan bir koleksiyondur. Yapısal olarak `Vec<u8>` ile benzer bir mantığa sahiptir ve üç temel bilgi taşır:

- Heap üzerindeki veriyi gösteren işaretçi
- Kullanılan bayt sayısını belirten uzunluk
- Ayrılmış toplam alanı belirten kapasite

Bu ilişkiyi kabaca şöyle gösterebiliriz:

$$0 \leq \text{length} \leq \text{capacity}$$

Metne yeni karakterler eklendiğinde uzunluk kapasiteyi aşarsa daha büyük bir bellek alanı ayrılır ve mevcut veri taşınabilir. Dolayısıyla büyütme işlemi her zaman ücretsiz değildir.

`str` ise dinamik boyutlu bir türdür; derleme anında kaç bayt tutacağı bilinmez. Bu nedenle çoğunlukla doğrudan `str` değil, `&str` biçiminde kullanılır. Bir `&str`, metin verisine işaret eden ödünç alınmış bir görünüm ile görünümün bayt uzunluğundan oluşur. Verinin sahibi değildir ve kapsam sona erdiğinde metni serbest bırakmaz.

| Özellik | `String` | `&str` |
|---|---|---|
| Sahiplik | Verinin sahibidir | Veriyi ödünç alır |
| Boyut | Değişebilir | Görünüm boyunca sabittir |
| Bellek | Genellikle heap | Heap, stack veya program verisi olabilir |
| Yapı | İşaretçi, uzunluk, kapasite | İşaretçi, uzunluk |
| Tipik kullanım | Metin üretmek ve değiştirmek | Metni okumak ve fonksiyonlara aktarmak |

## Oluşturma ve Ödünç Alma

Aşağıdaki örnekte değiştirilebilir bir `String` oluşturuluyor, büyütülüyor ve ardından bu veriye `&str` görünümü alınıyor:

```rust
fn kelime_sayisi(metin: &str) -> usize {
    metin.split_whitespace().count()
}

fn main() {
    let mut mesaj = String::from("Merhaba");
    mesaj.push_str(", Rust dünyası!");

    let gorunum: &str = &mesaj;
    println!("{}", gorunum);
    println!("Kelime: {}", kelime_sayisi(&mesaj));
}
```

`kelime_sayisi` parametresinin `&str` olması önemlidir. Böylece fonksiyon hem `String` içinden alınan dilimleri hem de doğrudan yazılmış metin sabitlerini kabul eder. `&String` kullanmak mümkün olsa da daha az esnek bir API ortaya çıkarır.

## UTF-8: Karakter Sayısı Bayt Sayısı Değildir

Rust stringleri geçerli UTF-8 olmak zorundadır. ASCII karakterleri genellikle bir bayt kullanırken Türkçe karakterler veya emojiler birden fazla bayt kullanabilir. Bu nedenle genel olarak:

$$\text{bayt sayısı} \geq \text{Unicode karakter sayısı}$$

```rust
fn main() {
    let metin = "çağrı 🦀";

    println!("Bayt: {}", metin.len());
    println!("Karakter: {}", metin.chars().count());
}
```

Buradaki `len()` kullanıcıların gördüğü karakterleri değil, UTF-8 baytlarını sayar. Rust’ın `metin[0]` biçiminde indekslemeye izin vermemesinin nedeni de budur: Bir bayt her zaman bağımsız bir karakter anlamına gelmez.

Dilimleme yapılırken sınırların geçerli UTF-8 karakter sınırlarına denk gelmesi gerekir:

```rust
let metin = String::from("İstanbul");
let parca = &metin[0..2]; // "İ", UTF-8 içinde iki bayttır
println!("{}", parca);
```

Yanlış bir bayt sınırı çalışma zamanında paniğe yol açabilir. Güvenli karakter işleme için `chars()`, bayt işleme için `bytes()` kullanılmalıdır.

## Hangisini Seçmeliyiz?

Yeni metin oluşturacak, birleştirecek veya değiştirecekseniz `String` doğru araçtır. Yalnızca mevcut metni okuyacak bir fonksiyon yazıyorsanız `&str` tercih etmek daha esnek ve ekonomiktir. Kısacası `String` metnin ev sahibi, `&str` ise anahtarı geçici olarak teslim edilmiş misafiridir. UTF-8 de evin oda planıdır; bayt sınırlarını bilmeden duvarı kırmaya çalışırsanız Rust güvenlik görevlisini, yani paniği, çağırır.
