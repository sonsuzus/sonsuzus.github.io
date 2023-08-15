---
title:  C++ Sanal (virtual) fonksiyonlar
author: sonsuz
date: 2023-08-15 21:16:07 +0300
categories: [Program,C++]
tags: [programlama,cpp,fonksiyon,sanal fonksiyon]
---



Sanal fonksiyonlar bir ana sınıf içinde bildirimi yapıldıktan sonra türetilen sınıf içinde tekrar tanımlanır. Sanal fonksiyon bildirimi için kullanılan genel yapı aşağıda gösterilmektedir:

```

class ana-sınıf {
  public:
    virtual veri-türü fonk-adı(parametreler)
    {
      // kod bloğu   
    }
}

class türetilen-sınıf public: ana-sınıf {
  public:
    veri-türü fonk-adı(parametreler)
    {
      // kod bloğu   
    }
}

```

Sanal bir fonksiyon oluşturmak için, ana sınıf içindeki fonksiyon bildiriminden önce virtual anahtar kelimesi kullanılır. Sanal fonksiyon içeren bir sınıftan yeni bir sınıf türetildiğinde, türetilen her sınıf içinde sanal fonksiyon, virtual anahtar kelimesi kullanılmadan, yeniden tanımlanır ve fonksiyon içeriği yeniden düzenlenir.

