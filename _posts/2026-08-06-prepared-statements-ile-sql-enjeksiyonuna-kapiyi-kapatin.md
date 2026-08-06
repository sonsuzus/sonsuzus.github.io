---
layout: post
title: "Prepared Statements ile SQL Enjeksiyonuna Kapıyı Kapatın"
math: true
categories: 
  - Bilgi
tags: 
  - SQL
  - Siber Güvenlik
  - Prepared Statements
---

Bir giriş formu düşünün: Kullanıcı adını ve parolayı alıp veritabanında arıyorsunuz. Masum görünen bu işlem, kullanıcı girdisini doğrudan SQL metnine eklerseniz saldırgana sorgunuzu yeniden yazma fırsatı verebilir. Prepared statements, yani hazırlanmış ifadeler, SQL komutunu veri parçalarından ayırarak bu tehlikeli kapıyı kapatır.

``

## SQL Enjeksiyonu Nasıl Ortaya Çıkar?

Güvensiz yaklaşımda sorgu, metin birleştirme yoluyla oluşturulur:

```javascript
const username = req.body.username;
const sql = "SELECT * FROM users WHERE username = '" + username + "'";
const result = await db.query(sql);
```

Normal bir kullanıcı `ayse` değerini gönderdiğinde sorgu beklendiği gibi çalışır. Ancak saldırgan şu girdiyi sağlayabilir:

```text
' OR 1=1 --
```

Ortaya çıkan sorgu yaklaşık olarak şöyledir:

```sql
SELECT * FROM users WHERE username = '' OR 1=1 --'
```

Burada `$1=1$` ifadesi her zaman doğrudur. `--` işareti ise sorgunun kalanını yorum satırına dönüştürebilir. Böylece uygulamanın amaçladığı koşul etkisiz hâle gelir. Sorun verinin “kötü karakterler” içermesi değil, verinin SQL dilinin bir parçası olarak yorumlanmasıdır.

## Prepared Statement Mantığı

Hazırlanmış ifadelerde sorgunun yapısı ve değerleri ayrı kanallardan gönderilir. Önce yer tutucular içeren bir SQL şablonu hazırlanır, ardından kullanıcı değerleri bu yer tutuculara bağlanır.

Bunu kavramsal olarak şöyle gösterebiliriz:

$$Q = S + D$$

Güvensiz yöntemde sorgu $Q$, SQL yapısı $S$ ile kullanıcı verisinin $D$ metinsel olarak birleştirilmesidir. Prepared statement yaklaşımında ise:

$$Q = \operatorname{prepare}(S), \quad R = \operatorname{execute}(Q, D)$$

Veritabanı motoru $D$ değerini komut olarak değil, yalnızca veri olarak ele alır. Kullanıcı `OR`, tırnak veya yorum işareti gönderse bile bunlar SQL sözdizimine dönüşmez.

| Özellik | Metin birleştirme | Prepared statement |
|---|---|---|
| SQL ve veri | Birbirine karışır | Ayrı tutulur |
| Enjeksiyon riski | Çok yüksek | Parametrelerde büyük ölçüde engellenir |
| Okunabilirlik | Karmaşıklaşır | Daha düzenlidir |
| Tür yönetimi | Elle yapılabilir | Sürücü tarafından desteklenir |
| Tekrar kullanım | Sınırlı | Verimli olabilir |

## Node.js ile Güvenli Kullanım

Aşağıdaki PostgreSQL örneğinde `$1` ve `$2` birer parametre yer tutucusudur:

```javascript
const username = req.body.username;
const email = req.body.email;

const sql = `
  SELECT id, username, email
  FROM users
  WHERE username = $1 AND email = $2
`;

const result = await db.query(sql, [username, email]);
return result.rows;
```

Bu kodda SQL şablonu değişmez. `username` ve `email` ayrı bir diziyle sürücüye iletilir. Sürücü, değerlerin uygun biçimde kodlanmasını ve SQL komutuna dönüşmemesini sağlar.

Güncelleme işlemlerinde de aynı yöntem uygulanmalıdır:

```javascript
const sql = `UPDATE users SET display_name = $1 WHERE id = $2`;
await db.query(sql, [req.body.displayName, req.user.id]);
```

## Sık Yapılan Hatalar

Prepared statements yalnızca değerleri güvenle bağlar; tablo adı, sütun adı veya `ASC` ve `DESC` gibi SQL anahtar sözcükleri genellikle parametreleştirilemez. Dinamik sıralama gerekiyorsa izin listesi kullanılmalıdır:

```javascript
const allowedColumns = new Set(["username", "created_at"]);
const sort = allowedColumns.has(req.query.sort)
  ? req.query.sort
  : "created_at";

const result = await db.query(
  `SELECT id, username FROM users ORDER BY ${sort} DESC`
);
```

Burada sorguya yalnızca önceden onaylanmış sütun adları girebilir. Ayrıca prepared statement kullanmak; en az yetkili veritabanı hesabı, giriş doğrulama, güvenli hata mesajları ve kayıt izleme gibi önlemlerin yerini tutmaz.

Kısacası temel kural nettir: Kullanıcı verisi SQL cümlesi yazmamalı, yalnızca SQL cümlesindeki boşlukları değer olarak doldurmalıdır. Sorguları parametrik kurmak küçük bir kodlama alışkanlığıdır; fakat uygulamanın verilerini, kullanıcılarını ve geliştiricinin gece uykusunu koruyan büyük bir güvenlik adımıdır.
