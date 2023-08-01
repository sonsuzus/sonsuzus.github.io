---
title:  SQL Programlama fonksiyonları
author: sonsuz
date: 2023-08-02 00:23:14 +0300
categories: [Program,SQL]
tags: [sql,programlama,fonksiyon,veri,veri tabanı]
---



Bilgisayarda fonksiyon bir veya daha fazla işlem satırından oluşan kodların bir kod bloğu şeklinde bir isim altında toplanması olarak ifade edilebilir. Böylece, sadece fonksiyon ismi çağrılarak, fonksiyon içinde yer alan kodlar çalıştırılır.

SQL içinde veriler üzerinde işlemler yapmak üzere hazır fonksiyonlar bulunur. SQL fonksiyonları genel olarak 2 gruba ayrılır:

### SQL Çoklu Satır (Aggregate) Fonksiyonları

Bu fonksiyonlar bir sütunda yer alan birden fazla değerler üzerinde yaptığı hesaplamalar sonrası tek bir değer geri verir.

* [AVG() :] Sayısal değer içeren bir tablo sütunundaki değerlerin ortalamasını verir.
* [COUNT() :] Verilen kriterlere uyan tablo satır sayısını verir.
* [FIRST() :] Tabloda belirtilen sütundaki ilk değeri verir.
* [LAST() :] Tabloda belirtilen sütundaki son değeri verir.
* [MAX() :] Tabloda belirtilen sütundaki en büyük değeri verir.
* [MIN() :] Tabloda belirtilen sütundaki en küçük değeri verir.
* [SUM() :] Sayısal değer içeren bir tablo sütunundaki değerlerin toplamını verir.

### SQL Sayısal (Scalar) Fonksiyonları

Bu fonksiyonlar bir sütunda yer alan tek bir değere işlem yapar ve tek bir değer geri verir.

* [LCASE() :] Bir alan değerini küçük harfe çevirir.
* [LEN() :] Bir metin alanının uzunluğunu verir.
* [MID() :] Bir metin alanındaki karakterlerin bir kısmını elde etmek kullanılır.
* [NOW() :] Bilgisayarın tarih ve saat değerlerini verir.
* [FORMAT() :] Bir veri alanının ne şekilde gösterileceğini belirler.
* [ROUND() :] Sayısal bir veri alanının değerini bir tamsayıya yuvarlar.
* [UCASE() :] Bir alan değerini büyük harfe çevirir.

| Mlzid | MlzAdi | Fiyat |
| --- | --- | --- |
| 1 | Masa | 250 |
| 2 | Sandalye | 80 |
| 3 | Kitaplık | 310 |
| 4 | Sehpa | 120 |
| 5 | Koltuk | 250 |

## AVG() fonksiyonu

Sayısal değer içeren bir tablo sütunundaki değerlerin ortalamasını verir.

AVG() fonksiyonunun yazım şekli aşağıdadır:

```sql
SELECT AVG(sütun_adı) FROM tablo_adı
```

Yukarıdaki malzeme adlı örnek tablo üzerinde işlemler yapmaya çalışalım:

Eğer aşağıdaki komutu kullanırsanız; malzeme tablosunun Fiyat sütununda yer alan değerlerin ortalaması sonuç tablosuna aktarılır:

```sql
SELECT AVG(Fiyat) AS OrtFiyat FROM malzeme
```

| OrtFiyat |
| --- |
| 202 |

## COUNT() fonksiyonu

Tanımlanan kriterlere uygun olan satırların sayısını verir.

COUNT() fonksiyonunun farklı kullanışlarına ait yazım şekilleri aşağıdadır:

Bir tablo içinde tanımlanan sütunda bulunan değer sayısını verir. NULL değerler dikkate alınmaz:

SELECT COUNT(sütun\_adı) FROM tablo\_adı

Bir tablo içinde bulunan tüm kayıtların sayısını verir:

SELECT COUNT(\*) FROM tablo\_adı

Bir tablo içinde tanımlanan bir sütundaki farklı değere sahip kayıtların sayısını verir:

SELECT COUNT(DISTINCT sütun\_adı) FROM tablo\_adı

Yukarıdaki malzeme adlı örnek tablo üzerinde işlemler yapmaya çalışalım:

Eğer aşağıdaki komutu kullanırsanız; malzeme tablosunun Fiyat sütununda 200'den büyük değer taşıyan kayıt sayısı (3 adet) sonuç tablosuna aktarılır:

```sql
SELECT COUNT(Fiyat) AS YuksekFiyat FROM malzeme WHERE Fiyat > 200
```

| YuksekFiyat |
| --- |
| 3 |

Eğer aşağıdaki komutu kullanırsanız; malzeme tablosunda yer alan kayıtların sayısı sonuç tablosuna aktarılır:

```sql
SELECT COUNT(*) AS SayiKayit FROM malzeme
```

| SayiKayit |
| --- |
| 5 |

Eğer aşağıdaki komutu kullanırsanız; malzeme tablosunda Fiyat sütununda yer alan farklı değere sahip kayıt sayısı sonuç tablosuna aktarılır:

