---
title:  PHP superglobal'ler
author: sonsuz
date: 2023-08-05 01:18:16 +0300
categories: [Program,PHP]
tags: [program,php,superglobal,değişken,web,post,get]
---


PHP'de, genel ya da fonksiyon içindeki tüm kodlar tarafından kullanılabilen önceden tanımlanmış değişkenlere Superglobals değişkenler adı verilir. Bu değişkenlere fonksiyonlar içinden erişim sağlamak için ayrıca global olarak tanımlamak gerekmez.

## $GLOBALS değişkeni

$GLOBALS değişkeni, PHP kodları içinde global alandaki tüm değişkenlere erişimi sağlar. Bu değişkene bağlı olan bir dizi içinde PHP kodları içinde tanımlanmış olan tüm değişkenlere ait referanslar yer alır.

Örnek

```php
<?php
  $deg = 17;
   
  function fonk1()
  {  
     $deg = 24;	  
	  
     // Lokal $deg değişken değerini ekrana yazar.
     echo $deg . '<br/>';  
     // Global $deg değişken değerini ekrana yazar.
     echo $GLOBALS['deg'] . '<br/>';
  }
   
  fonk1(); // Ekrana 24 ve 17 yazar.
  // Global $deg değişken değerini ekrana yazar.
  echo $deg;
?>


```

Yukarıdaki dosyayı çalıştırdığımızda, web tarayıcımızda aşağıdaki ifadeler karşımıza çıkar:

```

24
17
17

```

Yukarıdaki PHP dosyasında, biri global diğeri lokal olmak üzere iki adet değişken tanımlanmış, global değişkene fonk1() fonksiyonu içinden erişim için $GLOBALS değişkeni kullanılmıştır. Global değişkeni fonksiyon dışından yazdırmak için, sadece değişken adını kullanmak yeterlidir.

$GLOBALS değişkeni ile birlikte değişken adını kullanırken, değişken adından önce $ işaretinin yer almadığına, değişken adının parantez içinde yazıldığına dikkat ediniz.

## $\_SERVER değişkeni

$\_SERVER değişkeni, başlık, yol tanımlamaları ve kod yerleri gibi bilgileri içeren bir dizidir. Bu dizide yer alan tüm değerler web sunucusu tarafından oluşturulur. Ancak, bu değerlerin bazılarının sunucu tarafından oluşturulmama olasılığı vardır.

$\_SERVER dizisi içinde yer alan değerlerden bazıları aşağıdaki tabloda yer almaktadır:

$\_SERVER['PHP\_SELF'] 
: Çalışmakta olan PHP dosyasının yol tanımlamasını verir. Web sitesinin alan adını içermez.

$\_SERVER['SERVER\_ADDR'] 
: PHP dosyasının çalıştığı sunucunun IP adresini verir.

$\_SERVER['SERVER\_NAME'] 
: PHP dosyasının çalıştığı sunucunun adını verir (www.bilgigunlugum.net).

$\_SERVER['SERVER\_SOFTWARE'] 
: PHP dosyasının çalıştığı sunucu yazılımlarını gösterir (Apache/2.4.4 (Win64) PHP/5.4.12).

$\_SERVER['SERVER\_PROTOCOL'] 
: PHP sayfasının protokolü hakkında bilgi verir (HTTP/1.1).

$\_SERVER['REQUEST\_METHOD'] 
: PHP sayfasına erişim için kullanılan yöntemi verir (GET, POST gibi).

$\_SERVER['REQUEST\_TIME'] 
: PHP sayfasına erişim zamanını verir (1404204558 gibi, PHP 5.1.0 ile eklendi).

$\_SERVER['REQUEST\_TIME\_FLOAT'] 
: PHP sayfasına erişim zamanını mikrosaniye değeriyle verir (1404204558.077 gibi, PHP 5.4.0 ile eklendi).

$\_SERVER['QUERY\_STRING'] 
: PHP sayfasına erişimde, geçirilen parametreleri verir.

$\_SERVER['DOCUMENT\_ROOT'] 
: PHP sayfasının çalıştığı root dizini verir (WampServer kurulumunda C:/wamp/www).

$\_SERVER['HTTP\_ACCEPT'] 
: Eğer varsa, PHP sayfasındaki başlık bilgilerini verir (text/html,application/xhtml+xml,application/xml;q=0.9,\*/\*;q=0.8 gibi).

$\_SERVER['HTTP\_ACCEPT\_CHARSET'] 
: Eğer varsa, PHP sayfasındaki karakter seti bilgilerini verir (iso-8859-9 gibi).

$\_SERVER['HTTP\_ACCEPT\_ENCODING'] 
: Eğer varsa, PHP sayfasındaki kodlama bilgilerini verir (gzip, deflate gibi).

