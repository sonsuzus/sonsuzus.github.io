---
layout: post
title: "SQL ile Nokta Atışı: WHERE, ORDER BY, LIMIT ve Sayfalama"
math: true
categories: 
  - Bilgi
tags: 
  - SQL
  - Veritabanı
  - Sayfalama
---

Bir veritabanında binlerce ürün, kullanıcı veya sipariş bulunabilir. Fakat çoğu zaman bütün satırları değil, belirli koşulları sağlayan küçük bir bölümü görmek isteriz. SQL’in `WHERE`, `ORDER BY` ve `LIMIT` araçları; verileri süzmemizi, anlamlı biçimde sıralamamızı ve yönetilebilir parçalar hâlinde sunmamızı sağlar.
``
## Üç aşamalı veri hunisi

Bu komutları bir huni gibi düşünebiliriz. `WHERE` gereksiz kayıtları eler, `ORDER BY` kalanları düzenler, `LIMIT` ise sonuç kümesinden gösterilecek miktarı belirler.

| Komut | Görevi | Örnek kullanım |
|---|---|---|
| `WHERE` | Koşula uyan satırları filtreler | Aktif kullanıcılar |
| `ORDER BY` | Sonuçları sıralar | En yeni siparişler |
| `LIMIT` | Döndürülen satır sayısını sınırlar | İlk 20 kayıt |
| `OFFSET` | Belirli sayıda satırı atlar | İkinci sayfa |

SQL sorgusunun yazılış sırası ile mantıksal çalışma sırası tamamen aynı değildir. Basitleştirilmiş işlem sırası şöyledir:

$$FROM \rightarrow WHERE \rightarrow ORDER\ BY \rightarrow OFFSET \rightarrow LIMIT$$

Yani veritabanı önce tabloyu değerlendirir, ardından filtreleme ve sıralama yapar. Gösterilecek küçük bölüm en son seçilir.

## WHERE ile doğru kayıtları bulmak

`WHERE`, her satır için doğru veya yanlış sonuç üreten bir koşul çalıştırır. Örneğin fiyatı 500 TL’den yüksek, stokta bulunan elektronik ürünleri bulalım:

```sql
SELECT id, ad, fiyat, stok
FROM urunler
WHERE kategori = 'Elektronik'
  AND fiyat > 500
  AND stok > 0;
```

Buradaki `AND`, bütün koşulların sağlanmasını ister. Seçeneklerden herhangi birinin yeterli olduğu durumlarda `OR`; belirli bir aralık için `BETWEEN`; bir listeyle karşılaştırmak için `IN` kullanılabilir.

```sql
SELECT ad, sehir
FROM musteriler
WHERE sehir IN ('Ankara', 'İzmir', 'Bursa');
```

`NULL` değerleri karşılaştırırken `= NULL` kullanılmaz. Bunun yerine `IS NULL` veya `IS NOT NULL` yazılmalıdır. Bu küçük ayrıntı, sessizce boş sonuç döndüren sorguların klasik sebebidir.

## ORDER BY ile düzen kurmak

Sıralama belirtilmezse kayıtların geliş sırası garanti edilmez. Bu nedenle özellikle sayfalama sırasında `ORDER BY` kullanmak şarttır.

```sql
SELECT id, ad, fiyat
FROM urunler
WHERE stok > 0
ORDER BY fiyat DESC, id ASC
LIMIT 10;
```

`DESC` büyükten küçüğe, `ASC` ise küçükten büyüğe sıralar. Fiyatların eşit olması durumunda `id ASC` devreye girerek kararlı ve tekrarlanabilir bir sıra oluşturur.

## LIMIT ve OFFSET ile sayfalama

Bir sayfada $s$ kayıt gösterilsin ve sayfa numarası $p$ olsun. Atlanacak kayıt sayısı şu formülle hesaplanır:

$$OFFSET = (p - 1) \times s$$

Örneğin her sayfada 20 kayıt varsa üçüncü sayfa için $OFFSET=(3-1)\times20=40$ olur:

```sql
SELECT id, ad, olusturma_tarihi
FROM kullanicilar
WHERE aktif = TRUE
ORDER BY olusturma_tarihi DESC, id DESC
LIMIT 20 OFFSET 40;
```

Bu sorgu ilk 40 sonucu atlar ve sonraki 20 kaydı getirir. Toplam sayfa sayısı ise toplam kayıt sayısı $n$ olmak üzere şöyle bulunur:

$$toplam\_sayfa = \left\lceil \frac{n}{s} \right\rceil$$

Toplam kayıt için aynı filtreyle `COUNT(*)` sorgusu çalıştırılabilir.

## Büyük tablolarda performans

`OFFSET` kullanımı basittir; ancak milyonlarca satırda veritabanı atlanan kayıtları yine değerlendirebilir. Derin sayfalarda anahtar tabanlı sayfalama daha hızlıdır:

```sql
SELECT id, ad
FROM urunler
WHERE id > 5000
ORDER BY id ASC
LIMIT 20;
```

| Yöntem | Avantaj | Dezavantaj |
|---|---|---|
| `LIMIT/OFFSET` | Sayfa numarasına geçiş kolaydır | Büyük offset değerleri yavaşlayabilir |
| Anahtar tabanlı | Hızlı ve tutarlı ilerler | Rastgele sayfaya geçmek zordur |

Son olarak filtrelenen ve sıralanan sütunlara uygun indeksler eklemek performansı ciddi ölçüde artırır. Kısacası doğru koşul, kararlı sıralama ve uygun sayfalama birleştiğinde SQL, veri okyanusunda aradığınız kaydı oltayla değil radar sistemiyle bulur.
