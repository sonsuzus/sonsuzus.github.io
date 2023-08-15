---
title:  C++ Sınıf şablonları
author: sonsuz
date: 2023-08-15 21:48:48 +0300
categories: [Program,C++]
tags: [cpp,programlama,sınıf,şablonlar]
---

Şablon sınıflar oluşturmak için, bir sınıf içinde kullanılan değişkenlerin en az bir tanesini veri türü değişken parametre olarak tanımlamak gerekir. Veri türü değişken parametreleri sınıf içindeki fonksiyonlarda aynı kodlarla kullanabilir.

Şablon sınıftan bir nesne oluşturulurken, sınıfa parametre olarak geçirilecek değişkenlerin veri türü belirlenir.

Bir sınıf şablonları, farklı veri türlerine aynı kodlarla işlem yapılmasına olanak sağladığından, büyük kolaylık sağlar.

Bir sınıf şablonu da fonksiyon şablonu gibi template ve typename anahtar kelimeleri ile oluşturulur. Sınıf şablonu bildirimi için kullanılan genel yapı aşağıda gösterilmektedir:

```

template <typename T> class sınıf-adı {
  // Sınıf içi değişken ve fonksiyon bildirimleri
}

```

Sınıf şablon bildiriminde typename yerine class anahtar kelimesi de kullanılabilir. Her iki anahtar kelime de aynı işlemi yapar.

Burada T ifadesi, sınıf tarafından kullanılan bir veri türü için bir yer tutucu adını gösterir. Bu isim, sınıf bildiriminde en az bir adet olmak üzere kullanılır. Şablon sınıftan bir nesne oluşturulurken veri türü belirlendiğinden, derleyici sınıfın kopyasını bu veri türüne göre oluşturur.

Şablon sınıfının bildirimi yapıldıktan sonra, aşağıdaki şekilde nesne oluşturulur:

```

// Tek veri türü ile parametre geçirilen sınıf bildirimi 
sınıf-adı <T> nesne_adı;

// Çoklu veri türü ile parametre geçirilen sınıf bildirimi 
sınıf-adı <T1, T2, ...> nesne_adı;

```

## Tek parametre değeri alan şablon sınıflar

Şablon sınıf bildiriminde sadece tek parametre kullandığımızda, şablon sınıftan her nesne üretilmesinde sadece tek bir veri türü tanımlanır. Sınıf kopyası içinde sadece bu veri türü değişken olarak kullanılabilir.

Aynı veri türünden private, protected ve public değişkenlere işlem yapan fonksiyonlar içeren bir şablon sınıfının kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

