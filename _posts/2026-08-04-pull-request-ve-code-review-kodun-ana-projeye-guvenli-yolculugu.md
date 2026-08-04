---
layout: post
title: "Pull Request ve Code Review: Kodun Ana Projeye Güvenli Yolculuğu"
math: true
categories: 
  - Bilgi
tags: 
  - Git
  - Pull Request
  - Code Review
---

Bir özellik geliştirdiniz, testleri çalıştırdınız ve kodunuz bilgisayarınızda kusursuz görünüyor. Peki bu kod doğrudan ana projeye eklenmeli mi? Genellikle hayır! Pull Request ve Code Review süreçleri, kodun ana dala ulaşmadan önce teknik doğruluk, okunabilirlik, güvenlik ve ekip standartları açısından denetlendiği bir kalite kapısı oluşturur.
``

## Pull Request nedir?

**Pull Request (PR)**, bir dalda yapılan değişikliklerin başka bir dala alınması için oluşturulan resmi bir birleştirme talebidir. GitHub bu adı kullanırken GitLab aynı kavrama **Merge Request** der. İsimler değişse de temel fikir aynıdır: “Değişikliklerimi tamamladım; lütfen inceleyin ve uygunsa ana projeye dahil edin.”

PR yalnızca kod farklarını gösteren bir ekran değildir. Değişikliğin amacı, test yöntemi, ilişkili görevler, ekran görüntüleri ve inceleme konuşmaları için ortak bir çalışma alanıdır. Böylece kodun neden değiştirildiği, aylar sonra bile commit geçmişinden daha rahat anlaşılır.

Tipik akış şöyledir:

1. Ana daldan yeni bir özellik dalı oluşturulur.
2. Değişiklikler küçük ve anlamlı commit’lerle kaydedilir.
3. Dal uzak depoya gönderilir.
4. Bir Pull Request açılır.
5. Otomatik testler ve statik analiz araçları çalışır.
6. İnceleyiciler yorum yapar veya değişiklik ister.
7. Onaylanan kod ana dalla birleştirilir.

```bash
git switch main
git pull
git switch -c feature/kullanici-arama

# Kod değişikliklerinden sonra
git add .
git commit -m "Kullanıcı arama filtresi eklendi"
git push -u origin feature/kullanici-arama
```

Bu komutlar güncel `main` dalından bağımsız bir geliştirme dalı oluşturur, değişiklikleri kaydeder ve PR açılabilmesi için uzak depoya gönderir.

## Code Review neden gereklidir?

**Code Review**, başka bir geliştiricinin değişiklikleri sistematik biçimde değerlendirmesidir. Amaç hata avına çıkıp yazarı köşeye sıkıştırmak değil; ortak kod tabanını iyileştirmek ve ekip içinde bilgi paylaşmaktır. İnceleme sırasında doğruluk, performans, güvenlik, test kapsamı, isimlendirme ve sürdürülebilirlik değerlendirilir.

Basitleştirilmiş bir kalite modeli şöyle düşünülebilir:

$$Q = w_dD + w_tT + w_oO + w_gG$$

Burada $D$ doğruluğu, $T$ test edilebilirliği, $O$ okunabilirliği ve $G$ güvenliği temsil eder. $w$ katsayıları ise projenin öncelikleridir. Örneğin finans uygulamasında güvenliğin ağırlığı, küçük bir tanıtım sitesine göre daha yüksek olabilir.

| Kontrol alanı | İnceleyicinin sorusu | Olası risk |
|---|---|---|
| Doğruluk | Kod beklenen işi yapıyor mu? | Yanlış sonuç |
| Okunabilirlik | İsimler ve akış anlaşılır mı? | Bakım maliyeti |
| Testler | Kritik senaryolar sınanmış mı? | Regresyon |
| Güvenlik | Girdi doğrulama yeterli mi? | Veri sızıntısı |
| Performans | Gereksiz işlem veya sorgu var mı? | Yavaşlama |

## İyi bir PR nasıl hazırlanır?

İyi PR küçük, odaklı ve açıklayıcıdır. Aynı talepte hem kullanıcı araması eklemek hem dosya yapısını tamamen değiştirmek, incelemeyi zorlaştırır. Büyük PR’larda bilişsel yük artar; gözden kaçan hata olasılığı da yükselir. Kabaca inceleme etkinliğini

$$E \propto \frac{1}{S}$$

şeklinde düşünebiliriz. Burada $S$, değişiklik boyutudur. Bu kesin bir fizik yasası değildir; küçük değişikliklerin daha dikkatli incelenebildiğini anlatan pratik bir modeldir.

PR açıklamasında şu bilgiler bulunmalıdır:

- Değişikliğin amacı ve kapsamı
- İlgili görev veya hata kaydı
- Değişikliğin nasıl test edildiği
- Arayüz değiştiyse ekran görüntüsü
- Bilinen sınırlamalar ve riskler

## Yapıcı inceleme kültürü

Yorumlar kişiye değil koda yöneltilmelidir. “Bunu yanlış yazmışsın” yerine “Bu koşul boş değer geldiğinde hata üretebilir; burada erken dönüş kullanabilir miyiz?” demek daha yapıcıdır. Yazar da her yorumu saldırı olarak görmemeli, ancak gerekçesini açıklayamadığı önerileri körü körüne uygulamamalıdır.

| Zayıf yaklaşım | Yapıcı yaklaşım |
|---|---|
| “Bu kod kötü.” | “Bu fonksiyonu bölmek okunabilirliği artırabilir.” |
| “Böyle yapılmaz.” | “Projedeki mevcut servis desenini kullanabilir miyiz?” |
| Sessizce onaylamak | Kritik senaryoları ve testleri doğrulamak |

Sonuç olarak Pull Request bir izin ekranı, Code Review ise bürokratik bir engel değildir. İkisi birlikte hataları erken yakalayan, ekip bilgisini çoğaltan ve ana dalı güvenilir tutan bir mühendislik pratiğidir. Sağlıklı ekiplerde hedef, kimin haklı olduğunu kanıtlamak değil; kodu birlikte daha doğru, anlaşılır ve sürdürülebilir hâle getirmektir.
