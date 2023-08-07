---
title:  C++ İşlemci çoklu görev (Overloading)
author: sonsuz
date: 2023-08-07 22:19:17 +0300
categories: [Program,C++]
tags: [programlama,cpp,çoku görev,overloading]
---



## İşlemci çoklu görev tanımlama (Overloading)

C++'da işlemci çoklu görev tanımlama işlemi yapılırken de çok biçimlilik özelliği kullanılır. Bir işlemci için çoklu görev tanımlama işlemi yapıldığında, işlemci, sahip olduğu özelliklerin yanı sıra, bir sınıfa bağlı olarak ek işlem yapma özelliği kazanır.

Bir işlemci için çoklu görev tanımlama işlemi yapıldığında yani birden fazla işlem yapma kapasitesi kazandırıldığında, işlemcinin orjinal fonksiyonu ortadan kalkmaz.

> İşlemcilere çoklu görev tanımlama işlemi yapmak için işlemci fonksiyonları oluşturulur. Bir işlemci fonksiyonu, çoklu görev tanımlama uygulanan işlemcinin bağlı olduğu sınıfa göre gerçekleştireceği işlemleri tanımlar.
{: .prompt-tip }

İşlemci fonksiyonu operator anahtar kelimesi kullanılarak oluşturulur. İşlemci fonksiyonları, bir sınıfın üyesi olabilir veya olmayabilir. Üye olmayan işlemci fonksiyonları, sınıf için friend fonksiyon olarak tanımlanır. İşlemci fonksiyonlarının yapısı sınıf üyesi olma ve olmama durumuna göre farklılık gösterir.

## Sınıf üyesi olarak tanımlanan işlemci çoklu görev tanımlama fonksiyonları

Sınıf üyesi olarak tanımlanan işlemci fonksiyonunun genel yapısı aşağıda gösterilmektedir:

```cpp
veri-türü sınıf-adı::operatorişlemci(parametreler)
{
  // Kod bloğu
}

```

İşlemci fonksiyonları herhangi bir geçerli veri türü döndürebilmesine rağmen, genellikle ilgili oldukları sınıf cinsinden bir nesne geri döndürür. Çoklu görev tanımlama işlemi yapılacak olan işlemci operator anahtar kelimesinin hemen sağında yer alan "işlemci" ifadesinin yerine konacaktır.

Çoklu görev tanımlama işlemini, tek değere işlem yapan bir işlemciye uygularsak, parametre listesi boş olacak, iki değere işlem yapan bir işlemciye uygularsak, parametre listesinde tek bir parametre yer alacaktır.

Şimdi, + işlemcisine üye fonksiyon ile çoklu görev tanımlama işlemi uygulamasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```cpp
#include <iostream>

using namespace std;

class sinif {
  private:
    int id;
  public:
	// Çoklu görev tanımlama işlemi uygulanmış constructor fonksiyonları
	sinif();        // Parametresiz constructor fonksiyonu
	sinif(int pid); // Parametreli constructor fonksiyonu

	void deger_goster(void);
	
	// Sınıf üyesi olarak tanımlanmış + işlemcisi fonksiyonu 
	sinif operator+(sinif nes);
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

// Sınıf üyesi olarak tanımlanmış + işlemcisi fonksiyonu 
sinif sinif::operator+(sinif nes)
{
  sinif lnes;
  // id değişken değeri işlemcinin sol tarafında yer alan
  // nesneye ait olup this işaretçisi ile erişim sağlanır.
  lnes.id = nes.id + id;

  return lnes;
}

void sinif::deger_goster(void)
{
  cout << "id değişken değeri: " << id << endl;
}

int main(void)
{
  sinif nes01(21);             // Parametreli constructor fonksiyonu ile nesne oluşturma
  sinif nes02(17);             // Parametreli constructor fonksiyonu ile nesne oluşturma
  
  sinif nes03 = nes01 + nes02; // Çoklu görev tanımlama işlemi uygulanmış + işlemcisinin kullanımı

  nes01.deger_goster();
  nes02.deger_goster();
  nes03.deger_goster();

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

İlk değer ataması ile nesne oluşturma: 21
İlk değer ataması ile nesne oluşturma: 17
İlk değer ataması yapmadan nesne oluşturma!
id değişken değeri: 21
id değişken değeri: 17
id değişken değeri: 38

```

