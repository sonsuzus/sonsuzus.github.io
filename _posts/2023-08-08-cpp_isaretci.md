---
title:  C++ İşaretçiler (Pointers)
author: sonsuz
date: 2023-08-08 21:51:28 +0300
categories: [Program,C++]
tags: [cpp,programlama,işaretçi,pointer,adres]
---



İşaretçiler, bilgisayar belleğindeki belli bir adresin, genellikle bir değişkene ait, kaydedildiği ve kaydedilen bellek adresine doğrudan erişim sağlayan değişkenlerdir.

## İşaretçi bildirimi

İşaretçilerin diğer değişkenlerden tek farkı başka bir değişkenin bellek adresini içeriyor olmasıdır. Aşağıdaki satır işaretçi bildiriminin genel yapısını göstermektedir:

veri-türü \*değişken-adı;

Yukarıdaki satırda yer alan veri-türü ifadesi işaretçinin adresini gösterdiği değerin veri türünü, değişken-adı ifadesi ise işaretçinin adını göstermektedir. \* işareti işaretçi değişken bildiriminde kullanılmaktadır. Aşağıdaki işlem satırı ip adlı int bir işaretçi değişkeni oluşturmaktadır:

```c++
int *ip;


```

İşaretçiler, bildirimi yapıldıktan sonra doğrudan kullanılamazlar. Kullanmadan önce mutlaka bir bellek adresi atanması gerekir.

## İşaretçilere değer atanması

Bir işaretçiyi kullanmadan önce, bir bellek adresinin mutlaka işaretçiye atanması gerekir. Çünkü, işaretçi bellek adresleri ile işlem yapar. C++'da, işaretçilere bellek adresi atama işlemi, & işlemcisi ile yapılır.

C++'da işaretçilerle kullanılan iki farklı işlemci vardır. Bunlardan biri \* , diğeri ise & işlemcisidir. Bu iki işlemcinin görevlerinin anlaşılması işaretçi kavramını anlamak açısından çok önemlidir:

\* : Hangi işaretçi değişken adından önce kullanılırsa, o işaretçi değişkene adresi atanan değişkenin değerini verir.

& : Hangi değişken adından önce kullanılırsa, o değişkenin adresini verir.

İşaretçi tanımlamalarında veri türünü belirlerken, daha sonra adresini işaretçiye atanacak değişkenin veri türünü dikkate almamız gerekir. Başka bir ifade ile, işaretçi ile işaretçiye bellek adresi atanan değişkenin veri türü aynı olmalıdır.

Konunun daha kolay anlaşılması için işaretçi kullanılması ile \* ve & işlemcilerini örnekler üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

