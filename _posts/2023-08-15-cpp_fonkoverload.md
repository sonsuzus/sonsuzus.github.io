---
title:  C++ Fonksiyon çoklu görev (Overloading)
author: sonsuz
date: 2023-08-15 20:44:59 +0300
categories: [Program,C++]
tags: [cpp,programlama,fonksiyon,çoklu görev,overloading]
---


Çok biçimlilik sözlük anlamı olarak birden fazla şekilde varlık gösterebilen nesne ya da kavramları ifade etmektedir. Fonksiyonlar açısından çok biçimlilik aynı isme sahip bir fonksiyonun çok amaçlı kullanılması için, farklı sayıda ve veri türündeki parametrelerle tanımlanması olarak ifade edilebilir.

## Fonksiyonlarda çoklu görev tanımlama (overloading) işlemi

C++'da, fonksiyonlarda çoklu görev tanımlama işlemi yapılırken çok biçimlilik özelliği kullanılır. Birden fazla fonksiyon, farklı veri türündeki ve/veya farklı sayıda parametrelerle bildirimleri yapıldığında, aynı adı kullanır ve program içinden farklı parametreler ve aynı ad ile çağrılırlarsa, fonksiyon çoklu görev tanımlama işlemi gerçekleştirilmiş olur. Böylece, program içinde tek bir isim kullanarak birden fazla fonksiyona erişim sağlanabilir.

Burada kullanılan çoklu görev tanımlama ifadesi birden fazla fonksiyonun aynı isim ile çağrılarak kullanılacağını gösterir.

Böyle bir fonksiyon çağırıldığında, çağrı fonksiyon çağrısında kullanılan parametre sayısı ve tiplerine uygun olarak ilgili fonksiyona yönlendirilir. Bu özelliği bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

// topla() fonksiyonunun 2 farklı veri türünde parametre ile bildirimi yapılarak çoklu görev tanımlama işlemi
int topla (int id1, int id2);
float topla (float fd1, float fd2);

int main(void)
{
  // 2 adet int değer parametre ile fonksiyon çağrısı
  cout << "int değer toplamları: "<< topla (7, 8) << endl;
  
  // 2 adet float değer parametre ile fonksiyon çağrısı
  cout << "float değer toplamları: " << topla (21.8f, 17.5f) << endl;

  return 0;
}

// Fonksiyon ana yapı bildirimleri
int topla(int id1, int id2)
{
  return id1 + id2;      
}

float topla(float fd1, float fd2)
{
  return fd1 + fd2;      
}


```

Yukarıdaki programı derleyip çalıştırdığınız zaman aşağıdaki ifadeleri ekrana yazar:

```

int değer toplamları: 15
float değer toplamları: 39.3

```

Program çalışmaya başladığında, 2 kez topla() fonksiyonunu çağırır. İlk çağrıda 2 adet int değer ikinci çağrıda ise 2 adet float değer kullanılarak topla() fonksiyonu çalıştırılır.

C++ derleyicisi, fonksiyon çağrısında kullanılan parametre sayısı, sırası ve veri türlerine göre hangi fonksiyonun kullanılacağına karar verir.

> Çok biçimliliğin sağladığı olanakla yapılan fonksiyon çoklu görev tanımlama işlemi ile; sadece tek bir fonksiyon adı ile farklı veri türündeki parametrelerle aynı işlem yapılarak daha esnek programlar yazılabilmektedir.
{: .prompt-tip }

Fonksiyon çoklu görev tanımlama işleminin gerçekleşmesi için; aynı ada sahip fonksiyon bildirimlerinde yer alan parametrelerin türü ve/veya sayısı farklı olmalıdır. Ancak, fonksiyonların geri döndürdüğü değer aynı veya farklı olabilir.

Şimdi, aynı özelliği farklı bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

void deger_goster(int id) {
  cout << "int değişken değeri: " << id << endl;
}

void deger_goster(float fd) {
  cout << "float değişken değeri: " << fd << endl;
}

void deger_goster(char const *cp) {
  cout << "Karakter dizisi değeri: " << cp << endl;
}

int main(void) {
  deger_goster(21);
  deger_goster(145.82f);
  deger_goster("Fonksiyon çoklu görev tanımlama işlemi");
	
  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığınız zaman aşağıdaki ifadeleri ekrana yazar:

```

