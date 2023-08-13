---
title:  C++ Dinamik bellek kullanımı
author: sonsuz
date: 2023-08-13 18:33:14 +0300
categories: [Program,C++]
tags: [cpp,programlama,dinamik bellek,bellek,nesne,new,delete,malloc]
---


C++'da daha kaliteli uygulamalar geliştirmek için dinamik bellek kullanımını etkin bir şekilde kullanmamız gerekmektedir. Program normal koşullarda ihtiyaç duyulan bellek tahsisini ve bellek boşaltma işlemlerini işlem satırlarında yer alan kodlara uygun olarak yapar. Ancak, bazı durumlarda, değişkenlere atanacak verilerin boyutu ve ihtiyaç duyulan bellek miktarı programın çalışması esnasında belirlenebileceğinden, bellek tahsis ve boşaltma işlemlerini program çalışması esnasında dinamik olarak gerçekleştirmek gerekir.

Dizi tanımlaması gibi yapılan bazı işlemler belleğin otomatik olarak tahsis edilmesini sağlarken, bazı işlemler bu olanağı sağlamaz. Bu durumda, programın çalışması esnasında gereksinim duyduğumuzda bellek tahsis edebiliriz. Bu işleme dinamik bellek kullanımı yöntemi adı verilir.

## C++ dinamik bellek kullanımı

Program çalışırken dinamik olarak bellek tahsisi heap adı verilen bellek bölgesinden yapılır.

## new ve delete işlemcileri

C++'da dinamik bellek işlemleri için new ve delete işlemcileri kullanılır.

new işlemcisi bellek tahsisi yapar ve tahsis edilen belleğin başlangıç adresini geri döndürür. new işlemcisinin genel kullanım şekli aşağıdadır:

veri-türü işaretçi-adı = new veri-türü;

delete işlemcisi daha önce new işlemcisi ile tahsis edilen belleği boşaltır. delete işlemcisinin genel kullanım şekli aşağıdadır:

delete işaretçi-adı;

new işlemcisi, new işlemcisinin sağ tarafındaki veri türü büyüklüğünde bellek tahsis ederek, tahsis edilen belleğin başlangıç adresini geri döndürerek aynı veri türünden bir işaretçiye atar.

Bellek tahsis işleminde meydana gelebilecek sorunlar, genellikle heap bellek alanındaki yetersizlikten ötürü, program tarafından kontrol edilmelidir.

Şimdi, new ve delete işlemcilerinin kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>
#include <stdlib.h> // exit() fonksiyonu için

using namespace std;

