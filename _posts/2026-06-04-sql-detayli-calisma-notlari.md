---
layout: post
title: SQL Detaylı Çalışma Notları
math: false
excerpt_separator: "<!--more-->"
categories:
  - Program
tags:
  - sql
  - veritabanı
  - select
  - join
  - window-functions
  - cte
  - transaction
  - index
  - postgresql
  - sorgu
  - programlama
  - veri
---

SQL temellerini bilen ama sorguları daha bilinçli yazmak isteyenler için 70 konu, açıklama, örnek ve pratik notlarla hazırlanmış kapsamlı bir çalışma rehberi.

<!--more-->

**Pratik sıralama:** `SELECT` → `FROM` → `JOIN` → `WHERE` → `GROUP BY` → `HAVING` → `SELECT` hesapları → `ORDER BY` → `LIMIT`. SQL yazarken bu mantıksal akışı akılda tutmak hata sayısını ciddi azaltır.

| Konu aralığı | Odak |
|---|---|
| 1–20 | Temel sorgulama, veri ekleme/güncelleme/silme, anahtarlar ve transaction |
| 21–40 | JOIN türleri, aggregate fonksiyonlar, filtreler, tablo yapısı ve constraint konuları |
| 41–70 | CTE, window functions, performans, transaction izolasyonu, JSON, full text search ve ileri konular |

---

## Bölüm 1 — Temel ve Orta Seviye Konular

### 1. SELECT

**Ne işe yarar?** Tablodan hangi kolonları okuyacağını seçersin.

**Ne zaman kullanılır?** Raporlama, kontrol ve analiz sorgularının başlangıcıdır.

```sql
SELECT ad, soyad, sehir
FROM musteriler;
```

> `SELECT *` hızlı deneme için iyidir; kalıcı sorgularda ihtiyacın olan kolonları yazmak daha temizdir.

---

### 2. WHERE

**Ne işe yarar?** Satırları koşula göre filtreler.

**Ne zaman kullanılır?** Büyük tabloda doğru satırlara odaklanmanı sağlar.

```sql
SELECT *
FROM siparisler
WHERE toplam_tutar > 1000;
```

> `WHERE` satır seviyesinde çalışır; `GROUP BY` sonrası filtreleme için `HAVING` kullanılır.

---

### 3. JOIN

**Ne işe yarar?** İlişkili tabloları ortak alan üzerinden birleştirir.

**Ne zaman kullanılır?** Müşteri-sipariş, ürün-kategori gibi parçalanmış veriyi anlamlı hale getirir.

```sql
SELECT m.ad, s.toplam_tutar
FROM musteriler m
JOIN siparisler s ON s.musteri_id = m.id;
```

> `JOIN` koşulunu yazmayı unutmak çarpım etkisi oluşturabilir ve satır sayısını patlatır.

---

### 4. GROUP BY

**Ne işe yarar?** Satırları gruplar ve grup bazlı özet üretir.

**Ne zaman kullanılır?** Şehir bazlı müşteri sayısı, ürün bazlı satış gibi özetlerde kullanılır.

```sql
SELECT sehir, COUNT(*) AS musteri_sayisi
FROM musteriler
GROUP BY sehir;
```

> `SELECT` içinde aggregate olmayan her kolon genelde `GROUP BY` içinde de yer almalıdır.

---

### 5. ORDER BY

**Ne işe yarar?** Sonuçları artan veya azalan sıralar.

**Ne zaman kullanılır?** En pahalı ürünler, en yeni siparişler, en çok satanlar gibi listelerde kullanılır.

```sql
SELECT ad, fiyat
FROM urunler
ORDER BY fiyat DESC;
```

> `DESC` azalan, `ASC` artan sıralama yapar. `ASC` varsayılandır.

---

### 6. INDEX

**Ne işe yarar?** Arama ve `JOIN` performansını artıran veri yapısıdır.

**Ne zaman kullanılır?** `WHERE`, `JOIN`, `ORDER BY` alanlarında sık kullanılan kolonlarda faydalıdır.

```sql
CREATE INDEX idx_siparis_musteri
ON siparisler(musteri_id);
```

> Index okumayı hızlandırır ama `INSERT`/`UPDATE`/`DELETE` işlemlerini biraz yavaşlatabilir.

---

### 7. PRIMARY KEY

**Ne işe yarar?** Tablodaki her satırı benzersiz tanımlar.

**Ne zaman kullanılır?** `id` gibi tekrar etmeyen ana kimlik alanıdır.

```sql
CREATE TABLE musteriler (
  id SERIAL PRIMARY KEY,
  ad TEXT NOT NULL
);
```

