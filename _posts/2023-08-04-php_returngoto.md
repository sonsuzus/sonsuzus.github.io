---
title:  PHP return ve goto
author: sonsuz
date: 2023-08-04 12:28:15 +0300
categories: [Program,PHP]
tags: [programlama,php,return]
---


## return deyimi

return deyimi bir fonksiyonda kullanıldığında içinde bulunduğu fonksiyonun çalışmasını sona erdirir ve kendisine geçirilen değeri fonksiyon çağrısı değeri olarak döndürür. return deyimi aynı zamanda eval() fonksiyonunun veya PHP kod dosyasının çalışmasını sona erdirir.

Global olarak çağrıldığında, içinde bulunduğu komut dosyasının çalışmasını sona erdirir. Eğer aktif dosya include() ya da require() fonksiyonu ile başka bir dosyaya dahil edilmiş ise, return() deyimi kontrolu ana dosyaya aktarır. Eğer aktif dosya include() fonksiyonu ile başka bir dosyaya dahil edilmiş ise return() deyimine geçirilen değer include() çağrısının değeri olarak geri döndürülür.

Eğer return() deyimi ana komut dosyasından çağrılırsa, PHP komutlarının çalıştırılması sona erer.

* return deyimine değer geçirilmezse parentez kullanılmamalıdır. Değer geçirildiğinde ise parentez kullanmak gerekli değildir.

* Bir değişken referans olarak döndürülebilir, ancak bir deyimin sonucu döndürülemez. Bir değişkeni referans olarak döndürürken, asla parantez kullanılmamalıdır.

Örnek

```php
<html>
<body>

<?php
    function fonk1 ($deg01, $deg02) {
        return $deg01 * $deg02;
    }

    echo fonk1 (2, 3);   
?>

</body>
</html>


```

Yukarıdaki dosyayı çalıştırdığımızda, web tarayıcımızda aşağıdaki ifadeler karşımıza çıkar:

```

6

```

Yukarıdaki PHP dosyasında, fonksiyon kendisine geçirilen değerlerin çarpımını geri verir.

Örnek

```php
// dosya01.php ve deneme.php aynı dizinde olmalıdır!

// dosya01.php
<?php
    echo "Dahil edilen dosya ilk satır<br/>";

    return;
   
    echo "Dahil edilen dosya ikinci satır";   
?>

// deneme.php
<html>
<body>

<?php
    include("dosya01.php");
 
    echo "Esas dosya birinci satır<br/>";
    echo "Esas dosya ikinci satır";   
?>

</body>
</html>


```

Yukarıdaki dosyayı çalıştırdığımızda, web tarayıcımızda aşağıdaki ifadeler karşımıza çıkar:

```

Dahil edilen dosya ilk satır
Esas dosya birinci satır
Esas dosya ikinci satır

```

Yukarıdaki PHP dosyasında, dahil edilen dosya01.php dosyasındaki ilk satır ekrana yazılır. Ancak, return deyimiyle dahil edilen dosyadaki komutların çalışması sona erdirildiğinden ikinci satır ekran yazılmaz.

## goto deyimi

goto işlemcisi PHP kod sayfasında başka bir komut satırına atlamak için kullanılır. Hedeflenen komut satırında bir isim ve üstüste iki nokta kullanılır. Hedef komut satırı aynı dosya içinde ve kapsamda bulunmalıdır. Başka bir ifade ile, bir fonksiyon içine dışarıdan veya bir fonksiyon içinden dışarıya atlama yapılamaz. Aynı zamanda, bir döngü veya switch yapısı içine de atlama yapılamaz.

Örnek

```php
<html>
<body>

<?php      
    $deg01 = 24;
    $deg02 = 37;
   
    goto hedef;
   
    echo "$deg01 "; // Bu işlem satırı çalışmadan geçilir. 

    hedef:
   
    echo "$deg02";   
?>

</body>
</html>


```

Yukarıdaki dosyayı çalıştırdığımızda, web tarayıcımızda aşağıdaki ifadeler karşımıza çıkar:

```

37

```
