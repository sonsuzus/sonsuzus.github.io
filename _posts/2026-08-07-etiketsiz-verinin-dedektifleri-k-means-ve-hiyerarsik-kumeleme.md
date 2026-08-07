---
layout: post
title: "Etiketsiz Verinin Dedektifleri: K-Means ve Hiyerarşik Kümeleme"
math: true
categories: 
  - Bilgi
tags: 
  - denetimsiz öğrenme
  - K-Means
  - hiyerarşik kümeleme
---

Bir veri kümesinde hangi kayıtların birbirine benzediğini biliyor, fakat onları açıklayan hazır etiketlere sahip olmuyoruz. İşte denetimsiz öğrenme tam bu noktada sahneye çıkar: Veriye “Bunlar hangi sınıfa ait?” diye sormak yerine, “Burada kendiliğinden oluşan nasıl bir yapı var?” diye bakar. Müşteri segmentasyonu, belge gruplama, anomali keşfi ve biyolojik veri analizi bu yaklaşımın yaygın kullanım alanlarıdır.
``

## Denetimsiz öğrenmenin temel mantığı

Denetimli öğrenmede modele hem özellikler hem de doğru cevaplar verilir. Denetimsiz öğrenmede ise yalnızca $X = \{x_1, x_2, ..., x_n\}$ gözlemleri bulunur. Algoritma, gözlemler arasındaki uzaklık veya benzerlik ilişkilerinden yararlanarak gizli yapıyı keşfetmeye çalışır.

| Özellik | Denetimli öğrenme | Denetimsiz öğrenme |
|---|---|---|
| Etiket | Vardır | Yoktur |
| Temel amaç | Tahmin yapmak | Yapı keşfetmek |
| Örnek görev | Spam sınıflandırma | Müşteri segmentasyonu |
| Değerlendirme | Accuracy, F1 | Silhouette, küme içi varyans |

Kümelemenin kalbi benzerlik ölçümüdür. Sayısal verilerde sık kullanılan Öklid uzaklığı iki nokta için şöyle hesaplanır:

$$d(x,y)=\sqrt{\sum_{j=1}^{m}(x_j-y_j)^2}$$

Ölçekler farklıysa uzaklık yanıltıcı olabilir. Örneğin yaş 18–70, gelir ise binlerce birim aralığındaysa gelir özelliği hesaplamayı domine eder. Bu nedenle standardizasyon çoğu zaman zorunludur.

## K-Means: Merkezlerin etrafında toplanmak

K-Means, veriyi önceden belirlenen $K$ adet kümeye ayırır. Önce rastgele merkezler seçer, her noktayı en yakın merkeze atar, ardından merkezleri yeniden hesaplar. Atamalar değişmeyene kadar bu döngü sürer.

Amaç fonksiyonu, noktaların kendi küme merkezlerine uzaklıklarının karelerini küçültmektir:

$$J=\sum_{k=1}^{K}\sum_{x_i \in C_k}\lVert x_i-\mu_k\rVert^2$$

Aşağıdaki örnek müşterileri yıllık gelir ve harcama puanına göre gruplar:

```python
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

X = customers[['annual_income', 'spending_score']]
X_scaled = StandardScaler().fit_transform(X)

model = KMeans(n_clusters=3, random_state=42, n_init=10)
customers['cluster'] = model.fit_predict(X_scaled)

print(model.cluster_centers_)
```

`StandardScaler`, özellikleri karşılaştırılabilir ölçeğe getirir. `fit_predict` modeli eğitir ve her müşteriye bir küme numarası atar. Ancak bu numaralar sıralama ifade etmez; “küme 2”, “küme 1”den daha iyi değildir.

Doğru $K$ değerini seçmek için dirsek yöntemi veya Silhouette skoru kullanılabilir. Silhouette değeri $-1$ ile $1$ arasındadır; değerin $1$’e yaklaşması, kümelerin daha belirgin ayrıldığını gösterir.

## Hiyerarşik kümeleme: Verinin aile ağacı

Hiyerarşik kümeleme, kümelerin iç içe geçmiş ilişkilerini bir dendrogram üzerinde gösterir. Birleştirici yaklaşımda her gözlem başlangıçta ayrı bir kümedir; en yakın kümeler adım adım birleşir. Bölücü yaklaşım ise tüm veriyi tek kümeden başlayarak parçalar.

```python
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt

Z = linkage(X_scaled, method='ward')
dendrogram(Z)
plt.ylabel('Birleşme uzaklığı')
plt.show()
```

Ward yöntemi, birleşmeler sonucunda oluşan küme içi varyans artışını düşük tutmaya çalışır. Dendrogramın uzun dikey boşluklarından yatay kesilmesi, makul küme sayıları hakkında görsel ipucu verir.

| Ölçüt | K-Means | Hiyerarşik kümeleme |
|---|---|---|
| Küme sayısı | Başta belirtilir | Sonradan seçilebilir |
| Çıktı | Düz küme etiketleri | Dendrogram ve etiketler |
| Hız | Büyük veride genellikle hızlı | Büyük veride maliyetli |
| Küme şekli | Küresel kümelerde başarılı | Bağlantı yöntemine bağlı |
| Aykırı değer | Hassas | Yönteme göre hassas |

## Hangisini seçmeliyiz?

Büyük, sayısal ve yaklaşık küresel gruplara sahip verilerde K-Means iyi bir başlangıçtır. Küme sayısı bilinmiyorsa veya gruplar arasındaki soy ağacı benzeri ilişki incelenecekse hiyerarşik kümeleme daha açıklayıcıdır. Yine de sonuçlar mutlak gerçek olarak görülmemelidir. Özellik seçimi, ölçekleme, uzaklık metriği ve alan bilgisi değiştiğinde kümeler de değişebilir. Denetimsiz öğrenme sihirli bir etiket makinesi değil; verinin fısıltılarını duyulur hâle getiren güçlü bir keşif aracıdır.
