---
layout: post
title: "Rust Felsefesi ve Bellek Güvenliği: Çöp Toplayıcı Olmadan Güvenli Sistem Programlama"
math: true
categories: 
  - Bilgi
tags: 
  - Rust
  - Bellek Güvenliği
  - Sistem Programlama
---

C ve C++, programcıya belleğin anahtarlarını teslim eder; fakat anahtarlığın yanında kullanım kılavuzu vermez. Rust ise aynı donanım kontrolünü korurken “Bu bellek hâlâ geçerli mi?” sorusunu çalışma anına bırakmak yerine derleme sırasında yanıtlamaya çalışır. Üstelik bunu kodun arkasında dolaşan bir garbage collector olmadan gerçekleştirir.
``

## Sorun belleği ayırmak değil, doğru zamanda bırakmaktır

C dilinde `malloc` ile ayrılan alanın `free` ile serbest bırakılması programcının sorumluluğundadır. Serbest bırakma unutulursa bellek sızıntısı, erken yapılırsa use-after-free, iki kez yapılırsa double-free ortaya çıkabilir. C++ bu yükü RAII ve akıllı işaretçilerle azaltır; ancak ham işaretçiler ve karmaşık sahiplik ilişkileri hâlâ hata alanı oluşturur.

Rust’ın yaklaşımı üç temel kavrama dayanır:

1. **Ownership (sahiplik):** Her değerin tek bir sahibi vardır.
2. **Borrowing (ödünç alma):** Değere sahiplik aktarılmadan referansla erişilebilir.
3. **Lifetime (yaşam süresi):** Referans, işaret ettiği değerden daha uzun yaşayamaz.

Bir değerin kapsamı sona erdiğinde Rust otomatik olarak `drop` çağırır. Bu işlem çalışma zamanında izleme yapan bir çöp toplayıcıya değil, derleyicinin önceden doğruladığı deterministik kurallara dayanır.

Bellek kullanımını kabaca şöyle düşünebiliriz:

$$M_{aktif} = M_{ayrılan} - M_{serbest\ bırakılan}$$

Rust, sahip kapsamdan çıktığında serbest bırakma işlemini otomatik üretir. Böylece programcının her çıkış yolunda manuel temizlik yazması gerekmez.

| Özellik | C | C++ | Rust |
|---|---|---|---|
| Bellek yönetimi | Manuel | RAII + manuel seçenekler | Ownership + RAII |
| Garbage collector | Yok | Yok | Yok |
| Use-after-free koruması | Yok | Kısmi | Derleme zamanında |
| Veri yarışı koruması | Yok | Kısmi | Güvenli kodda derleme zamanında |
| Ham işaretçi | Doğrudan | Doğrudan | `unsafe` içinde |
| Serbest bırakma zamanı | Programcı belirler | Genellikle deterministik | Deterministik |

## Sahiplik aktarımı

Aşağıdaki örnekte heap üzerinde tutulan metnin sahipliği `mesaj` değişkeninden `yazdir` fonksiyonuna aktarılır:

```rust
fn yazdir(metin: String) {
    println!("{metin}");
} // metin kapsamdan çıkar ve bellek bırakılır

fn main() {
    let mesaj = String::from("Merhaba Rust!");
    yazdir(mesaj);

    // println!("{mesaj}"); // Derleme hatası: değer taşındı
}
```

Derleyici son satıra izin vermez; çünkü `mesaj` artık belleğin sahibi değildir. C veya C++ dünyasında bu tür bir hata geçersiz işaretçi erişimine dönüşebilirken Rust programı daha çalışmadan durdurur.

Veriyi tüketmeden kullanmak için ödünç alma tercih edilir:

```rust
fn uzunluk(metin: &String) -> usize {
    metin.len()
}

fn main() {
    let mesaj = String::from("Ferris iş başında");
    let sonuc = uzunluk(&mesaj);
    println!("{mesaj}: {sonuc} karakter");
}
```

Buradaki `&String`, sahipliği almayan değişmez bir referanstır. Borrow checker genel olarak aynı anda ya çok sayıda değişmez referansa ya da yalnızca bir değişebilir referansa izin verir:

$$N_{mutable}=1 \Rightarrow N_{immutable}=0$$

Bu kural, eş zamanlı programlarda veri yarışlarının önemli bir bölümünü engeller.

## Rust bellek sızıntısını tamamen imkânsız mı yapar?

Hayır; önemli bir nüans burada saklıdır. Rust, bellek sızıntısını **bellek güvenliği ihlali** saymaz. `Rc` ile döngüsel referanslar kurulması veya `std::mem::forget` kullanılması belleğin serbest bırakılmamasına yol açabilir. Buna karşın güvenli Rust kodunda sızan belleğe geçersiz biçimde erişilmez; use-after-free ve double-free gibi daha tehlikeli sonuçlar önlenir.

Döngüsel yapılarda güçlü bağlantılardan biri `Weak` referansa çevrilerek sayaç döngüsü kırılabilir. Dolayısıyla Rust’ın vaadi “hiç bellek sızmaz” değil, “belleğin yaşam süresi kuralları ihlal edilerek tanımsız davranış üretilmez” şeklinde okunmalıdır.

## Güvenlik ile kontrolün uzlaşması

Rust sıfır maliyetli soyutlamaları benimser: Kullanılmayan çalışma zamanı denetimleri programa eklenmez ve ownership kontrollerinin çoğu derleme sırasında tamamlanır. Gerektiğinde `unsafe`, ham işaretçiler ve FFI aracılığıyla düşük seviyeli kontrol sağlanır; ancak riskli bölge görünür biçimde sınırlandırılır.

Sonuç olarak Rust, programcıdan kontrolü almak yerine kontrolün sorumluluğunu kurallara bağlar. Derleyici zaman zaman huysuz bir ekip arkadaşı gibi görünse de üretimde gece yarısı çalan hata alarmından çok daha naziktir.
