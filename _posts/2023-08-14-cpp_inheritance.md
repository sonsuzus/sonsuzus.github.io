---
title:  C++ Kalıtım
author: sonsuz
date: 2023-08-14 11:53:32 +0300
categories: [Program,C++]
tags: [cpp,programlama,nesne,oop,sınıf,class,kalıtım]
---




Kalıtım nesneye yönelik programlamanın en önemli özelliklerinden biridir. Kalıtım bir nesneden türetilen bir nesnenin türetildiği nesnenin tüm özelliklerine sahip olmasıdır.

Kalıtım, nesneye yönelik programlamada mevcut bir sınıf içinde bulunan veri ve metotların bu sınıftan türetilen alt sınıflar içinde kullanılması olarak tanımlanabilir.

Kendisinden türetme yapılan sınıf ana, ebeveyn veya süper sınıf olarak, türetilen sınıflar ise çocuk, alt veya uzantı sınıf olarak isimlendirilir.

Bir ana sınıftan bir sınıf türetildiğinde, ana sınıfta yer alan tüm veri ve metotlar türetilen sınıf tarafından kullanılabileceği gibi, türetilen sınıf içinde de yeni veri ve metotlar tanımlanabilir. Eğer ihtiyaç duyulursa, ana sınıftan devralınan metotlar yeniden tanımlanır (overriding) ve aynı isim altında farklı kodlar yazılır.

Ana sınıftan bir alt sınıf türeterek, ana sınıfta yer alan veri ve metotların devralınması, devralınan metotlar için yeniden kod yazmaya gerek duymadan, ana sınıf içinde yer alan veri ve metotları kullanmaya olanak sağlar.

> Öncelikle bir ana sınıf tanımlaması yapılmalıdır. Ana sınıf tanımlaması yapılırken, bu sınıftan üretilecek olan sınıfların ortak olarak sahip olacağı ve birlikte kullanacağı özellikleri gösteren değişkenlerin tamamının bildirimi ana sınıf içinde yapılmalıdır. Ana sınıftan türetilen alt sınıfların sadece kendileri tarafından kullanılacak özellikleri gösteren değişkenlerin bildirimi ise türetilen alt sınıfların içinde yapılmalıdır.
{: .prompt-tip }

Ana sınıftan türetilen alt sınıflardan da alt sınıflar türetilerek çoklu kalıtım özelliği kullanılabilir.

## Ana sınıf erişim kontrolü

Bir sınıf ana sınıf olarak kabul edilerek bu sınıftan bir sınıf türetildiğinde, ana sınıf içinde yer alan tüm elemanlar (değişken ve fonksiyonlar) türetilen sınıfın üyesi haline gelir. C++ dilinde, bu işlemi gerçekleştirmek için aşağıda gösterilen genel yapı kullanılır:

```

class türetilen-sınıf : erişim-türü ana-sınıf {
  // Türetilen sınıf içeriği 
}

```

Türetilen sınıf içinden ana sınıf elemanlarına erişim durumu erişim-türü değeri ile belirlenir.

erişim-türü ifadesinin kullanımı isteğe bağlıdır. Kullanıldığında, aşağıdaki değerlerden birini almalıdır:

private:

protected:

public:

Eğer ana sınıftan bir alt sınıf türetilirken, erişim-türü ifadesi kullanılmazsa, bu değer ön tanımlı olarak private olacaktır.

Ana sınıf elemanlarına erişim koşulları

Ana sınıf elemanlarına kendi içinden, türetilmiş sınıftan ve sınıflar dışında kalan program kodlarından erişim yetkisini gösteren tablo aşağıdadır.

![](cprog/elemaneri.png)

Kalıtım türüne göre ana sınıf elemanlarının türetilen sınıf içindeki durumu

Kalıtım türüne göre ana sınıf elemanlarının türetilen sınıf içindeki durumunu gösteren tablo aşağıdadır:

![](cprog/inheritdeg.png)

## Public kalıtım

Bir ana sınıftan public olarak bir sınıf türetildiğinde, ana sınıfın tüm public elemanları türetilmiş sınıfın public elemanı ve ana sınıfın tüm protected elemanları türetilmiş sınıfın protected elemanı haline gelir. Ana sınıfın private elemanları ise, ana sınıfa özel kalır ve türetilmiş sınıfın elemanları tarafından erişilemez.

![](cprog/inhpublic01.png)

Public kalıtım işleminde, ana sınıfın tüm public elemanlarının türetilen sınıfın public elemanları olarak işlem göreceğini ve tıpkı türetilen sınıf içinde tanımlanmış değişkenler gibi, türetilen sınıf içinde yer alan üye fonksiyonlar tarafından erişim sağlanabileceğini gösterir. Bu durumda, ana sınıfın tüm protected elemanları türetilen sınıfın protected elemanları olarak işlem görecektir. Ancak, türetilen sınıf içinde yer alan üye fonksiyonlar ana sınıfın private elemanlarına direk olarak erişim sağlayamazlar.

> C++'da, bir sınıf elemanı protected olarak tanımlandığında, bu elemana sınıfın diğer elemanlarının yanısıra, bu sınıftan türetilen sınıfın elemanları da erişebilir. Başka bir ifade ile; bir sınıf içinde protected olarak tanımlanmış elemanlara sadece bu sınıftan türetilmiş sınıflar erişim sağlayabilir. Bu özellik, private ve protected olarak tanınmlanmış elemanların farkını göstermektedir.
{: .prompt-tip }

Şimdi, bir ana sınıftan public olarak türetilen bir sınıf ve her iki sınıfa ait nesnelerle yapılan işlemleri bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

class sinifana {
  private:
    // Bu değişkene sadece sinifana içindeki fonksiyonlar erişim sağlayabilir.
    int priidana;

  protected:
    // Bu değişkene sinifana içindeki fonksiyonlar ile sinifana sınıfından türetilmiş sınıf fonksiyonları erişim sağlayabilir.
    int proidana;

  public:
    // Bu değişkene sinifana içindeki fonksiyonlar ve sinifana sınıfından türetilmiş sınıf fonksiyonları ile
    // sinifana türünden ve türetilmiş sınıf türünden oluşturulmuş nesneler doğrudan erişim sağlayabilir.
    int pubidana;
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
    // Türetilen sınıf içindeki fonksiyonlar direk olarak
    // ana sınıfın public ve protected değişkenlerine erişim sağlayabilir.
    void deger_ata_tur(int pid1, int pid2)
    {
      priidtur = proidana + pubidana; proidtur = pid1; pubidtur = pid2;
      cout << "siniftur değişkenlerine değer atama: " << priidtur << " " << proidtur << " " <<  pubidtur << endl;
    }
    void deger_goster_tur() { cout << "siniftur değişken değerleri: " << priidtur << " " << proidtur << " " << pubidtur << endl; }
};

