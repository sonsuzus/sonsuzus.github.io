---
layout: post
title: "Form İşlemleri ve Güvenli Veri Doğrulama Rehberi"
math: true
categories: 
  - Bilgi
tags: 
  - form işlemleri
  - veri doğrulama
  - web güvenliği
---

Bir web formu, kullanıcı ile sunucu arasındaki dijital köprüdür. Ancak bu köprüden yalnızca isimler ve e-posta adresleri geçmez; hatalı değerler, bot istekleri ve kötü niyetli SQL parçaları da geçmeye çalışabilir. Bu nedenle veriyi doğrudan veritabanına göndermek, kapının anahtarını paspasın altına bırakmaya benzer.
``

## Formdan veritabanına uzanan yol

Tarayıcıda doldurulan alanlar genellikle `GET` veya `POST` yöntemiyle sunucuya iletilir. `GET`, filtreleme ve arama gibi adres çubuğunda görülebilecek işlemler için uygundur. Kişisel bilgiler veya veri değiştiren işlemler ise çoğunlukla `POST` kullanmalıdır. Yine de `POST` veriyi kendiliğinden güvenli yapmaz; yalnızca URL dışında taşır. İletişimin şifrelenmesi için HTTPS gerekir.

Sağlıklı bir veri akışı şu aşamalardan oluşur:

1. İstek yöntemini ve içerik türünü kontrol etme
2. Beklenen alanları alma
3. Veriyi normalize etme ve gereksiz boşlukları temizleme
4. Tür, biçim, uzunluk ve iş kuralı doğrulaması yapma
5. Parametreli sorguyla veritabanına yazma
6. Gösterim sırasında bağlama uygun çıktı kodlaması uygulama

## Filtreleme ve doğrulama aynı şey değildir

| İşlem | Amacı | Örnek |
|---|---|---|
| Normalizasyon | Veriyi standart biçime getirmek | Baştaki boşlukları silmek |
| Filtreleme | İstenmeyen karakterleri ayıklamak | Kontrol karakterlerini kaldırmak |
| Doğrulama | Değerin kurala uyduğunu sınamak | E-posta biçimini kontrol etmek |
| Kodlama | Veriyi hedef bağlamda güvenli göstermek | HTML karakterlerini dönüştürmek |

Bir alanın kabul koşulunu matematiksel olarak şöyle düşünebiliriz:

$$V(x)=T(x) \land L_{min}\leq |x|\leq L_{max} \land B(x)$$

Burada $T(x)$ biçim ve tür kontrolünü, $|x|$ uzunluğu, $B(x)$ ise uygulamanın iş kurallarını temsil eder. Koşullardan biri bile yanlışsa veri reddedilmelidir. Hatalı girdiyi sessizce değiştirmek yerine kullanıcıya anlaşılır bir mesaj göstermek çoğu zaman daha doğrudur.

## Sunucu tarafında güvenli örnek

Aşağıdaki PHP örneği; adı, e-posta adresini ve yaşı doğrular. Tarayıcıdaki `required`, `min` veya `type="email"` kontrolleri kullanıcı deneyimini iyileştirir, fakat geliştirici araçlarıyla aşılabildiği için güvenlik sınırı sayılmaz.

```php
<?php
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    exit('Yalnızca POST kabul edilir.');
}

$name = trim($_POST['name'] ?? '');
$email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
$age = filter_input(INPUT_POST, 'age', FILTER_VALIDATE_INT, [
    'options' => ['min_range' => 18, 'max_range' => 120]
]);

$errors = [];

if ($name === '' || mb_strlen($name) > 80) {
    $errors[] = 'Ad alanı 1-80 karakter olmalıdır.';
}

if ($email === false || $email === null) {
    $errors[] = 'Geçerli bir e-posta adresi girilmelidir.';
}

if ($age === false || $age === null) {
    $errors[] = 'Yaş 18 ile 120 arasında olmalıdır.';
}

if ($errors) {
    http_response_code(422);
    exit(implode("\n", $errors));
}
```

Kod, eksik alanlar için varsayılan değer kullanır ve her hatayı ayrı biçimde toplar. HTTP `422` cevabı, isteğin anlaşılmasına rağmen verilerin kurallara uymadığını belirtir.

## SQL enjeksiyonuna kapıyı kapatmak

Doğrulanan değerler bile SQL metnine birleştirilmemelidir. PDO prepared statement kullanıldığında sorgu ile veri ayrı kanallardan işlenir:

```php
$stmt = $pdo->prepare(
    'INSERT INTO users (name, email, age) VALUES (:name, :email, :age)'
);

$stmt->execute([
    'name' => $name,
    'email' => $email,
    'age' => $age
]);
```

Bu yaklaşım SQL enjeksiyonuna karşı temel savunmadır. Veritabanında ayrıca `UNIQUE`, `NOT NULL` ve uygun sütun türleri tanımlanmalıdır; çünkü güvenlik tek bir kontrol noktasına emanet edilmez.

Son olarak formlara CSRF token eklenmeli, hassas alanlar günlüklere yazılmamalı ve hata mesajlarında sorgu ayrıntıları gösterilmemelidir. Veritabanından okunan içerik HTML içinde sunulurken `htmlspecialchars` ile kodlanmalıdır. Kısacası doğru sıra şudur: istemcide kolaylaştır, sunucuda doğrula, parametreli sorguyla kaydet ve gösterirken güvenli biçimde kodla.
