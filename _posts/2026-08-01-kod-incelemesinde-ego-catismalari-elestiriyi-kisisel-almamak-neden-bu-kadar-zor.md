---
layout: post
title: "Kod İncelemesinde Ego Çatışmaları: Eleştiriyi Kişisel Almamak Neden Bu Kadar Zor?"
math: true
categories: 
  - Bilgi
tags: 
  - kod incelemesi
  - yazılım psikolojisi
  - geri bildirim
---

Kod incelemesinde bırakılan masum bir “Bu fonksiyon fazla karmaşık” yorumu, bazen geliştiricinin zihninde “Sen yetersiz bir programcısın” cümlesine dönüşür. Pull request birkaç satırlık teknik tartışma olmaktan çıkar; özsaygının savunulduğu küçük bir arenaya dönüşür. Peki profesyonel geri bildirim ile benlik algısı neden bu kadar kolay birbirine karışır?
``
## Kod, yalnızca kod değildir

Bir geliştirici yazdığı koda zamanını, bilgisini ve problem çözme tarzını yatırır. Özellikle zor bir görev günlerce uğraştırmışsa ortaya çıkan çözüm psikolojik olarak “benim ürünüm” değil, “benden bir parça” gibi algılanabilir. Bu duruma **psikolojik sahiplenme** denir.

Beyin eleştiriyi değerlendirirken kabaca iki sinyali karşılaştırır:

$$Tepki\ Şiddeti \approx Algılanan\ Tehdit \times Kimlikle\ Özdeşleşme$$

Kodumuzla ne kadar güçlü özdeşleşirsek küçük bir yorumun yarattığı tehdit de o kadar büyür. Böylece “Bu değişken adı belirsiz” gibi sınırlı bir tespit, zihinsel bir kestirmeyle “İsimlendirme konusunda kötüyüm” sonucuna ulaşabilir.

| Profesyonel geri bildirim | Benlik odaklı yorumlama |
|---|---|
| “Fonksiyonun sorumluluğu fazla geniş.” | “Temiz kod yazamıyorum.” |
| “Bu sorgu performans sorunu yaratabilir.” | “Yeterince deneyimli değilim.” |
| “Test senaryosu eksik kalmış.” | “Dikkatsiz bir geliştiriciyim.” |
| “Alternatif yaklaşımı değerlendirelim.” | “Benim çözümüm değersiz.” |

İki sütun arasındaki fark teknik değil, bilişseldir. Solda değiştirilebilir bir çıktı; sağda ise sabit bir kimlik yargısı vardır.

## Beyin neden savunmaya geçiyor?

Eleştiri, sosyal statümüzün veya gruptaki yerimizin tehdit edildiği hissini yaratabilir. Beyin bu durumda geri bildirimi öğrenme fırsatı olarak değil, saldırı olarak işlemeye başlar. Doğrulama yanlılığı da devreye girer: Yorumdaki yararlı kısmı aramak yerine eleştirmenin haksız olduğunu kanıtlayan ayrıntıları seçeriz.

Bu tepkiyi basitçe şöyle modelleyebiliriz:

$$Öğrenme\ Olasılığı = \frac{Merak}{Savunmacılık + 1}$$

Bu bilimsel bir ölçüm formülü değildir; ancak önemli bir ilişkiyi görünür kılar: Savunmacılık yükseldikçe geri bildirimden yararlanmak zorlaşır. Amaç egoyu tamamen yok etmek değil, merakı savunma refleksinden daha güçlü hâle getirmektir.

## Yorum dili çatışmayı nasıl değiştirir?

Kod incelemesinde yalnızca içeriğin doğruluğu değil, sunuluş biçimi de önemlidir. Aşağıdaki yorum teknik olarak bir soruna işaret etse bile kişiyi hedef alır:

```text
Bunu gereksiz yere karmaşık yazmışsın. Daha basit düşünmelisin.
```

Aynı gözlem, ortak hedefe ve gözlemlenebilir sonuca bağlanabilir:

```text
Bu fonksiyon üç farklı sorumluluk taşıyor gibi görünüyor.
Test edilebilirliği artırmak için doğrulama ve kayıt işlemlerini
ayrı fonksiyonlara bölmeyi değerlendirebilir miyiz?
```

İkinci örnek sorunu, gerekçeyi ve olası yönü açıklar. Emir vermek yerine tartışma alanı oluşturur. İyi bir inceleme yorumu çoğunlukla şu yapıyı izler:

```text
Gözlem → Olası etki → Öneri veya soru
```

## Eleştiriyi kişisel almamak için pratikler

1. **Kişi ile çıktıyı ayırın.** “Kodumda hata var” cümlesi, “Ben kötü bir geliştiriciyim” anlamına gelmez.
2. **Anında cevap vermeyin.** Duygusal yükselme hissediyorsanız kısa bir mola verin; ilk tepki çoğu zaman en savunmacı olandır.
3. **Niyeti tahmin etmek yerine açıklama isteyin.** “Buradaki temel risk performans mı, bakım maliyeti mi?” sorusu tartışmayı somutlaştırır.
4. **Haklı çıkmayı değil, ürünü iyileştirmeyi hedefleyin.** Kod incelemesi bir düello değil, dağıtımdan önce yapılan takım çalışmasıdır.
5. **Yorumları önem derecesiyle etiketleyin.** `blocker`, `suggestion` veya `nit` gibi etiketler her yorumun zorunlu değişiklik sanılmasını önler.

Sağlıklı ekip kültüründe geri bildirim, geliştiricinin değerini ölçen bir sınav değildir. Kod geçicidir; bugün savunduğumuz çözümü yarın kendimiz yeniden yazabiliriz. Profesyonellik hiç rahatsız olmamak değil, rahatsızlığı fark edip onu meraka çevirebilmektir. Sonuçta en iyi pull request, egonun kazandığı değil, ekibin birlikte daha iyi bir çözüm ürettiği pull request’tir.