> Primary key hem benzersizlik sağlar hem de `NULL` olamaz.

---

### 8. FOREIGN KEY

**Ne işe yarar?** Bir tablodaki alanın başka tablodaki anahtara bağlı olmasını sağlar.

**Ne zaman kullanılır?** Veri tutarlılığı için kullanılır; olmayan müşterinin siparişi girilemez.

```sql
CREATE TABLE siparisler (
  id SERIAL PRIMARY KEY,
  musteri_id INT REFERENCES musteriler(id)
);
```

> Foreign key veri kalitesini korur; silme/güncelleme davranışları için `ON DELETE` / `ON UPDATE` düşünülür.

---

### 9. INSERT

**Ne işe yarar?** Tabloya yeni satır ekler.

**Ne zaman kullanılır?** Yeni müşteri, yeni sipariş, yeni log kaydı oluştururken kullanılır.

```sql
INSERT INTO musteriler(ad, sehir)
VALUES ('Ali', 'Ankara');
```

> Kolon listesini yazmak güvenlidir; tablo yapısı değişse de sorgu daha okunur kalır.

---

### 10. UPDATE

**Ne işe yarar?** Var olan satırları günceller.

**Ne zaman kullanılır?** Adres, fiyat, durum, stok gibi değerleri değiştirmek için kullanılır.

```sql
UPDATE urunler
SET fiyat = fiyat * 1.10
WHERE kategori = 'Elektronik';
```

> `WHERE` unutulursa tablodaki tüm satırlar güncellenir. Önce `SELECT` ile kontrol etmek iyi alışkanlıktır.

---

### 11. DELETE

**Ne işe yarar?** Satır siler.

**Ne zaman kullanılır?** Yanlış, geçersiz veya artık gerekli olmayan kayıtları kaldırır.

```sql
DELETE FROM sepet
WHERE kullanici_id = 10 AND urun_id = 5;
```

> `DELETE` de `WHERE` ister. Kalıcı silme yerine bazı sistemlerde soft delete kullanılır.

---

### 12. HAVING

**Ne işe yarar?** Gruplandırılmış sonuçları filtreler.

**Ne zaman kullanılır?** `COUNT`, `SUM`, `AVG` gibi özet sonuçlar üzerinden koşul kurarsın.

```sql
SELECT musteri_id, SUM(toplam_tutar) AS toplam
FROM siparisler
GROUP BY musteri_id
HAVING SUM(toplam_tutar) > 5000;
```

> `WHERE` gruplamadan önce, `HAVING` gruplamadan sonra çalışır.

---

### 13. SUBQUERY

**Ne işe yarar?** Bir sorgunun içinde başka sorgu kullanmaktır.

**Ne zaman kullanılır?** Önce bir liste/sonuç bulup dış sorguda kullanmak için kullanılır.

```sql
SELECT ad
FROM musteriler
WHERE id IN (
  SELECT musteri_id FROM siparisler
);
```

> Subquery okunabilir olabilir; performans için bazen `JOIN` veya `EXISTS` daha iyi olur.

---

### 14. DISTINCT

**Ne işe yarar?** Tekrar eden değerleri teke indirir.

**Ne zaman kullanılır?** Tekil şehirler, tekil kategoriler, tekrar etmeyen kullanıcı listeleri için kullanılır.

```sql
SELECT DISTINCT sehir
FROM musteriler;
```

> `DISTINCT` tüm seçilen kolon kombinasyonuna bakar; sadece tek kolona değil.

---

### 15. LIMIT

**Ne işe yarar?** Döndürülecek satır sayısını sınırlar.

**Ne zaman kullanılır?** Deneme, sayfalama ve ilk N sonucu görmek için kullanılır.

```sql
SELECT *
FROM siparisler
ORDER BY created_at DESC
LIMIT 10;
```

> `LIMIT` genelde `ORDER BY` ile birlikte anlamlıdır; aksi halde hangi 10 satırın geleceği belirsiz olabilir.

---

### 16. UNION

**Ne işe yarar?** İki sorgu sonucunu alt alta birleştirir.

**Ne zaman kullanılır?** Benzer kolon yapısına sahip listeleri tek sonuç setinde toplar.

```sql
SELECT email FROM musteriler
UNION
SELECT email FROM tedarikciler;
```

> `UNION` tekrarlı satırları kaldırır. Hepsini korumak için `UNION ALL` kullanılır.

---

### 17. CASE

**Ne işe yarar?** SQL içinde if-else benzeri koşullu ifade yazar.

**Ne zaman kullanılır?** Raporlarda sınıflandırma ve etiketleme için çok kullanılır.