```sql
SELECT COUNT(DISTINCT Fiyat) AS FarkliKayit FROM malzeme
```

| FarkliFiyat |
| --- |
| 4 |

## FIRST() fonksiyonu

Bir tabloda seçilen sütundaki ilk değeri geri verir.

FIRST() fonksiyonunun yazım şekli aşağıdadır:

```sql
SELECT FIRST(sütun_adı) FROM tablo_adı

```

Yukarıdaki malzeme adlı örnek tablo üzerinde işlemler yapmaya çalışalım:

Eğer aşağıdaki komutu kullanırsanız; malzeme tablosunun MlzAdi sütununda yer alan ilk değer sonuç tablosuna aktarılır:

```sql
SELECT FIRST(MlzAdi) FROM malzeme
```

FIRST() fonksiyonunu desteklemeyen sistemler için:

```sql
SELECT MlzAdi FROM malzeme LIMIT 1
```

| MlzAdi |
| --- |
| Masa |

## LAST() fonksiyonu

Bir tabloda seçilen sütundaki son değeri geri verir.

LAST() fonksiyonunun yazım şekli aşağıdadır:

```sql
SELECT LAST(sütun_adı) FROM tablo_adı

```

Yukarıdaki malzeme adlı örnek tablo üzerinde işlemler yapmaya çalışalım:

Eğer aşağıdaki komutu kullanırsanız; malzeme tablosunun MlzAdi sütununda yer alan son değer sonuç tablosuna aktarılır:

```sql
SELECT LAST(MlzAdi) FROM malzeme
```

LAST() fonksiyonunu desteklemeyen sistemler için:

```sql
SELECT MlzAdi FROM malzeme ORDER BY Mlzid DESC LIMIT 1
```

| MlzAdi |
| --- |
| Koltuk |

## MAX() fonksiyonu

Bir tabloda seçilen sütundaki en büyük değeri geri verir.

MAX() fonksiyonunun yazım şekli aşağıdadır:

```sql
SELECT MAX(sütun_adı) FROM tablo_adı

```

Yukarıdaki malzeme adlı örnek tablo üzerinde işlemler yapmaya çalışalım:

Eğer aşağıdaki komutu kullanırsanız; malzeme tablosunun Fiyat sütununda yer alan en büyük değer sonuç tablosuna aktarılır:

```sql
SELECT MAX(Fiyat) as MaxFiyat FROM malzeme
```

| MaxFiyat |
| --- |
| 310 |

## MIN() fonksiyonu

Bir tabloda seçilen sütundaki en küçük değeri geri verir.

MIN() fonksiyonunun yazım şekli aşağıdadır:

```sql
SELECT MIN(sütun_adı) FROM tablo_adı

```

Yukarıdaki malzeme adlı örnek tablo üzerinde işlemler yapmaya çalışalım:

Eğer aşağıdaki komutu kullanırsanız; malzeme tablosunun Fiyat sütununda yer alan en küçük değer sonuç tablosuna aktarılır:

```sql
SELECT MIN(Fiyat) as MinFiyat FROM malzeme
```

| MinFiyat |
| --- |
| 80 |

## SUM() fonksiyonu

Bir tabloda seçilen sayısal sütundaki değerlerin toplamını geri verir.

SUM() fonksiyonunun yazım şekli aşağıdadır:

```sql
SELECT SUM(sütun_adı) FROM tablo_adı

```

Yukarıdaki malzeme adlı örnek tablo üzerinde işlemler yapmaya çalışalım:

Eğer aşağıdaki komutu kullanırsanız; malzeme tablosunun Fiyat sütununda yer alan değerlerin toplamı sonuç tablosuna aktarılır:

```sql
SELECT SUM(Fiyat) as TopFiyat FROM malzeme
```

| TopFiyat |
| --- |
| 1010 |

## LCASE() fonksiyonu

Bir tabloda seçilen metin alanındaki değeri küçük harfe çevirir.

LCASE() fonksiyonunun yazım şekli aşağıdadır:

```sql
SELECT LCASE(sütun_adı) FROM tablo_adı

```

Yukarıdaki malzeme adlı örnek tablo üzerinde işlemler yapmaya çalışalım:

Eğer aşağıdaki komutu kullanırsanız; malzeme tablosunun MlzAdi sütununda yer alan değerler küçük harfe çevrilerek sonuç tablosuna aktarılır:

```sql
SELECT LCASE(MlzAdi) as MlzKucuk FROM malzeme
```

| MlzKucuk |
| --- |
| masa |
| sandalye |
| kitaplık |
| sehpa |
| koltuk |

## LEN() fonksiyonu

Bir tabloda seçilen alandaki metin değerinin uzunluğunu verir.

LEN() fonksiyonunun yazım şekli aşağıdadır:

```sql
SELECT LEN(sütun_adı) FROM tablo_adı

```

Yukarıdaki malzeme adlı örnek tablo üzerinde işlemler yapmaya çalışalım:

Eğer aşağıdaki komutu kullanırsanız; malzeme tablosunun MlzAdi sütununda yer alan metin değerlerinin uzunluğu sonuç tablosuna aktarılır:

