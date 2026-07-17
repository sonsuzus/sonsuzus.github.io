---
layout: post
title: "SQL ile Anomali Tespiti: Log Denizinde Garip Balıkları Yakalamak"
math: true
categories: 
  - Bilgi
tags: 
  - SQL
  - anomali tespiti
  - log analizi
  - veri analizi
---

Sistem logları bazen sakin bir göl, bazen de üretim ortamında patlayan bir mısır tenceresi gibidir. Milyonlarca satır arasında “bir şeyler ters gidiyor” hissini elle aramak yerine, SQL ile olağandışı örüntüleri yakalayabiliriz. Üstelik bunun için her zaman dev bir yapay zekâ modeli gerekmez; iyi kurulmuş istatistiksel mantık, pencere fonksiyonları ve birkaç akıllı sorgu çoğu alarm zilini çaldırmaya yeter.

``

Anomali tespiti, verinin beklenen davranıştan anlamlı biçimde sapmasını bulma işidir. Log dünyasında bu sapma; hata sayısında ani artış, belirli bir servisin alışılmadık gecikmesi, tek bir IP’den anormal istek yağması veya normalde hiç görülmeyen hata kodlarının ortaya çıkması olabilir. Temel fikir şudur: Önce “normal” davranışı tanımlarız, sonra güncel değerin bu normale ne kadar uzaklaştığını ölçeriz.

En yaygın yöntemlerden biri z-skorudur. Bir ölçümün ortalamadan kaç standart sapma uzakta olduğunu gösterir:

$$z = \frac{x - \mu}{\sigma}$$

Burada $x$ gözlenen değer, $\mu$ geçmiş ortalama, $\sigma$ ise standart sapmadır. Örneğin bir serviste dakikada ortalama 20 hata varken standart sapma 5 ise, 45 hata geldiğinde $z = 5$ olur. Bu, “dostum burada bir şey yanıyor olabilir” demenin matematiksel hâlidir.

| Anomali Türü | Log Örneği | SQL ile Yaklaşım |
|---|---|---|
| Noktasal anomali | Bir dakikada 500 hata | Ortalama ve standart sapma karşılaştırması |
| Bağlamsal anomali | Gece 03:00’te normal, öğlen anormal trafik | Saat/gün bazlı gruplama |
| Kolektif anomali | Art arda gelen küçük timeout zinciri | Pencere fonksiyonları ve hareketli toplam |

Diyelim ki elimizde `app_logs` adlı bir tablo var: `ts`, `service_name`, `level`, `status_code`, `duration_ms`, `message`. İlk hedefimiz, her servis için dakikalık hata sayılarını çıkarmak olsun.

```sql
WITH minute_errors AS (
  SELECT
    DATE_TRUNC('minute', ts) AS minute_bucket,
    service_name,
    COUNT(*) AS error_count
  FROM app_logs
  WHERE level = 'ERROR'
  GROUP BY 1, 2
)
SELECT *
FROM minute_errors
ORDER BY minute_bucket DESC;
```

Bu sorgu ham logları daha anlamlı bir zaman serisine dönüştürür. Anomali tespitinde ilk büyük adım genellikle budur: Gürültülü satırları ölçülebilir metriklere çevirmek.

Şimdi geçmiş davranışı kullanarak z-skoru hesaplayalım. Aşağıdaki örnek PostgreSQL sözdizimine yakındır ve her servis için genel ortalama ile standart sapmayı çıkarır.

```sql
WITH minute_errors AS (
  SELECT
    DATE_TRUNC('minute', ts) AS minute_bucket,
    service_name,
    COUNT(*) AS error_count
  FROM app_logs
  WHERE level = 'ERROR'
  GROUP BY 1, 2
), baseline AS (
  SELECT
    service_name,
    AVG(error_count) AS avg_errors,
    STDDEV(error_count) AS std_errors
  FROM minute_errors
  WHERE minute_bucket < NOW() - INTERVAL '15 minutes'
  GROUP BY service_name
)
SELECT
  m.minute_bucket,
  m.service_name,
  m.error_count,
  ROUND((m.error_count - b.avg_errors) / NULLIF(b.std_errors, 0), 2) AS z_score
FROM minute_errors m
JOIN baseline b USING (service_name)
WHERE m.minute_bucket >= NOW() - INTERVAL '15 minutes'
  AND (m.error_count - b.avg_errors) / NULLIF(b.std_errors, 0) > 3
ORDER BY z_score DESC;
```

Burada `NULLIF` küçük ama hayat kurtaran bir detaydır; standart sapma sıfırsa bölme hatasını engeller. `z_score > 3` eşiği klasik bir başlangıç noktasıdır, fakat her sistem için kutsal değildir. Ödeme sisteminde eşik daha hassas, test ortamında daha gevşek olabilir.

Bazı durumlarda genel ortalama yanıltıcıdır. Pazartesi sabahı trafiği ile pazar gecesi trafiği aynı kefeye konmaz. Bu yüzden bağlamsal baz çizgiler kullanmak daha sağlıklıdır.

| Baseline Yöntemi | Avantaj | Dezavantaj |
|---|---|---|
| Genel ortalama | Basit ve hızlı | Saatlik/dönemsel farkları kaçırır |
| Saat bazlı ortalama | Gün içi ritmi yakalar | Daha fazla veri ister |
| Hareketli pencere | Güncel davranışa uyum sağlar | Ani anomalileri baseline’a katabilir |

Gecikme anomalileri için yüzdelikler de çok değerlidir. Ortalama bazen aldatır; birkaç aşırı yavaş istek ortalamayı şişirebilir. Bu yüzden p95 veya p99 gibi değerler kullanılır.

```sql
SELECT
  DATE_TRUNC('minute', ts) AS minute_bucket,
  service_name,
  PERCENTILE_CONT(0.95) WITHIN GROUP (ORDER BY duration_ms) AS p95_latency
FROM app_logs
GROUP BY 1, 2
HAVING PERCENTILE_CONT(0.95) WITHIN GROUP (ORDER BY duration_ms) > 1000
ORDER BY minute_bucket DESC;
```

Bu sorgu, isteklerin yüzde 95’inin altında kaldığı gecikme değerini bulur. Eğer p95 1000 ms üstüne çıkıyorsa kullanıcıların ciddi bir kısmı yavaşlık hissediyor olabilir.

Son olarak, SQL ile anomali tespiti sadece alarm üretmek değildir; açıklanabilirlik de sağlar. “Bir model söyledi” yerine “son 15 dakikada `payment-api` hata sayısı normalin 4.7 standart sapma üstüne çıktı” diyebilirsiniz. Bu da hem geliştiricinin hem SRE ekibinin hızlı aksiyon almasını kolaylaştırır.

Özetle SQL, log okyanusunda el feneri gibidir. Doğru gruplama, istatistiksel eşikler, pencere fonksiyonları ve bağlamsal düşünme ile beklenmeyen sistem hatalarını üretim ortamı yangına dönmeden yakalayabilirsiniz.