> Sanal fonksiyon ile, aynı isme sahip bir fonksiyon her sınıf için ayrı bir işlem yapacak şekilde tanımlanabilmektedir. Bu durum nesneye yönelik [programlamada çok biçimlilik](https://sonsuzus.github.io/posts/cpp_poly/) (Polymorphism) özelliğinin bir sonucudur.
{: .prompt-tip }

Sanal fonksiyonlar çalışma zamanı çok biçimlilik (Runtime Polymorphism) özelliği sağlar. Bu özellikle, virtual anahtar kelimesi derleyiciye fonksiyon bağlama işlemini derleme zamanında değil çalışma zamanında yapmasını bildirir.

[İşaretçi](https://sonsuzus.github.io/posts/cpp_isaretci/) kullanarak erişim sağlamak sanal fonksiyonları sınıf içindeki diğer fonksiyonlardan farklı hale getirir. Ana sınıf türünden oluşturulan bir işaretçi ana sınıf ve ana sınıftan türetilen tüm sınıflar içindeki sanal fonksiyonlara erişim sağlayabilir.

İlk bakışta, ana sınıf içinde bildirimi yapılan sanal bir fonksiyonunun ana sınıftan türetilen bir sınıf içinde yeniden tanımlanması, fonksiyon için çoklu işlem tanımlama (overloading) işlemi ile benzerlik gösterir. Ancak, türetilen sınıf içindeki sanal fonksiyonun yeniden tanımlanmasında kullanılan bildirim yapısı ana sınıf içindeki sanal fonksiyon ile aynı olmalıdır. Fonksiyon çoklu işlem tanımlama işleminde fonksiyon parametre sayısı ve veri türlerinden birisi mutlaka farklı olmalıdır. Ayrıca, fonksiyonun geri döndürdüğü değer de farklı olabilir. Eğer türetilen sınıf içindeki sanal fonksiyon bildirim yapısı ana sınıf içindekinden farklı olursa, fonksiyonun sanal özelliği kaybolur ve fonksiyon çoklu işlem tanımlama işlemi uygulanır.

## Sanal fonksiyonların ana sınıf işaretçisi ile çağrılması

Sanal fonksiyonlar genel olarak ana sınıf işaretçisi kullanılarak çağrılır. Bu yöntemde, ana sınıftan ve türetilen sınıflardan oluşturulan nesnelerin adresleri ana sınıf türünden tanımlanan işaretçiye atanarak her bir sınıfta yer alan sanal fonksiyona çağrı yapılır.

Sanal fonksiyon tanımlamayı bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

class sinifana {
  private:
    int priidana;

  protected:
    int proidana;

  public:
    int pubidana;
    // Sanal fonksiyon bildirimi
    virtual void deger_topla(void) {
      cout << "sinifana değişken toplamları: "<< priidana + proidana + pubidana << endl;
    }
    void deger_ata(int pid1, int pid2, int pid3)
    {
      priidana = pid1; proidana = pid2; pubidana = pid3;
      cout << "sinifana değişkenlerine değer atama: " << priidana << " " << proidana << " " << pubidana << endl;
    }
    void deger_goster()
    {
      cout << "sinifana değişken değerleri: " << priidana << " " << proidana << " " << pubidana << endl;
    }
};

class siniftur1 : public sinifana {
  private:
    int priidtur1;

  protected:
    int proidtur1;

  public:
    int pubidtur1;
    // Sanal fonksiyonun siniftur1 için yeniden tanımlanması
    void deger_topla(void) {
      cout << "siniftur1 değişken toplamları: "<< priidtur1 + proidtur1 + pubidtur1 << endl;
    }
    void deger_ata_tur1(int pid1, int pid2, int pid3)
    {
      priidtur1 = pid1; proidtur1 = pid2; pubidtur1 = pid3;
      cout << "siniftur1 değişkenlerine değer atama: " << priidtur1 << " " << proidtur1 << " " <<  pubidtur1 << endl;
    }
    void deger_goster_tur1() { cout << "siniftur1 değişken değerleri: " << priidtur1 << " " << proidtur1 << " " << pubidtur1 << endl; }
};

class siniftur2 : public sinifana {
  private:
    int priidtur2;

  protected:
    int proidtur2;

  public:
    int pubidtur2;
    // Sanal fonksiyonun siniftur2 için yeniden tanımlanması
    void deger_topla(void) {
      cout << "siniftur2 değişken toplamları: "<< priidtur2 + proidtur2 + pubidtur2 << endl;
    }
    void deger_ata_tur2(int pid1, int pid2, int pid3)
    {
      priidtur2 = pid1; proidtur2 = pid2; pubidtur2 = pid3;
      cout << "siniftur2 değişkenlerine değer atama: " << priidtur2 << " " << proidtur2 << " " <<  pubidtur2 << endl;
    }
    void deger_goster_tur2() { cout << "siniftur2 değişken değerleri: " << priidtur2 << " " << proidtur2 << " " << pubidtur2 << endl; }
};

int main(void)
{
  sinifana *pnes_ana, nes_ana;
  siniftur1 nes_tur1;
  siniftur2 nes_tur2;

  cout << "pnes_ana işaretçisi ile nes_ana değişkeninin sinifana elemanlarına erişimi:" << endl;
  cout << "---------------------------------------------------------------------------" << endl;
  pnes_ana = &nes_ana;                // sinifana türünden işaretçi sinifana nesnesinin adresini gösteriyor.
  pnes_ana->deger_ata(17, 874, 1345);
  pnes_ana->deger_goster();
  pnes_ana->deger_topla();            // sinifana sanal fonksiyonuna erişim.
  nes_ana.deger_topla();              // Yukarıdaki işlem satırı ile aynı işlemi yapar.

  cout << endl << "nes_tur1 değişkeninin siniftur1 elemanlarına erişimi:" << endl;
  cout << "-----------------------------------------------------" << endl;
  nes_tur1.deger_ata_tur1(15, 74, 384);
  nes_tur1.deger_goster_tur1();
  pnes_ana = &nes_tur1;               // sinifana türünden işaretçi siniftur1 nesnesinin adresini gösteriyor.
  pnes_ana->deger_topla();            // Burada işaretçinin siniftur1 fonksiyonuna erişmesinin nedeni fonksiyonun sanal olarak tanımlanması
  nes_tur1.deger_topla();             // Yukarıdaki işlem satırı ile aynı işlemi yapar.

  cout << endl << "nes_tur2 değişkeninin siniftur2 elemanlarına erişimi:" << endl;
  cout << "-----------------------------------------------------" << endl;
  nes_tur2.deger_ata_tur2(95, 291, 752);
  nes_tur2.deger_goster_tur2();
  pnes_ana = &nes_tur2;               // sinifana türünden işaretçi siniftur2 nesnesinin adresini gösteriyor.
  pnes_ana->deger_topla();            // Burada işaretçinin siniftur2 fonksiyonuna erişmesinin nedeni fonksiyonun sanal olarak tanımlanması
  nes_tur2.deger_topla();             // Yukarıdaki işlem satırı ile aynı işlemi yapar.

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

pnes_ana işaretçisi ile nes_ana değişkeninin sinifana elemanlarına erişimi:
--------------------------------------------------------------------------
sinifana değişkenlerine değer atama: 17 874 1345
sinifana değişken değerleri: 17 874 1345
sinifana değişken toplamları: 2236
sinifana değişken toplamları: 2236

nes_tur1 değişkeninin siniftur1 elemanlarına erişimi:
------------------------------------------------------
siniftur1 değişkenlerine değer atama: 15 74 384
siniftur1 değişken değerleri: 15 74 384
siniftur1 değişken toplamları: 473
siniftur1 değişken toplamları: 473

nes_tur2 değişkeninin siniftur2 elemanlarına erişimi:
------------------------------------------------------
siniftur2 değişkenlerine değer atama: 95 291 752
siniftur2 değişken değerleri: 95 291 752
siniftur2 değişken toplamları: 1138
siniftur2 değişken toplamları: 1138

```

Program, sinifana adlı bir sınıf ve bu sınıftan public olarak türetilen siniftur1 ve siniftur2 adlı iki adet sınıf oluşturur. Her üç sınıf içinde de private, protected ve public olmak üzere üç adet değişken ve bu değişkenlere değer atayan, ekranda gösteren ve değerlerini toplayan üç adet fonksiyon tanımlar.

Program, sinifana türünden pnes\_ana adlı bir işaretçi ve nes\_ana adlı bir nesne ile siniftur1 türünden nes\_tur1 adlı ve siniftur2 türünden nes\_tur2 adlı bir nesne oluşturur.

İlk olarak, nes\_ana nesnesinin bellek adresini pnes\_ana işaretçisine atar. Bu işaretçi ile, sinifana içindeki deger\_ata() ve deger\_goster() fonksiyonları ile sinifana içindeki değişkenlere birer değer atar ve ekrana yazar. İşaretçi ile deger\_topla() sanal fonksiyonunu kullanarak, sinifana içindeki değişken değerlerini toplar. Sonra, aynı işlemi nes\_ana nesnesi yoluyla yapar.

İkinci safhada, nes\_tur1 nesnesi yoluyla siniftur1 içindeki deger\_ata\_tur1() ve deger\_goster\_tur1() fonksiyonları ile siniftur1 içindeki değişkenlere birer değer atar ve ekrana yazar. Sonra, nes\_tur1 nesnesinin bellek adresini pnes\_ana işaretçisine atar. İşaretçi ile siniftur1 içindeki deger\_topla() sanal fonksiyonunu kullanarak, siniftur1 içindeki değişken değerlerini toplar. Sonra, aynı işlemi nes\_tur1 nesnesi yoluyla yapar.

Son olarak, nes\_tur2 nesnesi yoluyla siniftur2 içindeki deger\_ata\_tur2() ve deger\_goster\_tur2() fonksiyonları ile siniftur2 içindeki değişkenlere birer değer atar ve ekrana yazar. Sonra, nes\_tur2 nesnesinin bellek adresini pnes\_ana işaretçisine atar. İşaretçi ile siniftur2 içindeki deger\_topla() sanal fonksiyonunu kullanarak, siniftur2 içindeki değişken değerlerini toplar. Sonra, aynı işlemi nes\_tur2 nesnesi yoluyla yapar.

Her üç sınıf içinde ayrı ayrı tanımlanmış olan deger\_topla() sanal fonksiyonu, sinifana sınıfı türünden tanımlanmış işaretçiye her sınıftan oluşturulmuş nesnelerin bellek adresleri atandığında, işaretçinin her sınıfın sanal fonksiyonuna erişerek işlem yapmasını sağlar. Ana sınıf olan sinifana işaretçisi ile sanal fonksiyon çağrıldığında, derleyici ana sınıf veya türetilmiş sınıf içindeki sanal fonksiyonlardan hangisini kullanacağına çalışma zamanında karar verir. Bu özelliğe çalışma zamanı çok biçimliliği (Runtime Polymorphism) denir.

Diğer taraftan, sinifana sınıfı türünden tanımlanmış işaretçiye türetilen sınıflardan oluşturulmuş nesnelerin bellek adresleri atansa bile, işaretçi sanal fonksiyonlar dışındaki elemanlara erişim sağlayamaz.

Programın çalışmasını gösteren şema aşağıdadır:

![](cprog/fonkvirtual01.png)

## Sanal fonksiyonların ana sınıf referansı ile çağrılması

Bir ana sınıf ve bu sınıftan türetilen sınıflar içindeki sanal fonksiyonları çağırmak için ana sınıftan türünden oluşturulan referans değerlerini kullanabiliriz. Bu yöntemde, ana sınıftan ve türetilen sınıflardan oluşturulan nesneler ana sınıf türünden tanımlanan referansa atanarak her bir sınıfta yer alan sanal fonksiyona çağrı yapılır.

Sanal fonksiyonların ana sınıf referansı ile çağrılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

class sinifana {
  private:
    int priidana;

  protected:
    // Bu değişkenin sinifturtur sınıfında tek kopyası oluşur.
    int proidana;

  public:
    // Buradaki değişken ve fonksiyonların sinifturtur sınıfında tek kopyası oluşur.
    int pubidana;
    // Sanal fonksiyon bildirimi
    virtual void deger_topla(void) {
      cout << "sinifana değişken toplamları: "<< priidana + proidana + pubidana << endl;
    }
    void deger_ata(int pid1, int pid2, int pid3)
    {
      priidana = pid1; proidana = pid2; pubidana = pid3;
      cout << "sinifana değişkenlerine değer atama: " << priidana << " " << proidana << " " << pubidana << endl;
    }
    void deger_goster()
    {
      cout << "sinifana değişken değerleri: " << priidana << " " << proidana << " " << pubidana << endl;
    }
};

class siniftur1 : public sinifana {
  private:
    int priidtur1;

  protected:
    int proidtur1;

  public:
    int pubidtur1;
    // Sanal fonksiyonun siniftur1 için yeniden tanımlanması
    void deger_topla(void) {
      cout << "siniftur1 değişken toplamları: "<< priidtur1 + proidtur1 + pubidtur1 << endl;
    }
    void deger_ata_tur1(int pid1, int pid2, int pid3)
    {
      priidtur1 = pid1; proidtur1 = pid2; pubidtur1 = pid3;
      cout << "siniftur1 değişkenlerine değer atama: " << priidtur1 << " " << proidtur1 << " " <<  pubidtur1 << endl;
    }
    void deger_goster_tur1() { cout << "siniftur1 değişken değerleri: " << priidtur1 << " " << proidtur1 << " " << pubidtur1 << endl; }
};

class siniftur2 : public sinifana {
  private:
    int priidtur2;

  protected:
    int proidtur2;

  public:
    int pubidtur2;
    // Sanal fonksiyonun siniftur2 için yeniden tanımlanması
    void deger_topla(void) {
      cout << "siniftur2 değişken toplamları: "<< priidtur2 + proidtur2 + pubidtur2 << endl;
    }
    void deger_ata_tur2(int pid1, int pid2, int pid3)
    {
      priidtur2 = pid1; proidtur2 = pid2; pubidtur2 = pid3;
      cout << "siniftur2 değişkenlerine değer atama: " << priidtur2 << " " << proidtur2 << " " <<  pubidtur2 << endl;
    }
    void deger_goster_tur2() { cout << "siniftur2 değişken değerleri: " << priidtur2 << " " << proidtur2 << " " << pubidtur2 << endl; }
};

int main(void)
{
  sinifana nes_ana;
  siniftur1 nes_tur1;
  siniftur2 nes_tur2;

  cout << "rnes_ana referansı ile nes_ana değişkeninin sinifana elemanlarına erişimi:" << endl;
  cout << "--------------------------------------------------------------------------" << endl;
  sinifana &rnes_ana = nes_ana;          // sinifana türünden referans oluşturarak nes_ana nesnesini referansa atar.
  nes_ana.deger_ata(842, 1789, 3164);
  nes_ana.deger_goster();
  rnes_ana.deger_topla();                // rnes_ana referansı ile anasinif sanal fonksiyonuna erişim.

  cout << endl << "rnes_ana01 referansı ve nes_tur1 değişkeninin siniftur1 elemanlarına erişimi:" << endl;
  cout << "-----------------------------------------------------------------------------" << endl;
  sinifana &rnes_ana1 = nes_tur1;       // sinifana türünden referans oluşturarak nes_tur1 nesnesini referansa atar.
  nes_tur1.deger_ata_tur1(178, 315, 1065);
  nes_tur1.deger_goster_tur1();
  rnes_ana1.deger_topla();              // rnes_ana1 referansı ile siniftur1 sanal fonksiyonuna erişim.

  cout << endl << "rnes_ana02 referansı ve nes_tur2 değişkeninin siniftur2 elemanlarına erişimi:" << endl;
  cout << "-----------------------------------------------------------------------------" << endl;
  sinifana &rnes_ana2 = nes_tur2;       // sinifana türünden referans oluşturarak nes_tur1 nesnesini referansa atar.
  nes_tur2.deger_ata_tur2(127, 2284, 5542);
  nes_tur2.deger_goster_tur2();
  rnes_ana2.deger_topla();              // rnes_ana2 referansı ile siniftur2 sanal fonksiyonuna erişim.

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

rnes_ana referansı ile nes_ana değişkeninin sinifana elemanlarına erişimi:
--------------------------------------------------------------------------
sinifana değişkenlerine değer atama: 842 1789 3164
sinifana değişken değerleri: 842 1789 3164
sinifana değişken toplamları: 5795

rnes_ana01 referansı ve nes_tur1 değişkeninin siniftur1 elemanlarına erişimi:
-----------------------------------------------------------------------------
siniftur1 değişkenlerine değer atama: 178 315 1065
siniftur1 değişken değerleri: 178 315 1065
siniftur1 değişken toplamları: 1558

rnes_ana02 referansı ve nes_tur2 değişkeninin siniftur2 elemanlarına erişimi:
-----------------------------------------------------------------------------
siniftur2 değişkenlerine değer atama: 127 2284 5542
siniftur2 değişken değerleri: 127 2284 5542
siniftur2 değişken toplamları: 7953

```

Program, sinifana adlı bir sınıf ve bu sınıftan public olarak türetilen siniftur1 ve siniftur2 adlı iki adet sınıf oluşturur. Her üç sınıf içinde de private, protected ve public olmak üzere üç adet değişken ve bu değişkenlere değer atayan, ekranda gösteren ve değerlerini toplayan üç adet fonksiyon tanımlar.

Program, sinifana türünden nes\_ana adlı bir nesne ile siniftur1 türünden nes\_tur1 adlı ve siniftur2 türünden nes\_tur2 adlı bir nesne oluşturur.

İlk olarak, nes\_ana nesnesini sinifana türünden oluşturduğu rnes\_ana referansına atar. Nes\_ana nesnesi ile, sinifana içindeki deger\_ata() ve deger\_goster() fonksiyonları ile sinifana içindeki değişkenlere birer değer atar ve ekrana yazar. Sonra, rnes\_ana referansı ile sinifana sınıfı deger\_topla() sanal fonksiyonunu kullanarak, sinifana içindeki değişken değerlerini toplar.

İkinci safhada, nes\_tur1 nesnesini sinifana türünden oluşturduğu rnes\_ana1 referansına atar. Nes\_tur1 nesnesi yoluyla siniftur1 içindeki deger\_ata\_tur1() ve deger\_goster\_tur1() fonksiyonları ile siniftur1 içindeki değişkenlere birer değer atar ve ekrana yazar. Sonra, rnes\_ana1 nesnesi ile siniftur1 içindeki deger\_topla() sanal fonksiyonunu kullanarak, siniftur1 içindeki değişken değerlerini toplar.

Son olarak, nes\_tur2 nesnesini sinifana türünden oluşturduğu rnes\_ana2 referansına atar. Nes\_tur2 nesnesi yoluyla siniftur2 içindeki deger\_ata\_tur2() ve deger\_goster\_tur2() fonksiyonları ile siniftur2 içindeki değişkenlere birer değer atar ve ekrana yazar. Sonra, rnes\_ana2 nesnesi ile siniftur2 içindeki deger\_topla() sanal fonksiyonunu kullanarak, siniftur2 içindeki değişken değerlerini toplar.

Programın çalışmasını gösteren şema aşağıdadır:

![](cprog/fonkvirtual02.png)

Sanal fonksiyonların ana sınıf referansı ile çağrılması işleminde her bir sanal fonksiyon için ana sınıf türünden bir referans oluşturulması gerekir. Sanal fonksiyonların ana sınıf işaretçisi ile çağrılması işleminde ise ana sınıf cinsinden tek bir işaretçi oluşturmak ve her sınıfa ait nesne adresini bu işaretçiye atamak yeterlidir.

## Çok seviyeli kalıtımda sanal fonksiyonların kullanımı

Çok seviyeli kalıtımda, bir ana sınıftan türetilen bir sınıfı ana sınıf olarak kullanarak diğer bir sınıf türetildiğinde, ilk ana sınıf içindeki sanal fonksiyonlar yeniden tanımlanarak türetilen tüm sınıfların içinde kullanılabilir.

Çok seviyeli kalıtımda sanal fonksiyonların kullanımı bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

class sinifana {
  private:
    int priidana;

  protected:
    // Bu değişkenin sinifturtur sınıfında tek kopyası oluşur.
    int proidana;

  public:
    // Buradaki değişken ve fonksiyonların sinifturtur sınıfında tek kopyası oluşur.
    int pubidana;
    // Sanal fonksiyon bildirimi
    virtual void deger_topla(void) {
      cout << "sinifana değişken toplamları: "<< priidana + proidana + pubidana << endl;
    }
    void deger_ata(int pid1, int pid2, int pid3)
    {
      priidana = pid1; proidana = pid2; pubidana = pid3;
      cout << "sinifana değişkenlerine değer atama: " << priidana << " " << proidana << " " << pubidana << endl;
    }
    void deger_goster()
    {
      cout << "sinifana değişken değerleri: " << priidana << " " << proidana << " " << pubidana << endl;
    }
};

class siniftur : public sinifana {
  private:
    int priidtur;

  protected:
    int proidtur;

  public:
    int pubidtur;
    // Sanal fonksiyonun siniftur için yeniden tanımlanması
    virtual void deger_topla(void) {
      cout << "siniftur değişken toplamları: "<< priidtur + proidtur + pubidtur << endl;
    }
    void deger_ata_tur(int pid1, int pid2, int pid3)
    {
      priidtur = pid1; proidtur = pid2; pubidtur = pid3;
      cout << "siniftur değişkenlerine değer atama: " << priidtur << " " << proidtur << " " <<  pubidtur << endl;
    }
    void deger_goster_tur() { cout << "siniftur değişken değerleri: " << priidtur << " " << proidtur << " " << pubidtur << endl; }
};

class sinifturtur : public siniftur {
  private:
    int priidturtur;

  protected:
    int proidturtur;

  public:
    int pubidturtur;
    // Sanal fonksiyonun sinifturtur için yeniden tanımlanması
    void deger_topla(void) {
      cout << "sinifturtur değişken toplamları: "<< priidturtur + proidturtur + pubidturtur << endl;
    }
    void deger_ata_turtur(int pid1, int pid2, int pid3)
    {
      priidturtur = pid1; proidturtur = pid2; pubidturtur = pid3;
      cout << "sinifturtur değişkenlerine değer atama: " << priidturtur << " " << proidturtur << " " <<  pubidturtur << endl;
    }
    void deger_goster_turtur() { cout << "sinifturtur değişken değerleri: " << priidturtur << " " << proidturtur << " " << pubidturtur << endl; }
};

int main(void)
{
  sinifana *pnes_ana, nes_ana;
  siniftur nes_tur;
  sinifturtur nes_turtur;

  cout << "pnes_ana işaretçisi ile nes_ana değişkeninin sinifana elemanlarına erişimi:" << endl;
  cout << "---------------------------------------------------------------------------" << endl;
  pnes_ana = &nes_ana;                // sinifana türünden işaretçi sinifana nesnesinin adresini gösteriyor.
  pnes_ana->deger_ata(98, 391, 754);
  pnes_ana->deger_goster();
  pnes_ana->deger_topla();            // sinifana sanal fonksiyonuna erişim.

  cout << endl << "nes_tur değişkeninin siniftur elemanlarına erişimi:" << endl;
  cout << "---------------------------------------------------" << endl;
  nes_tur.deger_ata_tur(85, 294, 571);
  nes_tur.deger_goster_tur();
  pnes_ana = &nes_tur;               // sinifana türünden işaretçi siniftur nesnesinin adresini gösteriyor.
  pnes_ana->deger_topla();           // Burada işaretçinin siniftur fonksiyonuna erişmesinin nedeni fonksiyonun sanal olarak tanımlanması

  cout << endl << "nes_turtur değişkeninin sinifturtur elemanlarına erişimi:" << endl;
  cout << "---------------------------------------------------------" << endl;
  nes_turtur.deger_ata_turtur(164, 1094, 2468);
  nes_turtur.deger_goster_turtur();
  pnes_ana = &nes_turtur;             // sinifana türünden işaretçi sinifturtur nesnesinin adresini gösteriyor.
  pnes_ana->deger_topla();            // Burada işaretçinin sinifturtur fonksiyonuna erişmesinin nedeni fonksiyonun sanal olarak tanımlanması

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

pnes_ana işaretçisi ile nes_ana değişkeninin sinifana elemanlarına erişimi:
---------------------------------------------------------------------------
sinifana değişkenlerine değer atama: 98 391 754
sinifana değişken değerleri: 98 391 754
sinifana değişken toplamları: 1243

nes_tur değişkeninin siniftur elemanlarına erişimi:
---------------------------------------------------
siniftur değişkenlerine değer atama: 85 294 571
siniftur değişken değerleri: 85 294 571
siniftur değişken toplamları: 950

nes_turtur değişkeninin sinifturtur elemanlarına erişimi:
---------------------------------------------------------
sinifturtur değişkenlerine değer atama: 164 1094 2468
sinifturtur değişken değerleri: 164 1094 2468
sinifturtur değişken toplamları: 3726

```

Program, sinifana adlı bir sınıf ve bu sınıftan public olarak türetilen siniftur adlı bir sınıf ve siniftur sınıfından yine public olarak türetilen sinifturtur adlı bir sınıf oluşturur. Her üç sınıf içinde de private, protected ve public olmak üzere üç adet değişken ve bu değişkenlere değer atayan, ekranda gösteren ve değerlerini toplayan üç adet fonksiyon tanımlar.

Program, sinifana türünden pnes\_ana adlı bir işaretçi ve nes\_ana adlı bir nesne ile siniftur türünden nes\_tur adlı ve sinifturtur türünden nes\_turtur adlı bir nesne oluşturur.

İlk olarak, nes\_ana nesnesinin bellek adresini pnes\_ana işaretçisine atar. Bu işaretçi ile, sinifana içindeki deger\_ata() ve deger\_goster() fonksiyonları ile sinifana içindeki değişkenlere birer değer atar ve ekrana yazar. İşaretçi ile deger\_topla() sanal fonksiyonunu kullanarak, sinifana içindeki değişken değerlerini toplar.

İkinci safhada, nes\_tur nesnesinin bellek adresini pnes\_ana işaretçisine atar. Nes\_tur nesnesi yoluyla siniftur içindeki deger\_ata\_tur() ve deger\_goster\_tur() fonksiyonları ile siniftur içindeki değişkenlere birer değer atar ve ekrana yazar. İşaretçi ile siniftur içindeki deger\_topla() sanal fonksiyonunu kullanarak, siniftur içindeki değişken değerlerini toplar.

Son olarak, nes\_turtur nesnesinin bellek adresini pnes\_ana işaretçisine atar. Nes\_turtur nesnesi yoluyla sinifturtur içindeki deger\_ata\_turtur() ve deger\_goster\_turtur() fonksiyonları ile sinifturtur içindeki değişkenlere birer değer atar ve ekrana yazar. İşaretçi ile sinifturtur içindeki deger\_topla() sanal fonksiyonunu kullanarak, sinifturtur içindeki değişken değerlerini toplar.

Programın çalışmasını gösteren şema aşağıdadır:

![](cprog/fonkvirtual03.png)

## Türetilen sınıflarda tanımlanmayan sanal fonksiyonlar

Bir ana sınıf içinde sanal bir fonksiyon bildirimi yapıldıktan sonra, bu ana sınıftan türetilen sınıflardan herhangi birinde sanal fonksiyon tanımı yeniden yapılmayabilir. Bu durumda, içinde sanal fonksiyon tanımı yapılmayan sınıf, kendisinden üst sırada yer alan ve sanal fonksiyon içeren ilk sınıfın sanal fonksiyonunu kullanır.

Çok seviyeli kalıtımda, bir ana sınıftan türetilen bir sınıfı ana sınıf olarak kullanarak diğer bir sınıf türetildiğinde, sıralamada en altta olan ve sanal fonksiyon içermeyen bir sınıfın kullandığı sanal fonksiyonu bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

class sinifana {
  private:
    int priidana;

  protected:
    // Bu değişkenin sinifturtur sınıfında tek kopyası oluşur.
    int proidana;

  public:
    // Buradaki değişken ve fonksiyonların sinifturtur sınıfında tek kopyası oluşur.
    int pubidana;
    // Sanal fonksiyon bildirimi
    virtual void deger_topla(void) {
      cout << "sinifana değişken toplamları: "<< priidana + proidana + pubidana << endl;
    }
    void deger_ata(int pid1, int pid2, int pid3)
    {
      priidana = pid1; proidana = pid2; pubidana = pid3;
      cout << "sinifana değişkenlerine değer atama: " << priidana << " " << proidana << " " << pubidana << endl;
    }
    void deger_goster()
    {
      cout << "sinifana değişken değerleri: " << priidana << " " << proidana << " " << pubidana << endl;
    }
};

class siniftur : public sinifana {
  private:
    int priidtur;

  protected:
    int proidtur;

  public:
    int pubidtur;
    // Sanal fonksiyonun siniftur için yeniden tanımlanması
    virtual void deger_topla(void) {
      cout << "siniftur değişken toplamları: "<< priidtur + proidtur + pubidtur << endl;
    }
    void deger_ata_tur(int pid1, int pid2, int pid3)
    {
      priidtur = pid1; proidtur = pid2; pubidtur = pid3;
      cout << "siniftur değişkenlerine değer atama: " << priidtur << " " << proidtur << " " <<  pubidtur << endl;
    }
    void deger_goster_tur() { cout << "siniftur değişken değerleri: " << priidtur << " " << proidtur << " " << pubidtur << endl; }
};

class sinifturtur : public siniftur {
  private:
    int priidturtur;

  protected:
    int proidturtur;

  public:
    int pubidturtur;
    void deger_ata_turtur(int pid1, int pid2, int pid3)
    {
      priidturtur = pid1; proidturtur = pid2; pubidturtur = pid3;
      cout << "sinifturtur değişkenlerine değer atama: " << priidturtur << " " << proidturtur << " " <<  pubidturtur << endl;
    }
    void deger_goster_turtur() { cout << "sinifturtur değişken değerleri: " << priidturtur << " " << proidturtur << " " << pubidturtur << endl; }
};

int main(void)
{
  sinifana *pnes_ana, nes_ana;
  siniftur nes_tur;
  sinifturtur nes_turtur;

  cout << "pnes_ana işaretçisi ile nes_ana değişkeninin sinifana elemanlarına erişimi:" << endl;
  cout << "---------------------------------------------------------------------------" << endl;
  pnes_ana = &nes_ana;                // sinifana türünden işaretçi sinifana nesnesinin adresini gösteriyor.
  pnes_ana->deger_ata(183, 951, 1185);
  pnes_ana->deger_goster();
  pnes_ana->deger_topla();            // sinifana sanal fonksiyonuna erişim.

  cout << endl << "nes_tur değişkeninin sinifana ve siniftur elemanlarına erişimi:" << endl;
  cout << "---------------------------------------------------------------" << endl;
  nes_tur.deger_ata(347, 9435, 31648);  // sinifana sınıf değişkenlerine değer atar.
  nes_tur.deger_ata_tur(23, 914, 6724); // siniftur sınıf değişkenlerine değer atar.
  nes_tur.deger_goster_tur();
  pnes_ana = &nes_tur;                  // sinifana türünden işaretçi siniftur nesnesinin adresini gösteriyor.
  pnes_ana->deger_topla();              // siniftur fonksiyonunun sanal fonksiyonu çağrılır.

  cout << endl << "nes_turtur değişkeninin sinifana, siniftur ve sinifturtur elemanlarına erişimi:" << endl;
  cout << "-------------------------------------------------------------------------------" << endl;
  nes_turtur.deger_ata(51, 435, 1098);        // sinifana sınıf değişkenlerine değer atar.
  nes_turtur.deger_ata_tur(74, 628, 2045);    // siniftur sınıf değişkenlerine değer atar.
  nes_turtur.deger_ata_turtur(86, 724, 3164);
  nes_turtur.deger_goster_turtur();
  pnes_ana = &nes_turtur;                     // sinifana türünden işaretçi sinifturtur nesnesinin adresini gösteriyor.
  // siniftur sınıfı içinde sanal fonksiyon yeniden tanımlanmadığından, siniftur fonksiyonunun sanal fonksiyonu çağrılır.
  pnes_ana->deger_topla();

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

pnes_ana işaretçisi ile nes_ana değişkeninin sinifana elemanlarına erişimi:
---------------------------------------------------------------------------
sinifana değişkenlerine değer atama: 183 951 1185
sinifana değişken değerleri: 183 951 1185
sinifana değişken toplamları: 2319

nes_tur değişkeninin sinifana ve siniftur elemanlarına erişimi:
---------------------------------------------------------------
sinifana değişkenlerine değer atama: 347 9435 31648
siniftur değişkenlerine değer atama: 23 914 6724
siniftur değişken değerleri: 23 914 6724
siniftur değişken toplamları: 7661

nes_turtur değişkeninin sinifana, siniftur ve sinifturtur elemanlarına erişimi:
-------------------------------------------------------------------------------
sinifana değişkenlerine değer atama: 51 435 1098
siniftur değişkenlerine değer atama: 74 628 2045
sinifturtur değişkenlerine değer atama: 86 724 3164
sinifturtur değişken değerleri: 86 724 3164
siniftur değişken toplamları: 2747

```

Program, sinifana adlı bir sınıf ve bu sınıftan public olarak türetilen siniftur adlı bir sınıf ve siniftur sınıfından yine public olarak türetilen sinifturtur adlı bir sınıf oluşturur. Her üç sınıf içinde de private, protected ve public olmak üzere üç adet değişken ve bu değişkenlere değer atayan, ekranda gösteren iki adet fonksiyon ve sinifana ve siniftur sınıfları içinde değişken değerlerini toplayan birer adet sanal fonksiyon tanımlar.

Program, sinifana türünden pnes\_ana adlı bir işaretçi ve nes\_ana adlı bir nesne ile siniftur türünden nes\_tur adlı ve sinifturtur türünden nes\_turtur adlı bir nesne oluşturur.

İlk olarak, nes\_ana nesnesinin bellek adresini pnes\_ana işaretçisine atar. Bu işaretçi ile, sinifana içindeki deger\_ata() ve deger\_goster() fonksiyonları ile sinifana içindeki değişkenlere birer değer atar ve ekrana yazar. İşaretçi ile deger\_topla() sanal fonksiyonunu kullanarak, sinifana içindeki değişken değerlerini toplar.

İkinci safhada, nes\_tur nesnesini kullanarak sinifana içindeki deger\_ata() fonksiyonu ile sinifana içindeki değişkenlere birer değer atar, siniftur içindeki deger\_ata\_tur() ve deger\_goster\_tur() fonksiyonları ile siniftur içindeki değişkenlere birer değer atar ve ekrana yazar. Sonra, nes\_tur nesnesinin bellek adresini pnes\_ana işaretçisine atar. İşaretçi ile siniftur içindeki deger\_topla() sanal fonksiyonunu kullanarak, siniftur içindeki değişken değerlerini toplar.

Son olarak, nes\_turtur nesnesini kullanarak, sinifana içindeki deger\_ata() fonksiyonu ile sinifana içindeki değişkenlere birer değer atar, siniftur içindeki deger\_ata\_tur() ve deger\_goster\_tur() fonksiyonları ile siniftur içindeki değişkenlere birer değer atar ve sinifturtur içindeki deger\_ata\_turtur() ve deger\_goster\_turtur() fonksiyonları ile sinifturtur içindeki değişkenlere birer değer atar ve ekrana yazar. Sonra, nes\_turtur nesnesinin bellek adresini pnes\_ana işaretçisine atar. İşaretçi ile sinifturtur içindeki deger\_topla() sanal fonksiyonunu kullanarak, sinifturtur içindeki değişken değerlerini toplar.

Programın çalışmasını gösteren şema aşağıdadır:

![](cprog/fonkvirtual04.png)

Yukarıdaki örnekte siniftur sınıfı içindeki deger\_topla() sanal fonksiyonunu kaldırdığımızda, siniftur ve sinifturtur içinde sanal fonksiyon tanımlanmamış olduğundan, her iki sınıf sinifana içindeki deger\_topla() sanal fonksiyonunu kullanacaktır.

Şimdi, örneğimizin değiştirilmiş halini tekrar incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

class sinifana {
  private:
    int priidana;

  protected:
    // Bu değişkenin sinifturtur sınıfında tek kopyası oluşur.
    int proidana;

  public:
    // Buradaki değişken ve fonksiyonların sinifturtur sınıfında tek kopyası oluşur.
    int pubidana;
    // Sanal fonksiyon bildirimi
    virtual void deger_topla(void) {
      cout << "sinifana değişken toplamları: "<< priidana + proidana + pubidana << endl;
    }
    void deger_ata(int pid1, int pid2, int pid3)
    {
      priidana = pid1; proidana = pid2; pubidana = pid3;
      cout << "sinifana değişkenlerine değer atama: " << priidana << " " << proidana << " " << pubidana << endl;
    }
    void deger_goster()
    {
      cout << "sinifana değişken değerleri: " << priidana << " " << proidana << " " << pubidana << endl;
    }
};

class siniftur : public sinifana {
  private:
    int priidtur;

  protected:
    int proidtur;

  public:
    int pubidtur;
    void deger_ata_tur(int pid1, int pid2, int pid3)
    {
      priidtur = pid1; proidtur = pid2; pubidtur = pid3;
      cout << "siniftur değişkenlerine değer atama: " << priidtur << " " << proidtur << " " <<  pubidtur << endl;
    }
    void deger_goster_tur() { cout << "siniftur değişken değerleri: " << priidtur << " " << proidtur << " " << pubidtur << endl; }
};

class sinifturtur : public siniftur {
  private:
    int priidturtur;

  protected:
    int proidturtur;

  public:
    int pubidturtur;
    void deger_ata_turtur(int pid1, int pid2, int pid3)
    {
      priidturtur = pid1; proidturtur = pid2; pubidturtur = pid3;
      cout << "sinifturtur değişkenlerine değer atama: " << priidturtur << " " << proidturtur << " " <<  pubidturtur << endl;
    }
    void deger_goster_turtur() { cout << "sinifturtur değişken değerleri: " << priidturtur << " " << proidturtur << " " << pubidturtur << endl; }
};

int main(void)
{
  sinifana *pnes_ana, nes_ana;
  siniftur nes_tur;
  sinifturtur nes_turtur;

  cout << "pnes_ana işaretçisi ile nes_ana değişkeninin sinifana elemanlarına erişimi:" << endl;
  cout << "---------------------------------------------------------------------------" << endl;
  pnes_ana = &nes_ana;                // sinifana türünden işaretçi sinifana nesnesinin adresini gösteriyor.
  pnes_ana->deger_ata(183, 951, 1185);
  pnes_ana->deger_goster();
  pnes_ana->deger_topla();            // sinifana sanal fonksiyonuna erişim.

  cout << endl << "nes_tur değişkeninin sinifana ve siniftur elemanlarına erişimi:" << endl;
  cout << "---------------------------------------------------------------" << endl;
  nes_tur.deger_ata(347, 9435, 31648);  // sinifana sınıf değişkenlerine değer atar.
  nes_tur.deger_ata_tur(23, 914, 6724); // siniftur sınıf değişkenlerine değer atar.
  nes_tur.deger_goster_tur();
  pnes_ana = &nes_tur;                  // sinifana türünden işaretçi siniftur nesnesinin adresini gösteriyor.
  pnes_ana->deger_topla();              // sinifana fonksiyonunun sanal fonksiyonu çağrılır.

  cout << endl << "nes_turtur değişkeninin sinifana, siniftur ve sinifturtur elemanlarına erişimi:" << endl;
  cout << "-------------------------------------------------------------------------------" << endl;
  nes_turtur.deger_ata(51, 435, 1098);        // sinifana sınıf değişkenlerine değer atar.
  nes_turtur.deger_ata_tur(74, 628, 2045);    // siniftur sınıf değişkenlerine değer atar.
  nes_turtur.deger_ata_turtur(86, 724, 3164);
  nes_turtur.deger_goster_turtur();
  pnes_ana = &nes_turtur;                     // sinifana türünden işaretçi sinifturtur nesnesinin adresini gösteriyor.
  pnes_ana->deger_topla();                    // sinifana fonksiyonunun sanal fonksiyonu çağrılır.

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

pnes_ana işaretçisi ile nes_ana değişkeninin sinifana elemanlarına erişimi:
---------------------------------------------------------------------------
sinifana değişkenlerine değer atama: 183 951 1185
sinifana değişken değerleri: 183 951 1185
sinifana değişken toplamları: 2319

nes_tur değişkeninin sinifana ve siniftur elemanlarına erişimi:
---------------------------------------------------------------
sinifana değişkenlerine değer atama: 347 9435 31648
siniftur değişkenlerine değer atama: 23 914 6724
siniftur değişken değerleri: 23 914 6724
sinifana değişken toplamları: 41430

nes_turtur değişkeninin sinifana, siniftur ve sinifturtur elemanlarına erişimi:
-------------------------------------------------------------------------------
sinifana değişkenlerine değer atama: 51 435 1098
siniftur değişkenlerine değer atama: 74 628 2045
sinifturtur değişkenlerine değer atama: 86 724 3164
sinifturtur değişken değerleri: 86 724 3164
sinifana değişken toplamları: 1584

```

Program, sinifana adlı bir sınıf ve bu sınıftan public olarak türetilen siniftur adlı bir sınıf ve siniftur sınıfından yine public olarak türetilen sinifturtur adlı bir sınıf oluşturur. Her üç sınıf içinde de private, protected ve public olmak üzere üç adet değişken ve bu değişkenlere değer atayan, ekranda gösteren iki adet fonksiyon ve sinifana ve siniftur sınıfları içinde değişken değerlini toplayan birer adet sanal fonksiyon tanımlar.

Program, sinifana türünden pnes\_ana adlı bir işaretçi ve nes\_ana adlı bir nesne ile siniftur türünden nes\_tur adlı ve sinifturtur türünden nes\_turtur adlı bir nesne oluşturur.

İlk olarak, nes\_ana nesnesinin bellek adresini pnes\_ana işaretçisine atar. Bu işaretçi ile, sinifana içindeki deger\_ata() ve deger\_goster() fonksiyonları ile sinifana içindeki değişkenlere birer değer atar ve ekrana yazar. İşaretçi ile deger\_topla() sanal fonksiyonunu kullanarak, sinifana içindeki değişken değerlerini toplar.

İkinci safhada, nes\_tur nesnesini kullanarak sinifana içindeki deger\_ata() fonksiyonu ile sinifana içindeki değişkenlere birer değer atar, siniftur içindeki deger\_ata\_tur() ve deger\_goster\_tur() fonksiyonları ile siniftur içindeki değişkenlere birer değer atar ve ekrana yazar. Sonra, nes\_tur nesnesinin bellek adresini pnes\_ana işaretçisine atar. İşaretçi ile sinifana içindeki deger\_topla() sanal fonksiyonunu kullanarak, siniftur içindeki değişken değerlerini toplar.

Son olarak, nes\_turtur nesnesini kullanarak, sinifana içindeki deger\_ata() fonksiyonu ile sinifana içindeki değişkenlere birer değer atar, siniftur içindeki deger\_ata\_tur() ve deger\_goster\_tur() fonksiyonları ile siniftur içindeki değişkenlere birer değer atar ve sinifturtur içindeki deger\_ata\_turtur() ve deger\_goster\_turtur() fonksiyonları ile sinifturtur içindeki değişkenlere birer değer atar ve ekrana yazar. Sonra, nes\_turtur nesnesinin bellek adresini pnes\_ana işaretçisine atar. İşaretçi ile sinifturtur içindeki deger\_topla() sanal fonksiyonunu kullanarak, sinifturtur içindeki değişken değerlerini toplar.

Sanal fonksiyon tanımlaması sadece sinifana sınıfı içinde yapıldığından, siniftur ve sinifturtur sınıflarından oluşturulan nesneler sanal fonksiyon çağrısı yaptıklarında sinifana sınıfı içindeki sanal fonksiyon devreye girer.

Programın çalışmasını gösteren şema aşağıdadır:

![](cprog/fonkvirtual05.png)

## Saf sanal fonksiyonlar

Bir ana sınıf içinde kod bloğu içermeyecek ve bildirim satırında 0 değerine eşit olacak şekilde bildirimi yapılan sanal fonksiyonlara saf sanal fonksiyon adı verilir. Saf sanal fonksiyonların bildirimi aşağıdaki şekilde yapılır:

```

class ana-sınıf {
  public:
    virtual veri-türü fonk-adı(parametreler) = 0;
}

class türetilen-sınıf public: ana-sınıf {
  public:
    veri-türü fonk-adı(parametreler)
    {
      // kod bloğu   
    }
}

```

* Bir sınıf içinde en az bir adet saf sanal fonksiyon tanımlanırsa, bu sınıf soyut (abstract) sınıf haline gelir. Soyut sınıflardan nesne oluşturulamaz.
* Saf sanal fonksiyon bulunan ana sınıflardan türetilen sınıflarda sanal fonksiyon yeniden tanımlanmadığında, türetilen sınıf soyut sınıf olarak kabul edildiğinden, bu sınıflardan nesne oluşturulamaz.
* Soyut sınıflardan nesne oluşturulmaz, ancak işaretçi ve referans oluşturulabilir.
* Bir sınıf içinde saf sanal fonksiyon tanımlandığında, bu sınıftan türetilen tüm sınıflarda sanal fonksiyon bildirimi yeniden yapılmalıdır. Eğer yapılmazsa, türetilen sınıflarda soyut sınıf olarak kabul edilir.
* Soyut sınıflar saf sanal fonksiyon dışında normal fonksiyonlar ve değişkenler içerebilir.

Şimdi, saf sanal fonksiyon kullanımını bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

class sinifana {
  private:
    int priidana;

  protected:
    // Bu değişkenin sinifturtur sınıfında tek kopyası oluşur.
    int proidana;

  public:
    // Buradaki değişken ve fonksiyonların sinifturtur sınıfında tek kopyası oluşur.
    int pubidana;
    // Saf sanal fonksiyon bildirimi
    virtual void deger_topla(void) = 0;
    void deger_ata(int pid1, int pid2, int pid3)
    {
      priidana = pid1; proidana = pid2; pubidana = pid3;
      cout << "sinifana değişkenlerine değer atama: " << priidana << " " << proidana << " " << pubidana << endl;
    }
    void deger_goster()
    {
      cout << "sinifana değişken değerleri: " << priidana << " " << proidana << " " << pubidana << endl;
    }
};

class siniftur1 : public sinifana {
  private:
    int priidtur1;

  protected:
    int proidtur1;

  public:
    int pubidtur1;
    // Sanal fonksiyonun siniftur1 için yeniden tanımlanması
    void deger_topla(void) {
      cout << "siniftur1 değişken toplamları: "<< priidtur1 + proidtur1 + pubidtur1 << endl;
    }
    void deger_ata_tur1(int pid1, int pid2, int pid3)
    {
      priidtur1 = pid1; proidtur1 = pid2; pubidtur1 = pid3;
      cout << "siniftur1 değişkenlerine değer atama: " << priidtur1 << " " << proidtur1 << " " <<  pubidtur1 << endl;
    }
    void deger_goster_tur1() { cout << "siniftur1 değişken değerleri: " << priidtur1 << " " << proidtur1 << " " << pubidtur1 << endl; }
};

class siniftur2 : public sinifana {
  private:
    int priidtur2;

  protected:
    int proidtur2;

  public:
    int pubidtur2;
    // Sanal fonksiyonun siniftur2 için yeniden tanımlanması
    void deger_topla(void) {
      cout << "siniftur2 değişken toplamları: "<< priidtur2 + proidtur2 + pubidtur2 << endl;
    }
    void deger_ata_tur2(int pid1, int pid2, int pid3)
    {
      priidtur2 = pid1; proidtur2 = pid2; pubidtur2 = pid3;
      cout << "siniftur2 değişkenlerine değer atama: " << priidtur2 << " " << proidtur2 << " " <<  pubidtur2 << endl;
    }
    void deger_goster_tur2() { cout << "siniftur2 değişken değerleri: " << priidtur2 << " " << proidtur2 << " " << pubidtur2 << endl; }
};

int main(void)
{
  sinifana *pnes_ana;
  siniftur1 nes_tur1;
  siniftur2 nes_tur2;

  cout << "nes_tur1 değişkeninin siniftur1 elemanlarına erişimi:" << endl;
  cout << "-----------------------------------------------------" << endl;
  nes_tur1.deger_ata_tur1(249, 587, 1087);
  nes_tur1.deger_goster_tur1();
  pnes_ana = &nes_tur1;    // sinifana türünden işaretçi siniftur1 nesnesinin adresini gösteriyor.
  pnes_ana->deger_topla(); // siniftur1 sanal fonksiyonu çağrılır.

  cout << endl << "nes_tur2 değişkeninin siniftur2 elemanlarına erişimi:" << endl;
  cout << "-----------------------------------------------------" << endl;
  nes_tur2.deger_ata_tur2(725, 1945, 3154);
  nes_tur2.deger_goster_tur2();
  pnes_ana = &nes_tur2;    // sinifana türünden işaretçi siniftur2 nesnesinin adresini gösteriyor.
  pnes_ana->deger_topla(); // siniftur2 sanal fonksiyonu çağrılır.

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

nes_tur1 değişkeninin siniftur1 elemanlarına erişimi:
-----------------------------------------------------
siniftur1 değişkenlerine değer atama: 249 587 1087
siniftur1 değişken değerleri: 249 587 1087
siniftur1 değişken toplamları: 1923

nes_tur2 değişkeninin siniftur2 elemanlarına erişimi:
-----------------------------------------------------
siniftur2 değişkenlerine değer atama: 725 1945 3154
siniftur2 değişken değerleri: 725 1945 3154
siniftur2 değişken toplamları: 5824

```

Program, sinifana adlı bir sınıf ve bu sınıftan public olarak türetilen siniftur1 ve siniftur2 adlı iki adet sınıf oluşturur. Her üç sınıf içinde de private, protected ve public olmak üzere üç adet değişken ve bu değişkenlere değer atayan, ekranda gösteren ve değerlerini toplayan üç adet fonksiyon tanımlar.

Program, sinifana türünden pnes\_ana adlı bir işaretçi ile siniftur1 türünden nes\_tur1 adlı ve siniftur2 türünden nes\_tur2 adlı bir nesne oluşturur.

İlk olarak, nes\_tur1 nesnesi yoluyla siniftur1 içindeki deger\_ata\_tur1() ve deger\_goster\_tur1() fonksiyonları ile siniftur1 içindeki değişkenlere birer değer atar ve ekrana yazar. Sonra, nes\_tur1 nesnesinin bellek adresini pnes\_ana işaretçisine atar. İşaretçi ile siniftur1 içindeki deger\_topla() sanal fonksiyonunu kullanarak, siniftur1 içindeki değişken değerlerini toplar.

İkinci safhada, nes\_tur2 nesnesi yoluyla siniftur1 içindeki deger\_ata\_tur2() ve deger\_goster\_tur2() fonksiyonları ile siniftur2 içindeki değişkenlere birer değer atar ve ekrana yazar. Sonra, nes\_tur2 nesnesinin bellek adresini pnes\_ana işaretçisine atar. İşaretçi ile siniftur2 içindeki deger\_topla() sanal fonksiyonunu kullanarak, siniftur2 içindeki değişken değerlerini toplar.

Programda, sinifana sınıfı saf sanal fonksiyon tanımlaması ile soyut hale geldiğinden, sinifana türünden nesne oluşturulamaz, ancak işaretçi oluşturulabilir.

Programın çalışmasını gösteren şema aşağıdadır:

![](/public/images/cppprog/fonkvirtual06.png)
 