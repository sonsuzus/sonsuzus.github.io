---
title:  C++ Yorum satırları
author: sonsuz
date: 2023-08-06 14:59:49 +0300
categories: [Program,C++]
tags: [cpp,programlama,yorum satırı]
---


Kaynak kodlarının bulunduğu dosyaların içine bazen programın daha kolay anlaşılması için açıklayıcı satırlar eklenebilir. Bu satırlara "Yorum Satırı" adı verilir. Yorum satırlarının yazılan programla herhangi bir ilgisi yoktur. Sadece, programı inceleyenlerin, programı daha kolay bir şekilde anlamalarına yardımcı olur. Ayrıca, geçici olarak iptal etmek istediğiniz işlem satırlarını silmeden devre dışı bırakmak için de yorum satırı kavramını kullanabiliriz. Yorum satırlarına derleyici tarafından kesinlikle herhangi bir işlem yapılmaz ve hiç yokmuş gibi işlem görür.

C++'da 2 farklı şekilde yorum satırı oluşturabiliriz:

> /\* ve \*/ işaretleri ile
{: .prompt-info }

Yorum satırı veya satırları /\* işaretleri ile başlar ve \*/ işaretleri ile sona erer. Bu tanımlamada birden fazla yorum satırı eklenebilir.

> // işareti ile
{: .prompt-info }

Yorum satırı // işareti ile başlar. Bu tanımlamada tek satırlık yorum eklenebilir.

Örnek

```c++
#include <iostream>

using namespace std;

int main()
{
    /* Bu satır ile standart C++ kütüphanesinde yer alan 
    cout komutu ile ekran bir cümle yazılmaktadır. */
    cout << "C++ Programlama Dili" << endl;
    cout << "Nesneye Dayalı Programlama"; // cout komutu ikinci kullanım
    
    return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

C++ Programlama Dili
Nesneye Dayalı Programlama

```

Program içinde hem bir hem de birden fazla satırdan oluşan yorumlar yer almaktadır. Ancak, bu satırlar programın çalışmasını herhangi bir şekilde etkilemez.

Yorum satırlarını programınızın herhangi bir yerinde kullanabiliriz. Bu konuda herhangi bir sınırlama yoktur.

C++'da, /\* ve \*/ işaretleri ile birbiri içinde yer alan yorum satırları kullanamayız. Bu şekilde oluşturduğumuz bir dosyayı derlemek istediğinizde derleyici hata verir.

```c++
/* Bu yorum satırı içindeki /* diğer yorum satırı */ hataya yol açar! */


```

Yukarıda gösterilen yorum satırında, /\* diğer yorum satırı \*/ ifadesi programın hata vermesine neden olur.
