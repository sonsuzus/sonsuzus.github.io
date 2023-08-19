---
title: Python Yüz Algılama ve Tanıma Programı
author: sonsuz
date: 2023-08-19 14:46:01 +0300
categories: [Program,Python]
tags: [python,programlama,yüz algılama,yüz tanıma,kamera,fotoğraf,video]
---


## Yüz algılama ve tanıma programı

Bir fotoğraf, video veya bilgisayara bağlı bir kameradan alınan görüntü üzerindeki yüzleri algılayan ve bilgisayarımızda kayıtlı kişilere ait fotoğrafları kullanarak, algıladığı yüzlerin bu veritabanında olanları tanıyarak, altına kişi adlarını yazan bir program oluşturmaya çalışalım.

Programın tam verimli çalışabilmesi için, veritabanında yer alan fotoğrafların elden geldiğince kaliteli ve çok miktarda olması tercih edilmelidir. OpenCV dışında daha kesin ve güvenilir sonuçlar alan kütüphanelerde kullanılabilir.

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

Projede kullanılacak fotoğraflara ait dizin yapısı aşağıda gösterildiği şekilde olacaktır:

* Proje dizini: C:\Python396\envs\env01\projects
* Fotoğraf ana dizini: C:\Python396\envs\env01\projects\faces
* Kişi fotoğraf dizini: C:\Python396\envs\env01\projects\faces\kisi01

![](python/python_ornek11.png)

Projede üç kişiye ait fotoğraflar kendilerine ayrılmış dizinlere kaydedilmiştir.

Programa komut satırından aktarılan argüman yoluyla fotoğraf, video veya kameradan aldığı görüntülerden birine işlem yapması sağlanır:

* program-adı foto: Fotoğrafa işlem yapar.
* program-adı video: Videoya işlem yapar.
* program-adı kamera: Kamera görüntüsüne işlem yapar.
* program-adı: Videoya işlem yapar.

Örnek

```py
import cv2, sys, os
import numpy as np
from math import ceil

# Haar cascade classifier yükleme
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

frame = 0;

if(len(sys.argv)>1):
   if(sys.argv[1]=='foto'): # Video
      frame = cv2.imread('foto.jpg') # Fotoğraf dosyası okuma
   elif(sys.argv[1]=='video'): # Video
      video_capture = cv2.VideoCapture('video.mp4') # Video dosyası okuma
   elif(sys.argv[1]=='kamera'): # Kamera
      video_capture = cv2.VideoCapture(0)  # Birden fazla kamera bulunan bilgisayarlarda 0 değeri değişebilir.
   else:
      video_capture = cv2.VideoCapture('video.mp4')         
else:
   video_capture = cv2.VideoCapture('video.mp4')        
   
recognizer = cv2.face.LBPHFaceRecognizer_create() 
min_confidence = 10

# Yüz verilerini okuma
def get_face_data():
    images = [] # Fotoğraf listesi oluşturma
    image_label = [] # Fotoğraf isim listesi oluşturma
    names = [] # Dizin adı listesi oluşturma
    cd = os.getcwd() # Programın çalıştığı dizini elde etme
    dir_faces = os.path.join(cd, 'faces') # Çalışma dizinine faces dizinini ekleme
    folders = os.listdir(dir_faces) # faces dizini içindeki dizinlerin listesini alma
	
    # Faces dizini altındaki her bir dizin için işlem yapma
    for id1 in range(len(folders)):
        names.append(folders[id1]) # Faces dizini altındaki dizin adını names listesine ekleme 
        dir_per = os.path.join(dir_faces, folders[id1]) # Her bir kişiye ait dizin yol tanımlaması 
        folder_imgs = os.listdir(dir_per) # Her bir kişiye ait dizin içindeki fotoğraf dosyalarını alma
        # Her bir kişiye ait dizin içindeki her bir fotoğrafa işlem yapma
        for id2 in folder_imgs:
            im = cv2.imread(os.path.join(dir_per, id2), 0) # Her bir kişiye ait dizinde bulunan fotğraf dosyası yol tanımlaması 
            faces = face_cascade.detectMultiScale(im, 1.1, 5, minSize=(50,50)) # Fotoğraf dosyaları içindeki yüzleri alma
            # Her bir yüze işlem yapma			
            for (x,y,w,h) in faces:
                img_array = np.array(im[x:x+w,y:y+h],'uint8')
                images.append(img_array) # Yüz bilgilerini images listesine ekleme
                image_label.append(id1) # Kişi adını image_label listesine ekleme

    cv2.destroyAllWindows()
	
    return images, image_label, names

# Training işlemi
image_data, labels, names = get_face_data()
recognizer.train(image_data, np.array(labels))

while True:    
    if(sys.argv[1]!='foto'): # Video
       ret,frame = video_capture.read() # Video frame okuma
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Frame renklerini gri tonlara ayarlama
    faces = face_cascade.detectMultiScale(gray, 1.1, 5, minSize=(100,100)) # Frame'deki yüzlerin yerlerini tespit etme
    for (x,y,w,h) in faces: # Yüzleri işaretleme
        cv2.rectangle(frame, (x,y), (x+w,y+h), (250, 150, 250) ,2)
        test = gray[x:x+w,y:y+h]
        test_img = np.array(test,'uint8')
        if(test_img.any()): # Frame içinde yüz varsa tahmin yapma
            index, confidence = recognizer.predict(test_img)
        if(confidence>=min_confidence): # Tahmin değerini ekrana yazma
           cv2.putText(frame,names[index],(x,y+h+20),cv2.FONT_HERSHEY_DUPLEX,.5,(0,255,0)) # Kişi adını yazma
           cv2.putText(frame,str(ceil(confidence))+"%",(x,y-20),cv2.FONT_HERSHEY_DUPLEX,.5,(0,255,0)) # Güvenilirlik derecesini yazma

    if(sys.argv[1]=='foto'): 
       cv2.imshow('Foto', frame) # Yüzlerin işaretlendiği fotoğrafı ekranda gösterme
       cv2.waitKey(0) # Herhangi bir tuşa basıldığında program sona erer.
       break
		   
    cv2.imshow('Video', frame) # Frame'i ekranda gösterme
    k = cv2.waitKey(1) & 0xFF
    if k == 27: # Esc tuşu ile çıkış
       break

if(sys.argv[1]!='foto'):
   video_capture.release()
cv2.destroyAllWindows()


```

Programı çalıştırdığımızda, Haar cascade classifier'lar yüklenir. Fotoğraf ile işlem yaparsa tek bir fotoğrafı okur. Video veya kamera ile işlem yaparsa, görüntü yakalama işlemini başlatır. get\_face\_data() fonksiyonu ile veritabanından kişilere ait fotoğraf bilgilerini alır. recognizer.train() fonksiyonu ile verilere eğitme işlemi uygular. Video veya kamera işlemi ise, tek bir frame okunur. Elimizdeki frame değişkeninin renkleri gri tonlara çevrilir. Frame'de yer alan yüzler tespit edilir ve çerçeveye alınarak işaretlenir. Eğer veritabanında yer alıyorsa kişinin adı çerçevenin altına ve güvenilirlik derecesi ise çerçevenin üstüne yazılır. Fotoğraf ile işlem yaparsa, fotoğrafın işlem görmüş hali ekranda gösterilir ve herhangi bir tuşa basıldığında program sona erer. Video veya kamera ile işlem yapılıyorsa, Esc tuşuna basıldığında program sona erer.
