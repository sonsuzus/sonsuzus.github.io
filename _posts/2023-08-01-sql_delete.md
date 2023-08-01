---
title:  SQL Programlama DELETE
author: sonsuz
date: 2023-08-01 23:59:02 +0300
categories: [Program,SQL]
tags: [sql,programlama,delete,veri,veri tabanı]
---


DELETE komutu bir veritabanındaki tablolarda yer alan kayıtları silmek için kullanılır.

DELETE komutunun genel yazım şekli:

DELETE FROM tablo\_adı WHERE sütun\_adı=deger

WHERE yapısı kullanılmadığında tüm kayıtlar, kullanıldığında ise sadece koşulu karşılayan kayıtlar silinir.

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

Eğer aşağıdaki komutu kullanırsanız; "Seyfi Coşar" isimli kayıt silinir:

```sql
DELETE FROM personel WHERE Adi='Seyfi' AND Soyadi='Coşar'
```

Sonuç

| Adi | Soyadi | Gorevi | Memleketi | DTarihi |
| --- | --- | --- | --- | --- |
| Ahmet | Kara | Öğretmen | Sinop | 27.06.1980 |
| Mehmet | Ertürk | Öğretmen | Manisa | 05.02.1972 |
| Serdar | Şenel | Memur | Eskişehir | 25.09.1987 |
| Metin | Gökay | Memur | İzmir | 07.04.1989 |
| Mehmet | Keskin | Öğrenci | Kars | 28.08.1998 |
| Cihan | Özkan | Öğrenci | Sivas | 15.03.1997 |
