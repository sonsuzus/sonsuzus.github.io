---
title:  C Yorum satırları
author: sonsuz
date: 2023-07-30 22:07:41 +0300
categories: [Program,C]
tags: [programlama,c,yorum]
---

Kaynak dosyaların içine bazen programın daha kolay anlaşılması için açıklayıcı satırlar eklenebilir. Bu satırlara Yorum Satırı adı verilir. Yorum satırlarının yazılan programla herhangi bir ilgisi yoktur. Sadece, programı inceleyenlerin, programı daha kolay bir şekilde anlamalarına yardımcı olur. Ayrıca, geçici olarak iptal etmek istediğimiz işlem satırlarını silmeden devre dışı bırakmak için de yorum satırı kavramını kullanabilirniz. Yorum satırlarına derleyici tarafından kesinlikle herhangi bir işlem yapılmaz. Yorum satırları sanki hiç yokmuş gibi işlem görür.

Yorum satırı /\* işaretleri ile başlar ve \*/ işaretleri ile sona erer. Yorum satırı kullanılan bir programı incelemeye çalışalım:

Örnek

```c
#include <stdio.h>

void main(void)
{
  int id;            /* Değişken bildirimi */

  id = 27;           /* Değişkene değer atanması */
  printf("%d", id);  /* Değişken değerinin ekrana yazılması */
  
  return 0;
}


```

Yukarıdaki örnekte, program aşağıdaki satırı ekrana yazar: 

```
27
```

Program içinde tek satırlık yorumlar yer almaktadır. Ancak, bu satırlar programın çalışmasını herhangi bir şekilde etkilemez.

Bir satırdan fazla yer tutan yorumları kullanabilirsiniz. Bir satırdan fazla yer tutan yorum ise aşağıdaki şekilde yapılmaktadır:

```c
/* Burada yer alan yorum satırları
   programın çalışmasını etkilemez! */

```

C'de, yorumlarınızı programın herhangi bir yerinde yapabilirsiniz. Bu konuda herhangi bir sınırlama yoktur.

C'de, birbiri içinde yer alan yorum satırları kullanamazsınız. Bu şekilde oluşturduğunuz bir dosyayı derlemek istediğinizde derleyiciniz bir hata mesajı vererek derleme işlemine son verir:

/\* Bu yorum satırı içindeki /\* diğer yorum satırı \*/ hataya yol açar! \*/

Yukarıda gösterilen yorum satırında, turuncu renkle gösterilen değerler (/\* diğer yorum satırı \*/) programın hata vermesine neden olur.

C99 standartları ile birlikte // ifadesi kullanılarak tek satırlık yorum satırları tanımlama olanağı sağlanmıştır. Ancak, C89 standartları bu kullanımı desteklememektedir.

Örnek

```c
#include <stdio.h>

void main(void)
{
  int id;           // Değişken bildirimi

  id = 27;          // Değişkene değer atanması
  printf("%d", id); // Değişken değerinin ekrana yazılması
  
  return 0;
}
```
