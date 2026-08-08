---
layout: post
title: "MIDI’den Müziğe: Algoritmik Arpej ve Akor Motoru Geliştirmek"
math: true
categories: 
  - Proje
tags: 
  - MIDI
  - algoritmik beste
  - Python
---

Bir MIDI klavyede tek bir notaya basıp karşılığında tonaliteye uygun akorlar, kıvrak arpejler ve küçük beste fikirleri duyduğunuzu düşünün. Bunu yapmak için yapay zekâ ordusuna ihtiyacımız yok; biraz müzik teorisi, MIDI mesajları ve iyi tasarlanmış olasılık kuralları yeterli. Bu projede gelen notaları analiz eden ve seçilen gama sadık kalarak gerçek zamanlı müzikal çıktılar üreten bir beste motorunun temelini kuracağız.
``
## MIDI tarafında gerçekte ne geliyor?

MIDI ses taşımaz; müzikal olayları temsil eden sayısal mesajlar taşır. En önemli mesajlardan biri `note_on` mesajıdır. İçinde nota numarası, hız ve kanal bilgisi bulunur. Örneğin orta Do, MIDI standardında 60 numarasıdır.

Bir notanın frekansı şu formülle hesaplanabilir:

$$f(n)=440\times2^{\frac{n-69}{12}}$$

Burada $n$ MIDI nota numarasıdır. Dolayısıyla $n=69$, yani La4, tam olarak 440 Hz verir. Beste motorumuz çoğunlukla frekans yerine nota numaralarıyla çalışacak; çünkü transpoze işlemi yalnızca tam sayı eklemeye dönüşür.

| Kavram | MIDI karşılığı | Motordaki görevi |
|---|---:|---|
| Nota | 0–127 | Melodi ve akor kökü |
| Velocity | 0–127 | Vurgu ve dinamik |
| Kanal | 1–16 | Enstrüman ayrımı |
| Clock | Zamanlama mesajı | Tempo senkronizasyonu |

## Gamı matematiksel olarak modellemek

Bir gamı, kök notaya eklenecek yarım ses aralıkları listesi şeklinde tanımlayabiliriz. Do majör için bu küme $S=\{0,2,4,5,7,9,11\}$ olur. Gelen MIDI notasının perde sınıfı ise $p=n\bmod12$ ile bulunur.

Nota gam dışındaysa en yakın geçerli perdeye yuvarlayabiliriz:

$$q=\operatorname*{argmin}_{s\in S}|p-s|$$

Bu yaklaşım basittir; ancak eşit uzaklıktaki iki nota arasında sürekli aynı yönü seçmek mekanik duyulabilir. Daha müzikal bir sonuç için melodinin önceki yönünü veya velocity değerini karar sürecine katmak mümkündür.

| Yöntem | Avantaj | Olası sorun |
|---|---|---|
| En yakın notaya yuvarlama | Güvenli ve hızlı | Tekdüze sonuç |
| Ağırlıklı rastgele seçim | Daha canlı üretim | Kontrol azalabilir |
| Önceki notayı izleme | Melodik bütünlük | Durum saklamak gerekir |

## Akor ve arpej üreticisi

Bir gam akoru, gam derecelerini üçlü aralıklarla üst üste koyarak üretilebilir. Derece indeksimiz $i$ ise üç sesli akorun indeksleri $i$, $(i+2)\bmod7$ ve $(i+4)\bmod7$ olur. Arpej ise aynı notaların eşzamanlı değil, belirli bir sırayla çalınmasıdır.

Aşağıdaki Python kodu, `mido` kütüphanesiyle gelen notayı Do majöre yaklaştırır ve majör üçlüden oluşan bir arpej gönderir:

```python
import time
import mido

SCALE = [0, 2, 4, 5, 7, 9, 11]
ROOT = 60


def quantize(note):
    candidates = [ROOT + interval + 12 * octave
                  for octave in range(-2, 4)
                  for interval in SCALE]
    return min(candidates, key=lambda candidate: abs(candidate - note))


def play_arpeggio(output, root, velocity=80):
    chord = [root, root + 4, root + 7, root + 12]
    pattern = [0, 1, 2, 1, 3, 2]

    for index in pattern:
        note = chord[index]
        output.send(mido.Message("note_on", note=note,
                                 velocity=velocity))
        time.sleep(0.12)
        output.send(mido.Message("note_off", note=note, velocity=0))


with mido.open_input() as input_port, mido.open_output() as output_port:
    for message in input_port:
        if message.type == "note_on" and message.velocity > 0:
            safe_note = quantize(message.note)
            play_arpeggio(output_port, safe_note, message.velocity)
```

`quantize` fonksiyonu giriş notasını gamdaki en yakın notaya taşır. `pattern` dizisi ise akor seslerinin çalınma sırasını belirler. Bu diziyi rastgele seçmek yerine birkaç müzikal şablon arasında geçiş yapmak, sonuçların hem kontrollü hem de şaşırtıcı kalmasını sağlar.

## Beste motorunu geliştirmek

Gerçek bir motor için sabit `sleep` yerine BPM tabanlı zamanlama kullanılmalıdır. Bir vuruşun süresi $T=60/BPM$ formülüyle hesaplanır. Ayrıca Markov zinciriyle akor geçişleri tanımlanabilir; örneğin I akorundan IV veya V akoruna geçişe yüksek olasılık verilebilir.

Velocity değişimleri, oktav sıçramaları, sus notaları ve farklı arpej yönleri eklediğinizde sistem yalnızca doğru notaları basan bir makine olmaktan çıkar. Artık küçük tercihler yapan, bazen gerilim yaratan ve eve dönüş akorunu bulduğunda rahatlayan dijital bir grup arkadaşına dönüşür.