int main(void)
{
  sinifana nes_ana;

  cout << "nes_ana değişkeninin sinifana elemanlarına erişimi:" << endl;
  cout << "---------------------------------------------------" << endl;
  nes_ana.deger_ata(7, 21, 165);
  nes_ana.deger_goster();

  // nes_ana.priidana = 954;  // Derleme hatası verir (Nesne sınıf içindeki private değişkene doğrudan erişim sağlayamaz).
  // nes_ana.proidana = 954;  // Derleme hatası verir (Nesne sınıf içindeki protected değişkene doğrudan erişim sağlayamaz).
  nes_ana.pubidana = 954;     // Nesne sınıf içindeki public değişkene doğrudan erişim sağlar.

  nes_ana.deger_goster();

  siniftur nes_tur;

  cout << endl << "nes_tur değişkeninin sinifana elemanlarına doğrudan erişimi:" << endl;
  cout << "------------------------------------------------------------" << endl;
  // siniftur sınıfından oluşturulan nesne, sinifana sınıfı fonksiyonları yoluyla
  // sinifana sınıfı değişkenlerine değer atar ve ekrana yazar.
  
  nes_tur.deger_ata(8, 25, 246);
  nes_tur.deger_goster();

  // nes_tur.priidana = 741;  // Derleme hatası verir (Türetilen sınıf nesnesi ana sınıf içindeki private değişkene doğrudan erişim sağlayamaz).
  // nes_tur.proidana = 741;  // Derleme hatası verir (Türetilen sınıf nesnesi ana sınıf içindeki protected değişkene doğrudan erişim sağlayamaz).
  nes_tur.pubidana = 741;     // siniftur sınıfından oluşturulan nes_tur nesnesi ana sınıf içindeki public değişkene doğrudan erişim sağlar.

  nes_tur.deger_goster();

  cout << endl << "nes_tur değişkeninin sinifana ve siniftur elemanlarına erişimi:" << endl;
  cout << "---------------------------------------------------------------" << endl;
  // siniftur sınıfından oluşturulan nesne, kendi fonksiyonları yoluyla sinifana sınıfının
  // protected ve public değişkenlerine erişim sağlayarak kendi değişkenlerine değer atar ve ekrana yazar.
  nes_tur.deger_ata_tur(12, 34);
  nes_tur.deger_goster_tur();

  nes_tur.pubidtur = 687;

  nes_tur.deger_goster_tur();

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

nes_ana değişkeninin sinifana elemanlarına erişimi:
---------------------------------------------------
sinifana değişkenlerine değer atama: 7 21 165
sinifana değişken değerleri: 7 21 165
sinifana değişken değerleri: 7 21 954

nes_tur değişkeninin sinifana elemanlarına doğrudan erişimi:
------------------------------------------------------------
sinifana değişkenlerine değer atama: 8 25 246
sinifana değişken değerleri: 8 25 246
sinifana değişken değerleri: 8 25 741

nes_tur değişkeninin sinifana ve siniftur elemanlarına erişimi:
---------------------------------------------------------------
siniftur değişkenlerine değer atama: 766 12 34
siniftur değişken değerleri: 766 12 34
siniftur değişken değerleri: 766 12 687

```

Program, sinifana adlı bir sınıf ve bu sınıftan public olarak türetilen siniftur adlı bir sınıf oluşturur. Her iki sınıf içinde de private, protected ve public olmak üzere üç adet değişken ve bu değişkenlere değer atayan ve ekranda gösteren iki adet fonksiyon tanımlar.

Program çalışmaya başladığında, sinifana cinsinden bir nesne tanımlar. Ana sınıf nesnesi yoluyla, ana sınıf fonksiyonlarını çağırarak, önce ana sınıf içindeki değişkenlere birer değer atar sonra değişken değerlerini ekrana yazar. Ana sınıf nesnesini kullanarak doğrudan ana sınıf içinde public pubidana değişkenine bir değer atar ve ana sınıf içindeki deger\_goster() fonksiyonu ile değişken değerlerini tekrar ekrana yazar.

Program, ikinci safhada türetilmiş sınıf olan siniftur türünden nes\_tur adlı bir nesne oluşturur. Bu nesne yoluyla ana sınıf içindeki fonksiyonlara erişim sağlayarak, önce ana sınıf içindeki değişkenlere birer değer atar sonra değişken değerlerini ekrana yazar. Aynı nesne ile doğrudan ana sınıf içinde public pubidana değişkenine bir değer atar ve ana sınıf içindeki deger\_goster() fonksiyonu ile değişken değerlerini tekrar ekrana yazar.

Sonra, aynı nesne ile, türetilen sınıf içindeki deger\_ata\_tur() fonksiyonu ile sinifana sınıfının protected ve public değişkenlerine erişim sağlayarak, bu değişkenlerin toplamını, priidtur değişkenine atar. Aynı fonksiyon ile proidtur ve pubidtur değişkenlerine de birer değer atar. Türetilmiş siniftur sınıfı içindeki değişken değerlerini ekrana yazar. Aynı nesne ile doğrudan pubidtur değişkenine bir değer atar ve deger\_goster\_tur() fonksiyonu ile değişken değerlerini tekrar ekrana yazar.

Programda oluşturulan sınıfların içindeki elemanlar ile bu sınıflardan oluşturulan nesnelerin erişim durumlarını gösteren şema aşağıdadır:

![](cprog/inhpublic02.png)

Bir ana sınıftan public olarak türetilen bir sınıftan yine public olarak diğer bir sınıf türetildiğinde, ikinci türetilen sınıf elemanları ile bu sınıftan oluşturulan nesnelerin ana sınıf ile ana sınıftan ilk türetilen sınıfın elemanlarına erişim durumunu bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

class sinifana {
  private:
    // Bu değişkene sadece sinifana içindeki fonksiyonlar erişim sağlayabilir.
    int priidana;

  protected:
    // Bu değişkene sinifana içindeki fonksiyonlar ile sinifana sınıfından türetilmiş sınıf fonksiyonları erişim sağlayabilir.
    int proidana;

  public:
    // Bu değişkene sinifana içindeki fonksiyonlar ve sinifana sınıfından türetilmiş sınıf fonksiyonları ile
    // sinifana türünden ve türetilmiş sınıf türünden oluşturulmuş nesneler doğrudan erişim sağlayabilir.
    int pubidana;
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
    // Türetilen sınıf içindeki fonksiyonlar direk olarak
    // ana sınıfın public ve protected değişkenlerine erişim sağlayabilir.
    void deger_ata_tur(int pid1, int pid2)
    {
      priidtur = proidana + pubidana; proidtur = pid1; pubidtur = pid2;
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
    // Türetilen sınıftan türetilen sınıf içindeki fonksiyonlar direk olarak
    // ana sınıfın public ve protected değişkenlerine erişim sağlayabilir.
    void deger_ata_turtur(void)
    {
      priidturtur = proidana + pubidana; proidturtur = proidtur*2; pubidturtur = pubidtur*2;
      cout << "sinifturtur değişkenlerine değer atama: " << priidturtur << " " << proidturtur << " " << pubidturtur << endl;
    }
    void deger_goster_turtur() { cout << "sinifturtur değişken değerleri: " << priidturtur << " " << proidturtur << " " << pubidturtur << endl; }
};

int main(void)
{
  sinifturtur nes_turtur;

  // sinifturtur sınıfından oluşturulan nesne, sinifana sınıfı fonksiyonları yoluyla
  // sinifana sınıfı değişkenlerine değer atar ve ekrana yazar.
  cout << "nes_turtur değişkeninin sinifana elemanlarına erişimi:" << endl;
  cout << "------------------------------------------------------" << endl;
  nes_turtur.deger_ata(78, 121, 375);
  nes_turtur.deger_goster();

  nes_turtur.pubidana = 1765; // İkinci türetilen sınıf nesnesi ana sınıf içindeki public değişkene doğrudan erişim sağlar.

  nes_turtur.deger_goster();  // sinifana fonksiyonuna erişim

  // sinifturtur sınıfından oluşturulan nesne, siniftur sınıfı fonksiyonları yoluyla
  // sinifana ve sinifturtur sınıflarının protected ve public değişkenlerine erişim
  // sağlayarak siniftur sınıfı değişkenlerine değer atar ve ekrana yazar.
  cout << endl << "nes_turtur değişkeninin siniftur elemanlarına erişimi:" << endl;
  cout << "------------------------------------------------------" << endl;
  nes_turtur.deger_ata_tur(82, 217);
  nes_turtur.deger_goster_tur();

  nes_turtur.pubidtur = 4257;    // İkinci türetilen sınıf nesnesi ilk türetilen sınıf içindeki public değişkene doğrudan erişim sağlar.

  nes_turtur.deger_goster_tur(); // İkinci türetilen sınıf fonksiyonuna erişim

  // sinifturtur sınıfından oluşturulan nesne, kendi fonksiyonları yoluyla sinifana ve sinifturtur sınıflarının
  // protected ve public değişkenlerine erişim sağlayarak kendi değişkenlerine değer atar ve ekrana yazar.
  cout << endl << "nes_turtur değişkeninin sinifturtur elemanlarına erişimi:" << endl;
  cout << "---------------------------------------------------------" << endl;
  nes_turtur.deger_ata_turtur();
  nes_turtur.deger_goster_turtur();

  nes_turtur.pubidturtur = 6321; // İkinci türetilen sınıf nesnesi kendi içindeki public değişkene doğrudan erişim sağlar.

  nes_turtur.deger_goster_turtur();

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

nes_turtur değişkeninin sinifana elemanlarına erişimi:
------------------------------------------------------
sinifana değişkenlerine değer atama: 78 121 375
sinifana değişken değerleri: 78 121 375
sinifana değişken değerleri: 78 121 1765

nes_turtur değişkeninin siniftur elemanlarına erişimi:
------------------------------------------------------
siniftur değişkenlerine değer atama: 1886 82 217
siniftur değişken değerleri: 1886 82 217
siniftur değişken değerleri: 1886 82 4257

nes_turtur değişkeninin sinifturtur elemanlarına erişimi:
---------------------------------------------------------
sinifturtur değişkenlerine değer atama: 1886 164 8514
sinifturtur değişken değerleri: 1886 164 8514
sinifturtur değişken değerleri: 1886 164 6321

```

Program, sinifana adlı bir sınıf ve bu sınıftan public olarak türetilen siniftur adlı bir sınıf ve siniftur sınıfından yine public olarak türetilen sinifturtur adlı bir sınıf oluşturur. Her üç sınıf içinde de private, protected ve public olmak üzere üç adet değişken ve bu değişkenlere değer atayan ve ekranda gösteren iki adet fonksiyon tanımlar.

Program çalışmaya başladığında, sinifturtur sınıfı türünden nes\_turtur adlı bir nesne oluşturur. Bu nesne yoluyla ana sınıf içindeki fonksiyonlara erişim sağlayarak, önce ana sınıf içindeki değişkenlere birer değer atar sonra değişken değerlerini ekrana yazar. Aynı nesne ile doğrudan ana sınıf içinde public pubidana değişkenine bir değer atar ve ana sınıf içindeki deger\_goster() fonksiyonu ile değişken değerlerini tekrar ekrana yazar.

Sonra, aynı nesne ile, ilk türetilen sınıf içindeki deger\_ata\_tur() fonksiyonu ile sinifana sınıfının protected ve public değişkenlerine erişim sağlayarak, bu değişkenlerin toplamını, priidtur değişkenine atar. Aynı fonksiyon ile proidtur ve pubidtur değişkenlerine de birer değer atar. Son olarak, siniftur sınıfı içindeki değişken değerlerini ekrana yazar.

Daha sonra, aynı nesne ile, kendi sınıfı içindeki deger\_ata\_turtur() fonksiyonu ile sinifana ve siniftur sınıflarının protected ve public değişkenlerine erişim sağlayarak, ana sınıf değişkenlerinin toplamını priidturtur değişkenine, siniftur içindeki poridtur değişkeninin iki katını proidturtur değişkenine ve pubidtur değişkeninin iki katını pubidturtur değişkenine atar. Son olarak, sinifturtur sınıfı içindeki değişken değerlerini ekrana yazar.

Programda oluşturulan sınıfların içindeki elemanlar ile bu sınıflardan oluşturulan nesnelerin erişim durumlarını gösteren şema aşağıdadır:

![](cprog/inhpublic03.png)

## Private kalıtım

Bir ana sınıftan private erişim türü kullanılarak bir sınıf türetildiğinde, ana sınıfın tüm public ve protected elemanları türetilen sınıfın private elemanları olarak işlem görür.

![](cprog/inhprivate01.png)

> Private kalıtım ile türetilen bir sınıftan oluşturulan nesneler, doğrudan veya ana sınıf içinde bulunan public fonksiyonları kullanarak ana sınıf protected ve public değişkenlerine erişim sağlayamazlar. Ana sınıf protected ve public değişkenlerine erişim sağlamak için sadece kendi fonksiyonlarını kullanabilirler.
{: .prompt-tip }

> Private olarak türetilmiş sınıfa ait nesneler ana sınıfın hiçbir elemanına doğrudan erişemezler.
{: .prompt-danger }

> Bir ana sınıftan diğer bir sınıf türetildiğinde private değeri kullanılırsa, türetilen sınıftan oluşturulan nesneler, ana sınıf içinde bulunan public fonksiyonları kullanarak da olsa, ana sınıf public değişkenlerine erişim sağlayamazlar.
{: .prompt-warning }

Örnek

```c++
#include <iostream>

using namespace std;

class sinifana {
  private:
    // Bu değişkene sadece sinifana içindeki fonksiyonlar erişim sağlayabilir.
    int priidana;

  protected:
    // Bu değişkene sinifana ve siniftur içindeki fonksiyonlar erişim sağlayabilir.
    int proidana;

  public:
    // Bu değişkene sinifana içindeki fonksiyonlar ve sinifana türünden oluşturulmuş nesneler ile
    // siniftur içindeki fonksiyonlar doğrudan erişim sağlayabilir.
    int pubidana;
    void deger_ata(int pid1, int pid2, int pid3)
    {
      priidana = pid1; proidana = pid2; pubidana = pid3;
      cout << "sinifana değişkenlerine değer atama: " << priidana << " " << proidana << " " << pubidana << endl;
    }
    void deger_goster() { cout << "sinifana değişken değerleri: " << priidana << " " << proidana << " " << pubidana << endl; }
};

class siniftur : private sinifana {
  private:
    int priidtur;

  protected:
    int proidtur;

  public:
    int pubidtur;
    // Türetilen sınıf içindeki fonksiyonlar direk olarak
    // sadece türetilen sınıf değişkenlerine erişim sağlayabilir.
    void deger_ata_tur(int pid1, int pid2, int pid3, int pid4, int pid5)
    {
      proidana = pid1; pubidana = pid2;                  // Ana sınıf değişkenlerine değer atama
      priidtur = pid3; proidtur = pid4; pubidtur = pid5; // Türetilen sınıf değişkenlerine değer atama
      cout << "sinifana değişkenlerine değer atama: " << proidana << " " << pubidana << endl;
      cout << "siniftur değişkenlerine değer atama: " << priidtur << " " << proidtur << " " <<  pubidtur << endl;
    }
    void deger_goster_tur()
    {
      cout << "sinifana değişken değerleri: " << proidana << " " << pubidana << " " << endl;
      cout << "siniftur değişken değerleri: " <<  priidtur << " " << proidtur << " " << pubidtur << endl;
    }
};

int main(void)
{
  sinifana nes_ana;

  cout << "nes_ana değişkeninin sinifana elemanlarına erişimi:" << endl;
  cout << "---------------------------------------------------" << endl;
  nes_ana.deger_ata(7, 21, 165);
  nes_ana.deger_goster();

  // nes_ana.priidana = 954; // Derleme hatası verir (Nesne sınıf içindeki private değişkene doğrudan erişim sağlayamaz).
  // nes_ana.proidana = 954; // Derleme hatası verir (Nesne sınıf içindeki protected değişkene doğrudan erişim sağlayamaz).
  nes_ana.pubidana = 954;    // Nesne sınıf içindeki public değişkene doğrudan erişim sağlar.

  nes_ana.deger_goster();

  siniftur nes_tur;

  cout << endl << "nes_tur değişkeninin sinifana elemanlarına doğrudan erişimi:" << endl;
  cout << "------------------------------------------------------------" << endl;
  // siniftur sınıfından oluşturulan nesne, sinifana sınıfı fonksiyonları yoluyla
  // sinifana sınıfı değişkenlerine değer atayamaz ve ekrana yazamaz.
  // nes_tur.deger_ata(8, 25, 246); // public kalıtımda normal çalışır, private kalıtımda derleme hatası verir.
  // nes_tur.deger_goster();        // public kalıtımda normal çalışır, private kalıtımda derleme hatası verir.

  // Türetilen sınıf nesnesi ana sınıf içindeki private ve protected değişkenlere doğrudan erişim sağlayamaz.
  // nes_tur.priidana = 741;  // public ve private kalıtımda derleme hatası verir.
  // nes_tur.proidana = 741;  // public ve private kalıtımda derleme hatası verir.
  // nes_tur.pubidana = 741;  // public kalıtımda normal çalışır, private kalıtımda derleme hatası verir.

  // nes_tur.deger_goster(); // public kalıtımda normal çalışır, private kalıtımda derleme hatası verir.

  cout << endl << "nes_tur değişkeninin sınıfana ve siniftur elemanlarına erişimi:" << endl;
  cout << "---------------------------------------------------------------" << endl;
  // siniftur sınıfından oluşturulan nesne, kendi fonksiyonları yoluyla
  // sinifana ve siniftur içindeki protected ve public değişkenlere değer atar ve ekrana yazar.
  nes_tur.deger_ata_tur(9, 16, 4, 17, 28); // İlk iki parametre anasinif değişken değerleri için değer atar.
  nes_tur.deger_goster_tur();

  nes_tur.pubidtur = 687;

  nes_tur.deger_goster_tur();

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

nes_ana değişkeninin sinifana elemanlarına erişimi:
---------------------------------------------------
sinifana değişkenlerine değer atama: 7 21 165
sinifana değişken değerleri: 7 21 165
sinifana değişken değerleri: 7 21 954

nes_tur değişkeninin sinifana elemanlarına doğrudan erişimi:
------------------------------------------------------------

nes_tur değişkeninin sınıfana ve siniftur elemanlarına erişimi:
---------------------------------------------------------------
sinifana değişkenlerine değer atama: 9 16
siniftur değişkenlerine değer atama: 4 17 28
sinifana değişken değerleri: 9 16 
siniftur değişken değerleri: 4 17 28
sinifana değişken değerleri: 9 16 
siniftur değişken değerleri: 4 17 687

```

Program, sinifana adlı bir sınıf ve bu sınıftan private olarak türetilen siniftur adlı bir sınıf oluşturur. Her iki sınıf içinde de private, protected ve public olmak üzere üç adet değişken ve bu değişkenlere değer atayan ve ekranda gösteren iki adet fonksiyon tanımlar.

Program çalışmaya başladığında, sinifana cinsinden bir nesne tanımlar. Ana sınıf nesnesi yoluyla, ana sınıf fonksiyonlarını çağırarak, önce ana sınıf içindeki değişkenlere birer değer atar sonra değişken değerlerini ekrana yazar. Ana sınıf nesnesini kullanarak doğrudan ana sınıf içinde public pubidana değişkenine bir değer atar ve ana sınıf içindeki deger\_goster() fonksiyonu ile değişken değerlerini tekrar ekrana yazar.

Program, ikinci safhada türetilmiş sınıf olan siniftur türünden nes\_tur adlı bir nesne oluşturur. Bu nesne yoluyla ana sınıf içindeki fonksiyonlara erişim sağlayamaz.

Sonra, aynı nesne ile, türetilen sınıf içindeki deger\_ata\_tur() fonksiyonu ile sinifana içindeki proidana ve pubidana değişkenleri ile siniftur içindeki priidtur, proidtur ve pubidtur değişkenlerine birer değer atar. Son olarak, sinifana içindeki proidana ve pubidana değişkenler ile siniftur içindeki değişken değerlerini ekrana yazar.

> Bir sınıftan public kalıtım ile bir sınıf türetildiğinde, türetilmiş sınıftan oluşturulan bir nesne ile ana sınıfın protected ve public değişkenlerine erişim sağlanırken, kalıtım private olarak yapıldığında, ana sınıfın protected ve public değişkenlerine türetilen sınıfın fonksiyonlarından erişim sağlanmaktadır.
{: .prompt-info }

![](cprog/inhprivate02.png)

Bir ana sınıftan private olarak türetilen bir sınıftan public olarak diğer bir sınıf türetildiğinde, ana sınıfın bütün elemanları ilk türetilen sınıfın private elemanı haline geldiğinden, türetilen sınıftan türetilen sınıf ana sınıfın elemanlarına erişim sağlayamaz.

Bu özelliği bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

class sinifana {
  private:
    // Bu değişkene sadece sinifana içindeki fonksiyonlar erişim sağlayabilir.
    int priidana;

  protected:
    // Bu değişkene sinifana ve siniftur içindeki fonksiyonlar erişim sağlayabilir.
    int proidana;

  public:
    // Bu değişkene sinifana içindeki fonksiyonlar ve sinifana türünden oluşturulmuş nesneler ile
    // siniftur içindeki fonksiyonlar doğrudan erişim sağlayabilir.
    int pubidana;
    void deger_ata(int pid1, int pid2, int pid3)
    {
      priidana = pid1; proidana = pid2; pubidana = pid3;
      cout << "sinifana değişkenlerine değer atama: " << priidana << " " << proidana << " " << pubidana << endl;
    }
    void deger_goster() { cout << "sinifana değişken değerleri: " << priidana << " " << proidana << " " << pubidana << endl; }
};

class siniftur : private sinifana {
  private:
    int priidtur;

  protected:
    int proidtur;

  public:
    int pubidtur;
    // Türetilen sınıf içindeki fonksiyonlar direk olarak
    // sadece türetilen sınıf değişkenlerine erişim sağlayabilir.
    void deger_ata_tur(int pid1, int pid2, int pid3, int pid4, int pid5)
    {
      proidana = pid1; pubidana = pid2;                  // Ana sınıf değişkenlerine değer atama
      priidtur = pid3; proidtur = pid4; pubidtur = pid5; // Türetilen sınıf değişkenlerine değer atama
      cout << "sinifana değişkenlerine değer atama: " << proidana << " " << pubidana << endl;
      cout << "siniftur değişkenlerine değer atama: " << priidtur << " " << proidtur << " " <<  pubidtur << endl;
    }
    void deger_goster_tur()
    {
      cout << "sinifana değişken değerleri: " << proidana << " " << pubidana << " " << endl;
      cout << "siniftur değişken değerleri: " <<  priidtur << " " << proidtur << " " << pubidtur << endl;
    }
};

class sinifturtur : public siniftur {
  private:
    int priidturtur;

  protected:
    int proidturtur;

  public:
    int pubidturtur;
    // Türetilen sınıftan türetilen sınıf içindeki fonksiyonlar direk olarak
    // ana sınıfın public ve protected değişkenlerine erişim sağlayabilir.
    void deger_ata_turtur(void)
    {
      priidturtur = proidtur; proidturtur = proidtur*2; pubidturtur = pubidtur*2;
      cout << "sinifturtur değişkenlerine değer atama: " << priidturtur << " " << proidturtur << " " << pubidturtur << endl;
    }
    void deger_goster_turtur() { cout << "sinifturtur değişken değerleri: " << priidturtur << " " << proidturtur << " " << pubidturtur << endl; }
};

int main(void)
{
  siniftur nes_tur;

  cout << "nes_tur değişkeninin sinifana elemanlarına doğrudan erişimi:" << endl;
  cout << "------------------------------------------------------------" << endl;
  // siniftur sınıfından oluşturulan nesne, sinifana sınıfı fonksiyonları yoluyla
  // sinifana sınıfı değişkenlerine değer atayamaz ve ekrana yazamaz.
  // nes_tur.deger_ata(8, 25, 246); // public kalıtımda normal çalışır, private kalıtımda derleme hatası verir.
  // nes_tur.deger_goster();        // public kalıtımda normal çalışır, private kalıtımda derleme hatası verir.

  // Türetilen sınıf nesnesi ana sınıf içindeki private ve protected değişkenlere doğrudan erişim sağlayamaz.
  // nes_tur.priidana = 741;  // public ve private kalıtımda derleme hatası verir.
  // nes_tur.proidana = 741;  // public ve private kalıtımda derleme hatası verir.
  // nes_tur.pubidana = 741;  // public kalıtımda normal çalışır, private kalıtımda derleme hatası verir.

  // nes_tur.deger_goster(); // public kalıtımda normal çalışır, private kalıtımda derleme hatası verir.

  cout << endl << "nes_tur değişkeninin sınıfana ve siniftur elemanlarına erişimi:" << endl;
  cout << "---------------------------------------------------------------" << endl;
  // siniftur sınıfından oluşturulan nesne, kendi fonksiyonları yoluyla
  // sinifana ve siniftur içindeki protected ve public değişkenlere değer atar ve ekrana yazar.
  nes_tur.deger_ata_tur(9, 16, 4, 17, 28); // İlk iki parametre anasinif değişken değerleri için değer atar.
  nes_tur.deger_goster_tur();

  nes_tur.pubidtur = 687;

  nes_tur.deger_goster_tur();

  sinifturtur nes_turtur;

  // sinifturtur sınıfından oluşturulan nesne, sinifana sınıfı fonksiyonları yoluyla
  // sinifana sınıfı değişkenlerine atayamaz ve ekrana yazamaz.
  cout << endl << "nes_turtur değişkeninin sinifana elemanlarına erişimi:" << endl;
  cout << "------------------------------------------------------" << endl;
  // nes_turtur.deger_ata(78, 121, 375); // Derleme hatası verir.
  // nes_turtur.deger_goster();          // Derleme hatası verir.

  // nes_turtur.pubidana = 1765;         // Derleme hatası verir.

  // nes_turtur.deger_goster();          // Derleme hatası verir.

  // sinifturtur sınıfından oluşturulan nesne, siniftur sınıfı fonksiyonları yoluyla
  // sinifana ve sinifturtur sınıflarının protected ve public değişkenlerine erişim
  // sağlayarak siniftur sınıfı değişkenlerine değer atar ve ekrana yazar.
  cout << endl << "nes_turtur değişkeninin siniftur elemanlarına erişimi:" << endl;
  cout << "------------------------------------------------------" << endl;
  nes_turtur.deger_ata_tur(7, 19, 5, 21, 37);
  nes_turtur.deger_goster_tur();

  nes_turtur.pubidtur = 3754;    // İkinci türetilen sınıf nesnesi ilk türetilen sınıf içindeki public değişkene doğrudan erişim sağlar.

  nes_turtur.deger_goster_tur(); // İkinci türetilen sınıf fonksiyonuna erişim

  // sinifturtur sınıfından oluşturulan nesne, kendi fonksiyonları yoluyla sinifturtur sınıfının
  // protected ve public değişkenlerine erişim sağlayarak kendi değişkenlerine değer atar ve ekrana yazar.
  cout << endl << "nes_turtur değişkeninin sinifturtur elemanlarına erişimi:" << endl;
  cout << "---------------------------------------------------------" << endl;
  nes_turtur.deger_ata_turtur();
  nes_turtur.deger_goster_turtur();

  nes_turtur.pubidturtur = 9284; // İkinci türetilen sınıf nesnesi kendi içindeki public değişkene doğrudan erişim sağlar.

  nes_turtur.deger_goster_turtur();

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

nes_tur değişkeninin sinifana elemanlarına doğrudan erişimi:
------------------------------------------------------------

nes_tur değişkeninin sınıfana ve siniftur elemanlarına erişimi:
---------------------------------------------------------------
sinifana değişkenlerine değer atama: 9 16
siniftur değişkenlerine değer atama: 4 17 28
sinifana değişken değerleri: 9 16 
siniftur değişken değerleri: 4 17 28
sinifana değişken değerleri: 9 16 
siniftur değişken değerleri: 4 17 687

nes_turtur değişkeninin sinifana elemanlarına erişimi:
------------------------------------------------------

nes_turtur değişkeninin siniftur elemanlarına erişimi:
------------------------------------------------------
sinifana değişkenlerine değer atama: 7 19
siniftur değişkenlerine değer atama: 5 21 37
sinifana değişken değerleri: 7 19 
siniftur değişken değerleri: 5 21 37
sinifana değişken değerleri: 7 19 
siniftur değişken değerleri: 5 21 3754

nes_turtur değişkeninin sinifturtur elemanlarına erişimi:
---------------------------------------------------------
sinifturtur değişkenlerine değer atama: 21 42 7508
sinifturtur değişken değerleri: 21 42 7508
sinifturtur değişken değerleri: 21 42 9284

```

Program, sinifana adlı bir sınıf ve bu sınıftan private olarak türetilen siniftur adlı bir sınıf ve siniftur sınıfından public olarak türetilen sinifturtur adlı bir sınıf oluşturur. Her üç sınıf içinde de private, protected ve public olmak üzere üç adet değişken ve bu değişkenlere değer atayan ve ekranda gösteren iki adet fonksiyon tanımlar.

Program çalışmaya başladığında, siniftur sınıfı türünden nes\_tur adlı bir nesne oluşturur. Bu nesne yoluyla ana sınıf içindeki değişken ve fonksiyonlara erişim sağlayamaz.

Sonra, aynı nesne ile, siniftur içindeki deger\_ata\_tur() fonksiyonu ile sinifana sınıfının protected ve public değişkenlerine erişim sağlayarak, bu değişkenlere birer değer atar. Aynı fonksiyon ile priidtur, proidtur ve pubidtur değişkenlerine de birer değer atar. Son olarak, deger\_goster\_tur() fonksiyonu ile siniftur sınıfı içindeki değişken değerlerini ekrana yazar.

Sonra, sinifturtur sınıfı türünden nes\_turtur adlı bir nesne oluşturur. Bu nesne yoluyla ana sınıf içindeki değişken ve fonksiyonlara erişim sağlayamaz.

Sonra, aynı nesne ile, siniftur içindeki deger\_ata\_tur() fonksiyonu ile sinifana sınıfının protected ve public değişkenlerine erişim sağlayarak, bu değişkenlere birer değer atar. Aynı fonksiyon ile priidtur, proidtur ve pubidtur değişkenlerine de birer değer atar. Son olarak, deger\_goster\_tur() fonksiyonu ile siniftur sınıfı içindeki değişken değerlerini ekrana yazar.

Daha sonra, aynı nesne ile, kendi sınıfı içindeki deger\_ata\_turtur() fonksiyonu ile siniftur sınıfının protected ve public değişkenlerine erişim sağlayarak, bu değişiken değerlerini kullanarak, kendi değişkenlerine değer atar. Son olarak, sinifturtur sınıfı içindeki değişken değerlerini ekrana yazar.

> Ana sınıftan yapılan kalıtım işlemi private olarak yapıldığından, ana sınıfın tüm elemanları siniftur sınıfının private elemanı olur. Bu nedenle, sinifana sınıfı içindeki protected ve public değişkenlere sadece siniftur sınıfı içindeki fonksiyonlar yoluyla erişim sağlayabilir, sinifturtur sınıfı içindeki fonksiyonlar ise erişim sağlayamaz.
{: .prompt-tip }

Programda oluşturulan sınıfların içindeki elemanlar ile bu sınıflardan oluşturulan nesnelerin erişim durumlarını gösteren şema aşağıdadır:

![](cprog/inhprivate03.png)

## Protected kalıtım

Bir ana sınıftan protected erişim türü kullanılarak bir sınıf türetildiğinde, ana sınıfın tüm public ve protected elemanları türetilen sınıfın protected elemanı olur.

![](cprog/inhprotected01.png)

Bu özelliği bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

class sinifana {
  private:
    // Bu değişkene sadece sinifana içindeki fonksiyonlar erişim sağlayabilir.
    int priidana;

  protected:
    // Bu değişkene sinifana ve siniftur içindeki fonksiyonlar erişim sağlayabilir.
    int proidana;

  public:
    // Bu değişkene sinifana içindeki fonksiyonlar ve sinifana türünden oluşturulmuş nesneler ile
    // siniftur içindeki fonksiyonlar doğrudan erişim sağlayabilir.
    int pubidana;
    void deger_ata(int pid1, int pid2, int pid3)
    {
      priidana = pid1; proidana = pid2; pubidana = pid3;
      cout << "sinifana değişkenlerine değer atama: " << priidana << " " << proidana << " " << pubidana << endl;
    }
    void deger_goster() { cout << "sinifana değişken değerleri: " << priidana << " " << proidana << " " << pubidana << endl; }
};

class siniftur : protected sinifana {
  private:
    int priidtur;

  protected:
    int proidtur;

  public:
    int pubidtur;
    // Türetilen sınıf içindeki fonksiyonlar direk olarak
    // sadece türetilen sınıf değişkenlerine erişim sağlayabilir.
    void deger_ata_tur(int pid1, int pid2, int pid3, int pid4, int pid5)
    {
      proidana = pid1; pubidana = pid2;                  // Ana sınıf değişkenlerine değer atama
      priidtur = pid3; proidtur = pid4; pubidtur = pid5; // Türetilen sınıf değişkenlerine değer atama
      cout << "sinifana değişkenlerine değer atama: " << proidana << " " << pubidana << endl;
      cout << "siniftur değişkenlerine değer atama: " << priidtur << " " << proidtur << " " <<  pubidtur << endl;
    }
    void deger_goster_tur()
    {
      cout << "sinifana değişken değerleri: " << proidana << " " << pubidana << " " << endl;
      cout << "siniftur değişken değerleri: " <<  priidtur << " " << proidtur << " " << pubidtur << endl;
    }
};

int main(void)
{
  sinifana nes_ana;

  cout << "nes_ana değişkeninin sinifana elemanlarına erişimi:" << endl;
  cout << "---------------------------------------------------" << endl;
  nes_ana.deger_ata(7, 21, 165);
  nes_ana.deger_goster();

  // nes_ana.priidana = 954; // Derleme hatası verir (Nesne sınıf içindeki private değişkene doğrudan erişim sağlayamaz).
  // nes_ana.proidana = 954; // Derleme hatası verir (Nesne sınıf içindeki protected değişkene doğrudan erişim sağlayamaz).
  nes_ana.pubidana = 954;    // Nesne sınıf içindeki public değişkene doğrudan erişim sağlar.

  nes_ana.deger_goster();

  siniftur nes_tur;

  cout << endl << "nes_tur değişkeninin sinifana elemanlarına doğrudan erişimi:" << endl;
  cout << "------------------------------------------------------------" << endl;
  // siniftur sınıfından oluşturulan nesne, sinifana sınıfı fonksiyonları yoluyla
  // sinifana sınıfı değişkenlerine değer atayamaz ve ekrana yazamaz.
  // nes_tur.deger_ata(8, 25, 246); // public kalıtımda normal çalışır, private ve protected kalıtımda derleme hatası verir.
  // nes_tur.deger_goster();        // public kalıtımda normal çalışır, private ve protected kalıtımda derleme hatası verir.

  // Türetilen sınıf nesnesi ana sınıf içindeki private ve protected değişkenlere doğrudan erişim sağlayamaz.
  // nes_tur.priidana = 741;  // public ve private kalıtımda derleme hatası verir.
  // nes_tur.proidana = 741;  // public ve private kalıtımda derleme hatası verir.
  // nes_tur.pubidana = 741;  // public kalıtımda normal çalışır, private ve protected kalıtımda derleme hatası verir.

  // nes_tur.deger_goster(); // public kalıtımda normal çalışır, private kalıtımda derleme hatası verir.

  cout << endl << "nes_tur değişkeninin sınıfana ve siniftur elemanlarına erişimi:" << endl;
  cout << "---------------------------------------------------------------" << endl;
  // siniftur sınıfından oluşturulan nesne, kendi fonksiyonları yoluyla
  // sinifana ve siniftur içindeki protected ve public değişkenlere değer atar ve ekrana yazar.
  nes_tur.deger_ata_tur(9, 16, 4, 17, 28); // İlk iki parametre anasinif değişken değerleri için değer atar.
  nes_tur.deger_goster_tur();

  nes_tur.pubidtur = 687;

  nes_tur.deger_goster_tur();

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

nes_ana değişkeninin sinifana elemanlarına erişimi:
---------------------------------------------------
sinifana değişkenlerine değer atama: 7 21 165
sinifana değişken değerleri: 7 21 165
sinifana değişken değerleri: 7 21 954

nes_tur değişkeninin sinifana elemanlarına doğrudan erişimi:
------------------------------------------------------------

nes_tur değişkeninin sınıfana ve siniftur elemanlarına erişimi:
---------------------------------------------------------------
sinifana değişkenlerine değer atama: 9 16
siniftur değişkenlerine değer atama: 4 17 28
sinifana değişken değerleri: 9 16 
siniftur değişken değerleri: 4 17 28
sinifana değişken değerleri: 9 16 
siniftur değişken değerleri: 4 17 687

```

Program, sinifana adlı bir sınıf ve bu sınıftan protected olarak türetilen siniftur adlı bir sınıf oluşturur. Her iki sınıf içinde de private, protected ve public olmak üzere üç adet değişken ve bu değişkenlere değer atayan ve ekranda gösteren iki adet fonksiyon tanımlar.

Program çalışmaya başladığında, sinifana cinsinden bir nesne tanımlar. Ana sınıf nesnesi yoluyla, ana sınıf fonksiyonlarını çağırarak, önce ana sınıf içindeki değişkenlere birer değer atar sonra değişken değerlerini ekrana yazar. Ana sınıf nesnesini kullanarak doğrudan ana sınıf içinde public pubidana değişkenine bir değer atar ve ana sınıf içindeki deger\_goster() fonksiyonu ile değişken değerlerini tekrar ekrana yazar.

Program, ikinci safhada türetilmiş sınıf olan siniftur türünden nes\_tur adlı bir nesne oluşturur. Bu nesne yoluyla ana sınıf içindeki fonksiyonlara erişim sağlayamaz.

Sonra, aynı nesne ile, türetilen sınıf içindeki deger\_ata\_tur() fonksiyonu ile sinifana içindeki proidana ve pubidana değişkenleri ile siniftur içindeki priidtur, proidtur ve pubidtur değişkenlerine birer değer atar. Son olarak, sinifana içindeki proidana ve pubidana değişkenler ile siniftur içindeki değişken değerlerini ekrana yazar.

> Bir sınıftan public kalıtım ile bir sınıf türetildiğinde, türetilmiş sınıftan oluşturulan bir nesne ile ana sınıfın protected ve public değişkenlerine erişim sağlanırken, kalıtım protected olarak yapıldığında, ana sınıfın protected ve public değişkenlerine türetilen sınıfın fonksiyonlarından erişim sağlanmaktadır.
{: .prompt-warning }

![](cprog/inhprotected02.png)

## Çoklu ana sınıf ile kalıtım

İki veya daha fazla sınıf ana sınıf olarak kullanılmak suretiyle bir sınıf türetilerek çoklu klaıtım işlemi uygulanabilir. Bu işlem için, türetilen sınıfın tanımlama satırında, ana snıfları virgül ile ayırmak gerekir.

```

class türetilen-sınıf : erişim-türü anasınıf-1, erişim-türü anasınıf-2, ...
{
  // Kod bloğu
}

```

Bu özelliği bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

class sinifana1 {
  private:
    // Bu değişkene sadece sinifana içindeki fonksiyonlar erişim sağlayabilir.
    int priidana1;

  protected:
    // Bu değişkene sinifana içindeki fonksiyonlar ile sinifana sınıfından türetilmiş sınıf fonksiyonları erişim sağlayabilir.
    int proidana1;

  public:
    // Bu değişkene sinifana içindeki fonksiyonlar ve sinifana sınıfından türetilmiş sınıf fonksiyonları ile
    // sinifana türünden ve türetilmiş sınıf türünden oluşturulmuş nesneler doğrudan erişim sağlayabilir.
    int pubidana1;
    void deger_ata1(int pid1, int pid2, int pid3)
    {
      priidana1 = pid1; proidana1 = pid2; pubidana1 = pid3;
      cout << "sinifana1 değişkenlerine değer atama: " << priidana1 << " " << proidana1 << " " << pubidana1 << endl;
    }
    void deger_goster1()
    {
      cout << "sinifana1 değişken değerleri: " << priidana1 << " " << proidana1 << " " << pubidana1 << endl;
    }
};

class sinifana2 {

  private:
    // Bu değişkene sadece sinifana içindeki fonksiyonlar erişim sağlayabilir.
    int priidana2;

  protected:
    // Bu değişkene sinifana içindeki fonksiyonlar ile sinifana sınıfından türetilmiş sınıf fonksiyonları erişim sağlayabilir.
    int proidana2;

  public:
    // Bu değişkene sinifana içindeki fonksiyonlar ve sinifana sınıfından türetilmiş sınıf fonksiyonları ile
    // sinifana türünden ve türetilmiş sınıf türünden oluşturulmuş nesneler doğrudan erişim sağlayabilir.
    int pubidana2;
    void deger_ata2(int pid1, int pid2, int pid3)
    {
      priidana2 = pid1; proidana2 = pid2; pubidana2 = pid3;
      cout << "sinifana2 değişkenlerine değer atama: " << priidana2 << " " << proidana2 << " " << pubidana2 << endl;
    }
    void deger_goster2()
    {
      cout << "sinifana2 değişken değerleri: " << priidana2 << " " << proidana2 << " " << pubidana2 << endl;
    }
};

class siniftur : public sinifana1, public sinifana2 {
  private:
    int priidtur;

  protected:
    int proidtur;

  public:
    int pubidtur;
    // Türetilen sınıf içindeki fonksiyonlar direk olarak
    // ana sınıfın public ve protected değişkenlerine erişim sağlayabilir.
    void deger_ata_tur(int pid)
    {
      priidtur = proidana1 + proidana2; proidtur = pubidana1 + pubidana2; pubidtur = pid;
      cout << "siniftur değişkenlerine değer atama: " << priidtur << " " << proidtur << " " <<  pubidtur << endl;
    }
    void deger_goster_tur() { cout << "siniftur değişken değerleri: " << priidtur << " " << proidtur << " " << pubidtur << endl; }
};

int main(void)
{
  siniftur nes_tur;

  cout << "nes_tur değişkeninin sinifana1 ve sinifana2 elemanlarına doğrudan erişimi:" << endl;
  cout << "--------------------------------------------------------------------------" << endl;
  // siniftur sınıfından oluşturulan nesne, sinifana1 ve sinifana2 sınıfları fonksiyonları yoluyla
  // sinifana1 ve sinifana2 sınıfı değişkenlerine değer atar ve ekrana yazar.
  nes_tur.deger_ata1(5, 27, 357);
  nes_tur.pubidana1 = 741;         // nes_tur nesnesi sinifana1 içindeki public değişkene doğrudan erişim sağlar.
  nes_tur.deger_goster1();

  nes_tur.deger_ata2(9, 64, 821);
  nes_tur.pubidana2 = 7452;        // nes_tur nesnesi sinifana1 içindeki public değişkene doğrudan erişim sağlar.
  nes_tur.deger_goster2();

  cout << endl << "nes_tur değişkeninin sinifana1, sinifana2 ve siniftur elemanlarına erişimi:" << endl;
  cout << "---------------------------------------------------------------------------" << endl;
  // siniftur sınıfından oluşturulan nesne, kendi fonksiyonları yoluyla sinifana1 ve sinifana2 sınıflarının
  // protected ve public değişkenlerine erişim sağlayarak kendi değişkenlerine değer atar ve ekrana yazar.
  nes_tur.deger_ata_tur(36);
  nes_tur.pubidtur = 687;
  nes_tur.deger_goster_tur();

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

nes_tur değişkeninin sinifana1 ve sinifana2 elemanlarına doğrudan erişimi:
--------------------------------------------------------------------------
sinifana1 değişkenlerine değer atama: 5 27 357
sinifana1 değişken değerleri: 5 27 741
sinifana2 değişkenlerine değer atama: 9 64 821
sinifana2 değişken değerleri: 9 64 7452

nes_tur değişkeninin sinifana1, sinifana2 ve siniftur elemanlarına erişimi:
---------------------------------------------------------------------------
siniftur değişkenlerine değer atama: 91 8193 36
siniftur değişken değerleri: 91 8193 687

```

Program, sinifana1 ve sinifana2 adlı iki sınıf ve bu sınıflardan public olarak türetilen siniftur adlı bir sınıf oluşturur. Her üç sınıf içinde de private, protected ve public olmak üzere üç adet değişken ve bu değişkenlere değer atayan ve ekranda gösteren iki adet fonksiyon tanımlar.

Program, çalışmaya başladığında, türetilmiş sınıf olan siniftur türünden nes\_tur adlı bir nesne oluşturur. Bu nesne yoluyla ana sınıflar içindeki fonksiyonlara erişim sağlayarak, önce ana sınıflar içindeki değişkenlere birer değer atar. Aynı nesne ile doğrudan ana sınıf içinde public değişkenlere birer değer atar ve ana sınıflar içindeki deger\_goster1() ve deger\_goster2() fonksiyonları ile değişken değerlerini tekrar ekrana yazar.

Sonra, aynı nesne ile, türetilen sınıf içindeki deger\_ata\_tur() fonksiyonu ile sinifana1 ve sinifana2 sınıflarının protected ve public değişkenlerine erişim sağlayarak, bu değişken değerlerini kullanarak kendi değişkenlerine değer atar. Aynı nesne ile doğrudan pubidtur değişkenine bir değer atar ve deger\_goster\_tur() fonksiyonu ile değişken değerlerini tekrar ekrana yazar.

![](cprog/inhmultibase01.png)

## Kalıtımda constructor ve destructor fonksiyonları kullanımı

Kalıtım işleminde ana sınıf ve türetilen sınıflar için constructor ve destructor fonksiyonları tanımlanırsa, program içinde çalışma önceliği constructor fonksiyonları için ana sınıfa, destructor fonksiyonları için türetilen sınıfa aittir.

Constructor ve destructor fonksiyonları çalışma sırası

Ana sınıf contructor fonksiyonu

Türetilen sınıf contructor fonksiyonu

Türetilen sınıf destructor fonksiyonu

Ana sınıf destructor fonksiyonu

Kalıtım işleminde ana sınıf ve türetilen sınıf içinde kullanılan constructor ve destructor fonksiyonları birbirinden bağımsız veya birbiri ile ilgili olarak kullanılabilir.

## Kalıtımda ana ve türetilen sınıf constructor ve destructor fonksiyonlarının birbirinden bağımsız kullanımı

## Tek seviyeli kalıtımda constructor ve destructor fonksiyonlarının birbirinden bağımsız kullanımı

Kalıtım uygulandığında, ana sınıf constructor fonksiyonu türetilen sınıftan önce, ana sınıf destructor fonksiyonu ise türetilen sınıf destructor fonksiyonundan sonra çalıştırılır.

Şimdi, tek seviyeli kalıtımda ana sınıf ve türetilen sınıf içinde parametresiz olarak tanımlanan constructor fonksiyonları ile destructor fonksiyonlarının birbirinden bağımsız kullanımını bir örnek üzerinde incelemeye çalışalım.

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
	sinifana()
	{
	  cout << "sinifana constructor fonksiyonu!" << endl;
	}
	~sinifana()
	{
	  cout << "sinifana destructor fonksiyonu!" << endl;
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
	siniftur()
	{
	  cout << "siniftur constructor fonksiyonu!" << endl;
	}
	~siniftur()
	{
	  cout << "siniftur destructor fonksiyonu!" << endl;
	}
    void deger_ata_tur(int pid1, int pid2)
    {
      priidtur = proidana + pubidana; proidtur = pid1; pubidtur = pid2;
      cout << "siniftur değişkenlerine değer atama: " << priidtur << " " << proidtur << " " <<  pubidtur << endl;
    }
    void deger_goster_tur() { cout << "siniftur değişken değerleri: " << priidtur << " " << proidtur << " " << pubidtur << endl; }
};

int main(void)
{
  siniftur nes_tur;

  cout << endl << "nes_tur değişkeninin sinifana elemanlarına doğrudan erişimi:" << endl;
  cout << "------------------------------------------------------------" << endl;
  nes_tur.deger_ata(109, 236, 347);
  nes_tur.deger_goster();

  cout << endl << "nes_tur değişkeninin sinifana ve siniftur elemanlarına erişimi:" << endl;
  cout << "---------------------------------------------------------------" << endl;
  nes_tur.deger_ata_tur(42, 596);
  nes_tur.deger_goster_tur();

  cout << endl;

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

sinifana constructor fonksiyonu!
siniftur constructor fonksiyonu!

nes_tur değişkeninin sinifana elemanlarına doğrudan erişimi:
------------------------------------------------------------
sinifana değişkenlerine değer atama: 109 236 347
sinifana değişken değerleri: 109 236 347

nes_tur değişkeninin sinifana ve siniftur elemanlarına erişimi:
---------------------------------------------------------------
siniftur değişkenlerine değer atama: 583 42 596
siniftur değişken değerleri: 583 42 596

siniftur destructor fonksiyonu!
sinifana destructor fonksiyonu!

```

Program, sinifana adlı bir sınıf ve bu sınıftan public olarak türetilen siniftur adlı bir sınıf oluşturur. Her iki sınıf içinde de private, protected ve public olmak üzere üç adet değişken ve bu değişkenlere değer atayan ve ekranda gösteren iki adet fonksiyon tanımlar.

Program çalışmaya başladığında, türetilmiş sınıf olan siniftur türünden nes\_tur adlı bir nesne oluşturur. Bu nesne yoluyla ana sınıf içindeki fonksiyonlara erişim sağlayarak, önce ana sınıf içindeki değişkenlere birer değer atar sonra değişken değerlerini ekrana yazar. Aynı nesne ile doğrudan ana sınıf içinde public pubidana değişkenine bir değer atar ve ana sınıf içindeki deger\_goster() fonksiyonu ile değişken değerlerini tekrar ekrana yazar.

Sonra, aynı nesne ile, türetilen sınıf içindeki deger\_ata\_tur() fonksiyonu ile sinifana sınıfının protected ve public değişkenlerine erişim sağlayarak, bu değişkenlerin toplamını, priidtur değişkenine atar. Aynı fonksiyon ile proidtur ve pubidtur değişkenlerine de birer değer atar. Türetilmiş siniftur sınıfı içindeki değişken değerlerini ekrana yazar. Aynı nesne ile doğrudan pubidtur değişkenine bir değer atar ve deger\_goster\_tur() fonksiyonu ile değişken değerlerini tekrar ekrana yazar.

Program çalışmaya başladığında, constructor fonksiyonları sinifana ve siniftur çalıştırılır. Program sona ererken destructor fonksiyonları, siniftur ve sinifana sırasıyla çalıştırılır.

## Çok seviyeli kalıtımda constructor ve destructor fonksiyonlarının birbirinden bağımsız kullanımı

Çok seviyeli kalıtım uygulandığında, constructor fonksiyonları için çalışma sırası ana sınıftan başlayarak en son türetilen sınıfa doğru gider. Destructor fonksiyonları için çalışma sırası en son türetilen sınıftan başlayarak ana sınıfa doğru gider.

Şimdi, ana ve türetilen sınıf constructor ve destructor fonksiyonlarının bağımsız kullanımını türetilen sınıfın başka bir türetilen sınıf için ana sınıf olduğu bir çoklu kalıtım işlemi üzerinde incelemeye çalışalım.

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
	sinifana()
	{
	  cout << "sinifana constructor fonksiyonu!" << endl;
	}
	~sinifana()
	{
	  cout << "sinifana destructor fonksiyonu!" << endl;
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
	siniftur()
	{
	  cout << "siniftur constructor fonksiyonu!" << endl;
	}
	~siniftur()
	{
	  cout << "siniftur destructor fonksiyonu!" << endl;
	}
	void deger_ata_tur(int pid1, int pid2)
    {
      priidtur = proidana + pubidana; proidtur = pid1; pubidtur = pid2;
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
	sinifturtur()
	{
	  cout << "sinifturtur constructor fonksiyonu!" << endl;
	}
	~sinifturtur()
	{
	  cout << "sinifturtur destructor fonksiyonu!" << endl;
	}    void deger_ata_turtur(void)
    {
      priidturtur = proidana + pubidana; proidturtur = proidtur*2; pubidturtur = pubidtur*2;
      cout << "sinifturtur değişkenlerine değer atama: " << priidturtur << " " << proidturtur << " " << pubidturtur << endl;
    }
    void deger_goster_turtur() { cout << "sinifturtur değişken değerleri: " << priidturtur << " " << proidturtur << " " << pubidturtur << endl; }
};

int main(void)
{
  sinifturtur nes_turtur;

  cout << endl << "nes_turtur değişkeninin sinifana elemanlarına erişimi:" << endl;
  cout << "------------------------------------------------------" << endl;
  nes_turtur.deger_ata(135, 394, 776);
  nes_turtur.deger_goster();

  cout << endl << "nes_turtur değişkeninin siniftur elemanlarına erişimi:" << endl;
  cout << "------------------------------------------------------" << endl;
  nes_turtur.deger_ata_tur(346, 587);
  nes_turtur.deger_goster_tur();
  nes_turtur.deger_goster_tur(); // İkinci türetilen sınıf fonksiyonuna erişim

  cout << endl << "nes_turtur değişkeninin sinifturtur elemanlarına erişimi:" << endl;
  cout << "---------------------------------------------------------" << endl;
  nes_turtur.deger_ata_turtur();
  nes_turtur.deger_goster_turtur();

  cout << endl;

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

sinifana constructor fonksiyonu!
siniftur constructor fonksiyonu!
sinifturtur constructor fonksiyonu!

nes_turtur değişkeninin sinifana elemanlarına erişimi:
------------------------------------------------------
sinifana değişkenlerine değer atama: 135 394 776
sinifana değişken değerleri: 135 394 776

nes_turtur değişkeninin siniftur elemanlarına erişimi:
------------------------------------------------------
siniftur değişkenlerine değer atama: 1170 346 587
siniftur değişken değerleri: 1170 346 587
siniftur değişken değerleri: 1170 346 587

nes_turtur değişkeninin sinifturtur elemanlarına erişimi:
---------------------------------------------------------
sinifturtur değişkenlerine değer atama: 1170 692 1174
sinifturtur değişken değerleri: 1170 692 1174

sinifturtur destructor fonksiyonu!
siniftur destructor fonksiyonu!
sinifana destructor fonksiyonu!

```

Program, sinifana adlı bir sınıf ve bu sınıftan public olarak türetilen siniftur adlı bir sınıf ve siniftur sınıfından yine public olarak türetilen sinifturtur adlı bir sınıf oluşturur. Her üç sınıf içinde de private, protected ve public olmak üzere üç adet değişken ve bu değişkenlere değer atayan ve ekranda gösteren iki adet fonksiyon tanımlar.

Program çalışmaya başladığında, sinifturtur sınıfı türünden nes\_turtur adlı bir nesne oluşturur. Bu nesne yoluyla ana sınıf içindeki fonksiyonlara erişim sağlayarak, önce ana sınıf içindeki değişkenlere birer değer atar sonra değişken değerlerini ekrana yazar. Aynı nesne ile doğrudan ana sınıf içinde public pubidana değişkenine bir değer atar ve ana sınıf içindeki deger\_goster() fonksiyonu ile değişken değerlerini tekrar ekrana yazar.

Sonra, aynı nesne ile, ilk türetilen sınıf içindeki deger\_ata\_tur() fonksiyonu ile sinifana sınıfının protected ve public değişkenlerine erişim sağlayarak, bu değişkenlerin toplamını, priidtur değişkenine atar. Aynı fonksiyon ile proidtur ve pubidtur değişkenlerine de birer değer atar. Son olarak, siniftur sınıfı içindeki değişken değerlerini ekrana yazar.

Daha sonra, aynı nesne ile, kendi sınıfı içindeki deger\_ata\_turtur() fonksiyonu ile sinifana ve siniftur sınıflarının protected ve public değişkenlerine erişim sağlayarak, ana sınıf değişkenlerinin toplamını priidturtur değişkenine, siniftur içindeki poridtur değişkeninin iki katını proidturtur değişkenine ve pubidtur değişkeninin iki katını pubidturtur değişkenine atar. Son olarak, sinifturtur sınıfı içindeki değişken değerlerini ekrana yazar.

Program çalışmaya başladığında, constructor fonksiyonları sinifana, siniftur ve sinifturtur sırasıyla çalıştırılır. Program sona ererken destructor fonksiyonları, sinifturtur, siniftur ve sinifana sırasıyla çalıştırılır.

## Çoklu ana sınıf ile kalıtımda constructor ve destructor fonksiyonlarının birbirinden bağımsız kullanımı

Çoklu ana sınıf ile kalıtım uygulandığında, constructor fonksiyonları için çalışma sırası türetilen sınıf tanımlama satırındaki ana sınıfların tanımlanma sırasına ana sınıflardan başlayarak türetilen sınıfa doğru gider. Destructor fonksiyonları için çalışma sırası, en son türetilen sınıftan başlayarak türetilen sınıf tanımlama satırındaki ana sınıfların tanımlanma sırasınıın tersine doğru gider.

Şimdi, iki ana sınıflı tek seviyeli kalıtımda tüm sınıflar içinde parametresiz olarak tanımlanan constructor fonksiyonları ile destructor fonksiyonlarının birbirinden bağımsız kullanımını bir örnek üzerinde incelemeye çalışalım.

```c++
#include <iostream>

using namespace std;

class sinifana1 {
  private:
    int priidana1;

  protected:
    int proidana1;

  public:
    int pubidana1;
	sinifana1()
	{
	  cout << "sinifana1 constructor fonksiyonu!" << endl;
	}
	~sinifana1()
	{
	  cout << "sinifana1 destructor fonksiyonu!" << endl;
	}
    void deger_ata1(int pid1, int pid2, int pid3)
    {
      priidana1 = pid1; proidana1 = pid2; pubidana1 = pid3;
      cout << "sinifana1 değişkenlerine değer atama: " << priidana1 << " " << proidana1 << " " << pubidana1 << endl;
    }
    void deger_goster1()
    {
      cout << "sinifana1 değişken değerleri: " << priidana1 << " " << proidana1 << " " << pubidana1 << endl;
    }
};

class sinifana2 {
  private:
    int priidana2;

  protected:
    int proidana2;

  public:
    int pubidana2;
	sinifana2()
	{
	  cout << "sinifana2 constructor fonksiyonu!" << endl;
	}
	~sinifana2()
	{
	  cout << "sinifana2 destructor fonksiyonu!" << endl;
	}
    void deger_ata2(int pid1, int pid2, int pid3)
    {
      priidana2 = pid1; proidana2 = pid2; pubidana2 = pid3;
      cout << "sinifana2 değişkenlerine değer atama: " << priidana2 << " " << proidana2 << " " << pubidana2 << endl;
    }
    void deger_goster2()
    {
      cout << "sinifana2 değişken değerleri: " << priidana2 << " " << proidana2 << " " << pubidana2 << endl;
    }
};

class siniftur : public sinifana1, public sinifana2 {
  private:
    int priidtur;

  protected:
    int proidtur;

  public:
    int pubidtur;
	siniftur()
	{
	  cout << "siniftur constructor fonksiyonu!" << endl;
	}
	~siniftur()
	{
	  cout << "siniftur destructor fonksiyonu!" << endl;
	}
    void deger_ata_tur(int pid)
    {
      priidtur = proidana1 + proidana2; proidtur = pubidana1 + pubidana2; pubidtur = pid;
      cout << "siniftur değişkenlerine değer atama: " << priidtur << " " << proidtur << " " <<  pubidtur << endl;
    }
    void deger_goster_tur() { cout << "siniftur değişken değerleri: " << priidtur << " " << proidtur << " " << pubidtur << endl; }
};

int main(void)
{
  siniftur nes_tur;

  cout << endl << "nes_tur değişkeninin sinifana1 ve sinifana2 elemanlarına doğrudan erişimi:" << endl;
  cout << "--------------------------------------------------------------------------" << endl;
  nes_tur.deger_ata1(85, 487, 1051);
  nes_tur.deger_goster1();

  nes_tur.deger_ata2(21, 52, 732);
  nes_tur.deger_goster2();

  cout << endl << "nes_tur değişkeninin sinifana1, sinifana2 ve siniftur elemanlarına erişimi:" << endl;
  cout << "---------------------------------------------------------------------------" << endl;
  nes_tur.deger_ata_tur(42);
  nes_tur.deger_goster_tur();

  cout << endl;

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

sinifana1 constructor fonksiyonu!
sinifana2 constructor fonksiyonu!
siniftur constructor fonksiyonu!

nes_tur değişkeninin sinifana1 ve sinifana2 elemanlarına doğrudan erişimi:
--------------------------------------------------------------------------
sinifana1 değişkenlerine değer atama: 85 487 1051
sinifana1 değişken değerleri: 85 487 1051
sinifana2 değişkenlerine değer atama: 21 52 732
sinifana2 değişken değerleri: 21 52 732

nes_tur değişkeninin sinifana1, sinifana2 ve siniftur elemanlarına erişimi:
---------------------------------------------------------------------------
siniftur değişkenlerine değer atama: 539 1783 42
siniftur değişken değerleri: 539 1783 42

siniftur destructor fonksiyonu!
sinifana2 destructor fonksiyonu!
sinifana1 destructor fonksiyonu!

```

Program, sinifana1 ve sinifana2 adlı iki sınıf ve bu sınıflardan public olarak türetilen siniftur adlı bir sınıf oluşturur. Her üç sınıf içinde de private, protected ve public olmak üzere üç adet değişken ve bu değişkenlere değer atayan ve ekranda gösteren iki adet fonksiyon tanımlar.

Program, çalışmaya başladığında, türetilmiş sınıf olan siniftur türünden nes\_tur adlı bir nesne oluşturur. Bu nesne yoluyla ana sınıflar içindeki fonksiyonlara erişim sağlayarak, önce ana sınıflar içindeki değişkenlere birer değer atar. Aynı nesne ile doğrudan ana sınıf içinde public değişkenlere birer değer atar ve ana sınıflar içindeki deger\_goster1() ve deger\_goster2() fonksiyonları ile değişken değerlerini tekrar ekrana yazar.

Sonra, aynı nesne ile, türetilen sınıf içindeki deger\_ata\_tur() fonksiyonu ile sinifana1 ve sinifana2 sınıflarının protected ve public değişkenlerine erişim sağlayarak, bu değişken değerlerini kullanarak kendi değişkenlerine değer atar. Aynı nesne ile doğrudan pubidtur değişkenine bir değer atar ve deger\_goster\_tur() fonksiyonu ile değişken değerlerini tekrar ekrana yazar.

Program çalışmaya başladığında, constructor fonksiyonları sinifana1, sinifana2 ve siniftur sırasıyla çalıştırılır. Program sona ererken destructor fonksiyonları siniftur, sinifana2 ve sinifana1 sırasıyla çalıştırılır.

## Kalıtımda ana ve türetilen sınıf constructor ve destructor fonksiyonlarının birbirine bağımlı kullanımı

Bir kalıtım işlemi uygulandığında, ana ve türetilen sınıfların constructor fonksiyonlarına parametre geçirerek, ana ve türetilen sınıflar arasında parametre bağlantısı kurabiliriz. Bu yöntemle, türetilen sınıflar constructor fonksiyonları için tanımlanan parametreler ana sınıfların constructor fonksiyonlarına geçirilir.

Ana sınıfların constructor fonksiyonlarına parametre geçirmek için kullanılan türetilen sınıf constructor fonksiyon bildirimi aşağıdaki şekilde yapılır: 

```

türetilen-sınıf(parametreler) : anasınıf-1(parametreler), anasınıf-2(parametreler), ...
{
  // Kod bloğu
}

```

## Tek seviyeli kalıtımda constructor ve destructor fonksiyonlarının birbirine bağımlı kullanımı

Kalıtım uygulandığında, ana sınıf constructor fonksiyonu türetilen sınıftan önce, ana sınıf destructor fonksiyonu ise türetilen sınıf destructor fonksiyonundan sonra çalıştırılır.

Şimdi, tek seviyeli kalıtımda ana sınıf ve türetilen sınıf içinde parametreli olarak tanımlanan constructor fonksiyonları ile destructor fonksiyonlarının birbirine bağımlı kullanımını bir örnek üzerinde incelemeye çalışalım.

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
	// Buradaki pid1, pid2 ve pid3 değişkenleri siniftur constructor fonksiyonundan aktarılır.
	sinifana(int pid1, int pid2, int pid3)
	{
	  priidana = pid1; proidana = pid2; pubidana = pid3;
	  cout << "sinifana constructor fonksiyonu!" << endl;
	}
	~sinifana()
	{
	  cout << "sinifana destructor fonksiyonu!" << endl;
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
	// Burada constructor fonksiyonuna geçirilen pid4, pid5 ve pid6 değişkenleri sinifana constructor fonksiyonuna aktarılır.
	siniftur(int pid1, int pid2, int pid3, int pid4, int pid5, int pid6) : sinifana(pid4, pid5, pid6)
	{
	  priidtur = pid1; proidtur = pid2; pubidtur = pid3;
	  cout << "siniftur constructor fonksiyonu!" << endl;
	}
	~siniftur()
	{
	  cout << "siniftur destructor fonksiyonu!" << endl;
	}
    void deger_ata_tur(int pid1, int pid2)
    {
      priidtur = proidana + pubidana; proidtur = pid1; pubidtur = pid2;
      cout << "siniftur değişkenlerine değer atama: " << priidtur << " " << proidtur << " " <<  pubidtur << endl;
    }
    void deger_goster_tur() { cout << "siniftur değişken değerleri: " << priidtur << " " << proidtur << " " << pubidtur << endl; }
};

int main(void)
{
  // Constructor fonksiyonuna aktarılan ilk üç değişken siniftur nesnesi için kullanılır,
  // son üç değişken ise sinifana constructor fonksiyonuna aktarılır.
  siniftur nes_tur(9, 25, 335, 694, 1254, 3489);

  cout << endl << "nes_tur değişkeninin sinifana elemanlarına doğrudan erişimi:" << endl;
  cout << "------------------------------------------------------------" << endl;
  nes_tur.deger_goster();

  cout << endl << "nes_tur değişkeninin sinifana ve siniftur elemanlarına erişimi:" << endl;
  cout << "---------------------------------------------------------------" << endl;
  nes_tur.deger_goster_tur();

  cout << endl;

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

sinifana constructor fonksiyonu!
siniftur constructor fonksiyonu!

nes_tur değişkeninin sinifana elemanlarına doğrudan erişimi:
------------------------------------------------------------
sinifana değişken değerleri: 694 1254 3489

nes_tur değişkeninin sinifana ve siniftur elemanlarına erişimi:
---------------------------------------------------------------
siniftur değişken değerleri: 9 25 335

siniftur destructor fonksiyonu!
sinifana destructor fonksiyonu!

```

Program, sinifana adlı bir sınıf ve bu sınıftan public olarak türetilen siniftur adlı bir sınıf oluşturur. Her iki sınıf içinde de private, protected ve public olmak üzere üç adet değişken ve bu değişkenlere değer atayan ve ekranda gösteren iki adet fonksiyon tanımlar.

Program çalışmaya başladığında, türetilmiş sınıf olan siniftur türünden nes\_tur adlı bir nesne oluşturur. Bu nesne oluşturulurken constructor fonksiyonuna altı adet parametre değeri geçirilir. Constructor fonksiyonuna geçirilen ilk üç parametre siniftur nesnesi için kullanılarak siniftur içindeki değişkenlere birer değer atanır. Son üç parametre ise, sinifana constructor fonksiyonuna aktarılarak, sinifana
içindeki değişkenlere birer değer atanır.

Sonra, nes\_tur nesnesi yoluyla ana sınıf içindeki deger\_goster() fonksiyonu ile sinifana değişken değerlerini, siniftur sınıfı içindeki deger\_goster\_tur() fonksiyonu ile siniftur değişken değerlerini ekrana yazar.

## Çoklu ana sınıf ile kalıtımda constructor ve destructor fonksiyonlarının birbirine bağımlı kullanımı

Şimdi, iki ana sınıflı tek seviyeli kalıtımda tüm sınıflar içinde parametreli olarak tanımlanan constructor fonksiyonları ile destructor fonksiyonlarının birbirine bağımlı olarak kullanımı bir örnek üzerinde incelemeye çalışalım.

```c++
#include <iostream>

using namespace std;

class sinifana1 {
  private:
    int priidana1;

  protected:
    int proidana1;

  public:
    int pubidana1;
	sinifana1(int pid1, int pid2, int pid3)
	{
	  priidana1 = pid1; proidana1 = pid2; pubidana1 = pid3;
	  cout << "sinifana1 constructor fonksiyonu!" << endl;
	}
	~sinifana1()
	{
	  cout << "sinifana1 destructor fonksiyonu!" << endl;
	}
    void deger_ata1(int pid1, int pid2, int pid3)
    {
      priidana1 = pid1; proidana1 = pid2; pubidana1 = pid3;
      cout << "sinifana1 değişkenlerine değer atama: " << priidana1 << " " << proidana1 << " " << pubidana1 << endl;
    }
    void deger_goster1()
    {
      cout << "sinifana1 değişken değerleri: " << priidana1 << " " << proidana1 << " " << pubidana1 << endl;
    }
};

class sinifana2 {
  private:
    int priidana2;

  protected:
    int proidana2;

  public:
    int pubidana2;
	sinifana2(int pid1, int pid2, int pid3)
	{
	  priidana2 = pid1; proidana2 = pid2; pubidana2 = pid3;
	  cout << "sinifana constructor fonksiyonu!" << endl;
	}
	~sinifana2()
	{
	  cout << "sinifana2 destructor fonksiyonu!" << endl;
	}
    void deger_ata2(int pid1, int pid2, int pid3)
    {
      priidana2 = pid1; proidana2 = pid2; pubidana2 = pid3;
      cout << "sinifana2 değişkenlerine değer atama: " << priidana2 << " " << proidana2 << " " << pubidana2 << endl;
    }
    void deger_goster2()
    {
      cout << "sinifana2 değişken değerleri: " << priidana2 << " " << proidana2 << " " << pubidana2 << endl;
    }
};

class siniftur : public sinifana1, public sinifana2 {
  private:
    int priidtur;

  protected:
    int proidtur;

  public:
    int pubidtur;
	siniftur(int pid1, int pid2, int pid3, int pid4, int pid5, int pid6, int pid7, int pid8, int pid9) :
	         sinifana1(pid4, pid5, pid6), sinifana2(pid7, pid8, pid9)
	{
	  priidtur = pid1; proidtur = pid2; pubidtur = pid3;
	  cout << "siniftur constructor fonksiyonu!" << endl;
	}
	~siniftur()
	{
	  cout << "siniftur destructor fonksiyonu!" << endl;
	}
    void deger_ata_tur(int pid)
    {
      priidtur = proidana1 + proidana2; proidtur = pubidana1 + pubidana2; pubidtur = pid;
      cout << "siniftur değişkenlerine değer atama: " << priidtur << " " << proidtur << " " <<  pubidtur << endl;
    }
    void deger_goster_tur() { cout << "siniftur değişken değerleri: " << priidtur << " " << proidtur << " " << pubidtur << endl; }
};

int main(void)
{
  siniftur nes_tur(421, 897, 357, 726, 6542, 4537, 36, 951, 7534);

  cout << endl << "nes_tur değişkeninin sinifana1 ve sinifana2 elemanlarına doğrudan erişimi:" << endl;
  cout << "--------------------------------------------------------------------------" << endl;
  nes_tur.deger_goster1();
  nes_tur.deger_goster2();

  cout << endl << "nes_tur değişkeninin sinifana1, sinifana2 ve siniftur elemanlarına erişimi:" << endl;
  cout << "---------------------------------------------------------------------------" << endl;
  nes_tur.deger_goster_tur();

  cout << endl;

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

sinifana1 constructor fonksiyonu!
sinifana constructor fonksiyonu!
siniftur constructor fonksiyonu!

nes_tur değişkeninin sinifana1 ve sinifana2 elemanlarına doğrudan erişimi:
--------------------------------------------------------------------------
sinifana1 değişken değerleri: 726 6542 4537
sinifana2 değişken değerleri: 36 951 7534

nes_tur değişkeninin sinifana1, sinifana2 ve siniftur elemanlarına erişimi:
---------------------------------------------------------------------------
siniftur değişken değerleri: 421 897 357

siniftur destructor fonksiyonu!
sinifana2 destructor fonksiyonu!
sinifana1 destructor fonksiyonu!

```

Program, sinifana adlı bir sınıf ve bu sınıftan public olarak türetilen siniftur adlı bir sınıf oluşturur. Her iki sınıf içinde de private, protected ve public olmak üzere üç adet değişken ve bu değişkenlere değer atayan ve ekranda gösteren iki adet fonksiyon tanımlar.

Program çalışmaya başladığında, türetilmiş sınıf olan siniftur türünden nes\_tur adlı bir nesne oluşturur. Bu nesne oluşturulurken constructor fonksiyonuna dokuz adet parametre değeri geçirilir. Constructor fonksiyonuna geçirilen ilk üç parametre siniftur nesnesi için kullanılarak siniftur içindeki değişkenlere birer değer atanır. İkinci üç parametre, sinifana1 constructor fonksiyonuna aktarılarak, sinifana1 içindeki değişkenlere, üçüncü üç parametre ise, sinifana2 constructor fonksiyonuna aktarılarak, sinifana2 içindeki değişkenlere birer değer atanır.

Sonra, nes\_tur nesnesi yoluyla deger\_goster1() fonksiyonu ile sinifana1 değişken değerlerini, deger\_goster2() fonksiyonu ile sinifana2 değişken değerlerini ve siniftur sınıfı içindeki deger\_goster\_tur() fonksiyonu ile siniftur değişken değerlerini ekrana yazar.

## Kalıtımda sanal (virtual) ana sınıf tanımlamaları

Bir ana sınıftan türetilen iki farklı sınıfı ana sınıf kullanarak çoklu ana sınıf kalıtımı ile türetilen bir sınıf içinde ilk ana sınıfın iki kopyası olur. Bunun nedeni, ilk ana sınıfın elemanlarının kendisinden türetilen tüm sınıflara bir kopyasının aktarılmasıdır. Son olarak türetilen sınıf her iki sınıfa da erişim sağlayacağından, ilk ana sınıfa ait iki kopyayla karşılacaktır. Bu durum bir belirsizliğe yol açacaktır.

Aşağıdaki şekilde, sinifana sınıfından siniftur1 ve siniftur2 adlı iki adet sınıf public olarak türetilmiş, siniftur1 ve siniftur2 sınıfları ana sınıf olarak kullanılarak sinifturtur adlı sınıf yine public olarak türetilmiştir. Bu durumda, ana sınıf içindeki proidana protected değişkeni ile pubidana public değişkeni siniftur1 ve siniftur2 sınıflarına aynı erişim türü ile aktarılmıştır. Ancak, sinifturtur sınıfından bir nesne oluşturulduğunda, proidana ve pubidana değişkenlerinin, birisi siniftur1 üzerinden diğeri de siniftur2 üzerinden olmak üzere, aktarılan ikişer kopyası nesne üzerinde oluşacaktır. Bu durum, bir program içinde meydana geldiğinde, bir belirsizlik oluşturarak derleme hatası verecektir.

![](cprog/inhvirtual01.png)

Bu sorunu gidermek için sanal ana sınıf tanımlaması kullanılır. Sanal ana sınıf tanımlaması yapmak için virtual anahtar kelimesi ile yapılır. Yukarıdaki örnekte, sinifana sınıfından siniftur1 ve siniftur2 adlı iki adet sınıfı public olarak türetirken virtual anahtar kelimesini kullandığımızda, sinifturtur sınıfından bir nesne oluşturulduğunda, proidana ve pubidana değişkenlerinin sadece tek bir kopyası nesne üzerinde oluşacaktır. Böylece, programdaki belirsizlik ortadan kalkacağından, program normal bir şekilde çalışacaktır.

![](cprog/inhvirtual02.png)

Şimdi, bu özelliği bir örnek üzerinde incelemeye çalışalım:

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

class siniftur1 : virtual public sinifana {
  private:
    int priidtur1;

  protected:
    int proidtur1;

  public:
    int pubidtur1;
    void deger_ata_tur1(int pid1, int pid2)
    {
      priidtur1 = proidana + pubidana; proidtur1 = pid1; pubidtur1 = pid2;
      cout << "siniftur değişkenlerine değer atama: " << priidtur1 << " " << proidtur1 << " " <<  pubidtur1 << endl;
    }
    void deger_goster_tur1() { cout << "siniftur değişken değerleri: " << priidtur1 << " " << proidtur1 << " " << pubidtur1 << endl; }
};

class siniftur2 : virtual public sinifana {
  private:
    int priidtur2;

  protected:
    int proidtur2;

  public:
    int pubidtur2;
    void deger_ata_tur2(int pid1, int pid2)
    {
      priidtur2 = proidana + pubidana; proidtur2 = pid1; pubidtur2 = pid2;
      cout << "siniftur değişkenlerine değer atama: " << priidtur2 << " " << proidtur2 << " " <<  pubidtur2 << endl;
    }
    void deger_goster_tur2() { cout << "siniftur değişken değerleri: " << priidtur2 << " " << proidtur2 << " " << pubidtur2 << endl; }
};

class sinifturtur : public siniftur1, public siniftur2 {
  private:
    int priidturtur;

  protected:
    int proidturtur;

  public:
    int pubidturtur;
    void deger_ata_turtur(void)
    {
      priidturtur = proidana + pubidana; proidturtur = proidtur1+proidtur2; pubidturtur = pubidtur1+pubidtur2;
      cout << "sinifturtur değişkenlerine değer atama: " << priidturtur << " " << proidturtur << " " << pubidturtur << endl;
    }
    void deger_goster_turtur() { cout << "sinifturtur değişken değerleri: " << priidturtur << " " << proidturtur << " " << pubidturtur << endl; }
};

int main(void)
{
  sinifturtur nes_turtur;

  // siniftur1 ve siniftur2 sınıfları virtual olarak türetildiğinden,
  // sinifana içindeki protected ve public elemanların tek bir kopyası oluşur.
  cout << "nes_turtur değişkeninin sinifana elemanlarına erişimi:" << endl;
  cout << "------------------------------------------------------" << endl;
  nes_turtur.deger_ata(81, 138, 497);
  nes_turtur.deger_goster();

  cout << endl << "nes_turtur değişkeninin siniftur1 elemanlarına erişimi:" << endl;
  cout << "------------------------------------------------------" << endl;
  nes_turtur.deger_ata_tur1(15, 384);
  nes_turtur.deger_goster_tur1();

  cout << endl << "nes_turtur değişkeninin siniftur2 elemanlarına erişimi:" << endl;
  cout << "------------------------------------------------------" << endl;
  nes_turtur.deger_ata_tur2(95, 752);
  nes_turtur.deger_goster_tur2();

  cout << endl << "nes_turtur değişkeninin sinifturtur elemanlarına erişimi:" << endl;
  cout << "---------------------------------------------------------" << endl;
  nes_turtur.deger_ata_turtur();
  nes_turtur.deger_goster_turtur();

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

nes_turtur değişkeninin sinifana elemanlarına erişimi:
------------------------------------------------------
sinifana değişkenlerine değer atama: 81 138 497
sinifana değişken değerleri: 81 138 497

nes_turtur değişkeninin siniftur1 elemanlarına erişimi:
------------------------------------------------------
siniftur değişkenlerine değer atama: 635 15 384
siniftur değişken değerleri: 635 15 384

nes_turtur değişkeninin siniftur2 elemanlarına erişimi:
------------------------------------------------------
siniftur değişkenlerine değer atama: 635 95 752
siniftur değişken değerleri: 635 95 752

nes_turtur değişkeninin sinifturtur elemanlarına erişimi:
---------------------------------------------------------
sinifturtur değişkenlerine değer atama: 635 110 1136
sinifturtur değişken değerleri: 635 110 1136

```

Program, sinifana sınıfından siniftur1 ve siniftur2 adlı iki adet sınıfı public olarak türetirken virtual anahtar kelimesini kullanır. Sonra, siniftur1 ve siniftur2 sınıflarını ana sınıf olarak kullanarak sinifturtur adlı sınıfı yine public olarak türetir. Her üç sınıf içinde de private, protected ve public olmak üzere üç adet değişken ve bu değişkenlere değer atayan ve ekranda gösteren iki adet fonksiyon tanımlar.

Siniftur1 ve siniftur2 adlı sınıfları türetirken virtual anahtar kelimesini kullandığından, sinifturtur sınıfından bir nesne oluşturulduğunda, nes\_turtur değişkeni üzerinde ana sınıf içindeki elemanların sadece tek bir kopyası oluşur.

Program, çalışmaya başladığında, sinifturtur türünden nes\_turtur adlı bir nesne oluşturur. Bu nesne yoluyla ana sınıflar içindeki fonksiyonlara erişim sağlayarak, önce ana sınıf içindeki değişkenlere birer değer atar. Aynı nesne ile doğrudan ana sınıf içinde ki deger\_goster() fonksiyonu ile değişken değerlerini ekrana yazar.

Sonra, aynı nesne ile, deger\_ata\_tur1() ve deger\_ata\_tur2() fonksiyonları ile siniftur1 ve siniftur2 sınıflarının protected ve public değişkenlerine erişim sağlar ve bu değişken değerlerini kullanarak kendi değişkenlerine değer atar. Aynı nesne ile deger\_goster\_tur1() ve deger\_goster\_tur2() fonksiyonları ile değişken değerlerini ekrana yazar.

![](cprog/inhvirtual03.png)
 