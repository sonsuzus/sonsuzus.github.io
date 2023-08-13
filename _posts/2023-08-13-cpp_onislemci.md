---
title:  C++ Önişlemci direktifleri
author: sonsuz
date: 2023-08-13 18:09:29 +0300
categories: [Program, C++]
tags: [programlama,cpp,önişlemci,direktif,define]
---


Derleme işleminin ilk safhasında, önişlemci derleyiciye bazı direktifler ulaştırır. Derleyici tarafından bazı özel işlemlerin yapılmasını sağlayan bu direktiflere Önişlemci Direktifleri adı verilir. Şimdi, önişlemci direktiflerini sıra ile incelemeye çalışalım:

## #define önişlemci direktifi

#define önişlemci direktifi, programlarımızın herhangi bir işlem satırında kullanılmak üzere, istediğimiz ifadelerin kısa bir isim altında tanımlamamızı sağlar. #define önişlemci direktifinin genel yapısı aşağıda gösterilmektedir:

```

#define makro-adı karakter-dizisi

```

Yukarıdaki işlem satırını programımızın başında kullandığımızda, program makro-adı ifadesi ile gösterilen makro adını gördüğü her yerde karakter-dizisi ifadesi ile gösterilen karakter dizisi yazılmış gibi hareket eder. #define önişlemci direktifinin tanımlandığı satır normal işlem satırları gibi noktalı virgül işareti ile sona ermez.

Kullandığımız makro adlarını küçük veya büyük harflerle tanımyabiliriz. Programların daha kolay anlaşılması için büyük harf kullanılması tercih edilebilir. Makro adı ile karakter dizisi arasında bir veya birden fazla boşluk bırakabilirsiniz.

Şimdi, #define önişlemci direktifinin kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

#define MAK01 "ABCDE"

