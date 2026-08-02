---
layout: post
title: "Rust’ta Değişkenler: Varsayılan Değişmezlik ve mut Anahtar Kelimesi"
math: true
categories: 
  - Bilgi
tags: 
  - Rust
  - değişkenler
  - mutability
---

Rust’ta bir değişken tanımladığınızda, derleyici onu varsayılan olarak değişmez yani salt okunur kabul eder. İlk bakışta “Değişken değişmeyecekse neden adı değişken?” diye düşünebilirsiniz. Rust’ın cevabı nettir: Bir değerin değişmesi mümkün olabilir, fakat bu yetki açıkça verilmelidir. Böylece kodun hangi noktalarında durum değişikliği yaşanabileceği görünür hâle gelir ve sürprizlerin yerini bilinçli tercihler alır.

``

## Varsayılan davranış: Değişmezlik

Rust’ta değişkenler `let` anahtar kelimesiyle tanımlanır:

```rust
fn main() {
    let puan = 10;
    println!("Başlangıç puanı: {puan}");
}
```

Buradaki `puan` değişkenine bir kez değer atanmıştır. Aşağıdaki gibi ikinci bir atama yapmaya çalışırsak program derlenmez:

```rust
fn main() {
    let puan = 10;
    puan = 20; // Derleme hatası!
}
```

Derleyici, değişmez bir değişkene iki kez değer atanamayacağını bildirir. Bu kuralın amacı programcıyı kısıtlamak değil, verinin yaşam döngüsünü daha anlaşılır kılmaktır. Bir değerin değişmeyeceğini bilen derleyici ve kodu okuyan geliştirici, o değer hakkında daha güçlü varsayımlar yapabilir.

Matematiksel olarak değişmez bir atamayı şöyle düşünebiliriz:

$$x = 10 \Rightarrow x(t) = 10$$

Yani programın ilgili kapsamı boyunca zaman $t$ değişse bile $x$ aynı kalır. Değiştirilebilir durumda ise değer bir durum fonksiyonuna dönüşür:

$$x(t_0)=10, \quad x(t_1)=20$$

## Değişime bilinçli izin vermek: `mut`

Bir değişkenin gerçekten değişmesi gerekiyorsa `mut` anahtar kelimesi kullanılır. `mut`, İngilizce “mutable” kelimesinin kısaltmasıdır.

```rust
fn main() {
    let mut puan = 10;
    println!("İlk puan: {puan}");

    puan = puan + 5;
    println!("Yeni puan: {puan}");
}
```

Bu örnekte `puan` için değişiklik izni açıkça verilmiştir. `puan = puan + 5` satırı mevcut değeri okuyup beş ekler ve sonucu aynı değişkene yazar. Kodun başındaki `mut`, ilerleyen satırlarda durum değişikliği görebileceğimize dair küçük ama etkili bir uyarı levhasıdır.

| Özellik | `let` | `let mut` |
|---|---|---|
| Yeniden değer atanabilir mi? | Hayır | Evet |
| Varsayılan tercih mi? | Evet | Hayır |
| Niyeti açıklar mı? | Değer sabit kalacak | Değer değişebilir |
| Hata riskini azaltır mı? | Daha güçlü biçimde | Kontrollü kullanımda |

## Değişmezlik neden yararlıdır?

Değiştirilebilir durum, özellikle büyük uygulamalarda hataların önemli kaynaklarından biridir. Bir değişken farklı fonksiyonlar veya iş parçacıkları tarafından değiştirilebiliyorsa “Bu değer buraya nasıl geldi?” sorusu sıklaşır. Varsayılan değişmezlik şu avantajları sağlar:

- İstenmeyen atamaları derleme aşamasında yakalar.
- Kodun davranışını tahmin etmeyi kolaylaştırır.
- Eş zamanlı programlamada veri yarışlarının önlenmesine yardımcı olur.
- Gerçekten değişmesi gereken verileri görünür kılar.

Rust burada “Her şeyi kilitle” demez; “Önce kilitli kabul et, gerekiyorsa anahtarı bilinçli kullan” der.

## `mut` ile shadowing aynı şey değildir

Rust’ta aynı isimle yeni bir değişken oluşturmak da mümkündür. Buna shadowing denir:

```rust
fn main() {
    let veri = "42";
    let veri: i32 = veri.parse().expect("Sayı bekleniyordu");
    let veri = veri * 2;

    println!("Sonuç: {veri}");
}
```

Burada mevcut değişken değiştirilmez; her `let`, önceki ismi gölgeleyen yeni bir değişken oluşturur. Shadowing tür dönüşümüne de izin verirken `mut` kullanılan bir değişken genellikle aynı türde kalmalıdır.

| Yaklaşım | Yeni değişken oluşturur | Tür değişebilir | Yeniden atama yapar |
|---|---:|---:|---:|
| `let mut` | Hayır | Genellikle hayır | Evet |
| Shadowing | Evet | Evet | Hayır |

Pratik kural basittir: Değerin yaşamı boyunca güncellenmesi işin doğal parçasıysa `mut` kullanın; bir hesaplama aşamasından diğerine daha anlamlı veya farklı türde bir değer üretiyorsanız shadowing’i değerlendirin. Rust’ın varsayılan değişmezliği, kodunuzu katılaştıran bir engel değil, değişimin nerede gerçekleştiğini gösteren güçlü bir tasarım aracıdır.
