---
title:  PHP isim alanları
author: sonsuz
date: 2023-08-04 19:52:28 +0300
categories: [Program,PHP]
tags: [php,programlama,web,namespace]
---


PHP 5.3.0 ile birlikte gelen isim alanlarını kullanarak, bir projede kullanılan sınıfları daha düzgün bir şekilde gruplandırabilir ve farklı isim alanlarında tanımlanan birden fazla sınıfın aynı sınıf ismi ile tanınlanmasını sağlayabiliriz.

İsim alanları PHP'de kullanılan tüm öğeleri barındırılabilir. Aynı isime sahip sınıf, fonksiyon ve sabit değerleri farklı isim alanları içinde tanımlanarak kullanılabilir.

## İsim alanlarının tanımlanması

İsim alanlarında her tür PHP kodu bulunabilmesine karşın sadece sınıflar, fonksiyonlar ve sabitler isim alanlarından etkilenir.

İsim alanlarının bildirimi namespace anahtar kelimesi ile yapılır.

Bir isim alanını içeren bir dosyada isim alanı diğer tüm kodlardan önce dosyanın başında bildirilmelidir. Bu kurala tek istisna declare anahtar kelimesidir. Dosya başında yer alan boşluklar, <html> ve <body> ifadeleri dahil olmak üzere hiç bir ifade bir isim alanı bildiriminden önce yer alamaz.

```php
<?php 
    namespace name_bizim; // İsim alanı bildirimi

    const CONBOOL = 1;
    class sinif_bizim { /* ... */ }
    function deger_goster() { /* ... */  }
?>


```

Örnek

```php
<?php 
    namespace name_bizim;

    class sinif_bizim { // İsim alanı içinde sınıf bildirimi
	   public $pubdeg01; 
	   public $pubdeg02; 
       
	   function __construct ($arg01, $arg02)
       {
            $this->pubdeg01 = $arg01;       
            $this->pubdeg02 = $arg02; 
       }	   
      
	   public function deger_yaz()
       {
          echo $this->pubdeg01 . " " . $this->pubdeg02 . '<br/>';
       }	   
	}
    function fonk($arg) { // İsim alanı içinde fonksiyon bildirimi
	  echo $arg;
	}
	const CONINT = 17; // İsim alanı içinde sabit bildirimi

    $obj01 = new sinif_bizim(35, 84); // İsim alanındaki sınıftan nesne oluşturma
    $obj02 = new \name_bizim\sinif_bizim(42, 57); // İsim alanındaki sınıftan yol tanımı ile nesne oluşturma

    $obj01->deger_yaz();
	$obj02->deger_yaz();	
	
	echo CONINT; 
?>


```

Yukarıdaki dosyayı çalıştırdığımızda, web tarayıcımızda aşağıdaki ifadeler karşımıza çıkar::

```

35 84
42 57
17

```

## Alt isim alanlarının bildirilmesi

PHP isim alanı isimleri arasında bir hiyeraraşi oluşturulabileceğinden, bir isim alanı başka isim alanlarının altında tanımlanabilir.

```php
<?php 
    namespace name_bizim\Alt\Seviye;

    const CONBOOL = 1;
    class sinif_bizim { /* ... */ }
    function deger_goster() { /* ... */  }
?>


```

Yukarıdaki örnek ile, name\_bizim\Alt\Seviye\CONBOOL sabiti, name\_bizim\Alt\Seviye\sinif\_bizim sınıfı ve Projem\Alt\Seviye\deger\_goster fonksiyonu oluşturulmaktadır.

## Aynı dosyada birden fazla isim alanının tanımlanması

Aynı dosyada birden fazla isim alanının tanımlanabilir. Bu işlem için iki farklı yazım yöntemi vardır:

```php
<?php
    namespace Proje01;
        const CONBOOL = 1;
        class sinif_bizim { /* ... */ }
        function deger_goster() { /* ... */  }

    namespace Proje02;
        const CONBOOL = 1;
        class sinif_bizim { /* ... */ }
        function deger_goster() { /* ... */  }

    namespace Proje03 {
        const CONBOOL = 1;
        class sinif_bizim { /* ... */ }
        function deger_goster() { /* ... */  }
    }

    namespace Proje04 {
        const CONBOOL = 1;
        class sinif_bizim { /* ... */ }
        function deger_goster() { /* ... */  }
    }
?>


```

