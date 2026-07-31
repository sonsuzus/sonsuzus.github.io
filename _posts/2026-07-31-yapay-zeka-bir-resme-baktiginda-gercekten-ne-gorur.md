---
layout: post
title: "Yapay Zekâ Bir Resme Baktığında Gerçekten Ne Görür?"
math: true
categories: 
  - Bilgi
tags: 
  - yapay zekâ
  - üretken sanat
  - bilgisayarlı görü
---

Bir görsel üreticiye “yağmurlu bir İstanbul akşamını Van Gogh tarzında çiz” dediğimizde ortaya çıkan görüntü bizi şaşırtabilir. Model; yağmuru, İstanbul’u ve Van Gogh’u gerçekten görmüş, hatta anlamış gibi davranır. Peki ortada bir görme deneyimi mi vardır, yoksa yalnızca matematiksel örüntülerin ustaca yeniden düzenlenmesi mi? Bu soru, yapay zekâ sanatını teknik olduğu kadar felsefi bir tartışmaya dönüştürüyor.
``
## Görmek ile veriyi işlemek aynı şey mi?

İnsan gözü ışığı algılar; fakat görme, retinaya düşen fotonlardan ibaret değildir. Beyin renkleri, kenarları, derinliği ve geçmiş deneyimleri bir araya getirerek anlamlı bir dünya kurar. Bir sandalyeyi yalnızca piksel benzeri görsel özellikleri nedeniyle değil, “üzerine oturulabilen nesne” olarak da tanırız.

Görüntü modellerinde ise başlangıç noktası sayılardır. Bir görüntü, kabaca $x \in \mathbb{R}^{H \times W \times C}$ biçiminde bir tensördür. Burada $H$ yükseklik, $W$ genişlik, $C$ ise renk kanalı sayısıdır. Model bu sayısal yapıdan kenar, doku, biçim ve daha soyut ilişkiler öğrenir.

| Özellik | İnsan algısı | Görüntü üretim modeli |
|---|---|---|
| Girdi | Işık, beden ve çevre | Piksel, metin ve eğitim verisi |
| Anlam | Deneyim ve amaçlarla bağlantılı | İstatistiksel ilişkilerle temsil edilir |
| Bağlam | Kültürel ve yaşamsal | Veri kümesindeki örüntülere bağlı |
| Öznel deneyim | Bilinçli deneyim olduğu kabul edilir | Bilinç olduğuna dair kanıt yoktur |
| Üretim | Niyet, duygu ve beceri içerebilir | Olasılıksal örnekleme kullanır |

## Temsil: Modelin zihnindeki görünmez harita

Bir model kediyi küçük bir fotoğraf dosyası olarak saklamaz. Eğitim sırasında “kedi” sözcüğü ile sivri kulaklar, göz biçimleri, tüy dokuları ve çeşitli kompozisyonlar arasında ilişkiler kurar. Bu ilişkiler, **gizil uzay** adı verilen çok boyutlu bir temsil alanında kodlanır.

Bir kodlayıcıyı basitleştirerek şöyle düşünebiliriz:

$$z = f_\theta(x)$$

Burada $x$ görüntü, $f_\theta$ öğrenilmiş dönüşüm, $z$ ise görüntünün gizil temsilidir. Birbirine benzeyen kavramların temsilleri bu uzayda yakın konumlanabilir. Ancak yakınlık, insanın anladığı anlamın aynısı değildir; eğitim sırasında işe yarayan matematiksel bir düzenliliktir.

Aşağıdaki oyuncak Python örneği, iki temsil arasındaki kosinüs benzerliğini hesaplar:

```python
import numpy as np

def cosine_similarity(a, b):
    # Temsillerin yönsel yakınlığını ölçer.
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

cat = np.array([0.8, 0.2, 0.7])
tiger = np.array([0.9, 0.1, 0.8])
chair = np.array([0.1, 0.9, 0.2])

print(cosine_similarity(cat, tiger))
print(cosine_similarity(cat, chair))
```

Bu kod, modelin gerçek iç yapısını temsil etmez; yalnızca “benzer kavramlar benzer sayısal yönlere sahip olabilir” fikrini görünür kılar.

## Difüzyon modeli neyi hayal ediyor?

Difüzyon modelleri, eğitim görüntülerine aşamalı olarak gürültü eklemeyi ve bu süreci tersine çevirmeyi öğrenir. Üretim sırasında model rastgele gürültüden başlar, metin isteminin rehberliğinde olası bir görüntüye ilerler. Basitleştirilmiş ileri süreç şu şekilde yazılabilir:

$$x_t = \sqrt{\bar{\alpha}_t}x_0 + \sqrt{1-\bar{\alpha}_t}\epsilon$$

Burada $x_0$ özgün görüntü, $\epsilon$ rastgele gürültü, $x_t$ ise belirli bir adımdaki bozulmuş görüntüdür. Modelin görevi, gürültüyü tahmin ederek anlamlı yapıyı yeniden kurmaktır. Dolayısıyla model tuvali insan gibi seyretmez; koşullu olasılık dağılımından örnekleme yapar.

## Sanatçı mı, araç mı, ayna mı?

“Model görüyor mu?” sorusunun yanıtı, görmeyi nasıl tanımladığımıza bağlıdır. Görmek; görsel özellikleri ayırt etmek ve nesneler arasında ilişki kurmaksa model işlevsel anlamda görüyor sayılabilir. Görmek; bedensel deneyim, bilinç, niyet ve dünyayla yaşanmış bağ gerektiriyorsa bugünkü modellerin gördüğünü söylemek zordur.

Yine de onları basit birer fotokopi makinesi saymak da yetersizdir. Modeller öğrendikleri temsilleri yeni bileşimlerde kullanabilir; fakat seçimleri eğitim verisinin kültürel önyargılarını ve insan üreticilerin kararlarını taşır. Belki de yapay zekâ ne bütünüyle sanatçı ne de edilgen bir fırçadır. O, insan kültürünün sayısal bir aynasıdır: Görmeden görüntü üretir, yaşamadan üslup taklit eder ve tam da bu çelişki sayesinde sanatın ne olduğunu yeniden sormamıza yol açar.
