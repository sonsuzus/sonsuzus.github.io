---
title:  PHP integer
author: sonsuz
date: 2023-08-03 16:10:04 +0300
categories: [Program,PHP]
tags: [php,programlama,integer,tam sayı,web,sunucu]
---

Integer bir değer matematik derslerinde gösterilen tamsayılar kümesinin elemanı olan bir sayıdır:

Z = {..., -2, -1, 0, 1, 2, ...}

Integer değerler onluk (decimal), onaltılık (hexadecimal) veya sekizlik (octal) tabanda tanımlanabilirler, ve önlerinde isteğe bağlı bir + veya - işareti bulunabilir.

Sekizlik sayı sisteminde tanımlanan sayıların önüne 0(sıfır), onaltılık sayı sisteminde tanımlanan sayıların önüne ise 0x ifadesi getirilir.

Sayı sistemlerinde kullanılan değerler:

10'luk sayı sistemi: 0 1 2 3 4 5 6 7 8 9 (Toplam 10 değer)

16'lık sayı sistemi: 0 1 2 3 4 5 6 7 8 9 A B C D E F (Toplam 16 değer)

8'lik sayı sistemi: 0 1 2 3 4 5 6 7 (Toplam 8 değer)

```php
<?php 
    $deg = 127;   // 10'luk sayı değeri
    $deg = -85;   // Negatif 10'luk sayı değeri
    $deg = 0125;  // 8'lik sayı değeri (10'luk sayı sisteminde 85)	
    $deg = 0xF8   // 16'lık sayı değeri (10'luk sayı sisteminde 248)	
?>


```

Bir integer veri türünün azami boyutu işletim sistemine göre değişir:

* 32 bitlik işletim sistemlerde: 2.147.483.647
* 64 bitlik sistemlerde: 9E18 civarındadır.

PHP işaretsiz tamsayıları desteklemez, başka bir ifade ile sayının bir biti işaret biti olarak ayrılır. integer türünün boyutu PHP\_INT\_SIZE ve alabileceği en büyük değer ise PHP\_INT\_MAX sabiti ile bulunabilir.

Eğer PHP integer olarak tanımlanmış bir sayının integer veri türü azami boyutundan büyük olduğunu belirlerse, sayıya float bir sayı gibi işlem yapar. Bir işlem sonunda elde edilen sayı azami boyutu aştığında da geri verilen değer yine float bir değer olur.

```php
<html>
<body>

<?php
    // 32 bit işletim sistemi için PHP_INT_SIZE ve PHP_INT_MAX değerleri  
    echo "integer boyutu: " . PHP_INT_SIZE . "</br>";
    echo "Azami integer değeri: " . PHP_INT_MAX . "</br>";
	
    $deg01 = 348;
    $deg02 = PHP_INT_MAX + 775;
	
    var_dump($deg01);
    var_dump($deg02);
?>

</body>
</html>


```

Yukarıdaki dosyayı çalıştırdığınızda, web taracıyınızda aşağıdaki ifadeler karşınıza çıkar:

```
integer boyutu: 4
Azami integer değeri: 2147483647

int 348

float 2147484422

```

Yukarıdaki PHP dosyasında, birer adet boolean, integer ve float değer sırasıyla $var\_bool, $var\_int ve $var\_float adlı değişkenlere, iki adet string değer ise sırasıyla $var\_str1 ve $var\_str2 adlı değişkenlere atanır. Daha sonra, değişken değerleri sırasıyla ekrana yazılır.
