---
layout: post
title: "Rust'ta Enum ve Pattern Matching: Tüm Olasılıkları Yakalamak"
math: true
categories: 
  - Bilgi
tags: 
  - Rust
  - Enum
  - Pattern Matching
---

Bir verinin yalnızca tek bir biçimi olmak zorunda değildir. Örneğin bir ödeme başarılı, reddedilmiş veya hâlâ bekliyor olabilir. Bu durumları metinlerle temsil etmek mümkün olsa da küçük bir yazım hatası programın mantığını bozabilir. Rust'ın `enum` ve `match` araçları, farklı veri varyasyonlarını güvenli biçimde modelleyerek derleyiciyi adeta hata avlayan bir ekip arkadaşına dönüştürür.
``

## Enum neden gereklidir?

Enum, bir değerin önceden belirlenmiş varyasyonlardan **yalnızca biri** olabileceğini ifade eden veri tipidir. Matematiksel olarak bir enum'u ayrık birleşim biçiminde düşünebiliriz:

$$Durum = Bekliyor \;|\; Basarili \;|\; Reddedildi$$

Buradaki $|$ işareti, “bu seçeneklerden biri” anlamına gelir. Her varyasyon kendi verisini de taşıyabilir. Böylece yalnızca durumun adı değil, o durumla ilişkili bilgi de aynı yapı içinde güvenli şekilde saklanır.

```rust
enum OdemeDurumu {
    Bekliyor,
    Basarili { islem_no: String, tutar: f64 },
    Reddedildi(String),
}
```

Bu enum'da `Bekliyor` ek bilgi taşımaz. `Basarili`, işlem numarası ile tutarı; `Reddedildi` ise hata açıklamasını taşır. Birbirinden kopuk değişkenler oluşturmak yerine verinin şekli doğrudan tipe işlenmiştir.

| Yaklaşım | Tip güvenliği | Geçersiz durum riski | Ek veri taşıma |
|---|---:|---:|---:|
| Metin (`String`) | Düşük | Yüksek | Elle yönetilir |
| Sayısal kod | Orta | Orta | Ayrı değişken gerekir |
| `enum` | Yüksek | Düşük | Varyasyon içinde taşınır |

Metin kullanan bir sistemde `"başarılı"`, `"Başarılı"` ve yanlışlıkla yazılan `"başarlı"` farklı değerlerdir. Enum kullanıldığında ise derleyici yalnızca tanımlanmış varyasyonlara izin verir.

## Match ile varyasyonları açmak

`match`, bir enum değerini varyasyonlarına göre inceleyen ve uygun kod dalını çalıştıran ifadedir. Aynı zamanda varyasyonun içindeki verileri **desen eşleştirme** yoluyla çıkarabilir:

```rust
fn raporla(durum: OdemeDurumu) -> String {
    match durum {
        OdemeDurumu::Bekliyor => {
            String::from("Ödeme henüz tamamlanmadı.")
        }
        OdemeDurumu::Basarili { islem_no, tutar } => {
            format!("{} numaralı işlem tamamlandı: {:.2} TL", islem_no, tutar)
        }
        OdemeDurumu::Reddedildi(neden) => {
            format!("Ödeme reddedildi: {}", neden)
        }
    }
}
```

Burada `islem_no`, `tutar` ve `neden` değişkenleri yalnızca ilgili desen eşleştiğinde oluşturulur. Ayrıca `match` bir ifade olduğu için her dalın ürettiği `String`, fonksiyonun dönüş değeri olarak kullanılabilir.

## Eksiksizlik denetimi

Rust'taki `match` ifadesinin en güçlü özelliği **exhaustiveness**, yani eksiksizlik kontrolüdür. Enum'un varyasyon sayısı $n$ ise güvenli bir eşleştirme bütün olasılık kümesini kapsamalıdır:

$$Kapsanan\ Varyasyonlar = n$$

Örneğin `Reddedildi` dalını silersek kod derlenmez. Derleyici, hangi desenin eksik olduğunu bildirir. Daha sonra enum'a `IadeEdildi` varyasyonu eklendiğinde de ilgili tüm `match` ifadeleri yeniden kontrol edilir. Böylece yeni bir özelliğin unutulmuş kod yolları oluşturması engellenir.

Genel bir yakalama için `_` deseni kullanılabilir:

```rust
match durum {
    OdemeDurumu::Basarili { tutar, .. } => println!("Kazanç: {tutar}"),
    _ => println!("Henüz kazanç oluşmadı."),
}
```

`..`, varyasyondaki kullanılmayan alanları yok sayar; `_` ise kalan bütün varyasyonları eşleştirir. Ancak `_` aşırı kullanılırsa enum'a sonradan eklenen varyasyonlar sessizce bu dala düşebilir. Kritik iş kurallarında varyasyonları açıkça yazmak daha güvenlidir.

## Koruyucular ve daha hassas desenler

Desenlere `if` koruyucuları eklenerek aynı varyasyon farklı koşullara ayrılabilir:

```rust
match durum {
    OdemeDurumu::Basarili { tutar, .. } if tutar >= 10_000.0 => {
        println!("Yüksek tutarlı işlem kontrol edilmeli.");
    }
    OdemeDurumu::Basarili { tutar, .. } => println!("Onaylanan tutar: {tutar}"),
    OdemeDurumu::Bekliyor => println!("Bekleniyor..."),
    OdemeDurumu::Reddedildi(neden) => println!("Hata: {neden}"),
}
```

Enum verinin hangi biçimlerde bulunabileceğini, `match` ise her biçimde ne yapılacağını tanımlar. İkisi birlikte kullanıldığında geçersiz durumlar azalır, dallanma mantığı okunabilir hâle gelir ve unutulan olasılıklar çalışma zamanına ulaşmadan yakalanır. Kısacası derleyici yalnızca kodu çevirmekle kalmaz; olasılıkları sizinle birlikte sayar.
