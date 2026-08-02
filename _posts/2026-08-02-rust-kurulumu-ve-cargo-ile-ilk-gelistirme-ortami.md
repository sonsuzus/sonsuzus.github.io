---
layout: post
title: "Rust Kurulumu ve Cargo ile İlk Geliştirme Ortamı"
math: true
categories: 
  - Bilgi
tags: 
  - Rust
  - Cargo
  - VS Code
---

Rust öğrenme yolculuğunun ilk durağı, derleyiciyi kurup editörü hazırlamaktır. Neyse ki Rust dünyasında kurulum, farklı araçları tek tek avlamaktan çok daha düzenlidir: `rustup` araç zincirini yönetir, `rustc` kodu derler, Cargo ise proje ve bağımlılık işlerini üstlenir. VS Code eklentileri de eklenince geriye yalnızca güvenli ve hızlı kod yazmak kalır.
``
## Rust araç zincirini tanıyalım

Kuruluma başlamadan önce oyuncu kadrosunu tanımak faydalıdır. Rust tek bir programdan ibaret değildir; birlikte çalışan araçlardan oluşan bir ekosistemdir.

| Araç | Görevi | Tipik komut |
|---|---|---|
| `rustup` | Rust sürümlerini ve hedeflerini yönetir | `rustup update` |
| `rustc` | Rust kaynak kodunu derler | `rustc main.rs` |
| `cargo` | Proje, bağımlılık, test ve derleme yönetimi yapar | `cargo build` |
| `rustfmt` | Kod biçimini standartlaştırır | `cargo fmt` |
| `clippy` | Olası hatalar ve kötü pratikler için öneriler verir | `cargo clippy` |

Basitçe düşünürsek toplam derleme süresi yaklaşık olarak

$$T_{toplam} = T_{bağımlılık} + T_{derleme} + T_{bağlama}$$

şeklindedir. Cargo bu aşamaları bizim adımıza koordine eder ve değişmeyen parçaları önbellekten kullanarak sonraki derlemeleri hızlandırır.

## Rust kurulumu

Linux ve macOS üzerinde resmi `rustup` kurulum komutu şöyledir:

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

Kurulum ekranında varsayılan seçenek genellikle yeterlidir. İşlem bittikten sonra terminali yeniden açın veya ortam değişkenlerini yükleyin:

```bash
source "$HOME/.cargo/env"
rustc --version
cargo --version
```

macOS kullanıyorsanız bağlayıcı araçlar için `xcode-select --install` komutu gerekebilir. Debian veya Ubuntu tabanlı Linux sistemlerinde ise `sudo apt install build-essential` paketi yerel derlemelerde ihtiyaç duyulan araçları sağlar.

Windows kullanıcıları [rustup.rs](https://rustup.rs/) üzerinden `rustup-init.exe` dosyasını indirip çalıştırabilir. Kurulum, Microsoft C++ Build Tools isteyebilir. Bu bileşen, Rust programlarının Windows üzerinde bağlanabilmesi için gereklidir. Yeni bir PowerShell penceresinde sürüm komutlarını çalıştırarak kurulumu doğrulayın.

Kararlı araç zincirini güncellemek ve gerekli yardımcı bileşenleri eklemek için:

```bash
rustup update stable
rustup default stable
rustup component add rustfmt clippy
```

## VS Code ortamını hazırlama

VS Code içinde **Extensions** bölümünü açıp `rust-analyzer` eklentisini kurun. Resmî Rust eklentisi; otomatik tamamlama, tür gösterimi, hata analizi, yeniden adlandırma ve kod gezinme özellikleri sunar. Hata ayıklamak için ayrıca **CodeLLDB** kurulabilir.

| Eklenti | Sağladığı özellik | Gerekli mi? |
|---|---|---|
| rust-analyzer | Tamamlama ve anlık analiz | Evet |
| CodeLLDB | Kesme noktalarıyla hata ayıklama | Önerilir |
| Even Better TOML | `Cargo.toml` desteği | İsteğe bağlı |

VS Code ayarlarında dosya kaydedildiğinde biçimlendirmeyi etkinleştirmek, kod düzenini otomatik korur:

```json
{
  "[rust]": {
    "editor.defaultFormatter": "rust-lang.rust-analyzer",
    "editor.formatOnSave": true
  }
}
```

## Cargo ile ilk proje

Terminalde aşağıdaki komutlarla yeni bir uygulama oluşturun:

```bash
cargo new merhaba_rust
cd merhaba_rust
code .
cargo run
```

`cargo new`, kaynak kodunun bulunduğu `src/main.rs` dosyasını ve proje tanımı olan `Cargo.toml` dosyasını üretir. `cargo run` ise projeyi önce derler, ardından çalıştırır. Yalnızca hata kontrolü yapmak istediğinizde daha hızlı olan `cargo check` kullanılabilir.

Temel geliştirme döngüsü şu komutlardan oluşur:

```bash
cargo check    # Kodu hızlıca denetler
cargo fmt      # Biçimlendirmeyi düzeltir
cargo clippy   # İyileştirme önerileri sunar
cargo test     # Testleri çalıştırır
cargo run      # Uygulamayı derleyip başlatır
```

Bağımlılıklar `Cargo.toml` içindeki `[dependencies]` bölümünde tutulur ve kesin sürümler `Cargo.lock` dosyasına kaydedilir. Böylece ekipteki herkes aynı bağımlılıklarla tekrarlanabilir derlemeler yapar. Son kontrol olarak `cargo run` çıktısında “Hello, world!” görüyorsanız tebrikler: Rust atölyeniz üretime hazır!
