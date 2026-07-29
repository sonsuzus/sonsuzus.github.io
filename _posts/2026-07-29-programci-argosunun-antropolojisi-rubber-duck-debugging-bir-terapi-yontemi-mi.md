---
layout: post
title: "Programcı Argosunun Antropolojisi: Rubber Duck Debugging Bir Terapi Yöntemi mi?"
math: true
categories: 
  - Bilgi
tags: 
  - rubber-duck-debugging
  - yazılım-psikolojisi
  - hata-ayıklama
---

Bir programcının masasındaki plastik ördeğe ciddi ciddi kod anlatması, dışarıdan bakıldığında teknoloji çağının en tuhaf ritüellerinden biri olabilir. Ancak **rubber duck debugging**, yalnızca eğlenceli bir programcı argosu değildir. Problemi sesli biçimde açıklamak; düşünceleri dışsallaştırma, varsayımları sorgulama ve zihinsel çarpıtmaları fark etme bakımından bilişsel terapi teknikleriyle şaşırtıcı benzerlikler taşır.

``

## Ördek Nereden Çıktı?

Terim, Andrew Hunt ve David Thomas’ın *The Pragmatic Programmer* kitabında anlatılan bir hikâyeyle popülerleşti. Hikâyedeki programcı, yanında taşıdığı plastik ördeğe kodunu satır satır açıklayarak hataları buluyordu. Ördeğin teknik bilgisi yoktu; hatta dürüst olalım, ördeğin herhangi bir konuda bilgisi yoktu. İşe yarayan şey, programcının anlatırken kendi düşünce sürecini görünür hâle getirmesiydi.

Normalde kod okurken beynimiz boşlukları otomatik olarak tamamlar. Yazdığımız satırın ne yaptığını değil, **ne yapmasını amaçladığımızı** görmeye eğilimliyiz. Sesli açıklama ise niyet ile gerçek davranış arasındaki farkı açığa çıkarır.

Bunu basitçe şöyle modelleyebiliriz:

$$Hata\ Farkındalığı \approx Gerçek\ Davranış - Varsayılan\ Davranış$$

Bu fark zihinde belirsizken hata saklanabilir. Sözcüklere döküldüğünde ise çelişki elle tutulur hâle gelir.

## Bilişsel Terapiyle Benzerliği

Bilişsel davranışçı terapide kişi, otomatik düşüncelerini tanımayı ve bunların dayandığı varsayımları sorgulamayı öğrenir. Terapist çoğu zaman doğrudan cevap vermez; sorularla kişinin kendi düşüncesini incelemesini sağlar. Plastik ördek de son derece ekonomik, yargılamayan ve randevu istemeyen bir Sokratik sorgulayıcıdır.

| Kod açıklama pratiği | Bilişsel terapi yaklaşımı |
|---|---|
| “Bu fonksiyon neden burada?” | “Bu düşüncenin dayanağı nedir?” |
| Değişkenin değerini takip etmek | Duygu ve düşünce zincirini izlemek |
| Gizli varsayımı bulmak | Otomatik düşünceyi fark etmek |
| Alternatif algoritma üretmek | Alternatif yorum geliştirmek |
| Test sonucuyla doğrulamak | Kanıtlarla düşünceyi sınamak |

Elbette rubber duck debugging, klinik bir terapi yöntemi değildir ve psikolojik destek yerine geçmez. Benzerlik, her iki pratiğin de **metabiliş** kullanmasından kaynaklanır: Kişi yalnızca düşünmez, nasıl düşündüğünü de gözlemler.

## Kod Anlatılınca Neden Hata Beliriyor?

Aşağıdaki JavaScript fonksiyonu, listedeki pozitif sayıların ortalamasını hesaplamayı amaçlıyor:

```javascript
function pozitifOrtalama(sayilar) {
  const pozitifler = sayilar.filter(sayi => sayi > 0);
  const toplam = pozitifler.reduce((a, b) => a + b, 0);

  return toplam / sayilar.length;
}

console.log(pozitifOrtalama([-4, 10, 20]));
```

Kodu ördeğe anlatırken şu cümle kurulabilir: “Önce pozitifleri seçiyorum, onları topluyorum ve... bütün listenin uzunluğuna bölüyorum.” İşte o küçük duraksama, hatanın yakalandığı andır. Pay pozitif sayıların toplamıyken payda tüm sayıların adedidir. Doğru satır şöyledir:

```javascript
return pozitifler.length === 0
  ? 0
  : toplam / pozitifler.length;
```

Bu sürüm ayrıca boş sonuçta oluşabilecek sıfıra bölme problemini de ele alır. Ördek tek kelime etmeden hem mantık hatasını hem de uç durumu gündeme getirmiştir.

## Etkili Bir Ördek Seansı

Pratiği “koda bakıp homurdanmak” seviyesinden çıkarmak için şu sırayı izleyebilirsiniz:

1. Fonksiyonun amacını tek cümleyle açıklayın.
2. Her değişkenin o andaki değerini söyleyin.
3. Her koşul için neden doğru veya yanlış olduğunu belirtin.
4. “Burada ne varsayıyorum?” sorusunu sorun.
5. Beklenen sonuçla gerçek sonucu karşılaştırın.

Ördeğiniz yoksa kupa, saksı veya sabırlı bir takım arkadaşı da kullanılabilir. Temel mesele dinleyicinin uzmanlığı değil, açıklamanın düşünceyi yavaşlatmasıdır. Programcı kültürünün bu sevimli ritüeli bize önemli bir ders verir: Bazen hata kodun derinliklerinde değil, kod hakkında sessizce kurduğumuz hikâyededir.
