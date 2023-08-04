---
title:  PHP fonksiyonlar
author: sonsuz
date: 2023-08-04 13:28:17 +0300
categories: [Program,PHP]
tags: [php,programlama,fonksiyon]
---


PHP'de fonksiyon bir veya daha fazla işlem satırından oluşan PHP kodlarının bir kod bloğu şeklinde bir isim altında toplanmasıdır. Sadece fonksiyona verilen isim çağrılarak, fonksiyon içinde yer alan işlem satırlarının çalıştırılması sağlanır. Başka bir ifade ile bir veya daha fazla komutun içinde yer aldığı ve PHP programının herhangi bir yerinden sadece fonksiyon adı çağrılarak, fonksiyon içindeki komutların tamamının çalıştırılmasını sağlayan yapılara fonksiyon adı verilir. Aşağıdaki şekilde tanımlaması yapılır:

```php
function fonksiyon_adı()
{
   komut satırı;
   .
   .
   komut satırı;
}


```

PHP'de fonksiyonları, yerleşik ve kullanıcı tanımlı olmak üzere ikiye ayırabiliriz:

Yerleşik fonksiyonlar: PHP'de önceden tanımlanmış olarak kullanıma hazır fonksiyonlardır. Ayrıca, belirli PHP eklentilerinin derlenmesini gerektiren yerleşik fonksiyonlarda vardır.

Kullanıcı tanımlı fonksiyonlar: Kullanıcılar tarafından oluşturularak kullanılan fonksiyonlardır.

PHP'de kullanılan çok sayıda yerleşik fonksiyon bulunmaktadır.

## Kullanıcı tanımlı fonksiyonlar

Fonksiyon isimleri bir harf ya da alt çizgi ile başlar, herhangi bir sayıda geçerli harf, sayı ya da alt çizgi ile devam eder.

Örnek

```php
<html>
<body>

<?php
    function sayi_yazdir()
    {
        for ($deg01=1; $deg01<=10; $deg01++) echo "$deg01 ";
    }
   
    sayi_yazdir();   
?>

</body>
</html>


```

Yukarıdaki dosyayı çalıştırdığımızda, web tarayıcımızda aşağıdaki ifadeler karşımıza çıkar:

```

1 2 3 4 5 6 7 8 9 10

```

Yukarıdaki PHP dosyasında, fonksiyon çağrısı ile fonksiyon içindeki komutlar çalıştırılır. Fonksiyon içinde yer alan for döngüsü kullanılarak 1'den 10'a kadar olan sayılar ekrana yazılır.

## Fonksiyonlar argümanları

Fonksiyonlara değer geçirilmesini sağlamak için fonksiyon adından sonra yer alan parentezler içinde arasında virgül kullanarak istediğiniz sayıda değişken tanımlayabilirsiniz. Bu değişkenler fonksiyon içinde lokal olarak tanımlanmış değişkenler olarak kabul edilir. Fonksiyon çağrısı yaparken fonksiyon adından sonra yer alan parentez içine değerler yerleştirilerek bu değişkenlere değer geçirilir.

PHP'de fonksiyon argümanları değer olarak (öntanımlı), referans olarak ve öntanımlı argüman değeri olarak geçirilebilir:

Değer olarak geçirme: Fonksiyona geçirilen değişkenin sadece bir kopyası geçirilir. Bu nedenle, fonksiyon içinde değişken değeri üzerinde yapılan değişiklikler asıl değişken değerini etkilemez.

Referans olarak geçirme: Fonksiyona geçirilen değişken önüne & işareti konularak referans yoluyla geçirilir. Böylelikle, fonksiyon içinde değişken değeri üzerinde yapılan değişiklikler asıl değişken değerini etkiler.

Argüman değeri olarak geçirme: Argüman tanımlanmış bir fonksiyona herhangi bir değer geçirilmeden çağrı yapıldığında kullanılmak üzere, mevcut argümanlar için öntanımlı değerler atanabilir.

Örnek

```php
<html>
<body>

<?php
    function sayi_yazdir($deg_fonk=10)
    {
        $deg_fonk *= 2;
        for ($deg01=1; $deg01<=$deg_fonk; $deg01++) echo "$deg01 ";
    }
   
    function metin_yazdir(&$deg_fonk)
    {
        $deg_fonk .= " işlemleri";
        echo $deg_fonk;
    }

    $deg01 = 5;   
    sayi_yazdir($deg01); 
   
    echo "<br/> $deg01 <br/>"; // $deg01 değişken değeri değişmemiştir.
   
    $deg02 = "Fonksiyon";
    metin_yazdir($deg02); 
   
    echo "<br/> $deg02 <br/>"; // $deg02 değişken değeri değişmiştir.

    sayi_yazdir();   
?>

</body>
</html>


```

Yukarıdaki dosyayı çalıştırdığımızda, web tarayıcımızda aşağıdaki ifadeler karşımıza çıkar:

```

1 2 3 4 5 6 7 8 9 10
5
Fonksiyon işlemleri
Fonksiyon işlemleri
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20

```

