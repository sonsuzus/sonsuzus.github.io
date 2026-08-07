---
layout: post
title: "Maliyet Fonksiyonları ve Geri Yayılım: Sinir Ağları Hatalarından Nasıl Öğrenir?"
math: true
categories: 
  - Bilgi
tags: 
  - makine öğrenmesi
  - geri yayılım
  - sinir ağları
---

Bir sinir ağı ilk tahminini yaptığında genellikle pek de parlak değildir. Kedi fotoğrafına tost makinesi diyebilir veya ev fiyatını küçük bir servet kadar yanlış hesaplayabilir. Neyse ki modelin elinde iki güçlü araç vardır: hatanın büyüklüğünü ölçen **maliyet fonksiyonu** ve bu hatadan sorumlu ağırlıkları bulup düzelten **geri yayılım algoritması**.

``

## Önce hatayı ölçelim

Modelin ürettiği tahmin $\hat{y}$ ile gerçek değer $y$ arasındaki fark, öğrenmenin başlangıç noktasıdır. Ancak yalnızca $y-\hat{y}$ kullanmak yeterli değildir; pozitif ve negatif hatalar birbirini götürebilir. Bu nedenle hata, uygun bir maliyet fonksiyonuyla tek bir sayıya dönüştürülür.

Regresyon problemlerinde sık kullanılan **Ortalama Kare Hata** şöyledir:

$$J = \frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y}_i)^2$$

Kare alma işlemi negatif farkları pozitife çevirir ve büyük hataları daha sert cezalandırır. İkili sınıflandırmada ise çoğunlukla **Binary Cross-Entropy** tercih edilir:

$$J = -\frac{1}{n}\sum_{i=1}^{n}[y_i\log(\hat{y}_i)+(1-y_i)\log(1-\hat{y}_i)]$$

| Maliyet fonksiyonu | Kullanım alanı | Temel özelliği |
|---|---|---|
| Ortalama Kare Hata | Regresyon | Büyük hataları karesel cezalandırır |
| Ortalama Mutlak Hata | Regresyon | Aykırı değerlere daha dayanıklıdır |
| Binary Cross-Entropy | İkili sınıflandırma | Yanlış ve emin tahminleri ağır cezalandırır |
| Categorical Cross-Entropy | Çok sınıflı sınıflandırma | Sınıf olasılıklarını karşılaştırır |

## Geri yayılım ne yapar?

İleri yayılım sırasında girişler katmanlardan geçer ve tahmin oluşturulur. Maliyet hesaplandıktan sonra geri yayılım devreye girer. Amaç, her ağırlığın toplam hataya ne kadar katkıda bulunduğunu belirlemektir.

Tek bir nöronu düşünelim:

$$z = wx+b, \qquad a=f(z)$$

Burada $w$ ağırlık, $b$ bias, $f$ aktivasyon fonksiyonu ve $a$ nöron çıktısıdır. Maliyetin ağırlığa göre türevi doğrudan görünmeyebilir. Zincir kuralı bu ilişkiyi küçük parçalara ayırır:

$$\frac{\partial J}{\partial w}=\frac{\partial J}{\partial a}\cdot\frac{\partial a}{\partial z}\cdot\frac{\partial z}{\partial w}$$

Bu ifade adeta bir hata dedektifidir: Önce çıktının maliyete etkisini, sonra aktivasyonun çıktıya etkisini, en sonunda ağırlığın aktivasyon öncesi değere etkisini izler. Derin ağlarda aynı işlem katman katman geriye doğru tekrarlanır.

| Aşama | Yön | Yapılan işlem |
|---|---|---|
| İleri yayılım | Girişten çıkışa | Tahmin üretilir |
| Maliyet hesabı | Çıkışta | Tahmin hatası ölçülür |
| Geri yayılım | Çıkıştan girişe | Gradyanlar hesaplanır |
| Güncelleme | Tüm katmanlarda | Ağırlıklar optimize edilir |

## Ağırlıkların güncellenmesi

Gradyan, maliyetin en hızlı arttığı yönü gösterir. Hatayı azaltmak için bunun tersine gidilir. Gradyan inişi güncellemesi şöyledir:

$$w_{yeni}=w_{eski}-\eta\frac{\partial J}{\partial w}$$

Buradaki $\eta$, öğrenme oranıdır. Çok büyük seçilirse model minimum noktanın üzerinden zıplayabilir; çok küçük seçilirse eğitim kaplumbağa hızına iner.

Aşağıdaki Python kodu tek değişkenli basit bir regresyon modelinde bu süreci gösterir:

```python
x, y = 2.0, 10.0
w = 1.0
learning_rate = 0.05

for epoch in range(20):
    prediction = w * x
    loss = (y - prediction) ** 2

    # Kayıp fonksiyonunun w'ye göre türevi
    gradient = 2 * (prediction - y) * x
    w -= learning_rate * gradient

    print(epoch, round(loss, 4), round(w, 4))
```

Kod önce tahmini ve kare hatayı hesaplar. Ardından zincir kuralından gelen gradyanı kullanarak $w$ değerini günceller. İdeal durumda her turda maliyet azalır ve ağırlık doğru değere yaklaşır.

Özetle maliyet fonksiyonu modele **ne kadar yanlış olduğunu**, geri yayılım ise **bu yanlışta kimin payı bulunduğunu** söyler. Optimizasyon algoritması da gradyanları kullanarak ağırlıkları düzeltir. Sinir ağlarının öğrenmesi sihir değil; türev, zincir kuralı ve bol miktarda kontrollü hata düzeltmesidir.
