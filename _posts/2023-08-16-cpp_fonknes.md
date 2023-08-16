---
title:  C++ Fonksiyon nesneleri
author: sonsuz
date: 2023-08-16 23:14:49 +0300
categories: [Program,C++]
tags: [progrmalama,cpp,fonksiyon,nesne]
---


## Fonksiyon nesneleri hakkında

Fonksiyonları nesneleri, fonksiyon çağırma işlemcisi olan () işlemcisine çoklu görev tanımlama (overloading) işlemi uygulanarak, bir sınıftan oluşturulan nesnelerin bir fonksiyon gibi çağrılmasını sağlanmasıyla oluşturulur.

Tekli fonksiyon nesnesi tek bir parametre, ikili fonksiyon nesnesi ise iki parametre gerektirir.

## Yerleşik fonksiyon nesneleri

Tekli fonksiyon nesnesi tek bir parametre, ikili fonksiyon nesnesi ise iki parametre gerektirir.

STL içinde yer alan fonksiyon nesneleri aşağıdaki tabloda gösterilmektedir:

Fonksiyon nesneleri

| divides | equal\_to | greater | greater\_equal | less |
| less\_equal | logical\_and | logical\_not \* | logical\_or | minus |
| modulus | multiplies | negate \* | not\_equal\_to | plus |

Yanında \* işareti bulunanlar tek parametrelidir.

Fonksiyon nesneleri isimleri ile belirtilen işlemleri gerçekleştirir.

Yerleşik fonksiyon nesneleri, () işlemcisine çoklu görev tanımlama işlemi uygulayan, şablon sınıfları olup seçilen veri türü için belirtilen işlemin sonucunu geri döndürür. Örneğin, float verisi için plus() fonksiyon nesnesini çağırmak için aşağıdaki yapıyı kullanabiliriz:

`plus<float>()`

Yerleşik fonksiyon nesneleri `<functional>` başlık dosyasını kullanır.

Şimdi, tek parametre alan bir fonksiyon nesnesinin kullanımını bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>

using namespace std;

