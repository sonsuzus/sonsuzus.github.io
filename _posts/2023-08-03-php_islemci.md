---
title:  PHP işlemciler
author: sonsuz
date: 2023-08-03 16:41:33 +0300
categories: [Program,PHP]
tags: [php,programlama,web,işlem,ifade,atama,işlemci]
---


İşlemci aldığı bir veya daha fazla değere işlem yaparak farklı bir değer elde eden bir kavramdır. İşlemci aldığı değer veya değerlerle ifade kavramını oluşturur.

İşlemciler aldıkları değer sayısına göre gruplandırılabilir:

Tekli işlemciler 
: Tek bir değer alırlar (Örnek ++ artırım işlemcisi). 

İkili işlemciler 
: İki değer alırlar (Örnek + ve - matematik işlemcileri gibi).

Üçlü işlemci 
: Üç değer alır (Bu kategoride sadece ? : işlemcisi vardır).

## Aritmetik işlemciler

| İşlemci | Adı | Açıklama |
| --- | --- | --- |
| + | Toplama | İki değerin toplamını verir. |
| - | Çıkarma | İki değerin farkını verir. |
| \* | Çarpma | İki değerin çarpımını verir. |
| / | Bölme | Bir değerin diğerine bölümünü verir. |
| % | Kalan | Bir değerin diğerine bölümünde kalanı verir. |

Bölme işleminde kullanılan her iki değerde tamsayı ise ve birbirlerine tam olarak bölünürlerse sonuç bir tamsayı, aksi takdirde float bir değer olacaktır.

Kalan işlemcisinin değerleri tamsayıdan farklı ise tamsayıya dönüştürülür. Elde edilen sonuç bölünenin işaretini alır.

Örnek

```php
<html>
<body>

<?php
    $deg01 = 11 + 5;
    $deg02 = 14 - 6;
    $deg03 = 5 * 7;
    $deg04 = 28 / 4;   
    $deg05 = 83 % 10;
   
    echo "$deg01 $deg02 $deg03 $deg04 $deg05";   
?>

</body>
</html>


```

Yukarıdaki dosyayı çalıştırdığımızda, web tarayıcımızda aşağıdaki ifadeler karşımıza çıkar:

```

16 8 35 7 3

```

## Atama işlemcileri

PHP'de temel atama işlemcisi = olup sağ tarafında yer alan ifadeyi sol tarafındaki değişkene atar.

Dizilerde ise değer adına bir değer atamak için => işlemcisi kullanılır.

Diğer işlemcilerden bazıları temel atama işlemcisi ile birlikte kullanılarak birleşik atama işlemcileri oluşturulur.

| İşlemci | Adı | Açıklama |
| --- | --- | --- |
| = | Atama | Sağ tarafında yer alan ifadeyi sol tarafındaki değişkene atar. |
| => | Atama | Bir dizi içindeki değer adına bir değer atar. |
| += | Toplama ve Atama | Sağ tarafında yer alan değeri sol tarafındaki değişkene ekler ve sonucu sol tarafındaki değişkene atar. |
| -= | Çıkarma ve Atama | Sağ tarafında yer alan değeri sol tarafındaki değişkenden çıkarır ve sonucu sol tarafındaki değişkene atar. |
| \*= | Çarpma ve Atama | Sol tarafındaki değişken değerini sağ tarafındaki değeri çarpar ve sonucu sol tarafındaki değişkene atar. |
| /= | Bölme ve Atama | Sol tarafındaki değişken değerini sağ tarafındaki değere böler ve sonucu sol tarafındaki değişkene atar. |
| .= | Birleştirme ve Atama | Sol tarafındaki dizi ile sağ tarafındaki diziyi birleştirir ve sonucu sol tarafındaki değişkene atar. |
| %= | Kalan ve Atama | Sol tarafındaki değişken değerini sağ tarafındaki değere böler ve kalan değeri sol tarafındaki değişkene atar. |
| &= | Ve ve Atama | İki değer arasında & işlemi uygular ve sonucu sol tarafındaki değişkene atar. |
| \|= | Veya ve Atama | İki değer arasında | işlemi uygular ve sonucu sol tarafındaki değişkene atar. |
| ^= | Ayrıcalıklı Veya ve Atama | İki değer arasında ^ işlemi uygular ve sonucu sol tarafındaki değişkene atar. |
| <<= | Sola kaydırma ve Atama | İki değer arasında << işlemi uygular ve sonucu sol tarafındaki değişkene atar. |
| >>= | Sağa kaydırma ve Atama | İki değer arasında >> işlemi uygular ve sonucu sol tarafındaki değişkene atar. |

