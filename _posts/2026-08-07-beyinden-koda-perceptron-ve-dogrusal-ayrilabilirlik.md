---
layout: post
title: "Beyinden Koda: Perceptron ve Doğrusal Ayrılabilirlik"
math: true
categories: 
  - Bilgi
tags: 
  - yapay zeka
  - perceptron
  - makine öğrenmesi
---

İnsan beyni, milyarlarca nöronun elektriksel ve kimyasal sinyaller aracılığıyla haberleştiği olağanüstü bir bilgi işleme sistemidir. Yapay zekânın ilk araştırmacıları da “Bir nöronun karar verme mekanizmasını matematikle taklit edebilir miyiz?” sorusundan yola çıktı. Bu merak, modern sinir ağlarının mütevazı fakat tarihî atası olan **algılayıcıyı**, yani perceptronu ortaya çıkardı.
``
## Biyolojik nörondan matematiksel modele

Biyolojik bir nöron; sinyalleri **dendritleriyle** alır, hücre gövdesinde bir araya getirir ve yeterli uyarılma oluşursa akson üzerinden başka hücrelere iletir. Bu süreç birebir kopyalanmasa da temel fikir matematiksel bir modele dönüştürülebilir.

| Biyolojik yapı | Perceptrondaki karşılığı | Görevi |
|---|---|---|
| Dendrit | Girdi $x_i$ | Dışarıdan bilgi alır |
| Sinaps | Ağırlık $w_i$ | Sinyalin önemini belirler |
| Hücre gövdesi | Ağırlıklı toplam | Girdileri birleştirir |
| Ateşleme eşiği | Aktivasyon fonksiyonu | Çıkış kararını üretir |
| Akson | Tahmin $y$ | Sonucu sonraki birime taşır |

1943 yılında Warren McCulloch ve Walter Pitts, nöron davranışını mantıksal işlemlerle açıklayan ilk matematiksel modellerden birini geliştirdi. Frank Rosenblatt ise 1957’de bu fikri öğrenebilen bir yapıya dönüştürerek perceptronu tanıttı.

## Perceptron nasıl karar verir?

Perceptron, her girdiyi ilgili ağırlıkla çarpar, sonuçları toplar ve **bias** adı verilen ek değeri ekler:

$$z = w_1x_1 + w_2x_2 + \cdots + w_nx_n + b$$

Ardından basamak aktivasyon fonksiyonu uygulanır:

$$y = \begin{cases} 1, & z \geq 0 \\ 0, & z < 0 \end{cases}$$

Ağırlıklar girdilerin önemini, bias ise karar sınırının konumunu kontrol eder. Modelin yaptığı şey aslında şudur: “Toplam kanıt yeterince güçlüyse 1, değilse 0 de.” Bir e-postanın spam olup olmadığını düşünürsek “ücretsiz”, “ödül” ve “hemen tıkla” gibi özellikler girdileri temsil edebilir.

## Öğrenme süreci

Perceptron başlangıçta doğru ağırlıkları bilmez. Her örnek için tahmin üretir ve hata yaptığında ağırlıklarını günceller:

$$w_i \leftarrow w_i + \eta(t-y)x_i$$

$$b \leftarrow b + \eta(t-y)$$

Burada $t$ gerçek etiket, $y$ tahmin ve $\eta$ öğrenme oranıdır. Öğrenme oranı, düzeltme adımlarının ne kadar büyük olacağını belirler. Model doğru tahmin yaptığında $t-y=0$ olur ve ağırlıklar değişmez.

Aşağıdaki Python kodu, AND mantık kapısını öğrenen basit bir perceptron kurar:

```python
import numpy as np

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
t = np.array([0, 0, 0, 1])

w = np.zeros(2)
b = 0.0
learning_rate = 0.1

for epoch in range(10):
    for x, target in zip(X, t):
        z = np.dot(w, x) + b
        prediction = 1 if z >= 0 else 0
        error = target - prediction

        w += learning_rate * error * x
        b += learning_rate * error

print("Ağırlıklar:", w)
print("Bias:", b)
```

Kod, her eğitim örneğinde tahmin ile gerçek değer arasındaki farkı hesaplar. Hata varsa ağırlıklar ve bias, doğru sınıfa yaklaşacak yönde değiştirilir.

## Doğrusal ayrılabilirlik meselesi

Perceptronun karar sınırı iki boyutta bir doğru, üç boyutta bir düzlem ve daha yüksek boyutlarda bir **hiperdüzlemdir**:

$$w_1x_1 + w_2x_2 + b = 0$$

Sınıflar tek bir doğruyla birbirinden ayrılabiliyorsa veri **doğrusal ayrılabilir** kabul edilir.

| Mantık kapısı | Doğrusal ayrılabilir mi? | Tek perceptron öğrenebilir mi? |
|---|---:|---:|
| AND | Evet | Evet |
| OR | Evet | Evet |
| XOR | Hayır | Hayır |

XOR probleminde aynı sınıfa ait noktalar çapraz köşelerde bulunur; bu nedenle tek bir doğru yeterli olmaz. Bu sınırlama, yapay zekâ tarihinde büyük bir hayal kırıklığı yaratmış olsa da çözüm yeni bir kapı açtı: Birden fazla perceptronu katmanlar hâlinde birleştirmek. Gizli katmanlar ve doğrusal olmayan aktivasyonlar sayesinde çok katmanlı sinir ağları karmaşık karar sınırları öğrenebilir.

Kısacası perceptron küçük bir matematiksel hücredir; ancak ağırlık, bias, öğrenme ve karar sınırı gibi bugün hâlâ kullandığımız temel kavramları taşır. Modern derin öğrenme sistemleri çok daha gelişmiş olsa da onların aile albümündeki ilk ciddi fotoğraflardan biri kesinlikle perceptrondur.