int değişken değeri: 21
float değişken değeri: 145.82
Karakter dizisi değeri: Fonksiyon çoklu görev tanımlama işlemi

```

Program deger\_goster() fonksiyonunu, her defasında farklı bir veri türü kullanarak, 3 defa çağırır. Program fonksiyona geçirilen parametrenin veri türüne göre aynı isme sahip 3 fonksiyondan ilgili fonksiyonu çağırarak işlem yapar.

Şimdi, farklı sayıda parametreye sahip fonksiyon çoklu görev tanımlama işlemini bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

void carpim(int id1, int id2) {
  cout << "Çarpım sonucu: " << id1 * id2 << endl;
}

void carpim(int id1, int id2, int id3) {
  cout << "Çarpım sonucu: " << id1 * id2 * id3 << endl;
}

int main(void) {
  carpim(21, 5);
  carpim(17, 4, 8);
	
  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığınız zaman aşağıdaki ifadeleri ekrana yazar:

```

Çarpım sonucu: 105
Çarpım sonucu: 544

```

Program carpim() fonksiyonunu, her defasında farklı sayıda parametre kullanarak, 2 defa çağırır. Program fonksiyona geçirilen parametrenin sayısına göre aynı isme sahip 2 fonksiyondan ilgili fonksiyonu çağırarak işlem yapar.

## Sınıf üyesi fonksiyonlarda çoklu görev tanımlama (overloading) işlemi

Fonksiyon çoklu görev tanımlama işlemini normal fonksiyonlara uyguladığımız gibi, sınıflar içinde yer alan üye fonksiyonlara uyglayabiliriz. Bu özelliği bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

class sinif {
  private:
    int priid;
    int prifd;
  public:
	sinif() { priid=0; prifd=0.00f; };

	// Çoklu görev tanımlama işlemi uygulanmış fonksiyonlar
	void topla(int id1, int id2) { priid = id1+id2; };
	void topla(float fd1, float fd2) { priid = fd1+fd2; };
	void topla(int id1, int id2, int id3) { priid = id1+id2+id3; };

	void deger_goster()
	{
	  cout << "priid değişken değeri: " << priid << "\n";
	  cout << "prifd değişken değeri: " << prifd << "\n";
	};
};

int main(void)
{
  sinif nes; // Nesne oluşturma

  nes.topla(21, 35);
  nes.deger_goster();

  nes.topla(21, 35, 58);
  nes.deger_goster();

  nes.topla(17.35F, 45.54F);
  nes.deger_goster();

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığınız zaman aşağıdaki ifadeleri ekrana yazar:

```

priid değişken değeri: 56
prifd değişken değeri: 0
priid değişken değeri: 114
prifd değişken değeri: 0
priid değişken değeri: 62
prifd değişken değeri: 0

