---
title:  PHP if yapıları
author: sonsuz
date: 2023-08-04 01:52:27 +0300
categories: [Program,PHP]
tags: [php,programlama,if,karşılaştırma,web]
---


PHP'de kodlar işlem satırlarından oluşur. Bir işlem satırı bir atama, bir fonksiyon çağrısı, bir döngü, koşul içeren bir işlem satırı veya hiçbir şey yapmayan boş bir işlem satırından oluşabilir. İşlem satırı noktalı virgül ile sonlandırılır. İşlem satırları { ve } işaretleri arasında tanımlanarak işlem satırı grubu oluşturulur.

PHP'de bir işlem satırı veya işlem satırı gruplarının belirli koşullara bağlı olarak çalıştırılması için kontrol yapıları kullanılır.

## if yapısı

PHP'de if yapısı kodların belli bir koşula bağlı olarak çalıştırılmasını sağlar.

```php
if (ifade) işlem satırı;
   
if (ifade) {   
    işlem satırı;
    .
    .
    işlem satırı
}


```

Eğer bir if deyiminden sonra gelen ifade sonucu TRUE olan boolean bir değer verirse, if deyiminden sonra gelen işlem satırı ya da işlem satırı grubu PHP tarafından çalıştırılır, aksi takdirde (FALSE bir değer geri verirse), dikkate alınmaz.

Örnek

```php
<html>
<body>

<?php
    $deg01 = 34;
    $deg02 = 23; 

    if ($deg01>$deg02) 
        echo "\$deg01 değişken değeri \$deg02 değişken değerinden büyüktür.<br/>"; 
   
    if ($deg01>$deg02) {
        $deg03 = $deg01 + $deg02;
        $deg04 = $deg01 - $deg02;
        echo "$deg03 $deg04";
    }   
?>

</body>
</html>

```

Yukarıdaki dosyayı çalıştırdığımızda, web tarayıcımızda aşağıdaki ifadeler karşımıza çıkar:

```

$deg01 değişken değeri $deg02 değişken değerinden büyüktür.
57 11

```

PHP'de belirli işlem satırlarının belirli koşullarda çalıştırabilmek için, sınırsız sayıda içiçe if deyimleri kullanabiliriz.

Örnek

```php
<html>
<body>

<?php
    $deg01 = 18;
    $deg02 = 42; 

    if ($deg01+$deg02>50) {
        echo "\$deg01 ve \$deg02 değişken değerleri toplamı 50'den büyüktür.<br/>"; 
        if ($deg01%2==0) {
            echo "\$deg01 değişken değeri çift bir sayıdır.<br/>"; 
            if ($deg02%2==0) {
                echo "\$deg02 değişken değeri çift bir sayıdır."; 
            }
        } 
    }   
?>

</body>
</html>


```

Yukarıdaki dosyayı çalıştırdığımızda, web tarayıcımızda aşağıdaki ifadeler karşımıza çıkar:

```

$deg01 ve $deg02 değişken değerleri toplamı 50'den büyüktür.
$deg01 değişken değeri çift bir sayıdır.
$deg02 değişken değeri çift bir sayıdır.

```

## if else yapısı

PHP'de if yapısında yer alan ifade doğru sonuç verdiğinde belirli işlem satırı ya da satırları çalıştırılmakta, yanlış sonuç verdiğinde ise herhangi bir işlem yapılmamaktadır. if deyimi ile ilgili ifade yanlış sonuç verdiğinde belirli işlem satırlarını çalıştırmak için ise else deyimi kullanılır. else deyimi daima if deyimi ile birlikte kullanılmalıdır.

```php
if (ifade) işlem satırı;
else işlem satırı; // if deyimi ifadesi yanlış sonuç verirse  


```

Örnek

