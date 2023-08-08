---
title:  C++ Değişkenler
author: sonsuz
date: 2023-08-06 23:49:21 +0300
categories: [Program,C++]
tags: [cpp,değişken,programlama]
---


C++ dilinde bilgisayar belleğinin bir kısmına belirli bir isim vererek bu bellek alanını kendimiz için ayırabilir ve bu alana değerler yerleştirebiliriz. Bu değerleri de istediğimiz zaman değiştirebiliriz.

Bu işlemlere değişken bildirimi ve değişkene değer atama işlemleri diyoruz.

## Değişken bildirimi

Bir değişken bildirimi yaparak, bilgisayarın belleğinde belirli büyüklükte bir alanı kendimize ayırabiliriz. Bu bellek boyutu değişken veri türüne göre değişecektir. Bu işlemi yaptığımızda belleğin belirli bir bölümü bizim için ayrılmış olur.

Değişken bildirimi aşağıda gösterilen 3 farklı yerde yapılabilir:

1. Lokal değişkenler: Fonksiyonların içinde
2. Parametre olarak tanımlanan değişkenler: Fonksiyon parametresi olarak
3. Global değişkenler: Tüm fonksiyonların dışında

> C++ programlama dilinde, bir değişken ifade içinde kullanılmadan önce mutlaka bildirimi yapılmalı ve bir değer atanmalıdır. Bu bildirim işlemi, ister main() ister başka bir fonksiyon içinde olsun fonksiyonun veya kod bloğunun herhangi bir satırında yapılabilir.
{: .prompt-tip }

Bir değişken bildirimi aşağıdaki şekilde görüldüğü gibi yapılır:

veri-türü değişken-adı;

Değişken bildiriminin bir işlem satırı ile yapıldığından bahsetmiştik. Bu nedenle noktalı virgül (;) ile sona erer. veri-türü ifadesi bildirimi yapılan değişkeninin veri türünü, değişken-adı ifadesi ise değişkenin adını göstermektedir.

Değişken bildiriminde değişken-adı ifadesi yerine kullanılacak değişken adları, sizin verebileceğiniz herhangi bir ad olabilir. Bu ad harflerden, rakamlardan ve (\_) işaretinden oluşan bir karakter dizisi olmalıdır. C++, küçük ve büyük harflere farklı işlem yapar. FD ve fd olarak verilen değişken adları birbirinden tamamen farklı olarak kabul edilir.

Aşağıdaki işlem satırlarından birincisi id adlı int, ikincisi fd adlı float ve üçüncüsü dd adlı double bir değişken bildirimi yapar:

```c++
int id;
float fd;
double dd;


```

Değişken bildirimlerini, main() fonksiyonu da dahil olmak üzere, fonksiyonların başında veya herhangi bir satırında veya bütün fonksiyonların dışında olmak üzere kaynak kod dosyamızın başında veya herhangi bir satırında yapabiliriz.

Aynı türden olan birden fazla değişken bildirimini aynı işlem satırında yapabiliriz. Aşağıdaki işlem satırı id1, id2 ve id3 adlarında üç adet int değişken bildirimi yapar:

```c++
int id1, id2, id3;


```

## Lokal değişkenler

Eğer değişken bildirimini fonksiyonların yada kod bloklarının içinde yaparsak bu değişkenlere "lokal değişken" adı verilir.

Lokal değişkenlerin en önemli özelliği sadece tanımlanmış olduğu fonksiyonlar içinde geçerli olması ve bu fonksiyon tarafından kullanılabilmesidir. Lokal değişken bildirimi fonksiyonun içinde yapılır ve sadece içinde tanımlandığı fonksiyon çalıştığı sürece geçerlidir.

> Bir fonksiyon programın herhangi bir yerinden çağrıldığında, çağrılan fonksiyonun içindeki lokal değişkenler oluşturulur ve fonksiyonun son işlem satırına işlem yapıldıktan sonra yok edilirler.
{: .prompt-tip }

Aynı ada sahip olsalar bile, bir fonksiyondaki lokal bir değişkenin diğer bir fonksiyon içindeki lokal değişken ile herhangi bir ilgisi yoktur.

```c++
void fonk1(void)     void fonk2(void)
{                    {
  int id;              int id;

  işlem satırı;        işlem satırı;
  .                    .
  .                    .
  .                    .
  işlem satırı;        işlem satırı;
}                    }


```

Yukarıda gösterilen fonk1() ile fonk2() fonksiyonları içinde yer alan id adlı int değişkenleri birbirinden tamamen farklıdır ve birbiri üzerinde herhangi bir etkisi yoktur. Sadece tanımlandıkları fonksiyon içinde geçerlidirler.

Lokal değişkenlerle ilgili bahsettiklerimizi bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

void fonk1(void);
void fonk2(void);

int main(void)
{
  int id;

  id = 21; // Bu değişken sadece main() fonksiyonu içinde geçerlidir.
  cout << "main() fonksiyonu içindeki id değişken değeri: " << id << "\n";

  fonk1();
  fonk2();

  return 0;
}

void fonk1(void)
{
  int id;

  id = 175; // Bu değişken sadece fonk1() fonksiyonu içinde geçerlidir.
  cout << "fonk1() fonksiyonu içindeki id değişken değeri: " << id << "\n";
}

