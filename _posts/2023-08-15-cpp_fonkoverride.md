---
title:  C++ Fonksiyonları yeniden tanımlama (Overriding)
author: sonsuz
date: 2023-08-15 20:51:09 +0300
categories: [Program,C++]
tags: [programlama,cpp,fonksiyon,overriding,nesne,sınıf]
---



# Fonksiyonları yeniden tanımlama (Overriding)

Nesneye yönelik programlamada, [kalıtım](https://sonsuzus.github.io/posts/cpp_inheritance/) özelliğini kullanarak, bir ana sınıftan sınıflar türetebiliriz. Bir ana sınıftan bir sınıf türetildiğinde, ana sınıfta yer alan tüm değişken ve fonksiyonlar türetilen sınıf tarafından kullanılabileceği gibi, türetilen sınıf içinde de yeni değişken ve fonksiyonlar tanımlanabilir.

Eğer ihtiyaç duyulursa, ana sınıftan devralınan fonksiyon adları ile aynı ada sahip fonksiyonlar tanımlanarak, ana sınıftan devralınan fonksiyonlar geçersiz hale getirilir ve aynı isim altında farklı kodlar yazılır. Bu durumda, aynı fonksiyon hem ana sınıfta hem de türetilmiş sınıfta tanımlanmış olur. Bu fonksiyon türetilmiş sınıf nesnesi ile çağrıldığında, türetilmiş sınıfın fonksiyonu çağrılır. Bu özelliğe, Fonksiyonu Yeniden Tanımlama adı verilir. Türetilmiş sınıftaki fonksiyon, ana sınıftaki fonksiyonun yerini alır.

> Fonksiyonu yeniden tanımlama işleminin yapılabilmesi için, bir ana sınıftan bir sınıf türetilmesine, kalıtım özelliğinin kullanılmasına, ihtiyaç vardır.
{: .prompt-warning }

Fonksiyonları yeniden tanımlama işlemi, bir ana sınıf ve ana sınıftan türetilmiş olan bir veya daha fazla türetilmiş sınıf içinde yapılır. Bu işlem iki farklı yöntemle uygulanabilir:

* Sınıf fonksiyonlarını doğrudan yeniden tanımlama
* Sınıf fonksiyonlarını sanal yöntemle (virtual) yeniden tanımlama

İki yöntemin kullanılması arasındaki fark, doğrudan yeniden tanımlama yönteminde, ana sınıf işaretçisine türetilen sınıf nesnesinin adresi atandığında, ana sınıf işaretçisi ana sınıf içindeki fonksiyonlara erişim sağlarken, sanal yöntemle yeniden tanımlama yönteminde, türetilen sınıf içindeki fonksiyonlara erişim sağlamaktadır.

## Sınıf fonksiyonlarını doğrudan yeniden tanımlama

Sınıf üye fonksiyonlarını yeniden tanımlama işlemi yaparken, ana sınıf içinde tanımlanan bir fonksiyon ile aynı isme sahip bir fonksiyon ana sınıftan türetilmiş bir sınıf içinde tanımlanır ve kod içeriği yeniden yazılır. Bu durumda, ana sınıf ve bu sınıf içinde aynı isme sahip iki fonksiyon oluşturulur. Bu fonksiyonlara ana sınıf ve türetilmiş sınıftan oluşturulan işaretçi ve nesneler yoluyla yapılan erişimler aşağıda gösterilen esaslara göre yapılmaktadır:

1. Türetilen sınıf içinde yeniden tanımlanan fonksiyon ile aynı isme sahip ana sınıf içindeki fonksiyona ana sınıf nesnesi ile erişim sağlanır.
2. Türetilen sınıf içinde yeniden tanımlanan fonksiyona türetilen sınıf nesnesi ile erişim erişim sağlanır.
3. Türetilen sınıf içinde yeniden tanımlanan ana sınıf fonksiyonlarına türetilen sınıf nesnesi ile erişim sağlamak aşağıdaki ifadeyi kullanabiliriz: `türetilen-sınıf-nesnesi.ana-sınıf-adı::fonksiyon-adı`
4. Ana sınıf işaretçisine türetilen sınıf nesnesinin adresini atandığında, bu işaretçi yoluyla türetilen sınıf içinde yeniden tanımlanan fonksiyon ile aynı isme sahip ana sınıf içindeki fonksiyona eriğşim sağlanır.
5. Türetilen sınıf içinde yeniden tanımlanan fonksiyon içinden aşağıdaki ifade kullanıldığında, aynı isme sahip ana sınıf içindeki fonksiyona erişim sağlanır. `ana-sınıf-adı::fonksiyon-adı`

Şimdi, bu uygulamaları bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

class sinifana {
  private:
    int priidana;
  public:
    void deger_ata(int pid) {
        priidana = pid;
        cout << "priidana değişkenine değer atama!" << "\n";
    };
    void deger_goster(void)
    {
      cout << "priidana değişken değeri: " << priidana << "\n\n";
    }
};

class siniftur : public sinifana {
  private:
    int priidtur;
  public:
    void deger_ata(int pid) {
        priidtur = pid;
        cout << "priidtur değişkenine değer atama!" << "\n";

    };
    void deger_goster(void)
    {
      cout << "priidtur değişken değeri: " << priidtur << "\n\n";
    }
};

int main(void)
{
  sinifana *pnes;
  sinifana nes_ana;
  siniftur nes_tur;

  // Türetilen sınıf içinde yeniden tanımlanan fonksiyonlar ile aynı
  // isme sahip ana sınıf içindeki fonksiyonlara erişim sağlanır.
  nes_ana.deger_ata(154);
  nes_ana.deger_goster();

  // Türetilen sınıf içinde yeniden tanımlanan fonksiyonlara türetilen
  // sınıf nesnesi ile erişim erişim sağlanır.
  nes_tur.deger_ata(21);
  nes_tur.deger_goster();

  // Türetilen sınıf içinde yeniden tanımlanan ana sınıf
  // fonksiyonlarına türetilen sınıf nesnesi ile erişim
  nes_tur.sinifana::deger_ata(35);
  nes_tur.sinifana::deger_goster();

  // Ana sınıf işaretçisine türetilen sınıf nesnesinin
  // adresini atayarak ana sınıf fonksiyonlarına erişim
  pnes = &nes_tur;
  pnes->deger_ata(47);
  pnes->deger_goster();

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

priidana değişkenine değer atama!
priidana değişken değeri: 154

priidtur değişkenine değer atama!
priidtur değişken değeri: 21

priidana değişkenine değer atama!
priidana değişken değeri: 35

priidana değişkenine değer atama!
priidana değişken değeri: 47

```

Program, priidana adlı private int bir değişken, bu değişkene değer atayan deger\_ata() adlı bir fonksiyon ve bu değişken değerini ekrana yazan deger\_goster() adlı bir fonksiyon içeren sinifana adlı bir ana sınıf bildirimi yapar. Sonra, priidtur adlı private int bir değişken, bu değişkene değer atayan deger\_ata() adlı bir fonksiyon ve bu değişken değerini ekrana yazan deger\_goster() adlı bir fonksiyon içeren ve sinifana adlı sınıftan türetilen siniftur adlı bir sınıf bildirimi yapar. Ana sınıf ve türetilen sınıf içinde yer alan fonksiyonlar aynı isme sahip olduklarından, yeniden tanımlanmış fonksiyonlardır.

Program, sinifana sınıfından pnes adlı bir işaretçi ile nes\_ana adlı bir nesne ile siniftur adlı sınıftan nes\_tur adlı bir nesne bildirimi yapar. nes\_ana nesnesini kullanarak, ana sınıf içindeki fonksiyonlar yoluyla, priidana değişkenine 154 değerini atar ve değişken değerini ekrana yazar. Böylece, türetilen sınıf içinde yeniden tanımlanan fonksiyon ile aynı isme sahip ana sınıf içindeki fonksiyonlar erişim sağlanır. nes\_tur nesnesini kullanarak, türetilen sınıf içindeki fonksiyonlar yoluyla, priidtur değişkenine 21 değerini atar ve değişken değerini ekrana yazar. Böylece, türetilen sınıf içinde yeniden tanımlanan fonksiyonlara türetilen sınıf nesnesi ile erişim sağlanır. nes\_tur nesnesini ana sınıf adı ve :: işlemcisi ile birlikte kullanarak, ana sınıf içindeki fonksiyonlar yoluyla, priidana değişkenine 35 değerini atar ve değişken değerini ekrana yazar. Böylece, nes\_tur nesnesi ile ana sınıf fonksiyonlarına erişim sağlanır. pnes adlı ana sınıf işaretçisine nes\_tur adlı türetilen sınıf nesnesinin adresi atar. Bu işaretçi yoluyla ana sınıf fonksiyonlarını kullanarak, priidana değişkenine 47 değerini atar ve değişken değerini ekrana yazar. Böylece, bu işaretçi yoluyla türetilen sınıf içinde yeniden tanımlanan fonksiyonlar ile aynı isme sahip ana sınıf içindeki fonksiyonlara erişim sağlanır.

Programın çalışma şeklini gösteren şekil aşağıdadır:

![](cprog/fonkoverride01.png)

Şimdi, türetilen sınıf içinde yeniden tanımlanan fonksiyon içinde ana sınıf adı ile birlikte :: işlemcisini kullanarak, ana sınıf içindeki aynı isme sahip fonksiyona erişim sağlanmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

class sinifana {
  private:
    int priidana;
  public:
    void deger_ata(int pid) {
        priidana = pid;
        cout << "priidana değişkenine değer atama!" << "\n";
    };
    void deger_goster(void)
    {
      cout << "priidana değişken değeri: " << priidana << "\n";
    }
};

class siniftur : public sinifana {
  private:
    int priidtur;
  public:
    void deger_ata(int pid1, int pid2) {
        priidtur = pid1;
        cout << "priidtur değişkenine değer atama!" << "\n";
        sinifana::deger_ata(pid2);
    };
    void deger_goster(void)
    {
      cout << "priidtur değişken değeri: " << priidtur << "\n";
      sinifana::deger_goster();
    }
};

int main(void)
{
  siniftur nes_tur;

  nes_tur.deger_ata(27,35);
  nes_tur.deger_goster();

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

priidtur değişkenine değer atama!
priidana değişkenine değer atama!
priidtur değişken değeri: 27
priidana değişken değeri: 35

```

Program, priidana adlı private int bir değişken, bu değişkene değer atayan deger\_ata() adlı bir fonksiyon ve bu değişken değerini ekrana yazan deger\_goster() adlı bir fonksiyon içeren sinifana adlı bir ana sınıf bildirimi yapar. Sonra, priidtur adlı private int bir değişken, bu değişkene değer atayan deger\_ata() adlı bir fonksiyon ve bu değişken değerini ekrana yazan deger\_goster() adlı bir fonksiyon içeren ve sinifana adlı sınıftan türetilen siniftur adlı bir sınıf bildirimi yapar. Ana sınıf ve türetilen sınıf içinde yer alan fonksiyonlar aynı isme sahip olduklarından, yeniden tanımlanmış fonksiyonlardır. Türetilen sınıf içinde yeniden tanımlanan fonksiyonlar ana sınıf adı ile :: işlemcisini kullanarak, aynı isme sahip ana sınıf fonksiyonlarını çağırmaktadır.

Program, siniftur adlı sınıftan nes\_tur adlı bir nesne bildirimi yapar. nes\_tur nesnesini kullanarak, türetilen sınıf içindeki fonksiyonlar yoluyla, priidtur değişkenine 27 değerini ve priidana değişkenine 35 değerini atar ve değişken değerlerini ekrana yazar. Böylece, türetilen sınıf içinde yeniden tanımlanan fonksiyonlara türetilen sınıf nesnesi ile erişim sağlanırken aynı zamanda, fonksiyonlar içinden ana sınıf fonksiyonlarına da erişim sağlanır.

## Sınıf fonksiyonlarını sanal yöntemle (virtual) yeniden tanımlama

Sanal fonksiyonlar, çalışma zamanı çok biçimlilik (Runtime Polymorphism) özelliği sağlar. Sanal bir fonksiyon oluşturmak için, ana sınıf içindeki fonksiyon bildiriminden önce virtual anahtar kelimesi kullanılır. Sanal fonksiyon içeren bir sınıftan yeni bir sınıf türetildiğinde, türetilen her sınıf içinde sanal fonksiyon, virtual anahtar kelimesi kullanılmadan, yeniden tanımlanır ve fonksiyon içeriği yeniden düzenlenir. Bu özellikle, virtual anahtar kelimesi derleyiciye fonksiyon bağlama işlemini derleme zamanında değil çalışma zamanında yapmasını bildirir. Sanal fonksiyon ile, aynı isme sahip bir fonksiyon her sınıf için ayrı bir işlem yapacak şekilde tanımlanabilmektedir. Bu durum nesneye yönelik programlamada çok biçimlilik (Polymorphism) özelliğinin bir sonucudur. İşaretçi kullanarak erişim sağlamak sanal fonksiyonları sınıf içindeki diğer fonksiyonlardan farklı hale getirir. Ana sınıf türünden oluşturulan bir işaretçi ana sınıf ve ana sınıftan türetilen tüm sınıflar içindeki sanal fonksiyonlara erişim sağlayabilir.

> Sınıf fonksiyonları için sanal yöntemle (virtual) yeniden tanımlama (Overriding) işlemi için mutlaka bir ana sınıftan türetilmiş olan en az bir adet sınıf bildirimi yapılmış olmalıdır.
{: .prompt-warning }

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

Sanal fonksiyonlar genel olarak ana sınıf işaretçisi kullanılarak çağrılır. Bu yöntemde, ana sınıftan ve türetilen sınıflardan oluşturulan nesnelerin adresleri ana sınıf türünden tanımlanan işaretçiye atanarak her bir sınıfta yer alan sanal fonksiyona çağrı yapılır.

Şimdi, bu uygulamaları bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

class sinifana {
  private:
    int priidana;
  public:
    void deger_ata(int pid) {
        priidana = pid;
        cout << "priidana değişkenine değer atama!" << "\n";
    };
    void deger_goster(void)
    {
      cout << "priidana değişken değeri: " << priidana << "\n\n";
    }
};

class siniftur : public sinifana {
  private:
    int priidtur;
  public:
    void deger_ata(int pid) {
        priidtur = pid;
        cout << "priidtur değişkenine değer atama!" << "\n";

    };
    void deger_goster(void)
    {
      cout << "priidtur değişken değeri: " << priidtur << "\n\n";
    }
};

int main(void)
{
  sinifana *pnes;
  sinifana nes_ana;
  siniftur nes_tur;

  // Türetilen sınıf içinde yeniden tanımlanan fonksiyonlar ile aynı
  // isme sahip ana sınıf içindeki fonksiyonlara erişim sağlanır.
  nes_ana.deger_ata(154);
  nes_ana.deger_goster();

  // Türetilen sınıf içinde yeniden tanımlanan fonksiyonlara türetilen
  // sınıf nesnesi ile erişim erişim sağlanır.
  nes_tur.deger_ata(21);
  nes_tur.deger_goster();

  // Türetilen sınıf içinde yeniden tanımlanan ana sınıf
  // fonksiyonlarına türetilen sınıf nesnesi ile erişim
  nes_tur.sinifana::deger_ata(35);
  nes_tur.sinifana::deger_goster();

  // Ana sınıf işaretçisine türetilen sınıf nesnesinin
  // adresini atayarak ana sınıf fonksiyonlarına erişim
  pnes = &nes_tur;
  pnes->deger_ata(47);
  pnes->deger_goster();

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

priidana değişkenine değer atama!
priidana değişken değeri: 154

priidtur değişkenine değer atama!
priidtur değişken değeri: 21

priidana değişkenine değer atama!
priidana değişken değeri: 35

priidtur değişkenine değer atama!
priidtur değişken değeri: 47

```

Program, priidana adlı private int bir değişken, bu değişkene değer atayan deger\_ata() adlı ve bu değişken değerini ekrana yazan deger\_goster() adlı iki adet sanal (virtual) fonksiyon içeren sinifana adlı bir ana sınıf bildirimi yapar. Sonra, priidtur adlı private int bir değişken, bu değişkene değer atayan deger\_ata() adlı ve bu değişken değerini ekrana yazan deger\_goster() adlı iki adet fonksiyon içeren ve sinifana adlı sınıftan türetilen siniftur adlı bir sınıf bildirimi yapar. Ana sınıf içindeki sanal fonksiyonlarla türetilen sınıf içinde yer alan fonksiyonlar aynı isme sahip olduklarından, yeniden tanımlanmış fonksiyonlardır.

Program, sinifana sınıfından pnes adlı bir işaretçi ile nes\_ana adlı bir nesne ile siniftur adlı sınıftan nes\_tur adlı bir nesne bildirimi yapar. nes\_ana nesnesini kullanarak, ana sınıf içindeki fonksiyonlar yoluyla, priidana değişkenine 154 değerini atar ve değişken değerini ekrana yazar. Böylece, türetilen sınıf içinde yeniden tanımlanan fonksiyon ile aynı isme sahip ana sınıf içindeki fonksiyonlar erişim sağlanır. nes\_tur nesnesini kullanarak, türetilen sınıf içindeki fonksiyonlar yoluyla, priidtur değişkenine 21 değerini atar ve değişken değerini ekrana yazar. Böylece, türetilen sınıf içinde yeniden tanımlanan fonksiyonlara türetilen sınıf nesnesi ile erişim sağlanır. nes\_tur nesnesini ana sınıf adı ve :: işlemcisi ile birlikte kullanarak, ana sınıf içindeki fonksiyonlar yoluyla, priidana değişkenine 35 değerini atar ve değişken değerini ekrana yazar. Böylece, nes\_tur nesnesi ile ana sınıf fonksiyonlarına erişim sağlanır.

pnes adlı ana sınıf işaretçisine nes\_tur adlı türetilen sınıf nesnesinin adresi atar. Bu işaretçi yoluyla türetilen sınıf fonksiyonlarını kullanarak, priidtur değişkenine 47 değerini atar ve değişken değerini ekrana yazar. Böylece, bu işaretçi yoluyla türetilen sınıf içinde yeniden tanımlanan fonksiyonlara erişim sağlanır.

Programın çalışma şeklini gösteren şekil aşağıdadır:

![](cprog/fonkoverride02.png)

Sınıf fonksiyonlarının doğrudan ve sanal yöntemle (virtual) yeniden tanımlanması arasındaki fark, doğrudan yeniden tanımlama yönteminde, ana sınıf işaretçisine türetilen sınıf nesnesinin adresi atandığında, ana sınıf işaretçisi ana sınıf içindeki fonksiyonlara erişim sağlarken, sanal yöntemle yeniden tanımlama yönteminde, türetilen sınıf içindeki fonksiyonlara erişim sağlamaktadır.
