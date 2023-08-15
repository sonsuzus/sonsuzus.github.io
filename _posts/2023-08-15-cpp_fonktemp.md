---
title:  C++ Fonksiyon şablonları
author: sonsuz
date: 2023-08-15 21:26:56 +0300
categories: [Program,C++]
tags: [cpp,programlama,fonksiyon,şablonlar]
---



Bir fonksiyon şablonu, çeşitli veri türlerine uygulanacak genel bir işlem grubunu tanımlar. Fonksiyonun üzerinde çalışacağı veri türü fonksiyona bir parametre olarak aktarılır. Fonksiyon şablonu ile, geniş bir veri yelpazesine tek bir genel kod yapısı uygulanabilir. Farklı veri türlerine aynı kodlarla işlem yapılması gerektiğinde fonksiyon şablonlarını kullanılması büyük kolaylık sağlar.

Bir fonksiyon şablonu template ve typename anahtar kelimeleri ile oluşturulur. Fonksiyon şablonu bildirimi için kullanılan genel yapı aşağıda gösterilmektedir:

```

template <typename T> veri-türü fonk-adı(parametreler)
{
  // kod bloğu
}

```

Fonksiyon şablon bildiriminde typename yerine class anahtar kelimesi de kullanılabilir. Her iki anahtar kelime de aynı işlemi yapar.

Burada T ifadesi, fonksiyon tarafından kullanılan bir veri türü için bir yer tutucu adını gösterir. Bu isim, fonksiyon tanımında kullanılabilir. Ancak, derleyicinin fonksiyonun belirli bir sürümünü oluşturduğunda otomatik olarak gerçek veri türüyle değiştireceği bir yer tutucudur.

## Tek parametre değeri alan şablon fonksiyonlar

Şablon fonksiyon bildiriminde typename T şeklinde yer alan her bir ifade fonksiyon parametrelerinde aynı anda kullanılabilecek bir veri türü için ayrılan bir yer olarak kabul edilebilir. Eğer tek bir tür tanımlaması yaparsak, fonksiyon parametrelerinde ve fonksiyon kod bloğu içinde, aynı anda sadece tek bir veri türü kullanılabilmektedir.

Kendisine geçirilen parametre değerinin karesini alan bir şablon fonksiyonunun kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

// Şablon fonksiyon tanımlama
template <typename t> void kare_al(t x)
{
  cout << "Değerin karesi = " << x * x << endl;
}

