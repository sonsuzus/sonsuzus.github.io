---
title: Python Kameradan Yüz Tanıma Programı
author: sonsuz
date: 2023-08-19 14:35:12 +0300
categories: [Program,Python]
tags: [python,programlama,kamera,yüz algılama,yüz tanıma,numpy]
---

## Yüz algılama programı (Kamera üzerinde)

Bilgisayara bağlı bir kameradan alınan görüntü üzerindeki yüzleri tespit edip işaretleyen bir program oluşturmaya çalışalım.

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
import cv2

# Haar cascade classifier yükleme
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Birden fazla kamera bulunan bilgisayarlarda 0 değeri değişebilir.
video_capture = cv2.VideoCapture(0)

while True:
	ret,frame = video_capture.read() # Video frame okuma
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Frame renklerini gri tonlara ayarlama
	faces = face_cascade.detectMultiScale(gray, 1.1, 5, minSize=(100,100)) # Frame'deki yüzlerin yerlerini tespit etme
	for (x,y,w,h) in faces: # Yüzleri işaretleme
		cv2.rectangle(frame, (x,y), (x+w,y+h), (250, 150, 250) ,2)
		cv2.putText(frame, "İnsan yüzü", (x,y+h+20), cv2.FONT_HERSHEY_DUPLEX, .5, (250, 150, 250))

	cv2.imshow('Video', frame) # Frame'i ekranda gösterme
	k = cv2.waitKey(1) & 0xFF
	if k == 27: # Esc tuşu ile çıkış
		break

video_capture.release()
cv2.destroyAllWindows()


```

Programı çalıştırdığımızda, Haar cascade classifier'lar yüklenir. Kameradan bir frame okunur ve renkleri gri tonlara çevrilir. Frame'de yer alan yüzler tespit edilir ve çerçeveye alınarak işaretlenir. Esc tuşuna basıldığında program sona erer.