Yukarıdaki örnek ile, ilk ikisi düz yazım ve son ikisi parentezli yazım yöntemi ile olmak üzere toplam 4 farklı isim alanı tanımlanmıştır. Parentezli yöntemin kullanılması tavsiye edilmektedir.

Birden fazla isim alanının aynı dosyada içinde tanımlanması tavsiye edilmemektedir.

İsim alansız global kod ile isim alanlı kodu aynı dosyada kullanmak için parentezli yazım yöntemi kullanmak zorunludur.

```php
<?php
    namespace ProjeEsas {
        const CONBOOL = 1;
        class deger_goster() { /* ... */ }
        function deger_goster() { /* ... */  }
    {

    namespace {  // global kod
        session_start();
        $obj = ProjeEsas\deger_goster();
        echo ProjeEsas\deger_goster()::basla();
    }
?>


```

## İsim alanlarının kullanılmasında temel kavramlar

İsim alanlarının kullanımı konusuna değinmeden önce PHP'nin kodun hangi isim alanını gösterdiğini nasıl anladığını açıklamaya çalışalım. Bu amaçla, PHP isim alanları ile dosya sistemleri arasında mantık açısından bir bağ kurulabilir. Bir dosya sisteminde yer alan bir dosyaya üç yolla erişilebilir:

1. deneme.txt gibi bir dosya ismiyle: Bu isim dosya sisteminde geçerlidizin/deneme.txt olarak işlem görür (geçerlidizin ifadesi içinde bulunulan dizini gösterir). Eğer, geçerli dizin /veri/dosyalar ise dosya ismi /veri/dosyalar/deneme.txt olarak işlem görecektir.

2. altdizin/deneme.txt şeklinde bağlantılı bir dosya yoluyla: Bu isim dosya sisteminde geçerlidizin/altdizin/deneme.txt olarak işlem görür.

3. /veri/dosyalar/deneme.txt şeklinde kesin bir dosya yoluyla: Bu isim dosya sisteminde /veri/dosyalar/deneme.txt olarak işlem görür.

Aynı kurallar PHP'de isim alanı içinde yer alan elemanlara da uygulanabilir. Örneğin bir sınıf ismine üç şekilde erişim sağlanabilir:

1. $obj = new sinif\_bizim(); veya sinif\_bizim::static\_ yontem(); gibi bir nitelenmemiş isim veya öneksiz bir sınıf ismi: Eğer geçerli isim alanı ismi geçerlisimalanı ise bu isim, geçerlisimalanı\sinif\_bizim olarak işlem görür. Eğer kod global ve isim alansız ise, isim sinif\_bizim olarak işlem görür. Eğer isim alannda yer alan fonksiyon ve sabitler tanımlı değil ise, fonksiyon ve sabitler için nitelenmemiş isimler global olarak işlem görürler.

2. $obj = new altisimalanı\sinif\_bizim(); veya altisimalanı\sinif\_bizim::static\_ yontem(); gibi bir nitelenmiş isim veya önekli bir sınıf ismi: Eğer geçerli isim alanı ismi geçerlisimalanı ise bu isim, geçerlisimalanı\altisimalanı\sinif\_bizim olarak işlem görür. Eğer kod global ve isim alansız ise, isim altisimalanı\sinif\_bizim olarak işlem görür.

3. $obj = new \geçerlisimalanı\sinif\_bizim(); veya \geçerlisimalanı\sinif\_bizim::static\_yontem(); gibi tamamen nitelenmiş isim veya küresel önekli bir isim: Bu isim daima kodda belirtildiği gibi geçerlisimalanı\sinif\_bizim olarak çözümlenir.

Örnek