int main(void)
{
  int *ip, id; // int bir işaretçi ve değişken bildirimi
  id = 21;
  ip = &id    // id değişken adresini ip işaretçisine atar.

  // İşaretçi kullanarak id değişken değerini ekrana yazar.
  cout << "id değişken değeri: " << *ip;

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

id değişken değeri: 21

```

Program önce id adlı bir int değişken ve ip adlı bir işaretçi değişkeni oluşturur. id değişkenine 21 değerini atar. id değişkeninin adresini ip işaretçisine atar. id değişken değerini işaretçi kullanarak ekrana yazar.

Örnek

```c++
#include <iostream>

using namespace std;

int main(void)
{
  int *ip, id; // int bir işaretçi ve değişken bildirimi
  id = 21;
  ip = &id    // id değişken adresini ip işaretçisine atar.

  // Değişken adını kullanarak id değişken değerini ekrana yazar.
  cout << "id değişken değeri: " << id << "\n";

  // İşaretçi kullanarak id değişken değerini ekrana yazar.
  cout << "id değişken değeri: " << *ip << "\n";

  // Değişken referansını kullanarak id değişken adresini ekrana yazar.
  cout << "id değişken bellek adresi: " << &id << "\n";

  // İşaretçi adını kullanarak id değişken adresini ekrana yazar.
  cout << "id değişken bellek adresi: " << ip << "\n";

  return 0;
}


```

Yukarıdaki örnekte, program ekrana aşağıdaki satırları yazar:

```

id değişken değeri: 21
id değişken değeri: 21
id değişken bellek adresi: 0x6dfee8
id değişken bellek adresi: 0x6dfee8

```

Program önce id adlı bir int değişken ve ip adlı bir işaretçi değişkeni oluşturur. id değişkenine 21 değerini atar. id değişkeninin adresini ip işaretçisine atar. id değişken değerini önce değişken adını sonra işaretçi kullanarak, iki kez ekrana yazar. id değişkeninin bellek adresini önce değişken referans değerini sonra işaretçi adını kullanarak ekrana yazar. Bellek adresi her bilgisayarda farklı bir değer alabilir.

> Konumuza devam etmeden önce, 0x6dfee8 ifadesini kısaca inceleyelim. Bu ifade bilgisayar belleğinin belirli bir adresini 16'lık (Hexadecimal) sayı sisteminde göstermektedir. Yukarıdaki örnek programı çalıştırdığımızda farklı bir bellek adres değeri alabiliriz. Burada gösterilen bütün adres değerleri, her bilgisayar için farklı olabilir.
{: .prompt-tip }

## İşaretçilere ilk değer atama

Global veya statik olarak tanımlanan işaretçilere, tanımlanır tanımlanmaz otomatik olarak NULL bir değer ilk değer olarak atanır.

Statik olmayan ve yerel bir işaretçi bildirimi yaptığımızda ise, bu işaretçiye bir bellek adresi atamanın iki farklı yöntemi vardır:

1. Bir değişkenin bellek adresini & işlemcisi ile işaretçiye atamak.
2. malloc() fonksiyonu yoluyla tahsis edilen bir bellek bölümünün başlangıç adresini işaretçiye atamak.

Bu iki yöntemle işaretçiye bir bellek adresi atamadan önce, işaretçi bilinmeyen belirsiz bir değer taşır. Eğer işaretçiye bir değer atamadan kullanırsak program beklenmeyen sonuçlar verir.

Programlarda oluşabilecek muhtemel sorunları çözmek için, bir bellek adresi atanmamış statik olmayan ve yerel işaretçilerde ilk değer olarak 0 veya NULL değeri ilk değer olarak verilir.

```c++
char *p = 0;

veya 

char *p = NULL;


```

Ancak, bu uygulama sorunun tamamen çözülmesi için yeterli değildir. Bu işlem satırından sonra da işaretçiye atanan değerlerin bir bellek adresi olmasına dikkat edilmelidir.

C++'da, bir işaretçiye karakter dizisi sabitlerini ilk değer olarak atayabiliriz.

```c++
char *cp = "Bilgisayar";


```

Burada, cp bir işaretçi olduğundan sadece bir bellek adresini gösterdiği kabul edilir. Ancak, C++'da derleyiciler program tarafından kullanılan karakter dizilerini yükledikleri karakter dizisi tablosu adlı bir tablo oluştururlar. Böylece, program bir işaretçi değişkeni ile gösterilen bir karakter dizisini karakter dizisi tablosundan okuyarak işlem yapar.

## İşaretçiler yoluyla değişkenlere değer atama

İşaretçileri kullanarak, işaretçinin adresini içerdiği değişkene bir değer atayabiliriz. Bu özelliği bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

int main(void)
{
  int *ip1, *ip2, id1, id2;

  ip1 = &id1 // id1 değişkeninin adresini ip1 işaretçisine atama
  ip2 = &id2 // id2 değişkeninin adresini ip2 işaretçisine atama
  id1 = 42;   // id1 değişkenine değer atama
  *ip2 = 67;  // id2 değişkenine ip2 işaretçisi yoluyla değer atama

  cout << "id1 değişkeninin değeri: " << *ip1 << "\n";
  cout << "id2 değişkeninin değeri: " << *ip2 << "\n";
  cout << "id1 değişkeninin bellek adresi: " << ip1 << "\n";
  cout << "id2 değişkeninin bellek adresi: " << ip2;

  cout << "\n\n";

  cout << "ip1 işaretçisinin bellek adresi: " << &ip1 << "\n";
  cout << "ip2 işaretçisinin bellek adresi: " << &ip2;

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

id1 değişkeninin değeri: 42
id2 değişkeninin değeri: 67
id1 değişkeninin bellek adresi: 0x6dfee4
id2 değişkeninin bellek adresi: 0x6dfee0

ip1 işaretçisinin bellek adresi: 0x6dfeec
ip2 işaretçisinin bellek adresi: 0x6dfee8

```

Program önce ip1 ve ip2 adlı 2 adet işaretçi değişkeni ile id1 ve id2 adlı 2 adet int değişken tanımlar. id1 değişkeninin bellek adresini ip1 işaretçisine id2 değişkeninin bellek adresini ip2 işaretçisine atar. id1 değişkenine direk olarak 42 sayısını atar. id2 değişkenine ise, ip2 işaretçisini kullanarak, 67 sayısını dolaylı yöntemle atar. Sonra id1 ve id2 değişkenlerinin değerlerini ve bellek adreslerini ekrana yazar. Programın her işlem satırından sonraki bellek durumu ise aşağıda gösterilmektedir:

![](cprog/isaretci001.png)

Bir işaretçi kullanmadan önce, bir bellek adresi mutlaka işaretçiye atanmalıdır. Eğer bir bellek adresi atamadan işaretçi kullanılırsa, istenen netice elde edilemez. Çünkü, bir işaretçi tanımladığımızda sadece bir bellek adresini atayabilecek bir değişken oluşturmuş oluruz. Ancak, işaretçi değişkenine atanmış herhangi bir bellek adres değeri yoktur. Aynı şekilde eğer bir işaretçi değişken bildiriminden sonra, bir değişkenin bellek adresini işaretçiye atamadan, bir int değeri işaretçi değişkenine atarsak, yine istediğimiz neticeyi elde edemeyiz.

Aşağıda yer alan işlem satırlarından 1 ve 2 sayıları ile gösterilen satırlar, C++ dili kurallarına göre geçersizdir:

```c++
int *ip;

*ip = 357;   // 1
cout << *ip; // 2


```

Şimdi, işaretçi kullanılan farklı bir örneği incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

int main(void)
{
  char *cp, cd;

  cp = &cd

  for (cd='A'; cd<'L'; cd++) cout << *cp << " ";

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

A B C D E F G H I J K

```

Program büyük A harfinden başlamak üzere ASCII karakterlerin alfabenin ilk 11 tanesini ekrana yazar. Program önce cp adlı işaretçi bir değişken ve cd adlı bir char değişken tanımlar. cd değişkeninin bellek adresini cp işaretçisine atar. Bir for döngüsü ve cp işaretçini kullanarak sıra ile harflerin atandığı cd değişken değerlerini ekrana yazar. Burada, program for döngüsü yoluyla, cd değişken değerini 10 kez değiştirir ve her defasında cp işaretçisini kullanarak değişken değerini ekrana yazar.

## Diğer işaretçi işlemcileri ve işlemci aritmetiği

Daha önce incelediğimiz \* ve & işlemcilerine ek olarak, işaretçilerle kullanabileceğiniz 4 işlemci daha vardır:

```
+   -   ++  --
```

Artırma ve azaltma işlemcilerinin işaretçilerle kullanılmasında özel bir durum vardır. Herhangi bir veri türünden tanımlanmış olan bir işaretçi değerini bir değer artırmak veya azaltmak istediğimizde, işaretçi değere sadece tanımlandığı veri türünün boyutu kadar bir değer ekler veya çıkarabiliriz.

```c++
int *ip, id;

ip = &id;

id = 21;

ip = ip + 1; // ip işaretçisinin gösterdiği bellek adresini int veri boyutu kadar ileri taşır.
ip = ip + (1 * sizeof (int)); // ip işaretçisinin gösterdiği bellek adresini int veri boyutu kadar ileri taşır.


```

Yukarıdaki son iki işlem satırının her ikisinde de, ip işaretçisinin gösterdiği bellek adresi int veri türü boyutu kadar (4 byte) ileri taşınır.

Şimdi, bu özelliği bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

int main(void)
{
  char cdizi[] = { 'A', 'B', 'C', 'D', 'E', 'F' };
  char *cp;
  int len, id;

  cp = cdizi; // cp = &cdizi[0];

  len = sizeof(cdizi) / sizeof(char);

  for (id=0; id<len; id++) cout << *cp++ << " ";

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

A B C D E F

```

Program, cdizi adlı bir diziye ilk değer atama yöntemi ile A-F arasındaki harfleri atar. Sonra, cp adlı bir işaretçi ile len ve id adlı iki adet int değişken bildirimi yapar. cdizi dizisinin bellek adresini cp işaretçisine atar. Dizi eleman sayısını, dizi boyutunu char veri türü boyutuna bölerek elde eder ve len değişkenine atar. Bir for döngüsü, dizi eleman değerlerini ekrana yazar. for döngüsünün her tekrarında cp işaretçi değeri bir byte (char veri türü için) kadar artırılarak, bir sonraki dizi elemanının bellek adresini göstermesi sağlanır.

Örnek

```c++
#include <iostream>

using namespace std;

int main(void)
{
  int *ip;
  int idizi[5] = { 5, 17, 21, 34, 46 };
  int id;

  cout << "İşaretçi bellek adresi: " << &ip << "\n\n";

  ip = idizi; // ip = &idizi[0];

  for (id=0; id<5; id++, ip++) {
       cout << "İşaretçinin içerdiği bellek adresi: " << ip << " " << &idizi[id] << "\n";
       cout << "İşaretçinin gösterdiği değişken değeri: " << *ip << " " << idizi[id] << "\n\n";
  }

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

İşaretçi bellek adresi: 0x6dfed8

İşaretçinin içerdiği bellek adresi: 0x6dfec4 0x6dfec4
İşaretçinin gösterdiği değişken değeri: 5 5

İşaretçinin içerdiği bellek adresi: 0x6dfec8 0x6dfec8
İşaretçinin gösterdiği değişken değeri: 17 17

İşaretçinin içerdiği bellek adresi: 0x6dfecc 0x6dfecc
İşaretçinin gösterdiği değişken değeri: 21 21

İşaretçinin içerdiği bellek adresi: 0x6dfed0 0x6dfed0
İşaretçinin gösterdiği değişken değeri: 34 34

İşaretçinin içerdiği bellek adresi: 0x6dfed4 0x6dfed4
İşaretçinin gösterdiği değişken değeri: 46 46

```

Program, önce ip adlı int bir işaretçi ile idizi adlı 5 elemanlı int bir dizi tanımlar. İşaretçi bellek adresini ekrana yazdıktan sonra, dizinin ilk elemanının adresini işaretçiye atar. Bir for döngüsü içinde, her defasında işaretçi değerini int boyutu kadar artırmak suretiyle, işaretçinin bir sonraki dizi elemanının adresini göstermesini sağlayarak işaretçinin içerdiği adresi ve gösterdiği dizi değişken değerini hem işaretçi adı hem de dizi adını kullanarak ikişer defa ekrana yazar.

for döngüsüne ilk girdiğinde bellek durumu aşağıdaki ilk şekildeki gibidir. Döngü içinde ip++ ifadesi ilk çalıştığında ise, ip int bir işaretçi olduğundan, int boyutu kadar (32 bit bilgisayarlarda 4 byte) yukarıdaki bellek adresinin değerini alır. Yani, daha önce idizi[0] değişken adresini içeren ip işaretçisi artık idizi[1] değişkeninin adresini içermektedir. Aslında, işlem satırındaki ip++ ifadesinin gerçek değeri aşağıdaki gibidir.

ip = ip + (1\*sizeof(int));

![](cprog/isaretci002.png)

Sonuç olarak, for döngüsünün her tekrarında ip++ işlemi ile ip işaretçisinin içerdiği adres int boyutu kadar artarak bir sonraki dizi değerinin adresini gösterir.

* Bir işaretçiye eklenen veya çıkarılan değer mutlaka int bir değer olmalıdır.

* İşaretçilerle toplama veya çıkarma dışında bir işlem yapılamaz.

Örnek

```c++
#include <iostream>

using namespace std;

int main(void)
{
  int *ip;
  int idizi[5] = { 15, 72, 154, 298, 345 };

  cout << "İşaretçi bellek adresi: " << &ip << "\n\n";

  ip = &idizi[4];

  cout << "İşaretçinin içerdiği adres: " << ip << "\n";
  cout << "İşaretçinin gösterdiği değişken değeri: " << *ip << "\n\n";

  ip-=2; // ip -= (4 * sizeof (int));

  cout << "İşaretçinin içerdiği adres: " << ip << "\n";
  cout << "İşaretçinin gösterdiği değişken değeri: " << *ip;

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

İşaretçi bellek adresi: 0x6dfeec

İşaretçinin içerdiği adres: 0x6dfee8
İşaretçinin gösterdiği değişken değeri: 345

İşaretçinin içerdiği adres: 0x6dfee0
İşaretçinin gösterdiği değişken değeri: 154

```

Program, önce ip adlı int bir işaretçi ile idizi adlı 5 elemanlı int bir dizi oluşturur. İşaretçi bellek adresini ekrana yazdıktan sonra, dizinin son elemanının adresini işaretçiye atar. İşaretçinin içerdiği adresi ve gösterdiği dizi değişken değerini ekrana yazar. Sonra, işaretçiden 4 int boyutu kadar değer çıkararak işaretçinin ilk dizi elemanının adresini göstermesini sağlayarak, işaretçinin gösterdiği adresi ve bu adreste bulunan dizi değerini ekrana yazar.

Programın çalışma süresince bellek içeriğindeki değişim aşağıda gösterilmektedir:

![](cprog/isaretci003.png)

## İşaretçiler yoluyla değişken değerlerinin değiştirilmesi

++ ve -- operatörleri ile normal toplama ve çıkarma işlemlerini kullanarak işaretçinin adresini gösterdiği değişken değerini dolaylı yöntemle artırabiliriz:

Örnek

```c++
#include <iostream>

using namespace std;

int main(void)
{
  int *ip, id;

  id = 274;

  ip = &id

  cout << "id değişken değeri: " << id << "\n";

  // ip işaretçisinin adresini gösterdiği değişken değerini artırma
  (*ip)++;

  cout << "id değişken değeri: " << id;

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

id değişken değeri: 274
id değişken değeri: 275

```

Program, ip adlı int bir işaretçi ve id adlı int bir değişken oluşturur. id değişkenine 274 sayısını atar. id değişkeninin adresini ip işaretçisine atar. Değişken değerini ekrana yazdıktan sonra ip işaretçisini kullanarak, id değişken değerini artırır ve değişken değerini tekrar ekrana yazar.

Örnek

```c++
#include <iostream>

using namespace std;

int main(void)
{
  int *ip, id;

  id = 541;

  ip = &id

  cout << "id değişken değeri: " << id << "\n";

  // ip işaretçisinin adresini gösterdiği değişken değerini 20 azaltma
  *ip = *ip - 20;

  cout << "id değişken değeri: " << id;

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

id değişken değeri: 541
id değişken değeri: 521

```

Program, bir önceki programın yaptığı işlemin aynısını gerçekleştirir. Tek fark, değişken değerini tek sayı artırmak yerine 20 sayı azaltmasıdır.

Şimdi, işaretçi kullanarak işaretçinin gösterdiği bellek adresini ve gösterdiği değişken değerini değiştirme işlemini gösteren bir örneği incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

int main(void)
{
  int *ip;
  int idizi[5] = { 36, 64, 127, 152, 183 };

  ip = idizi; // ip = &idizi[0];

  cout << "Dizinin ilk eleman değeri: " << idizi[0] << "\n";
  cout << "Dizinin ilk eleman değeri: " << *ip << "\n";
  cout << "Dizinin ilk eleman bellek adresi: " << &idizi[0] << "\n";
  cout << "Dizinin ilk eleman bellek adresi: " << ip << "\n\n";

  // İşaretçinin gösterdiği bellek adresini artırma
  *ip++; // ip++ ile aynı işlemi gerçekleştirir.

  cout << "Dizinin ikinci eleman değeri: " << idizi[1] << "\n";
  cout << "Dizinin ikinci eleman değeri: " << *ip << "\n";
  cout << "Dizinin ikinci eleman bellek adresi: " << &idizi[1] << "\n";
  cout << "Dizinin ikinci eleman bellek adresi: " << ip << "\n\n";

  // İşaretçinin gösterdiği dizi elemanının değerini artırma
  (*ip)++; // idizi[1]++ ile aynı işlemi gerçekleştirir.

  cout << "Dizinin ikinci eleman değeri: " << idizi[1] << "\n";
  cout << "Dizinin ikinci eleman değeri: " << *ip << "\n";
  cout << "Dizinin ikinci eleman bellek adresi: " << &idizi[1] << "\n";
  cout << "Dizinin ikinci eleman bellek adresi: " << ip;

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Dizinin ilk eleman değeri: 36
Dizinin ilk eleman değeri: 36
Dizinin ilk eleman bellek adresi: 0x6dfed8
Dizinin ilk eleman bellek adresi: 0x6dfed8

Dizinin ikinci eleman değeri: 64
Dizinin ikinci eleman değeri: 64
Dizinin ikinci eleman bellek adresi: 0x6dfedc
Dizinin ikinci eleman bellek adresi: 0x6dfedc

Dizinin ikinci eleman değeri: 65
Dizinin ikinci eleman değeri: 65
Dizinin ikinci eleman bellek adresi: 0x6dfedc
Dizinin ikinci eleman bellek adresi: 0x6dfedc

```

Program, ip adlı bir işaretçi ile 5 elemanlı idizi adlı int bir dizi oluşturur. Dizinin ilk elemanının adresini ip işaretçisine atar. Dizinin ilk eleman değeri ile bellek adresini, değişken adını ve işaretçiyi kullanarak ikişer defa ekrana yazar. ip işaretçinin gösterdiği adresi int boyutu kadar artırdıktan sonra değerleri tekrar ekrana yazar. ip işaretçisinin adresini gösterdiği değişkenin değerini artırdıktan sonra değerleri tekrar ekrana yazar.

```c++
ip++;    // İşaretçinin gösterdiği bellek adresini artırır.

(*ip)++; // İşaretçinin gösterdiği bellek adresindeki değişken değerini artırır.


```

## İşaretçilerle dizi kullanımı

Bir dizi oluşturduktan sonra, sadece dizi adı kullanıldığında dizi başlangıç elemanını gösteren bir işaretçi tanımlanmış olur. Bu durumda aşağıdaki son işlem satırında gösterilen her iki ifade aynı sonucu sağlar. Dizi adını doğrudan kullanmak veya dizi başlangıç elemanının adresini kullanmak, dizinin bellek başlangıç adresini gösterir.

```c++
int idizi[10]; // int dizi bildirimi
int id;
int *ip;

ip = idizi; // ip = &idizi[0];


```

## Tek boyutlu dizi elemanlarına işaretçilerle erişim

Bir dizinin ilk elemanının bellek adres değerini bir işaretçiye geçirerek dizi elemanlarına işaretçi yoluyla erişilebilir.

Örnek

```c++
#include <iostream>

using namespace std;

int main(void)
{
  int idizi[10] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };

  int *ip;
  int id;

  ip = idizi; // idizi ile &idizi[0] aynı anlamdadır.

  // Dizi elemanlarını indeksleme yöntemi ile ekrana yazma
  for (id=0; id<10; id++) cout << idizi[id] << " ";

  cout << "\n";

  // Dizi elemanlarını işaretçi aritmetiği yöntemi ile ekrana yazma
  for (id=0; id<10; id++) cout << *(ip+id) << " ";

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10

```

Program, önce 1'den 10'a kadar olan sayıları 10 elemanlık idizi adlı bir diziye ilk değer atama metodu ile atar. ip adlı int bir işaretçi ve id adlı int bir değişken tanımlar. idizi dizisinin ilk eleman adresini ip işaretçisine atar. Sonra, idizi dizisinin elemanlarını hem dizi indeksleme yöntemi hem de işaretçi aritmetiği kullanarak iki kez ekrana yazar.

## Çok boyutlu dizi elemanlarına işaretçilerle erişim

Çok boyutlu dizilerde istediğimiz dizi elemanına ulaşmak için, aşağıda gösterilen formülü kullanmak gerekir:

\*(p + (eleman satır numarası \* dizi sütun sayısı) + eleman numarası)

Dizinin sütun sayısı ile dizi elemanının bulunduğu satır numarasını çarpar, dizi elemanının bulunduğu satırdaki eleman sıra numarası ile birlikte dizi başlangıç adresini gösteren işaretçiye eklediğimizde, istenen dizi elemanına ulaşabiliriz. Bu özelliği bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

int main(void)
{
  int idizi[10][15];
  int *ip;

  ip = idizi[0];
  idizi[7][5] = 458;

  cout << "Dizi eleman değeri: " << *(ip+(7*15)+5);

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Dizi eleman değeri: 458

```

Program, önce 10\*15 boyutlarında int bir dizi oluşturur. Dizinin başlangıç adresini ip adlı int bir işaretçiye atar. Dizi indeksleme metodu ile, dizinin yedinci satır beşinci sütununa 458 sayısını atar. Sonra işaretçi aritmetiği kullanarak aynı değeri ekrana yazar. Tek ya da çok boyutlu dizilerle işlem yaparken hem dizi indeksleme metodu hem de işaretçi aritmetiği kullanılabilir. Hangi yöntemin kullanılacağı tamamen tercihe bağlıdır. İşaretçi aritmetiği kullanılan programlar, dizi indeksleme yöntemi kullanılan programlardan daha hızlı çalışır.

## İşaretçi indeksleme

Bir işaretçi tıpkı bir dizi gibi indekslenebilir. Ancak bu işlemi gerçekleştirebilmek için, indekslenen işaretçiye mutlaka bir dizinin başlangıç adresini atamak gerekir. Bu özelliği bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

int main(void)
{
  int idizi[10];
  int *ip, id;

  ip = idizi;

  for (id=1; id<10; id++) {
       ip[id] = id; // İşaretçi indeksleme
       cout << ip[id] << " ";
  }

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

1 2 3 4 5 6 7 8 9

```

Program, oluşturduğu idizi adlı dizinin başlangıç adresini ip işaretçisine atar. Sonra idizi[id] ifadesi yerine ip[id] ifadesini kullanarak 1'den 9'a kadar olan sayıları diziye atar ve dizi eleman değerlerini ekrana yazar.

## Dizi adı ile işaretçi aritmetiği kullanarak dizi elemanlarına erişim

Dizi adı, dizi başlangıcını gösteren bir işaretçi olarak kullanılabildiğinden, bir dizinin başlangıç adresini bir işaretçiye atamadan, direk olarak dizi adı ile işaretçi aritmetiğini kullanarak dizi elemanlarına erişim sağlanabilir. Ancak bu durumda, dizi adını kullanarak oluşturulan bir işaretçi değeri değiştirilemez. Şimdi, bu özelliği bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

int main(void)
{
  int idizi[10];

  *(idizi+4) = 25;

  cout << *(idizi+4);

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

25

```

Program, dizi adını kullanarak bir işaretçi oluşturur ve dizinin beşinci elemanına 25 sayısını atar. Yine aynı yöntemle sayıyı ekrana yazar.

Şimdi öğrendiklerimizi örneklerle pekiştirmeye çalışalım:

Örnek

```c++
#include <iostream>
#include <cstring>

using namespace std;

int main(void)
{
  char cdizi[20];
  int id;
  char *cp;

  strcpy(cdizi, "Bilgisayar");

  for (id=0; cdizi[id]; id++) cout << cdizi[id];

  cout << "\n";

  cp = cdizi;
  for ( ; *cp; cp++) cout << *cp;

  cout << "\n";

  cp = cdizi;
  while (*cp) cout << *cp++;

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Bilgisayar
Bilgisayar
Bilgisayar

```

Program, 20 elemanlık bir karakter dizisi oluşturur ve diziye bir karakter dizisi kopyalar. Bir for döngüsü ile dizi indeksleme yöntemi kullanarak, dizi elemanlarını sırayla ekrana yazar. Dizinin ilk elemanının bellek adresini bir işaretçiye atar. Bir for döngüsü ile işaretçi aritmetiği yöntemi kullanarak, dizi elemanlarını sırayla ekrana yazar. Dizinin ilk elemanının bellek adresini tekrar bir işaretçiye atar. Bir while döngüsü ile işaretçi aritmetiği yöntemi kullanarak, dizi elemanlarını sırayla ekrana yazar.

## Karakter dizileri ile işaretçi kullanımı

Daha önce karakter dizilerinin gerek normal değer atama gerekse ilk değer atama metodu ile (" ") işaretleri arasına alınan karakter dizilerini char dizilere atandığını görmüştük. Aynı şekilde tanımlanan karakter dizilerini, her iki değer atama metodu ile işaretçilere de atayabiliriz. Bu özelliği bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

int main(void)
{
  char *cp1 = "İşaretçiler";
  char *cp2;

  cp2 = "ve karakter dizileri";

  cout << cp1 << " " << cp2;

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

İşaretçiler ve karakter dizileri

```

Program, önce cp1 ve cp2 adlı iki adet char işaretçi tanımlar. Sonra, cp1 işaretçisine ilk değer atama cp2 işaretçisine ise normal yöntemle atadığı karakter dizilerini cp1 ve cp2 işaretçileri yoluyla ekrana yazar.

İncelediğimiz örneklerde gördüğünüz gibi, bir karakter dizisini hem dizi hem de işaretçilerle kullanabiliriz. Ancak;

Karakter dizisi bir işaretçi ile tanımlandığında, karakter dizisi için bellekte bir yer ayrılmaz.

Karakter dizisi bir dizi ile tanımlandığında ise, karakter dizisi için bellekte bir yer ayrılır.

Şimdi, öğrendiklerimizi örneklerle pekiştirmeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

int main(void)
{
  char *cp1, *cp2;

  cp1 = "İşaretçiler";
  cp2 = " ve karakter dizileri";

  while (*cp1) cout << *cp1++;

  cout << cp2;

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

İşaretçiler ve karakter dizileri

```

Program, oluşturduğu cp1 ve cp2 adlı iki adet char işaretçiye adreslerini atadığı karakter dizilerini işaretçi yoluyla ekrana yazar. cp1 işaretçisine bağlı karakter dizisini birer birer, diğer karakter dizisini ise bir defada ekrana yazar.

Örnek

```c++
#include <iostream>
#include <cstring>

using namespace std;

int main(void)
{
  char *cp1 = "İlk karakter dizisi";
  char *cp2;
  char cdizi[30];

  cp2 = "İkinci karakter dizisi";
  strcpy (cdizi, "Üçüncü karakter dizisi");

  cout << cp1 << "\n" << cp2 << "\n" << cdizi << "\n\n";

  cout << cp1[9] << " " << cp2[9] << " " << cdizi[9] << " " << *(cdizi+9);

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

İlk karakter dizisi
İkinci karakter dizisi
Üçüncü karakter dizisi

t r r r

```

Yukarıdaki örnekte, program tanımladığı char işaretçi ve dizilere farklı yöntemlerle atadığı karakter dizilerini ve bu karakter dizilerinde yer alan dokuzuncu karakterleri farklı indeksleme yöntemleri ile ekrana yazar.

## İşaretçi dizileri oluşturma

İşaretçiler bir dizi elemanı olarak tanımlanabilir. Örneğin, aşağıdaki işlem satırı aynı anda 10 adet int işaretçi tanımlar:

```c++
int *ip[10];


```

İşaretçi dizilerinin kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

int main(void)
{
  int *ip[3];
  int id1, id2, id3;
  int id4;

  ip[0] = &id1;
  ip[1] = &id2;
  ip[2] = &id3;

  for (id4=0; id4<3; id4++) {
       *ip[id4] = id4 + 10;
       cout << *ip[id4] << " ";
  }

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

10 11 12

```

Program, önce üç elemanlı int bir işaretçi dizisi tanımlar. Üç adet int değişkenin adreslerini sıra ile dizi içinde yer alan işaretçilere atar. Sonra, işaretçileri kullanarak değişkenlere bir değer atar ve atadığı değerleri ekrana yazar.

Şimdi, işaretçi dizilerinin farklı olarak kullanılmasını örnekler üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

int main(void)
{
 char *cp[] = {
    "Kitap",
    "Defter",
    "Kalem",
    "Silgi",
    "Cetvel",
    ""
  };

  int id;

  for (id=0; *cp[id]; id++) cout << cp[id] << "\n";

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Kitap
Defter
Kalem
Silgi
Cetvel

```

Program, önce char bir işaretçi dizi tanımlar. İlk değer atama metodu ile beş farklı karakter dizisini bu diziye atar. Bir for döngüsü kullanarak dizi içeriğini ekrana yazar. Burada, işaretçi dizileri boyutsuz dizilerle aynı amaçla kullanılmaktadır.

Örnek

```c++
#include <iostream>

using namespace std;

int main(void)
{
  char *cp[][4] = {
     "Ahmet", "Kibar",  "1974", "Ankara",
     "Mehmet", "Efendi", "1987", "İstanbul",
     "Aytaç", "Yiğit", "1980", "Samsun",
     "Nedim", "Mülayim", "1961", "Sivas",
     "Murat", "Sakin",  "1992", "Manisa",
     "Erson", "Nazik", "1983", "Ağrı",
     "", "", "", ""
  };

  int id1, id2;

  for (id1=0; *cp[id1][0]; id1++) {
       for (id2=0; id2<4;id2++) {
            cout << cp[id1][id2] << " ";
       }
       cout << "\n";
  }

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Ahmet Kibar 1974 Ankara 
Mehmet Efendi 1987 İstanbul 
Aytaç Yiğit 1980 Samsun 
Nedim Mülayim 1961 Sivas 
Murat Sakin 1992 Manisa 
Erson Nazik 1983 Ağrı 

```

Program, bir karakter dizisi tablosu oluşturmak için 2 boyutlu bir işaretçi dizisi tanımlar. İlk değer atama yöntemi ile bu diziye bazı değerler atar. Sonra dizi içeriğini ekrana yazar.

## İşaretçi adresi taşıyan işaretçiler (Çoklu kullanım)

Bir işaretçi değişkeni başka bir değişkenin bellek adresini içerir. Bir işaretçi değişkeni başka bir işaretçi değişkeninin bellek adresini de içerebilir. Bu özelliğe ÇOKLU DOLAYLI YÖNLENDİRME adı verilir. Bir işaretçi değişkeninin adresini içeren bir işaretçi değişkeninin tanımlanması için kullanılan genel yapı aşağıdaki şekildedir:

veri-türü \*\*işaretçi-adı;

Örneğin aşağıdaki ilk işlem satırı, ip adlı int bir işaretçinin adresini gösteren ipp adlı int bir işaretçi değişkeni ve ayrıca id adlı int bir değişken tanımlar. İkinci işlem satırı id değişkeninin adresini ip adlı işaretçiye, üçüncü işlem satırı ise ip işaretçisinin adresini ipp adlı işaretçiye atar. Bu durumda ipp işaretçisini kullanarak id değişkenine bir değer atayabilir veya değerini değiştirebiliriz.

```c++
int **ipp, *ip, id;
ip = &id
ipp = &ip


```

Ayrıca, çoklu dolaylı yönlendirme işlemini ikiden fazla işaretçi ile de kullanabiliriz. Her bir işaretçi eklemenizde ilave olarak bir \* işareti kullanmamız gerekir. Gereğinden fazla işaretçi kullanılarak yapılan çoklu dolaylı yönlendirme pratik bir kullanım imkanı sağlamaz. Yaptığımız program anlaşılması çok güç bir hale gelebilir.

Şimdi bu konuyu örnekler üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

int main(void)
{
  int *ip, **ipp, id;
  char *cp, **cpp, cd;

  ip = &id
  ipp = &ip

  cp = &cd
  cpp = &cp

  **ipp = 237;
  cd = 'K';

  cout << "id değişken değeri: " << id << " " << *ip << " " << **ipp << "\n";
  cout << "id değişken bellek adresi: " << &id << " " << ip << "\n";
  cout << "ip işaretçi bellek adresi: " << ipp << "\n\n";

  cout.setf(ios::hex, ios::basefield);
  cout.setf(ios::showbase);

  cout << "cd değişken değeri: " << cd << " " << *cp << " " << **cpp << "\n";
  cout << "cd değişken bellek adresi: " << (int) &cd << " " << (int) cp << "\n";
  cout << "cp işaretçi bellek adresi: " << (int) cpp;

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

id değişken değeri: 237 237 237
id değişken bellek adresi: 0x6dfed0 0x6dfed0
ip işaretçi bellek adresi: 0x6dfed4

cd değişken değeri: K K K
cd değişken bellek adresi: 0x6dfecb 0x6dfecb
cp işaretçi bellek adresi: 0x6dfecc

```

Program, int veri türünden birer adet değişken, işaretçi değişkeni ve işaretçi adresi gösteren işaretçi değişken bildirimi yapar. char veri türünden değişken, işaretçi değişkeni ve işaretçi adresi gösteren işaretçi değişken bildirimi yapar. id adlı int değişken adresini ip işaretçisine, ip işaretçi adresini de ipp işaretçisine atar. cd adlı char değişken adresini cp işaretçisine, cp işaretçi adresini de cpp işaretçisine atar. id değişkenine ipp işaretçisi yoluyla cd değişkenine direk olarak bir değer atar. Değişken değerleri ile işaretçilerin gösterdiği adresleri hem normal hem de dolaylı yoldan ekrana yazar.

id vd cd değişken değerlerini, değişken adı, işaretçi ve işaretçi adresi gösteren işaretçi yoluyla, id ve cd değişken bellek adreslerini değişken referans, işaretçi ve işaretçi adresi gösteren işaretçi yoluyla ekrana yazar.

Örnek

```c++
#include <iostream>
#include <cstring>

using namespace std;

int main(void)
{
  char **cpp, *cp, cdizi[20];

  cp = cdizi;
  cpp = &cp;

  strcpy(cdizi, "İşaretçi işlemleri");

  cout << cdizi << "\n";
  cout << cp << "\n";
  cout << *cpp;

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

İşaretçi işlemleri
İşaretçi işlemleri
İşaretçi işlemleri

```

Program, char veri türünden birer adet işaretçi adresi gösteren işaretçi değişken, işaretçi değişkeni ve karakter dizisi bildirimi yapar. cdizi karakter dizisinin bellek başlangıç adresini cp işaretçisine, cp işaretçisinin bellek adresini cpp işaretçisine atar. cdizi karakter dizisine bir karakter dizisi atar. Karakter dizisini dizi adı, işaretçi ve işaretçi adresi gösteren işaretçi yoluyla üç defa ekrana yazar.

Örnek

```c++
#include <iostream>

using namespace std;

int main(void)
{
  int **ipp1, *ip1, id1;
  int **ipp2, *ip2, id2;

  ip1 = &id1
  ipp1 = &ip1

  ip2 = &id2
  ipp2 = &ip2

  *ip1 = 175;
  **ipp2 = 421;

  cout << ipp1 << " " << ip1 << " " << &id1 << "\n";
  cout << **ipp1 << " " << *ip1 << " " << id1;

  cout << "\n\n";

  cout << ipp2 << " " << ip2 << " " << &id2 << "\n";
  cout << **ipp2 << " " << *ip2 << " " << id2;

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

0x6dfed4 0x6dfed0 0x6dfed0
175 175 175

0x6dfecc 0x6dfec8 0x6dfec8
421 421 421

```

Program, int veri türünden ikişer adet işaretçi adresi gösteren değişken, işaretçi değişkeni ve normal değişken tanımlar. id1 değişken adresini ip1 işaretçisine, ip1 işaretçi adresini ipp1 işaretçisine atar. id2 değişken adresini ip2 işaretçisine, ip2 işaretçi adresini ipp2 işaretçisine atar. ip1 işaretçi değişkenini kullanarak id1 değişkenine, ipp2 işaretçi değişkenini kullanarak id2 değişkenine bir değer atar. Sonra, id1 ve id2 değişkenlerinin adreslerini, işaretçi adreslerini ve değişken değerlerini farklı yöntemlerle ekrana yazar.

Örnek

```c++
#include <iostream>

using namespace std;

int main(void)
{
  int **ipp1, *ip1, id1;
  int **ipp2, *ip2, id2;
  int **ipp3, *ip3, id3;

  ip1 = &id1, ipp1 = &ip1
  ip2 = &id2, ipp2 = &ip2
  ip3 = &id3, ipp3 = &ip3

  **ipp1 = **ipp2 = 21;

  **ipp3 = **ipp1 + **ipp2;

  cout << **ipp3;

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

42

```

Program, işaretçi adresi gösteren işaretçi değişkenleri ile yaptığı işlem sonucunu ekrana yazar.

## İşaretçilerin fonksiyon parametresi olarak kullanımı

İşaretçileri fonksiyonlara argüman olarak geçirilebilir. Diziler ile işlem yapan fonksiyonları çağırırken, argüman olarak kullandığınız dizi isimleri aslında bir fonksiyona bir işaretçi geçirmemizi sağlar. Bir fonksiyona geçirilen işaretçi veri tipi ile, çağrılan fonksiyonun parametresi olarak tanımlanmış işaretçi veri tipi aynı olmalıdır. Bir fonksiyona argüman olarak geçirilen işaretçi değeri fonksiyon tarafından değiştirilebilir.

Bir karakter dizisinin sadece adını tanımlayarak bir fonksiyona bir argüman olarak geçirebiliriz. Aslında bu durumda fonksiyona geçirilen değer karakter dizisinin kendisi değil, karakter dizisinin ilk karakterinin bellek adresidir. Bu özelliği bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>
#include <cstring>

using namespace std;

void fonk(char *cp1, char *cp2);

int main(void)
{
  char cdizi1[20], cdizi2[30];

  strcpy(cdizi1, "İşaretçiler");
  strcpy(cdizi2, "ve karakter dizileri");

  fonk(cdizi1, cdizi2);

  return 0;
}

void fonk(char *cp1, char *cp2)
{
  cout << cp1 << " " << cp2;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

İşaretçiler ve karakter dizileri

```

Yukarıdaki örnekte, program iki char diziye kopyalanan karakter dizilerini fonk() fonksiyonuna argüman olarak geçirir. fonk() fonksiyonu karakter dizilerini ekrana yazar.

Standart kütüphane fonksiyonlarından puts() fonksiyonu kendisine geçirilen karakter dizisini ekrana yazar ve otomatik olarak satır başı ve satır aralığı karakteri ekleyerek yeni satıra geçiş olanağı sağlar.

```c++
int puts(const char *str);


```

str parametresi ile gösterilen karakter dizisindeki tüm karakterleri ve bir adet '\n' karakterini ekrana yazar. str ile gösterilen karakter dizisi sonunda yer alan '\0' karakteri yazılmaz.

Şimdi, puts() fonksiyonu ile puts() fonksiyonuna benzer bir fonksiyonun kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

void bg_fputs(char *cp);

int main(void)
{
  char cdizi[20];

  strcpy(cdizi, "Bilgisayar");

  cout << cdizi << "\n";
  puts(cdizi);

  bg_fputs(cdizi);

  return 0;
}

void bg_fputs(char *cp)
{
  while (*cp) cout << *cp++;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Bilgisayar
Bilgisayar
Bilgisayar

```

Program, bir karakter dizisine atanan karakter dizisini üç farklı yöntemle ekrana yazar. İlk yöntemde, cout fonksiyonu ile dizi ve "\n" karakteri ekrana yazılır. İkinci yöntemde puts() fonksiyonu ve üçüncü yöntemde bg\_puts() ile karakter dizisi ekrana yazılır. puts()
fonksiyonu karakter dizisini ekrana yazarken sonuna "\n" karakteri ekler. bg\_puts() fonksiyonu da aynı yöntemi uygular.

Şimdi, strcpy(), strcat(), strcmp() ve strlen() fonksiyonlarına benzeyen fonksiyonların kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

void bg_strcpy(char *cp1, char *cp2);
void bg_strcat(char *cp1, char *cp2);
int bg_strcmp(char *cp1, char *cp2);
int bg_strlen(char *cp);

int main(void)
{
  char cdizi1[50], cdizi2[50];
  int id;

  bg_strcpy(cdizi1, "Dizi ");
  bg_strcat(cdizi1, "bellek adresleri");

  bg_strcpy(cdizi2, "Bilgisayar");

  cout << cdizi1 << "\n" << cdizi2 << "\n\n";

  cout << "Dizi uzunlukları: " << bg_strlen(cdizi1) << " " << bg_strlen(cdizi2) << "\n\n";

  id = bg_strcmp(cdizi1, cdizi2);

  if(id==0) cout << "İki dizi birbirine eşittir!";
  else if(id<0) cout << "İlk dizi ikincisinden küçüktür!";
  else cout << "İlk dizi ikincisinden büyüktür!";

  return 0;
}

void bg_strcpy(char *cp1, char *cp2)
{
  while (*cp2) *cp1++ = *cp2++;
  *cp1 = '\0';
}

void bg_strcat(char *cp1, char *cp2)
{
  while (*cp1) cp1++;
  while (*cp2) *cp1++ = *cp2++;
  *cp1 = '\0';
}

int bg_strcmp(char *cp1, char *cp2)
{
  while (*cp1==*cp2) {
     cp1++;
     cp2++;
  }
  if (*cp1 == '\0') return 0;
  return *cp1 - *cp2;
}

int bg_strlen(char *cp)
{
  int id = 0;

  while (*cp) {
     id++;
     cp++;
  }
  return id;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Dizi bellek adresleri
Bilgisayar

Dizi uzunlukları: 21 10

İlk dizi ikincisinden büyüktür!

```

Program, strcpy(), strcat(), strcmp() ve strlen() fonksiyonlarına benzeyen fonksiyonlarla yaptığı işlem sonuçlarını ekrana yazar.

Şimdi, öğrendiklerimizi değişik örneklerle pekiştirmeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

void fonk(int *ip1, int *ip2);

int main(void)
{
  int id1, id2;
  id1 = 62;
  id2 = 153;

  fonk(&id1, &id2);
  cout << id1 << " " << id2;

  return 0;
}

void fonk(int *ip1, int *ip2)
{
  *ip1 = 123;
  *ip2 = 347;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

123 347

```

Program, oluşturduğu id1 ve id2 adlı değişkenlere sırasıyla 62 ve 153 sayılarını atar. Değişken adreslerini fonk() fonksiyonuna argüman olarak geçirir. fonk() fonksiyonu değişkenlerin değerlerini sırasıyla 123 ve 347 olarak değiştirir. Program, değişken değerlerini ekrana yazar.

Örnek

```c++
#include <iostream>

using namespace std;

void fonk(int *ip);

int main(void)
{
  int idizi[10];
  int id;

  for (id=0; id<10; id++) {
       idizi[id] = id+1;
       cout << idizi[id] << " ";
  }

  cout << "\n";

  fonk(idizi);
  for (id=0; id<10; id++) cout << idizi[id] << " ";

  return 0;
}

void fonk(int *ip)
{
  int id;

  for (id=0; id<10; id++) *ip++ += 10;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

1 2 3 4 5 6 7 8 9 10
11 12 13 14 15 16 17 18 19 20

```

Program, oluşturduğu idizi adlı int bir diziye 1'den 10'a kadar olan sayıları atar ve dizi içeriğini ekrana yazar. Dizi başlangıç adresini argüman olarak geçirerek fonk() fonksiyonunu çağırır. fonk() fonksiyonu dizi eleman değerlerine 10 değeri ekler. Program, dizi içeriğini tekrar ekrana yazar.
