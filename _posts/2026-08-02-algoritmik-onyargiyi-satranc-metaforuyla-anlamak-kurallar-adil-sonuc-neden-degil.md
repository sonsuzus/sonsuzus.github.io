---
layout: post
title: "Algoritmik Önyargıyı Satranç Metaforuyla Anlamak: Kurallar Adil, Sonuç Neden Değil?"
math: true
categories: 
  - Bilgi
tags: 
  - algoritmik önyargı
  - etik
  - kural tabanlı sistemler
---

Satrançta kurallar herkes için aynıdır: Piyon bir kare ilerler, fil çapraz gider, şah tehdit altındaysa korunmalıdır. Yine de bir oyuncuya vezir, diğerine yalnızca birkaç piyon vererek oyunu başlatırsak kuralların eşit olması karşılaşmayı adil yapmaz. Kural tabanlı yazılımlarda algoritmik önyargı da çoğu zaman böyle doğar. Kod herkese aynı koşulları uygulayabilir; fakat başlangıç koşulları, kullanılan göstergeler ve geçmişten alınan veriler eşit değilse sonuçlar sistematik biçimde bazı grupları dezavantajlı hâle getirebilir.

``

## Tahta Aynı, Başlangıç Konumları Farklı

Kural tabanlı sistemler, önceden belirlenen koşullara göre karar verir. Örneğin bir kredi sistemi şöyle çalışabilir: “Geliri belirli bir sınırın altında olan ve son iki yılda düzenli ödeme geçmişi bulunmayan başvuruyu reddet.” Bu kuralda cinsiyet, yaş veya etnik köken açıkça yazmıyor olabilir. Dolayısıyla sistem ilk bakışta tarafsız görünür.

Ancak ödeme geçmişi oluşturma fırsatı herkese eşit dağılmamışsa kural, geçmişteki eşitsizlikleri yeniden üretir. Satranç metaforuyla söylersek hakem taşların rengini önemsemiyordur; fakat oyunculardan biri oyuna zaten eksik taşlarla başlamıştır.

Bir grubun olumlu karar alma oranını şöyle gösterebiliriz:

$$P(\hat{Y}=1 \mid G=g)$$

Burada $\hat{Y}=1$ olumlu kararı, $G=g$ ise belirli bir gruba üyeliği ifade eder. İki grup için bu olasılıklar ciddi biçimde farklıysa açıkça ayrımcı bir kural bulunmasa bile sonuçlarda önyargı olabilir.

## Önyargı Hangi Hamlelerde Gizlenir?

| Satranç unsuru | Algoritmik karşılığı | Olası adaletsizlik |
|---|---|---|
| Başlangıç dizilimi | Geçmiş veri ve koşullar | Eski eşitsizliklerin devralınması |
| Hamle kuralları | İş kuralları ve eşikler | Herkese aynı görünen katı ölçütler |
| Taşın değeri | Özelliklere verilen önem | Bazı göstergelerin abartılması |
| Hakemin kararı | Denetim ve itiraz süreci | Hataların düzeltilememesi |
| Oyun sonucu | Kabul, ret veya sıralama | Belirli grupların sürekli geride kalması |

Özellikle **vekil değişkenler** önemlidir. Sistem mahalle kodunu kullanıyor ama etnik kökeni kullanmıyor olabilir. Ne var ki mahalle kodu toplumsal ayrışma nedeniyle etnik köken veya gelir düzeyiyle güçlü biçimde ilişkiliyse yasaklanan bilgi arka kapıdan oyuna döner. Fil yerine “çapraz ilerleyen uzun taş” demek, onun fil olduğu gerçeğini değiştirmez.

## Basit Bir Kural Nasıl Sorun Üretir?

Aşağıdaki örnek, başvuruları gelir ve kredi geçmişine göre değerlendirir:

```python
def kredi_karari(gelir, kredi_gecmisi_ayi):
    puan = 0

    if gelir >= 30_000:
        puan += 1
    if kredi_gecmisi_ayi >= 24:
        puan += 1

    return "Kabul" if puan == 2 else "Ret"
```

Kod kısa, anlaşılır ve herkese aynı şekilde uygulanır. Fakat düzenli finansal hizmetlere erişemeyen kişiler 24 aylık geçmiş koşulunu karşılayamaz. Böylece teknik olarak “eşit” kural, fırsat eşitsizliğini cezaya dönüştürür.

Sonuçları incelemek için seçim oranları karşılaştırılabilir:

$$\text{Oran} = \frac{P(\hat{Y}=1 \mid G=A)}{P(\hat{Y}=1 \mid G=B)}$$

Bu değerin $1$'den belirgin biçimde uzaklaşması araştırılması gereken bir dengesizliğe işaret eder. Ancak tek bir matematiksel ölçü adaletin tamamını açıklamaz; yanlış ret oranları, ekonomik koşullar ve kararın insanlar üzerindeki etkisi de değerlendirilmelidir.

## Daha Adil Bir Oyun Kurmak

İlk adım, yalnızca kodu değil oyunun tamamını denetlemektir. Kurallar farklı gruplara ait örnek verilerle test edilmeli, vekil değişkenler araştırılmalı ve eşik değerlerinin etkisi ölçülmelidir. İnsanlara karar gerekçesi sunmak ve itiraz kanalı açmak da kritiktir.

Ayrıca “herkese aynı kural” ile “herkese adil fırsat” arasındaki fark unutulmamalıdır. Bazen geçmişi daha kısa olan başvurular için alternatif güvenilirlik göstergeleri kullanmak gerekir. Amaç bir gruba bedava vezir vermek değil, kimsenin oyuna şahı eksik başlamadığından emin olmaktır.

Algoritmik adalet, yalnızca tarafsız görünen kurallar yazma işi değildir. Asıl soru şudur: Tahtayı kim kurdu, taşların değerini kim belirledi ve oyun bittiğinde kaybedenler neden hep aynı tarafta kaldı?
