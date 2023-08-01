---
title:  C Programlama Fonksiyonlar
author: sonsuz
date: 2023-08-01 15:04:00 +0300
categories: [Program,C]
tags: [programlama,fonksiyon,c,parametre,argüman,return]
---

C'de, fonksiyon bir veya daha fazla işlem satırından oluşan kodların bir kod bloğu şeklinde yapılandırılması ile oluşturulur. Fonksiyonlar oluşturulduktan sonra programın herhangi bir yerinden sadece fonksiyon adı kullanılarak çağrılabilir. Bu sayede, çok fazla sayıda işlem satırı tek bir isim kullanılarak çalıştırılmış olur.

## Fonksiyon yapısı

Fonksiyon, eğer varsa, kendisine geçirilen parametreleri de kullanarak kod bloğu içindeki işlem satırları ile bir takım işlemler yaparak bir sonuç elde eder. Elde edilen sonuç, ihtiyaca bağlı olarak, fonksiyon içinde ya da return komutu ile geri döndürüldükten sonra program içinde kullanılır.

```c
veri-türü fonksiyon-adı (parametreler)
{
  işlem satırı
  .
  .
  işlem satırı
 
  return ifade;
}

```

Fonksiyon yapısında 5 temel eleman vardır. Bu elemanlardan fonksiyon-adı ve işlem satırı mutlaka bulunmalıdır. Ancak, veri-türü, parametreler ve return ifadelerinin tanımlanması programcının ihtiyaçları doğrultusunda isteğe bağlıdır. Parametre yerine argüman ifadesi de kullanılmaktadır.

veri-türü : Fonksiyonun geri döndürdüğü veri türünü gösterir.

fonksiyon-adı : Fonksiyon adını gösterir.

parametreler : Fonksiyona geçirilen verileri gösterir. Sayısı birden fazla olabilir.

İşlem satırı : Fonksiyon içindeki işlem satırlarını gösterir.

return : Verileri geri döndürmeye yarar. Son satırda kullanılması şart değildir.

ifade : Değişken, sabit ve işlemciler kullanılarak oluşturulan veridir. Elde edilen veri türü fonksiyonun geri döndürdüğü veri türü ile aynı olmalıdır.

Fonksiyon, kendisine geçirilen parametrelerin değerlerini, işlem durumuna bağlı olarak, değiştirerek veya değiştirmeden kullanabilir.

Bir fonksiyonun geri verdiği veri türü dizi dışında herhangi bir veri olabilir. Fonksiyon dizi tipinde bir veri geri döndüremez, ancak farklı yöntemlerle bu işlemi gerçekleştiribilir.

Bir fonksiyon için geri dönen veri türü ve parametre tanımlanmadığında, bu ifadelerin yerine void ifadesini kullanarak bu durumu derleyiciye bildirebiliriz. main() fonksiyonundan önce de void ifadesi kullanılabilir.

```c
void fonksiyon-adı (void)
{
  işlem satırları
}

```

veri-türü ifadesi Eğer bir fonksiyonun adının başında veri türü tanımlanmazsa, fonksiyon int bir değer geri verir. Eğer bir fonksiyonun int değer dışında bir veri türü geri vermesi isteniyorsa, fonksiyon adının başında mutlaka bir veri türü tanımlanması gerekir.

Aşağıdaki bir ve ikinci fonksiyonlar int bir değer, üçüncü fonksiyon ise float bir değer geri verir:

```c
fonk(int d1, int d2)
{
  .
  .
  .
  
  return id+id2;
}

int fonk(int d1, int d2)
{
  .
  .
  .
  
  return id+id2;
}

float fonk(float fd1, float fd2)
{
  .
  .
  .
  
  return fd1+fd2;
}


```

## Fonksiyon bildirimi

Normal olarak, fonksiyonların kullanılmadan önce fonksiyon prototipi yöntemiyle bildirimi yapılmalıdır. Ffonksiyonların ana yapısı main() fonksiyonundan önce yer alırsa, fonksiyon bildirimi yapılmayabilir. Ancak, main() fonksiyonundan sonra yer alıyorsa, mutlaka main() fonksiyonunda önce fonksiyon bildirimi yapılmalıdır.

```c
// Fonksiyon bildiriminin yapılması gereken durum
fonk(int d1, int d2); // Fonksiyon bildirimi

int main(void)
{
  .
  .
  .
  
  return 0;
}

fonk(int d1, int d2) // Fonksiyon ana yapı bildirimi
{
  .
  .
  .
  
  return id+id2;
}

// Fonksiyon bildiriminin yapılması şart olmayan durum
fonk(int d1, int d2) // Fonksiyon ana yapı bildirimi
{
  .
  .
  .
  
  return id+id2;
}

int main(void)
{
  .
  .
  .
   
  return 0;
}


```

Bir veri türü geri veren bir fonksiyon kullanılacağı zaman, bu fonksiyonu kullanmadan önce, fonksiyonun geri vereceği veri türü ile fonksiyona geçirilecek argümanların sayısını ve türlerini programın başında belirlenmesi gerekir. Bu işleme Fonksiyon bildirimi adı verilir.

Eğer fonksiyonun yapısı main() fonksiyonundan önce tanımlanırsa, ayrıca prototip yöntemiyle bir bildirim yapılmasına ihtiyaç duyulmaz.

Fonksiyon bildiriminin genel yapısı aşağıda gösterilmektedir:

veri-türü fonksiyon-adı (veri-türü parametre1, veri-türü parametre2, ...);

Fonksiyon bildirimi yapıldığında, eğer fonksiyonu çağırırken kullandığınız argümanların sayısı ve argüman veri türü, bildirim yaparken tanımladığınızdan farklı olursa, derleyici bir hata mesajı verir. Program, fonksiyonların her çağrılmasında tanımlanan argüman sayısının ve argüman veri türlerinin fonksiyon bildirimine uygun olup olmadığını kontrol eder. Fonksiyon çağrısı ile fonksiyon bildirimi arasında uyuşmazlık olduğunda, derleyici programı derlemez. Örneğin, 3 parametreli olarak bildirimi yapılmış bir fonksiyonu 4 parametre ile çağırırsanız derleyici bir hata mesajı vererek çalışmasını sona erdirir.

Fonksiyon bildirimini bir örnek üzerinde incelemeye çalışalım:

Örnek

```c
#include <stdio.h>

int kare_al(int id); // 1

int main(void)
{
  int id;

  id = 21;

  printf("%d sayısının karesi: %d", id, kare_al(id));

  return 0;
}

int kare_al(int id)
{
  return id*id;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

21 sayısının karesi: 441

```

Program, id adlı int bir değişken tanımladıktan sonra değişkene 21 değerini atar. id değişkenini parametre olarak geçirerek kare\_al() fonksiyonunu çağırır. Fonksiyon kendisine paramter olarak geçirilen değişkenin karesini alarak elde ettiği değeri geri döndürür. Program, fonksiyon tarafından geri döndürülen değeri ekrana yazar. Başlangıçta 1 sayısı ile gösterilen işlem satırında fonksiyon bildirimi yapar. Yapılan fonksiyon bildirimi, kare\_al() fonksiyonunun geri verdiği veri türünün int olacağını ve bir adet int değişkenin parametre olarak tanımlandığını derleyiciye bildirir.

Parametre kullanmayan bir fonksiyon için yapılan bildirimin parametre bölümünde void ifadesi kullanılır:

