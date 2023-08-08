---
title:  C++ İşlemciler
author: sonsuz
date: 2023-08-07 14:13:13 +0300
categories: [Program,C++]
tags: [programlama,cpp,işlem,işlemci,operatör,bit,atama]
---


İfade kavramının işlem yapan parçası olarak ifade edebileceğimiz işlemciler, ifade içinde yer alan değişken ve sabitlere işlem yaparlar. Belli gruplar altında sınıflandırabileceğimiz işlemcileri sıra ile incelemeye çalışalım:

## Aritmetik işlemciler

C++ dilinde kullanılan 5 adet aritmetik işlemci aşağıda gösterilmektedir. İşlemciler öncelik sırasına göre sıralanmıştır:

C++ ilişkisel işlemcileri

| İşlemci | Kullanma amacı |
| + | Toplama |
| - | Çıkarma |
| \* | Çarpma |
| / | Bölme |
| % | Bölme işleminde kalanı verme |

C++'da, işlemciler arasında öncelik sırası adı verilen bir kural vardır. İşlemci önceliği kavramının matematik derslerinde gördüğümüz konudan hiçbir farkı yoktur. Buna göre, eğer bir işlem satırında birden fazla işlemci kullanırsak, C++ işlemcilere öncelik sırasına göre işlem yapar. Bu şekilde işlem yapılınca, programlar bizim düşündüğünüzden farklı sonuçlar verebilir. Bazı işlemlerin önceliğini normal kuralların dışında belirlemek istediğimizde, işlemi parantez içine almak yeterlidir.

> % işlemcisi dışında kalan bütün aritmetik işlemcilerini temel veri türlerinin tamamı ile birlikte kullanabiliiz. % işlemcisi ise bölme işleminin kalanını verdiğinden sadece int veri türü ile kullanılabilir.
{: .prompt-tip }

\- işlemcisini hem çıkarma işlemi, hem de sayıların negatif değerlerini göstermek için kullanabiliriz.

Şimdi, örneklerle öğrendiklerimizi incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

