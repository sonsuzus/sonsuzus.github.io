---
layout: post
title: "Rust’ta Yaşam Süreleri: Dangling Referanslara Derleyici Freni"
math: true
categories: 
  - Bilgi
tags: 
  - Rust
  - Lifetimes
  - Bellek Güvenliği
---

Bir referans, işaret ettiği değer ortadan kalktıktan sonra kullanılmaya çalışılırsa ortaya **dangling reference** çıkar. C ve C++ gibi dillerde bu hata bazen program çalışana, hatta üretim ortamında gizemli bir çöküş yaşanana kadar fark edilmez. Rust ise yaşam sürelerini derleme aşamasında çözümleyerek “Bu referans hâlâ geçerli mi?” sorusunu program çalışmadan cevaplar.
``
## Yaşam süresi nedir?

Bir değerin **lifetime** yani yaşam süresi, o değerin bellekte geçerli olduğu program bölgesidir. Referansın yaşam süresi ise referansın kullanılabileceği aralığı ifade eder. Rust’ın temel kuralı oldukça nettir: Bir referans, işaret ettiği değerden daha uzun süre yaşayamaz.

Bir referansın kullanım aralığını $L_r$, referans verilen değerin geçerlilik aralığını $L_v$ ile gösterirsek güvenli kullanım koşulu şöyledir:

$$L_r \subseteq L_v$$

Yani referansın yaşam süresi, değerin yaşam süresinin alt kümesi olmalıdır. Rust derleyicisindeki **borrow checker**, sahiplik ve ödünç alma bilgileriyle birlikte bu ilişkiyi denetler.

| Kavram | Ne anlatır? | Derleyicinin kontrolü |
|---|---|---|
| Ownership | Değerden kimin sorumlu olduğunu | Aynı değerin yanlışlıkla iki kez serbest bırakılmasını önler |
| Borrowing | Değer taşınmadan referans alınmasını | Paylaşımlı ve değiştirilebilir erişimleri sınırlar |
| Lifetime | Referansın ne kadar kullanılabileceğini | Referansın değerden uzun yaşamasını engeller |

## Dangling referans nasıl yakalanır?

Aşağıdaki fonksiyon, yerel bir `String` değerine referans döndürmeye çalışır:

```rust
fn gecersiz_referans() -> &String {
    let mesaj = String::from("Merhaba!");
    &mesaj
}
```

`mesaj`, fonksiyon tamamlandığında bellekten kaldırılır. Döndürülen referans ise artık var olmayan bir değeri gösterecektir. Rust bu kodu derlemez; çünkü fonksiyon dönüşünden sonra referansın güvenli olabileceği bir yaşam süresi bulunamaz. Başka bir deyişle referans kapıdan çıkmak isterken sahibi montunu alıp çoktan eve gitmiştir.

Çözüm, değerin sahipliğini döndürmektir:

```rust
fn gecerli_deger() -> String {
    let mesaj = String::from("Merhaba!");
    mesaj // Sahiplik çağıran koda taşınır.
}
```

Burada `String` taşındığı için veri fonksiyon sonunda yok edilmez; yeni sahibi çağıran kod olur.

## Lifetime annotation ne işe yarar?

Derleyici çoğu yaşam süresini **lifetime elision** kurallarıyla kendisi çıkarır. Ancak bir fonksiyon birden fazla referans alıp referans döndürüyorsa aradaki ilişkinin açıkça belirtilmesi gerekebilir:

```rust
fn uzun_olan<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() >= y.len() { x } else { y }
}
```

`'a`, referansların sonsuza kadar yaşayacağını söylemez. Dönen referansın, `x` ve `y` için ortak olan en kısa geçerli yaşam süresiyle sınırlı olduğunu belirtir. Matematiksel olarak dönüş süresi yaklaşık şu ilişkiyi izler:

$$L_{sonuc} \subseteq L_x \cap L_y$$

Bu nedenle sonuç, girdilerden biri kapsam dışına çıktıktan sonra kullanılamaz.

| Yaklaşım | Kontrol zamanı | Olası sonuç |
|---|---|---|
| Ham işaretçi ağırlıklı model | Çoğunlukla çalışma zamanı veya geliştirici sorumluluğu | Use-after-free ve belirsiz davranış |
| Çöp toplayıcı | Çalışma zamanı | Ek çalışma zamanı maliyeti |
| Rust lifetimes | Derleme zamanı | Hata daha program çalışmadan reddedilir |

## Non-Lexical Lifetimes

Modern Rust, **Non-Lexical Lifetimes (NLL)** kullanır. Böylece bir referansın ömrü yalnızca süslü parantezlere göre değil, son gerçek kullanımına göre hesaplanır:

```rust
let mut sayilar = vec![1, 2, 3];
let ilk = &sayilar[0];
println!("{ilk}"); // `ilk` burada son kez kullanılıyor.
sayilar.push(4);   // Artık değiştirilebilir erişim güvenli.
```

Eski ve daha kaba bir kapsam analizi, `ilk` değişkenini bloğun sonuna kadar etkin kabul edebilirdi. NLL ise veri akışını inceleyerek ödünç almanın `println!` sonrasında bittiğini anlar.

Sonuç olarak lifetimes, belleği ne zaman temizleyeceğinizi belirleyen bir çöp toplayıcı değildir. Referanslar ile sahip olunan değerler arasındaki geçerlilik ilişkisini kanıtlayan statik bir sistemdir. İlk bakışta apostroflarla dolu küçük bir bilmece gibi görünse de karşılığında dangling referansları, use-after-free hatalarını ve gece yarısı gelen “sunucu neden çöktü?” mesajlarını büyük ölçüde daha kod çalışmadan durdurur.
