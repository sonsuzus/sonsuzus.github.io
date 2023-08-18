---
title: Python Konuşma Tanıma Programı
author: sonsuz
date: 2023-08-18 22:01:33 +0300
categories: [Program,Python]
tags: [python,programlama,konuşma,tanıma,ses,pyaudio]
---



## Konuşma tanıma (Speech recognition) programı

Konuşma tanıma (Speech recognition) veya konuşmadan metne (speech-to-text), bir cihazın veya programın yüksek sesle konuşulan kelimeleri tanımlama ve bunları okunabilir metne dönüştürmesi işlemidir.

Konuşma tanıma ve ses tanıma (voice recognition) terimleri bazen birbirinin yerine kullanılmasına rağmen, aslında iki terim birbirinden farklıdır. Konuşma tanıma, konuşulan dildeki kelimeleri tanımlamak için kullanılır. Ses tanıma ise, belirli bir kişinin sesini veya konuşmacıyı tanımlamak için kullanılan biyometrik bir teknolojidir.

Program için aşağıda bilgileri ve sanal ortamda kurulum komutları verilen kütüphaneleri kullanacağız:

- SpeechRecognition kütüphanesi

Çeşitli motorlar ve API'ler için çevrimiçi ve çevrimdışı desteği sağlayan konuşma tanıma kütüphanesidir.

```


pip install SpeechRecognition


```

- PyAudio kütüphanesi

Tüm işletim sistemlerinde çalışan ses giriş/çıkış akışı kütüphanesidir. Ses ile ilgili işlemlerde kullanılır.

Bu kütüphanenin doğrudan "pip install pyaudio" komutu ile kurulmasında herhangi bir sorun yaşandığında kurulumu gerçekleştirmek için, Christoph Gohlke tarafından Python paketleri için resmi olmayan Windows işletim sistemi dosyalarını içeren web sitesine ait [buradaki](https://www.lfd.uci.edu/~gohlke/pythonlibs/) bağlantıdan bilgisayarımızın işletim sistemine göre indirdiğimiz aşağıdaki dosyalardan birisini, sanal ortamın altındaki Scripts dizini altına kopyalayarak kullanıyoruz:

PyAudio-0.2.11-cp39-cp39-win\_amd64.whl

PyAudio-0.2.11-cp39-cp39-win32.whl

```


pip install PyAudio-0.2.11-cp39-cp39-win_amd64.whl


```

Örnek

```py
import speech_recognition as sr

r = sr.Recognizer() # speech_recognition için recognizer nesnesi tanımlama

# Konuşmayı metine çeviren fonksiyon
def SpeechToText(stt_mic):        
    print("Konuşun:")
    # Recognizer'ın çevredeki gürültü seviyesine göre enerji eşiğini ayarlamasına izin vermek için bir saniye bekleme 
    r.adjust_for_ambient_noise(mic, duration=0.2)			  
    audio = r.listen(stt_mic) # Kullanıcı girişini alma

    text = r.recognize_google(audio, language='tr-TR') # Google ile sesi metine çevirme
    text = text.lower() # Metni küçük harfe çevirme
    print(f"Alınan metin: {text}") # Metni ekrana yazma	

try:
   while True:
         with sr.Microphone() as mic: #  Giriş kaynağı olarak nikrofon kullanma
              SpeechToText(mic)                

except KeyboardInterrupt: # Ctrl-C ile çıkış
       pass		


```

Programı çalıştırdığımızda, mikrofondan gelen insan sesini metne çevirir ve metin değerini ekrana yazar. Aynı işlem sürekli tekrar eder. Ctrl-C tuş bileşimine bastığımızda, program sona erer.
