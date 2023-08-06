---
title:  C++ Geçici veri türü dönüştürme (Casting)
author: sonsuz
date: 2023-08-06 23:40:00 +0300
categories: [Program,C++]
tags: [cpp,programlama,veri türü]
---


C++'da, bir veri türünü diğer bir veri türüne dönüştürerek kullanabiliriz. Veri türü dönüşümü adı verilen bu işlem iki farklı şekilde yapılabilir:

1. Üstü kapalı (Implicit) dönüştürme

2. Açık (Explicit) dönüştürme

Açık veri türü dönüştürme geçici veri türü dönüştürme (Type casting) olarak adlandırabiliriz. Çünkü, veri türü değiştirilen değişken değeri, farklı bir değişkene aktarılırken, kendi değeri aynı veri türünde kalmaktadır. 

## Üstü kapalı (Implicit) veri türü dönüştürme

Otomatik dönüştürme olarak ta bilinen üstü kapalı veri türü dönüştürme işlemi derleyici tarafından otomatik olarak yapılır.

Şimdi, bu özelliği bir örnek üzerinde incelemeye çalışalım:

Örnek

```cpp
#include <iostream>

using namespace std;

int main(void)
{
  int id = 21; // int bir değişkene ilk değer atama
  float fd; // float bir değişken bildirimi

  fd = id; // Üstü kapalı veri türü dönüştürme

  cout << "id = " << id << " fd = " << fd;

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

id değişken değeri: 21 fd değişken değeri: 21

```

Program, id adlı int bir değişken bildirimi yaparak 21 değerini atar ve fd adlı float bir değişken bildirimi yapar. id değişken değerini fd değişkenine atar. Bu atama işleminde üstü kapalı veri türü dönüştürme işlemi uygulanır. Böylece, int bir değişken değerini float veri türüne dönüştürerek, fd değişkenine atar. Sonra, değişken değerlerini ekrana yazar.

Şimdi, float veri türünden bir değişkenin int veri türüne dönüştürülmesini, bir örnek üzerinde incelemeye çalışalım:

Örnek

```cpp
#include <iostream>

using namespace std;

int main(void)
{
  float fd = 21.354; // float bir değişkene ilk değer atama
  int id; // int bir değişken bildirimi

  id = fd; // Üstü kapalı veri türü dönüştürme

  cout << "fd değişken değeri: " << fd << " id değişken değeri: " << id;

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

fd değişken değeri: 21.354 id değişken değeri: 21

```

Program, fd adlı float bir değişken bildirimi yaparak 21.354 değerini atar ve id adlı int bir değişken bildirimi yapar. fd değişken değerini id değişkenine atar. Bu atama işleminde üstü kapalı veri türü dönüştürme işlemi uygulanır. Böylece, float bir değişken değerini int veri türüne dönüştürerek, id değişkenine atar. Veri dönüştürme esnasında, float değişkeninin ondalık basamaklarında yer alan değerler otomatik olarak kesilir. Sonra, değişken değerlerini ekrana yazar.

## Açık (Explicit) veri türü dönüştürme (Type casting)

Bazen, programlarımızı oluştururken belirli veri türünde tanımladığımız değişkenleri geçici olarak farklı veri türüne dönüştürerek, dönüştürdüğümüz veri türünden tanımladığımız değişkenlere atama ihtiyacı duyabiliriz. Bu durumda, açık veri türü dönüştürme işlemi yapmamız gerekir.

C++'da, açık bir şekilde veri türü dönüştürme işlemi yapmak için aşağıda gösterilen üç farklı yöntemi kullanabiliriz:

1. () işlemcisi arasında veri türü adı kullanarak veri türü dönüştürme
2. Veri türünü fonksiyon adı gibi kullanarak veri türü dönüştürme
3. Veri türü değiştirme işlemcileri ile veri türü dönüştürme

## () işlemcisi arasında veri türü adı kullanarak veri türü dönüştürme

() işlemcisi arasında veri türü adı kullanarak, belirli veri türünü diğer bir veri türüne çevirebiliriz. Bu işlemi yapmak için kullanılan genel yapı aşağıda gösterilmektedir:

(veri-türü) ifade;

Yukarıdaki işlem satırında, ifade yerine bir değişken, sabit, değişken ve sabitlerle yapılan bir işlem, fonksiyon çağrısı gibi değerler gelebilir.

Bu özelliği bir program üzerinde incelemeye çalışalım:

Örnek

```cpp
#include <iostream>

using namespace std;

int main(void)
{
  double dd;
  int id;

  dd = 632.524;
  id = (int) dd; // () işlemcisi ile açık veri türü dönüştürme

  cout << "dd değişken değeri: " << dd << " id değişken değeri: " << id;

  return 0;
}


```

Yukarıdaki örnekte, program aşağıdaki satırı ekrana yazar:

```

dd değişken değeri: 632.524 id değişken değeri: 632

```

