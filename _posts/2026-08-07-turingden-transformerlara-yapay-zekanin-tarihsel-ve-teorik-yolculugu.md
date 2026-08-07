---
layout: post
title: "Turing'den Transformer'lara: Yapay Zekânın Tarihsel ve Teorik Yolculuğu"
math: true
categories: 
  - Bilgi
tags: 
  - yapay zeka
  - Alan Turing
  - makine öğrenmesi
---

Yapay zekâ, makinelerin yalnızca hesap yapmasını değil; algılama, öğrenme, akıl yürütme ve karar verme gibi zekâyla ilişkilendirilen görevleri gerçekleştirmesini amaçlayan disiplinler arası bir alandır. Bugün sohbet botlarından otonom araçlara kadar her yerde karşımıza çıksa da bu yolculuk, “Makineler düşünebilir mi?” sorusuyla başladı.
``
## Turing Testi ve zekânın ölçülmesi

Alan Turing, 1950 tarihli *Computing Machinery and Intelligence* makalesinde düşünmenin kesin bir tanımını yapmak yerine davranışsal bir ölçüt önerdi. **Taklit Oyunu** olarak adlandırılan ve sonradan Turing Testi diye bilinen düzende bir insan değerlendirici, yazılı mesajlarla insan ve makineyle konuşur. Değerlendirici hangisinin makine olduğunu güvenilir biçimde ayırt edemiyorsa makine, insan benzeri dil davranışı sergilemiş kabul edilir.

Test önemli bir felsefi dönüşüm yarattı: İç dünyası gözlemlenemeyen bir sistemin zekâsı, davranışı üzerinden değerlendirilebilirdi. Ancak test; bilinç, doğruluk veya gerçek anlama garantisi vermez. Son derece ikna edici biçimde yanlış konuşan bir program testi geçebilir. Günümüzün büyük dil modelleri etrafındaki tartışmalar da tam olarak bu noktaya dokunur.

## Sembolik yapay zekâ dönemi

“Yapay zekâ” terimi, 1956 Dartmouth çalıştayında akademik kimlik kazandı. İlk araştırmacılar zekânın semboller ve açık kurallar aracılığıyla modellenebileceğine inanıyordu. Bu yaklaşımda bilgi, mantıksal ifadeler şeklinde temsil edilir:

$$İnsan(x) \land İnsanlarınÖlümlüOlması \Rightarrow Ölümlü(x)$$

Bir uzman sistem, mevcut olgulara kurallar uygulayarak yeni sonuçlar üretir. Örneğin basit bir teşhis mekanizması şöyle yazılabilir:

```python
belirtiler = {"ates", "oksuruk"}

if {"ates", "oksuruk"}.issubset(belirtiler):
    sonuc = "Solunum yolu enfeksiyonu araştırılmalı"
else:
    sonuc = "Yeterli kural eşleşmesi yok"

print(sonuc)
```

Bu kod, sembolik yaklaşımın şeffaflığını gösterir: Sonucun hangi koşuldan çıktığı bellidir. Fakat gerçek dünya istisnalarla doludur. Binlerce kuralı elle yazmak, çelişkileri çözmek ve belirsizliği temsil etmek zorlaşır. Bu darboğazlar ile sınırlı donanım, 1970'ler ve 1980'lerin sonlarında “yapay zekâ kışı” denilen yatırım ve ilgi düşüşlerine katkıda bulundu.

## Veriden öğrenmeye geçiş

Modern istatistiksel yaklaşımda geliştirici bütün kuralları yazmaz; model, örneklerden örüntü öğrenir. Amaç çoğu zaman belirli girdiler altında en olası çıktıyı bulmaktır:

$$\hat{y}=\arg\max_y P(y\mid x)$$

Bu dönüşümü daha fazla dijital veri, güçlü işlemciler, internet ve gelişmiş optimizasyon yöntemleri hızlandırdı. 1990'larda olasılıksal modeller ve destek vektör makineleri öne çıkarken, 2010'larda derin öğrenme görüntü ve konuşma alanlarında büyük sıçramalar sağladı. 2012'de AlexNet'in başarısı, GPU destekli sinir ağlarının gücünü görünür hâle getirdi.

| Özellik | Sembolik yaklaşım | İstatistiksel yaklaşım |
|---|---|---|
| Bilgi kaynağı | İnsan tarafından yazılan kurallar | Veriden öğrenilen parametreler |
| Güçlü yanı | Açıklanabilir akıl yürütme | Gürültüye ve karmaşık örüntülere uyum |
| Zayıf yanı | Kural patlaması ve kırılganlık | Veri ihtiyacı ve düşük açıklanabilirlik |
| Tipik örnek | Uzman sistem | Sinir ağı |

## Transformer çağı ve üretken yapay zekâ

2017'de tanıtılan Transformer mimarisi, dizilerdeki öğelerin birbirleriyle ilişkisini **dikkat mekanizması** üzerinden hesapladı. Basitleştirilmiş dikkat formülü şöyledir:

$$Attention(Q,K,V)=softmax(QK^T/\sqrt{d_k})V$$

Bu yapı paralel eğitime elverişli olduğu için devasa metin koleksiyonlarından dil örüntülerinin öğrenilmesini kolaylaştırdı. Büyük dil modelleri bir sonraki belirtecin olasılığını tahmin ederek eğitilse de ölçek büyüdükçe özetleme, kod üretme ve soru yanıtlama gibi yetenekler sergiledi.

Yine de günümüz yapay zekâsı kusursuz değildir: Yanlış bilgi üretebilir, eğitim verilerindeki önyargıları yansıtabilir ve yüksek enerji tüketebilir. Alanın geleceği muhtemelen sembolik yöntemlerle istatistiksel öğrenmenin rakip değil, tamamlayıcı kabul edildiği hibrit sistemlerde yatıyor. Kısacası Turing'in sorusu hâlâ masada; yalnızca makinelerin verdiği cevaplar artık çok daha etkileyici.