$\_SERVER['HTTP\_ACCEPT\_LANGUAGE'] 
: Eğer varsa, PHP sayfasındaki dil bilgilerini verir (tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3 gibi).

$\_SERVER['HTTP\_CONNECTION'] 
: Eğer varsa, PHP sayfasındaki bağlantı bilgilerini verir (keep-alive gibi).

$\_SERVER['HTTP\_HOST'] 
: PHP sayfasının hosting bilgilerini verir (localhost gibi).

$\_SERVER['HTTP\_REFERER'] 
: PHP sayfasının adres bilgilerini verir (http://localhost/ gibi). Bazen bu değer elde edilemeyebilir.

$\_SERVER['HTTP\_USER\_AGENT'] 
: PHP sayfasına giriş yapan kullanıcının sistem bilgilerini verir (Mozilla/5.0 (Windows NT 6.2; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0 gibi).

$\_SERVER['HTTPS'] 
: PHP sayfasına güvenli HTTPS protokolü ile giriş yapılıp yapılmadığı hakkında bilgi verir.

$\_SERVER['REMOTE\_ADDR'] 
: Aktif PHP sayfasını görüntüleyen kullanıcının IP adresini verir.

$\_SERVER['REMOTE\_HOST'] 
: Aktif PHP sayfasını görüntüleyen kullanıcının Host adını verir.

$\_SERVER['REMOTE\_PORT'] 
: Kullanıcının cihazında web sunucu ile haberleşmek için kullanılan bilgisini verir.

$\_SERVER['REMOTE\_USER'] 
: Kullanıcı bilgisini verir.

$\_SERVER['REDIRECT\_REMOTE\_USER'] 
: Eğer talep dahili olarak yeniden yönlendirilmişse, kllanıcı bilgisini verir.

$\_SERVER['SCRIPT\_FILENAME'] 
: Çalışmakta olan PHP dosyasının tam yol tanımlamasını verir (C:/wamp/www/deneme/index.php gibi).

$\_SERVER['SERVER\_ADMIN'] 
: Web sunucu konfigürasyon dosyasındaki SERVER\_ADMIN (Apache için) direktifine atanan değeri verir (admin@example.com gibi).

$\_SERVER['SERVER\_PORT'] 
: Web sunucu tarafından iletişim amacıyla kullanılan sunucu cihazundaki port değerini verir (80 gibi).

$\_SERVER['SERVER\_SIGNATURE'] 
: Web sunucu sürümünü ve sanak host adını içeren karakter dizisini verir.

$\_SERVER['PATH\_TRANSLATED'] 
: Çalışmakta olan PHP dosyasının dosya sistemine bağlı yol tanımlamasını verir.

$\_SERVER['SCRIPT\_NAME'] 
: Çalışmakta olan PHP dosyasının yol tanımlamasını verir.

$\_SERVER['REQUEST\_URI'] 
: Çalışmakta olan PHP dosyasının URI değerini verir.

$\_SERVER['PHP\_AUTH\_DIGEST'] 
: Digest HTTP authentication işleminde, bu değişken istemci tarafından gönderilen 'Authorization' başlık değerini alır.

$\_SERVER['PHP\_AUTH\_USER'] 
: HTTP authentication işleminde, bu değişken kullanıcı tarafından girilen kullanıcı adını alır.

$\_SERVER['PHP\_AUTH\_PW'] 
: HTTP authentication işleminde, bu değişken kullanıcı tarafından girilen parolayı alır.

$\_SERVER['AUTH\_TYPE'] 
: HTTP authentication işleminde, bu değişken authentication tipini alır.

$\_SERVER['PATH\_INFO'] 
: Çalışmakta olan PHP dosyasının istemci tarafından verilen yol tanımlamasını verir.

$\_SERVER['ORIG\_PATH\_INFO'] 
: 'PATH\_INFO' değerinin PHP tarafından işlem görmeden önceki halini verir.

## $\_GET değişkeni

$\_GET değişkeni, web tarayıcısında açılan aktif PHP sayfasına, tarayıcıdaki web sayfa adresi satırından URL parametreleri yoluyla geçirilen değişkenler dizisidir.

Eğer siteadi.com adlı bir sitenin index.php dosyasını web tarayıcınızın adres satırından aşağıdaki şekilde çağırırsanız, 'Matematik' karakter dizisini 'ders' adı ile index.php adlı dosyaya parametre olarak geçirmiş olursunuz:

http://siteadi.com/index.php?ders=Matematik

Örnek

```php
<?php
   echo $deg . '<br/>';  
   echo 'Dersin adı: ' . htmlspecialchars($_GET["ders"]);	 
?>


```

Yukarıdaki dosyayı çalıştırdığımızda, web tarayıcımızda aşağıdaki ifadeler karşımıza çıkar:

```

Dersin adı: Matematik

```

PHP dosyası içinde adres satırından aktarılan ve $GET dizini içinde ders anahtar adı ile yer alan Matematik karakter dizisi değeri echo komutu ile ekrana yazılır.

## $\_POST değişkeni

$\_POST değişkeni, web tarayıcısında açılan aktif PHP sayfasına HTTP POST metodu yoluyla geçirilen değişkenler dizisidir.

$\_POST değişkenini kullanarak, bir HTML veya PHP dosyasındaki FORM için post metodu tanımladığımızda, form içindeki değişken değerlerini formun içinde bulunduğu veya farklı bir PHP dosyasına aktarabiliriz.

1. Aynı PHP dosyasına değer aktarma

Aşağıdaki index.php adlı dosyada, bir form içinde bir veri girişi alanı ile submit butonu yer almaktadır. Eğer veri giriş alanına "Fizik" değerini girer ve submit butonuna tıklarsanız, form değerleri formun action bölümünde tanımlı dosyaya aktarılır. Burada, form değerleri aynı dosyaya aktarılacağından, $\_SERVER['PHP\_SELF'] değişkeni kullanılmaktadır. Dosyaya değer aktarıldıktan sonra, $\_POST['ders'] değişkeni bir değer içerdiğinden, PHP kodları devreye girer ve gönderilen değeri ekrana yazar.

Örnek

```php
<html>
<body>

<form method="post" action="<?php echo $_SERVER['PHP_SELF'];?>">
Ders adı: <input type="text" id="ders" name="ders">
<input type="submit" value="Gönder">
</form>

<?php
  if (!empty($_POST['ders'])) {
      $ders = $_POST['ders'];
      echo 'Dersin adı: ' . $ders;
  }
?>

</body>
</html>


```

Yukarıdaki dosyayı çalıştırdığımızda, web tarayıcımızda aşağıdaki ifadeler karşımıza çıkar:

```

Dersin adı: Fizik

```

2. Farklı bir PHP dosyasına değer aktarma

Aşağıdaki form.php adlı dosyada, bir form içinde bir veri girişi alanı ile submit butonu yer almaktadır. Eğer veri giriş alanına "Fizik" değerini girer ve submit butonuna tıklarsanız, form değerleri formun action bölümünde tanımlı formislem.php dosyasına aktarılır. Değer aktarıldıktan sonra, formislem.php dosyası içinde, PHP kodları devreye girer ve gönderilen değeri ekrana yazar.

form.php (Aktaran dosya)

```php
<html>
<body>

<form method="post" action="formislem.php">
Ders adı: <input type="text" id="ders" name="ders">
<input type="submit" value="Gönder">
</form>

</body>
</html>


```

formislem.php (Aktarılan dosya)

```php
<html>
<body>

<?php
  if (!empty($_POST['ders'])) {
      $ders = $_POST['ders'];
      echo 'Dersin adı: ' . $ders;
  }
?>

</body>
</html>


```

Yukarıdaki form.php dosyasında veri giriş alanına "Fizik" değerini girip submit butonuna bastığınızda, formislem.php dosyası çağrılır ve web tarayıcınızda aşağıdaki ifadeler karşınıza çıkar:

```

Dersin adı: Fizik

```

## $\_FILES değişkeni

$\_FILES değişkeni, web tarayıcısında açılan aktif PHP sayfasına HTTP POST metodu yoluyla upload edilen dosya ile ilgili bilgileri içeren değişkenler dizisidir. Değişken içindeki değerler, dosyanın adını, boyutunu, tipini, geçici olarak verilen dosya adını ve eğer varsa meydana gelen hata kodunu içerir.

Aşağıdaki formdosya.php adlı dosyada, bir form içinde bir dosya adı giriş alanı ile submit butonu yer almaktadır. Eğer dosya adı giriş alanında bir dosya adı seçer ve submit butonuna tıklarsanız, dosya ile ilgili değerler formun action bölümünde tanımlı islemdosya.php dosyasına aktarılır. Değer aktarıldıktan sonra, islemdosya.php dosyası içinde, PHP kodları devreye girer ve gönderilen değerleri ekrana yazar.

formdosya.php (Dosya aktarımı yapan dosya)

```php
<html>
<body>

<form method="post" action="islemdosya.php" enctype="multipart/form-data">
Dosya adı: <input type="file" id="dosya" name="dosya">
<input type="submit" value="Gönder">
</form>

</body>
</html>


```

islemdosya.php (Dosyanın aktarıldığı dosya)

```php
<html>
<body>

<?php
  if ($_FILES["file"]["error"] > 0) {
      echo "Hata: " . $_FILES["dosya"]["error"] . "<br/>";
  } 
  else {
      echo "Dosya adı: " . $_FILES["dosya"]["name"] . "<br/>";
      echo "Dosya tipi: " . $_FILES["dosya"]["type"] . "<br/>";
      echo "Dosya boyutu: " . ($_FILES["dosya"]["size"] / 1024) . " kB<br/>";
      echo "Dosya geçici adı: " . $_FILES["dosya"]["tmp_name"];
  }
?>

</body>
</html>


```

## $\_REQUEST değişkeni

$\_REQUEST değişkeni, $\_GET, $\_POST ve $\_COOKIE değişkenlerinin değerlerini içeren değişkenler dizisidir.

Örneğin, $\_POST değişkenini kullanarak, bir HTML veya PHP dosyasındaki FORM için post metodu tanımladığınızda, form içindeki değişken değerlerini formun içinde bulunduğu bir PHP dosyasına aktardığınızda, aktarılan değerlere erişim sağlamak için, $\_POST değişkeni yerine $\_REQUEST değişkeni kullanabilirsiniz.

Aşağıdaki index.php adlı dosyada, bir form içinde bir veri girişi alanı ile submit butonu yer almaktadır. Eğer veri giriş alanına "Fizik" değerini girer ve submit butonuna tıklarsanız, form değerleri formun action bölümünde tanımlı dosyaya aktarılır. Burada, form değerleri aynı dosyaya aktarılacağından, $\_SERVER['PHP\_SELF'] değişkeni kullanılmaktadır. Dosyaya değer aktarıldıktan sonra, $\_REQUEST['ders'] değişkeni bir değer içerdiğinden, PHP kodları devreye girer ve gönderilen değeri ekrana yazar.

Örnek

```php
<html>
<body>

<form method="post" action="<?php echo $_SERVER['PHP_SELF'];?>">
Ders adı: <input type="text" id="ders" name="ders">
<input type="submit" value="Gönder">
</form>

<?php
  if (!empty($_REQUEST['ders'])) {
      $ders = $_REQUEST['ders'];
      echo 'Dersin adı: ' . $ders;
  }
?>

</body>
</html>


```

Yukarıdaki dosyayı çalıştırdığımızda, web tarayıcımızda aşağıdaki ifadeler karşımıza çıkar:

```

Dersin adı: Fizik

```

## $\_SESSION değişkeni

$\_SESSION değişkeni, aktif PHP dosyası içindeki session değişkenlerini değerlerini içeren değişkenler dizisidir.

$\_SESSION dizini, bir kullanıcı bilgisayarındaki tarayıcıyı kullanarak bir web sayfasını açtığında, farklı sayfalarda gezinirken bazı ortak değerlerin kaydedilmesi ve istenildiğinde kullanılması amacıyla kullanılır. Kullanıcı açtığı web sitesinin hangi sayfasında olursa olsun, $\_SESSION dizinine atanmış değerlere erişim sağlamak mümkündür.

$\_SESSION değerleri sunucuya kaydedildiğinden, kullanıcı web sayfasını kapattığında, oturum da otomatik olarak kapatıldığından, $\_SESSION değerleri silinir. 

Kullanıcı oturum açtıktan sonra sunucuya kaydedilen $\_SESSION değerlerini, kullanıcının sonraki oturum açışlarında kullanabilmek için, bir veritabanına kaydetmek gerekir.

## $\_ENV değişkeni

$\_ENV değişkeni, aktif PHP dosyasına environment metodu ile aktarılan değişkenler dizisidir.

Bu değişkenler, PHP parser'ın çalıştığı ortamdan PHP'nin global namespace alanına aktarılır.

phpinfo() fonksiyonu ile tarayıcı ekranınızda görebileceğiniz tüm ortam değişkenlerine erişim için, $\_ENV değişkenini veya getenv() fonksiyonunu kullanabilirsiniz.

Örnek

```php
<html>
<body>

<?php
  echo 'Bilgisayar adı: ' . $_ENV['COMPUTERNAME'] . "<br/>";
  echo 'Bilgisayar adı: ' . getenv('COMPUTERNAME');
?>

</body>
</html>


```

Yukarıdaki dosyayı çalıştırdığınızda, web tarayıcınızda çalıştığınız bilgisayar adı ekrana yazılır.

## $\_COOKIE değişkeni

$\_COOKIE değişkeni, aktif PHP dosyasına HTTP Cookie'ler yoluyla aktarılan değişkenler dizisidir.

Örnek

```php
<html>
<body>

<?php
   echo 'Dersin adı: ' . htmlspecialchars($_COOKIE["ders"]);
?>

</body>
</html>


```

Daha önceden, $\_COOKIE dizinine ders adı altında Kimya değeri verdiğimizi kabul ederek, yukarıdaki dosyayı çalıştırdığınızda, web tarayıcınızda aşağıdaki ifadeler karşınıza çıkar:

```

Dersin adı: Kimya

```
