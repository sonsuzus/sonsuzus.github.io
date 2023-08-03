---
title:  PHP değişkenler
author: sonsuz
date: 2023-08-03 16:29:09 +0300
categories: [Program,PHP]
tags: [php,programlama,değişken,web,]
---


PHP'de değişkenler, herhangi bir veri türündeki değeri depolamak için kullanılan ve bir isim ile ifade edilen bir kavramdır. Bir değişkene bir değer atadıktan sonra, PHP kodları içinde aynı değeri değişken adı ile istediğimiz zaman kullanabiliriz.

PHP değişkenler $ işareti ile başlayan bir değişken adı ile tanımlanır. Değişken adı bir harf veya alt çizgi karakteri ile başlamalı ve harf, rakam ve alt çizgi karakterlerinden oluşan ifadelerle devam etmelidir.

$deg\_adi = değişken değeri; 

* Değişken adlarında kullanılan harfleri küçük veya büyük olarak tanımladığınızda, değişkeni her işlem yapmanızda harfleri aynı şekilde kullamanız gerekir ($deg\_adi ve $Deg\_adi birbirinden farklı kabul edilir).
* Değişkenlere boolean, integer, float ve text veri türleri ile dizi (array) değerleri atanabilir.
* PHP'de değişkenlere direk bir değer atadığınız anda bildirimini yapmış sayılırsınız. Değişkene hangi tür veri atarsanız, değişken aynı veri türüne çevrilir.

Örnek

```php
<html>
<body>

<?php
    $deg_int01;
    $deg_int02 = 21;

    $deg_int01 = 37;

    echo "$deg_int01 $deg_int02";
?>

</body>
</html>


```

Yukarıdaki dosyayı çalıştırdığımızda, web tarayıcımızda aşağıdaki ifadeler karşımıza çıkar:

```

21 37

```

Program, biri ilk değer verilmeden iki adet integer değişken tanımlar. İlk değişkenin değerini sonradan verir ve her iki değişken değerini ekrana yazar.

## Değişkenlere değer yoluyla değer atama

Normal olarak, bir değişkene değer yoluyla atama yapılır. Yani, bir değişkene bir ifade atamak istediğinizde, orjinal ifadenin tüm değeri olduğu gibi değer atanacak değişkene kopya edilir. Bu durumda, bir değişkenin değerinin diğer bir değişkene atadıktan sonra, değişkenlerin herhangi birinin değerini değiştirmenizin diğer değişken değeri üzerinde etkisi olmayacaktır.

İfade (expression) kavramı veri türleri ve işlemcilerin birlikte kullanılmasından elde edilir. Veri ise değişken ve/veya sabitlerden oluşur.

ifade = veri + işlemciler

veri = değişkenler + sabitler

$deg01 = 42; // ifade (değişken ve sabit) değer yoluyla atama

$deg02 = $deg01; // ifade (sadece değişkenler) değer yoluyla atama $deg01 ve $deg02 değeri 42 olur.

$deg01 = $deg01 + 5; // $deg01 değeri 47 olur ancak, $deg02 değerini etkilemez.

## Değişkenlere referans yoluyla değer atama

PHP'de değişkenlere değer atamak için referans yolunu kullandığınızda, değer atadığınız değişken değeri atadığınız asıl değişkenin adresini gösterecek şekilde oluşturulur. Bu durumda hangi değişkenin değerini değiştirirseniz değiştirin, diğerinin değerini etkileyecektir.

Referans yoluyla atamanın sadece değişkenler arasında gerçekleştirilebileceğine dikkat ediniz.

Referans yoluyla atama yapmak için değeri atanacak asıl değişkenin başına & işareti eklememiz yeterlidir.

```php
$deg01 = 42; // $deg01 değeri 42 olur.
$deg02 = &$deg01; // referans yoluyla atama $deg01 ve $deg02 değeri 42 olur.
$deg01 = $deg01 + 5; // $deg01 ve $deg02 değeri 47 olur (sadce $deg01 değişmesine rağmen).


```

Örnek

