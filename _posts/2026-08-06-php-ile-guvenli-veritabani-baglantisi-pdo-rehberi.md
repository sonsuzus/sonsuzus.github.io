---
layout: post
title: "PHP ile Güvenli Veritabanı Bağlantısı: PDO Rehberi"
math: true
categories: 
  - Bilgi
tags: 
  - PHP
  - PDO
  - MySQL
---

Bir PHP uygulamasının verilerle konuşabilmesi için güvenilir bir köprüye ihtiyacı vardır. PDO, yani PHP Data Objects, PHP ile MySQL gibi veritabanları arasında bu köprüyü kuran nesne yönelimli bir arayüzdür. Hazırlanmış sorgular, hata yönetimi ve farklı veritabanı sistemlerine uyum gibi özellikleri sayesinde hem güvenli hem de esnek uygulamalar geliştirmeyi kolaylaştırır.
``

## PDO tam olarak nedir?

PDO, doğrudan bir veritabanı değil, veritabanı sürücüleri üzerinde çalışan ortak bir erişim katmanıdır. MySQL yerine PostgreSQL kullanmaya karar verdiğinizde uygulamanın bütün veri erişim mantığını baştan yazmanız gerekmez. Bağlantı bilgisini ve veritabanına özgü bazı sorguları değiştirmek çoğu zaman yeterlidir.

Bir veritabanı işleminin yaklaşık toplam süresi şöyle düşünülebilir:

$$T_{toplam} = T_{bağlantı} + T_{sorgu} + T_{aktarım}$$

Bağlantıyı gereksiz yere tekrar oluşturmak $T_{bağlantı}$ maliyetini artırır. Bu nedenle bağlantıyı merkezi bir dosyada veya kontrollü bir sınıfta yönetmek iyi bir yaklaşımdır.

| Özellik | PDO | MySQLi |
|---|---|---|
| Desteklenen sistemler | MySQL, PostgreSQL, SQLite ve diğerleri | Yalnızca MySQL |
| Kullanım yaklaşımı | Nesne yönelimli | Nesne yönelimli ve prosedürel |
| Hazırlanmış sorgular | Var | Var |
| Taşınabilirlik | Yüksek | Düşük |
| İsimlendirilmiş parametreler | Desteklenir | Desteklenmez |

## MySQL bağlantısını oluşturmak

PDO bağlantısı kurulurken DSN adı verilen bağlantı tanımı kullanılır. DSN içerisinde sürücü, sunucu, veritabanı ve karakter seti belirtilir.

```php
<?php
$host = 'localhost';
$dbname = 'blog';
$username = 'root';
$password = '';

$dsn = "mysql:host=$host;dbname=$dbname;charset=utf8mb4";

$options = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    PDO::ATTR_EMULATE_PREPARES => false,
];

try {
    $pdo = new PDO($dsn, $username, $password, $options);
    echo 'Bağlantı başarılı!';
} catch (PDOException $exception) {
    error_log($exception->getMessage());
    exit('Veritabanına bağlanılamadı.');
}
```

`ERRMODE_EXCEPTION`, hataları istisna olarak yakalamamızı sağlar. `FETCH_ASSOC`, sonuçları sütun adlarının anahtar olduğu diziler halinde getirir. `utf8mb4` ise Türkçe karakterleri ve emojileri sorunsuz saklar. Çünkü veritabanımızın emoji görünce bayılmasını istemeyiz.

Gerçek projelerde kullanıcı adı ve parola kaynak koduna yazılmamalıdır. Bu bilgiler `.env` gibi ortam dosyalarında tutulmalı ve ilgili dosya Git deposuna eklenmemelidir.

## Prepared statement neden önemlidir?

Kullanıcıdan gelen değeri sorgunun içine doğrudan eklemek SQL injection saldırılarına kapı açar. Hazırlanmış sorgular SQL komutunu veriden ayırır. Böylece saldırganın girdiği metin, çalıştırılacak komut değil yalnızca veri olarak değerlendirilir.

```php
$email = $_POST['email'] ?? '';

$sql = 'SELECT id, name, email FROM users WHERE email = :email';
$statement = $pdo->prepare($sql);
$statement->execute(['email' => $email]);

$user = $statement->fetch();

if ($user) {
    echo htmlspecialchars($user['name']);
}
```

Buradaki `:email` isimlendirilmiş bir parametredir. `prepare()` sorgu şablonunu hazırlar, `execute()` ise gerçek değeri güvenli biçimde bağlar. Çıktıda `htmlspecialchars()` kullanılması da veritabanı güvenliğinden farklı bir konu olan XSS riskini azaltır.

| Yöntem | Güvenlik | Okunabilirlik |
|---|---|---|
| Değeri sorguya eklemek | Tehlikeli | Kısa ama riskli |
| Prepared statement | Yüksek | Açık ve düzenli |
| Parametre türü belirtmek | Daha kontrollü | Biraz daha ayrıntılı |

## Veri ekleme ve işlem yönetimi

Birden fazla sorgunun ya hep birlikte ya da hiç çalışmaması gerekiyorsa transaction kullanılır. Bu yaklaşım atomiklik ilkesiyle ifade edilir: başarı oranı ya $1$ ya da $0$ olmalıdır.

```php
try {
    $pdo->beginTransaction();

    $statement = $pdo->prepare(
        'INSERT INTO users (name, email) VALUES (:name, :email)'
    );
    $statement->execute([
        'name' => 'Ada',
        'email' => 'ada@example.com'
    ]);

    $pdo->commit();
} catch (Throwable $error) {
    $pdo->rollBack();
    error_log($error->getMessage());
}
```

`commit()` değişiklikleri kalıcılaştırırken `rollBack()` başarısız işlemden önceki duruma döner. Özellikle sipariş, ödeme ve stok güncelleme süreçlerinde transaction kullanmak kritik öneme sahiptir.

Sonuç olarak PDO; taşınabilirlik, prepared statement desteği, istisna tabanlı hata yönetimi ve transaction özellikleriyle modern PHP projelerinin güçlü araçlarından biridir. Bağlantı bilgilerini korumak, kullanıcı verilerini parametrelerle bağlamak ve hataları ziyaretçiye göstermeden kaydetmek güvenli bir veri katmanının temelini oluşturur.
