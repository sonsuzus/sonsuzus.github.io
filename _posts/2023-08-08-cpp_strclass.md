---
title:  C++ String sınıfı
author: sonsuz
date: 2023-08-08 21:43:05 +0300
categories: [Program,C++]
tags: [cpp,programlama,string,sınıf]
---


## String sınıfı hakkında

C++'da karakter dizisi işlemleri için boş bir karakterle ('\0') sonlandırılan karakter dizilerinin yanı sıra, string veri türündeki sınıf nesnelerini de kullanabiliriz.

Aslında, string sınıfı, basic\_string şablon sınıfını temel almaktadır. 8 bitlik karakter dizilerini destekleyen sınıfın adı string, geniş karakterli dizileri destekleyen sınıfın adı ise wstring'dir.

C++'da, boş bir karakterle ('\0') sonlandırılan karakter dizileri ile ilgili işlemler değer atama, kopyalama ve ekleme gibi işlemler **cstring** (string.h) başlık dosyasında yer alan fonksiyonlarla gerçekleştirilebilmektedir. Ancak, bu tür işlemleri yapmak için işlemciler kullanılamamaktadır. Bu işlemleri gerçekleştirmek için, string sınıfı ile işlemciler rahatlıkla kullanılabilir.

> String sınıfını kullanmanın diğer önemli bir avantajı da, boş bir karakterle sonlandırılan karakter dizilerinde yaşanan boyut üzerinde işlem yapma sorunlarının yaşanmamasıdır.
{: .prompt-tip }

String sınıfı kullanmanın sağladığı avantajlar:

- Karakter dizileri işlemlerinde işlemciler kullanılabilir.

- Karakter dizileri işlemlerinde boyut üzerinde işlem yapma sorunu yaşanmaz.

- Algoritmaları da destekleyen string sınıfını programlarımızda kullanmak için, `<string>` başlık dosyasını programımıza eklememiz gerekir.

Birçok üye fonksiyon ve constructor fonksiyonu içeren string sınıfında en yaygın olarak kullanılan constructor fonksiyonlarının genel yapısı aşağıda gösterilmektedir:

```cpp
string();
string(const char *str);
string(const string &str);


```

İlk yapı boş bir string nesnesi oluşturur.

İkinci yapı, str ile gösterilen ve boş bir karakterle sonlandırılan bir string nesnesi oluşturur. Boş bir karakterle sonlandırılan karakter dizisi string nesnelerine çevrilir.

Üçüncü yapı, diğer bir string nesnesinden bir string nesnesi oluşturur.

String nesnelerine uygulanabilecek işlemler aşağıdaki tabloda gösterilmektedir:

Kullanılan işlemciler

|   İşlemci  | Anlamı |   İşlemci  | Anlamı |
| = | Atama | <= | Küçük veya eşit |
| + | Ekleme | > | Büyüktür |
| += | Ekleyerek atama | >= | Büyük veya eşit |
| == | Eşitlik | [ ] | Subscripting |
| != | Eşitsizlik | << | Çıkış |
| < | Küçüktür | >> | Giriş |

## String sınıfından nesne oluşturma ve değer atama

Şimdi, string sınıfının kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```cpp
#include <iostream>
#include <string>

using namespace std;

int main(void)
{
  string str1;           // Boş nesne oluşturma
  string str2 = "bbbbb"; // Nesne oluştururken atama işlemcisi ile ilk değer atama
  string str3("ccccc");  // Nesne oluştururken constructor fonksiyonu ile ilk değer atama
  string str4(str3);     // Nesne oluştururken atama işlemcisi ile başka bir nesneden ilk değer atama
  string str5;           // Boş nesne oluşturma
  string str6;           // Boş nesne oluşturma

  str1 = "aaaaa"; // str1 nesnesine karakter dizisi atama
  str5 = str4;    // str4 nesnesini str5 nesnesine atama

  // str1 ve str2 nesnelerini birleştirerek str6 nesnesine atama
  str6 = str1 + str2;

  cout << "str1: " << str1 << " str2: " << str2 << " str3: " << str3 << "\n";
  cout << "str4: " << str4 << " str5: " << str5 << " str6: " << str6;

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

str1: aaaaa str2: bbbbb str3: ccccc
str4: ccccc str5: ccccc str6: aaaaabbbbb

```

