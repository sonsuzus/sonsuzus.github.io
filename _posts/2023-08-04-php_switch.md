---
title:  PHP switch yapısı
author: sonsuz
date: 2023-08-04 01:57:23 +0300
categories: [Program,PHP]
tags: [php,programlama,switch,karşılaştırma,web]
---


switch yapısı bir değişken veya ifadenin sonucuna bağlı olarak içinde yer alan herhangi bir seçenekteki işlem satırlarını çalıştıran bir yapıdır. switch satırında yer alan değişken veya ifade değeri birden fazla case satırında yer alan değerlerle karşılaştırılır ve eşit değerle karşılaşıldığında ilgili satırda yer alan işlem satırları çalıştırılır. Aynı işlem if elseif yapısı ile de yapılabilir. switch yapısında koşul ifadesi başlangıçta bir kez değerlendirilir ve sonuç her case satır değeri ile karşılaştırılır. if elseif yapısında ise koşul her satırda tekrar değerlendirilir. switch yapısının 2 genel yazım şekli aşağıda gösterilmektedir:

```php
switch (değişken(ifade)) {
    case değer:
         işlem satırı;	  
         break;
    case değer:
         işlem satırı;	  
         break;
         .
         .
         .
    default:
         işlem satırı;		 
}

switch (değişken(ifade)) :
    case değer:
         işlem satırı;	  
         break;
    case değer:
         işlem satırı;	  
         break;
         .
         .
         .
    default:
         işlem satırı;		 
endswitch;


```

* switch ve case satırlarında kullanılan değişken değeri veya ifade sonucu integer, float veya string veri türünden olabilir.

* switch satırında yer alan ifade değeri ile aynı değeri taşıyan ilk case satırındaki işlem satırları çalıştırılır. İlk break deyimmi ile karşılaşılana veya switch yapısının sonuna kadar tüm işlem satırları çalıştırılmaya devam eder.

* Bir case satırında herhangi bir işlem satırı ve break deyimi tanımlanmayabilir. Bu durumda bir sonraki case satırından çalışmaya devam edilir.

* Eğer case satırlarının hiçbiri gereken koşulu sağlamıyorsa, default satırında yer alan işlem satırları çalıştırılır.

* switch kalıbı içinde default deyiminin, case satırları içinde de break deyiminin tanımlanma zorunluluğu yoktur.

* Eğer, case satırlarında yer alan sabit değerlerinden hiçbiri değişken değeri ile aynı değilse ve switch kalıbı içinde default satırı tanımlanmamışsa, switch kalıbından herhangi bir işlem yapmadan çıkılır.

Örnek

```php
<html>
<body>

<?php
    $deg01 = 2;

    switch ($deg01) {
        case 1:
            echo "Değişken değeri: 1 ";
            break;
        case 2:
            echo "Değişken değeri: 2 ";
            break;
        case 3:
            echo "Değişken değeri: 3 ";
            break;
    }

    echo "<br/>";
   
    $deg02 = "Kalem";

    switch ($deg02) {
        case "Kitap":
            echo "Karakter dizisi: Kitap";
            break;
        case "Defter":
            echo "Karakter dizisi: Defter";
            break;
        case "Kalem":
            echo "Karakter dizisi: Kalem";
            break;
    }   
?>

</body>
</html>


```

Yukarıdaki dosyayı çalıştırdığımızda, web tarayıcımızda aşağıdaki ifadeler karşımıza çıkar:

```

Değişken değeri: 2
Karakter dizisi: Kalem

```

Yukarıdaki PHP dosyasında, ilk switch yapısında integer, ikinci switch yapısında ise string bir değişken değer karşılaştırması yapılarak, aynı değere sahip case satırlarında yer alan karakter dizileri ekran yazılır ve break deyimi ile birlikte switch yapısından çıkılır.

Örnek

```php
<html>
<body>

<?php
    $deg01 = 1;

    switch ($deg01) {
        case 1:
            echo "Değişken değeri: 1<br/>";
        case 2:
            echo "Değişken değeri: 2<br/>";
        case 3:
            echo "Değişken değeri: 3<br/>";
    }

    echo "<br/>";
   
    switch ($deg01) {
        case 1:
        case 2:
        case 3:
            echo "Değişken değeri 1-3 arasındadır!";
            break;
        case 4:
            echo "Değişken değeri: 4";
            break;
    }   
?>

</body>
</html>


```

Yukarıdaki dosyayı çalıştırdığımızda, web tarayıcımızda aşağıdaki ifadeler karşımıza çıkar:

```

Değişken değeri: 1
Değişken değeri: 2
Değişken değeri: 3

Değişken değeri 1-3 arasındadır!

```

Yukarıdaki PHP dosyasında, ilk switch yapısında break deyimi kullanılmadığından ilk case satırında doğru sonuç edilerek işlem satırlarının çalıştırılmasına başlanmış ve switch yapısında yer alan tüm işlem satırları çalıştırılmıştır. Sadece ilk case satırının doğru sonuç vermesi diğer case satırlarının çalışmasını sağlamıştır. İkinci switch yapısında ise ilk 3 case satırı için tek bir işlem satırı kullanılmıştır.

Örnek

```php
<html>
<body>

<?php
    $deg01 = 7;

    switch ($deg01) {
        case 1:
            echo "Değişken değeri: 1<br/>";
            break;
        case 2:
            echo "Değişken değeri: 2<br/>";
            break;
        case 3:
            echo "Değişken değeri: 3<br/>";
            break;
        default:
            echo "Değişken değeri: 1, 2 veya 3'ten farklıdır!";
    }   
?>

</body>
</html>


```

Yukarıdaki dosyayı çalıştırdığımızda, web tarayıcımızda aşağıdaki ifadeler karşımıza çıkar:

```

Değişken değeri: 1, 2 veya 3'ten farklıdır!

```

Yukarıdaki PHP dosyasında, ilk 3 case satırında doğru sonuç edilmediğinden default satırı için tanımlanan işlem satırı çalıştırılmıştır.
