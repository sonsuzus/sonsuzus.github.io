---
layout: post
title: "CNN ile Görsel Algı: Piksellerden Kenar, Doku ve Şekillere"
math: true
categories: 
  - Bilgi
tags: 
  - CNN
  - Görüntü İşleme
  - Derin Öğrenme
---

Bir bilgisayar için fotoğraf, sevimli bir kedi veya kırmızı bir otomobil değil; yalnızca sayılardan oluşan çok boyutlu bir matristir. Evrişimli Sinir Ağları, yani CNN’ler, bu sayı yığınını anlamlandırarak kenarları, dokuları, şekilleri ve sonunda nesneleri keşfeder. Bunu yaparken görüntünün mekânsal yapısını koruyan evrişim filtrelerinden ve gereksiz ayrıntıları azaltan havuzlama işlemlerinden yararlanır.

``

## Görüntü bilgisayara nasıl görünür?

Gri tonlamalı bir görüntü $H \times W$ boyutlu bir matris, renkli görüntü ise genellikle $H \times W \times 3$ boyutlu bir tensördür. Son boyuttaki üç kanal kırmızı, yeşil ve maviyi temsil eder. Klasik tam bağlı ağlarda her piksel her nörona bağlanır; bu yaklaşım büyük görüntülerde devasa sayıda parametre üretir ve pikseller arasındaki komşuluk ilişkisini göz ardı eder.

CNN ise küçük bir filtreyi görüntü üzerinde gezdirir. Böylece hem daha az parametre kullanır hem de aynı özelliği görüntünün farklı bölgelerinde arayabilir. Bir kedinin kulağı sağda da olsa solda da olsa aynı filtre tarafından yakalanabilir.

## Evrişim: Görüntü üzerinde gezinen büyüteç

Evrişim katmanındaki filtre, örneğin $3 \times 3$ boyutunda öğrenilebilir bir ağırlık matrisidir. Filtre her konumda görüntünün ilgili bölgesiyle eleman bazında çarpılır ve sonuçlar toplanır:

$$
Y(i,j)=\sum_m\sum_n X(i+m,j+n)K(m,n)+b
$$

Burada $X$ giriş görüntüsünü, $K$ filtreyi, $b$ bias değerini ve $Y$ üretilen özellik haritasını gösterir. İlk katmanlar çoğunlukla yatay veya dikey kenarları öğrenir. Daha derin katmanlar bu basit bilgileri birleştirerek köşe, doku, göz, tekerlek veya kanat gibi daha karmaşık örüntüler oluşturur.

Çıktı boyutu yaklaşık olarak şu formülle hesaplanır:

$$
O=\left\lfloor\frac{N+2P-K}{S}\right\rfloor+1
$$

$N$ giriş boyutu, $K$ filtre boyutu, $P$ padding ve $S$ stride değeridir. Padding görüntünün kenarlarına boşluk eklerken stride filtrenin kaç piksel atlayacağını belirler.

| Kavram | Görevi | Etkisi |
|---|---|---|
| Filtre | Yerel özellikleri arar | Kenar ve doku haritaları üretir |
| Stride | Filtrenin adımını belirler | Boyutu ve hesaplama maliyetini değiştirir |
| Padding | Kenarlara değer ekler | Mekânsal boyutu koruyabilir |
| Aktivasyon | Doğrusal olmayanlık ekler | Karmaşık örüntülerin öğrenilmesini sağlar |

## Havuzlama: Önemli bilgiyi sıkıştırmak

Pooling katmanı öğrenilebilir filtre taşımaz. Belirli bir pencere içindeki değerleri özetler. Max pooling en büyük değeri seçerken average pooling ortalamayı alır. Örneğin $2 \times 2$ max pooling, dört değerden en güçlü aktivasyonu saklar. Böylece özellik haritası küçülür, hesaplama hızlanır ve küçük konum değişikliklerine karşı dayanıklılık artar.

| Yöntem | Seçim biçimi | Kullanım karakteri |
|---|---|---|
| Max Pooling | En büyük değer | Belirgin özellikleri korur |
| Average Pooling | Değerlerin ortalaması | Daha yumuşak özet üretir |
| Global Average Pooling | Kanalın tamamının ortalaması | Sınıflandırma öncesi parametreleri azaltır |

## PyTorch ile küçük bir CNN

Aşağıdaki model, renkli $32 \times 32$ görüntüleri on sınıftan birine ayırabilecek temel bir mimari kurar:

```python
import torch.nn as nn

class MiniCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 16, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(16, 32, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2)
        )
        self.classifier = nn.Linear(32 * 8 * 8, 10)

    def forward(self, x):
        x = self.features(x)
        x = x.flatten(1)
        return self.classifier(x)
```

İlk evrişim katmanı RGB görüntüden 16 özellik haritası çıkarır. ReLU negatif değerleri sıfırlayarak modele doğrusal olmayanlık kazandırır. İki havuzlama işlemi görüntüyü $32 \times 32$ boyutundan $8 \times 8$ boyutuna indirir. Son katman ise çıkarılan özellikleri sınıf puanlarına dönüştürür.

CNN’lerin asıl gücü hiyerarşik öğrenmedir: erken katmanlar kenarları, orta katmanlar dokuları ve parçaları, derin katmanlar ise bütün nesneleri temsil eder. Bu nedenle CNN’ler yüz tanıma, tıbbi görüntü analizi, otonom sürüş ve kalite kontrol gibi alanlarda dijital dünyanın keskin gözleri hâline gelmiştir.
