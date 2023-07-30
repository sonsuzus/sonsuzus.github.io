---
title:  C Programlama Değişkenler
author: sonsuz
date: 2023-07-31 00:10:45 +0300
categories: [Program,C]
tags: [programlama,c,değişken]
---


C dilinde bilgisayar belleğinin bir kısmına belirli bir isim vererek bu bellek alanını kendimiz için ayırabilir ve bu alana değerler yerleştirebiliriz. Bu değerleri de istediğimiz zaman değiştirebiliriz.

Bu işlemlere değişken bildirimi ve değişkene değer atama işlemleri diyoruz.

## Değişken bildirimi

Bir değişken bildirimi yaparak, bilgisayarın belleğinde belirli büyüklükte bir alanı kendimize ayırabiliriz. Bu bellek boyutu değişken veri türüne göre değişecektir. Bu işlemi yaptığımızda belleğin belirli bir bölümü bizim için ayrılmış olur.

Değişken bildirimi aşağıda gösterilen 3 farklı yerde yapılabilir:

1. Lokal değişkenler: Fonksiyonların içinde
2. Parametre olarak tanımlanan değişkenler: Fonksiyon parametresi olarak
3. Global değişkenler: Tüm fonksiyonların dışında

C programlama dilinde bir değişken ifade içinde kullanılmadan önce mutlaka bildirimi yapılmalı ve bir değer atanmalıdır. Bu bildirim işlemi, ister main() ister başka bir fonksiyon içinde olsun mutlaka fonksiyonun veya kod bloğunun başında yapılmalıdır.

Ancak, C99 standartlarına göre, bir fonksiyon içindeki yerel değişken bildirimi fonksiyonun veya fonksiyon içinde yer alan bir kod bloğu içinde herhangi bir yerde yapılabilir.

Bir değişken bildirimi aşağıdaki gösterildiği şekildeyapılır:

veri-türü değişken-adı;

Değişken bildirimi bir işlem satırı ile yapıldığından, noktalı virgül (;) ile sona erer. veri-türü ifadesi bildirimi yapılan değişkeninin veri türünü, değişken-adı ifadesi ise değişkenin adını göstermektedir.

Değişken bildiriminde değişken-adı ifadesi yerine kullanılacak değişken adları, sizin verebileceğiniz herhangi bir ad olabilir. Bu ad harflerden, rakamlardan ve (_) işaretinden oluşan bir karakter dizisi olmalıdır. C küçük ve büyük harflere farklı işlem yapar. VAR1 ve var1 olarak verilen değişken adları birbirinden tamamen farklı olarak kabul edilir.

Aşağıdaki işlem satırlarından birincisi id1 adlı int ve ikincisi fd1 adlı float bir değişken bildirimi yapar:

```c
int id;
float fd;
double dd;
```

Değişkenler bildirimlerini, main() fonksiyonu da dahil olmak üzere, fonksiyonların hemen başında veya bütün fonksiyonların dışında olmak üzere kaynak dosyamızın hemen başında yapabiliriz.

Aynı türden olan birden fazla değişken bildirimini aynı işlem satırında yapabiliriz. Aşağıdaki işlem satırı id1, id2 ve id3 adlarında üç adet int değişken bildirimi yapar:

```c
int id1, id2, id3;
```

## Lokal Değişkenler

Eğer değişken bildirimini fonksiyonların yada kod bloklarının içinde yaparsak bu değişkenlere "lokal değişken" adı verilir.

Lokal değişkenlerin en önemli özelliği sadece tanımlanmış olduğu fonksiyonlar içinde geçerli olması ve bu fonksiyon tarafından kullanılabilmesidir. Lokal değişken bildirimi fonksiyonun içinde yapılır ve sadece içinde tanımlandığı fonksiyon çalıştığı sürece geçerlidir.
Bir fonksiyon programın herhangi bir yerinden çağrıldığında, çağrılan fonksiyonun içindeki lokal değişkenler oluşturulur ve fonksiyonun son işlem satırına işlem yapıldıktan sonra yok edilirler.

Aynı ada sahip olsalar bile, bir fonksiyondaki lokal bir değişkenin diğer bir fonksiyon içindeki lokal değişken ile herhangi bir ilgisi yoktur.

```c
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

```c
#include <stdio.h>

/* Fonksiyon bildirimleri */
void fonk1(void);
void fonk2(void);

int main(void)
{
  int id;
 
  id = 5; // Bu değişken sadece main() fonksiyonu içinde geçerlidir.
  
  printf("main() fonksiyonu içindeki id değişken değeri: %d\n", id);
  
  fonk1();
  fonk2();
  
  return 0;
}

/* Fonksiyon ana yapıları */
void fonk1(void)
{
  int id;

  id = 27; // Bu değişken sadece fonk2() fonksiyonu içinde geçerlidir.  
  printf("fonk1() fonksiyonu içindeki id değişken değeri: %d\n", id);
}