```php
<html>
<body>

<?php
    $deg01 = 24;
    $deg02 = 11; 

    if ($deg01>$deg02) 
        echo "\$deg01 değişken değeri \$deg02 değişken değerinden büyüktür.<br/>"; 
    else echo "\$deg01 değişken değeri \$deg02 değişken değerinden büyük değildir.<br/>";
   
    if ($deg02>$deg01)
        echo "\$deg02 değişken değeri \$deg01 değişken değerinden büyüktür."; 
    else echo "\$deg02 değişken değeri \$deg01 değişken değerinden büyük değildir.";   
?>

</body>
</html>


```

Yukarıdaki dosyayı çalıştırdığınızda, web tarayıcınızda aşağıdaki ifadeler karşınıza çıkar:

```

$deg01 değişken değeri $deg02 değişken değerinden büyüktür.
$deg02 değişken değeri $deg01 değişken değerinden büyük değildir. 

```

## if elseif yapısı

PHP'de if yapısında yer alan ifade yanlış sonuç verdiğinde, alternatif ifadelerin kontrolü ile farklı işlem satırlarının çalışmasını sağlamak için if deyimi ile birlikte elseif deyimini kullanabilirsiniz. else deyiminden farklı olarak, elseif deyimi ile ilgili işlem satırının çalışması için elseif ile ilgili ifadenin doğru sonuç vermesi gerekir. elseif deyimi daima if deyimi ile birlikte kullanılmalıdır.

```php
if (ifade) işlem satırı;
elseif (ifade) işlem satırı;// if ifadesi yanlış sonuç verirse çalışır.
else işlem satırı;// if ve elseif ifadelerinin her ikisi de yanlış sonuç verirse çalışır.  


```

Bir if yapısı içinde birden fazla elseif deyimi kullanabiliriz. if elseif yapısı içinde, if deyimi de dahil olmak üzere, doğru sonuç veren ilk ifadenin yer aldığı satır çalıştırılır. Bir elseif deyimi işlem satırı, kendisinden önce gelen if ve/veya elseif deyimlerine bağlı ifadelerin tamamı yanlış sonuç verdiğinde ve kendi ifadesi doğru sonuç verdiğinde çalışır.

elseif deyimi 'else if' şelinde iki ayrı kelime olarak yazılabilir.

Örnek

```php
<html>
<body>

<?php
    $deg01 = 7;
    $deg02 = 15; 

    if ($deg01>$deg02) 
        echo "\$deg01 değişken değeri \$deg02 değişken değerinden büyüktür.<br/>"; 
    else if ($deg01==$deg02) 
        echo "\$deg01 ve \$deg02 değişken değerleri birbirine eşittir.<br/>";
    else echo "\$deg01 değişken değeri \$deg02 değişken değerinden küçüktür.";   
?>

</body>
</html>


```

Yukarıdaki dosyayı çalıştırdığımızda, web tarayıcımızda aşağıdaki ifadeler karşımıza çıkar:

```

$deg01 değişken değeri $deg02 değişken değerinden küçüktür.

```

## Kontrol yapıları için alternatif yazım şekli

PHP'de if, while, for, foreach ve switch konrol yapıları için alternatif bir yazım şekli vardır. Bu yazım şeklinde açma parentezi ({) yerine (:) işareti, kapatma parentezi yerine de sırasıyla endif;, endwhile;, endfor;, endforeach; ve endswitch; deyimleri kullanılır.

Örnek

```php
<html>
<body>

<?php
    $deg01 = 25;

    if ($deg01>17) echo "\$deg01 değişken değeri 17'den büyüktür.<br/>"; 
?>   

<?php if ($deg01 > 17): ?>
    $deg01 değişken değeri 17'den büyüktür.
<?php endif; ?>

</body>
</html>


```

```

$deg01 değişken değeri 17'den büyüktür.
$deg01 değişken değeri 17'den büyüktür.

```

Yukarıdaki PHP dosyasında, ilk iki işlem satırı ile son üç işlem satırı aynı işlemi gerçekleştirmektedir. İkinci yöntemde alternatif yazım şekli kullanılmaktadır.