Program, dd adlı double ve id adlı int olmak üzere iki adet değişken bildirimi yapar. dd değişkenine 632.524 değerini atar. dd değişken değerini de id değişkenine atar. Bu atama işleminde açık veri türü dönüştürme işlemi uygulanır. Böylece, double bir değişken değerini int veri türüne dönüştürerek, id değişkenine atar. Veri dönüştürme esnasında, double değişkeninin ondalık basamaklarında yer alan değerler otomatik olarak kesilir. Sonra, değişken değerlerini ekrana yazar.

Bir atama işleminde, atama işaretinin sol tarafında type cast metodu kullanılamaz.

Şimdi, () işlemcisi arasında veri türü adı kullanarak, veri türü dönüştürme işlemi yapılmasını farklı bir örnek üzerinde incelemeye çalışalım:

Örnek

```cpp
#include <iostream>

using namespace std;

int main(void)
{
  double dd1 = 7.21;
  double dd2 = 15.12;
  double dd3;
  int id;

  // double değişken değerin ondalıklı kısmı otomatik olarak devre dışı kalır.
  id = dd1;
  cout << "id değişken değeri: " << id << "\n";

  id = (int) dd1;
  cout << "id değişken değeri: " << id << "\n";

  dd3 = dd1 + dd2;
  cout << "dd3 değişken değeri: " << dd3 << "\n";

  dd3 = (int) dd1 + dd2;
  cout << "dd3 değişken değeri: " << dd3 << "\n";

  dd3 = (int) dd1 + (int) dd2;
  cout << "dd3 değişken değeri: " << dd3 << "\n";

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımız zaman aşağıdaki ifadeleri ekrana yazar:

```

id değişken değeri: 7
id değişken değeri: 7
dd3 değişken değeri: 22.33
dd3 değişken değeri: 22.12
dd3 değişken değeri: 22

```

Program, üç adet double ve bir adet int değişken bildirimi yapar. Önce, dd1 değişken değerini atama işlemcisi ile id int değişkenine atar ve sonucu ekrana yazar. Bu atama işleminde, double değişken değerin ondalıklı kısmı otomatik olarak devre dışı kalır. Sonra, geçici veri türü dönüştürme işlemcisi ile dd1 değişken değerini atama işlemcisi ile tekrar id int değişkenine atar ve sonucu ekrana yazar. dd1 ve dd2 double değişken değerlerini toplayarak dd3 double değişkenine atar ve sonucu ekrana yazar. dd1 ve dd2 double değişken değerlerini toplayarak, iki defa dd3 double değişkenine atar ve sonucu ekrana yazar. Ancak, ilkinde dd1 değişken değerini ikincisinde ise, dd1 ve dd2 değişken değerlerini geçici veri türü dönüştürme işlemcisi ile int veri türüne çevirerek kullanır. int veri türüne çevrilen double değişken değerlerin ondalık kısmı devre dışı kalır.

## Veri türünü fonksiyon adı gibi kullanarak veri türü dönüştürme

Veri türünü fonksiyon adı gibi kullanarak, belirli veri türünü diğer bir veri türüne çevirebiliriz. Bu işlemi yapmak için kullanılan genel yapı aşağıda gösterilmektedir:

veri-türü (ifade);

Yukarıdaki işlem satırında, ifade yerine bir değişken, sabit, değişken ve sabitlerle yapılan bir işlem, fonksiyon çağrısı gibi değerler gelebilir.

Bu özelliği bir program üzerinde incelemeye çalışalım:

Örnek

```cpp
#include <iostream>

using namespace std;

int main(void)
{
  double dd;
  int id;

  dd = 17.21;
  id = int(dd) + int(dd); // veri türünü fonksiyon adı gibi kullanarak açık veri türü dönüştürme

  cout << "dd değişken değeri: " << dd << " id değişken değeri: " << id;

  return 0;
}


```

Yukarıdaki örnekte, program aşağıdaki satırı ekrana yazar:

```

dd değişken değeri: 17.21 id değişken değeri: 34

```

Program, dd adlı double ve id adlı int olmak üzere iki adet değişken bildirimi yapar. dd değişkenine 17.21 değerini atar. dd değişken değerini, veri türünü fonksiyon adı gibi kullanarak, iki kez açık veri türü dönüştürme işlemi uygular ve iki değerin toplamını id değişkenine atar. Veri dönüştürme esnasında, double değişkeninin ondalık basamaklarında yer alan değerler otomatik olarak kesilir. Sonra, değişken değerlerini ekrana yazar.

## Veri türü değiştirme işlemcileri ile veri türü dönüştürme

Aşağıda yer alan dört adet geçici veri türü dönüştürme işlemcisi ile de özel durumlara ait geçici veri değişimi yapabiliriz:

## const\_cast geçici veri türü dönüştürme işlemcisi

const\_cast işlemcisi, işlem yapılan nesnenin sabit ve/veya volatile özelliğini kaldırır veya yeniden kazandırır. Aslında, bir nesnenin const özelliğini kaldırma, o nesnenin bellekteki değerini değiştirmeden, sadece const olmayan bir değer kabul edilen bir ifade veya fonksiyon parametresinde kullanılmasını sağlar.

const\_cast işlemcisi;

* Sadece işaretçi ve referanslarla kullanılabilir.
* Sadece aynı veri türleri ile kullanılabilir.

const\_cast işlemcisi, const olarak tanımlanmış bir nesnenin ilk değerini hiç bir şekilde değiştiremez.

const\_cast veri türü dönüştürme işlemcisinin genel yapısı aşağıdadır:

const\_cast <veri-türü> (ifade)

veri-türü: İfade ile elde edilecek olan verinin geçici olarak çevrileceği veri türüdür.
ifade: Değişken, sabit ve işlemcilerden oluşan değerlerdir.

const\_cast işlemcisi, bir sabit nesnenin sabit durumunu doğrudan geçersiz kılmaz, sadece atanan veri türünün sabit olmayan bir şekilde tanımlanmasını sağlar.

Şimdi, const\_cast veri türü dönüştürme işlemcisinin int veri türü ile kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```cpp
#include <iostream>

