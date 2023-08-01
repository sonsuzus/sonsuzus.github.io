---
title:  SQL Programlama SELECT
author: sonsuz
date: 2023-08-01 23:34:21 +0300
categories: [Program,SQL]
tags: [sql,select,programlama,veri,veri tabanı,sorgu]
---


SELECT komutu bir veritabanında yer alan bir veya daha fazla tablodan istenen satır değerlerini almak için kullanılır.

SELECT komutu ile elde edilen veriler yine bir tabloya aktarılarak üzerinde işlem yapılır.

SELECT komutunun genel yazım şekli aşağıdadır. İlk satır sadece seçilen sütunları, ikinci satır ise tüm sütunları seçer:

SELECT sütun\_adı1, sütun\_adı2, ... FROM tablo\_adı

SELECT \* FROM tablo\_adı

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

Eğer aşağıdaki komutu kullanırsanız; personel tablosunda yer alan tüm sütunlarda yer alan veriler sonuç tablosuna aktarılır:

SELECT \* FROM personel

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

Eğer aşağıdaki komutu kullanırsanız; personel tablosunun ilk 3 sütununda yer alan veriler sonuç tablosuna aktarılır:

SELECT Adi, Soyadi, Gorevi FROM personel

Sonuç

| Adi | Soyadi | Gorevi |
| --- | --- | --- |
| Ahmet | Kara | Öğretmen |
| Mehmet | Ertürk | Öğretmen |
| Serdar | Şenel | Memur |
| Metin | Gökay | Memur |
| Mehmet | Keskin | Öğrenci |
| Seyfi | Coşar | Öğrenci |
| Cihan | Özkan | Öğrenci |

## SELECT WHERE kullanımı

WHERE yapısı bir tabloda yer alan kayıtlardan belirli bir koşula uygun olanları almaya yarar.

WHERE genel yapısı aşağıdaki şekildedir:

SELECT sütun\_adı1, sütun\_adı2, ... FROM tablo\_adı WHERE sütun\_adı işlemci değer 

Eğer aşağıdaki komutu kullanırsanız; sadece personel tablosunda yer alan öğretmenler sonuç tablosuna aktarılır:

SELECT \* FROM personel WHERE Gorevi='Öğretmen'

Sonuç

| Adi | Soyadi | Gorevi | Memleketi | DTarihi |
| --- | --- | --- | --- | --- |
| Ahmet | Kara | Öğretmen | Sinop | 27.06.1980 |
| Mehmet | Ertürk | Öğretmen | Manisa | 05.02.1972 |

Eğer aşağıdaki komutu kullanırsanız; personel tablosundaki "Mehmet" isimli kayıtlar sonuç tablosuna aktarılır:

SELECT \* FROM personel WHERE Adi='Mehmet'

Sonuç

| Adi | Soyadi | Gorevi | Memleketi | DTarihi |
| --- | --- | --- | --- | --- |
| Mehmet | Ertürk | Öğretmen | Manisa | 05.02.1972 |
| Mehmet | Keskin | Öğrenci | Kars | 28.08.1998 |

## SELECT DISTINCT kullanımı

DISTINCT yapısı bir tablodaki sütunlarda yer alan aynı değerlerden sadece birinin alınmasını sağlar.

DISTINCT genel yapısı aşağıdaki şekildedir:

SELECT DISTINCT sütun\_adı1, sütun\_adı2, ... FROM tablo\_adı

Eğer aşağıdaki komutu kullanırsanız; personel tablosunun ilk sütununda yer alan veriler, birbirine benzer kayıtlar ("Mehmet") sadece bir kez olmak üzere, sonuç tablosuna aktarılır:

SELECT DISTINCT Adi FROM personel

Sonuç

| Adi |
| --- |
| Ahmet |
| Mehmet |
| Serdar |
| Metin |
| Seyfi |
| Cihan |

## SELECT komutu ile AND ve OR işlemcileri kullanımı

AND ve OR kullanarak veritabanından verileri alırken birden fazla koşul tanımlayabilirsiniz.

AND işlemcisini kullandığınızda her iki koşulun da sağlanması gerekir.

