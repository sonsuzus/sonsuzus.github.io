---
title:  C++ Vektörler
author: sonsuz
date: 2023-08-16 19:20:15 +0300
categories: [Program,C++]
tags: [cpp,programlama,vektör]
---



## Vektörler hakkında

Konteynerlerin içinde genel amaçlı kullanımda ileri çıkan vektördür. Vektör sınıfı, ihtiyaç duyulduğunda boyutları artan dinamik dizileri destekler. C++'da bir dizinin boyutu derleme zamanında sabit hale getirilir. Bu uygulama, dizileri kullanmanın en verimli yolu olsa da, çalışma zamanında dizinin boyutu, değişen ihtiyaca göre ayarlanamadığından, esneklik konusunda yeterli değildir. Bir vektör, ihtiyaç duyulan belleği ayırarak bu sorunu çözer.

> Vektörler, **boyutları değişebilen dizileri temsil eden sıralı konteynerlerdir**.Tıpkı diziler gibi, vektörler de elemanları için bitişik depolama konumlarını kullanır. Ancak dizilerden farklı olarak, depolama alanları konteyner tarafından otomatik olarak işleme tutulduğundan, boyutları dinamik olarak değişebilir.
{: .prompt-tip }

Vektörler, boyutu değiştirebilen sıralı konteynerlerdir. Konteyner, aynı türdeki verileri tutan nesnelerdir. Sıra konteynerleri, öğeleri kesinlikle doğrusal sırayla depolar.

Vektörler tıpkı diziler gibi tek bir veri türü ile tanımlanabilir.

Bir vektör için şablon bildiriminin genel yapısı aşağıda gösterilmektedir:

```


template <class T, allocator<T>> class vector


```

T: Kaydedilen veri türünü gösterir.

allocator: Tahsis ediciyi ifade eder.

Vector konteyneri aşağıdaki constructor fonksiyonlarını içerir:

```c++
explicit vector(const Allocator &a = Allocator());

explicit vector(size_type num, const T &val = T(), const Allocator &a = Allocator());

vector(const vector<T, Allocator> &nes);

template <class InIter> vector(InIter start, InIter end, const Allocator &a = Allocator());
```

İlk yapı boş bir vektör oluşturur. İkinci yapı, val değerine sahip num kadar elemanlı bir vektör oluşturur. Üçüncü yapı, nes nesnesi ile aynı elemanları içeren bir vektör oluşturur. Dördüncü yapı, start ve end tekrarlayıcıları ile gösterilen aralıktaki elemanları içeren bir vektör oluşturur.

Azami esneklik ve taşınabilirlik amacıyla, bir vektöre depolanacak herhangi bir nesne, varsayılan bir constructor fonksiyonu tanımlamalıdır. Aynı zamanda, < ve == işlemlerini de tanımlamalıdır.

Bir vektör bildirimi ile örnekler aşağıda yer almaktadır:

```


vector<int> iv;           // Sıfır uzunluğunda int vektör oluşturma
vector<char> cv(10);      // 10 elemanlı char vektör oluşturma
vector<char> cv(10, 'x'); // İlk değer atayarak 10 elemanlı char vektör oluşturma
vector<int> iv2(iv);      // Bir int vektörden int bir vektör oluşturma


```

Aşağıdaki işlemciler vektörlerle birlikte kullanılabilir:

`==, <, <=, !=, >, >=, [ ]`

Vektör konteyneri içinde tanımlanan bazı üye fonksiyonlar aşağıdaki tabloda yer almaktadır:

