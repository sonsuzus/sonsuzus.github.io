---
title:  C++ Numaralandırma (Enumeration)
author: sonsuz
date: 2023-08-10 15:53:15 +0300
categories: [Program,C++]
tags: [programlama,cpp,numaralandırma,enum]
---


C++'da, belirli int sabitlerinin bir liste halinde tanımlanan karakter dizilerine atanmasına yarayan numaralandırma kavramının genel yapısı aşağıda gösterilmektedir:

```


enum etiket-adı {liste} değişken-listesi;


```

etiket-adı veya değişken-listesi ifadelerinden biri isteğe bağlı olarak tanımlanır. etiket-adı ifadesi numaralandırma işleminin adını gösterir. Numaralandırma değişkenleri sadece numaralandırma bildirimi içinde yer alan değerleri içerebilir. Bu özelliği aşağıdaki satır ile incelemeye çalışalım:

```c++
enum renk { mavi, turuncu, mor, siyah } e;


```

Yukarıdaki satırda, e değişkenine sadece mavi, turuncu, mor ve siyah değerleri verilebilir. Normal olarak derleyici listedeki sabitlere en soldan başlamak suretiyle birer değer artırarak int değerler atar. En solda yer alan değere 0'dan başlayarak numara verilir. Yani burada mavi'ye 0, turuncu'ya 1, mor'a 2 ve siyah'a 3 değeri verilir. Numaralandırma yöntemi ile elde edilen değerler #define direktifi kullanarak da elde edilebilir:

```c++
#define mavi 0
#define turuncu 1
#define mor 2
#define siyah 3


```

Listedeki kelimelere istediğimiz değerleri verebiliriz.

```c++
enum renk { mavi=3, turuncu, mor=7, siyah } e1;


```

Yukarıdaki satırda, mavi'ye 3, turuncu'ya 4, mor'a 7 ve siyah'a 8 değeri verilir.

Numaralandırma bir kez tanımlandıktan sonra programın herhangi bir yerinde e1 dışında bir değişken tanımlayabiliriz:

```


enum renk e2


```

Şimdi, numaralandırma kavramını örneklerle incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

enum renk { mavi, turuncu, mor };

int main(void)
{
  enum renk e1, e2, e3;

  e1 = mavi;
  e2 = turuncu;
  e3 = mor;

  cout << e1 << " " << e2 << " " << e3 << "\n";
  cout << mavi << " " << turuncu << " " << mor;

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

0 1 2
0 1 2

```

Program, renk çeşitlerini içeren 3 elemanlı ve renk adında bir numaralandırma bildirimi yapar. Bildirimden sonra tanımladığı e1, e2 ve e3 adlı numaralandırma değişkenlerine sıra ile numaralandırma elemanlarının değerlerini atar. Listede yer alan değerleri hem direk olarak hem de değişkenler yoluyla ekrana yazar.

Örnek

```c++
#include <iostream>

using namespace std;

enum renk {mavi=7, turuncu, mor=12};

int main(void)
{
  enum renk e1, e2, e3;

  e1 = mavi;
  e2 = turuncu;
  e3 = mor;

  cout << e1 << " " << e2 << " " << e3 << "\n";
  cout << mavi << " " << turuncu << " " << mor;

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

7 8 12
7 8 12

```

Program, bir önceki programın yaptığı işlemin aynısını gerçekleştirir. Tek farkı, numaralandırma elemanlarına verilen değerlerin otomatik olarak değil bildirim esnasında verilmiş olmasıdır.

Örnek

```c++
#include <iostream>

using namespace std;

enum meyve { Karpuz, Kavun, Kiraz, Erik } e;

int main(void)
{
  int option;

  cout << "Bir sayı giriniz[0-3]: ";
  cin >> option;

  e = static_cast<meyve>(option);

  switch (e) {
    case Karpuz:
         cout << "Karpuz";
         break;
    case Kiraz:
         cout << "Kiraz";
         break;
    case Erik:
         cout << "Erik";
         break;
    case Kavun:
         cout << "Kavun";
  }

  return 0;
}


```

Program, girilen sabit bir değerin atandığı numaralandırma elemanının adını ekrana yazar.
