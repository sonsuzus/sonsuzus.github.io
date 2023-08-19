---
title: Python Fotoğraf Üzerinde Yüz Algılama Programı
author: sonsuz
date: 2023-08-19 14:30:10 +0300
categories: [Program,Python]
tags: [python,programlama,yüz tanıma,yüz algılama,fotoğraf,proje]
---

## Yüz algılama programı (Fotoğraf üzerinde)

Bir fotoğraftaki yüzleri ve gözleri tespit edip işaretleyen bir program oluşturmaya çalışalım.

Program için aşağıda bilgileri ve sanal ortamda kurulum komutları verilen kütüphaneleri kullanacağız:

- Opencv-python kütüphanesi

Görüş algılama için kullanılan bir kütüphanedir.

```


pip install opencv-contrib-python


```

Bu kurulum ana modülü ve katkı sağlayan ekstra modülleri içerir.

- NumPy kütüphanesi

NumPy, Python ile dizi hesaplamada kullanılan temel kütüphanedir.

```


pip install numpy


```

Örnek

```py
# Yüz ve gözleri işaretleme
import cv2, sys

# Haar cascade classifier yükleme
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

img = cv2.imread('foto.jpg') # Fotoğraf dosyasını okuma
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Fotoğrafın renklerini gri tonlara ayarlama

# Fotoğraftaki yüzlerin yerlerini tespit etme
faces = face_cascade.detectMultiScale(gray, 1.3, 5, minSize = (80, 80))

# Yüzleri işaretleme
for (x, y, w, h) in faces:
    img = cv2.rectangle(img, (x,y), (x+w,y+h), (250, 150, 250), 2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    # Her bir yüz içinde gözleri tespit etme
    eyes = eye_cascade.detectMultiScale(roi_gray, minSize=(30, 30))
    # Gözleri işaretleme
    for (x1, y1, w1, h1) in eyes:
        cv2.rectangle(roi_color, (x1,y1), (x1+w1,y1+h1), (150, 250, 150), 2)

cv2.imshow('Foto', img) # Yüz ve gözlerin işaretlendiği fotoğrafı ekranda gösterme
cv2.imwrite("output.jpg", img) # Yüz ve gözlerin işaretlendiği fotoğrafı kaydetme
cv2.waitKey(0) # Herhangi bir tuşa basıldığında program sona erer.
cv2.destroyAllWindows()


```

Programı çalıştırdığımızda, Haar cascade classifier'lar yüklenir. Fotoğraf dosyası okunur ve renkleri gri tonlara çevrilir. Fotoğraftaki yüzler tespit edilir ve işaretlenir. Her bir yüz içindeki gözler tespit edilir ve işaretlenir. Yüz ve gözlerin işaretlendiği fotoğraf ekranda gösterilir ve kaydedilir. Herhangi bir tuşa basıldığında program sona erer.