void fonk2(void)
{
  int id;

  id = 54; // Bu değişken sadece fonk2() fonksiyonu içinde geçerlidir.  
  printf("fonk2() fonksiyonu içindeki id değişken değeri: %d", id);
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```c
main() fonksiyonu içindeki id değişken değeri: 5
fonk1() fonksiyonu içindeki id değişken değeri: 27
fonk2() fonksiyonu içindeki id değişken değeri: 54
```

Program, biri direk diğer ikisi ise fonksiyon çağrısı yoluyla olmak üzere 3 farklı değişken değerini ekrana yazar. main(), fonk1() ve fonk2() fonksiyonlarının tamamında id adlı bir değişken yer almaktadır. Ancak, her üç değişkende, aynı ada sahip olmalarına rağmen, birbirinden tamamen farklı olup, içinde bulundukları fonksiyon içinde geçerlidir.

Fonksiyonlarda kod bloğu içinde tanımlanan lokal değişkenler

Bir fonksiyondaki kod bloklarının içinde tanımlanan değişkenler sadece o kod bloğu içinde geçerlidir. Bu değişken sadece tanımlandığı kod bloğu tarafından kullanılabilir, kod bloğu dışından değişkene erişim sağlanamaz.

Bu özelliği bir örnek üzerinde incelemeye çalışalım:

Örnek

```c
#include <stdio.h>

int main(void)
{
  int id1=5;

  if (id1>0) {
      int id2 = id1 * id1;
      printf("id1 değişken değeri: %d id2 değişken değeri: %d\n", id1, id2);
  }
  
  printf("id1 değişken değeri: %d", id1); 
  
  /* id2 değişkenine buradan erişim sağlanamaz. */ 
  // printf("id2 değişken değeri: %d", id2);
  
  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```c
id1 değişken değeri: 5 id2 değişken değeri: 25
id1 değişken değeri: 5
```

Program, main() fonksiyonu içinde, id1 adlı bir değişken tanımlayarak 5 değerini atar. Bir if koşulu kod bloğu içinde, id2 adlı int bir değişken tanımlayarak id1 değişkeninin karesini bu değişkene atar ve her iki değişken değerini ekrana yazar. if koşulu dışında id1 değişken değerini tekrar ekrana yazar. Ancak, id2 değişkenine buradan erişim sağlayamaz, çünkü id2 değişkeni sadece if koşul bloğu içinde geçerlidir. Erişim sağlamaya çalıştığımızda, derleyici hata verir.

Bir fonksiyon içinde ve fonksiyonun içinde yer alan bir kod bloğu içinde aynı isme sahip değişken tanımlanırsa, bu değişkenler sadece tanımlandıkları kapsamda dikkate alınırlar. Bu değişken ismine kod bloğu dışından yapılan erişimlerde, fonksiyon içinde bildirimi yapılan değişken, kod bloğu içinden yapılan erişimlerde ise kod bloğu içinde bildirimi yapılan değişken esas alınır.

Bu özelliği bir örnek üzerinde incelemeye çalışalım:

Örnek

```c
#include <stdio.h>

int main(void)
{
  int id=5; /* main() fonksiyonu içinde geçerlidir. */

  if (id>0) {
      int id = 10; /* Kod bloğu içinde geçerlidir. */
      printf("Kod bloğu içindeki id değişken değeri: %d\n", id);
  }

  printf("main() fonksiyonu içindeki id değişken değeri: %d", id);

  return 0;  
}
```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```c
Kod bloğu içindeki id değişken değeri: 10
main() fonksiyonu içindeki id değişken değeri: 5
```

## Fonksiyon parametre değişkenleri

Eğer bir fonksiyon kendisine aktarılan değerlere işlem yapacaksa, aktarılan değerlerin atanması için fonksiyon adından hemen sonra parantez içinde bir veya daha fazla değişken parametre tanımlanır. Bu değişkenlere fonksiyon parametre değişkenleri adı verilir.

Fonksiyon parametre değişkenleri fonksiyon lokal değişkenleri ile aynı özelliklere sahiptir. Tek farkları fonksiyona geçirilen değerlerin bu değişkenlere aktarılmasıdır.

Fonksiyonlara bir parametre geçirdiğinizde de aslınızda lokal bir değişken tanımlamış olursunuz. Bir fonksiyonun parametresi olarak tanımlanmış olan lokal değişkenler, fonksiyon çağrıldığında fonksiyona geçirilen argümanların değerini alırlar. Bu değişkenlerde tıpkı lokal değişkenler gibi fonksiyon çağrıldığında oluşturulur ve fonksiyon sona erdiğinde yok edilirler.

Bu özelliği bir örnek üzerinde incelemeye çalışalım:

Örnek

```c
#include <stdio.h>

void carpim(int id1, int id2);

int main(void)
{
  int id1=21, id2=7;

  carpim(id1, id2);
  
  return 0;
}

void carpim(int id1, int id2)
{
  printf("Çarpım sonucu: %d", id1*id2);
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

```c
#include <stdio.h>

int gid; // Global değişken bildirimi

int deger_ekle(int id);

int main(void)
{
  int id;

  id = 42;
  gid = 57; // Global değişkene erişim
 
  printf("id değişken değeri: %d\n", id);
  printf("gid değişken değeri: %d\n", gid);
 
  printf("deger_ekle() fonksiyon sonucu: %d", deger_ekle(247));
  
  return 0;
}

int deger_ekle(int id)
{
  return id + gid; // Global değişkene erişim
}  
```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```
id değişken değeri: 42
gid değişken değeri: 57
deger_ekle() fonksiyon sonucu: 304
```

Program, gid adlı global int bir değişken ve main() fonksiyonu içinde id adlı lokal bir değişken bildirimi yapar. id değişkenine 21 değerini gid değişkenine ise 35 değerini atar. Her iki değişken derğerini ekrana yazdıktan sonra, 247 değerini parametre olarak geçirerek deger_ekle() fonksiyonunu çağırır. Fonksiyon içinde parametre değeri ile gid değişken değerini toplar ve elde ettiği değeri geri döndürerek ekrana yazar. Global değişkene main() ve deger_ekle() fonksiyonları içinden erişim sağlanmaktadır.

Global değişkenlere herhangi bir ilk değer atanmadığında, otomatik olarak 0 (sıfır) değeri atanır. Lokal değişkenlere ise bir ilk değer atanmadığında, kendiliğinden herhangi bir değer atanmaz.

## Değişkenlere ilk değer atama

Önce, değer atanmamış bir lokal değişken değerini ekrana yazdırmak istediğimizde nasıl bir sonuç aldığımızı görmek için aşağıdaki örneği inceleyelim:

Örnek

```c
#include <stdio.h>

int main(void)
{
  int id;

  printf("%d", id); // Derleyici uyarı verir.
  
  return 0;
}
```

Yukarıdaki örneği derlediğimizde, derleyici uyarı verir. Programı çalıştırdığımızda, ekrana hiçbir anlamı olmayan çok farklı bir sayı yazar. Bu değerin ekrana yazılmasının nedeni henüz değişkene bir değer atanmamış olmasıdır.

Lokal bir değişkene değer vermeden kullandığımızda, belirsiz sonuçlara neden olur.

Şimdi, bildirimi yapılan değişkenlere bir değer atama işlemini incelemeye çalışalım. Bir değişken bildirimi ile yapılan ilk değer atama işlemi aşağıdaki şekilde yapılır:

veri-türü değişken-adı = sabit;

```c
int id = 1354;
```

Bir değişkene değer atamak için işlem satırında önce değişkenin adı, sonra eşit işareti (=) ve en son olarak atanacak değer yazılır.

Bir değişken bildirimi ve bu değişkene değer atama işlemi iki ayrı satırda yapılabileceği gibi tek işlem satırında da yapılabilir. Aşağıda yer alan ilk işlem satırı id adlı bir değişken bildirimi yapar ve ikinci işlem satırı id değişkenine 537 değerini atar. Üçüncü işlem satırı ise, id2 adlı int bir değişken bildirimi yaparken değişkene 751 değerini atayarak, üstteki iki satırın yaptığı işlemi tek işlem satırında gerçekleştirir.

```c
int id1;   // Değişken bildirim satırı
id1 = 537; // Değişkene değer atama satırı

int id2 = 751; // Değişken bildirimi ve değer atama işlemi aynı satırda yapılır.
```

Sonuç olarak, bir değişkene ya ilk bildirildiğinde, ya da daha sonra bir değer atanabilir.

Değişkenlere ilk değer atama işlemini bir örnek üzerinde incelemeye çalışalım:

Örnek

```c
#include <stdio.h>

int main(void)
{
  char cd = 'A';
  int id = 43;  

  printf("cd değişken değeri: %c\n", cd);
  printf("id değişken değeri: %d", id);
  
  return 0;
}
```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```c
cd değişken değeri: A
id değişken değeri: 43
```

Program, oluşturduğu cd adlı char bir değişkene 'A' karakterini, id adlı int bir değişkene ise 43 sayısınıilk değer atama yöntemi ile atar. Sonra değişken değerlerini ekrana yazar.

İlk değer atama işlemlerinde, global değişkenlere atanan değerler mutlaka sabit bir değer olmalıdır. Atanan değer bir değişken olarak tanımlanamaz. Başka bir deyişle, ilk değer atama işlemlerinde, ilk değer atama işlemcisinin (=) sağ tarafında yer alan değer mutlaka bir sabit olmalıdır.

Örnek

```c
#include <stdio.h>

int gid = 21; // Global değişkene sadece sabit bir değer atanabilir.

int fonk(void);

int main(void)
{
  int id1 = 84;      // Lokal değişkene sabit değer atama
  int id2 = id1/gid; // Lokal değişkene bir işlem sonucunu atama
  int id3 = fonk();  // Lokal değişkene fonksiyonun geri döndürdüğü değeri atama

  printf("id1 değişken değeri: %d\n", id1);
  printf("id2 değişken değeri: %d\n", id2);
  printf("id3 değişken değeri: %d", id3);
  
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
id3 değişken değeri: 7
```

Program, oluşturduğu gid adlı global bir değişkene ve id1 adlı lokal değişkene yaptığı ilk değer atamalarında sabit değerler kullanır. id2 değişkenine bir işlem sonucunu, id3 değişkenine ise fonk() fonksiyonu içinde yapılan bir işlem sonucunu atar.

Global değişkenlere bir defaya mahsus olmak üzere sadece programın başında bir ilk değer atama yapabiliriz. Lokal değişkenlere ise içinde tanımlandıkları fonksiyonların her çağrılışında bir ilk değer atama işlemi yapılır.

Bu özelliği bir örnek üzerinde incelemeye çalışalım:

Örnek

```c
#include <stdio.h>

int gid = 21;

int kare_al(int id);

int main(void)
{
  int id=5;

  printf("id değişkeninin karesi: %d\n", kare_al(id));

  id=7;
  printf("id değişkeninin karesi: %d\n", kare_al(id));

  printf("gid değişken değeri: %d", gid);

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

Program, gid adlı global int bir değişken oluştururken 21 değerini ilk değer olarak atar. main() fonksiyonu içinde, id adlı int bir değişken oluştururken 5 değerini ilk değer olarak atar. kare_al() fonksiyonunu id değişken değerini önce 5 sonra 7 değeri ile parametre olarak geçirerek, iki defa çağırır. Her defasında, fonksiyon içindeki id2 lokal int değişkenine parametre olarak geçirdiği değişken değerini ilk değer atama yöntemi ile atar. Bir fonksiyonun her çağrılışında, lokal değişken değerleri yeniden bir ilk değer alır.

Program yazarken başka bir işlem satırında değer atama yapmak yerine ilk değer atama yöntemini kullanmanın en büyük avantajı daha kısa ve daha hızlı bir kodlama yapabilmektir.

Global bir değişkene bir ilk değer atamazsak, değişken sıfır (0) değerini alır. Lokal bir değişkene bir ilk değer atamazsak, değişken anlamsız bir değer alır. Şimdi, bu özelliği bir örnek üzerinde incelemeye çalışalım:

Örnek

```c
#include <stdio.h>

int gid;

int main(void)
{
  int id;

  printf("gid global değişken değeri: %d\n", gid);
  printf("id lokal değişken değeri: %d", id); // Derleyici uyarı verir.

  return 0;
}
```

Program, oluşturduğu gid adlı global int bir değişkene ve id adlı lokal int bir değişkene bir ilk değer vermediği için, global değişken için ekrana sıfır (0), lokal değişken için anlamsız bir değer yazar.

Bir işlem satırında birden fazla değişkene ilk değer atama yapılabilir:

```c
int id1 = 7, id2 = 21, id3;
char cd1 = 'A', cd2 = 'F';
float fd1 = 45.324, fd2 = 852.321
```

Bu özelliği de bir örnek üzerinde incelemeye çalışalım:

Örnek

```c
#include <stdio.h>

int main(void)
{
  int id1 = 7, id2 = 21;
  char cd1 = 'F', cd2 = 'K';
  double dd1 = 652.435, dd2 = 234.741;

  printf("int değişken değerleri: %d %d\n", id1, id2);
  printf("char değişken değerleri: %c %c\n", cd1, cd2);
  printf("double değişken değerleri: %f %f", dd1, dd2);

  return 0;
}
```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar: 

```
int değişken değerleri: 7 21
char değişken değerleri: F K
double değişken değerleri: 652.435000 234.741000
```

Program, değişken bildiriminin yapıldığı her iki satırda ilk değer atama yöntemi ile ikişer farklı değişkene değerler atar ve ekrana yazar.

## Atamalarda veri çeşidi değişimi

C'de, atama işlemlerinde, eğer atama işlemcisinin her iki tarafında yer alan verilerin çeşitleri farklı ise, program verilerin çeşidini değiştirir. Bu veri çeşidi değişimi belirli bir kurala göre yapılır.

Atama yapılan bir işlem satırında, atama işaretinin sağ tarafında yer alan veri çeşidi atama işaretinin sol tarafında yer alan veri çeşidinden farklı ise sağ tarafta yer alan verinin çeşidi sol taraftaki veri çeşidine çevrilir.

Bu özelliği bir örnek üzerinde incelemeye çalışalım:

Örnek

```c
#include <stdio.h>

int main(void)
{
  int id1, id2;  // 32 bit int değişken
  char cd1, cd2; // 8 bit char değişken

  id1 = 87;  // 87 = W = 00000000 00000000 00000000 01010111
  cd1 = 'K'; // K = 75 = 01001011

  printf("id1 değişken değeri: %d\n", id1);
  printf("cd1 değişken değeri: %c\n", cd1);

  id2 = cd1; // id2 = 75 = K = 00000000 00000000 00000000 01001011
  cd2 = id1; // cd2 = 87 = W = 01010111

  printf("id2 değişken değeri: %d\n", id2);
  printf("cd2 değişken değeri: %c", cd2);
  
  return 0;
}
```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```c
id1 değişken değeri: 87
cd1 değişken değeri: K
id2 değişken değeri: 75
cd2 değişken değeri: W
```

Program, id1 ve id2 adlı iki adet int ve cd1 ve cd2 adlı iki adet char veri türünden olmak üzere dört adet değişken tanımlar. id1 ve cd1 değişkenlerine atadığı değerleri sıra ile id2 ve cd2 değişkenlerine atar. Sonra, değişken değerlerini ekrana yazar. id2 int değişkenine atanan değer char, cd2 char değişkenine atanan değer int bir değer olduğu halde herhangi bir veri kaybı olmaz. Çünkü, 32 bit'lik int değişkenlere atanan değer 8 bit'lik char değişkenlerinb alabileceği büyüklüktedir.

Konunun daha iyi anlaşılabilmesi için aşağıdaki ifadeleri birlikte inceleyelim:

```c
               char                        int

  K (75)     01001011      00000000 00000000 00000000 01001011

  87 (W)     01010111      00000000 00000000 00000000 01010111
```

id1 int değişkenine atanan 87 sayısının ikili sistemdeki yazılımı yukarıdaki ikinci satırın sağ tarafında yer almaktadır. 32 bit'ten oluşan bu değer cd2 char değişkenine atandığında, en soldaki 24 bit kaybolur. cd1 char değişkenine atanan 'K' karakterinin ikili sistemdeki yazılımı ise yukarıdaki ilk satırın sol tarafında yer almaktadır. 8 bit'ten oluşan bu değer id2 int değişkenine atandığında, ikili sistemdeki yazılımın sol tarafına 24 bit eklenir.

Eğer sol taraftaki veri çeşidi sağ taraftakinden büyük ise veri çeşidi değişiminde herhangi bir sorun çıkmaz. Ancak, sol taraftaki veri çeşidi sağ taraftakinden küçük ise değişimden dolayı veri kaybı meydana gelebilir. Bu özelliği bir örnek üzerinde incelemeye çalışalım:

Örnek

```c
#include <stdio.h>

int main(void)
{
  char cd;
  int id;

  id = 3698;
  cd = id;

  printf("id değişken değeri: %d\n", id);
  printf("cd değişken değeri: %d", (int)cd);

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

```c
#include <stdio.h>

int main(void)
{
  int id;
  short int sid;
  long int lid;
  float fd;
  double dd;

  fd = 2431.52;
  id = fd;

  printf("fd değişken değeri: %.2f\n", fd);
  printf("id değişken değeri: %d\n\n", id);

  dd = fd;

  printf("fd değişken değeri: %.2f\n", fd);
  printf("dd değişken değeri: %.2f\n\n", dd);

  lid = 91615;
  sid = lid;

  printf("lid değişken değeri: %ld\n", lid);
  printf("sid değişken değeri: %hd", sid);

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

## Değişken tanımlayıcıları

C, aşağıda gösterilen 7 kelimeyi değişken adlarından önce tanımlayarak size değişkenleri farklı şekilde kullanma olanağı sağlar.

```
. auto
. extern
. register
. static
. const
. volatile
. restrict (C99)
```

## auto değişken tanımlayıcısı

auto değişken tanımlayıcısı, bir fonksiyon veya kod bloğu içinde tanımlanan bütün lokal değişkenler için ön tanımlı belirleyici olarak kullanılır. Bir değişken için, bir depolama sınıf belirleyicisi tanımlanmadığında, otomatik olarak auto değişken tanımlayıcısı sahip olacaktır.

auto olarak bildirimi yapılan değişkenlerin kapsamı, tanımlandıkları fonksiyon veya kod bloğu içerisinde olup, bu fonksiyon veya kod bloğunun dışından erişim sağlanmaz.

auto olarak bildirimi yapılan değişkenlerin ömrü, tanımlandıkları fonksiyon veya kod bloğu sona erdiğinde sona erer.

## extern değişken tanımlayıcısı

C dilinde yazılan uzun programlar derleme zamanını çok artıracağı için, genellikle uzun programlar iki veya daha fazla dosyaya bölünerek derlenir. Bu sistemden aynı zamanda farklı amaçlarla kullanılan kodların düzenlenmesi içinde faydalanılır. Bir proje içinde içinde yer alan bu dosyalar tek bir komutla ayrı ayrı derlendikten sonra birleştirilerek tek bir çalışan .exe uzantılı dosya oluşturulur. Bu durumda, bir dosya içinde tanımladığınız global değişkenler diğer dosya içinde tanınmazlar. Eğer bir dosya içinde tanımladığımız global değişkenlerin diğer dosyalar içinde geçerli olmasını istersek, diğer dosyalarda yer alan bütün fonksiyonların dışında yaptığımız değişken tanımlamalarının baş tarafına extern ifadesini getirmemiz gerekir.

Bir değişkeninin başında extern ifadesini kullanmak, o değişkenin projede yer alan kod dosyalarının birinde tanımlandığını ve o değişkene extern ifadesini kullandığımız dosya içinden erişim sağlamak istediğimizi gösterir. extern değişken belirleyicisinin kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```c
// deneme1.c
#include <stdio.h>

void fonk(void);

int gid = 287; // global int değişken tanımlaması

int main(void)
{
  printf("deneme1.c gid değişken değeri: %d\n", gid);

  fonk(); // deneme2.c dosyasındaki fonk() fonksiyonuna çağrı

  return 0;
}

// deneme2.c
extern int gid; // global int değişken bildirimi

void fonk(void)
{
  printf("deneme2.c gid değişken değeri: %d", gid);
}
```

Yukarıda verilen iki dosyayı deneme1.c ve deneme2.c adları ile bir proje içine kaydettikten sonra derleyiciyi kullanarak projeyi derler ve deneme.exe adlı tek bir program adı ile çalıştırırsak aşağıdaki ifadeleri ekrana yazar:

```
deneme1.c gid değişken değeri: 287
deneme2.c gid değişken değeri: 287
```

Programda, ilk satırı ekrana yazan deneme1.c, ikinci satırı ekrana yazan ise deneme2.c dosyasındaki fonk() fonksiyonu içindeki işlem satırıdır.

## register değişken tanımlayıcısı

register değişken tanımlayıcısı, her veri türüne uygulanabilir.

Program, bir değişken register değişken tanımlayıcısı ile tanımladığında, derleyicinin bu değişkenin değerini, normal koşullarda değişkenlerin depolandığı bellek yerine, CPU içindeki yazmaçlardan birine kaydetmesini ister. Bu durumda, değişken üzerinde yapılan tüm işlemler yazmaç üzerinde yapılacağı için, bellek erişimi gerekmediğinden, işlemler daha hızlı gerçekleştirilir.

register değişken tanımlayıcısı sadece lokal değişkenlerle birlikte kullanılabilir.

Bir fonksiyon veya kod bloğu içinde tanımlanan veya bir fonksiyon parametresi olarak bildirimi yapılan değişkenleri register değişken tanımlayıcısı ile birlikte tanımlayabiliriz.

Derleyici register değişken tanımlayıcısı ile tanımlanan değişken sayısı belirli bir sınırı aştığında, otomatik olarak bu değişkenlerin bir kısmını normal değişken haline çevirecektir.

Eğer programımızda bir değişkeni çok sık kullanıyorsak, bu değişken bildiriminin başında register ifadesini kullanmamız programımızın hızını artırır. Çünkü, bilgisayar bu şekilde tanımlanan değişkenlere daha hızlı bir şekilde ulaşır.

Ancak, CPU'da sınırlı sayıda yazmaç bulunduğu için, eğer register değişken sayısı çok fazla olursa, bilgisayar belli bir sayıdan sonraki register değişkenleri normal değişken olarak kabul eder. Bu tanımlamayı yaptığımızda, derleyiciye bu değişkene öncelik tanıyarak, performansı artırması için bellek yerine CPU içinde yer alan yazmaçlara yerleştirmesi konusunda bir istek yapılmış olur. Ama, bu isteğin mutlaka yerine getirileceğine dair bir garanti yoktur. Bu nedenle, çok sık kullanılan değişkenleri register olarak tanımlamak gerekir. Buna örnek olarak, döngüleri kontrol etmekte kullanılan değişkenler gösterilebilir. Bu değişkenler çok sık kullanıldığından programımızın performansı hissedilir ölçüde artacaktır.

Aslında, normal koşullarda bir değişken herhangi bir değişken tanımlayıcısı ile tanımlanmasa bile, derleyici eğer iyileştirme yapma gereği duyarsa, bu değişkeni CPU yazmacına kaydederek kullanır. Bir değişkeni volatile olarak tanımladığımızda, derleyicisinin iyileştirme işlemi yapmasını istemediğimizi, register olarak tanımladığımızda ise, derleyicisinin iyileştirme işlemi yapmasını özellikle istediğimizi ve değişkeni CPU yazmacına kaydetmesini belirtmiş oluruz.

Şimdi, register değişken tanımlayıcısının kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```c
#include <stdio.h>
#include <time.h>

int main(void)
{
  clock_t start_t, end_t;
  register int id1, id2;

  start_t = clock();

  for(id1=0; id1<2000000; id1++){
      for (id2=0; id2<100; id2++) { }
  }

  end_t = clock();

  printf("start_t değeri: %lu\n", start_t);
  printf("end_t değeri: %lu\n", end_t);
  printf("Döngü çalışma süresi (saniye): %.3f", (double)(end_t - start_t) / CLOCKS_PER_SEC);

  return 0;
}
```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```
start_t değeri: 0
end_t değeri: 132
Döngü çalışma süresi (saniye): 0.132
```

Program clock() fonksiyonu ile bir döngü çalışmasından önce ve sonra olmak üzere iki defa işlemci süresini hesaplar, bu değerleri saat tik sayısı olarak ve iki değerin farkını saniye olarak ekrana yazar. Program içindeki döngünün çalışma süresi 132 milisaniye'dir. Bu değer bilgisayarlar arasında farklılıklar gösterebilir.

Şimdi, aynı programı register değişken tanımlayıcısı yerine volatile değişken tanımlayıcısı kullandığımız bir örnek üzerinde incelemeye çalışalım:

Örnek

```c
#include <stdio.h>
#include <time.h>

int main(void)
{
  clock_t start_t, end_t;
  volatile int id1, id2;

  start_t = clock();

  for(id1=0; id1<2000000; id1++){
      for (id2=0; id2<100; id2++) { }
  }

  end_t = clock();

  printf("start_t değeri: %lu\n", start_t);
  printf("end_t değeri: %lu\n", end_t);
  printf("Döngü çalışma süresi (saniye): %.3f", (double)(end_t - start_t) / CLOCKS_PER_SEC);

  return 0;
}
```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```
start_t değeri: 0
end_t değeri: 536
Döngü çalışma süresi (saniye): 0.536
```

Program clock() fonksiyonu ile bir döngü çalışmasından önce ve sonra olmak üzere iki defa işlemci süresini hesaplar, bu değerleri saat tik sayısı olarak ve iki değerin farkını saniye olarak ekrana yazar. Program içindeki döngünün çalışma süresi 536 milisaniye'dir. Bu değer bilgisayarlar arasında farklılıklar gösterebilir.

## static değişken tanımlayıcısı

static değişken tanımlayıcısını lokal ve global değişkenlerle birlikte kullanabiliriz. Normal olarak, içinde lokal değişken tanımlanan bir fonksiyonu her çağırdığımızda, lokal değişken değeri yenilenir. Ancak, bu lokal değişkeni static olarak tanımlarsak, fonksiyonu her çağırmamızda, lokal değişken bir önceki fonksiyon çağrısındaki en son değerini korur. Sonuç olarak, static lokal bir değişkene sadece fonksiyonun ilk çağrılışında bir defaya mahsus olmak üzere değer verebiliriz.

static değişkenler, sadece tanımlandıkları fonksiyon içinde kalıcı olarak değer taşırlar. Fonksiyon dışından bu değişkenlere erişim sağlanamaz.

Şimdi, static lokal bir değişken kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```c
#include <stdio.h>

void fonk(void);
void fonk_sta(void);

int main(void)
{
  fonk();
  fonk_sta();

  printf("\n");

  fonk();
  fonk_sta();

  return 0;
}

void fonk(void)
{
  int id = 1;

  printf("fonk() id değişken değeri: %d\n", id);

  id = id + 21;

  printf("fonk() id değişken değeri: %d\n", id);
}

void fonk_sta(void)
{
  static int id = 1; // Sadece fonksiyonun ilk çağrısında çalışır.

  printf("fonk_sta() id değişken değeri: %d\n", id);

  id = id + 21;

  printf("fonk_sta() id değişken değeri: %d\n", id);
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

Program, fonk() ve fonk_sta() fonksiyonlarını sırasıyla ikişer kez çağırarak, lokal olarak tanımlanmış değişken değerlerini ekrana yazdırır. Her iki fonksiyonda da lokal değişken değerleri artırılmasına rağmen sadece fonk_sta() fonksiyonu içindeki id değişkeni bir önceki fonksiyon çağrısında aldığı değeri korumaktadır. Bu olanağı sağlayan değişkenin statik tanımlanmış olmasıdır.

fonk_sta() fonksiyonuna yapılan ilk çağrıda, fonksiyon içindeki id lokal değişkenine, sadece bir defaya mahsus olmak üzere, ilk değer olarak 1 değeri atanır. Değişken değeri ekrana yazılır. Değişken değerine 21 değeri eklenir ve değişken tekrar ekrana yazılır. fonk_sta() fonksiyonuna yapılan bir sonraki çağrıda, id lokal değişkeni bildirim ve ilk değer verme satırı dever dışı kalır. Böylece, değişkene bir önceki fonksiyon çağrısında verilen değer korunur. fonk_sta() fonksiyonu ikinci kez çağrıldığında, fonksiyon girişinde lokal id değişken değeri 22 olur.

static depolama sınıfı belirleyicisini global değişkenlerle de kullanabiliriz. static global bir değişken tanımladığımızda, bu değişkeni sadece içinde tanımlandığı dosyada bulunan fonksiyonlar kullanabilir. Bunun yanında, aynı programa ait farklı dosyalarda bulunan ve aynı isme sahip biri normal diğeri de static olan iki global değişken tanımlayabiliriz. Bu özelliği bir örnek üzerinde incelemeye çalışalım:

Örnek

```c
// deneme1.c
#include <stdio.h>

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
  printf("deneme1.c gid değişken değeri: %d\n", gid);
}

// deneme2.cpp
#include <iostream>

using namespace std;

int gid = 35; // global int değişken bildirimi

void fonk2(void)
{
  printf("deneme2.c gid değişken değeri: %d", gid);
}
```

Yukarıda verilen iki dosyayı deneme1.c ve deneme2.c adları ile bir proje içine kaydettikten sonra derleyiciyi kullanarak projeyi derler ve deneme.exe adlı tek bir program adı ile çalıştırırsak aşağıdaki ifadeleri ekrana yazar:

```
deneme1.c gid değişken değeri: 21
deneme2.c gid değişken değeri: 35
```

Program, her iki dosyada gid adlı birer adet global değişken tanımlar. Aynı isme sahip 2 değişken olduğu halde deneme1.c dosyasındaki değişkenin static olarak tanımlanması farklı 2 değişken olarak algılanmalarını sağlar.

## const değişken tanımlayıcısı

Değişken bildiriminin başına const ifadesini getirdiğimizde, program değişkenin değerini hiç bir şekilde değiştiremez. const değişkenlere bir ilk değer verilebilir.

Bir fonksiyona geçirilen bir parametrenin, fonksiyon tarafından değiştirilmesini önlemek için const değişken tanımlayıcısını kullanabiliriz. Böylece fonksiyona aktardığımız değişken değerinin korunmasını garantiye alırız.

Şimdi, const tanımlayıcısının bir değişkenle kullanılmasını bir örnekle incelemeye çalışalım:

Örnek

```c
#include <stdio.h>

int main(void)
{
  int id1 = 7;
  const int id2 = 21;

  printf("id1 değişken değeri: %d\n", id1);
  printf("id2 değişken değeri: %d\n\n", id2);

  id1 = 35;
  // const bir değişkene değer atama yapılamayacağından, derleyici hata verir.
  // id2 = 49;

  printf("id1 değişken değeri: %d\n", id1);
  printf("id2 değişken değeri: %d", id2);

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

```c
#include <stdio.h>

int kare_al(const int id);

int main(void)
{
  int id = 7;

  printf("id değişken değerinin karesi: %d", kare_al(id));

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

Program, id adlı int bir değişken bildirimi yaparken değişkene bir ilk değer atar. id değişkenini parametre olarak geçirerek, kare_al() fonksiyonunu çağırır. Fonksiyon parametre değerinin karesini alarak elde ettiği değeri geri döndürür. Parametrenin bildirimi const olarak yapıldığından fonksiyon içinde id değişkeninin değiştirilmesi derleyicinin hata vermesine neden olur. Geri döndürülen değeri ekrana yazar.

## volatile değişken tanımlayıcısı

Eğer bir değişken bildiriminin başına volatile ifadesini getirirsek, derleyici bu değişken değerinin program içinde herhangi bir zamanda, program içinde yer alan kodlar dışında, farklı kaynaklar tarafından değiştirilebileceğini anlar. Burada bahsi geçen kaynaklar, bir kesme (interrupt), harici kesme, doğrudan bellek erişimi veya paylaşılan kaynaklar olabilir. Normal değişkenler kullanıldığında, derleyici iyileştirme işlemi uygular ve değişkeni bellek yerine yazmaca ve ön belleğe yükler.

Kesme (Interrupt), işlemcinin yazılım tarafından işlem yapılması gereken bir olaya verdiği karşılıktır. Bir kesme koşulu, işlemciyi uyarır ve işlemciye izin verildiğinde o anda yürütülen kodu kesintiye uğratması için bir talep görevini yerine getirir. Böylece ortaya çıkan olaya zamanında işlem yapılır. Talep kabul edilirse, işlemci, olayla ilgilenmek için mevcut faaliyetlerini askıya alarak, durumunu kaydederek ve kesme işleyicisi (kesme hizmeti rutini - ISR) adı verilen bir fonksiyonu çalıştırarak karşılık verir. Genellikle donanım aygıtları tarafından dikkat gerektiren elektronik veya fiziksel durum değişikliklerini belirtmek için kullanılan kesmeler, özellikle gerçek zamanlı hesaplamada bilgisayar çoklu görevini uygulamak için de yaygın olarak kullanılır.

Doğrudan Bellek Erişimi (Direct Memory Access - DMA), daha hızlı bir şekilde veri transferi yapabilmek amacıyla, merkezi işlem biriminden (Central Processing Unit - CPU) bağımsız olarak, disk sürücü kontrol birimleri, grafik kartları, ağ kartları ve ses kartları gibi çevre bileşenlerinin Rastgele Erişimli Hafıza (Random Access Memory - RAM) bloğuna erişebilmesini sağlayan bir özelliktir.

volatile değişkenler kullanıldığında, derleyici iyileştirme işlemi yapmaz ve değişkeni yazmaç yerine belleğe yükler. Değişkeni kullanmak istediğimizde, değişken değeri bellekten yazmaca aktarılır, gerekli işlemler yapılır ve sonuçta elde edilen değişken değeri tekrar belleğe yüklenir.

Bir değişken volatile olarak tanımlandığında, derleyicinin herhangi bir iyileştirme yapmaması ve değişken değerinin bellekten okuması sağlanır.

volatile niteleyicisinin değişken ve işaretçilerle kullanılmasını gösteren farklı örnekler aşağıda gösterilmektedir:

```c
volatile int id; // volatile değişken bildirimi
volatile int *ip; // işaretçi volatile değil, gösterdiği değişken volatile
int *volatile ip; // işaretçi volatile, gösterdiği değişken volatile değil
volatile int *volatile ip; // işaretçi ve değişken volatile 
```

Bir değişken normal yöntemle tanımlandığında, derleyici iyileştirme uygulamaz ve değişken değerinin değişmeyeceğini kabul ederek, yazmaca yükler. Değişkeni kullanmak istediğinde, her defasında yazmaçtan okur.

```c
// Normal değişken bildirimi (Derleyici iyileştirme yapar)
int id1 = 21;
yazmaç = id1; // id1 değeri yazmaca kopyalanır.

int id2 = yazmaç; // id1 değerine yazmaç yoluyla erişim sağlanır.
int id3 = yazmaç; // id1 değerine yazmaç yoluyla erişim sağlanır.

// volatile değişken bildirimi
volatile int id1 = 21;

int id2 = id1; // id1 değerine bellek yoluyla erişim sağlanır.
int id3 = id1; // id1 değerine bellek yoluyla erişim sağlanır.


```

Bir değişken değerinin beklenmedik şekilde değişebildiği durumlarda, değişken volatile olarak bildirilmelidir. Bu şekilde değişim gösterebilen üç tip değişken vardır:

1. Memory-mapped çevresel (peripheral) register'lar

Gömülü sistemler, genellikle karmaşık çevre birimleri olan gerçek donanım içerir. Gömülü sistemlerde, tüm çevre birimleri belirli bir bellek adresinde bulunur. Bu çevre birimleri, değerleri program akışına zaman uyumsuz olarak değişebilen register'lar içerir.

Bir programda, çevre birim register'larına uygun bir şekilde erişmek için, çevre birim register'larına bir c değişkeni ile eşleştirmeli ve bu değişkene işaretçi kullanarak erişim sağlamalıyız.

2. Bir kesme (interrupt) servis rutini tarafından değiştirilen global değişkenler

Interrupt servisi ile ilgili bir fonksiyon kullanıldığında, programın main() fonksiyonu ile interrupt servis fonksiyonu global bir değişkeni ortaklaşa kullanırlar. Bu durumda, global değişken her iki fonksiyon tarafından okunabilir veya değişkene bir değer atanabilir.

3. Multi-threaded bir uygulamada birden fazla görev tarafından erişilen global değişkenler

Gerçek zamanlı işletim sistemlerinde kuyrukların, pipes ve zamanlayıcıların esasına göre çalışan diğer iletişim mekanizmalarının varlığına rağmen, gerçek zamanlı işletim sistemlerinde görevlerin paylaşılan bir bellek konumu (global değişkenler) aracılığıyla bilgi alışverişinde bulunması mümkündür. Bu nedenle, tüm paylaşılan global nesneler (değişkenler, bellek tamponları, donanım register'ları vb.) derleyicinin beklenmeyen davranışlarını önlemek için volatile olarak bildirilmelidir.

volatile anahtar kelimesi, nesneleri derleyici optimizasyonundan koruyan ve derleyiciye, nesnenin (değişken) değerinin kod tarafından herhangi bir işlem yapılmadan herhangi bir zamanda değişebileceğini söyleyen bir niteleyicidir. Bir değişkenin önbellekten register'a aktarılmasını engeller ve değişkenin her erişimde bellekten okunmasını sağlar.

Bir C programında volatile anahtar kelimesinin kullanımına aşağıdaki durumlarda ihtiyaç duyulabiliriz:

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

Şimdi, volatile tanımlayıcısının kullanılmasını çoklu thread ile çalışan bir örnekle incelemeye çalışalım:

Örnek

```c
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

#define DEGER 10000

volatile int gid = 0;
volatile int durum = 1;

void *deger_artir(void* pname);
void *deger_bildir_yuz(void* pname);
void *deger_bildir_bin(void* pname);

int main(void)
{
  pthread_t thread1, thread2, thread3;
  int id=0;
  int idth;

  printf("Thread oluşturma: %d\n", id++);
  idth = pthread_create(&thread1, NULL, deger_artir, NULL);
  if (idth) {
      printf("Thread oluşturma hatası: %d\n", idth);
      exit(-1);
  }

  printf("Thread oluşturma: %d\n", id++);
  idth = pthread_create(&thread2, NULL, deger_bildir_yuz, NULL);
  if (idth) {
      printf("Thread oluşturma hatası: %d\n", idth);
      exit(-1);
  }

  printf("Thread oluşturma: %d\n", id);
  idth = pthread_create(&thread3, NULL, deger_bildir_bin, NULL);
  if (idth) {
      printf("Thread oluşturma hatası: %d\n", idth);
      exit(-1);
  }

  printf("\n");

  while (gid<DEGER) {
     if (durum==2) printf("\n\n100'ler basamağı geçildi!\n\n");
     else if (durum==3) printf("\n\n100'ler basamağı geçildi!\n\n");
     durum=0;
  }

  return 0;
}

void *deger_artir(void* pname)
{
  int id;

  while(durum); // deger_bildir_bin() thread fonksiyonundan önce başlamaması için

  for (id=0; id<DEGER; id++) printf("%d ", gid++);

  return 0;
}

void *deger_bildir_yuz(void* pname)
{
  while(durum); // deger_bildir_bin() thread fonksiyonundan önce başlamaması için

  while (gid<DEGER) {
    if ((gid>0) && (gid%100==0)) durum = 2;
  }

  return 0;
}

void *deger_bildir_bin(void* pname)
{
  durum = 0;

  while (gid<DEGER) {
    if ((gid>0) && (gid%1000==0)) durum = 3;
  }

  return 0;
}
```

Program, önce thread1 adlı bir thread oluşturur. İlk thread'e ait olan deger_artir() fonksiyonu çalışmaya başlar. Fonksiyon, durum adlı global değişken değeri 1 olduğundan while döngüsünde beklemeye başlar. Program, herhangi bir thread oluşturduktan sonra, main() fonksiyonundaki bir sonraki işlem satırından çalışmasına devam etmek için, bu thread'e ait olan fonksiyonun çalışmasının sona ermesini beklemez. Bu nedenle, hiç beklemeden thread2 adlı bir thread oluşturur. İkinci thread'e ait olan deger_bildir_yuz() fonksiyonu çalışmaya başlar. Fonksiyon, durum adlı değişken değeri 1 olduğundan while döngüsünde beklemeye başlar. Son olarak, thread3 adlı bir thread oluşturur. Üçüncü thread'e ait olan deger_bildir_bin() fonksiyonu çalışmaya başlar. Fonksiyon, ilk olarak durum adlı değişkene 0 değeri atar. Böylece, deger_bildir_yuz() ve deger_bildir_bin() fonksiyonları içindeki while döngüleri sona erer ve bir sonraki döngüler çalışmaya başlar.

Bu durumda, main() fonksiyonu ve her üç thread'e ait fonksiyonlarda yer alan son döngüler aynı anda çalışmaya başlar. deger_artir() fonksiyonu gid adlı global değişken değerini, her defasında bir değer olmak üzere, 10000 sayısından küçük olduğu sürece artırır ve değişken değerini ekrana yazar. deger_bildir_yuz() fonksiyonu gid değişkeninin aldığı değeri takip ederek, 100 ve katlarını aldığında, durum adlı değişkene 2 değerini atar. main() fonksiyonundaki while döngüsü içinde if koşulu karşılandığından, "100'ler basamağı geçildi!" ifadesi ekrana yazılır ve durum adlı değişkenine 0 değeri atanır. deger_bildir_bin() fonksiyonu da deger_bildir_yuz() fonksiyonunun yaptığı işlemlerin aynısını 1000 sayısı için yapar. main() fonksiyonundaki while döngüsü içinde if koşulu karşılandığından, "1000'ler basamağı geçildi!" ifadesi ekrana yazılır ve durum adlı değişkenine 0 değeri atanır.

Şimdi, volatile tanımlayıcısının kullanılmasını farklı bir örnekle incelemeye çalışalım:

Örnek

```c
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

#define MAXDEGER 10000
#define DEGER 75

volatile int gidcur = 0;
volatile int gid = 0;

void *deger_artir(void* pname);

int main(void)
{
  pthread_t thread;
  int idth;
  int ulid=0;

  printf("Thread oluşturma\n\n");
  idth = pthread_create(&thread, NULL, deger_artir, NULL);
  if (idth) {
	  printf("Thread oluşturma hatası: %d\n", idth);
      exit(-1);
  }

  while (gidcur<MAXDEGER) {
    if (gid) {
        ulid++;
        gid=0;
    }
  };

  while(gid);

  printf("\nmain(): 0-%d arasında %d  sayısına tam olarak bölünenlerin sayısı: ",  MAXDEGER, DEGER, ulid;

  return 0;
}

void *deger_artir(void* pname)
{
  int id1;
  int id2=0;

  for (id1=0; id1<MAXDEGER; id1++) {
       if (id1%75==0) {
           printf("%d ", id1);
           gid=1;
           id2++;
       }
       gidcur++;
  }

  printf("\n\ndeger_artir(): 0-%d arasında 75 sayısına tam olarak bölünenlerin sayısı: %d", MAXDEGER, id2);

  return 0;
}
```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```c
Thread oluşturma

0 75 150 225 300 375 450 525 600 675 750 825 900 975 ... 9750 9825 9900 9975 

deger_artir(): 0-10000 arasında 75 sayısına tam olarak bölünenlerin sayısı: 134
main(): 0-10000 arasında 75 sayısına tam olarak bölünenlerin sayısı: 134

```

Program, önce thread adlı bir thread oluşturur. Thread'e ait olan deger_artir() fonksiyonu çalışmaya başlar. Program, herhangi bir thread oluşturduktan sonra, main() fonksiyonundaki bir sonraki işlem satırından çalışmasına devam etmek için, bu thread'e ait olan fonksiyonun çalışmasının sona ermesini beklemez. Bu nedenle, hiç beklemeden main() fonksiyonu içindeki while döngüsü çalışmaya başlar.

Thread'e ait olan deger_artir() fonksiyonu gidcur adlı global değişken değerini, her defasında bir değer olmak üzere, 10000 sayısından küçük olduğu sürece artırır ve değişken değeri 75 ve katları ise, değeri ekrana yazar ve 
gid değişkenine 1 değeri atar ve ulid2 adlı değişken değerini bir artırır. main() fonksiyonu içindeki while döngüsü içinde if koşulu karşılandığından, ulid değeri bir artırılır ve gid değişkenine 0 değeri atanır.

deger_artir() ve main() fonksiyonu içindeki döngüler sona erdiğinde, 0-10000 arasında 75 sayısına tam olarak bölünenlerin sayısı olan 134 değeri iki kez ekrana yazılır.

## restrict değişken tanımlayıcısı

restrict değişken tanımlayıcısı, C99 standardı ile getirilmiş olan ve işaretçi bildirimlerinde kullanılabilen bir anahtar kelimedir. Bu anahtar sözcüğü ile, programcı derleyiciye işaretçinin kullanım süresince, yalnızca işaretçinin kendisinin veya doğrudan ondan türetilmiş bir değerin, işaretçinin işaret ettiği nesneye erişmek için kullanılabileceğini bildirmiş olur. Farklı bir ifade ile, restrict anahtar kelimesi ile tanımlanan işaretçi ile adreslenen bellek değiştirilemez veya sadece bu işaretçi ile erişilebilir.

restrict değişken tanımlayıcısı ile tanımlanan işaretçilerle tasarlanan kodlar daha hızlı çalışır.

restrict değişken tanımlayıcısı sadece işaretçilerle birlikte kullanılabilir.
