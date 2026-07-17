---
layout: post
title: "Python ile Matematiksel Ağırlıklı Otomatik Makale Özetleyici"
math: true
categories: 
  - Proje
tags: 
  - Python
  - Doğal Dil İşleme
  - Otomatik Özetleme
---

Uzun bir makaleyi okumadan önce “bana özü ver” demek, modern yazılımcının kahve istemesi kadar doğal hale geldi. Python ile geliştireceğimiz otomatik özetleyici, metindeki cümleleri matematiksel olarak puanlayıp en önemli olanları seçer. Yani modelimiz metni yeniden yazmaz; metnin içinden en temsilî cümleleri avlar. Bu yönteme çıkarımsal özetleme denir ve haberlerden akademik yazılara kadar birçok alanda oldukça kullanışlıdır.

``

## Fikir: Her Cümle Bir Adaydır

Bir makaleyi cümlelere böldüğümüzde aslında elimizde küçük aday özet parçaları oluşur. Amacımız, her cümleye bir önem puanı vermektir. Bu puan; kelime sıklığı, cümlenin konumu ve metnin genel temasına benzerliği gibi sinyallerden oluşabilir.

Basit bir ağırlık formülü şöyle düşünülebilir:

$score(s)=0.5 \times freq(s)+0.3 \times sim(s)+0.2 \times pos(s)$

Burada $freq(s)$ cümlede geçen önemli kelimelerin toplam ağırlığıdır. $sim(s)$ cümlenin tüm belge vektörüne benzerliğini, $pos(s)$ ise cümlenin metindeki stratejik konumunu temsil eder. Örneğin giriş ve sonuç bölümlerindeki cümleler çoğu zaman daha bilgilendiricidir.

| Özellik | Ne Ölçer? | Neden Önemli? |
|---|---|---|
| Kelime sıklığı | Anahtar kelimelerin yoğunluğu | Konunun merkezini yakalar |
| Kosinüs benzerliği | Cümle ile belge arasındaki yakınlık | Temsil gücünü ölçer |
| Konum puanı | Cümlenin metindeki yeri | Giriş/sonuç etkisini hesaba katar |

## Teorik Altyapı: TF-IDF ve Kosinüs Benzerliği

Kelime saymak tek başına yeterli değildir. “ve”, “bir”, “ile” gibi kelimeler çok geçer ama anlam taşıma güçleri düşüktür. Bu yüzden TF-IDF kullanırız. TF, bir kelimenin cümlede ne kadar sık geçtiğini; IDF ise o kelimenin tüm cümleler arasında ne kadar ayırt edici olduğunu gösterir.

Matematiksel olarak:

$tfidf(t,d)=tf(t,d) \times idf(t)$

Bir cümleyi ve tüm belgeyi vektör olarak düşündüğümüzde, aralarındaki açı bize benzerliği verir:

$cos(\theta)=\frac{A \cdot B}{\|A\|\|B\|}$

Açı küçüldükçe benzerlik artar. Yani cümle, makalenin genel fikrine yaklaşıyorsa özet için güçlü bir adaydır.

## Python ile Orta Seviye Bir Uygulama

Aşağıdaki kod, metni cümlelere ayırır, TF-IDF matrisi üretir, her cümleyi belge ortalamasıyla karşılaştırır ve en yüksek puanlı cümleleri seçer.

```python
import re
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

STOPWORDS = {'ve', 'ile', 'bir', 'bu', 'da', 'de', 'için', 'gibi', 'çok', 'ama'}

def split_sentences(text):
    sentences = re.split(r'(?<=[.!?]) +', text.strip())
    return [s for s in sentences if len(s.split()) > 4]

def clean(sentence):
    sentence = sentence.lower()
    sentence = re.sub(r'[^a-zA-ZçğıöşüÇĞİÖŞÜ0-9 ]', ' ', sentence)
    words = [w for w in sentence.split() if w not in STOPWORDS]
    return ' '.join(words)

def summarize(text, ratio=0.3):
    sentences = split_sentences(text)
    cleaned = [clean(s) for s in sentences]

    vectorizer = TfidfVectorizer()
    matrix = vectorizer.fit_transform(cleaned)

    document_vector = matrix.mean(axis=0)
    similarities = cosine_similarity(matrix, document_vector)

    scores = []
    n = len(sentences)
    for i, sim in enumerate(similarities.flatten()):
        position_score = 1 - (i / max(n - 1, 1)) * 0.3
        final_score = 0.8 * sim + 0.2 * position_score
        scores.append((i, final_score))

    count = max(1, int(n * ratio))
    selected = sorted(scores, key=lambda x: x[1], reverse=True)[:count]
    selected_indexes = sorted(i for i, score in selected)

    return ' '.join(sentences[i] for i in selected_indexes)
```

Kodda `TfidfVectorizer`, her cümleyi sayısal bir vektöre dönüştürür. `document_vector`, bütün metnin ortalama anlam merkezidir. Her cümle bu merkeze ne kadar yakınsa, `cosine_similarity` sonucu o kadar yüksek çıkar. Son olarak, skorlar büyükten küçüğe sıralanır; seçilen cümleler orijinal sırasına göre birleştirilir. Böylece özet, hem anlamlı hem de okunabilir kalır.

## Çıkarımsal ve Soyutlayıcı Özetleme

| Yaklaşım | Nasıl Çalışır? | Avantaj | Dezavantaj |
|---|---|---|---|
| Çıkarımsal | Metinden cümle seçer | Hızlı ve güvenilir | Yeni cümle kuramaz |
| Soyutlayıcı | Metni yeniden yazar | İnsan gibi özetler | Daha maliyetli ve riskli |

Bu projede çıkarımsal yöntemi seçmemizin sebebi, daha anlaşılır ve kontrol edilebilir olmasıdır. Özellikle ilk NLP projeleri için harika bir başlangıçtır.

## Geliştirme Fikirleri

Bu aracı daha akıllı hale getirmek için Türkçe kök bulma, özel isim tanıma veya başlık ağırlığı eklenebilir. Ayrıca `sentence-transformers` gibi modellerle cümleleri bağlamsal vektörlere çevirerek daha güçlü benzerlik hesapları yapılabilir.

Sonuç olarak, otomatik özetleme sadece “kısaltma” işi değildir; metnin matematiksel haritasını çıkarma sanatıdır. Python ise bu haritayı çizmek için oldukça eğlenceli bir pusula sunar.
