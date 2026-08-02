---
layout: post
title: "Rust’ta Kontrol Akışı: if-else, loop, while ve for"
math: true
categories: 
  - Bilgi
tags: 
  - Rust
  - Kontrol Akışı
  - Döngüler
---

Bir programın karar verebilmesi ve tekrarlanan işleri otomatikleştirebilmesi, kontrol akışı yapıları sayesinde mümkündür. Rust; `if-else`, `loop`, `while` ve `for` yapılarını tanıdık bir söz dizimiyle sunarken ifade tabanlı yaklaşımı, güvenli tür sistemi ve döngü etiketleri gibi kendine özgü özelliklerle işleri daha kontrollü hâle getirir.

``

## Kontrol akışının temel mantığı

Kontrol akışı, komutların hangi sırayla çalışacağını belirler. Bir koşulun sonucu doğruysa bir dal, yanlışsa başka bir dal çalıştırılabilir. Koşulu $C$ ile gösterirsek seçim mantığı şöyle özetlenebilir:

$$
Akış(C) = \begin{cases}
A, & C = true \\
B, & C = false
\end{cases}
$$

Döngülerde ise bir işlem belirli sayıda ya da bir koşul sağlandığı sürece tekrarlanır. Yaklaşık toplam işlem sayısı, iterasyon sayısı $n$ ve her iterasyonun maliyeti $k$ olmak üzere $T = n \cdot k$ şeklinde düşünülebilir.

## `if-else`: Parantezsiz fakat kesin kararlar

Rust’ta `if` koşulunun çevresine parantez koymak gerekmez. Buna karşılık koşul mutlaka `bool` olmalıdır; C gibi dillerdeki `if (1)` yaklaşımı geçerli değildir.

```rust
fn main() {
    let sicaklik = 27;

    if sicaklik > 30 {
        println!("Hava oldukça sıcak!");
    } else if sicaklik >= 20 {
        println!("Hava gayet güzel.");
    } else {
        println!("Montu unutma!");
    }
}
```

Rust’ta `if` yalnızca bir komut değil, aynı zamanda değer üreten bir ifadedir. Bu nedenle sonucu doğrudan değişkene atayabiliriz:

```rust
let puan = 75;
let sonuc = if puan >= 50 { "Geçti" } else { "Kaldı" };
```

Buradaki dalların uyumlu türler üretmesi gerekir. Bir dal `&str`, diğer dal sayı döndürürse derleyici buna izin vermez. Rust adeta “Kararını ver ama türünü değiştirme!” der.

## Döngü ailesini tanıyalım

| Yapı | Kullanım amacı | Koşul | Rust’a özgü avantaj |
|---|---|---|---|
| `loop` | Belirsiz süreli tekrar | Doğrudan yok | `break` ile değer döndürebilir |
| `while` | Koşula bağlı tekrar | Her turda denetlenir | Açık ve okunabilir kontrol |
| `for` | Koleksiyon veya aralık gezme | Iterator tarafından yönetilir | Güvenli ve sınır kontrollü |

### `loop`: Sonsuza kadar, aksi söylenene dek

`loop`, açıkça durdurulmadığında sonsuz çalışan döngüdür. Rust’ın ilginç özelliği, `break` üzerinden döngüden değer alınabilmesidir:

```rust
let mut sayac = 0;

let sonuc = loop {
    sayac += 1;

    if sayac == 5 {
        break sayac * 10;
    }
};

println!("Sonuç: {sonuc}");
```

Bu kodda döngü sona erdiğinde `sonuc` değeri `50` olur. `continue` ise mevcut turun kalanını atlayıp sonraki iterasyona geçer.

### `while`: Koşul doğru olduğu sürece

Kaç tekrar yapılacağı önceden bilinmiyorsa ancak devam koşulu belliyse `while` uygundur:

```rust
let mut enerji = 3;

while enerji > 0 {
    println!("Çalışıyor! Enerji: {enerji}");
    enerji -= 1;
}
```

Koşul başlangıçta yanlışsa gövde hiç çalışmaz. Ayrıca koşulda kullanılan değişkeni güncellemeyi unutmak, istemeden sonsuz döngü oluşturabilir.

### `for`: Rust’ın gözde döngüsü

Rust’ta koleksiyonları ve aralıkları dolaşmak için çoğunlukla `for` tercih edilir:

```rust
let diller = ["Rust", "Go", "Python"];

for (indeks, dil) in diller.iter().enumerate() {
    println!("{indeks}: {dil}");
}

for sayi in 1..=3 {
    println!("{sayi}");
}
```

`1..=3` aralığı 3’ü içerirken `1..3` yalnızca 1 ve 2’yi içerir. `for`, elle indeks kullanmaya göre sınır aşımı riskini azaltır ve iterator optimizasyonlarından yararlanır.

## İç içe döngüler ve etiketler

Rust, hangi döngünün kırılacağını belirtmek için `'etiket` söz dizimini kullanır:

```rust
'dis: for x in 1..=3 {
    for y in 1..=3 {
        if x * y == 6 {
            break 'dis;
        }
        println!("{x} x {y}");
    }
}
```

Sonuç olarak koşullu seçimlerde `if-else`, değer üretmekte `loop`, koşullu tekrarlarda `while`, koleksiyon gezilerinde ise `for` öne çıkar. Doğru yapıyı seçmek kodu yalnızca çalışır değil, Rust’ın ruhuna uygun biçimde güvenli ve okunabilir de yapar.
