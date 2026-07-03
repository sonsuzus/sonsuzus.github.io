---
layout: post
title: Yapay Zeka İncelemesi
math: false
excerpt_separator: "<!--more-->"
categories:
  - Program
tags:
  - yapay-zeka
  - makine-öğrenmesi
  - derin-öğrenme
  - sinir-ağı
  - llm
  - transformers
  - prompt
  - eğitim
  - overfitting
  - gradient-descent
  - programlama
  - algoritma
  - veri
  - felsefe
  - teknoloji
---

Yapay zeka, makinelerin insana özgü sanılan davranışları — öğrenme, akıl yürütme, örüntü tanıma — sergilemesini sağlayan bir disiplindir. Ama dikkat: bu bir tanım değil, bir davettir. Asıl soru şu: *özgü* kelimesini ne zamana kadar kullanabileceğiz?

<!--more-->

---

## Temel Kavramlar

### Yapay Zeka Nedir — Ne Değildir?

Yapay zeka (YZ), geniş anlamda makinelerin **akıllıca görünen** kararlar almasını sağlayan her türlü tekniği kapsar. Dar anlamda ise bugün çoğunlukla **istatistiksel örüntü eşleştirme** demektir.

> Bir YZ sistemi "anlamıyor". Veriyle örüntü öğreniyor. Anlam ile örüntü arasındaki mesafe, alanın en büyük tartışmasıdır.

Popüler ayrım:

| Tür | Açıklama | Örnek |
|---|---|---|
| **Dar YZ** | Tek bir görevi iyi yapar | Satranç motoru, spam filtresi |
| **Genel YZ (AGI)** | İnsan gibi genelleşebilir | Henüz yok |
| **Süper YZ** | İnsanı her alanda geçer | Spekülatif |

---

### Makine Öğrenmesi

Klasik programlamada kuralları **insan** yazar; makine öğrenmesinde (ML) kuralları **veriden** çıkarırsın.

```
Klasik : Veri + Kurallar → Çıktı
ML     : Veri + Çıktı   → Kurallar
```

Üç ana öğrenme paradigması:

- **Gözetimli öğrenme** — Etiketli veri. "Bu kedi, bu değil." Model doğru etiketi tahmin etmeyi öğrenir.
- **Gözetimsiz öğrenme** — Etiketsiz veri. Model kendi başına küme ve yapı arar.
- **Pekiştirmeli öğrenme** — Ödül/ceza sinyali. Satranç oynayan, oyun kazanmayı öğrenen ajan bu yoldan yetişir.

---

### Gradient Descent — Modelin Yanılgıdan Öğrenmesi

Model bir tahmin yapar, tahmin yanlışsa **hata** hesaplanır; hata küçültülecek şekilde model parametreleri güncellenir. Bu döngü milyonlarca kez tekrarlanır.

Görsel olarak: düz olmayan bir arazide gözleri bağlı birinin vadiye inmesi. Her adımda "hangi yöne eğim var?" sorusunu sorar, o yönde küçük bir adım atar.

```
kayıp = tahmin ile gerçek arasındaki fark
gradyan = bu kaybın parametrelere göre türevi
güncelleme = parametre - öğrenme_hızı × gradyan
```

> **Öğrenme hızı** çok büyük olursa vadi atlanır; çok küçük olursa yüzyıllar sürer.

---

### Overfitting — Ezbercinin Trajedisi

Model eğitim verisini çok iyi öğrenirse **test verisinde berbat** sonuç verir. Sınav sorularını değil, tam o soruların cevaplarını ezberleyen öğrenci gibi.

| Durum | Eğitim | Test |
|---|---|---|
| Underfitting | Kötü | Kötü |
| İyi model | İyi | İyi |
| Overfitting | Mükemmel | Kötü |

Çözümler: daha fazla veri, dropout, regularization, erken durdurma.

---

### Sinir Ağları ve Derin Öğrenme

Sinir ağları, birden fazla katmanla hiyerarşik özellik öğrenir. İlk katmanlar kenar ve doku öğrenirken, derin katmanlar "kedi kulağı" gibi soyut kavramları öğrenir.

**Derin öğrenme**, çok katmanlı sinir ağlarından başka bir şey değildir — ama bu "başka bir şey değil" cümlesi, son 15 yılın bütün devrimini küçümsemek olur.

---

### Transformer Mimarisi ve Büyük Dil Modelleri

2017'de yayımlanan *"Attention Is All You Need"* makalesi mimarisi değiştirdi. **Transformer**, metindeki her kelimenin diğer tüm kelimelerle ilişkisini paralel hesaplar — sıra takip etmez, bağlamı bir bütün olarak kavrar.

Büyük Dil Modelleri (LLM), bu mimari üstüne trilyonlarca kelimeyle eğitilir. Sonuç: "bir sonraki kelimeyi tahmin et" gibi basit bir görevden, kod yazan, şiir kuran, argüman üreten sistemler çıkar.

> Bir LLM'in "anlayıp anlamadığı" sorusu hâlâ açıktır. Ama bu soruyu sormak zorunda hissettiriyorsa, o da küçük bir mucizedir.

---

### Prompt Mühendisliği

LLM'lere verilen giriş metnine **prompt** denir. İyi bir prompt, modeli doğru çıktıya yönlendiren bir kaldıraçtır.

Temel teknikler:

- **Zero-shot** — Hiç örnek vermeden doğrudan sormak.
- **Few-shot** — 2–3 örnek gösterip aynı formatı istemek.
- **Chain-of-thought** — "Adım adım düşün" diyerek mantık zinciri kurmak.
- **Role prompting** — "Sen bir uzman fizikçisin" diyerek bağlam vermek.

---

## Kısa Sözlük

| Terim | Ne demek? |
|---|---|
| **Parametre** | Modelin öğrendiği sayısal ağırlıklar |
| **Epoch** | Eğitim verisinin baştan sona bir kez işlenmesi |
| **Batch** | Her adımda modele gösterilen örnek grubu |
| **Token** | LLM'lerin işlediği temel metin birimi (kelime veya hece) |
| **Embedding** | Kelimelerin sayı vektörlerine dönüştürülmesi |
| **Fine-tuning** | Önceden eğitilmiş modeli yeni görev için ince ayar yapmak |
| **Hallucination** | Modelin kendinden emin ama yanlış bilgi üretmesi |

---

## Bir Adım Geri

Yapay zeka bir araçtır — çekiç kadar tarafsız, kullanıcısı kadar niyetli. Ondan korkmak ne kadar anlamsızsa, ona körce güvenmek de o kadar tehlikelidir. En sağlıklı yaklaşım şu olabilir: nasıl çalıştığını yeterince anlamak ki ne yapamayacağını da bilesin.

> Satranç tahtasında her taşın değerini bilmek oyunu kazandırmaz — ama bilmemek kesinlikle kaybettirir.

---

> **Kaynak:** Bu yazı; *Deep Learning* (Goodfellow vd.), *Attention Is All You Need* (Vaswani vd., 2017) ve çeşitli birincil araştırma makalelerinden derlenerek özgün olarak yazılmıştır.