```sql
SELECT LEN(MlzAdi) as MlzAdiUzun FROM malzeme
```

| MlzAdiUzun |
| --- |
| 4 |
| 8 |
| 8 |
| 5 |
| 7 |

## MID() fonksiyonu

Bir tabloda seçilen metin alanından karakterler elde etmeyi sağlar.

MID() fonksiyonunun yazım şekli aşağıdadır:

```sql
SELECT MID(sütun_adı, başlangıç[, uzunluk]) FROM tablo_adı

```

sütun\_adı : Karakterlerin alınacağı alan adı

başlangıç : Veri alanı içindeki başlangıç yeri (En düşük değer 1)

uzunluk : (İsteğe bağlı) Alınacak karakter sayısı. Tanımlanmadığında, metinin geri kalanı alınır.

Yukarıdaki malzeme adlı örnek tablo üzerinde işlemler yapmaya çalışalım:

Eğer aşağıdaki komutu kullanırsanız; malzeme tablosunun MlzAdi sütununda yer alan metin değerlerinin ilk 3 karakteri sonuç tablosuna aktarılır:

```sql
SELECT MID(MlzAdi, 1, 3) as MlzAdiİlkUc FROM malzeme
```

| MlzAdiİlkUc |
| --- |
| Mas |
| San |
| Kit |
| Seh |
| Kol |

## NOW() fonksiyonu

Bilgisayar sistem tarih ve zamanını verir.

NOW() fonksiyonunun yazım şekli aşağıdadır:

```sql
SELECT NOW() FROM tablo_adı

```

Eğer aşağıdaki komutu kullanırsanız; sistem tarih ve zamanı sonuç tablosuna aktarılır:

```sql
SELECT NOW() as TarihSaat
```

| TarihSaat |
| --- |
| 2013-02-15 21:41:24 |

## FORMAT() fonksiyonu

Bir tabloda seçilen veri alanının ekranda gösterilme şeklini belirler.

FORMAT() fonksiyonunun yazım şekli aşağıdadır:

```sql
SELECT FORMAT(sütun_adı, format) FROM tablo_adı
```

sütun\_adı : Gösterilme şekli belirlenecek alan adı

format : Gösterilme şekli

Yukarıdaki malzeme adlı örnek tablo üzerinde işlemler yapmaya çalışalım:

Eğer aşağıdaki komutu kullanırsanız; malzeme tablosunda yer alan değerler sistem tarihi ile birlikte sonuç tablosuna aktarılır:

```sql
SELECT Mlzid, MlzAdi, Fiyat, FORMAT(Now(),'DD.MM.YYYY') as Tarih FROM malzeme
```

| Mlzid | MlzAdi | Fiyat | Tarih |
| --- | --- | --- | --- |
| 1 | Masa | 250 | 16.02.1013 |
| 2 | Sandalye | 80 | 16.02.1013 |
| 3 | Kitaplık | 310 | 16.02.1013 |
| 4 | Sehpa | 120 | 16.02.1013 |
| 5 | Koltuk | 250 | 16.02.1013 |

## ROUND() fonksiyonu

Bir tabloda seçilen sayısal veri alanı değerini tanımlanan ondalık değerine yuvarlar.

ROUND() fonksiyonunun yazım şekli aşağıdadır:

```sql
SELECT ROUND(sütun_adı, ondalık) FROM tablo_adı

```

sütun\_adı : Yuvarlanacak alan adı

ondalık : Ondalık sayısını gösterir.

Yukarıdaki malzeme adlı örnek tablo üzerinde işlemler yapmaya çalışalım:

Eğer aşağıdaki komutu kullanırsanız; malzeme tablosu Fiyat sütununda yer alan değerler yuvarlanarak sonuç tablosuna aktarılır:

```sql
SELECT ROUND(Fiyat, 0) as TamFiyat FROM malzeme
```

| Mlzid | MlzAdi | Fiyat |
| --- | --- | --- |
| 1 | Masa | 250,75 |
| 2 | Sandalye | 80,50 |
| 3 | Kitaplık | 310,25 |
| 4 | Sehpa | 120,75 |
| 5 | Koltuk | 250,25 |

| TamFiyat |
| --- |
| 250 |
| 80 |
| 310 |
| 120 |
| 250 |

## UCASE() fonksiyonu

Bir tabloda seçilen metin alanındaki değeri büyük harfe çevirir.

UCASE() fonksiyonunun yazım şekli aşağıdadır:

```sql
SELECT UCASE(sütun_adı) FROM tablo_adı

```

Yukarıdaki malzeme adlı örnek tablo üzerinde işlemler yapmaya çalışalım:

Eğer aşağıdaki komutu kullanırsanız; malzeme tablosunun MlzAdi sütununda yer alan değerler büyük harfe çevrilerek sonuç tablosuna aktarılır:

SELECT UCASE(MlzAdi) as MlzBuyuk FROM malzeme

| MlzBuyuk |
| --- |
| MASA |
| SANDALYE |
| KİTAPLIK |
| SEHPA |
| KOLTUK |
