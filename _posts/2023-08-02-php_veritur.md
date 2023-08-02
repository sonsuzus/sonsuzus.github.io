---
title:  PHP veri türleri
author: sonsuz
date: 2023-08-02 18:55:20 +0300
categories: [Program,PHP]
tags: [php,veri türü,programlama,string,integer,web]
---


PHP'de 4 farklı temel veri türü vardır:

* boolean : Doğruluk değeri ifade eden ve TRUE (Doğru) ya da FALSE (Yanlış) değeri alan bir veri türüdür.
* integer : Bir tamsayı değer içeren bir veri türüdür.
* float : Gerçek sayılar olarak da bilinen büyük ve ondalıklı sayıları tanımlamaya yarayan veri türüdür.
* string : Karakter dizileri tanımlamaya yarayan bir veri türüdür.

PHP'de 2 bileşik veri türü vardır:

* Dizi (Array) : Farklı veri türlerini tek bir değişken adı ile tanımlayan bir veri kümesidir.
* Nesne (Object) : Farklı veri türlerine ve fonksiyonlardan oluşan bir veri topluluğuna tek bir isim ile erişim sağlayan bir veri türüdür.

PHP'de 2 özel veri türü vardır:

* resource : Özel fonksiyonlar tarafından oluşturulan ve kullanılan harici kaynaklara erişim için kullanılan özel bir değişkendir. Genellikle, bir MySQL dosyasına veya normal dosyaya sıra ile işlem yapmak için kullanılır.
* NULL : Özel NULL değeri, değeri olmayan bir değişkeni ifade etmektedir. NULL veri tipinin tek olası değeri NULL'dur.

Ayrıca, PHP'de kullanılan sözde veri türleri ve değişkenler vardır:

* mixed : Bu ifade bir fonksiyonun birden fazla veri türünde parametre alabileceğini gösterir. Ancak bu fonkisyonun tüm veri türlerini parametre olarak albileceğini göstermez.
* number : Bu ifade bir fonksiyonun integer veya float veri türünde parametre alabileceğini gösterir.
* callback : Global fonksiyonları, nesne fonksiyonlarını veya bir sınıf yapısının statik fonksiyonlarına erişim sağlayan ve bir fonksiyona, yine aynı fonksiyon tarafından daha sonra belirli koşullar sağlandığında çalıştırılmak üzere, aktarılan kod kümesidir.
* void : Bir fonksiyon tarafından geri verilen değer olarak tanımlandığında herhangi bir şekilde kullanımı mümkün değildir. Bir fonksiyonun parametre listesi yerinde tanımlandığında, fonksiyona herhangi bir parametre geçirilemeyeceğini gösterir.

```php
<html>
<body>

<?php 
    $var_bool = TRUE;               // boolean değer
    $var_int = 21;                  // integer değer
    $var_float = 217.234;           // float değer
    $var_str1 = "PHP veri türleri"; // string (karakter dizisi)
    $var_str2 = 'PHP değişkenler';  // string (karakter dizisi - " " yerine ' ')

    echo "boolean değer: $var_bool</br>";
    echo "integer değer: $var_int</br>";
    echo "float değer: $var_float</br>";
    echo "karakter dizisi: $var_str1</br>";
    echo "karakter dizisi: $var_str2</br>";
?>

</body>
</html>


```

Yukarıdaki dosyayı çalıştırdığınızda, web taracıyınızda aşağıdaki ifadeler karşınıza çıkar:

```php
boolean değer: 1
integer değer: 21
float değer: 217.234
karakter dizisi: PHP veri türleri
karakter dizisi: PHP değişkenler

```

Yukarıdaki PHP dosyasında, birer adet boolean, integer ve float değer sırasıyla $var\_bool, $var\_int ve $var\_float adlı değişkenlere, iki adet string değer ise sırasıyla $var\_str1 ve $var\_str2 adlı değişkenlere atanır. Daha sonra, değişken değerleri sırasıyla ekrana yazılır.

PHP değişkenler $ işareti ile başlayan bir değişken adı ile tanımlanır. Değişkenler veri türü değerlerini yerleştirmek için kullanılır.  
  
PHP'de karakter dizilerini hem " " hem de ' ' ifadeleri arasında tanımlayabilirsiniz.  
  
PHP boolean veri tipinde TRUE değeri 1, FALSE değeri 0 olarak ekrana yazılır.
