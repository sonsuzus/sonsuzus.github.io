---
layout: post
title: "Git Commit Mesajlarının Sosyolojisi: Kod Geçmişinden Takım Kültürünü Okumak"
math: true
categories: 
  - Bilgi
tags: 
  - Git
  - Takım Kültürü
  - Yazılım Geliştirme
---

Bir Git deposunun commit geçmişi yalnızca kodun nasıl değiştiğini anlatmaz; ekibin iletişim alışkanlıklarını, baskı altında nasıl davrandığını ve sorumluluğu nasıl paylaştığını da gösterir. “fix”, “nihayet çalıştı” veya “ödeme servisinde zaman aşımını düzelt” ifadeleri teknik olarak aynı değişikliği işaret edebilir; fakat her biri bambaşka bir ekip kültürünün izini taşır.

``

## Commit mesajı neden sosyal bir veridir?

Commit mesajı, geliştiricinin gelecekteki okuyucuya bıraktığı küçük bir nottur. Bu okuyucu ekip arkadaşı, kod incelemecisi veya altı ay sonraki kendisi olabilir. Dolayısıyla mesaj yazarken harcanan emek, ekibin ortak hafızaya verdiği önemi yansıtır.

Bu ilişkiyi basitçe şöyle modelleyebiliriz:

$$K = \frac{B \times O}{G + 1}$$

Burada $K$ kurumsal hafıza katkısını, $B$ mesajın bilgi yoğunluğunu, $O$ okunabilirliğini ve $G$ gereksiz gürültüyü temsil eder. Bu bilimsel bir ölçüm değil, düşünme aracıdır: Bilgi ve okunabilirlik arttıkça geçmiş daha anlaşılır hâle gelir; gürültü arttıkça `git log` arkeolojik kazıya dönüşür.

## Üsluplar ne anlatabilir?

| Commit üslubu | Örnek | Muhtemel kültürel işaret |
|---|---|---|
| Aşırı kısa | `fix` | Hız baskısı veya düşük dokümantasyon alışkanlığı |
| Açıklayıcı | `Sepet toplamında KDV yuvarlamasını düzelt` | Gelecekteki okuyucuya özen |
| Emir kipinde | `Add retry policy to payment client` | Ortak ve standartlaştırılmış dil |
| Duygusal | `Finally fix this nightmare` | Samimiyet, yorgunluk ya da tükenmişlik sinyali |
| Suçlayıcı | `Undo Ahmet's broken change` | Düşük psikolojik güvenlik ve kişiselleştirme riski |
| Kural tabanlı | `fix(api): handle expired tokens` | Otomasyon ve süreç odaklı çalışma |

Bu tablo kesin teşhis koymaz. Tek bir “WIP” mesajı kaotik kültür kanıtı değildir; geliştirici aceleyle ara kayıt almış olabilir. Sosyolojik okuma, tekil örneklerden değil, tekrar eden örüntülerden yapılmalıdır.

## Mesajların görünmeyen aktörleri

Commit geçmişinde yalnızca yazar bulunmaz. Kod inceleme kuralları, CI sistemi, teslim tarihleri ve yöneticilerin beklentileri de mesaj biçimini etkiler. Örneğin Conventional Commits kullanan bir ekipte düzenli mesajlar, herkesin doğal olarak titiz olduğunu değil, otomasyonun davranışı yönlendirdiğini gösterebilir.

```text
feat(search): add typo tolerance
fix(auth): reject expired refresh tokens
refactor(cart): extract price calculator
```

Bu yapıdaki `feat`, `fix` ve `refactor` türleri değişikliğin amacını makine tarafından okunabilir hâle getirir. Böylece sürüm notları üretilebilir ve değişiklikler sınıflandırılabilir. Ancak şablon doğru olsa bile açıklama anlamsız olabilir: `fix(api): fix bug` biçimsel olarak düzenli, içerik olarak yoksuldur.

## Kültürel sinyalleri ölçmek

Bir deponun mesaj uzunluklarını hızlıca incelemek için şu komut kullanılabilir:

```bash
git log --pretty=format:%s |
awk '{ total += length($0); count++ }
END { print "Ortalama:", total / count }'
```

Komut, commit başlıklarının ortalama karakter sayısını hesaplar. Yine de uzunluk kalite değildir. Daha anlamlı bir değerlendirme için açıklayıcılık oranı düşünülebilir:

$$A = \frac{N_{bağlamlı}}{N_{toplam}} \times 100$$

Burada bağlamlı mesaj; neyin değiştiğini ve mümkünse nedenini belirten mesajdır. Oranı sürüm dönemlerine göre karşılaştırmak, teslim tarihi yaklaşırken iletişim kalitesinin düşüp düşmediğini gösterebilir.

## Sağlıklı bir commit dili kurmak

İyi bir ekip, commit mesajını performans değerlendirme silahına dönüştürmez. Bunun yerine birkaç ortak ilke belirler:

- Değişikliğin **ne yaptığını** açıkça yazmak,
- Koddan anlaşılmayan durumlarda **nedenini** belirtmek,
- İnsanları değil davranışı ve teknik sonucu tarif etmek,
- Aynı dil ve biçim standardını kullanmak,
- Büyük değişiklikleri anlamlı, küçük parçalara ayırmak.

Sonuçta commit geçmişi takımın günlüğüdür. Düzenli, açıklayıcı ve saygılı mesajlar yalnızca iyi Git kullanımı değildir; ortak sorumluluğun, psikolojik güvenliğin ve gelecekteki ekip arkadaşlarına duyulan nezaketin küçük ama kalıcı göstergeleridir.