```php
// dosya01.php
<?php
    namespace name_bizim\proje01\name_alt;

    const CONINT = 1;
    function fonk_bizim()
    {
	    echo "Alt isim alanı fonksiyonu çalıştı.<br/>";   
    }
    class sinif_bizim
    {
        static function static_yontem()
        {
	        echo "Alt isim alanı sınıfı içindeki static fonksiyon çalıştı.<br/>";   
        }		
    }	
?> 

// deneme.php
<?php
    namespace name_bizim\proje01;
    include 'dosya01.php';

    const CONINT = 2;
    function fonk_bizim()
    {
	    echo "Üst isim alanı fonksiyonu çalıştı.<br/>";   
    }
    class sinif_bizim
    {
        static function static_yontem()
        {
	        echo "Üst isim alanı sınıfı içindeki static fonksiyon çalıştı.<br/>";   
        }
    }

    // Nitelenmemiş isim  
    fonk_bizim(); // name_bizim\proje01\fonk_bizim fonksiyonu çalışır.
    // name_bizim\proje01\sinif_bizim sınıfına ait static_yontem() yöntemi çalışır.
    sinif_bizim::static_yontem();
    echo CONINT . "<br/>"; // name_bizim\proje01\CONINT sabiti ekrana yazılır.

    // Nitelenmiş isim
    name_alt\fonk_bizim(); // name_bizim\proje01\name_alt\fonk_bizim fonksiyonu çalışır.
    // name_bizim\proje01\name_alt\sinif_bizim sınıfına ait static_yontem() yöntemi
    // çalışır.
    name_alt\sinif_bizim::static_yontem();
    // name_bizim\proje01\name_alt\CONINT sabiti ekrana yazılır.
    echo name_alt\CONINT . "<br/>"; 
                                  
    // Tamamen nitelenmiş isim
    \name_bizim\proje01\fonk_bizim();// name_bizim\proje01\fonk_bizim fonksiyonu çalışır.
    // name_bizim\proje01\sinif_bizim sınıfına ait static_yontem() yöntemi çalışır.
    \name_bizim\proje01\sinif_bizim::static_yontem();
    // name_bizim\proje01\CONINT sabiti ekrana yazılır.
    echo \name_bizim\proje01\CONINT . "<br/>"; 
?>


```

Yukarıdaki dosyayı çalıştırdığımızda, web tarayıcımızda aşağıdaki ifadeler karşımıza çıkar::

```

Üst isim alanı fonksiyonu çalıştı.
Üst isim alanı sınıfı içindeki static fonksiyon çalıştı.
2
Alt isim alanı fonksiyonu çalıştı.
Alt isim alanı sınıfı içindeki static fonksiyon çalıştı.
1
Üst isim alanı fonksiyonu çalıştı.
Üst isim alanı sınıfı içindeki static fonksiyon çalıştı.
2

```

Örnek

```php
<?php
    namespace name_bizim;

    function strlen($str) 
    {
        echo "name_bizim isim alanı strlen() fonksiyonu çalışıyor.<br/>";
        for ($deg01=0; $str[$deg01]; $deg01++) {
             echo $str[$deg01];	  
        }
        echo " uzunluğu: "; 
		
        return $deg01;
    }
		
    echo strlen('İsim alanları') . "<br/>"; // name_bizim strlen() fonksiyonu çağrılır.
                                  
    echo \strlen('Global fonksiyonlar'); // Global strlen() fonksiyonu çağrılır.
?>


```

Yukarıdaki dosyayı çalıştırdığımızda, web tarayıcımızda aşağıdaki ifadeler karşımıza çıkar::

```

name_bizim isim alanı strlen() fonksiyonu çalışıyor.
İsim alanları uzunluğu: 13
19

```

## İsim alanları ve dinamik dil özellikleri

PHP'de isim alanlarının uygulanması bir programlama dili olarak PHP'nin dinamik yapısından etkilenir. Aşağıdaki dosya01.php dosyasında yer alan kodlar bir sonraki örnekte isim alanlı koda dönüştürülmüştür. Bu durumda, tamamen nitelenmiş isim kullanmak gerekir(isim alanı önekli sınıf adı). Dinamik bir sınıf, fonksiyon ve sabit adı içinde nitelenmiş bir isim ile tamamen nitelenmiş bir isim arasında bir fark olmadığından, baştaki ters bölüm işareti gereksizdir.

Örnek

```php
<?php
    class sinif_adi
    {
        function __construct()
        {
            echo __METHOD__,"<br/>";
        }	
    }

    function fonk_adi()
    {
        echo __FUNCTION__,"<br/>";
    }

    const sabit_adi = "global";

    $a = 'sinif_adi';
    $obj = new $a; // sinif_adi::__construct ifadesini ekrana yazar.
    $b = 'fonk_adi';
    $b(); // fonk_adi ifadesini ekrana yazar.
    echo constant('sabit_adi'), "<br/>"; // global ifadesini ekrana yazar.	
?>


```

