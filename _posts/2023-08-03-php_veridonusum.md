---
title:  PHP veri dönüşümleri
author: sonsuz
date: 2023-08-03 16:27:10 +0300
categories: [Program,PHP]
tags: [php,programlama,web,sunucu]
---


## Veri tipi belirleme

PHP değişken bildiriminde bir veri türü tanımlamanız gerekmez. Değişkene hangi veri türünü atarsanız, değişken o veri türüne ait bir değişken haline gelir.

```php
<html>
<body>

<?php
    $deg01 = TRUE;          // $deg01 boolean bir değişken  
    $deg02 = 21;            // $deg02 integer bir değişken
    $deg03 = 14.64;         // $deg03 float bir değişken
    $deg04 = "Veri tipi";   // $deg04 string bir değişken
?>

</body>
</html>


```

Örnek

```php
<html>
<body>

<?php
    $deg01 = TRUE;
    $deg02 = 21;
    $deg03 = 14.64;
    $deg04 = "Veri tipi";

    var_dump ($deg01, $deg02, $deg03, $deg04);
?>

</body>
</html>
```

Yukarıdaki dosyayı çalıştırdığımızda, web taracıyımızda aşağıdaki ifadeler karşınıza çıkar:

```

boolean true

int 21

float 14.64

string 'Veri tipi' (length=9)

```

Yukarıdaki PHP dosyasında, dört temel veri türü birer değişkene atanarak değişken veri türleri belirlenmektedir. Daha sonra, var\_dump() fonksiyonu kullanılarak değişken türleri ve değerleri ekrana yazılmaktadır.

## Geçici veri tipi belirleme

Geçici veri tipi belirleme (type casting) C programlama dilindeki gibi gerçekleştirilir. Veri tipi geçici olarak değiştirilerek başka bir değişkene aktarılacak değişkenin önüne istenen veri türü parantez içinde yazılır:

```php
$yeni_deg = (veri türü) $mevcut_deg;

$deg01 = 21;                  // $deg01 integer 
$deg02 = (string) $deg01;     // $deg02 string
```

## Tanımlanabilecek geçici veri tipleri

```

(int), (integer)           : integer türüne dönüşüm
(bool), (boolean)          : boolean türüne dönüşüm
(float), (double), (real)  : float türüne dönüşüm
(string)                   : string türüne dönüşüm
(array)                    : array türüne dönüşüm
(object)                   : object türüne dönüşüm
(unset)                    : NULL'a dönüşüm (PHP 5)

```

Örnek

```php
<html>
<body>

<?php
    $deg01 = 21;                         
    $deg02 = (string) $deg01; 
    $deg03 = (bool) $deg01; 
    $deg04 = (float) $deg01; 

    var_dump ($deg01, $deg02, $deg03, $deg04);   
?>

</body>
</html>


```

Yukarıdaki dosyayı çalıştırdığımızda, web taracıyımızda aşağıdaki ifadeler karşınıza çıkar:

```

int 21

string '21' (length=2)

boolean true

float 21

```

Yukarıdaki PHP dosyasında, önce integer bir değişken tanımlanır. Integer değişkeninin veri tipi sırasıyla string, boolean ve float veri tiplerine geçici olarak dönüştürülüp farklı değişkenlere atanır. Daha sonra, var\_dump() fonksiyonu kullanılarak değişken türleri ve değerleri ekrana yazılmaktadır.