Örnek

```php
<html>
<body>

<?php
    $deg01 = 26;

    $deg01 += 7; // Bu satır $deg01 = $deg01 + 7 ile aynı işlemi yapar. 
    echo $deg01 . " "; // Ekrana 33 yazar. 
   
    $deg01 -= 11; // Bu satır $deg01 = $deg01 - 11 ile aynı işlemi yapar. 
    echo $deg01 . " "; // Ekrana 22 yazar.   
   
    $deg01 *= 4; // Bu satır $deg01 = $deg01 * 8 ile aynı işlemi yapar. 
    echo $deg01 . " "; // Ekrana 88 yazar.   

    $deg01 /= 2; // Bu satır $deg01 = $deg01 / 2 ile aynı işlemi yapar. 
    echo $deg01 . " "; // Ekrana 44 yazar.

    $deg01 %= 7; // Bu satır $deg01 = $deg01 % 7 ile aynı işlemi yapar. 
    echo $deg01 . " "; // Ekrana 2 yazar.

    $deg02 = "Atama ";
   
    // Bu satır $deg02 = $deg02 . "İşlemcileri" ile aynı işlemi yapar. 
    $deg02 .= "İşlemcileri"; 
	
    echo $deg02; // Ekrana "Atama İşlemcileri" yazar.   
?>

</body>
</html>


```

Yukarıdaki dosyayı çalıştırdığımızda, web tarayıcımızda aşağıdaki ifadeler karşımıza çıkar:

```

33 22 88 44 2 Atama İşlemcileri

```

## Bit işlemcileri

Bit işlemcileri bir tamsayı içinde yer alan bit değerlerini işlem yaparak kulanmamızı sağlar. Bu konuyu daha iyi anlayabilmek için temel bilgilerinizi gözden geçirmek veya bilgi sahibi olmak amacıyla [sayı sistemleri](bilgi_sayi) bölümünü okuyabilirsiniz.

| İşlemci | Adı | Açıklama |
| --- | --- | --- |
| & | Ve | İşleme giren değerlerin her ikisinde de bit değeri 1 ise sonuç 1 olur. |
| \| | Veya | İşleme giren değerlerin herhangi birinin bit değeri 1 ise karşılık 1 olur. |
| ^ | Ayrıcalıklı Veya | İşleme giren değerlerin bitleri farklı ise sonuç 0, aksi takdirde 1 olur. |
| ~ | Değil | İşleme giren değerin 1 olan bitleri 0, 0 olan bitleri ise 1 olur. |
| << | Sola kaydırma | Solda yer alan değerin bitleri sağda yer alan değer kadar sola kayar. |
| >> | Sağa kaydırma | Solda yer alan değerin bitleri sağda yer alan değer kadar sağa kayar. |

Bit seviyesinde yapılan işlemlerde, işlem değerlerin bitleri arasında yapılır.

> PHP'de tamsayılar daima işaret biti içerecek şekilde tanımlıdır.

PHP'de kullanılan tamsayı ile ön tanımlı sabitlerden ikisi aşağıdadır:

PHP\_INT\_SIZE: 4 (32 bit bilgisayarlar için)

PHP\_INT\_MAX: 2147483647 (32 bit bilgisayarlar için)

2147483647 : 01111111111111111111111111111111 (Toplam 32 bit, en soldaki bit işaret bitidir.)

* İşaret biti 0 ise sayı pozitif, 1 ise negatif olur.

* Bir sayıyı 2'ye bölmek sayının bitlerini bir basamak sağa kaydırmak, 2 ile çarpmak ise bir basamak sola kaydırmak ile aynı sonucu verir.

* PHP'de bir sayının değilini (tamlayanını) almak, aynı sayının negatifini alıp bir çıkarmak ile aynı sonucu verir. 