Yukarıdaki dosyayı çalıştırdığımızda, web tarayıcımızda aşağıdaki ifadeler karşımıza çıkar::

```

sinif_adi::__construct
fonk_adi
global

```

Örnek

```php
// dosya01.php
<?php
    class sinif_adi
    {
        function __construct()
        {
            echo __METHOD__,"<br/>";
        }	
    }

    function fonk_adi()
    {
        echo __FUNCTION__,"<br/>";
    }

    const sabit_adi = "global";
?>

// deneme.php
<?php
    namespace name_bizim;
	
    class sinif_adi
    {
        function __construct()
        {
            echo __METHOD__,"<br/>";
        }	
    }

    function fonk_adi()
    {
        echo __FUNCTION__,"<br/>";
    }

    const sabit_adi = "isimalanlı";
	
    include 'dosya01.php';

    $a = 'sinif_adi';
    $obj = new $a; // sinif_adi::__construct ifadesini ekrana yazar.
    $b = 'fonk_adi';
    $b(); // fonk_adi ifadesini ekrana yazar.
    echo constant('sabit_adi'), "<br/>"; // global ifadesini ekrana yazar.

    // Eğer çift tırnak kullanılırsa, "\\name_bizim\\sinif_adi" şeklinde tanımlanmalıdır.
    $a = '\name_bizim\sinif_adi';
    $obj = new $a; // name_bizim\sinif_adi::__construct ifadesini ekrana yazar.
    $a = 'name_bizim\sinif_adi';
    $obj = new $a; // name_bizim\sinif_adi::__construct ifadesini ekrana yazar.
    $b = 'name_bizim\fonk_adi';
    $b(); // name_bizim\fonk_adi ifadesini ekrana yazar.
    $b = '\name_bizim\fonk_adi';
    $b(); // name_bizim\fonk_adi ifadesini ekrana yazar.
    echo constant('\name_bizim\sabit_adi'), "<br/>";// isimalanlı ifadesini ekrana yazar.
    echo constant('name_bizim\sabit_adi'), "<br/>"; // isimalanlı ifadesini ekrana yazar.	
?>


```

Yukarıdaki dosyayı çalıştırdığımızda, web tarayıcımızda aşağıdaki ifadeler karşımıza çıkar::

```

sinif_adi::__construct
fonk_adi
global
name_bizim\sinif_adi::__construct
name_bizim\sinif_adi::__construct
name_bizim\fonk_adi
name_bizim\fonk_adi
isimalanlı
isimalanlı

```

## namespace anahtar kelimesi ve \_\_NAMESPACE\_\_ sabiti

PHP'de geçerli isim alanı içindeki elemanlara mutlak olarak \_\_NAMESPACE\_\_ sihirli sabiti ve namespace anahtar kelimesi ile erişimi destekler.

\_\_NAMESPACE\_\_ sabitinin değeri içinde bulunulan isim alanının adını içeren bir karakter dizisidir. Global olarak değerlendirildiğinde, isim alanı olmayan kodlar içinde, boş bir karakter dizisi içerir.

```php
<?php
    //İsim alanı kodlu __NAMESPACE__ örneği
    namespace name_bizim;

    echo '"', __NAMESPACE__, '"'; // Ekrana "name_bizim" yazar.
?>


```

```php
<?php
    //Global kodlu __NAMESPACE__ örneği

    echo '"', __NAMESPACE__, '"'; // Ekrana "" yazar.
?>


```

\_\_NAMESPACE\_\_ sabiti isimleri dinamik olarak oluşturmak için kullanılabilir:

```php
<?php
    namespace name_bizim;

    function isim_al($classname)
    {
        $a = __NAMESPACE__ . '\\' . $classname;
        return new $a;
    }	
?>


```

namespace anahtar kelimesi geçerli isim alanı veya alt isim alanında yer alan bir elemana erişim için kullanılır. Sınıflardaki self işlemcisinin isim alanlarındaki karşılığıdır.

```php
<?php
    // İsim alanı içinde namespace örneği
    namespace name_bizim;

    use blah\blah as mine;

    blah\mine(); // name_bizim\blah\mine() fonksiyonunu çağırır.
    namespace\blah\mine(); // name_bizim\blah\mine() fonksiyonunu çağırır.

    namespace\func(); // name_bizim\func() fonksiyonunu çağırır.
    namespace\sub\func(); // name_bizim\sub\func() fonksiyonunu çağırır.
    // name_bizim\cname sınıfının yontem adlı static fonksiyonunu çağırır.
    namespace\cname::yontem();
	
    // name_bizim\sub\cname sınıfına ait bir nesne oluşturur.
    $a = new namespace\sub\cname();
    $b = namespace\CONSTANT; // name_bizim\CONSTANT sabitini $b değişkenine atar.
?>


```

