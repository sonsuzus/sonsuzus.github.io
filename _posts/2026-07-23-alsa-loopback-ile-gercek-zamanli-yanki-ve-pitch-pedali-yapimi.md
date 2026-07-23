---
layout: post
title: "ALSA Loopback ile Gerçek Zamanlı Yankı ve Pitch Pedalı Yapımı"
math: true
categories: 
  - Proje
tags: 
  - ALSA
  - Linux Audio
  - DSP
  - Python
  - Ses Efekti
---

Linux üzerinde gitar pedalı gibi çalışan bir ses efekti sistemi kurmak kulağa stüdyo büyüsü gibi gelebilir; ama ALSA’nın loopback cihazı ve biraz DSP bilgisiyle mikrofon girişini yakalayıp yankı ve pitch değişimi uygulayan gerçek zamanlı bir pedal yapmak gayet mümkün. Bu yazıda hedefimiz: mikrofonu sanal bir ses hattına bağlamak, sesi küçük tamponlar halinde işlemek ve çıktıyı hoparlöre ya da başka bir uygulamaya göndermek.
``
ALSA’da loopback cihazı, fiziksel kablo takmadan ses sinyalini bir uygulamadan diğerine taşıyan sanal bir ses kartıdır. `snd-aloop` modülü yüklendiğinde sistemde genellikle `Loopback` adlı yeni bir kart görünür. Mantık şudur: bir tarafa yazılan ses, diğer taraftan okunabilir. Böylece mikrofon, efekt işlemcisi ve hoparlör arasında dijital bir pedal tahtası kurarız.

Önce modülü etkinleştirelim:

```bash
sudo modprobe snd-aloop
aplay -l
arecord -l
```

Kalıcı yapmak için `/etc/modules-load.d/alsa-loopback.conf` içine şu satır eklenebilir:

```bash
snd-aloop
```

Ses zincirimiz teorik olarak şöyle çalışır:

| Aşama | Görev | Gecikmeye Etkisi |
|---|---|---|
| Mikrofon girişi | Analog sesi sayısala çevirir | Düşük/orta |
| ALSA buffer | Sesi bloklar halinde taşır | Kritik |
| Efekt işlemcisi | Yankı ve pitch uygular | CPU’ya bağlı |
| Loopback çıkışı | İşlenmiş sesi yönlendirir | Düşük |
| Hoparlör/uygulama | Son sesi çalar veya kaydeder | Değişken |

Gerçek zamanlı ses işlemede en önemli denklem gecikmedir. Örnekleme frekansı $f_s$ ve tampon boyutu $N$ ise tek tampon gecikmesi yaklaşık şöyledir:

$L = \frac{N}{f_s}$

Örneğin $N=256$ ve $f_s=48000$ için $L \approx 5.3ms$ olur. Bu değer küçükse pedal hızlı tepki verir; ancak çok küçültürsek CPU yetişemez ve çıtırtılar başlar. Yani düşük gecikme ile kararlılık arasında tatlı bir denge ararız.

Yankı efekti temelde gecikmiş sinyalin tekrar karıştırılmasıdır:

$y[n] = x[n] + g \cdot x[n-D]$

Burada $D$ gecikme örneği, $g$ ise geri besleme veya karışım miktarıdır. Pitch değiştirme ise daha hilelidir; sesi hızlandırıp/yavaşlatmak perdeyi değiştirir ama süreyi de bozar. Basit bir pedal prototipinde kısa tamponlar üzerinde yeniden örnekleme kullanabiliriz. Profesyonel sonuç için phase vocoder veya granular yöntemler tercih edilir.

Aşağıdaki Python örneği, `sounddevice` ile girişten ses alır, basit yankı ekler ve pitch için yeniden örnekleme tabanlı kaba bir yaklaşım uygular. Üretim ortamında JACK/PipeWire daha esnek olabilir; fakat ALSA mantığını kavramak için bu örnek yeterli bir laboratuvardır.

```python
import numpy as np
import sounddevice as sd
from scipy.signal import resample

fs = 48000
block = 512
delay_ms = 280
delay_samples = int(fs * delay_ms / 1000)
feedback = 0.35
mix = 0.55
pitch_ratio = 1.12  # 1.0 normal, >1 tiz, <1 pes

delay_buffer = np.zeros(delay_samples, dtype=np.float32)
write_pos = 0

def pitch_shift_simple(x, ratio):
    # Kısa bloğu yeniden örnekleyerek perdeyi kaba şekilde değiştirir.
    # Sonra tekrar eski blok boyuna getirir.
    if ratio == 1.0:
        return x
    n = len(x)
    stretched = resample(x, max(1, int(n / ratio)))
    shifted = resample(stretched, n)
    return shifted.astype(np.float32)

def callback(indata, outdata, frames, time, status):
    global write_pos, delay_buffer
    if status:
        print(status)

    x = indata[:, 0].astype(np.float32)
    pitched = pitch_shift_simple(x, pitch_ratio)
    y = np.zeros_like(pitched)

    for i, sample in enumerate(pitched):
        delayed = delay_buffer[write_pos]
        y[i] = sample * (1 - mix) + delayed * mix
        delay_buffer[write_pos] = sample + delayed * feedback
        write_pos = (write_pos + 1) % delay_samples

    outdata[:, 0] = y

with sd.Stream(channels=1, samplerate=fs, blocksize=block, callback=callback):
    print("Efekt pedalı çalışıyor. Durdurmak için Ctrl+C.")
    while True:
        sd.sleep(1000)
```

Bu kodda `delay_buffer` geçmiş sesi saklayan dairesel hafızadır. `write_pos` sona gelince başa döner; böylece sonsuz uzunlukta dizi kullanmadan yankı üretiriz. Pitch kısmı bilerek sade tutuldu: amaç algoritmanın iskeletini görmek. Daha pürüzsüz sonuç için pencereleme, overlap-add ve faz sürekliliği gerekir.

ALSA loopback yönlendirmesi için `pavucontrol`, PipeWire patchbay araçları veya doğrudan `.asoundrc` kullanılabilir. Basit testlerde mikrofonu Python uygulamasına giriş, uygulama çıkışını da Loopback oynatma cihazına vermek yeterlidir. Ardından OBS, DAW veya başka bir kayıt aracı Loopback yakalama tarafını dinleyebilir.

| Parametre | Küçük Değer | Büyük Değer |
|---|---|---|
| Buffer | Az gecikme, riskli CPU | Stabil, hissedilir gecikme |
| Feedback | Kısa yankı | Uzayan tekrarlar |
| Mix | Doğal sinyal baskın | Efekt baskın |
| Pitch ratio | Pesleşme | Tizleşme |

Sonuçta ALSA loopback bize sanal kabloyu, Python/DSP kodu ise pedalın elektronik devresini verir. Birkaç parametreyi MIDI kontrolcüye bağlayarak gerçek bir sahne pedalına yaklaşabilir; hatta zincire distortion, chorus ve compressor ekleyerek Linux tabanlı kendi mini efekt istasyonunuzu kurabilirsiniz.
