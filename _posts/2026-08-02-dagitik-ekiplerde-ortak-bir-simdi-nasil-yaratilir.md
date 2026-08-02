---
layout: post
title: "Dağıtık Ekiplerde Ortak Bir “Şimdi” Nasıl Yaratılır?"
math: true
categories: 
  - Bilgi
tags: 
  - uzaktan çalışma
  - dağıtık ekipler
  - saat dilimleri
---

Uzaktan çalışma ofisi ortadan kaldırırken zamanı da görünmez biçimde yeniden tasarladı. İstanbul’daki bir geliştirici güne başlarken San Francisco’daki ekip arkadaşı uyuyor, Tokyo’daki tasarımcı ise bilgisayarını kapatıyor olabilir. Böyle bir ekipte “hemen konuşalım” masum bir öneri değil, coğrafi bir ayrıcalıktır. Ortak bir “şimdi” yaratmak, herkesi aynı anda çevrim içi tutmak değil; eşzamanlı ve eşzamansız çalışmayı bilinçli biçimde dengelemektir.
``

## Saat aynı, deneyim farklı

Saat dilimleri teknik olarak UTC’ye göre tanımlanan ofsetlerdir. Bir kişinin yerel zamanı basitçe şöyle gösterilebilir:

$$T_{yerel} = T_{UTC} + O$$

Burada $O$, saat dilimi ofsetidir. Ancak insan deneyimi bu formülden daha karmaşıktır. Saat 09.00’da yapılan bir toplantı bir çalışan için kahveyle başlayan sakin bir sabah, diğeri için aile yemeğinin ortası olabilir. Üstelik yaz saati uygulamaları nedeniyle ofsetler yıl boyunca sabit kalmayabilir.

Dağıtık ekiplerde zamanın üç farklı biçimi vardır:

| Zaman biçimi | Anlamı | Örnek |
|---|---|---|
| Kronolojik zaman | Takvim ve saatle ölçülen zaman | Sprint pazartesi başlar |
| Biyolojik zaman | Bedenin uyku ve enerji ritmi | Gece toplantısında odak düşer |
| Sosyal zaman | Aile ve toplum düzeni | Akşam yemeği, okul çıkışı |

İyi bir çalışma düzeni yalnızca kronolojik zamanı optimize etmez; diğer iki katmanı da hesaba katar.

## Eşzamanlılık bir spektrumdur

Ofis kültürü çoğu zaman üretkenliği aynı anda bulunmakla eşleştirir. Oysa yazılım ekiplerinde işlerin önemli bir bölümü eşzamansız yürütülebilir. Kod incelemesi, teknik karar kaydı ve durum güncellemesi için herkesin aynı görüntülü görüşmede bulunması gerekmez.

| Eşzamanlı çalışma | Eşzamansız çalışma |
|---|---|
| Hızlı geri bildirim sağlar | Derin çalışmayı destekler |
| Belirsiz konuları çözmekte etkilidir | Saat dilimlerinden bağımsızdır |
| Toplantı yorgunluğu yaratabilir | Yanıt gecikmesi oluşturabilir |
| Beyin fırtınasına uygundur | Kalıcı ve aranabilir kayıt üretir |

Buradaki amaç yöntemlerden birini seçmek değil, iletişimin gecikme maliyetine göre seçim yapmaktır. Bir mesajın bekleme süresi $L$, ekip üyeleri arasındaki saat farkı $D$ ve günlük ortak çalışma penceresi $W$ ile ilişkili düşünülebilir:

$$L \approx \max(0, D - W)$$

Ortak pencere küçüldükçe soruların bir sonraki güne taşınma ihtimali artar. Bu nedenle iyi yazılmış bir mesaj; bağlamı, beklenen çıktıyı ve son tarihi birlikte içermelidir.

## Ortak pencereyi adil biçimde bulmak

Aşağıdaki Python örneği, ekip üyelerinin UTC cinsinden çalışma aralıklarının kesişimini hesaplar:

```python
from typing import List, Tuple

def ortak_pencere(araliklar: List[Tuple[int, int]]) -> Tuple[int, int] | None:
    baslangic = max(aralik[0] for aralik in araliklar)
    bitis = min(aralik[1] for aralik in araliklar)

    if baslangic >= bitis:
        return None
    return baslangic, bitis

calisma_saatleri = [(6, 14), (8, 16), (12, 20)]
print(ortak_pencere(calisma_saatleri))  # (12, 14)
```

Fonksiyon en geç başlangıç ile en erken bitişi karşılaştırır. Sonuç `(12, 14)` ise ekip UTC 12.00–14.00 arasında buluşabilir. Ancak matematiksel kesişim otomatik olarak adalet anlamına gelmez. Sürekli aynı kişinin sabahın köründe toplantıya katılması, zaman yükünü görünmez biçimde ona aktarır. Kritik toplantı saatlerini dönüşümlü planlamak daha adildir.

## “Şimdi”yi bir protokole dönüştürmek

Sağlıklı bir dağıtık ekip şu pratikleri benimseyebilir:

- Tarih ve saatleri yerel kısaltmalar yerine UTC ile belirtmek.
- Kararları toplantı sonrasında yazılı olarak kaydetmek.
- Mesajlarda “acil”, “bugün” ve “bu hafta” seviyelerini ayırmak.
- Çevrim içi durumunu anında yanıt zorunluluğu saymamak.
- Ortak saatleri kararlar için, bireysel saatleri üretim için korumak.
- Toplantı yükünü ve uygunsuz saatleri ekip içinde dönüşümlü dağıtmak.

Sonuçta ortak bir “şimdi”, duvardaki saatlerin eşitlenmesi değildir. Ekibin ne zaman birlikte düşünmesi, ne zaman bağımsız ilerlemesi ve ne kadar gecikmeyi kabul etmesi gerektiğine dair paylaşılan bir protokoldür. Dağıtık ekipler zamanı yönetmekten çok, zaman hakkında güven inşa eder. İyi tasarlanmış bir düzende iş güneşi takip eder; çalışanlar ise onu kovalamak zorunda kalmaz.
