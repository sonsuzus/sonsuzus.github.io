---
layout: post
title: "Biyometrik Örüntü Tanıma: Parmak İzi ve İris Eşleştirme Sistemi"
math: true
categories: 
  - Proje
tags: 
  - biyometri
  - örüntü tanıma
  - Python
---

Telefonun kilidini parmağınla açarken cihazın içinde minik bir dedektif çalışır: Görüntüyü temizler, ayırt edici özellikleri çıkarır ve bunları kayıtlı şablonla karşılaştırır. Bu projede gerçek kişisel veriler toplamadan, parmak izi veya iris verisini temsil eden yapay özellik vektörleriyle temel bir biyometrik eşleştirme sisteminin mantığını inceleyeceğiz.

``

## Biyometrik eşleştirme nasıl çalışır?

Bir biyometrik sistem ham görüntüleri doğrudan karşılaştırmak yerine genellikle **şablon** adı verilen sayısal temsiller üretir. Parmak izinde çizgi sonları ve çatallanmalar; iriste ise doku frekansları, halkalar ve yerel desenler özellik olarak kullanılabilir.

Tipik işlem hattı şöyledir:

1. Sensörden görüntü alınır.
2. Gürültü azaltılır ve görüntü normalize edilir.
3. İlgi bölgesi belirlenir.
4. Ayırt edici özellikler çıkarılır.
5. Özellik vektörü kayıtlı şablonla karşılaştırılır.
6. Benzerlik belirlenen eşiği geçiyorsa eşleşme kabul edilir.

| Aşama | Parmak izi örneği | İris örneği |
|---|---|---|
| Ön işleme | Çizgileri belirginleştirme | Göz bebeğini ayırma |
| Özellik | Minutiae noktaları | Doku kodları |
| Sorun | Parmağın kayması | Göz kapağı ve yansıma |
| Temsil | Nokta ve yön listesi | İkili veya sayısal vektör |

## Benzerliği matematikle ölçmek

İki özellik vektörü arasındaki uzaklık için Öklid uzaklığı kullanılabilir. Kayıtlı şablon $x$, yeni örnek $y$ ise:

$$d(x,y)=\sqrt{\sum_{i=1}^{n}(x_i-y_i)^2}$$

Uzaklık küçüldükçe örnekler birbirine daha çok benzer. Benzerlik puanını $[0,1]$ aralığına taşımak için basitçe şu dönüşüm uygulanabilir:

$$s(x,y)=\frac{1}{1+d(x,y)}$$

Karar kuralımız $s \geq t$ olabilir. Buradaki $t$ eşik değeridir. Eşiği yükseltmek güvenliği artırabilir ancak gerçek kullanıcıların reddedilmesine de yol açabilir.

| Eşik tercihi | Avantaj | Dezavantaj |
|---|---|---|
| Düşük | Kullanım daha rahat | Yanlış kabul artabilir |
| Yüksek | Yetkisiz kabul azalabilir | Yanlış ret artabilir |
| Dengeli | İki hata türünü dengeler | Test verisi gerektirir |

## Python ile basit prototip

Aşağıdaki kod gerçek görüntüler yerine sentetik biyometrik vektörler kullanır. Böylece kişisel veri toplamadan eşleştirme mekanizmasını deneyebiliriz.

```python
import numpy as np

class BiometricMatcher:
    def __init__(self, threshold=0.80):
        self.threshold = threshold
        self.templates = {}

    def enroll(self, user_id, features):
        vector = np.asarray(features, dtype=float)
        norm = np.linalg.norm(vector)
        if norm == 0:
            raise ValueError("Sıfır vektörü kaydedilemez.")
        self.templates[user_id] = vector / norm

    def verify(self, user_id, sample):
        if user_id not in self.templates:
            return False, 0.0

        sample = np.asarray(sample, dtype=float)
        norm = np.linalg.norm(sample)
        if norm == 0:
            return False, 0.0

        sample = sample / norm
        template = self.templates[user_id]
        distance = np.linalg.norm(template - sample)
        score = 1 / (1 + distance)
        return score >= self.threshold, score

matcher = BiometricMatcher(threshold=0.80)
matcher.enroll("kullanici_42", [0.12, 0.77, 0.31, 0.55, 0.18])

accepted, score = matcher.verify(
    "kullanici_42",
    [0.11, 0.75, 0.34, 0.53, 0.20]
)
print(f"Kabul: {accepted}, skor: {score:.3f}")
```

`enroll` metodu özellik vektörünü normalize ederek saklar. `verify` ise yeni örnekle kayıtlı şablonun uzaklığını hesaplar. Normalizasyon, ölçüm ölçeğindeki farklılıkların etkisini azaltır; fakat gerçek sistemlerde dönüş, konum ve sensör kalitesi için çok daha gelişmiş işlemler gerekir.

## Başarıyı nasıl değerlendirebiliriz?

Sistemi yalnızca “çalıştı” diyerek değerlendirmek yeterli değildir. **FAR** yetkisiz örneklerin kabul oranını, **FRR** ise gerçek kullanıcıların reddedilme oranını gösterir:

$$FAR=\frac{yanlış\ kabuller}{yetkisiz\ denemeler}$$

$$FRR=\frac{yanlış\ retler}{gerçek\ kullanıcı\ denemeleri}$$

Eşiği farklı değerlerde deneyerek bu iki metriği karşılaştırabiliriz. Ayrıca farklı sensör koşulları, gürültü seviyeleri ve kullanıcı gruplarıyla test yapmak olası yanlılıkları ortaya çıkarır.

Son olarak biyometrik veri parola gibi kolayca değiştirilemez. Bu nedenle ham görüntü saklamak yerine şifrelenmiş veya iptal edilebilir şablonlar kullanılmalı; açık rıza, veri minimizasyonu, erişim kontrolü ve silme politikaları tasarımın merkezinde olmalıdır. Küçük dedektifimiz zeki olabilir, ama aynı zamanda mahremiyete saygılı olmak zorundadır.
