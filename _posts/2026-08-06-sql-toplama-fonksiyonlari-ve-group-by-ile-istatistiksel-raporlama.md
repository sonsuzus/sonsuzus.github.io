---
layout: post
title: "SQL Toplama Fonksiyonları ve GROUP BY ile İstatistiksel Raporlama"
math: true
categories: 
  - Bilgi
tags: 
  - SQL
  - GROUP BY
  - Veritabanı
---

Bir e-ticaret veritabanında binlerce sipariş olduğunu düşünün. Satırları tek tek incelemek yerine “Kaç sipariş aldık?”, “Toplam ciro nedir?” veya “En çok hangi kategori kazandırdı?” gibi sorular sormak isteriz. SQL toplama fonksiyonları ve `GROUP BY`, ham verileri anlamlı özetlere dönüştürerek bu sorulara hızlı cevaplar verir.

``

## Toplama fonksiyonlarının teorik mantığı

Toplama, diğer adıyla agregasyon, bir satır kümesini tek bir özet değere indirgeme işlemidir. Örneğin satış tutarlarımız $x_1, x_2, \ldots, x_n$ olsun. Toplam satış şu şekilde hesaplanır:

$$S = \sum_{i=1}^{n} x_i$$

Ortalama satış ise toplamın kayıt sayısına bölünmesidir:

$$\bar{x} = \frac{1}{n}\sum_{i=1}^{n}x_i$$

SQL bu matematiksel işlemleri hazır fonksiyonlarla gerçekleştirir:

| Fonksiyon | Görevi | `NULL` davranışı |
|---|---|---|
| `COUNT(*)` | Tüm satırları sayar | `NULL` içeren satırı da sayar |
| `COUNT(kolon)` | Değeri bulunan satırları sayar | `NULL` değerleri saymaz |
| `SUM(kolon)` | Sayısal değerleri toplar | `NULL` değerleri yok sayar |
| `AVG(kolon)` | Aritmetik ortalama hesaplar | `NULL` değerleri yok sayar |
| `MIN(kolon)` | En küçük değeri bulur | `NULL` değerleri yok sayar |
| `MAX(kolon)` | En büyük değeri bulur | `NULL` değerleri yok sayar |

Elimizde `siparisler` isimli bir tablo bulunduğunu varsayalım. Bu tabloda `id`, `musteri_id`, `kategori`, `tutar`, `durum` ve `siparis_tarihi` sütunları olsun.

```sql
SELECT
    COUNT(*) AS siparis_sayisi,
    SUM(tutar) AS toplam_ciro,
    AVG(tutar) AS ortalama_sepet,
    MIN(tutar) AS en_dusuk_siparis,
    MAX(tutar) AS en_yuksek_siparis
FROM siparisler;
```

Bu sorgu bütün tabloyu tek bir grup kabul eder ve tek satırlık bir rapor üretir. Takma adlar, yani `AS` ifadeleri, sonuç sütunlarını daha okunabilir hâle getirir.

## GROUP BY ile veriyi bölümlere ayırmak

`GROUP BY`, aynı değere sahip satırları mantıksal gruplara ayırır. Toplama fonksiyonu daha sonra her grup için ayrı ayrı çalışır. Kategorilere göre satış raporu şöyle hazırlanabilir:

```sql
SELECT
    kategori,
    COUNT(*) AS siparis_sayisi,
    SUM(tutar) AS toplam_ciro,
    AVG(tutar) AS ortalama_tutar
FROM siparisler
GROUP BY kategori
ORDER BY toplam_ciro DESC;
```

Burada önce satırlar kategoriye göre kovalar gibi ayrılır; ardından her kovanın sayısı, toplamı ve ortalaması hesaplanır. `ORDER BY` ise en yüksek ciroyu listenin başına getirir.

Birden fazla sütunla gruplama yapmak da mümkündür:

```sql
SELECT
    kategori,
    durum,
    COUNT(*) AS adet,
    SUM(tutar) AS toplam
FROM siparisler
GROUP BY kategori, durum;
```

Bu sorguda her benzersiz kategori-durum çifti ayrı bir gruptur. Örneğin “Elektronik-Tamamlandı” ile “Elektronik-İptal” aynı gruba girmez.

## WHERE ve HAVING arasındaki kritik fark

`WHERE`, gruplama yapılmadan önce tekil satırları filtreler. `HAVING` ise gruplama tamamlandıktan sonra oluşan özet sonuçları filtreler.

| Komut | Filtrelediği şey | Çalışma zamanı |
|---|---|---|
| `WHERE` | Ham satırlar | `GROUP BY` öncesi |
| `HAVING` | Oluşturulan gruplar | `GROUP BY` sonrası |

```sql
SELECT
    kategori,
    SUM(tutar) AS toplam_ciro
FROM siparisler
WHERE durum = 'Tamamlandı'
GROUP BY kategori
HAVING SUM(tutar) > 100000
ORDER BY toplam_ciro DESC;
```

Önce yalnızca tamamlanan siparişler seçilir. Ardından kategoriler oluşturulur ve cirosu 100.000’den büyük gruplar gösterilir. `WHERE SUM(tutar) > 100000` yazmak hatalıdır; çünkü `WHERE` çalışırken toplam henüz hesaplanmamıştır.

## NULL değerler ve güvenli hesaplama

`AVG(tutar)`, `NULL` değerleri paydaya katmaz. Eksik tutarları sıfır kabul etmek gerekiyorsa `COALESCE` kullanılabilir:

```sql
SELECT AVG(COALESCE(tutar, 0)) AS ortalama_tutar
FROM siparisler;
```

Ancak sıfır ile bilinmeyen değer aynı şey değildir. Bu dönüşüm raporun anlamını değiştirebileceğinden iş kuralına göre uygulanmalıdır.

Sonuç olarak toplama fonksiyonları veriyi özetler, `GROUP BY` bu özeti kategorilere böler, `WHERE` ham veriyi ve `HAVING` oluşan grupları süzer. Bu araçlar doğru kullanıldığında SQL, yalnızca kayıt saklayan bir dil olmaktan çıkar ve güçlü bir raporlama motoruna dönüşür.
