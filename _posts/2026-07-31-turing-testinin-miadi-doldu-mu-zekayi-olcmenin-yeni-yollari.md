---
layout: post
title: "Turing Testinin Miadı Doldu mu? Zekâyı Ölçmenin Yeni Yolları"
math: true
categories: 
  - Bilgi
tags: 
  - yapay zekâ
  - Turing Testi
  - LLM değerlendirme
---

Bir makineyle yazıştığınızı bilmeden onun insan olduğuna ikna olursanız, karşınızdaki sistem gerçekten zeki midir? Alan Turing’in 1950’de ortaya attığı taklit oyunu, bu soruya davranış üzerinden yaklaşan son derece etkili bir düşünce deneyiydi. Ancak günümüzün büyük dil modelleri akıcı metin üretirken yanlış bilgi uydurabiliyor, basit mantık hataları yapabiliyor ve fiziksel dünyayı deneyimlemiyor. Dolayısıyla artık yalnızca “İnsan gibi konuşuyor mu?” sorusu yeterli görünmüyor.

``

## Turing Testi aslında neyi ölçer?

Turing Testi, zekânın içsel mekanizmasını tanımlamak yerine gözlemlenebilir çıktıya odaklanır. Bir insan değerlendirici, yazılı görüşme yaptığı tarafın makine olduğunu güvenilir biçimde anlayamıyorsa sistem testi geçmiş sayılır. Bu yaklaşımın gücü, “düşünmek” gibi tanımlanması zor bir kavramı ölçülebilir bir oyuna dönüştürmesidir.

Basitleştirilmiş biçimde başarıyı şöyle ifade edebiliriz:

$$T = P(Değerlendiricinin\ makineyi\ insan\ sanması)$$

$T$ yükseldikçe sistemin insanı taklit etme başarısı artar. Fakat yüksek $T$, doğruluk, tutarlılık veya gerçek dünya anlayışı anlamına gelmez. Model; mizah, tereddüt ve gündelik dil kalıplarını kullanarak ikna edici olabilir. Başka bir deyişle test, zekâ ile zekâ performansını birbirine karıştırabilir.

## Bugünün modelleri neden testi zorluyor?

Büyük dil modelleri, çok büyük metin koleksiyonlarından bir sonraki kelime veya belirtecin olasılığını öğrenir. Temel hedef kabaca şöyledir:

$$P(x_t | x_1, x_2, ..., x_{t-1})$$

Bu mekanizma şaşırtıcı derecede yeteneklidir; fakat modelin söylediği her şeyi doğruladığını göstermez. Üstelik kısa bir sohbette kusurlar gizlenebilir. Bilgi kesim tarihi, halüsinasyonlar, uzun görevlerde hedef kaybı ve nedensellik hataları ancak sistematik deneylerle ortaya çıkar.

| Ölçüt | Güçlü yanı | Temel açığı |
|---|---|---|
| Turing Testi | Doğal iletişimi sınar | Taklidi anlayış sanabilir |
| Standart benchmark | Sonuçları karşılaştırmayı kolaylaştırır | Eğitim verisine sızabilir |
| İnsan değerlendirmesi | Nüansı ve yararlılığı yakalar | Pahalı ve öznel olabilir |
| Gerçek görev testi | Pratik başarıyı ölçer | Ortama ve araçlara bağımlıdır |

## Tek puan yerine yetenek profili

Yeni değerlendirme yaklaşımı, zekâyı tek boyutlu bir sayı değil, bir yetenekler vektörü olarak ele almalıdır:

$$Z = (D, M, G, U, E, A)$$

Burada $D$ doğruluk, $M$ muhakeme, $G$ genelleme, $U$ uzun vadeli tutarlılık, $E$ emniyet ve $A$ araç kullanma becerisidir. Böylece çok güzel yazan ama kaynak doğrulayamayan bir model ile daha kısa konuşup güvenilir işlem yapan model aynı kefeye konmaz.

Örneğin küçük bir değerlendirme sistemi, ağırlıklı başarı puanı hesaplayabilir:

```python
scores = {
    "dogruluk": 0.82,
    "muhakeme": 0.74,
    "genelleme": 0.69,
    "emniyet": 0.91
}

weights = {
    "dogruluk": 0.35,
    "muhakeme": 0.30,
    "genelleme": 0.20,
    "emniyet": 0.15
}

total = sum(scores[k] * weights[k] for k in scores)
print(f"Bileşik puan: {total:.2f}")
```

Bu kod, farklı yetenekleri ağırlıklandırarak bileşik bir sonuç üretir. Yine de puanın yanında alt sonuçlar mutlaka gösterilmelidir; çünkü ortalama, kritik bir güvenlik zayıflığını saklayabilir.

## Daha iyi testler nasıl görünmeli?

Geleceğin testleri dinamik olmalı; sorular düzenli yenilenmeli ve internette ezberlenebilir cevaplara dönüşmemelidir. Modelden yalnızca cevap değil, doğrulanabilir kaynak, belirsizlik tahmini ve gerektiğinde “Bilmiyorum” diyebilme becerisi istenmelidir. Uzun süreli görevler, karşıt örnekler, yeni kurallar altında genelleme, kod çalıştırma ve insanlarla iş birliği de değerlendirmeye katılmalıdır.

Turing Testi tamamen değersiz değildir; doğal diyalog kalitesini ölçen tarihsel ve sezgisel bir araç olarak yaşamaya devam edebilir. Fakat artık zekânın final sınavı değil, kapsamlı bir değerlendirme paketindeki eğlenceli sorulardan biridir. Günümüzün asıl meselesi makinenin insan rolünü ne kadar iyi oynadığı değil; ne kadar doğru, uyarlanabilir, şeffaf ve güvenli biçimde iş yaptığıdır.