void fonksiyon-adı(void);

Yukarıdaki satırda yer alan ilk void ifadesi fonk() fonksiyonunun herhangi bir değer geri döndürmeyeceğini, ikinci void ifadesi ise fonk() fonksiyonu için herhangi bir parametre tanımlanmadığını, başka bir deyişle fonk() fonksiyonuna herhangi bir argüman geçirilmeyeceğini göstermektedir.

Örnek

```c
#include <stdio.h>

int deger_yaz_topla(int id1, int id2);

int main(void)
{
  int id1=7, id2=21;

  printf("%d ve %d arasındaki sayıların toplamı: %d\n", id1, id2, deger_yaz_topla(id1, id2));

  id1=35, id2=50;
  
  printf("%d ve %d arasındaki sayıların toplamı: %d\n", id1, id2, deger_yaz_topla(id1, id2));

  return 0;
}

int deger_yaz_topla(int id1, int id2)
{
  int id3=0;

  for ( ; id1<=id2; id1++) {
       printf("%d ", id1);
       id3 += id1;
  }

  printf("\n");

  return id3;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 
7 ve 21 arasındaki sayıların toplamı: 210
35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 
35 ve 50 arasındaki sayıların toplamı: 680

```

Program, id1 ve id2 adlı iki adet int değişken tanımlayarak sırasıyla 7 ve 21 değerlerini atar. Değişken derğerlerini parametre oarak geçirerek, deger\_yaz\_topla() fonksiyonunu çağırır. Fonksiyon ilk değişken değeri ikinci değişken değerinden büyük veya eşit ise, 0 değeri geri döndürerek program dönüş yapar. Aksi takdirde, iki değişken değerleri arasında yer alan sayıları ekrana yazar ve bu sayıların toplamını geri döndürür. Program, fonksiyon tarafında geri döndürülen değeri ekrana yazar. Program, aynı işlemleri 35 ve 50 sayıları için yapar.

Örnek

```c
#include <stdio.h>

int topla(int id1, int id2);
int kare_al(int id);

int main(void)
{
  int id;

  id = 21;

  printf("%d sayısı ile karesinin toplamı: %d", id, topla(id, kare_al(id)));

  return 0;
}

int topla(int id1, int id2)
{
  return id1+id2;
}

int kare_al(int id)
{
  return id*id;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

21 sayısı ile karesinin toplamı: 462

```

Program, iki adet fonksiyon bildirimi yapar. Tek parametre alan kare\_al() fonksiyonu ile 21 sayısının karesini alır ve bu değeri topla() fonksiyonuna ikinci parametre olarak geçirir. İki parametre alan topla() fonksiyonu ise 21 sayısı ile sayının karesini toplar. Program, topla() fonksiyonunun geri döndürdüğü değeri ekrana yazar. Burada, bir fonksiyonun geri döndürdüğü değer diğer bir fonksiyona parametre olarak geçirilmektedir.

## Fonksiyonlar ve return ifadesi kullanımı

return ifadesi bir fonksiyondan çıkış yapmak ve program içinde fonksiyon çağrısının yapıldığı işlem satırından bir sonraki işlem satırına geçiş yapmak için kullanılır.
Eğer bir fonksiyon void olmayan bir değer geri döndürecek şekilde tanımlanmış ise, return ifadesi fonksiyonun geri döndürdüğü değerle birlikte dönüş yapar. Eğer fonksiyon void bir değer geri döndürecek şekilde tanımlanmış ise, return değeri de herhangi bir değer geri döndürmez.

return ifadesi fonksiyonun geri döndürmesi gereken değerle dönüş yapar (void veya void olmayan bir veri türü).

return ifadesinin genel kullanım şekli aşağıdaki şekildedir:

```c
veri-türü fonksiyon-adı (parametreler)
{
  işlem satırı
  .
  .
  işlem satırı
 
  return ifade;
}

```

Return satırında yer alan ifade kavramı sadece fonksiyon bir değer döndürecek şekilde tanımlanmış ise eklenir. Bu durumda, ifade ile elde edilen değer fonksiyonun geri döndüreceği değer olacaktır.

Bir fonksiyon içinde istediğimiz kadar dönüş ifadesi kullanabiliriz. Fonksiyon içindeki return ifadeleri doğrudan veya bir koşula bağlı olarak eklenebilir. Ancak, program ilk return ifadesi ile karşılaştığında, fonksiyon sona erer ve programda fonksiyon çağrısının yapıldığı işlem satırından sonraki satırdan çalışmaya devam eder.

Fonksiyonun sonunda bulunan } değerine gelindiğinde de fonksiyon tanımlanmamış bir değer döndürür. Eğer bu durum, void olmayan bir değer döndürecek şekilde tanımlanan bir fonksiyonda meydana gelirse, fonksiyonun geri döndürdüğü değer tanımsız olur.

Fonksiyon void bir değer döndürecek şekilde tanımlandığında, bir değer içeren return ifadesi kullanılamaz.

İlk olarak, herhangi bir değer döndürmeyen ve işlem satırlarının çalışması sona erdiği için } işaretinden hemen önce programa dönüş yapan bir fonksiyonun çalışmasını bir örnek üzerinde inceleyelim:

Örnek

```c
#include <stdio.h>

void deger_yaz(int limit);

int main(void)
{
  deger_yaz(10);

  return 0;
}

void deger_yaz(int limit)
{
  int id;

  for (id=1; id<=limit; id++) printf("%d ", id);
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

1 2 3 4 5 6 7 8 9 10

```

Program, deger\_yaz() fonksiyonu yoluyla, 1'den başlayarak fonksiyona parametre olarak geçirdiği 10 değerine kadar olan sayıları ekrana yazar. Döngü sona erdiğinde fonksiyonun çalışması sona erer ve main() fonksiyonu içine dönüş yapılır. Görüldüğü gibi, void bir değer geri döndüren deger\_yaz() fonksiyonu herhangi bir değer döndürmez.

Şimdi, int bir değer döndüren ve return ifadesinin sadece en son satırda kullanıldığı bir fonksiyonun çalışmasını bir örnek üzerinde inceleyelim:

Örnek

```c
#include <stdio.h>

int deger_yaz_topla(int limit);

int main(void)
{
   printf("Sayıların toplamı: %d", deger_yaz_topla(10));

  return 0;
}

int deger_yaz_topla(int limit)
{
  int id1, id2;

  for (id1=1, id2=0; id1<=limit; id1++) {
       printf("%d ", id1);
       id2 += id1;
  }

  printf("\n");

  return id2;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

1 2 3 4 5 6 7 8 9 10 
Sayıların toplamı: 55

```

Program, deger\_yaz\_topla() fonksiyonu yoluyla, 1'den başlayarak fonksiyona parametre olarak geçirdiği 10 değerine kadar olan sayıları ekrana yazar ve sayıları toplayarak bir değişkene aktarır. Fonksiyon sayıların toplamını içeren değişken değerini fonksiyonun son satırında bulunan return ifadesi ile geri döndürür. Geri döndürülen değer main() fonksiyonu içine ekrana yazılır.

Şimdi, char bir işaretçi değer döndüren ve return ifadesinin biri fonksiyonun sonunda olmak üzere 2 kez kullanıldığı, bir karakter dizi içinde bir karakterin bulunduğu konumun indeks değerini alan bir fonksiyonun çalışmasını bir örnek üzerinde inceleyelim:

