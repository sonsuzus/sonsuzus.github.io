---
layout: post
title: "Yapay Zekânın Vicdanı: Önyargı, Açıklanabilirlik ve Güvenlik"
math: true
categories: 
  - Bilgi
tags: 
  - yapay-zeka-etiği
  - algoritmik-önyargı
  - XAI
---

Yapay zekâ modelleri tarafsız matematik makineleri gibi görünse de insanların ürettiği verilerle öğrenir. Dolayısıyla toplumdaki eşitsizlikleri, eksik temsilleri ve geçmiş kararların hatalarını da miras alabilirler. Bir işe alım modelinin belirli grupları sistematik biçimde elemesi veya sağlık uygulamasının bazı hastalarda daha fazla yanılması, yalnızca teknik bir hata değil; etik, hukuki ve toplumsal bir sorundur.

``

## Algoritmik önyargı nereden gelir?

Bir modelin temel amacı, kayıp fonksiyonunu en aza indirmektir:

$$\theta^* = \arg\min_\theta \frac{1}{n}\sum_{i=1}^{n} L(f_\theta(x_i), y_i)$$

Ancak bu denklem neyin **adil** olduğunu kendiliğinden bilmez. Eğitim verisinde bir grup az temsil ediliyorsa model, toplam hatayı düşürürken o grubun hatasını önemsemeyebilir. Önyargı; veri toplama yönteminden, hatalı etiketlerden, seçilen özelliklerden veya sistemin kullanıldığı bağlamdan kaynaklanabilir.

| Önyargı türü | Kaynak | Olası sonuç |
|---|---|---|
| Örnekleme önyargısı | Bazı grupların az temsil edilmesi | Dengesiz hata oranları |
| Tarihsel önyargı | Geçmiş ayrımcılığın veriye yansıması | Eski eşitsizliklerin otomasyonu |
| Ölçüm önyargısı | Yanlış veya eksik değişkenler | Hatalı risk puanları |
| Dağılım kayması | Gerçek ortamın eğitim verisinden farklılaşması | Zamanla düşen güvenilirlik |

Adalet denetiminde yalnızca genel doğruluk yeterli değildir. Örneğin iki grup için doğru pozitif oranları karşılaştırılabilir:

$$\Delta_{TPR} = |TPR_A - TPR_B|$$

Fark büyüdükçe modelin gruplar arasında eşit fırsat sağlamadığı düşünülebilir. Yine de hiçbir adalet metriği evrensel değildir; demografik eşitlik, eşit fırsat ve hata oranı eşitliği bazı durumlarda birbiriyle çelişebilir.

## Önyargıyı kodla denetlemek

Aşağıdaki Python örneği, iki grubun doğru pozitif oranlarını hesaplayarak basit bir denetim gerçekleştirir:

```python
from sklearn.metrics import confusion_matrix

def true_positive_rate(y_true, y_pred):
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
    return tp / (tp + fn) if tp + fn else 0

for group in ["A", "B"]:
    mask = data["group"] == group
    rate = true_positive_rate(y_test[mask], predictions[mask])
    print(group, round(rate, 3))
```

Bu kod nihai bir adalet sertifikası vermez; yalnızca incelemeyi başlatır. Sonuçlar veri bilimciler, alan uzmanları, hukukçular ve etkilenen topluluklarla birlikte değerlendirilmelidir.

## XAI: Model neden böyle karar verdi?

Açıklanabilir yapay zekâ, model davranışını insanlar için anlaşılır hâle getiren yöntemleri kapsar. SHAP, özelliklerin tahmine katkısını oyun teorisi yaklaşımıyla ölçerken LIME, belirli bir tahminin çevresinde daha basit bir yerel model kurar. Karar ağaçları doğrudan yorumlanabilir olabilir; derin ağlar ise çoğunlukla sonradan açıklama araçlarına ihtiyaç duyar.

| Yaklaşım | Güçlü tarafı | Sınırlaması |
|---|---|---|
| SHAP | Tutarlı özellik katkıları | Hesaplama maliyeti |
| LIME | Yerel ve sezgisel açıklama | Farklı çalıştırmalarda değişkenlik |
| Özellik önemi | Kolay özetleme | Nedensellik göstermemesi |
| Model kartı | Amaç ve sınırları belgeleme | Güncel tutulma zorunluluğu |

Açıklama, kararın doğru veya adil olduğunu kanıtlamaz. Model ayrımcı bir kuralı gayet anlaşılır biçimde açıklayabilir! Bu nedenle XAI, adalet testleri ve insan gözetimiyle birlikte kullanılmalıdır.

## Geleceğin risklerine karşı etik emniyet kemeri

Üretken modeller; yanlış bilgi, mahremiyet ihlali, siber saldırı desteği, manipülasyon ve kontrol kaybı gibi riskler doğurabilir. Çözüm, yalnızca modele “iyi davran” demek değildir. Riskli kullanım senaryoları önceden modellenmeli, kırmızı takım testleri yapılmalı, hassas veriler anonimleştirilmeli ve erişim yetkileri sınırlandırılmalıdır.

Kuruluşlar ayrıca veri ve model kartları yayımlamalı, olay bildirim mekanizmaları kurmalı, yüksek etkili kararlarda insan itiraz hakkını korumalıdır. Modeller dağıtımdan sonra performans, güvenlik ve grup bazlı hata açısından sürekli izlenmelidir. Etik yapay zekâ tek seferlik bir kontrol kutusu değil, modelin tüm yaşam döngüsüne yayılan bir mühendislik disiplinidir. Kısacası güçlü model yapmak önemlidir; fakat kimin için, hangi bedelle ve kimin denetiminde güçlü olduğunu sormak çok daha önemlidir.