Program, parametre atayarak nes01 ve nes02 adlı iki adet nesne oluşturur. Üçüncü nesne olan nes03 nesnesini oluştururken değer atamak yerine çoklu görev tanımlama işlemi işlem uygulanmış + işlemcisinin fonksiyonunu kullanarak ilk iki nesnenin id değişken değerlerini toplayarak nes03 nesnesinin id değişkenine atar. Bütün nesneler yoluyla id değişken değerlerini ekrana yazar.

Burada, + işlemcisi sol tarafında yer alan nes01 nesnesi işlemci fonksiyonuna this işaretçisi yoluyla, nes02 nesnesi ise parametre olarak geçirilir. Fonksiyonun sonunda sinif cinsinden bir nesne geri döndürülür.

## Friend olarak tanımlanan işlemci çoklu görev tanımlama işlemi fonksiyonları

Bir sınıfın üyesi olmayan friend fonksiyon kullanarak bir sınıf için bir işlemciye çoklu görev tanımlama işlemi işlemi uygulayabiliriz. Bir friend fonksiyon bir sınıfın üyesi olmadığından this işaretçisi ile kullanılamaması, çoklu görev tanımlama işlemi yapılan işlemcinin fonksiyonunda, tek değere işlem yapan işlemciler için tek parametre, iki değere işlem yapan işlemciler için iki parametre yer alacaktır.

Sınıf üyesi olarak tanımlanan işlemci fonksiyonunun genel yapısı aşağıdadır:

![](cprog/oproverload01.png)

Şimdi, + işlemcisine üye olmayan friend bir fonksiyon ile çoklu görev tanımlama işlemi uygulamasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```cpp
#include <iostream>

using namespace std;

class sinif {
  private:
    int id;
  public:
	// Çoklu görev tanımlama işlemi uygulanmış constructor fonksiyonları
	sinif();        // Parametresiz constructor fonksiyonu
	sinif(int pid); // Parametreli constructor fonksiyonu

	void deger_goster(void);
	
	// Sınıf üyesi olarak tanımlanmış + işlemcisi fonksiyonu 
	friend sinif operator+(sinif nes01, sinif nes02);
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

// Friend fonksiyon olarak tanımlanmış + işlemcisi fonksiyonu 
sinif operator+(sinif nes01, sinif nes02)
{
  sinif lnes;
 
  lnes.id = nes01.id + nes02.id;

  return lnes;
}

void sinif::deger_goster(void)
{
  cout << "id değişken değeri: " << id << endl;
}

int main(void)
{
  sinif nes01(21);             // Parametreli constructor fonksiyonu ile nesne oluşturma
  sinif nes02(17);             // Parametreli constructor fonksiyonu ile nesne oluşturma
  
  sinif nes03 = nes01 + nes02; // Çoklu görev tanımlama işlemi uygulanmış + işlemcisinin kullanımı

  nes01.deger_goster();
  nes02.deger_goster();
  nes03.deger_goster();

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

İlk değer ataması ile nesne oluşturma: 21
İlk değer ataması ile nesne oluşturma: 17
İlk değer ataması yapmadan nesne oluşturma!
id değişken değeri: 21
id değişken değeri: 17
id değişken değeri: 38

```

Program, parametre atayarak nes01 ve nes02 adlı iki adet nesne oluşturur. Üçüncü nesne olan nes03 nesnesini oluştururken değer atamak yerine çoklu görev tanımlama işlemi uygulanmış + işlemcisinin fonksiyonunu kullanarak ilk iki nesnenin id değişken değerlerini toplayarak nes03 nesnesinin id değişkenine atar. Bütün nesneler yoluyla id değişken değerlerini ekrana yazar.

Burada, + işlemcisinin her iki tarafında yer alan nes01 ve nes02 nesneleri parametre olarak geçirilir. Fonksiyonun sonunda sinif cinsinden bir nesne geri döndürülür.

Friend fonksiyonlarla işlemcileri için çoklu görev tanımlama işlemi uygulanamaz.

= () [] ->

Friend fonksiyon kullanılarak, ++ ve -- işlemcilerine çoklu görev tanımlama işlemi uyguladığımızda, friend fonksiyonlar this işaretçisini kullanamadığından, fonksiyona geçirilen parametreleri referans değer olarak geçirmemiz gerekir. Referans değer olarak geçirdiğimizde fonksiyon içinde parametre değerinde yapılan değişiklik fonksiyon sona erdikten sonra da geçerli olacaktır.

