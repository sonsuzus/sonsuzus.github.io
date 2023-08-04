---
title:  PHP include işlemleri
author: sonsuz
date: 2023-08-04 12:17:21 +0300
categories: [Program,PHP]
tags: [php,programlama,include,web]
---


## include, require, include\_once ve require\_once deyimleri

include() deyimi tanımladığı dosyayı içinde bulunduğu PHP dosyasına ekler. Eklenen dosyanın içinde ye alan PHP kodları include() deyiminin kullanıldığı satırda yazılmış gibi işlem görür.

Dahil edilecek dosyalar, dosya yolu gösteren dizin tanımlanmış ise dosya yoluna göre, tanımlanmamış ise include\_path değeri içinde tanınlanmış yollara göre aktif dosyaya dahil edilir. Eğer dosya include\_path içinde tanımlanan yollarda bulunamazsa, include() aktif PHP dosyasının yer aldığı dizini kontrol eder. Dosya burada da bulunamazsa, include() deyimi bir hata verir.

Eğer bir yol tanımlaması yapılmışsa, include\_path değeri dikkate alınmaz.

require() deyimi ile include() deyimi ile aynı işlemi gerçekleştirir. Tek farkı hata durumunda E\_COMPILE\_ERROR seviyesinde bir hata vermesidir. seviyesinden ölümcül bir hata vermesi dışında include() deyimi ile aynıdır. include() deyiminin sadece bir uyarı (E\_WARNING) vererek çalışmayı sürdürdüğü durumda require() deyimi PHP kodlarının durmasına neden olur.

include\_once() deyimi ile include() deyimi ile aynı işlemi gerçekleştirir. Tek farkı, önceden dahil edilmiş olan dosyaların tekrar dahil edilmemesidir. Böylelikle, bir dosyanın iki kez dahil edilmesi önlenmiş olur.

require\_once() deyimi ile require() deyimi ile aynı işlemi gerçekleştirir. Tek farkı, önceden dahil edilmiş olan dosyaların tekrar dahil edilmemesidir. Böylelikle, bir dosyanın iki kez dahil edilmesi önlenmiş olur.

Bir PHP dosyası diğer bir PHP dosyası içine dahil edildiğinde, çağıran dosyada dahil etme işleminin yapıldığı satıra kadar tanımlanmış olam tüm değişkenler dahil edilen dosya içinde kullanılabilir. Ayrıca, dahil edilen dosya içinde yapılan fonksiyon ve sınıf tanımlamaları ana dosyanın tamamında geçerlidir.

Örnek

```php
// dosya01.php ve deneme.php aynı dizinde olmalıdır!

// dosya01.php
<?php
    $deg01 = 7;
    $deg02 = 25;

    class personel
    {
        public $adi; 
        public $soyadi; 
        public $yasi;
	
        function yaz_bilgi() {
           echo $this->adi . " " . $this->soyadi . " " . $this->yasi . '<br/>';
        }
    }
   
    function fonk1() {
        echo "Dahil edilen dosya içindeki fonksiyon karakter dizisi<br/>";   
    }
   
    echo "$deg03 <br/>";   
?>

// deneme.php
<html>
<body>

<?php      
    $deg03 = 83;
   
    include ("dosya01.php");
   
    $obj_per = new personel;

    $obj_per->adi = "Mehmet";       
    $obj_per->soyadi = "Çalışkan";  
    $obj_per->yasi = 25;            

    $obj_per->yaz_bilgi();
   
    fonk1();
   
    echo "$deg01 $deg02 <br/>";
   
    echo "Çağıran dosya karakter dizisi";   
?>

</body>
</html>


```

Yukarıdaki dosyayı çalıştırdığımızda, web taracıyımızda aşağıdaki ifadeler karşımıza çıkar:

```

83
Mehmet Çalışkan 25
Dahil edilen dosya içindeki fonksiyon karakter dizisi
7 25
Çağıran dosya karakter dizisi

```

Dahil etme işlemi çağıran dosyanın bir fonksiyonu içinde yapılırsa, dahil edilen dosyanın içindeki tüm kodlar o fonksiyon içinde yazılmış gibi işlem görür. 

Örnek

```php
// dosya01.php ve deneme.php aynı dizinde olmalıdır!

// dosya01.php
<?php
    $deg01 = 7;   
?>

// deneme.php
<html>
<body>

<?php      
    function fonk1() {
        include ("dosya01.php");
	  
        echo "$deg01<br/>";
    }
   
    fonk1();
    echo "$deg01"; // Ekrana herhangi bir değer yazmaz.   
?>

</body>
</html>


```

Yukarıdaki dosyayı çalıştırdığımızda, web taracıyımızda aşağıdaki ifadeler karşımıza çıkar:

```

7

```