```sql
SELECT ad,
  CASE
    WHEN toplam_harcama >= 10000 THEN 'VIP'
    ELSE 'Standart'
  END AS musteri_tipi
FROM musteriler;
```

> `CASE` kolon üretir; `WHERE`, `SELECT`, `ORDER BY` içinde kullanılabilir.

---

### 18. VIEW

**Ne işe yarar?** Kaydedilmiş sorgu gibi davranan sanal tablodur.

**Ne zaman kullanılır?** Karmaşık sorguları basitleştirmek ve raporları standartlaştırmak için kullanılır.

```sql
CREATE VIEW aktif_musteriler AS
SELECT * FROM musteriler
WHERE aktif = TRUE;
```

> View veri kopyalamaz; sorgulandığında alttaki tablolardan okur.

---

### 19. TRIGGER

**Ne işe yarar?** Tabloda olay olunca otomatik çalışan mekanizmadır.

**Ne zaman kullanılır?** Log tutma, denetim, otomatik alan güncelleme gibi işlerde kullanılır.

```sql
-- PostgreSQL'de önce function, sonra trigger yazılır
CREATE TRIGGER trg_log
AFTER INSERT ON siparisler
FOR EACH ROW EXECUTE FUNCTION log_siparis();
```

> Trigger güçlüdür ama gizli iş mantığı yaratabilir; dikkatli ve dökümante kullanılmalıdır.

---

### 20. TRANSACTION

**Ne işe yarar?** Birden fazla işlemi tek bir bütün olarak çalıştırır.

**Ne zaman kullanılır?** Para transferi gibi yarım kalmaması gereken işlemlerde kullanılır.

```sql
BEGIN;
UPDATE hesaplar SET bakiye = bakiye - 100 WHERE id = 1;
UPDATE hesaplar SET bakiye = bakiye + 100 WHERE id = 2;
COMMIT;
```

> Hata olursa `ROLLBACK` ile tüm işlemleri geri alırsın.

---

### 21. INNER JOIN

**Ne işe yarar?** Sadece iki tabloda da eşleşen satırları getirir.

**Ne zaman kullanılır?** Siparişi olan müşterileri görmek gibi eşleşme şart olan raporlarda kullanılır.

```sql
SELECT m.ad, s.id
FROM musteriler m
INNER JOIN siparisler s ON s.musteri_id = m.id;
```

> `JOIN` yazdığında çoğu veritabanında varsayılan `INNER JOIN`'dir.

---

### 22. LEFT JOIN

**Ne işe yarar?** Sol tablodaki tüm satırları, sağdan eşleşenleri getirir.

**Ne zaman kullanılır?** Siparişi olmayan müşterileri de görmek istediğinde kullanılır.

```sql
SELECT m.ad, s.id AS siparis_id
FROM musteriler m
LEFT JOIN siparisler s ON s.musteri_id = m.id;
```

> Sağ tarafta eşleşme yoksa kolonlar `NULL` gelir.

---

### 23. RIGHT JOIN

**Ne işe yarar?** Sağ tablodaki tüm satırları, soldan eşleşenleri getirir.

**Ne zaman kullanılır?** `LEFT JOIN`'in ters yönlüsüdür.

```sql
SELECT m.ad, s.id
FROM musteriler m
RIGHT JOIN siparisler s ON s.musteri_id = m.id;
```

> Okunabilirlik için çoğu ekip `RIGHT JOIN` yerine tablo sıralamasını değiştirip `LEFT JOIN` kullanır.

---

### 24. FULL OUTER JOIN

**Ne işe yarar?** İki tablodaki tüm satırları getirir; eşleşenleri yan yana koyar.

**Ne zaman kullanılır?** İki kaynağı karşılaştırma ve eksik eşleşmeleri bulma işlerinde kullanılır.

```sql
SELECT a.id, b.id
FROM kaynak_a a
FULL OUTER JOIN kaynak_b b ON b.id = a.id;
```

> Her veritabanında desteklenmeyebilir; MySQL'de alternatif çözüm gerekir.

---

### 25. COUNT

**Ne işe yarar?** Satır veya değer sayar.

**Ne zaman kullanılır?** Raporların en temel aggregate fonksiyonudur.

```sql
SELECT COUNT(*) AS toplam_siparis
FROM siparisler;
```

> `COUNT(*)` satır sayar; `COUNT(kolon)` `NULL` olmayan değerleri sayar.

---

### 26. SUM

**Ne işe yarar?** Sayısal değerleri toplar.

**Ne zaman kullanılır?** Ciro, toplam stok, toplam ödeme gibi hesaplarda kullanılır.

```sql
SELECT SUM(toplam_tutar) AS ciro
FROM siparisler
WHERE durum = 'tamamlandi';
```