template <typename t> class sinif {

  private:
    t priid;

  protected:
    t proid;

  public:
    t pubid;
    void deger_ata(t pid1, t pid2, t pid3)
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
  sinif <int> nes1;

  nes1.deger_ata(121, 745, 1059);
  nes1.deger_goster();

  sinif <float> nes2;

  nes2.deger_ata(72.21f, 1084.47f, 1273.85f);
  nes2.deger_goster();

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

sinif değişkenlerine değer atama: 121 745 1059
sinif değişken değerleri: 121 745 1059
sinif değişkenlerine değer atama: 72.21 1084.47 1273.85
sinif değişken değerleri: 72.21 1084.47 1273.85

```

Program, önce tek bir veri türünün parametre olarak geçirildiği bir sınıf tanımlar. Tanımladığı sinif türünden nes1 nesnesini oluştururken int veri türünü parametre olarak sınıfa geçirir. Sınıf içindeki deger\_ata() fonksiyonu ile tüm değişkenlere bir değer atar ve deger\_goster() fonksiyonu ile değişken değerlerini ekrana yazar. Aynı işlemleri nes2 nesnesini tanımlarken float veri türü ile yapar.

## Farklı veri türünde çoklu parametre değeri alan şablon sınıflar

Şablon sınıf bildiriminde birden fazla veri türü için parametre kullandığımızda, sınıf içinde birden fazla değişkenin veri türü nesne oluşturulması ile belirlenebilir.

İki farklı veri türünden private, protected ve public değişkenlere işlem yapan fonksiyonlar içeren bir şablon sınıfının kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

template <typename t1, typename t2> class sinif {

  private:
    t1 priid1;
    t2 priid2;

  protected:
    t1 proid1;
    t2 proid2;

  public:
    t1 pubid1;
    t2 pubid2;

    void deger_ata(t1 pid1, t1 pid2, t1 pid3, t2 pid4, t2 pid5, t2 pid6)
    {
      priid1 = pid1; proid1 = pid2; pubid1 = pid3;
      priid2 = pid4; proid2 = pid5; pubid2 = pid6;
    }

    void deger_goster()
    {
      cout << "sinif t1 değişken değerleri: " << priid1 << " " << proid1 << " " << pubid1 << endl;
      cout << "sinif t2 değişken değerleri: " << priid2 << " " << proid2 << " " << pubid2 << endl;
    }
};

int main(void)
{
  sinif <int, int> nes1;

  nes1.deger_ata(246, 526, 1254, 4315, 5873, 10951);
  nes1.deger_goster();

  cout << endl;

  sinif <float, float> nes2;

  nes2.deger_ata(841.12f, 1754.21f, 2482.95f, 321.85f, 9432.47f, 11544.21f);
  nes2.deger_goster();

  cout << endl;

  sinif <int, float> nes3;

  nes3.deger_ata(357, 9421, 44625, 742.13f, 1412.54f, 3475.24f);
  nes3.deger_goster();

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

sinif t1 değişken değerleri: 246 526 1254
sinif t2 değişken değerleri: 4315 5873 10951

sinif t1 değişken değerleri: 841.12 1754.21 2482.95
sinif t2 değişken değerleri: 321.85 9432.47 11544.21

sinif t1 değişken değerleri: 357 9421 44625
sinif t2 değişken değerleri: 742.13 1412.54 3475.24

```

Program, önce iki farklı veri türünün parametre olarak geçirildiği bir sınıf tanımlar. Tanımladığı sinif türünden nes1 nesnesini oluştururken her iki parametre için de int veri türünü sınıfa geçirir. Sınıf içindeki deger\_ata() fonksiyonu ile tüm değişkenlere bir değer atar ve deger\_goster() fonksiyonu ile değişken değerlerini ekrana yazar. Aynı işlemleri nes2 nesnesini tanımlarken bu kez float veri türü ile yapar. Son olarak, nes2 nesnesini tanımlarken ilk veri türü olarak int ikinci veri türü olarak float değerleri sınıfa geçirir ve fonksiyonlarla değer atama ve ekrana yazdırma işlemlerini yapar.

## Şablon sınıflarda sabit veri türü parametreleri

Normal koşullarda, şablon sınıflar parametrelerinin veri türlerini, kullanıcıların sınıflar için oluşturdukları nesnelerin bildiriminde kullandıkları veri türüne uygun olarak belirler ve verilere uygun olan sınıf kopyası içinde işlem yaparlar. Ancak, bazı durumlarda, şablon sınıflara değişken veri türüne sahip parametrelerin yanı sıra sabit bir veri türünden parametre değeri geçirmek gerekebilir. Şablon sınıf bildiriminde bu şekildeki parametreler için belirli bir veri türünden tanımlama yapılır.

Sabit veri türü içeren sınıf şablonu bildirimi için kullanılan genel yapı aşağıda gösterilmektedir:

```

template <typename T, veri-türü değişken-adı> class sınıf-adı {
  // Sınıf içi değişken ve fonksiyon bildirimleri
}

```

Şablon sınıfının bildirimi yapıldıktan sonra, aşağıdaki şekilde nesne oluşturulur:

```

sınıf-adı <T, sabit-değer> nesne_adı;

```

Şablon sınıf bildiriminde kullanılan sabit veri türü parametreleri

* sadece int, işaretçi veya referans değerler olarak tanımlanabilir.
* sadece bir int sabiti, global bir fonksiyonu veya nesneyi gösteren bir işaretçiyi veya referansı değer olarak alabilir.
* nesne oluşturma esnasında sabit bir değer alır.
* sabit değerler içerdiğinden değerleri değiştirilemez.

Kendisine geçirilen bir adet değişken ve bir adet sabit veri türündeki parametrelerle işlem yapan bir şablon sınıfın kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

template <typename t, int power> class sinif {

  private:
    t priid;

  public:
    t pubid;

    void bg_pow(t x)
    {
      t sonuc;
      int id;

      priid = x;

      if (power==0) sonuc = 1;
      else {
         sonuc = x;
         for (id=2; id<=power; id++) sonuc *= x;
      }	  

      pubid = sonuc;

      cout << x << " değerinin " << power << ". kuvveti = " << sonuc << endl;
    }

    void deger_goster()
    {
      cout << priid << " sayısının " << power << ". kuvveti = " << pubid << endl;
    }
};

int main(void)
{
  sinif <int, 2> nes1;

  nes1.bg_pow(5);
  nes1.deger_goster();

  sinif <float, 4> nes2;

  nes2.bg_pow(6.25);
  nes2.deger_goster();

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

5 değerinin 2. kuvveti = 25
5 sayısının 2. kuvveti = 25
6.25 değerinin 4. kuvveti = 1525.88
6.25 sayısının 4. kuvveti = 1525.88

```

Program, önce bir değişken veri türü ile sabit değerin parametre olarak geçirildiği bir sınıf tanımlar. Tanımladığı sinif türünden nes1 nesnesini oluştururken değişken veri türü olarak int, ikinci parametre değeri olarak 2 sabit değerini sınıfın kopyasına geçirir. Sınıf içindeki bg\_pow() fonksiyonuna 5 değerini geçirerek 5 sayısının 2.kuvvetini alarak ekrana yazar. Sonra, deger\_goster() fonksiyonunu kullanarak aynı değerleri tekrar ekrana yazar. İkinci kez sinif türünden nes2 nesnesi oluştururken değişken veri türü olarak float, ikinci parametre değeri olarak 4 sabit değerini sınıfın kopyasına geçirir. Sınıf içindeki bg\_pow() fonksiyonuna 6.25 değerini geçirerek 6.25 sayısının 4.kuvvetini alarak ekrana yazar. Sonra, deger\_goster() fonksiyonunu kullanarak aynı değerleri tekrar ekrana yazar.

Şablon sınıfı sinif türünden nesne oluştururken ikinci parametre ile aktarılan int sabit değeri bg\_pow() fonksiyonu içinde sayının kaçıncı kuvvetinin alınacağını gösteren power değeridir.

## Şablon sınıflarda ön tanımlı parametre kullanımı

Şablon sınıfların bildirimi yapılırken kullanılan değişken ve sabit veri türündeki parametrelere ön tanımlı değerler verilebilir. Bu durumda, değişken veri türündeki parametrelere veri türü sabit veri türündeki parametrelere ise sabit değer ön tanımlı değer olarak verilir.

Ön tanımlı değer verilen değişken ve sabit veri türü içeren sınıf şablonu bildirimi için kullanılan genel yapı aşağıda gösterilmektedir:

```

template <typename T=veri-türü, veri-türü değişken-adı=sabit-değer> class sınıf-adı {
  // Sınıf içi değişken ve fonksiyon bildirimleri
}

```

Şablon sınıfının bildirimi yapıldıktan sonra, üç farklı şekilde nesne oluşturulabilir:

```

sınıf-adı <T, sabit-değer> nesne_adı; // Her iki parametre için ön tanımlı değer atama

sınıf-adı <T> nesne_adı; // Sadece değişken veri türü için ön tanımlı değer atama

sınıf-adı <> nesne_adı; // Ön tanımlı değer kullanmadan nesne oluşturma

```

Kendisine geçirilen bir adet değişken ve bir adet sabit veri türündeki parametrelerle işlem yapan bir şablon sınıfın kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

template <typename t=int, int power=2> class sinif {

  private:
    t priid;

  public:
    t pubid;

    void bg_pow(t x)
    {
      t sonuc;
      int id;

      priid = x;

      if (power==0) sonuc = 1;
      else {
         sonuc = x;
         for (id=2; id<=power; id++) sonuc *= x;
      }

      pubid = sonuc;

      cout << x << " değerinin " << power << ". kuvveti = " << sonuc << endl;
    }

    void deger_goster()
    {
      cout << priid << " sayısının " << power << ". kuvveti = " << pubid << endl;
    }
};

int main(void)
{
  sinif <float, 3> nes1; // float veri türü ve 3 sabit değeri tanımlı

  nes1.bg_pow(4.25);     // 4.25 sayısının 3.kuvvetini alır.
  nes1.deger_goster();

  cout << endl;

  sinif <double> nes2;   // sadece int veri türü tanımlı, 2 sabit değeri ön tanımlı

  nes2.bg_pow(5.75);     // 5.75 sayısının 2.kuvvetini alır.
  nes2.deger_goster();

  cout << endl;

  sinif <> nes3;         // Değişken veri türü int, sabit değer 2 olarak ön tanımlı

  nes3.bg_pow(7);        // 7 sayısının 2.kuvvetini alır.
  nes3.deger_goster();

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

4.25 değerinin 3. kuvveti = 76.7656
4.25 sayısının 3. kuvveti = 76.7656

5.75 değerinin 2. kuvveti = 33.0625
5.75 sayısının 2. kuvveti = 33.0625

7 değerinin 2. kuvveti = 49
7 sayısının 2. kuvveti = 49

```

Program, önce bir değişken veri türü ile sabit değerin parametre olarak geçirildiği bir sınıfı, int veri türünü ve 2 sabit değerini ön tanımlı değer vererek tanımlar. Tanımladığı sinif türünden nes1 nesnesini oluştururken değişken veri türü olarak float, ikinci parametre değeri olarak 3 sabit değerini sınıfın kopyasına geçirir. Sınıf içindeki bg\_pow() fonksiyonuna 4.25 değerini geçirerek 4.25 sayısının 3.kuvvetini alarak ekrana yazar. Sonra, deger\_goster() fonksiyonunu kullanarak aynı değerleri tekrar ekrana yazar. İkinci kez sinif türünden nes2 nesnesi oluştururken değişken veri türü olarak double değerini sınıfın kopyasına geçirir. Sınıf için ön tanımlı sabit değer 2 olduğundan, sınıf içindeki bg\_pow() fonksiyonuna 5.75 değerini geçirerek 5.75 sayısının 2.kuvvetini alarak ekrana yazar. Sonra, deger\_goster() fonksiyonunu kullanarak aynı değerleri tekrar ekrana yazar. Son olarak, sinif türünden nes3 nesnesi oluştururken herhangi bir parametre tanımlamaz. Sınıf için ön tanımlı değişken veri türü int ve sabit değer 2 olduğundan, sınıf içindeki bg\_pow() fonksiyonuna 7 değerini geçirerek 7 sayısının 2.kuvvetini alarak ekrana yazar. Sonra, deger\_goster() fonksiyonunu kullanarak aynı değerleri tekrar ekrana yazar.

Kendisine geçirilen bir adet değişken ve bir adet sabit veri türündeki parametrelerle işlem yapan bir şablon sınıfın karakter dizileriyle kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

template <typename t=int, int repeat=1> class sinif {

  public:
    void veri_goster(t x)
    {
      int id;

      for (id=0; id<repeat; id++) cout << x << " ";

      cout << endl;
    }
};

int main(void)
{
  char cdizi[]="Sınıf şablonları";
  sinif <char*, 3> nes1;

  nes1.veri_goster(cdizi);

  sinif <float, 5> nes2;
  nes2.veri_goster(7.25);

  sinif <int, 10> nes3;
  nes3.veri_goster(21);

  sinif <> nes4;
  nes4.veri_goster(1079);

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Sınıf şablonları Sınıf şablonları Sınıf şablonları 
7.25 7.25 7.25 7.25 7.25 
21 21 21 21 21 21 21 21 21 21 
1079 

```

Program, önce bir değişken veri türü ile sabit değerin parametre olarak geçirildiği bir sınıfı, int veri türünü ve 1 sabit değerini ön tanımlı değer vererek tanımlar. Tanımladığı sinif türünden nes1 nesnesini oluştururken değişken veri türü olarak char\*, ikinci parametre değeri olarak 3 sabit değerini sınıfın kopyasına geçirir. Sınıf içindeki veri\_goster() fonksiyonuna bir karakter dizisi geçirerek 3 defa ekrana yazar. İkinci kez sinif türünden nes2 nesnesi oluştururken değişken veri türü olarak float ve sabit değer olarak 5 değerini sınıfın kopyasına geçirir. Sınıf içindeki veri\_goster() fonksiyonuna 7.25 değerini geçirerek bu sayıyı 5 defa ekrana yazar. Sonra, üçüncü kez sinif türünden nes3 nesnesi oluştururken değişken veri türü olarak int ve sabit değer olarak 10 değerini sınıfın kopyasına geçirir. Sınıf içindeki veri\_goster() fonksiyonuna 21 değerini geçirerek bu sayıyı 10 defa ekrana yazar. Son olarak, sinif türünden nes4 nesnesi oluştururken herhangi bir parametre tanımlamaz. Sınıf için ön tanımlı değişken veri türü int ve sabit değer 1 olduğundan, sınıf içindeki veri\_goster() fonksiyonuna 1079 değerini geçirerek bu sayıyı 1 defa ekrana yazar.

## Şablon sınıflarının belirli bir veri türü için yeniden tanımlanması

Şablon sınıflarını, template<> yapısını kullanarak, belirli bir veri türü için yeniden tanımlayabiliriz. 

```

template <typename T> class sınıf-adı
{
  // Sınıf içi değişken ve fonksiyon bildirimleri
}

// Yeniden tanımlama
template <> class sınıf-adı T
{
  // Sınıf içi değişken ve fonksiyon bildirimleri
}

```

Aynı veri türünden private, protected ve public değişkenlere işlem yapan fonksiyonlar içeren bir şablon sınıfının kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

template <typename t> class sinif {

  private:
    t priid;

  protected:
    t proid;

  public:
    t pubid;
    void deger_ata(t pid1, t pid2, t pid3)
    {
      priid = pid1; proid = pid2; pubid = pid3;
      cout << "Şablon sinif değişkenlerine değer atama: " << priid << " " << proid << " " << pubid << endl;
    }
    void deger_goster()
    {
      cout << "Şablon sinif değişken değerleri: " << priid << " " << proid << " " << pubid << endl;
    }
};

// sinif sınıfının int veri türü için yeniden tanımlanması
template <> class sinif<int>{

  private:
    int priid;

  protected:
    int proid;

  public:
    int pubid;
    void deger_ata(int pid1, int pid2, int pid3)
    {
      priid = pid1; proid = pid2; pubid = pid3;
      cout << "int veri türü için yeniden tanımlanmış şablon sinif değişkenlerine değer atama: " << priid << " " << proid << " " << pubid << endl;
    }
    void deger_goster()
    {
      cout << "int veri türü için yeniden tanımlanmış şablon sinif değişken değerleri: " << priid << " " << proid << " " << pubid << endl;
    }
};

int main(void)
{
  sinif <float> nes1; // Şablon sınıfının orjinal yapısı ile nesne oluşturma

  nes1.deger_ata(176.42f, 1487.21f, 3487.65f);
  nes1.deger_goster();

  cout << endl;

  sinif <int> nes2;  // int veri türü için yeniden tanımlanmış şablon sınıfının yapısı ile nesne oluşturma

  nes2.deger_ata(1215, 2843, 9514);
  nes2.deger_goster();

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Şablon sinif değişkenlerine değer atama: 176.42 1487.21 3487.65
Şablon sinif değişken değerleri: 176.42 1487.21 3487.65

int veri türü için yeniden tanımlanmış şablon sinif değişkenlerine değer atama: 1215 2843 9514
int veri türü için yeniden tanımlanmış şablon sinif değişken değerleri: 1215 2843 9514

```

Program, önce tek bir veri türünün parametre olarak geçirildiği bir şablon sınıf tanımlar. Sonra, sadece int veri türü ile işlem yapacak şekilde şablon sınıfını yeniden tanımlar. İlk olarak, tanımladığı sinif türünden nes1 nesnesini oluştururken float veri türünü parametre olarak sınıfa geçirir. Sınıf içindeki deger\_ata() fonksiyonu ile tüm değişkenlere bir değer atar ve deger\_goster() fonksiyonu ile değişken değerlerini ekrana yazar. Aynı işlemleri nes2 nesnesini tanımlarken int veri türü ile yaptığından, şablon sınıfının int veri için tanımlanan yeniden tanımlanan sürümünün kopyası oluşturulur.

## Değişken sayıda parametre alan sınıf şablonları

C++11 sürümünden önce, şablonların, bildirim esnasında tanımlanması gereken sabit sayıda parametresi vardı. Şablonlar, değişken sayıda parametresi olan bir sınıf şablonu oluşturmak için kullanılamazdı.

C++11 sürümü ile birlikte gelen değişken parametre sayılı şablonlar özelliği ile, sıfır da dahil olmak üzre, herhangi bir sayıda parametreye sahip sınıf fonksiyon şablonları tanımlayabiliriz.

Fonksiyon şablonlarında, değişken sayıda tanımlanan parametrelerle ilgili işlemler çalışma zamanında değil derleme zamanında yapılır.

Bir parametre paketi, şablonlar için herhangi bir veri türünden bir parametre olabilir. Değişken parametre sayılı şablonlarda, 0 veya daha fazla parametre içeren ve ... ifadesi ve tek bir parametre adı ile temsil edilen parametre paketi (parameter pack) kavramı kullanılmaktadır.

> Şablon tanımında, bir parametre paketi tek bir parametre olarak ele alınır. Parametre paketinin içinde tanımlandığı şablona çağrı yapıldığında, parametre paketi genişletilir ve çağrı yapıldığında kullanılan parametre sayısı kadar tanımlanan veri türüne göre parametre oluşturulmaktadır.
{: .prompt-tip }

Parametre paketinin kullanıldığı yere bağlı olarak, parametre paketi bir fonksiyon parametre paketi olabilir.

Parametre paketleri şablon bildirimlerinde template anahtar kelimesinden sonra kullanılabilir.

Değişken sayıda parametre içeren sınıf şablonu da template anahtar kelimesi ile birlikte kullanılan ... ifadesi ile oluşturulur. Değişken sayıda parametre içeren sınıf şablonu bildirimi için kullanılan iki farklı genel yapı aşağıda gösterilmektedir:

```

template <typename T, typename... params> class sınıf-adı {
  // Sınıf içi değişken ve fonksiyon bildirimleri
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

// Ana yapı bildirimi
template<typename... T> class sinif { };

// Tekrar edici genel yapı bildirimi
template<typename T, typename... TParams> // Şablon parametre paketi
class sinif<T, TParams...>                // Sınıf parametre paketi
{
  public:
    T first;
    sinif<TParams...> tparams;            // Parametre paketi açılımı
    sinif(const T& f, const TParams& ... tp) : first(f), tparams(tp...)
    {
      cout << f << endl;
    };
};

int main(void)
{
  sinif<int, int, int> sin1(7, 21, 124);
  sinif<char, string, int> sin2('k', "Template", 25);

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