OR işlemcisini kullandığınızda sadece tek koşulun da sağlanması yeterlidir.

AND ve OR işlemcilerinin kullanımı aşağıdaki şekildedir:

SELECT sütun\_adı1, sütun\_adı2, ... FROM tablo\_adı WHERE sütun\_adı işlemci değer 

Eğer aşağıdaki komutu kullanırsanız; personel tablosundaki "Mehmet" isimli aynı zamanda "Öğretmen" olan tek kayıt sonuç tablosuna aktarılır:

SELECT \* FROM personel WHERE Adi='Mehmet' AND Gorevi='Öğretmen'

Sonuç

| Adi | Soyadi | Gorevi | Memleketi | DTarihi |
| --- | --- | --- | --- | --- |
| Mehmet | Ertürk | Öğretmen | Manisa | 05.02.1972 |

Eğer aşağıdaki komutu kullanırsanız; personel tablosundaki "Öğretmen" veya "Öğrenci" olan kayıtlar sonuç tablosuna aktarılır:

SELECT \* FROM personel WHERE Gorevi='Öğretmen' OR Gorevi='Öğrenci'

Sonuç

| Adi | Soyadi | Gorevi | Memleketi | DTarihi |
| --- | --- | --- | --- | --- |
| Ahmet | Kara | Öğretmen | Sinop | 27.06.1980 |
| Mehmet | Ertürk | Öğretmen | Manisa | 05.02.1972 |
| Mehmet | Keskin | Öğrenci | Kars | 28.08.1998 |
| Seyfi | Coşar | Öğrenci | Kırşehir | 09.11.1996 |
| Cihan | Özkan | Öğrenci | Sivas | 15.03.1997 |

## SELECT ORDER BY kullanımı

ORDER BY yapısı tablodaki verileri tanımlanan bir sütun değerine göre sıralamak için kullanılır.

ORDER BY yapısı ön tanımlı olarak yükselen sıralama ile verileri sıralar. Azalan sıralama ile sıralama yapmak için DESC kelimesi kullanılır.

ORDER BY genel yapısı aşağıdaki şekildedir:

SELECT sütun\_adı1, sütun\_adı2, ... FROM tablo\_adı ORDER BY sütun\_adı1, sütun\_adı2, ... ASC|DESC

Eğer aşağıdaki komutu kullanırsanız; personel tablosundaki kayıtlar Adi sütununa göre sıralı olarak sonuç tablosuna aktarılır:

SELECT \* FROM personel ORDER BY Adi

Sonuç

| Adi | Soyadi | Gorevi | Memleketi | DTarihi |
| --- | --- | --- | --- | --- |
| Ahmet | Kara | Öğretmen | Sinop | 27.06.1980 |
| Cihan | Özkan | Öğrenci | Sivas | 15.03.1997 |
| Mehmet | Ertürk | Öğretmen | Manisa | 05.02.1972 |
| Mehmet | Keskin | Öğrenci | Kars | 28.08.1998 |
| Metin | Gökay | Memur | İzmir | 07.04.1989 |
| Serdar | Şenel | Memur | Eskişehir | 25.09.1987 |
| Seyfi | Coşar | Öğrenci | Kırşehir | 09.11.1996 |

Eğer aşağıdaki komutu kullanırsanız; personel tablosundaki kayıtlar Soyadi sütununa göre sıralı olarak sonuç tablosuna aktarılır:

SELECT \* FROM personel ORDER BY Soyadi

Sonuç

| Adi | Soyadi | Gorevi | Memleketi | DTarihi |
| --- | --- | --- | --- | --- |
| Cihan | Özkan | Öğrenci | Sivas | 15.03.1997 |
| Seyfi | Coşar | Öğrenci | Kırşehir | 09.11.1996 |
| Mehmet | Ertürk | Öğretmen | Manisa | 05.02.1972 |
| Metin | Gökay | Memur | İzmir | 07.04.1989 |
| Ahmet | Kara | Öğretmen | Sinop | 27.06.1980 |
| Mehmet | Keskin | Öğrenci | Kars | 28.08.1998 |
| Serdar | Şenel | Memur | Eskişehir | 25.09.1987 |