* Sağa ve sola kaydırma işlemlerinde her iki uçtan da taşan bitler dever dışı kalır. Sola kaydırmada, sağ tarafta boşalan bit yerleri 0 ile doldurulur ve en solda yer alan işaret biti de kaydırılır ve korunmaz. Sağa kaydırmada ise işaret biti korunur.

Örnek

```php
<html>
<body>

<?php
    $deg01 = 83;
  
    echo $deg01 . " sayısının ikili sayı sistemindeki karşılığı: ";
  
    echo ($deg01 & 128) ? '1 ' : '0 ';
    echo ($deg01 & 64) ? '1 ' : '0 ';
    echo ($deg01 & 32) ? '1 ' : '0 ';
    echo ($deg01 & 16) ? '1 ' : '0 ';
    echo ($deg01 & 8) ? '1 ' : '0 ';
    echo ($deg01 & 4) ? '1 ' : '0 ';
    echo ($deg01 & 2) ? '1 ' : '0 ';
    echo ($deg01 & 1) ? '1' : '0';
?>

</body>
</html>


```

Yukarıdaki dosyayı çalıştırdığımızda, web tarayıcımızda aşağıdaki ifadeler karşımıza çıkar:

```

83 sayısının ikili sayı sistemindeki karşılığı: 0 1 0 1 0 0 1 1 

```

Yukarıdaki PHP dosyasında, $deg01 değişkenine sıra ile 128, 64, 32, 16, 8, 4, 2 ve 1 sayılarıyla & işlemi uygulanır. İşleme sokulan 8 sayının sadece 1 bit'i 1 değeri, diğer basamaklar ise 0 değeri taşır. Böylece en yüksek yani en soldaki bit'den başlayarak 83 sayısının her defasında bir bit'i kendisine karşılık gelen 1 değeri ile karşılaştırılmış olur. Eğer $deg01 değişkeninin 1 değeri taşıyan hanesine karşılık gelen hanesi 1 değeri taşıyorsa 1, aksi takdirde 0 değeri ekrana yazılır.

Örnek

```php
<html>
<body>

<?php
    function ikili_yazdir($deger) {
        echo ": ";
        for ($deg01=PHP_INT_MAX+1; $deg01>=1; $deg01/=2) {
	        echo ($deger & $deg01) ? '1 ' : '0 ';	  
        }
        echo "<br/>";	  
    }  
  
    $deg01 = 145;
    $deg02 = 172;
  
    echo $deg01;
    ikili_yazdir($deg01);
    echo $deg02;
    ikili_yazdir($deg02);    
    echo ($deg01 & $deg02);
    ikili_yazdir($deg01 & $deg02);
    echo ($deg01 | $deg02);
    ikili_yazdir($deg01 | $deg02);
    echo ($deg01 ^ $deg02);
    ikili_yazdir($deg01 ^ $deg02);
    echo (~$deg01);
    ikili_yazdir(~$deg01);
    echo $deg01 + (~$deg01) . "<br/>";
    echo ($deg01 << 2);
    ikili_yazdir($deg01 << 2);
    echo ($deg01 >> 2);
    ikili_yazdir($deg01 >> 2);
?>

</body>
</html>


```

Yukarıdaki dosyayı çalıştırdığımızda, web tarayıcımızda aşağıdaki ifadeler karşımıza çıkar:

```

145: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 1 0 0 0 1
172: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 1 0 1 1 0 0
128: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0
189: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 1 1 1 1 0 1
61: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 0 1
-146: 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 1 1 0 1 1 1 0
-1
580: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 1 0 0 0 1 0 0
36: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 1 0 0 

```

Yukarıdaki PHP dosyasında, $deg01 ve $deg02 değişkenlerine sıra ile 145 ve 172 değerleri atanır. Önce değişken değerleri, daha sonra değişkenler üzerinde uygulanan bit işlemleri sonuçları onluk sayı sistemine ve ikili\_yazdir() fonksiyonu ile ikili sayı sistemine göre ekrana yazılır.

ikili\_yazdir() fonksiyonu içinde PHP\_INT\_MAX ön tanımlı sabiti kullanılmaktadır:

2147483647 : 01111111111111111111111111111111 (Toplam 32 bit, en soldaki bit işaret bitidir.)

\* İşaret biti 0 ise sayı pozitif, 1 ise negatif olur.