```php
<html>
<body>

<?php
    $deg01 = 42; // $deg01 değeri 42 olur.    
    $deg02 = $deg01; // $deg01 ve $deg02 değeri 42 olur.
    $deg01 = $deg01 + 5; // $deg01 değeri 47 olur ancak, $deg02 değerini etkilemez.   
    
    $deg03 = 25; // $deg03 değeri 25 olur.    
    $deg04 = &$deg03; // referans yoluyla atama $deg03 ve $deg04 değeri 25 olur.
    // $deg03 ve $deg04 değeri 33 olur (sadece $deg03 değişmesine rağmen).
    $deg03 = $deg03 + 8;

    echo "deg01 değişken değeri: $deg01 <br/>";
    echo "deg02 değişken değeri: $deg02 <br/>";
    echo "deg03 değişken değeri: $deg03 <br/>";
    echo "deg04 değişken değeri: $deg04 <br/>";
?>

</body>
</html>



```

Yukarıdaki dosyayı çalıştırdığımızda, web tarayıcımızda aşağıdaki ifadeler karşımıza çıkar:

```

deg01 değişken değeri: 47
deg02 değişken değeri: 42
deg03 değişken değeri: 33
deg04 değişken değeri: 33 

```

## İlk değer verilmeyen değişkenlerin değeri

PHP'de tanımladığınız değişkenlere bir ilk değer vermediğiniz takdirde, değişkenler veri türlerine göre otomatik olarak bir ilk değer alır:

boolean: FALSE

integer ve float: sıfır

string: boş karakter dizisi

array: boş dizi

## Değişken etki alanı

PHP'de tanımlanan bir değişkenin etki alanı içinde tanımlandığı alanı kapsar. Değişken bir PHP sayfasının başında tanımlandığında, fonksiyonların içi hariç, o sayfanın tamamında etkilidir. Değişkenin etki alanı, değişken tanımından sonra include() ve require() fonksiyonları ile PHP dosyasına içeriği dahil edilen dosyaları da kapsar.

```php
<?php 
    $deg = 21;
    include 'kod.php'; // $deg değişkeni kod.php içinde de geçerlidir.       
?>


```

Bir PHP dosyasında fonksiyon içinde tanımlanan değişkenlerin etki alanı sadece fonksiyonun içini kapsar. Fonksiyon içinde ve dışında aynı isimle tanımlanan değişkenler ise tamamen birbirinden farklıdır.

Örnek

```php
<?php 
    // Global bir değişken olup fonksiyon içleri hariç tüm dosyada geçerlidir.
    $deg01 = 17;
    // Global bir değişken olup fonksiyon içleri hariç tüm dosyada geçerlidir.
    $deg02 = 24; 
   
    function fonk1()
    {
      // Lokal değişken, fonksiyon içinde geçerli, Global $deg01 değişkeninden farklı
      $deg01 = 36;
      echo "$deg01 $deg02 <br/>"; // Ekrana sadece 36 değerini yazar.
    } 
   
    fonk1(); // Ekrana 36 değerini yazar.
    echo "$deg01 $deg02 <br/>"; // Ekrana 17 ve 24 değerlerini yazar.
?>


```

Yukarıdaki dosyayı çalıştırdığımızda, web tarayıcımızda aşağıdaki ifadeler karşımıza çıkar:

```

36
17 24

```

## global anahtar kelimesi ve $GLOBALS array

PHP'de global değişkenleri fonksiyonlar içinde kullanabilmek için değişkeni kullanılacağı fonksiyon içinde global anahtar kelimesi ile değişkeni yeniden tanımlamanız veya $GLOBALS array değeri ile birlikte değişken adını kullanmanız gerekir.

Örnek

```php
<?php 
    $deg01 = 17;
    $deg02 = 24;
   
    function fonk1()
    {
        global $deg01; // Global değişkenler hem fonksiyon hem de dosya içinde geçerli
	  
        echo "$deg01 "; // Ekrana 17 yazar (global anahtar kelimesi yöntemiyle).
        echo $GLOBALS['deg02'] . "<br/>"; // Ekrana 24 yazar ($GLOBALS array yöntemiyle).
	  
        $deg01 = $deg01 + 5; // Global değişken $deg01 değerine 5 ekler.
        
        // Global değişken $deg02 değerine 8 ekler.
        $GLOBALS['deg02'] = $GLOBALS['deg02'] + 8; 
    }
   
    fonk1(); // Ekrana 17 ve 24 yazar.
    echo "$deg01 $deg02"; // Ekrana 22 ve 32 değerlerini yazar.
?>


```

Yukarıdaki dosyayı çalıştırdığımızda, web tarayıcımızda aşağıdaki ifadeler karşımıza çıkar:

