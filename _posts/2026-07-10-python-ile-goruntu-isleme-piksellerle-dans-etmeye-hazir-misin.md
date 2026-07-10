---
layout: post
title: "Python ile Görüntü İşleme: Piksellerle Dans Etmeye Hazır mısın?"
math: true
categories: 
  - Program
tags: 
  - python
  - görüntü işleme
  - opencv
  - numpy
---

Görüntü işleme, bilgisayara bir resmi sadece ‘görmeyi’ değil, onu anlamayı da öğretme sanatıdır. Python ise bu iş için adeta İsviçre çakısı gibidir: kolay sözdizimi, güçlü kütüphaneler ve bolca topluluk desteği. Bir fotoğrafı siyah-beyaza çevirmekten yüz tanımaya, belge taramadan otonom araçlara kadar pek çok alanda görüntü işleme kullanılır.

En basit haliyle bir görüntü, sayılardan oluşan bir matristir. Gri tonlamalı bir resimde her piksel 0 ile 255 arasında değer alır. 0 siyahı, 255 beyazı temsil eder. Renkli görüntülerde ise genellikle üç kanal bulunur: kırmızı, yeşil ve mavi. Yani bir piksel aslında şöyle düşünülebilir: $(R, G, B)$.



## Görüntü İşleme İçin Popüler Python Kütüphaneleri

Python ekosisteminde görüntü işleme için birçok araç var. En sık kullanılanları şöyle özetleyebiliriz:
``
| Kütüphane | Kullanım Alanı | Avantajı |
|---|---|---|
| OpenCV | Gerçek zamanlı görüntü işleme | Hızlı ve çok kapsamlı |
| Pillow | Basit resim düzenleme | Öğrenmesi kolay |
| NumPy | Matris işlemleri | Piksel verisiyle çalışmak için ideal |
| scikit-image | Akademik ve bilimsel işlemler | Hazır algoritmalar sunar |
| Matplotlib | Görselleştirme | Sonuçları çizdirmek için pratik |

OpenCV, özellikle kamera görüntüsü alma, filtre uygulama, nesne tespiti ve video işleme gibi konularda oldukça güçlüdür. NumPy ise görüntüyü bir sayı dizisi olarak manipüle etmemizi sağlar.

## İlk Adım: Resmi Okuma ve Gösterme

Aşağıdaki örnekte bir görseli okuyup gri tonlamaya çeviriyoruz:

```python
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('kedi.jpg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plt.subplot(1, 2, 1)
plt.title('Renkli')
plt.imshow(img_rgb)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Gri Tonlama')
plt.imshow(gray, cmap='gray')
plt.axis('off')

plt.show()
```

Burada dikkat edilmesi gereken minik bir tuzak var: OpenCV görselleri varsayılan olarak BGR formatında okur, Matplotlib ise RGB bekler. Yani kırmızı kediniz bir anda mavi uzaylıya dönüşmesin diye `cv2.cvtColor` kullanıyoruz.

## Piksel Mantığı: Matematik Nerede Devreye Girer?

Görüntü işleme aslında bol bol matematik içerir. Örneğin gri tonlama dönüşümü çoğu zaman renk kanallarının ağırlıklı toplamıyla yapılır:

$$
Gray = 0.299R + 0.587G + 0.114B
$$

Bu formül insan gözünün yeşile daha duyarlı olmasını hesaba katar. Yani her kanal eşit önemde değildir. Bir başka temel işlem de eşikleme, yani thresholding işlemidir:

$$
f(x,y) = \begin{cases} 255, & I(x,y) > T \\ 0, & I(x,y) \leq T \end{cases}
$$

Burada $T$ eşik değeridir. Piksel değeri bu eşiğin üzerindeyse beyaz, altındaysa siyah yapılır. Bu yöntem belge tarama, plaka okuma ve basit nesne ayırma işlemlerinde sıkça kullanılır.

## Basit Bir Filtre Uygulayalım

Bulanıklaştırma, gürültü azaltmak için kullanılan temel işlemlerden biridir. OpenCV ile birkaç satır yeterlidir:

```python
import cv2

img = cv2.imread('sokak.jpg')
blur = cv2.GaussianBlur(img, (7, 7), 0)
edge = cv2.Canny(blur, 100, 200)

cv2.imwrite('bulanık.jpg', blur)
cv2.imwrite('kenarlar.jpg', edge)
print('Görüntüler kaydedildi!')
```

`GaussianBlur`, görüntüyü yumuşatır. `Canny` ise kenarları tespit eder. Böylece bir görüntüdeki şekiller, sınırlar ve nesne hatları daha belirgin hale gelir.

## Mini Proje Fikri: Otomatik Belge Tarayıcı

Python ile eğlenceli bir proje yapmak istersen telefonla çekilmiş belge fotoğraflarını taranmış gibi düzelten bir uygulama geliştirebilirsin. Genel adımlar şöyle olur:

1. Görüntüyü oku.
2. Gri tonlamaya çevir.
3. Gürültüyü azalt.
4. Kenarları bul.
5. En büyük dörtgeni tespit et.
6. Perspektif dönüşümü uygula.
7. Sonucu siyah-beyaz belge gibi kaydet.

Bu proje hem OpenCV pratiği kazandırır hem de gerçek hayatta işe yarar. Üstelik arkadaşlarına ‘Ben scanner yaptım’ deme lüksü sağlar.

## Sonuç

Python ile görüntü işleme, ilk bakışta karmaşık görünse de temel mantık oldukça basittir: görüntüleri matris olarak düşün, pikseller üzerinde işlem yap ve sonucu görselleştir. OpenCV, NumPy ve Matplotlib üçlüsüyle kısa sürede etkileyici uygulamalar geliştirebilirsin. Bir sonraki adımda kamera akışından canlı görüntü işleme, yüz algılama veya nesne takibi gibi daha havalı konulara geçebilirsin. Kısacası, pikseller seni bekliyor!
