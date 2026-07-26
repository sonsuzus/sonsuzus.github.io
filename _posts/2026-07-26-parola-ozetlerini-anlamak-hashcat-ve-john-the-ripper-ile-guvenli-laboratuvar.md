---
layout: post
title: "Parola Özetlerini Anlamak: Hashcat ve John the Ripper ile Güvenli Laboratuvar"
math: true
categories: 
  - Bilgi
tags: 
  - siber güvenlik
  - hashcat
  - john the ripper
---

Parolalar çoğu sistemde doğrudan saklanmaz; bunun yerine tek yönlü bir fonksiyondan geçirilerek elde edilen özetler saklanır. Parola denetimi ya da kurtarma çalışmaları, tahmin edilen adayların özetlerini hesaplayıp kayıtlı değerle karşılaştırır. Hashcat ve John the Ripper bu işlemi hızlandıran güçlü araçlardır; ancak yalnızca sahibi olduğunuz veya test izni aldığınız sistemlerde kullanılmalıdır. Aksi hâlde eğitici görünen bir deneme, hukuki sonuçları olan yetkisiz erişime dönüşebilir.

``

## Hash şifreleme değildir

Şifreleme, doğru anahtarla geri çevrilebilir. Güvenli bir parola özeti ise tek yönlüdür: Araçlar özeti matematiksel olarak “çözmez”; olası parolaları deneyerek eşleşme arar. Basitleştirilmiş süreç şöyledir:

$$h = H(p, s)$$

Burada $p$ parola, $s$ salt ve $H$ özetleme veya parola türetme fonksiyonudur. Bir aday $p'$ için $H(p',s)=h$ olduğunda parola bulunmuş sayılır. Salt, aynı parolaların farklı özetler üretmesini sağlar ve önceden hazırlanmış gökkuşağı tablolarının etkisini azaltır.

Bir saldırının yaklaşık süresi şu şekilde düşünülebilir:

$$T \approx \frac{N}{R}$$

$N$ aday sayısını, $R$ ise saniyede denenebilen aday sayısını gösterir. Sekiz karakterli ve 62 sembollü bir uzayda $N=62^8$ olur. Hızlı algoritmalar saldırganın işini kolaylaştırırken Argon2id gibi bilinçli olarak yavaş ve bellek maliyetli fonksiyonlar deneme hızını düşürür.

| Yöntem | Mantık | Güçlü yanı | Zayıf yanı |
|---|---|---|---|
| Sözlük | Listedeki adayları dener | Yaygın parolalarda hızlıdır | Rastgele parolalarda başarısızdır |
| Kural tabanlı | Kelimeleri sayılar ve eklerle değiştirir | İnsan alışkanlıklarını yakalar | Aday sayısı hızla büyür |
| Maske | Bilinen karakter yapısını tarar | Biçim biliniyorsa verimlidir | Uzunluk arttıkça pahalılaşır |
| Kaba kuvvet | Tüm uzayı araştırır | Teorik olarak kapsamlıdır | Üstel büyüme nedeniyle yavaştır |

## Güvenli bir laboratuvar

Aşağıdaki örnekler yalnızca kendi ürettiğiniz deneme verileri için kullanılmalıdır. Önce zararsız bir laboratuvar parolasının SHA-256 özetini oluşturalım:

```bash
printf 'Laboratuvar42!' | sha256sum
```

Çıktıdaki özet değerini `hash.txt` dosyasına, içinde `Laboratuvar42!` satırı bulunan küçük eğitim listesini ise `adaylar.txt` dosyasına kaydedebilirsiniz. Hashcat ile sözlük denetimi:

```bash
hashcat -m 1400 -a 0 hash.txt adaylar.txt
```

Burada `-m 1400` SHA-256 türünü, `-a 0` sözlük modunu belirtir. John the Ripper için dosya biçimini açıkça seçmek yanlış algılama riskini azaltır:

```bash
john --format=raw-sha256 --wordlist=adaylar.txt hash.txt
john --show --format=raw-sha256 hash.txt
```

İlk komut adayları karşılaştırır, ikincisi laboratuvarda bulunan eşleşmeyi gösterir. Gerçek parola verilerini çevrim içi hizmetlere yüklememek, deneme dosyalarını iş bitince silmek ve sonuçları yetkilendirilmiş raporlarda tutmak önemlidir.

## Araçların rolleri

| Araç | Öne çıkan özellik | Uygun kullanım |
|---|---|---|
| Hashcat | GPU hızlandırma ve ayrıntılı saldırı modları | Kontrollü performans testleri |
| John the Ripper | Esnek biçim algılama ve kurallar | Denetim ve eğitim laboratuvarları |

Başarıyla bulunan parola, aracın “sihirli” olduğunu değil, parolanın tahmin edilebilir veya saklama yönteminin yetersiz olduğunu gösterir. Savunmada Argon2id, scrypt ya da bcrypt gibi uygun maliyet parametrelerine sahip fonksiyonlar; benzersiz salt, parola yöneticisi, uzun ve benzersiz parolalar, hız sınırlaması ve çok faktörlü kimlik doğrulama birlikte kullanılmalıdır. Ayrıca eski MD5 ve SHA-1 özetleri yalnızca yeniden hashlenmemeli; kullanıcı doğrulandıktan sonra modern algoritmaya güvenli biçimde taşınmalıdır. En iyi parola kırma deneyi, sonunda daha sağlam bir sistemi doğuran deneydir.
