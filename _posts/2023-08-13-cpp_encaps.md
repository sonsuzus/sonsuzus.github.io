---
title:  C++ Kapsülleme
author: sonsuz
date: 2023-08-13 19:14:46 +0300
categories: [Program,C++]
tags: [cpp,programlama,kapsülleme,nesne,oop]
---


Kapsülleme, programda bir sınıf içinde tanımlanan verileri ve yine aynı sınıf içinde tanımlanan ve bu verilere erişim sağlayarak kullanan metod veya fonksiyon adı verilen sistemi ifade eder. Bu sistemle, sınıf içinde ye alan veriler ve bu verilere erişim sağlayan kodlar bir bütünlük içinde korunarak, dışarıdan erişimi kısıtlanır. Böylece, program kendi içinde bir kod ve veri güvenliği sağlar. Bu sistemde, kod ve veri tek bir isim altında tanımlanarak, oluşturulan bir sınıf içindeki veri ve kodlar (metodlar) korunur.

Kapsülleme verileri ve bu verileri kullanan ya da değiştiren program kodlarını birbirine bağlayarak dışarıdan yapılabilecek müdahalelere karşı koruyan bir sistemdir. Nesneye yönelik programlamada, bir sınıf tanımlaması altında kod ve veri bu şekilde koruma altına alındığında bir nesne oluşturulmuş olur. Nesne kapsamındaki veri ve verilere işlem yapan kodlar; sadece içinde tanımlı olduğu nesne tarafından (private) veya dışarıdan erişilecek şekilde (public) tanımlanabilir. Nesne içinde private olarak tanımlanmış özel kod ve verilere sadece nesne içinde yer alan diğer kodlar tarafından erişilebilir. Nesne dışında yer alan kodlar nesneye ve özel verilere erişemezler.

Nesne içinde public olarak tanımlanan kod ve veriler tüm erişimlere açık olduğundan, programın nesne dışında kalan kodları bu kod ve verilere erişim sağlar. Nesne içinde programdaki tüm kodların erişimine açık veri ve kodlar açık olarak tanımlanır. Tüm erişimlere açık olan nesne elemanları, nesneye özel elemanlara erişim için kullanılır. Bu durumda, nesne dışındaki kodlar nesne içindeki tüm erişimlere açık kodlar yoluyla nesne içindeki nesneye özel veri ve kodlara da erişebilirler.

Şimdi, kapsülleme özelliğinin çalışma prensibini göstermek amacıyla, bir sınıf içinde bildirimi yapılmış olan private, protected ve public değişkenlere, aynı sınıf türünden oluşturulmuş bir nesne yoluyla erişim koşullarını gösteren bir örneği incelemeye çalışalım:

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
