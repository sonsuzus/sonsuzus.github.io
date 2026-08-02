---
layout: post
title: "ETL Süreçleriyle Ham Veriden Güvenilir Veri Boru Hatlarına"
math: true
categories: 
  - Bilgi
tags: 
  - ETL
  - veri mühendisliği
  - data pipeline
---

Bir e-ticaret şirketinde siparişler PostgreSQL’de, reklam verileri bir API’de, müşteri yorumları JSON dosyalarında tutulabilir. Analiz ekibinin bütün bunları tek tek toplaması hem zaman kaybettirir hem de hata üretir. ETL süreçleri, dağınık ham veriyi otomatik biçimde çekip temizleyerek analiz edilmeye hazır, güvenilir bir veri kaynağına dönüştürür.

``

## ETL nedir?

ETL; **Extract, Transform, Load** kelimelerinin baş harflerinden oluşur. Bir veri boru hattı ise verinin kaynaktan hedefe düzenli, izlenebilir ve mümkünse hatalara dayanıklı biçimde akmasını sağlayan daha geniş otomasyon sistemidir.

| Aşama | Temel soru | Örnek işlem |
|---|---|---|
| Extract | Veri nereden alınacak? | API, veritabanı veya CSV okuma |
| Transform | Veri nasıl kullanılabilir hâle gelecek? | Temizleme, birleştirme, doğrulama |
| Load | Veri nereye yazılacak? | Veri ambarına veya data lake’e yükleme |

### 1. Extract: Veriyi kaynağından çekmek

Çıkarma aşamasında ilişkisel veritabanları, uygulama günlükleri, sensörler, bulut depoları ve harici API’ler gibi farklı kaynaklara bağlanılır. Buradaki önemli karar, verinin tamamının mı yoksa yalnızca değişen bölümünün mü alınacağıdır.

Tam yükte her çalıştırmada $N$ kayıt okunur. Artımlı yükte yalnızca değişen $\Delta N$ kayıt işlenir. Genellikle $\Delta N \ll N$ olduğundan artımlı yaklaşım ağ ve işlem maliyetini ciddi ölçüde azaltır. Bunun için zaman damgası, artan kimlik veya CDC (Change Data Capture) kullanılabilir.

### 2. Transform: Ham veriyi anlamlı hâle getirmek

Dönüştürme, ETL’in mutfağıdır. Eksik alanlar ele alınır, tarih biçimleri standartlaştırılır, tekrar eden kayıtlar silinir ve iş kuralları uygulanır. Örneğin toplam sipariş geliri şu şekilde hesaplanabilir:

$$Gelir = \sum_{i=1}^{n} adet_i \times birim\_fiyat_i$$

Ancak matematik doğru olsa bile para birimleri farklıysa sonuç yanıltıcıdır. Bu nedenle dönüşüm yalnızca kod yazmak değil, verinin iş bağlamını anlamaktır.

```python
import pandas as pd

def transform_orders(df: pd.DataFrame) -> pd.DataFrame:
    # Kimliği olmayan kayıtlar güvenilir biçimde eşleştirilemez.
    df = df.dropna(subset=["order_id"])
    df = df.drop_duplicates(subset=["order_id"])

    # Farklı tarih gösterimlerini ortak tipe dönüştürür.
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
    df["total_amount"] = df["quantity"] * df["unit_price"]

    # Geçersiz veya negatif tutarları dışarıda bırakır.
    return df[df["total_amount"] >= 0]
```

Bu fonksiyon temel temizlik, tip dönüşümü ve gelir hesaplamasını tek adımda gerçekleştirir. Gerçek sistemlerde kurallar testlerle desteklenmelidir.

### 3. Load: Sonucu hedefe taşımak

Temizlenen veri; Snowflake, BigQuery, Redshift gibi veri ambarlarına veya bir data lake’e yüklenebilir. Yükleme tam yenileme, ekleme ya da **upsert** yöntemiyle yapılabilir. Upsert, mevcut kaydı günceller; yoksa yeni kayıt ekler.

| Yaklaşım | Avantaj | Dezavantaj |
|---|---|---|
| Batch | Basit ve ekonomik | Veri gecikmeli gelir |
| Streaming | Düşük gecikme | İşletmesi daha karmaşıktır |
| ETL | Hedefe temiz veri gider | Dönüşüm altyapısı gerekir |
| ELT | Ham veri korunur, esnektir | Güçlü hedef sistem ister |

## Sağlam bir pipeline nasıl tasarlanır?

İyi bir veri boru hattı yalnızca başarılı durumda çalışmamalıdır. Aynı işlem tekrar çalıştırıldığında sonucu bozmayan **idempotent** adımlar tasarlanmalı; başarısız kayıtlar ayrı bir hata kuyruğuna gönderilmelidir. Loglama, veri kalite kontrolleri, şema doğrulama ve uyarılar da sistemin vazgeçilmez parçalarıdır.

Airflow, Dagster veya Prefect görevlerin sırasını ve zamanlamasını yönetebilir. Kafka gerçek zamanlı veri akışında, dbt ise SQL tabanlı dönüşümlerde öne çıkar. Araç seçiminden önce veri hacmi, gecikme beklentisi, maliyet ve ekip deneyimi değerlendirilmelidir.

Sonuç olarak ETL, veriyi A noktasından B noktasına taşıyan basit bir kargo hizmeti değildir. Kaynakları uzlaştıran, kaliteyi koruyan ve analitik kararların güvenilir temelini oluşturan otomatik bir üretim hattıdır. Boru hattı görünmez çalıştığında herkes mutludur; durduğunda ise neden veri mühendislerine ihtiyaç duyulduğu hemen anlaşılır!