> `NULL` değerler toplama dahil edilmez; gerekirse `COALESCE` kullanılır.

---

### 27. AVG

**Ne işe yarar?** Ortalama hesaplar.

**Ne zaman kullanılır?** Ortalama sepet tutarı, ortalama yaş, ortalama puan gibi raporlarda kullanılır.

```sql
SELECT AVG(toplam_tutar) AS ortalama_sepet
FROM siparisler;
```

> `AVG` `NULL` değerleri yok sayar.

---

### 28. MIN / MAX

**Ne işe yarar?** En küçük ve en büyük değeri bulur.

**Ne zaman kullanılır?** En erken tarih, en son sipariş, en ucuz ürün gibi sorgularda kullanılır.

```sql
SELECT MIN(fiyat) AS en_ucuz, MAX(fiyat) AS en_pahali
FROM urunler;
```

> Tarihlerde `MIN` en eskiyi, `MAX` en yeni tarihi verir.

---

### 29. BETWEEN

**Ne işe yarar?** İki sınır arasını filtreler.

**Ne zaman kullanılır?** Tarih, fiyat, yaş aralıklarında pratik kullanılır.

```sql
SELECT *
FROM siparisler
WHERE toplam_tutar BETWEEN 100 AND 500;
```

> `BETWEEN` iki sınırı da dahil eder.

---

### 30. IN

**Ne işe yarar?** Bir kolonun verilen listede olup olmadığını kontrol eder.

**Ne zaman kullanılır?** Birden fazla eşitlik koşulunu temiz yazmak için kullanılır.

```sql
SELECT *
FROM musteriler
WHERE sehir IN ('Ankara', 'Istanbul', 'Izmir');
```

> `IN` listesi subquery ile de doldurulabilir.

---

### 31. LIKE

**Ne işe yarar?** Metin desenine göre arama yapar.

**Ne zaman kullanılır?** İsim, email, açıklama gibi alanlarda basit arama yapar.

```sql
SELECT *
FROM musteriler
WHERE ad LIKE 'A%';
```

> `%` herhangi uzunlukta karakter, `_` tek karakter anlamına gelir.

---

### 32. IS NULL

**Ne işe yarar?** `NULL` değeri kontrol eder.

**Ne zaman kullanılır?** Eksik telefon, atanmış olmayan teslimat tarihi gibi kayıtları bulur.

```sql
SELECT *
FROM musteriler
WHERE telefon IS NULL;
```

> `NULL = NULL` yazılmaz; `IS NULL` veya `IS NOT NULL` kullanılır.

---

### 33. EXISTS

**Ne işe yarar?** Alt sorguda en az bir satır var mı diye bakar.

**Ne zaman kullanılır?** İlişkili kaydın varlığını kontrol etmek için güçlüdür.

```sql
SELECT m.ad
FROM musteriler m
WHERE EXISTS (
  SELECT 1 FROM siparisler s WHERE s.musteri_id = m.id
);
```

> `EXISTS` genelde varlık kontrolünde `IN`'e göre daha niyet belirgin ve performanslı olabilir.

---

### 34. ALTER TABLE

**Ne işe yarar?** Tablo yapısını değiştirir.

**Ne zaman kullanılır?** Kolon ekleme, kolon tipi değiştirme, constraint ekleme gibi işlerde kullanılır.

```sql
ALTER TABLE musteriler
ADD COLUMN dogum_tarihi DATE;
```

> Canlı sistemde `ALTER TABLE` dikkat ister; büyük tabloda kilit ve süre sorunu yaratabilir.

---

### 35. DROP TABLE

**Ne işe yarar?** Tabloyu tamamen siler.

**Ne zaman kullanılır?** Test tablosunu kaldırmak veya eski yapıları temizlemek için kullanılır.

```sql
DROP TABLE eski_raporlar;
```

> `DROP` geri dönüşü zor bir işlemdir. Üretimde mutlaka yedek ve yetki kontrolü gerekir.

---

### 36. CREATE TABLE

**Ne işe yarar?** Yeni tablo oluşturur.

**Ne zaman kullanılır?** Veriyi düzenli saklamak için kolonlar ve veri tipleri belirlenir.

```sql
CREATE TABLE urunler (
  id SERIAL PRIMARY KEY,
  ad TEXT NOT NULL,
  fiyat NUMERIC(10,2)
);
```

> Tablo tasarımı sonradan tüm sorgu kalitesini etkiler.

---

### 37. DEFAULT

**Ne işe yarar?** Kolon için varsayılan değer tanımlar.

**Ne zaman kullanılır?** Kayıt eklerken belirtilmeyen alanlara otomatik değer vermek için kullanılır.

