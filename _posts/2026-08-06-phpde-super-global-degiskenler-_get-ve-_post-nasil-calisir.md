---
layout: post
title: "PHP’de Süper Global Değişkenler: $_GET ve $_POST Nasıl Çalışır?"
math: true
categories: 
  - Bilgi
tags: 
  - PHP
  - GET ve POST
  - Web Programlama
---

Bir kullanıcı arama kutusuna kelime yazdığında, giriş formunu doldurduğunda veya bir bağlantıya tıkladığında tarayıcı ile sunucu arasında veri alışverişi gerçekleşir. PHP, gelen bu verilere erişebilmemiz için `$_GET` ve `$_POST` adlı süper global değişkenleri sunar. Adlarındaki “süper” ifadesi boşuna değildir; bu değişkenlere fonksiyonların içinden bile doğrudan erişilebilir.
``
## İstek ve yanıt döngüsü

Web iletişimi temel olarak **istemci–sunucu modeline** dayanır. Tarayıcı istemci olarak bir HTTP isteği gönderir, sunucu isteği işler ve bir HTTP yanıtı üretir. Basitleştirilmiş süreç şöyledir:

1. Kullanıcı bir bağlantıya tıklar veya form gönderir.
2. Tarayıcı GET ya da POST isteği oluşturur.
3. Web sunucusu isteği PHP dosyasına yönlendirir.
4. PHP, verileri ilgili süper global diziye yerleştirir.
5. Uygulama veriyi işler ve tarayıcıya yanıt döndürür.

İletişim süresini kabaca $T_{toplam} = T_{istek} + T_{işleme} + T_{yanıt}$ biçiminde düşünebiliriz. Ağ gecikmesi ve sunucudaki işlem yükü arttıkça kullanıcının bekleme süresi de artar.

## GET metodu ve `$_GET`

GET, verileri URL’nin **sorgu dizesine** ekler. Örneğin aşağıdaki adres, `kategori` ve `sayfa` isimli iki değer taşır:

```text
urunler.php?kategori=kitap&sayfa=2
```

Soru işaretinden sonraki bölüm sorgu dizesidir. Parametreler `&` karakteriyle ayrılır ve her biri `anahtar=değer` biçimindedir. PHP bunları ilişkisel bir dizi olan `$_GET` içine aktarır:

```php
<?php
$kategori = $_GET['kategori'] ?? 'tumu';
$sayfa = filter_input(INPUT_GET, 'sayfa', FILTER_VALIDATE_INT) ?: 1;

echo "Kategori: " . htmlspecialchars($kategori, ENT_QUOTES, 'UTF-8');
echo " | Sayfa: " . $sayfa;
```

Buradaki `??` operatörü parametre gönderilmediyse varsayılan değer sağlar. `filter_input` sayfanın gerçekten tam sayı olup olmadığını denetler. `htmlspecialchars` ise çıktıyı HTML içinde güvenli göstererek XSS riskini azaltır.

GET; arama, filtreleme, sıralama ve sayfalama için idealdir. URL paylaşılabilir, yer imlerine eklenebilir ve tarayıcı geçmişinde tutulabilir. Bu nedenle parola gibi hassas bilgiler GET ile gönderilmemelidir.

## POST metodu ve `$_POST`

POST verileri URL’ye değil, HTTP isteğinin gövdesine yerleştirir. Genellikle kayıt, giriş, yorum ekleme veya veri güncelleme işlemlerinde kullanılır:

```html
<form action="kaydet.php" method="post">
  <input type="text" name="kullanici" required>
  <input type="password" name="parola" required>
  <button type="submit">Gönder</button>
</form>
```

Form gönderildiğinde PHP alanlara `$_POST` üzerinden erişir:

```php
<?php
$kullanici = trim($_POST['kullanici'] ?? '');
$parola = $_POST['parola'] ?? '';

if ($kullanici === '' || $parola === '') {
    exit('Tüm alanları doldurun.');
}

$parolaOzeti = password_hash($parola, PASSWORD_DEFAULT);
echo 'Veriler işlenmeye hazır.';
```

`trim` gereksiz boşlukları temizler, `password_hash` ise parolayı düz metin olarak saklamak yerine güvenli bir özet üretir. Ancak POST tek başına şifreleme sağlamaz; gerçek gizlilik için mutlaka **HTTPS** kullanılmalıdır.

## GET ve POST karşılaştırması

| Özellik | GET | POST |
|---|---|---|
| Veri konumu | URL sorgu dizesi | İstek gövdesi |
| Görünürlük | Adres çubuğunda görünür | URL’de görünmez |
| Paylaşılabilirlik | Kolaydır | Doğrudan mümkün değildir |
| Tipik kullanım | Arama ve filtreleme | Kayıt ve güncelleme |
| Veri miktarı | URL sınırlarına bağlı | Sunucu ayarlarına bağlı |
| Güvenlik | Hassas veriye uygun değil | HTTPS ile daha uygundur |

## Güvenlik altın kuralı

İstemciden gelen hiçbir veri güvenilir kabul edilmemelidir. Kullanıcı sayı beklenen yere metin, HTML veya kötü niyetli SQL gönderebilir. Bu yüzden verileri **doğrulamak**, uygun biçime dönüştürmek ve veritabanı işlemlerinde prepared statement kullanmak gerekir.

Ayrıca isteğin metodunu kontrol etmek kodun niyetini belirginleştirir:

```php
<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Yalnızca POST ile gelen form burada işlenir.
}
```

Özetle GET okunabilir ve paylaşılabilir sorguların, POST ise sunucuda değişiklik oluşturan form işlemlerinin doğal tercihidir. `$_GET` ve `$_POST` yalnızca veri taşıyan diziler değildir; doğru doğrulama, HTTPS ve güvenli çıktı yöntemleriyle birlikte sağlam PHP uygulamalarının temelini oluştururlar.
