---
layout: post
title: "Güvenli Dosya Yükleme: Formdan Sunucuya Sağlam Bir Yolculuk"
math: true
categories: 
  - Program
tags: 
  - dosya-yükleme
  - web-güvenliği
  - php
---

Dosya yükleme özelliği, profil fotoğrafından PDF başvuru belgelerine kadar pek çok web uygulamasının vazgeçilmezidir. Ancak kullanıcıdan gelen bir dosyayı doğrudan sunucuya kabul etmek, kapıyı çalan herkese anahtarı teslim etmeye benzeyebilir. Güvenli bir sistem; dosyanın adını, boyutunu, gerçek türünü ve saklanacağı konumu denetlemelidir.

``

## Dosya yükleme nasıl çalışır?

Tarayıcı, dosyayı genellikle `multipart/form-data` biçiminde HTTP isteğine ekler. Sunucu dosyayı geçici bir dizine alır, uygulama da doğrulama tamamlandıktan sonra kalıcı konuma taşır. Kritik nokta şudur: **Kullanıcı tarafından gönderilen hiçbir bilgi güvenilir kabul edilmemelidir.**

Bir yükleme isteğinin yaklaşık maliyetini şöyle düşünebiliriz:

$$M_{toplam} = M_{dosya} + M_{istek} + M_{işleme}$$

Burada büyük dosyalar yalnızca disk alanını değil; ağ trafiğini, belleği ve işlem süresini de tüketir. Bu nedenle uygulama seviyesindeki sınırın yanında web sunucusu ve PHP yapılandırmasında da boyut sınırı bulunmalıdır.

| Kontrol | Güvensiz yaklaşım | Güvenli yaklaşım |
|---|---|---|
| Dosya türü | Uzantıya bakmak | İçeriğin MIME türünü incelemek |
| Dosya adı | Kullanıcının adını korumak | Rastgele ve benzersiz ad üretmek |
| Boyut | Sınırsız kabul etmek | Uygun üst sınır belirlemek |
| Saklama | Herkese açık dizine koymak | Web kökü dışında saklamak |
| Hata mesajı | Sistem yolunu göstermek | Genel ve kontrollü mesaj vermek |

## Formun hazırlanması

Formda `enctype` belirtilmezse dosya içeriği sunucuya doğru biçimde ulaşmaz:

```html
<form action="upload.php" method="post" enctype="multipart/form-data">
  <input type="hidden" name="csrf_token" value="SUNUCUDA_URETILEN_TOKEN">
  <input type="file" name="document" accept="image/jpeg,image/png,application/pdf" required>
  <button type="submit">Güvenli biçimde yükle</button>
</form>
```

`accept` özelliği kullanıcı deneyimini iyileştirir fakat güvenlik önlemi değildir; istek elle değiştirilerek başka dosyalar gönderilebilir. CSRF belirteci ise başka bir sitenin kullanıcı adına yükleme başlatmasını zorlaştırır.

## PHP ile güvenli doğrulama

Aşağıdaki örnek; yükleme hatasını, boyutu ve gerçek MIME türünü denetler. Ayrıca tahmin edilmesi güç bir dosya adı üretir:

```php
<?php
session_start();

if (!hash_equals($_SESSION['csrf_token'] ?? '', $_POST['csrf_token'] ?? '')) {
    http_response_code(403);
    exit('Geçersiz istek.');
}

$file = $_FILES['document'] ?? null;

if (!$file || $file['error'] !== UPLOAD_ERR_OK) {
    exit('Dosya yüklenemedi.');
}

$maxSize = 5 * 1024 * 1024; // 5 MB
if ($file['size'] > $maxSize) {
    exit('Dosya boyutu sınırı aşıldı.');
}

$finfo = new finfo(FILEINFO_MIME_TYPE);
$mime = $finfo->file($file['tmp_name']);
$allowed = [
    'image/jpeg' => 'jpg',
    'image/png' => 'png',
    'application/pdf' => 'pdf'
];

if (!isset($allowed[$mime])) {
    exit('Desteklenmeyen dosya türü.');
}

$name = bin2hex(random_bytes(16)) . '.' . $allowed[$mime];
$target = dirname(__DIR__) . '/private_uploads/' . $name;

if (!move_uploaded_file($file['tmp_name'], $target)) {
    exit('Dosya kaydedilemedi.');
}

echo 'Yükleme tamamlandı.';
```

`finfo`, yalnızca kullanıcının bildirdiği türe güvenmek yerine dosya içeriğini inceler. `random_bytes` tabanlı adlandırma ise `rapor.php.jpg` gibi yanıltıcı adları ve aynı isimli dosyaların birbirini ezmesini engeller.

## Görseller için ek savunmalar

Bir dosyanın MIME türünün görsel görünmesi, tamamen güvenli olduğu anlamına gelmez. Görseller mümkünse GD veya Imagick ile açılıp yeniden kodlanmalıdır. Belgeler antivirüs servisiyle taranabilir; yüksek riskli sistemlerde tarama bitene kadar karantina dizininde tutulmalıdır.

| Katman | Önerilen önlem |
|---|---|
| Uygulama | MIME, boyut, yetki ve CSRF kontrolü |
| Dosya sistemi | Yazma iznini sınırlama, çalıştırmayı kapatma |
| Sunucu | İstek ve zaman aşımı sınırları |
| Operasyon | Zararlı yazılım taraması ve kayıt tutma |

Son olarak dosyaları doğrudan tahmin edilebilir URL’lerle sunmak yerine, kullanıcının erişim yetkisini kontrol eden bir indirme uç noktası kullanın. Böylece güvenli yükleme tek bir `if` koşulu değil, birbirini tamamlayan savunma katmanlarından oluşan sağlam bir kale hâline gelir.