```

Program, priid adlı int ve prifd adlı float veri türündne olmak üzere iki adet değişken, değişkenlere ilk değer vermede kullanılan bir constructor fonksiyonu, ilki iki adet int parametre, ikincisi iki adet float parametre ve üçüncüsü üç adet int parametre alan üç adet toplama işlemi yapan topla() adlı fonksiyon ve sınıf içindeki değişken değerlerini ekranda gösteren deger\_goster() adlı bir fonksiyon içeren bir sınıf bildirimi yapar. sinif türünden oluşturduğu nes adlı nesne yoluyla, topla() fonksiyonunu farklı parametrelerle çağırır ve sonuçları ekana yazar.

## Constructor fonksiyonlarda çoklu görev tanımlama (overloading) işlemi

Sınıf içinde aynı isme sahip birden fazla constructor fonksiyonu tanımlanarak, constructor fonksiyonları için çoklu görev tanımlama işlemi yapılabilir.

Constructor fonksiyonları için çoklu görev tanımlama işlemi yaptığımızda, aynı isme sahip tüm constructor fonksiyonlarının parametre sayısı birbirinden farklı olmalıdır.

İlk değer verilen ve verilmeyen constructor fonksiyonları için çoklu görev tanımlama (overloading) işlemi
Constructor fonksiyonlarını bir sınıf içinde yer alan değişkenlere ilk değer atamadan veya ilk değer atayarak kullanmak için, constructor fonksiyonlarını herhangi bir parametre olmadan veya farklı sayıda parametre ile kullanmak için çoklu görev tanımlama işlemi uygulayabiliriz.

Bu yöntemle, oluşturduğumuz sınıf cinsinden tanımladığımız nesneler yoluyla sınıf içinde bulunan değişkenlere, tanımlama anında herhangi bir değer atamayabilir veya farklı sayıda ilk değer atayabiliriz. Böylece, program içinde nesne oluşturma işlemini ilk değer yapmadan veya yaparak gerçekleştirebiliriz.

Bu özelliği bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

class sinif {
  private:
    int id; 
  public:
	// Çoklu görev tanımlama işlemi uygulanmış constructor fonksiyonları
	sinif();        // İlk değer ataması yok.
	sinif(int pid); // İlk değer ataması var.
	~sinif();
	
	void deger_goster(void);
};

// Çoklu görev tanımlama işlemi uygulanmış constructor fonksiyonları ana yapısı
sinif::sinif()
{
  id = 0;
  cout << "İlk değer ataması olmadan nesne oluşturma!" << endl;
}

sinif::sinif(int pid)
{
  id = pid;
  cout << "İlk değer ataması ile nesne oluşturma: " << id << endl;
}

sinif::~sinif()
{
  cout << "Nesne yok ediliyor!" << endl;
}

void sinif::deger_goster(void)
{
  cout << "id değişken değeri: " << id << endl;
}

int main(void)
{
  sinif nes01;     // İlk değer ataması olmadan nesne oluşturma
  sinif nes02(21); // İlk değer ataması ile nesne oluşturma
  
  nes01.deger_goster();
  nes02.deger_goster();

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığınız zaman aşağıdaki ifadeleri ekrana yazar:

```

İlk değer ataması olmadan nesne oluşturma!
İlk değer ataması ile nesne oluşturma: 21
id değişken değeri: 0
id değişken değeri: 21
Nesne yok ediliyor!
Nesne yok ediliyor!

```

Program, iki adet nesne oluştururken sinif() constructor fonksiyonunu, önce ilk değer atamadan sonra bir ilk değer atayarak çağırır. Program fonksiyona parametre geçirilip geçirilmeme durumuna göre ilgili fonksiyonu çağırarak işlem yapar. İlk nesne oluşturmada, herhangi bir değer atanmadığından, parametre almayan constructor fonksiyonu, ikinci nesne oluşturmada ise, ilk değer atama için bir değer kullanıldığından, tek parametreli constructor fonksiyonu çağrılır.

Birden fazla ve farklı sayıda parametre içeren constructor fonksiyonları için çoklu görev tanımlama (overloading) işlemi
Bir sınıf içinde yer alan değişkenlere, constructor fonksiyonunu kullanarak, farklı yöntemlerle değer atmak istediğimizde, constructor fonksiyonlarında en az bir parametre olmak üzere farklı sayıda parametre geçirme yöntemiyle çoklu görev tanımlama işlemi uygulayabiliriz.

Bu yöntemle, oluşturduğumuz sınıf cinsinden tanımladığımız nesneler yoluyla sınıf içinde bulunan değişkenlere, tanımlama anında yapacağımız ilk değer atamalarını daha esnek bir hale getirebiliriz. Böylece program içinde nesne oluşturma anında farklı şekillerde yapılan veri girişlerini aynı sınıf değişkenlerine atayabiliriz.

Constructor fonksiyonları için çoklu görev tanımlama işlemi uygularken, fonksiyonların en az bir parametre olmak üzere farklı sayıda parametre içerebilir. Bu özelliği bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

class sinif {
  private:
    int alan; 
  public:
	// Çoklu görev tanımlama işlemi uygulanmış constructor fonksiyonları
	sinif(int id);           // Kare alan hesaplama için
	sinif(int id1, int id2); // Dikdörtgen alan hesaplama için
	~sinif();
	
	void deger_goster(void);
};

// Çoklu görev tanımlama işlemi uygulanmış constructor fonksiyonları ana yapısı
sinif::sinif(int pid)
{
  cout << "Karenin kenar boyutu: " << pid << endl;
  alan = pid * pid;
}

sinif::sinif(int pid1, int pid2)
{
  cout << "Dikdörtgenin kenar boyutları: " << pid1 << " " << pid2 << endl;
  alan = pid1 * pid2;
}

sinif::~sinif()
{
  cout << "Nesne yok ediliyor!" << endl;
}

void sinif::deger_goster(void)
{
  cout << "Alan değeri: " << alan << endl;
}

int main(void)
{
  sinif nes01(21);    // Kare için alan hesaplama
  sinif nes02(17, 5); // Dikdörtgen için alan hesaplama
  
  nes01.deger_goster();
  nes02.deger_goster();

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığınız zaman aşağıdaki ifadeleri ekrana yazar:

```