Bu sayıya 1 eklediğimizde ise aşağıdaki değeri elde ederiz:

2147483648 : 10000000000000000000000000000000

ikili\_yazdir() fonksiyonuna geçirilen onluk sistem değeri önce bu değerle daha sonra sırasıyla bu sayının 2'ye bölümü ile elde edilen değerlerle & işlemine tabi tutulur:

2147483648 : 10000000000000000000000000000000

1073741824 : 01000000000000000000000000000000

536870912 : 00100000000000000000000000000000

.............................................

1 : 00000000000000000000000000000001

Örnek

```php
<html>
<body>

<?php
    $deg01 = 145;
    $deg02 = 172;
  
    $format = '%1$d: ' . '%1$0' . (PHP_INT_SIZE * 8) . 'b' . '<br/>';
  
    printf ($format, $deg01);
    printf ($format, $deg02);  
    printf ($format, ($deg01 & $deg02));
    printf ($format, ($deg01 | $deg02));
    printf ($format, ($deg01 ^ $deg02));
    printf ($format, ~$deg01);
    printf ($format, ($deg01 << 2));
    printf ($format, ($deg01 >> 2));
?>

</body>
</html>


```

Yukarıdaki dosyayı çalıştırdığınızda, web tarayıcınızda aşağıdaki ifadeler karşınıza çıkar:

```

145: 00000000000000000000000010010001
172: 00000000000000000000000010101100
128: 00000000000000000000000010000000
189: 00000000000000000000000010111101
61: 00000000000000000000000000111101
-146: 11111111111111111111111101101110
580: 00000000000000000000001001000100
36: 00000000000000000000000000100100

```

Yukarıdaki PHP dosyası, bir önceki dosya ile aynı işlemi yapmaktadır. Tek fark, echo fonksiyonu yerine printf() fonksiyonu ve PHP\_INT\_SIZE ön tanımlı değişkeninin kullanılmasıdır.

## Karşılaştırma işlemcileri

Karşılaştırma işlemcilerini kullanarak iki değeri karşılaştırabilir ve sonuç olarak değeri TRUE veya FALSE olan boolean bir değer elde edebilirsiniz.

| İşlemci | Adı | Açıklama |
| --- | --- | --- |
| == | Eşittir | İki değer birbirine eşitse sonuç TRUE olur. |
| === | Aynıdır | İki değer birbirine eşit ve veri türleri aynı ise sonuç TRUE olur. |
| != | Eşit değildir | İki değer birbirine eşit değilse sonuç TRUE olur. |
| <> | Eşit değildir | İki değer birbirine eşit değilse sonuç TRUE olur. |
| !== | Farklıdır | İki değer birbirine eşit değilse veya veri türleri farklı ise sonuç TRUE olur. |
| < | Küçüktür | Sol tarafındaki değişken değeri sağ taraftakinden küçük ise sonuç TRUE olur. |
| > | Büyüktür | Sol tarafındaki değişken değeri sağ taraftakinden büyük ise sonuç TRUE olur. |
| <= | Küçük veya eşittir | Sol tarafındaki değişken değeri sağ taraftakinden küçük veya eşit ise sonuç TRUE olur. |
| >= | Büyük veya eşittir | Sol tarafındaki değişken değeri sağ taraftakinden büyük veya eşit ise sonuç TRUE olur. |

Örnek

```php
<html>
<body>

<?php
    $deg01 = 24;
    $deg02 = $deg01;
    $deg03 = 35;
    $deg04 = "24";
  
    printf ("%d %d" . "<br/>", $deg01 == $deg02, $deg01 == $deg03);
    printf ("%d %d" . "<br/>", $deg01 === $deg02, $deg01 === $deg04);
    printf ("%d %d" . "<br/>", $deg01 != $deg02, $deg01 <> $deg03);
    printf ("%d %d %d %d", $deg01 < $deg02, $deg01 > $deg03, $deg01 <= $deg03, $deg01 >= $deg03);
?>

</body>
</html>
```

Yukarıdaki dosyayı çalıştırdığımızda, web tarayıcımızda aşağıdaki ifadeler karşımıza çıkar:

```

1 0
1 0
0 1
0 0 1 0

```

