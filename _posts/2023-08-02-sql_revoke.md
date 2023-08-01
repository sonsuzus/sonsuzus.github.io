---
title:  SQL Programlama REVOKE
author: sonsuz
date: 2023-08-02 00:18:57 +0300
categories: [Program,SQL]
tags: [sql,programlama,yetki,veri,veri tabanı]
---


Birden fazla kullanıcının işlem yaptığı veritabanı sistemlerinde Veri Kontrol Dili (Data Control Language - DCL) komutları kullanılarak güvenlik sağlanır. Veritabanı yöneticisi bir veritabanı veya tablo üzerindeki işlem yetkilerini verir veya kaldırır.

REVOKE komutu veritabanı ve tablolar için GRANT komutu ile verilen yetkiyi kullanıcılardan geri almak için kullanılır.

REVOKE komutu yazım şekli aşağıdadır:

REVOKE yetki\_adı

ON nesne\_adı

FROM { kullanıcı\_adı | PUBLIC | rol\_adı }

yetki\_adı : Geri alınacak olan erişim yetkisidir.

nesne\_adı: Üzerinde yetki geri alınacak olan tablo, View, Stored Proc gibi bir veritabanı nesnesini gösterir.

kullanıcı\_adı: Yetkisi geri alınacak kullanıcının adını gösterir.

PUBLIC: Bütün kullanıcılardan yetkiyi geri almak için kullanılır.

rol\_adı: Bir grup için toplanan yetkileri gösterir.

Aşağıdaki komut personel tablosu üzerinde SELECT komutunu kullanma yetkisini tüm kullanıcılardan geri alır:

```sql
REVOKE SELECT ON personel FROM *.*
```
