---
layout: post
title: "Ses Dalgalarıyla Konuşan Bir Akustik Modem: FSK ile Veri İletimi"
math: true
categories: 
  - Proje
tags: 
  - akustik modem
  - FSK
  - Python
---

Eski çevirmeli modemlerin çıkardığı robotik sesler rastgele gürültü değildi; bilgisayarların veriyi ses dalgalarına dönüştürerek telefon hattından taşıma yöntemiydi. Bu projede aynı fikri daha küçük ölçekte uygulayacak, Frekans Kaydırmalı Anahtarlama (FSK) kullanarak hoparlörden veri gönderen ve mikrofonla çözen basit bir akustik modem tasarlayacağız.

``

## Akustik modem nasıl çalışır?

Dijital sistemde bitler yalnızca 0 ve 1'dir. Hoparlör ise doğrudan bit çalamaz; zamana göre değişen bir elektrik sinyalini sese dönüştürür. Bu nedenle bitleri ölçülebilir ses özellikleriyle temsil etmemiz gerekir.

İkili FSK, yani **BFSK**, iki farklı frekans kullanır:

- `0` biti için $f_0=1200\,Hz$
- `1` biti için $f_1=2200\,Hz$

Bir bitin süresi $T_b$ ise üretilen sinyal şöyle tanımlanabilir:

$$
s(t)=A\sin(2\pi f_b t), \qquad 0\leq t<T_b
$$

Burada $A$ genlik, $f_b$ ise bitin değerine göre seçilen frekanstır. Bit hızı yaklaşık olarak

$$R_b=\frac{1}{T_b}$$

bağıntısıyla bulunur. Örneğin her bit 20 milisaniye sürerse hız $50\,bit/s$ olur. Daha kısa semboller iletişimi hızlandırır; fakat yankı, gürültü ve zamanlama hatalarına karşı hassasiyeti artırır.

| Yöntem | Bitleri temsil eden özellik | Avantaj | Dezavantaj |
|---|---|---|---|
| FSK | Frekans | Gürültüye dayanıklı, anlaşılır | Daha geniş bant kullanır |
| ASK | Genlik | Uygulaması kolay | Ses seviyesi değişimlerinden etkilenir |
| PSK | Faz | Bant genişliğini verimli kullanır | Senkronizasyonu daha zordur |

İlk proje için FSK iyi bir tercihtir; çünkü alıcının yalnızca iki frekanstan hangisinin daha güçlü olduğunu belirlemesi yeterlidir.

## Verici tarafı

Aşağıdaki Python kodu metni bitlere çevirir, her bit için uygun sinüs dalgasını üretir ve sonucu WAV dosyasına kaydeder:

```python
import numpy as np
from scipy.io.wavfile import write

SAMPLE_RATE = 44100
BIT_TIME = 0.02
FREQUENCIES = {'0': 1200, '1': 2200}

def text_to_bits(text):
    return ''.join(f'{byte:08b}' for byte in text.encode('utf-8'))

def make_tone(frequency):
    sample_count = int(SAMPLE_RATE * BIT_TIME)
    t = np.arange(sample_count) / SAMPLE_RATE
    return 0.5 * np.sin(2 * np.pi * frequency * t)

payload = text_to_bits('Merhaba modem!')
frame = '1010101010101010' + payload
signal = np.concatenate([make_tone(FREQUENCIES[b]) for b in frame])
write('mesaj.wav', SAMPLE_RATE, np.int16(signal * 32767))
```

Baştaki dönüşümlü bitler bir **preamble** oluşturur. Alıcı bu bilinen örüntüyü yakalayarak mesajın nerede başladığını ve sembol sınırlarını tahmin edebilir. Gerçek bir protokolde preamble sonrasında veri uzunluğu ve hata denetim alanı da bulunmalıdır.

## Alıcı frekansı nasıl tanır?

Kaydı `BIT_TIME` uzunluğunda parçalara ayırıp her parçada 1200 Hz ile 2200 Hz enerjisini karşılaştırabiliriz. Bunun için FFT kullanılabilir. Yalnızca birkaç frekans aranıyorsa **Goertzel algoritması** daha hesaplıdır.

Bir frekansın ayrıştırılabilmesi örnekleme hızına bağlıdır. Nyquist koşuluna göre

$$f_s>2f_{max}$$

olmalıdır. Burada $f_s=44100\,Hz$ olduğu için 2200 Hz rahatlıkla örneklenebilir.

```python
import numpy as np

samples_per_bit = int(SAMPLE_RATE * BIT_TIME)

def energy_at(chunk, frequency):
    windowed = chunk * np.hanning(len(chunk))
    spectrum = np.fft.rfft(windowed)
    freqs = np.fft.rfftfreq(len(chunk), 1 / SAMPLE_RATE)
    index = np.argmin(np.abs(freqs - frequency))
    return abs(spectrum[index]) ** 2

def decode_chunk(chunk):
    low = energy_at(chunk, 1200)
    high = energy_at(chunk, 2200)
    return '1' if high > low else '0'
```

Hann penceresi, sembol sınırındaki ani kesilmelerin FFT üzerinde oluşturduğu spektral sızıntıyı azaltır. Çözülen bitler sekizli gruplara ayrılarak baytlara, ardından UTF-8 metne dönüştürülebilir.

## Modemi daha güvenilir yapmak

Oda yankısı ve arka plan sesi kusursuz dalgaları küçük bir kaosa çevirebilir. Bu nedenle çerçeveye CRC-16 eklemek, her baytı birden fazla göndermek veya Hamming kodu kullanmak faydalıdır. Otomatik eşik belirleme, mikrofon kazancını dengeleme ve korelasyonla preamble arama da başarı oranını yükseltir.

Testleri önce WAV dosyaları arasında, sonra aynı odadaki hoparlör ve mikrofonla yapın. Ses düzeyini rahatsız etmeyecek seviyede tutun. Birkaç ıslık benzeri tonla başlayan bu proje; paketleme, hata düzeltme ve daha gelişmiş modülasyonlarla gerçek bir mini iletişim sistemine dönüşebilir.
