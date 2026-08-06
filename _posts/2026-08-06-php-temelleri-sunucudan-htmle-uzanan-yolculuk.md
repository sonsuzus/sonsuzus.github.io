---
layout: post
title: "PHP Temelleri: Sunucudan HTML’e Uzanan Yolculuk"
math: true
categories: 
  - Bilgi
tags: 
  - PHP
  - Web Programlama
  - Sunucu Tarafı
---

Bir web sayfasındaki kullanıcı adı, ürün listesi veya sepet tutarı kendiliğinden ortaya çıkmaz. Perdenin arkasında çalışan PHP; isteği karşılar, verileri işler ve tarayıcıya gönderilecek HTML çıktısını üretir. Tarayıcı PHP kodunu görmez; yalnızca onun hazırladığı sonucu görür. Gelin bu mutfağa girip PHP’nin çalışma mantığını, sözdizimini ve veri tiplerini inceleyelim.
``
## PHP nasıl çalışır?

PHP, **sunucu tarafında** çalışan yorumlanan bir programlama dilidir. Kullanıcı `profil.php` adresini açtığında süreç kabaca şöyledir:

1. Tarayıcı sunucuya HTTP isteği gönderir.
2. Web sunucusu `.php` dosyasını PHP yorumlayıcısına iletir.
3. PHP kodu çalışır; gerekirse veritabanı veya dosyalarla iletişim kurar.
4. Üretilen HTML istemciye gönderilir.
5. Tarayıcı gelen HTML’yi ekranda gösterir.

Toplam yanıt süresini basitçe şöyle düşünebiliriz:

$$T_{yanıt}=T_{ağ}+T_{PHP}+T_{veritabanı}$$

PHP kodunun tarayıcıya gönderilmemesi hem uygulama mantığını gizler hem de sunucuda güvenli işlemler yapılabilmesini sağlar. Ancak bu durum kodun otomatik olarak güvenli olduğu anlamına gelmez; kullanıcı girdileri yine doğrulanmalıdır.

| Özellik | PHP | JavaScript (tarayıcıda) |
|---|---|---|
| Çalıştığı yer | Sunucu | İstemci |
| Veritabanına doğrudan erişim | Yapabilir | Genellikle yapamaz |
| Kaynak kodunu kullanıcı görür mü? | Hayır | Evet |
| Temel görevi | Dinamik çıktı ve veri işlemleri | Arayüz ve kullanıcı etkileşimi |

## Temel sözdizimi

PHP kodu `<?php` etiketiyle başlar. Komutların çoğu noktalı virgülle biter ve değişken adlarının önünde `$` bulunur.

```php
<?php
$isim = "Ada";
$yas = 28;

if ($yas >= 18) {
    echo "Merhaba, " . $isim . "!";
} else {
    echo "Erişim için yaşınız yeterli değil.";
}
```

Burada `.` operatörü metinleri birleştirir. `echo`, oluşturulan metni HTTP çıktısına ekler. Değişkenin tipi ayrıca belirtilmemiştir; PHP, atanan değere bakarak türü çalışma anında belirler.

PHP değişken adları büyük-küçük harfe duyarlıdır. Dolayısıyla `$isim` ile `$Isim` aynı değişken değildir. Açıklamalar `//`, `#` veya çok satırlı içerikler için `/* ... */` kullanılarak yazılabilir.

## Veri tipleri

PHP’nin sık kullanılan veri tipleri aşağıdaki gibidir:

| Veri tipi | Örnek | Kullanım amacı |
|---|---|---|
| `string` | `"Merhaba"` | Metin saklamak |
| `int` | `42` | Tam sayılar |
| `float` | `19.95` | Ondalıklı sayılar |
| `bool` | `true` | Mantıksal durumlar |
| `array` | `["PHP", "HTML"]` | Birden fazla değer |
| `null` | `null` | Değer bulunmadığını belirtmek |

```php
<?php
$urun = "Klavye";
$fiyat = 850.50;
$stoktaMi = true;
$etiketler = ["donanım", "aksesuar"];

$kdvliFiyat = $fiyat * 1.20;
echo $kdvliFiyat;
```

Bu örnek ürün bilgilerini farklı veri tipleriyle saklar ve yüzde 20 KDV ekler. Matematiksel karşılığı $F_{son}=F_{ilk}\times1.20$ biçimindedir. Bir değişkenin tipini görmek için `gettype($fiyat)`, ayrıntılı içeriğini incelemek için `var_dump($fiyat)` kullanılabilir.

## PHP’yi HTML içine gömmek

PHP’nin güçlü yanlarından biri, HTML arasında yalnızca ihtiyaç duyulan bölgelerde kullanılabilmesidir:

```php
<?php
$kullanici = "Deniz";
$dersler = ["PHP", "MySQL", "HTML"];
?>

<h2>Hoş geldin, <?= htmlspecialchars($kullanici) ?></h2>
<ul>
    <?php foreach ($dersler as $ders): ?>
        <li><?= htmlspecialchars($ders) ?></li>
    <?php endforeach; ?>
</ul>
```

`<?= ... ?>`, bir değeri kısa yoldan ekrana yazdırır. `foreach` dizideki her ders için bir `<li>` üretir. `htmlspecialchars()` ise özel HTML karakterlerini dönüştürerek zararlı içeriklerin sayfaya kod olarak basılmasını önlemeye yardımcı olur.

Özetle PHP, sunucuda hesap yapan ve sonuç olarak HTML üreten bir mutfak şefidir. Değişkenleri, koşulları, dizileri ve döngüleri öğrendiğinizde statik sayfaları kullanıcıya ve veriye göre değişen gerçek web uygulamalarına dönüştürebilirsiniz.
