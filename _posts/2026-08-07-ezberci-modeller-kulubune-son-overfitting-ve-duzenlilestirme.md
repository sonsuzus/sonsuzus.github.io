---
layout: post
title: "Ezberci Modeller Kulübüne Son: Overfitting ve Düzenlileştirme"
math: true
categories: 
  - Bilgi
tags: 
  - makine öğrenmesi
  - overfitting
  - düzenlileştirme
---

Bir makine öğrenmesi modeli eğitim örneklerini kusursuz tahmin ederken yeni veriler karşısında afallıyorsa karşımızda çalışkan değil, ezberci bir öğrenci vardır. **Aşırı öğrenme (overfitting)** adı verilen bu durum, modelin verideki gerçek örüntülerle birlikte gürültüyü ve tesadüfi ayrıntıları da öğrenmesiyle ortaya çıkar. Neyse ki Dropout, L1/L2 düzenlileştirme ve erken durdurma gibi yöntemlerle modele biraz disiplin kazandırabiliriz.
``
## Overfitting neden oluşur?

Bir modelin amacı yalnızca eğitim hatasını küçültmek değil, daha önce görmediği örneklerde de başarılı olmaktır. Model gereğinden fazla karmaşıksa sınırlı sayıdaki eğitim verisine özel kurallar geliştirebilir. Örneğin çok derin bir karar ağacı, her yaprağa tek örnek düşene kadar dallanarak veriyi neredeyse ezberleyebilir.

Genelleme performansını anlamak için veri genellikle eğitim, doğrulama ve test kümelerine ayrılır. Eğitim kaybı azalırken doğrulama kaybının yükselmeye başlaması önemli bir alarmdır.

| Durum | Eğitim hatası | Doğrulama hatası | Yorum |
|---|---:|---:|---|
| Underfitting | Yüksek | Yüksek | Model fazla basit |
| İdeal öğrenme | Düşük | Düşük | Örüntüler genelleniyor |
| Overfitting | Çok düşük | Yüksek | Model ayrıntıları ezberliyor |

Bu problem, **bias-variance dengesi** ile de açıklanır. Basit modeller yüksek bias nedeniyle gerçek ilişkiyi kaçırırken aşırı karmaşık modeller yüksek variance nedeniyle veri değişikliklerine fazla duyarlı olur. Hedef, iki uç arasında uygun dengeyi bulmaktır.

## L1 ve L2 düzenlileştirme

Düzenlileştirme, standart kayıp fonksiyonuna büyük ağırlıkları cezalandıran bir terim ekler:

$$J = L(y, \hat{y}) + \lambda R(w)$$

Burada $L$ tahmin hatası, $R(w)$ ceza fonksiyonu ve $\lambda$ cezanın gücüdür. Lambda büyüdükçe model daha sade davranır; ancak aşırı büyük bir değer underfitting yaratabilir.

| Yöntem | Ceza | Temel etkisi |
|---|---|---|
| L1 (Lasso) | $\lambda \sum_i |w_i|$ | Bazı ağırlıkları sıfırlar, özellik seçimi sağlar |
| L2 (Ridge) | $\lambda \sum_i w_i^2$ | Ağırlıkları küçültür, daha dengeli dağıtır |

L1, gereksiz özellikleri oyundan çıkaran sert bir teknik direktör gibidir. L2 ise oyuncuları kovmak yerine hepsinin egosunu küçültür. Birlikte kullanıldıklarında **Elastic Net** yaklaşımı ortaya çıkar.

## Dropout: Nöronlara zorunlu izin

Dropout, sinir ağlarında eğitim sırasında bazı nöronları rastgele geçici olarak devre dışı bırakır. Böylece ağ belirli nöronlara bağımlı olamaz ve farklı temsil yolları öğrenir. Bir nöronun tutulma olasılığı $p$ ise kabaca şu maske uygulanır:

$$h' = m \odot h, \quad m_i \sim Bernoulli(p)$$

TensorFlow/Keras ile örnek bir ağ şöyle kurulabilir:

```python
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Dropout

model = Sequential([
    Dense(128, activation="relu", input_shape=(50,)),
    Dropout(0.4),  # Eğitimde nöronların %40'ını geçici kapatır
    Dense(64, activation="relu"),
    Dropout(0.2),
    Dense(1, activation="sigmoid")
])
```

Dropout yalnızca eğitim sırasında etkindir. Tahmin aşamasında tüm nöronlar kullanılır; kütüphane gerekli ölçeklemeyi otomatik olarak yönetir.

## Early stopping: Zamanında bırakmak

Erken durdurma, doğrulama kaybını izler ve iyileşme sona erdiğinde eğitimi durdurur. Böylece modelin eğitim verisini ezberlemeye başladığı bölgeye fazla ilerlenmez.

```python
from tensorflow.keras.callbacks import EarlyStopping

stopper = EarlyStopping(
    monitor="val_loss",
    patience=5,
    restore_best_weights=True
)

model.fit(
    X_train, y_train,
    validation_split=0.2,
    epochs=100,
    callbacks=[stopper]
)
```

`patience=5`, doğrulama kaybı beş dönem boyunca iyileşmezse eğitimi bitirir. `restore_best_weights=True` ise son ağırlıklar yerine en başarılı dönemin ağırlıklarını geri yükler.

## Hangisini kullanmalı?

Bu yöntemler rakip değil, takım arkadaşıdır. L1/L2 model ağırlıklarını sınırlar, Dropout nöron bağımlılığını azaltır, early stopping ise eğitim süresini kontrol eder. En iyi değerler doğrulama kümesi ve hiperparametre aramasıyla belirlenmelidir. Test kümesine sürekli bakmak ise test verisini de dolaylı biçimde ezberlemek demektir. Kısacası iyi model, sınav sorularını hatırlayan değil; konuyu öğrenip yeni soruları çözebilendir.