using namespace std;

int kare_al(int *ip)
{
  return (*ip) * (*ip);
}

int main(void)
{
  const int id = 21;

  // kare_al() fonksiyonu const olmayan bir parametre gerektirdiğinden, hata verir.
  // kare_al(id);

  // id değişkeninin const özelliğini geçici olarak değiştirerek bellek adresini ip işaretçisin atar.
  // ip işaretçisi id değişken değerini değiştiremez, sadece const özelliği olmadan kullanılmasını sağlar.
  int *ip = const_cast<int*>(&id);

  // Aşağıdaki işlem satırları derleme işleminde hata vermez. Ancak, sonuçlar belirsiz olur.
  // ip ve &id ifadelerinin gösterdiği bellek adresi aynı olur, içerdiği değerler farklı olur.
  // *ip = 35;
  // cout << "ip işaretçisinin gösterdiği bellek adresi: " << ip << " değer: " << *ip << "\n";
  // cout << "id değişkeninin bellek adresi: " << &id << " değeri: " << id << "\n";

  // Fonksiyon normal bir int beklediğinden çalışır.
  cout << ip << " adresindeki " << *ip << " değerinin karesi: " << kare_al(ip);

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımız zaman aşağıdaki ifadeleri ekrana yazar:

```

0x6dfed8 adresindeki 21 değerinin karesi: 441

```

Program, önce int veri türünden bir adet const değişken tanımlar. Bu değişkenin referansını const\_cast işlemcisi ile int veri türünden bildirimi yapılan ip işaretçisine atar. Parametre olarak geçirilen int değerin karesini geri döndüren kare\_al() fonksiyonunu, const olmayan ip işaretçisi ile çağırır. Fonksiyon tarafından geri döndürülen değer ekrana yazılır.

Şimdi, const\_cast veri türü dönüştürme işlemcisinin char veri türü ile kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```cpp
#include <iostream>

using namespace std;

// Normal bir char işaretçi parametre alır.
void deger_goster(char *p)
{
  cout << p << "\n";
}

int main(void)
{
  const char *pdizi = "C++ Programlama Dili";

  // const char diziyi char bir diziye çevirme
  deger_goster(const_cast<char*> (pdizi));

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımız zaman aşağıdaki ifadeleri ekrana yazar:

```

C++ Programlama Dili

```

Program, önce char veri türünden bir adet const değişken tanımlayarak bir karakter dizisi atar. İşaretçi bildirimi yaparken, değişken adresini işaretçiye atar. Fonksiyonun beklediği değer normal char bir işaretçi olduğundan, const\_cast işlemcisini kullanarak, pdizi işaretçisini normal bir işaretçiye çevirir ve fonksiyonu çağırır. Fonksiyonun kendisine geçirilen değeri ekrana yazar.

## dynamic\_cast geçici veri türü dönüştürme işlemcisi

dynamic\_cast işlemcisi, sadece, en az bir adet sanal fonksiyon içeren sınıflardan oluşan, bir ana sınıf ve bu ana sınıftan türetilmiş sınıflarda, çok biçimlilik ile ilgili veri türü değişiklikleri yapmak için kullanılır. Bu çok biçimlilik sisteminde yer alan ve en az bir adet sanal fonksiyon içeren sınıfların herhangi birinden oluşturulan bir işaretçi veya nesne referansını yine aynı sistemde yer alan diğer bir sınıf işaretçi veya referansına dönüştürebiliriz.

dynamic\_cast veri türü dönüştürme işlemcisinin genel yapısı aşağıdadır:

dynamic\_cast <veri-türü> (ifade)

veri-türü: İfade ile elde edilecek olan verinin geçici olarak çevrileceği veri türüdür. İşaretçi veya referans veri türünden olmalıdır.
ifade: Değişken, sabit ve işlemcilerden oluşan değerlerdir. Elde edilen sonuç, işaretçi veya referans olmalıdır.

dynamic\_cast işlemcisi, bir veri türündeki işaretçinin diğer bir veri türüne, bir veri türündeki referansın da diğer bir veri türüne çevrilmesini sağlar.

dynamic\_cast işlemcisinin esas amacı, bir ana sınıf ve bu ana sınıftan türetilmiş sınıfların yer aldığı ve her sınıfın en az bir adet sanal fonksiyon içerdiği bir programda, herhangi bir sınıftan oluşturulmuş işaretçi ve referans değerler üzerinde geçici veri türü değişikliği yapmaktır.

Ana sınıf türünden tanımlanan işaretçiler, ana sınıftan oluşturulan veya ana sınıftan türetilen sınıflardan oluşturulan herhangi bir nesnenin adresini gösterebileceğinden, dynamic\_cast işlemcisi türetilmiş sınıf işaretçisini ana sınıf işaretçisine dönüştürebilir. Ancak, dynamic\_cast işlemcisi, sadece gösterilen nesne bir türetilmiş sınıf nesnesi ise, bir ana sınıf işaretçisini türetilmiş sınıf işaretçisine dönüştürebilir.

Dönüştürülecek olan işaretçi veya referans, hedef veri türünden bir nesne veya hedef veri türünden türetilen bir nesne ise, dynamic\_cast işlemi başarıyla sonuçlanır.

Dönüştürme işlemi başarısız olduğunda, işlem işaretçi ile yapılıyorsa, NULL sonuç elde edilir. Referans ile işlem yapılıyorsa, bir bad\_cast hata sonucu alınır.

Şimdi, dynamic\_cast veri türü dönüştürme işlemcisinin kullanılmasını örnekler üzerinde incelemeye çalışalım:

Örnek

```cpp
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

class siniftur : public sinifana {
  private:
    int priidtur;

  protected:
    int proidtur;

  public:
    int pubidtur;
    // Sanal fonksiyonun siniftur için yeniden tanımlanması
    void deger_topla(void) {
      cout << "siniftur değişken toplamları: "<< priidtur + proidtur + pubidtur << endl;
    }
    void deger_ata_tur(int pid1, int pid2, int pid3)
    {
      priidtur = pid1; proidtur = pid2; pubidtur = pid3;
      cout << "siniftur değişkenlerine değer atama: " << priidtur << " " << proidtur << " " <<  pubidtur << endl;
    }
    void deger_goster_tur() { cout << "siniftur değişken değerleri: " << priidtur << " " << proidtur << " " << pubidtur << endl; }
};

int main(void)
{
  sinifana *pnes_ana = new sinifana;
  siniftur *pnes_tur = new siniftur;

  cout << "pnes_ana işaretçisi ile nes_ana değişkeninin sinifana elemanlarına erişimi" << "\n";
  cout << "--------------------------------------------------------------------------" << "\n";
  pnes_ana->deger_ata(17, 874, 1345);
  pnes_ana->deger_goster();
  pnes_ana->deger_topla(); // Sanal fonksiyon

  cout << "\n";

  cout << "nes_tur değişkeninin siniftur elemanlarına erişimi" << "\n";
  cout << "--------------------------------------------------" << "\n";
  pnes_tur->deger_ata_tur(15, 74, 384);
  pnes_tur->deger_goster_tur();
  pnes_tur->deger_topla(); // Sanal fonksiyon

  cout << "\n";

  pnes_ana = pnes_tur; // Bu atama işlemi olmazsa, aşağıdaki her iki dynamic_cast işlemi de olumsuz sonuç verir.

  cout << "sinifana işaretçisinden siniftur işaretçisine dönüşüm işlemi" << "\n";
  cout << "------------------------------------------------------------" << "\n";
  pnes_tur = dynamic_cast<siniftur*> (pnes_ana);
  if(pnes_tur) {
     cout << "sinifana işaretçi -> siniftur işaretçi dönüşüm işlemi tamamlandı!\n";
     pnes_tur->deger_topla();
  }
  else cout << "sinifana işaretçi -> siniftur işaretçi dönüşüm hatası!" << "\n";

  cout << "\n";

  cout << "siniftur işaretçisinden sinifana işaretçisine dönüşüm işlemi" << "\n";
  cout << "------------------------------------------------------------" << "\n";
  pnes_ana = dynamic_cast<sinifana*> (pnes_tur);
  if(pnes_ana) {
     cout << "siniftur işaretçi -> sinifana işaretçi dönüşüm işlemi tamamlandı!\n";
     pnes_ana->deger_topla();
  }
  else cout << "siniftur işaretçi -> sinifana işaretçi dönüşüm hatası!" << "\n";

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımız zaman aşağıdaki ifadeleri ekrana yazar:

```

pnes_ana işaretçisi ile nes_ana değişkeninin sinifana elemanlarına erişimi
--------------------------------------------------------------------------
sinifana değişkenlerine değer atama: 17 874 1345
sinifana değişken değerleri: 17 874 1345
sinifana değişken toplamları: 2236

nes_tur değişkeninin siniftur elemanlarına erişimi
--------------------------------------------------
siniftur1 değişkenlerine değer atama: 15 74 384
siniftur değişken değerleri: 15 74 384
siniftur değişken toplamları: 473

sinifana işaretçisinden siniftur işaretçisine dönüşüm işlemi
------------------------------------------------------------
sinifana işaretçi -> siniftur işaretçi dönüşüm işlemi tamamlandı!
siniftur değişken toplamları: 473

siniftur işaretçisinden sinifana işaretçisine dönüşüm işlemi
------------------------------------------------------------
siniftur işaretçi -> sinifana işaretçi dönüşüm işlemi tamamlandı!
siniftur değişken toplamları: 473

```

Program, sinifana adlı bir sınıf ve bu sınıftan public olarak türetilen siniftur adlı bir sınıf oluşturur. Her iki sınıf içinde de private, protected ve public olmak üzere üç adet değişken ve bu değişkenlere değer atayan, ekranda gösteren ve değerlerini toplayan üç adet fonksiyon tanımlar. Sonra, sinifana türünden pnes\_ana adlı bir işaretçi ile siniftur türünden pnes\_tur adlı bir işaretçi oluşturur.

İlk olarak, pnes\_ana işaretçisi ile, sinifana içindeki deger\_ata() ve deger\_goster() fonksiyonları ile sinifana içindeki değişkenlere birer değer atar ve ekrana yazar. Sonra, sinifana içindeki deger\_topla() sanal fonksiyonunu kullanarak, sinifana içindeki değişken değerlerini toplar.

İkinci safhada, pnes\_tur işaretçisi siniftur içindeki deger\_ata\_tur() ve deger\_goster\_tur() fonksiyonları ile siniftur içindeki değişkenlere birer değer atar ve ekrana yazar. Sonra, siniftur içindeki deger\_topla() sanal fonksiyonunu kullanarak, siniftur içindeki değişken değerlerini toplar.

Sonra, pnes\_tur işaretçisini pnes\_ana işaretçisine atar. Bu atama işlemi olmazsa, dynamic\_cast işlemleri olumsuz sonuç verir

Önce, dynamic\_cast işlemcisini kullanarak, pnes\_ana işaretçisini siniftur türünden bir işaretçiye dönüştürerek pnes\_tur işaretçisine atar. İşaretçi ile siniftur içindeki deger\_topla() sanal fonksiyonunu kullanarak, siniftur içindeki değişken değerlerini toplar.

Sonra, dynamic\_cast işlemcisini kullanarak, pnes\_tur işaretçisini sinifana türünden bir işaretçiye dönüştürerek pnes\_ana işaretçisine atar. İşaretçi ile siniftur içindeki deger\_topla() sanal fonksiyonunu kullanarak, siniftur içindeki değişken değerlerini toplar.

Örnek

```cpp
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

class siniftur : public sinifana {
  private:
    int priidtur;

  protected:
    int proidtur;

  public:
    int pubidtur;
    // Sanal fonksiyonun siniftur için yeniden tanımlanması
    void deger_topla(void) {
      cout << "siniftur değişken toplamları: "<< priidtur + proidtur + pubidtur << endl;
    }
    void deger_ata_tur(int pid1, int pid2, int pid3)
    {
      priidtur = pid1; proidtur = pid2; pubidtur = pid3;
      cout << "siniftur değişkenlerine değer atama: " << priidtur << " " << proidtur << " " <<  pubidtur << endl;
    }
    void deger_goster_tur() { cout << "siniftur değişken değerleri: " << priidtur << " " << proidtur << " " << pubidtur << endl; }
};

int main(void)
{
  sinifana *pnes_ana, nes_ana;
  siniftur *pnes_tur, nes_tur;

  cout << "pnes_ana işaretçisi ile nes_ana değişkeninin sinifana elemanlarına erişimi" << "\n";
  cout << "--------------------------------------------------------------------------" << "\n";
  pnes_ana = &nes_ana;                // sinifana türünden işaretçi sinifana nesnesinin adresini gösteriyor.
  pnes_ana->deger_ata(17, 874, 1345);
  pnes_ana->deger_goster();
  pnes_ana->deger_topla();

  cout << "\n";

  cout << "nes_tur değişkeninin siniftur elemanlarına erişimi" << "\n";
  cout << "--------------------------------------------------" << "\n";
  nes_tur.deger_ata_tur(15, 74, 384);
  nes_tur.deger_goster_tur();
  nes_tur.deger_topla();

  cout << "\n";

  cout << "siniftur nesne referansından sinifana işaretçisine dönüşüm işlemi" << "\n";
  cout << "-----------------------------------------------------------------" << "\n";
  pnes_ana = dynamic_cast<sinifana*> (&nes_tur);
  if(pnes_ana) {
     cout << "siniftur nesne referansı -> sinifana işaretçi dönüşüm işlemi tamamlandı!\n";
     pnes_ana->deger_topla();
  }
  else cout << "siniftur nesne referansı -> sinifana işaretçi dönüşüm hatası!" << "\n";

  cout << "\n";

  cout << "sinifana nesne referansından siniftur işaretçisine dönüşüm işlemi" << "\n"; // hata
  cout << "-----------------------------------------------------------------" << "\n";
  pnes_tur = dynamic_cast<siniftur*> (&nes_ana);
  // Program buraya giriş yapmaz
  if(pnes_tur) {
     cout << "sinifana nesne referansı -> siniftur işaretçi dönüşüm işlemi tamamlandı!\n";
     pnes_tur->deger_topla();
  }
  else cout << "sinifana nesne referansı -> siniftur işaretçi dönüşüm hatası!" << "\n";

  cout << "\n";

  cout << "sinifana işaretçisinden siniftur işaretçisine dönüşüm işlemi" << "\n";
  cout << "------------------------------------------------------------" << "\n";
  pnes_ana = &nes_tur; // Ana sınıf işaretçisi türetilen sınıf nesnesini gösteriyor.
  pnes_tur = dynamic_cast<siniftur*> (pnes_ana);
  if(pnes_tur) {
     cout << "sinifana işaretçi -> siniftur işaretçi dönüşüm işlemi tamamlandı!\n";
     pnes_tur->deger_topla();
  }
  else cout << "sinifana işaretçi -> siniftur işaretçi dönüşüm hatası!" << "\n";

  cout << "\n";

  cout << "sinifana işaretçisinden siniftur işaretçisine dönüşüm işlemi" << "\n";  // hata
  cout << "------------------------------------------------------------" << "\n";
  pnes_ana = &nes_ana; // Ana sınıf işaretçisi ana sınıf nesnesini gösteriyor.
  pnes_tur = dynamic_cast<siniftur*> (pnes_ana);
  // Program buraya giriş yapmaz
  if(pnes_tur) {
     cout << "sinifana işaretçi -> siniftur işaretçi dönüşüm işlemi tamamlandı!\n";
     pnes_tur->deger_topla();
  }
  else cout << "sinifana işaretçi -> siniftur işaretçi dönüşüm hatası!" << "\n";

  cout << "\n";

  cout << "sinifana işaretçisinden siniftur işaretçisine dönüşüm işlemi" << "\n";
  cout << "------------------------------------------------------------" << "\n";
  pnes_tur = &nes_tur; // Türetilmiş sınıf işaretçisi türetilmiş sınıf nesnesini gösteriyor.
  pnes_ana = dynamic_cast<sinifana*> (pnes_tur);
  if(pnes_ana) {
     cout << "sinifana işaretçi -> siniftur işaretçi dönüşüm işlemi tamamlandı!\n";
     pnes_ana->deger_topla();
  }
  else cout << "siniftur işaretçi -> sinifana işaretçi dönüşüm hatası!" << "\n";

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımız zaman aşağıdaki ifadeleri ekrana yazar:

```

pnes_ana işaretçisi ile nes_ana değişkeninin sinifana elemanlarına erişimi
--------------------------------------------------------------------------
sinifana değişkenlerine değer atama: 17 874 1345
sinifana değişken değerleri: 17 874 1345
sinifana değişken toplamları: 2236

nes_tur değişkeninin siniftur elemanlarına erişimi
--------------------------------------------------
siniftur1 değişkenlerine değer atama: 15 74 384
siniftur değişken değerleri: 15 74 384
siniftur değişken toplamları: 473

siniftur nesne referansından sinifana işaretçisine dönüşüm işlemi
-----------------------------------------------------------------
siniftur nesne referansı -> sinifana işaretçi dönüşüm işlemi tamamlandı!
siniftur değişken toplamları: 473

sinifana nesne referansından siniftur işaretçisine dönüşüm işlemi
-----------------------------------------------------------------
sinifana nesne referansı -> siniftur işaretçi dönüşüm hatası!

sinifana işaretçisinden siniftur işaretçisine dönüşüm işlemi
------------------------------------------------------------
sinifana işaretçi -> siniftur işaretçi dönüşüm işlemi tamamlandı!
siniftur değişken toplamları: 473

sinifana işaretçisinden siniftur işaretçisine dönüşüm işlemi
------------------------------------------------------------
sinifana işaretçi -> siniftur işaretçi dönüşüm hatası!

sinifana işaretçisinden siniftur işaretçisine dönüşüm işlemi
------------------------------------------------------------
sinifana işaretçi -> siniftur işaretçi dönüşüm işlemi tamamlandı!
siniftur değişken toplamları: 473

```

Program, sinifana adlı bir sınıf ve bu sınıftan public olarak türetilen siniftur adlı bir sınıf oluşturur. Her iki sınıf içinde de private, protected ve public olmak üzere üç adet değişken ve bu değişkenlere değer atayan, ekranda gösteren ve değerlerini toplayan üç adet fonksiyon tanımlar. Sonra, sinifana türünden pnes\_ana adlı bir işaretçi ve nes\_ana adlı bir nesne ile siniftur türünden pnes\_tur adlı bir işaretçi ve nes\_tur adlı bir nesne oluşturur.

İlk olarak, nes\_ana nesnesinin bellek adresini pnes\_ana işaretçisine atar. Bu işaretçi ile, sinifana içindeki deger\_ata() ve deger\_goster() fonksiyonları ile sinifana içindeki değişkenlere birer değer atar ve ekrana yazar. Sonra, sinifana içindeki deger\_topla() sanal fonksiyonunu kullanarak, sinifana içindeki değişken değerlerini toplar.

İkinci safhada, nes\_tur nesnesi yoluyla siniftur içindeki deger\_ata\_tur() ve deger\_goster\_tur() fonksiyonları ile siniftur içindeki değişkenlere birer değer atar ve ekrana yazar. Sonra, siniftur içindeki deger\_topla() sanal fonksiyonunu kullanarak, siniftur içindeki değişken değerlerini toplar.

Üçüncü safhada, dynamic\_cast işlemcisini kullanarak, nes\_tur nesnesinin referansını sinifana türünden bir işaretçiye dönüştürerek pnes\_ana işaretçisine atar. İşaretçi ile siniftur içindeki deger\_topla() sanal fonksiyonunu kullanarak, siniftur içindeki değişken değerlerini toplar.

Dördüncü safhada, dynamic\_cast işlemcisini kullanarak, nes\_ana nesnesinin referansını siniftur türünden bir işaretçiye dönüştürerek pnes\_tur işaretçisine atamaya çalışır. Ancak, işlem hata verir.

Beşinci safhada, nes\_tur nesnesinin bellek adresini pnes\_ana işaretçisine atar. Sonra, dynamic\_cast işlemcisini kullanarak, pnes\_ana işaretçisini siniftur türünden bir işaretçiye dönüştürerek pnes\_tur işaretçisine atar. İşaretçi ile siniftur içindeki deger\_topla() sanal fonksiyonunu kullanarak, siniftur içindeki değişken değerlerini toplar.

Altıncı safhada, nes\_ana nesnesinin bellek adresini pnes\_ana işaretçisine atar. Sonra, dynamic\_cast işlemcisini kullanarak, pnes\_ana işaretçisini siniftur türünden bir işaretçiye dönüştürerek pnes\_tur işaretçisine atamaya çalışır. Ancak, işlem hata verir.

Son safhada, nes\_tur nesnesinin bellek adresini pnes\_tur işaretçisine atar. Sonra, dynamic\_cast işlemcisini kullanarak, pnes\_tur işaretçisini sinifana türünden bir işaretçiye dönüştürerek pnes\_ana işaretçisine atar. İşaretçi ile siniftur içindeki deger\_topla() sanal fonksiyonunu kullanarak, siniftur içindeki değişken değerlerini toplar.

Programda, dynamic\_cast işleminde, nesne referanslarını sınıf işaretçilerine dönüştürme işleminden önce herhangi bir atama işlemine gerek duyulmamaktadır. Ancak, sınıf işaretçilerinin diğer bir sınıf işaretçisine dönüştürme işleminden önce, bir nesne bellek adresinin dönüştürülecek veri türünün atanacağı işaretçiye atanması gerekir.

## reinterpret\_cast geçici veri türü dönüştürme işlemcisi

reinterpret\_cast işlemcisi bir veri türünü tamamen farklı bir veri türüne dönüştürür.

reinterpret\_cast veri türü dönüştürme işlemcisinin genel yapısı aşağıdadır:

reinterpret\_cast <veri-türü> (ifade)

veri-türü: İfade ile elde edilecek olan verinin çevrileceği veri türüdür.
ifade: Değişken, sabit ve işlemcilerden oluşan değerlerdir. Çevrilecek olan veri türünü gösterir.

Şimdi, reinterpret\_cast veri türü dönüştürme işlemcisinin kullanılmasını örnekler üzerinde incelemeye çalışalım:

Örnek

```cpp
#include <iostream>

using namespace std;

int main(void)
{
  int id = 121;
  int *ip;

  // Bu işlem satırı hata verir. Normal koşullarda id değişkeninin adresi işaretçiye atanır.
  // ip = id;
  ip = reinterpret_cast<int*>(id);

  // Onaltılık sayı sisteminde 0x79 (121) değerini ekrana yazar.
  cout << "id değişken değeri: " << ip << " " << id;

  // Bu işlem satırı hata verir. ip işaretçisi normal olarak bir değişkenin adresini gösterirken
  // bu durumda id değişken değerini göstermektedir.
  // cout << *ip;

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımız zaman aşağıdaki ifadeleri ekrana yazar:

```

id değişken değeri: 0x79 121

```

Program, int veri türünden bir değişken ve bir işaretçi oluşturur. Değişkenin int veri türünü, reinterpret\_cast işlemcisini kullanarak int işaretçi veri türüne dönüştürür. Sonra, id değişken değerini işaretçi ve int değişken yoluyla ekrana yazar.

Şimdi, int bir işaretçisinin char bir işaretçiye, int bir değerin int bir işaretçiye ve int bir işaretçinin long int bir değişkene dönüştürülmesini bir örnek üzerinde incelemeye çalışalım:

Örnek

```cpp
#include <iostream>

using namespace std;

int main(void)
{
  int id=65;
  int *ip;

  ip = &id

  // Farklı veri türünde işaretçiler arasında dönüşüm
  char *cp = reinterpret_cast<char*>(ip);
  cout << *cp << "\n";

  // Bir veri türünü aynı veri türünden bir işaretçiye dönüştürme
  int *ip2 = reinterpret_cast<int*>(id);
  cout << ip2 << "\n";

  // Bir işaretçiden bir veri türüne dönüşüm
  long int lid = reinterpret_cast<long>(ip2);
  cout << lid << "\n";

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımız zaman aşağıdaki ifadeleri ekrana yazar:

```

A
0x41
65

```

Program, int veri türünden bir değişken ve bir işaretçi oluşturur. Değişkenin bellek adresini işaretçiye atar. Veri türü int olan ip işaretçisini reinterpret\_cast işlemcisi ile cp adlı char bir işaretçiye dönüştürür. cp işaretçisinin gösterdiği bellekte yer alan değeri ekrana yazar. Sonra, id değişkeninin veri türünü int bir işaretçiye dönüştürerek ip2 işaretçisine atar ve ip2 değerini ekrana yazar. Daha sonra, ip2 int işaretçisini long int veri türüne dönüştürerek lid değişkenine atar ve lid değerini ekrana yazar.

## static\_cast geçici veri türü dönüştürme işlemcisi

Normal geçici veri türü dönüştürme işlemcisi yerine kullanılan bir işlemci olup herhangi bir standart veri türü dönüştürme işlemi yapılabilir.

static\_cast veri türü dönüştürme işlemcisinin genel yapısı aşağıdadır:

static\_cast <veri-türü> (ifade)

veri-türü: İfade ile elde edilecek olan verinin çevrileceği veri türüdür.
ifade: Değişken, sabit ve işlemcilerden oluşan değerlerdir. Çevrilecek olan veri türünü gösterir.

Şimdi, static\_cast veri türü dönüştürme işlemcisinin kullanılmasını örnekler üzerinde incelemeye çalışalım:

Örnek

```cpp
#include <iostream>

using namespace std;

int main(void)
{
  double dd1 = 7.21;
  double dd2 = 15.12;
  double dd3;

  dd3 = (int) dd1 + dd2;
  cout << "dd3 değişken değeri: " << dd3 <<  "\n";

  dd3 = static_cast<int>(dd1) + dd2;
  cout << "dd3 değişken değeri: " << dd3;

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımız zaman aşağıdaki ifadeleri ekrana yazar:

```

dd3 değişken değeri: 22.12
dd3 değişken değeri: 22.12

```

Program, üç adet double değişken bildirimi yapar. Önce, dd1 ve dd2 double değişken değerlerini toplayarak dd3 double değişkenine atar ve sonucu ekrana yazar. dd1 değişkenini geçici veri türü dönüştürme işlemcisi ile int veri türüne çevirerek kullanır. Sonra dd1 ve dd2 double değişken değerlerini toplayarak dd3 double değişkenine atar ve sonucu ekrana yazar. Ancak, bu defa dd1 değişkenini static\_cast işlemcisi ile int veri türüne çevirerek kullanır.

## İfadelerde veri türü değişimi

C++'da, bir ifade içinde birbirinden veri türleri kullandığımızda, bu ifade ile elde edilen sonucun veri türü otomatik olarak belirlenmektedir.

Otomatik veri çeşidi değişimleri yapıldıktan sonra, program ifadelerde yer alan bütün verileri aynı ifade içindeki en büyük verinin çeşidine çevirir. Bu işlem aşağıda belirtilen kurallara göre yapılır:

```


İlk veri çeşidi      Diğer verilerin çeşidi     Elde edilen veri çeşidi

long double          ..........                 long double
double               ..........                 double
float                ..........                 float
unsigned long        ..........                 unsigned long
long                 ..........                 long
unsigned int         ..........                 unsigned int


```

Yukarıdaki kurala göre, bir ifade içinde long double bir veri türü yer alıyorsa, diğer verilerin türlerine bakılmaksızın, elde edilen sonuç long double veri türünden olacaktır.

Şimdi, öğrendiklerimizi örnekler üzerinde incelemeye çalışalım:

Örnek

```cpp
#include <iostream>

using namespace std;

int main(void)
{
  unsigned int uid;
  float fd;

  uid = 21;
  fd = 345.74;

  cout << uid*fd; // İfade sonucu otomatik olarak float veri türüne dönüşür.

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

7260.54

```

Program, unsigned int bir değerle float bir değerin çarpımını ekrana yazar. C++'da uygulanan veri türü dönüştürme kurallarına göre program float ve unsigned int değerleri aynı ifade içinde kullandığında, sonucu float veri türünden verir.

Örnek

```cpp
#include <iostream>

using namespace std;

int main(void)
{
  int id1=24, id2=2;
  double dd=65;

  cout << dd/(id1/id2); // İfade sonucu otomatik olarak double veri türüne dönüşür.

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

5.41667

```

Progam, id1 ve id2 adlı iki adet int ve dd adlı bir adet double veri türünden değişken tanımlar. dd değişken değerini id1 değişkenini id2 değişkenine bölerek elde ettiği sonuca böler. Elde edilen sonuç double veri türünden olur.