Program, string sınıfından str1, str2 ve str3 adlı üç adet boş nesne, atama işlemcisi ile ilk değer atadığı str2 adlı bir nesne, constructor fonksiyonu ile ilk değer atadığı str3 adlı bir nesne ve başka bir nesneden ilk değer atadığı str4 adlı bir nesne oluşturur.

Atama işlemcisini kullanarak, bir karakter dizisini str1 nesnesine ve str4 nesnesini str5 nesnesine atar. + işlemcisini kullanarak, str1 ve str2 nesnelerini birleştirir ve str6 nesnesine atar. Tüm nesnelerin değerlerini ekrana yazar.

## String sınıfı ile karşılaştırma işlemcilerini kullanma

Şimdi, karşılaştırma işlemcilerinin string sınıfı ile kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```cpp
#include <iostream>
#include <string>

using namespace std;

int main(void)
{
  string str1("aaaaa");
  string str2("bbbbb");
  string str3(str1);     // Nesne oluştururken atama işlemcisi ile başka bir nesneden ilk değer atama

  if (str1!=str2) {
      cout << "str1 ve str2 nesneleri birbirinden farklıdır!" << "\n";

      if (str1>str2) cout << "str1 nesnesi str2 nesnesinden büyüktür!" << "\n";
      else cout << "str1 nesnesi str2 nesnesinden küçüktür!" << "\n";
  }

  if (str1==str3) cout << "str2 ve str3 nesneleri birbirine eşittir!";

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

str1 ve str2 nesneleri birbirinden farklıdır!
str1 nesnesi str2 nesnesinden küçüktür!
str2 ve str3 nesneleri birbirine eşittir!

```

Program, string sınıfından constructor fonksiyonu ile ilk değer atadığı str1 ve str2 adlı iki nesne ile constructor fonksiyonu ile str1 nesnesinden ilk değer atadığı str3 adlı bir nesne oluşturur.

!= işlemcisini str1 ve str2 nesnelerini karşılaştırır, birbirine eşit olmadığından if koşulu kod bloğuna giriş yapar. Bu defa, > işlemcisini kullanarak, str1 nesnesinin str2 nesnesinden büyük olup olmadığını kontrol eder. Büyük olmadığından if koşulu gerçekleşmez ve else kod satırı devreye girer. Sonra, == işlemcisini kullanarak str1 ve str3 birbirine eşit olup olmadığını kontrol eder. Eşit olduğundan, karakter dizini ekrana yazar.

## String sınıfı üye fonksiyonlarını kullanma

İşlemcilerin yanı sıra, string sınıfı üye fonksiyonlarını kullanarak ta karakter string nesneleri ile işlemler gerçekleştirebiliriz.

## String sınıfı nesne içeriklerini değiştirmek için üye fonksiyonları kullanma

String sınıfı üye fonksiyonlarını kullanarak, bir string nesnesine değer atayabilir, sonuna veya arasına bir karakter dizisi ekleyebilir, bir bölümünü değiştirebilir, sonuna karakter ekleyebilir, son karakterini silebilir, belirli sayıda karakteri silebiliriz. Ayrıca, iki string nesnesini birbiriyle değiştirebiliriz.

Şimdi, üye fonksiyonların string sınıfı nesnelerini değiştirmek için kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```cpp
#include <iostream>
#include <string>

using namespace std;

int main(void)
{
  string str1;
  string str2("bbbbb");

  str1.assign("aaaaa"); // str1 nesnesine karakter dizisi atama
  cout << "str1: " << str1 << "\n";

  str1.append("aaaaa"); // str1 nesnesine karakter dizisi ekleme
  cout << "str1: " << str1 << "\n";

  str1.insert(3, "ccccc"); // str1 nesnesine belirli bir indekse karakter dizisi ekleme
  cout << "str1: " << str1 << "\n";

  str1.replace(5, 3, "ddd"); // str1 nesnesinde belirli bir indekste belirli uzunlukta karakter dizisi ekleme
  cout << "str1: " << str1 << "\n";

  str1.push_back('e'); // str1 nesnesinin sonuna bir karakter ekleme
  cout << "str1: " << str1 << "\n";

  str1.pop_back(); // C++11 str1 nesnesinin sonundaki karakteri silme
  cout << "str1: " << str1 << "\n";

  str1.erase(3, 5); // str1 nesnesinde belirli bir indekste belirli uzunlukta karakter dizisini silme
  cout << "str1: " << str1 << "\n";

  str1.swap (str2); // str1 ve str2 nesnelerini değiştirme
  cout << "str1: " << str1 << " str2: " << str2;

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

str1: aaaaa
str1: aaaaaaaaaa
str1: aaacccccaaaaaaa
str1: aaaccdddaaaaaaa
str1: aaaccdddaaaaaaae
str1: aaaccdddaaaaaaa
str1: aaaaaaaaaa
str1: bbbbb str2: aaaaaaaaaa

```

