---
title:  C++ Veri türü tanımlama (Typedef)
author: sonsuz
date: 2023-08-10 16:01:35 +0300
categories: [Program,C++]
tags: [cpp,programlama,typedef,veri türü]
---


typedef ifadesini kullanarak, standart veri türlerinini (int, char, float, vs.) veya kullanıcı tanımlı yapıları farklı isimlerle tanımlayabiliriz. Bu şekilde mevcut bir veri türü için yeni bir isim veya yeni bir veri türü oluşturabiliriz. typedef ifadesinin genel yapısı aşağıdaki gösterilmektedir:

```


typedef eski-isim yeni-isim;


```

Yukarıdaki işlem satırı ile oluşturulan yeni-isim ifadesini değişken bildiriminde kullanabiliriz.

Aşağıdaki işlem satırı, bir int değişken tanımlamak için tms ifadesini kullanma olanağı sağlar:

```c++
typedef int tms;


```

Yukarıdaki işlem satırını tanımladıktan sonra, program içinde int bir değişken tanımlamak için int ifadesi yerine tms ifadesini kullanabiliriz.

Şimdi, bu özelliği bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

typedef int tms;

int main(void)
{
  tms id;

  id = 21;

  cout << id;

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

21

```

Program typedef kullanarak int ifadesi ile aynı işlemi gerçekleştiren tms adlı bir başka bir ifade tanımlar. Değişken bildiriminde tms ifadesini kullanır.

typedef ifadesini kullanarak bir veri türünü temsil eden ikinci bir ifade tanımlamamız ilk ifadeyi geçersiz hale getirmez. Bir veri türünü temsil eden ikiden fazla ifade tanımlayabiliriz. Bu özelliği bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

typedef int tms;
typedef tms tams;

int main(void)
{
  int id1;

  tms id2;
  tams id3;

  id2 = 4;
  id3 = 11;

  for (id1=0; id1<5; id1++, id2++, id3++) cout << id2+id3 << " ";

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

15 17 19 21 23

```

Program, size bir int değişkeni tanımlamak için 3 farklı ifade kullanma olanağı sağlar. Sonuç olarak, id1, id2 ve id3 değişkenlerinin hepsi birer int değişkendir.

Uzun ifadelerle bildirimleri yapılan veri türleri için typedef ifadesini kullanarak kısa kelimeler elde edebiliriz:

Örnek

```c++
#include <iostream>

using namespace std;

typedef unsigned short int usi;

int main(void)
{
  usi usid;

  usid = 32453;

  cout << usid;

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

32453

```

Program, unsigned short int veri türündeki bir değişkeni usi gibi çok kısa bir ifade ile tanımlama olanağı sağlar.

Yapılarla birlikte typedef ifadesini kullanabiliriz:

```c++
typedef struct {
  char cdizi1[20];
  char cdizi2[20];
  int id;
} yap;


```

Yukarıdaki satırları kullandıktan sonra, yapı ile ilgili değişkenler tanımlayabiliriz. Aşağıdaki işlem satırı yukarıdaki yapı için 2 adet farklı değişken tanımlar:

```


yap yd1, yd2;


```

Şimdi, bu özelliği bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>
#include <cstring>

using namespace std;

typedef struct {
  char cdizi1[20];
  char cdizi2[20];
  int id;
} yap;

int main(void)
{
  yap yd1, yd2;

  strcpy(yd1.cdizi1, "Bilgisayar");
  strcpy(yd1.cdizi2, "Programlama");
  yd1.id = 21;

  strcpy(yd2.cdizi1, "C++");
  strcpy(yd2.cdizi2, "Programlama");
  yd2.id = 34;

  cout << yd1.cdizi1 << " " << yd1.cdizi2 << " " << yd1.id << "\n";
  cout << yd2.cdizi1 << " " << yd2.cdizi2 << " " << yd2.id;

  return 0;
}


```

Yukarıdaki örnekte, program aşağıdaki satırları ekrana yazar:

```

Bilgisayar Programlama 21
C++ Programlama 34

```

Program, bir yapı ve bu yapı ile bağlantılı 2 adet değişken bildirimi yapar. Değişkenler yoluyla yapı elemanlarına atadığı değerleri ekrana yazar.

Yukarıda bahsettiğimiz yöntemi kullanarak, bir yapı için bir işaretçi bildirimi de yapabiliriz. Bu özelliği bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>
#include <cstring>

using namespace std;

typedef struct {
  char cdizi1[20];
  char cdizi2[20];
  int id;
} yap;

int main(void)
{
  yap *yp;

  yp = (yap*) new yap;

  strcpy(yp->cdizi1, "Bilgisayar");
  strcpy(yp->cdizi2, "Programlama");
  yp->id = 21;

  cout << yp->cdizi1 << " " << yp->cdizi2 << " " << yp->id;

  delete yp;

  return 0;
}


```

Yukarıdaki örnekte, program aşağıdaki satırları ekrana yazar:

```

Bilgisayar Programlama 21

```

Program, bir yapı ve bu yapı ile bağlantılı bir adet işaretçi değişken bildirimi yapar. İşaretçi yoluyla yapı elemanlarına atadığı değerleri ekrana yazar. Bir yapı boyutu için bellekte yer ayırır ve ayırdığı belleğin başlangıç adresini yp işaretçisine atar.
