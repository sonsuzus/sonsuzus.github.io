---
layout: post
title: "Kelimeleri Sayılardan Anlama: NLP ve Word Embeddings Rehberi"
math: true
categories: 
  - Bilgi
tags: 
  - NLP
  - Word2Vec
  - GloVe
---

İnsanlar için “kedi”, “köpek” ve “uçak” kelimelerini ayırmak kolaydır: İlk ikisi hayvandır, üçüncüsü ise gökyüzünde dolaşan metal bir araçtır. Bilgisayar açısından bakıldığındayse hepsi yalnızca karakter dizileridir. Doğal Dil İşleme (NLP), bu karakterlerin ardındaki anlamı makinelerin işleyebileceği matematiksel temsillere dönüştürür. Kelime gömme yöntemleri de tam burada devreye girerek kelimelere sayısal birer kimlik değil, anlamsal birer koordinat kazandırır.
``

## Bilgisayar kelimeleri nasıl görür?

En temel yaklaşım, her kelimeyi sözlükteki konumuna göre temsil eden **one-hot encoding** yöntemidir. Örneğin sözlüğümüzde üç kelime varsa “kedi” şu şekilde gösterilebilir:

$$kedi = [1, 0, 0]$$

“köpek” ise:

$$köpek = [0, 1, 0]$$

Bu vektörler farklı kelimeleri ayırır ancak aralarındaki anlam ilişkisini taşımaz. Matematiksel olarak “kedi” ile “köpek”, “kedi” ile “uçak” kadar uzaktır. Ayrıca sözlük yüz binlerce kelime içeriyorsa vektörler gereksiz derecede büyük ve seyrek olur.

Word embeddings, her kelimeyi genellikle 50–300 boyutlu yoğun bir vektörle temsil eder. Eğitim sırasında benzer bağlamlarda kullanılan kelimeler vektör uzayında birbirine yaklaşır. Bu fikir, dağılımsal anlambilimin meşhur özetine dayanır: **Bir kelimeyi, birlikte bulunduğu kelimelerden tanırsın.**

| Özellik | One-hot | Word Embedding |
|---|---|---|
| Boyut | Sözlük büyüklüğü | Sabit ve daha küçük |
| Yapı | Seyrek | Yoğun |
| Anlamsal ilişki | Yok | Var |
| Öğrenilebilirlik | Sabit temsil | Veriden öğrenilir |

## Word2Vec: Komşuna bak, kelimeyi tanı

Word2Vec, kelimelerin yakın çevresinden yararlanır ve iki temel mimari sunar:

- **CBOW**, çevredeki kelimelerden merkezdeki kelimeyi tahmin eder.
- **Skip-gram**, merkez kelimeden çevredeki kelimeleri tahmin eder.

“Minik kedi koltukta uyudu” cümlesinde CBOW, “minik” ve “koltukta” kelimelerinden “kedi”yi bulmaya çalışabilir. Skip-gram ise “kedi” verildiğinde çevresindeki sözcükleri tahmin eder. Büyük veri kümelerinde Skip-gram, nadir kelimeleri öğrenmekte çoğu zaman daha başarılıdır.

İki vektörün anlamsal yakınlığı sıklıkla kosinüs benzerliğiyle ölçülür:

$$cos(\theta) = \frac{A \cdot B}{||A||\,||B||}$$

Sonuç 1’e yaklaştıkça yönler ve dolayısıyla anlamlar daha benzerdir. Ünlü vektör aritmetiği örneği de şöyledir:

$$kral - erkek + kadın \approx kraliçe$$

## GloVe: Büyük resmin istatistiği

**GloVe**, yalnızca yerel kelime pencerelerine odaklanmak yerine bütün metindeki ortak görülme sayılarını kullanır. Bir kelimenin başka kelimelerle kaç kez yan yana geldiğini içeren eş-oluşum matrisi oluşturulur. Model, bu küresel istatistikleri düşük boyutlu vektörlere sıkıştırır.

| Yöntem | Temel bilgi kaynağı | Güçlü yanı |
|---|---|---|
| Word2Vec | Yerel bağlam pencereleri | Hızlı ve sezgisel eğitim |
| GloVe | Küresel eş-oluşum istatistikleri | Genel dağılımı iyi yakalama |

## Python ile hazır vektörleri kullanmak

Aşağıdaki örnek, Gensim üzerinden hazır GloVe vektörlerini yükler ve “computer” kelimesine yakın sözcükleri getirir:

```python
import gensim.downloader as api

# Önceden eğitilmiş 50 boyutlu GloVe modelini indirir.
model = api.load("glove-wiki-gigaword-50")

# Vektör uzayındaki en yakın kelimeleri listeler.
for word, score in model.most_similar("computer", topn=5):
    print(word, round(score, 3))
```

Model, “software” veya “computers” gibi sözcükleri yüksek benzerlik puanlarıyla döndürebilir. Ancak klasik Word2Vec ve GloVe modellerinde her kelimenin yalnızca tek vektörü vardır. Bu nedenle “yüz” kelimesinin insan yüzü ve sayı anlamları bağlama göre ayrılamaz. BERT gibi bağlamsal modeller bu sınırlamayı giderse de kelime gömmeler; arama, öneri sistemleri, duygu analizi ve metin sınıflandırma projelerinde hâlâ hızlı, öğretici ve güçlü bir başlangıç noktasıdır.
