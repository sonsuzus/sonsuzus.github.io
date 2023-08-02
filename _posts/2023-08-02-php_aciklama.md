---
title:  PHP'de açıklamalar
author: sonsuz
date: 2023-08-02 18:46:31 +0300
categories: [Program,PHP]
tags: [php,programlama,sunucu,açıklama]
---


PHP'de sadece kodlar hakkında bilgi vermek, hatırlatma yapmak vb.amaçlarla kodlar arasına açıklama cümleleri ekleyebilirsiniz. Bu açıklama ifadeleri PHP komut çevirici tarafından sanki hiç yazılmamış gibi işlem görür.

```

Bir PHP dosyasına açıklama (yorum) ekleyebilmek için:

1. C Programlama Dili yapısını ve     /* Açıklama metini */
2. C++ Programlama Dili yapısını     // Açıklama metini 

kullanabilirsiniz.

```

Bir örnek üzerinde incelemeye çalışalım:

```php
<html>
<body>

<?php 
    echo '<p>Bu ilk PHP yazısıdır!</p>';       /* Bu dosyadaki ilk PHP komutudur. */
    echo '<p>Bu ikinci PHP yazısıdır!</p>';   // Bu dosyadaki ikinci PHP komutudur. 
   
    /*
      Yukarıdaki 2 komut satırında  
      farklı tarzda yorum yapılmıştır!
    */   
?>

</body>
</html>


```

Yukarıdaki dosyayı çalıştırdığınızda, web taracıyınızda aşağıdaki ifadeler karşınıza çıkar:

```

Bu ilk PHP yazısıdır!

Bu ikinci PHP yazısıdır!

```

PHP komutları içinde kullanılan açıklama satırları hiç yazılmamış gibi işlem görmektedir.
