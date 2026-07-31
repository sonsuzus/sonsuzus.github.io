---
layout: post
title: "Yapay Zekânın Kara Kutusu: Açıklayamadığımız Bir Karara Güvenebilir miyiz?"
math: true
categories: 
  - Bilgi
tags: 
  - yapay zeka etiği
  - açıklanabilir yapay zeka
  - makine öğrenmesi
---

Bir yapay zekâ sistemi kredi başvurunuzu reddettiğinde, işe alım sürecinde sizi elediğinde veya tıbbi görüntünüzü “riskli” olarak işaretlediğinde yalnızca sonuca bakmak yeterli midir? Model yüksek doğruluk oranına sahip olsa bile “Neden?” sorusuna cevap veremiyorsa ortada teknik olduğu kadar etik bir sorun da vardır. İşte **kara kutu sorunu**, modelin girdileri ile çıktıları arasındaki mantığın insanlar tarafından anlaşılmasının güç olduğu bu noktada ortaya çıkar.
``
## Kara kutu tam olarak nedir?

Karar ağaçları ve doğrusal regresyon gibi bazı modellerin davranışları görece kolay izlenebilir. Buna karşılık milyonlarca parametre içeren derin sinir ağlarında tek bir kararın hangi iç ilişkiler sonucunda üretildiğini açıklamak zordur. Model matematiksel olarak çalışır; ancak matematiksel işlemlerin mevcut olması, kararın insan açısından anlamlı biçimde açıklanabildiği anlamına gelmez.

Basit bir sınıflandırıcı şu fonksiyonla düşünülebilir:

$$\hat{y} = f(x; \theta)$$

Burada $x$ girdileri, $\theta$ öğrenilmiş parametreleri, $\hat{y}$ ise tahmini temsil eder. Eğitim sırasında amaç, gerçek değer $y$ ile tahmin arasındaki kaybı azaltmaktır:

$$\theta^* = \arg\min_\theta \sum_{i=1}^{n} L(f(x_i;\theta), y_i)$$

Dikkat edilirse bu hedef, açıklanabilirliği doğrudan ödüllendirmez. Modelden yalnızca hatasını küçültmesi istenir. Dolayısıyla performans yarışındaki bir sistem, doğru cevaba etik açıdan sorunlu kestirme yollarla ulaşabilir. Örneğin hastalık yerine görüntünün çekildiği hastaneyi öğrenebilir.

## Şeffaflık mı, performans mı?

Model seçimi çoğu zaman tek boyutlu bir “en yüksek doğruluk kazanır” yarışına dönüştürülür. Oysa mühendislik açısından maliyet, gecikme, denetlenebilirlik ve kararın etkisi birlikte değerlendirilmelidir.

| Yaklaşım | Güçlü yanı | Zayıf yanı | Uygun kullanım |
|---|---|---|---|
| Doğrusal model | Kolay açıklanır ve denetlenir | Karmaşık ilişkileri kaçırabilir | Kredi puanlama, basit risk analizi |
| Karar ağacı | Kurallar görselleştirilebilir | Derinleşince karmaşıklaşır | Operasyonel karar sistemleri |
| Derin sinir ağı | Yüksek temsil gücü sunar | Kararlar opak olabilir | Görüntü, ses ve doğal dil |
| Hibrit sistem | Performans ile kontrolü dengeler | Tasarımı ve bakımı daha zordur | Yüksek riskli uygulamalar |

Buradaki ödünleşim mutlak değildir. Açıklanabilir bir model her zaman düşük performanslı olmadığı gibi, karmaşık bir model de otomatik olarak daha başarılı değildir. Önce basit bir taban model denenmeli; karmaşıklığın sağladığı ölçülebilir fayda, getirdiği denetim maliyetinden büyükse daha opak modele geçilmelidir.

## Açıklama üretmek, modeli açıklamak mıdır?

LIME ve SHAP gibi yöntemler modelin belirli bir tahmininde hangi özelliklerin etkili olduğunu tahmin eder. Ancak bunlar çoğunlukla modelin kendisi değil, davranışının yerel bir yorumudur. Yani açıklama kulağa ikna edici gelebilir fakat modelin gerçek iç mantığını eksiksiz göstermeyebilir.

Aşağıdaki örnek, bir tahminin yanında özellik katkılarını da raporlayan basitleştirilmiş bir kontrol katmanı kurar:

```python
def karar_raporu(model, explainer, veri, esik=0.70):
    olasilik = model.predict_proba(veri)[0, 1]
    katkilar = explainer(veri)

    en_etkili = sorted(
        zip(veri.columns, katkilar.values[0]),
        key=lambda x: abs(x[1]),
        reverse=True
    )[:3]

    return {
        "karar": "onay" if olasilik >= esik else "inceleme",
        "guven": round(float(olasilik), 3),
        "etkili_faktorler": en_etkili
    }
```

Bu kod, modeli bütünüyle şeffaflaştırmaz. Bunun yerine sonucu, güven değerini ve en etkili üç faktörü sunarak insan denetimine elverişli hâle getirir. Özellikle eşik altındaki vakaların otomatik reddedilmek yerine uzman incelemesine gönderilmesi önemlidir.

## Güven nasıl inşa edilir?

Güven, yalnızca açıklama paneli eklemekle oluşmaz. Veri kaynağı belgelenmeli, farklı gruplar için hata oranları ölçülmeli, model sürümleri kaydedilmeli ve kararlara itiraz yolu sağlanmalıdır. Yüksek riskli alanlarda amaç “Her kararı yapay zekâ versin” değil, **hangi kararın otomasyona bırakılabileceğini kanıtlamak** olmalıdır.

Sonuç olarak şeffaflık ile performans arasındaki seçim teknik bir ayar değil, toplumsal etkileri bulunan bir tasarım kararıdır. Bir puanlık doğruluk artışı açıklanabilirliği, adaleti ve itiraz hakkını yok ediyorsa bu artış başarı sayılmayabilir. İyi mühendislik yalnızca çalışan model değil; sınırlarını söyleyebilen, denetlenebilen ve gerektiğinde kararını insana bırakabilen sistem üretir.