Şimdi, ++ ve -- işlemcilerine üye olmayan friend bir fonksiyon ile çoklu görev tanımlama işlemi uygulamasını bir örnek üzerinde incelemeya çalışalım:

Örnek

```cpp
#include <iostream>

using namespace std;

class sinif {
  private:
    int id;
  public:
	// Çoklu görev tanımlama işlemi uygulanmış constructor fonksiyonları
	sinif();        // Parametresiz constructor fonksiyonu
	sinif(int pid); // Parametreli constructor fonksiyonu

	void deger_goster(void);
	
	// Sınıf üyesi olarak tanımlanmış ++ işlemcisi fonksiyonu 
	friend sinif operator++(sinif &nes);
	// Sınıf üyesi olarak tanımlanmış -- işlemcisi fonksiyonu
	friend sinif operator--(sinif &nes);
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

// Friend fonksiyon olarak tanımlanmış ++ işlemcisi fonksiyonu 
sinif operator++(sinif &nes)
{
  nes.id++;
  
  return nes;
}

// Friend fonksiyon olarak tanımlanmış -- işlemcisi fonksiyonu 
sinif operator--(sinif &nes)
{
  nes.id--;
  
  return nes;
}

void sinif::deger_goster(void)
{
  cout << "id değişken değeri: " << id << endl;
}

int main(void)
{
  sinif nes01(21);       // Parametreli constructor fonksiyonu ile nesne oluşturma
  
  sinif nes02 = ++nes01; // nes01 nesnesini bir artırarak nes02 nesnesine atama
  
  nes01.deger_goster();
  nes02.deger_goster();
  
  --nes01;                 // nes01 nesnesini bir azaltma

  nes01.deger_goster();
  nes02.deger_goster();
  
  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

İlk değer ataması ile nesne oluşturma: 21
id değişken değeri: 22
id değişken değeri: 22
id değişken değeri: 21
id değişken değeri: 22

```

Program, parametre atayarak nes01 adlı bir nesne oluşturur. İkinci nesne olan nes02 nesnesini oluştururken ++ işlemcisi ile nes01 nesnesini bir artırarak nes02 nesnesine atar. Nesneler içindeki id değişken değerlerini ekrana yazar. Sonra -- işlemcisini kulanarak nes01 nesnesini bir azaltır ve nesneler içindeki id değişken değerlerini tekrar ekrana yazar.

Burada, ++ ve -- işlemcileri nesne değişkeninin önünde yer almalıdır. Aksi takdirde, derleyici hata verir.

Eğer ++ ve -- işlemcilerine friend fonksiyonlar ile çoklu görev tanımlama işlemi uyguladığımızda, ++ ve -- işlemcilerini nesne değişkenlerinin önünde tanımlamak istersek, fonksiyon bildiriminde ve genel yapısında hayali bir parametre kullanmamız gerekir. Şimdi bu özelliği yukarıdaki örneği değiştirerek incelemeye çalışalım: 

Örnek

```cpp
#include <iostream>

using namespace std;

class sinif {
  private:
    int id;
  public:
	// Çoklu görev tanımlama işlemi uygulanmış constructor fonksiyonları
	sinif();        // Parametresiz constructor fonksiyonu
	sinif(int pid); // Parametreli constructor fonksiyonu

	void deger_goster(void);
	
	// Sınıf üyesi olarak tanımlanmış ++ işlemcisi fonksiyonu
	friend sinif operator++(sinif &nes, int id);
	// Sınıf üyesi olarak tanımlanmış -- işlemcisi fonksiyonu
	friend sinif operator--(sinif &nes, int id);
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

// Friend fonksiyon olarak tanımlanmış ++ işlemcisi fonksiyonu 
sinif operator++(sinif &nes, int id)
{
  nes.id++;
  
  return nes;
}

// Friend fonksiyon olarak tanımlanmış -- işlemcisi fonksiyonu 
sinif operator--(sinif &nes, int id)
{
  nes.id--;
  
  return nes;
}

void sinif::deger_goster(void)
{
  cout << "id değişken değeri: " << id << endl;
}

int main(void)
{
  sinif nes01(21);       // Parametreli constructor fonksiyonu ile nesne oluşturma
  
  sinif nes02 = nes01++; // nes01 nesnesini bir artırarak nes02 nesnesine atama
  
  nes01.deger_goster();
  nes02.deger_goster();
  
  nes01--;                 // nes01 nesnesini bir azaltma

  nes01.deger_goster();
  nes02.deger_goster();
  
  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

İlk değer ataması ile nesne oluşturma: 21
id değişken değeri: 22
id değişken değeri: 22
id değişken değeri: 21
id değişken değeri: 22

```