## Hata kontrol işlemcileri

PHP'de kullanılan tek hata kontrol işlemcisi @ işaretidir. Bir ifadenin önüne getirildiğinde, o ifade tarafından oluşturulan hata mesajları dikkate alınmaz.

Eğer track\_errors özelliği etkinse bu ifade tarafından oluşturulan hata mesajları $php\_errormsg değişkenine kaydedilir. Her hata durumunda bu değişken değeri değişeceğinden, her defasında değişken değerini kontrol etmeniz gerekir.

Örnek

```php
<html>
<body>

<?php
    $deg_file01 = file ('dosya01.txt');
    $deg_file02 = @file ('dosya01.txt');
    $deg_file03 = @file ('dosya01.txt') or die ("Dosya açma hatası: '$php_errormsg'");  
?>

</body>
</html>



```

Yukarıdaki dosyayı çalıştırdığımızda, "dosya01.txt" dosyası bulunmadığından ilk satırda hata verecek, ikinci satırda ise @ işlemcisini kullanıldığından hata vermeyecek, üçüncü satırda ise hatayı $php\_errormsg değişkeni yoluyla ekrana yazacaktır.

## Çalıştırma işlemcisi

PHP'de kullanılan tek çalıştırma işlemcisi ``(Ters tırnak) işaretidir. Bu işaretlerin bildiğiniz tek tırnak işareti değildir. PHP bu işaret arasında yer alan komutları çalıştırır ve çıktıyı geri döndürür. Çıktı ekrana değil bir değişkene atanabilir. Ters tırnak işlemcisi shell\_exec() fonksiyonu ile aynı işlemi gerçekleştirir.

Safe mode devrede ise veya shell\_exec() fonksiyonu devre dışı ise ters tırnak işlemcisi devre dışı kalır.

## Artırma ve azaltma işlemcileri

Artırma ve azaltma işlemcileri tek bir değere işlem yapan işlem yapılan değişken değerini 1 artıran ya da azaltan işlemcilerdir.

| İşlemci | Adı | Açıklama |
| --- | --- | --- |
| ++ | Artırma | İşlem yapılan değişkenin değerini 1 artırır. |
| -- | Azaltma | İşlem yapılan değişkenin değerini 1 azaltır. |

Artırma ve azaltma işlemcileri bir değişkenin önüne gelirse elde edilen sonuç işlemcinin kullanıldığı ifade içinde, arkasına gelirse daha sonraki işlem satırlarında kullanılır:

Örnek

```php
<html>
<body>

<?php
    $deg01 = 7;
    $deg02 = 18;
   
    echo "İşlem öncesi değerler: " . $deg01 . " " . $deg02 . "<br/>";
    echo "deg01 değeri: " . $deg01++ . "<br/>";
    echo "deg02 değeri: " . ++$deg02 . "<br/>";
    echo "İşlem sonrası değerler: " . $deg01 . " " . $deg02;   
?>

</body>
</html>


```

Yukarıdaki dosyayı çalıştırdığımızda, web tarayıcımızda aşağıdaki ifadeler karşımıza çıkar:

```

İşlem öncesi değerler: 7 18
deg01 değeri: 7
deg02 değeri: 19
İşlem sonrası değerler: 8 19

```

## Mantıksal işlemciler

Mantıksal işlemcileri kullanarak iki değeri karşılaştırabilir ve sonuç olarak değeri TRUE veya FALSE olan boolean bir değer elde edebilirsiniz.

Ve ve veya işlemcilerinin 2 farklı şekilde kullanılmasının nedeni, işlemcilerin farklı önceliğe sahip olmasıdır.

| İşlemci | Adı | Açıklama |
| --- | --- | --- |
| && (and) | Ve | İşleme giren değerlerin her ikisi de doğru ise sonuç TRUE olur. |
| \|\| (or) | Veya | İşleme giren değerlerin herhangi birinin değeri doğru ise sonuç TRUE olur. |
| xor | Ayrıcalıklı Veya | İşleme giren değerler farklı ise sonuç TRUE olur. |
| ! | Değil | İşleme giren değerin değili alınır (TRUE ise FALSE, FALSE ise TRUE). |

Örnek

