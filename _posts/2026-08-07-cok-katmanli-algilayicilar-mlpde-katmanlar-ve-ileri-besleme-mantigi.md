---
layout: post
title: "Çok Katmanlı Algılayıcılar: MLP’de Katmanlar ve İleri Besleme Mantığı"
math: true
categories: 
  - Bilgi
tags: 
  - yapay sinir ağları
  - MLP
  - derin öğrenme
---

Bir yapay sinir ağının fotoğraftaki rakamı tanıması, müşterinin alışveriş davranışını tahmin etmesi veya bir evin fiyatını hesaplaması ilk bakışta sihir gibi görünebilir. Oysa Çok Katmanlı Algılayıcıların, yani MLP’lerin arkasında düzenli bir matematiksel veri akışı vardır: Bilgiler girişten alınır, katmanlar boyunca dönüştürülür ve anlamlı bir çıktıya çevrilir.

``

## MLP nedir?

**Multi-Layer Perceptron (MLP)**, birbirine bağlı yapay nöronlardan oluşan ileri beslemeli bir sinir ağıdır. “İleri beslemeli” denmesinin nedeni, verinin girişten çıkışa doğru tek yönde ilerlemesidir. Döngü veya geçmiş durumu saklayan bir bağlantı bulunmaz.

Bir MLP genellikle üç bölümden oluşur:

| Katman | Görevi | Örnek |
|---|---|---|
| Girdi katmanı | Ham özellikleri kabul eder | Yaş, gelir, ürün fiyatı |
| Gizli katmanlar | Özellikleri dönüştürür ve örüntüleri öğrenir | Fiyat-gelir ilişkisini keşfetmek |
| Çıktı katmanı | Tahmin veya sınıf üretir | “Satın alır” olasılığı |

Girdi katmanında hesaplama genellikle yapılmaz; değerler yalnızca ilk gizli katmana aktarılır. Asıl öğrenme, ağırlık ve sapma değerlerini kullanan gizli katmanlarda gerçekleşir.

## Bir nöron nasıl çalışır?

Bir nöron, kendisine ulaşan değerleri ağırlıklandırır ve toplar. Katman $l$ için bu işlem şöyle gösterilebilir:

$$z^{(l)} = W^{(l)}a^{(l-1)} + b^{(l)}$$

Burada $W$ ağırlık matrisini, $a$ önceki katmanın çıktısını, $b$ ise sapma değerini temsil eder. Elde edilen $z$ değeri doğrudan sonraki katmana gönderilmez; önce bir aktivasyon fonksiyonundan geçirilir:

$$a^{(l)} = f(z^{(l)})$$

Bu küçük görünen $f$ fonksiyonu son derece önemlidir. Aktivasyon kullanılmazsa, art arda eklenen katmanlar matematiksel olarak tek bir doğrusal dönüşüme indirgenir. Başka bir ifadeyle ağ çok katlı görünür, ancak tek katlı bir hesap makinesi gibi davranır.

## Doğrusal olmayanlığın süper gücü

Aktivasyon fonksiyonları MLP’nin eğri karar sınırları ve karmaşık ilişkiler öğrenmesini sağlar.

| Aktivasyon | Özellik | Yaygın kullanım |
|---|---|---|
| ReLU | $f(x)=max(0,x)$, hızlı ve basit | Gizli katmanlar |
| Sigmoid | Değeri 0 ile 1 arasına sıkıştırır | İkili sınıflandırma çıktısı |
| Tanh | Değeri -1 ile 1 arasına taşır | Bazı gizli katmanlar |
| Softmax | Sınıflar için olasılık dağılımı üretir | Çok sınıflı çıktı |

Örneğin XOR problemi tek bir doğrusal çizgiyle ayrılamaz. Gizli katmana ve doğrusal olmayan aktivasyona sahip bir MLP ise girdileri yeni bir temsil uzayına taşıyarak bu problemi çözebilir. Gizli katmanların “temsil öğrenmesi” denilen yeteneği tam olarak budur.

## İleri besleme adım adım

İleri besleme sırasında eğitim yapılmaz; mevcut ağırlıklarla tahmin hesaplanır. Veri her katmanda şu yolculuğu gerçekleştirir:

1. Özellik vektörü giriş katmanına verilir.
2. Girdiler ağırlıklarla çarpılıp sapmalarla toplanır.
3. Sonuç aktivasyon fonksiyonundan geçirilir.
4. Üretilen değerler sonraki katmanın girdisi olur.
5. Çıktı katmanı nihai tahmini üretir.

Aşağıdaki NumPy örneği, tek gizli katmanlı bir ağın ileri beslemesini gerçekleştirir:

```python
import numpy as np

def relu(x):
    return np.maximum(0, x)

x = np.array([0.8, 0.2])

W1 = np.array([[0.5, -0.3],
               [0.7,  0.4],
               [-0.2, 0.9]])
b1 = np.array([0.1, 0.0, -0.1])

W2 = np.array([[0.6, -0.5, 0.8]])
b2 = np.array([0.2])

hidden = relu(W1 @ x + b1)
output = W2 @ hidden + b2

print(output)
```

Burada `W1 @ x` girişleri gizli nöronlarla birleştirir, `relu` doğrusal olmayan dönüşümü uygular ve `W2 @ hidden` gizli temsilden sonucu hesaplar. Gerçek bir eğitim sürecinde çıktı ile hedef arasındaki hata ölçülür; geri yayılım da ağırlıkları günceller.

MLP’ler tablo verileri, sınıflandırma ve regresyon problemleri için güçlü bir başlangıç noktasıdır. Ancak katman veya nöron sayısını rastgele artırmak başarı garantisi değildir. Uygun veri ölçekleme, aktivasyon seçimi ve aşırı öğrenmeye karşı düzenlileştirme gerekir. Kısacası MLP, bilgiyi katman katman işleyen matematiksel bir montaj hattıdır; ileri besleme ise bu hattın girişten tahmine uzanan tek yönlü üretim turudur.