| Üye fonksiyon | Açıklama |
| --- | --- |
| reference back();const\_reference back() const; | Vektördeki son elemanın referansını geri döndürür. |
| iterator begin();const\_iterator begin() const; | Vektördeki ilk elemanı gösteren bir tekrarlayıcı geri döndürür. |
| void clear(); | Vektördeki tüm elemanları siler. |
| bool empty() const; | Eğer çağıran vektör boş ise doğru, aksi takdirde yanlış bir değer geri döndürür. |
| iterator end();const\_iterator end() const; | Vektörün sonunu gösteren bir tekrarlayıcı geri döndürür. |
| iterator erase(iterator i); | i ile gösterilen elemanı siler.Silinen elemandan sonraki elemanı gösteren bir tekrarlayıcı geri döndürür. |
| iterator erase(iterator start, iterator end); | start ile end arasındaki elemanları siler.Silinen en son elemandan sonraki elemanı gösteren bir tekrarlayıcı geri döndürür. |
| reference front();const\_reference front() const; | Vektördeki ilk elemanı gösteren bir referans geri döndürür. |
| iterator insert(iterator i, const T &val); | i ile gösterilen elemandan hemen önce val değerini ekler.Elemanı gösteren bir tekrarlayıcı geri döndürür. |
| void insert(iterator i, size\_type num, const T &val) | i ile gösterilen elemandan hemen önce num değeri kadar val değerini ekler. |
| template  void insert(iterator i, InIter start, InIter end); | i ile gösterilen elemandan önce start ve end ile gösterilen sırayı ekler. |
| reference operator[ ](size\_type i) const;const\_reference operator[ ](size\_type i) const; | i ile gösterilen elemanın referansını geri döndürür. |
| void pop\_back(); | Vektördeki son elemanı siler. |
| void push\_back(const T &val); | val ile gösterilen değeri vektörün sonuna ekler. |
| size\_type size() const; | Vektördeki elemanların sayısını geri döndürür. |

## Vektör ve dizilerin karşılaştırılması

Çalışma zamanında eleman sayısını artırma veya azaltma işlemlerine ihtiyaç duyulmadığında, vektörler ve diziler aynı amaçla kullanılabilirler. Dizi ve vektör elemanlarına erişim [ ] işlemcisiyle veya diziler için işaretçiler yoluyla vektörler için ise işaretçilere benzer mantıkla çalışan tekrarlayıcılar yoluyla yapılabilir.

Bir vektör bildirimi ile normal bir dizi bildiriminin birlikte ele alındığı bir örneği incelemeye çalışalım:

Örnek

```c++
#include <iostream>
#include <vector>

using namespace std;

int main(void)
{
  vector<int> iv(10); // 10 elemanlı bir int vektör bildirimi yapar.
  int idizi[10];
  int id;

  // iv vektörünün eleman sayısını yazar.
  cout << "iv vektör eleman sayısı: " << iv.size() << endl;

  // idizi dizisinin eleman sayısını yazar.
  int numElem = sizeof(idizi)/sizeof(idizi[0]); // Dizi eleman sayısı
  cout << "idizi dizi eleman sayısı: " << numElem << endl;

  // Vektör ve diziye değer atama işlemi
  for(id=0; id<10; id++) {
      iv[id] = id+1;
      idizi[id] = id+1;
  }

  // Vektör içeriğini ekrana yazma
  cout << "Vektör içeriği: ";
  for(id=0; id<(int)iv.size(); id++) cout << iv[id] << " ";

  cout << endl;

  // Dizi içeriğini ekrana yazma
  cout << "Dizi içeriği: ";
  for(id=0; id<numElem; id++) cout << idizi[id] << " ";

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

iv vektör eleman sayısı: 10
idizi dizi eleman sayısı: 10
Vektör içeriği: 1 2 3 4 5 6 7 8 9 10 
Dizi içeriği: 1 2 3 4 5 6 7 8 9 10 

```

Program, 10'ar elemanlı bir int vektör ile bir int dizi bildirimi yapar. Vektörün eleman sayısını size() fonksiyonu ile dizinin boyutunu ise sizeof() işlemcisi ile dizinin boyutunu tek biri dizi elemanının boyutuna bölüp bularak, ekrana yazar. Bir for döngüsü içinde 1-10 arasındaki sayıları vektör ve diziye indeksleme ile atar. Vektör eleman değerleri ile dizi eleman değerlerini birer for döngüsü kullanarak ekrana yazar.

## Çalışma zamanında eleman ekleyerek vektör boyutunu değiştirme

Vektörlerin en önemli özelliği, çalışma zamanında eleman eklenerek vektör boyutunu değiştirilebilmesidir. Bu özellik sayesinde programda ihtiyaç duyulan boyutlara uygun olarak esneklik sağlanmaktadır.

Şimdi, bu özelliği bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>
#include <vector>

using namespace std;

