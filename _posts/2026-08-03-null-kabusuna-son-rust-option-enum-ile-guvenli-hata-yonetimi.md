---
layout: post
title: "Null Kabusuna Son: Rust Option Enum ile Güvenli Hata Yönetimi"
math: true
categories: 
  - Bilgi
tags: 
  - Rust
  - Option
  - Hata Yönetimi
---

Bir nesnenin var olduğunu düşünerek kod yazarsınız, uygulamayı çalıştırırsınız ve aniden meşhur “null reference” hatasıyla karşılaşırsınız. Rust, bu sürprizi çalışma zamanına bırakmak yerine bir değerin yokluğunu `Option` enum’u ile açıkça modellememizi ister. Böylece “Belki vardır, belki yoktur” ihtimali, derleyicinin denetleyebildiği güvenli bir tipe dönüşür.
``
## Option neden gereklidir?

Java, C# ve JavaScript gibi dillerde bir referansın `null` olması mümkündür. Buna rağmen değişkenin tipi çoğu zaman bu ihtimali yeterince görünür kılmaz. Programcı kontrol yapmayı unutursa hata çalışma zamanında ortaya çıkar.

Rust’ta sıradan bir referans kendiliğinden `null` olamaz. Bir değerin bulunmaması geçerli bir durumsa standart kütüphanedeki şu enum kullanılır:

```rust
enum Option<T> {
    Some(T),
    None,
}
```

Buradaki `T`, saklanabilecek değerin tipidir. Örneğin `Option<i32>`, ya `Some(i32)` biçiminde bir tam sayı ya da `None` içerir. Olası durumların sayısını basitçe şöyle gösterebiliriz:

$$Option(T) = T + 1$$

Formüldeki ekstra bir durum `None` seçeneğidir. Örneğin `bool` iki farklı değere sahipken `Option<bool>` üç durumu temsil eder: `Some(true)`, `Some(false)` ve `None`.

| Yaklaşım | Değer varsa | Değer yoksa | Güvenlik |
|---|---|---|---|
| Null kullanılabilen referans | Nesne | `null` | Kontrol unutulabilir |
| `Option<T>` | `Some(T)` | `None` | Derleyici iki durumu da ele aldırır |
| Varsayılan değer | Gerçek değer | Örneğin `0` | Yokluk ile gerçek değer karışabilir |

## Pattern matching ile değeri açmak

`Option` içindeki veriye doğrudan erişilemez. Önce hangi varyantla karşı karşıya olduğumuzu belirlememiz gerekir. En açık yöntem `match` ifadesidir:

```rust
fn kullanici_bul(id: u32) -> Option<String> {
    if id == 42 {
        Some(String::from("Ada"))
    } else {
        None
    }
}

fn main() {
    match kullanici_bul(42) {
        Some(isim) => println!("Kullanıcı bulundu: {isim}"),
        None => println!("Kullanıcı bulunamadı"),
    }
}
```

Fonksiyon, sonuç bulmayı garanti etmediği için `String` yerine `Option<String>` döndürür. `match`, hem `Some` hem de `None` kolunu yazmamızı zorunlu tutar. Bir kol unutulursa program derlenmez; yani hata, kullanıcıya ulaşmadan yakalanır.

Yalnızca değer bulunduğunda işlem yapılacaksa `if let` daha kısa olabilir:

```rust
if let Some(isim) = kullanici_bul(42) {
    println!("Hoş geldin, {isim}!");
}
```

## Option yardımcı metotları

Rust, sık kullanılan senaryolar için pratik metotlar sunar:

| Metot | Davranış | Uygun kullanım |
|---|---|---|
| `unwrap_or(x)` | `None` ise `x` döndürür | Güvenli varsayılan değer |
| `map(f)` | Mevcut değeri dönüştürür | Kısa veri işleme zinciri |
| `and_then(f)` | Yeni bir `Option` üreten işlem yapar | Ardışık kontroller |
| `is_some()` | Değer varsa `true` döndürür | Yalnızca varlık kontrolü |
| `unwrap()` | Değeri çıkarır, yoksa panikletir | Varlık kesin olarak kanıtlandıysa |

Örneğin yaş bilgisini güvenli biçimde dönüştürebiliriz:

```rust
fn yas_metni(yas: Option<u8>) -> String {
    yas.map(|deger| format!("{deger} yaşında"))
        .unwrap_or(String::from("Yaş bilinmiyor"))
}
```

`map`, yalnızca değer varsa closure’ı çalıştırır. Sonuç `None` kalırsa `unwrap_or` varsayılan metni üretir. Böylece elle dallanma yazmadan güvenli bir akış kurulur.

## Option ile Result aynı şey değildir

`Option`, yalnızca değer bulunup bulunmadığını anlatır. Başarısızlığın nedenini de taşımak gerekiyorsa `Result<T, E>` daha uygundur.

```rust
fn bol(a: f64, b: f64) -> Option<f64> {
    if b == 0.0 { None } else { Some(a / b) }
}
```

Bu örnekte yokluk sebebi zaten açıktır. Dosya okuma gibi bir işlemde ise “dosya yok”, “izin reddedildi” veya “disk hatası” ayrımı gerektiğinden `Result` seçilmelidir.

Kısacası `Option`, null değerini sihirli ve tehlikeli bir istisna olmaktan çıkarıp tip sisteminin parçası yapar. Rust size “Bu değer kesinlikle var mı?” sorusunu kod derlenmeden önce sordurur. Biraz disiplin karşılığında daha az gece yarısı hatası alınır; bu da oldukça kârlı bir takastır.