```sql
CREATE TABLE kullanicilar (
  id SERIAL PRIMARY KEY,
  aktif BOOLEAN DEFAULT TRUE
);
```

> `created_at` için `DEFAULT now()` çok yaygın kullanılır.

---

### 38. UNIQUE

**Ne işe yarar?** Aynı değerin tekrar girmesini engeller.

**Ne zaman kullanılır?** Email, kullanıcı adı, fatura no gibi tekil olması gereken alanlarda kullanılır.

```sql
CREATE TABLE kullanicilar (
  id SERIAL PRIMARY KEY,
  email TEXT UNIQUE
);
```

> `UNIQUE` constraint veri kalitesini uygulama koduna bırakmadan veritabanında korur.

---

### 39. CHECK

**Ne işe yarar?** Kolona veya satıra kural koyar.

**Ne zaman kullanılır?** Negatif fiyat, geçersiz yaş gibi hatalı verileri engeller.

```sql
CREATE TABLE urunler (
  fiyat NUMERIC CHECK (fiyat >= 0)
);
```

> `CHECK`, veri kurallarını merkezi ve güvenli hale getirir.

---

### 40. SERIAL / AUTO INCREMENT

**Ne işe yarar?** Otomatik artan id üretir.

**Ne zaman kullanılır?** Her kayda benzersiz sayısal kimlik vermek için kullanılır.

```sql
CREATE TABLE musteriler (
  id SERIAL PRIMARY KEY,
  ad TEXT NOT NULL
);
```

> PostgreSQL'de modern alternatif `GENERATED AS IDENTITY` yapısıdır.

---

## Bölüm 2 — Orta-İleri ve İleri SQL Konuları

### 41. CTE — WITH

**Ne işe yarar?** Sorgu içinde geçici isimlendirilmiş sonuç oluşturur.

**Ne zaman kullanılır?** Karmaşık sorguları adım adım okunur hale getirir.

```sql
WITH aylik_satis AS (
  SELECT date_trunc('month', created_at) AS ay, SUM(toplam_tutar) AS ciro
  FROM siparisler
  GROUP BY 1
)
SELECT * FROM aylik_satis
ORDER BY ay;
```

> CTE, sorguyu bölümlere ayırmak için harikadır. Bazı veritabanlarında optimizasyon davranışı değişebilir.

---

### 42. Recursive CTE

**Ne işe yarar?** Kendi sonucuna tekrar başvuran CTE'dir.

**Ne zaman kullanılır?** Kategori ağacı, organizasyon şeması, graph benzeri hiyerarşilerde kullanılır.

```sql
WITH RECURSIVE kategori_agaci AS (
  SELECT id, parent_id, ad, 1 AS seviye
  FROM kategoriler WHERE parent_id IS NULL
  UNION ALL
  SELECT k.id, k.parent_id, k.ad, ka.seviye + 1
  FROM kategoriler k
  JOIN kategori_agaci ka ON k.parent_id = ka.id
)
SELECT * FROM kategori_agaci;
```

> Recursive sorgularda sonsuz döngü riskine karşı seviye sınırı veya veri kontrolü düşünülmelidir.

---

### 43. Window Functions

**Ne işe yarar?** Satırları kaybetmeden grup bazlı hesap yapar.

**Ne zaman kullanılır?** Sıralama, küme içinde toplam, hareketli ortalama gibi analizlerde kullanılır.

```sql
SELECT musteri_id, created_at, toplam_tutar,
  SUM(toplam_tutar) OVER (PARTITION BY musteri_id ORDER BY created_at) AS kume_toplam
FROM siparisler;
```

> `GROUP BY` satırları özetler; window function satırları korur.

---

### 44. ROW_NUMBER

**Ne işe yarar?** Her grup içinde sıralı numara verir.

**Ne zaman kullanılır?** Her müşterinin en son siparişini bulmak gibi işlerde kullanılır.

```sql
WITH sirali AS (
  SELECT *, ROW_NUMBER() OVER (PARTITION BY musteri_id ORDER BY created_at DESC) AS rn
  FROM siparisler
)
SELECT * FROM sirali WHERE rn = 1;
```

> Aynı sıralama değerlerinde sonuç deterministik olsun diye `ORDER BY`'a ikinci kolon eklenebilir.

---

### 45. RANK / DENSE_RANK

**Ne işe yarar?** Eşitlik durumunu dikkate alan sıralama fonksiyonlarıdır.

**Ne zaman kullanılır?** Puan tablosu, satış liderleri gibi listelerde kullanılır.

```sql
SELECT urun_id, toplam_satis,
  RANK() OVER (ORDER BY toplam_satis DESC) AS sira
FROM urun_satis_ozet;
```

