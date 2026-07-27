---
layout: post
title: "Bizans Generalleri Problemi: Dağıtık Sistemlerin İçindeki İnsan Hikâyesi"
math: true
categories: 
  - Bilgi
tags: 
  - dağıtık sistemler
  - Bizans hata toleransı
  - sosyal güven
---

Bir grup insanın ortak karar vermesi gerektiğini düşünün: Bazıları dürüst, bazıları kararsız, bazılarıysa kasıtlı olarak yalan söylüyor. Üstelik kimse aynı odada değil; iletişim gecikebilir, mesajlar kaybolabilir ve farklı kişilere farklı bilgiler ulaşabilir. Bu senaryo bir aile grubunu, şirket toplantısını veya siyasi ittifakı çağrıştırsa da dağıtık sistemlerin en ünlü problemlerinden birini anlatır: **Bizans Generalleri Problemi**. Bilgisayar bilimindeki bu teknik mesele, özünde güvenilir bir otorite olmadan işbirliği yapabilmenin hikâyesidir.
``

## Generaller neden anlaşamıyor?

Problemde Bizans ordusunu kuşatan generaller, saldırmak ya da geri çekilmek konusunda ortak karar vermelidir. Başarı için yalnızca karar vermeleri yetmez; dürüst generallerin **aynı kararı** vermesi gerekir. Ancak aralarında hainler bulunabilir. Bir hain, bir generale “saldır”, diğerine “geri çekil” mesajı göndererek uzlaşmayı sabote edebilir.

Buradaki temel hedefler şunlardır:

1. **Tutarlılık:** Bütün dürüst katılımcılar aynı sonuca ulaşmalıdır.
2. **Geçerlilik:** Komutan dürüstse onun önerdiği değer kabul edilmelidir.
3. **Sonlanma:** Katılımcılar sonsuza kadar beklememeli, sonunda karar vermelidir.

Bu ilkeler teknik görünse de günlük hayattaki güven beklentilerimize benzer. Bir ekipte herkesin aynı plana göre hareket etmesini, doğru bilginin korunmasını ve toplantının bir gün gerçekten bitmesini isteriz.

## Matematik bize ne söylüyor?

Klasik Bizans hata toleransında, en fazla $f$ kötü niyetli düğüme dayanabilmek için genellikle en az

$$n \geq 3f + 1$$

düğüm gerekir. Örneğin bir kötü niyetli katılımcıya karşı sistemde en az dört düğüm bulunmalıdır. Karar oluşturmak için kullanılan tipik yeter sayı ise $2f+1$ dürüstlük ağırlığı taşıyan oydur.

Bunun mantığı “çoğunluk her zaman haklıdır” demek değildir. Amaç, iki çelişkili kararın aynı anda yeterli desteği toplamasını engellemektir. Yeter sayılar kesiştiğinde, bu kesişimde en az bir dürüst katılımcı bulunur ve dürüst düğüm iki farklı kararı onaylamaz.

| İnsan topluluğu | Dağıtık sistem | Ortak sorun |
|---|---|---|
| Söylenti yayan kişi | Hatalı veya kötü niyetli düğüm | Çelişkili bilgi üretmek |
| Toplantı tutanağı | Dağıtık kayıt | Geçmişi doğrulanabilir kılmak |
| Güvenilir çoğunluk | Quorum | Karara yeterli destek sağlamak |
| İmza ve mühür | Dijital imza | Mesajın kaynağını kanıtlamak |
| Son teslim tarihi | Zaman aşımı | Sonsuz beklemeyi önlemek |

## Küçük bir oylama modeli

Aşağıdaki Python örneği, düğümlerin önerilerini sayarak bir karar için yeter sayı aranmasını gösterir:

```python
from collections import Counter

def bizans_karari(oylar, f):
    """En az 2f+1 destek alan değeri döndürür."""
    gereken = 2 * f + 1
    sayac = Counter(oylar)

    for karar, destek in sayac.items():
        if destek >= gereken:
            return karar

    return "UZLASMA_YOK"

oylar = ["SALDIR", "SALDIR", "SALDIR", "GERI_CEKIL"]
print(bizans_karari(oylar, f=1))  # SALDIR
```

Kodda tek bir hain düğüm farklı oy verse bile üç uyumlu oy kararı oluşturur. Elbette gerçek protokoller bundan daha karmaşıktır: Mesaj turları, kimlik doğrulama, lider seçimi, ağ gecikmeleri ve tekrar saldırıları hesaba katılır. PBFT gibi protokoller bu fikirleri uygularken blokzincir sistemleri ekonomik teşvikleri de güven modeline ekler.

## Güven, kişilik değil mekanizma meselesidir

Bizans Generalleri Problemi’nin en insani dersi şudur: Sağlam işbirliği, herkesin iyi niyetli olduğunu varsayarak kurulmaz. Bunun yerine sistem, anlaşmazlığı görünür kılar, iddiaları doğrular ve kötü davranışın etkisini sınırlar.

Toplumlarda bunu şeffaf kayıtlar, bağımsız denetim ve görev ayrılığıyla yaparız. Yazılımda ise çoğaltma, dijital imza, quorum ve hata toleranslı protokoller kullanırız. Güven böylece “Sana inanıyorum” cümlesinden çıkarak “Yanlış davransan bile sistem çalışmaya devam ediyor” güvencesine dönüşür.

Sonuçta Bizans generalleri yalnızca sunucuların hikâyesi değildir. Farklı bilgilere, çıkarlara ve niyetlere sahip aktörlerin ortak bir gerçeklik üretme çabasıdır. Dağıtık sistemler bize kusursuz insanları değil, kusurlara rağmen işbirliğini mümkün kılan kuralları tasarlamamız gerektiğini hatırlatır.
