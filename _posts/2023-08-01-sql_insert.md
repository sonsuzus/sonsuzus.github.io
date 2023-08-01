---
title:  SQL Programlama INSERT
author: sonsuz
date: 2023-08-01 23:42:57 +0300
categories: [Program,SQL]
tags: [sql,programlama,insert,veri,veri tabanı]
---


INSERT INTO komutu bir veritabanında yer alan tablolara yeni kayıt eklemek için kullanılır. Eklenen her bir kayıt tabloya yeni bir satır ekler.

INSERT INTO komutunu hem sütun adı hem de eklenecek verileri içerecek şekilde veya sadece eklenecek değerleri tanımlayarak kullanabilirsiniz:

Sütun adı ve veri tanımlayarak:

INSERT INTO tablo\_adı (sütun\_adı1, sütun\_adı2, ...) VALUES (deger1, deger2, ...)

Sadece veri tanımlayarak:

INSERT INTO tablo\_adı VALUES (deger1, deger2, ...)

Aşağıdaki personel adlı örnek tablo üzerinde işlemler yapmaya çalışalım:

| Adi | Soyadi | Gorevi | Memleketi | DTarihi |
| --- | --- | --- | --- | --- |
| Ahmet | Kara | Öğretmen | Sinop | 27.06.1980 |
| Mehmet | Ertürk | Öğretmen | Manisa | 05.02.1972 |
| Serdar | Şenel | Memur | Eskişehir | 25.09.1987 |
| Metin | Gökay | Memur | İzmir | 07.04.1989 |
| Mehmet | Keskin | Öğrenci | Kars | 28.08.1998 |
| Seyfi | Coşar | Öğrenci | Kırşehir | 09.11.1996 |
| Cihan | Özkan | Öğrenci | Sivas | 15.03.1997 |

Eğer aşağıdaki komutu kullanırsanız; tanımlanan veriler karşılık gelen sütunlara aktarılarak personel tablosunda yeni bir satır yani kayıt oluşturulur:


```sql
INSERT INTO personel (Adi, Soyadi, Gorevi, Memleketi, DTarihi) VALUES ('Mustafa', 'Karagöz', 'Öğretmen', 'Kastamonu', '1986-04-11')
```

Sonuç

| Adi | Soyadi | Gorevi | Memleketi | DTarihi |
| --- | --- | --- | --- | --- |
| Ahmet | Kara | Öğretmen | Sinop | 27.06.1980 |
| Mehmet | Ertürk | Öğretmen | Manisa | 05.02.1972 |
| Serdar | Şenel | Memur | Eskişehir | 25.09.1987 |
| Metin | Gökay | Memur | İzmir | 07.04.1989 |
| Mehmet | Keskin | Öğrenci | Kars | 28.08.1998 |
| Seyfi | Coşar | Öğrenci | Kırşehir | 09.11.1996 |
| Cihan | Özkan | Öğrenci | Sivas | 15.03.1997 |
| Mustafa | Karagöz | Öğretmen | Kastamonu | 11.04.1986 |

Eğer aşağıdaki komutu kullanırsanız; tanımlanan veriler personel tablosunda yeni bir satır yani kayıt oluşturulur:

```sql
INSERT INTO personel VALUES ('Kerim', 'Sade', 'Öğrenci', 'Isparta', '1997-07-27')
```

Sonuç

| Adi | Soyadi | Gorevi | Memleketi | DTarihi |
| --- | --- | --- | --- | --- |
| Ahmet | Kara | Öğretmen | Sinop | 27.06.1980 |
| Mehmet | Ertürk | Öğretmen | Manisa | 05.02.1972 |
| Serdar | Şenel | Memur | Eskişehir | 25.09.1987 |
| Metin | Gökay | Memur | İzmir | 07.04.1989 |
| Mehmet | Keskin | Öğrenci | Kars | 28.08.1998 |
| Seyfi | Coşar | Öğrenci | Kırşehir | 09.11.1996 |
| Cihan | Özkan | Öğrenci | Sivas | 15.03.1997 |
| Mustafa | Karagöz | Öğretmen | Kastamonu | 11.04.1986 |
| Kerim | Sade | Öğrenci | Isparta | 27.07.1997 |
