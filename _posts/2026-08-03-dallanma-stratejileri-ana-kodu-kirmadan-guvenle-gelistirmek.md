---
layout: post
title: "Dallanma Stratejileri: Ana Kodu Kırmadan Güvenle Geliştirmek"
math: true
categories: 
  - Bilgi
tags: 
  - Git
  - Branching
  - Versiyon Kontrolü
---

Yeni bir özelliği denerken ana uygulamayı bozmak, çalışan motora tornavidayla yaklaşmaya benzer: Küçük bir değişiklik bütün sistemi durdurabilir. Git dalları sayesinde geliştiriciler ana kod tabanından bağımsız çalışma alanları oluşturabilir, deneylerini güvenle yapabilir ve yalnızca hazır olan değişiklikleri projeye ekleyebilir.
``

## Dal Nedir ve Neden Kullanılır?

Dal, belirli bir commit'i gösteren hareketli bir işaretçidir. Yeni dal oluşturulduğunda Git bütün proje dosyalarını fiziksel olarak kopyalamaz; yalnızca commit geçmişinde yeni bir referans meydana getirir. Bu nedenle dal oluşturmak hızlı ve düşük maliyetlidir.

Bir projenin commit kümesini $C$, belirli bir dalın erişebildiği commit'leri ise $B$ ile gösterirsek dal şu şekilde düşünülebilir:

$$B \subseteq C$$

Her yeni commit, aktif dalın işaretçisini ileri taşır. Ana dal yerinde kalırken özellik dalı kendi geçmişini oluşturur. Böylece yarım kalan kod, üretime gönderilmeye hazır kodla karışmaz.

```bash
git switch -c feature/arama
```

Bu komut `feature/arama` adında yeni bir dal oluşturur ve çalışma alanını o dala geçirir. Burada yapılan commit'ler `main` dalını doğrudan etkilemez.

## Yaygın Dallanma Stratejileri

Her ekip aynı geliştirme temposuna sahip değildir. Haftada birkaç kez sürüm çıkaran küçük bir web ekibiyle, aylar süren kurumsal sürümler hazırlayan ekip aynı modeli kullanmak zorunda değildir.

| Strateji | Temel yaklaşım | Avantajı | Uygun olduğu ortam |
|---|---|---|---|
| GitHub Flow | Kısa ömürlü dallar ve pull request | Basit, hızlı ve anlaşılır | Sürekli dağıtım yapan ekipler |
| Git Flow | `develop`, özellik, sürüm ve düzeltme dalları | Sürümleri düzenli biçimde ayırır | Planlı sürüm yayınlayan projeler |
| Trunk-Based | Çok kısa dallar veya doğrudan ana gövde | Entegrasyon gecikmesini azaltır | Güçlü CI/CD kültürüne sahip ekipler |
| Release Branching | Her sürüm için ayrı bakım dalı | Eski sürümlere destek sağlar | Birden fazla sürümü yaşatan ürünler |

### GitHub Flow

Geliştirici `main` üzerinden bir özellik dalı açar, değişikliklerini gönderir ve pull request oluşturur. Kod incelemesiyle otomatik testler tamamlandıktan sonra dal birleştirilir. Küçük ekipler için bürokrasisi az, kullanışlı bir seçenektir.

### Git Flow

Git Flow'da `main` üretimdeki kararlı kodu, `develop` ise sıradaki sürümün birleşim alanını temsil eder. Özellikler `feature`, sürüm hazırlıkları `release`, acil üretim düzeltmeleri ise `hotfix` dallarında yürütülür. Düzenlidir; ancak çok sık dağıtım yapan ekiplerde dal trafiği küçük bir otoyol kavşağına dönüşebilir.

### Trunk-Based Development

Bu yaklaşımda geliştiriciler değişiklikleri sık aralıklarla ana gövdeye entegre eder. Dallar varsa bile birkaç saat veya gün yaşar. Tamamlanmamış özellikler, feature flag kullanılarak kullanıcıdan gizlenebilir.

Entegrasyon riski kabaca dalın ömrü ve değişiklik büyüklüğüyle artar:

$$R \propto T \times D$$

Burada $R$ risk, $T$ dalın yaşam süresi, $D$ ise değişiklik miktarıdır. Uzun yaşayan ve yüzlerce dosyayı değiştiren dallar, birleştirme çatışmalarını büyütür.

## Güvenli Bir Çalışma Akışı

```bash
git switch main
git pull --ff-only
git switch -c fix/sepet-toplami

# Değişikliklerden sonra
git add .
git commit -m 'Sepet toplamı hesaplamasını düzelt'
git push -u origin fix/sepet-toplami
```

İlk iki komut güncel ana dalı temel almayı sağlar. Ardından hata düzeltme dalı açılır, değişiklikler commit edilir ve uzak depoya gönderilir. Son aşamada pull request açılarak test, inceleme ve onay süreçleri işletilir.

## İyi Dal Kullanımının Kuralları

- Dallara `feature/`, `fix/` veya `hotfix/` gibi anlaşılır adlar verin.
- Tek dalda birbiriyle ilgisiz değişiklikleri biriktirmeyin.
- Dalları kısa ömürlü tutun ve ana dalla düzenli olarak senkronize edin.
- Birleştirmeden önce otomatik testleri çalıştırın.
- Tamamlanan uzak dalları silerek depo görünümünü temiz tutun.
- Ana dalı koruma kurallarıyla doğrudan gönderimlere kapatın.

Dallanma, yalnızca bir Git komutu değil, ekip içi risk yönetimi yöntemidir. Doğru strateji seçildiğinde geliştiriciler daha cesur deneyler yapar, hatalar daha kontrollü düzeltilir ve ana kod tabanı üretime hazır kalır. En iyi model en karmaşık olan değil; ekibin sürüm sıklığına, büyüklüğüne ve otomasyon seviyesine en iyi uyum sağlayandır.
