---
title:  SQL Programlama CREATE
author: sonsuz
date: 2023-08-02 00:02:07 +0300
categories: [Program,SQL]
tags: [sql,programlama,create,tablo,veri,veri tabanı]
---


CREATE DATABASE komutu veritabanı oluşturmak için kullanılır.

CREATE DATABASE komutunun genel yazım şekli:

CREATE DATABASE veritabanı\_adı

Aşağıdaki komut dbase\_temel adlı bir veritabanı oluşturur:

CREATE DATABASE dbase\_temel

Bir veritabanı oluşturduktan sonra, CREATE TABLE komutu ile veritabanı içinde tablolar oluşturulabilir.

CREATE TABLE komutunun genel yazım şekli:

CREATE TABLE tablo\_adı

(

sütun\_adı1 veri\_türü,

sütun\_adı1 veri\_türü,

...

)

Eğer aşağıdaki komutu kullanırsanız; 5 sütundan oluşan personel adlı bir tablo oluşturulur:

```sql

CREATE TABLE personel (
  Adi varchar(30),
  Soyadi varchar(30),
  Gorevi varchar(30),
  Memleketi varchar(30),
  DTarihi date
)

```

Sonuç

| Adi | Soyadi | Gorevi | Memleketi | DTarihi |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

INSERT INTO komutu ile boş tabloya yeni kayıtlar ekleyebilirsiniz.
