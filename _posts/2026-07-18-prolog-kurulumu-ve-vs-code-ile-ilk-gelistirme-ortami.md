---
layout: post
title: "Prolog Kurulumu ve VS Code ile İlk Geliştirme Ortamı"
math: true
categories: 
  - Program
tags: 
  - prolog
  - swi-prolog
  - vscode
  - mantıksal-programlama
---

Prolog, programcıya “nasıl yapılır?” yerine “ne doğrudur?” diye sorduran hoş bir zihin jimnastiğidir. Bu yazıda SWI-Prolog kurulumunu tamamlayacak, derleyici/yorumlayıcı ayarlarını kontrol edecek ve VS Code üzerinde teorik bilgiyi pratiğe dökeceğimiz küçük bir laboratuvar hazırlayacağız.
``

## Prolog’un Kafası Nasıl Çalışır?

Prolog, mantıksal programlama ailesindendir. Program; **olgular**, **kurallar** ve **sorgular** üzerine kurulur. Klasik dillerde akış çoğunlukla yukarıdan aşağıya komutlarla ilerlerken, Prolog hedefe ulaşmak için kuralları dener, eşleştirme yapar ve gerekirse geri izleme, yani **backtracking**, uygular.

Bir Prolog kuralını kabaca şöyle düşünebiliriz:

$H \leftarrow B_1 \land B_2 \land ... \land B_n$

Yani “$H$ doğrudur, eğer tüm $B$ koşulları doğruysa.” Prolog’da bu yapı şöyle yazılır:

```prolog
ata(ahmet, mehmet).
ata(mehmet, zeynep).

dede(X, Y) :- ata(X, Z), ata(Z, Y).
```

Bu kodda ilk iki satır **olgu**, son satır ise **kuraldır**. `dede(X, Y)` sorgusu için Prolog, uygun `Z` değerini arar. Değişkenler büyük harfle başlar; `X`, `Y`, `Z` birer bilinmeyendir. Eşleştirme işleminde Prolog bir yerine koyma bulur; buna $\theta = \{X/ahmet, Y/zeynep\}$ gibi bakabiliriz.

| Kavram | Prolog’daki Karşılığı | Sezgisel Anlamı |
|---|---|---|
| Olgu | `ata(ahmet, mehmet).` | Veritabanındaki kesin bilgi |
| Kural | `dede(X,Y) :- ...` | Koşullu mantıksal çıkarım |
| Sorgu | `?- dede(ahmet, zeynep).` | “Bu doğru mu?” sorusu |
| Backtracking | Alternatifleri deneme | Dedektif gibi iz sürme |

## SWI-Prolog Kurulumu

Modern Prolog geliştirme için en pratik seçeneklerden biri **SWI-Prolog**’dur. Windows, macOS ve Linux üzerinde çalışır, paket yöneticileriyle kolay kurulur ve VS Code ile iyi anlaşır.

```bash
# macOS
brew install swi-prolog

# Ubuntu/Debian
sudo apt update
sudo apt install swi-prolog
```

Bu komutlar SWI-Prolog yorumlayıcısını sisteminize kurar. Kurulumdan sonra terminalde şu komutla kontrol edebilirsiniz:

```bash
swipl --version
```

Eğer sürüm bilgisi görüyorsanız, derleyici/yorumlayıcı yolu başarıyla yapılandırılmış demektir. Windows’ta kurulum sihirbazında **Add swipl to PATH** benzeri seçeneği işaretlemek önemlidir. İşaretlemediyseniz, SWI-Prolog’un `bin` klasörünü sistem PATH değişkenine elle eklemeniz gerekir.

## VS Code Ortamını Hazırlama

VS Code tarafında amaç; dosya düzenleme, sözdizimi renklendirme ve terminal üzerinden hızlı çalıştırma konforunu sağlamaktır. Eklentiler bölümünden **VSC-Prolog** veya güncel Prolog sözdizimi desteği sunan bir uzantı kurabilirsiniz.

| Bileşen | Görev | Neden Gerekli? |
|---|---|---|
| SWI-Prolog | Programı çalıştırır | Mantık motoru burada |
| VS Code | Kod editörü | Rahat yazma ve gezinme |
| Prolog eklentisi | Renklendirme sağlar | Hataları daha hızlı fark ettirir |
| Entegre terminal | Sorgu çalıştırır | Editörden çıkmadan test |

Proje klasörünüzü açın ve `aile.pl` adında bir dosya oluşturun:

```prolog
kadın(ayse).
erkek(ali).
ebeveyn(ayse, ali).

anne(X, Y) :- kadın(X), ebeveyn(X, Y).
```

Bu dosya basit bir bilgi tabanı kurar. `anne(X, Y)` kuralı, `X` kişisinin kadın ve `Y` kişisinin ebeveyni olup olmadığını kontrol eder.

Terminalde dosyayı şu şekilde yükleyin:

```bash
swipl aile.pl
```

Ardından Prolog etkileşimli kabuğunda sorgu yazabilirsiniz:

```prolog
?- anne(ayse, ali).
?- anne(Kim, ali).
```

İlk sorgu doğruysa `true.` döner. İkinci sorguda Prolog değişkeni doldurmaya çalışır ve `Kim = ayse.` gibi bir cevap üretir.

## İlk Ayar Kontrol Listesi

Kurulumda sorun yaşarsanız şu küçük liste hayat kurtarır:

- `swipl --version` çalışıyor mu?
- `.pl` dosyası doğru klasörde mi?
- VS Code terminali aynı proje dizininde mi açıldı?
- Dosyadaki her olgu ve kural nokta ile bitiyor mu?
- Değişkenler büyük harfle, atomlar küçük harfle mi başlıyor?

Prolog öğrenirken en güzel yöntem, küçük bilgi tabanları kurup bol bol sorgu sormaktır. Çünkü Prolog’da program yazmak biraz şehir haritası çizmek gibidir: yolları siz tanımlarsınız, hedefe giden rotayı mantık motoru bulur.
