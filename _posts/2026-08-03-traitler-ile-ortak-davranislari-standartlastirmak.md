---
layout: post
title: "Trait’ler ile Ortak Davranışları Standartlaştırmak"
math: true
categories: 
  - Bilgi
tags: 
  - Rust
  - Trait
  - Nesne Tabanlı Programlama
---

Bir uygulamada kuşlar uçar, uçaklar uçar, hatta yeterince kararlı bir geliştiricinin yazdığı kod bile bazen “uçar”. Bu nesneler birbirinden tamamen farklı veri yapılarına sahip olsa da ortak bir davranışı paylaşabilir. Rust’taki **trait** yapısı, farklı tiplerin sahip olması gereken yetenekleri ortak bir sözleşmeyle tanımlamamızı sağlar. Nesne tabanlı dillerdeki `interface` kavramına benzese de varsayılan metotlar, generic kısıtları ve güvenli çok biçimlilik gibi güçlü araçlarla daha geniş bir kullanım alanı sunar.

``

## Trait nedir?

Trait, bir veri tipinin hangi davranışları sağlayacağını bildiren metot imzaları bütünüdür. Buradaki önemli fikir, tipin **ne olduğundan** çok **ne yapabildiğiyle** ilgilenmektir. Örneğin bir `Kus` ve `Ucak` aynı alanlara sahip değildir; ancak ikisi de `Ucan` davranışını uygulayabilir.

Bir trait’i matematiksel bir sözleşme gibi düşünebiliriz. $T$ bir veri tipi, $D$ ise bir davranış kümesi olsun. Eğer $T$, gerekli bütün metotları sağlıyorsa şu ilişkiyi kurarız:

$$T \models D$$

Yani “$T$ tipi, $D$ davranış sözleşmesini karşılar” deriz. Böylece kodumuz somut tiplere değil, yeteneklere bağımlı hâle gelir.

| Özellik | Trait | Interface | Kalıtım |
|---|---|---|---|
| Ortak davranış tanımlar | Evet | Evet | Evet |
| Ortak veri alanı taşır | Hayır | Genellikle hayır | Evet |
| Birden fazla uygulanabilir | Evet | Evet | Dile bağlı |
| Varsayılan metot içerebilir | Evet | Dile bağlı | Evet |
| Tipler arasında güçlü bağ kurar | Hayır | Hayır | Evet |

## İlk trait’imizi yazalım

Aşağıdaki örnekte uçabilen nesneler için ortak bir şablon oluşturuyoruz:

```rust
trait Ucan {
    fn isim(&self) -> &str;
    fn hiz(&self) -> u32;

    fn bilgi_ver(&self) {
        println!("{} saatte {} km hızla uçuyor.", self.isim(), self.hiz());
    }
}

struct Kus {
    ad: String,
    ucus_hizi: u32,
}

impl Ucan for Kus {
    fn isim(&self) -> &str {
        &self.ad
    }

    fn hiz(&self) -> u32 {
        self.ucus_hizi
    }
}
```

`isim` ve `hiz` metotlarının uygulanması zorunludur. `bilgi_ver` ise varsayılan bir gövdeye sahiptir; isteyen tip bunu doğrudan kullanabilir, isteyen kendi sürümünü yazabilir. Böylece tekrar azaltılırken davranışın özelleştirilebilirliği korunur.

## Trait bound ile yetenek istemek

Generic bir fonksiyon her tipi kabul edebilir; fakat bazen “Her tip gelsin ama uçmayı bilsin!” demek isteriz. Bunun için **trait bound** kullanılır:

```rust
fn yarisa_kat<T: Ucan>(katilimci: &T) {
    println!("Yarışmacı: {}", katilimci.isim());
    katilimci.bilgi_ver();
}
```

Buradaki `T: Ucan`, `T` tipinin `Ucan` trait’ini uygulaması gerektiğini belirtir. Başka bir ifadeyle kabul edilen tipler kümesi şöyledir:

$$K = \{T \mid T \models Ucan\}$$

Bu kontrol derleme zamanında yapılır. Uçma davranışını sağlamayan bir tipi fonksiyona gönderirsek program henüz çalışmadan anlaşılır bir hata alırız.

Birden fazla koşul da tanımlanabilir:

```rust
fn raporla<T>(nesne: &T)
where
    T: Ucan + std::fmt::Debug,
{
    println!("{:?}", nesne);
    nesne.bilgi_ver();
}
```

Bu fonksiyon, tipin hem `Ucan` hem de `Debug` davranışlarını sağlamasını ister.

## Statik ve dinamik çok biçimlilik

Trait’ler iki temel biçimde kullanılabilir:

| Yaklaşım | Yazım | Özellik |
|---|---|---|
| Statik dispatch | `T: Ucan` | Hızlıdır, derleyici tipe özel kod üretir |
| Dinamik dispatch | `&dyn Ucan` | Farklı tipleri çalışma zamanında birleştirir |

`Vec<Box<dyn Ucan>>` kullanarak kuşları, uçakları ve başka uçan tipleri aynı koleksiyonda saklayabiliriz. Bunun küçük bir çalışma zamanı maliyeti vardır; buna karşılık esnek bir mimari sağlar.

Trait’lerin asıl gücü, “Bu nesne hangi sınıftan?” sorusunu geri plana atıp “Bu nesne hangi işleri yapabilir?” sorusunu öne çıkarmasıdır. Sonuçta daha gevşek bağlı, test edilebilir ve genişletilebilir kod elde edilir. Yeni bir tip eklemek için mevcut algoritmaları değiştirmek gerekmez; yalnızca ilgili davranış sözleşmesini uygulamak yeterlidir.