> `RANK` eşitlikte boşluk bırakır; `DENSE_RANK` boşluk bırakmaz.

---

### 46. LAG / LEAD

**Ne işe yarar?** Önceki veya sonraki satırdaki değeri okur.

**Ne zaman kullanılır?** Aydan aya değişim, önceki fiyatla karşılaştırma gibi analizlerde kullanılır.

```sql
SELECT ay, ciro,
  ciro - LAG(ciro) OVER (ORDER BY ay) AS onceki_aya_gore_fark
FROM aylik_ciro;
```

> Zaman serisi analizlerinde çok kullanışlıdır.

---

### 47. COALESCE

**Ne işe yarar?** İlk `NULL` olmayan değeri döndürür.

**Ne zaman kullanılır?** `NULL` değerleri raporda anlamlı varsayılanlarla göstermek için kullanılır.

```sql
SELECT ad, COALESCE(telefon, 'Telefon yok') AS telefon
FROM musteriler;
```

> `COALESCE` SQL'in en pratik `NULL` yönetimi araçlarından biridir.

---

### 48. NULLIF

**Ne işe yarar?** İki ifade eşitse `NULL` döndürür.

**Ne zaman kullanılır?** Sıfıra bölme hatasını önlemek gibi durumlarda kullanılır.

```sql
SELECT toplam_tutar / NULLIF(urun_adedi, 0) AS ortalama_birim_tutar
FROM siparisler;
```

> `NULLIF(a,b)` → `a = b` ise `NULL`; değilse `a` döndürür.

---

### 49. CAST / Type Conversion

**Ne işe yarar?** Bir veri tipini başka tipe çevirir.

**Ne zaman kullanılır?** Metni sayıya, tarihi metne veya sayıyı metne çevirmek gerekebilir.

```sql
SELECT CAST('2026-05-07' AS DATE) AS tarih;
```

> Yanlış format cast hatası üretir. Veri temizliği önemlidir.

---

### 50. Date Functions

**Ne işe yarar?** Tarihleri parçala, yuvarla veya aralık hesapla.

**Ne zaman kullanılır?** Günlük/aylık raporlama ve zaman filtreleri için kullanılır.

```sql
SELECT date_trunc('month', created_at) AS ay, COUNT(*)
FROM siparisler
GROUP BY 1
ORDER BY 1;
```

> Tarih fonksiyonları veritabanına göre değişir; PostgreSQL, MySQL, SQL Server farklıdır.

---

### 51. String Functions

**Ne işe yarar?** Metinleri birleştirme, parçalama, küçültme/büyütme gibi işlemler yapar.

**Ne zaman kullanılır?** Arama, temizlik ve raporlama formatları için kullanılır.

```sql
SELECT LOWER(TRIM(email)) AS temiz_email
FROM kullanicilar;
```

> Metin temizliği yaparken index kullanımı etkilenebilir; expression index gerekebilir.

---

### 52. Aggregate Filtering

**Ne işe yarar?** Aggregate hesaba koşullu veri dahil eder.

**Ne zaman kullanılır?** Aynı sorguda farklı sayım ve toplamları üretmek için kullanılır.

```sql
SELECT
  COUNT(*) AS toplam,
  COUNT(*) FILTER (WHERE durum = 'tamamlandi') AS tamamlanan
FROM siparisler;
```

> `FILTER` PostgreSQL'de çok temizdir; diğer sistemlerde `CASE` ile yazılabilir.

---

### 53. Conditional Aggregation

**Ne işe yarar?** `SUM`/`COUNT` içinde `CASE` kullanarak koşullu özet üretir.

**Ne zaman kullanılır?** Pivot benzeri raporlarda ve dashboard metriklerinde çok kullanılır.

```sql
SELECT
  SUM(CASE WHEN durum = 'tamamlandi' THEN 1 ELSE 0 END) AS tamamlanan,
  SUM(CASE WHEN durum = 'iptal' THEN 1 ELSE 0 END) AS iptal
FROM siparisler;
```

> Tek sorguda birden fazla metriği hesaplamak için çok pratiktir.

---

### 54. UNION ALL

**Ne işe yarar?** İki sonucu tekrar kontrolü yapmadan birleştirir.

**Ne zaman kullanılır?** Log, arşiv ve canlı tabloyu birlikte okumak gibi durumlarda kullanılır.

```sql
SELECT id, created_at FROM siparisler_2025
UNION ALL
SELECT id, created_at FROM siparisler_2026;
```

> `UNION ALL` genelde `UNION`'dan daha hızlıdır çünkü tekrar silme maliyeti yoktur.

