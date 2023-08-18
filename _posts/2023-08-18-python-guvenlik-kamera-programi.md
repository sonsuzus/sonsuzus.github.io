---
title: Python Bilgisayara Bağlı Kamerayı Güvenlik Kamerası Yapma Programı
author: sonsuz
date: 2023-08-18 22:14:05 +0300
categories: [Program,Python]
tags: [python,programlama,kamera,görüntü,işlem]
---



## Bilgisayara bağlı bir kamerayı güvenlik kamerası olarak kullanan program

Bilgisayara bağlı bir kamerayı güvenlik kamerası olarak kullanan bir program oluşturmaya çalışacağız.

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
import cv2 # opencv-python kütüphanesi
import winsound

cam = cv2.VideoCapture(0) # Birden fazla kamera bulunan bilgisayarlarda 0 değeri değişebilir.

while cam.isOpened():
    ret, frame1 = cam.read() # İlk görüntüyü alma
    ret, frame2 = cam.read() # İkinci görüntüyü alma
    diff = cv2.absdiff(frame1, frame2) # İki görüntü arasındaki farkı alma
    gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY) # İki görüntü arasındaki farkı gri renklere çevirme 
    blur = cv2.GaussianBlur(gray, (5, 5), 0) # İki görüntü arasındaki farkı bulanıklaştırma
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY) # Gürültüden kurtulma işlemi
    dilated = cv2.dilate(thresh, None, iterations=3) # Genişletme işlemi
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # Hatları belirleme
    # cv2.drawContours(frame1, contours, -1, (250, 150, 250), 2)
    # Farklılık görünen alanları çerçeve içine alma 
    for c in contours:
        if cv2.contourArea(c) < 5000:
            continue
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (250, 150, 250), 2)
        winsound.PlaySound('alert.wav', winsound.SND_ASYNC)
		
    if cv2.waitKey(10) == ord('q'): # q tuşuna basınca program sona erer.
        break
    # cv2.imshow('Sistem kamerası', diff) # gray, blur, thresh
    cv2.imshow('Sistem kamera', frame1)	


```

Programı çalıştırdığımızda, bir while döngüsü içinde sürekli olarak üst üste iki kamera görüntüsü alınır. İki görüntünün farkları değerlendirilerek, belirli bir seviyenin üzerinde olan farklılıklar için, farklı alanların etrafına renkli bir çerçeve çizilir ve alarm sesi çalar. Kullanıcı q tuşuna bastığında, program sona erer.
