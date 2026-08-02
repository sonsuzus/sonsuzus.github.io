---
layout: post
title: "Veri Tipleri, Bellek Boyutları ve Tip Çıkarımının Perde Arkası"
math: true
categories: 
  - Bilgi
tags: 
  - veri tipleri
  - tip çıkarımı
  - bellek yönetimi
---

Bir değişkeni yalnızca “değer saklayan kutu” olarak düşünmek kolaydır; ancak derleyici için bu kutunun biçimi, kapasitesi ve hangi işlemlere izin verdiği de önemlidir. Tam sayılar, ondalık sayılar ve mantıksal değerler tek bir veriyi temsil ederken; diziler ve demetler birden fazla değeri düzenli biçimde bir araya getirir. Statik tip analizi ise program çalışmadan önce bu yapıların uyumlu kullanılıp kullanılmadığını denetleyen görünmez bir güvenlik görevlisi gibidir.

``

## Skaler veri tipleri

Skaler tipler tek bir değeri temsil eder. Bir tipin bellek boyutu, dilin kurallarına ve hedef mimariye bağlıdır. Örneğin Rust'taki `i32` her zaman 32 bit iken C dilindeki `int` için standart kesin bir bit sayısı garanti etmez.

| Tip | Örnek | Yaygın boyut | Açıklama |
|---|---:|---:|---|
| Tam sayı | `i32` | 4 bayt | İşaretsiz veya işaretli olabilir |
| Ondalık | `f64` | 8 bayt | IEEE 754 kayan nokta gösterimi kullanır |
| Mantıksal | `bool` | Genellikle 1 bayt | `true` veya `false` taşır |
| Karakter | Rust `char` | 4 bayt | Bir Unicode skaler değerini temsil eder |

Bit sayısı $n$ olan işaretsiz bir tam sayının değer aralığı

$$0 \leq x \leq 2^n-1$$

şeklindedir. İşaretli ve ikinin tümleyeni kullanılan bir sayı için yaklaşık aralık ise

$$-2^{n-1} \leq x \leq 2^{n-1}-1$$

olur. Dolayısıyla `u8`, 0 ile 255 arasında değer saklarken `i8`, -128 ile 127 arasını kapsar. Aynı 1 bayt, farklı yorum; belleğin küçük bir kimlik krizi!

## Bileşik tipler: Demet ve dizi

Dizi, aynı tipte ve sabit sayıda elemanı ardışık biçimde saklar. Eleman boyutu $s$, eleman sayısı $k$ ise temel dizi boyutu

$$B = k \times s$$

olarak hesaplanır. Dört adet `i32` içeren bir dizi, ek metadata bulunmadığı durumda $4 \times 4=16$ bayttır.

Demet ise farklı tipleri tek yapıda birleştirebilir. `(i32, bool, f64)` bunun tipik örneğidir. Teorik toplam 13 bayt görünse de işlemci hizalama kuralları nedeniyle aralara **padding** eklenebilir ve gerçek boyut 16 bayt olabilir.

| Özellik | Dizi | Demet |
|---|---|---|
| Eleman tipleri | Aynı | Farklı olabilir |
| Uzunluk | Sabit | Sabit |
| Erişim | İndeksle | Konum veya parçalama ile |
| Boyut hesabı | Genellikle çarpım | Toplam ve olası padding |

## Tip çıkarımı nasıl çalışır?

Statik tipli dillerde derleyici, değişkenlerin tiplerini çalışma zamanından önce belirler. Bunun için başlangıç değerlerini, operatörleri, fonksiyon imzalarını ve kullanım bağlamını inceler. Bu sürece **tip çıkarımı** denir.

```rust
fn main() {
    let adet = 12;             // Kullanımdan i32 çıkarılır.
    let oran = 2.5;            // Varsayılan olarak f64 olur.
    let aktif = true;          // bool
    let koordinat = (10, 4.5); // (i32, f64) demeti
    let puanlar = [80, 90, 75];// [i32; 3] dizisi

    let toplam = adet + puanlar[0];
    println!("Toplam: {toplam}, aktif: {aktif}");
}
```

Derleyici `adet` ile `puanlar[0]` değerlerinin uyumlu olduğunu görür ve toplama işlemine izin verir. Buna karşılık `adet + oran` ifadesi Rust'ta doğrudan geçerli değildir; çünkü `i32` ile `f64` kendiliğinden birleştirilmez. Açık dönüşüm gerekir:

```rust
let sonuc = adet as f64 + oran;
```

Bu katılık gereksiz bürokrasi değil, veri kaybını ve belirsiz davranışı önleyen bir kontroldür. Tip denetleyici kabaca her ifadeye bir tip atar, kısıtlar üretir ve bu kısıtların çelişip çelişmediğini sınar. Örneğin $T(adet)=i32$ ve toplama operatörü iki eş tip bekliyorsa diğer operandın da `i32` olması gerekir.

## Neden önemli?

Sabit boyut bilgisi derleyicinin yığın belleğini düzenlemesini, dizilerde doğru adresi hesaplamasını ve verimli makine kodu üretmesini sağlar. Statik analiz de yanlış tipe işlem uygulama, hatalı fonksiyon çağrısı ve uyumsuz atama gibi sorunları program çalışmadan yakalar. Kısacası veri tipi yalnızca bir etiket değil; bellek yerleşimi, geçerli işlemler ve program güvenliği arasında yapılan güçlü bir sözleşmedir.