int main(void)
{
  int *ip;

  ip = new int; // int değer büyüklüğünde bellek tahsis eder.

  if (!ip) {
      cout << "Bellek tahsis hatası!";   
      exit(1); // Programı sona erdirir.
  }
  
  *ip = 21; // İşaretçi yoluyla belleğe değer atar.

  cout << ip << " bellek adresindeki değer: " << *ip;
  
  delete ip;
  
  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

0x181a30 bellek adresindeki değer: 21

```

Program, int veri türünden ip adlı bir işaretçi değişken oluşturur. Sonra, new işlemcisini kullanarak, int veri türü büyüklüğünde bellek tahsis eder ve tahsis ettiği belleğin başlangıç adresini ip işaretçisine atar. Eğer bellek tahsisinde bir sorun yaşanırsa, ekran bir hata mesajı yazar ve programı sona erdirir. ip işaretçisinin gösterdiği bellek adresine ise 21 sayısını atar. Daha sonra ip işaretçisinin taşıdığı bellek adresi değeri ile bu adreste yer alan int değeri ekrana yazar. Program sonra ermeden, delete işlemcisi ile tahsis edilen belleği boşaltır.

## Tahsis edilen bellek bölgesine ilk değer atama

Dinamik bellek tahsisi yaparken aşağıdaki gösterildiği şekilde ilk değer atama işlemi gerçekleştirebiliriz:

veri-türü işaretçi-adı = new veri-türü ilk-değer;

Şimdi, bellek tahsisi yaparken ilk değer atama işlemini bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>
#include <stdlib.h> // exit() fonksiyonu için

using namespace std;

int main(void)
{
  int *ip;

  ip = new int(75); // int değer büyüklüğünde bellek tahsis ederek bellek adresine 75 değerini atar.

  if (!ip) {
      cout << "Bellek tahsis hatası!";   
      exit(1); // Programı sona erdirir.
  }
  
  cout << ip << " bellek adresindeki değer: " << *ip;
  
  delete ip;
  
  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

0x1b1a60 bellek adresindeki değer: 75

```

Program, int veri türünden ip adlı bir işaretçi değişken oluşturur. Sonra, new işlemcisini kullanarak, int veri türü büyüklüğünde bellek tahsis eder ve tahsis ettiği belleğin başlangıç adresini ip işaretçisine atar. Bellek tahsisi yaparken 75 değerini bellek adresine atar. Daha sonra ip işaretçisinin taşıdığı bellek adresi değeri ile bu adreste yer alan int değeri ekrana yazar. Program sonra ermeden, delete işlemcisi ile tahsis edilen belleği boşaltır.

## Dizilere dinamik bellek tahsisi

Tıpkı değişkenlere yapıldığı gibi, dizilere de dinamik bellek tahsisi yapabiliriz. Dizilere bellek atama işleminde new ve delete işlemcilerinin kullanma şekli aşağıda gösterilmektedir:

veri-türü işaretçi-adı = new dizi-veri-türü [dizi-boyutu];

delete [ ] işaretçi-adı;

Şimdi, dizilere bellek tahsisini bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>
#include <stdlib.h> // exit() fonksiyonu için

using namespace std;

int main(void)
{
  int *ip, id;

  ip = new int[5]; // 5 boyutlu int dizi büyüklüğünde bellek tahsis eder.

  if (!ip) {
      cout << "Bellek tahsis hatası!";   
      exit(1); // Programı sona erdirir.
  }
  
  for (id=0; id<5; id++) ip[id] = (id+1) * (id+1);
  
  for (id=0; id<5; id++) {
	   cout << &ip[id] << " bellek adresindeki değer: " << ip[id] << endl;
  }
  
  delete [] ip;
  
  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

0xe11690 bellek adresindeki değer: 1
0xe11694 bellek adresindeki değer: 4
0xe11698 bellek adresindeki değer: 9
0xe1169c bellek adresindeki değer: 16
0xe116a0 bellek adresindeki değer: 25

```

Program, int veri türünden ip adlı bir işaretçi ve bir değişken oluşturur. Sonra, new işlemcisini kullanarak, 5 boyutlu int dizi büyüklüğünde bellek tahsis eder ve tahsis ettiği belleğin başlangıç adresini ip işaretçisine atar. Daha sonra tahsis edilen belleğe 1-5 arasındaki sayıların karelerini sırasıyla atar. Bellekte yer alan değerleri adresleriyle birlikte ekrana yazar. Program sonra ermeden, delete işlemcisi ile tahsis edilen belleği boşaltır.

## Nesnelere dinamik bellek tahsisi

C++'da sınıflardan oluşturduğumuz nesneler için de new işlemcisini kullanarak dinamik bellek tahsisi yapabiliriz. Bu işlemi yaptığımızda, sınıf büyüklüğünde bellek tahsisi yapılarak, tahsis edilen belleğin başlangıç adresi sınıf cinsinden tanımlanmış işaretçiye atanır.

Şimdi, nesnelere bellek tahsisini bir örnek üzerinde incelemeye çalışalım:

```c++
#include <iostream>
#include <stdlib.h> // exit() fonksiyonu için

using namespace std;

class sinif {
  int id; 

  public:
    sinif(int pid);
    ~sinif();  
    void deger_yaz () { cout << id << endl; }
};

sinif::sinif(int pid)
{
  id = pid;
  cout << "Nesne oluşturuluyor: " << id << endl; 
}

sinif::~sinif()
{
  cout << "Nesne yok ediliyor: " << id << endl; 
}

int main(void)
{
  sinif *pnes;

  pnes = new sinif(21); // sinif büyüklüğünde bellek tahsis ederken 21 değerini ilk değer olarak atar.

  if (!pnes) {
      cout << "Bellek tahsis hatası!";   
      exit(1); // Programı sona erdirir.
  }	
	
  pnes->deger_yaz();
  
  delete pnes;
  
  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Nesne oluşturuluyor: 21
21
Nesne yok ediliyor: 21

```

Program, new işlemcisini kullanarak sinif büyüklüğünde bellek tahsisi yapar ve sinif cinsinden bir nesne oluşturarak, tahsis edilen belleğin başlangıç adresi sınıf cinsinden tanımlanmış işaretçiye atar. Bir nesne oluşturulduğundan, constructor fonksiyonu çalışır. İşaretçi ile nesneye erişim sağlayarak id değişken değerini ekrana yazar. Sonra, delete işlemcisi ile tahsis edilen belleği boşaltır. Nesne yok edildiğinden, destructor fonksiyonu çalışır.

## C temelli dinamik bellek kullanımı

Tüm derleyiciler tarafından sağlanan dört adet dinamik bellek tahsis fonksiyonu vardır:

* malloc()
* calloc()
* realloc()
* free()

## malloc() fonksiyonu

Dinamik bellek kullanımı için genellikle malloc() ve free() fonksiyonları birlikte kullanılır. malloc() fonksiyonu belleği tahsis ederken, free() fonksiyonu ise önceden tahsis edilmiş belleği boşa çıkarır. Bu fonksiyonların genel yapısı aşağıda gösterilmektedir:

```c++
void *malloc (size_t byte-sayısı);
void free (void *p);


```

malloc() fonksiyonunda kullanılan byte-sayısı ifadesi tahsis etmek istediğiniz belleğin byte olarak değerini gösterir. malloc() fonksiyonu
tahsis edilmiş belleğin başlangıcını gösteren bir işaretçi geri verir. Tahsis edilmek istenen bellek ihtiyacını karşılayamadığında, NULL bir işaretçi geri verir.

Tahsis edilen belleği boşa çıkarmak için, free() fonksiyonu, daha önce malloc() fonksiyonu ile tahsis edilen belleğin başlangıcını gösteren, bir işaretçi ile kullanılır.

malloc() ve free() fonksiyonları cstdlib başlık dosyasını kullanır.

malloc() fonksiyonunun en önemli özelliği bir işaretçiye bir değer atamadan önce bir değişken adresi atama gereksinimini ortadan kaldırmış olmasıdır. Bunun nedeni, malloc() fonksiyonunun tahsis ettiği belleğin başlangıç adresini otomatik olarak işaretçiye geri vermesidir.

Bir program sona erdiği zaman tahsis edilmiş belleğin tamamı otomatik olarak boşa çıkar.

Şimdi, malloc() ve free() fonksiyonlarının kullanılmasını örneklerle incelemeye çalışalım:

Örnek

```c++
#include <iostream>
#include <cstdlib>

using namespace std;

int main(void)
{
  int *ip;

  // int veri türü boyutu kadar kadar bellek tahsisi
  ip = (int*) malloc(sizeof(int));
  *ip = 126;

  cout << "Tahsis edilen bellek adres başlangıcı: " << ip << "\n";
  cout << "Tahsis edilen bellekteki değişken değeri: " << *ip;

  free(ip);

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Tahsis edilen bellek adres başlangıcı: 0xec1ab0
Tahsis edilen bellekteki değişken değeri: 126

```

Program, malloc() fonksiyonunun geri verdiği değeri direkt olarak ip işaretçisine atar. Böylece, int bir değer için ayrılmış olan bellek alanının başlangıç adresi ip işaretçisine atanmış olur. ip işaretçisinin gösterdiği adrese ise 126 sayısını atar. Daha sonra ip işaretçi değeri ile işaretçinin gösterdiği adreste yer alan değeri ekrana yazar. free() fonksiyonu ise tahsis edilen belleği boşaltır.

Bir işaretçiyi kullanmadan önce mutlaka bir adres atanması gerektiğinden, ip işaretçisine bellek adresini malloc() fonksiyonu atamaktadır.

Örnek

```c++
#include <iostream>
#include <cstdlib>
#include <cstring>

using namespace std;

int main(void)
{
  char *cp;

  cp = (char*) malloc(40);

  if (!cp) {
      cout << "Bellek tahsis hatası!";
      exit(1);
  }

  strcpy(cp, "Bilgisayar");
  cout << cp;

  free(cp);

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Bilgisayar

```

Program, 40 byte'lık bir bellek tahsisi yapar ve bu belleğin başlangıç adresini bir char işaretçiye atar. cp işaretçisine bi rkarakter dizisi kopyalar ve diziyi ekrana yazar. Sonra, free() fonksiyonunu kullanarak tahsis edilen belleği boşaltır.

Örnek

```c++
#include <iostream>
#include <cstdlib>
#include <cstring>

using namespace std;

int main(void)
{
  char *cp1 = "İlk karakter dizisi";
  char *cp2, *cp3;
  char cdizi[30];

  cp2 = "İkinci karakter dizisi";

  cp3 = (char*) malloc(50);
  strcpy(cp3, "Üçüncü karakter dizisi"); // malloc() ve free() fonksiyonları kullanılmadığında hata verir.
  strcpy (cdizi, "Dördüncü karakter dizisi");

  cout << cp1 << "\n" << cp2 << "\n" << cp3 << "\n" << cdizi;

  free(cp3);

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

İlk karakter dizisi
İkinci karakter dizisi
Üçüncü karakter dizisi
Dördüncü karakter dizisi

```

## calloc() fonksiyonu

Bellek tahsislerinde calloc() fonksiyonu da kullanılabilir. Bu fonksiyonun malloc() fonksiyonundan tek farkı ayrılacak bellek miktarının
eleman boyutu ve eleman sayısı olarak iki argüman halinde tanımlanmış olmasıdır. calloc() fonksiyonunun genel yapısı aşağıda gösterilmektedir:

```


void *calloc (size_t elem-say, size_t elem_boy);


```

Yukarıdaki satırda, elem\_say ifadesi eleman sayısını, elem\_boy ifadesi ise, eleman boyutunu ifade eder. Aşağıda yer alan her iki işlem satırı aynı işlemi gerçekleştirir:

```


ip = malloc (10 * sizeof(int));
ip = calloc (10, sizeof (int));


```

Şimdi, calloc() fonksiyonunun kullanılmasını bir örnek ile incelemeye çalışalım:

Örnek

```c++
#include <iostream>
#include <cstdlib>

using namespace std;

int main(void)
{
  int *ip, id;

  ip = (int *) calloc(5, sizeof(int));

  for (id=0; id<5; id++) {
       *(ip+id) = (id+1) * 10;
       cout << (ip+id) << " adresindeki değer: " << *(ip+id) << "\n";
  }

  free(ip);

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

0x180538 adresindeki değer: 10
0x18053c adresindeki değer: 20
0x180540 adresindeki değer: 30
0x180544 adresindeki değer: 40
0x180548 adresindeki değer: 50

```

Program, calloc() fonksiyonunu kullanarak 5 adet int değer için bellek tahsisi yapar. Her bellek adresine int bir değer atar. Daha sonra, bellek adreslerini ve bu adreslere atadığı değerleri ekrana yazar.

## realloc() fonksiyonu

realloc() fonksiyonu, daha önce malloc(), calloc() veya realloc() fonksiyonu ile tahsis edilen belleğin boyutunu, boyutu byte olarak ifade edilen size parametre değeri kadar, değiştirir.

```c++
void* realloc(void *ptr, size_t size);


```

Yeniden bellek tahsis işlemi ptr parametresi ile gösterilen bellek adresi büyütülerek veya küçültülerek yapılabilir. Bellek alanı genişletilirse, tahsis edilen önceki bellek içeriği değişmeden kalır ve eklenen bellek içeriğine herhangi bir değer atanmaz.

Yeterli bellek yoksa, eski bellek bloğu serbest bırakılmaz ve NULL bir işaretçi geri döndürülür.

ptr parametresi yeniden tahsis edilecek bellek bölgesini ve size parametresi tahsis edilecek belleğin yeni boyutunu byte olarak gösterir.

Başarı durumunda tahsis edilen belleğin başlangıç adresini geri döndürür. Bellek sorunlarını engellemek için, gerekli işlemler yapıldıktan sonra, bu işaretçi free() veya realloc() fonksiyonu ile boşaltılmalıdır. Hata durumunda, NULL bir işaretçi geri döndürülür. Bu durumda, geçerliliğini devam ettiren önceki işaretçi free() veya realloc() fonksiyonu ile boşaltılmalıdır.

Örnek

```c++
#include <iostream>
#include <cstdlib>

using namespace std;

int main(void)
{
  int *ip, id;

  ip = (int *) malloc(5 * sizeof(int));

  for (id=0; id<5; id++) {
       *(ip+id) = id+1;
       cout << (ip+id) << " adresindeki değer: " << *(ip+id) << "\n";
  }

  ip = (int *) realloc(ip, 10 * sizeof(int));

  cout << "Genişletilmiş bellek değerleri:" << "\n";

  for (  ; id<10; id++) { // Burada id değişken değeri 5 olarak başlar.
       *(ip+id) = id+1;
       cout << (ip+id) << " adresindeki değer: " << *(ip+id) << "\n";
  }

  free(ip);

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

0xde1690 adresindeki değer: 1
0xde1694 adresindeki değer: 2
0xde1698 adresindeki değer: 3
0xde169c adresindeki değer: 4
0xde16a0 adresindeki değer: 5
Genişletilmiş bellek değerleri:
0xde16a4 adresindeki değer: 6
0xde16a8 adresindeki değer: 7
0xde16ac adresindeki değer: 8
0xde16b0 adresindeki değer: 9
0xde16b4 adresindeki değer: 10

```

Program, malloc() fonksiyonunu kullanarak 5 adet int değer için bellek tahsisi yapar ve her bellek adresine int bir değer atayarak bellek adreslerini ve bu adreslere atadığı değerleri ekrana yazar. Daha sonra, realloc() fonksiyonuyla tahsis edilen bellek miktarını 10 int değer alacak kadar genişletir ve yeni atadığı değerleri ve bellek adreslerini ekrana yazar.

## 2 boyutlu dizilere dinamik bellek tahsisi

C++'da, işaretçi dizileri kullanarak çok boyutlu dizilere dinamik bellek tahsisi yapabiliriz. Şimdi, bir örnek üzerinde iki boyutlu bir karakter dizisine bellek tahsisi işlemini incelemeye çalışalım:

Örnek

```c++
#include <iostream>
#include <cstdlib>
#include <cstring>

using namespace std;

int main(void)
{
  char *pdizi[5];
  int id;

  // Bellek tahsisi
  for (id=0; id<5; id++) {
       pdizi[id] = (char *) malloc(20 * sizeof(char));
  }

  // Dizi atama
  for (id=0; id<5; id++) {
       strcpy(pdizi[id], "Karakter dizisi");
  }
  // Yazdırma
  for (id=0; id<5; id++) {
       cout << pdizi[id] << "\n";
  }

  // Bellek boşaltma
  for (id=0; id<5; id++) {
       free(pdizi[id]);
  }

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Karakter dizisi
Karakter dizisi
Karakter dizisi
Karakter dizisi
Karakter dizisi

```

Program 5 elemanlı bir işaretçi dizisi oluşturur. Her bir işaretçi dizisine 20 byte boyutundaki belleğin başlangıç adresini atar. İşaretçi indeksleme yöntemi ile her bir işaretçiye "Karakter dizisi" ifadesini kopyalar ve ekrana yazdırır. Program sona ermeden önce, free() fonksiyonunu bir döngü içinde kullanarak tahsis edilen belleği boşaltır.
