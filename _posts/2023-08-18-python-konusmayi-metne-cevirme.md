---
title: Python Konuşma Tanıma ve Metni Konuşmaya Çevirme Programı
author: sonsuz
date: 2023-08-18 22:07:19 +0300
categories: [Program,Python]
tags: [python,programlama,konuşma,ses,pyaudio,metin,çevirici]
---



## Konuşma tanıma (Speech recognition) ve metni konuşmaya çevirme (speech-to-text) programıı

Konuşma tanıma (Speech recognition) veya konuşmadan metne (speech-to-text), bir cihazın veya programın yüksek sesle konuşulan kelimeleri tanımlama ve bunları okunabilir metne dönüştürmesi işlemidir.

Konuşma tanıma ve ses tanıma (voice recognition) terimleri bazen birbirinin yerine kullanılmasına rağmen, aslında iki terim birbirinden farklıdır. Konuşma tanıma, konuşulan dildeki kelimeleri tanımlamak için kullanılır. Ses tanıma ise, belirli bir kişinin sesini veya konuşmacıyı tanımlamak için kullanılan biyometrik bir teknolojidir.

Program için aşağıda bilgileri ve sanal ortamda kurulum komutları verilen kütüphaneleri kullanacağız:

- SpeechRecognition kütüphanesi

Çeşitli motorlar ve API'ler için çevrimiçi ve çevrimdışı desteği sağlayan konuşma tanıma kütüphanesidir.

```


pip install SpeechRecognition


```

- gTTS kütüphanesi

gTTS (Google Text-to-Speech), Google Translate API'si kullanarak metini çeviren bir kütüphanedir.

```


pip install gTTS


```

Bu kütüphane ile birlikte, urllib3, idna, colorama, charset-normalizer, certifi, six, requests ve click kütüphaneleri otomatik olarak yüklenir.

- Playsound kütüphanesi

Ses çalmak için kullanılan bir kütüphanedir.

```


pip install playsound


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
from gtts import gTTS # Google text to speech kütüphanesi
from playsound import playsound
import random
import os

r = sr.Recognizer() # speech_recognition için recognizer nesnesi tanımlama

# Konuşmayı metine çeviren ve ekrana yazan fonksiyon
def SpeechToText(stt_mic):        
    print("Konuşun:")
    # Recognizer'ın çevredeki gürültü seviyesine göre enerji eşiğini ayarlamasına izin vermek için bir saniye bekleme 
    r.adjust_for_ambient_noise(mic, duration=0.2)			  
    audio = r.listen(stt_mic) # Kullanıcı girişini alma

    text = r.recognize_google(audio, language='tr-TR') # Google ile sesi metine çevirme
    text = text.lower() # Metni küçük harfe çevirme
    print(f"Alınan metin: {text}") # Metni ekrana yazma	
    return text
	
# Metni konuşmaya çeviren ve oynatan fonksiyon
def TextToSpeech(tts_text):        
    tts = gTTS(tts_text, lang='tr')
    rand = random.randint(1, 10000)
    file = 'audio-' + str(rand) + '.mp3'
    tts.save(file) # Dosyayı kaydetme
    playsound(file) # Dosyayı oynatma
    os.remove(file) # Dosyayı silme	

try:
   while True:
         with sr.Microphone() as mic: #  Giriş kaynağı olarak nikrofon kullanma
              text = SpeechToText(mic) # Konuşmayı metine çevirme ve ekrana yazma
              TextToSpeech(text) # Metni konuşmaya çevirme ve oynatma				  

except KeyboardInterrupt: # Ctrl-C ile çıkış
       pass	   


```

Programı çalıştırdığımızda, SpeechToText() fonksiyonu mikrofondan gelen insan sesini metne çevirir ve metin değerini ekrana yazar. Sonra, TextToSpeech() fonksiyonu ile metni konuşmaya çevirir ve oynatır. Aynı işlem sürekli tekrar eder. Ctrl-C tuş bileşimine bastığımızda, program sona erer.