```php
<html>
<body>

<?php
    $deg01 = 23;
    $deg02 = 78;
   
    printf ("%d %d" . "<br/>", $deg01 > $deg02, $deg01 < $deg02);

    printf ("%d %d", $deg01 < $deg02 && $deg01 > $deg02, $deg01 < $deg02 || $deg01 > $deg02);
?>

</body>
</html>


```

Yukarıdaki dosyayı çalıştırdığımızda, web tarayıcımızda aşağıdaki ifadeler karşımıza çıkar:

```

0 1
0 1

```

## Karakter dizisi işlemcileri

PHP'de kullanılan karakter dizisi işlemcisi birleştirme işlemcisi olan . (nokta) işaretidir. Birleştirme işlemcisi her iki tarafında yer alan değeri birleştirerek bir karakter dizisi oluşturur. Birleştirme işlemcisi = atama işlemcisi ile birlikte kullanılarak .= birleştirme ve atama işlemcisini oluşturur.

Örnek

```php
<html>
<body>

<?php
    $deg01 = "Karakter " . "dizisi ";
    $deg01 .= "işlemcisi "; 
   
    $deg02 = 5 . 6; // Sonuç : "56" 

   echo $deg01 . $deg02;
?>

</body>
</html>


```

Yukarıdaki dosyayı çalıştırdığımızda, web tarayıcımızda aşağıdaki ifadeler karşımıza çıkar:

```

Karakter dizisi işlemcisi 56 

```

Yukarıdaki PHP dosyasında, iki adet tamsayıyı birleştirme işlemcisi ile birleştirdiğinizde bir karakter dizisi elde edersiniz.

## Dizi işlemcileri

Dizi işlemcilerini kullanarak iki diziyi birleştirerek sonucu yine bir dizi olan bir değer veya iki dizi arasında eşitlik, aynılık, eşitsizlik veya farklılık konusunda karşılaştırma yaparak sonucu TRUE veya FALSE olan boolean bir değer elde edebiliriz.

| İşlemci | Adı | Açıklama |
| --- | --- | --- |
| + | Birleşim | İki dizinin birleşimini verir (Sonuç bir dizidir). |
| == | Eşitlik | İki dizi aynı değer adı ve değerlere sahipse sonuç TRUE olur. |
| === | Aynılık | İki dizi sıra ve türleri aynı olan aynı değer adı ve değerlere sahipse sonuç TRUE olur. |
| != | Eşitsizlik | İki dizi birbirine eşit değilse sonuç TRUE olur. |
| <> | Eşitsizlik | İki dizi birbirine eşit değilse sonuç TRUE olur. |
| !== | Farklılık | İki dizi birbirinin aynı değil ise sonuç TRUE olur. |

Birleşim işlemcisi işlem yapılan dizilerin tüm elemanlarını birleştirerek yeni bir dizi oluşturmaz. Sonuçta oluşturulan dizinin boyutu işleme giren dizilerden boyutu büyük olanla aynı olacaktır. Örneğin, işleme giren diziler 2 ve 5 elemanlı ise sonuçta oluşturulacak dizi eleman sayısı 5 olacaktır. İşlemcinin sol tarafında yer alan dizi elemanlarının tamamı sonuçtaki dizi içinde yer alacak, eğer yer kalırsa sağ tarafta yer alan dizinin elemanları, sonuç dizisi içindeki boş kalan sıra numarasıyla, sonuç dizisine yerleştirilecektir. Eğer sol tarafta yer alan dizi eleman sayısı sol taraftakinden büyük ise sağ taraftaki dizi elemanları sonuç dizisinde yer almayacaktır.

Örnek

```php
<html>
<body>

<?php

    $deg01 = array("mavi", "siyah", "beyaz");
    $deg02 = array("kırmızı", "lacivert", "sarı", "yeşil", "gri", "mor");

    $deg03 = $deg01 + $deg02;
    echo "\$deg01 ve \$deg02 birleşimi: \n";
    var_dump($deg03);

    $deg03 = $deg02 + $deg01;
    echo "\$deg02 ve \$deg01 birleşimi: \n";
    var_dump($deg03);
   
?>

</body>
</html>


```

Yukarıdaki dosyayı çalıştırdığımızda, web tarayıcımızda aşağıdaki ifadeler karşımıza çıkar:

