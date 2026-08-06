---
layout: post
title: "Temel SQL Sorguları ile CRUD İşlemlerini Öğrenme"
math: true
categories: 
  - Bilgi
tags: 
  - SQL
  - CRUD
  - Veritabanı
---

Bir veritabanıyla çalışan hemen her uygulama aynı dört temel ihtiyaca sahiptir: yeni veri eklemek, mevcut verileri okumak, bilgileri güncellemek ve artık gerekli olmayan kayıtları silmek. Bu işlemler İngilizce karşılıklarının baş harfleriyle **CRUD** olarak adlandırılır. SQL dünyasında CRUD, karmaşık görünen veritabanı macerasının sağlam ve oldukça pratik başlangıç noktasıdır.
``
## CRUD Mantığı Nedir?

CRUD, verinin yaşam döngüsünü temsil eder. Bir kullanıcı sisteme kaydolduğunda kayıt oluşturulur; profilini görüntülediğinde veri okunur; adresini değiştirdiğinde kayıt güncellenir; hesabını kapattığında ise veri silinir.

Bir tablodaki toplam kayıt sayısını $N$ ile gösterirsek, yeni kayıt eklendiğinde sayı genellikle $N+1$, bir kayıt silindiğinde ise $N-1$ olur. Güncelleme ve okuma işlemleri kayıt sayısını değiştirmez; yalnızca verinin içeriğini veya görüntülenme biçimini etkiler.

| CRUD işlemi | SQL komutu | Temel amaç | Kayıt sayısına etkisi |
|---|---|---|---|
| Create | `INSERT` | Yeni kayıt eklemek | Genellikle $N+1$ |
| Read | `SELECT` | Kayıtları okumak | Değişmez |
| Update | `UPDATE` | Mevcut kaydı değiştirmek | Değişmez |
| Delete | `DELETE` | Kayıt silmek | Genellikle $N-1$ |

Örneklerimizde aşağıdaki `kullanicilar` tablosunun bulunduğunu varsayalım:

```sql
CREATE TABLE kullanicilar (
    id INT PRIMARY KEY,
    ad VARCHAR(100) NOT NULL,
    eposta VARCHAR(150) UNIQUE,
    yas INT
);
```

Burada `PRIMARY KEY`, her kaydı benzersiz biçimde tanımlar. `NOT NULL` alanın boş bırakılamayacağını, `UNIQUE` ise aynı e-posta adresinin tekrar kullanılamayacağını belirtir.

## Create: INSERT ile Kayıt Ekleme

Yeni bir kullanıcı eklemek için `INSERT INTO` komutu kullanılır:

```sql
INSERT INTO kullanicilar (id, ad, eposta, yas)
VALUES (1, 'Ada Yılmaz', 'ada@example.com', 28);
```

Sütun adlarıyla değerlerin sırası birbiriyle eşleşmelidir. Birden fazla kayıt da tek sorguda eklenebilir:

```sql
INSERT INTO kullanicilar (id, ad, eposta, yas)
VALUES
    (2, 'Mert Kaya', 'mert@example.com', 34),
    (3, 'Ece Demir', 'ece@example.com', 22);
```

## Read: SELECT ile Veri Okuma

Bütün sütunları ve kayıtları görüntülemek için yıldız karakteri kullanılabilir:

```sql
SELECT * FROM kullanicilar;
```

Gerçek projelerde yalnızca ihtiyaç duyulan sütunları seçmek daha anlaşılır ve verimlidir:

```sql
SELECT ad, eposta
FROM kullanicilar
WHERE yas >= 25
ORDER BY ad ASC;
```

`WHERE` sonuçları filtreler, `ORDER BY` ise sıralar. Bu örnek, yaşı en az 25 olan kullanıcıları ada göre artan biçimde getirir. Koşulu sağlayan kayıtların kümesini $S$ olarak düşünürsek sonuç sayısı $|S| \leq N$ olur.

## Update: UPDATE ile Kayıt Güncelleme

Bir kullanıcının yaşını değiştirmek için şu sorgu çalıştırılabilir:

```sql
UPDATE kullanicilar
SET yas = 29
WHERE id = 1;
```

Buradaki en kritik bölüm `WHERE` koşuludur. Koşul yazılmazsa tablodaki **tüm kullanıcıların** yaşı 29 olur. SQL bu konuda fazla yardımseverdir; ne söylediyseniz onu yapar, ne demek istediğinizi tahmin etmez!

Birden fazla alan aynı anda güncellenebilir:

```sql
UPDATE kullanicilar
SET ad = 'Ada Yıldız', eposta = 'ada.yildiz@example.com'
WHERE id = 1;
```

## Delete: DELETE ile Kayıt Silme

Belirli bir kaydı silmek için yine güvenli bir filtre gerekir:

```sql
DELETE FROM kullanicilar
WHERE id = 3;
```

`WHERE` olmadan çalıştırılan `DELETE FROM kullanicilar;` sorgusu tablodaki tüm kayıtları siler. Bu nedenle silmeden veya güncellemeden önce aynı koşulu bir `SELECT` sorgusuyla test etmek iyi bir alışkanlıktır:

```sql
SELECT * FROM kullanicilar WHERE id = 3;
```

## Güvenli Kullanım İçin İpuçları

| Riskli yaklaşım | Daha güvenli yaklaşım |
|---|---|
| Kullanıcı girdisini sorguya eklemek | Parametreli sorgu kullanmak |
| `WHERE` olmadan güncellemek | Önce `SELECT` ile koşulu doğrulamak |
| Doğrudan toplu silme yapmak | Transaction ve yedek kullanmak |
| Her zaman `SELECT *` yazmak | Gerekli sütunları seçmek |

CRUD komutları basit görünse de uygulamaların veri katmanının temelini oluşturur. `INSERT`, `SELECT`, `UPDATE` ve `DELETE` komutlarını doğru filtreler, kısıtlamalar ve transaction mantığıyla kullanmak; hem veriyi korur hem de daha güvenilir uygulamalar geliştirmenizi sağlar.
