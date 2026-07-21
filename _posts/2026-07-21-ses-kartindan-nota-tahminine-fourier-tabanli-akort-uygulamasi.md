---
layout: post
title: "Ses Kartından Nota Tahminine: Fourier Tabanlı Akort Uygulaması"
math: true
categories: 
  - Proje
tags: 
  - ses işleme
  - fourier dönüşümü
  - python
  - akort
  - dsp
---

Bir akort uygulaması kulağa basit gelir: teli çal, ekranda notayı gör. Ama perdenin arkasında ses kartından gelen ham örnekler, gürültü, pencereleme, Fourier dönüşümü ve biraz müzik teorisi birlikte dans eder. Bu yazıda, mikrofon ya da ses kartı girişinden alınan ham sinyali frekans analizine sokup enstrümanın notasını tahmin eden orta seviye bir uygulamanın mantığını kuracağız.
``
Ses kartı aslında sürekli bir analog hava titreşimini sayılara çevirir. Bu işleme örnekleme denir. Saniyede alınan örnek sayısı $f_s$ ile gösterilir; örneğin 44100 Hz, saniyede 44100 ölçüm demektir. Bir buffer içinde $N$ adet örnek toplarsak, analiz edebileceğimiz frekans çözünürlüğü yaklaşık olarak şudur:

$$\Delta f = \frac{f_s}{N}$$

Yani $f_s=44100$ ve $N=4096$ ise çözünürlük yaklaşık 10.77 Hz olur. Bu, gitar akordu için çalışır ama çok hassas değildir. Buffer büyüdükçe frekans çözünürlüğü artar, fakat gecikme de artar. Akort uygulamasının temel tasarım savaşı budur: hızlı mı olsun, hassas mı?

| Parametre | Küçük Değer | Büyük Değer | Akort Uygulamasına Etkisi |
|---|---:|---:|---|
| Buffer boyutu $N$ | Düşük gecikme | İyi frekans çözünürlüğü | Denge gerekir |
| Örnekleme oranı $f_s$ | Daha az veri | Daha geniş bant | 44100 Hz genelde yeterli |
| Pencere fonksiyonu | Basit analiz | Daha az sızıntı | Hann iyi başlangıçtır |

Ham sinyal doğrudan Fourier dönüşümüne verildiğinde bazı sorunlar çıkar. Çünkü biz sonsuz uzunlukta değil, kısa bir ses parçası inceleriz. Kesilen sinyalin kenarları ani sıçrama gibi davranır ve spektral sızıntı oluşur. Bu yüzden buffer’a Hann penceresi uygularız. Ayrık Fourier dönüşümünün fikri şudur:

$$X[k] = \sum_{n=0}^{N-1} x[n] e^{-j2\pi kn/N}$$

Burada $X[k]$, sinyalin hangi frekans bileşenlerinde güçlü olduğunu söyler. En büyük genlikli frekans çoğu zaman temel frekanstır; ama enstrümanlarda harmonikler yüzünden bazen ikinci ya da üçüncü harmonik temel frekanstan daha güçlü olabilir. Bu yüzden gerçek uygulamalarda yalnızca en yüksek tepeye güvenmek yerine belirli aralıkta arama, parabolik interpolasyon veya YIN gibi algoritmalar da kullanılır.

Nota tahmini için frekansı en yakın müzikal notaya eşleriz. Batı müziğinde A4 notası 440 Hz kabul edilirse MIDI nota numarası şu formülle bulunabilir:

$$m = 69 + 12\log_2\left(\frac{f}{440}\right)$$

Sonra $m$ değerini en yakın tam sayıya yuvarlarız. Farkı cent cinsinden gösterirsek kullanıcıya telin pes mi tiz mi olduğunu anlatabiliriz:

$$cent = 1200\log_2\left(\frac{f}{f_{nota}}\right)$$

| Cent Değeri | Anlamı | Kullanıcıya Mesaj |
|---:|---|---|
| -20 | Pes | Teli biraz sık |
| 0 | Tam akort | Harika, dokunma |
| +20 | Tiz | Teli biraz gevşet |

Aşağıdaki Python örneği `sounddevice` ile ses kartından veri alır, NumPy ile FFT uygular ve en yakın notayı hesaplar. Kod öğretici amaçlıdır; sahnede kullanmadan önce gürültü eşiği ve daha sağlam temel frekans algılama eklemek iyi olur.

```python
import numpy as np
import sounddevice as sd

FS = 44100
N = 4096
NOTE_NAMES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

def freq_to_note(freq):
    midi = 69 + 12 * np.log2(freq / 440.0)
    nearest = int(round(midi))
    note_freq = 440.0 * (2 ** ((nearest - 69) / 12))
    cents = 1200 * np.log2(freq / note_freq)
    name = NOTE_NAMES[nearest % 12] + str(nearest // 12 - 1)
    return name, cents, note_freq

def detect_pitch(samples):
    samples = samples - np.mean(samples)
    windowed = samples * np.hanning(len(samples))
    spectrum = np.fft.rfft(windowed)
    magnitudes = np.abs(spectrum)
    freqs = np.fft.rfftfreq(len(samples), 1 / FS)

    valid = (freqs > 60) & (freqs < 1200)
    index = np.argmax(magnitudes[valid])
    freq = freqs[valid][index]
    return freq

with sd.InputStream(channels=1, samplerate=FS, blocksize=N) as stream:
    while True:
        data, _ = stream.read(N)
        samples = data[:, 0]
        if np.max(np.abs(samples)) < 0.01:
            continue
        freq = detect_pitch(samples)
        note, cents, target = freq_to_note(freq)
        print(f'{freq:7.2f} Hz -> {note}, hedef {target:7.2f} Hz, sapma {cents:+5.1f} cent')
```

Kodda önce DC bileşenini temizlemek için ortalamayı çıkarıyoruz. Ardından Hann penceresi uygulayıp `rfft` ile yalnızca pozitif frekansları hesaplıyoruz. 60-1200 Hz aralığı gitar, bağlama, ukulele ve birçok melodik enstrüman için pratik bir başlangıçtır. En büyük spektral tepe bulunuyor, sonra bu frekans nota adına çevriliyor.

Daha profesyonel bir akort uygulaması için üç geliştirme önerisi çok işe yarar: tepe çevresinde parabolik interpolasyonla frekansı inceltmek, harmonikleri kontrol ederek temel frekansı doğrulamak ve ekranda cent sapmasını ibre ya da renkli göstergeyle sunmak. Sonuçta iyi bir tuner sadece matematik yapmaz; müzisyene sakin, okunabilir ve güvenilir geri bildirim verir. Fourier burada büyülü değnek değil, sesin içindeki düzeni görünür kılan güçlü bir büyüteçtir.
