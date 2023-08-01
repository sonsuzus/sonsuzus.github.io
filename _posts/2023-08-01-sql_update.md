---
title:  SQL Programlama UPDATE
author: sonsuz
date: 2023-08-01 23:57:16 +0300
categories: [Program,SQL]
tags: [sql,programlama,veri tabanı,veri,update]
---


UPDATE komutu bir veritabanındaki tablolarda yer alan kayıtlarda değişiklik yapmak ve güncellemek için kullanılır. 

UPDATE komutunun genel yazım şekli:

UPDATE tablo\_adı SET sütun\_adı1=deger1, sütun\_adı2=deger2, ... WHERE sütun\_adı=deger

WHERE yapısı kullanılmadığında tüm kayıtlar, kullanıldığında ise sadece koşulu karşılayan kayıtlar güncellenir.

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

Eğer aşağıdaki komutu kullanırsanız; "Seyfi Coşar" isimli kaydın ismi "Nedim Özdemir" olarak değiştirilir:

```sql
UPDATE personel SET Adi='Nedim', Soyadi='Özdemir' WHERE Adi='Seyfi' AND Soyadi='Coşar'
```

Sonuç

| Adi | Soyadi | Gorevi | Memleketi | DTarihi |
| --- | --- | --- | --- | --- |
| Ahmet | Kara | Öğretmen | Sinop | 27.06.1980 |
| Mehmet | Ertürk | Öğretmen | Manisa | 05.02.1972 |
| Serdar | Şenel | Memur | Eskişehir | 25.09.1987 |
| Metin | Gökay | Memur | İzmir | 07.04.1989 |
| Mehmet | Keskin | Öğrenci | Kars | 28.08.1998 |
| Nedim | Özdemir | Öğrenci | Kırşehir | 09.11.1996 |
| Cihan | Özkan | Öğrenci | Sivas | 15.03.1997 |