Örnek

```c
#include <stdio.h>

char *bg_strchr(const char *p, int id);

int main(void)
{
  const char cstr[] = "Bilgisayar";
  char *p;
  char cd = 's';

  p = bg_strchr(cstr, cd);

  if (p) {
      printf("%c karakterinden itibaren dizi değeri: %s\n", cd, p);
      printf("%c karakterinin indeks değeri: %d\n", cd, p-cstr);	  
  }
  else printf("Karakter bulunamadı!\n");

  cd = 't';

  p = bg_strchr(cstr, cd);

  if (p) {
      printf("%c karakterinden itibaren dizi değeri: %s\n", cd, p);
      printf("%c karakterinin indeks değeri: %d\n", cd, p-cstr);
  }
  else printf("Karakter bulunamadı!\n");

  return 0;
}

char *bg_strchr(const char *p, int id)
{
  while(*p != '\0') {
    if(*p == (char)id) return ((char *)p);
    p++;
  }

  return (NULL);
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

s karakterinden itibaren dizi değeri: sayar
s karakterinin indeks değeri: 5
Karakter bulunamadı!

```

Program, bg\_strchr() fonksiyonu yoluyla, 's' ve 't' karakterlerini "Bilgisayar" karakter dizisi içinde arar, eğer karakter varsa, bulunduğu yerin bellek adres değerini geri döndürür. Eğer karakteri bulamazsa, NULL bir değer geri döndürür. Aynı zamanda, karakterden itibaren karakter dizisinin içeriğini ekrana yazar.

## Kendi kendini çağıran fonksiyonlar

Şimdiye kadar incelediğimiz örneklerde, fonksiyonların bir programın herhangi bir işlem satırından çağrılabildiğini gördük. Bir fonksiyon yine aynı fonksiyonun içinde yer alan bir işlem satırı ile de çağırabilir.

Kendi kendini çağıran fonksiyonlar kullanırken, bu fonksiyonlarda yer alan kendini çağırma işlem satırını, programın mutlaka bir if koşuluna bağlı olarak çalıştırmasını sağlayacak şekilde, tanımlamak gerekir. Aksi takdirde, beklenmedik sonuçlarla karşılaşılabilir.

Bir fonksiyonun kendini çağırdığı işlem satırı mutlaka bir if koşuluna bağlı olarak çalıştırılmalıdır.

Fonksiyonların kendi kendini çağırma özelliğini sadece gerekli olduğu zaman kullanmakta fayda vardır. Aksi takdirde, yazılan programların anlaşılması oldukça zorlaşır.

Şimdi bu özelliği örnekler üzerinde incelemeye çalışalım:

Örnek

```c
#include <stdio.h>

void fonk(char *cp1, char *cp2);

int main(void)
{
  char cdizi[50] = "Kendi kendini ";

  fonk(cdizi, "çağxırxan fonxksxiyoxnlxar");
  printf("%s", cdizi);

  return 0;
}

void fonk(char *cp1, char *cp2)
{
  while (*cp1) cp1++; // 1

  if (*cp2) {
      if (*cp2!='x') *cp1++ = *cp2;
      *cp2++;

      fonk(cp1, cp2);
  }
  else *cp1 = '\0';
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Kendi kendini çağıran fonksiyonlar

```

Program, iki karakter dizisini birbirine ekleyen bir fonksiyonun çalışmasını göstermektedir. Program, önce cdizi adlı char bir diziye ilk karakter dizisini atar. cdizi dizisi ile ikinci karakter dizisini argüman olarak kullanarak fonk() fonksiyonunu çağırır. fonk() fonksiyonu 1 sayısı ile gösterilen işlem satırında cp1 işaretçisinin cdizi karakter dizisinde yer alan karakter dizisinin son elemanının adresini göstermesini sağlar. Sonra, cp2 işaretçisi ile gösterilen karakter dizisinde yer alan 'x' karakteri dışındaki karakterleri cdizi dizisinin sonuna ekler. Bu işlemi, fonksiyonun kendini her çağırmasında bir karakter eklemek üzere, yapar.

Örnek

```c
#include <stdio.h>

void bg_strcpy(char *cp1, char *cp2);
int bg_strcmp(char *cp1, char *cp2);

int main(void)
{
  int id;
  char cdizi1[20], cdizi2[20];

  bg_strcpy(cdizi1, "Bilgisayar");
  bg_strcpy(cdizi2, "Bilgisayar");

  id = bg_strcmp(cdizi1, cdizi2);

  if (id==0) printf("İki dizi birbirine eşittir!");
  else if(id<0) printf("İlk dizi ikincisinden küçüktür!");
  else printf("İlk dizi ikincisinden büyüktür!");

  return 0;
}

void bg_strcpy(char *cp1, char *cp2)
{
  while (*cp2) *cp1++ = *cp2++;
  *cp1 = '\0';
}

int bg_strcmp(char *cp1, char *cp2)
{
  if (*cp1 < *cp2) return -1;
  else if (*cp1 > *cp2) return 1;
  else if (*cp1 == '\0') return 0;

  return bg_strcmp(cp1+1, cp2+1);
}
	  

```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

İki dizi birbirine eşittir!

```

Program, bg\_strcpy() fonksiyonu ile, 20 byte uzunluğundaki iki diziye aynı karakter dizisini atar. Kendi kendini çağırma yöntemiyle yazılmış olan bg\_strcmp() fonksiyonu ile karşılaştırarak sonucu ekrana yazar.

Örnek

```c
#include <stdio.h>

void deger_yaz(char *cp);
void deger_yaz_ters(char *cp);

int main(void)
{
  deger_yaz("Fonksiyonlar");

  printf("\n");

  deger_yaz_ters("Fonksiyonlar");

  return 0;
}

void deger_yaz(char *cp)
{
  if (*cp) {
      printf("%c", *cp);
      deger_yaz(cp+1);
  }
}