```php
<?php
    //Global kod içinde namespace örneği
    namespace\func(); // func() fonksiyonunu çağırır.
    namespace\sub\func(); // sub\func() fonksiyonunu çağırır.
    namespace\cname::yontem();// cname sınıfının yontem adlı static fonksiyonunu çağırır.
    $a = new namespace\sub\cname(); // sub\cname sınıfına ait bir nesne oluşturur.
    $b = namespace\CONSTANT; // CONSTANT sabitini $b değişkenine atar.
?>


```

## İsim alanlarının kullanımı: İthal/Rumuz (Aliasing/Importing)

İsim alanlarının önemli özelliklerinden birisi, tamamen nitelenmiş harici bir isme takma bir adla veya ithal ederek erişim sağlamasıdır.

PHP isim alanları ile bir sınıf, arayüz ve isim alanına takma ad veya ithal etme işlemi uygulanabilir. Bir fonksiyon veya sabite ise bu işlem uygulanmaz.

PHP'de, takma ad verme işlemi use işlemcisi ile gerçekleştirilir.

```php
<?php
    namespace name_bizim;
    use My\Full\Classname as Another;

    My\Full\NSname as NSname ifadesi ile aynı işlemi gerçekleştirir.
    use My\Full\NSname;

    // global bir sınıf ithal eder.
    use ArrayObject;

    $obj = new namespace\Another; // name_bizim\Another sınıfından bir nesne tanımlar.
    $obj = new Another; // My\Full\Classname sınıfından bir nesne tanımlar.
    NSname\subns\func(); // My\Full\NSname\subns\func fonksiyonunu çağırır.
    // ArrayObject sınıfından bir nesne tanımlar
    // Eğer "use ArrayObject" kullanılmasaydı, name_bizim\ArrayObject sınıfından bir
    // nesne tanımlayacaktı.    
    $a = new ArrayObject(array(1));	
?>


```

İsim alanlı adlar için (), önünde yer alan \ işareti gereksiz olup kullanılması önerilmez, ithal edilmiş isimler tamamen nitelenmiş olması gerektiğinden, ve içinde bulunulan isim alanına göre işlem yapılmazlar.

PHP'de aynı komut satırında birden fazla use ifadesi kullanılabilir:

```php
<?php
    use My\Full\Classname as Another, My\Full\NSname;

    $obj = new Another; // My\Full\Classname sınıfından bir nesne tanımlar.
    NSname\subns\func(); // My\Full\NSname\subns\func fonksiyonunu çağırır.
?>


```

Dahil etme işlemi derleme zamanında gerçekleşeceğinden dinamik olarak oluşturulmuş sınıf, fonksiyon ve sabit adlarını etkilemez:

```php
<?php
    use My\Full\Classname as Another, My\Full\NSname;

    $obj = new Another; // My\Full\Classname sınıfından bir nesne tanımlar.
    $a = 'Another';
    $obj = new $a; // Another sınıfından bir nesne tanımlar.
?>


```

Ayrıca, ithal etme işlemi sadece nitelenmemiş ve nitelenmiş isimleri etkiler. Tamamen nitelenmiş isimler mutlak olup ithal işleminden etkilenmez:

```php
<?php
    use My\Full\Classname as Another, My\Full\NSname;

    $obj = new Another; // My\Full\Classname sınıfından bir nesne tanımlar.
    $obj = new \Another; // Another sınıfından bir nesne tanımlar.
    $obj = new Another\thing; // My\Full\Classname\thing sınıfından bir nesne tanımlar.
    $obj = new \Another\thing; // Another\thing sınıfından bir nesne tanımlar.
?>


```

## Global alan

Herhangi bir isim alanı tanımı yapılmadığında, tüm sınıf ve işlev tanımlamaları global alana yerleştirilir. Bir ismin önüne doğrudan doğruya \ işareti konulması, bu ismin, bir isim alanı içinde yer alsa bile, küresel alanda tanımlnamış bir isim olarak işlem görmesini sağlar.

