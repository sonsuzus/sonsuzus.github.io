---
layout: post
title: "RNN ve LSTM: Sıralı Verilere Hafıza Kazandırmak"
math: true
categories: 
  - Bilgi
tags: 
  - RNN
  - LSTM
  - Derin Öğrenme
---

Bir cümleyi anlamak, yalnızca son kelimeye bakmakla mümkün değildir; önceki kelimeleri de hatırlamak gerekir. Zaman serileri, borsa fiyatları, ses sinyalleri ve sensör kayıtları da benzer biçimde geçmişten izler taşır. Tekrarlayan Sinir Ağları, yani RNN’ler, bu ardışık bağı yakalamak için geliştirilmiş bellekli mimarilerdir. LSTM ise RNN’in unutkanlığını azaltan daha gelişmiş kuzenidir.
``

## Sıralı veri neden farklıdır?

Klasik ileri beslemeli ağlarda her girdi genellikle diğerlerinden bağımsız değerlendirilir. Oysa sıralı verilerde örneklerin konumu ve geliş sırası anlam taşır. “Kedi köpeği kovaladı” ile “Köpek kediyi kovaladı” aynı kelimeleri içerir; ancak sıra değişince anlam da değişir.

Bir RNN, mevcut girdiyi işlerken önceki adımdan gelen gizli durumu kullanır:

$$h_t = f(W_x x_t + W_h h_{t-1} + b)$$

Burada $x_t$ mevcut girdiyi, $h_{t-1}$ geçmişten taşınan bilgiyi, $h_t$ ise güncellenmiş hafızayı temsil eder. Ağın çıktısı çoğunlukla şu şekilde hesaplanır:

$$y_t = W_y h_t + c$$

Başka bir deyişle RNN, her adımda hem yeni veriyi okur hem de eski not defterine göz atar.

## RNN neden her şeyi hatırlayamıyor?

RNN teoride uzun süreli ilişkileri öğrenebilir. Pratikte ise eğitim sırasında kullanılan geriye yayılım, zaman boyunca çok sayıda çarpma işlemi gerçekleştirir. Türevler sürekli küçük değerlerle çarpılırsa gradyan sıfıra yaklaşır; buna **kaybolan gradyan** denir. Büyük değerlerle çarpıldığında ise **patlayan gradyan** oluşabilir.

Sonuç olarak standart RNN, birkaç adım önceki bilgiyi başarıyla kullanırken yüzlerce adım önceki kritik bir ayrıntıyı unutabilir. Romanın ilk bölümündeki karakteri finalde hatırlamayan bir okur gibi davranır.

## LSTM: Kapılarla yönetilen hafıza

Long Short-Term Memory, hücre durumu adı verilen daha kararlı bir bilgi yolu kullanır. Bilginin kaderini üç temel kapı belirler:

- **Unutma kapısı:** Eski bilginin ne kadarının silineceğine karar verir.
- **Girdi kapısı:** Yeni bilginin ne kadarının hafızaya yazılacağını seçer.
- **Çıktı kapısı:** Hafızanın hangi bölümünün dışarı aktarılacağını belirler.

Unutma kapısının basitleştirilmiş hesabı şöyledir:

$$f_t = sigmoid(W_f [h_{t-1}, x_t] + b_f)$$

$sigmoid$ sonucu 0 ile 1 arasındadır. Sıfıra yakın değer “unut”, bire yakın değer ise “sakla” anlamına gelir.

| Özellik | Standart RNN | LSTM |
|---|---|---|
| Hafıza yapısı | Gizli durum | Gizli durum ve hücre durumu |
| Uzun bağımlılıklar | Zayıf | Daha başarılı |
| Parametre sayısı | Az | Daha fazla |
| Eğitim maliyeti | Daha düşük | Daha yüksek |
| Uygun senaryo | Kısa diziler | Uzun ve karmaşık diziler |

## Keras ile küçük bir LSTM modeli

Aşağıdaki model, son 30 zaman adımını inceleyerek bir sonraki sayısal değeri tahmin eder. Borsa kapanış fiyatları veya sensör ölçümleri gibi verilerde kullanılabilir:

```python
from tensorflow.keras import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

model = Sequential([
    LSTM(64, input_shape=(30, 1), return_sequences=True),
    Dropout(0.2),
    LSTM(32),
    Dense(1)
])

model.compile(optimizer="adam", loss="mse")
model.fit(X_train, y_train, epochs=20, batch_size=32)
```

İlk LSTM katmanı bütün zaman adımlarına ait çıktıları ikinci LSTM katmanına aktarır. `Dropout`, nöronların bir bölümünü eğitim sırasında geçici olarak kapatarak ezberlemeyi azaltır. Son `Dense` katmanı tek bir tahmin üretir. Modelden önce verileri ölçeklendirmek ve örnekleri `(örnek, zaman_adımı, özellik)` biçimine getirmek gerekir.

## Nerelerde kullanılır?

RNN ve LSTM; konuşma tanıma, metin üretimi, duygu analizi, hava tahmini, anomali tespiti ve finansal modelleme gibi alanlarda kullanılabilir. Bununla birlikte borsa tahmininde geçmiş fiyatların geleceği garanti etmediği unutulmamalıdır. Günümüzde Transformer mimarileri birçok dil görevinde öne çıksa da LSTM, daha küçük veri kümeleri ve düşük kaynaklı zaman serisi projeleri için hâlâ güçlü, anlaşılır ve pratik bir seçenektir.
