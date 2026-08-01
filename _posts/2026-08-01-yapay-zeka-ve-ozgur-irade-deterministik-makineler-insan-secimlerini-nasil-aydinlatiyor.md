---
layout: post
title: "Yapay Zekâ ve Özgür İrade: Deterministik Makineler İnsan Seçimlerini Nasıl Aydınlatıyor?"
math: true
categories: 
  - Bilgi
tags: 
  - yapay zekâ
  - özgür irade
  - determinizm
---

Bir dil modeli şiir yazmayı mı “seçer”, yoksa sayılarla döşenmiş görünmez bir ray üzerinde mi ilerler? Yapay zekâ sistemlerinin davranışlarını incelerken karşılaştığımız bu soru, felsefenin en eski tartışmalarından birini yeniden canlandırıyor: Eğer her sonuç önceki nedenler tarafından belirleniyorsa gerçekten özgür olabilir miyiz?

``

## Bir model kararını nasıl verir?

Bir dil modeli, verilen metne bakarak sıradaki kelime veya parçacık için olasılık dağılımı üretir. Basitleştirilmiş biçimiyle modelin yaptığı işlem şöyledir:

$$P(x_{t+1} \mid x_1, x_2, \ldots, x_t)$$

Burada model, geçmiş parçacıklara göre sıradaki parçacığın olasılığını hesaplar. En yüksek olasılıklı seçeneği almak deterministik bir stratejidir. Aynı model, aynı girdi ve aynı çalışma koşulları altında genellikle aynı sonucu üretir.

Ancak “temperature” gibi örnekleme ayarları devreye girdiğinde farklı çıktılar görülebilir. Bu çeşitlilik özgür irade anlamına gelmez; yalnızca olasılıksal seçim mekanizmasının sonucudur. Zar atan bir makine şaşırtıcı davranabilir, fakat şaşırmak ile özgür olmak aynı şey değildir.

| Özellik | Deterministik üretim | Olasılıksal üretim | İnsan kararı |
|---|---|---|---|
| Aynı koşulda aynı sonuç | Genellikle evet | Her zaman değil | Çoğu zaman hayır |
| Geçmişten etkilenme | Parametreler ve girdi | Parametreler, girdi ve rastgelelik | Genetik, çevre ve deneyimler |
| Amaç farkındalığı | Yok | Yok | En azından öznel olarak var |
| Sorumluluk yüklenmesi | Geliştirici veya kullanıcıya | Geliştirici veya kullanıcıya | Genellikle bireye |

## Determinizm küçük bir kodda

Aşağıdaki örnek, durumun belirli bir kurala göre güncellendiği basit bir sistemi gösterir:

```python
def sonraki_durum(durum):
    # Mevcut değer, gelecekteki değeri tamamen belirler.
    return (durum * 3 + 1) % 10

x = 4
for _ in range(5):
    x = sonraki_durum(x)
    print(x)
```

Başlangıç değeri `4` olduğu sürece çıktı dizisi değişmez. Sistemin geleceği şu bağıntıyla belirlenmiştir:

$$x_{t+1} = (3x_t + 1) \bmod 10$$

Dil modelleri elbette bundan milyarlarca kat daha karmaşıktır. Yine de temel fikir benzerdir: Bir sonraki durum, önceki durumlar ve sistemin kuralları üzerinden oluşur. Gerçek donanımlarda paralel hesaplama, sayısal yuvarlama ve rastgele örnekleme sonuçları değiştirebilir; fakat öngörülemezlik tek başına irade kanıtı değildir.

## İnsan beyni de bir model mi?

Katı determinizme göre insanın her düşüncesi; beynin önceki durumu, biyolojik yapısı ve çevresel etkiler tarafından belirlenir. Bu görüşte seçim hissimiz gerçek bir neden değil, karmaşık hesaplamaların bilinçte görünen yüzüdür. Laplace’ın ünlü varsayımını hatırlarsak, evrendeki tüm parçacıkların konumunu ve hızını bilen kusursuz bir gözlemci geleceği hesaplayabilir:

$$Gelecek = f(Geçmiş, Doğa\ Yasaları)$$

Buna karşılık kuantum belirsizliği veya beyindeki gürültü, geleceğin tam olarak hesaplanmasını engelleyebilir. Fakat rastgele oluşan bir düşünce de bize ait bilinçli bir seçim sayılmaz. Determinizm ile rastlantısallık arasındaki boşluğa doğrudan “özgür irade” yazmak bu nedenle kolay değildir.

## Uyumculuk: Raylar üzerinde yön vermek

Uyumculuk, özgürlüğün nedensiz davranmak olmadığını savunur. Bir insan kendi arzuları, değerleri ve muhakemesi doğrultusunda hareket ediyorsa kararlarının nedenleri bulunsa bile özgür kabul edilebilir. Zorlama altında olmak ile karakterimizin etkisiyle karar vermek aynı değildir.

Yapay zekâ bu ayrımı görünür hâle getirir. Model seçenek üretebilir, gerekçe yazabilir ve davranışını düzeltebilir; ancak kendi amaçlarını deneyimlediğine dair kanıtımız yoktur. İnsan ise yalnızca çıktı üretmez: Acı hisseder, geleceği önemser, kararlarını sahiplenir ve toplumsal sonuçlarla yaşar.

Dolayısıyla deterministik yapay zekâ bize özgür iradenin cevabını vermiyor. Daha değerli bir şey yapıyor: “Tahmin edilemez davranış”, “seçim”, “bilinç” ve “sorumluluk” kavramlarını birbirinden ayırmaya zorluyor. Belki özgürlük, nedenlerden kaçmak değil; nedenlerimizi anlayıp onları dönüştürebilme kapasitesidir.