```php
<?php
    namespace A\B\C;

    // A\B\C\fopen fonkisyonunu gösterir.
    function fopen() { 
         $f = \fopen(...); // Global fopen fonkisyonunu çağırır.
         return $f;
    } 
?>


```

## İsim alanlarında global fonksiyon ve sabitlerin son seçenek olarak kullanılması

Bir isim alanı içinde, PHP nitelenmemiş bir sınıf, fonksiyon veya sabit ismine rastladığında, bunları farklı önceliklerle ele alır. Sınıf isimleri daima geçerli isim alanına göre değerlendirilir. Dolayısıyla yerleşik veya isim alansız kullanıcı sınıflarına erişmek için, tamamen nitelenmiş isimlerinin kullanılması gerekir:

```php
<?php
    namespace A\B\C;
    class Exception extends \Exception {}

    $a = new Exception('hi'); // $a A\B\C\Exception sınıfının bir nesnesidir.
    $b = new \Exception('hi'); // $b Exception sınıfının bir nesnesidir.

    $c = new ArrayObject; // Hata, A\B\C\ArrayObject sınıfı bulunamadı.
?>


```

Fonksiyon ve sabitler için, bir isim alanlı fonksiyon veya sabit mevcut değilse, PHP son çare olarak global fonksiyon ve sabitleri kullanır.

Örnek

```php
<?php
    namespace A\B\C;

    const E_ERROR = 45;
    function strlen($str)
    {
         return \strlen($str) - 1;
    }

    echo E_ERROR, "<br/>"; // Ekrana "45" yazar.
    echo INI_ALL, "<br/>"; // Ekrana "7" yazar - global INI_ALL

    echo strlen('hi'), "<br/>"; // Ekrana "1" yazar.
    if (is_array('hi')) { // Ekrana "dizi değildir" yazar.
        echo "dizidir<br/>";
    } 
    else {
        echo "dizi değildir<br/>";
    }
?>


```

Yukarıdaki dosyayı çalıştırdığımızda, web tarayıcımızda aşağıdaki ifadeler karşımıza çıkar::

```

45
7
1
dizi değildir

```

## İsim çözünürlük kuralları

İsim alanı adı tanımları

* Nitelenmemiş isim: name\_bizim gibi bir isim alanı ayracı içermeyen bir niteleyici.
* Nitelenmiş isim: name\_bizim\Proje01 gibi bir isim alanı ayracı içeren bir niteleyici.
* Tamamen nitelenmiş isim: \name\_bizim\Proje01 gibi bir isim alanı ayracı ile başlayan isim alanı ayraçlı bir niteleyici. namespace\name\_bizim ifadesi de tamamen nitelenmiş bir isimdir.

İsimler aşağıdaki kurallara göre çözümlenir:

1. Tamamen nitelenmiş fonksiyon, sınıf ve sabit isimleri derleme sırasında çözümlenir. Örneğin, new \A\B deyimi A\B sınıfı olarak çözümlenir.

2. Nnitelenmemiş ve nitelenmiş isimlerin tamamı derleme sırasında geçerli ithal kurallarına göre dönüştürülür. Örneğin, A\B\C isim alanı C olarak ithal edilmişse bir C\D\e() çağrısı A\B\C\D\e() çağrısına dönüştürülür.

3. Bir isim alanı içinde ithal kurallarına göre dönüştürülmeyen tüm nitelenmiş isimlerin önüne geçerli isim alanı ismi getirilir. Örneğin, A\B isim alanında yapılmış bir C\D\e() çağrısı A\B\C\D\e() çağrısına dönüştürülür.

4. Nitelenmemiş sınıf isimleri derleme sırasında geçerli ithal kurallarına göre dönüştürülür (kısa ithal ismi için tam isim kullanılır). Örneğin, A\B\C isim alanı C olarak ithal edilmişse new C() deyimi new A\B\C() deyimine dönüştürülür.

5. İsim alanı içindeki (A\B olsun), nitelenmemiş işlev çağrıları çalışma anında çözümlenir. fonk() diye bir işlev şöyle çözümlenir:

	a. Geçerli isim alanında A\B\fonk() işlevi aranır.

	b. Global fan() işlevi bulunmaya ve çağrılmaya çalışılır.

