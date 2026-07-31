---
layout: post
title: "Yapay Zekâ Dili Nasıl Öğreniyor: Çocuk mu, İstatistiksel Papağan mı?"
math: true
categories: 
  - Bilgi
tags: 
  - yapay zekâ
  - dil edinimi
  - makine öğrenmesi
---

Bir çocuk “kedi” kelimesini öğrenirken tüylü bir canlıya dokunur, miyavlamasını duyar ve bazen kuyruğunun çekilmemesi gerektiğini deneyimleyerek keşfeder. Bir yapay zekâ modeli ise milyonlarca cümlede “kedi” sözcüğünün hangi kelimelerle yan yana geldiğini inceler. İkisi de örüntü öğrenir; fakat birinin dünyası oyuncaklar, insanlar ve duyulardan, diğerinin dünyası çoğunlukla veri ile matematikten oluşur.

``

## İnsanların dil edinimi

Dil edinimini açıklayan tek bir kuram yoktur. **Davranışçı yaklaşım**, çocuğun taklit, tekrar ve ödüllendirme yoluyla konuşmayı öğrendiğini savunur. Çocuk “su” dediğinde bardağa kavuşuyorsa doğru kullanım pekiştirilmiş olur. Bu görüş, makine öğrenmesindeki ödül mekanizmalarına oldukça benzer.

**Doğuştancı yaklaşım** ise Noam Chomsky ile özdeşleşir. Buna göre insan beyni, dilin temel yapılarını öğrenmeye hazır biyolojik bir donanımla doğar. Çocuklar sınırlı ve hatalı örneklere rağmen daha önce hiç duymadıkları kurallı cümleler üretebilir. Bu durum, dil öğrenmenin yalnızca ezber olmadığını gösterir.

**Etkileşimci yaklaşım**, biyolojik kapasite ile sosyal çevreyi birleştirir. Çocuğa yöneltilen konuşmalar, jestler, ortak dikkat ve geri bildirim dilin anlam kazanmasını sağlar. “Top” yalnızca üç harfli bir dizilim değildir; yuvarlanan, atılan ve bazen cam kıran bir nesnedir.

| Boyut | İnsan çocuğu | Dil modeli |
|---|---|---|
| Öğrenme kaynağı | Duyu, beden ve sosyal etkileşim | Metin, görsel veya başka sayısal veriler |
| Temel sinyal | Anlam, ihtiyaç ve geri bildirim | İstatistiksel hata ve optimizasyon |
| Veri miktarı | Görece az | Genellikle çok büyük |
| Dünya deneyimi | Doğrudan ve fiziksel | Çoğunlukla dolaylı |
| Yeni cümle üretimi | Kural ve bağlamla | Olasılık dağılımlarıyla |

## Makine kelimeleri nasıl öğrenir?

Büyük dil modelleri metni önce **token** adı verilen parçalara böler. Token bazen bir kelime, bazen ek veya noktalama işaretidir. Her token, modelin işleyebileceği sayısal bir vektöre dönüştürülür. Transformer mimarisindeki dikkat mekanizması, cümledeki parçaların birbirleriyle ilişkisini hesaplar.

Modelin temel görevi çoğunlukla sıradaki tokenı tahmin etmektir:

$$P(w_t \mid w_1, w_2, \ldots, w_{t-1})$$

Burada model, önceki tokenlar verildiğinde $w_t$ tokenının olasılığını hesaplar. Eğitim sırasında gerçek token ile tahmin arasındaki fark, çapraz entropi kaybıyla ölçülebilir:

$$L=-\sum_i y_i\log(\hat{y}_i)$$

Hata geriye yayılım ile ağırlıklara aktarılır. Milyarlarca tekrar sonunda model; dil bilgisi, üslup, kavram ilişkileri ve hatta bazı akıl yürütme kalıpları geliştirir.

Aşağıdaki küçük Python örneği, gerçek modellerden çok daha basit biçimde bir sonraki kelimeyi sayımlarla tahmin eder:

```python
from collections import defaultdict, Counter

metin = "çocuk dili öğrenir model dili tahmin eder çocuk oyun oynar"
kelimeler = metin.split()
gecisler = defaultdict(Counter)

for mevcut, sonraki in zip(kelimeler, kelimeler[1:]):
    gecisler[mevcut][sonraki] += 1

def tahmin_et(kelime):
    adaylar = gecisler.get(kelime)
    return adaylar.most_common(1)[0][0] if adaylar else None

print(tahmin_et("çocuk"))  # En sık gelen kelimeyi döndürür
```

Bu kod anlamı kavramaz; yalnızca ardışıklıkları sayar. Büyük modeller de temelde olasılık öğrenir, ancak dikkat katmanları ve devasa parametre uzayları sayesinde çok daha karmaşık ilişkiler kurar.

## Çocuk mu, papağan mı?

“İstatistiksel papağan” benzetmesi, modellerin kelimeleri gerçek dünyada deneyimlemeden yeniden birleştirdiğini vurgular. Benzetme yararlıdır ama eksiktir: Model sabit cümleleri tekrar etmekten fazlasını yapabilir; yeni özetler, kodlar ve benzetmeler üretebilir. Yine de akıcı bir yanıt, bilinç veya gerçek deneyim kanıtı değildir.

En dengeli sonuç şudur: Yapay zekâ ne insan gibi bir çocuk ne de basit bir papağandır. O, dilin izlerinden etkileyici yapılar çıkaran matematiksel bir örüntü öğrencisidir. Çocuk dili dünyada yaşamak için öğrenir; model ise dünyayı, dilde bırakılmış izlerden tahmin etmeye çalışır.
