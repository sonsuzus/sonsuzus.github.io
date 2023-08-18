---
title: Python Ses Kaydetme Programları
author: sonsuz
date: 2023-08-18 21:51:44 +0300
categories: [Program,Python]
tags: [python,programlama,ses,kayıt,pyaudio,wave,numpy,sounddevice,scipy]
---



## Ses kaydetme programı (pyaudio ve wave kütüphaneleri ile)

Program için aşağıda bilgileri ve sanal ortamda kurulum komutları verilen kütüphaneleri kullanacağız:

- PyAudio kütüphanesi

Tüm işletim sistemlerinde çalışan ses giriş/çıkış akışı kütüphanesidir. Ses ile ilgili işlemlerde kullanılır.

Bu kütüphanenin doğrudan "pip install pyaudio" komutu ile kurulmasında herhangi bir sorun yaşandığında kurulumu gerçekleştirmek için, Christoph Gohlke tarafından Python paketleri için resmi olmayan Windows işletim sistemi dosyalarını içeren web sitesine ait [buradaki](https://www.lfd.uci.edu/~gohlke/pythonlibs/) bağlantıdan bilgisayarımızın işletim sistemine göre indirdiğimiz aşağıdaki dosyalardan birisini, sanal ortamın altındaki Scripts dizini altına kopyalayarak kullanıyoruz:

PyAudio-0.2.11-cp39-cp39-win\_amd64.whl

PyAudio-0.2.11-cp39-cp39-win32.whl

```


pip install PyAudio-0.2.11-cp39-cp39-win_amd64.whl


```

- Wave kütüphanesi

Sesleri ses dosyalarına kaydetmek için kullanılır.

```


pip install Wave


```

Örnek

```py
import pyaudio # Sürüm 0.2.11
import wave # Sürüm 0.0.2

audio = pyaudio.PyAudio() # pyaudio nesnesi oluşturma

stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024) # Bir ses akışı açma

frames = []

try:
   while True:
         data = stream.read(1024) # Ses okuma
         frames.append(data) # Ses verisini ekleme

except KeyboardInterrupt: # Ctrl-C ile çıkış
       pass		 

stream.stop_stream() # Ses okumayı durdurma
stream.close() # Akışı kapatma
audio.terminate() # pyaudio nesnesini sona erdirme

wave_file = wave.open("kayit.wav", "wb") # Ses dosyası oluşturma
wave_file.setnchannels(1)
wave_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16)) 
wave_file.setframerate(44100)
wave_file.writeframes(b''.join(frames)) # Ses verilerini yazma
wave_file.close() # Ses dosyasını kapatma


```

Programı çalıştırdığımızda, ses kaydetmeye başlar. Ctrl-C tuş bileşimine bastığımızda, ses kaydı sona erer ve kaydedilen ses verileri bir dosyaya kaydedilir.

## Ses kaydetme programı (sounddevice ve scipy kütüphaneleri ile)

Sounddevice kütüphanesi ile, mikrofonumuzdan sesi alarak bir NumPy dizisi olarak kaydedebilir ve bu ses verisini WAV formatına dönüştürülebiliriz.

Program için aşağıda bilgileri ve sanal ortamda kurulum komutları verilen kütüphaneleri kullanacağız:

- Sounddevice kütüphanesi

PortAudio kütüphanesi bağlantıları ve fonksiyonlarla ses sinyalleri içeren NumPy dizilerini oynatır ve kaydeder.

```


pip install sounddevice


```

Bu kütüphane ile birlikte, cffi ve pycparser kütüphaneleri otomatik olarak yüklenir.

- Scipy kütüphanesi

NumPy kütüphanesine bağlı olarak çalışan bu kütüphane sesleri ses dosyalarına kaydetmek için kullanılır.

```


pip install scipy


```

Bu kütüphane ile birlikte, Numpy kütüphanesi otomatik olarak yüklenir.

Aşağıdaki program ile, belirlenen bir süre boyunca ses kaydı yapılarak bir dosyaya kaydedilir.

Örnek

```py
import sounddevice as sd
from scipy.io.wavfile import write

fs = 44100  # Saniyedeki örnekleme sayısı
saniye = 5 # Kayıt süresi

kayit = sd.rec(int(saniye * fs), samplerate=fs, channels=2)
sd.wait() # Kayıt bitene kadar bekleme
write('kayit.wav', fs, kayit) # wav dosyası olarak kaydetme 


```

Programı çalıştırdığımızda, 5 saniye süre ile ses kaydetmeye başlar. Süre sona erdiğinde, ses kaydı sona erer ve kaydedilen ses verileri bir dosyaya kaydedilir.

## Ses kaydetme programı (sounddevice ve soundfile kütüphaneleri ile)

Sounddevice kütüphanesi ile, mikrofonumuzdan sesi alarak bir NumPy dizisi olarak kaydedebilir ve bu ses verisini WAV formatına dönüştürülebiliriz. Daha sonra, soundfile kütüphanesi ile ses verilerini dosyaya kaydedebiliriz.

Program için aşağıda bilgileri ve sanal ortamda kurulum komutları verilen kütüphaneleri kullanacağız:

- Sounddevice kütüphanesi

PortAudio kütüphanesi bağlantıları ve fonksiyonlarla ses sinyalleri içeren NumPy dizilerini oynatır ve kaydeder.

SoundFile kütüphanesi ile, mikrofonumuzdan sesi alarak bir NumPy dizisi olarak kaydedebilir ve bu ses verisini WAV formatına dönüştürülebiliriz.

```


pip install sounddevice


```

- SoundFile kütüphanesi

PortAudio kütüphanesi bağlantıları ve fonksiyonlarla ses sinyalleri içeren NumPy dizilerini oynatır ve kaydeder.

```


pip install SoundFile


```

Bu kütüphane ile birlikte, cffi ve pycparser kütüphaneleri otomatik olarak yüklenir.

- NumPy kütüphanesi

NumPy, Python ile dizi hesaplamada kullanılan temel kütüphanedir.

```


pip install numpy


```

Aşağıdaki program komut satırından isteğe bağlı olarak tanımlayabileceğimiz 7 farklı argüman alabilir. Hiç argüman tanımlamasak bile, program bu değerlerin bazılarını kendisi tanımlayarak kullanır. Programın komut satırı kullanımı ve tanımlanabilecek argümanlar aşağıda gösterilmektedir

```


projeadi.py [-h] [-l] [-d DEVICE] [-r SAMPLERATE] [-c CHANNELS] [-t SUBTYPE] [FILENAME]


```

-h: Program kullanım şekline gösterir.

--list-devices: Ses aygıtlarını listeler ve program sona erer.

--device: Ses aygıtının sayısal ID değeri veya ad.

--samplerate: Örnekleme oranı.

--channels: Giriş kanallarının sayısı.

--subtype: Ses dosyası alt türü.

dosyaadi: Sesin kaydedileceği dosyanın adı.

Örnek

```py
import argparse
import tempfile
import queue
import sys

import sounddevice as sd
import soundfile as sf
import numpy # NumPy kütüphanesi callback fonksiyonu içinde kullanılmadan yüklemek için
assert numpy # "imported but unused" mesajını  (W0611) engellemek için

def int_or_str(text):
    try:
        return int(text)
    except ValueError:
        return text

parser = argparse.ArgumentParser(add_help=False)
parser.add_argument('-l', '--list-devices', action='store_true', help='Ses aygıtlarını listeler ve sona erer')
args, remaining = parser.parse_known_args()

if args.list_devices:
   print(sd.query_devices())
   parser.exit(0)
	
parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter, parents=[parser])
parser.add_argument('filename', nargs='?', metavar='FILENAME', help='Sesin kaydedileceği dosyanın adı')
parser.add_argument('-d', '--device', type=int_or_str, help='input device(Ses aygıtının sayısal ID değeri veya adı)')
parser.add_argument('-r', '--samplerate', type=int, help='Örnekleme oranı')
parser.add_argument('-c', '--channels', type=int, default=1, help='Giriş kanallarının sayısı')
parser.add_argument('-t', '--subtype', type=str, help='Ses dosyası alt türü(örneğin "PCM_24")')

args = parser.parse_args(remaining)

q = queue.Queue()

def callback(indata, frames, time, status):
    if status:
       print(status, file=sys.stderr)
    q.put(indata.copy())

try:
    if args.samplerate is None: # Örnekleme oranı komut satırından girilmemiş ise
       device_info = sd.query_devices(args.device, 'input')
       args.samplerate = int(device_info['default_samplerate'])
    if args.filename is None: # Dosya adı komut satırından  girilmemiş ise
       args.filename = 'kayit.wav' # Kayıt dosyası adı
	   # args.filename = tempfile.mktemp(prefix='kayit_', suffix='.wav', dir='') # Her defasında farklı dosya adı belirlemek için

    # Kayıttan önce dosya açma
    with sf.SoundFile(args.filename, mode='w', samplerate=args.samplerate, channels=args.channels, subtype=args.subtype) as file:
         with sd.InputStream(samplerate=args.samplerate, device=args.device, channels=args.channels, callback=callback):
              print('Ctrl+C ile kaydı durdurabilirsiniz!')
              while True:
                    file.write(q.get())
except KeyboardInterrupt:
       parser.exit(0)
except Exception as e:
       parser.exit(type(e).__name__ + ': ' + str(e))


```

Programı çalıştırdığımızda, ses kaydetmeye başlar. Ctrl-C tuş bileşimine bastığımızda, ses kaydı sona erer ve kaydedilen ses verileri bir dosyaya kaydedilir.