int main(void)
{
  // Boş bir int vektör bildirimi yapar.
  vector<int> iv;
  vector<int>::iterator ipv; // Tekrarlayıcı bildirimi yapar.
  int id;

  // iv vektörüne 1-10 arasındaki sayıları eleman olarak atama
  for(id=1; id<=10; id++) iv.push_back(id);

  // Vektör içeriğini ekrana yazma
  cout << "Vektör içeriği: ";
  for (ipv=iv.begin(); ipv!=iv.end(); ) cout << *ipv++ << " ";

  cout << endl;

  // negate() fonksiyon nesnesini kullanma
  ipv = transform(iv.begin(), iv.end(), iv.begin(), negate<int>());

  // Vektör içeriğini ekrana yazma
  cout << "Vektör içeriği: ";
  for (ipv=iv.begin(); ipv!=iv.end(); ) cout << *ipv++ << " ";

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Vektör içeriği: 1 2 3 4 5 6 7 8 9 10 
Vektör içeriği: -1 -2 -3 -4 -5 -6 -7 -8 -9 -10

```

Program, 10 elemanlı bir int vektör ve bir tekrarlayıcı bildirimi yapar. Bir for döngüsü içinde, push\_back() fonksiyonu ile, 1-10 arasındaki sayıları vektöre atar. Bir for döngüsü içinde, tekrarlayıcı kullanarak vektör eleman değerlerini ekrana yazar. Sonra, transform() algoritmasının son parametresinde negate() fonksiyon nesnesi kullanarak, vektör eleman değerlerini eksi hale getirir. Vektör eleman değerlerini bir for döngüsü kullanarak tekrar ekrana yazar.

Şimdi, iki parametre alan bir fonksiyon nesnesinin kullanımını bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>

using namespace std;

int main(void)
{
  // İki adet boş int vektör bildirimi yapar.
  vector<int> iv1, iv2;
  vector<int>::iterator ipv; // Tekrarlayıcı bildirimi yapar.
  int id;

  // iv vektörüne 1-10 arasındaki sayıları eleman olarak atama
  for(id=1; id<=10; id++) {
      (id%2) ? iv1.push_back(id) : iv2.push_back(id);
  }

  // Vektör içeriklerini ekrana yazma
  cout << "iv1 vektör içeriği: ";
  for (ipv=iv1.begin(); ipv!=iv1.end(); ) cout << *ipv++ << " ";
  cout << endl;

  cout << "iv2 vektör içeriği: ";
  for (ipv=iv2.begin(); ipv!=iv2.end(); ) cout << *ipv++ << " ";
  cout << endl;

  // plus() fonksiyon nesnesini kullanma
  ipv = transform(iv1.begin(), iv1.end(), iv2.begin(), iv1.begin(), plus<int>());

  // Vektör içeriklerini ekrana yazma
  cout << "iv1 vektör içeriği: ";
  for (ipv=iv1.begin(); ipv!=iv1.end(); ) cout << *ipv++ << " ";
  cout << endl;

  cout << "iv2 vektör içeriği: ";
  for (ipv=iv2.begin(); ipv!=iv2.end(); ) cout << *ipv++ << " ";

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

iv1 vektör içeriği: 1 3 5 7 9 
iv2 vektör içeriği: 2 4 6 8 10 
iv1 vektör içeriği: 3 7 11 15 19 
iv2 vektör içeriği: 2 4 6 8 10 

```

Program, 10 elemanlı iki adet int vektör ve bir tekrarlayıcı bildirimi yapar. Bir for döngüsü içinde, push\_back() fonksiyonu ile, 1-10 arasındaki sayıların tek olanlarını iv1 vektörüne çift olanlarını ise iv2 vektörüne atar. Bir for döngüsü içinde, tekrarlayıcı kullanarak vektör eleman değerlerini ekrana yazar. Sonra, transform() algoritmasının son parametresinde plus() fonksiyon nesnesi kullanarak, vektör eleman değerlerini toplayarak iv1 vektörüne atar. Vektör eleman değerlerini bir for döngüsü kullanarak tekrar ekrana yazar.

Burada, transform() algoritmasının 4.parametresi elde edilen toplam değerlerin aktarılacağı vektörün bağlangıcını gösterir.

## Fonksiyon nesneleri oluşturma

STL içinde yer alan yerleşik fonksiyonlarının dışında, kendimize ait fonksiyon nesneleri tanımlayabiliriz. Bu işlemi gerçekleştirmek için, () işlemcisine çoklu görev tanımlama işlemi uygulayan bir sınıf tanımlayabiliriz:

Şimdi, fonksiyon nesnesinin kullanımını bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

// Fonksiyon nesnesi için sınıf bildirimi
class deger_ekle {
  private:
    int priid;

  public:
    deger_ekle(int pid) : priid(pid) {}  // Constructor fonksiyonu
    int operator()(int id) const { return priid + id; } // () işlemcisine çoklu görev tanımlama işlemi uygulama
    void deger_goster(void) { cout << "priid değişken değeri: " << priid << "\n"; }
};

int main(void)
{
  int id;
  deger_ekle nes(21); // deger_ekle sınıfından bir nesne bildirimi yapar.

  nes.deger_goster(); // priid değişken değerini gösterir.

  id = nes(8); // Fonksiyon nesnesi ile priid değişken değeri ile 8 değerini toplar.
  nes.deger_goster();
  cout << "id değişken değeri: " << id << "\n";

  id = nes(14); // Fonksiyon nesnesi ile priid değişken değeri ile 14 değerini toplar.
  nes.deger_goster();
  cout << "id değişken değeri: " << id << "\n";

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

priid değişken değeri: 21
priid değişken değeri: 21
id değişken değeri: 29
priid değişken değeri: 21
id değişken değeri: 35

```

Program, priid adlı private bir değişken, bir constructor fonksiyonu ve değişken değerini ekranda gösteren deger\_goster() adlı bir fonksiyon ve () işlemcisine çoklu görev tanımlama işlemi uygulanarak tanımlanmış, kendisine geçirilen parametre değerini priid değişken değeri ile toplayarak elde ettiği değeri geri döndüren bir fonksiyon içeren deger\_ekle adlı bir sınıf oluşturur.

Bir int değişken ve 21 değerini atayarak deger\_ekle sınıfından nes adlı bir nesne oluşturur. Sonra, nes nesnesi yoluyla deger\_goster() fonksiyonunu çağırarak, priid değişken değerini ekrana yazar.

8 değerini parametre olarak geçirerek fonksiyon nesnesini çağırır. () işlemcisine çoklu görev tanımlama işlemi uygulanarak elde edilen fonksiyon içinde, 21 olan priid değerine 8 değerini ekleyerek, elde ettiği değeri geri döndürür ve id değişkenine atar. priid değişken değeri aynı kalır. Sonra, deger\_goster() fonksiyonu ile priid değişken değerini ve id değişken değerini doğrudan ekrana yazar. Sonra, aynı işlemleri 21 yerine 14 sayısını kullanarak yapar.

Şimdi, fonksiyon nesnesinin kullanımını farklı bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

// Fonksiyon nesnesi bildirimi
class kare_al {
  public:
    int operator()(int id) const { return id * id; } // () işlemcisine çoklu görev tanımlama işlemi uygulama
};

int main(void)
{
  int id;
  kare_al nes; // kare_al sınıfından bir nesne bildirimi yapar.

  id = nes(7); // Fonksiyon nesnesi ile 7 sayısının karesini alır.
  cout << "id değişken değeri: " << id << "\n";

  id = nes(21); // Fonksiyon nesnesi ile 21 sayısının karesini alır.
  cout << "id değişken değeri: " << id << "\n";

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

id değişken değeri: 64
id değişken değeri: 196

```

Program, () işlemcisine çoklu görev tanımlama işlemi uygulanarak tanımlanmış, kendisine geçirilen parametre değerin karesini alarak, elde ettiği değeri geri döndüren bir fonksiyon içeren kare\_al adlı bir sınıf oluşturur.

Bir int değişken ve kare\_al sınıfından nes adlı bir nesne oluşturur. 7 değerini parametre olarak geçirerek fonksiyon nesnesini çağırır. () işlemcisine çoklu görev tanımlama işlemi uygulanarak elde edilen fonksiyon içinde, 7 değerinin karesini alarak, elde ettiği değeri geri döndürür ve id değişkenine atar. Sonra, aynı işlemleri 7 yerine 21 sayısını kullanarak yapar.

## Fonksiyon nesnelerini konteynerlerle kullanma

Tanımladığımız fonksiyon nesnelerini konteynerlerle de kullanabiliriz.

Şimdi, fonksiyon nesnesinin konteynerlerle kullanımını bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// Fonksiyon nesnesi bildirimi
class deger_ekle {
  private:
    int priid;

  public:
    deger_ekle(int pid) : priid(pid) {}  // Constructor fonksiyonu
    int operator()(int id) const { return priid + id; } // () işlemcisine çoklu görev tanımlama işlemi uygulama
    void deger_goster(void) { cout << "priid değişken değeri: " << priid << "\n"; }
};

int main(void)
{
  vector<int> iv; // Boş bir vektör bildirimi yapar.
  vector<int>::iterator ipv; // Tekrarlayıcı bildirimi yapar.
  int id;

  // iv vektörüne 1-10 arasındaki sayıları eleman olarak atama
  for(id=1; id<=10; id++) iv.push_back(id);

  // Vektör içeriğini ekrana yazma
  cout << "Vektör içeriği: ";
  for (ipv=iv.begin(); ipv!=iv.end(); ) cout << *ipv++ << " ";

  cout << endl;

  // deger_ekle fonksiyon nesnesi transform algoritmasına parametre olarak geçirilir.
  // deger_ekle fonksiyon nesnesi vektörün her bir elemanı için çağrılır ve sonuç yine vektöre atanır.
  ipv = transform(iv.begin(), iv.end(), iv.begin(), deger_ekle(10));

  // Vektör içeriğini ekrana yazma
  cout << "Vektör içeriği: ";
  for (ipv=iv.begin(); ipv!=iv.end(); ) cout << *ipv++ << " ";

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Vektör içeriği: 1 2 3 4 5 6 7 8 9 10 
Vektör içeriği: 11 12 13 14 15 16 17 18 19 20 

```

Program, priid adlı private bir değişken, bir constructor fonksiyonu ve değişken değerini ekranda gösteren deger\_goster() adlı bir fonksiyon ve () işlemcisine çoklu görev tanımlama işlemi uygulanarak tanımlanmış, kendisine geçirilen parametre değerini priid değişken değeri ile toplayarak elde ettiği değeri geri döndüren bir fonksiyon içeren deger\_ekle adlı bir sınıf oluşturur.

Program, 10 elemanlı bir int vektör ve bir tekrarlayıcı bildirimi yapar. Bir for döngüsü içinde, push\_back() fonksiyonu ile, 1-10 arasındaki sayıları vektöre atar. Bir for döngüsü içinde, tekrarlayıcı kullanarak vektör eleman değerlerini ekrana yazar. Sonra, transform() algoritmasının son parametresinde deger\_ekle() fonksiyon nesnesi 10 parametre değeri ile kullanarak, vektör eleman değerlerine 10 ekler. deger\_ekle fonksiyon nesnesi vektörün her bir elemanı için çağrılır ve sonuç yine vektöre atanır. Vektör eleman değerlerini bir for döngüsü kullanarak tekrar ekrana yazar.