```

17 24
22 32

```

Yukarıdaki PHP dosyasında, iki adet global değişken tanımlanmış, değişkenlerin fonk1() fonksiyonu içinde kullanılabilmesi için $deg01 değişkeni global anahtar kelimesi ile fonksiyon içinde yeniden tanımlanmıştır. $deg02 değişkenine fonk1() içinden erişim için ise $GLOBALS array değeri kullanılmıştır. Bu sayede, fonksiyon içinden değişken değerlerine yapılan ekleme tüm dosya için geçerli hale gelmiştir.

## static değişkenler

Normal olarak, bir fonksiyon içinde bir değişken tanımlayıp bir değer verdiğinizde, eğer fonksiyon içindeki kodlarla değişken değeri değişir ise değişkenin aldığı son değer fonksiyonun sonraki kullanılmalarında geçerliliğini kaybeder. Örneğin, fonksiyon başında $deg01 adlı bir değişkene 5 değeri atadıysanız ve fonksiyonun diğer satırlarında bu değere 6 değerini eklediyseniz, fonksiyonun bir sonraki çağrısında $deg01 değişkeninin alacağı değer yine 5 olacaktır. Eğer fonksiyon sonunda elde edilen değerin korunmasını isterseniz static anahtar kelimesini kullanmanız gerekir.

Örnek

```php
<?php
 
    function fonk1()
    {
       $deg01 = 5;
       static $deg02 = 5;

       echo "$deg01 $deg02 <br/>"; // $deg01 daima 5, $deg02 ise farklı

       // $deg01 değeri bir sonraki fonksiyon çağrısında korunmaz.
       $deg01 = $deg01 + 2; 
       // $deg02 değeri static olduğundan bir sonraki fonksiyon çağrısında korunur.
       $deg02 = $deg02 + 2; 
    }
   
    fonk1(); // Ekrana 5 ve 5 yazar.
    fonk1(); // Ekrana 5 ve 7 yazar.
    fonk1(); // Ekrana 5 ve 9 yazar.
    fonk1(); // Ekrana 5 ve 11 yazar.
   
?>


```

Yukarıdaki dosyayı çalıştırdığımızda, web tarayıcımızda aşağıdaki ifadeler karşımıza çıkar:

```

5 5
5 7
5 9
5 11 

```

Yukarıdaki PHP dosyasında, fonksiyon içinde iki adet lokal değişken tanımlanmıştır. $deg01 değişkeni normal tanımlandığından her fonksiyon çağrısında kendisine verilen ilk değeri alır. $deg02 değişkeni ise static olarak tanımlandığından bir önceki fonksiyon çağrısı sonunda aldığı değeri alır.

static değişkenlere sabit veri türleri atanmalıdır. Eğer değişken veya değişken ile sabirlerden oluşan ifadeler atamak isterseniz hata verecektir.

static $deg01 = 7; // Doğru

static $deg02 = $deg01 // hatalı (ifade olduğu için)

static $deg03 = 7+8; // hatalı (ifade olduğu için)

## Değişken değişkenler

Bir değişkene bir karakter dizisi atayarak tanımladığınızda, o değişken adının önüne ikinci bir $ işareti ekleyerek başka bir değişken adı oluşturup herhangi bir veri türü atarsanız, ikinci değişken adı olarak ilk değişkene atadığınız karakter dizisini kullanabilirsiniz.

Örnek

```php
<?php
    $deg01 = 'degadidegeri';
    $$deg01 = 27; // $deg01 değeri "degadidegeri" ve $degadidegeri değeri 27

    echo "$deg01 ${$deg01} <br/>"; // degadidegeri ve 27
    echo "$deg01 $degadidegeri"; // degadidegeri ve 27
?>


```

Yukarıdaki dosyayı çalıştırdığımızda, web tarayıcımızda aşağıdaki ifadeler karşımıza çıkar:

```

degadidegeri 27
degadidegeri 27 

```

Yukarıdaki PHP dosyasında, fonksiyon içinde iki adet lokal değişken tanımlanmıştır. $deg01 değişkeni normal tanımlandığından her fonksiyon çağrısında kendisine verilen ilk değeri alır. $deg02 değişkeni ise static olarak tanımlandığından bir önceki fonksiyon çağrısı sonunda aldığı değeri alır.
