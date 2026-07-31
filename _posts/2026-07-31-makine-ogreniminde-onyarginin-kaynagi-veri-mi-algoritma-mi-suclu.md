---
layout: post
title: "Makine Öğreniminde Önyargının Kaynağı: Veri mi, Algoritma mı Suçlu?"
math: true
categories: 
  - Bilgi
tags: 
  - makine öğrenimi
  - algoritmik önyargı
  - veri etiği
---

Bir makine öğrenimi modeli ayrımcı bir karar verdiğinde ilk şüpheli genellikle algoritmadır. Oysa algoritma çoğu zaman toplumsal gerçekliği yansıtan, hatta büyüten bir ayna gibi çalışır. İşe alımdan kredi değerlendirmesine kadar geçmiş kararlarla oluşturulan veri kümeleri; eşitsizlikleri, eksik temsili ve insan önyargılarını sessizce modele taşıyabilir. Kısacası mesele yalnızca “kötü kod” değil, hangi dünyanın sayılara dönüştürüldüğüdür.
``

## Veri tarafında neler oluyor?

Bir veri kümesi tarafsız bir doğa olayı değildir. Önce neyin ölçüleceğine karar verilir, ardından kimlerden veri toplanacağı seçilir ve son olarak gözlemler etiketlenir. Bu üç aşamanın her birinde toplumsal eşitsizlik sisteme sızabilir.

Örneğin geçmişte yöneticilik pozisyonlarına çoğunlukla erkekler atanmışsa, başarılı yöneticileri tanımak için eğitilen model “erkek olmayı” başarıyla ilişkili görebilir. Cinsiyet sütunu kaldırılsa bile okul, posta kodu, kariyer boşluğu veya kullanılan kelimeler gibi değişkenler onu dolaylı biçimde temsil edebilir. Bu değişkenlere **vekil değişkenler** denir.

| Önyargı kaynağı | Nasıl oluşur? | Olası sonuç |
|---|---|---|
| Örnekleme yanlılığı | Bazı gruplar az temsil edilir | Model bu gruplarda daha çok hata yapar |
| Etiket yanlılığı | İnsan kararları gerçek kabul edilir | Geçmiş ayrımcılık öğrenilir |
| Ölçüm yanlılığı | Aynı özellik gruplarda farklı ölçülür | Hatalı karşılaştırmalar yapılır |
| Tarihsel yanlılık | Veri mevcut eşitsizliği yansıtır | Eşitsizlik otomatikleştirilir |

## Peki algoritma masum mu?

Tam olarak değil. Algoritma, verideki örüntülerden hangilerinin önemli sayılacağını kullanılan amaç fonksiyonuna göre belirler. Standart sınıflandırmada hedef genellikle ortalama kaybı azaltmaktır:

$$\min_{\theta} \frac{1}{n}\sum_{i=1}^{n} L(f_{\theta}(x_i), y_i)$$

Bu formül her kaydın kaybını toplar; ancak hataların toplumsal maliyetini bilmez. Çoğunluk grubunda başarıyı artıran bir karar, azınlık grubundaki ciddi hata artışını örtebilir. Üstelik doğruluk oranı yüksek olsa bile model adil olmayabilir.

| Ölçüt | Sorduğu soru | Tek başına yeterli mi? |
|---|---|---|
| Accuracy | Toplam tahminlerin kaçı doğru? | Hayır |
| Demografik eşitlik | Olumlu karar oranları benzer mi? | Her durumda değil |
| Eşit fırsat | Gerçek pozitifler eşit yakalanıyor mu? | Bağlama bağlı |
| Kalibrasyon | Aynı puan aynı riski mi ifade ediyor? | Diğer hataları gizleyebilir |

Örneğin eşit fırsat yaklaşımında grupların doğru pozitif oranlarının yakın olması beklenir:

$$P(\hat{Y}=1\mid Y=1,A=a) \approx P(\hat{Y}=1\mid Y=1,A=b)$$

Buradaki $A$, hassas grubu temsil eder. Ancak farklı adalet ölçütleri matematiksel olarak birbiriyle çatışabilir. Bu nedenle “adil model” tek düğmeyle etkinleştirilen bir özellik değildir; hukuki, etik ve bağlamsal bir tercihtir.

## Küçük bir adalet kontrolü

Aşağıdaki Python kodu, modelin gruplara göre doğru pozitif oranını hesaplar. Böylece genel başarı puanının arkasında saklanan farklar görülebilir:

```python
import pandas as pd

def true_positive_rate(group):
    positives = group[group["gercek"] == 1]
    if len(positives) == 0:
        return None
    return (positives["tahmin"] == 1).mean()

sonuclar = (
    veri.groupby("grup")
        .apply(true_positive_rate, include_groups=False)
)

print(sonuclar)
print("En büyük fark:", sonuclar.max() - sonuclar.min())
```

Kod, her grup için gerçekten olumlu örneklerin ne kadarının doğru bulunduğunu ölçer. Büyük fark görülmesi doğrudan ayrımcılığı kanıtlamaz; fakat veri toplama, eşik seçimi ve hata maliyetlerinin araştırılması gerektiğini gösteren güçlü bir alarmdır.

## Suçlu aramak yerine sistemi incelemek

Önyargı genellikle veri **veya** algoritma şeklinde ikili bir seçime indirgenemez. Veri toplumsal geçmişi taşır; algoritma onu optimize eder; kurum ise sonuçların nasıl kullanılacağını belirler. Çözüm, veri kaynağını belgelemek, eksik grupları temsil etmek, etiketleri denetlemek, grup bazlı metrikler yayımlamak ve modeli kullanım sonrasında izlemektir.

En önemlisi de etkilenen toplulukları tasarım sürecine katmaktır. Çünkü adalet yalnızca matematikçilerin tanımladığı bir denklem değil, sonuçlarına insanların katlandığı toplumsal bir karardır. Makine tarafsız görünse de ona geçmişi biz anlatırız; hangi geleceği kuracağını da yine biz belirleriz.
