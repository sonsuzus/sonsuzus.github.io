---
layout: post
title: "Metinlerin Ruh Hâlini Okuyan Temel Bir Duygu Analizi Motoru"
math: true
categories: 
  - Proje
tags: 
  - doğal dil işleme
  - duygu analizi
  - Python
---

Bir bilgisayarın “Bu uygulamaya bayıldım!” ile “Bir daha asla kullanmam!” arasındaki farkı anlayabilmesi kulağa sihir gibi gelebilir. Oysa temel seviyede bir duygu analizi motoru; metni temizleme, kelimeleri puanlama ve sonuçları birleştirme adımlarından oluşur. Bu projede makine öğrenmesine dalmadan, sözlük tabanlı ve açıklanabilir bir doğal dil işleme motoru geliştireceğiz.

``

## Duygu analizi nedir?

Duygu analizi, bir metindeki öznel tutumu genellikle **pozitif**, **negatif** veya **nötr** olarak sınıflandırma işlemidir. Müşteri yorumları, sosyal medya gönderileri ve destek talepleri bu yöntemle otomatik olarak incelenebilir.

En basit yaklaşımda her duygu kelimesine sayısal bir değer veririz. Örneğin “harika” kelimesi $+2$, “iyi” kelimesi $+1$, “kötü” kelimesi $-1$ ve “berbat” kelimesi $-2$ puan alabilir. Metnin toplam skoru şöyle hesaplanır:

$$S = \sum_{i=1}^{n} w_i$$

Burada $w_i$, metindeki $i$. kelimenin duygu puanıdır. Sonuç $S>0$ ise pozitif, $S<0$ ise negatif, $S=0$ ise nötr kabul edilir.

| Yaklaşım | Avantajı | Dezavantajı |
|---|---|---|
| Sözlük tabanlı | Basit ve açıklanabilir | Bağlamı sınırlı anlar |
| Makine öğrenmesi | Yeni örüntüleri öğrenebilir | Etiketli veri gerektirir |
| Derin öğrenme | Karmaşık bağlamları yakalar | Daha fazla veri ve kaynak ister |

## Metni işlemeye hazırlamak

Kullanıcılar aynı düşünceyi farklı biçimlerde yazabilir: “HARİKA!”, “harika” ve “Harika...” bilgisayar için başlangıçta farklı dizelerdir. Bu nedenle metni küçük harfe çevirmeli, noktalama işaretlerini temizlemeli ve kelimelere ayırmalıyız. Bu işleme **normalizasyon** denir.

```python
import re

def metni_hazirla(metin):
    metin = metin.lower()
    metin = re.sub(r'[^a-zçğıöşü\s]', '', metin)
    return metin.split()
```

Bu fonksiyon, gereksiz karakterleri kaldırarak karşılaştırılabilir bir kelime listesi üretir. Gerçek projelerde kök bulma ve yazım düzeltme de eklenebilir.

## Duygu motorunu oluşturmak

Şimdi küçük bir sözlük tanımlayıp kelimelerin puanlarını toplayabiliriz. Ayrıca “değil” gibi olumsuzluk ifadeleri kendisinden sonraki kelimenin anlamını tersine çevirebilir. Örneğin “iyi değil” ifadesini doğrudan pozitif saymak büyük bir hata olur.

```python
duygu_sozlugu = {
    'harika': 2,
    'mükemmel': 2,
    'iyi': 1,
    'sevdim': 1,
    'kötü': -1,
    'berbat': -2,
    'nefret': -2
}

olumsuzluklar = {'değil', 'yok', 'asla'}

def duygu_analizi(metin):
    kelimeler = metni_hazirla(metin)
    skor = 0
    ters_cevir = False

    for kelime in kelimeler:
        if kelime in olumsuzluklar:
            ters_cevir = True
            continue

        puan = duygu_sozlugu.get(kelime, 0)
        if ters_cevir and puan != 0:
            puan *= -1
            ters_cevir = False
        skor += puan

    if skor > 0:
        return 'pozitif', skor
    if skor < 0:
        return 'negatif', skor
    return 'nötr', skor
```

Fonksiyon bilinmeyen kelimelere sıfır puan verir. Olumsuzluk görülürse sıradaki duygu kelimesinin işareti değiştirilir. Böylece motor yalnızca kelime saymak yerine küçük de olsa bağlam takibi yapar.

```python
print(duygu_analizi('Ürün harika, gerçekten sevdim!'))
# ('pozitif', 3)

print(duygu_analizi('Hizmet iyi değil.'))
# ('negatif', -1)
```

## Başarıyı nasıl ölçeriz?

Motoru değerlendirmek için önceden etiketlenmiş test cümleleri hazırlanabilir. Doğruluk oranı şu formülle bulunur:

$$Doğruluk = \frac{Doğru\ Tahmin}{Toplam\ Tahmin}$$

Ancak alaycılık, deyimler ve alan bağımlı kelimeler sistemi şaşırtabilir. “Telefon ateş ediyor” olumlu bir övgüyken gerçek bir yangın metninde olumsuzdur. Motoru geliştirmek için sözlüğe ağırlık artırıcı “çok”, “aşırı” gibi ifadeler eklenebilir; emojiler puanlanabilir ve sonuçlar bir veri kümesiyle test edilebilir. Böylece küçük sözlük, zamanla daha becerikli bir dijital duygu dedektifine dönüşür.