void deger_yaz_ters(char *cp)
{
  if (*cp) {
      deger_yaz_ters(cp+1);
      printf("%c", *cp);
  }
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Fonksiyonlar
ralnoyisknoF

```

Program, bir karakter dizisini argüman olarak kullanarak deger\_yaz() ve deger\_yaz\_ters() fonksiyonlarını çağırır. deger\_yaz() fonksiyonu içinde, ilk karakteri ekrana yazdıktan sonra kendi kendini çağırarak dizi elemanlarını tamamını ekrana yazar. Sonra, işaretçi değerini bir artırır. deger\_yaz\_ters() fonksiyonu ise karakter dizisini tersten ekrana yazar. Bunun nedeni, deger\_yaz() fonksiyonu içinde yer alan işlem satırlarının yer değiştirmiş olmasıdır.

## Fonksiyon parametrelerine argüman geçirme

Bir fonksiyona argüman geçirmenin 2 farklı yöntemi vardır:

```

1. Değer yoluyla
2. Referans yoluyla

```

## Değer yoluyla argüman geçirme

Değer yoluyla argüman geçirme yöntemi kullanıldığında, argüman olarak kullanılan değişkenler çağrılan fonksiyonun parametrelerine geçirilir. Bu durumda, çağrılan fonksiyon içindeki işlem satırları tarafından değerleri değiştirilen parametre değişkenleri, fonksiyon çağırırken argüman olarak kullanılan değişken değerlerini etkilemez.

Bu özelliği bir örnek üzerinde incelemeye çalışalım:

Örnek

```c
#include <stdio.h>

void fonk(int id);

int main(void)
{
  int id = 21;

  fonk(id);

  printf("main() fonksiyonu içinde id değişken değeri: %d", id);

  return 0;
}

void fonk(int id)
{
  id = id + 35;

  printf("Fonksiyon içinde id değişken değeri: %d\n", id);
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Fonksiyon içinde id değişken değeri: 56
main() fonksiyonu içinde id değişken değeri: 21

```

Program, int bir değişken parametresi olan fonk() adlı bir fonksiyon bildirimi yapar. 21 değerini atadığı id değişkenini argüman olarak kullanıp, fonk() fonksiyonunu çağırır. fonk() fonksiyonu kendisine parametre olarak geçirilen id değişkenine, 35 sayısını ekleyerek, elde ettiği değeri ekrana yazar. Fonksiyondan çıktıktan sonra, program id değişken değerini ekrana yazar. Bu değer, fonksiyon çağrıldığında id değişkeninin sahip olduğu değer ile aynı olduğundan, fonksiyon içinde id değişkenine yapılan değişiklik, id değişkeninin program içindeki değerini etkilememiş olur.

## Referans yoluyla argüman geçirme

Referans yoluyla argüman geçirme metodunu kullanıldığında, argüman olarak kullanılan değerlerin bellek adresleri çağrılan fonksiyonun parametrelerine geçirilir. Bu durumda, çağrılan fonksiyon içinde değeri değiştirilen parametreler, fonksiyonu çağırırken argüman olarak kullanılan değişken değerlerini değiştirir. Çünkü, fonksiyon parametrelerine geçirilen değerler argümanların bellek adresleridir.

Bu özelliği bir önceki örneği değiştirerek incelemeye çalışalım:

Örnek

```c
#include <stdio.h>

void fonk(int *ip);

int main(void)
{
  int id = 21;

  fonk(&id);

  printf("main() fonksiyonu içinde id değişken değeri: %d", id);

  return 0;
}

void fonk(int *ip)
{
  *ip = (*ip) + 35;

  printf("Fonksiyon içinde id değişken değeri: %d\n", *ip);
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Fonksiyon içinde id değişken değeri:56
main() fonksiyonu içinde id değişken değeri:56

```

Programda, fonk() fonksiyonuna argüman olarak geçirilen id değişken değerinin değişmesinin tek nedeni, değişken adresinin fonksiyona geçirilmiş olmasıdır. Bu durumda, fonk() fonksiyonu içinde değeri değiştirilen id değişken değeri, fonksiyondan çıkıldıktan sonra da, program içinde aynı değeri korumaktadır.

Kısaca ifade etmek gerekirse, bir fonksiyona argüman olarak geçirilen değerlere, fonksiyon içinde yapılan değişikliklerin, fonksiyonun çalışması sona erdikten sonra, program içinde de geçerli olması istendiğinde Referans Yoluyla Argüman Geçirme yöntemi, aksi takdirde Değer Yoluyla Argüman Geçirme yöntemi kullanılmalıdır.

## Tek boyutlu dizileri fonksiyonlara argüman geçirme

Eğer bir fonksiyonu çağırırken argüman olarak bir dizi kullanırsak, program sadece dizinin ilk elemanının bellek adresini (dizi başlangıç adresi) fonksiyon parametrelerine geçirir. Bir dizinin başlangıç adresini bir fonksiyona geçirmek için, fonksiyon parametresini bu işlemi yapacak şekilde tanımlamak gerekir. Aşağıdaki her üç işlem satırı da bir dizinin ilk elemanının bellek adresini geçirebileceğimiz parametreye sahip bir fonksiyon bildirimi yapar:

```


void fonk (int idizi[10]);
void fonk (int idizi[]);
void fonk (int *ip);


```

Yukarıdaki ilk işlem satırı, fonksiyonun çağrılmasında argüman olarak kullanılan dizi ile aynı veri türüne sahip ve aynı boyutta bir fonksiyon parametre tanımlaması yapar. İkinci işlem satırı, parametreyi boyutsuz bir dizi olarak tanımlar. Üçüncü işlem satırı ise, fonksiyonun çağrılmasında argüman olarak kullanılan dizinin veri türü ile aynı veri türüne sahip bir işaretçiyi parametre olarak tanımlar.

Şimdi, aşağıdaki örnek programlar üzerinde sıra ile bu farklı parametre tanımlamalarını incelemeye çalışalım:

Örnek

```c
#include <stdio.h>

void fonk1(int idizi[10]);
void fonk2(int idizi[]);
void fonk3(int *ip);

int main(void)
{
  int idizi[10];
  int id;

  for (id=0; id<10; id++) idizi[id] = id;

  printf("main() fonksiyonu içinde dizi değerleri: ");
  for (id=0; id<10; id++) printf("%d ", idizi[id]);

  printf("\n");

  fonk1(idizi); // fonk1(&idizi[0])
  fonk2(idizi); // fonk2(&idizi[0])
  fonk3(idizi); // fonk3(&idizi[0])

  printf("main() fonksiyonu içinde dizi değerleri: ");
  for (id=0; id<10; id++) printf("%d ", idizi[id]);

  return 0;
}

void fonk1(int idizi[10])
{
  int id;

  printf("fonk1() fonksiyonu içinde dizi değerleri: ");
  for (id=0; id<10; id++) {
       idizi[id] += 5;
       printf("%d ", idizi[id]);
  }
  printf("\n");
}

void fonk2(int idizi[])
{
  int id;

  printf("fonk2() fonksiyonu içinde dizi değerleri: ");
  for (id=0; id<10; id++) {
       idizi[id] += 5;
       printf("%d ", idizi[id]);
  }
  printf("\n");
}

void fonk3(int *ip)
{
  int id;

  printf("fonk3() fonksiyonu içinde dizi değerleri: ");
  for (id=0; id<10; id++) {
       ip[id] += 5;
       printf("%d ", ip[id]);
  }
  printf("\n");
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

main() fonksiyonu içinde dizi değerleri: 0 1 2 3 4 5 6 7 8 9 
fonk1() fonksiyonu içinde dizi değerleri: 5 6 7 8 9 10 11 12 13 14 
fonk2() fonksiyonu içinde dizi değerleri: 10 11 12 13 14 15 16 17 18 19 
fonk3() fonksiyonu içinde dizi değerleri: 15 16 17 18 19 20 21 22 23 24 
main() fonksiyonu içinde dizi değerleri: 15 16 17 18 19 20 21 22 23 24 

```

Program, üç adet fonksiyon bildirimi yapar. Her üç fonksiyon da parametre oalrak geçirilen dizinin elemanlarına 5 sayısı ekler. İlk fonksiyondaki parametreyi 10 boyutlu int bir dizi, ikinci fonksiyondaki parametreyi boyutsuz int bir dizi ve üçüncü fonksiyondaki parametreyi ise int bir işaretçi olarak tanımlar. Oluşturduğu 10 elemanlı idizi adlı int bir diziye 0-9 arasındaki sayıları atar. Dizi değerlerini ekrana yazar. Her fonksiyonu sıra ile çağırır. Her fonksiyon içinde, yapılan değer ekleme işleminden sonra dizi elemanlarını ekrana yazar. Son olarak, main() fonksiyonu içinde dizi elemanlarını tekrar ekrana yazar. Fonksiyonlar içinde yapılan değişiklikler fonksiyon sona erdikten sonra da geçerli olmaktadır.

Şimdi bu özellikleri örnekler üzerinde incelemeye devam edelim:

Örnek

```c
#include <stdio.h>

void fonk(char *cp1, char *cp2);

int main(void)
{
  char cdizi[] = "Fonksiyon ";

  fonk(cdizi, "kullanımı");

  return 0;
}

void fonk(char *cp1, char *cp2)
{
  int id;

  printf("%s", cp1);

  for (id=0; cp2[id]; id++) printf("%c", cp2[id]);
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Fonksiyon kullanımı

```

Program iki adet char işaretçi parametre içeren fonk() adlı bir fonksiyon bildirimi yapar. "Fonksiyon " kelimesini cdizi adlı bir char diziye atar. cdizi dizisini ve "kullanımı" kelimesini argüman olarak fonk() fonksiyonuna geçirerek, fonk() fonksiyonunu çağırır. fonk() fonksiyonu ilk karakter bellek adresleri kendisine argüman olarak geçirilen karakter dizilerinin ilkini direk olarak, ikincisini ise her defasında bir karakter olmak üzere ekrana yazar.

Örnek

```c
#include <stdio.h>

void fonk(int *ip1, int *ip2);

int main(void)
{
  int idizi1[5] = {5, 7, 14, 21, 34};
  int idizi2[5] = {8, 15, 23, 35, 42};
  int id;

  for (id=0; id<5; id++) printf("%d ", idizi1[id]+idizi2[id]);

  printf("\n");
  
  fonk(idizi1, idizi2);

  for (id=0; id<5; id++) printf("%d ", idizi1[id]+idizi2[id]);

  return 0;
}

void fonk(int *ip1, int *ip2)
{
  int id;

  for (id=0; id<5; id++) {
       ip1[id] *= 2;
       ip2[id] *= 3;
  }
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

13 22 37 56 76
34 59 97 147 194

```

Program, iki adet int dizi içinde yer alan eleman değerlerini toplayarak ekrana yazar. fonk() fonksiyonu yoluyla ilk dizi eleman değerlerini 2 ve ikinci dizi eleman değerlerini ise 3 kat artırarak aynı işlemi tekrar yapar.

Bir fonksiyona argüman olarak bir işaretçi geçirdiğinizde, fonksiyon kendisine argüman olarak geçirilen işaretçinin adresini gösterdiği değişken değerini değiştirebilir. Ancak, bir fonksiyonda işaretçi olarak bildirimi yapılmış bir parametre önüne const tanımlayıcısı getirilirse, fonksiyon çağrıldığında bu parametreye argüman olarak geçirilen değişken değeri kesinlikle fonksiyon tarafından değiştirilemez.

Örnek

```c
// Bu program derleyici tarafından derlenmez.
#include <stdio.h>

void fonk(const int *ip); // Derleyici hata verir.

int main (void)
{
  int idizi[5] = { 1, 2, 3, 4, 5 };
  int id;

  for (id=0; id<5; id++) printf("%d ", idizi[id]);

  printf("\n");

  fonk(idizi);

  for (id=0; id<5; id++) printf("%d ", idizi[id]);

  return 0;
}

void fonk(const int *ip) // Derleyici hata verir.
{
  int id;

  for (id=0; id<5; id++) ip[id] = ip[id] + 1;
}


```

Program, const tanımlamalarından dolayı derleyici tarafından derlenmez ve hata verir.

## Çok boyutlu dizileri fonksiyonlara argüman geçirme

C'de, çok boyutlu diziler de, tıpkı tek boyutlu diziler gibi, bir fonksiyona argüman olarak geçirilebilir. Bu işlemi gerçekleştirirken, fonksiyonda parametre olarak kullanılan dizi boyutlu veya boyutsuz olarak tanımlanabilir.

Şimdi, bu konuyu örnekler üzerinde incelemeye çalışalım:

Örnek

```c
#include <stdio.h>

void fonk1(int idizi[3][5]);
void fonk2(int idizi[][5]);

int main(void)
{
  int idizi[3][5];
  int id1, id2;

  for (id1=0; id1<3; id1++) {
       for (id2=0; id2<5; id2++) {
            idizi[id1][id2] = 5;
            printf("%d ", idizi[id1][id2]);
       }
       printf("\n");
  }

  printf("\n");
  fonk1 (idizi);
  printf("\n");
  fonk2 (idizi);

  return 0;
}

void fonk1(int idizi[5][5])
{
  int id1, id2;

  for (id1=0; id1<3; id1++) {
       for (id2=0; id2<5; id2++) {
            idizi[id1][id2] += 1;
            printf("%d ", idizi[id1][id2]);
       }
       printf("\n");
  }
}

void fonk2(int idizi[][5])
{
  int id1, id2;

  for (id1=0; id1<3; id1++) {
       for (id2=0; id2<5; id2++) {
            idizi[id1][id2] += 2;
            printf("%d ", idizi[id1][id2]);
       }
       printf("\n");
  }
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

5 5 5 5 5
5 5 5 5 5
5 5 5 5 5

6 6 6 6 6
6 6 6 6 6
6 6 6 6 6

8 8 8 8 8
8 8 8 8 8
8 8 8 8 8

```

Program, 2 boyutlu (5\*5) int bir dizi oluşturur. Dizi elemanlarına 5 değerini atar ve eleman değerlerini ekrana yazar. Diziyi argüman olarak geçirdiği fonk1() fonksiyonu içinde eleman değerlerini 1 artırarak, fonk2() fonksiyonu içinde ise 2 artırarak ekrana yazar. fonk2() fonksiyonu parametresi olan dizi için ilk boyut tanımının yapılmadığına dikkat ediniz.

## main() fonksiyonuna argüman geçirme

C'de, kullanıcı tarafından komut satırından programlara argümanlar yoluyla değer geçirme olanağı vardır. Bu işlemin nasıl gerçekleştiğini incelemeye başlamadan önce komut satırı argümanları hakkında kısaca bilgi vermeye çalışalım. Komut satırı argümanı, komut satırında derlenmiş .exe uzantılı program adından sonra bir boşluk bırakarak yazılır ve programlara dışarıdan bilgi geçirmeye yarar. Birden fazla komut satırı argümanı tanımlanabilir, ancak argümanlar arasında en az bir karakter boşluğu bırakmak gerekir.

Bir program yazıldıktan sonra, bu programda dışarıdan verilen değerlerin kullanılması gerektiğinde, işletim sistemi ortamında iken, yazılan program adından sonra komut satırı argümanları tanımlamak yeterlidir. Daha basit bir şekilde ifade etmek gerekirse, bir program içinde bir fonksiyona argümanlar yoluyla değer geçirirken, programın kendisine işletim sistemi ortamından komut satırı argümanları yoluyla değer geçirilir. Bu uygulamanın şekli aşağıdaki satırda gösterilmektedir:

prog-adı arg-1 arg-2

Yukarıdaki satır, işletim sistemi ortamında yani komut satırında iken, yazıldığında, prog-adı ifadesi ile temsil edilen programa arg-1 ve arg-2 ifadeleri ile gösterilen iki farklı argüman geçirilmiş olur.

```

deneme 21 417

```

Yukarıdaki satır komut satırında iken yazıldığında, deneme.exe programı çalıştırılarak 21 ve 417 sayıları bu programa komut satırından argüman olarak geçirilir. deneme.exe programı, kendisine argüman olarak geçirilen bu değerleri program içinde herhangi bir şekilde kullanır.

## main() fonksiyon parametreleri

Daha önce incelediğimiz gibi, bir programda yer alan bir fonksiyona argümanlar yoluyla geçirilen değerleri, fonksiyonun mevcut parametrelerine aktardık. C'de yazılmış bir programa işletim sistemi ortamından, komut satırı argümanları yoluyla geçirilen değerler ise main() fonksiyonuna ait argc ve argv adlı parametrelere aktarılır. Komut satırı argümanları kullanıldığında, programımızdaki main() fonksiyon başlangıç satırı aşağıdaki şekilde olacaktır:

```c
void main(int argc, char *argv[])
```

Yukarıdaki satırda yer alan argc parametresi int bir değerdir. Komut satırında kullanılan argüman sayısını gösterir. Program adı da bir argüman olarak kabul edildiğinden, komut satırında program adından başka bir argüman kullanmasak bile, argc parametresinin değeri en az 1 olacaktır.

Yukarıdaki satırda yer alan argv parametresi ise bir karakter dizisi işaretçi dizisidir ve boyutsuz olarak tanımlanmıştır. Bu nedenle, komut satırı argümanları, komut satırından programa bir karakter dizisi olarak geçirilir. Programa geçirdiğiniz argümanlardan birine ulaşmak için argv parametresindeki sıra numarasını kullanmamız gerekir. argv parametresinin ilk değeri olan argv[0] ifadesi program adını, bundan sonraki ifadeler sıra ile argüman değerlerini içerir.

Örnek

```c
#include <stdio.h>

int main(int argc, char *argv[])
{
  int id;

  for (id=0; id<argc; id++) printf("%s ", argv[id]);

  printf("\n");

  for (id=1; id<argc; id++) printf("%s ", argv[id]);

  return 0;
}


```

Yukarıdaki örnekte, program önce komut satırında program adı da dahil olmak üzere tüm argümanları, sonra program adından sonra yazılan argümanları ekrana yazar.

Daha önce komut satırında kullanılan argümanlar arasında en az bir karakter boşluğu bırakmak gerektiğini belirtmiştik. Eğer, bir cümle tek başına bir komut satırı argümanı olarak tanımlanmak istenirse, cümleyi " " işaretleri arasına almak gerekir.

C'de, main() fonksiyonu ile birlikte kullanılan parametrelere argc ve argv adları verilmiştir. Bu adları, istediğimiz şekilde değiştirebiliriz.

## atoi(), atof() ve atol() fonksiyonları

İşletim sistemi komut satırından programa geçirilen argümanlar bir karakter dizisi olarak geçirildiğinden, programa int bir değer bile geçirilse, program bu sayıları karakter dizisi olarak kabul eder. Programa karakter dizisi olarak geçirilen sayıları, program içinde sayısal bir değer olarak kullanabilmek için, bu karakter dizilerini sayısal bir değere çevirmemiz gerekir. Bu işlemi gerçekleştirebilmek için aşağıda gösterilen standart kütüphane fonksiyonlarını kullanabiliriz:

```c
int atoi(char *cdizi);    // cdizi değerini int bir değere çevirir.
double atof(char *cdizi); // cdizi değerini double bir değere çevirir.
long atol(char *cdizi);   // cdizi değerini long int bir değere çevirir.
```

Yukarıda yer alan fonksiyonların tamamı stdlib.h başlık dosyasını kullanmaktadır. Bu fonksiyonları geçersiz bir sayı olan bir karakter dizisi ile çağırırsak, fonksiyonlar 0 değerini geri döndürürler.

Örnek

```c
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
  int id;
  long int lid;

  if (argc>1) {
      id = atoi(argv[1]);
      lid = atol(argv[2]);

      printf("Karakter dizisi: %s %s\n", argv[1], argv[2]);	  
      printf("Sayı değerleri: %d %ld", id, lid);
  }

  return 0;
}


```

Program, komut satırında program adından sonra argüman girilirse, sıra ile girdiğiniz karakter dizisi yapısındaki, int ve long int değerleri hem karakter dizisi hem de gerçek sayı şeklinde ekrana yazar.

Örnek

```c
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
  int id;

  if (argc>1) {
      for (id=0; id<atoi(argv[1]); id++) printf("Komut satırı argümanları\n");
  }

  return 0;
}


```

Program, komut satırında program adından sonra yazılan int değer kadar karakter dizisini ekrana yazar. Yukarıdaki örneği deneme.exe adı ile derler ve komut satırında iken aşağıdaki komutu yazarsak, program karakter dizisini üç kez ekrana yazar:

deneme 3

Örnek

```c
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
  int id;

  if (argc>1) {
      for (id=0; id<atoi(argv[1]); id++) printf("%s ", argv[2]);
  }

  return 0;
}


```

Program, komut satırında program adından sonra ikinci argüman olarak girilen karakter dizisini ilk argüman olan int değer kadar sayıda ekrana yazar. Yukarıdaki örneği deneme.exe adı ile derler ve komut satırında iken aşağıdaki komutu yazarsak, program "Komut" kelimesini 5 kez ekrana yazar:

deneme 5 Komut

Yukarıdaki örnekler, komut satırında program adı dışında bir argüman kullanmadan çalıştırıldığında, herhangi bir işlem yapmaz. C, bu tür programlar komut satırı argümanı kullanılmadan veya istenen sayıda komut satırı argümanı tanımlanmadan çalıştırıldığında, size bir tür kontrol sistemi oluşturma olanağı sağlar. Bu özelliği bir örnek üzerinde incelemeye çalışalım:

Örnek

```c
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
  int id;

  if (argc!=3) {
      printf("Kullanım: deneme <Sayı> <Karakter dizisi>");
      exit(1);
  }

  for (id=0; id<atoi(argv[1]); id++) printf("%s ", argv[2]);

  return 0;
}


```

Yukarıdaki örnekte, programı çalıştırabilmek için mutlaka 2 komut satırı argümanı tanımlamak gerekir. Aksi takdirde program sadece aşağıda
yer alan satırı ekrana yazar:

```

Kullanım: deneme <Sayı> <Karakter dizisi>

```

Yukarıdaki satır, uygun sayıda argüman kullanılmadığında, kullanıcıya argüman sayısını hatırlatmak yoluyla programın komut satırından çalıştırma şeklini gösterir. Komut satırı argümanları uygun şekilde ve sayıda kullanıldığında program normal olarak çalışır.

Şimdi, öğrendiklerimizi örneklerle pekiştirmeye çalışalım:

Örnek

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
  if (argc!=3) {
      printf("Kullanım: deneme <Karakter dizisi> <Karakter dizisi>");
      exit(1);
  }

  printf("İlk karakter dizisinin uzunluğu: %d\n", strlen(argv[1]));
  printf("İkinci karakter dizisinin uzunluğu: %d", strlen(argv[2]));

  return 0;
}


```

Program, komut satırından girilen iki karakter dizisinin uzunluğunu ekrana yazar.

Örnek

```c
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
  char *cp1, *cp2;

  if (argc != 3) {
      printf("Kullanım: deneme <Karakter dizisi> <Karakter dizisi>");
      exit(1);
  }
  cp1 = argv[1];
  cp2 = argv[2];

  while (*cp1 && *cp2) {
     printf("%c%c", *cp1++, *cp2++);
  }

  return 0;
}



```

Pprogram, komut satırından argüman olarak girilen karakter dizilerinin harflerini, baştan itibaren her karakter dizisinden sıra ile bir karakter alarak, ekrana yazar. Karakter dizilerinden herhangi biri sona erdiğinde işlem sona erer.

## Fonksiyon işaretçileri

İşaretçileri fonksiyon adresleri ile birlikte kullanarak fonksiyonları çağırabiliriz.

Derleyici bir programı derlediğinde, programdaki her bir fonksiyon için bir giriş noktası oluşturur. Programı derledikten ve diğer dosyalarla birleştirdikten sonra, bu giriş noktasının ulaşılabilecek fiziksel bir adresi oluşur. İşte, bu adrese fonksiyon işaretçilerini kullanarak ulaşabiliriz.

Fonksiyon işaretçisi, bir fonksiyonun giriş noktasının adresini içeren bir değişkendir. Bir fonksiyonu her çağırmada bu adresi rahatlıkla kullanabiliriz.

Bir fonksiyonu gösteren bir işaretçi oluşturmak için, işaretçinin başına fonksiyonun geri verdiği veri türü, sonuna ise fonksiyonun parametreleri yazılır:

veri-türü (\*işaretçi-adı) (par1, par2, ...);

int bir değer geri veren ve 2 adet int parametre içeren bir fonksiyona bir işaretçi tanımlamak için aşağıdaki ifadeyi kullanabiliriz:

```c
int (*fp) (int id1, int id2);
```

\*fp etrafındaki parantezler, işlemci öncelik kurallarından dolayı kullanılmaktadır.

Bir fonksiyon bildirimi yapılmasını, fonksiyon giriş noktası adresinin bir işaretçiye atanmasını ve fonksiyonun işaretçi yoluyla çağrılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```c
#include <stdio.h>

int fonk(int id1, int id2); // Fonksiyon bildirimi

int main(void)
{
  int (*fp) (int id1, int id2); // Fonksiyon işaretçi bildirimi
  int id3;

  fp = fonk; // Fonksiyon adresinin işaretçiye atanması

  id3 = (*fp) (21, 10); // İşaretçi ile fonksiyon çağrılması

  printf("%d", id3);

  return 0;
}

int fonk(int id1, int id2)
{
  int id3, id4;

  for (id3=0, id4=0; id3<id2; id3++) {
       printf("%d ", id1);
       id4 += id1;
  }
  printf("\n");

  return id4;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

21 21 21 21 21 21 21 21 21 21 
210

```

Şimdi, öğrendiklerimizi örneklerle pekiştirmeye çalışalım:

Örnek

```c
#include <stdio.h>

int fonk1(int *ip);
int fonk2(int *ip);

int (*fpdizi[2]) (int *ip);

int main(void)
{
  int idizi[5];
  int id1;

  for (id1=0; id1<5; id1++) {
       idizi[id1] = id1+1;
       printf("%d ", idizi[id1]);
  }
  fpdizi[0] = fonk1;
  fpdizi[1] = fonk2;

  printf("\n");

  printf("Dizi eleman değerleri toplamı: %d\n", (*fpdizi[0])(idizi));
  printf("Dizi eleman değerleri çarpımı: %d", (*fpdizi[1])(idizi));

  return 0;
}

int fonk1(int *ip)
{
  int id1, id2;

  for (id1=0, id2=0; id1<5; id1++) id2 += *ip++;

  return id2;
}

int fonk2(int *ip)
{
  int id1, id2;

  for (id1=0, id2=1; id1<5; id1++) id2 *= *ip++;

  return id2;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

1 2 3 4 5
Dizi eleman değerleri toplamı: 15
Dizi eleman değerleri çarpımı: 120

```

Program, iki fonksiyon için iki elemanlı işaretçisi dizisi bildirimini yapar. Tanımlanan dizinin her bir elemanı bir fonksiyonun adresini gösteren bir işaretçi içerir. Sonra, program işaretçiler yoluyla her iki fonksiyonu sıra ile çalıştırır. İlk fonksiyon int bir dizi elemanlarının toplamını, ikinci fonksiyon ise çarpımını geri verir.

Örnek

```c
#include <stdio.h>
#include <string.h>

void fonk(char *cdizi);

void (*cp) (char *cdizi);

int main(void)
{
  char cdizi[40];

  cp = fonk;

  strcpy(cdizi, "Fonksiyon işaretçileri");

  printf("%s\n", cdizi);

  (*cp) (cdizi);

  return 0;
}
void fonk(char *cdizi)
{
  int id1, id2;
  char cdizi2[40];

  id2 = strlen(cdizi)-1;

  for (id1=0; id2>=0; id1++, id2--) {
       cdizi2[id1] = cdizi[id2];
  }

  cdizi2[id1] = '\0';

  printf("%s\n", cdizi2);
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Fonksiyon işaretçileri
ireliçteraşi noyisknoF

```

Program, bir karakter dizisini ekrana yazar. Sonra, fonk() fonksiyonu yoluyla, karakter dizisi içinde yer alan karakterleri ters çevirerek tekrar ekrana yazar.

## Fonksiyonlardan dizi değeri döndürme

C programlama dilinde bir fonksiyondan bir dizi değerini doğrudan geri döndürmek için herhangi bir yöntem bulunmamaktadır.

C dilinde doğrudan dizi geri döndüren fonksiyon tanımlaması bulunmamaktadır.

Ancak, aşağıda sırasıyla ele alacağımız 4 farklı yöntemle fonksiyonların dolaylı olarak dizi geri döndürmelerini sağlayabiliriz.

## 1. Geri döndürülecek diziyi fonksiyona argüman olarak geçirme

Bu yöntemde, çağıracağımız fonksiyona bir dizi geçirerek, fonksiyon içinde dizi üzerinde gerekli işlemleri yaptıktan sonra dizi geri döndürülür. İşlemi örnekler üzerinde incelemeye çalışalım:

Örnek

```c
#include <stdio.h>

int *fonk(int ildizi[]);

int main(void)
{
  int id, idizi[10], *ip;

  for (id=0; id<10; id++) idizi[id]=id+1;

  ip = fonk(idizi);

  for (id=0; id<10; id++) printf("%d ", *ip++);

  return 0;
}

int *fonk(int ildizi[])
{
  int id;

  for (id=0; id<10; id++) {
       ildizi[id] = ildizi[id] * 2;
  }

  return ildizi;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

2 4 6 8 10 12 14 16 18 20

```

Program integer veri türünden bir değişken, 10 boyutlu bir dizi ve bir işaretçi oluşturur. 1-10 arasındaki değerleri diziye atar. Bu diziyi argüman olarak atayarak fonk() fonksiyonunu çağırır. Fonksiyon kendisine parametre olarak geçirilen dizi değerlerini 2 ile çarparak diziye kaydeder ve diziyi geri döndürür. Geri döndürülen dizi başlangıç adresi ip işaretçisine atanır ve dizi değerleri ekrana yazılır.

Bu örnekte, fonksiyona parametre olarak geçirilen dizi fonksiyon çağrısından önce tanımlandığından, bu dizinin adresi fonksiyon içindeki ildizi dizine aktarılır. ildizi ile yapılan işlemler idizi dizisine yapıldığından, fonksiyon sona erdiğinde geri döndürülerek ip işaretçisine atanan adres aslında idizi dizisinin adresidir. 

Bu durumda, program fonksiyonun geri döndürmesi için bir dizi oluşturarak bu dizinin fonksiyon tarafından kullanılmasını sağlamış olur.

Fonksiyona parametre olarak geçirilen diziye kendi boyutundan fazla değer yükleyerek hata oluşmasını engellemek için fonksiyona aktardığımız dizinin boyutunu gösteren int bir değeri de ikinci bir parametre olarak fonksiyona aktarabiliriz. Aşağıdaki örnekte, program içinde oluşturulan idizi dizisinin boyutunu fonk() fonksiyonuna parametre olarak geçirerek bu değeri fonksiyon içinde kullanıyoruz.

Örnek

```c
#include <stdio.h>

int *fonk(int ildizi[], int boyut);

int main(void)
{
  int id, idizi[10], *ip;

  for (id=0; id<10; id++) idizi[id]=id+1;

  ip = fonk(idizi, 10);

  for (id=0; id<10; id++) printf("%d ", *ip++);

  return 0;
}

int *fonk(int ildizi[], int boyut)
{
  int id;

  for (id=0; id<boyut; id++) {
       ildizi[id] = ildizi[id] * 2;
  }

  return ildizi;
}


```

Program, bir önceki programın yaptığı işlemin aynısını gerçekleştirir.

## 2. Geri döndürülecek diziyi fonksiyon içinde static olarak tanımlama

Bu yöntemde, fonksiyon tarafından geri döndürülecek dizi fonksiyon içinde static olarak tanımlanır ve gerekli işlemler yapıldıktan sonra, fonksiyon diziyi geri döndürür. Ancak, fonksiyon sona ermesine rağmen, dizi static olarak tanımlandığından program sona erene kadar bellekte kalır. Bu yöntemi bir örnek üzerinde incelemeye çalışalım:

Örnek

```c
#include <stdio.h>

int *fonk(int fark);

int main(void)
{
  int id, *ip;

  ip = fonk(2);

  for (id=0; id<10; id++) printf("%d ", *ip++);

  return 0;
}

int *fonk(int fark)
{
  static int idizista[10];
  int id;

  for (id=0; id<10; id++) {
       idizista[id] = (id+1)*fark;
  }

  return idizista;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

2 4 6 8 10 12 14 16 18 20

```

Program integer veri türünden bir değişken ve bir işaretçi oluşturur. 10 değerini parametre olarak geçirerek fonk() fonksiyonunu çağırır. Fonksiyon static olarak idizista adlı ve 10 elemanlı bir int dizi oluşturur. Parametre değeri olan 10 değeri kadar oluşturulan diziye 1 değerinden başlayarak değer atar. Fonksiyon idizista dizisini geri döndürür. Geri döndürülen dizinin başlangıç adresi ip işaretçisine atanır ve dizi değerleri ekrana yazılır.

Ancak, bu yöntemde fonksiyonu her çağırmamızda, fonksiyon aynı static dizini ve işaretçi değişkenini kullanır. Fonksiyonu ikinci kez çağırdığımızda, bir önceki fonksiyon çağrısında elde ettiğimiz dizi değerlerinin üzerine yazılır. İlk fonksiyon çağrısında geri döndürülen dizinin adresini alan işaretçi değişkeni ile ikinci fonksiyon çağrısında geri döndürülen dizinin adresini alan işaretçi değişkeni aynı bellek adresini gösterecektir. Bu nedenle, bu fonksiyonu bir defadan fazla kullandığımızda, istediğimiz sonucu elde edemeyiz.

Bu durumu aşağıdaki örnek üzerinde incelemeye çalışalım:

Örnek

```c
#include <stdio.h>

int *fonk(int fark);

int main(void)
{
  int id, *ip1, *ip2;

  ip1 = fonk(2);
  ip2 = fonk(3);

  for (id=0; id<10; id++) printf("%d ", *ip1++);

  printf("\n");

  for (id=0; id<10; id++) printf("%d ", *ip2++);

  return 0;
}

int *fonk(int fark)
{
  static int idizista[10];
  int id;

  for (id=0; id<10; id++) {
       idizista[id] = (id+1)*fark;
  }

  return idizista;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

3 6 9 12 15 18 21 24 27 30
3 6 9 12 15 18 21 24 27 30

```

Yukarıdaki ekran çıktısından da görülebileceği gibi, ip1 ve ip2 işaretçi değişkenleri aynı adresi göstermektedir.

## 3. Geri döndürülecek dizi için fonksiyon içinde malloc() fonksiyonu ile dinamik bellek tahsis etme

Bu yöntemde, fonksiyon tarafından geri döndürülecek dizi için fonksiyon içinde malloc() fonksiyonu ile bellekten dinamik olarak yer tahsis edilerek, ayrılan belleğin başlangıç adresi int bir işaretçi değişkene atanır. Eğer bellek ayırma işlemi başarısız olursa, fonksiyon NULL bir değer geri döndürür. Bu işaretçiyi indeksleyerek, ayrılan belleğe integer değerler atanır. Sonra, fonksiyon tahsis edilen belleğin başlangıç adresini geri döndürür. Fonksiyonun geri döndürdüğü adres değerinin atandığı işaretçi bir değişken yoluyla değerler ekrana yazılır. Ayrılan bellek boşaltılır. Bu yöntemi bir örnek üzerinde incelemeye çalışalım:

Örnek

```c
#include <stdio.h>
#include <stdlib.h>

int *fonk(void);

int main(void)
{
  int id, *ip;

  if((ip = fonk())!=NULL){
     for (id=0; id<10; id++) printf("%d ", *ip++);
     free(ip);
  }

  return 0;
}

int *fonk(void)
{
  int *idizi = (int*) malloc(10 * sizeof(int));
  int id;
  if(idizi==NULL) return NULL;

  for (id=0; id<10; id++) {
       idizi[id] = id+1;
  }

  return idizi;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

1 2 3 4 5 6 7 8 9 10

```

## 4. Fonksiyondan dizi geri döndürme işlemini yapılar yoluyla gerçekleştirme

Bu yöntemde, içinde int bir dizi içeren global bir yapı oluşturulur. Fonksiyon içinde bir yapı değişkeni oluşturularak, yapı içindeki dizine değerler atandıktan sonra yapı değişkeni fonksiyon tarafından geri döndürülür. Geri döndürülen değer main() fonksiyonu içinde oluşturulmuş olan bir yapı değişkenine atanarak değişkenin içindeki dizi değerleri ekrana yazılır. Bu yöntemi bir örnek üzerinde incelemeye çalışalım:

Örnek

```c
#include <stdio.h>

struct yapdizi {
  int idizi[10];
};

struct yapdizi fonk(void);

int main(void)
{
  struct yapdizi yp;
  int id;

  yp = fonk();

  for (id=0; id<10; id++) printf("%d ", yp.idizi[id]);
}

struct yapdizi fonk(void)
{
  struct yapdizi ypfonk;
  int id;

  for (id=0; id<10; id++) {
       ypfonk.idizi[id] = id+1;
  }

  return ypfonk;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

1 2 3 4 5 6 7 8 9 10

```
