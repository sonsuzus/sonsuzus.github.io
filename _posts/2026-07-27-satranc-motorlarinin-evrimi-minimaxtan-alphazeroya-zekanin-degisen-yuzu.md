---
layout: post
title: "Satranç Motorlarının Evrimi: Minimax’tan AlphaZero’ya Zekânın Değişen Yüzü"
math: true
categories: 
  - Bilgi
tags: 
  - satranç motorları
  - yapay zeka
  - AlphaZero
---

Bir satranç motorunun tahtaya bakıp “Bu hamle bana mantıklı geliyor” dediğini hayal ederiz; oysa uzun yıllar boyunca makinelerin sezgisi değil, yalnızca yorulmak bilmeyen hesap gücü vardı. Satranç motorlarının Minimax’tan AlphaZero’ya uzanan tarihi, daha fazla pozisyon hesaplamanın ötesinde, “Zekâ nedir?” sorusuna verilen mühendislik cevaplarının da tarihidir.

``

## Satranç neden yapay zekânın laboratuvarı oldu?

Satranç; kuralları kesin, sonuçları ölçülebilir ve seçenekleri olağanüstü geniş bir oyundur. Ortalama bir konumda yaklaşık 35 yasal hamle bulunur. Bir motor yalnızca $d$ yarım hamle ileri bakarsa incelemesi gereken düğüm sayısı kabaca

$$N \approx 35^d$$

olur. Sadece 8 yarım hamlede bu sayı trilyonlara yaklaşır. Dolayısıyla bütün oyunu baştan sona hesaplamak pratik değildir. Asıl mesele, olası geleceklerin hangilerinin araştırılmaya değer olduğunu belirlemektir.

## Minimax: Rakibin de akıllı olduğunu varsaymak

1950’lerin klasik yaklaşımı olan **Minimax**, oyuncuların kusursuz davranacağını kabul eder. Motor kendi hamlesinde skoru büyütürken rakibin cevabında skorun küçültüleceğini varsayar. Başka bir ifadeyle “Benim en iyi hamlem, rakibimin en güçlü cevabından sonra bile beni en iyi durumda bırakan hamledir” der.

Basitleştirilmiş algoritma şöyledir:

```python
def minimax(dugum, derinlik, maksimize):
    # Arama sınırına gelince konumu sayısal olarak değerlendirir.
    if derinlik == 0 or dugum.oyun_bitti():
        return dugum.degerlendir()

    skorlar = [
        minimax(cocuk, derinlik - 1, not maksimize)
        for cocuk in dugum.cocuklar()
    ]

    # Sıra bizdeyse en yüksek, rakipteyse en düşük skor seçilir.
    return max(skorlar) if maksimize else min(skorlar)
```

Buradaki kritik unsur **değerlendirme fonksiyonudur**. Motor; taş değerleri, şah güvenliği, piyon yapısı ve merkez kontrolü gibi özellikleri ağırlıklandırır:

$$E(s)=9V+5K+3F+3A+P+0.2M$$

Burada semboller vezir, kale, fil, at, piyon ve hareketlilik farklarını temsil edebilir. Bu formül “satranç bilgisi”nin insan tarafından makineye çevrilmiş hâlidir.

## Alpha-Beta ve kaba kuvvetin akıllanması

**Alpha-Beta budaması**, sonucu değiştiremeyeceği kesinleşen dalları incelemez. Doğru hamle sıralamasıyla Minimax’ın etkili karmaşıklığını yaklaşık $O(b^d)$ seviyesinden $O(b^{d/2})$ seviyesine indirebilir. Böylece aynı sürede neredeyse iki kat derinlik araştırılır.

1997’de Garry Kasparov’u yenen **Deep Blue**, bu geleneğin zirvesiydi: özel donanım, uzmanlarca yazılmış değerlendirme kuralları ve saniyede milyonlarca konum. Zeki görünüyordu; fakat bilgisini kendi deneyiminden üretmiyordu.

| Yaklaşım | Bilginin kaynağı | Temel güç | Başlıca sınır |
|---|---|---|---|
| Minimax | İnsan yapımı kurallar | Tutarlı planlama | Üstel arama ağacı |
| Deep Blue | Uzman bilgisi ve donanım | Çok derin hesap | Dar alana bağımlılık |
| AlphaZero | Kendi kendine oyun | Öğrenilmiş sezgi | Yüksek eğitim maliyeti |

## AlphaZero: Hesaplamadan öğrenilmiş sezgiye

2017’de tanıtılan **AlphaZero**, açılış kitapları veya insan oyunları olmadan yalnızca kuralları öğrendi. Kendisine karşı milyonlarca oyun oynayarak iki önemli çıktı üreten bir sinir ağı geliştirdi: hamle olasılıklarını veren **politika** $p(a|s)$ ve konumun kazanma beklentisini veren **değer** $v(s)$.

Bu ağ, **Monte Carlo Ağaç Araması** ile birleşir. Sistem her dalı eşit biçimde araştırmak yerine umut vadeden hamlelere yoğunlaşır; arama sonuçları da ağı yeniden eğitir. Böylece döngü oluşur: oyna, değerlendir, öğren ve daha güçlü yeniden oyna. AlphaZero’nun fedaları bazen romantik bir büyükustayı andırır; ancak bu estetik, önceden öğretilmiş ilkelerden değil, kazanma olasılığını optimize etmekten doğar.

## Zekâ gerçekten nerede?

Minimax zekâyı mantıklı seçim, Deep Blue devasa hesaplama, AlphaZero ise deneyimden temsil öğrenme olarak yorumlar. Yine de AlphaZero “şah güvenliği”ni bizim gibi kavramsallaştırmak zorunda değildir. İşe yarayan örüntüyü sayılara gömer.

Bu tarih küçük bir felsefi sürpriz sunar: Zeki davranış için insan gibi düşünmek gerekmeyebilir. Kaba kuvvet ile sezgi birbirinin zıddı da değildir; modern motorlarda öğrenilmiş sezgi, hesaplamanın nereye bakacağını söyler. Satranç tahtası böylece yalnızca bir oyun alanı değil, aklın kurallardan mı, deneyimden mi, yoksa ikisinin sürekli etkileşiminden mi doğduğunu sınayan siyah-beyaz bir laboratuvara dönüşür.
