---
layout: post
title: "Sentetik Verinin Felsefi Riski: Model Kendi Sesinin Yankısında Kaybolursa"
math: true
categories: 
  - Bilgi
tags: 
  - sentetik veri
  - yapay zekâ
  - model çöküşü
---

Bir yapay zekâ modelinin ürettiği metinler, görseller veya kodlar yeni modellerin eğitim verisine karıştığında tuhaf bir döngü başlar: Makine, dünyayı doğrudan gözlemlemek yerine kendi yankısını dinlemeye koyulur. İlk bakışta ucuz ve sınırsız görünen sentetik veri, kontrol edilmediğinde bilgi kirliliğini büyütebilir; istisnaları silebilir ve özgünlüğü istatistiksel bir ortalamaya dönüştürebilir.
``
## Döngüsel öğrenme nedir?

Klasik eğitimde model, insanlar ve fiziksel dünya tarafından üretilmiş verilere bakarak bir dağılım öğrenir. Döngüsel öğrenmede ise önceki modelin çıktıları, sonraki modelin girdilerine dönüşür:

$$Gerçek\ Veri \rightarrow Model_1 \rightarrow Sentetik\ Veri \rightarrow Model_2$$

Buradaki temel sorun, sentetik çıktının gerçekliğin kendisi değil, gerçekliğe ilişkin sıkıştırılmış bir tahmin olmasıdır. Her model bazı ayrıntıları atar, yaygın örüntüleri güçlendirir ve düşük olasılıklı örnekleri gözden kaçırır. Bu süreç tekrarlandığında dağılımın kuyrukları giderek küçülür.

Basitçe, bir nesildeki eğitim karışımını şöyle gösterebiliriz:

$$D_{t+1} = (1-\alpha)D_{gerçek} + \alpha D_{sentetik,t}$$

Burada $\alpha$, sentetik verinin ağırlığıdır. Değer büyüdükçe modelin dünya ile doğrudan teması azalır. Sentetik veri hatalıysa hata yalnızca korunmaz; güvenli ve akıcı bir dille yeniden paketlenerek daha inandırıcı hâle gelebilir.

## Yankı odasının üç riski

| Boyut | Gerçek veri ağırlıklı eğitim | Sentetik veri ağırlıklı eğitim |
|---|---|---|
| Çeşitlilik | Nadir ve düzensiz örnekleri barındırır | Yaygın kalıplara yakınsar |
| Hata yapısı | Hatalar farklı kaynaklardan gelir | Aynı hata nesiller boyunca çoğalabilir |
| Özgünlük | Yeni deneyimler ve bakışlar içerir | Önceki üretimlerin türevlerini üretir |
| İzlenebilirlik | Kaynağa ulaşmak görece mümkündür | İlk kaynağın insan mı model mi olduğu bulanıklaşır |

İlk risk **model çöküşüdür**. Model, az rastlanan durumları unutup en olası cevaplara sıkışır. İkinci risk **epistemik aklama**dır: Dayanağı olmayan bir iddia, binlerce sentetik metinde tekrarlandığı için yaygın ve güvenilir görünür. Üçüncüsü ise **özgünlük kaybıdır**. Kültür, yalnızca çoğunluk örüntülerinden oluşmaz; aykırı fikirler, yerel ifadeler ve başarısız denemeler de yaratıcı ilerlemenin hammaddesidir.

## Küçük bir simülasyon

Aşağıdaki Python kodu, bir dağılımın yalnızca en merkezi sentetik örneklerle tekrar tekrar öğrenilmesini kabaca canlandırır:

```python
import numpy as np

veri = np.random.normal(0, 3, 10_000)

for nesil in range(6):
    ortalama = veri.mean()
    sapma = veri.std()

    # Model uç değerleri daha az üretiyor.
    yeni_veri = np.random.normal(ortalama, sapma * 0.8, 10_000)
    veri = yeni_veri
    print(nesil, round(veri.std(), 2))
```

Standart sapma her nesilde küçülür. Bu, gerçek modellerin eksiksiz bir temsili değildir; ancak çeşitliliğin neden sessizce kaybolabileceğini gösterir. Sistem hâlâ düzgün cümleler kurabilirken kapsadığı dünya daralmış olabilir.

## Sentetik veri tamamen kötü mü?

Hayır. Mahremiyet gerektiren sağlık çalışmalarında, nadir hata senaryolarında veya veri artırmada son derece yararlı olabilir. Kritik ayrım, sentetik verinin **ikame** mi yoksa **destek** mi olduğudur. Gerçek veriyi tamamen değiştirmek yerine dengeli biçimde kullanılması; kaynağının etiketlenmesi, insan denetiminden geçirilmesi ve bağımsız test kümeleriyle ölçülmesi gerekir.

Sağlıklı bir yaklaşım için veri kökeni kaydedilmeli, sentetik oranı sınırlandırılmalı, azınlık örnekleri özellikle korunmalı ve modeller güncel gerçek dünya verileriyle düzenli olarak yeniden bağlanmalıdır. Çünkü mesele yalnızca teknik doğruluk değildir. Kendi ürettiğini tüketen bir model, sonunda bize dünyayı değil, dünya hakkında daha önce söylediği şeylerin ortalamasını anlatabilir. Yankı kusursuz duyulsa bile artık dışarıdan gelen bir ses olmayabilir.
