---
layout: post
title: "Rust Ownership Sistemi: Çöp Toplayıcı Olmadan Güvenli Bellek Yönetimi"
math: true
categories: 
  - Bilgi
tags: 
  - rust
  - ownership
  - bellek-yönetimi
---

Rust öğrenmeye başlayanların karşısına çıkan ilk büyük bölüm sonu canavarı **ownership**, yani sahiplik sistemidir. İlk bakışta derleyicinin değişkenlerinize gereğinden fazla karıştığını düşünebilirsiniz. Oysa bu sistem; çöp toplayıcı kullanmadan bellek güvenliği sağlamak, sarkan işaretçileri önlemek ve kaynakların ne zaman temizleneceğini kesin biçimde belirlemek için tasarlanmıştır.

``

## Sahiplik neden gerekli?

Programlar çalışırken verileri çoğunlukla **stack** ve **heap** adlı iki bellek alanında tutar. Boyutu derleme zamanında bilinen ve hızlı erişilen değerler genellikle stack üzerinde bulunur. Çalışma sırasında büyüyebilen `String` gibi yapılar ise verilerini heap üzerinde saklar.

Heap belleğinin yönetilmesi gerekir. Bellek erken temizlenirse geçersiz bir adrese erişilebilir; hiç temizlenmezse bellek sızıntısı oluşur. Rust bu problemi sahiplik kurallarıyla çözer:

1. Rust'taki her değerin bir sahibi vardır.
2. Bir değerin aynı anda yalnızca bir sahibi olabilir.
3. Sahip kapsam dışına çıktığında değer otomatik olarak temizlenir.

Bir kaynağın yaşam süresini kabaca şöyle ifade edebiliriz:

$$T_{kaynak} = T_{scope\ sonu} - T_{oluşturulma}$$

Kaynağın sahibi kapsamdan çıktığında Rust, `drop` mekanizmasını çalıştırır ve heap belleğini serbest bırakır. Böylece geliştiricinin elle `free` çağırması gerekmez.

| Yaklaşım | Bellek temizliği | Çalışma zamanı maliyeti | Yaygın risk |
|---|---|---:|---|
| C/C++ manuel yönetim | Programcı yapar | Düşük | Sızıntı, çift temizleme |
| Garbage Collector | Çöp toplayıcı yapar | Değişken | Duraklama ve ek yük |
| Rust ownership | Kapsam sonunda otomatik | Çok düşük | Derleme zamanı hataları |

## Taşıma: Değer yeni sahibine gidiyor

Aşağıdaki örnekte heap üzerinde veri tutan bir `String` oluşturulur:

```rust
fn main() {
    let mesaj = String::from("Merhaba Rust!");
    let yeni_sahip = mesaj;

    println!("{}", yeni_sahip);
}
```

`mesaj`, `yeni_sahip` değişkenine atandığında veri varsayılan olarak kopyalanmaz; sahiplik **taşınır**. Bu işlemden sonra `mesaj` kullanılamaz. Rust böylece iki değişkenin aynı heap alanını temizlemeye çalışmasını engeller.

```rust
let mesaj = String::from("Selam");
let yeni_sahip = mesaj;
println!("{}", mesaj); // Derleme hatası!
```

Bu davranış ilk başta katı görünür, fakat olası bir **double free** hatasını program çalışmadan yakalar. Gerçek bir kopya gerekiyorsa `clone` kullanılabilir:

```rust
let ilk = String::from("Rust");
let ikinci = ilk.clone();

println!("{} ve {}", ilk, ikinci);
```

`clone`, heap verisini de çoğalttığı için maliyeti yaklaşık veri boyutuyla büyür: $C_{clone} = O(n)$. Bu nedenle yalnızca gerçekten bağımsız bir kopya gerektiğinde tercih edilmelidir.

## Copy türleri neden farklı davranır?

Tamsayı, boolean ve karakter gibi boyutu sabit basit türler `Copy` özelliğini uygular. Bunlar stack üzerinde ucuz biçimde kopyalanır:

```rust
let x = 42;
let y = x;
println!("x = {x}, y = {y}");
```

| İşlem | `i32` | `String` |
|---|---|---|
| Atama davranışı | Kopyalama | Sahipliği taşıma |
| Eski değişken kullanılabilir mi? | Evet | Hayır |
| Heap tahsisi | Yok | Genellikle var |
| Bağımsız kopya yöntemi | Otomatik | `clone()` |

## Fonksiyonlar da sahipliği etkiler

Bir değeri fonksiyona vermek de atama gibi taşıma gerçekleştirebilir:

```rust
fn yazdir(metin: String) {
    println!("{metin}");
} // metin burada temizlenir

fn main() {
    let not = String::from("Ownership çalışıyorum");
    yazdir(not);
}
```

Çağrıdan sonra `not` artık kullanılamaz. Değeri tüketmeden paylaşmak için referans, yani **borrowing**, kullanılabilir:

```rust
fn yazdir(metin: &String) {
    println!("{metin}");
}

fn main() {
    let not = String::from("Rust artık daha mantıklı!");
    yazdir(&not);
    println!("{not}");
}
```

Buradaki `&not`, sahipliği devretmeden geçici erişim verir. Kısacası ownership Rust'ın geliştiriciye çıkardığı bir engel değil, derleme zamanında çalışan dikkatli bir bellek güvenliği asistanıdır. Kurallar öğrenildiğinde derleyiciyle kavga etmek yerine onunla takım arkadaşı olmaya başlarsınız.