void fonk2(void)
{
  int id;

  id = 2178; // Bu değişken sadece fonk2() fonksiyonu içinde geçerlidir.
  cout << "fonk2() fonksiyonu içindeki id değişken değeri: " << id << "\n";
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

main() fonksiyonu içindeki id değişken değeri: 21
fonk1() fonksiyonu içindeki id değişken değeri: 175
fonk2() fonksiyonu içindeki id değişken değeri: 2178

```

Program biri direk diğer ikisi ise fonksiyon çağrısı yoluyla olmak üzere 3 farklı değişken değerini ekrana yazar. main(), fonk1() ve fonk2() fonksiyonlarının tamamında id adlı bir değişken yer almaktadır. Ancak, her üç değişkende, aynı ada sahip olmalarına rağmen, birbirinden tamamen farklı olup, içinde bulundukları fonksiyon içinde geçerlidir.

Fonksiyonlarda kod bloğu içinde tanımlanan lokal değişkenler

Bir fonksiyondaki kod bloklarının içinde tanımlanan değişkenler sadece o kod bloğu içinde geçerlidir. Bu değişken sadece tanımlandığı kod bloğu tarafından kullanılabilir, kod bloğu dışından değişkene erişim sağlanamaz.

Bu özelliği bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

int main(void)
{
  int id1=21;

  if (id1>0) {
      int id2 = id1 * id1;
      cout << "id1 değişken değeri: " << id1 << " id2 değişken değeri: " << id2 << "\n";
  }

  cout << "id1 değişken değeri: " << id1;
  // id2 değişkenine buradan erişim sağlanamaz. Program derleme hatası verir.
  // cout << " id2 değişken değeri: " << id2;

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

id1 değişken değeri: 21 id2 değişken değeri: 441
id1 değişken değeri: 21

```

Program, main() fonksiyonu içinde, id1 adlı bir değişken tanımlayarak 21 değerini atar. Bir if koşulu kod bloğu içinde, id2 adlı int bir değişken tanımlayarak id1 değişkeninin karesini bu değişkene atar ve her iki değişken değerini ekrana yazar. if koşulu dışında id1 değişken değerini tekrar ekrana yazar. Ancak, id2 değişkenine buradan erişim sağlayamaz, çünkü id2 değişkeni sadece if koşul bloğu içinde geçerlidir. Erişim sağlamaya çalıştığımızda, derleyici hata verir.

Bir fonksiyon içinde ve fonksiyonun içinde yer alan bir kod bloğu içinde aynı isme sahip değişken tanımlanırsa, bu değişkenler sadece tanımlandıkları kapsamda dikkate alınırlar. Bu değişken ismine kod bloğu dışından yapılan erişimlerde, fonksiyon içinde bildirimi yapılan değişken, kod bloğu içinden yapılan erişimlerde ise kod bloğu içinde bildirimi yapılan değişken esas alınır.

Bu özelliği bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

int main(void)
{
  int id=21; // main() fonksiyonu içinde geçerlidir.

  if (id>0) {
      int id = 35; // Kod bloğu içinde geçerlidir.
      cout << "Kod bloğu içindeki id değişken değeri: " << id << "\n";
  }

  cout << "main() fonksiyonu içindeki id değişken değeri: " << id;

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Kod bloğu içindeki id değişken değeri: 35
main() fonksiyonu içindeki id değişken değeri: 21

```

Program, main() fonksiyonu içinde, id adlı bir değişken tanımlayarak 21 değerini atar. Bir if koşulu kod bloğu içinde, yine id adlı int bir değişken tanımlayarak 35 değerini atar ve her iki değişken değerini ekrana yazar. if koşulu dışında id değişken değerini tekrar ekrana yazar.

## Fonksiyon parametre değişkenleri

Eğer bir fonksiyon kendisine aktarılan değerlere işlem yapacaksa, aktarılan değerlerin atanması için fonksiyon adından hemen sonra parantez içinde bir veya daha fazla değişken parametre tanımlanır. Bu değişkenlere fonksiyon parametre değişkenleri adı verilir.

Fonksiyon parametre değişkenleri fonksiyon lokal değişkenleri ile aynı özelliklere sahiptir. Tek farkları fonksiyona geçirilen değerlerin bu değişkenlere aktarılmasıdır.

> Fonksiyonlara bir parametre geçirdiğinizde de aslınızda lokal bir değişken tanımlamış olursunuz. Bir fonksiyonun parametresi olarak tanımlanmış olan lokal değişkenler, fonksiyon çağrıldığında fonksiyona geçirilen argümanların değerini alırlar. Bu değişkenlerde tıpkı lokal değişkenler gibi fonksiyon çağrıldığında oluşturulur ve fonksiyon sona erdiğinde yok edilirler.
{: .prompt-tip }

Bu özelliği bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

void carpim(int id1, int id2);

int main(void)
{
  int id1=21, id2=7;

  carpim(id1, id2);

  return 0;
}

void carpim(int id1, int id2)
{
  cout << "Çarpım sonucu: " << id1*id2;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Çarpım sonucu: 147

```

Program, id1 ve id2 adlı iki adet int değişken tanımlayarak 21 ve 7 değerlerini atar. Sonra, değişkenleri parametre olarak geçirerek, carpim() fonksiyonunu çağırır. Fonksiyon çağrılınca, fonksiyon parametreler yoluyla iki adet id1 ve id2 adlı lokal değişken oluşturarak, kemdisine parametre yoluyla geçirilen değişken değerlerini bu değişkenlere atar. Değişken değerlerini biribiryle çarparak elde ettiği sonucu ekrana yazar.

main() fonksiyonu içinde bildirimi yapılan id1 ve id2 değişkenleri, fonksiyon bildiriminde parametre olarak bildirimi yapılan id1 ve id2 değişkenleri ile tamamen farklıdır.

## Global değişkenler

Eğer bir değişken bildirimini bütün fonksiyonların dışında ve kaynak dosyamızın içinde yaparsak bu değişkenlere global değişken adı verilir. Global değişken bildirimlerinin kaynak dosyamızın başında yapılması kod takibi açısından kolaylık sağlar.

Global değişkenlere main() fonksiyonu da dahil olmak üzere bütün fonksiyonlar erişim sağlayabilir.

Bu değişkenlere, main() fonksiyonu veya diğer fonksiyonların işlem satırından herhangi bir işlem yapabiliriz. Global değişkenler kaynak dosyamızın içinde tanımlandığından, programın çalışması sona erene kadar varlıklarını sürdürürler.

Global değişkenler bir program çalıştığı sürece varlıklarını sürdüreceklerinden sürekli bellekte kaplarlar. Bu nedenle, sadece ihtiyaç olduğunda, lobal değişkenleri kullanmak daha doğru bir tercih olacaktır.

Örnek

```c++
#include <iostream>

using namespace std;

int gid; // Global değişken bildirimi

int deger_ekle(int id);

int main(void)
{
  int id;

  id = 21;
  gid = 35; // Global değişkene erişim

  cout << "id değişken değeri: " << id << " gid değişken değeri: " << gid << "\n";

  cout << "deger_ekle() fonksiyon sonucu: " << deger_ekle(247);

  return 0;
}

int deger_ekle(int id)
{
  return id + gid; // Global değişkene erişim
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

id değişken değeri: 21 gid değişken değeri: 35
deger_ekle() fonksiyon sonucu: 282

```

Program, gid adlı global int bir değişken ve main() fonksiyonu içinde id adlı lokal bir değişken bildirimi yapar. id değişkenine 21 değerini gid değişkenine ise 35 değerini atar. Her iki değişken derğerini ekrana yazdıktan sonra, 247 değerini parametre olarak geçirerek deger\_ekle() fonksiyonunu çağırır. Fonksiyon içinde parametre değeri ile gid değişken değerini toplar ve elde ettiği değeri geri döndürerek ekrana yazar. Global değişkene main() ve deger\_ekle() fonksiyonları içinden erişim sağlanmaktadır.

> Bir fonksiyon veya bir kod bloğu içinde bildirimi yapılan lokal değişken adı global değişken adı ile aynı olursa, fonksiyon veya kod bloğu içinde bu değişken adı ile ilgili işlemler doğrudan lokal değişkeni etkiler. Global değişkeni etkilemez.
{: .prompt-warning }

Şimdi, bu özelliği bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

int id=7; // Global değişken bildirimi

void deger_goster(void);

int main(void)
{
  int id; // Lokal değişken bildirimi

  id = 21;

  cout << "main fonksiyonu içindeki id değişken değeri: " << id << "\n";

  deger_goster();

  return 0;
}

void deger_goster(void)
{
  int id; // Lokal değişken bildirimi

  id = 35;

  cout << "deger_goster() fonksiyonu içindeki id değişken değeri: " << id;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

main fonksiyonu içindeki id değişken değeri: 21
deger_goster() fonksiyonu içindeki id değişken değeri: 35

```

Program, biri global, diğer ikisi main() fonksiyonu ve deger\_goster() fonksiyonu içinde olmak üzere toplam üç adet id adlı int değişken bildirimi yapar. main() fonksiyonu içinde id değişkenine 21 değerini atayarak, deger\_goster() fonksiyonu içinde de 35 değerini atayarak değişken değerlerini ekrana yazar. id lokal değişkenlerine main() ve deger\_goster() fonksiyonları içinde yapılan değişiklikler global id değişkenini etkilemez.

Global değişkenlere herhangi bir ilk değer atanmadığında, otomatik olarak 0 (sıfır) değeri atanır. Lokal değişkenlere ise bir ilk değer atanmadığında, kendiliğinden herhangi bir değer atanmaz.

## Değişkenlere ilk değer atama

Önce, değer atanmamış bir lokal değişken değerini ekrana yazdırmak istediğimizde nasıl bir sonuç aldığımızı görmek için aşağıdaki örneği inceleyelim:

Örnek

```c++
#include <iostream>

using namespace std;

int main(void)
{
  int id;

  cout << id; // Derleyici uyarı verir.

  return 0;
}


```

Yukarıdaki örneği derlediğimizde, derleyici uyarı verir. Programı çalıştırdığımızda, ekrana hiçbir anlamı olmayan çok farklı bir sayı yazar. Bu değerin ekrana yazılmasının nedeni henüz değişkene bir değer atanmamış olmasıdır. Şimdi, bildirimi yapılan değişkenlere bir değer atama işlemini incelemeye çalışalım.

Lokal bir değişkene değer vermeden kullandığımızda, belirsiz sonuçlara neden olur.

Bir değişken bildirimi ile yapılan ilk değer atama işlemi aşağıdaki şekilde yapılır:

veri-türü değişken-adı = sabit;

```


int id = 1354;


```

Bir değişkene değer atamak için işlem satırında önce değişkenin adı, sonra eşit işareti (=) ve en son olarak atanacak değer yazılır.

Bir değişken bildirimi ve bu değişkene değer atama işlemi iki ayrı satırda yapılabileceği gibi tek işlem satırında da yapılabilir. Aşağıda yer alan ilk işlem satırı id adlı bir değişken bildirimi yapar ve ikinci işlem satırı id değişkenine 537 değerini atar. Üçüncü işlem satırı ise, id2 adlı int bir değişken bildirimi yaparken değişkene 751 değerini atayarak, üstteki iki satırın yaptığı işlemi tek işlem satırında gerçekleştirir.

```c++
int id1;   // Değişken bildirim satırı
id1 = 537; // Değişkene değer atama satırı

int id2 = 751; // Değişken bildirimi ve değer atama işlemi aynı satırda yapılır.


```

Sonuç olarak, bir değişkene ya ilk bildirildiğinde, ya da daha sonra bir değer atanabilir.

Değişkenlere ilk değer atama işlemini bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

int main(void)
{
  char cd = 'A';
  int id = 21;

  cout << "cd değişken değeri: " << cd << "\n";
  cout << "id değişken değeri: " << id;

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

cd değişken değeri: A
id değişken değeri: 21

```

Program, oluşturduğu cd adlı char bir değişkene 'A' karakterini, id adlı int bir değişkene ise 21 sayısını ilk değer atama yöntemi ile atar. Sonra değişken değerlerini ekrana yazar.

İlk değer atama işlemlerinde, global değişkenlere atanan değerler mutlaka sabit bir değer olmalıdır. Atanan değer bir değişken olarak tanımlanamaz. Başka bir deyişle, ilk değer atama işlemlerinde, ilk değer atama işlemcisinin (=) sağ tarafında yer alan değer mutlaka bir sabit olmalıdır.

Şimdi, bu özelliği bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

int gid = 21; // Global değişkene sadece sabit bir değer atanabilir.

int fonk(void);

int main(void)
{
  int id1 = 84;      // Lokal değişkene sabit değer atama
  int id2 = id1/gid; // Lokal değişkene bir işlem sonucunu atama
  int id3 = fonk();  // Lokal değişkene fonksiyonun geri döndürdüğü değeri atama

  cout << "id1 değişken değeri: " << id1 << "\n";
  cout << "id2 değişken değeri: " << id2 << "\n";
  cout << "id3 değişken değeri: " << id3;

  return 0;
}

int fonk(void)
{
  int id = gid/3;

  return id;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

id1 değişken değeri: 84
id2 değişken değeri: 4
id1 değişken değeri: 7

```

Program, oluşturduğu gid adlı global bir değişkene ve id1 adlı lokal değişkene yaptığı ilk değer atamalarında sabit değerler kullanır. id2 değişkenine bir işlem sonucunu, id3 değişkenine ise fonk() fonksiyonu içinde yapılan bir işlem sonucunu atar.

Global değişkenlere bir defaya mahsus olmak üzere sadece programın başında bir ilk değer atama yapabiliriz. Lokal değişkenlere ise içinde tanımlandıkları fonksiyonların her çağrılışında bir ilk değer atama işlemi yapılır.

Bu özelliği bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

int gid = 21;

int kare_al(int id);

int main(void)
{
  int id=5;

  cout << "id değişkeninin karesi: " << kare_al(id) << "\n";

  id=7;
  cout << "id değişkeninin karesi: " << kare_al(id) << "\n";

  cout << "gid değişken değeri: " << gid;

  return 0;
}

int kare_al(int id1)
{
  int id2 = id1;

  return id2 * id2;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

id değişkeninin karesi: 25
id değişkeninin karesi: 49
gid değişken değeri: 21

```

Program, gid adlı global int bir değişken oluştururken 21 değerini ilk değer olarak atar. main() fonksiyonu içinde, id adlı int bir değişken oluştururken 5 değerini ilk değer olarak atar. kare\_al() fonksiyonunu id değişken değerini önce 5 sonra 7 değeri ile parametre olarak geçirerek, iki defa çağırır. Her defasında, fonksiyon içindeki id2 lokal int değişkenine parametre olarak geçirdiği değişken değerini ilk değer atama yöntemi ile atar. Bir fonksiyonun her çağrılışında, lokal değişken değerleri yeniden bir ilk değer alır.

Program yazarken başka bir işlem satırında değer atama yapmak yerine ilk değer atama yöntemini kullanmanın en büyük avantajı daha kısa ve daha hızlı bir kodlama yapabilmektir.

Global bir değişkene bir ilk değer atamazsak, değişken sıfır (0) değerini alır. Lokal bir değişkene bir ilk değer atamazsak, değişken anlamsız bir değer alır. Şimdi, bu özelliği bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

int gid;

int main(void)
{
  int id;

  cout << "gid global değişken değeri: " << gid << "\n";
  cout << "id lokal değişken değeri: " << id; // Derleyici uyarı verir.

  return 0;
}


```

Program, oluşturduğu gid adlı global int bir değişkene ve id adlı lokal int bir değişkene bir ilk değer vermediği için, global değişken için ekrana sıfır (0), lokal değişken için anlamsız bir değer yazar.

Bir işlem satırında birden fazla değişkene ilk değer atama yapılabilir:

```


int id1 = 7, id2 = 21, id3;
char cd1 = 'A', cd2 = 'F';
float fd1 = 45.324, fd2 = 852.321


```

Şimdi, bu özelliği bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

int main(void)
{
  int id1 = 7, id2 = 21;
  char cd1 = 'F', cd2 = 'K';
  double dd1 = 652.435, dd2 = 234.741;

  cout << "int değişken değerleri: " << id1 << " " << id2 <<"\n";
  cout << "char değişken değerleri: " << cd1 << " " << cd2 << "\n";
  cout << "double değişken değerleri: " << dd1 << " " << dd2;

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

int değişken değerleri: 7 21
char değişken değerleri: F K
double değişken değerleri: 652.435 234.741

```

Program, değişken bildiriminin yapıldığı her iki satırda ilk değer atama yöntemi ile ikişer farklı değişkene değerler atar ve ekrana yazar.

## Atamalarda veri türü dönüşümü

C++'da, atama işlemlerinde, eğer atama işlemcisinin her iki tarafında yer alan verilerin türleri farklı ise, program verilerin türünü dönüştürür. Bu veri türü dönüşümü belirli bir kurala göre yapılır.

Atama yapılan bir işlem satırında, atama işaretinin sağ tarafında yer alan veri türü atama işaretinin sol tarafında yer alan veri türünden farklı ise sağ tarafta yer alan verinin türü sol taraftaki veri türüne çevrilir.

Bu özelliği bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

int main(void)
{
  int id1, id2;  // 32 bit int değişken
  char cd1, cd2; // 8 bit char değişken

  id1 = 87;  // 87 = W = 00000000 00000000 00000000 01010111
  cd1 = 'K'; // K = 75 = 01001011

  cout << "id1 değişken değeri: " << id1 << "\n";
  cout << "cd1 değişken değeri: " << cd1 << "\n";

  id2 = cd1; // id2 = 75 = K = 00000000 00000000 00000000 01001011
  cd2 = id1; // cd2 = 87 = W = 01010111

  cout << "id2 değişken değeri: " << id2 << "\n";
  cout << "cd2 değişken değeri: " << cd2;

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

id1 değişken değeri: 87
cd1 değişken değeri: K
id2 değişken değeri: 75
cd2 değişken değeri: W

```

Program, id1 ve id2 adlı iki adet int ve cd1 ve cd2 adlı iki adet char veri türünden olmak üzere dört adet değişken tanımlar. id1 ve cd1 değişkenlerine atadığı değerleri sıra ile id2 ve cd2 değişkenlerine atar. Sonra, değişken değerlerini ekrana yazar. id2 int değişkenine atanan değer char, cd2 char değişkenine atanan değer int bir değer olduğu halde herhangi bir veri kaybı olmaz. Çünkü, 32 bit'lik int değişkenlere atanan değer 8 bit'lik char değişkenlerinb alabileceği büyüklüktedir.

Konunun daha iyi anlaşılabilmesi için aşağıdaki ifadeleri birlikte inceleyelim:

```


               char                        int

  K (75)     01001011      00000000 00000000 00000000 01001011

  87 (W)     01010111      00000000 00000000 00000000 01010111


```

id1 int değişkenine atanan 87 sayısının ikili sistemdeki yazılımı yukarıdaki ikinci satırın sağ tarafında yer almaktadır. 32 bit'ten oluşan bu değer cd2 char değişkenine atandığında, en soldaki 24 bit kaybolur. cd1 char değişkenine atanan 'K' karakterinin ikili sistemdeki yazılımı ise yukarıdaki ilk satırın sol tarafında yer almaktadır. 8 bit'ten oluşan bu değer id2 int değişkenine atandığında, ikili sistemdeki yazılımın sol tarafına 24 bit eklenir.

Eğer sol taraftaki veri türü sağ taraftakinden büyük ise veri türü dönüşümünde herhangi bir sorun çıkmaz. Ancak, sol taraftaki veri türü sağ taraftakinden küçük ise dönüşümden dolayı veri kaybı meydana gelebilir. Bu özelliği bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

int main(void)
{
  char cd;
  int id;

  id = 3698;
  cd = id;

  cout << "id değişken değeri: " << id << "\n";
  cout << "cd değişken değeri: " << (int)cd;

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

id değişken değeri: 3698
cd değişken değeri: 114

```

Program önce id adlı int değişkene 3698 sayısını atar. 3698 sayısının ikili sistemdeki yazılımı aşağıda yer almaktadır:

id = 3698 = 00000000 00000000 00001110 01110010

Program id değişken değerini cd adlı char bir değişkene atar. char değişken 8 bit ve int değişken 32 bit olarak kabul edildiğinde, id değişkeninin ikili sistemdeki yazılımının sol tarafında yer alan 24 bit'i yok eder ve cd değişkeni aşağıda ikili sistemdeki yazılımı verilen 114 değerini alır. Başka bir ifade ile, cd değişkenine sadece id değişkeninin sağ baştan itibaren 8 bit'i atanır:

cd = 114 = 01110010

Atama işleminde, farklı veri türlerinin birbirine dönüştürülmesinde görülen değişiklikler aşağıda yer almaktadır:

```


char değişken-adı = int (ifade); // 8 bit devre dışı kalır.

short int değişken-adı = int (ifade); // 24 bit devre dışı kalır.
short int değişken-adı = long int (ifade); // 24 bit devre dışı kalır.
short int değişken-adı = long long int (ifade); // 48 bit devre dışı kalır.

float değişken-adı = double (ifade); // ondalık bölümün hassaslığı azalır.
double değişken-adı = long double (ifade); // ondalık bölümün hassaslığı azalır.
   
int değişken-adı = float (ifade); // Ondalık bölümü ortadan kalkar (Float değer int kapasitesinden büyük ise anlamsız bir değer).


```

Şimdi, öğrendiklerimizi bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

int main(void)
{
  int id;
  short int sid;
  long int lid;
  float fd;
  double dd;

  fd = 2431.52;
  id = fd;

  cout << "fd değişken değeri: " << fd << "\n";
  cout << "id değişken değeri: " << id << "\n\n";

  dd = fd;

  cout << "fd değişken değeri: " << fd << "\n";
  cout << "dd değişken değeri: " << dd << "\n\n";

  lid = 91615;
  sid = lid;

  cout << "lid değişken değeri: " << lid << "\n";
  cout << "sid değişken değeri: " << sid;

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

fd değişken değeri: 2431.52
id değişken değeri: 2431

fd değişken değeri: 2431.52
dd değişken değeri: 2431.52

lid değişken değeri: 91615
sid değişken değeri: 26079

```

Program id adlı int, sid adlı short int, lid adlı long int, fd adlo float ve dd adlı double veri türünden değişken bildirimleri yapar. fd değişkenine 2431.52 değerini atar. fd değişkenini id değişkenine atar. Değerin ondalık bölümü devre dışı kalır. id ve fd değişken değerlerini ekrana yazar. fd değişkenini dd değişkenine atar. fd ve dd değişken değerlerini ekrana yazar. lid değişkenine 91615 değerini atar. lid değişkenini sid değişkenine atar. Değerin sol tarafındaki 16 bit devre dışı kalır. lid ve sid değişkenlerini ekrana yazar.

## Değişken niteleyiciler (qualifiers)

Veri türü niteleyicileri, bir değişken, bir fonksiyon, parametre veya fonksiyonun bildirimini düzenlemek için kullanılır. C++'da değişken bildirimlerinin başında kullanılan niteleyiciler ile değişkenlere farklı özellikler kazandırabiliriz. C++'da, const, volatile ve restrict olmak üzere üç niteleyici kullanılmaktadır. Ancak, restrict niteleyicisi C++ anahtar kelimleri içinde yer almamasına ve resmi olarak açıklanmamış olmasına rağmen, bazı derleyiciler tarafından destek verilmektedir.

## const değişken niteleyicisi

Değişken bildiriminin başına const ifadesini getirdiğimizde, program değişkenin değerini hiç bir şekilde değiştiremez. const değişkenlere bir ilk değer verilebilir.

Bir fonksiyona geçirilen bir parametrenin, fonksiyon tarafından değiştirilmesini önlemek için const değişken tanımlayıcısını kullanabiliriz. Böylece fonksiyona aktardığımız değişken değerinin korunmasını garantiye alırız.

Şimdi, const tanımlayıcısının bir değişkenle kullanılmasını bir örnekle incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

int main(void)
{
  int id1 = 7;
  const int id2 = 21;

  cout << "id1 değişken değeri: " << id1 << "\n";
  cout << "id2 değişken değeri: " << id2 << "\n\n";

  id1 = 35;
  // const bir değişkene değer atama yapılamayacağından, derleyici hata verir.
  // id2 = 49;

  cout << "id1 değişken değeri: " << id1 << "\n";
  cout << "id2 değişken değeri: " << id2;

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

id1 değişken değeri: 7
id2 değişken değeri: 21

id1 değişken değeri: 35
id2 değişken değeri: 21

```

Program, id1 adlı int ve id2 adlı const int değişken bildirimleri yaparken her iki değişkene birer ilk değer atar. Değişken değerlerini ekrana yazar. id1 değişkenine 35 değerini atar. Ancak, id2 değişkenine bir değer atamak isterse, derleyici hata verir. Sonra, her iki değişken değerini tekrar ekrana yazar.

Şimdi, const tanımlayıcısının bir fonksiyon parametresi ile kullanılmasını bir örnekle incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

int kare_al(const int id);

int main(void)
{
  int id = 7;

  cout << "id değişken değerinin karesi: " << kare_al(id);

  return 0;
}

int kare_al(const int id)
{
  // Fonksiyon içinde id değişkeninin değiştirilmesi derleyici hatası verir.
  // id++;
  return id*id;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

id değişken değerinin karesi: 49

```

Program, id adlı int bir değişken bildirimi yaparken değişkene bir ilk değer atar. id değişkenini parametre olarak geçirerek, kare\_al() fonksiyonunu çağırır. Fonksiyon parametre değerinin karesini alarak elde ettiği değeri geri döndürür. Parametrenin bildirimi const olarak yapıldığından fonksiyon içinde id değişkeninin değiştirilmesi derleyicinin hata vermesine neden olur. Geri döndürülen değeri ekrana yazar.

## volatile değişken niteleyicisi

Eğer bir değişken bildiriminin başına volatile ifadesini getirirsek, derleyici bu değişken değerinin program içinde herhangi bir zamanda, program içinde yer alan kodlar dışında, farklı kaynaklar tarafından değiştirilebileceğini anlar. Burada bahsi geçen kaynaklar, bir kesme (interrupt), harici kesme, doğrudan bellek erişimi veya paylaşılan kaynaklar olabilir. Normal değişkenler kullanıldığında, derleyici iyileştirme işlemi uygular ve değişkeni bellek yerine yazmaca ve ön belleğe yükler.

Kesinti (Interrupt), işlemcinin yazılım tarafından işlem yapılması gereken bir olaya verdiği karşılıktır. Bir kesme koşulu, işlemciyi uyarır ve işlemciye izin verildiğinde o anda yürütülen kodu kesintiye uğratması için bir talep görevini yerine getirir. Böylece ortaya çıkan olaya zamanında işlem yapılır. Talep kabul edilirse, işlemci, olayla ilgilenmek için mevcut faaliyetlerini askıya alarak, durumunu kaydederek ve kesme işleyicisi (kesme hizmeti rutini - ISR) adı verilen bir fonksiyonu çalıştırarak karşılık verir. Genellikle donanım aygıtları tarafından dikkat gerektiren elektronik veya fiziksel durum değişikliklerini belirtmek için kullanılan kesmeler, özellikle gerçek zamanlı hesaplamada bilgisayar çoklu görevini uygulamak için de yaygın olarak kullanılır.

Doğrudan Bellek Erişimi (Direct Memory Access - DMA), daha hızlı bir şekilde veri transferi yapabilmek amacıyla, merkezi işlem biriminden (Central Processing Unit - CPU) bağımsız olarak, disk sürücü kontrol birimleri, grafik kartları, ağ kartları ve ses kartları gibi çevre bileşenlerinin Rastgele Erişimli Hafıza (Random Access Memory - RAM) bloğuna erişebilmesini sağlayan bir özelliktir.

Volatile değişkenler kullanıldığında, derleyici optimize işlemi uygulamaz ve değişkeni yazmaç yerine belleğe yükler. Değişkeni kullanmak istediğimizde, değişken değeri bellekten yazmaca aktarılır, gerekli işlemler yapılır ve sonuçta elde edilen değişken değeri tekrar belleğe yüklenir.

Bir değişken volatile olarak tanımlandığında, derleyicinin herhangi bir iyileştirme yapmaması ve değişken değerinin bellekten okuması sağlanır.

Volatile niteleyicisinin değişken ve işaretçilerle kullanılmasını gösteren farklı örnekler aşağıda gösterilmektedir:

```c++
volatile int id; // volatile değişken bildirimi
volatile int *ip; // işaretçi volatile değil, gösterdiği değişken volatile
int *volatile ip; // işaretçi volatile, gösterdiği değişken volatile değil
volatile int *volatile ip; // işaretçi ve değişken volatile 


```

Bir değişken normal yöntemle tanımlandığında, derleyici iyileştirme uygulamaz ve değişken değerinin değişmeyeceğini kabul ederek, yazmaca yükler. Değişkeni kullanmak istediğinde, her defasında yazmaçtan okur.

```c++
// Normal değişken bildirimi (Derleyici iyileştirme yapar)
int id1 = 21;
yazmaç = id1; // id1 değeri yazmaca kopyalanır.

int id2 = yazmaç; // id1 değerine yazmaç yoluyla erişim sağlanır.
int id3 = yazmaç; // id1 değerine yazmaç yoluyla erişim sağlanır.

// Volatile değişken bildirimi
volatile int id1 = 21;

int id2 = id1; // id1 değerine bellek yoluyla erişim sağlanır.
int id3 = id1; // id1 değerine bellek yoluyla erişim sağlanır.


```

Bir değişken değerinin beklenmedik şekilde değişebildiği durumlarda, değişken volatile olarak bildirilmelidir. Bu şekilde değişim gösterebilen üç tip değişken vardır:

- Memory-mapped çevresel (peripheral) register'lar

Gömülü sistemler, genellikle karmaşık çevre birimleri olan gerçek donanım içerir. Gömülü sistemlerde, tüm çevre birimleri belirli bir bellek adresinde bulunur. Bu çevre birimleri, değerleri program akışına zaman uyumsuz olarak değişebilen register'lar içerir.

Bir programda, çevre birim register'larına uygun bir şekilde erişmek için, çevre birim register'larına bir c değişkeni ile eşleştirmeli ve bu değişkene işaretçi kullanarak erişim sağlamalıyız.

- Bir kesme (interrupt) servis rutini tarafından değiştirilen global değişkenler

Interrupt servisi ile ilgili bir fonksiyon kullanıldığında, programın main() fonksiyonu ile interrupt servis fonksiyonu global bir değişkeni ortaklaşa kullanırlar. Bu durumda, global değişken her iki fonksiyon tarafından okunabilir veya değişkene bir değer atanabilir.

- Multi-threaded bir uygulamada birden fazla görev tarafından erişilen global değişkenler

Gerçek zamanlı işletim sistemlerinde kuyrukların, pipes ve zamanlayıcıların esasına göre çalışan diğer iletişim mekanizmalarının varlığına rağmen, gerçek zamanlı işletim sistemlerinde görevlerin paylaşılan bir bellek konumu (global değişkenler) aracılığıyla bilgi alışverişinde bulunması mümkündür. Bu nedenle, tüm paylaşılan global nesneler (değişkenler, bellek tamponları, donanım register'ları vb.) derleyicinin beklenmeyen davranışlarını önlemek için volatile olarak bildirilmelidir.

Volatile anahtar kelimesi, nesneleri derleyici optimizasyonundan koruyan ve derleyiciye, nesnenin (değişken) değerinin kod tarafından herhangi bir işlem yapılmadan herhangi bir zamanda değişebileceğini söyleyen bir niteleyicidir. Bir değişkenin önbellekten register'a aktarılmasını engeller ve değişkenin her erişimde bellekten okunmasını sağlar.

Bir C++ programında volatile anahtar kelimesinin kullanımına aşağıdaki durumlarda ihtiyaç duyulabiliriz:

* Program normal çalışmasına rağmen, derleyicinin optimizasyon seviyesi yükseltildiğinde beklendiği şekilde çalışmazsa,
* Program normal çalışırken, interrupt'ları etkinleştirdiğimizde, kodların işleyişi değişir ve beklendiği şekilde çalışmazsa,
* Kesintisiz donanım sürücüleri,
* Tek başına normal çalışırken, diğer görevler etkinleştirildiğinde kilitlenen görevler.

Aşağıda gösterilen özel durumlarda volatile değişken kullanımı gerekir:

Çalışmakta olan bir thread kontrolü dışında, herhangi bir yerden bir değişken değeri değiştirilebildiğinde,

* Bellek eşlemeli Giriş/Çıkış yazmaçları,
* Doğrudan Bellek Erişimi (Direct Memory Access - DMA) aktarımları için kullanılan bellek,
* Kesme ve/veya thread bağlamları arasında paylaşılan bellek,

Program dışında yer alan bir interrupt hizmeti tarafından değiştirilen global değişkenler: Bir veri portunu temsil eden global bir değişken dinamik olarak değiştirilebilir. Veri portunu okuyan kod içinde kullanılan değişken, port üzerindeki en son veriyi okuyabilmek için, volatile olarak tanımlanmalıdır. Eğer değişken volatile olarak tanımlanmazsa, derleyici port üzerinde yer alan veriyi bir kez okur ve hız açısından iyileştirme yapmak için, aynı veriyi yazmaca yükler ve sürekli buradaki veriyi kullanır.

Çoklu thread uygulamalarında kullanılan global değişkenler: Birden fazla thread kullanan bir uygulama içinde, thread'ler arasında ortak veri kullanımı için global olarak bildirimi yapılan volatile değişkenler kullanılabilir. Bir uygulama içindeki thread'ler eş zamanlı olarak çalışmadıklarından, bir thread tarafından değiştirilen değişken değeri diğer thread tarafından anında okunabilir.

* Bağımsız işlemciler arasında paylaşılan bellek

Mantıksal olarak herhangi bir etkisi olmasa bile, değişken erişiminin gereki olduğu durumlarda

* Boş gecikme döngüleri için kullanılan döngü sayaçları, aksi takdirde tüm döngü tamamen optimize edilebilir ve zaman sayımı gerçekleşmez.
* Bir hata ayıklayıcıya yazılan ancak hiçbir zaman inceleme amacıyla okunmayan değişkenler.

Şimdi, volatile niteleyicisinin kullanılmasını çoklu thread ile çalışan bir örnekle incelemeye çalışalım:

Örnek

```c++
#include <iostream>
#include <cstdlib> // exit() fonksiyonu için
#include <pthread.h>

using namespace std;

#define DEGER 10000

volatile int gid = 0;
volatile int durum = 1;

void *deger_artir(void*);
void *deger_bildir_yuz(void*);
void *deger_bildir_bin(void*);

int main(void)
{
  pthread_t thread1, thread2, thread3;
  int id=0;
  int idth;

  cout << "Thread oluşturma: " << id++ << endl;
  idth = pthread_create(&thread1, NULL, deger_artir, NULL);
  if (idth) {
      cout << "Thread oluşturma hatası: " << idth << endl;
      exit(-1);
  }

  cout << "Thread oluşturma: " << id++ << endl;
  idth = pthread_create(&thread2, NULL, deger_bildir_yuz, NULL);
  if (idth) {
      cout << "Thread oluşturma hatası: " << idth << endl;
      exit(-1);
  }

  cout << "Thread oluşturma: " << id << endl;
  idth = pthread_create(&thread3, NULL, deger_bildir_bin, NULL);
  if (idth) {
      cout << "Thread oluşturma hatası: " << idth << endl;
      exit(-1);
  }

  cout << endl;

  while (gid<DEGER) {
     if (durum==2) cout << "\n\n100'ler basamağı geçildi!" << "\n\n";
     else if (durum==3) cout << "\n\n1000'ler basamağı geçildi!" << "\n\n";
     durum=0;
  }

  return 0;
}

void *deger_artir(void*)
{
  int id;

  while(durum); // deger_bildir_bin() thread fonksiyonundan önce başlamaması için

  for (id=0; id<DEGER; id++) cout << gid++ << " ";

  return 0;
}

void *deger_bildir_yuz(void*)
{
  while(durum); // deger_bildir_bin() thread fonksiyonundan önce başlamaması için

  while (gid<DEGER) {
    if ((gid>0) && (gid%100==0)) durum = 2;
  }

  return 0;
}

void *deger_bildir_bin(void*)
{
  durum = 0;

  while (gid<DEGER) {
    if ((gid>0) && (gid%1000==0)) durum = 3;
  }

  return 0;
}


```

Program, önce thread1 adlı bir thread oluşturur. İlk thread'e ait olan deger\_artir() fonksiyonu çalışmaya başlar. Fonksiyon, durum adlı global değişken değeri 1 olduğundan while döngüsünde beklemeye başlar. Program, herhangi bir thread oluşturduktan sonra, main() fonksiyonundaki bir sonraki işlem satırından çalışmasına devam etmek için, bu thread'e ait olan fonksiyonun çalışmasının sona ermesini beklemez. Bu nedenle, hiç beklemeden thread2 adlı bir thread oluşturur. İkinci thread'e ait olan deger\_bildir\_yuz() fonksiyonu çalışmaya başlar. Fonksiyon, durum adlı değişken değeri 1 olduğundan while döngüsünde beklemeye başlar. Son olarak, thread3 adlı bir thread oluşturur. Üçüncü thread'e ait olan deger\_bildir\_bin() fonksiyonu çalışmaya başlar. Fonksiyon, ilk olarak durum adlı değişkene 0 değeri atar. Böylece, deger\_bildir\_yuz() ve deger\_bildir\_bin() fonksiyonları içindeki while döngüleri sona erer ve bir sonraki döngüler çalışmaya başlar.

Bu durumda, main() fonksiyonu ve her üç thread'e ait fonksiyonlarda yer alan son döngüler aynı anda çalışmaya başlar. deger\_artir() fonksiyonu gid adlı global değişken değerini, her defasında bir değer olmak üzere, 10000 sayısından küçük olduğu sürece artırır ve değişken değerini ekrana yazar. deger\_bildir\_yuz() fonksiyonu gid değişkeninin aldığı değeri takip ederek, 100 ve katlarını aldığında, durum adlı değişkene 2 değerini atar. main() fonksiyonundaki while döngüsü içinde if koşulu karşılandığından, "100'ler basamağı geçildi!" ifadesi ekrana yazılır ve durum adlı değişkenine 0 değeri atanır. deger\_bildir\_bin() fonksiyonu da deger\_bildir\_yuz() fonksiyonunun yaptığı işlemlerin aynısını 1000 sayısı için yapar. main() fonksiyonundaki while döngüsü içinde if koşulu karşılandığından, "1000'ler basamağı geçildi!" ifadesi ekrana yazılır ve durum adlı değişkenine 0 değeri atanır.

Şimdi, volatile niteleyicisinin kullanılmasını farklı bir örnekle incelemeye çalışalım:

Örnek

```c++
#include <iostream>
#include <cstdlib> // exit() fonksiyonu için
#include <pthread.h>

using namespace std;

#define MAXDEGER 10000
#define DEGER 75

volatile int gidcur = 0;
volatile int gid = 0;

void *deger_artir(void*);

int main(void)
{
  pthread_t thread;
  int idth;
  int ulid=0;

  cout << "Thread oluşturma" << "\n\n";
  idth = pthread_create(&thread, NULL, deger_artir, NULL);
  if (idth) {
      cout << "Thread oluşturma hatası!" << idth << endl;
      exit(-1);
  }

  while (gidcur<MAXDEGER) {
    if (gid) {
        ulid++;
        gid=0;
    }
  };

  while(gid);

  cout << "\nmain(): 0-" << MAXDEGER << " arasında " << DEGER << " sayısına tam olarak bölünenlerin sayısı: " << ulid;

  return 0;
}

void *deger_artir(void*)
{
  int ulid;
  int ulid2=0;

  for (ulid=0; ulid<MAXDEGER; ulid++) {
       if (ulid%75==0) {
           cout << ulid << " ";
           gid=1;
           ulid2++;
       }
       gidcur++;
  }

  cout << "\n\ndeger_artir(): 0-" << MAXDEGER << " arasında 75 sayısına tam olarak bölünenlerin sayısı: " << ulid2;

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Thread oluşturma

0 75 150 225 300 375 450 525 600 675 750 825 900 975 ... 9750 9825 9900 9975 

deger_artir(): 0-10000 arasında 75 sayısına tam olarak bölünenlerin sayısı: 134
main(): 0-10000 arasında 75 sayısına tam olarak bölünenlerin sayısı: 134

```

Program, önce thread adlı bir thread oluşturur. Thread'e ait olan deger\_artir() fonksiyonu çalışmaya başlar. Program, herhangi bir thread oluşturduktan sonra, main() fonksiyonundaki bir sonraki işlem satırından çalışmasına devam etmek için, bu thread'e ait olan fonksiyonun çalışmasının sona ermesini beklemez. Bu nedenle, hiç beklemeden main() fonksiyonu içindeki while döngüsü çalışmaya başlar.

Thread'e ait olan deger\_artir() fonksiyonu gidcur adlı global değişken değerini, her defasında bir değer olmak üzere, 10000 sayısından küçük olduğu sürece artırır ve değişken değeri 75 ve katları ise, değeri ekrana yazar ve 
gid değişkenine 1 değeri atar ve ulid2 adlı değişken değerini bir artırır. main() fonksiyonu içindeki while döngüsü içinde if koşulu karşılandığından, ulid değeri bir artırılır ve gid değişkenine 0 değeri atanır.

deger\_artir() ve main() fonksiyonu içindeki döngüler sona erdiğinde, 0-10000 arasında 75 sayısına tam olarak bölünenlerin sayısı olan 134 değeri iki kez ekrana yazılır.

## Depolama sınıfı belirleyicileri (Storage class specifiers))

C++'da depolama sınıfı, değişkenlerin ömrünü ve görünürlüğünü tanımlar. Bir değişkenin ömrü, değişkenin aktif kaldığı süreyi, görünürlük ise, programın farklı modüllerinden bir değişkene erişilebilirliği ifade eder.

C++'da, her değişken için mutlaka tanımlanması gereken veri türü ve isteğe bağlı olarak tanımlanan bir depolama sınıfı vardır. Bir değişken için depolama sınıfı tanımlanmadığında, derleyici değişken için ön tanımlı depolama sınıfını tanımlar. Depolama sınıfı bir değişkeninin ömrünü ve kapsamını belirler. Bir değişkenin depolama sınıfı, değişkenin bellekteki depolama konumu, ön tanımlı başlangıç ​​değeri, değişkenin kapsamı ve ömrü ile ilgili bilgiler içerir.

Depolama sınıfı belirleyicileri ile ilgili kullanılan genel yapı aşağıda gösterilmektedir:

depolama-belirleyici değişken\_adı;

Bu belirleyiciler derleyiciye bir değişkeni nasıl depolayacağını bildirir.

C++'da, aşağıda gösterilen 5 anahtar kelimeyi değişken adlarından önce kullanarak değişkenleri farklı şekilde kullanabiliriz:

```


auto
register
static
extern
mutable


```

## auto değişken belirleyicisi

auto depolama sınıf belirleyicisi, bir fonksiyon veya kod bloğu içinde tanımlanan bütün lokal değişkenler için ön tanımlı belirleyici olarak kullanılır. Bir değişken için, bir depolama sınıf belirleyicisi tanımlanmadığında, otomatik olarak auto depolama sınıf belirleyicisine sahip olacaktır.

auto olarak bildirimi yapılan değişkenlerin kapsamı, tanımlandıkları fonksiyon veya kod bloğu içerisinde olup, bu fonksiyon veya kod bloğunun dışından erişim sağlanmaz.

auto olarak bildirimi yapılan değişkenlerin ömrü, tanımlandıkları fonksiyon veya kod bloğu sona erdiğinde sona erer.

## register değişken belirleyicisi

register depolama sınıf belirleyicisi, her veri türüne uygulanabilir.

Program, bir değişken register depolama sınıf belirleyicisi ile tanımladığında, derleyicinin bu değişkenin değerini, normal koşullarda değişkenlerin depolandığı bellek yerine, CPU içindeki yazmaçlardan birine kaydetmesini ister. Bu durumda, değişken üzerinde yapılan tüm işlemler yazmaç üzerinde yapılacağı için, bellek erişimi gerekmediğinden, işlemler daha hızlı gerçekleştirilir.

register depolama sınıf belirleyicisi sadece lokal değişkenlerle birlikte kullanılabilir.

Bir fonksiyon veya kod bloğu içinde tanımlanan veya bir fonksiyon parametresi olarak bildirimi yapılan değişkenleri register depolama sınıf belirileyicisi ile birlikte tanımlayabiliriz.

Derleyici register depolama sınıf belirleyicisi ile tanımlanan değişken sayısı belirli bir sınırı aştığında, otomatik olarak bu değişkenlerin bir kısmını normal değişken haline çevirecektir.

> Eğer programımızda bir değişkeni çok sık kullanıyorsak, bu değişken bildiriminin başında register ifadesini kullanmamız programımızın hızını artırır. Çünkü, bilgisayar bu şekilde tanımlanan değişkenlere daha hızlı bir şekilde ulaşır.
{: .prompt-tip }

Ancak, CPU'da sınırlı sayıda yazmaç bulunduğu için, eğer register değişken sayısı çok fazla olursa, bilgisayar belli bir sayıdan sonraki register değişkenleri normal değişken olarak kabul eder. Bu tanımlamayı yaptığımızda, derleyiciye bu değişkene öncelik tanıyarak, performansı artırması için bellek yerine CPU içinde yer alan yazmaçlara yerleştirmesi konusunda bir istek yapılmış olur. Ama, bu isteğin mutlaka yerine getirileceğine dair bir garanti yoktur. Bu nedenle, çok sık kullanılan değişkenleri register olarak tanımlamak gerekir. Buna örnek olarak, döngüleri kontrol etmekte kullanılan değişkenler gösterilebilir. Bu değişkenler çok sık kullanıldığından programınızın performansı hissedilir ölçüde artacaktır.

Aslında, normal koşullarda bir değişken herhangi bir değişken niteleyicisi (const ve volatile) veya bir depolama sınıf belirleyicisi ile tanımlanmasa bile, derleyici eğer iyileştirme yapma gereği duyarsa, bu değişkeni CPU yazmacına kaydederek kullanır. Bir değişkeni volatile olarak tanımladığımızda, derleyicisinin iyileştirme işlemi yapmasını istemediğimizi, register olarak tanımladığımızda ise, derleyicisinin iyileştirme işlemi yapmasını özellikle istediğimizi ve değişkeni CPU yazmacına kaydetmesini belirtmiş oluruz.

Şimdi, register depolama sınıf belirleyicisinin kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>
#include <ctime>

using namespace std;

int main(void)
{
  clock_t start_t, end_t;
  register int id1, id2;

  start_t = clock();

  for(id1=0; id1<2000000; id1++){
      for (id2=0; id2<100; id2++) { }
  }

  end_t = clock();

  cout << "start_t değeri: " << start_t << "\n";
  cout << "end_t değeri: " << end_t << "\n";
  cout << "Döngü çalışma süresi (saniye): " << (double)(end_t - start_t) / CLOCKS_PER_SEC;

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

start_t değeri: 0
end_t değeri: 182
Döngü çalışma süresi (saniye): 0.182

```

Program clock() fonksiyonu ile bir döngü çalışmasından önce ve sonra olmak üzere iki defa işlemci süresini hesaplar, bu değerleri saat tik sayısı olarak ve iki değerin farkını saniye olarak ekrana yazar. Program içindeki döngünün çalışma süresi 182 milisaniye'dir. Bu değer bilgisayarlar arasında farklılıklar gösterebilir.

Şimdi, aynı programı depolama sınıf belirleyicisi yerine volatile değişken niteleyicisi kullandığımız bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>
#include <ctime>

using namespace std;

int main(void)
{
  clock_t start_t, end_t;
  volatile int id1, id2;

  start_t = clock();

  for(id1=0; id1<2000000; id1++){
      for (id2=0; id2<100; id2++) { }
  }

  end_t = clock();

  cout << "start_t değeri: " << start_t << "\n";
  cout << "end_t değeri: " << end_t << "\n";
  cout << "Döngü çalışma süresi (saniye): " << (double)(end_t - start_t) / CLOCKS_PER_SEC;

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

start_t değeri: 0
end_t değeri: 528
Döngü çalışma süresi (saniye): 0.528

```

Program clock() fonksiyonu ile bir döngü çalışmasından önce ve sonra olmak üzere iki defa işlemci süresini hesaplar, bu değerleri saat tik sayısı olarak ve iki değerin farkını saniye olarak ekrana yazar. Program içindeki döngünün çalışma süresi 528 milisaniye'dir. Bu değer bilgisayarlar arasında farklılıklar gösterebilir.

## static değişken belirleyicisi

static depolama sınıfı belirleyicisini lokal ve global değişkenlerle birlikte kullanabiliriz. Normal olarak, içinde lokal değişken tanımlanan bir fonksiyonu her çağırdığımızda, lokal değişken değeri yenilenir. Ancak, bu lokal değişkeni static olarak tanımlarsak, fonksiyonu her çağırmamızda, lokal değişken bir önceki fonksiyon çağrısındaki en son değerini korur. Sonuç olarak, static lokal bir değişkene sadece fonksiyonun ilk çağrılışında bir defaya mahsus olmak üzere değer verebiliriz.

Static değişkenler, sadece tanımlandıkları fonksiyon içinde kalıcı olarak değer taşırlar. Fonksiyon dışından bu değişkenlere erişim sağlanamaz.

Şimdi, static lokal bir değişken kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

void fonk(void);
void fonk_sta(void);

int main(void)
{
  fonk();
  fonk_sta();

  cout << "\n";

  fonk();
  fonk_sta();

  return 0;
}

void fonk(void)
{
  int id = 1;

  cout << "fonk() id değişken değeri: " << id << "\n";

  id = id + 21;

  cout << "fonk() id değişken değeri: " << id << "\n";
}

void fonk_sta(void)
{
  static int id = 1; // Sadece fonksiyonun ilk çağrısında çalışır.

  cout << "fonk_sta() id değişken değeri: " << id << "\n";

  id = id + 21;

  cout << "fonk_sta() id değişken değeri: " << id << "\n";
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

fonk() id değişken değeri: 1
fonk() id değişken değeri: 22
fonk_sta() id değişken değeri: 1
fonk_sta() id değişken değeri: 22

fonk() id değişken değeri: 1
fonk() id değişken değeri: 22
fonk_sta() id değişken değeri: 22
fonk_sta() id değişken değeri: 43

```

Program, fonk() ve fonk\_sta() fonksiyonlarını sırasıyla ikişer kez çağırarak, lokal olarak tanımlanmış değişken değerlerini ekrana yazdırır. Her iki fonksiyonda da lokal değişken değerleri artırılmasına rağmen sadece fonk\_sta() fonksiyonu içindeki id değişkeni bir önceki fonksiyon çağrısında aldığı değeri korumaktadır. Bu olanağı sağlayan değişkenin statik tanımlanmış olmasıdır.

fonk\_sta() fonksiyonuna yapılan ilk çağrıda, fonksiyon içindeki id lokal değişkenine, sadece bir defaya mahsus olmak üzere, ilk değer olarak 1 değeri atanır. Değişken değeri ekrana yazılır. Değişken değerine 21 değeri eklenir ve değişken tekrar ekrana yazılır. fonk\_sta() fonksiyonuna yapılan bir sonraki çağrıda, id lokal değişkeni bildirim ve ilk değer verme satırı dever dışı kalır. Böylece, değişkene bir önceki fonksiyon çağrısında verilen değer korunur. fonk\_sta() fonksiyonu ikinci kez çağrıldığında, fonksiyon girişinde lokal id değişken değeri 22 olur.

static depolama sınıfı belirleyicisini global değişkenlerle de kullanabiliriz. static global bir değişken tanımladığımızda, bu değişkeni sadece içinde tanımlandığı dosyada bulunan fonksiyonlar kullanabilir. Bunun yanında, aynı programa ait farklı dosyalarda bulunan ve aynı isme sahip biri normal diğeri de static olan iki global değişken tanımlayabiliriz. Bu özelliği bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
// deneme1.cpp
#include <iostream>

using namespace std;

void fonk1(void);
void fonk2(void);

static int gid = 21; // Static global int değişken bildirimi

int main(void)
{
  fonk1();
  fonk2();

  return 0;
}

void fonk1(void)
{
  cout << "deneme1.cpp gid değişken değeri: " << gid << "\n";
}

// deneme2.cpp
#include <iostream>

using namespace std;

int gid = 35; // global int değişken bildirimi

void fonk2(void)
{
  cout << "deneme2.cpp gid değişken değeri: " << gid;
}


```

Yukarıda verilen iki dosyayı deneme1.cpp ve deneme2.cpp adları ile bir proje içine kaydettikten sonra derleyiciyi kullanarak projeyi derler ve deneme.exe adlı tek bir program adı ile çalıştırırsak aşağıdaki ifadeleri ekrana yazar:

```

deneme1.cpp gid değişken değeri: 21
deneme2.cpp gid değişken değeri: 35

```

Program, her iki dosyada gid adlı birer adet global değişken tanımlar. Aynı isme sahip 2 değişken olduğu halde deneme1.cpp dosyasındaki değişkenin static olarak tanımlanması farklı 2 değişken olarak algılanmalarını sağlar.

## extern değişken belirleyicisi

C++ dilinde yazılan uzun programlar derleme zamanını çok artıracağı için, genellikle uzun programlar iki veya daha fazla dosyaya bölünerek derlenir. Bu sistemden aynı zamanda farklı amaçlarla kullanılan kodların düzenlenmesi içinde faydalanılır. Bir proje içinde içinde yer alan bu dosyalar tek bir komutla ayrı ayrı derlendikten sonra birleştirilerek tek bir çalışan .exe uzantılı dosya oluşturulur. Bu durumda, bir dosya içinde tanımladığınız global değişkenler diğer dosya içinde tanınmazlar. Eğer bir dosya içinde tanımladığımız global değişkenlerin diğer dosyalar içinde geçerli olmasını istersek, diğer dosyalarda yer alan bütün fonksiyonların dışında yaptığımız değişken tanımlamalarının baş tarafına extern ifadesini getirmemiz gerekir.

Bir değişkeninin başında extern ifadesini kullanmak, o değişkenin projede yer alan kod dosyalarının birinde tanımlandığını ve o değişkene extern ifadesini kullandığımız dosya içinden erişim sağlamak istediğimizi gösterir.

extern değişken belirleyicisinin kullanılmasını örnekler üzerinde incelemeye çalışalım:

Örnek

```c++
// deneme1.cpp
#include <iostream>

using namespace std;

void fonk(void);

int gid = 287; // global int değişken tanımlaması

int main(void)
{
  cout << "deneme1.cpp gid değişken değeri: " << gid << "\n";

  fonk(); // deneme2.cpp dosyasındaki fonk() fonksiyonuna çağrı

  return 0;
}

// deneme2.cpp
#include <iostream>

using namespace std;

extern int gid; // global int değişken bildirimi

void fonk(void)
{
  cout << "deneme2.cpp gid değişken değeri: " << gid;
}


```

Yukarıda verilen iki dosyayı deneme1.cpp ve deneme2.cpp adları ile bir proje içine kaydettikten sonra derleyiciyi kullanarak projeyi derler ve deneme.exe adlı tek bir program adı ile çalıştırırsak aşağıdaki ifadeleri ekrana yazar:

```

deneme1.cpp gid değişken değeri: 287
deneme2.cpp gid değişken değeri: 287

```

Programda, ilk satırı ekrana yazan deneme1.cpp, ikinci satırı ekrana yazan ise deneme2.cpp dosyasındaki fonk() fonksiyonu içindeki işlem satırıdır.

## mutable değişken belirleyicisi

Normal koşullarda, bir sınıf içindeki üye fonksiyonları const olarak tanımladığımızda, bu sınıftan oluşturulan bir nesne ile çağırdığımız const fonksiyon nesne içinde yer alan değişken değerlerini değiştiremez.

Bir sınıf içinde const olarak tanımlanan bir fonksiyonun, sınıf içindeki bir değişken değerini değiştirebilmesi için, değişkeninin mutable olarak tanımlanmış olması gerekir.

Şimdi, mutable olarak tanımlanmış değişkenler ile const üye fonksiyonların kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

class sinif {
  private:
    mutable int priid;
  public:
    // const fonksiyon bildirimleri
	void deger_ata(int pid) const { priid = pid; };    
    void deger_goster(void) const
    {
      cout << "priid değişken değeri: " << priid;
    };
};

int main(void)
{
  sinif nes;

  // const fonksiyonları çağırma
  nes.deger_ata(21);
  nes.deger_goster();

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

priid değişken değeri: 21

```

Program, priid adlı private int bir değer, bu int değere bir değer atayan deger\_ata() adlı ve priid değişken değerini ekrana yazan deger\_goster() adlı iki adet const fonksiyon içeren bir sınıf oluşturur. Bu sınıftan nes adlı bir nesne oluşturur. Sonra, deger\_ata() fonksiyonu ile priid değişkenine 21 değeri atar. Daha sonra, deger\_goster() fonksiyonunu kullanarak, priid değişken değerini ekrana yazar.

Burada, deger\_ata() fonksiyonu const olarak tanımlandığı halde, sınıf içindeki değişken değerini değiştirebilmektedir. Bunun nedeni, değişkenin mutable olarak tanımlanmasıdır.
