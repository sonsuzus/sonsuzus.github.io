---
layout: post
title: "Denetimli Öğrenme Arenası: k-NN, Karar Ağaçları ve SVM"
math: true
categories: 
  - Bilgi
tags: 
  - makine öğrenmesi
  - sınıflandırma
  - python
---

Bir e-postanın spam olup olmadığını, bir müşterinin aboneliğini iptal edip etmeyeceğini veya bir tümörün iyi huylu olup olmadığını tahmin etmek istediğimizi düşünelim. Geçmiş örneklerin doğru cevapları elimizdeyse denetimli öğrenmenin kapısından içeri gireriz. Bu yaklaşımda algoritma, etiketlenmiş verilerden örüntüler öğrenerek daha önce görmediği örnekler hakkında karar verir.

``

## Denetimli öğrenmenin temel mantığı

Bir veri kümesindeki her örnek, özellikler ve hedef etiketten oluşur. Özellik vektörünü $x$, etiketi $y$ ile gösterirsek eğitim kümesi şu biçimdedir:

$$D = \{(x_1,y_1),(x_2,y_2),\ldots,(x_n,y_n)\}$$

Amaç, gerçek ilişkiyi mümkün olduğunca iyi temsil eden $f(x)$ fonksiyonunu öğrenmektir. Sınıflandırmada çıktı ayrık bir sınıftır: spam veya normal, hasta veya sağlıklı gibi. Regresyonda ise ev fiyatı gibi sürekli bir değer tahmin edilir.

Modelin yalnızca eğitim örneklerini ezberlemesi yeterli değildir. Asıl başarı, görülmemiş veriler üzerinde doğru tahmin yapabilmesidir. Eğitim başarısı yüksek fakat test başarısı düşükse **aşırı öğrenme**, model iki tarafta da zayıfsa **yetersiz öğrenme** gündemdedir.

| Algoritma | Temel fikir | Güçlü yönü | Dikkat edilmesi gereken |
|---|---|---|---|
| k-NN | En yakın komşular oy verir | Basit ve sezgiseldir | Ölçeklendirmeye duyarlıdır |
| Karar Ağacı | Sorularla veriyi dallara ayırır | Kolay açıklanabilir | Aşırı öğrenebilir |
| SVM | Sınıflar arasındaki marjı büyütür | Karmaşık sınırlarda etkilidir | Parametre seçimi önemlidir |

## k-En Yakın Komşu: Mahalle ne diyorsa o

k-NN, yeni bir örneğin eğitim kümesindeki en yakın $k$ komşusunu bulur ve çoğunluğun etiketini seçer. Öklid uzaklığı yaygın bir ölçüdür:

$$d(x,z)=\sqrt{\sum_{j=1}^{m}(x_j-z_j)^2}$$

$k=1$ seçimi gürültüye karşı hassas olabilir; çok büyük $k$ ise farklı sınıfları birbirine karıştırabilir. Ayrıca yaş ile gelir gibi farklı ölçeklerdeki özellikler kullanılacaksa standartlaştırma yapılmalıdır. Aksi hâlde büyük sayılara sahip özellik, mesafe hesabının megafonunu ele geçirir.

## Karar Ağaçları: Evet mi, hayır mı?

Karar ağacı, veriyi art arda sorularla böler. Örneğin “Gelir 40.000'den yüksek mi?” sorusu iki dal oluşturabilir. En faydalı bölünmeyi belirlemek için Gini safsızlığı kullanılabilir:

$$Gini = 1-\sum_{i=1}^{C}p_i^2$$

Saf bir düğümde örneklerin tamamı aynı sınıftadır. Ağacın kontrolsüz büyümesi ezberlemeye yol açabileceğinden `max_depth` ve `min_samples_split` gibi sınırlar önemlidir.

## Destek Vektör Makineleri: En geniş güvenlik koridoru

SVM, sınıfları ayıran bir hiper düzlem bulur ve bu düzlemle en yakın örnekler arasındaki marjı en büyük yapmaya çalışır. Kararı belirleyen kritik örneklere **destek vektörleri** denir. Doğrusal ayrım mümkün değilse RBF gibi çekirdekler, veriyi açıkça dönüştürmeden daha karmaşık karar sınırları kurabilir. `C` parametresi hatalara verilen cezayı, `gamma` ise tek bir örneğin etki alanını kontrol eder.

## Python ile üç modeli karşılaştırmak

Aşağıdaki kod, özellikleri standartlaştırır ve modelleri aynı test kümesinde değerlendirir:

```python
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC

X, y = load_breast_cancer(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

models = {
    "k-NN": make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=5)),
    "Karar Ağacı": DecisionTreeClassifier(max_depth=4, random_state=42),
    "SVM": make_pipeline(StandardScaler(), SVC(kernel="rbf"))
}

for name, model in models.items():
    model.fit(X_train, y_train)
    print(name, model.score(X_test, y_test))
```

Doğruluk tek başına her zaman yeterli değildir. Dengesiz sınıflarda kesinlik, duyarlılık, F1 skoru ve karmaşıklık matrisi de incelenmelidir. Sonuçta en iyi algoritma diye evrensel bir şampiyon yoktur; veri yapısına, açıklanabilirlik ihtiyacına ve hata maliyetine en uygun yarışmacı vardır.
