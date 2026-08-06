---
layout: post
title: "Veritabanı Temelleri: Düz Dosyalardan MySQL ve İlişkisel Mantığa"
math: true
categories: 
  - Bilgi
tags: 
  - MySQL
  - RDBMS
  - Veritabanı
---

Bir uygulamanın kullanıcılarını, siparişlerini veya ürünlerini düz metin dosyalarında saklamak ilk bakışta kolay görünebilir. Ancak veri büyüdükçe arama yapmak, aynı kaydın tekrarını önlemek ve eş zamanlı işlemleri güvenle yönetmek zorlaşır. İlişkisel Veritabanı Yönetim Sistemleri, yani RDBMS’ler, bu karmaşayı tablolar, kurallar ve ilişkiler aracılığıyla düzenler. MySQL de bu dünyanın en yaygın temsilcilerinden biridir.

``

## Düz dosya neden yeterli değildir?

Bir CSV dosyasında her satır bir kullanıcıyı temsil edebilir. Fakat aynı kullanıcının yüz siparişi varsa kullanıcı bilgilerini yüz kez tekrarlamak gerekebilir. Kullanıcının adresi değiştiğinde bütün satırların güncellenmesi gerekir; biri unutulursa veriler çelişir. Buna **güncelleme anomalisi** denir.

RDBMS, farklı varlıkları ayrı tablolarda saklayarak tekrarları azaltır. Kullanıcı bir tabloda, sipariş başka bir tabloda bulunur ve aralarındaki bağlantı kimlik alanlarıyla kurulur.

| Özellik | Düz metin dosyası | İlişkisel veritabanı |
|---|---|---|
| Veri yapısı | Satır tabanlı, gevşek | Tablo ve sütun şeması |
| İlişkiler | Uygulama tarafından takip edilir | Anahtarlarla tanımlanır |
| Eş zamanlı erişim | Çakışmaya açıktır | İşlem ve kilit mekanizmaları vardır |
| Sorgulama | Özel kod gerekir | SQL kullanılır |
| Veri bütünlüğü | Manuel kontrol edilir | Kısıtlarla korunur |

## Tablo, satır ve sütun mantığı

Bir tablo belirli türdeki varlıkları temsil eder. `users` tablosu kullanıcıları, tablodaki her **satır** tek bir kullanıcıyı, **sütunlar** ise ad veya e-posta gibi özellikleri ifade eder. Sütunların veri türleri bulunur; örneğin `INT` tam sayıları, `VARCHAR` değişken uzunluktaki metinleri tutar.

Matematiksel ilişkisel modelde tablo bir ilişki, satır ise bir demet olarak düşünülebilir. Bir tablonun satır sayısı $n$, sütun sayısı $m$ ise veri yapısı kabaca $n \times m$ boyutlu görünür. Fakat ilişkisel model yalnızca bir matris değildir; anahtarlar ve kısıtlar veriye anlam kazandırır.

```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL
);
```

Bu kod bir kullanıcı tablosu oluşturur. `PRIMARY KEY`, her satırı benzersiz tanımlayan `id` alanını belirler. `NOT NULL`, değerin boş bırakılamayacağını; `UNIQUE` ise aynı e-posta adresinin iki kez kaydedilemeyeceğini söyler.

## İlişkiler nasıl kurulur?

Bir kullanıcının birden fazla siparişi olabilir. Bu durum **bire-çok** ilişkidir ve $1:N$ biçiminde gösterilir. Sipariş tablosundaki yabancı anahtar, siparişin hangi kullanıcıya ait olduğunu belirtir.

```sql
CREATE TABLE orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    total DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

Buradaki `user_id`, `users.id` alanına başvurur. Var olmayan bir kullanıcıya sipariş eklenmesini engelleyen bu mekanizmaya **referans bütünlüğü** denir.

| İlişki | Gösterim | Örnek |
|---|---:|---|
| Bire bir | $1:1$ | Kullanıcı–profil |
| Bire çok | $1:N$ | Kullanıcı–sipariş |
| Çoka çok | $N:M$ | Öğrenci–ders |

Çoka çok ilişkiler doğrudan değil, iki yabancı anahtar taşıyan bir ara tabloyla modellenir. Örneğin `student_courses`, öğrenci ve ders kimliklerini birlikte saklar.

## SQL ile ilişkili veriyi okumak

Ayrı tablolardaki veriler `JOIN` sayesinde yeniden anlamlı bir bütün hâline getirilir:

```sql
SELECT users.name, orders.total
FROM users
JOIN orders ON orders.user_id = users.id;
```

Bu sorgu kullanıcı adını ilgili sipariş tutarıyla eşleştirir. Böylece bilgiler depolamada ayrılmış, sorgulama sırasında birleştirilmiş olur.

RDBMS yaklaşımının özü şudur: Veriyi gereksiz yere tekrarlama, ilişkileri açıkça tanımla ve doğruluğu yalnızca uygulama koduna bırakma. MySQL; şema, anahtar, kısıt, işlem ve SQL desteğiyle veriyi pasif bir dosya yığını olmaktan çıkarıp güvenilir, sorgulanabilir ve ölçeklenebilir bir modele dönüştürür.
