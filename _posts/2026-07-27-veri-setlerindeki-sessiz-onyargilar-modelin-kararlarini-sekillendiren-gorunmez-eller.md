---
layout: post
title: "Veri Setlerindeki Sessiz Önyargılar: Modelin Kararlarını Şekillendiren Görünmez Eller"
math: true
categories: 
  - Bilgi
tags: 
  - yapay zeka etiği
  - veri önyargısı
  - makine öğrenmesi
---

Bir makine öğrenmesi modeli dünyayı doğrudan gözlemlemez; ona sunduğumuz veri setinin penceresinden bakar. Pencerenin camı çizik, renkli veya yalnızca belirli bir sokağa dönükse model de gerçeği öyle sanır. Bu nedenle toplumsal önyargılar, kötü niyetli bir algoritma yazılmasa bile veri toplama, etiketleme ve örnekleme süreçlerinden modele sessizce sızabilir.
``

## Model değil, geçmiş konuşuyor

Denetimli öğrenmede model, girdiler $X$ ile hedef değişken $Y$ arasındaki ilişkiyi öğrenmeye çalışır. Basitçe amaç, tahmin hatasını küçülten bir $f(X)$ fonksiyonu bulmaktır:

$$f^* = argmin_f E[L(Y, f(X))]$$

Ancak $Y$ tarafındaki etiketler geçmişte verilmiş insan kararlarından oluşuyorsa model yalnızca gerçeği değil, o kararların önyargılarını da öğrenir. Örneğin işe alım verisinde geçmiş çalışanların çoğu erkekse, başarılı çalışan etiketi erkeklikle dolaylı biçimde ilişkilendirilebilir. Cinsiyet sütununu silmek de yeterli değildir; askerlik durumu, okul, posta kodu veya kariyer araları aynı bilgiyi taşıyan vekil değişkenlere dönüşebilir.

| Veri toplama sorunu | Somut örnek | Modeldeki olası sonuç |
|---|---|---|
| Eksik temsil | Yüz veri setinde koyu tenli kişilerin az olması | Bazı yüzlerde daha yüksek hata |
| Tarihsel önyargı | Geçmiş terfilerde kadınların geri planda kalması | Terfi puanlarının eşitsizleşmesi |
| Ölçüm yanlılığı | Sağlık ihtiyacını harcama miktarıyla ölçmek | Sağlığa erişemeyenleri düşük riskli sanmak |
| Seçim yanlılığı | Anketi yalnızca internet kullanıcılarına sunmak | Toplumun tamamını temsil etmeyen sonuçlar |
| Etiketleme yanlılığı | Aynı davranışın farklı gruplarda farklı yorumlanması | Hatalı sınıflandırma oranlarının ayrışması |

## Polis verisi paradoksu

Bir bölgede daha fazla polis devriyesi yapılırsa daha fazla olay kaydedilebilir. Veri seti bu kayıtlarla oluşturulduğunda model, bölgenin doğası gereği daha riskli olduğu sonucuna varır. Ardından bölgeye daha fazla devriye gönderilir ve daha çok kayıt üretilir. Böylece veri, tahmini; tahmin de yeni veriyi besleyen bir döngü yaratır. Bu durum, termometrenin ateşi ölçmek yerine ateşi yükseltmesine benzer.

Benzer bir sorun sağlık alanında görülür. Bir sistem, hastanın sağlık ihtiyacını geçmiş sağlık harcamasıyla temsil edebilir. Oysa iki grubun hastalık düzeyi aynı olsa bile sağlık hizmetine erişimi düşük grubun harcaması daha azdır. Model şu hatalı varsayımı öğrenir: düşük harcama eşittir düşük ihtiyaç.

## Ortalamalar adaleti garanti etmez

Bir modelin genel doğruluğunun yüzde 92 olması etkileyici görünebilir. Fakat başarı gruplara göre ayrıştırılmadığında önemli farklar saklanır. Örneğin yanlış negatif oranı şöyle tanımlanır:

$$FNR = FN / (FN + TP)$$

Toplam hata düşükken $FNR_A = 0.08$ ve $FNR_B = 0.31$ olabilir. Yani model, B grubundaki gerçek olumlu örnekleri yaklaşık dört kat daha sık kaçırmaktadır.

Aşağıdaki Python kodu, sonuçları gruplara göre inceleyerek bu sessiz farkı görünür kılar:

```python
import pandas as pd
from sklearn.metrics import confusion_matrix

def grup_raporu(df):
    for grup, parca in df.groupby('grup'):
        tn, fp, fn, tp = confusion_matrix(
            parca['gercek'], parca['tahmin'], labels=[0, 1]
        ).ravel()

        fnr = fn / (fn + tp) if fn + tp else 0
        fpr = fp / (fp + tn) if fp + tn else 0
        print(grup, {'FNR': round(fnr, 3), 'FPR': round(fpr, 3)})
```

Kod, yalnızca genel doğruluğa bakmak yerine her grup için yanlış negatif ve yanlış pozitif oranlarını hesaplar. Elbette grupları analiz etmek, kişileri kalıcı kalıplara hapsetmek için değil, sistematik zararları teşhis etmek için kullanılmalıdır.

## Daha dikkatli veri, daha dürüst model

| Kontrol | Sorulması gereken soru |
|---|---|
| Kaynak analizi | Veriyi kim, hangi amaçla topladı? |
| Temsil kontrolü | Hangi gruplar az veya hiç temsil edilmiyor? |
| Etiket denetimi | Etiket bir gerçek mi, insan yorumu mu? |
| Vekil değişken taraması | Hassas özellikler başka sütunlardan çıkarılabilir mi? |
| Grup bazlı değerlendirme | Hata oranları gruplar arasında değişiyor mu? |
| Sürekli izleme | Model devreye girdikten sonra yeni eşitsizlik üretiyor mu? |

Çözüm yalnızca veri setini büyütmek değildir; yanlış mekanizmayla toplanan daha fazla veri, önyargıyı daha güvenilir biçimde yeniden üretir. Veri kartları hazırlamak, örnekleme sürecini belgelemek, etkilenen toplulukları tasarıma katmak ve modelleri düzenli olarak denetlemek gerekir. Çünkü algoritmalar görünmez eller değildir; asıl görünmez eller, hangi olayın kaydedildiğine, kimin temsil edildiğine ve neyin başarı sayıldığına karar veren süreçlerdir.
