---
title:  PHP session
author: sonsuz
date: 2023-08-05 01:34:16 +0300
categories: [Program,PHP]
tags: [programlama,php,session,oturum,web,çerez]
---


Bir kullanıcı bir web sitesine girip çıktıktan sonra; kullanıcının o web sitesinin sayfalarında girdiği veriler tamamen kaybolur. Eğer bu verilerin saklanmasına ihtiyaç duyulursa, çerezler (Cookies) veya oturumlar (Sessions) kullanılır.

Çerez ve oturumun en önemli farkı; çerezlerin kullanıcının bilgisayarındaki tarayıcıya, oturum değerlerinin ise sunucuya kaydedilmesidir.

Oturumlar sadece kullanıcının sunucu üzerinde tanımlanabilmesi için eşsiz bir değer (UID) içeren bir çerez kullanır. Oturumlar her kullanıcı için bir UID oluştur ve bu UID'ye göre değişkenleri kaydederek çalışır.

PHP'de oturumlar daha sonraki sayfa girişlerinde belirli verileri saklamaya yarar. Kullanıcının herhangi bir web sayfasına giriş yaptıktan sonra girdiği değerler oturum değişkenlerine aktarılır. Böylece kullanıcı aynı sayfayı tekrar çağırdığında veya aynı web sitesinin farklı sayfalarına giriş yaptığında; oturum değişkenlerinde saklanan veriye, tekrar veri girişi yapmaya gerek kalmadan, erişim sağlar. Oturum değişkenleri sadece tek bir kullanıcı için bilgiler içerir

Bir kullanıcı bir web sitesine girdiğinde, kullanıcı tarafından girilen bilgiler ilerde kullanılmak üzere PHP tarafından SESSION değişkenine atanır. PHP aynı bilgileri, kullanıcı web sitesinden çıktıktan sonra korumak için, bir veritabanına kaydeder.

Oturum (SESSION) çalışma sırası:

- Oturumda kullanıcı bilgilerini kaydetmeden önce, öncelikle session\_start() komutu ile oturumun başlatılması gerekir.

session\_start() komutu <html> ifadesinden önce yer almalıdır.

Bu komutla kullanıcının oturumu sunucuya kaydedilir ve oturum için bir UID tahsis edilir.

- Oturum başlatıldıktan sonra $\_SESSION değişkeni kullanılarak oturum değişkenleri kaydedilir ve bu değişkenlere erişim sağlanır.

- isset() değişkeni kullanılarak oturum değişkenlerinin tanımlanıp tanımlanmadığı kontrol edilir.

- Oturum tanınmlanan değişkenleri silmek için unset() metodunu ve kullanıcı oturum bilgilerini tamamen silmek için session\_destroy() metodunu kullanabilirsiniz:

Bir oturum değişkenini unset() metodu ile sildiğinizde aynı sayfada o değişkene bir daha erişim sağlayamazsınız. Ancak; session\_destroy() metodunu kullandığınızda, sayfayı kapatmadığınız sürece oturum değişkenlerine erişim sağlayabilirsiniz.

Örnek

```php
<?php
   // Oturumu başlatır.
   session_start();
?>

<html>
<body>

<?php
   // Oturum verilerini kaydeder.
   $_SESSION['degerint01']=24;
   $_SESSION['degerint02']=35;
   $_SESSION['degerstr']="Oturum karakter dizisi";
   // Oturum değişkenlerini ekrana yazar.
   echo "Veriler: " . $_SESSION['degerint01'] . " " . $_SESSION['degerint02'] . " " . $_SESSION['degerstr'] . "</br>";
   
   // degerint01 oturum değişkenini siler.
   if(isset($_SESSION['degerint01'])) unset($_SESSION['degerint01']);

   // Sadece degerint01 oturum değişkeninin yazılmadığına dikkat ediniz.   
   echo "Veriler: " . $_SESSION['degerint01'] . " " . $_SESSION['degerint02'] . " " . $_SESSION['degerstr'] . "</br>";
   
   // Kullanıcı oturumunu komple siler.
   session_destroy();

   // session_destroy() komutu kullanıldığı halde aynı sayfada unset() metodu 
   ile silinmeyen tüm değişkenlere halen erişildiğine dikkat ediniz.
   echo "Veriler: " . $_SESSION['degerint01'] . " " . $_SESSION['degerint02'] . " " . $_SESSION['degerstr'] . "</br>";
?>

</body>
</html>


```

Yukarıdaki dosyayı çalıştırdığımızda, web tarayıcımızda aşağıdaki ifadeler karşımıza çıkar:

```

Veriler: 24 35 Oturum karakter dizisi
Veriler: 35 Oturum karakter dizisi
Veriler: 35 Oturum karakter dizisi

```
