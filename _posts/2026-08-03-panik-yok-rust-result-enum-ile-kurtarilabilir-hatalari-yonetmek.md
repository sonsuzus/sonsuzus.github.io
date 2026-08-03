---
layout: post
title: "Panik Yok: Rust Result Enum ile Kurtarılabilir Hataları Yönetmek"
math: true
categories: 
  - Bilgi
tags: 
  - Rust
  - Result Enum
  - Hata Yönetimi
---

Bir dosyanın bulunamaması, kullanıcının harf yerine sayı girmesi veya sunucunun geçici olarak yanıt vermemesi programın kıyamet senaryosu değildir. Bunlar beklenebilen ve çoğu zaman düzeltilebilen durumlardır. Rust, böyle hataları görünmez bir kontrol akışına teslim etmek yerine `Result` enum'u aracılığıyla açıkça modellememizi sağlar. Böylece hata yönetimi, kodun kenarında unutulan bir ayrıntı değil, fonksiyonun sözleşmesinin parçası olur.
``
## Kurtarılabilir hata nedir?

Hataları kabaca iki gruba ayırabiliriz. Programın varsayımlarını tamamen bozan durumlar kurtarılamaz kabul edilir ve Rust'ta çoğunlukla `panic!` ile ilişkilendirilir. Eksik dosya, geçersiz kullanıcı girdisi veya başarısız ağ isteği gibi olaylarsa kurtarılabilir hatalardır. Program bunları kullanıcıya bildirebilir, işlemi tekrarlayabilir ya da alternatif bir yol seçebilir.

Bir işlemin sonucunu basitçe şu küme gibi düşünebiliriz:

$$R = \{Ok(T), Err(E)\}$$

Burada $T$ başarılı değerin, $E$ ise hata bilgisinin türüdür. Rust standart kütüphanesindeki yapı kavramsal olarak şöyledir:

```rust
enum Result<T, E> {
    Ok(T),
    Err(E),
}
```

Bu tanım, bir fonksiyonun aynı anda hem başarı hem hata olamayacağını anlatır. Sonuç iki olasılıktan tam olarak biridir.

| Yaklaşım | Başarı durumu | Hata durumu | Derleyici kontrolü |
|---|---|---|---|
| `try-catch` | Normal dönüş | Fırlatılan exception | Genellikle sınırlı |
| `Result<T, E>` | `Ok(T)` | `Err(E)` | Güçlü ve açık |
| `panic!` | Dönüş beklenmez | Program akışı kesilir | Kurtarma amacı taşımaz |

## Result değerini eşleştirmek

Bir metni sayıya dönüştüren fonksiyon yazalım. Fonksiyon hata mesajını da dönüş türünde ilan ediyor:

```rust
fn sayiya_cevir(girdi: &str) -> Result<i32, String> {
    match girdi.trim().parse::<i32>() {
        Ok(sayi) => Ok(sayi),
        Err(_) => Err(format!("Geçersiz sayı: {girdi}")),
    }
}

fn main() {
    match sayiya_cevir("42") {
        Ok(deger) => println!("Sonuç: {deger}"),
        Err(hata) => eprintln!("Hata: {hata}"),
    }
}
```

`match`, iki ihtimali de ele almaya zorlar. Böylece hata yolunu yanlışlıkla unutmak zorlaşır. Üstelik hata bir değer olduğu için kaydedilebilir, dönüştürülebilir veya başka bir fonksiyona aktarılabilir.

## Soru işareti operatörüyle erken dönüş

Her adımda `match` yazmak güvenli olsa da kodu kalabalıklaştırabilir. `?` operatörü, değer `Ok` ise içeriğini çıkarır; `Err` ise hatayı çağıran fonksiyona hemen döndürür.

```rust
use std::fs;
use std::io;

fn ayarlari_oku() -> Result<String, io::Error> {
    let icerik = fs::read_to_string("ayarlar.txt")?;
    Ok(icerik)
}

fn main() {
    match ayarlari_oku() {
        Ok(ayarlar) => println!("Ayarlar yüklendi:\n{ayarlar}"),
        Err(hata) => eprintln!("Ayarlar okunamadı: {hata}"),
    }
}
```

Bu akış matematiksel olarak ardışık işlemlerin başarısına bağlıdır. $A$ ve $B$ adımları için toplam başarı koşulu $A \land B$ olur. İlk `Err` oluştuğunda zincir kısa devre yapar; gereksiz işlemler çalışmaz.

## Result dönüştürme araçları

Rust, sık kullanılan senaryolar için yardımcı metotlar sunar:

| Metot | Kullanım amacı |
|---|---|
| `map` | Başarılı değeri dönüştürür |
| `map_err` | Hata değerini dönüştürür |
| `and_then` | Yeni bir `Result` üreten işlemi zincirler |
| `unwrap_or` | Hata halinde varsayılan değer verir |
| `expect` | Hata halinde açıklamalı panik oluşturur |

```rust
fn iki_kati(girdi: &str) -> Result<i32, String> {
    girdi
        .parse::<i32>()
        .map(|sayi| sayi * 2)
        .map_err(|_| "Sayı biçimi geçersiz".to_string())
}
```

Burada `map`, yalnızca başarı halinde çalışır; `map_err` ise yalnızca hatayı uygulamaya uygun bir mesaja çevirir. Bu ayrım, mutlu yol ile hata yolunu birbirine dolamadan yönetir.

`unwrap` ve `expect` hızlı prototiplerde kullanışlıdır ancak üretim kodunda ölçülü kullanılmalıdır; çünkü `Err` geldiğinde programı panikletirler. Beklenen hatalarda `match`, `?` ve dönüştürme metotları daha dayanıklı tercihlerdir. Kısacası `Result`, hataları saklamaz: onları görünür, tür güvenli ve test edilebilir verilere dönüştürür. Program da tökezlediğinde yere kapanmak yerine neden tökezlediğini anlayıp yoluna devam eder.
