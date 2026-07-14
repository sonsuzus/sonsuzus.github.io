---
layout: post
title: "PHP ile RESTful API Tasarımı: Ortak Veritabanına Güvenli Köprü"
math: true
categories: 
  - Program
tags: 
  - PHP
  - RESTful API
  - Backend
---

Bir mobil uygulama, web paneli ve masaüstü istemcisi aynı veriye ulaşmak istediğinde ortada bir hakem gerekir: RESTful API. PHP ile yazacağımız API, cihazların doğrudan veritabanına dalmasını engeller; bunun yerine standart JSON yanıtları, HTTP metodları ve güvenlik katmanlarıyla düzenli bir trafik polisi gibi çalışır. Böylece iOS, Android, React, Vue ya da başka bir sistem aynı kurallarla konuşur.
``
REST mimarisinin temel fikri kaynak kavramıdır. Kullanıcılar, ürünler, siparişler gibi her şey birer resource olarak düşünülür. Örneğin `/api/users/15` adresi 15 numaralı kullanıcıyı temsil eder. Burada işlem türünü URL’ye fiil olarak yazmak yerine HTTP metodlarıyla anlatırız: listelemek için `GET`, oluşturmak için `POST`, güncellemek için `PUT/PATCH`, silmek için `DELETE`.

Küçük bir matematiksel sezgiyle API yükünü şöyle düşünebiliriz: Toplam istek maliyeti $T = n \times c$ olsun. Burada $n$ istek sayısı, $c$ ise her isteğin ortalama maliyetidir. Gereksiz büyük yanıtlar veya kötü sorgular $c$ değerini büyütür; sayfalama, filtreleme ve indeksli veritabanı sorguları ise API’yi hızlandırır.

| Kavram | Kötü Yaklaşım | RESTful Yaklaşım |
|---|---|---|
| Kullanıcı listeleme | `/getUsers.php` | `GET /api/users` |
| Kullanıcı ekleme | `/addUser.php` | `POST /api/users` |
| Yanıt formatı | Karışık metin | Standart JSON |
| Hata yönetimi | Her zaman 200 | Uygun HTTP durum kodu |

Standart yanıt yapısı API’nin farklı platformlarda tahmin edilebilir olmasını sağlar. Örneğin her cevapta `success`, `data`, `message` ve `errors` alanlarını kullanmak, istemci tarafındaki kodu sadeleştirir. Başarılı listeleme için durum kodu $200$, kayıt oluşturma için $201$, yetkisiz erişim için $401$, bulunamayan kaynak için $404$ tercih edilir.

Aşağıdaki örnek, basit ama düzenli bir PHP API iskeleti gösterir. PDO ile hazırlanmış sorgular SQL injection riskini azaltır, `json_response` fonksiyonu ise tüm çıktıları tek biçime sokar.

```php
<?php
header('Content-Type: application/json; charset=utf-8');

$pdo = new PDO(
    'mysql:host=localhost;dbname=app;charset=utf8mb4',
    'api_user',
    'secret_password',
    [PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION]
);

function json_response($status, $success, $data = null, $message = '', $errors = []) {
    http_response_code($status);
    echo json_encode([
        'success' => $success,
        'data' => $data,
        'message' => $message,
        'errors' => $errors
    ], JSON_UNESCAPED_UNICODE);
    exit;
}

$method = $_SERVER['REQUEST_METHOD'];
$path = trim(parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH), '/');
$parts = explode('/', $path);

if ($parts[0] !== 'api' || $parts[1] !== 'users') {
    json_response(404, false, null, 'Kaynak bulunamadı');
}

if ($method === 'GET') {
    $stmt = $pdo->query('SELECT id, name, email FROM users ORDER BY id DESC LIMIT 20');
    json_response(200, true, $stmt->fetchAll(PDO::FETCH_ASSOC), 'Kullanıcılar listelendi');
}

json_response(405, false, null, 'Bu metod desteklenmiyor');
```

Bu kodun yaptığı şey basit: Gelen isteğin metodunu ve yolunu okur, `/api/users` kaynağına gelen `GET` isteklerinde kullanıcıları JSON olarak döndürür. Gerçek projede bu yönlendirme mantığını ayrı bir router sınıfına almak, controller katmanı eklemek ve veritabanı işlemlerini repository yapısına taşımak daha sürdürülebilir olur.

Güvenlik tarafında en kritik konu kimlik doğrulamadır. Oturum tabanlı klasik yaklaşım yerine API’lerde genellikle token kullanılır. Kullanıcı giriş yapınca bir erişim token’ı alır ve sonraki isteklerde `Authorization: Bearer TOKEN` başlığıyla gönderir. Token doğrulanmadan hassas kaynaklara erişim verilmemelidir.

| Önlem | Neden Gerekli? | PHP Tarafındaki Karşılığı |
|---|---|---|
| HTTPS | Token sızıntısını önler | Sunucu SSL yapılandırması |
| Prepared statement | SQL injection engeller | PDO parametre bağlama |
| Rate limit | Bot saldırılarını yavaşlatır | IP bazlı sayaç |
| CORS kontrolü | İzinli istemcileri belirler | `Access-Control-Allow-Origin` |

Basit bir token kontrolü şöyle kurgulanabilir:

```php
function require_token() {
    $headers = getallheaders();
    $auth = $headers['Authorization'] ?? '';

    if (!str_starts_with($auth, 'Bearer ')) {
        json_response(401, false, null, 'Token eksik');
    }

    $token = substr($auth, 7);
    if ($token !== 'demo-secure-token') {
        json_response(403, false, null, 'Token geçersiz');
    }
}
```

Elbette canlı sistemde sabit token kullanılmaz; JWT, OAuth2 veya veritabanında saklanan süreli erişim anahtarları tercih edilir. Ayrıca API sürümleme unutulmamalıdır: `/api/v1/users` gibi bir yapı, ileride kırıcı değişiklikleri yönetmeyi kolaylaştırır.

Sonuç olarak PHP ile RESTful API tasarlamak, yalnızca birkaç endpoint yazmak değildir. Kaynak modelleme, HTTP semantiği, güvenlik, hata standardı ve performans bir araya geldiğinde platform bağımsız, güvenilir ve keyifli bir veri köprüsü ortaya çıkar. Doğru kuralları koyarsanız, cihazlarınız aynı veritabanıyla kavga etmeden konuşur.
