---
layout: post
title: "Pivot Kim Olacak? Quicksort’tan Toplumsal Hiyerarşilere Algoritmik Bir Yolculuk"
math: true
categories: 
  - Bilgi
tags: 
  - algoritmalar
  - quicksort
  - algoritmik adalet
---

Bir sınıftaki öğrencileri nota, çalışanları performansa veya kredi başvurularını risk puanına göre sıraladığımızı düşünelim. İlk bakışta bu işlemler Quicksort’un yaptığına benzer: Bir ölçüt seçilir, herkes bu ölçüte göre gruplara ayrılır ve düzen ortaya çıkar. Ancak insanları sıralarken kullanılan “pivot”, yalnızca teknik bir değişken değildir; fırsatları, görünürlüğü ve gücü belirleyen toplumsal bir tercihe dönüşebilir.

``

## Önce Quicksort’u Masaya Yatırmak

Quicksort, **böl ve yönet** yaklaşımına dayanan bir sıralama algoritmasıdır. Diziden bir pivot seçer; küçük değerleri pivotun soluna, büyük değerleri sağına taşır. Ardından aynı işlemi iki alt grup üzerinde tekrarlar.

Ortalama çalışma süresi şu bağıntıyla modellenebilir:

$$T(n)=2T\left(\frac{n}{2}\right)+O(n)=O(n\log n)$$

Fakat pivot sürekli en küçük veya en büyük eleman seçilirse gruplar dengesizleşir:

$$T(n)=T(n-1)+O(n)=O(n^2)$$

Yani pivot seçimi, algoritmanın kaderini değiştirir. İşte metaforun kapısı tam burada açılır: Toplumlarda da başarıyı ölçmek için seçilen merkezi kriterler, insanları dengeli biçimde değerlendirebilir veya mevcut eşitsizlikleri derinleştirebilir.

```python
def quicksort(insanlar, olcut):
    if len(insanlar) <= 1:
        return insanlar

    pivot = insanlar[len(insanlar) // 2]
    dusuk = [kisi for kisi in insanlar if olcut(kisi) < olcut(pivot)]
    esit = [kisi for kisi in insanlar if olcut(kisi) == olcut(pivot)]
    yuksek = [kisi for kisi in insanlar if olcut(kisi) > olcut(pivot)]

    return quicksort(dusuk, olcut) + esit + quicksort(yuksek, olcut)
```

Bu kod, kişileri verilen bir ölçüte göre sıralar. Teknik açıdan masum görünen `olcut` fonksiyonu gelir, sınav puanı veya üretkenlik olabilir. Fakat ölçüt geçmişteki ayrıcalıkları içeriyorsa algoritma onları sorgulamaz; yalnızca daha düzenli hâle getirir.

## Pivot ile Ayrıcalık Arasındaki Benzerlik

Bir işe alım sistemi “başarılı çalışan” profilini mevcut yöneticilere bakarak oluşturursa yöneticiler toplumsal pivot hâline gelir. Onlara benzeyen adaylar uygun, uzak kalanlar riskli sayılabilir. Böylece sistem, geçmiş hiyerarşiyi geleceğin matematiksel standardına dönüştürür.

| Quicksort kavramı | Toplumsal metafor | Olası sorun |
|---|---|---|
| Pivot | Başarı standardı | Tek bir grubun norm kabul edilmesi |
| Karşılaştırma | Puanlama ve değerlendirme | Bağlamın göz ardı edilmesi |
| Bölümleme | Sınıf veya statü grupları | Keskin ve kalıcı kategoriler |
| Özyineleme | Düzenin yeniden üretilmesi | Eşitsizliğin nesiller boyunca sürmesi |
| Dengesiz dizi | Fırsat eşitsizliği | Bazı grupların sürekli geride kalması |

## Hızlı Olmak, Adil Olmak Değildir

Bir algoritmanın doğruluğu ile adaleti aynı şey değildir. Quicksort, tanımlanan karşılaştırma kuralına göre kusursuz sıralama yapabilir; ancak kuralın ahlaki açıdan doğru olup olmadığını bilemez. Benzer şekilde kredi modeli ödememe riskini doğru tahmin ederken belirli mahalleleri dolaylı biçimde cezalandırabilir.

Algoritmik adalette kullanılan ölçütlerden biri **demografik eşitliktir**:

$$P(\hat{Y}=1\mid A=a)=P(\hat{Y}=1\mid A=b)$$

Bu ifade, farklı grupların olumlu karar alma oranlarının eşit olmasını ister. **Fırsat eşitliği** ise gerçekten uygun kişiler arasındaki kabul oranlarına odaklanır:

$$P(\hat{Y}=1\mid Y=1,A=a)=P(\hat{Y}=1\mid Y=1,A=b)$$

| Yaklaşım | Temel soru | Kör noktası |
|---|---|---|
| Verimlilik | Sonuç ne kadar hızlı üretiliyor? | Sonucun kime zarar verdiği |
| Doğruluk | Tahminler ne kadar isabetli? | Hataların gruplara dağılımı |
| Eşitlik | Gruplar benzer fırsat alıyor mu? | Bireysel farklılıklar |
| Açıklanabilirlik | Karar anlaşılabiliyor mu? | Açıklamanın adil olduğu varsayımı |

## Metaforun Sınırı ve Asıl Ders

İnsanlar sayı değildir; toplum da sıralanmayı bekleyen bir dizi değildir. Bu nedenle Quicksort benzetmesi bir çözüm değil, düşünme aracıdır. Ama güçlü bir uyarı sunar: **Pivotu kim seçiyor, karşılaştırma kuralını kim yazıyor ve yanlış tarafta kalanların itiraz hakkı var mı?**

Adil sistemler yalnızca daha iyi kodla kurulmaz. Temsilî veri, etki analizi, bağımsız denetim, açıklanabilir kararlar ve insan müdahalesi gerekir. Bazen en adil seçenek, sıralamayı iyileştirmek değil; herkesi tek bir hiyerarşiye sokma fikrini sorgulamaktır. Çünkü toplumsal hayatta mesele yalnızca $O(n\log n)$ hızına ulaşmak değil, hiçbir insanı görünmez bir pivotun gölgesinde bırakmamaktır.
