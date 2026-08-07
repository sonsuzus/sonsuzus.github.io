---
layout: post
title: "Kütüphanesiz Yapay Sinir Ağıyla El Yazısı Rakamları Tanıma"
math: true
categories: 
  - Proje
tags: 
  - yapay sinir ağı
  - Python
  - MNIST
---

Bir yapay sinir ağının gerçekten nasıl öğrendiğini anlamanın en iyi yolu, hazır makine öğrenmesi kütüphanelerini bir kenara bırakıp bütün parçaları kendimiz yazmaktır. Bu projede yalnızca Python dilinin temel özelliklerini kullanarak MNIST benzeri el yazısı rakamlarını tanıyan, girişten çıkışa ve hatadan geriye doğru öğrenebilen küçük bir sinir ağı geliştireceğiz.

``

## Problemi sayılara dönüştürmek

28×28 piksellik gri tonlamalı bir rakam resmi, ağ açısından resim değil, 784 sayıdan oluşan bir vektördür. Her pikseli 255'e bölerek değerleri $[0,1]$ aralığına taşırız:

$$x_i = \frac{piksel_i}{255}$$

Çıkış katmanında ise 10 nöron bulunur. Örneğin doğru cevap 3 ise hedef vektörü $[0,0,0,1,0,0,0,0,0,0]$ olur. Buna **one-hot kodlama** denir.

| Katman | Nöron sayısı | Görevi |
|---|---:|---|
| Giriş | 784 | Piksel değerlerini almak |
| Gizli | 64 | Çizgi, kıvrım ve kenar örüntülerini öğrenmek |
| Çıkış | 10 | 0-9 sınıflarını puanlamak |

Bir nöron önce ağırlıklı toplam hesaplar:

$$z_j = \sum_i x_i w_{ij} + b_j$$

Ardından doğrusal olmayan sigmoid fonksiyonu uygulanır:

$$\sigma(z)=\frac{1}{1+e^{-z}}$$

Doğrusal olmayan aktivasyon kullanılmazsa çok sayıda katman, matematiksel olarak tek bir doğrusal dönüşüme dönüşür. Başka bir deyişle ağ büyür, fakat zekâsı pek büyümez.

## Ağı sıfırdan kodlamak

Aşağıdaki Python kodu matris kütüphanesi kullanmaz. Ağırlıkları üretmek için kendi basit sözde rastgele sayı üretecimizi bile yazıyoruz:

```python
seed = 123456

def rnd():
    global seed
    seed = (1103515245 * seed + 12345) % (2 ** 31)
    return seed / (2 ** 31) - 0.5

def sigmoid(x):
    return 1.0 / (1.0 + 2.718281828 ** (-max(-30, min(30, x))))

def matrix(rows, cols):
    return [[rnd() * 0.1 for _ in range(cols)] for _ in range(rows)]

INPUT, HIDDEN, OUTPUT = 784, 64, 10
w1 = matrix(HIDDEN, INPUT)
b1 = [0.0] * HIDDEN
w2 = matrix(OUTPUT, HIDDEN)
b2 = [0.0] * OUTPUT

def forward(x):
    hidden = []
    for j in range(HIDDEN):
        z = b1[j] + sum(w1[j][i] * x[i] for i in range(INPUT))
        hidden.append(sigmoid(z))

    output = []
    for k in range(OUTPUT):
        z = b2[k] + sum(w2[k][j] * hidden[j] for j in range(HIDDEN))
        output.append(sigmoid(z))
    return hidden, output
```

`forward` fonksiyonu tahmin üretir; ancak öğrenme için hatayı ağırlıklara geri dağıtmamız gerekir. Ortalama karesel hata kullanırsak temel hedefimiz şudur:

$$L=\frac{1}{2}\sum_k(y_k-\hat{y}_k)^2$$

```python
def train(x, target, rate=0.1):
    hidden, output = forward(x)

    out_delta = [
        (output[k] - target[k]) * output[k] * (1 - output[k])
        for k in range(OUTPUT)
    ]

    hid_delta = []
    for j in range(HIDDEN):
        error = sum(out_delta[k] * w2[k][j] for k in range(OUTPUT))
        hid_delta.append(error * hidden[j] * (1 - hidden[j]))

    for k in range(OUTPUT):
        for j in range(HIDDEN):
            w2[k][j] -= rate * out_delta[k] * hidden[j]
        b2[k] -= rate * out_delta[k]

    for j in range(HIDDEN):
        for i in range(INPUT):
            w1[j][i] -= rate * hid_delta[j] * x[i]
        b1[j] -= rate * hid_delta[j]
```

## Eğitim ve tahmin

Her eğitim resmi için piksel listesini normalize eder, doğru rakamın hedef değerini 1 yapar ve `train` fonksiyonunu çağırırız. Bu işlemin tüm veri üzerinde bir kez yapılmasına **epoch** denir. Eğitimden sonra tahmin, en yüksek çıkış değerinin indeksidir:

```python
def predict(pixels):
    x = [p / 255.0 for p in pixels]
    _, scores = forward(x)
    return max(range(10), key=lambda i: scores[i])
```

| Yaklaşım | Avantaj | Dezavantaj |
|---|---|---|
| Sıfırdan ağ | Matematiği görünür kılar | Yavaş çalışır |
| Hazır kütüphane | Hızlı ve optimize | Ayrıntıları gizleyebilir |

Bu ağ modern modellerle yarışmayacaktır; fakat ileri yayılım, geri yayılım, gradyan inişi ve sınıflandırmanın nasıl birleştiğini açıkça gösterir. Sonraki adım olarak mini-batch eğitimi, ReLU, softmax ve çapraz entropi eklenebilir. Artık sinir ağı gizemli bir kara kutu değil; bolca döngü, türev ve sabırdan oluşan anlaşılır bir makinedir.
