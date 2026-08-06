---
layout: post
title: "PHP Kurulumu ve XAMPP/MAMP ile Yerel Sunucu Ortamı"
math: true
categories: 
  - Bilgi
tags: 
  - PHP
  - XAMPP
  - MAMP
---

PHP ile dinamik bir web uygulaması geliştirirken dosyaya çift tıklamak yeterli değildir. Tarayıcı PHP kodunu doğrudan çalıştıramaz; isteğin bir web sunucusuna ulaşması, PHP yorumlayıcısından geçmesi ve gerekiyorsa veritabanıyla konuşması gerekir. XAMPP ve MAMP, bu parçaları tek pakette sunarak bilgisayarımızı internete açmadan küçük bir geliştirme sunucusuna dönüştürür.

``

## Yerel sunucu neden gereklidir?

HTML, CSS ve JavaScript çoğunlukla tarayıcı tarafında çalışır. PHP ise sunucu taraflı bir dildir. Teknik olarak PHP kodları klasik anlamda doğrudan makine koduna derlenmek yerine PHP motoru tarafından işlenir; modern PHP sürümleri opcode ve JIT gibi optimizasyonlardan da yararlanabilir.

Tipik bir isteğin yolu şöyledir:

1. Tarayıcı `http://localhost/proje` adresine istek gönderir.
2. Apache isteği karşılar ve ilgili PHP dosyasını bulur.
3. PHP motoru kodu çalıştırır.
4. Gerekirse MySQL veya MariaDB sunucusuna sorgu gönderilir.
5. Üretilen HTML tarayıcıya döndürülür.

Toplam yanıt süresini basitçe şu şekilde düşünebiliriz:

$$T_{toplam} = T_{sunucu} + T_{PHP} + T_{veritabani} + T_{ag}$$

Yerel geliştirmede ağ gecikmesi çok düşük olduğundan kod ve veritabanı performansını daha rahat gözlemleyebiliriz.

## XAMPP ve MAMP karşılaştırması

| Özellik | XAMPP | MAMP |
|---|---|---|
| İşletim sistemleri | Windows, macOS, Linux | macOS ve Windows |
| Web sunucusu | Apache | Apache veya Nginx seçenekleri |
| Veritabanı | MariaDB | MySQL |
| Yönetim biçimi | Kontrol paneli | Masaüstü uygulaması |
| Kullanım yaklaşımı | Esnek ve yaygın | Özellikle macOS'ta sade |

Her iki araç da başlangıç için uygundur. Windows kullanıcıları genellikle XAMPP'ı, macOS kullanıcıları ise MAMP'ı tercih eder. Seçim yaparken projenin kullanacağı PHP sürümünü kontrol etmek önemlidir.

## Kurulum ve servislerin başlatılması

Paketi yalnızca resmi XAMPP veya MAMP sitesinden indirin. Kurulum sırasında en az Apache, PHP ve MySQL/MariaDB bileşenlerini seçin. XAMPP kullanıyorsanız kontrol panelinden **Apache** ve **MySQL** servislerini `Start` düğmesiyle çalıştırın. MAMP'ta ise **Start Servers** düğmesi aynı görevi üstlenir.

Tarayıcıda `http://localhost` adresini açtığınızda karşılama sayfasını görüyorsanız web sunucusu hazırdır. Apache başlamıyorsa çoğunlukla 80 veya 443 numaralı port başka bir uygulama tarafından kullanılıyordur. Bu durumda ilgili uygulamayı kapatabilir ya da Apache yapılandırmasında portu örneğin `8080` yapabilirsiniz. Yeni adresiniz `http://localhost:8080` olur.

## İlk PHP dosyasını çalıştırmak

XAMPP'ta proje dosyaları genellikle `htdocs`, MAMP'ta ise `htdocs` veya ayarlanan belge kökü içine yerleştirilir. `php-deneme` adlı klasörde `index.php` oluşturun:

```php
<?php
$uygulama = "Yerel PHP Sunucusu";
$saat = date("H:i:s");

 echo "<h1>{$uygulama}</h1>";
 echo "<p>Sunucu saati: {$saat}</p>";
?>
```

Bu kod bir değişken tanımlar, sunucu saatini hesaplar ve dinamik HTML üretir. Dosyayı doğrudan açmak yerine `http://localhost/php-deneme` adresine gidin. Kodun kendisi değil, oluşturduğu başlık ve saat görünmelidir.

Kurulu PHP sürümünü terminalden denetlemek için şu komutu kullanabilirsiniz:

```bash
php -v
```

Ancak terminaldeki PHP sürümüyle Apache'nin kullandığı sürüm farklı olabilir. Web tarafını kesin olarak kontrol etmek için geçici bir dosyada `phpinfo();` çalıştırabilirsiniz. Bu sayfa ayrıntılı sistem bilgileri gösterdiğinden inceleme sonrasında mutlaka silinmelidir.

## Veritabanını doğrulamak

XAMPP ve MAMP genellikle phpMyAdmin arayüzü sağlar. Buradan `deneme_db` adlı bir veritabanı oluşturabilir, tablo ve kullanıcıları yönetebilirsiniz. Geliştirme sırasında varsayılan yönetici hesabı pratik görünse de gerçek projelerde ayrı kullanıcı ve güçlü parola kullanın.

Yerel ortam artık hazırdır: Apache istekleri karşılar, PHP uygulama mantığını yürütür, MySQL veya MariaDB verileri saklar. Böylece internetteki sunucuya her değişiklikte dosya göndermek yerine hızlı, güvenli ve kahve dökülmesine dayanıklı sayılabilecek bir geliştirme döngüsü elde edersiniz.
