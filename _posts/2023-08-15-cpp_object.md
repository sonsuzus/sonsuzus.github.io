---
title:  C++ Nesne
author: sonsuz
date: 2023-08-15 20:32:22 +0300
categories: [Program,C++]
tags: [programlama,cpp,nesne,oop,object,sınıf]
---


## Nesne (Object) hakkında

Nesneye yönelik programlama (NYP) ile geliştirilen uygulamalarda program içinde, veriler ile verilere işlem yapacak olan fonksiyonlar (metodlar) sınıf (class) adı verilen yapılar içinde tanımlandıktan sonra bu sınıf türünden bir değişken (nesne) oluşturularak, bu nesne yoluyla sınıf içinde yer alan tüm değişken ve fonksiyonlara erişim sağlanır.

> Bir nesne oluşturmadan önce, class anahtar kelimesini kullanarak nesnenin tüm değişken ve fonksiyonlarını gösteren genel yapısını tanımlamamız gerekir.
{: .prompt-tip }

Sınıflar class anahtar kelimesi ile oluşturulur. Bir sınıf oluşturulduğunda, sınıf içindeki verilere yine sınıf içindeki fonksiyonların işlem yapmasını sağlayan yeni bir veri türü tanımlanmış olur.

Sınıf adı verilen bu yeni veri türü oluşturulduktan sonra, bu sınıfa ait nesne bildirimi yapılır. Bu işlem, int bir veri türünden değişken tanımlamaya benzer.

## Nesne (Object) bildirimi

Nesne bildirimi 2 farklı yöntemle yapılabilir:

1. Nesne bildirimi sınıf bildirimi ile birlikte yapılır.

2. Sınıf bildirimi yapıldıktan sonra, sınıf adını kullanarak nesne bildirimi yapılır.

### Sınıf bildirimi ile birlikte nesne bildirimi

```c++
class sinif {
  // Sadece sınıf fonksiyonlarının erişebileceği private değişkenler
  private:  
    int priid;
  // Sadece sınıf fonksiyonları ile türetilmiş sınıf fonksiyonlarının erişebileceği private değişkenler
  protected:  
    int proid;	
  // Sınıf fonksiyonları, türetilmiş sınıf fonksiyonları ve sınıf nesneleri erşim sağlayabilir.
  public: 
    int pubid;
	void deger_ata(int pid1, int pid2, int pid3);
    void deger_goster();
} nes;


```

Yukarıda, sinif adlı bir sınıfı oluşturulurken aynı zamanda sinif türünden nes adlı bir nesne tanımlanır.

### Sınıf bildirimi yapıldıktan sonra nesne bildirimi

Bir sınıf tanımlayarak, yeni bir veri tipi oluşturduktan sonra, bu veri tipinden değişkenler oluşturmak için nesne bildirimi yapılır. Nesne bildirimi yapmak için sınıf adı ile birlikte oluşturulacak nesne adı kullanılır:

sınıf-adı nesne-adı

Aşağıdaki kod satırı sinif sınıfından nes adlı bir nesne oluşturur:

```


sinif nes;


```

Tanımlaması yaptığımız sınıf içindeki fonksiyonların sadece bildirimini yaptık. Bu fonksiyonların içinde yer alacak kodları yazabilmek için aşağıdaki genel yapıyı kullanmamız gerekir:

```

geri-dönüş-değeri sınıf-adı::fonksiyon-adı(parametre1, parametre2, ...)
{
  işlem satırı;
  .
  .  
}

```

Fonksiyon kodlarını tanımlayan ana yapı içinde yer alan :: işlemcisi bu fonksiyonun sol tarafta yer alan sınıfa ait olduğunu gösterir.

Şimdi, yukarıda tanımlamasını yaptığımız sınıf içinde yer alan fonksiyonların ana yapılarını da içeren programı oluşturmaya çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

class sinif {
  private:
    // Bu değişkene sadece sinif içindeki fonksiyonlar erişim sağlayabilir.
    int priid;