Karenin kenar boyutu: 21
Dikdörtgenin kenar boyutları: 17 5
Alan değeri: 441
Alan değeri: 85
Nesne yok ediliyor!
Nesne yok ediliyor!

```

Program, iki adet nesne oluştururken sinif() constructor fonksiyonunu, her defasında farklı sayıda parametre kullanarak çağırır. Program fonksiyona geçirilen parametrenin sayısına göre aynı isme sahip 2 fonksiyondan ilgili fonksiyonu çağırarak işlem yapar. İlk nesne oluşturmada, ilk değer atama için tek değer kullanıldığından, kare alan hesabı yapan tek parametreli constructor fonksiyonu, ikinci nesne oluşturmada ise, ilk değer atama için iki değer kullanıldığından, dikdörtgen alan hesabı yapan iki parametreli constructor fonksiyonu çağrılır. Her iki constructor fonksiyonu da hesapladığı değeri sınıf içindeki alan değişkenine atar. Sonra, hesapladığı değerleri ekrana yazar.

## Copy constructor fonksiyonları için çoklu görev tanımlama (overloading) işlemi

Bir sınıf cinsinden oluşturduğumuz bir nesne ile birebir aynı bellek adresini taşıyan başka bir nesne kopyası oluşturmak için atama işlemcisini kullanabiliriz. Bu durumda, iki nesnenin herhangi biri üzerinden nesne içeriğinde yer alan değişkenlerde yapılacak değişiklikler, aynı bellek adresini kullandıklarından, diğerini de doğrudan etkileyecektir.

Herhangi bir sınıf cinsinden daha önceden oluşturulmuş olan bir nesneyi kullanarak, aynı sınıf cinsinden ve farklı bellek bölgesini kullanacak başka bir nesne oluşturmak istediğimizde copy constructor fonksiyonları devreye girer.

Copy constructor fonksiyonları bir nesnenin değerlerini kullanarak başka bir nesne oluşturur.

Eğer bir sınıf içinde herhangi bir copy constructor tanımlanmamışsa, derleyici otomatik olarak tanımlar.

Bir sınıf içinde tanımlanacak copy constructor fonksiyonlarının genel yapısı aşağıda gösterilmektedir.

```

sınıf-adı (const sınıf-adı &nes) {
  // Kod bloğu
}

```

Bir sınıf türünden bir nesne tanımladıktan sonra, bu nesneden constructor fonksiyonuyla yeni bir nesne oluşturmak için iki farklı yöntem kullanabiliriz:

```

sınıf-adı ilk-nesne-adı(21);
  
Aşağıdaki her iki işlem satırı aynı işlemi yapar.  
  