int main(void)
{
  int id1, id2, id3;

  id1 = 15 + 4 * 3;    // Önce çarpma işlemi yapılır.
  id2 = (15 + 4) * 3;  // Önce toplama işlemi yapılır.

  id3 = 15 % 4;        // Bölme işleminin kalanı elde edilir.

  cout << "id1 değişken değeri: " << id1 << "\n";
  cout << "id2 değişken değeri: " << id2 << "\n";
  cout << "id3 değişken değeri: " << id3 << "\n";

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

id1 değişken değeri: 27
id2 değişken değeri: 57
id3 değişken değeri: 3

```

Program ilk satırda, \* işlemcisine öncelik verdiğinden, önce 4 ile 3 sayısını çarpar, sonra elde edilen sonucu 15 sayısı ile toplayarak 27 sayısı elde eder. İkinci satırda ise parantez kullanarak işlemci önceliğini toplama işlemine verir. Önce 15 ile 4 sayısını toplar, sonra elde edilen sonucu 3 sayısı ile çarparak 57 sayısını elde eder. Üçüncü işlem satırında ise bir bölme işleminin kalan değerini elde eder. Sonuçları içeren her üç değişken değeri ekrana yazar.

Örnek

```c++
#include <iostream>

using namespace std;

int main(void)
{
  int id1, id2;

  id1 = 21;
  id2 = 7;

  cout << id1+id2 << " " << id1-id2 << " " << id1*id2-2 << " " << id1*(id2-2);

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

28 14 145 105

```

Program, farklı değerlerle yapılan işlemlerin sonuçlarını ekrana yazar. cout satırında kullanılan son iki değer aynı ifadeleri içerdiği halde, işlemci önceliği kuralı parantezlerle değiştirildiği için, ekrana farklı değerler yazar.

Örnek

```c++
#include <iostream>

using namespace std;

int main(void)
{
  int id1, id2, id3, id4;

  id1 = 36 * 5 / 3;
  id2 = 49 % 2;
  id3 = id1 + id2 * 2 ;
  id4 = id3 * 2 - 20;

  cout << 36 * 5 / 3 << " " << 49 % 2 << " ";
  cout << (36 * 5 / 3) + (49 % 2) * 2 << " " << ((36 * 5 / 3) + (49 % 2) * 2) * 2 - 20 << "\n";

  cout << id1 << " " << id2 << " " << id3 << " " << id4;

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

60 1 62 104
60 1 62 104

```

Program, yaptığı işlemlerin sonucunu 4 farklı değişkene atar, önce direk olarak sabitleri kullanarak sonra direk değişken tanımlamalarını kullanarak değişken değerlerini ekrana yazar.

## İlişkisel İşlemciler

C++'da kullanılan 6 adet ilişkisel işlemci öncelik sırasına göre aşağıda gösterilmektedir:

C++ ilişkisel işlemcileri

| İşlemci | Kullanma amacı |
| < | Küçüktür |
| <= | Küçüktür veya eşittir |
| > | Büyüktür |
| >= | Büyüktür veya eşittir |
| == | Eşittir |
| != | Eşit değildir |

İlişkisel işlemciler bir sabit, değişken veya ifadeden oluşan iki değeri karşılaştırdıktan sonra doğru veya yanlış bir sonuç verir. Doğru olarak verilen değer 1, yanlış olarak verilen değer ise 0'dır.

Şimdi, ilişkisel işlemcilerin kullanılmasını örnekler üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

int main(void)
{
  int id1, id2, id3, id4;

  id1 = 21;
  id2 = 35;

  id3 = id1 > id2;
  id4 = id2 > id1;

  cout << "id3 değişken değeri: " << id3 << "\n";
  cout << "id4 değişken değeri: " << id4;

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

id3 değişken değeri: 0
id4 değişken değeri: 1

```

Program, bildirimini yaptığı id1 ve id2 adlı iki adet int değişkene birer sabit değer atar. Değişkenlere uyguladığı ilişkisel işlemci sonuçlarını id3 ve id4 adlı int değişkenlere atadıktan sonra ekrana yazar.

Örnek

```c++
#include <iostream>

using namespace std;

int main(void)
{
  int id1, id2;

  id1 = 254;
  id2 = 1029;

  cout << (id1<id2) << " " << (id1>id2) << " " << (id1<=id2) << "\n";
  cout << (id1>=id2) << " " << (id1==id2) << " " << (id1!=id2);

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

1 0 1
0 0 1

```

Program, bildirimini yaptığı iki adet int değişkene birer sabit değer atar. Değişkenlere uyguladığı ilişkisel işlemci sonuçlarını ekrana yazar.

## Mantıksal işlemciler

C++'da kullanılan 3 adet mantıksal işlemci öncelik sırasına göre aşağıda gösterilmektedir:

C++ mantıksal işlemcileri

| İşlemci | Kullanma amacı |
| ! | NOT |
| && | AND |
| \|\| | OR |

Burada göreceğimiz mantıksal işlemciler de matematik derslerinden hatırlayacağımız gibi, doğru veya yanlış sonuç veren ifadeler arasında işlem yapan işlemcilerdir. Doğru ve yanlış ifade ile kastedilen sırasıyla 1 ve 0 değerleridir. Mantıksal işlemciler doğru ve/veya yanlış sonuçları birleştirip tek bir sonuç verirler. Genellikle ilişkisel işlemcilerle birlikte kullanılan mantıksal işlemciler AND, OR ve NOT ile ilgili mantıksal işlemlerin yerine getirilmesini sağlarlar. Doğru ifadeler için 1, yanlış ifadeler için 0 değeri kullanılarak oluşturulmuş mantıksal işlemci tablosu aşağıdadır:

```


x   y     x && y    x || y     !x

0   0        0         0        1
0   1        0         1        1
1   1        1         1        0
1   0        0         1        0


```

Yukarıdaki tabloda gösterilen x ve y ifadeleri, sabit, değişken veya ifadelerden oluşan iki adet değerin ilişkisel işlemcilerle yapılan işlemin sonucunda elde edilen sonuçları gösterir.

Şimdi, öğrendiklerimizi örnekler üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

int main(void)
{
  int id1, id2;
  id1 = 46;
  id2 = 138;

  // İlişkisel işlemci kullanımı
  cout << (id1==id2) << " " << (id1>id2) << " " << (id1<id2) << " " << (id1!=id2) << "\n";

  // İlişkisel ve mantıksal işlemcilerin birlikte kullanımı
  cout << ((id1<id2) && (id1!=id2)) << " " << ((id1<id2) || (id1!=id2)) << "\n";
  cout << ((id1>id2) && (id1!=id2)) << " " << ((id1>id2) || (id1==id2));

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

0 0 1 1
1 1
0 0

```

Program farklı değerler atadığı 2 adet int değişken arasında yaptığı karşılaştırmaları ve bu karşılama sonuçları ile yaptığı mantıksal işlem sonuçlarını ekrana yazar. İlişkisel işlemciler öncelikli işlem gördüğünden birinci safha sonunda aşağıdaki değerler elde edilir. Daha sonra, devreye giren mantıksal işlemciler ile elde edilen sonuç ekrana yazılır.

```c++
cout << ((id1<id2) && (id1!=id2)) << " " << ((id1<id2) || (id1!=id2)) << "\n";

1 && 1, 1 || 1 // İlişkisel işlemler sonucu (İlk safha)
1 1            // Mantıksal işlemler sonucu (İkinci safha)

cout << ((id1>id2) && (id1!=id2)) << " " << ((id1>id2) || (id1==id2));

0 && 1, 0 || 0 // İlişkisel işlemler sonucu (İlk safha)
0 0            // Mantıksal işlemler sonucu (İkinci safha)


```

Programda, önce ilişkisel sonra mantıksal işlemcilerle yapılan uygulamaların detaylı şeması aşağıdadır:

![](cprog/islemci01.png)

Aynı programı değişken karşılaştırmalarını da farklı değişkenlere atayarak tekrar yazalım:

Örnek

```c++
#include <iostream>

using namespace std;

int main(void)
{
  int id1, id2;
  int id3, id4, id5, id6;
  id1 = 46;
  id2 = 138;

  // İlişkisel işlemci kullanımı
  id3 = id1==id2;    // 0
  id4 = id1>id2;     // 0
  id5 = id1<id2;     // 1
  id6 = id1!=id2;    // 1

  cout << id3 << " " << id4 << " " << id5 << " " << id6 << "\n";

  // İlişkisel ve mantıksal işlemcilerin birlikte kullanımı
  //        1      1               1      1
  cout << (id5 && id6) << " " << (id5 || id6) << "\n";
  //        0      1               0      0
  cout << (id4 && id6) << " " << (id4 || id3);

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

0 0 1 1
1 1
0 0

```

Program farklı değerler atadığı 2 adet int değişken arasında yaptığı karşılaştırmaları ve bu karşılama sonuçları ile yaptığı mantıksal işlem sonuçlarını ekrana yazar. İlişkisel işlemcilerle yapılan sonuçlar int veri türünden değişkenlere atandıktan sonra mantıksal işlemler yapılır ve elde edilen sonuç ekrana yazılır.

Mantıksal işlemcilerin normal öncelik sırası parantezler tarafından değiştirilebilir.

Örnek

```c++
#include <iostream>

using namespace std;

int main(void)
{
  int id1, id2, id3;

  id1 = 1;
  id2 = 0;

  id3 = (!id1 || id1) && (!id2 || id1);

  cout << "id3 değişken değeri: " << id3 << "\n";

  id3 = (!id1 || id1) && (!(id2 || id1));

  cout << "id3 değişken değeri: " << id3;

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

id3 değişken değeri: 1
id3 değişken değeri: 0

```

Yukarıdaki örnekte, program parantez kullanımından dolayı elde edilen farklı sonuçları ekrana yazar.

İlişkisel işlemciler bir sabit, değişken veya ifadeden oluşan iki değeri karşılaştırdıktan sonra doğru (1) veya yanlış (0) bir sonuç verir.

Mantıksal işlemciler ise, doğru (1) veya yanlış (0) sonuç veren ifadeler arasında işlem yapan işlemcilerdir.

## Bit işlemcileri

C'de bit seviyesinde işlem yapan 4 adet özel işlemci vardır:

& AND

\| OR

^ XOR

~ 1'in tamamlayanı

Bu işlemciler sadece char ve int veri türünden olan değerlerle kullanılabilir.

İşlem yapılan değerlerin karşılıklı gelen bit'leri karşılıklı işleme tabi tutulur.

& : Eğer, karşılıklı gelen her iki bit 1 ise, sonuç bit bölümüne 1 yazılarak sonuç değeri elde edilir.

\| : Eğer karşılıklı gelen bit'lerden en az bir tanesi 1 ise, sonuç bit bölümüne 1, aksi takdirde 0 yazılarak sonuç değeri elde edilir.

^ : Eğer karşılıklı gelen bit'lerden her ikisi de aynı değeri taşıyorsa, sonuç bit bölümüne 0, aksi takdirde 1 yazılarak sonuç değeri elde edilir.

~ : Tek değere işlem yapar. int veya char bir değer içindeki bütün bit değerlerini tersine çevirir (1 ise 0, 0 ise 1 yapar).

Şimdi, bit işlemcilerinin kullanılmasını örnekler üzerinde incelemeye çalışalım:

Aşağıdaki örnekte, program iki adet int değer arasında bit işlemcileri ile işlem yaparak sonuçları ekrana yazar.

Örnek

```c++
#include <iostream>

using namespace std;

int main(void)
{
  unsigned short int usid1 = 83;  // 83  = 00000000 01010011
  unsigned short int usid2 = 165; // 165 = 00000000 10100101

  cout << "& işlemi sonucu: " << (usid1 & usid2) << "\n"; // 1 = 00000000 00000001
  cout << "| işlemi sonucu: " << (usid1 | usid2) << "\n"; // 247 = 00000000 11110111
  cout << "^ işlemi sonucu: " << (usid1 ^ usid2) << "\n"; // 246 = 00000000 11110110
  // -84 = 11111111 10101100 -166 = 11111111 01011010
  cout << "~ işlemi sonucu: " << (~usid1) << " " << (~usid2);

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

& işlemi sonucu: 1
| işlemi sonucu: 247
^ işlemi sonucu: 246
~ işlemi sonucu: -84 -166

```

Program ile yapılan işlemleri bit seviyesinde gösteren karşılaştırma bilgileri aşağıdaki tabloda yer almaktadır.

```

  01010011   83     01010011   83     01010011   83
  10100101  165     10100101  165     10100101  165
&                 |                 ^
----------------  ----------------  ----------------
  00000001    1     11110111  247     11110110  246

```

Şimdi, bit işlemcilerini kullanarak short int bir değerin ikili sayı sisteminde yazılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

int main(void)
{
  unsigned short usi = 34651; // 1000011101011011
  unsigned short usimask; // 1000000000000000 (16 bit -> 32768) 

  cout << "usi değişken değerinin ikili sayı sisteminde yazılışı: ";

  for (usimask=32768; usimask>0; usimask/=2) {
       cout << ((usi & usimask) ? '1' : '0');
  }

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

usi değişken değerinin ikili sayı sisteminde yazılışı: 1000011101011011

```

Program, 34651 değerini içeren 16 bit'lik unsigned short int bir değişken içeriğini ikili sayı sisteminde yazdırmak amacıyla, bu değişken değerini en solda yer alan bit değerinden başlayarak birer birer kontrol eder. Değişkenin konrol edilen bit değerine karşılık gelen bit değeri 1, diğer basamak değerleri 0 olan sayılarla bu kontrolü yapar. Sadece en soldaki bit değeri 1 olan 32768 sayısı ile kontrol başlar. Her defasında bit değeri bir sağa kayacak şekilde, değişken değeri ile sayısal değeri & işlemcisi ile karşılaştırarak, elde edilen değeri ekrana yazar.

Programın karşılaştırma işlemini gösteren tablo aşağıdadır:

```

                          3465                           Karşılaştırılan değer          Elde edilen değer

1.safha     1 0 0 0 0 1 1 1 0 1 0 1 1 0 1 1    1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 (32768)   1
2.safha     1 0 0 0 0 1 1 1 0 1 0 1 1 0 1 1    0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 (16384)   0
3.safha     1 0 0 0 0 1 1 1 0 1 0 1 1 0 1 1    0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 ( 8192)   0
4.safha     1 0 0 0 0 1 1 1 0 1 0 1 1 0 1 1    0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 ( 4096)   0
5.safha     1 0 0 0 0 1 1 1 0 1 0 1 1 0 1 1    0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 ( 2048)   0
6.safha     1 0 0 0 0 1 1 1 0 1 0 1 1 0 1 1    0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 ( 1024)   1
7.safha     1 0 0 0 0 1 1 1 0 1 0 1 1 0 1 1    0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 (  512)   1
8.safha     1 0 0 0 0 1 1 1 0 1 0 1 1 0 1 1    0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 (  256)   1
9.safha     1 0 0 0 0 1 1 1 0 1 0 1 1 0 1 1    0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 (  128)   0
10.safha    1 0 0 0 0 1 1 1 0 1 0 1 1 0 1 1    0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 (   64)   1
11.safha    1 0 0 0 0 1 1 1 0 1 0 1 1 0 1 1    0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 (   32)   0
12.safha    1 0 0 0 0 1 1 1 0 1 0 1 1 0 1 1    0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 (   16)   1
13.safha    1 0 0 0 0 1 1 1 0 1 0 1 1 0 1 1    0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 (    8)   1
14.safha    1 0 0 0 0 1 1 1 0 1 0 1 1 0 1 1    0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 (    4)   0
15.safha    1 0 0 0 0 1 1 1 0 1 0 1 1 0 1 1    0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 (    2)   1
16.safha    1 0 0 0 0 1 1 1 0 1 0 1 1 0 1 1    0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 (    1)   1

```

Eğer karşılaştırılan sayının 1 değeri taşıyan hanesine karşılık gelen 34651 değerinin hanesi 1 değeri taşıyorsa program 1, aksi takdirde 0 değerini ekrana yazar.

Önce, aşağıdaki iki değeri & işlemcisi ile karşılaştırır:

```

  1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0  (32768) usimask değişken değeri   
  1 0 0 0 0 1 1 1 0 1 0 1 1 0 1 1  (34651) usi değişken değeri
&
---------------------------------
  1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

```

Elde ettiği sonuç 0'dan büyük olduğundan, koşul doğru sonuç verir ve 1 değerini ekrana yazar:

1 . . . . . . . . . . . . . . .

İkinci safhada ise aşağıdaki iki değeri karşılaştırır:

```

  0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0  (16384) usimask değişken değeri   
  1 0 0 0 0 1 1 1 0 1 0 1 1 0 1 1  (34651) usi değişken değeri
&
---------------------------------
  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

```

Elde ettiği sonuç 0'dan büyük olduğundan, koşul doğru sonuç verir ve 0 değerini ekrana yazar:

1 0 . . . . . . . . . . . . . .

Bu şekilde devam eden program sonuç olarak 34651 sayısının ikili sayı sisteminde ekrana yazar.

1 0 0 0 0 1 1 1 0 1 0 1 1 0 1 1

Eğer iki değişken değeri arasında ^ bit işlemcisi ile işlem yaptıktan sonra, işlem sonucunda elde edilen değerle ikinci değişken arasında aynı işlem tekrarlarsak, ilk değişken değerini elde ederiz. Farklı bir ifade ile, bir sayı ile başka bir sayı arasında iki kez üst üste ^ işlemi uyguladığımızda, ilk sayı değerini elde ederiz. Bir örnekle incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

void IntToBin(short int val)
{
  unsigned short usimask; // 1000000000000000 (16 bit -> 32768)

  for (usimask=32768; usimask>0; usimask/=2) {
       cout << ((val & usimask) ? '1' : '0');
  }
  cout << "\n";
}

int main(void)
{
  short int sid1 = 19287; // 1011100000110111
  short int sid2 = 28624; // 0110111111010000

  cout << "sid1 değişken değeri: ";
  IntToBin(sid1);
  cout << "sid2 değişken değeri: ";
  IntToBin(sid2);

  cout << "\n";

  sid1 = sid1 ^ sid2;

  cout << "sid1 değişken değeri: ";
  IntToBin(sid1); // 1101011111100111

  cout << "\n";

  sid1 = sid1 ^ sid2;

  cout << "sid1 değişken değeri: ";
  // sid1 değişkeni ilk değerini alıyor.
  IntToBin(sid1); // 1011100000110111

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

sid1 değişken değeri: 0100101101010111
sid2 değişken değeri: 0110111111010000

sid1 değişken değeri: 0010010010000111

sid1 değişken değeri: 0100101101010111

```

Program, sid1 ve sid2 değişkenleri arasında ^ bit işlemcisi ile işlem yaptıktan sonra, işlem sonucunda elde edilen değerle sid2 değişkeni arasında aynı işlem tekrarlandığında sid1 değişkeninin ilk değerinin elde edileceğini göstermektedir.

Şimdi, bit işlemcilerinin long int değerlerle ile kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

void IntToBin(string varname, long int val)
{
  unsigned long int ulimask; // 1000000000000000 0000000000000000  (32 bit -> 2.147.483.648)

  cout << varname << " değişken değeri: " << val << " ";

  for (ulimask=2147483648U; ulimask>0; ulimask/=2) {
       cout << ((val & ulimask) ? '1' : '0');
  }
  cout << "\n";
}

int main(void)
{
  long int lid1 = 1895548291; // 0111000011111011 1100010110000011
  long int lid2 = 1462158752; // 0101011100100110 1100010110100000
  long int lid3 = 1165324875; // 0100010101110101 0111001001001011
  long int lid4 = 1391532487; // 0101001011110001 0001100111000111

  IntToBin("lid1", lid1);
  IntToBin("lid2", lid2);
  IntToBin("lid3", lid3);
  IntToBin("lid4", lid4);

  cout << "\n";

  lid1 = lid1 & lid2;
  IntToBin("lid1", lid1);

  lid1 = lid1 | lid3;
  IntToBin("lid1", lid1);

  lid1 = lid1 ^ lid4;
  IntToBin("lid1", lid1);

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

lid1 değişken değeri: 1895548291 01110000111110111100010110000011
lid2 değişken değeri: 1462158752 01010111001001101100010110100000
lid3 değişken değeri: 1165324875 01000101011101010111001001001011
lid4 değişken değeri: 1391532487 01010010111100010001100111000111

lid1 değişken değeri: 1344456064 01010000001000101100010110000000
lid1 değişken değeri: 1433925579 01010101011101111111011111001011
lid1 değişken değeri: 126283276 00000111100001101110111000001100

```

Program, lid1, lid2, lid3 ve lid4 adlı dört aet long int değişken tanımlar ve değişkenlere birer ilk değer atar. IntToBin() fonksiyonu ile değişkenlerin değerlerini onlu ve ikili sayı sisteminde ekrana yazar. lid1 değişkeni ile lid2 değişkeni arasında & işlemcisi ile yaptığı işlemin sonucunu lid1 değişkenine atar ve lid1 değişken değerini ekrana yazar. lid1 değişkeni ile lid3 değişkeni arasında | işlemcisi ile yaptığı işlemin sonucunu lid1 değişkenine atar ve lid1 değişken değerini ekrana yazar. lid1 değişkeni ile lid4 değişkeni arasında ^ işlemcisi ile yaptığı işlemin sonucunu lid1 değişkenine atar ve lid1 değişken değerini ekrana yazar.

## Bit kaydırma işlemcileri

C++'da, bit kaydırma işlemcilerini kullanarak, char ve int değerlerin bit değerini sola veya sağa kaydırabiliriz. << ifadesi sola bit kaydırma ve >> ifadesi sağa bit kaydırma işlemcisini temsil eder. Bu işlemcilerin genel yapısı aşağıda gösterilmektedir:

değişken-adı << int-değer

değişken-adı >> int-değer

Sola kaydırma bit işlemcisini kullandığımızda, değişkenin ikili sayı sistemine göre yazılmış olan değerinde yer alan bitler << işlemcisinin sağında yer alan int değer kadar sola kayar. Bu durumda, en sağda boşalan bitlerin yerine 0 değeri gelir. Sağa kaydırma bit işlemcisi kullandığımızda ise, değişkenin ikili sayı sistemine göre yazılmış olan değerinde yer alan bitler >> işlemcisinin sağında yer alan int değer kadar sağa kayar. Bu durumda en solda boşalan bitlerin yerine 0 değeri gelir.

Bu özellikleri bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

void IntToBin(string varname, short int val)
{
  unsigned short usimask; // 1000000000000000 (16 bit -> 32768)

  cout << varname << " değişken değeri: " << val << " ";

  for (usimask=32768; usimask>0; usimask/=2) {
       cout << ((val & usimask) ? '1' : '0');
  }
  cout << "\n";
}

int main(void)
{
  short int sid1 = 17159; // 1011100000110111
  short int sid2 = 28624; // 0110111111010000

  IntToBin("sid1", sid1);
  IntToBin("sid2", sid2);

  cout << "\n";

  sid1 = sid1 << 3; // Sayının bit değerlerini 3 defa sola kaydırır.
  sid2 = sid2 >> 3; // Sayının bit değerlerini 3 defa sağa kaydırır.

  IntToBin("sid1", sid1);
  IntToBin("sid2", sid2);

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

sid1 değişken değeri: 17159 0100001100000111
sid2 değişken değeri: 28624 0110111111010000

sid1 değişken değeri: 6200 0001100000111000
sid2 değişken değeri: 3578 0000110111111010

```

Program, unsigned short int veri türünden tanımladığı sid1 ve sid2 değişkenlerine atadığı değerleri onluk ve ikili sayı sistemine göre ekrana yazar. sid1 değişkeninin bitlerini üç defa sola, sid2 değişkeninin bitlerini ise üç defa sağa kaydırdıktan sonra, değişken değerlerini tekrar onluk ve ikili sayı sistemine göre ekrana yazar. İlk kaydırma işleminde, sid1 değişkeninin en sağında yer alan bitlerin yerine ve ikinci kaydırma işleminde sid2 değişkeninin en solunda yer alan bitlerin yerine 0 değeri gelecektir.

C++'da, bir sayıyı ikiye bölmek veya ikiyle çarpmak için bit kaydırma işlemcilerini kullanabiliriz. Aşağıdaki ilk işlem satırı id değişkenini ikiye bölmemizi, ikinci işlem satırı ise iki ile çarpmamızı sağlar.

```


id = id >> 1; // id = id/2
id = id << 1; // id = id*2


```

Şimdi, bu özelliği bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

void IntToBin(string varname, short int val)
{
  unsigned short usimask; // 1000000000000000 (16 bit -> 32768)

  cout << varname << " değişken değeri: " << val << " ";

  for (usimask=32768; usimask>0; usimask/=2) {
       cout << ((val & usimask) ? '1' : '0');
  }
  cout << "\n";
}

int main(void)
{
  short int sid = 12643; // 0011000101100011

  IntToBin("sid", sid);

  IntToBin("sid", sid>>1); // Değişken değerini yarısı

  IntToBin("sid", sid<<1); // Değişken değerinin iki katı

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

sid değişken değeri: 12643 0011000101100011
sid değişken değeri: 6321 0001100010110001
sid değişken değeri: 25286 0110001011000110

```

Program, sid değişkenine atadığı değeri, >> ve << işlemcilerini kullanarak, yarısını ve iki katını alır ve aldığı değerleri ekrana yazar.

Bir sayı üzerinde uygulanan bit kaydırma işlemlerini ve elde edilen değerlerin ikili sayı sisteminde yazılmasını sağlayan bir fonksiyonu bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

void IntToBin(string varname, long int val)
{
  char cdizi[100];
  int id;

  int bitsayi = sizeof(val) * 8; // long int değerin bit adet değeri

  unsigned long int u = *(unsigned long int*)&val

  unsigned long int mask = 1 << (bitsayi-1); // 10000000 00000000 00000000 00000000 (2.147.483.648)

  cout << varname << " değişken değeri: " << val << " ";

  for (id=0; id<bitsayi; id++, mask >>= 1) {
       // Döngü değişkeninin her artışında mask değerinin en solundaki 1 değeri bir sağa kayar.
       cdizi[id] = (u & mask) ? '1' : '0';
  }
  cdizi[id] = '\0';

  cout << cdizi << "\n";
}

int main(void)
{
  long int lid = 754254958; // 00101100111101010000010001101110

  IntToBin("lid", lid);

  IntToBin("lid", lid>>1); // Değişken değerinin yarısı

  IntToBin("lid", lid<<1); // Değişken değerinin iki katı

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

lid değişken değeri: 754254958 00101100111101010000010001101110
lid değişken değeri: 377127479 00010110011110101000001000110111
lid değişken değeri: 1508509916 01011001111010100000100011011100

```

Program, long int veri türünden tanımlanmış lid değişkenine atadığı değere, >> ve << işlemcilerini kullanarak işlem yapar. Elde edilen tüm değerleri bir fonksiyon yoluyla onlu ve ikli sayı sisteminde ekrana yazar.

## Bit ve bit kaydırma işlemcilerinin birlikte kullanımı

Bit ve bit kaydırma işlemcilerinin birlikte kullanımını unsigned integer bir sayının bit değerlerini değiştirme, tersine çevirme ve değerlerini alma işlemlerini yapan bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>
#include <cstdlib>

using namespace std;

// Bit işlem fonksiyonu mode: 1 (1 değeri verme), 0 (0 değeri verme), 2 (0 ve 1 değeri arasında geçiş yapma
long int bg_bitopr(long int val, int index, int mode);
// Belirli bir sıradaki bit değerini kontrol etme
int bg_bitcheck(long int val, int index);
// Unsigned long int değeri ikili sistemde yazma
void bg_IntToBin(string varname, long int val);

int main(void)
{
  long int lid1 = 121;           // 00000000 00000000 00000000 01111001
  long int lid2;
  bg_IntToBin("lid1", lid1);

  // 1 değeri verme (Sağ taraftan başlayarak 10.sıradaki bit)
  lid2 = bg_bitopr(lid1, 10, 1); // 00000000 00000000 00000010 01111001 (633)
  bg_IntToBin("lid2", lid2);

  // 0 değeri verme (Sağ taraftan başlayarak 7.sıradaki bit)
  lid2 = bg_bitopr(lid2, 7, 0);  // 00000000 00000000 00000010 00111001 (569)
  bg_IntToBin("lid2", lid2);

  // Bit değerini tersine çevirme (Sağ taraftan başlayarak 12.sıradaki bit)
  lid2 = bg_bitopr(lid2, 12, 2); // 00000000 00000000 00001010 00111001 (2617)
  bg_IntToBin("lid2", lid2);

  // Bit değer kontrolu
  cout << "Bit değeri: " << (bg_bitcheck(lid2, 4) ? 1 : 0);

  return 0;
}

// Bit işlem fonksiyonu mode: 0 (0 değeri verme), 1 (1 değeri verme), 2 (0 ve 1 değeri arasında geçiş yapma)
long int bg_bitopr(long int val, int index, int mode)
{
  switch(mode) {
     case 0: // 0 değeri verme
          val = val & ~(1 << (index-1));
          break;
     case 1: // 1 değeri verme
          val = val | ( 1 << (index-1));
          break;
     case 2: // 0 ve 1 değeri arasında geçiş yapma
          val = val ^ (1 << (index-1));
          break;
  }

  return val;
}

// Belirli bir sıradaki bit değerini kontrol etme
int bg_bitcheck(long int val, int index)
{
  return ((val >> (index-1)) & 1);
}

void bg_IntToBin(string varname, long int val)
{
  int bitsayi = sizeof(val) * 8; // long int değerin bit adet değeri
  char *cdizi = (char*) malloc(bitsayi+1); // Dizi sonu '\0' karakteri için
  int id;

  cdizi[bitsayi] = '\0';

  unsigned long int u = *(unsigned long int*)&val

  unsigned long int mask = 1 << (bitsayi-1); // 10000000 00000000 00000000 00000000 (2.147.483.648)

  cout << varname << " değişken değeri: " << val << " ";

  for (id=0; id<bitsayi; id++, mask >>= 1) {
       // Döngü değişkeninin her artışında mask değerinin en solundaki 1 değeri bir sağa kayar.
       cdizi[id] = (u & mask) ? '1' : '0';
  }

  cout << cdizi << "\n";
  free(cdizi);
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

lid1 değişken değeri: 121 00000000000000000000000001111001
lid2 değişken değeri: 633 00000000000000000000001001111001
lid2 değişken değeri: 569 00000000000000000000001000111001
lid2 değişken değeri: 2617 00000000000000000000101000111001
Bit değeri: 1

```

Program, bg\_bitopr() fonksiyonunu 3 farklı mod ile kullanarak, unsigned integer bir sayının bit değerlerini değiştirme, tersine çevirme ve değerlerini alma işlemlerini gerçekleştirir. Fonksiyonun index parametresi işlem yapılacak bit'in sağ taraftan başlamak üzere sırasını gösterir. Fonksiyonun mode parametresi ise, 1 değeri aldığında bit'e 1 değerinin, 0 değeri aldığında bit'e 0 değerinin verileceğini, 2 değeri aldığında ise, bit değerinin tersine çevrileceğini gösterir. Herhangi bir sıradaki bit değerinin 0 veya 1 değeri aldığı bg\_bitcheck() fonksiyonu ile kontrol edilir.

## İşaretçi işlemcileri

C++ dilinde, işaretçilerle kullanılan 3 adet işlemci vardır. Bu işlemciler aşağıda yer almaktadır:

\* işlemcisi

& işlemcisi

-> işlemcisi

İşaretçiler değişkenlerin bellek adreslerini içeren değişkenler olup adresini içereceği değişkenin veri türünden tanımlı olmalıdır.

İşaretçileri kullanarak, işaretçilerin adresini içerdiği değişkenlere dolaylı yoldan işlem yapabiliriz.

İşaretçi değişkenleri, tıpkı diğer değişkenler gibi, kullanılmadan önce mutlaka tanımlanmalıdır. \* işlemcisi işaretçilerin tanımlanması işleminde kullanılır. Aşağıdaki işlem satırı işaretçi tanımlamasının genel yapısını göstermektedir:

veri-türü \*işaretçi-adı;

Yukarıdaki satırda yer alan veri-türü ifadesi C++'da kullanılan herhangi bir veri türünü, işaretçi-adı ifadesi ise işaretçi adı olarak kullanabileceğimiz herhangi bir karakter dizisini gösterir.

Aşağıdaki işlem satırı ip adlı int veri türünden bir işaretçi tanımlar:

```c++
int *ip;


```

\* işlemcisini ayrıca, işaretçilerin adreslerini içerdiği değişkenlerin değerlerine dolaylı yoldan işlem yapmak için kullanabiliriz.

Bir işaretçi tanımlaması yaptıktan sonra, işaretçi kullanabilmemiz için aynı veri türünden bir değişkenin adresini işaretçiye atamamız gerekir. Bu işlem için & işlemcisini kullanmamız gerekir. Aşağıdaki işlem satırı işaretçilere bir değişken adresi atama işleminin genel yapısını göstermektedir:

işaretçi-adı = &değişken-adı;

Yukarıdaki satırda yer alan işaretçi-adı ifadesi işaretçi adı olarak kullanabileceğimiz herhangi bir karakter dizisini, değişken-adı ifadesi ise herhangi bir değişken adını göstermektedir. Aşağıdaki ilk işlem satırı ip adlı int bir işaretçi ve id adlı int bir değişken tanımlar. İkinci işlem satırı ise id değişkeninin bellek adresini ip işaretçisine atar:

```c++
int *ip, id;
ip = &id;


```

Şimdi, işaretçi işlemcilerinin kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

int main(void)
{
  int *ip, id = 21;

  ip = &id // Değişken adresini işaretçiye atama
  cout << "id değişken değeri (değişken yoluyla): " << id << "\n";
  cout << "id değişken değeri (işaretçi yoluyla): " << *ip << "\n";
  cout << "id değişkeni bellek adresi (değişken yoluyla): " << &id << "\n";
  cout << "id değişkeni bellek adresi (işaretçi yoluyla): " << ip << "\n\n";

  *ip = 35; // id değişken değerini değiştirme (işaretçi yoluyla)
  cout << "id değişken değeri (değişken yoluyla): " << id << "\n";
  cout << "id değişken değeri (işaretçi yoluyla): " << *ip << "\n";
  cout << "id değişkeni bellek adresi (değişken yoluyla): " << &id << "\n";
  cout << "id değişkeni bellek adresi (işaretçi yoluyla): " << ip << "\n\n";

  (*ip)++;  // id değişken değerini değiştirme (işaretçi yoluyla)
  cout << "id değişken değeri (değişken yoluyla): " << id << "\n";
  cout << "id değişken değeri (işaretçi yoluyla): " << *ip << "\n";
  cout << "id değişkeni bellek adresi (değişken yoluyla): " << &id << "\n";
  cout << "id değişkeni bellek adresi (işaretçi yoluyla): " << ip << "\n\n";

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

id değişken değeri (değişken yoluyla): 21
id değişken değeri (işaretçi yoluyla): 21
id değişkeni bellek adresi (değişken yoluyla): 0x6dfee8
id değişkeni bellek adresi (işaretçi yoluyla): 0x6dfee8

id değişken değeri (değişken yoluyla): 35
id değişken değeri (işaretçi yoluyla): 35
id değişkeni bellek adresi (değişken yoluyla): 0x6dfee8
id değişkeni bellek adresi (işaretçi yoluyla): 0x6dfee8

id değişken değeri (değişken yoluyla): 36
id değişken değeri (işaretçi yoluyla): 36
id değişkeni bellek adresi (değişken yoluyla): 0x6dfee8
id değişkeni bellek adresi (işaretçi yoluyla): 0x6dfee8

```

Program, önce ip adlı int bir işaretçi ve, 21 değerini ilk değer olarak vererek, id adlı int bir değişken tanımlar. id değişken adresini ip işaretçisine atar. id değişken değerini, değişken adını kullanarak doğrudan ve işaretçi adını \* işlemcisi ile kullanarak dolaylı olarak ekrana yazar. Sonra, id değişken adresini, değişken adını & işlemcisi ile kullanarak ve işaretçi adını kullanarak ekrana yazar. Aynı işlemleri, id değişken değerine işaretçi yoluyla 35 olarak değiştirdikten ve bir değer artırdıktan sonra, tekrarlar. Ekrana yazılan bellek adres değerleri her bilgisayarda farklı olacaktır.

C++'da, -> işlemcisi yapı ve sınıflarla birlikte kullanılmaktadır. Farklı veri türlerinin tek bir isim altında toplandığı yapılar veya farklı veri türleri ile bu veri türlerine işlem yapan fonksiyonların tek bir isim altında toplandığı sınıflar için bir işaretçi tanımlandığı zaman, bu yapı veya sınıf işaretçileri yoluyla, yapı veya sınıf nesne (değişken) adresleri işaretçiye atandıktan sonra, yapı veya sınıfın her bir elemanına ayrı ayrı ulaşabiliriz. İşaretçi yoluyla yapı veya sınıf elemanlarına erşim sağlamak için -> işlemcisi kullanılır.

Şimdi, işaretçi işlemcilerini yapılar ile kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

struct yap {
  int id;
  char cd;
};

int main(void)
{
  struct yap *yp, yd1, yd2;

  yp = &yd1
  yp->id = 21;
  yp->cd = 'A';

  yp = &yd2
  yp->id = 35;
  yp->cd = 'B';

  cout << "yd1 yapı değişkeni id değeri: " << yd1.id << "\n";
  cout << "yd1 yapı değişkeni cd değeri: " << yd1.cd << "\n\n";

  cout << "yd2 yapı değişkeni id değeri: " << yd2.id << "\n";
  cout << "yd2 yapı değişkeni cd değeri: " << yd2.cd;

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

yd1 yapı değişkeni id değeri: 21
yd1 yapı değişkeni cd değeri: A

yd2 yapı değişkeni id değeri: 35
yd2 yapı değişkeni cd değeri: B

```

Program, önce bir adet int ve bir adet char değişken içeren yap adlı bir yapı tanımlar. Sonra, bu yapı türünden yp adlı bir işaretçi ile yd1 ve yd2 adlı iki adet değişken bildirimi yapar. yd1 değişkeninin bellek adresini yp işaretçisine atar. İşaretçi yoluyla yd1 yapı kopyasındaki id değişkenine 21 sayısını ve cd değişkenine 'A' karakterini atar. yd2 değişkeninin bellek adresini yp işaretçisine atar. İşaretçi yoluyla yd2 yapı kopyasındaki id değişkenine 35 sayısını ve cd değişkenine 'B' karakterini atar. Son olarak, yapı değişkenleri yoluyla tüm değerleri ekrana yazar.

Şimdi, işaretçi işlemcilerinin sınıflarla kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

class sinif {
  private:
    int priid;
  public:
    int pubid;
    sinif(int pid1, int pid2)
    {
      priid=pid1;
      pubid=pid2;
    };
    void deger_goster()
    {
      cout << "priid değişken değeri: " << priid << "\n";
      cout << "pubid değişken değeri: " << pubid << "\n";
    }
};

int main(void)
{
  sinif *pnes, nes1(7, 21), nes2(35, 64);

  pnes = &nes1
  pnes->deger_goster();

  pnes = &nes2
  pnes->deger_goster();

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

priid değişken değeri: 7
pubid değişken değeri: 21
priid değişken değeri: 35
pubid değişken değeri: 64

```

Program, önce bir adet priid adlı private int ve bir adet pubid adlı public int değişken ile bu değişkenlere ilk değer atama işlemi yapan bir constructor fonksiyonu ve bu değişken değerlerini ekranda gösteren deger\_goster() adlı bir fonksiyon içeren bir sınıf bildirimi yapar. Sonra, bu sınıf türünden pnes adlı bir işaretçi ile nes1 ve nes2 adlı iki adet nesne bildirimi yapar. nes1 değişkeninin bellek adresini pnes işaretçisine atar. İşaretçi yoluyla deger\_goster() fonksiyonunu çağırarak, nes1 sınıf kopyasındaki değişkenlerin değerlerini ekrana yazar. nes2 değişkeninin bellek adresini pnes işaretçisine atar. İşaretçi yoluyla deger\_goster() fonksiyonunu çağırarak, nes2 sınıf kopyasındaki değişkenlerin değerlerini ekrana yazar.

## . işlemcisi

. işlemcisi de tıpkı -> işlemcisi gibi yapı ve sınıflarla birlikte kullanılır. Bir yapı veya sınıf için bir değişken tanımladığımızda . işlemcisini, bir işaretçi tanımladığımızda ise, aynı yapı veya sınıf için tanımlanan değişken bellek adresini işaretçiye atadıktan sonra, -> işlemcisini, kullanmamız gerekir. Bu işlemci ile yapının veya sınıfın her bir elemanına ayrı ayrı ulaşabiliriz.

Şimdi, . işlemcisinin yapılar ile kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

struct yap {
  int id;
  char cd;
};

int main(void)
{
  struct yap yd1, yd2;

  yd1.id = 165;
  yd1.cd = 'K';

  yd2.id = 384;
  yd2.cd = 'T';

  cout << "yd1 yapı değişkeni id değeri: " << yd1.id << "\n";
  cout << "yd1 yapı değişkeni cd değeri: " << yd1.cd << "\n\n";

  cout << "yd2 yapı değişkeni id değeri: " << yd2.id << "\n";
  cout << "yd2 yapı değişkeni cd değeri: " << yd2.cd;

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

yd1 yapı değişkeni id değeri: 165
yd1 yapı değişkeni cd değeri: K

yd2 yapı değişkeni id değeri: 384
yd2 yapı değişkeni cd değeri: T

```

Program, önce bir adet int ve bir adet char değişken içeren yap adlı bir yapı tanımlar. Sonra, bu yapı türünden yd1 ve yd2 adlı iki adet değişken bildirimi yapar. yd1 değişkeni yoluyla, yd1 yapı kopyasındaki id değişkenine 165 sayısını ve cd değişkenine 'K' karakterini atar. yd2 değişkeni yoluyla, yd2 yapı kopyasındaki id değişkenine 384 sayısını ve cd değişkenine 'T' karakterini atar. Son olarak, yapı değişkenleri yoluyla tüm değerleri ekrana yazar.

Şimdi, . işlemcisinin sınıflarla kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

class sinif {
  private:
    int priid;
  public:
    int pubid;
    sinif(int pid1, int pid2)
    {
      priid=pid1;
      pubid=pid2;
    };
    void deger_goster()
    {
      cout << "priid değişken değeri: " << priid << "\n";
      cout << "pubid değişken değeri: " << pubid << "\n";
    }
};

int main(void)
{
  sinif *pnes, nes1(7, 21), nes2(35, 64);

  pnes = &nes1
  pnes->deger_goster();

  pnes = &nes2
  pnes->deger_goster();

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

priid değişken değeri: 95
pubid değişken değeri: 134
priid değişken değeri: 852
pubid değişken değeri: 3514

```

Program, önce bir adet priid adlı private int ve bir adet pubid adlı public int değişken ile bu değişkenlere ilk değer atama işlemi yapan bir constructor fonksiyonu ve bu değişken değerlerini ekranda gösteren deger\_goster() adlı bir fonksiyon içeren bir sınıf bildirimi yapar. Sonra, bu sınıf türünden nes1 ve nes2 adlı iki adet nesne bildirimi yapar. nes1 nesnesi yoluyla deger\_goster() fonksiyonunu çağırarak, nes1 sınıf kopyasındaki değişkenlerin değerlerini ekrana yazar. nes2 nesnesi yoluyla deger\_goster() fonksiyonunu çağırarak, nes2 sınıf kopyasındaki değişkenlerin değerlerini ekrana yazar.

## Artırma ve azaltma işlemcileri

Aşağıdaki işlem satırı değişken-adı ifadesi ile gösterilen değişkenin değerini bir sayı artırır:

değişken-adı = değişken-adı + 1;

C++ dilinde, yukarıdaki işlem satırında yer alan ifade ile aynı işlemi gerçekleştiren aşağıdaki ifadeyi kullanabiliriz:

değişken-adı++;

Bir değişken değerini birer birer artıran ve iki adet artı (+) işaretinden oluşan bu işlemciye artırma işlemcisi adı verilir. Artı işaretlerinin arasında boşluk olmamalıdır. Aşağıda yer alan her iki işlem satırı da aynı işlemi gerçekleştirir:

```c++
id = id + 1;
id++;


```

Yukarıdaki iki satır arasında, yaptıkları işlem açısından, hiçbir fark yoktur. Şimdi, örnekler üzerinde konuyu incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

int main(void)
{
  int id;

  id = 21;
  cout << "id değişken değeri: " << id << "\n";

  id = id + 1;
  cout << "id değişken değeri: " << id << "\n";

  id++;
  cout << "id değişken değeri: " << id;

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

id değişken değeri: 21
id değişken değeri: 22
id değişken değeri: 23

```

Program, başlangıçta 21 sayısını atadığı id int değişken değerini önce normal yöntemle, sonra artırma işlemcisi yoluyla 1 sayı artırarak elde ettiği bütün değerleri ekrana yazar.

Örnek

```c++
#include <iostream>

using namespace std;

int main(void)
{
  int id1=35, id2, id3;

  cout << "id1 değişken değeri: " << id1 << "\n";

  id1 = id1 + 1; // 36
  cout << "id1 değişken değeri: " << id1 << "\n";
  id1++;         // 37
  cout << "id1 değişken değeri: " << id1 << "\n\n";

  id2 = id1++;   // id2=37 id1=38 (id1 değişken değeri id2 değişkenine atandıktan sonra, id1 değişken değeri artırılır.)
  id3 = ++id1;   // id3=39 id1=39 (id1 değişken değeri artırıldıktan sonra, id1 değişkeni id2 değişkenine atanır.)

  cout << "id1 değişken değeri: " << id1 << "\n";
  cout << "id2 değişken değeri: " << id2 << "\n";
  cout << "id3 değişken değeri: " << id3;

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

id1 değişken değeri: 35
id1 değişken değeri: 36
id1 değişken değeri: 37

id1 değişken değeri: 39
id2 değişken değeri: 37
id3 değişken değeri: 39

```

Program, başlangıçta 35 sayısını atadığı id1 int değişken değerini önce normal yöntemle, sonra artırma işlemcisi yoluyla 1 sayı artırarak elde ettiği bütün değerleri ekrana yazar. Sonra, ++ işlemcisini id1 değişken adından sonra kullanarak id1 değişken değerini id2 değişkenine atar. Bu durumda, id1 değişken değeri id2 değişkenine atandıktan sonra, id1 değişken değeri artırılır. ++ işlemcisini id1 değişken adından önce kullanarak id1 değişken değerini id3 değişkenine atar. Bu durumda, id1 değişken değeri artırıldıktan sonra, id1 değişken değerini id2 değişkenine atar.id3 değişkeni id1 değişkeninin artırılmış değerini alır. Tüm değişken değerlerini ekrana yazar.

> ++ işlemcisi değişken adından sonra kullanıldığında, artırılmış değişken değeri, artırma işleminin yapıldığı işlem satırında sonraki işlem satırlarında geçerlidir. ++ işlemcisi değişken adından önce kullanıldığında ise, artırılmış değişken değeri, artırma işleminin yapıldığı işlem satırında geçerlidir.
{: .prompt-tip }

Artırma işlemcisine benzer şekilde, bir değişken değerini birer birer azaltan ve iki adet eksi (-) işaretinden oluşan bu işlemciye azaltma işlemcisi adı verilir.

değişken-adı--;

Eksi işaretlerinin arasında boşluk olmamalıdır. Aşağıda yer alan her iki işlem satırı da aynı işlemi gerçekleştirir:

```c++
id = id - 1;
id--;


```

Yukarıdaki iki işlem satırı arasında yaptıkları işlem açısından hiçbir fark yoktur. İlk satırdaki id1=id1-1 ifadesinin yerine ikinci satırda id1-- ifadesi kullanılmıştır. Şimdi, konuyu bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

int main(void)
{
  int id;

  id = 54;
  cout << "id değişken değeri: " << id << "\n";

  id = id - 1; // 53
  cout << "id değişken değeri: " << id << "\n";

  id--; // 52
  cout << "id değişken değeri: " << id;

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

id değişken değeri: 54
id değişken değeri: 53
id değişken değeri: 52

```

Program, başlangıçta 54 sayısını atadığı id int değişken değerini önce normal yöntemle, sonra artırma işlemcisi yoluyla 1 sayı azaltarak elde ettiği bütün değerleri ekrana yazar.

Artırma ve azaltma işlemcileri, atama işaretine göre biraz daha hızlı olduğu için kullanılmaktadır. Ayrıca program yazarken, uzun değişken adları kullandığımızda, yazacağınız karakter sayısını azaltır.

Artırma ve azaltma işlemcilerinin kullanılmasında bir incelik vardır. Bu operatörler değişken adının hem başına hem de sonuna gelebilirler. Her iki durumda değişkeni aynı şekilde etkilemesine rağmen program içinde işlemcinin yeri bazı farklılıklar yaratır.

Bu konuyu bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

int main(void)
{
  int id1, id2, id3, id4;

  id1 = 27;
  id2 = 11;

  cout << "id1 değişken değeri: " << id1 << "\n";
  cout << "id2 değişken değeri: " << id2 << "\n\n";

  id3 = id1 + id2++; // 1
  id4 = id1 + id2;

  cout << "id1 değişken değeri: " << id1 << "\n";
  cout << "id2 değişken değeri: " << id2 << "\n";
  cout << "id3 değişken değeri: " << id3 << "\n";
  cout << "id4 değişken değeri: " << id4 << "\n\n";

  id3 = id1 + ++id2; // 2
  id4 = id1 + id2;

  cout << "id1 değişken değeri: " << id1 << "\n";
  cout << "id2 değişken değeri: " << id2 << "\n";
  cout << "id3 değişken değeri: " << id3 << "\n";
  cout << "id4 değişken değeri: " << id4;

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

id1 değişken değeri: 27
id2 değişken değeri: 11

id1 değişken değeri: 27
id2 değişken değeri: 12
id3 değişken değeri: 38
id4 değişken değeri: 39

id1 değişken değeri: 27
id2 değişken değeri: 13
id3 değişken değeri: 40
id4 değişken değeri: 40

```

Program önce id1, id2, id3 ve id4 değişken bildirimlerini yapar, sonra id1 değişkenine 27 ve id2 değişkenine 11 değerini atar ve değişken değerlerini ekrana yazar. 1 sayısı ile gösterilen işlem satırında ise id1 ve id2 değişken değerlerini toplayarak 38 sayısını id3 değişkenine atar, aynı işlem satırında iken, atama işleminden sonra id2 değişken değerini, artırma işlemcisi ile 1 artırarak 12'ye çıkarır. Bu işlem satırından sonra artık id2 değişken değeri 12 olur. id1 ve id2 değişken değerlerini tekrar toplayarak id4 değişkenine atar ve bütün değişken değerlerini ekrana yazar.

Ancak, 2 sayısı ile gösterilen satırda ise id1 ve id2 değişken değerlerini toplayıp id3 değişkenine atamadan önce id2 değişken değerini artırır. 40 sayısını id3 değişkenine atar. Bu işlem satırından sonra artık id2 değişken değeri 12 olur ve bütün değişken değerleri ekrana yazılır. id1 ve id2 değişken değerlerini tekrar toplayarak id4 değişkenine atar ve bütün değişken değerlerini ekrana yazar.

Kısaca ifade etmek gerekirse, artırma veya azaltma işlemcisi bir değişken adından önce kullanılırsa elde edilen sonuç bulunduğu işlem satırında, değişken adından sonra kullanılırsa bulunduğu işlem satırından sonra geçerli olur.

## ? işlemcisi

C++ dilinde kullanılan işlemcilerden biri de, if yapısı yerine kullanılabilen ? işlemcisidir. ? işlemcisinin genel yapısı aşağıda gösterildiği şekildedir:

koşul ? ifade1 : ifade2;

? işlemcisi en az 3 değer gerektirir. ? işaretinden önce bir koşul, ? işaretinden sonra ise arasında : işareti bulunan iki ifade yer almalıdır. Koşul sonucunda elde edilen değer 1 (doğru) veya 0 (yanlış) olmalıdır. İfade bir sabit, değişken veya sabit ve değerlerin karışımından oluşan bir değerdir.

? işlemcisinin kullanılmasını örnekler üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

int main(void)
{
  int id1, id2, id3;

  id1 = 44;
  id2 = 71;

  id3 = (id1 < id2) ? 1 : 0;

  cout << "id3 değişken değeri: " << id3;

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

id3 değişken değeri: 1

```

Program, id1 ve id2 adlı 2 değişkene atadığı değerleri < ilişkisel işlemcisi ile karşılaştırır. id1 değişken değeri id2 değişken değerinden küçük olduğu için 1 değerini id3 değişkenine atar ve ekrana yazar. Eğer id1 değeri küçük olsaydı ekrana 0 değerini yazacaktı. Burada, ? işlemcisi ile elde edilen sonuç bir değişkene atanmıştır.

Örnek

```c++
#include <iostream>

using namespace std;

int main(void)
{
  int id1, id2;

  id1 = 75;
  id2 = 21;

  cout << "id1 değişkeni id2 değişkeninden ";
  (id1>id2) ? cout << "büyüktür!" : cout << "küçük veya eşittir!";

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

id1 değişkeni id2 değişkeninden büyüktür!

```

Yukarıdaki örnekte, program id1 ve id2 adlı 2 değişkene atadığı değerleri > ilişkisel işlemcisi ile karşılaştırır. id1 değişken değeri id2 değişken değerinden büyük olduğu ve koşul doğru sonuç verdiği için, ? işaretinden sonra gelen ilk ifadeyi ekrana yazar. Eğer id1 değeri id2 değerinden küçük veya eşit olsaydı ikinci ifadeyi ekrana yazacaktı.

## Atama işlemcisi

Normal koşullarda, atama işlemcisini kullanarak tek bir değişkene değer atayabiliriz.

```c++
int id;
id = 17;


```

Aynı zamanda, aynı işlem satırında birden fazla değişkene değer atayabiliriz. Aşağıdaki işlem satırı id1, id2 ve id3 değişkenlerine 26 değerini atar:

```c++
id1 = id2 = id3 = 26;


```

Yukarıdaki işlem satırında önce 26 değeri id3 değişkenine, id3 değişken değeri id2 değişkenine ve id2 değişken değeri id1 değişkenine atanır. C++'da, aşağıdaki işlem satırındaki örneğe benzer atamaları daha pratik bir şekilde yapabiliriz:

Bir değişken değerinde değişiklik yapmak için kullandığımız atama işlemcisi ve diğer işlemcileri iki farklı yapıda kullanabiliriz:

değişken-adı işlemci = değişken-adı + ifade;

değişken-adı işlemci= ifade;

Yukarıda yer alan her iki tanımlama da aynı işlemi gerçekleştirmektedir. İfade ise, bir değişken, sabit veya değişken veya sabitlerin ortaklaşa kullanılarak oluşturulduğu değerleri gösterir.

İkinci işlem satırında yer alan atamalarda, işlemci ile = işareti arasında boşluk bırakılmamalıdır.

```c++
id = id + 5;
id += 5;


```

Yukarıdaki işlem satırında yer alan işlemci ifadesi yerine aşağıdaki işlemcilerden birini kullanabiliriz:

+ - \* / % << >> & \| ^

Şimdi, öğrendiklerimizi örnekler üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

int main(void)
{
  int id1, id2, id3;

  id1 = id2 = id3 = 1849;

  cout << "id1 değişken değeri: " << id1 << "\n";
  cout << "id2 değişken değeri: " << id2 << "\n";
  cout << "id3 değişken değeri: " << id3;

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

id1 değişken değeri: 1849
id2 değişken değeri: 1849
id3 değişken değeri: 1849

```

Program, üç adet int değişken bildirimi yapar. Tek işlem satırında her üç değişkene atama işlemcisini kullanarak aynı değeri atar. Değişken değerlerini ekrana yazar.

Örnek

```c++
#include <iostream>

using namespace std;

int main(void)
{
  int id;

  id = 235;

  id = id + 21;
  cout << "Değişken değeri: " << id << "\n";

  id += 78;
  cout << "Değişken değeri: " << id;

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Değişken değeri: 256
Değişken değeri: 334

```

Program, ilk artırma işlemi için id = id + 21; ifadesini, ikinci artırma işlemi için ise id += 78; ifadesini kullanır.

## Virgül(,) işlemcisi

Virgül işlemcisi genellikle for döngüsünün bölümlerinde birden fazla işlem yapıldığında kullanılır. Bir işlem satırında, birden fazla işlem yapmak istediğimizde kullandığımız bir yöntem olarak tanımlayabiliriz.

Şimdi, bu özelliği bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

int main(void)
{
  int id1, id2, id3;

  for (id1=0, id2=0, id3=0; id1<5; id1++, id2+=2, id3+=3) {
       cout << id1 << " " << id2 << " " << id3 << "\n";
  }

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

0 0 0
1 2 3
2 4 6
3 6 9
4 8 12

```

Program, for döngüsünün ilk değer atama bölümünde virgül işlemcisini kullanır.

## () işlemcisi

Parantez işlemcisi, içinde yer alan işlemleri parantez dışında kalan işlemcilerin önceliklerini göz önüne almadan yapar. Bu işlemciyi bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

int main(void)
{
  int id1, id2;

  id1 = 21;
  id2 = 7;

  cout << "İlk ifade sonucu: " << id1*id2+3 << "\n"; // 1
  cout << "İkinci ifade sonucu: " << id1*(id2+3); // 2

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

İlk ifade sonucu: 150
İkinci ifade sonucu: 210

```

Program, 1 ve 2 sayısı ile gösterilen işlem satırlarında, ifadelerde aynı veri ve işlemcileri kullandığı halde, her iki işlem satırı ile ekrana yazılan değerler birbirinden farklıdır. Bunun nedeni, 2 sayısı ile gösterilen işlem satırında id2+3 ifadesinin, parantez işlemcisi ile, id1\*id2 işleminden önce gerçekleşmesidir.

## [] işlemcisi

[] işlemcisi dizilerle ilgili işlemlerde kullanılır. [] işlemcisini kullanarak bir dizi bildirimi yapabilir veya dizi elemanlarına direk olarak erişme olanağı sağlayabiliriz. Aşağıda yer alan ilk işlem satırı 10 elemanlı ve idizi adlı int bir dizi bildirimi yapar. İkinci işlem satırı ise bu dizinin beşinci (Dördüncü değil çünklü dizinin ilk elemanı sıfır ile gösterilir) elemanına 11 sayısını atar:

```c++
int idizi[20]; // 20 elemanlı int bir dizi bildirimi yapar.
idizi[4] = 11; // Dizinin beşinci elemanına 11 değeri atar. 


```

Bu işlemciyi bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

int main(void)
{
  int idizi[10];
  int id;

  for (id=0; id<10; id++) idizi[id]=id+1;

  for (id=0; id<10; id++) cout << idizi[id] << " ";

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

1 2 3 4 5 6 7 8 9 10

```

Program, 10 elemanlı int bir dizi bildirimi yapar. Bir for döngüsü ile, 1-10 arasındaki sayıları bu diziye atar. Sonra, bu dizi değerlerini ekrana yazar.

## Geçici veri türü değiştirme işlemcisi (type cast)

Geçici veri türü değiştirme işlemcisini kullanarak bazen bir değişkenin veri çeşidini geçici olarak değiştirebiliriz. Bu değişkenin genel kullanımı aşağıda gösterilmektedir:

(veri-türü) değişken;

Şimdi, bu özelliği bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

int main(void)
{
  int id1, id2;
  double dd1, dd2;

  id1 = 29;
  id2 = 77;

  dd1 = 52.281;
  dd2 = 79.9769;

  cout << id1 << " " << id2  << "\n";
  cout << dd1 << " " << dd2  << "\n\n";

  cout << showpoint << (double)id1 << " " << (double)id2  << "\n";
  cout << (int)dd1 << " " << (int)dd2;

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

29 77
52.281 79.9769

29.0000 77.0000
52 79

```

Program, önce iki adet int ve iki adet double değişken değerini normal olarak, sonra geçici veri türü değiştirme işlemcisini kullanarak int değişken değerlerini double, double değişken değerlerini ise int değer olarak ekrana yazar.

Bir atama işleminde, atama işaretinin sol tarafında geçici veri türü değiştirme işlemcisini kullanamayız.

## sizeof işlemcisi

sizeof işlemcisini kullanarak herhangi bir veri türünün veya bir değişkenin byte olarak boyutunu elde edebiliriz. Aşağıdaki ilk satır bir veri türünün, ikinci satır ise bir değişkenin boyutunun hesaplanmasında kullanılan sizeof işlemcisinin genel yapısını göstermektedir:

sizeof (veri-türü);
sizeof değişken-adı;

sizeof ifadesi veri türü ile kullanıldığında parantezlerle birlikte tanımlanmasına rağmen, değişken adı ile kullanıldığı zaman, parantezlere gerek yoktur.

Şimdi, sizeof işlemcisinin kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

int main(void)
{
  char cd;
  int id;
  float fd;
  double dd;

  cout << "char veri türü boyutu: " << sizeof(char) << "\n";
  cout << "int veri türü boyutu: " << sizeof(int) << "\n";
  cout << "float veri türü boyutu: " << sizeof(float) << "\n";
  cout << "double veri türü boyutu: " << sizeof(double) << "\n\n";

  cout << "cd değişken boyutu: " << sizeof cd << "\n";
  cout << "id değişken boyutu: " << sizeof id << "\n";
  cout << "fd değişken boyutu: " << sizeof fd << "\n";
  cout << "dd değişken boyutu: " << sizeof dd;

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

char veri türü boyutu: 1
int veri türü boyutu: 4
float veri türü boyutu: 4
double veri türü boyutu: 8

cd değişken boyutu: 1
id değişken boyutu: 4
fd değişken boyutu: 4
dd değişken boyutu: 8

```

Program, 4 farklı veri türünün boyutunu hem veri türü hem de değişken adı yoluyla hesaplayarak ekrana yazar.

## İşlemci öncelikleri

Şimdiye kadar incelediğimiz bütün işlemcilerin öncelik dereceleri aşağıda yer almaktadır:

```

() [] -> .
! ~ ++ -- - (veri-türü) * & sizeof
* / %
+ -
<< >>
< <= > >=
== !=
<
^
|
<<
||
?
= += -= *= /= %=
,

```

C++, yaptığı bütün işlemleri yukarıdaki işlemci önceliği kuralına uygun olarak yapar.