Program bir önceki programın yaptığı işlemin aynısını yapar. Tek farkı, ++ ve -- işlemcilerinin nesne değişkeninden sonra yer almasıdır.

## << ve >> işlemcilerine çoklu görev tanımlama işlemi uygulama

C++'da, << ve >> işlemcilerini mevcut ve kullanıcı tanımlı veri tipleri üzerinde giriş ve çıkış işlemleri yapabilmek için çoklu görev tanımlama işlemi uygulayabiliriz.

## Akışlara veri gönderen << işlemcisine çoklu görev tanımlama işlemi uygulama

Oluşturduğumuz bir sınıf için aşağıdaki genel yapı ile bir << işlemcisine çoklu görev tanımlama işlemi uygulayabiliriz:

```cpp
ostream &operator<<(ostream &stream, const sınıf_adı &nesne)
{
  // Kod bloğu
  return stream;
}

```

İlk parametre çıkış akışını gösteren bir akış olmalıdır.

İkinci parametre çıkış işlem yapılacak sınıftan oluşturulan bir nesne referansı olmalıdır.

Çoklu görev tanımlama işlemi ile elde edilen << fonksiyonu mutlaka stream değeri geri döndürmelidir.

Şimdi, çoklu görev tanımlama işlemi yapılmış bir << işlemcisinin kullanılmasını bir örnek üzerinde incelemeye çalışalım:

```cpp
#include <iostream>

using namespace std;

class sinif {
  public:
    int pubid1, pubid2, pubid3;
    sinif(int pid1, int pid2, int pid3)
    {
      pubid1 = pid1; pubid2 = pid2; pubid3 = pid3;
    }
    void deger_goster()
    {
      cout << "Değişken değerleri (Sınıf fonksiyonu ile): " << pubid1 << " " << pubid2 << " " << pubid3 << endl;
    }
};

// Çoklu görev tanımlamag işlemi uygulanmış << işlemcisi fonksiyonu
ostream &operator<<(ostream &stream, const sinif &nes)
{
  stream << "Değişken değerleri (<< fonksiyonu ile): " << nes.pubid1 << " " << nes.pubid2 << " " << nes.pubid3 << endl;

  return stream;
}

int main(void)
{
  sinif nes(7, 21, 143);

  nes.deger_goster(); // Değerlerin sınıf fonksiyonu ile gösterilmesi

  cout << nes;        // Değerlerin çoklu görev tanımlama işlemi uygulanmış << işlemcisi fonksiyonu ile gösterilmesi

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Değişken değerleri (Sınıf fonksiyonu ile): 7 21 143
Değişken değerleri (<< fonksiyonu ile): 7 21 143

```

Program, üç adet public int değer, bu int değerlere birer değer atayan constructor fonksiyonu ve bu değerleri ekranda gösteren bir fonksiyon içeren bir sınıf oluşturur. Ayrıca, << işlemcisine çoklu görev tanımlamag işlemi uygulayarak, kendisine geçirilen nesne yoluyla bir sınıf kopyası içindeki değişken değerlerini ekranda gösteren, bir fonksiyon oluşturur. Sonra, oluşturduğu sınıftan bir nesne bildirimi yapar. Nesne yoluyla, sınıf kopyası içinde yer alan değişken değerlerini önce sınıf fonksiyonu ile sonra da çoklu görev tanımlama işlemi ile oluşturulan fonksiyon ile ekrana yazar.

Programda, << işlemcisine çoklu görev tanımlama işlemi ile oluşturulan fonksiyon sınıfın bir elemanı olarak tanımlanmamıştır.

> Herhangi bir operatör fonksiyonu bir sınıfın üyesi olduğunda, ilk parametresi işlemci fonsiyonuna yapılan çağrıyı oluşturan nesnedir. Ayrıca bu nesne, operatör fonksiyonunun üyesi olduğu sınıfın bir nesnesidir. Herhangi bir işlemci için yapılan çoklu görev tanımlama işlemi ile oluşturulan bir fonksiyon bir sınıfın üyesi ise, en soldaki parametre bu sınıfın bir nesnesi olmalıdır.
{: .prompt-warning }

```

veri-türü sınıf-adı::operator<<(sınıf_adı nesne)

```

