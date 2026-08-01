---
layout: post
title: "Yapay Genel Zekânın Tanım Sorunu: AGI Deyince Ne Anlıyoruz?"
math: true
categories: 
  - Bilgi
tags: 
  - AGI
  - yapay zeka
  - teknoloji felsefesi
---

Bir araştırmacı “AGI henüz çok uzakta” derken bir şirket yöneticisi “AGI’ye yaklaştık” diyebilir; ikisi de kendi ölçütlerine göre haklı olabilir. Çünkü Yapay Genel Zekâ, yani AGI, herkesin üzerinde uzlaştığı teknik bir hedef olmaktan çok bilim, felsefe ve pazarlama arasında şekil değiştiren hareketli bir kavramdır.
``

## “Genel” kelimesi ne kadar genel?

Dar yapay zekâ belirli görevlerde uzmanlaşır: satranç oynar, yüz tanır veya metin üretir. AGI’den ise çoğunlukla farklı alanlarda öğrenmesi, bilgisini yeni durumlara aktarması ve daha önce görmediği problemleri çözmesi beklenir. Fakat bu tanım hemen yeni sorular üretir: Kaç farklı görev yeterlidir? İnsan seviyesindeki performans hangi insanla karşılaştırılacaktır? Bilinç gerekli midir?

Genelliği basitçe görevler üzerindeki ortalama başarı gibi yazabiliriz:

$$G = \sum_{i=1}^{n} w_i P_i$$

Burada $P_i$, sistemin $i$ görevindeki performansını; $w_i$ ise o görevin önemini temsil eder. Sorun şudur: Görevleri ve ağırlıkları seçen kişi, AGI tanımını da büyük ölçüde belirler. Matematik tarafsız görünür ama ölçüm tasarımı değildir.

## Üç dünyanın üç farklı AGI’si

| Alan | AGI’den beklenen | Temel soru | Yaygın risk |
|---|---|---|---|
| Bilim | Çok sayıda görevde genelleme ve uyum | Ölçülebilir performans nedir? | Testlere aşırı uyum |
| Felsefe | Anlama, niyet, özerklik veya bilinç | Makine gerçekten anlıyor mu? | Ölçülemeyen ölçütler |
| Pazarlama | Etkileyici ve ekonomik değeri yüksek ürün | Kullanıcı bunu devrimsel bulur mu? | Kavramın abartılması |

Bilimsel yaklaşım, tekrar üretilebilir deneyler ister. Bir sistem yeni bir dili az örnekle öğrenebiliyor, robot kontrolüne geçebiliyor ve planlarını hatalarına göre düzeltebiliyorsa “genel” davranış sergilediği söylenebilir. Ancak testlerde başarılı olmak, açık dünyada güvenilir olmakla aynı şey değildir.

Felsefi yaklaşım davranışın arkasına bakar. Bir model doğru cevap verdiğinde gerçekten kavram mı oluşturmuştur, yoksa devasa örüntüler arasında güçlü bir tahmin mi yapmıştır? İşlevselcilik için doğru ve esnek davranış yeterli olabilirken bilinç merkezli görüşler öznel deneyim arar. Ne yazık ki bilinci doğrulayacak evrensel bir `unit_test()` henüz bulunmuyor.

Pazarlama dili ise kesin eşiklerden hoşlanmaz. “AGI destekli” ifadesi, teknik ayrıntı vermeden yenilik ve gelecek hissi yaratır. Böylece kavram, bilimsel hipotezden marka vaadine dönüşebilir.

## Tanımları kodla görünür kılmak

Aşağıdaki küçük Python örneği, farklı kurumların aynı sisteme neden farklı etiketler verebileceğini gösterir:

```python
criteria = {
    "bilim": {"transfer": 0.4, "reasoning": 0.4, "autonomy": 0.2},
    "felsefe": {"transfer": 0.2, "reasoning": 0.3, "autonomy": 0.5},
    "pazarlama": {"transfer": 0.2, "reasoning": 0.2, "autonomy": 0.1,
                   "etki": 0.5}
}

system = {
    "transfer": 0.8,
    "reasoning": 0.75,
    "autonomy": 0.45,
    "etki": 0.95
}

for perspective, weights in criteria.items():
    score = sum(system[key] * weight for key, weight in weights.items())
    print(perspective, round(score, 2))
```

Kod, sistem özelliklerini farklı ağırlıklarla puanlar. Pazarlama yaklaşımı kullanıcı etkisine, felsefi yaklaşım ise özerkliğe daha fazla önem verdiği için sonuçlar değişir. Bu bir AGI testi değildir; ölçüt seçiminin sonucu nasıl yönlendirdiğini gösteren düşünce deneyidir.

## Tek bir eşik yerine tanım kartı

“Bu sistem AGI mi?” sorusundan önce şu sorular sorulmalıdır:

- Hangi görev evreninde genellik aranıyor?
- Başarı eşiği ve insan karşılaştırma grubu nedir?
- Öğrenme, aktarım ve özerklik nasıl ölçülüyor?
- Bilinç veya niyet tanımın parçası mı?
- İddia bağımsız deneylerle doğrulandı mı?

AGI muhtemelen tek bir anda açılan sihirli başarı rozeti değildir. Daha çok yeteneklerin, toplumsal beklentilerin ve felsefi kabullerin birleştiği çok boyutlu bir spektrumdur. Bu nedenle sağlıklı tartışmanın ilk adımı, AGI’ye ulaşılıp ulaşılmadığını ilan etmek değil, kullanılan AGI tanımını açıkça masaya koymaktır.
