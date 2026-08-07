---
layout: post
title: "Hata Yüzeyinde Yolculuk: Gradient Descent, Adam ve RMSprop"
math: true
categories: 
  - Bilgi
tags: 
  - optimizasyon
  - gradient-descent
  - makine-öğrenmesi
---

Bir makine öğrenmesi modelini eğitmek, sisli bir dağda en alçak noktayı bulmaya benzer. Modelin parametreleri bulunduğumuz konumu, hata fonksiyonu yüksekliği, optimizasyon algoritması ise hangi yöne adım atacağımızı belirler. Gradient Descent bu yolculuğun klasik pusulasıyken Adam ve RMSprop, arazi koşullarına göre adımlarını ayarlayan daha modern navigasyon sistemleridir.
``
## Optimizasyonun temel amacı

Bir modelin tahminleri ile gerçek değerler arasındaki fark, **kayıp fonksiyonu** üzerinden ölçülür. Parametreleri $\theta$ ile gösterirsek amaç şu problemi çözmektir:

$$\theta^* = \arg\min_{\theta} J(\theta)$$

Burada $J(\theta)$ hata yüzeyini, $\theta^*$ ise mümkün olan en düşük hatayı sağlayan parametreleri temsil eder. Gradyan, bu yüzeyde hatanın en hızlı arttığı yönü gösterir. Dolayısıyla hatayı azaltmak için gradyanın tersine ilerleriz:

$$\theta_{t+1} = \theta_t - \eta \nabla J(\theta_t)$$

$\eta$ öğrenme oranıdır. Çok küçük seçilirse eğitim kaplumbağa hızına düşer; çok büyük seçilirse algoritma minimum noktanın üzerinden zıplayabilir.

## Gradient Descent çeşitleri

Geleneksel Gradient Descent, her güncellemede bütün veri kümesini kullanır. Bu yöntem kararlı olsa da büyük veri kümelerinde pahalıdır. **Stochastic Gradient Descent** (SGD) her adımda tek örnek kullanır. Gürültülü hareket eder fakat yerel çukurlardan kaçmasına yardımcı olabilecek kadar hareketlidir. Mini-batch yaklaşımı ise küçük veri gruplarıyla çalışarak iki yöntemi dengeler.

| Yöntem | Güncelleme verisi | Avantaj | Dezavantaj |
|---|---:|---|---|
| Batch Gradient Descent | Tüm veri | Kararlı gradyan | Yavaş ve bellek maliyetli |
| SGD | Tek örnek | Hızlı güncelleme | Fazla dalgalanma |
| Mini-batch SGD | Küçük grup | Paralelleştirmeye uygun | Batch boyutu ayarlanmalı |

## Momentum: Yokuş aşağı yuvarlanan top

Momentum, geçmiş gradyanları kullanarak güncellemelerin yönünü yumuşatır:

$$v_t = \beta v_{t-1} + (1-\beta)\nabla J(\theta_t)$$

$$\theta_{t+1} = \theta_t - \eta v_t$$

Bunu yokuş aşağı yuvarlanan bir top gibi düşünebiliriz. Top doğru yönde hız kazanırken sağa sola oluşan küçük salınımlar bastırılır. Özellikle uzun ve dar hata vadilerinde klasik SGD'den daha hızlı ilerler.

## RMSprop ve Adam nasıl çalışır?

RMSprop, her parametre için gradyan karelerinin hareketli ortalamasını tutar:

$$s_t = \rho s_{t-1} + (1-\rho)g_t^2$$

Güncelleme, $\theta_{t+1}=\theta_t-\eta g_t/(\sqrt{s_t}+\epsilon)$ biçimindedir. Sık ve büyük gradyan alan parametrelerin adımı küçülürken seyrek güncellenenlerin adımı görece büyür.

Adam, Momentum'un birinci moment tahminiyle RMSprop'un ikinci moment tahminini birleştirir. Ayrıca başlangıçtaki yanlılığı düzeltir. Böylece farklı ölçeklerdeki parametreler için otomatik uyarlanan adımlar üretir.

| Algoritma | Temel fikir | Güçlü olduğu durum | Dikkat edilmesi gereken |
|---|---|---|---|
| SGD | Sabit öğrenme oranı | İyi genelleme | Hassas ayar ister |
| Momentum | Geçmiş yönleri biriktirme | Dar hata vadileri | Ek momentum katsayısı |
| RMSprop | Kare gradyan ortalaması | Değişken ve gürültülü problemler | Öğrenme oranına duyarlı olabilir |
| Adam | Momentum + RMSprop | Hızlı başlangıç, seyrek gradyanlar | Her zaman en iyi genellemeyi sağlamaz |

## Python ile küçük bir karşılaştırma

Aşağıdaki PyTorch kodu, aynı model için optimizasyon algoritmasının nasıl değiştirileceğini gösterir:

```python
import torch

model = torch.nn.Linear(10, 1)
loss_fn = torch.nn.MSELoss()

optimizers = {
    "sgd": torch.optim.SGD(model.parameters(), lr=0.01, momentum=0.9),
    "rmsprop": torch.optim.RMSprop(model.parameters(), lr=0.001),
    "adam": torch.optim.Adam(model.parameters(), lr=0.001)
}

optimizer = optimizers["adam"]

for features, targets in data_loader:
    optimizer.zero_grad()
    predictions = model(features)
    loss = loss_fn(predictions, targets)
    loss.backward()
    optimizer.step()
```

`zero_grad()` eski gradyanları temizler, `backward()` türevleri hesaplar, `step()` ise parametreleri seçilen algoritmaya göre günceller.

## Hangisini seçmeliyiz?

Adam çoğu derin öğrenme projesinde güçlü bir başlangıç seçeneğidir; hızlı yakınsar ve az ayar gerektirir. Bununla birlikte SGD ve Momentum, uygun öğrenme oranı zamanlamasıyla daha iyi genelleme sağlayabilir. RMSprop ise tekrarlayan sinir ağları ve gürültülü hedeflerde hâlâ kullanışlıdır. En doğru yaklaşım, doğrulama kaybını izlemek, birkaç algoritmayı aynı koşullarda denemek ve yalnızca eğitim hızına değil modelin görülmemiş verideki başarısına da bakmaktır.