Ancak, << işlemcisi ile yapılan çoklu görev tanımlama işlemi ile oluşturulan bir fonksiyonda, en solda yer alan ilk parametre bir stream değeri, ikinci parametre ise sınıftan oluşturulmuş bir nesne olmalıdır.

```cpp
ostream &operator<<(ostream &stream, const sınıf_adı &nesne)

```

Bu nedenlerle, << işlemcisi ile yapılan çoklu görev tanımlama işlemi ile oluşturulan fonksiyonlar işlem yaptıkları sınıfın üyesi olamazlar.

<< işlemcisine çoklu görev tanımlama işlemi uygulanarak oluşturulan fonksiyonlar işlem yaptıkları sınıfın bir üyesi olamadığından, sınıfın private elemanlarına erişim sağlamaları için, bu fonksiyonlar friend fonksiyon olarak tanımlanır.

Şimdi, bu özelliği bir örnek üzerinde incelemeye çalışalım:

```cpp
#include <iostream>

using namespace std;

class sinif {
  private:
    int priid1, priid2, priid3;

  public:
    sinif(int pid1, int pid2, int pid3)
    {
      priid1 = pid1; priid2 = pid2; priid3 = pid3;
    }
    void deger_goster()
    {
      cout << "Değişken değerleri (Sınıf fonksiyonu ile): " << priid1 << " " << priid2 << " " << priid3 << endl;
    }

    friend ostream &operator<<(ostream &stream, const sinif &nes);
};

// Çoklu görev tanımlama işlemi uygulanmış << işlemcisi fonksiyonu
ostream &operator<<(ostream &stream, const sinif &nes)
{
  stream << "Değişken değerleri (<< fonksiyonu ile): " << nes.priid1 << " " << nes.priid2 << " " << nes.priid3 << endl;

  return stream;
}

int main(void)
{
  sinif nes(7, 21, 143);

  nes.deger_goster(); // Değerlerin sınıf fonksiyonu ile gösterilmesi

  cout << nes; // Değerlerin çoklu görev tanımlama işlemi uygulanmış << işlemcisi fonksiyonu ile gösterilmesi

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Değişken değerleri (Sınıf fonksiyonu ile): 7 21 143
Değişken değerleri (<< fonksiyonu ile): 7 21 143

```

Program, üç adet private int değer, bu int değerlere birer değer atayan constructor fonksiyonu ve bu değerleri ekranda gösteren bir fonksiyon içeren bir sınıf oluşturur. Ayrıca, << işlemcisine çoklu görev tanımlama işlemi uygulayarak, kendisine geçirilen nesne yoluyla bir sınıf kopyası içindeki değişken değerlerini ekranda gösteren, friend bir fonksiyon oluşturur. Sonra, oluşturduğu sınıftan bir nesne bildirimi yapar. Nesne yoluyla, sınıf kopyası içinde yer alan değişken değerlerini önce sınıf fonksiyonu ile sonra da çoklu görev tanımlama işlemi ile oluşturulan fonksiyon ile ekrana yazar.

## Akışlardan veri alan >> işlemcisine çoklu görev tanımlama işlemi uygulama

Oluşturduğumuz bir sınıf için aşağıda genel yapı ile bir >> işlemcisine çoklu görev tanımlama işlemi uygulayabiliriz:

```cpp
istream &operator>>(istream &stream, sınıf_adı &nesne)
{
  // Kod bloğu
  return stream;
}

```

İlk parametre giriş akışını gösteren bir akış olmalıdır.

İkinci parametre giriş işlemi yapılacak sınıftan oluşturulan bir nesne referansı olmalıdır.

Çoklu görev tanımlama işlemi ile elde edilen >> fonksiyonu mutlaka stream değeri geri döndürmelidir.

Şimdi, bu özelliği bir örnek üzerinde incelemeye çalışalım:

