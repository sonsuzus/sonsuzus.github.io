---
layout: post
title: "Veri Ambarı ve Yıldız Şeması: Operasyonel Veriden İş Zekâsına"
math: true
categories: 
  - Bilgi
tags: 
  - veri ambarı
  - yıldız şeması
  - iş zekâsı
---

Bir e-ticaret sisteminde sipariş vermek saniyeler sürerken, “Son üç yılda hangi şehirde, hangi ürün kategorisi daha kârlıydı?” sorusunun yanıtı milyonlarca kaydın incelenmesini gerektirebilir. Veri ambarı, günlük operasyonları yavaşlatmadan bu tür geriye dönük analizleri gerçekleştirmek için tasarlanmış merkezi veri yapısıdır.

``

## OLTP ve OLAP dünyaları

Operasyonel sistemler, yani **OLTP** uygulamaları; sipariş oluşturma, ödeme alma veya stok güncelleme gibi anlık işlemlere odaklanır. Veri ambarlarının temelini oluşturan **OLAP** yaklaşımı ise veriyi farklı açılardan inceleyerek karar desteği sağlar.

| Özellik | OLTP sistemi | Veri ambarı / OLAP |
|---|---|---|
| Temel amaç | Günlük işlemleri yürütmek | Analiz ve raporlama yapmak |
| Veri kapsamı | Güncel ve ayrıntılı | Tarihsel ve bütünleşik |
| Sorgu türü | Kısa ekleme ve güncelleme | Büyük tarama ve toplulaştırma |
| Modelleme | Genellikle normalize | Genellikle boyutsal |
| Kullanıcı | Uygulama ve operasyon ekibi | Analist ve yöneticiler |

Normalize edilmiş operasyonel veritabanlarında tekrar azaltılır. Ancak raporlama sırasında çok sayıda tabloyu birleştirmek gerekebilir. Veri ambarı, kontrollü veri tekrarını kabul ederek sorguları anlaşılır ve hızlı hâle getirir. Kısacası biri kasadaki kuyruğu hızlandırır, diğeri geçen yıl kasadan ne kadar kazandığımızı araştırır.

## Yıldız şemasının anatomisi

Yıldız şemasının merkezinde ölçülebilir olayları saklayan bir **fact (olgu) tablosu** bulunur. Bu tabloyu ürün, müşteri, mağaza ve tarih gibi **dimension (boyut) tabloları** çevreler. Şema çizildiğinde ortaya yıldızı andıran bir görüntü çıkar.

Bir satış olgu tablosunda şu ölçüler bulunabilir:

- Satılan adet
- Birim fiyat
- İndirim tutarı
- Maliyet
- Net satış tutarı

Boyut tabloları ise bu sayıların bağlamını açıklar. Örneğin tarih boyutu yıl, çeyrek ve ay; ürün boyutu marka ve kategori bilgilerini taşır. Böylece toplam gelir şu şekilde ifade edilebilir:

$$NetGelir = \sum_{i=1}^{n}(Adet_i \times BirimFiyat_i - Indirim_i)$$

Buradaki en kritik karar **grain**, yani olgu tablosundaki bir satırın neyi temsil ettiğidir. “Her sipariş”, “siparişteki her ürün satırı” ve “ürünün günlük toplam satışı” birbirinden farklı ayrıntı seviyeleridir. Grain belirsizse aynı satışın iki kez sayılması gibi tatsız sürprizler kaçınılmazdır.

## Örnek tablo tasarımı

Aşağıdaki SQL, her satırın bir sipariş kalemini temsil ettiği sade bir model kurar:

```sql
CREATE TABLE dim_product (
    product_key INT PRIMARY KEY,
    product_id INT,
    product_name VARCHAR(150),
    category VARCHAR(100),
    brand VARCHAR(100)
);

CREATE TABLE dim_date (
    date_key INT PRIMARY KEY,
    full_date DATE,
    year_number INT,
    quarter_number INT,
    month_name VARCHAR(20)
);

CREATE TABLE fact_sales (
    date_key INT REFERENCES dim_date(date_key),
    product_key INT REFERENCES dim_product(product_key),
    order_id INT,
    quantity INT,
    unit_price DECIMAL(12,2),
    discount_amount DECIMAL(12,2),
    cost_amount DECIMAL(12,2)
);
```

`product_key` gibi ambar tarafından üretilen alanlara **surrogate key** denir. Kaynak sistemdeki kimlikler değişse bile tarihsel kayıtların tutarlı kalmasını sağlarlar.

## Tarihsel değişiklikler ve veri akışı

Bir müşteri şehir değiştirdiğinde eski satışlar hangi şehre bağlanmalıdır? **Slowly Changing Dimension (SCD)** yaklaşımı bu problemi çözer. SCD Tip 1 eski değeri günceller ve geçmişi korumaz. SCD Tip 2 ise yeni bir boyut satırı açarak başlangıç ve bitiş tarihleriyle geçmişi muhafaza eder.

Veriler genellikle **ETL** sürecinden geçer: Kaynaklardan çıkarılır, temizlenip dönüştürülür ve ambara yüklenir. Modern bulut platformlarında önce yükleyip sonra dönüştüren **ELT** yaklaşımı da yaygındır.

İyi tasarlanmış bir yıldız şeması yalnızca hızlı sorgu üretmez; iş kullanıcılarının veriyi ortak bir dille konuşmasını sağlar. Sağlam bir grain, doğru ölçüler ve tarihsel boyut yönetimi birleştiğinde dağınık operasyon kayıtları güvenilir karar mekanizmasına dönüşür.
