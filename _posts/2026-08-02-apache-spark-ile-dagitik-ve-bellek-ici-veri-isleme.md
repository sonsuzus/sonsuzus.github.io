---
layout: post
title: "Apache Spark ile Dağıtık ve Bellek İçi Veri İşleme"
math: true
categories: 
  - Bilgi
tags: 
  - Apache Spark
  - Büyük Veri
  - PySpark
---

Devasa bir veri setini tek bilgisayarda işlemeye çalışmak, taşınma günü bütün kolileri küçük bir otomobile doldurmaya benzer: Bir noktadan sonra ne bagaj kapanır ne de süreç ilerler. Apache Spark, verileri kümeye dağıtarak ve ara sonuçları mümkün olduğunca bellekte tutarak bu sorunu çözer. Böylece haritalama, filtreleme ve indirgeme gibi işlemler, her aşamada diske yazma zorunluluğuna takılmadan çok daha hızlı gerçekleştirilebilir.

``

## Spark neden hızlıdır?

Geleneksel Hadoop MapReduce modelinde bir işin çıktısı çoğunlukla diske yazılır ve sonraki aşama bu veriyi yeniden diskten okur. Disk erişimi, özellikle yinelemeli algoritmalarda önemli bir darboğazdır. Spark ise çalışma verilerini RAM üzerinde saklayabilir ve aynı veri tekrar kullanılacaksa `cache()` veya `persist()` ile bellekte tutabilir.

Basitleştirilmiş toplam çalışma süresini şöyle düşünebiliriz:

$$T_{toplam} = T_{okuma} + T_{hesaplama} + T_{iletisim} + T_{yazma}$$

Spark, özellikle $T_{okuma}$ ve $T_{yazma}$ bileşenlerini azaltmaya çalışır. Ancak “Spark her şeyi RAM’de yapar” demek doğru değildir. Bellek yetersiz kalırsa bazı bölümler diske taşabilir; ayrıca shuffle sırasında ağ ve disk kullanılabilir.

| Özellik | Geleneksel MapReduce | Apache Spark |
|---|---|---|
| Ara sonuçlar | Genellikle diske yazılır | Bellekte tutulabilir |
| Yinelemeli işler | Daha yavaş | Cache sayesinde hızlı |
| İşlem modeli | Map ve Reduce aşamaları | DAG tabanlı esnek aşamalar |
| Gerçek zamanlı kullanım | Sınırlı | Structured Streaming desteği |
| API seçenekleri | Daha düşük seviyeli | Python, Scala, Java ve R |

## Dağıtık işlem mantığı

Spark uygulamasında **driver**, yapılacak işi planlar; **executor** süreçleri ise verinin parçaları üzerinde hesaplama yapar. Veri, partition adı verilen bölümlere ayrılır. Her partition farklı bir executor tarafından işlenebildiği için paralellik elde edilir.

Teorik olarak $N$ kayıt, eşit güçte $P$ işlemciye kusursuz biçimde dağıtılırsa işlem yükü yaklaşık olarak şöyledir:

$$W_{birim} \approx \frac{N}{P}$$

Gerçekte ağ iletişimi, görev planlama ve dengesiz partition dağılımı nedeniyle doğrusal hızlanma her zaman mümkün değildir. Örneğin kayıtların büyük kısmı tek bir anahtara aitse **data skew** oluşur ve bir executor diğerleri kahvesini bitirmişken hâlâ çalışıyor olabilir.

## PySpark ile MapReduce benzeri analiz

Aşağıdaki örnek, bir metindeki kelimeleri sayar. `flatMap` satırları kelimelere ayırır, `map` her kelimeyi `(kelime, 1)` çiftine dönüştürür ve `reduceByKey` aynı kelimelerin sayılarını toplar.

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("KelimeSayaci") \
    .getOrCreate()

satirlar = spark.sparkContext.textFile("veri/metinler.txt")

sonuclar = (
    satirlar
    .flatMap(lambda satir: satir.lower().split())
    .map(lambda kelime: (kelime, 1))
    .reduceByKey(lambda a, b: a + b)
)

for kelime, adet in sonuclar.take(10):
    print(kelime, adet)

spark.stop()
```

Buradaki dönüşümler hemen çalışmaz. Spark, **lazy evaluation** yaklaşımıyla işlemleri bir DAG üzerinde biriktirir. `take(10)` gibi bir action çağrıldığında plan optimize edilir ve görevler executorlara gönderilir. Bu sayede gereksiz hesaplamalar azaltılabilir.

## RDD mi, DataFrame mi?

| Yapı | Avantajı | Uygun kullanım |
|---|---|---|
| RDD | Düşük seviyeli kontrol | Özel veri dönüşümleri |
| DataFrame | Catalyst optimizasyonu | Analiz ve ETL süreçleri |
| Dataset | Tip güvenliği | Scala ve Java uygulamaları |

Modern projelerde çoğunlukla DataFrame API tercih edilir. Çünkü Spark’ın Catalyst optimizer bileşeni sorgu planını inceleyerek filtreleri erkene alma ve gereksiz sütunları okumama gibi iyileştirmeler yapabilir.

Spark sihirli bir hızlandırma düğmesi değildir; doğru partition sayısı, uygun cache kullanımı ve shuffle maliyetlerinin izlenmesi gerekir. Yine de büyük veri setlerinde tekrarlı analiz, makine öğrenmesi, ETL ve akış işleme ihtiyaçları söz konusu olduğunda bellek içi yaklaşımı, klasik disk merkezli modellere karşı son derece güçlü bir avantaj sağlar.
