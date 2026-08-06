---
layout: post
title: "İlişkisel Veri Sorguları: INNER JOIN ve LEFT JOIN Rehberi"
math: true
categories: 
  - Bilgi
tags: 
  - SQL
  - JOIN
  - Veritabanı
---

Bir e-ticaret sisteminde müşteriler bir tabloda, siparişler başka bir tabloda tutulur. Peki “Hangi müşteri hangi siparişi verdi?” sorusunu nasıl yanıtlarız? SQL dünyasının çöpçatanı `JOIN`, farklı tablolardaki ilişkili satırları ortak sütunlar üzerinden buluşturur ve sonuçları tek bir sanal tablo gibi sunar.
``
## İlişkisel modelin temel mantığı

İlişkisel veritabanlarında bilgiler, gereksiz tekrarı azaltmak amacıyla farklı tablolara ayrılır. Örneğin her sipariş satırına müşterinin adını ve e-posta adresini yazmak yerine, sipariş tablosunda yalnızca müşteriyi işaret eden bir kimlik tutulur.

`musteriler` tablosundaki `id` alanı **birincil anahtar** (`PRIMARY KEY`), `siparisler` tablosundaki `musteri_id` alanı ise **yabancı anahtar** (`FOREIGN KEY`) olabilir. Aralarındaki ilişki şöyle ifade edilir:

$$Musteriler.id = Siparisler.musteri\_id$$

Bir müşteri birden fazla sipariş verebildiği için bu, bire-çok ilişkisidir. Müşteri başına ortalama sipariş sayısı basitçe şu şekilde düşünülebilir:

$$Ortalama = \frac{Toplam\ Siparis\ Sayisi}{Toplam\ Musteri\ Sayisi}$$

JOIN işlemi tabloları fiziksel olarak birleştirmez. Sorgu çalışırken koşula uyan satırlardan geçici bir sonuç kümesi üretir. Yani veritabanı mobilyalarını birbirine vidalamaz; yalnızca aynı fotoğraf karesine alır.

## INNER JOIN ve LEFT JOIN karşılaştırması

| Özellik | INNER JOIN | LEFT JOIN |
|---|---|---|
| Eşleşen kayıtlar | Getirilir | Getirilir |
| Sol tabloda eşleşmeyen kayıtlar | Getirilmez | Getirilir |
| Eksik sağ taraf değerleri | Sonuçta bulunmaz | `NULL` olur |
| Tipik kullanım | Yalnızca ilişkili veriler | Ana listedeki tüm kayıtlar |

### INNER JOIN kullanımı

`INNER JOIN`, iki tabloda da eşleşmesi bulunan satırları döndürür. Sipariş vermiş müşterileri ve siparişlerini listeleyelim:

```sql
SELECT
    m.id,
    m.ad,
    s.id AS siparis_id,
    s.tutar
FROM musteriler AS m
INNER JOIN siparisler AS s
    ON m.id = s.musteri_id;
```

Buradaki `ON` bölümü eşleşmenin hangi koşula göre yapılacağını belirtir. `AS` ile tanımlanan kısa tablo adları sorguyu okunabilir kılar. Siparişi olmayan bir müşteri bu sonuçta görünmez; çünkü eşleşme yalnızca tek tarafta kalmıştır.

### LEFT JOIN kullanımı

Şimdi mağazaya kayıtlı bütün müşterileri, sipariş vermemiş olsalar bile görmek istediğimizi düşünelim:

```sql
SELECT
    m.id,
    m.ad,
    s.id AS siparis_id,
    s.tutar
FROM musteriler AS m
LEFT JOIN siparisler AS s
    ON m.id = s.musteri_id;
```

`LEFT JOIN`, soldaki `musteriler` tablosunun bütün satırlarını korur. Eşleşen sipariş yoksa `siparis_id` ve `tutar` alanları `NULL` görünür. Sipariş vermeyen müşterileri bulmak için bu davranıştan yararlanabiliriz:

```sql
SELECT m.id, m.ad
FROM musteriler AS m
LEFT JOIN siparisler AS s
    ON m.id = s.musteri_id
WHERE s.id IS NULL;
```

Bu sorgu, pazarlama ekibinin “Sepetler neden bu kadar sessiz?” araştırmasına güzel bir başlangıç olabilir.

## ON ve WHERE tuzağı

`LEFT JOIN` kullanırken sağ tabloya ait filtreyi `WHERE` bölümüne dikkatsizce eklemek, sorguyu fiilen `INNER JOIN` gibi davranmaya zorlayabilir:

```sql
-- Siparişi olmayan müşterileri sonuçtan çıkarır
SELECT m.ad, s.tutar
FROM musteriler AS m
LEFT JOIN siparisler AS s ON m.id = s.musteri_id
WHERE s.tutar > 1000;
```

Eşleşmeyen satırlarda `s.tutar` değeri `NULL` olduğundan koşul sağlanmaz. Sol tablonun tamamını korumak istiyorsak filtreyi birleştirme koşuluna taşıyabiliriz:

```sql
SELECT m.ad, s.tutar
FROM musteriler AS m
LEFT JOIN siparisler AS s
    ON m.id = s.musteri_id
   AND s.tutar > 1000;
```

## Performans ve okunabilirlik

JOIN sütunlarına indeks eklemek, özellikle büyük tablolarda eşleşme aramasını hızlandırabilir. Ayrıca `SELECT *` yerine yalnızca gerekli sütunları seçmek ağ trafiğini ve bellek kullanımını azaltır. Sütun adlarını tablo takma adlarıyla nitelemek de belirsizliği önler.

Özetle, yalnızca karşılıklı eşleşen kayıtlar gerekiyorsa `INNER JOIN`; soldaki ana listenin tamamı korunacaksa `LEFT JOIN` tercih edilir. Doğru anahtarlar, bilinçli filtreler ve anlaşılır sorgular sayesinde dağınık görünen tablolar anlamlı bir veri hikâyesine dönüşür.