6. İsim alanı içindeki (A\B olsun), nitelenmemiş (tamamen nitelenmemiş) veya nitelenmiş sınıf ismi çağrıları çalışma anında çözümlenir. new C() ve new D\E() deyimlerinin çözümlenişi aşağıda verilmiştir.

new C() için:

* Geçerli isim alanında A\B\C sınıfı aranır.

* A\B\C otomatik olarak yüklenmeye çalışılır.

new D\E() için:

* Önüne geçerli isim alanı A\B\D\E getirilmiş bir sınıf aranır.

* A\B\D\E otomatik olarak yüklenmeye çalışılır.

Global isim alanındaki global bir sınıfa başvururken new \C() şeklinde tamamen nitelenmiş bir isim kullanılmalıdır.

```php
<?php
    namespace A;
    use B\D, C\E as F;

    // Fonksiyon çağrıları

    fonk(); // Önce "A" isim alanındaki "fonk", yoksa "fonk" global fonksiyonu çağrılır.

    \fonk(); // Global alandaki "fonk" fonksiyonu çağrılır.
  
    my\fonk(); // "A\my" isim alanındaki "fonk" fonksiyonu çağrılır.

    F(); // "A" isim alanındaki "F", yoksa "F" global fonksiyonu çağrılır. 

    // Sınıf erişimleri

    // "A" isim alanında tanımlanan "B" sınıfından bir nesne oluşturur, 
    // eğer bulunamazsa "A\B" sınıfını otomatik olarak yüklemeye çalışır.
    new B();
	
    // İthal kurallarını kullanarak, "B" isim alanında tanımlanan "D" sınıfından bir
    // nesne oluşturur,eğer bulunamazsa "B\D" sınıfını otomatik olarak yüklemeye çalışır.
    new D();

    // İthal kurallarını kullanarak, "C" isim alanında tanımlanan "E" sınıfından bir
    // nesne oluşturur,eğer bulunamazsa "C\E" sınıfını otomatik olarak yüklemeye çalışır. 
    new F();

    // Global alanda tanımlanan "B" sınıfından bir nesne oluşturur, 
    // eğer bulunamazsa "B" sınıfını otomatik olarak yüklemeye çalışır.
    new \B();

    // Global alanda tanımlanan "D" sınıfından bir nesne oluşturur, 
    // eğer bulunamazsa "D" sınıfını otomatik olarak yüklemeye çalışır.
    new \D();
	
    // Global alanda tanımlanan "F" sınıfından bir nesne oluşturur, 
    // eğer bulunamazsa "F" sınıfını otomatik olarak yüklemeye çalışır.
    new \F();

    // Farklı bir isim alanındaki static yöntemler/isim alanı fonksiyonları

    // "fonk" fonksiyonunu "A\B" isim alanından çağırır.
    B\fonk();

    // "A" isim alanında tanımlanan "B" sınıfına ait "fonk" fonksiyonunu çağırır, 
    // eğer "A\B" sınıfı bulunamazsa "A\B" sınıfını otomatik olarak yüklemeye çalışır. 
    B::fonk();
	
    // İthal kurallarını kullanarak, "B" isim alanında tanımlanan "D" sınıfına ait
    // "fonk" fonksiyonunu çağırır, eğer "B\D" sınıfı bulunamazsa "B\D" sınıfını
    // otomatik olarak yüklemeye çalışır.	
    D::fonk();

    // "fonk" fonksiyonunu "B" isim alanından çağırır.
    \B\fonk();
	
    // Global alanda tanımlanan "B" sınıfına ait "fonk" fonksiyonunu çağırır, 
    // eğer "B" sınıfı bulunamazsa "B" sınıfını otomatik olarak yüklemeye çalışır.
    \B::fonk();

    // Geçerli isim alanındaki static yöntemler/isim alanı fonksiyonları

    // "A\A" isim alanında tanımlanan "B" sınıfına ait "fonk" fonksiyonunu çağırır, 
    // eğer "A\A\B" sınıfı bulunamazsa "A\A\B" sınıfını otomatik olarak yüklemeye
    // çalışır. 	
    A\B::fonk();
	
    // "A" isim alanında tanımlanan "B" sınıfına ait "fonk" fonksiyonunu çağırır, 
    // eğer "A\B" sınıfı bulunamazsa "A\B" sınıfını otomatik olarak yüklemeye çalışır. 	
    \A\B::fonk();
?>


```
 