```cpp
#include <iostream>

using namespace std;

class sinif {
  private:
    int priid1, priid2, priid3;

  public:
    sinif() {
      priid1=0; priid2=0; priid3=0;
    }
    sinif(int pid1, int pid2, int pid3)
    {
      priid1 = pid1; priid2 = pid2; priid3 = pid3;
    }
    void deger_goster(void)
    {
      cout << "Değişken değerleri (Sınıf fonksiyonu ile): " << priid1 << " " << priid2 << " " << priid3 << endl;
    }
    friend ostream &operator<<(ostream &stream, const sinif &nes);
    friend istream &operator>>(istream  &stream, sinif &nes);
};

ostream &operator<<(ostream &stream, const sinif &nes)
{
  stream << "Değişken değerleri (<< fonksiyonu ile): " << nes.priid1 << " " << nes.priid2 << " " << nes.priid3 << endl;

  return stream;
}

istream &operator>>(istream &stream, sinif &nes)
{
  cout << "1.değişken değerini giriniz: ";
  stream >> nes.priid1;

  cout << "2.değişken değerini giriniz: ";
  stream >> nes.priid2;

  cout << "3.değişken değerini giriniz: ";
  stream >> nes.priid3;

  return stream;
}

int main(void)
{
  sinif nes;

  cin >> nes;         // Değerlerin çoklu görev tanımlama işlemi uygulanmış >> işlemcisi fonksiyonu ile girilmesi

  nes.deger_goster(); // Değerlerin sınıf fonksiyonu ile gösterilmesi

  cout << nes;        // Değerlerin çoklu görev tanımlama işlemi uygulanmış << işlemcisi fonksiyonu ile gösterilmesi

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

1.değişken değerini giriniz: 7
2.değişken değerini giriniz: 21
3.değişken değerini giriniz: 35
Değişken değerleri (Sınıf fonksiyonu ile): 7 21 35
Değişken değerleri (<< fonksiyonu ile): 7 21 35

```

Program, üç adet private int değer, bu int değerlere parametre almadan sıfır değeri atayan bir constructor fonksiyonu, birer int değer atayan parametre alan bir constructor fonksiyonu ve bu değerleri ekranda gösteren bir fonksiyon içeren bir sınıf oluşturur. Sonra, >> işlemcisine çoklu görev tanımlama işlemi uygulayarak, kendisine geçirilen nesne referansı yoluyla bir sınıf kopyası içindeki değişken değerlerine klavyeden değer alan friend bir fonksiyon oluşturur ve << işlemcisine overloading işlemi uygulayarak, kendisine geçirilen nesne yoluyla bir sınıf kopyası içindeki değişken değerlerini ekranda gösteren, friend bir fonksiyon oluşturur. Oluşturduğu sınıftan bir nesne bildirimi yapar. Nesne yoluyla, sınıf kopyası içinde yer alan değişken değerlerine overloading işlemi ile oluşturulan fonksiyon ile değer atar. Sonra, değişken değerlerini önce sınıf fonksiyonu ile sonra da overloading işlemi ile oluşturulan fonksiyon ile ekrana yazar.

## Dönüştürme fonksiyonları oluşturma

C++'da, bir sınıftan oluşturulan nesnenin veri türünü herhangi bir veri türüne çevirmek istediğimizde, dönüştürme fonksiyonlarını kullanabiliriz.

Dönüştürme fonksiyonlarının genel yapısı aşağıda gösterilmektedir:

operator veri-türü { return deger; }

veri-türü: Sınıftan oluşturulan nesnenin dönüştürüleceği veri türünü gösterir.

deger: DÖnüşüm işleminden sonra sınıftan oluşturulan nesnenin alacağı değeri gösterir.

Dönüştürme fonksiyonları;

* Sadece veri-türü ile tanımlanan veri türünden veri geri döndürebilir.
* Parametre ile kullanılmazlar.
* İşlem yaptığı sınıfın bir üyesi olmalıdır.
* Türetilmiş sınıflara aktarılabilirler.
* Sanal olarak tanımlanabilirler.

Şimdi, dönüştürme fonksiyonlarının kullanılmasını bir örnek üzerinde incelemeye çalışalım:

```cpp
#include <iostream>

using namespace std;

class sinif {
  private:
    int priid;

  public:
    sinif(int pid=0) { priid = pid; };
    operator int() { return priid; } // Dönüştürme fonksiyonu bildirimi
};

int main(void)
{
  sinif nes(21);

  int id = nes; // Dönüştürme fonksiyonu kullanımı

  cout << "id değişken değeri: " << id;

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

id değişken değeri: 21

```

Program, priid adlı private int bir değer, bu int değere parametre ile bir değer atayan bir constructor fonksiyonu ve priid değişken değerini geri döndüren bir dönüştürme fonksiyonu içeren bir sınıf oluşturur. Bu sınıftan nes adlı bir nesne oluşturarak 21 değerini atar. Sonra, oluşturduğu id değişken değerine nes adlı nesneyi atadığında, dönüştürme fonksiyonu yoluyla id değişkenine 21 değerini atar. Değişken değerini ekrana yazar.