Program, string sınıfından str1 adlı boş bir nesne ve constructor fonksiyonu ile ilk değer atadığı str2 adlı bir nesne oluşturur.

assign() fonksiyonunu kullanarak, str1 nesnesine "aaaaa" karakter dizisini atar. append() fonksiyonunu kullanarak, str1 nesnesine "aaaaa" karakter dizisini ekler. insert() fonksiyonunu kullanarak, str1 nesnesinin 3.indeksine "ccccc" karakter dizisini ekler. replace() fonksiyonunu kullanarak, str1 nesnesinin 5.indeksinde 3 karakter uzunluğundaki bölümü "ddd" karakter dizisi ile değiştirir. push\_back() fonksiyonunu kullanarak, str1 nesnesinin sonuna 'e' karakteri ekler. pop\_back() fonksiyonunu kullanarak, str1 nesnesinin sonundaki 'e' karakterini siler. erase() fonksiyonunu kullanarak, str1 nesnesinin 3.indeksinde 5 karakter uzunluğundaki bölümü siler. Son olarak, swap() fonksiyonu ile str1 ve 
str2 nesnelerini değiştirir. Yaptığı her işlem sonrasında nesneyi ekrana yazar.

## String sınıfı nesnelerinde karakterlere erişim

String sınıfı nesnelerinde karakterlere erişim için at() üye fonksiyonunu veya [ ] işlemcisini kullanabiliriz.

Şimdi, string sınıfı nesnelerinde karakterlere doğrudan erişim sağlama işlemini bir örnek üzerinde incelemeye çalışalım:

Örnek

```cpp
#include <iostream>
#include <string>

using namespace std;

int main(void)
{
  string str("Bilgisayar");

  cout << "3.indekste yer alan karakter: " << str.at(3) << "\n";
  cout << "3.indekste yer alan karakter: " << str[3];

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

3.indekste yer alan karakter: g
3.indekste yer alan karakter: g

```

Program, string sınıfından constructor fonksiyonu ile ilk değer atadığı str adlı bir nesne oluşturur. Önce at() fonksiyonunu sonra [ ] işlemcisini kullanarak, nesnenin 3.karakterini ekrana yazar.

## String sınıfı nesnelerinde dizi işlemleri

String sınıfından bir nesne içinde, bir karakter dizisinin indeksini bulma, bir alt dizi geri döndürme ve alt dizilerle karşılaştırma gibi işlemleri üye fonksiyonlarla gerçekleştirebiliriz.

Şimdi, string sınıfı nesnelerinde dizi işlemleri yapılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```cpp
#include <iostream>
#include <string>

using namespace std;

int main(void)
{
  string str1 ("String sınıfı içinde arama, alt karakter dizisi alma ve karşılaştırma işlemleri");
  string str2 ("arama");

  // str1 nesnesi içinde "arama" kelimesinin indeksini alma
  size_t strindex = str1.find(str2);
  if (strindex!=string::npos) cout << "\"arama\" kelimesinin indeksi: " << strindex << "\n";

  // str1 nesnesi içinde 32.indeksten itibaren tüm karakterleri alma
  cout << str1.substr(32) << "\n";

  // str1 nesnesi içinde 32.indeksten itibaren 8 karakteri alma
  cout << str1.substr(32, 8) << "\n";

  // str1 nesnesi içinde 14.indeksten itibaren 6 karakteri içeren dizi ile "içinde" kelimesini karşılaştırma
  if (!str1.compare(14, 6, "içinde")) cout << "str1 nesnesinin 14.indeksten itibaren 6 karakteri içeren dizi ile \"içinde\" kelimesi aynıdır!";

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

"arama" kelimesinin indeksi: 21
karakter dizisi alma ve karşılaştırma işlemleri
karakter
str1 nesnesinin 14.indeksten itibaren 6 karakteri içeren dizi ile "içinde" kelimesi aynıdır!

```

