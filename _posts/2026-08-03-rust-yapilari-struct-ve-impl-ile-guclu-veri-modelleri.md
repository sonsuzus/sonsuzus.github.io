---
layout: post
title: "Rust Yapıları: Struct ve impl ile Güçlü Veri Modelleri"
math: true
categories: 
  - Bilgi
tags: 
  - Rust
  - Struct
  - Veri Modelleme
---

Bir uygulamada kullanıcı adı, yaş, e-posta adresi ve aktiflik durumu gibi birbirleriyle ilişkili değerleri ayrı değişkenlerde tutmak mümkündür. Ancak proje büyüdükçe bu yaklaşım, çekmeceleri etiketlenmemiş bir dolaba dönüşür. Rust dilindeki `struct` yapıları, farklı tiplerdeki verileri anlamlı bir isim altında birleştirerek kendi veri tiplerimizi oluşturmamızı sağlar.
``
## Struct Nedir?

`struct`, belirli bir kavramı temsil eden alanların tek bir veri tipi altında toplanmasıdır. Örneğin bir kullanıcı; metin biçiminde ada, sayısal yaşa ve mantıksal aktiflik durumuna sahip olabilir. Bu değerlerin tipleri farklı olsa da aynı varlığı tanımlar.

Matematiksel açıdan bir yapı, farklı kümelerin Kartezyen çarpımından seçilen bir kayıt gibi düşünülebilir:

$$Kullanici = String \times u8 \times String \times bool$$

Buradaki her kullanıcı, bu kümelerden gelen değerlerin oluşturduğu bir bütündür. Struct kullanmak yalnızca verileri paketlemez; alan adları sayesinde verinin anlamını da kodun içine taşır.

| Yaklaşım | Avantaj | Dezavantaj |
|---|---|---|
| Ayrı değişkenler | Küçük örneklerde hızlıdır | İlişkiler kolayca kaybolur |
| Tuple | Değerleri gruplar | Alanların anlamı belirsiz olabilir |
| Struct | İsimlendirilmiş ve güvenli model sunar | Önceden tip tanımı gerektirir |

## İlk Yapımızı Tanımlayalım

Aşağıdaki yapı, bir uygulama kullanıcısını modellemektedir:

```rust
struct Kullanici {
    ad: String,
    yas: u8,
    eposta: String,
    aktif: bool,
}

fn main() {
    let kullanici = Kullanici {
        ad: String::from("Ada"),
        yas: 28,
        eposta: String::from("ada@example.com"),
        aktif: true,
    };

    println!("Kullanıcı: {}", kullanici.ad);
}
```

Her alanın tipi derleme zamanında bellidir. Örneğin `yas` alanına yanlışlıkla bir metin atanırsa Rust programı çalıştırmadan önce hata verir. Bu özellik, veri modelini aynı zamanda bir güvenlik sözleşmesine dönüştürür.

Bir örneğin değiştirilebilmesi için tamamının `mut` olarak tanımlanması gerekir:

```rust
let mut kullanici = Kullanici {
    ad: String::from("Ece"),
    yas: 24,
    eposta: String::from("ece@example.com"),
    aktif: false,
};

kullanici.aktif = true;
```

Rust, yalnızca tek bir alanı `mut` yapmaya izin vermez. Değişebilirlik struct örneğinin tamamına aittir.

## impl ile Yapıya Davranış Kazandırmak

Veri modellemek çoğu zaman yeterli değildir; modelin davranışları da olmalıdır. `impl` bloğu, belirli bir struct için metot ve ilişkili fonksiyon tanımlamamızı sağlar.

```rust
impl Kullanici {
    fn yeni(ad: String, yas: u8, eposta: String) -> Self {
        Self {
            ad,
            yas,
            eposta,
            aktif: true,
        }
    }

    fn yetiskin_mi(&self) -> bool {
        self.yas >= 18
    }

    fn devre_disi_birak(&mut self) {
        self.aktif = false;
    }
}
```

`yeni`, bir ilişkili fonksiyondur; çağrılmak için mevcut bir nesneye ihtiyaç duymaz. `Self`, `Kullanici` tipinin kısa yazımıdır. `yetiskin_mi` metodu `&self` ile veriyi yalnızca ödünç alır. `devre_disi_birak` ise `&mut self` kullandığı için örneği değiştirebilir.

| Alıcı | Yetki | Tipik kullanım |
|---|---|---|
| `&self` | Salt okunur erişim | Bilgi sorgulama |
| `&mut self` | Değiştirme | Durum güncelleme |
| `self` | Sahipliği devralma | Nesneyi tüketme |
| Alıcı yok | Örneğe ihtiyaç duymaz | Kurucu fonksiyon |

Metotlar şu şekilde kullanılabilir:

```rust
let mut kisi = Kullanici::yeni(
    String::from("Mert"),
    20,
    String::from("mert@example.com"),
);

println!("Yetişkin mi? {}", kisi.yetiskin_mi());
kisi.devre_disi_birak();
```

## Neden Önemlidir?

İyi tasarlanmış bir struct, programın iş kurallarını görünür hâle getirir. Kullanıcı, ürün, sipariş veya oyun karakteri gibi kavramlar; alanları ve davranışlarıyla bağımsız modellere dönüşür. Böylece fonksiyonlara uzun parametre listeleri taşımak yerine tek ve anlamlı bir değer gönderilir.

Struct ve `impl` birlikteliği, Rust'ta veri ile davranış arasında düzenli bir bağ kurar. Sonuç; okunabilir, tip güvenli ve büyümeye hazır koddur. Kısacası struct verinin iskeletiyse, `impl` o iskelete hareket kazandıran kaslardır.
