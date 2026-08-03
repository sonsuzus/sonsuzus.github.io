---
layout: post
title: "Git Uzak Depolar ve Klonlama: Kodun Bulutla Buluşması"
math: true
categories: 
  - Bilgi
tags: 
  - Git
  - GitHub
  - Versiyon Kontrolü
---

Bir projeyi yalnızca kendi bilgisayarında tutmak, bütün yumurtaları aynı sepete koymaya benzer. Git’in uzak depo mekanizması sayesinde kodlar GitHub, GitLab veya Bitbucket gibi servislerde saklanabilir; ekip üyeleri aynı proje üzerinde çalışabilir ve yerel değişiklikler dış dünyayla paylaşılabilir. Bu süreçte `clone`, `remote`, `fetch`, `pull` ve `push` komutları başrolü üstlenir.

``

## Yerel ve uzak depo nedir?

**Yerel depo**, bilgisayarındaki çalışma dosyalarını, commit geçmişini, dalları ve Git metadata’sını içeren depodur. **Uzak depo** ise genellikle internete bağlı bir sunucuda barındırılan ve ekip için ortak buluşma noktası görevi gören Git deposudur.

Git dağıtık bir sürüm kontrol sistemi olduğu için uzak sunucu, geçmişin tek sahibi değildir. Bir projeyi klonladığında commit geçmişinin tamamına yakın bir kopyasını alırsın. Başka bir deyişle yerel depo $L$, uzak depo $R$ ile gösterilirse klonlama sonrasında başlangıçta yaklaşık olarak şu ilişki kurulur:

$$L \approx R$$

Zamanla iki tarafta farklı commit’ler oluşabilir. Ayrışma miktarını basitçe şu şekilde düşünebiliriz:

$$\Delta = |C_L \triangle C_R|$$

Burada $C_L$ ve $C_R$ yerel ve uzak commit kümelerini, $\triangle$ ise iki küme arasındaki farklılığı temsil eder. `fetch`, `pull` ve `push` işlemleri bu farkı yönetmemizi sağlar.

| Özellik | Yerel depo | Uzak depo |
|---|---|---|
| Konum | Kendi bilgisayarın | Git sunucusu veya bulut servisi |
| İnternet gereksinimi | Çoğu işlemde gerekmez | Veri alışverişinde gerekir |
| Temel amaç | Geliştirme ve commit oluşturma | Paylaşım, yedekleme ve iş birliği |
| Tipik dallar | `main`, özellik dalları | `origin/main`, ekip dalları |

## Bir projeyi klonlamak

Var olan bir uzak projeyi bilgisayara indirmek için `git clone` kullanılır:

```bash
git clone https://github.com/kullanici/proje.git
cd proje
```

Bu komut yalnızca dosyaları indirmez. Commit geçmişini getirir, çalışma dizinini hazırlar ve uzak adresi varsayılan olarak `origin` adıyla kaydeder. Farklı bir klasör adı kullanmak da mümkündür:

```bash
git clone https://github.com/kullanici/proje.git benim-projem
```

HTTPS kolay başlangıç sunarken SSH, anahtar tabanlı kimlik doğrulamasıyla sık işlem yapan geliştiriciler için daha rahattır.

| Bağlantı türü | Örnek | Avantajı | Dikkat edilmesi gereken |
|---|---|---|---|
| HTTPS | `https://github.com/a/b.git` | Kurulumu kolaydır | Token gerekebilir |
| SSH | `git@github.com:a/b.git` | Parolasız ve güvenli kullanım | SSH anahtarı kurulmalıdır |

## Yerel depoyu uzak sunucuya bağlamak

Bilgisayarında sıfırdan oluşturduğun bir projeyi uzak depoya bağlamak için önce serviste boş bir depo oluşturabilir, ardından şu komutları çalıştırabilirsin:

```bash
git init
git add .
git commit -m "İlk sürüm"
git branch -M main
git remote add origin git@github.com:kullanici/proje.git
git push -u origin main
```

`git remote add origin ...`, adrese `origin` takma adını verir. `git push -u origin main` ise yerel `main` dalını sunucuya gönderir ve takip ilişkisi kurar. Sonraki gönderimlerde çoğunlukla yalnızca `git push` yazmak yeterlidir.

Kayıtlı bağlantıları incelemek için:

```bash
git remote -v
```

Yanlış adres eklediysen bağlantıyı değiştirebilirsin:

```bash
git remote set-url origin yeni-adres
git remote remove origin
```

## Fetch, pull ve push farkı

Bu üç komut benzer görünse de aynı işi yapmaz:

| Komut | Yön | Etkisi |
|---|---|---|
| `git fetch` | Uzak → Yerel metadata | Değişiklikleri getirir, çalışma dalını birleştirmez |
| `git pull` | Uzak → Yerel dal | Fetch yapar, ardından birleştirir veya rebase uygular |
| `git push` | Yerel → Uzak | Yerel commit’leri sunucuya gönderir |

Özellikle ekip çalışmalarında önce `git fetch` çalıştırıp farkları incelemek daha kontrollü olabilir:

```bash
git fetch origin
git log --oneline main..origin/main
git pull --rebase origin main
git push origin main
```

Bu akış, uzaktaki commit’leri görmeni, değişiklikleri doğrusal bir geçmişle bütünleştirmeni ve ardından kendi commit’lerini paylaşmanı sağlar. Kısacası `clone` projeye giriş kapısı, `remote` adres defteri, `fetch` haberci, `pull` teslimatçı ve `push` ise kodunu buluta taşıyan kurye gibidir.
