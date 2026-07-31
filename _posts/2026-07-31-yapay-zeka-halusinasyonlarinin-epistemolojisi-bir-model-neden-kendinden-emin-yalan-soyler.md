---
layout: post
title: "Yapay Zekâ Halüsinasyonlarının Epistemolojisi: Bir Model Neden Kendinden Emin Yalan Söyler?"
math: true
categories: 
  - Bilgi
tags: 
  - yapay zekâ
  - halüsinasyon
  - epistemoloji
---

Bir dil modeline az bilinen bir kitabın özetini sorduğunuzu düşünün. Model; yazarın niyetinden, karakterlerin çatışmalarından ve hatta hiç var olmamış bir bölümden büyük bir rahatlıkla bahsedebilir. Cümleleri düzgün, tonu kararlı, ayrıntıları ikna edicidir. Tek sorun, anlattıklarının uydurma olmasıdır. Bu davranış çoğu zaman “kendinden emin yalan söylemek” diye tanımlansa da mesele ahlaki değil, epistemolojiktir: Modelin doğruyu bilmesiyle doğru görünen bir cümle üretmesi aynı şey değildir.

``

## Bilgi, inanç ve güven aynı şey mi?

Klasik epistemolojide bilgi çoğunlukla “gerekçelendirilmiş doğru inanç” yaklaşımıyla tartışılır. Basitleştirilmiş biçimiyle:

$$Bilgi = İnanç + Doğruluk + Gerekçelendirme$$

Bir insan “Ankara Türkiye’nin başkentidir” dediğinde bu önermeye inanabilir, doğruluğunu sınayabilir ve tarihsel ya da kurumsal gerekçeler sunabilir. Dil modeli ise insan anlamında inanmaz. Eğitim verilerindeki örüntülerden hareketle sıradaki kelimeyi, daha doğrusu tokenı, tahmin eder:

$$P(t_i \mid t_1, t_2, \ldots, t_{i-1})$$

Buradaki yüksek olasılık, cümlenin dünyada doğru olduğunu değil, önceki metne göre uygun göründüğünü belirtir. Modelin “Paris, Fransa’nın başkentidir” demesi de hayalî bir akademik makaleye DOI numarası üretmesi de aynı temel mekanizmanın sonucudur: olası tokenları ardışık biçimde seçmek.

| Kavram | İnsan açısından | Dil modeli açısından |
|---|---|---|
| Bilgi | Doğru ve gerekçeli kabul | Parametrelerde temsil edilen örüntü |
| Güven | Öznel eminlik derecesi | Olasılık dağılımı veya dilsel üslup |
| Gerekçe | Kanıt, deneyim, kaynak | İstendiğinde üretilen açıklama metni |
| Yanlışlık | Hatalı inanç veya aldatma | Gerçeklikle uyuşmayan çıktı |

Tablodaki kritik ayrıntı şudur: Modelin sunduğu gerekçe, cevabı doğuran gerçek bir muhakeme kaydı olmak zorunda değildir. Bazen yalnızca cevaptan sonra üretilmiş, kulağa makul gelen başka bir metindir.

## Halüsinasyon neden ortaya çıkar?

Modelin temel hedefi çoğunlukla “doğru bilgi ver” değil, “bağlama uygun devam üret” biçiminde kuruludur. Eğitim verileri eksik, çelişkili veya güncelliğini yitirmiş olabilir. Kullanıcının sorusu yanlış bir öncül içerdiğinde model, öncülü reddetmek yerine konuşmayı sürdürmeyi seçebilir. Ayrıca yardımcı görünmeye yönelik ince ayar, “bilmiyorum” demek yerine boşlukları doldurma eğilimini artırabilir.

Burada sıcaklık gibi üretim ayarları da rol oynar. Sıcaklık yükseldikçe dağılım düzleşir ve daha çeşitli seçimler mümkün olur:

$$P_i' = \frac{e^{z_i/T}}{\sum_j e^{z_j/T}}$$

Ancak düşük sıcaklık doğruluk garantisi değildir. Model, en yüksek olasılıklı yanlış cevabı son derece tutarlı biçimde tekrarlayabilir. Yani kararlılık, hakikat değildir.

## Güven nasıl yanıltır?

İnsanlar akıcı anlatımı uzmanlıkla ilişkilendirmeye eğilimlidir. “Kesinlikle”, “bilindiği üzere” veya “araştırmalar göstermektedir” gibi ifadeler epistemik güven izlenimi yaratır. Oysa modelin dilsel özgüveni ile cevabın doğruluk olasılığı kalibre edilmemiş olabilir.

Basit bir kalibrasyon kontrolü şöyle uygulanabilir:

```python
predictions = [
    {"confidence": 0.9, "correct": 1},
    {"confidence": 0.9, "correct": 0},
    {"confidence": 0.6, "correct": 1},
    {"confidence": 0.6, "correct": 0},
]

for level in {p["confidence"] for p in predictions}:
    group = [p for p in predictions if p["confidence"] == level]
    accuracy = sum(p["correct"] for p in group) / len(group)
    print(f"Beyan edilen güven: {level:.0%}, gerçek başarı: {accuracy:.0%}")
```

Bu kod, aynı güven seviyesindeki cevapları gruplandırıp gerçek doğruluk oranıyla karşılaştırır. Model yüzde 90 güven bildirdiği cevaplarda yalnızca yüzde 50 başarılıysa güveni kötü kalibre edilmiştir.

## “Yalan” sözcüğüne dikkat

Yalan, genellikle kişinin yanlış olduğunu bildiği bir önermeyi aldatma niyetiyle söylemesini gerektirir. Günümüz dil modellerinde niyet, bilinç ve inanç bulunduğunu varsaymak için yeterli kanıt yoktur. Bu nedenle “kendinden emin yalan” etkileyici bir mecazdır; teknik olarak daha doğru ifade, “yüksek güven izlenimi veren temelsiz üretim” olabilir.

Pratik çözüm, modeli susturmak değil çıktıyı sınanabilir hâle getirmektir. Kaynak istemek, kaynakları gerçekten açmak, belirsizlik beyanı talep etmek, güncel veriler için arama araçları kullanmak ve kritik kararları insan denetimine bırakmak gerekir. Çünkü akıcılık bir sunum özelliğidir; bilgi ise gerçeklikle kurulmuş, doğrulanabilir bir ilişkidir.
