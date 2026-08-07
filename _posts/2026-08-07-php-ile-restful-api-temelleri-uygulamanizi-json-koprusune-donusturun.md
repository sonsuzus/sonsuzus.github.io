---
layout: post
title: "PHP ile RESTful API Temelleri: Uygulamanızı JSON Köprüsüne Dönüştürün"
math: true
categories: 
  - Bilgi
tags: 
  - PHP
  - REST API
  - JSON
---

Bir PHP uygulaması yalnızca HTML üretmek zorunda değildir. Aynı uygulama; mobil istemcilere, JavaScript arayüzlerine ve başka sunuculara dinamik veri sağlayan bir API olarak da çalışabilir. Bunun anahtarı, kaynakları HTTP üzerinden anlaşılır biçimde sunmak ve yanıtları ortak bir veri formatı olan JSON ile iletmektir.
``
## REST nedir?

REST, yani **Representational State Transfer**, katı bir protokolden çok web servisleri tasarlamak için kullanılan mimari ilkeler bütünüdür. Temel fikir şudur: Sistemdeki kullanıcı, ürün veya sipariş gibi varlıklar birer **kaynak** olarak ele alınır. Her kaynak bir URL ile temsil edilir ve kaynak üzerinde yapılacak işlem HTTP metodu tarafından belirtilir.

Örneğin `/api/products/12` adresi, kimliği 12 olan ürünü temsil edebilir. URL'nin `urun-getir.php?id=12` gibi bir eylem anlatması yerine kaynağı tanımlaması REST yaklaşımına daha uygundur.

| HTTP metodu | Amaç | Örnek adres | Olası durum kodu |
|---|---|---|---|
| `GET` | Kaynak okumak | `/api/products/12` | `200 OK` |
| `POST` | Yeni kaynak oluşturmak | `/api/products` | `201 Created` |
| `PUT` | Kaynağı bütünüyle güncellemek | `/api/products/12` | `200 OK` |
| `PATCH` | Kısmi güncelleme yapmak | `/api/products/12` | `200 OK` |
| `DELETE` | Kaynağı silmek | `/api/products/12` | `204 No Content` |

REST servislerinin **durumsuz** olması beklenir. Sunucu, önceki isteği hatırlamak zorunda kalmamalıdır; ihtiyaç duyulan kimlik doğrulama ve parametreler her istekte taşınmalıdır. Böylece istek sayısı $n$ olduğunda işlemler birbirinden bağımsız kalır ve sistemin yatay olarak ölçeklenmesi kolaylaşır.

## JSON neden kullanılır?

JSON, anahtar-değer çiftlerinden ve dizilerden oluşan hafif bir veri formatıdır. PHP dizileri, JavaScript nesneleri ve pek çok dildeki sözlük yapılarıyla rahatça eşleştirilebilir.

```json
{
  "id": 12,
  "name": "Mekanik Klavye",
  "price": 2499.90,
  "inStock": true
}
```

JSON yalnızca veriyi taşır; görünüm kararını istemciye bırakır. Aynı yanıt mobil uygulamada kart, yönetim panelinde tablo, başka bir sistemde ise rapor satırı olarak gösterilebilir. Yaklaşık yanıt boyutu $B$ ve saniyedeki istek sayısı $R$ ise ağ yükü kabaca $B \times R$ ile ifade edilebilir. Gereksiz alanları kaldırmak bu nedenle önemlidir.

## PHP ile basit bir API uç noktası

Aşağıdaki örnek, PDO kullanarak veritabanından ürünleri okur ve JSON yanıtı döndürür:

```php
<?php
header('Content-Type: application/json; charset=utf-8');

$pdo = new PDO(
    'mysql:host=localhost;dbname=shop;charset=utf8mb4',
    'api_user',
    'secret',
    [PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION]
);

try {
    $stmt = $pdo->query(
        'SELECT id, name, price FROM products ORDER BY id DESC'
    );

    $products = $stmt->fetchAll(PDO::FETCH_ASSOC);

    http_response_code(200);
    echo json_encode([
        'success' => true,
        'data' => $products,
        'count' => count($products)
    ], JSON_UNESCAPED_UNICODE | JSON_PRESERVE_ZERO_FRACTION);
} catch (Throwable $error) {
    http_response_code(500);
    echo json_encode([
        'success' => false,
        'error' => 'Sunucu hatası oluştu.'
    ], JSON_UNESCAPED_UNICODE);
}
```

`Content-Type` başlığı istemciye yanıtın JSON olduğunu bildirir. `json_encode()` PHP dizisini JSON metnine dönüştürür. Hata oluştuğunda ayrıntılı veritabanı mesajını dışarı vermemek ise tablo adları veya bağlantı bilgileri gibi hassas ayrıntıların sızmasını önler.

## İstek gövdesini okumak

`POST` ve `PATCH` isteklerinde JSON verisi `php://input` üzerinden alınabilir:

```php
$body = file_get_contents('php://input');
$input = json_decode($body, true);

if (!is_array($input) || empty($input['name'])) {
    http_response_code(422);
    echo json_encode(['error' => 'name alanı zorunludur.']);
    exit;
}
```

Burada `422 Unprocessable Content`, JSON okunabilse bile doğrulama kurallarının sağlanmadığını anlatır. Geçersiz JSON için `400 Bad Request`, bulunamayan kaynak için `404 Not Found` kullanılmalıdır. Her hataya `200` dönmek, yangın alarmını ne olursa olsun yeşil yakmaya benzer!

Son olarak API'yi HTTPS, token tabanlı kimlik doğrulama, giriş doğrulama, hız sınırlama ve sürümleme ile güçlendirin. `/api/v1/products` gibi sürümlü adresler, gelecekte yapılacak değişikliklerin mevcut istemcileri bozmamasına yardımcı olur. Böylece PHP uygulamanız bir web sayfası üreticisinden, farklı sistemlerin güvenle konuşabildiği gerçek bir veri köprüsüne dönüşür.
