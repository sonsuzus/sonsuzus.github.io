---
layout: post
title: "Transformer Mimarisi: Attention ile Kelimeler Arasındaki Görünmez Bağları Yakalamak"
math: true
categories: 
  - Bilgi
tags: 
  - transformer
  - attention
  - yapay zeka
---

Bir cümleyi anlamak, kelimeleri soldan sağa doğru ezberlemekten çok daha fazlasıdır. Örneğin “Robot, masadaki kitabı aldı çünkü onu merak etti” cümlesindeki “onu” sözcüğünün kitabı işaret ettiğini bağlam sayesinde anlarız. Transformer mimarisi de benzer biçimde çalışır: Cümledeki kelimelerin birbirleriyle ilişkilerini aynı anda inceler ve hangilerinin daha önemli olduğuna karar verir.

``

## Transformer’dan Önce Ne Vardı?

Doğal dil işlemede uzun süre RNN ve LSTM gibi tekrarlayan sinir ağları kullanıldı. Bu modeller metni sırayla işler: İkinci kelime için birincinin, üçüncü kelime için ilk ikisinin işlenmesini beklemek gerekir. Bu bağımlılık paralel hesaplamayı zorlaştırır ve uzun cümlelerin başındaki bilgilerin unutulmasına yol açabilir.

Transformer ise eğitim sırasında dizideki bütün konumları paralel olarak ele alır. Böylece hem modern GPU’lardan daha iyi yararlanır hem de birbirinden uzaktaki kelimeler arasında doğrudan bağlantı kurar. Ancak önemli bir ayrıntı var: GPT benzeri otoregresif modeller, metin üretirken sonraki token önceki tokenlara bağlı olduğu için çıkarım aşamasında hâlâ adım adım ilerler.

| Özellik | RNN / LSTM | Transformer |
|---|---|---|
| Veri işleme | Sıralı | Eğitimde büyük ölçüde paralel |
| Uzak ilişkiler | Yakalamak zor olabilir | Doğrudan attention ile yakalanır |
| Eğitim hızı | Görece düşük | Yüksek paralellik sayesinde hızlı |
| Temel bellek | Gizli durum | Attention ağırlıkları ve temsiller |
| Uzun dizi maliyeti | Zaman adımı sayısıyla büyür | Standart attention’da karesel büyür |

## Attention’ın Üç Kahramanı: Query, Key ve Value

Self-attention mekanizmasında her token için üç vektör üretilir:

- **Query (Q):** Tokenın ne aradığını temsil eder.
- **Key (K):** Tokenın hangi bilgiyi sunduğunu belirtir.
- **Value (V):** Eşleşme gerçekleştiğinde aktarılacak bilgidir.

Bir query ile bütün key vektörlerinin benzerliği hesaplanır. Sonuçlar ölçeklenir, `softmax` ile olasılık benzeri ağırlıklara dönüştürülür ve value vektörleri bu ağırlıklarla birleştirilir:

$$\text{Attention}(Q,K,V)=\text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$

Buradaki $d_k$, key vektörlerinin boyutudur. $\sqrt{d_k}$ ile bölme işlemi, büyük boyutlarda noktasal çarpımların aşırı büyümesini ve softmax fonksiyonunun dengesizleşmesini önler. Kısacası model, “Bu kelimeyi anlamak için diğer kelimelere ne kadar bakmalıyım?” sorusuna sayısal bir cevap verir.

## Neden Birden Fazla Dikkat Başı Var?

Tek bir attention işlemi yalnızca belirli bir ilişki türüne odaklanabilir. **Multi-head attention**, farklı temsil uzaylarında birden fazla attention hesabını paralel yürütür. Bir baş özne-yüklem ilişkisini, başka biri zamirlerin referansını, diğeri ise anlamsal yakınlığı öğrenebilir.

$$\text{MultiHead}(Q,K,V)=\text{Concat}(head_1,\ldots,head_h)W^O$$

Bu yapı, aynı cümleye farklı büyüteçlerle bakmak gibidir. Transformer katmanlarında attention sonrasında ileri beslemeli ağ, residual bağlantılar ve katman normalizasyonu da bulunur. Böylece bilgiler yalnızca seçilmez; dönüştürülür ve kararlı biçimde sonraki katmana aktarılır.

## Kelime Sırası Nasıl Biliniyor?

Transformer kelimeleri aynı anda işlediği için sıra bilgisini kendiliğinden algılayamaz. Bu nedenle token temsillerine **positional encoding** eklenir. Klasik yaklaşım sinüs ve kosinüs fonksiyonlarını kullanır:

$$PE(pos,2i)=\sin\left(pos/10000^{2i/d}\right)$$

$$PE(pos,2i+1)=\cos\left(pos/10000^{2i/d}\right)$$

Böylece “köpek adamı ısırdı” ile “adam köpeği ısırdı” aynı kelimeleri içerse bile farklı anlamlara sahip olur.

## Basitleştirilmiş Attention Kodu

Aşağıdaki PyTorch fonksiyonu, scaled dot-product attention hesabını gerçekleştirir:

```python
import torch
import math

def attention(query, key, value, mask=None):
    d_k = query.size(-1)
    scores = query @ key.transpose(-2, -1)
    scores = scores / math.sqrt(d_k)

    if mask is not None:
        scores = scores.masked_fill(mask == 0, float("-inf"))

    weights = torch.softmax(scores, dim=-1)
    output = weights @ value
    return output, weights
```

`mask`, modelin dolgu tokenlarını görmesini veya gelecekteki kelimelere bakmasını engeller. Döndürülen `weights` ise hangi tokenın hangisine ne ölçüde dikkat ettiğini incelemeyi sağlar.

## Güçlü Ama Bedelsiz Değil

Standart self-attention’ın zaman ve bellek maliyeti dizi uzunluğuna göre yaklaşık $O(n^2)$ seviyesindedir. Bu nedenle çok uzun belgeler pahalı olabilir. Sparse attention, FlashAttention ve pencere tabanlı yaklaşımlar bu yükü azaltmayı hedefler.

Yine de Transformer; çeviri, metin üretimi, görüntü işleme ve protein analizi gibi alanlarda ortak bir temel oluşturdu. Devrimin özü basit ama güçlüdür: Her kelimeyi tek başına değil, diğer bütün kelimelerle kurduğu ilişkiler üzerinden anlamlandırmak.