---

### 55. INTERSECT / EXCEPT

**Ne işe yarar?** Kesişim ve fark işlemleri yapar.

**Ne zaman kullanılır?** İki liste arasında ortak veya eksik kayıtları bulmak için kullanılır.

```sql
-- Kesişim
SELECT email FROM liste_a
INTERSECT
SELECT email FROM liste_b;

-- Fark
SELECT email FROM liste_a
EXCEPT
SELECT email FROM liste_b;
```

> Veri karşılaştırma ve mutabakat işlerinde çok kullanışlıdır.

---

### 56. UPSERT

**Ne işe yarar?** Kayıt varsa güncelle, yoksa ekle mantığıdır.

**Ne zaman kullanılır?** Tekil anahtara göre tekrarlı veri girişini yönetir.

```sql
INSERT INTO urun_stok(urun_id, adet)
VALUES (10, 5)
ON CONFLICT (urun_id)
DO UPDATE SET adet = urun_stok.adet + EXCLUDED.adet;
```

> PostgreSQL'de `ON CONFLICT` kullanılır. SQL Server'da `MERGE` alternatif olabilir.

---

### 57. Stored Procedure

**Ne işe yarar?** Veritabanında saklanan işlem bloklarıdır.

**Ne zaman kullanılır?** Tekrarlanan iş kurallarını veritabanında çalıştırmak için kullanılır.

```sql
CALL siparis_kapat(123);
```

> Procedure kullanımı ekip ve mimariye bağlıdır. Aşırı iş mantığı veritabanını karmaşıklaştırabilir.

---

### 58. User Defined Function

**Ne işe yarar?** Veritabanında kendi fonksiyonunu tanımlarsın.

**Ne zaman kullanılır?** Tekrar eden hesaplamaları merkezi hale getirir.

```sql
CREATE FUNCTION kdvli_fiyat(fiyat NUMERIC)
RETURNS NUMERIC AS $$
  SELECT fiyat * 1.20;
$$ LANGUAGE SQL;
```

> Fonksiyonlar okunabilirlik sağlar; ama performans ve yan etki konularına dikkat edilir.

---

### 59. Materialized View

**Ne işe yarar?** View sonucunu fiziksel olarak saklar.

**Ne zaman kullanılır?** Ağır raporları hızlandırmak için kullanılır.

```sql
CREATE MATERIALIZED VIEW aylik_ciro AS
SELECT date_trunc('month', created_at) AS ay, SUM(toplam_tutar) AS ciro
FROM siparisler
GROUP BY 1;

REFRESH MATERIALIZED VIEW aylik_ciro;
```

> Normal view her okumada hesaplar; materialized view saklar ama güncelleme ister.

---

### 60. Normalization

**Ne işe yarar?** Veriyi tekrar azaltacak şekilde tablolara ayırma prensibidir.

**Ne zaman kullanılır?** Müşteri, sipariş, ürün gibi varlıkları doğru modellemek için kullanılır.

```sql
-- Müşteri bilgisi sipariş tablosunda tekrar tekrar tutulmaz
-- siparisler.musteri_id -> musteriler.id
```

> Aşırı normalizasyon sorguları zorlaştırabilir; raporlama için bazen denormalizasyon kullanılır.

---

### 61. Denormalization

**Ne işe yarar?** Performans veya raporlama için bazı verileri bilinçli tekrar tutmaktır.

**Ne zaman kullanılır?** Dashboard, analitik tablo, cache tablo gibi yerlerde kullanılır.

```sql
-- siparis_ozet tablosunda musteri_adi ve toplam_tutar hazır tutulabilir
```

> Tutarlılık riski vardır; verinin nasıl güncelleneceği net olmalıdır.

---

### 62. Query Optimization

**Ne işe yarar?** Sorguyu daha hızlı ve az maliyetli çalışacak hale getirmektir.

**Ne zaman kullanılır?** Yavaş raporlar, ağır `JOIN`'ler, büyük tablolarla çalışırken gerekir.

```sql
EXPLAIN ANALYZE
SELECT * FROM siparisler WHERE musteri_id = 10;
```

> Optimizasyon tahminle değil ölçümle yapılır. `EXPLAIN` ana araçtır.

---

### 63. Execution Plan — EXPLAIN

**Ne işe yarar?** Veritabanının sorguyu nasıl çalıştıracağını gösterir.

**Ne zaman kullanılır?** Index kullanıldı mı, full scan mı yapıldı, `JOIN` sırası ne gibi sorulara cevap verir.

```sql
EXPLAIN ANALYZE
SELECT *
FROM siparisler
WHERE created_at >= CURRENT_DATE - INTERVAL '30 days';
```