Yukarıdaki PHP dosyasında, sayi\_yazdir() fonksiyonu $deg01 değişkeni değer geçirilerek çağrıldığında, $deg01 değişkenine fonksiyon içinde yapılan değişiklik değişken kopyası üzerinde yapıldığından, değişkenin değerini değiştirmez. metin\_yazdir() fonksiyonu $deg02 değişkeni referans geçirilerek çağrıldığında, $deg02 değişkenine fonksiyon içinde yapılan değişiklik değişken üzerinde yapıldığından, değişkenin değerini değiştirir. sayi\_yazdir() fonksiyonu ikinci çağrılışında herhangi bir değer geçirilmediğinden, sayi\_yazdir() fonksiyonundaki öntanımlı değişken değeri kullanılır.

## Fonksiyonlarda değer döndürme

Fonksiyonlar içinde isteğe bağlı olarak kullanılan return deyimi ile, dizi ve nesnelerde dahil olmak üzere, herhangi bir veri türü döndürülebilir. return deyiminin kullanıldığı satırda fonksiyonun çalışması sona erer ve fonksiyonun çağrıldığı satırdan itibaren PHP kodları çalışmaya devam eder.

Örnek

```php
<html>
<body>

<?php
    function sayi_yazdir($deg_fonk)
    {
        for ($deg01=0, $deg02=0; $deg01<=$deg_fonk; $deg01+=2) $deg02 += $deg01;
	  
        return $deg02;
    }
   
    echo sayi_yazdir(20);   
?>

</body>
</html>


```

Yukarıdaki dosyayı çalıştırdığımızda, web tarayıcımızda aşağıdaki ifadeler karşımıza çıkar:

```

110

```

Yukarıdaki PHP dosyasında, sayi\_yazdir() fonksiyonu 20'ye kadar olan çift sayıların toplamını alarak geri döndürür. Elde edilen değer ekrana yazılır.

## Değişken fonksiyonlar

Bir fonksiyon adı bir değişkene atandığında, değişken adının sonuna parentez ekleyerek, değişkene adı atanan fonksiyonu çağırabilirsiniz.

Örnek

```php
<html>
<body>

<?php
    function sayi_yazdir($deg_fonk)
    {
        for ($deg01=0, $deg02=0; $deg01<=$deg_fonk; $deg01+=2) $deg02 += $deg01;
	  
        return $deg02;
    }
   
    $fonk_deg = 'sayi_yazdir';
   
    echo $fonk_deg(10); // sayi_yazdir(10); ile aynı işlemi yapar.
?>

</body>
</html>


```

Yukarıdaki dosyayı çalıştırdığımızda, web tarayıcımızda aşağıdaki ifadeler karşımıza çıkar:

```

30

```

Yukarıdaki PHP dosyasında, sayi\_yazdir() fonksiyonu $fonk\_deg fonksiyon değişkeni yoluyla çağrılarak 10'a kadar olan çift sayıların toplamı alınarak geri döndürülür ve elde edilen değer ekrana yazılır.

## Anonim fonksiyonlar

Anonim fonksiyonlar, bir fonksiyon ismi kullanılmadan oluşturulan fonksiyonlardır. Genellikle, bir fonksiyonun parametresi olarak tanımlanır ve o fonksiyona bir argüman değeri sağlarlar.

Örnek

```php
<html>
<body>

<?php
    $fonk_deg = function ($deg01)
    {
        echo "$deg01<br/>";
    };
 
    $fonk_deg('Değişken fonksiyonlar');
    $fonk_deg('Anonim fonksiyonlar');   
?>

</body>
</html>


```

Yukarıdaki dosyayı çalıştırdığımızda, web tarayıcımızda aşağıdaki ifadeler karşımıza çıkar:

```

Değişken fonksiyonlar
Anonim fonksiyonlar 

```

Yukarıdaki PHP dosyasında, isimsiz olarak tanımlanan fonksiyon atandığı $fonk\_deg değişkeni yoluyla çağrılarak kendisine aktarılan değerleri ekrana yazar.

Örnek

```php
<html>
<body>

<?php
    $fonk_deg = function ($deg_benzer)
    {
        return  "fonksiyonlar";
    };
 
    echo preg_replace_callback ('/değişkenler/', $fonk_deg, "Anonim değişkenler");   
?>

</body>
</html>


```

Yukarıdaki dosyayı çalıştırdığımızda, web tarayıcımızda aşağıdaki ifadeler karşımıza çıkar:

```

Anonim fonksiyonlar 

```

Yukarıdaki PHP dosyasında, isimsiz olarak tanımlanan fonksiyon atandığı $fonk\_deg değişkeni yoluyla preg\_replace\_callback() fonksiyonu içinde callback fonksiyonu olarak kullanılır. Aynı fonksiyonun ilk parametresinin ("değişkenler") üçüncü parametre içinde eşleştiği kısım yerine "fonksiyonlar" ifadesini geri döndürür.