```

$deg01 ve $deg02 birleşimi:

array
  0 => string 'mavi' (length=4)
  1 => string 'siyah' (length=5)
  2 => string 'beyaz' (length=5)
  3 => string 'yeşil' (length=5)
  4 => string 'gri' (length=3)
  5 => string 'mor' (length=3)

$deg02 ve $deg01 birleşimi:

array
  0 => string 'kırmızı' (length=7)
  1 => string 'lacivert' (length=8)
  2 => string 'sarı' (length=4)
  3 => string 'yeşil' (length=5)
  4 => string 'gri' (length=3)
  5 => string 'mor' (length=3)

```

Örnek

```php
<html>
<body>

<?php
    $deg01 = array("masa", "sandalye", "dolap");
    $deg02 = array(2=>"dolap", 1=>"sandalye", 0=>"masa");   
    $deg03 = array("perde", "tül", "örtü", "halı");

    printf ("%d %d %d", $deg01 == $deg02, $deg01 === $deg02, $deg01 != $deg03);   
?>

</body>
</html>


```

Yukarıdaki dosyayı çalıştırdığımızda, web tarayıcımızda aşağıdaki ifadeler karşımıza çıkar:

```

1 0 1

```

## Tür işlemcileri

instanceof işlemcisi, bir değişkenin belli bir sınıf için tanımlanan bir nesne olup olmadığını belirlemek için kullanılır.

Örnek

```php
<html>
<body>

<?php
    class personel
    {
        var $adi;          
        var $soyadi;       
        var $yasi;         
    }
   
    class musteri
    {
        var $adi;          
        var $soyadi;       
        var $sirket;         
    }

    $obj = new personel;

    echo "obj değişkeni personel sınıfına ait bir nesne";
    echo ($obj instanceof personel) ? 'dir!' : ' değildir!';
    echo '<br/>';
    echo "obj değişkeni musteri sınıfına ait bir nesne";
    echo ($obj instanceof musteri) ? 'dir!' : ' değildir!';   
?>

</body>
</html>


```

Yukarıdaki dosyayı çalıştırdığımızda, web tarayıcımızda aşağıdaki ifadeler karşımıza çıkar:

```

obj değişkeni personel sınıfına ait bir nesnedir!
obj değişkeni musteri sınıfına ait bir nesne değildir!

```

## İşlemci önceliği

İşlemci önceliği aynı ifade içinde yer alan değişkenlerden hangisine önce işlem yapılacağını belirler. İşlemcilere farklı sıra ile işlem yapılması ifadeden elde edilecek değeri değiştirebilmektedir.

Aşağıdaki atama işleminde $deg01 değişkenine 84 değeri atanır. \* işlemcisi öncelikli olduğundan önce 3 ile 2 sayısı çarpılır, sonra sonuç 14 sayısı ile toplanarak $deg01 değişkenine atanır.

$deg01 = 14 + 3 \* 2;

İşlemci önceliğini değiştirmek için parentez kullanabilirsiniz.

$deg01 = (14 + 3) \* 2; // $deg01 değişkenine 34 değeri atanır.

İşlemciler eşit önceliğe sahip olduğunda, değerlendirmenin sağdan veya soldan başlaması işlemciler arasındaki ilişkiye bağlıdır.

Aşağıdaki listede işlemciler en yüksekten en düşük öncelikliye doğru sıralanmış olup aynı satırda yer alan eşit öncelikli işlemcilerin hangi sırada değerlendirileceğini aralarındaki bağ belirler:

```

İlişkilendirme İşlemci

Yönsüz	            clone new
Soldan	            [
Yönsüz        	    ++ --
Sağdan	            ~ - (int) (float) (string) (array) (object) (bool) @
Yönsüz	            instanceof
Sağdan	            !
Soldan	            * / %
Soldan	            + - .
Soldan	            << >>
Yönsüz	            < <= > >= <>
Yönsüz	            == != === !==
Soldan	            &
Soldan     	            ^
Soldan	            |
Soldan	            &&
Soldan	            ||
Soldan	            ? :
Sağdan	            = += -= *= /= .= %= &= |= ^= <<= >>= => 
Soldan	            and
Soldan	            xor
Soldan	            or
Soldan	            ,

```
 