> `ANALYZE` sorguyu gerçekten çalıştırır; üretimde dikkatli kullanılır.

---

### 64. Partitioning

**Ne işe yarar?** Büyük tabloyu mantıksal/fiziksel parçalara ayırır.

**Ne zaman kullanılır?** Yıllık/aylık log veya sipariş tablolarında performans ve bakım kolaylığı sağlar.

```sql
CREATE TABLE siparisler (
  id BIGINT,
  created_at DATE NOT NULL
) PARTITION BY RANGE (created_at);
```

> Doğru partition anahtarı seçilmezse faydası azalır.

---

### 65. ACID

**Ne işe yarar?** Transaction güvenilirliğinin dört temel ilkesidir.

**Ne zaman kullanılır?** Finans, stok, sipariş gibi tutarlılık gereken sistemlerde kritiktir.

```
Atomicity  : Ya hepsi olur ya hiçbiri
Consistency: Kurallar bozulmaz
Isolation  : İşlemler birbirini bozmaz
Durability : Commit edilen veri kalıcıdır
```

> ACID mantığını bilmek transaction, lock ve hata yönetimini anlamayı kolaylaştırır.

---

### 66. Isolation Levels

**Ne işe yarar?** Aynı anda çalışan transaction'ların birbirini nasıl göreceğini belirler.

**Ne zaman kullanılır?** Dirty read, non-repeatable read, phantom read gibi problemleri kontrol eder.

```sql
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
BEGIN;
-- islemler
COMMIT;
```

> Yüksek izolasyon daha fazla güvenlik ama daha fazla kilit/performans maliyeti getirebilir.

---

### 67. Locks

**Ne işe yarar?** Veriye aynı anda erişimde tutarlılık için kilit mekanizmasıdır.

**Ne zaman kullanılır?** Aynı kaydı iki kişi güncellerken çarpışmayı önler.

```sql
SELECT *
FROM hesaplar
WHERE id = 1
FOR UPDATE;
```

> Kilitler doğaldır; uzun transaction deadlock ve bekleme sorunu yaratabilir.

---

### 68. Deadlock

**Ne işe yarar?** İki transaction birbirinin kilidini bekleyince oluşur.

**Ne zaman kullanılır?** Yoğun güncelleme yapan sistemlerde karşına çıkabilir.

```sql
-- Çözüm prensibi:
-- Kayıtları her transaction'da aynı sırayla kilitle.
```

> Deadlock tamamen yok edilemeyebilir; uygulama retry mantığı içermelidir.

---

### 69. JSON SQL

**Ne işe yarar?** JSON alanları içindeki veriyi sorgular.

**Ne zaman kullanılır?** Esnek şemalı ek bilgiler, event payload'ları, API cevapları için kullanılır.

```sql
SELECT data->>'email' AS email
FROM events
WHERE data->>'type' = 'signup';
```

> JSON esneklik sağlar ama her şeyi JSON yapmak relational gücü azaltır.

---

### 70. Full Text Search

**Ne işe yarar?** Metin içinde kelime bazlı etkili arama yapar.

**Ne zaman kullanılır?** Makale, ürün açıklaması, destek kaydı gibi alanlarda kullanılır.

```sql
SELECT *
FROM makaleler
WHERE to_tsvector('simple', baslik || ' ' || icerik) @@ plainto_tsquery('sql');
```

> `LIKE '%kelime%'` basit arama için yeterli olabilir; ciddi arama için full text search düşünülür.

---

## Mini Cheat Sheet

| İhtiyaç | Kullanılacak konu |
|---|---|
| Satır filtreleme | `WHERE` |
| Grup filtreleme | `HAVING` |
| Eşleşenleri getir | `INNER JOIN` |
| Eşleşmeyenleri de koru | `LEFT JOIN` / `FULL OUTER JOIN` |
| Tekrarları kaldır | `DISTINCT` / `UNION` |
| Tüm tekrarlarla birleştir | `UNION ALL` |
| Grup özetleri | `GROUP BY` + `COUNT`/`SUM`/`AVG` |
| Satırları kaybetmeden analiz | Window Functions |
| Karmaşık sorguyu okunur yap | CTE |
| Performans incele | `EXPLAIN ANALYZE` |
| Kayıt varsa güncelle | `UPSERT` |
| Güvenli çoklu işlem | `TRANSACTION` + `COMMIT`/`ROLLBACK` |

---

> **Çalışma önerisi:** Her konu için önce örneği çalıştır, sonra tablo ve kolon adlarını kendi verine göre değiştir. En hızlı öğrenme yolu, aynı kavramı farklı senaryolarda tekrar yazmaktır.