  protected:
    // Bu değişkene sinif içindeki fonksiyonlar ile sinifana sınıfından türetilmiş sınıf fonksiyonları erişim sağlayabilir.
    int proid;

  public:
    // Bu değişkene sinif içindeki fonksiyonlar ve sinif sınıfından türetilmiş sınıf fonksiyonları ile
    // sinifana türünden ve türetilmiş sınıf türünden oluşturulmuş nesneler doğrudan erişim sağlayabilir.
    int pubid;
    void deger_ata(int pid1, int pid2, int pid3)
    {
      priid = pid1; proid = pid2; pubid = pid3;
      cout << "sinif değişkenlerine değer atama: " << priid << " " << proid << " " << pubid << endl;
    }
    void deger_goster()
    {
      cout << "sinif değişken değerleri: " << priid << " " << proid << " " << pubid << endl;
    }
};

int main(void)
{
  sinif nes;

  cout << "nes değişkeninin sinif elemanlarına erişimi:" << endl;
  cout << "--------------------------------------------" << endl;
  nes.deger_ata(7, 21, 135);
  nes.deger_goster();

  // nes.priid = 954; // Derleme hatası verir (Nesne sınıf içindeki private değişkene doğrudan erişim sağlayamaz).
  // nes.proid = 954; // Derleme hatası verir (Nesne sınıf içindeki protected değişkene doğrudan erişim sağlayamaz).
  nes.pubid = 954;    // Nesne sınıf içindeki public değişkene doğrudan erişim sağlar.

  nes.deger_goster();

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

nes değişkeninin sinif elemanlarına erişimi:
--------------------------------------------
sinif değişkenlerine değer atama: 7 21 135
sinif değişken değerleri: 7 21 135
sinif değişken değerleri: 7 21 954

```

Program, sinif adlı bir sınıf oluşturur. Sınıf içinde de private, protected ve public olmak üzere üç adet değişken ve bu değişkenlere değer atayan ve ekranda gösteren iki adet fonksiyon tanımlar.

Program çalışmaya başladığında, sinif cinsinden nes adlı bir nesne tanımlar. Nesne yoluyla, sınıf fonksiyonlarını çağırarak, önce deger\_ata() fonksiyonu ile sınıf içindeki değişkenlere birer değer atar, sonra deger\_goster() fonksiyonu ile değişken değerlerini ekrana yazar. Nesne yoluyla sınıf içindeki pubid adlı public değişkene 954 değeri atar. Sınıf içinde yer alan private ve protected değişkenlere doğrudan nesne yoluyla erişim sağlamaya çalışırsa, program derleme hatası verir. Sonra, deger\_goster() fonksiyonu ile değişken değerlerini tekrar ekrana yazar.

![](cprog/class01.png)

Bir sınıftan oluşturulmuş nesneler ayrı bir sınıf kopyası üzerinde işlem yaptığından, farklı nesnelere ait değişken değerlerinin birbiri ile ilgisi yoktur.

Bir sınıf içinde yer alan üye fonksiyonların, aynı sınıf içinde yer alan diğer fonksiyon ve değişkenlere erişim için nokta (.) işlemcisini kullanmasına gerek yoktur.

Bir sınıftan oluşturulan nesne yoluyla sınıf içinde yer alan private ve protected değişken ve fonksiyonlara direk erişim sağlanmaz, bu erişim aynı sınıf içinde yer alan üye fonksiyonlar yoluyla sağlanır.

## Bir fonksiyona nesne geçirme ve döndürme

Nesnelerde tıpkı diğer değişkenler gibi, fonksiyonlara parametre olarak geçirilebilir ve bir fonksiyon bir nesneyi geri döndürebilir.

### Bir fonksiyona nesne geçirme

Nesneler fonksiyonlara geçirilirken sadece değer olarak geçirilir, yani fonksiyon içinde nesne üzerinde yapılan işlemler fonksiyon sona erdiğinde ortadan kalkar.

Şimdi, bu özelliği bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

class sinif {
    int id;

  public:
    sinif(int pid);
    ~sinif();
    void deger_ata(int pid) { id = pid; }
    void deger_goster(void) { cout << id << endl; }
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

void fonk(sinif nes);

int main(void)
{
  sinif nes(12);

  fonk(nes);

  cout << "Ana program içindeki değer: ";
  nes.deger_goster();

  return 0;
}

void fonk(sinif nes)
{
  nes.deger_ata (24);

  cout << "Fonksiyon içindeki değer: ";
  nes.deger_goster();
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Nesne oluşturuluyor: 12
Fonksiyon içindeki değer: 24
Nesne yok ediliyor: 24
Ana program içindeki değer: 12
Nesne yok ediliyor: 12

```

Program main() fonksiyonu içinde bir nesne oluştururken constructor fonksiyonu yoluyla sınıf içindeki değişkene 12 değerini atar. Bu durumda, constructor fonksiyonu bir kez çağrılır. Sonra, oluşturduğu nesneyi fonk() fonksiyonuna değer yoluyla geçirir. Nesne yeni bir kopyası oluşturulduğu halde, constructor fonksiyonu çağrılmaz. Fonksiyon içinde deger\_ata() fonksiyonu yoluyla değişkene 24 değerini atar ve ekrana yazar. Fonksiyon sona erdiğinde destructor fonksiyonu çağrılır ve fonksiyon çağrısı ile oluşturulan nesne kopyası yok edilir. Daha sonra, main() fonksiyonu içinde fonksiyon çağrısı öncesinde değişkenin sahip olduğu 12 değeri ekrana yazılır. Program sona ererken de, destructor fonksiyonu çağrılır ve ilk oluşturulan nesne yok edilir.

Programda, constructor fonksiyonu bir kez, destructor fonksiyonu ise iki kez çağrılmaktadır.

main() fonksiyonu içinde nesne oluşturulduğunda, constructor fonksiyonu çağrılır. Nesne fonksiyona parametre olarak geçirildiğinde, nesnenin yeni bir kopyası oluşturulur, ancak constructor fonksiyonu yerine copy constructor adı verilen bir fonksiyon kullanılır. Copy constructor sınıf içinde programcı tarafından tanımlanabileceği gibi, tanımlanmadığı takdirde, mevcut nesnenin bire bir kopyasını oluşturacak şekilde C++ tarafından tanımlanır. Copy constructor oluşturulan nesnenin o ana kadar aldığı değerleri ile bir kopyasının oluşturulmasını, normal Constructor fonksiyonu ise verilen ilk değerlerle yeni bir nesne oluşturulmasını sağlar.

Normal constructor fonksiyonu yerine copy constructor kullanılmasının nedeni, oluşturulan nesnenin fonksiyona geçirildiğinde sahip olduğu mevcut değerlerle geçirilmesini sağlamaktır.

### Bir fonksiyondan nesne döndürme

Bir fonksiyon tarafından bir nesne geri döndürüldüğünde, geri döndürülen nesne değerlerini korumak için geçici bir nesne oluşturulur. Fonksiyon tarafından döndürülen bir this nesnesi olup, değer geri döndürüldükten sonra yok edilir.

Şimdi, bu özelliği bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

class sinif {
    int id;

  public:
    void deger_ata(int pid) { id = pid; }
    void deger_goster(void) { cout << id << endl; }
};

sinif fonk(void);

int main(void)
{
  sinif nes;

  nes = fonk();

  nes.deger_goster();

  return 0;
}

sinif fonk(void)
{
  sinif nes;

  nes.deger_ata (24);

  return nes;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

24

```

Program main() fonksiyonu içinde oluşturduğu bir nesneyi, bir fonksiyon içinde oluşturulan ve bir değişken değeri atandıktan sonra geri döndürülen nesne değerlerini atamak için kullanır.

## Nesneleri birbirine atama

Bir sınıftan oluşturulmuş olan nesneleri birbirine atayabilirsiniz. Bu durumda, kopyalama birebir yapılır. Atama işlemcisinin sağında yer alan nesnelere ait değerler işlemcinin sol tarafında yer alan nesneye atanır.

Şimdi, bu özelliği bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

class sinif {
    int id;

  public:
    void deger_ata(int pid) { id = pid; }
    void deger_goster() { cout << id << endl; }
};

int main(void)
{
  sinif nes1, nes2;

  nes1.deger_ata(17);

  nes2 = nes1;

  nes1.deger_goster();
  nes2.deger_goster();

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

17
17

```

Program sinif sınıfından 2 adet nesne oluşturur. İlk nesneye bir değer atadıktan sonra, ilk nesne ikinci nesneye atanır. Her iki nesnede yer alan ve aynı değere sahip değişken değerleri ekrana yazılır.

## Nesne dizileri

C++'da nesneleri bir dizi içinde tanımlayabiliriz. Nesne dizileri bildirimi diğer veri türleri dizi tanımlamaları gibi yapılır. Aşağıdaki satırı bir nesne dizisi tanımlamanın genel yapısını göstermektedir:

nesne-adı[boyut];

### Nesne dizilerinin normal fonksiyonlarla kullanımı

Şimdi, nesne dizi bildirimini bir program üzerinde incelemeye çalışalım:

```c++
// Başlık tanımlaması
#include <iostream>

using namespace std;

// Sınıf tanımlaması
class sinif {
  int id;
public:
  void deger_ata(int pid);
  void deger_goster(void);
};

// Fonksiyonların kodlarının yer aldığı ana yapı bildirimleri
void sinif::deger_ata(int pid)
{
  id = pid;
}

void sinif::deger_goster()
{
  cout << id << endl;
}

int main(void)
{
  sinif nes[5]; // Nesne dizi bildirimi
  int id;

  // Sınıf içindeki değişkene değer atama
  for(id=0; id<5; id++) nes[id].deger_ata(id+1);

  // Sınıf içindeki değişkeni yazdırma
  for(id=0; id<5; id++) nes[id].deger_goster();

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

1
2
3
4
5

```

Program bir adet private int değişken ile bu değişkene değer atayan deger\_ata() adlı bir fonksiyon ve değişken değerini ekrana yazan deger\_goster() adlı iki fonksiyonun yer aldığı sinif adlı bir sınıf bildirimi yapar. Sınıf türünden beş elemanlı bir nesne dizisi oluşturur. Bir for döngüsü ile, nesne dizisinin elemanlarını sıra ile kullanarak, deger\_ata() fonksiyonu yoluyla sınıf içindeki değişkene int bir değer atar. Sonra, aynı sistemi kullanarak, bu defa deger\_goster() fonksiyonu ile değişken değerlerini ekrana yazar.

### Nesne dizilerinin constructor fonksiyonlarıyla kullanımı

Eğer sınıf içinde parametre aktardığımız bir constructor fonksiyonu tanımlarsak, dizi içindeki her bir nesneye bir ilk değer atayabiliriz.Bir önceki programda, deger\_ata() fonksiyonunu aynı işlemi yapan bir constructor fonksiyonu ile değiştirelim:

```c++
#include <iostream>

using namespace std;

class sinif {
  int id;
public:
  sinif(int pid) { id=pid; } // constructor fonksiyonu
  void deger_goster(void);
};

// Fonksiyonların kodlarının yer aldığı ana yapı bildirimleri
void sinif::deger_goster()
{
  cout << id << endl;
}

int main(void)
{
  // Nesne dizi bildirimi ile birlikte değere atama (Her sayı yerine aslında constructor fonksiyonu çağrılmaktadır.)
  sinif nes[5] = { 1, 2, 3, 4, 5 };
  int id;

  // Sınıf içindeki değişkeni yazdırma
  for(id=0; id<5; id++) nes[id].deger_goster();

  return 0;
}


```

Burada, dizi içindeki nesnelere değer atamada sadece sayılar yer almasına rağmen, aslında her bir atamada constructor fonksiyonu çağrılmaktadır. Ancak, tek bir parametre kullanıldığından, bu şekilde yazılabilmektedir.

Şimdi, iki parametre geçirilen bir constructor fonksiyonu içeren bir örneği incelemeye çalışalım:

```c++
#include <iostream>

using namespace std;

class sinif {
  int id1, id2;
public:
  sinif(int pid1, int pid2) { id1=pid1; id2=pid2; } // constructor fonksiyonu
  void deger_goster(void);
};

// Fonksiyonların kodlarının yer aldığı ana yapı bildirimleri
void sinif::deger_goster(void)
{
  cout << id1 << " " << id2 << endl;
}

int main(void)
{
  // Nesne dizi bildirimi ile birlikte 2 değişkene değer atama
  sinif nes[5] = {
	  sinif(1, 6),
      sinif(2, 7),
	  sinif(3, 8),
	  sinif(4, 9),
	  sinif(5, 10)
  };

  int id;

  // Sınıf içindeki değişkeni yazdırma
  for(id=0; id<5; id++) nes[id].deger_goster();

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

1 6
2 7
3 8
4 9
5 10

```

Program iki adet private int değişken ile bu değişkenlere değer atayan bir constructor fonksiyonu ve değişken değerlerini ekrana yazan deger\_goster() adlı bir fonksiyonun yer aldığı sinif adlı bir sınıf bildirimi yapar. Sınıf türünden beş elemanlı bir nesne dizisi oluşturur. Dizi oluştururken, ilk değer atama yöntemi ile constructor fonksiyonunu kullanarak, sınıf içindeki değişkenlere birer değer atar. Bir for döngüsü ile, deger\_goster() fonksiyonu ile değişken değerlerini ekrana yazar.

## Nesne işaretçileri

Oluşturduğumuz nesnelere işaretçiler yoluyla da erişim sağlayabiliriz. İşaretçiler yoluyla nesnelere erişim sağlamak için -> işlemcisi kullanılır.

### Nesne işaretçilerini tek bir nesne ile kullanma

Nesne işaretçilerinin tek bir nesne ile kulllanımını bir örnek üzerinde incelemeye çalışalım:

```c++
#include <iostream>

using namespace std;

class sinif {
  int id;      
public:
  sinif(int pid) { id = pid; };
  void deger_goster(void);
};

void sinif::deger_goster()
{
  cout << id << endl;
}

int main(void)
{
  sinif nes(21);   // Nesne bildirimi
  sinif *pnes;     // Nesne işaretçi bildirimi

  pnes = &nes;     // Nesne bellek adresini işaretçiye atama

  nes.deger_goster();   // Nesne yoluyla değişkene erişim
  pnes->deger_goster(); // Nesne işaretçisi yoluyla değişkene erişim 
	
  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

21
21

```

Program bir adet private int değişken ile bu değişkene değer atayan bir constructor fonksiyonu ve değişken değerini ekrana yazan deger\_goster() adlı bir fonksiyonun yer aldığı sinif adlı bir sınıf bildirimi yapar. Sınıf türünden bir nesne ve bir adet nesne işaretçisi bildirimi yapar. Sonra, nesnenin bellek adresini işaretçiye atar. Nesne ve nesne işaretçisi yoluyla iki defa deger\_goster() fonksiyonunu kullanarak değişken değerini ekrana yazar.

### Nesne işaretçilerini birden fazla nesne ile kullanma

Şimdi nesne işaretçilerinin nesne dizileri ile kullanımını bir örnek üzerinde incelemeye çalışalım:

```c++
#include <iostream>

using namespace std;

class sinif {
  int id;
public:
  sinif(int pid) { id = pid; };
  void deger_goster(void);
};

void sinif::deger_goster()
{
  cout << id << endl;
}

int main(void)
{
  sinif nes[5] = { 1, 2, 3, 4, 5 };   // Nesne dizisi bildirimi
  sinif *pnes; // Nesne işaretçi bildirimi
  int id;

  pnes = nes;    // Nesne bellek adresini işaretçiye atama

  for (id=0; id<5; id++) {
       cout << "Nesne dizisi yoluyla: ";
	   nes[id].deger_goster();   // Nesne yoluyla değişkene erişim
       cout << "Nesne işaretçisi yoluyla: ";
	   pnes->deger_goster();     // Nesne işaretçisi yoluyla değişkene erişim

	   pnes++;                   // Dizideki bir sonraki nesnenin adresini alma
  }

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Nesne dizisi yoluyla: 1
Nesne işaretçisi yoluyla: 1
Nesne dizisi yoluyla: 2
Nesne işaretçisi yoluyla: 2
Nesne dizisi yoluyla: 3
Nesne işaretçisi yoluyla: 3
Nesne dizisi yoluyla:4
Nesne işaretçisi yoluyla: 4
Nesne dizisi yoluyla: 5
Nesne işaretçisi yoluyla: 5

```

Program bir adet private int değişken ile bu değişkene değer atayan bir constructor fonksiyonu ve değişken değerini ekrana yazan deger\_goster() adlı bir fonksiyonun yer aldığı sinif adlı bir sınıf bildirimi yapar. Sınıf türünden beş elemanlı bir nesne dizisi ve bir adet nesne işaretçisi bildirimi yapar. Sonra, nesne dizisinin bellek adresini işaretçiye atar. Bir for döngüsü ile, nesne dizisi ve nesne işaretçisi yoluyla iki defa deger\_goster() fonksiyonunu kullanarak değişken değerini ekrana yazar.

## Ana sınıf için tanımlanmış işaretçileri türetilmiş sınıf nesneleri için kullanma

Bir ana sınıftan bir sınıf türetildiğinde, ana sınıf türünden oluşturulan bir işaretçiye türetilmiş sınıftan oluşturulmuş bir nesnenin adresini atarsak, bu işaretçi yoluyla ana sınıf içinde yer alan veri ve fonksiyonlara erişim sağlayabiliriz.

Şimdi, bu uygulamayı bir örnek üzerinde incelemeye çalışalım:

```c++
#include <iostream>

using namespace std;

class sinifana {
  int priidana;
public:
  void deger_ata_ana(int pid) { priidana = pid; };
  void deger_goster_ana(void);
};

class siniftur: public sinifana {
  int priidtur;
public:
  void deger_ata_tur(int pid) { priidtur = pid; };
  void deger_goster_tur(void);
};

void sinifana::deger_goster_ana()
{
  cout << "priidana değişken değeri: " << priidana << endl;
}

void siniftur::deger_goster_tur()
{
  cout << "priidtur değişken değeri: " << priidtur << endl;
}

int main(void)
{
  sinifana *pnes_ana; // Ana sınıf türünden nesne işaretçi bildirimi
  siniftur nes_tur;   // Türetilen sınıf nesne bildirimi

  // Türetilen sınıf nesnesini kendi sınıf fonksiyonları için kullanma
  nes_tur.deger_ata_tur(35);
  nes_tur.deger_goster_tur();

  pnes_ana = &nes_tur; // Türetilen sınıf nesne bellek adresini ana sınıf işaretçisine atama

  // Türetilen sınıf nesnesi yoluyla ana sınıf fonksiyonlarına erişim
  pnes_ana->deger_ata_ana(21);
  pnes_ana->deger_goster_ana();

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

priidtur değişken değeri: 35
priidana değişken değeri: 21

```

Program, bir adet private int değişken ile bu değişkene değer atayan deger\_ata() adlı ve değişken değerini ekrana yazan deger\_goster() adlı iki fonksiyonun yer aldığı sinifana adlı bir sınıf bildirimi yapar. Sonra, sinifana sınıfından siniftur adlı bir sınıf oluşturarak, sınıfın içinde bir adet private int değişken ile bu değişkene değer atayan deger\_ata\_tur() adlı ve değişken değerini ekrana yazan deger\_goster\_tur() adlı iki fonksiyon bildirimi yapar.

sinifana türünden pnes\_ana adlı bir nesne işaretçisi ve siniftur türünden nes\_tur adlı bir nesne bildirimi yapar. Önce, nes\_tur nesnesi ile türetilen sınıf fonksiyonlarını kullanarak, türetilen sınıf içindeki değişkene bir değer atar ve ekrana yazar. Sonra, nes\_tur nesnesinin bellek adresini pnes\_ana işaretçisine atar. Ana sınıf işaretçisine atanan türetilen sınıf nesnesi yoluyla, ana sınıf fonksiyonlarını kullanarak, ana sınıf içindeki değişkene bir değer atar ve ekrana yazar.

Burada, türetilen sınıf nesne adresini gösteren ana sınıf işaretçisi ile, türetilmiş sınıfın fonksiyonlarına erişim sağlanmaz.

## this işaretçisi

Bir sınıfta yer alan üye fonksiyon çağrıldığında, this adı verilen ve çağıran nesneyi gösteren bir işaretçi otomatik olarak, bu fonksiyona geçirilir.

```c++
#include <iostream>

using namespace std;

class sinif {
  int id;
public:
  // Burada id değişkeni önündeki this-> ifadesini kullanmak gerekli değildir.
  sinif(int pid) { this->id = pid; };
  void deger_goster(void);
};

void sinif::deger_goster()
{
  cout << "id değişken değeri: " << id << endl;
}

int main()
{
  sinif nes(21); // Nesne bildirimi

  nes.deger_goster(); // Nesne yoluyla değişkene erişim

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeyi ekrana yazar:

```

id değişken değeri: 21

```

Program, sinif sınıfı içindeki id değişkenine constructor fonksiyonunda this-> ifadesi ile erişim sağlar. Bu ifade kullanılmasa da erişim sağlanır. Burada, this işaretçisi nes adlı çağıran nesneyi gösterir.

## Sınıf üyeleri işaretçileri

C++'da, bir sınıfta bulunan veri ve fonksiyonlara erişim için kullanılan işaretçiler vardır. Bu işaretçiler için .\* ve ->\* işlemcileri kullanılır.

Şimdi, sınıf üyeleri işaretçilerinin kullanımını bir örnek üzerinde incelemeye çalışalım:

```c++
#include <iostream>

using namespace std;

class sinif {
  public:
    int id;
    sinif(int pid) { id=pid; } // constructor fonksiyonu
    void deger_goster(void);
};

// Fonksiyonların kodlarının yer aldığı ana yapı bildirimi
void sinif::deger_goster()
{
  cout << "id değişken değeri: " << id << endl;
}

int main()
{
  int sinif::*pdata;      // Sınıftaki veri (değişken) için işaretçi tanımlama
  void (sinif::*pfunc)(); // Sınıftaki fonksiyon için işaretçi tanımlama

  sinif nes(21);          // Nesne oluşturma
  sinif *pnes;            // Nesne işaretçisi oluşturma

  pnes = &nes            // Nesne adresini işaretçiye atama

  pdata = &sinif::id;           // id değişkeni adresini işaretçiye atama
  pfunc = &sinif::deger_goster; // deger_goster() fonksiyonunun adresini işaretçiye atama

  // Nesne üzerinden erişim
  cout << nes.*pdata << endl;   // Sınıf içindeki değişkene nesne üzerinden işaretçi yoluyla erişim
  (nes.*pfunc)();               // Sınıf içindeki fonksiyona nesne üzerinden işaretçi yoluyla erişim

  // Nesne işaretçisi üzerinden erişim
  cout << pnes->*pdata << endl; // Sınıf içindeki değişkene nesne işaretçisi üzerinden işaretçi yoluyla erişim
  (pnes->*pfunc)();             // Sınıf içindeki fonksiyona nesne işaretçisi üzerinden işaretçi yoluyla erişim

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

21
id değişken değeri: 21
21
id değişken değeri: 21

```

Program, önce sınıf içindeki değişken ve fonksiyon için birer işaretçi tanımlar. Sınıf cinsinden birer adet nesne ve nesne işaretçisi oluşturarak, nesne adresini işaretçiye atar. Değişken adresini değişken için tanımlanan işaretçiye ve fonksiyon adresini fonksiyon için tanımlanan işaretçiye atar. Sınıf içindeki değişken ve fonksiyona önce nesne üzerinden sonra nesne işaretçisi üzerinden erişim sağlayarak işlem yapar.
