---
layout: post
title: "Makine Öğrenmesi Paradigmaları: Veriden Öğrenmenin Üç Farklı Yolu"
math: true
categories: 
  - Bilgi
tags: 
  - makine öğrenmesi
  - yapay zekâ
  - algoritmalar
---

Makine öğrenmesi, bilgisayarlara her olasılık için ayrı bir kural yazmak yerine örneklerden davranış geliştirme imkânı verir. Ancak “veriden öğrenmek” tek bir yöntemi ifade etmez. Kimi sistemler doğru cevaplarla çalışır, kimileri verinin içindeki gizli yapıyı keşfeder, kimileri ise deneme-yanılma yoluyla ödül toplamayı öğrenir. Denetimli, denetimsiz ve pekiştirmeli öğrenme; yalnızca farklı algoritmalar değil, öğrenmenin doğasına ilişkin üç ayrı felsefi yaklaşımdır.
``

## Öğrenmek ne anlama gelir?

Klasik programlamada insan kuralları ve girdileri verir, bilgisayar sonucu üretir. Makine öğrenmesinde ise girdilerle birlikte örnek sonuçlar veya bir değerlendirme mekanizması sunulur; sistem uygun kuralları kendisi yaklaşık olarak çıkarır.

Bu süreç genellikle bir amaç fonksiyonunun iyileştirilmesidir. Bir modelin parametreleri $\theta$, tahmini $f_\theta(x)$ ve gerçek cevap $y$ olsun. Denetimli öğrenmede hedef çoğunlukla şu kaybı küçültmektir:

$$
\theta^* = \arg\min_\theta \frac{1}{n}\sum_{i=1}^{n} L(f_\theta(x_i), y_i)
$$

Buradaki kritik fikir şudur: Sistem “gerçeği” doğrudan öğrenmez; verilen veri, hedef ve ölçüm yöntemi altında başarılı olan bir temsil öğrenir.

## Üç paradigmanın karşılaştırması

| Paradigma | Öğrenme sinyali | Temel soru | Tipik kullanım |
|---|---|---|---|
| Denetimli | Etiket veya doğru cevap | Bu girdi için sonuç nedir? | Sınıflandırma, regresyon |
| Denetimsiz | Yalnızca ham veri | Bu veride nasıl bir yapı var? | Kümeleme, boyut indirgeme |
| Pekiştirmeli | Ödül ve ceza | Uzun vadede hangi eylem daha iyi? | Robotik, oyunlar, kontrol |

### Denetimli öğrenme: Öğretmenli eğitim

Denetimli öğrenmede veri kümesi $(x_i, y_i)$ çiftlerinden oluşur. Örneğin bir e-postanın özellikleri $x$, “spam” etiketi ise $y$ olabilir. Model, tahminleriyle etiketler arasındaki hatayı azaltır.

Felsefi açıdan bu yaklaşım, bilginin dışarıdan sağlanan doğru örneklerle kazanıldığını varsayar. Güçlüdür; fakat öğretmenin hatalarını da miras alır. Etiketlerde önyargı varsa model bunu şaşırtıcı bir disiplinle öğrenebilir.

```python
from sklearn.linear_model import LogisticRegression

# Özelliklerden ikili sınıf etiketini tahmin eden model
model = LogisticRegression()
model.fit(X_train, y_train)
tahminler = model.predict(X_test)
```

Lojistik regresyon, sınıf olasılığını sigmoid fonksiyonuyla modeller: $\sigma(z)=1/(1+e^{-z})$. Basit görünmesine rağmen metin sınıflandırma ve risk tahmini gibi alanlarda güçlü bir başlangıçtır.

### Denetimsiz öğrenme: Haritasız keşif

Denetimsiz öğrenmede doğru cevap anahtarı yoktur. Algoritma benzerlik, yoğunluk veya istatistiksel bağımlılık gibi ölçütlerle yapılar arar. K-means, noktaları merkezlerine olan kareli uzaklığı küçülterek $k$ kümeye ayırır:

$$
J = \sum_{j=1}^{k}\sum_{x_i \in C_j}\lVert x_i-\mu_j\rVert^2
$$

Burada “doğru küme” mutlak değildir. Müşteriler yaşa göre başka, alışveriş davranışına göre başka biçimde gruplanabilir. Dolayısıyla sonuç, seçilen özelliklerin ve benzerlik tanımının bir yorumudur.

```python
from sklearn.cluster import KMeans

# Etiketsiz müşterileri üç davranış grubuna ayırır
model = KMeans(n_clusters=3, random_state=42)
kume_numaralari = model.fit_predict(musteri_ozellikleri)
```

### Pekiştirmeli öğrenme: Sonuçlardan ders çıkarmak

Pekiştirmeli öğrenmede bir ajan, durum $s$ içinde eylem $a$ seçer; çevre yeni durum ve ödül üretir. Amaç anlık ödülü değil, indirgenmiş toplam getiriyi büyütmektir:

$$
G_t = \sum_{k=0}^{\infty}\gamma^k r_{t+k+1}
$$

$\gamma$, gelecekteki ödüllere verilen önemi belirler. Bu paradigma davranışçı öğrenmeye benzer: Ajan hangi eylemin doğru olduğunu önceden bilmez, sonuçları deneyimler. En büyük ikilem keşif ve sömürüdür; yeni seçenekler mi denenmeli, yoksa bilinen iyi davranış mı tekrarlanmalıdır?

| Özellik | Denetimli | Denetimsiz | Pekiştirmeli |
|---|---|---|---|
| Geri bildirim | Anında ve açık | Doğrudan yok | Gecikmeli olabilir |
| Veri üretimi | Genellikle sabit | Genellikle sabit | Etkileşimle oluşur |
| Başlıca risk | Aşırı öğrenme | Anlamsız desenler | Yanlış ödül tasarımı |

## Hangisi seçilmeli?

Elinizde güvenilir etiketler varsa denetimli öğrenme, yapıyı keşfetmek istiyorsanız denetimsiz öğrenme, ardışık kararlar ve çevresel etkileşim söz konusuysa pekiştirmeli öğrenme uygundur. Gerçek sistemlerde bu sınırlar bulanıktır: Bir robot görüntüleri denetimli öğrenmeyle tanıyabilir, denetimsiz yöntemle temsil çıkarabilir ve hareketlerini pekiştirmeli öğrenmeyle geliştirebilir. Kısacası mesele en havalı algoritmayı seçmek değil, eldeki geri bildirim türünü doğru anlamaktır.
