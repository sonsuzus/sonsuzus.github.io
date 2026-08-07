---
layout: post
title: "Sinir Ağlarının Karar Motoru: Sigmoid, ReLU ve Tanh"
math: true
categories: 
  - Bilgi
tags: 
  - yapay zeka
  - derin öğrenme
  - aktivasyon fonksiyonları
---

Bir sinir ağını yalnızca matris çarpımları yapan dev bir hesap makinesi olmaktan çıkarıp görüntü tanıyan, metin üreten ve karmaşık kararlar veren bir modele dönüştüren temel bileşen aktivasyon fonksiyonudur. Sigmoid, ReLU ve Tanh gibi fonksiyonlar, nöronların hangi bilgiyi ne ölçüde sonraki katmana aktaracağını belirler. Kısacası ağın matematiksel reflekslerini oluştururlar.

``

## Aktivasyon fonksiyonu neden gereklidir?

Bir yapay nöron önce girdilerin ağırlıklı toplamını hesaplar:

$$z = w_1x_1 + w_2x_2 + \cdots + w_nx_n + b$$

Ardından bu değer bir aktivasyon fonksiyonundan geçirilir:

$$a = f(z)$$

Eğer bütün katmanlarda aktivasyon kullanılmazsa ağ yalnızca doğrusal dönüşümler gerçekleştirir. Üst üste kaç doğrusal katman eklenirse eklensin sonuç yine tek bir doğrusal dönüşüme indirgenebilir:

$$W_3(W_2(W_1x)) = W'x$$

Bu durumda model, doğrusal bir çizgiyle ayrılamayan XOR gibi problemleri öğrenemez. Aktivasyon fonksiyonları sisteme **doğrusal olmama** özelliği kazandırır; böylece eğriler, sınırlar ve karmaşık örüntüler modellenebilir.

## Sigmoid: Olasılık yorumunun klasiği

Sigmoid fonksiyonu herhangi bir gerçek sayıyı 0 ile 1 arasına sıkıştırır:

$$\sigma(x) = \frac{1}{1 + e^{-x}}$$

Çıktısının olasılık gibi yorumlanabilmesi, onu özellikle ikili sınıflandırma modellerinin çıkış katmanında kullanışlı yapar. Örneğin çıktı $0.87$ ise model bunu yüzde 87 pozitif sınıf olasılığı olarak yorumlayabilir.

Ancak büyük pozitif veya negatif girdilerde türevi sıfıra yaklaşır. Geri yayılım sırasında gradyanlar katmanlar boyunca küçüldüğünde **kaybolan gradyan problemi** ortaya çıkar. Derin ağlarda öğrenme adeta fısıltıya dönüşür.

## Tanh: Sıfır merkezli sigmoid

Tanh, değerleri -1 ile 1 arasına taşır:

$$\tanh(x) = \frac{e^x-e^{-x}}{e^x+e^{-x}}$$

Sıfır merkezli olması, pozitif ve negatif sinyallerin daha dengeli aktarılmasını sağlar. Bu nedenle klasik tekrarlayan sinir ağlarında sıkça tercih edilmiştir. Yine de uç değerlerde doygunluğa ulaşır ve sigmoid gibi gradyan kaybı yaşayabilir.

## ReLU: Basit ama güçlü

ReLU, modern derin öğrenmenin en yaygın gizli katman aktivasyonlarından biridir:

$$f(x) = \max(0, x)$$

Pozitif değerleri değiştirmeden geçirir, negatif değerleri ise sıfırlar. Hesaplaması hızlıdır ve pozitif bölgede sabit gradyana sahip olduğu için kaybolan gradyan sorununu azaltır. Dezavantajı, sürekli negatif girdi alan nöronların sıfır çıktı üretip öğrenmeyi bırakabilmesidir. Buna **ölen ReLU** denir.

| Fonksiyon | Çıktı aralığı | Güçlü yönü | Temel sorun | Tipik kullanım |
|---|---:|---|---|---|
| Sigmoid | $(0,1)$ | Olasılık yorumu | Kaybolan gradyan | İkili sınıflandırma çıkışı |
| Tanh | $(-1,1)$ | Sıfır merkezli çıktı | Doygunluk | RNN ve ara katmanlar |
| ReLU | $[0,\infty)$ | Hızlı ve seyrek aktivasyon | Ölen nöronlar | Derin gizli katmanlar |

## Python ile fonksiyonları görmek

Aşağıdaki kod üç fonksiyonun aynı girdi üzerindeki davranışını çizer. Böylece Sigmoid ve Tanh’ın uçlarda yataylaştığı, ReLU’nun ise negatif bölgede tamamen kapandığı görülebilir.

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-6, 6, 400)
sigmoid = 1 / (1 + np.exp(-x))
tanh = np.tanh(x)
relu = np.maximum(0, x)

plt.plot(x, sigmoid, label="Sigmoid")
plt.plot(x, tanh, label="Tanh")
plt.plot(x, relu, label="ReLU")
plt.axhline(0, color="black", linewidth=0.5)
plt.legend()
plt.grid(True)
plt.show()
```

## Hangisini seçmeliyiz?

Gizli katmanlar için iyi bir başlangıç tercihi genellikle ReLU’dur. Ölen nöron problemi yaşanıyorsa negatif bölgede küçük eğime sahip Leaky ReLU denenebilir. İkili sınıflandırmanın çıkışında Sigmoid, çok sınıflı problemlerde ise çoğunlukla Softmax kullanılır. Tanh, çıktının negatif ve pozitif olmasının anlam taşıdığı yapılarda değerlidir.

Aktivasyon seçimi küçük bir ayar gibi görünse de ağın gradyan akışını, eğitim hızını ve öğrenebileceği karar sınırlarını doğrudan etkiler. Başka bir ifadeyle ağırlıklar modelin bildiklerini saklarken aktivasyon fonksiyonları bu bilgilerin nasıl konuşacağını belirler.