sınıf-adı yeni-nesne-adı = ilk-nesne-adı;  // Copy constructor fonksiyonu çağrılır.
sınıf-adı yeni-nesne-adı(ilk-nesne-adı);   // Copy constructor fonksiyonu çağrılır.

```

Bu özelliği bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

class sinif {
  private:
    int id;
  public:
	// Çoklu görev tanımlama işlemi uygulanmış constructor fonksiyonları
	sinif();                 // Parametresiz constructor fonksiyonu
	sinif(int pid);          // Parametreli constructor fonksiyonu
	sinif(const sinif &nes); // Copy constructor fonksiyonu

	void deger_goster(void);
	void deger_degistir(int pid);
};

// Çoklu görev tanımlama işlemi uygulanmış constructor fonksiyonları ana yapısı
sinif::sinif()
{
  id = 0;
  cout << "İlk değer ataması yapmadan nesne oluşturma!" << endl;
}

sinif::sinif(int pid)
{
  id = pid;
  cout << "İlk değer ataması ile nesne oluşturma: " << id << endl;
}

// Copy constructor fonksiyonu
sinif::sinif(const sinif &nes)
{
  id = nes.id;
  cout << "Copy constructor fonksiyonu: " << id << endl;
}

void sinif::deger_goster(void)
{
  cout << &id << " adresindeki" << " id değişken değeri: " << id << endl;
}

void sinif::deger_degistir(int pid)
{
  id = pid;
}

int main(void)
{
  sinif nes01(21);     // Parametreli constructor fonksiyonu ile nesne oluşturma
  sinif nes02;         // Parametresiz constructor fonksiyonu çağrılır.
  sinif nes03 = nes01; // Copy constructor fonksiyonu çağrılır.
  sinif nes04(nes01);  // Copy constructor fonksiyonu çağrılır.

  nes02 = nes01;       // Atama işlemcisi ile nesne bir diğerine atanır.

  nes01.deger_goster();
  nes02.deger_goster();
  nes03.deger_goster();
  nes04.deger_goster();

  nes01.deger_degistir(35);

  nes01.deger_goster();
  nes02.deger_goster();
  nes03.deger_goster();
  nes04.deger_goster();

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığınız zaman aşağıdaki ifadeleri ekrana yazar:

```

İlk değer ataması ile nesne oluşturma: 21
İlk değer ataması yapmadan nesne oluşturma!
Copy constructor fonksiyonu: 21
Copy constructor fonksiyonu: 21
0x6dfeec adresindeki id değişken değeri: 21
0x6dfee8 adresindeki id değişken değeri: 21
0x6dfee4 adresindeki id değişken değeri: 21
0x6dfee0 adresindeki id değişken değeri: 21
0x6dfeec adresindeki id değişken değeri: 35
0x6dfee8 adresindeki id değişken değeri: 21
0x6dfee4 adresindeki id değişken değeri: 21
0x6dfee0 adresindeki id değişken değeri: 21

```

Program, biri parametre atayarak (nes01) diğeri ise parametre atamadan (nes02) iki adet nesne oluşturur. İki farklı yöntemle, copy constructor fonksiyonunu çağırarak, iki adet nesne (nes03 ve nes04) daha oluşturur. Yeni oluşturduğu nesnelere, constructor fonksiyonu yoluyla, ilk oluşturduğu nesnenin (nes01) değerini atar. Atama işlemcisini kullanarak nes02 nesnesine nes01 nesnesini atar. Sonuç olarak, bir nesneye atama işlemcisi ile iki nesneye ise copy constructor yolu ile nes01 nesnesini atar. Bütün nesneler yoluyla id değişken bellek adres ve değerlerini ekrana yazar. nes01 nesnesi yoluyla deger\_degistir() fonksiyonunu kullanarak id değişken değerini değiştirir. Bütün nesneler yoluyla id değişken bellek adres ve değerlerini tekrar ekrana yazar. Sadece ilk nesneye ait değişkene değerinin değiştiği görülür.