int main(void)
{
  vector<int> iv(10); // 10 elemanlı bir int vektör bildirimi yapar.
  int id;

  // iv vektörünün eleman sayısını yazar.
  cout << "iv vektör eleman sayısı: " << iv.size() << endl;

  // Vektöre değer atama işlemi
  for(id=0; id<10; id++) iv[id] = id+1;

  // Vektör içeriğini ekrana yazma
  cout << "Vektör içeriği: ";
  for(id=0; id<(int)iv.size(); id++) cout << iv[id] << " ";

  cout << endl;

  // Vektöre yeni değerlerler atayarak eleman sayısını artırma
  for(id=iv.size(); id<20; id++) iv.push_back(id+1);

  // iv vektörünün eleman sayısını yazar.
  cout << "iv vektör eleman sayısı: " << iv.size() << endl;

  // Vektör içeriğini ekrana yazma
  cout << "Vektör içeriği: ";
  for(id=0; id<(int)iv.size(); id++) cout << iv[id] << " ";

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

iv vektör eleman sayısı: 10
Vektör içeriği: 1 2 3 4 5 6 7 8 9 10 
iv vektör eleman sayısı: 20
Vektör içeriği: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 

```

Program, 10 elemanlı bir int vektör bildirimi yapar. Vektörün eleman sayısını size() fonksiyonu ile ekrana yazar. Bir for döngüsü içinde 1-10 arasındaki sayıları vektöre atar. Vektör eleman değerlerini bir for döngüsü kullanarak ekrana yazar. Sonra, push\_back() fonksiyonu ile 11-12 arasındaki sayıları bir for döngüsü ile vektörün sonuna ekler. Vektörün eleman sayısını ve içeriğini tekrar ekrana yazar.

## Vektör elemanlarının değerini [ ] işlemcisi ile değiştirme

Şimdi, vektör eleman değerlerinin değiştirilmesini bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>
#include <vector>

using namespace std;

int main(void)
{
  vector<int> iv(10); // 10 elemanlı bir int vektör bildirimi yapar.
  int id;

  // iv vektörünün eleman sayısını yazar.
  cout << "iv vektör boyutu: " << iv.size() << endl;

  // Vektöre değer atama işlemi
  for(id=0; id<10; id++) iv[id] = id+1;

  // Vektör içeriğini ekrana yazma
  cout << "Vektör içeriği: ";
  for(id=0; id<(int)iv.size(); id++) cout << iv[id] << " ";

  cout << endl;

  // Vektör eleman değerlerini değiştirme
  for(id=0; id<10; id++) iv[id] = iv[id]*iv[id];

  // Vektör içeriğini ekrana yazma
  cout << "Vektör içeriği: ";
  for(id=0; id<(int)iv.size(); id++) cout << iv[id] << " ";

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

iv vektör boyutu: 10
Vektör içeriği: 1 2 3 4 5 6 7 8 9 10 
Vektör içeriği: 1 4 9 16 25 36 49 64 81 100 

```

Program, 10 elemanlı bir int vektör bildirimi yapar. Vektörün eleman sayısını size() fonksiyonu ile ekrana yazar. Bir for döngüsü içinde 1-10 arasındaki sayıları vektöre atar. Vektör eleman değerlerini bir for döngüsü kullanarak ekrana yazar. Sonra, bir for döngüsü ile vektör içindeki her bir elemanın karesini yine kendisine atar. Vektör içeriğini tekrar ekrana yazar.

## Vektör elemanlarının değerini tekrarlayıcı ile değiştirme

Şimdi, vektör elemanlarına değer atama, değerleri yazma ve değiştirme işlemlerinin tekrarlayıcılar yoluyla, while döngüsü kullanarak, yapılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>
#include <vector>

using namespace std;

int main(void)
{
  vector<int> iv(10);        // 10 elemanlı bir int vektör bildirimi yapar.
  vector<int>::iterator ipv; // Tekrarlayıcı bildirimi yapar.
  int id;

  // iv vektörünün eleman sayısını yazar.
  cout << "iv vektör eleman sayısı: " << iv.size() << endl;

  // Vektöre değer atama işlemi
  ipv = iv.begin();
  id=1;
  while(ipv!=iv.end()) {
    *ipv++ = id++;
  }

  // Vektör içeriğini ekrana yazma
  cout << "Vektör içeriği: ";
  ipv = iv.begin();
  while(ipv!=iv.end()) {
    cout << *ipv++ << " ";
  }

  cout << endl;

  // Vektör eleman değerlerini değiştirme
  ipv = iv.begin();
  while(ipv!=iv.end()) {
    *ipv = (*ipv) * (*ipv);
    ipv++;
  }

  // Vektör içeriğini ekrana yazma
  cout << "Vektör içeriği: ";
  ipv = iv.begin();
  while(ipv!=iv.end()) {
    cout << *ipv++ << " ";
  }

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

iv vektör eleman sayısı: 10
Vektör içeriği: 1 2 3 4 5 6 7 8 9 10 
Vektör içeriği: 1 4 9 16 25 36 49 64 81 100 

```

Program, 10 elemanlı bir int vektör ve bir int tekrarlayıcı bildirimi yapar. Vektörün eleman sayısını size() fonksiyonu ile ekrana yazar. Önce, begin() fonksiyonu ile vektörün ilk elemanının bellek adresini ipv adlı tekrarlayıcıya atar. Bir while döngüsü kullanarak, ipv tekrarlayıcısı end() fonksiyonu ile geri döndürülen bellek adresinden farklı olana kadar, id değişken değerini ipv tekrarlayıcısının bellek adresine atar. Döngünün her tekrarında ipv ve id değerleri bir kez artırılır. Aynı yöntemle vektör eleman değerlerini ekrana yazar. Yine aynı yöntemle, vektör içindeki her bir elemanın karesini yine kendisine atar ve eleman değerlerini ekrana yazar.

Şimdi, vektör elemanlarına değer atama, değerleri yazma ve değiştirme işlemlerinin tekrarlayıcılar yoluyla, for döngüsü kullanarak, yapılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>
#include <vector>

using namespace std;

int main(void)
{
  vector<int> iv(10);        // 10 elemanlı bir int vektör bildirimi yapar.
  vector<int>::iterator ipv; // Tekrarlayıcı bildirimi yapar.
  int id;

  // iv vektörünün eleman sayısını yazar.
  cout << "iv vektör eleman sayısı: " << iv.size() << endl;

  // Vektöre değer atama işlemi
  for (ipv=iv.begin(), id=1; ipv!=iv.end(); ) {
       *ipv++ = id++;
  }

  // Vektör içeriğini ekrana yazma
  cout << "Vektör içeriği: ";
  for (ipv=iv.begin(); ipv!=iv.end(); ) {
       cout << *ipv++ << " ";
  }

  cout << endl;

  // Vektör eleman değerlerini değiştirme
  for (ipv=iv.begin(); ipv!=iv.end(); ipv++) {
       *ipv = (*ipv) * (*ipv);
  }

  // Vektör içeriğini ekrana yazma
  cout << "Vektör içeriği: ";
  for (ipv = iv.begin(); ipv!=iv.end(); ) {
       cout << *ipv++ << " ";
  }

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

iv vektör eleman sayısı: 10
Vektör içeriği: 1 2 3 4 5 6 7 8 9 10 
Vektör içeriği: 1 4 9 16 25 36 49 64 81 100 

```

Şimdi, vektör elemanlarının değiştirme işlemlerinin tekrarlayıcılar yoluyla, while döngüsü kullanarak, sondan başa doğru yapılmasını, bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>
#include <vector>

using namespace std;

int main(void)
{
  vector<int> iv(10);        // 10 elemanlı bir int vektör bildirimi yapar.
  vector<int>::iterator ipv; // Tekrarlayıcı bildirimi yapar.
  int id;

  // iv vektörünün eleman sayısını yazar.
  cout << "iv vektör eleman sayısı: " << iv.size() << endl;

  // Vektöre değer atama işlemi
  ipv = iv.begin();
  id=1;
  while(ipv!=iv.end()) {
    *ipv++ = id++;
  }

  // Vektör içeriğini ekrana yazma
  cout << "Vektör içeriği: ";
  ipv = iv.begin();
  while(ipv!=iv.end()) {
    cout << *ipv++ << " ";
  }

  cout << endl;

  // Vektör eleman değerlerini değiştirme
  ipv = iv.end();
  while(ipv!=iv.begin()) {
    ipv--;
    *ipv = (*ipv) * (*ipv);
  }

  // Vektör içeriğini ekrana yazma
  cout << "Vektör içeriği: ";
  ipv = iv.begin();
  while(ipv!=iv.end()) {
    cout << *ipv++ << " ";
  }

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

iv vektör eleman sayısı: 10
Vektör içeriği: 1 2 3 4 5 6 7 8 9 10 
Vektör içeriği: 1 4 9 16 25 36 49 64 81 100 

```

Program, 10 elemanlı bir int vektör ve bir int tekrarlayıcı bildirimi yapar. Vektörün eleman sayısını size() fonksiyonu ile ekrana yazar. Önce, begin() fonksiyonu ile vektörün ilk elemanının bellek adresini ipv adlı tekrarlayıcıya atar. Bir while döngüsü kullanarak, ipv tekrarlayıcısı end() fonksiyonu ile geri döndürülen bellek adresinden farklı olana kadar, id değişken değerini ipv tekrarlayıcısının bellek adresine atar. Döngünün her tekrarında ipv ve id değerleri bir kez artırılır. Aynı yöntemle vektör eleman değerlerini ekrana yazar.

Sonra, end() fonksiyonu ile vektörün son elemanından sonra gelen bellek adresini ipv adlı tekrarlayıcıya atar. Bir while döngüsü kullanarak, ipv tekrarlayıcısı begin() fonksiyonu ile geri döndürülen bellek adresinden farklı olana kadar, her bir eleman değerinin karesini elemana atar. Döngünün her tekrarında ipv değeri işlem yapılmadan önce bir kez azaltılır.

## Vektörlere değer atama yöntemleri

Vektör bildirimlerini yaparken, farklı yöntemler kullanarak boş, değer atanmamış elemanlara sahip veya ilk değer verilmiş elemanlara sahip olarak tanımlama yapabiliriz.

Aşağıda farklı yöntemlerle yapılan vektör bildirimleri gösterilmektedir:

* Sonradan push\_back() fonksiyonu ile elemanları oluşturulan boş vektör bildirimi
* Sonradan [ ] işlemcisi veya tekrarlayıcı ile elemanlarına değer atanan, ilk değer atanmamış elemanlı vektör bildirimi
* Her elemanı aynı değere sahip ilk değer atanan elemanlı vektör bildirimi
* Her elemanına farklı ilk değer atanan elemanlı vektör bildirimi
* Farklı bir vektör elemanları ile ilk değer atanan vektör bildirimi
* Sonradan fill() fonksiyonu ile elemanlarına aynı değer atanan, elemanlı vektör bildirimi

Şimdi, farklı yöntemlerle vektör bildirimi yapılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>
#include <vector>

using namespace std;

int main(void)
{
  vector<int> iv1; // Boş bir vektör bildirimi
  vector<int> iv2(10); // 10 elemanlı bir vektör bildirimi
  vector<int> iv3(10, 21); // Bütün eleman değerleri 21 olan 10 elemanlı bir vektör bildirimi
  vector<int> iv4 = { 1, 2, 3, 4 , 5, 6, 7, 8, 9, 10 }; // C++11 1-10 arasında değerlerin atandığı 10 elemanlı bir vektör bildirimi
  vector<int> iv5(iv4);
  vector<int> iv6(10); // 10 elemanlı bir vektör bildirimi
  vector<int>::iterator ipv; // Tekrarlayıcı bildirimi yapar.
  int id;

  // iv1 vektörüne 1-10 arasındaki sayıları eleman olarak atama
  for(id=1; id<=10; id++) iv1.push_back(id);

  // iv2 vektörüne değer atama işlemi
  for (ipv=iv2.begin(), id=1; ipv!=iv2.end(); ) *ipv++ = id++;

  // iv6 vektörünün tüm elemanlarına 7 sayısını atama
  fill(iv6.begin(), iv6.end(), 7);

  cout << "Vektör boyutları: " << iv1.size() << " " << iv2.size() << " " << iv3.size() << " ";
  cout << iv4.size() << " " << iv5.size() << " " << iv6.size();

  // Vektör içeriklerini ekrana yazma
  cout << "\nVektör içerikleri:\n";
  cout << "------------------\n";

  cout << "iv1: ";
  for (ipv=iv1.begin(); ipv!=iv1.end(); ) cout << *ipv++ << " ";

  cout << "\niv2: ";
  for (ipv=iv2.begin(); ipv!=iv2.end(); ) cout << *ipv++ << " ";

  cout << "\niv3: ";
  for (ipv=iv3.begin(); ipv!=iv3.end(); ) cout << *ipv++ << " ";

  cout << "\niv4: ";
  for (ipv=iv4.begin(); ipv!=iv4.end(); ) cout << *ipv++ << " ";

  cout << "\niv5: ";
  for (ipv=iv5.begin(); ipv!=iv5.end(); ) cout << *ipv++ << " ";

  cout << "\niv6: ";
  for (ipv=iv6.begin(); ipv!=iv6.end(); ) cout << *ipv++ << " ";

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Vektör boyutları: 10 10 10 10 10 10
Vektör içerikleri:
------------------
iv1: 1 2 3 4 5 6 7 8 9 10 
iv2: 1 2 3 4 5 6 7 8 9 10 
iv3: 21 21 21 21 21 21 21 21 21 21 
iv4: 1 2 3 4 5 6 7 8 9 10 
iv5: 1 2 3 4 5 6 7 8 9 10 
iv6: 7 7 7 7 7 7 7 7 7 7 

```

Program, 6 adet vektör bildirimi yapar. İlk vektörü boş olarak, ikinci vektörü 10 elemanlı olarak, üçüncü vektörü herbirinin değeri 21 olan 10 elemanlı olarak, dördüncü vektörü 1-10 arasındaki sayılar ilk değer atama yöntemiyle atanmış 10 elemanlı olarak, beşinci vektörü dördüncü vektörden oluşturarak, altıncı vektörü 10 elemanlı olarak tanımlar.

Önce boş olan iv1 vektörüne push\_back() fonksiyonu ile 1-10 arasındaki sayıları atar. iv2 vektör elemanlarına ipv tekrarlayıcısını kullanarak 1-10 arasındaki sayıları atar. iv6 vektör elemanlarına find() fonksiyonunu kullanarak 7 değerini atar.

Tüm vektörlerin eleman sayısını size() fonksiyonu ile eleman değerlerini de tekrarlayıcı yoluyla ekrana yazar.

## Vektörün herhangi bir sırasına eleman ekleme ve silme

Bir vektörü oluşturduktan sonra, elemanların her birine [ ] işlemcisi veya tekrarlayıcılar kullanarak değer atayabilir ve push\_back() fonksiyonunu kullanarak vektörün sonuna yeni eleman ekleyebiliriz.

Vektörün herhangi bir sırasına eleman eklemek için ise, insert() fonksiyonunu kullanabiliriz.

Vektördeki elemanlardan birisini silmek için erase() fonksiyonunu kullanabiliriz.

Şimdi, vektör elemanlarına değer atama, değerleri yazma ve değiştirme işlemlerinin tekrarlayıcılar yoluyla, while döngüsü kullanarak, yapılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>
#include <vector>

using namespace std;

int main(void)
{
  vector<int> iv(10);        // 10 elemanlı bir int vektör bildirimi yapar.
  vector<int>::iterator ipv; // Tekrarlayıcı bildirimi yapar.
  int id;

  // Vektöre değer atama işlemi
  for(id=0; id<10; id++) iv[id] = id+1;

  // Vektör içeriğini ekrana yazma
  cout << "Vektör içeriği: ";
  for(id=0; id<(int)iv.size(); id++) cout << iv[id] << " ";

  cout << endl;

  // Vektöre yeni elemanlar ekleme
  ipv = iv.begin();
  ipv += 3;
  iv.insert(ipv, 5, 21);
  for(id=iv.size(); id<20; id++) iv.push_back(id+1);

  // Vektör içeriğini ekrana yazma
  cout << "Vektör içeriği: ";
  for(id=0; id<(int)iv.size(); id++) cout << iv[id] << " ";

  cout << endl;

  // Vektöre eklenen 5 elemanın ilk ikisini silme
  ipv = iv.begin();
  ipv += 4;
  iv.erase(ipv, ipv+2);

  // Vektör içeriğini ekrana yazma
  cout << "Vektör içeriği: ";
  for(id=0; id<(int)iv.size(); id++) cout << iv[id] << " ";

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Vektör içeriği: 1 2 3 4 5 6 7 8 9 10 
Vektör içeriği: 1 2 3 21 21 21 21 21 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 
Vektör içeriği: 1 2 3 21 21 21 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 

```

Program, 10 elemanlı bir int vektör ve bir int tekrarlayıcı bildirimi yapar. 1-10 arasındaki sayıları vektör elemanlarına atar ve eleman değerlerini ekrana yazar. Önce, begin() fonksiyonu ile vektörün ilk elemanının bellek adresini ipv adlı tekrarlayıcıya atar. Tekrarlayıcı değerini üç defa artırarak tekrarlayıcının vektördeki dördüncü elemanın bellek adresini göstermesini sağlar. Önce, insert() fonksiyonunu kullanarak, bu adrese beş defa 21 değerini ekler. Sonra, push\_back() fonksiyonunu kullanarak, vektörün sonuna 11-20 arasındaki sayıları ekler. Vektör eleman değerlerini ekrana yazar. Vektöre eklenen 5 elemanın ilk ikisini erase() fonksiyonu ile sildikten sonra, vektör eleman değerlerini tekrar ekrana yazar.

## Vektörlerle sınıf nesneleri kullanma

Bir vektöre herhangi bir veri türünden oluşturulan nesneleri kaydedebiliriz.

Şimdi, bir vektör üzerinde sınıf ile ilgili işlemlerin yapılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>
#include <vector>

using namespace std;

class sinif {
  private:
    int priid;

  protected:
    int proid;

  public:
    int pubid;
    sinif(int pid1, int pid2, int pid3)
    {
      priid = pid1; proid = pid2; pubid = pid3;
    }
    sinif() { };
    void deger_ata(int pid1, int pid2, int pid3)
    {
      priid = pid1; proid = pid2; pubid = pid3;
    }
    void deger_goster()
    {
      cout << "priid=" << priid << " proid=" << proid << " pubid=" << pubid << endl;
    }
};

int main(void)
{
  vector<sinif> cv(5); // 5 elemanlı bir sinif vektör bildirimi yapar.
  int id;

  // Vektör içindeki nesnelere değer atama işlemi
  for(id=1; id<=5; id++) cv[id-1].deger_ata(id, id*id, id*id*id);

  // Vektör içindeki nesne değişken değerlerini ekrana yazma
  for(id=0; id<(int)cv.size(); id++) {
      cout << "cv[" << id << "]: ";
      cv[id].deger_goster();
  }

  cout << endl;

  // Vektöre nesne ekleme
  for(id=cv.size()+1; id<=10; id++) cv.push_back(sinif(id, id*id, id*id*id));

  // Vektör içindeki nesne değişken değerlerini ekrana yazma
  for(id=0; id<(int)cv.size(); id++) {
      cout << "cv[" << id << "]: ";
      cv[id].deger_goster();
  }

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

cv[0]: priid=1 proid=1 pubid=1
cv[1]: priid=2 proid=4 pubid=8
cv[2]: priid=3 proid=9 pubid=27
cv[3]: priid=4 proid=16 pubid=64
cv[4]: priid=5 proid=25 pubid=125

cv[0]: priid=1 proid=1 pubid=1
cv[1]: priid=2 proid=4 pubid=8
cv[2]: priid=3 proid=9 pubid=27
cv[3]: priid=4 proid=16 pubid=64
cv[4]: priid=5 proid=25 pubid=125
cv[5]: priid=6 proid=36 pubid=216
cv[6]: priid=7 proid=49 pubid=343
cv[7]: priid=8 proid=64 pubid=512
cv[8]: priid=9 proid=81 pubid=729
cv[9]: priid=10 proid=100 pubid=1000

```

Program, içinde private, protected ve public olmak üzere üç adet değişken ve parametreli ve parametresiz olmak üzere, iki adet constructor fonksiyonu ile değişkenlere değer atayan ve ekranda gösteren iki adet fonksiyon tanımladığı sinif adlı bir sınıf oluşturur.

sinif türünden 5 elemanlı bir vektör bildirimi yapar. Vektör içindeki her bir nesneyi sıra ile kullanarak deger\_ata() fonksiyonu yoluyla sınıf içindeki değişkenlere 1-5 arasındaki sayıların sırasıyla kendisini, karesini ve küpünü atar. Sonra, deger\_goster() fonksiyonu yoluyla, vektör içindeki nesnelerin temsil ettiği sınıf kopyasının değişken değerlerini ekrana yazar.

Önce, push\_back() fonksiyonunu kullanarak, vektör sonuna 5 yeni nesne ekler. Bu fonksiyona geçirilen parametre değeri parametreli constructor fonksiyonudur. Sonra, deger\_goster() fonksiyonu yoluyla, vektör içindeki nesnelerin temsil ettiği sınıf kopyasının değişken değerlerini tekrar ekrana yazar.

Şimdi, aynı programı tekrarlayıcıları kullanacak şekilde düzenlediğimiz bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>
#include <vector>

using namespace std;

class sinif {
  private:
    int priid;

  protected:
    int proid;

  public:
    int pubid;
    sinif(int pid1, int pid2, int pid3)
    {
      priid = pid1; proid = pid2; pubid = pid3;
    }
    sinif() { };
    void deger_ata(int pid1, int pid2, int pid3)
    {
      priid = pid1; proid = pid2; pubid = pid3;
    }
    void deger_goster()
    {
      cout << "priid=" << priid << " proid=" << proid << " pubid=" << pubid << endl;
    }
};

int main(void)
{
  vector<sinif> cv(5);         // 5 elemanlı bir sinif vektör bildirimi yapar.
  vector<sinif>::iterator cpv; // Tekrarlayıcı bildirimi yapar.
  int id;

  // Vektör içindeki nesnelere değer atama işlemi
  for (cpv=cv.begin(), id=1; cpv!=cv.end(); id++) {
       cpv++->deger_ata(id, id*id, id*id*id);
  }

  // Vektör içindeki nesne değişken değerlerini ekrana yazma
  for (cpv=cv.begin(); cpv!=cv.end(); ) {
       cpv++->deger_goster();
  }

  cout << endl;

  // Vektöre nesne ekleme
  for(id=cv.size()+1; id<=10; id++) cv.push_back(sinif(id, id*id, id*id*id));

  // Vektör içindeki nesne değişken değerlerini ekrana yazma
  for (cpv=cv.begin(); cpv!=cv.end(); ) {
       cpv++->deger_goster();
  }

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

priid=1 proid=1 pubid=1
priid=2 proid=4 pubid=8
priid=3 proid=9 pubid=27
priid=4 proid=16 pubid=64
priid=5 proid=25 pubid=125

priid=1 proid=1 pubid=1
priid=2 proid=4 pubid=8
priid=3 proid=9 pubid=27
priid=4 proid=16 pubid=64
priid=5 proid=25 pubid=125
priid=6 proid=36 pubid=216
priid=7 proid=49 pubid=343
priid=8 proid=64 pubid=512
priid=9 proid=81 pubid=729
priid=10 proid=100 pubid=1000

```

Program, içinde private, protected ve public olmak üzere üç adet değişken ve parametreli ve parametresiz olmak üzere, iki adet constructor fonksiyonu ile değişkenlere değer atayan ve ekranda gösteren iki adet fonksiyon tanımladığı sinif adlı bir sınıf oluşturur.

sinif türünden 5 elemanlı bir vektör ve bir tekrarlayıcı bildirimi yapar. Vektör içindeki her bir nesneyi gösteren tekrarlayıcıyı sıra ile kullanarak deger\_ata() fonksiyonu yoluyla sınıf içindeki değişkenlere 1-5 arasındaki sayıların sırasıyla kendisini, karesini ve küpünü atar. Sonra, deger\_goster() fonksiyonu yoluyla, vektör içindeki nesnelerin temsil ettiği sınıf kopyasının değişken değerlerini tekrarlayıcı kullanarak ekrana yazar.

Önce, push\_back() fonksiyonunu kullanarak, vektör sonuna 5 yeni nesne ekler. Bu fonksiyona geçirilen parametre değeri parametreli constructor fonksiyonudur. Sonra, deger\_goster() fonksiyonu yoluyla, vektör içindeki nesnelerin temsil ettiği sınıf kopyasının değişken değerlerini tekrarlayıcı kullanarak tekrar ekrana yazar.
