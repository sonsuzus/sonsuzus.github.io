---
layout: post
title: "WebAssembly ile Tarayıcıda Turbo Hızında Görüntü İşleme ve Video Kodlama"
math: true
categories: 
  - Proje
tags: 
  - WebAssembly
  - Rust
  - Görüntü İşleme
---

Tarayıcıda bir fotoğrafa filtre uygularken arayüzün donması veya video dönüştürürken fanların uçuşa geçmesi tanıdık geliyor mu? WebAssembly, hesaplama yoğun algoritmaları JavaScript’in tek başına zorlanabileceği noktalarda yüksek performansla çalıştırmamızı sağlar. Bu projede Rust ile yazılmış bir görüntü işleme çekirdeğini WebAssembly’ye derleyecek, JavaScript üzerinden çağıracak ve video kodlama seçeneklerini inceleyeceğiz.
``

## WebAssembly neden hızlıdır?

WebAssembly, kısaca Wasm, tarayıcıların çalıştırabildiği düşük seviyeli ve taşınabilir bir ikili komut formatıdır. Rust, C veya C++ kodu Wasm modülüne derlenebilir. JavaScript kaynak kodu çalışma sırasında analiz ve optimize edilirken Wasm daha öngörülebilir türlere ve bellek düzenine sahiptir.

Bir görüntü, çoğunlukla RGBA kanallarından oluşan doğrusal bir byte dizisi olarak düşünülebilir. Genişliği $W$, yüksekliği $H$ olan bir görüntü için işlenecek kanal sayısı yaklaşık olarak:

$$N = W \times H \times 4$$

olur. Her pikseli bir kez ziyaret eden gri tonlama algoritmasının zaman karmaşıklığı $O(W \times H)$ düzeyindedir. 4K görüntüde milyonlarca piksel bulunduğundan döngünün verimliliği ciddi fark yaratır.

| Yaklaşım | Güçlü yanı | Zayıf yanı | Uygun kullanım |
|---|---|---|---|
| JavaScript | Kolay geliştirme, DOM erişimi | Yoğun döngülerde dalgalı performans | Basit filtreler |
| WebAssembly | Hızlı ve öngörülebilir hesaplama | Veri aktarımı maliyetli olabilir | Filtre, codec, sıkıştırma |
| WebCodecs | Donanım hızlandırmalı medya erişimi | Tarayıcı desteği değişebilir | Gerçek zamanlı video |
| Sunucu tarafı | Güçlü donanım kullanılabilir | Yükleme süresi ve gizlilik sorunu | Büyük toplu işlemler |

## Rust ile görüntü çekirdeği

Önce Rust ortamına `wasm-pack` kurulur ve bir kütüphane projesi oluşturulur:

```bash
cargo install wasm-pack
cargo new --lib wasm-image-lab
cd wasm-image-lab
```

`Cargo.toml` dosyasına `wasm-bindgen` bağımlılığı eklenir. Ardından RGBA tamponunu yerinde değiştiren fonksiyon yazılır:

```rust
use wasm_bindgen::prelude::*;

#[wasm_bindgen]
pub fn grayscale(pixels: &mut [u8]) {
    for rgba in pixels.chunks_exact_mut(4) {
        let gray = (0.2126 * rgba[0] as f32
            + 0.7152 * rgba[1] as f32
            + 0.0722 * rgba[2] as f32) as u8;

        rgba[0] = gray;
        rgba[1] = gray;
        rgba[2] = gray;
    }
}
```

Katsayıların eşit olmamasının nedeni insan gözünün yeşile daha duyarlı olmasıdır. Parlaklık yaklaşık olarak $Y=0.2126R+0.7152G+0.0722B$ formülüyle hesaplanır. Alfa kanalı değiştirilmediği için saydamlık korunur.

Modülü web hedefi için derleyelim:

```bash
wasm-pack build --target web --release
```

`--release`, derleyici optimizasyonlarını etkinleştirir. Geliştirme sırasında hızlı derleme için kaldırılabilir; performans ölçümünde mutlaka kullanılmalıdır.

## Canvas ile Wasm bağlantısı

JavaScript tarafında görüntüyü Canvas üzerinden alıp Rust fonksiyonuna göndeririz:

```javascript
import init, { grayscale } from "./pkg/wasm_image_lab.js";

await init();

const canvas = document.querySelector("canvas");
const ctx = canvas.getContext("2d");
const frame = ctx.getImageData(0, 0, canvas.width, canvas.height);

grayscale(frame.data);
ctx.putImageData(frame, 0, 0);
```

Buradaki kritik konu JavaScript ile Wasm belleği arasındaki veri hareketidir. Algoritma çok kısa, kopyalama maliyeti ise yüksekse Wasm beklenen avantajı sağlamayabilir. Bu nedenle tek piksel yerine bütün kareyi işlemek ve gereksiz tampon kopyalarından kaçınmak gerekir.

## Video kodlama mimarisi

Video için her kare `VideoFrame` olarak WebCodecs API ile çözülebilir, Wasm filtresinden geçirilebilir ve `VideoEncoder` ile yeniden kodlanabilir. AV1 veya H.264 codec’ini tamamen Wasm içinde çalıştırmak için FFmpeg ya da libavif derlenebilir; ancak modül boyutu ve CPU tüketimi artar. Pratik mimari, özel filtreleri Wasm’da, donanım destekli kodlamayı WebCodecs’te çalıştırmaktır.

Uzun işlemleri ana iş parçacığında çalıştırmak arayüzü dondurur. Bu yüzden Wasm modülünü bir Web Worker içine taşımak, kareleri `OffscreenCanvas` ile işlemek ve süreleri `performance.now()` ile ölçmek iyi bir fikirdir. SIMD desteği etkinleştirildiğinde bir komutla birden fazla piksel kanalı işlenebilir. Sonuç: kullanıcı dosyasını sunucuya göndermeden hızlı, gizlilik dostu ve etkileyici bir medya laboratuvarı!
