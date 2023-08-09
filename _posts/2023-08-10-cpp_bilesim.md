---
title:  C++ Bileşimler (Unions)
author: sonsuz
date: 2023-08-10 02:01:01 +0300
categories: [Program,C++]
tags: [cpp,bileşim,programlama,unions]
---


Bileşim, iki veya daha fazla değişken tarafından ortaklaşa kullanılan tek bir bellek birimidir. Burada bahsi geçen değişkenler farklı veri türünden olabilir. Ancak, aynı bellek bölgesini paylaşan değişkenlerden sadece bir tanesi aynı anda bellek bölgesini kullanabilir. Genel görünüşü ile yapılara benzeyen bileşimlerin genel yapısı aşağıdaki gösterilmektedir:

```c++
union adı {
   veri-türü eleman1;
   veri-türü eleman2;
   .
   .
   .
   veri-türü elemanN;
} değişken-listesi;


```

Yukarıda görülen union kelimesi bir bileşim tanımlar. adı ifadesi ise bileşimin adını göstermektedir. veri-türü ifadesi C++'da kullanılan herhangi bir veri türünü gösterir. değişken-listesi bileşim için tanımlanan değişken değerleri göstermektedir. adı veya değişken-listesi ifadelerinden birinin mutlaka tanımlanması gerekir.

> Bileşimin elemanlarına işlem yapmak için, yapı kavramında olduğu gibi, . veya -> işaretlerinden birini kullanabiliriz.
{: .prompt-tip }

Bir bileşim içinde farklı veri türünden değişkenler tanımladığımızda, program bileşimdeki en büyük değişken veri türü değeri kadar bellekte yer ayırır. Örneğin, aşağıdaki bileşim tanımlaması bellekte 8 byte'lık bir yer ayırır. Sadece bir int değer ataması yapsak bile bileşim 8 byte'lık bir bellek alanı işgal eder. Ancak, int değer söz konusu bellek alanının ilk 4 byte'ını kullanır (32 bit bilgisayarlar için):

```c++
union bir {
   int id;
   char cd;
   double dd;
};


```

> Yapı içinde yer alan her bir eleman yapı boyutuna kendi boyutu kadar ekleme yapar. Ancak, bileşim içindeki elemanlar bileşim boyutuna ekleme yazmaz. Bileşimin boyutu, bileşim içinde yer alan en büyük boyuta sahip eleman boyutuna eşittir.
{: .prompt-tip }

Şimdi, öğrendiklerimizi örnekler üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

union bir {
  int id;
  double dd;
  char cd;
} bd;

int main(void)
{
  bd.id = 21;
  bd.cd = 'A';

  cout << bd.id << " " << bd.cd << "\n"; // 1

  bd.id = 127;
  cout << bd.id << " " << bd.cd << "\n"; // 2

  bd.dd = 34.75;
  cout << bd.id << " " << bd.dd;         // 3

  return 0;
}


```

Program, 1 sayısı ile gösterilen işlem satırında bir bileşiminde yer alan cd değişkeninin, 2 sayısı ile gösterilen işlem satırında id değişkeninin ve 3 sayısı ile gösterilen işlem satırında dd değişkeninin değerini normal olarak ekrana yazar. Aynı işlem satırlarında bahsi geçen değişkenler dışında kalan değerleri istendiği şekilde ekrana yazmaz, çünkü aynı bileşim içinde yer alan değişkenlerden aynı anda sadece bir tanesi ayrılan bellek bölgesini kullanabilir. Bu nedenle, sadece en son olarak atama yapılan bileşim değişkeni ekrana normal olarak yazılabilir.

Örnek

```c++
#include <iostream>

using namespace std;

struct yap {
  int id1;
  int id2;
  int id3;
  double dd;
  char cd1;
  char cd2;
  char cd3;
} yd;

union bir {
  int id1;
  int id2;
  int id3;
  double dd;
  char cd1;
  char cd2;
  char cd3;
} bd;

int main(void)
{
  cout << "Yapı boyutu: " << sizeof(yd) << "\n";

  cout << "Bileşim boyutu: " << sizeof(bd);

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Yapı boyutu: 32
Bileşim boyutu: 8

```

Program, aynı veri türlerinden ve aynı sayıda elemana sahip birer adet yapı ve bileşim tanımlar. Yapı ve bileşim boyutlarını ekrana yazar. Aynı elemanlara sahip olmalarına rağmen yapıya eklenen elemanların yapı boyutunu artırdığı, bileşim elemanlarının ise sadece en büyük olanının bileşim boyutunu belirlediği görülür.

Örnek

```c++
#include <iostream>

using namespace std;

void fonk1(char cd);
char fonk2(char cd1);

int main(void)
{
  char cd1 = 87; // 'W' = 01010111
  char cd2;

  cout << "Karakter değeri: " << cd1 << " " << (int)cd1 << " ";
  fonk1(cd1);
  cd2 = fonk2(cd1);
  cout << "Karakter değeri: " << cd2 << " " << (int)cd2 << " "; // 'u' = 01110101
  fonk1(cd2);

  return 0;
}

void fonk1(char cd)
{
  int id;

  for (id=128; id>0; id/=2) {
       if (cd&id) cout << "1 ";
       else cout << "0 ";
  }
  cout << "\n";
}

char fonk2(char cd1)
{
  struct yap1 {
    char cd1:4;
    char cd2:4;
  };

  union bir1 {
    char cd1;
    struct yap1 yd1;
  } bd1;

  char cd2;

  bd1.cd1 = cd1;             // 1

  cd2 = bd1.yd1.cd1;         // 2
  bd1.yd1.cd1 = bd1.yd1.cd2; // 3
  bd1.yd1.cd2 = cd2;         // 4

  return bd1.cd1;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Karakter değeri: W 87 0 1 0 1 0 1 1 1 
Karakter değeri: u 117 0 1 1 1 0 1 0 1 

```

Program, char bir değişkene atadığı 'W' değerini karakter, onluk sayı sistemi ve ikili sayı sisteminde sayı olarak ekrana yazar. Sonra, fonk2() fonksiyonu yoluyla değişkenin ilk 4 bit'ini son 4 bit'i ile değiştirerek elde edilen 'u' değerini aynı şekilde tekrar ekrana yazar.

fonk2() fonksiyonu içinde her işlem satırında yapılan değişken değerleri aktarım işlemleri aşağıdaki şekilde gösterilmektedir. fonk2() fonksiyonu içindeki cd2 değişkeni geçici veri depolama değişkeni olarak kullanılmaktadır.

![](cprog/union01.png)
 