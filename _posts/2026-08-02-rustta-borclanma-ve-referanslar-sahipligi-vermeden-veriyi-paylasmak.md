---
layout: post
title: "Rust’ta Borçlanma ve Referanslar: Sahipliği Vermeden Veriyi Paylaşmak"
math: true
categories: 
  - Bilgi
tags: 
  - Rust
  - Borrowing
  - Referanslar
---

Rust’ın bellek güvenliğindeki süper gücü, verileri sürekli kopyalamak veya çöp toplayıcı kullanmak değil; sahiplik ile borçlanmayı derleme aşamasında denetlemektir. Bir değeri başka bir fonksiyona gönderirken sahipliğini devretmek istemiyorsak `&` işaretiyle referans oluştururuz. Böylece fonksiyon veriyi geçici olarak ödünç alır; fakat onun kalıcı sahibi olmaz.
``
## Sahiplik devri ile borçlanma arasındaki fark

Rust’ta her değerin tek bir sahibi vardır. Bir `String` başka bir değişkene doğrudan atanırsa çoğunlukla sahiplik taşınır. Eski değişken artık kullanılamaz. Referans kullanıldığında ise yalnızca verinin adresine güvenli bir erişim sağlanır.

```rust
fn uzunluk_hesapla(metin: &String) -> usize {
    metin.len()
}

fn main() {
    let mesaj = String::from("Merhaba Rust");
    let uzunluk = uzunluk_hesapla(&mesaj);

    println!("{} karakter: {}", uzunluk, mesaj);
}
```

Burada `&mesaj`, `mesaj` değişkeninin sahipliğini fonksiyona taşımaz. `uzunluk_hesapla` yalnızca salt okunur bir referans alır. Fonksiyon tamamlandığında borç sona erer ve asıl değer kullanılmaya devam eder.

| İşlem | Sözdizimi | Sahiplik taşınır mı? | Veri değiştirilebilir mi? |
|---|---|---:|---:|
| Değer aktarımı | `islem(mesaj)` | Evet | Fonksiyona bağlı |
| Değişmez borç | `islem(&mesaj)` | Hayır | Hayır |
| Değiştirilebilir borç | `islem(&mut mesaj)` | Hayır | Evet |

## Değişmez ve değiştirilebilir referanslar

Bir referans varsayılan olarak değişmezdir. Veriyi düzenlemek için hem değişkenin `mut` olarak tanımlanması hem de `&mut` referansı verilmesi gerekir.

```rust
fn unlem_ekle(metin: &mut String) {
    metin.push('!');
}

fn main() {
    let mut mesaj = String::from("Rust güvenlidir");
    unlem_ekle(&mut mesaj);
    println!("{}", mesaj);
}
```

Bu fonksiyon `String` değerini sahiplenmeden değiştirir. Kritik kural şudur: Belirli bir anda aynı veri için ya birden fazla değişmez referans ya da yalnızca bir değiştirilebilir referans bulunabilir.

Bu ilişkiyi basitleştirerek şöyle gösterebiliriz:

$$N_{mut} \leq 1$$

Ayrıca değiştirilebilir bir referans etkinken değişmez referans sayısı sıfır olmalıdır:

$$N_{mut} = 1 \Rightarrow N_{shared} = 0$$

| Geçerli durum | Değişmez referans | Değiştirilebilir referans | Sonuç |
|---|---:|---:|---|
| Çoklu okuma | Bir veya daha fazla | 0 | Güvenli |
| Tek yazıcı | 0 | 1 | Güvenli |
| Okuma ve yazma | Bir veya daha fazla | 1 | Reddedilir |
| Çoklu yazıcı | 0 | İki veya daha fazla | Reddedilir |

## Neden yalnızca tek değiştirilebilir referans var?

İki kod parçasının aynı veriyi eş zamanlı değiştirebildiğini düşünelim. Biri dizinin kapasitesini büyütüp bellekte başka bir konuma taşırken diğeri eski adresi kullanabilir. Bu durum veri yarışı, geçersiz işaretçi ve beklenmeyen sonuçlar üretebilir. Borrow checker bu olasılığı program çalışmadan engeller.

```rust
let mut sayilar = vec![1, 2, 3];
let ilk = &mut sayilar;
// let ikinci = &mut sayilar; // Derleme hatası

ilk.push(4);
```

`ilk` değiştirilebilir borcu aktifken `ikinci` bir başka yazma yetkisi oluşturmaya çalışır. Rust bunu reddederek “tek veri, tek aktif yazıcı” ilkesini uygular.

Modern Rust, Non-Lexical Lifetimes sayesinde referansın ömrünü yalnızca süslü parantezlere göre değil, son kullanıldığı noktaya göre değerlendirir:

```rust
let mut puan = 10;
let gorunum = &puan;
println!("{}", gorunum); // Değişmez borcun son kullanımı

let duzenleyici = &mut puan;
*duzenleyici += 5;
```

İki referans aynı blokta görünse de etkin kullanım süreleri çakışmadığından kod güvenlidir. Özetle `&T` paylaşılabilen okuma izni, `&mut T` ise özel yazma iznidir. Rust’ın ampersandı sadece bir adres operatörü değil, derleyici tarafından denetlenen geçici bir erişim sözleşmesidir.