int main(void)
{
  kare_al(21);      // int değerin karesi
  kare_al(115.84f); // float değerin karesi
  
  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Değerin karesi = 441
Değerin karesi = 13418.9

```

Program, önce aynı veri türünden aldığı parametre değerinin karesini ekrana yazan kare\_al() adlı bir şablon fonksiyonu tanımlar. Şablon fonksiyonunu önce int değer sonra float bir değer ile çağırarak, fonksiyona geçirilen değerlerin karesini ekrana yazar.

Program çalıştığında yapılan fonksiyon çağrılarının veri türü değişimine göre oluşturulan fonksiyon yapıları aşağıdaki şekilde gösterilmektedir.

![](cprog/tempfonk01.png)

Şablon fonksiyon tanımlamasındaki `<typename t>` ifadesi, aynı anda sadece tek bir veri türü ile işlem yapılabileceğini göstermektedir.

## Çoklu parametre değeri alan şablon fonksiyonlar

Şablon fonksiyon bildiriminde typename T şeklinde tek bir ifade yer alıyorsa, aynı anda tek bir veri türü kullanılabileceğinden, fonksiyon parametrelerinin sayısı birden fazla olsa bile, her parametre için aynı anda sadece tek bir veri türü kullanılabilmektedir.

Aynı veri türünden iki parametre ile toplama işlemi yapan bir şablon fonksiyonunun kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

// Şablon fonksiyon tanımlama
// Şablon fonksiyona geçirilen her iki parametre aynı veri türünden olmalıdır.
template <typename t> void topla(t x, t y)
{
  cout << "Değerlerin toplamı = " << x + y << endl;
}

int main(void)
{
  topla(21, 57);           // 2 adet int değer toplama işlemi
  topla(174.84f, 321.52f); // 2 adet float değer toplama işlemi

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Değerlerin toplamı = 78
Değerlerin toplamı = 496.36

```

Program, önce aynı veri türünden iki parametre alarak toplamını ekrana yazan topla() adlı bir şablon fonksiyonu tanımlar. Şablon fonksiyonunu önce iki adet int değer sonra iki adet float değer ile çağırarak, fonksiyona geçirilen değerlerin toplamını ekrana yazar.

Şablon fonksiyon tanımlamasındaki `<typename t>` ifadesi, birden fazla parametre kullanılsa bile, aynı anda sadece tek bir veri türü ile işlem yapılabileceğini göstermektedir.

## Farklı veri türünde çoklu parametre değeri alan şablon fonksiyonlar

Şablon fonksiyon bildiriminde typename T şeklinde birden fazla ifade yer alıyorsa, aynı anda birden fazla veri türü kullanılabileceğinden, parametreler için aynı anda birden fazla veri türü kullanılabilmektedir. Fonksiyon tanımına eklenen her bir tür ifadesi aynı anda kullanılabilecek veri türü miktarını artırır.

Farklı veri türünden iki parametre ile toplama işlemi yapan bir şablon fonksiyonunun kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

// Şablon fonksiyon tanımlama
// Şablon fonksiyona geçirilen parametreler aynı veya farklı veri türünden olabilir.
template <typename t1, typename t2> void topla(t1 x, t2 y)
{
  cout << "Değerlerin toplamı = " << x + y << endl;
}

int main(void)
{
  topla(36, 73);          // İki adet int değer toplama
  topla(14.48f, 648.34f); // İki adet float değer toplama
  topla(79, 321.52f);     // Birer adet int ve float değer toplama

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Değerlerin toplamı = 109
Değerlerin toplamı = 662.82
Değerlerin toplamı = 400.52

```

Program, önce aynı veya farklı veri türünden iki parametre alarak toplamını ekrana yazan topla() adlı bir şablon fonksiyonu tanımlar. Şablon fonksiyonunu sırasıyla iki adet int değer, iki adet float değer ve bir int ve bir float değer ile çağırarak, fonksiyona geçirilen değerlerin toplamını ekrana yazar.

Şablon fonksiyon tanımlamasındaki `<typename t1, typename t2>` ifadesi, aynı anda iki veri türü ile işlem yapılabileceğini göstermektedir.

## Şablon fonksiyonları çoklu görev tanımlama (overloading) işlemi

Şablon fonksiyonlarında, tek bir veri türü için veya komple çoklu görev tanımlama (overloading) işlemi uygulayabiliriz. Tek bir veri türü için çoklu görev tanımlama işlemi uygulandığında, ilgili veri türü ile yapılan fonksiyon çağrılarında, yeni bildirimi yapılan fonksiyon devreye girer. Komple çoklu görev tanımlama işleminde ise, fonksiyon yapısında, örneğin parametre sayısı, yapılan değişiklikle şablon fonksiyonunun tamamı değişir.

## Şablon fonksiyonlarında veri türü için çoklu görev tanımlama (overloading) işlemi

Normal koşullarda, şablon fonksiyonları kendisine aktarılan parametrelerin veri türüne bağlı olarak kendisine çoklu görev tanımlama işlemi uygular ve gerekli kodları çalıştırır. İhtiyaç duyulduğunda, şablon fonksiyonlarına program içinde ayrıca çoklu görev tanımlama işlemi uygulanabilir. Bu yöntemle çoklu görev tanımlama işlemi uygulandığında, yeni tanımlanan fonksiyon aynı veri türüne sahip parametrelerle işlem yapan şablon fonksiyonunu devre dışı bırakır.

Şablon fonksiyonlarına çoklu görev tanımlama işlemi, parametre veri türü esasına bağlı olarak yapılır.

Şablon fonksiyonlarını veri türü için çoklu görev tanımlama işlemi bildirimi normal fonksiyon bildirimi veya şablon fonksiyon bildirimi benzeri yöntemlerinden birisi ile yapılabilir. Her iki yöntemde aynı sonucu verir.

## Şablon fonksiyonlarını veri türü için normal fonksiyon bildirimi ile çoklu görev tanımlama işlemi

Bu yöntemde, yeni yapılan fonksiyon bildiriminde, şablon fonksiyonunda class ifadesinden sonra ve parametre bölümünde yer alan veri türü için ayrılmış değerler yerine, doğrudan veri türü yazılır.

```c++
template <typename t> void topla(t x, t y)
{
  // kod bloğu
}

// Çoklu görev tanımlama işlemi
void topla(int x, int y)
{
  // kod bloğu
}

```

Aynı veri türünden iki parametre ile toplama işlemi yapan bir şablon fonksiyonuna int veri türü için çoklu görev tanımlama işlemi uygulayan bir örneği incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

// Şablon fonksiyon tanımlama
// Şablon fonksiyona geçirilen her iki parametre aynı veri türünden olmalıdır.
template <typename t> void topla(t x, t y)
{
  cout << "Şablon fonksiyonu değerlerin toplamı = " << x + y << endl;
}

// Şablon fonksiyonu çoklu görev tanımlama işlemi 
void topla(int x, int y)
{
  cout << "Çoklu görev tanımlama fonksiyon değerlerin toplamı = " << x + y << endl;
}

int main(void)
{
  topla(175, 542);         // Çoklu görev tanımlama işlemi ile elde edilen fonksiyon çağrılır.
  topla(683.43f, 185.25f); // Orjinal şablon fonksiyonu çağrılır.

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Çoklu görev tanımlama fonksiyon değerlerin toplamı = 717
Şablon fonksiyonu değerlerin toplamı = 868.68

```

Program, önce aynı veri türünden iki parametre alarak toplamını ekrana yazan topla() adlı bir şablon fonksiyonu tanımlar. Sonra, şablon fonksiyonuna int veri türü için çoklu görev tanımlama işlemi uygular. Böylece, şablon fonksiyonuna int veri türü ile çağrı yapıldığında çoklu görev tanımlama işlemi ile elde edilen fonksiyon, float değer ile çağrı yapıldığında orjinal şablon fonksiyonu devreye girerek, fonksiyona geçirilen değerlerin toplamını ekrana yazar.

## Şablon fonksiyonlarını veri türü için şablon fonksiyon benzeri bildirim ile çoklu görev tanımlama işlemi

Bu yöntemde, yeni yapılan fonksiyon bildiriminde, şablon fonksiyonunun benzeri bir yapı kullanılarak, `<class t>` ifadesi yerine ve parametre bölümündeki t ifadeleri yerine doğrudan veri türü olan int ifadesi yazılır.

```

template <typename t> void topla(t x, t y)
{
  // kod bloğu
}

// Çoklu görev tanımlama işlemi
template <int> void topla(int x, int y)
{
  // kod bloğu
}

```

Şimdi, yukarıdaki örnekte yapılan çoklu görev tanımlama işleminin template anahtar kelimesini kullanılarak yapılmasını gösteren bir örneği incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

// Şablon fonksiyon tanımlama
// Şablon fonksiyona geçirilen her iki parametre aynı veri türünden olmalıdır.
template <typename t> void topla(t x, t y)
{
  cout << "Şablon fonksiyonu değerlerin toplamı = " << x + y << endl;
}

// Şablon fonksiyonu çoklu görev tanımlama işlemi
template <int> void topla(int x, int y)
{
  cout << "Çoklu görev tanımlama fonksiyon değerlerin toplamı = " << x + y << endl;
}

int main(void)
{
  topla(254, 348);         // Çoklu görev tanımlama işlemi ile elde edilen fonksiyon çağrılır.
  topla(121.35f, 287.84f); // Orjinal şablon fonksiyonu çağrılır.

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Şablon fonksiyonu değerlerin toplamı = 602
Şablon fonksiyonu değerlerin toplamı = 409.19

```

Program, önce aynı veri türünden iki parametre alarak toplamını ekrana yazan topla() adlı bir şablon fonksiyonu tanımlar. Sonra, şablon fonksiyonuna int veri türü için şablon fonksiyon yapısına benzer bir yapı ile çoklu görev tanımlama işlemi uygular. Böylece, şablon fonksiyonuna int veri türü ile çağrı yapıldığında çoklu görev tanımlama işlemi ile elde edilen fonksiyon, float değer ile çağrı yapıldığında orjinal şablon fonksiyonu devreye girerek, fonksiyona geçirilen değerlerin toplamını ekrana yazar.

## Şablon fonksiyonlarının tamamı için çoklu görev tanımlama (overloading) işlemi

Şablon fonksiyonları için komple çoklu görev tanımlama işlemi yapıldığında, fonksiyon yapısı tamamen değişir. Bu değişiklik fonksiyonun parametre sayısı ve geri döndürdüğü veri türü gibi değerler olabilir.

Aynı veri türünden iki parametre ile toplama işlemi yapan bir şablon fonksiyonuna, farklı veri türünden iki parametre ile toplamı işlemi yapan bir fonksiyon ile çoklu görev tanımlama işlemi uygulayan bir örneği incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

// Şablon fonksiyon tanımlama
// Şablon fonksiyona geçirilen her iki parametre aynı veri türünden olmalıdır.
template <typename t> void topla(t x, t y)
{
  cout << "Şablon fonksiyonu değerlerin toplamı = " << x + y << endl;
}

// Şablon fonksiyona geçirilen her iki parametre ayrı veri türünden olmalıdır.
template <typename t1, typename t2> void topla(t1 x, t2 y)
{
  cout << "Çoklu görev tanımlama fonksiyonu değerlerin toplamı = " << x + y << endl;
}

int main(void)
{
  topla(147, 724);        // Orjinal şablon fonksiyonu çağrılır.
  topla(45.87f, 315.65f); // Orjinal şablon fonksiyonu çağrılır.  
  topla(912, 824.75f);    // Çoklu görev tanımlama işlemi ile elde edilen fonksiyon çağrılır.
  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Şablon fonksiyonu değerlerin toplamı = 871
Şablon fonksiyonu değerlerin toplamı = 361.52
Çoklu görev tanımlama fonksiyonu değerlerin toplamı = 1736.75

```

Program, önce aynı veri türünden iki parametre alarak toplamını ekrana yazan topla() adlı bir şablon fonksiyonu tanımlar. Sonra, şablon fonksiyonuna komple çoklu görev tanımlama işlemi uygulayarak, iki farklı veri türünden iki parametre alarak toplamını ekrana yazan ikinci bir fonksiyon oluşturur. İlk fonksiyon çağrısında, iki adet int değer kullanıldığından orjinal şablon fonksiyonu, ikinci fonksiyon çağrısında, iki adet float değer kullanıldığından yine orjinal şablon fonksiyonu, üçüncü fonksiyon çağrısında ise, bir int ve bir float değer ile çağrı yapıldığından, çoklu görev tanımlama işlemi ile elde edilen fonksiyon çağrılır. Her iki fonksiyon çağrısı, fonksiyona geçirilen değerlerin toplamını ekrana yazar.

## Şablon fonksiyonlarda sabit veri türü parametreleri

Normal koşullarda, şablon fonksiyonlar parametrelerinin veri türlerini kullanıcıların fonksiyon çağrısında kullandıkları veri türüne uygun olarak belirler ve verilere uygun olan fonksiyonu kullanırlar. Ancak, bazı durumlarda, şablon fonksiyonlara değişken veri türüne sahip parametrelerin yanı sıra sabit bir veri türünden parametre değeri geçirmek gerekebilir. Şablon fonksiyon bildiriminde bu şekildeki parametreler için belirli bir veri türünden tanımlama yapılır.

Kendisine geçirilen değişken veri türündeki parametre değerinin kuvvetini yine kendisine geçirilen sabit veri türündeki değer kadar alan bir şablon fonksiyonunun kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

// Sabit veri türünden parametre içeren şablon fonksiyon bildirimi
template <typename t> void bg_pow(t x, int y)
{
  t sonuc;
  int id;

  if (y==0) sonuc = 1;
  else {
     sonuc = x;
	 for (id=2; id<=y; id++) sonuc *= x;
  }

  cout << x << " değerinin " << y << ". kuvveti = " << sonuc << endl;
}

int main(void)
{
  bg_pow(5, 3);     // int bir değerin 3.kuvveti
  bg_pow(5, 0);     // int bir değerin 0.kuvveti
  bg_pow(12.47, 5); // float bir değerin 5.kuvveti

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

5 değerinin 3. kuvveti = 125
5 değerinin 0. kuvveti = 1
12.47 değerinin 5. kuvveti = 301531

```

Program, önce kendisine geçirilen değişken veri türündeki ilk parametre değerinin kuvvetini yine kendisine geçirilen sabit veri türündeki (int) değer kadar alan bir şablon fonksiyonunun bildirimini yapar. Şablon fonksiyonunu iki kez ilk parametre değeri int veri türü ve bir kez de float veri türü çağırır. Her üç çağrıda da fonksiyona geçirilen ikinci parametre int veri türündendir. Fonksiyon ilk parametre değerinin ikinci parametre değeri kadar kuvvetini alarak ekrana yazar.

## Şablon fonksiyonlarla çoklu görev tanımlama yöntemi uygulanmış fonksiyon karşılaştırması

Şablon fonksiyonlarla çoklu görev tanımlama yöntemi uygulanmış fonksiyonlar bazı benzerlikler göstermektedir. Bu iki yöntem aşağıdaki tabloda birbiri ile karşılaştırılmaktadır.

| Özellik | Şablon fonksiyonlar | Çoklu görev tanımlama fonksiyonları |
| --- | --- | --- |
| Bildirim | Tek fonksiyon bildirimi tüm veri tipleri için fonksiyon tanımlamaya yeterlidir. | Her bir veri türü için ayrı bir fonksiyon bildirimi gerekir. |
| İşlemler | Aynı isme sahip fonksiyonların hepsi aynı işlemleri yapar. | Aynı isme sahip fonksiyonların her biri farklı işlemler yapabilir. |
| Parametre | Farklı parametre veri türleri için tek bir bildirim yeterlidir. | Her bir parametre veri türü için ayrı bir bildirim gerekir. |
| Çağrılma esası | Derleyici, fonksiyon çağrısında kullanılan parametre veya parametrelerin veri türlerine göre hangi fonksiyonun kullanılacağına karar verir. | Derleyici, fonksiyon çağrısında kullanılan parametre sayısı, sırası ve veri türlerine göre hangi fonksiyonun kullanılacağına karar verir. |

Aynı veri türünden iki parametre ile toplama işlemi yapan bir şablon fonksiyonu ile çoklu görev tanımlama işlemi yapılmış fonksiyonların kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

// Şablon fonksiyon tanımlama
// Şablon fonksiyona geçirilen her iki parametre aynı veri türünden olmalıdır.
template <typename t> void topla_sablon(t x, t y)
{
  cout << "Değerlerin toplamı = " << x + y << endl;
}

// topla_overload() fonksiyonunun 2 farklı veri türünde
// parametre ile bildirimi yapılarak çoklu görev tanımlama işlemi
int topla_overload(int id1, int id2)
{
  return id1 + id2;
}

float topla_overload(float fd1, float fd2)
{
  return fd1 + fd2;
}

int main(void)
{
  // Şablon fonksiyon çağrıları
  topla_sablon(154, 521);         // 2 adet int değer toplama işlemi
  topla_sablon(162.73f, 725.34f); // 2 adet float değer toplama işlemi

  // 2 adet int değer parametre ile çoklu görev tanımlama işlemi yapılmış fonksiyon çağrısı
  cout << "int değer toplamları: "<< topla_overload(21, 251) << endl;

  // 2 adet float değer parametre ile çoklu görev tanımlama işlemi yapılmış fonksiyon çağrısı
  cout << "float değer toplamları: " << topla_overload(15.83f, 134.45f) << endl;

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Değerlerin toplamı = 675
Değerlerin toplamı = 888.07
int değer toplamları: 272
float değer toplamları: 150.28

```

Program, önce aynı veri türünden iki parametre alarak toplamını ekrana yazan topla() adlı bir şablon fonksiyon ile aynı işlemi int ve float veriler için yapan iki adet fonksiyon tanımlar. Şablon fonksiyonu önce iki adet int sonra iki adet float değer ile çağırarak, fonksiyona geçirilen değerlerin toplamını ekrana yazar. Sonra, aynı işlemleri çoklu görev tanımlama işlemi yapılmış fonksiyonlarla yapar.

## Değişken sayıda parametre alan fonksiyon şablonları (C++11)

C++11 sürümünden önce, şablonların, bildirim esnasında tanımlanması gereken sabit sayıda parametresi vardı. Şablonlar, değişken sayıda parametresi olan fonksiyon şablonu oluşturmak için kullanılamazdı.

C++11 sürümü ile birlikte gelen değişken parametre sayılı şablonlar özelliği ile, sıfır da dahil olmak üzre, herhangi bir sayıda parametreye sahip fonksiyon şablonları tanımlayabiliriz.

Fonksiyon şablonlarında, değişken sayıda tanımlanan parametrelerle ilgili işlemler çalışma zamanında değil derleme zamanında yapılır.

Bir parametre paketi, şablonlar için herhangi bir veri türünden bir parametre olabilir. Değişken parametre sayılı şablonlarda, 0 veya daha fazla parametre içeren ve ... ifadesi ve tek bir parametre adı ile temsil edilen parametre paketi (parameter pack) kavramı kullanılmaktadır.

Şablon tanımında, bir parametre paketi tek bir parametre olarak ele alınır. Parametre paketinin içinde tanımlandığı şablona çağrı yapıldığında, parametre paketi genişletilir ve çağrı yapıldığında kullanılan parametre sayısı kadar tanımlanan veri türüne göre parametre oluşturulmaktadır.

Değişken sayıda parametre içeren fonksiyon şablonu template anahtar kelimesi ile birlikte kullanılan ... ifadesi ile oluşturulur. Değişken sayıda parametre içeren fonksiyon şablonu bildirimi için kullanılan iki farklı genel yapı aşağıda gösterilmektedir:

```

// Ana fonksiyon
template <typename T>
veri-türü fonk-adı(T t)
{
  // Fonksiyon kod bloğu
}
	
// Genel fonksiyon
template <typename T, typename... Params>
veri-türü fonk-adı(T par1, Params... params)
{
  // Fonksiyon kod bloğu	
}

```

Değişken sayıda parametre içeren fonksiyon şablonu tanımlamak için bir ana yapı fonksiyonu ile tekrar eden özelliği içeren genel yapı fonksiyonunun ayrı ayrı bildirimi yapılmalıdır.

Değişken sayıda parametre içeren şablon fonksiyonu aşağıdaki şekilde çağırabiliriz:

```

veri-türü değişken-adı = fonk-adı(par1, par2, par3, ...);

```

Kendisine geçirilen parametreleri toplayarak geri döndüren değişken sayıda parametre içeren bir fonksiyon şablonunun kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include<iostream>

using namespace std;

// Değişken sayıda parametre alan şablon fonksiyon bildirimi
// Ana fonksiyon
template<typename T>
T topla(T t) {
  cout << "Ana fonksiyon içeriği" << endl;
  return t;
}
// Tekrar eden fonksiyon
template <typename T, typename... Params>
T topla(T par1, Params... params)
{
  return par1 + topla(params...);
}

int main(void)
{
  cout << topla(7, 21, 35, 42, 54, 102) << endl;  // int değerler ile fonksiyon çağrısı
  
  cout << endl;

  string str1 = "Karakter ", str2 = "dizisi ", str3 = "fonksiyon ", str4 = "çağrısı";
  cout << topla(str1, str2, str3, str4) << endl;  // Karakter dizisi ile fonksiyon çağrısı

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Ana fonksiyon içeriği
261
Ana fonksiyon içeriği
Karakter dizisi fonksiyon çağrısı

```

Program, kendisine geçirilen parametreleri toplayarak geri döndüren değişken sayıda parametre içeren bir fonksiyon şablonunu tanımlar. Önce, altı adet int değeri parametre olarak geçirerek fonksiyonu çağırır. Fonksiyon her defasında bir parametreye işlem yapacak şekilde, kendi kendini çağırarak tüm değerlerin toplamını elde ederek geri döndürür. Sonra, aynı fonksiyonu dört adet karakter dizisi ile çağırır. Fonksiyon aynı işlemi yaparak, karakter dizilerini birbirine ekleyerek geri döndürür.

Programda ana fonksiyon, tekrar eden fonksiyonun her çağrılmasından önce bir kez çağrılır.

Şimdi, kendisine geçirilen parametreleri sırasıyla ekrana yazan değişken sayıda parametre içeren bir fonksiyon şablonunun kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include<iostream>

using namespace std;

// Değişken sayıda parametre alan şablon fonksiyon bildirimi
// Ana fonksiyon
void deger_goster() {
  cout << "Ana fonksiyon içeriği" << endl;
}

// Tekrar eden fonksiyon
template <typename T, typename... Params>
void deger_goster(T t1, Params... params) {
   cout << t1 << endl;
   deger_goster(params...) ;
}

int main(void)
{
   deger_goster(21, 43.25, "Değişken sayıda parametre alan şablon fonksiyonlar");

   cout << endl;

   deger_goster(35, 51.42, 67, 71.12);

   return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

21
43.25
Değişken sayıda parametre alan şablon fonksiyonlar
Ana fonksiyon içeriği

35
51.42
67
71.12
Ana fonksiyon içeriği

```

Program, sırasıyla ekrana yazan değişken sayıda parametre içeren bir fonksiyon şablonunu tanımlar. Önce, birer adet int, float ve karakter dizisi değerini parametre olarak geçirerek fonksiyonu çağırır. Fonksiyon her defasında bir parametreye işlem yapacak şekilde, kendi kendini çağırarak tüm değerleri sırasıyla ekran yazar. Sonra, fonksiyonu ikişer adet int ve float değerlerle çağırarak aynı işlemleri tekrarlar.

Programda ana fonksiyon, tekrar eden fonksiyonun her çağrılmasından sonra bir kez çağrılır.