Program, string sınıfından constructor fonksiyonu ile ilk değer atadığı str1 ve str2 adlı iki adet nesne oluşturur. Önce, str2 nesnesini parametre olarak geçirerek, str1 nesnesi ile find() fonksiyonunu çağırır. str2 nesnesi içinde yer alan "arama" kelimesininin, str1 nesnesi içinde bulunduğu konumun indeksini ekrana yazar. Sonra, str1 nesnsi ile substr() fonksiyonunu kullanarak, 32.indeksten itibaren tüm karakterleri ve 32.indeksten itibaren 8 karakteri ekrana yazar. Daha sonra, str1 nesnsi ile compare() fonksiyonunu kullanarak, 14.indeksten itibaren 6 karakteri içeren dizi ile "içinde" kelimesini karşılaştırarak sonucu ekrana yazar.

## String sınıfı nesneleri boyut belirleme ve içerik silme işlemleri

String sınıfından bir nesne ile ilgili boyut alma, yeniden boyutlandırma, içeriğini silme ve boş olup olmadığını kontrol etme işlemlerini, üye fonksiyonlarla gerçekleştirebiliriz. Şimdi, string sınıfı nesnelerinde bu işlemlerin yapılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```cpp
#include <iostream>
#include <string>

using namespace std;

int main(void)
{
  string str ("String sınıfı boyut işlemleri");

  // Nesnenin boyutunu alma
  cout << "str nesnesinin boyutu: " << str.size() << " byte" << "\n";
  cout << "str nesnesinin boyutu: " << str.length() << " byte" << "\n";

  // Bir karakteri belirli sayıda ekleyerek nesneyi yeniden boyutlandırma
  str.resize(str.size()+5, 'i');
  cout << "str : " << str << "\n";

  // Nesneyi yeniden boyutlandırma
  str.resize(13);
  cout << "str : " << str << "\n";

  // Nesne içini silme
  str.clear();
  cout << "str : " << str << "\n";

  if (str.empty()) cout << "str nesne içi boştur.";

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

str nesnesinin boyutu: 29 byte
str nesnesinin boyutu: 29 byte
str : String sınıfı boyut işlemleriiiiii
str : String sınıfı
str : 
str nesne içi boştur.

```

Program, string sınıfından constructor fonksiyonu ile ilk değer atadığı str adlı bir nesne oluşturur. size() ve length() fonksiyonlarını kullanarak, str nesnesinin boyutunu ekrana yazar. Önce, resize() fonksiyonu yoluyla, 'i' karakterini 5 defa ekleyerek nesneyi yeniden boyutlandırır. Sonra, yine resize() fonksiyonu yoluyla, nesnenin boyutunu 13 karaktere indirir. clear() fonksiyonunu kullanarak, nesnenin içini tamamen boşaltır. empty() fonksiyonunu kullanarak, nesne içeriğinin boş olup olmadığın kontro eder. Tüm işlemlerin sonuçlarını ekrana yazar.

## String sınıfını tekrarlayıcılarla kullanma

String sınıfı ile ilgili işlemlerde takrarlayıcıları kullanabiliriz. Şimdi, string sınıfı nesnelerinde bu işlemlerin yapılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```cpp
#include <iostream>
#include <string>

using namespace std;

int main(void)
{
  string str ("String sınıfı işlemleri");
  string::iterator sp;
  int id;

  // Nesne içeriğini [ ] işlemcisi ile ekrana yazma
  cout << "str: ";
  for(id=0; id<(int)str.size(); id++) cout << str[id];

  cout << endl;

  // Nesne içeriğini tekrarlayıcı ile ekrana yazma
  cout << "str: ";
  for (sp=str.begin(); sp!=str.end(); ) {
       cout << *sp++;
  }

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

str: String sınıfı işlemleri
str: String sınıfı işlemleri

```

Program, string sınıfından constructor fonksiyonu ile ilk değer atadığı str adlı bir nesne ve bir tekrarlayıcı oluşturur. Nesne içeriğini önce [ ] işlemcisini sonra tekrarlayıcı kullanarak ekrana yazar.