int main(void)
{
  cout << MAK01; // = cout << "ABCDE";

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

ABCDE

```

Program, "ABCDE" karakter dizisine karşılık gelen MAK01 adlı bir makro tanımlar. main() fonksiyonu içindeki işlem satırında MAK01 ifadesi yerine "ABCDE" karakter dizisi otomatik olarak yerleştirilmektedir.

Şimdi, biraz daha ayrıntılı bir örneği incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

#define MAK01 "Bir int değer giriniz: "
#define MAK02 20

int main(void)
{
  int id;

  cout << MAK01;    // 1
  cin >> id;

  cout << MAK02+id; // 2

  return 0;
}


```

Program, MAK01 ve MAK02 adlı 2 makro tanımlar. MAK01 makrosu "Bir int değer giriniz: ", MAK02 makrosu ise 20 karakter dizisini temsil eder. Program, 1 sayısı ile gösterilen işlem satırında MAK01 ifadesi ile karşılaştığı her yerde, makronun temsil ettiği karakter dizisini yerleştirdiği için "Bir int değer giriniz:" karakter dizisini ekrana yazar. Girdiğiniz int değeri id değişkenine atar. 2 sayısı ile gösterilen işlem satırında ise MAK02 makrosunun karşılığı olan 20 değeri ile id değişken değerini toplayarak ekrana yazar. Başlangıçta bir karakter dizisi olarak kabul edilen 20 ifadesini sayısal bir değere çeviren derleyicidir.

Makro işlemlerinde, #define satırında tanımlanan ve program içinde makro adının yerine kullanılan ifade ister karakter ister sayısal değerler içersin, daima bir karakter dizisi olarak kabul edilir.

#define önişlemci direktifi ile tanımlanan makrolar, ister bütün fonksiyonların dışında ister herhangi bir fonksiyonun içinde tanımlansın, makro bir kez tanımlandıktan sonra, bütün fonksiyonlar dahil olmak üzere programın herhangi bir yerinde kullanılabilir. Bu özelliği bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

void fonk1(void);
void fonk2(void);

#define MAK01 5

int main(void)
{
  #define MAK02 10

  int id;

  for (id=0; id<MAK01; id++) cout << id+1 << " ";
  cout << "\n";

  fonk1();
  fonk2();

  return 0;
}

void fonk1(void)
{
  #define MAK03 15

  int id;

  for (id=0; id<MAK02; id++) cout << id+1 << " ";
  cout << "\n";
}

void fonk2(void)
{
  int id;

  for (id=0; id<MAK03; id++) cout << id+1 << " ";
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

1 2 3 4 5
1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15

```

Program, bütün fonksiyonların dışında MAK01 adlı, main() fonksiyonunda MAK02 adlı ve fonk1() fonksiyonu içinde MAK03 adlı bir makro oluşturur. Tanımlandıkları yerden farklı olarak, MAK01 makrosunu main() fonksiyonu içinde, MAK02 makrosunu fonk1() fonksiyonu içinde ve MAK03 makrosunu fonk2() fonksiyonu içinde kullanılır.

Bir program içinde, aynı değeri kullandığımız birden fazla yer varsa ve bu değer sık sık değiştiriliyorsa, makro kullanmak çok büyük bir kolaylık sağlayacaktır. Bu durumda, programımızın bir çok yerinde tek tek değişiklik yapmak yerine sadece makro değerini değiştirmek yeterli olacaktır. Bu özelliği bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

void fonk(int *ip);

#define MAK01 10

int main(void)
{
  int cdizi[MAK01];
  int id;

  for (id=0; id<MAK01; id++) {
       cdizi[id] = id+1;
       cout << cdizi[id] << " ";
  }
  cout << "\n";

  fonk(cdizi);

  return 0;
}

void fonk(int *ip)
{
  int id;

  for (id=0; id<MAK01; id++) cout << ip[id] + MAK01+2 << " ";
  cout << "\n";
  for (id=0; id<MAK01; id++) cout << ip[id] + MAK01+4 << " ";
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

1 2 3 4 5 6 7 8 9 10
13 14 15 16 17 18 19 20 21 22
15 16 17 18 19 20 21 22 23 24

```

Program, MAK01 adlı bir makro tanımlar ve bu makroyu 7 farklı yerde kullanır. Makroya 10 değerini verdiği için, önce 10 elemanlı bir dizi oluşturur. 1'den 10'a kadar olan sayıları diziye atar ve eleman değerlerini ekrana yazar. Sonra, fonk() fonksiyonu ile önce dizi eleman değerlerine MAK01 makro değerinin 2 fazlasını ekleyerek, sonra dizi eleman değerlerine MAK01 makro değerinin 4 fazlasını ekleyerek ekrana yazar. Programda bir değişiklik yapmak istediğimizde, sadece #define önişlemci satırındaki MAK01 makro değerini değiştirerek programın 7 farklı yerindeki değeri otomatik olarak değiştirmiş oluruz.

Şimdiye kadar #define direktifi ile basit bir makro tanımlayarak, program içinde bu makronun geçtiği her yerde, makro ile ilgili karakter dizisinin program tarafından makro yerine kullanıldığını gördük.

Bu uygulamanın yanı sıra, #define önişlemci direktifini kullanarak fonksiyona benzeyen makrolar oluşturabiliriz.

#define önişlemci direktifinin kullanılmasını farklı örnekler üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>
#include <cstring>

using namespace std;

#define MAK01(id1, id2) id1+id2         
#define MAK02(cp1, cp2) strcpy(cp1, cp2)
#define MAK03(cp1, cp2) strcat(cp1, cp2)
#define MAK04(id1) fonk(id1) 

void fonk(int id1);

int main(void)
{
  char cdizi[50];

  MAK02(cdizi, "Bilgisayar");

  cout << MAK01(261, 82) << " " << MAK03(cdizi, " Programlama") << "\n";

  MAK04(21);

  return 0;
}

void fonk(int id1)
{
  int id2;

  for (id2=0; id2<10; id2++) cout << id1 << " ";
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

343 Bilgisayar Programlama
21 21 21 21 21 21 21 21 21 21 

```

Program, fonksiyona benzer makrolar tanımlayarak, bir toplama işlemi ile strcpy(), strcat() ve fonk() fonksiyonlarını çağırma işlemlerini bu makrolar yoluyla yapmaktadır.

Örnek

```c++
#include <iostream>

using namespace std;

#define MAK01(id1, id2) (id1<id2) && (id1>5) && (id1%2==0) ? 1 : 0

int main(void)
{
  int id1, id2;

  cout << "Bir int değer giriniz: ";
  cin >> id1;

  cout << "Bir int değer daha giriniz: ";
  cin >> id2;

  cout << MAK01(id1, id2);

  return 0;
}


```

Program, bir makro tanımlaması yapar. İki int değer girilmesini ister. Makro yoluyla, girilen ilk int değer ikincisinden küçük, 5 sayısından büyük ve çift bir sayı ise 1 sayısını, aksi takdirde 0 sayısını ekrana yazar.

Örnek

```c++
#include <iostream>

using namespace std;

#define MAK01(id1, id2) (id1>id2) ? id1 : id2

int main(void)
{
  int id1, id2;

  id1 = 121;
  id2 = 96;

  cout << (MAK01(id1, id2)) << " ";

  id2 += 50;

  cout << (MAK01(id1, id2));

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

121 146

```

Program, #define önişlemci direktifi ile bir makro bildirimi yapar. id1 ve id2 değişkenlerine sıra ile 121 ve 96 sayılarını atar. Sonra, makroyu kullanarak iki kez işlem yapar ve elde ettiği sonuçları ekrana yazar.

## #include önişlemci direktifi

En çok kullanılan ve sistem tarafından hazır olarak sunulan fonksiyonlar kütüphane dosyaları adı verilen .LIB uzantılı dosyalara yerleştirilmiştir. Bu dosyalarda yer alan kütüphane fonksiyonlarının prototipleri ise başlık dosyası adı verilen .H uzantılı dosyalarda yer alır.

#include direktifini kullanarak, başlık dosyalarında bildirimleri yer alan fonksiyonları programımızda yazılmış gibi kullanabiliriz.

Aşağıdaki satırı programımıza dahil ettiğimizde, <cstdio> başlık dosyası içinde bildirimleri bulunan bütün kütüphane fonksiyonlarını, programımızda yazılmış gibi kullanabiliriz:

```c++
#include <cstdio>


```

#include önişlemci direktifini aşağıda gösterilen 2 farklı şekilde kullanabiliriz.

```


#include <dosya-adı>
#include "dosya-adı"


```

> Eğer dosya adını < > işaretleri arasında tanımlarsak, derleyici tanımladığımız dosyayı başlık dosyalarının içinde bulunduğu alt dizinde arar. Bu dizin genellikle include alt dizinidir. Eğer dosya adını " " işaretleri arasında tanımlarsak, derleyici tanımlanan dosyayı önce aktif dizinde, daha sonra diğer dizinlerde arar. " " işaretlerini kullandığımızda, eğer varsa, derleyici tanımladığımız dosyayı mutlaka bulur. Sistem uygun şekilde düzenlendiğinde, < > işaretlerini kullanmak derleme zamanını kısaltır.
{: .prompt-tip }

Şimdi, #include önişlemci direktifinin kullanılmasını örnekler üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>
#include <cstring>

using namespace std;

int main(void)
{
  char cdizi[20];

  strcpy(cdizi, "Bilgisayar");

  cout << cdizi;

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Bilgisayar

```

Program, bir karakter dizisine "Bilgisayar" kelimesini atar ve dizi değerini ekrana yazar. iostream ve cstring başlık dosyalarının her ikisini de < > işaretleri arasında tanımlar.

Örnek

```c++
#include <iostream>
#include "cstring"

using namespace std;

int main(void)
{
  char cdizi[20];

  strcpy(cdizi, "Bilgisayar");

  cout << cdizi;

  return 0;
}


```

Program, bir önceki program tarafından yapılan işlemin aynısını gerçekleştirir. Tek fark, başlık dosyalarının birini < >, diğerini ise " " işaretleri arasında tanımlamış olmasıdır.

## Koşula bağlı derleme

C++'da, yazılan programların belirli bölümlerini seçeneğe bağlı olarak derleyebiliriz. Bu işleme Koşula Bağlı Derleme adı verilir. Koşula bağlı derleme aşağıdaki direktifler tarafından gerçekleştirilir:

```


#if
#else
#elif
#endif
#ifdef
#ifndef


```

#if direktifinin genel yapısı aşağıda göstermektedir:

```


#if sabit-ifade
   işlem-satırları
#endif


```

Burada, sabit-ifade değeri doğru sonuç verirse #if ile #endif satırı arasında kalan bütün işlem satırları derlenir, aksi takdirde derleyici bu satırları derlemeden geçer. Derlemenin ilk safhası önişlem safhası olduğu için burada bahsi geçen sabit-ifade yerine herhangi bir değişken değeri kullanamayız. #if ve #endif direktiflerinin kullanılmasını örneklerle incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

#define MAK01 20
#define MAK02 50

int main(void)
{
  #if MAK01<MAK02
     cout << "MAK01 değeri MAK02 değerinden küçüktür." << "\n";
     cout << "MAK01 değeri: " << MAK01 << "\n";
     cout << "MAK02 değeri: " << MAK02;
  #endif

  // Aşağıda yer alan işlem satırları derleyici tarafından derlenmez.
  #if MAK01>MAK02
     cout << "MAK01 değeri MAK02 değerinden büyüktür." << "\n";
     cout << "MAK01 değeri: " << MAK01 << "\n";
     cout << "MAK02 değeri: " << MAK02;
  #endif

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

MAK01 değeri MAK02 değerinden küçüktür.
MAK01 değeri: 20
MAK02 değeri: 50

```

Program, MAK01 değeri MAK02 değerinden küçük olduğundan, sadece ilk #if direktifi içinde yer alan satırları derler. İkinci #if direktifi içinde yer alan işlem satırları hiç derlenmez.

Örnek

```c++
#include <iostream>

using namespace std;

#define MAK01 20
#define MAK02 12

int main(void)
{
  // Aşağıda yer alan üç işlem satırı derleyici tarafından derlenmez.
  #if MAK01<MAK02
     cout << "MAK01 değeri MAK02 değerinden küçüktür." << "\n";
     cout << "MAK01 değeri: " << MAK01 << "\n";
     cout << "MAK02 değeri: " << MAK02;
  #endif

  #if MAK01>MAK02
     cout << "MAK01 değeri MAK02 değerinden büyüktür." << "\n";
     cout << "MAK01 değeri: " << MAK01 << "\n";
     cout << "MAK02 değeri: " << MAK02;
  #endif

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

MAK01 değeri MAK02 değerinden büyüktür.
MAK01 değeri: 20
MAK02 değeri: 12

```

Program, MAK01 değeri MAK02 değerinden büyük olduğundan, sadece ikinci #if direktifi içinde yer alan satırları derler. İlk #if direktifi içinde yer alan işlem satırları hiç derlenmez.

#if direktifi ile birlikte #else direktifini kullanabiliriz. #else direktifinin genel yapısı aşağıda gösterilmektedir:

```


#if sabit-ifade
   işlem-satırları
#else
   işlem-satırları
#endif


```

#if satırında yer alan sabit-ifade doğru sonuç verirse, #if direktifi ile ilgili işlem satırları, aksi takdirde #else direktifi ile ilgili işlem satırları derlenir. Bu özelliği örnekler üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

#define MAK01 1

int main(void)
{
  int id;

  #if MAK01 == 1
     for (id=0; id<10; id++) cout << id+1 << " ";
  #else
     for (id=10; id>0; id--) cout << id << " ";
  #endif

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

1 2 3 4 5 6 7 8 9 10

```

Program, #if satırındaki ifade doğru sonuç verdiği için, sadece #if direktifi ile ilgili işlem satırını derler ve 1'den 10'a kadar olan sayıları ekrana yazar. Diğer işlem satırları hiç derlenmez.

Örnek

```c++
#include <iostream>

using namespace std;

#define MAK01 2

int main(void)
{
  int id;

  #if MAK01 == 1
     for (id=0; id<10; id++) cout << id+1 << " ";
  #else
     for (id=10; id>0; id--) cout << id << " ";
  #endif

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

10 9 8 7 6 5 4 3 2 1

```

Program, #if satırındaki ifade yanlış sonuç verdiği için, sadece #else direktifi ile ilgili işlem satırını derler ve 1'den 10'a kadar olan sayıları sondan başlayarak ekrana yazar. Diğer işlem satırları ise hiç derlenmez.

Aşağıda genel yapısı verilen #elif direktifini kullanarak bir if-else-if merdiveni oluşturabiliriz:

```


#if sabit-ifade1
   işlem-satırları
#elif sabit-ifade2
   işlem-satırları
#elif sabit-ifade3
   işlem-satırları
.
.
.
#endif


```

if-else-if merdiveninde doğru olan ilk ifadenin yer aldığı #if veya #elif satırına bağlı olan işlem satırları derlenir, diğer işlem satırları derleyici tarafından dikkate alınmaz. if-else-if merdiveninin kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

#define MAK01 3

int main(void)
{
  int id;

  #if MAK01 == 1
    for (id=1; id<=10; id++) cout << id << " ";
  #elif MAK01 == 2
    for (id=2; id<=10; id++) cout << id << " ";
  #elif MAK01 == 3
    for (id=3; id<=10; id++) cout << id << " ";
  #endif

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

3 4 5 6 7 8 9 10

```

MAK01 makrosuna 1 ile 3 arasındaki sayılardan hangisini atarsak, program o sayıdan başlamak suretiyle 10'a kadar olan sayıları ekrana yazar.

#ifdef direktifinin genel yapısı ise aşağıda gösterilmektedir:

```


#ifdef makro-adı
   işlem-satırları
#endif


```

Makro adı tanımlanırsa, derleyici #ifdef direktifi ile ilgili işlem satırlarını derler. Aksi takdirde, söz konusu işlem satırlarını dikkate almaz. #ifdef direktifi ile birlikte #else direktifini kullanabiliriz.

#ifndef direktifinin genel yapısı da tıpkı #ifdef direktifi gibidir. Tek fark #ifndef direktifi ile ilgili işlem satırlarının sadece makro adı tanımlanmadığında derlenmesidir.

Şimdi, bu özellikleri örnekler üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

#define MAK01 4

int main(void)
{
  int id1;

  #ifdef MAK01
     int id2=0;
  #endif

  for (id1=0; id1<10; id1++) {
       cout << id1+1 << " ";

       #ifdef MAK01
          id2 += MAK01 * (id1+1);
       #endif
  }

  #ifdef MAK01
     cout << "\n" << "Toplam: " << id2;
  #endif

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

1 2 3 4 5 6 7 8 9 10
Toplam: 220

```

Program, 1'den 10'a kadar olan sayıları ve bu sayıların 4 ile çarpımlarının toplamını ekrana yazar. id2 değişkeni ile ilgili işlem satırlarının derlenerek çalışmasının nedeni, programda MAK01 adlı bir makronun tanımlanmış olmasıdır.

Örnek

```c++
#include <iostream>

using namespace std;

int main(void)
{
  int id1;

  #ifdef MAK01
     int id2=0;
  #endif

  for (id1=0; id1<10; id1++) {
       cout << id1+1 << " ";

       #ifdef MAK01
          id2 += MAK01 * (id1+1);
       #endif
  }

  #ifdef MAK01
     cout << "\n" << "Toplam: " << id2;
  #endif

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

1 2 3 4 5 6 7 8 9 10

```

Program, 1'den 10'a kadar olan sayıları ekrana yazar. id2 değişkeni ile ilgili işlem satırlarının derlenmemesinin nedeni, programda MAK01 adlı bir makronun tanımlanmamış olmasıdır.

Örnek

```c++
#include <iostream>

using namespace std;

int main(void)
{
  int id1;

  #ifndef MAK01
     int id2=0;
  #endif

  for (id1=0; id1<10; id1++) {
       cout << id1+1 << " ";

       #ifndef MAK01
          id2 += 4 * (id1+1);
       #endif
  }

  #ifndef MAK01
     cout << "\n" << "Toplam: " << id2;
  #endif

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

1 2 3 4 5 6 7 8 9 10
Toplam: 220

```

Program, 1'den 10'a kadar olan sayıları ve bu sayıların 4 ile çarpımlarının toplamını ekrana yazar. id2 değişkeni ile ilgili işlem satırlarının derlenerek çalışmasının nedeni, programda MAK01 adlı bir makronun tanımlanmamış olmasıdır.

Kısaca özetlemek gerekirse, #ifdef direktifi içinde yer alan işlem satırlarının derlenmesi için direktif içinde geçen makronun mutlaka program içinde tanımlanmış olması, #ifndef direktifi ile ilgili işlem satırlarının derlenmesi için ise, direktif içinde geçen makronun tanımlanmamış olması gerekir.

## #error, #undef, #line ve #pragma önişlemci direktifleri

#error direktifinin genel yapısı aşağıda gösterilmektedir:

```


#error hata-mesajı


```

#error direktifi derleyicinin çalışmasını durdurur ve hata ile ilgili bilgileri içeren hata mesajını verir. Derleyici bir dosya içinde #error ifadesini gördüğünde derleme işlemi sona erer. #error direktifini bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

int main(void)
{
  int id;

  cout << "Bir int değer giriniz: ";
  cin >> id;

  #error Programda hata var! // 1
  cout << id;

  return 0;
}


```

Program, derleyici tarafından derlenmez. Derleyici #error direktifini görür görmez, derleme işlemini sona erdirir.

#undef direktifinin genel yapısı aşağıda gösterildiği şekildedir:

```


#undef makro-adı


```

#undef direktifi tanımlanmış bir makro adını geçersiz hale getirir. Yani, #undef direktifi ile geçersiz hale getirilen bir makroya, derleyici program tarafından daha önce tanımlanan makroya hiç tanımlanmamış gibi işlem yapar. Eğer, makro adı tanımlanmamışsa #undef direktifinin herhangi bir etkisi olmaz.

Şimdi, #undef direktifinin kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

#define MAK01 21

int main(void)
{
  #undef MAK01

  #ifdef MAK01
     cout << "MAK01 değeri: " << MAK01;
  #endif

  #ifndef MAK01
     cout << "MAK01 makrosu tanımlanmamıştır!";
  #endif

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

MAK01 makrosu tanımlanmamıştır!

```

Program, MAK01 makrosunu main() fonksiyonundan önce tanımlar. Ancak, MAK01 makro tanımlaması #undef direktifi ile geçersiz hale getirildiğinden, #ifdef direktifi ile ilgili işlem satırı derleyici tarafından derlenmez, sadece #ifndef direktifi ile ilgili işlem satırı derlenir.

#line direktifinin genel yapısı aşağıda gösterilmektedir:

```


#line satır-numarası "dosya-adı"


```

Bir derleyici, bir dosyayı derlerken 2 çeşit bilgi içerir:

1. Derlenmekte olan satırın numarası
2. Derlenmekte olan kaynak dosyanın adı

#line direktifi bu 2 değeri değiştirmek için kullanılır. Başka bir ifade ile, birazdan inceleyeceğimiz \_\_LINE\_\_ ve \_\_FILE\_\_ makrolarının içeriğini değiştirmeye yarar.

#line direktifinin kullanılmasında, satır-numarası ifadesi dosya içinde derlenecek olan ilk satır numarasını verir. satır-numarası ifadesinin değeri 1 ile 32767 arasında olmalıdır. dosya-adı ifadesi ise derlenen dosya adıdır. Dosya adı, işletim sistemine göre verilen bir dosya adıdır. Dosya adının tanımlanması isteğe bağlıdır.

Örnek

```c++
#include <iostream>

using namespace std;

#line 40
                     // 40
int main(void)       // 41
{                    // 42
  cout << __LINE__;  // 43

  return 0;
}


```

Yukarıdaki örnekte, program aşağıdaki değeri ekrana yazar:

```

43

```

Program, line direktifi kendisinden sonra gelen kod satırının numarasını 40 değerine ayarlar. Bundan dolayı cout fonksiyon satırında satır numarası 43 olarak ekrana yazılır.

#pragma direktifi, bir derleyiciye ek bilgi göndererek derleyicinin belirli özelliklerini kontrol eden, dilin standartları tarafından tanımlanmış özel derleyici komutlarıdır. Bu direktifi kullanarak programlara özel direktifler verebiliriz. #pragma direktifleri bilgisayar, işletim sistemi ve derleyiciye bağlı olarak değişebilir. Bu direktifin genel yapısı aşağıda gösterilmektedir:

```


#pragma pragma-adı


```

pragma-adı ifadesi kullanılacak olan direktifin adını gösterir. Eğer derleyici tanımadığı bir #pragma ifadesi ile karşılaşırsa, onu dikkate almaz.

#pragma direktiflerinin sayısı derleyicilere göre değişebilir.

## Ön tanımlı makrolar

ANSI C standartlarına uygun bütün derleyicilerde en az 5 adet önceden tanımlanmış makro bulunur. Bu makrolar aşağıda gösterilmektedir:

\_\_LINE\_\_ : Derlenmekte olan satırın numarasını taşıyan int bir değerdir.

\_\_FILE\_\_ : Derlenmekte olan dosyanın adını gösteren bir karakter dizisidir.

\_\_DATE\_\_ : Sistemin tarihini gösteren bir karakter dizisidir. Genel yapısı : ay/gün/yıl

\_\_TIME\_\_ : Programın derleme başlangıcındaki zamanı gösteren bir karakter dizisidir. Genel yapısı : Saat:Dakika:Saniye

\_\_STDC\_\_ : Eğer derleyici ANSI standardına uygun ise 1 olarak tanımlanır.

Yukarıda bahsi geçen makroları #undef direktifini kullanarak geçersiz hale getiremeyiz.

Şimdi, öğrendiklerimizi bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

int main(void)
{
  int id;

  for (id=0; id<10; id++) cout << id+1 << " ";

  cout << "\nDerlenen dosya: " << __FILE__ << "\n";
  cout << "Derlenen satır: " << __LINE__ << "\n";
  cout << "Derleme tarihi: " << __DATE__ << "\n";
  cout << "Derleme zamanı: " << __TIME__;
  
  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

1 2 3 4 5 6 7 8 9 10 
Derlenen dosya: C:\CppProgs\deneme\main.cpp
Derlenen satır: 14
Derleme tarihi: Dec 26 2020
Derleme zamanı: 19:34:07

```

Program, 1'den 10'a kadar olan sayıları ekrana yazar. Sonra, derlenen dosya adını, derlenen satır sayısını, derleme tarihini ve zamanını ekrana yazar. Derlenen dosya adı ile derleme tarih ve zamanı her bilgisayarda farklı değerler alacaktır.

## # ve ## işlemcileri

\# işlemcisi, fonksiyona benzeyen makroların argümanını tırnak içinde bir karakter dizisi olarak geri verir.

\## işlemcisi iki tanımlayıcıyı birleştirir.

\# ve ## işlemcilerinin kullanılmasını örnekler üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

#define MAK01(id1) #id1

int main(void)
{
  int id2;

  id2 = 21;

  cout << MAK01(id2) << " değişken değeri: " << id2; // MAK01(id2) = "id2"

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

id2 değişken değeri: 21

```

Program, cout fonksiyonundaki MAK01(id2) ifadesinin yerine "id2" ifadesini koyar.

Örnek

```c++
#include <iostream>

using namespace std;

#define MAK01(id1) cout << (id1 ## 1) + (id1 ## 2)

int main(void)
{
  int id1, id2;

  id1 = 12;
  id2 = 25;

  MAK01(id); // = cout << id1+id2;

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

37

```

Program, MAK01 makrosu için argüman olarak verilen ifadeye 1 ve 2 karakterlerini ayrı ayrı ekleyerek elde ettiği 2 değişken toplamını ekrana yazar.
