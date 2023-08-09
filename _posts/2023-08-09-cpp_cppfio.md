---
title:  C++ dosya Giriş/Çıkış (I/O)
author: sonsuz
date: 2023-08-09 17:05:46 +0300
categories: [Program,C++]
tags: [programlama,cpp,dosya,giriş,çıkış,io]
---


## Dosya giriş/çıkış işlemleri için kullanılan başlık dosyası ve sınıflar

Dosya giriş/çıkış işlemlerini gerçekleştirmek için programlarımızın başına <fstream> başlık dosyasını eklememiz gerekir. Bu dosyada ifstream, ofstream ve fstream sınıflarının da yer aldığı bazı sınıf bildirimleri yer alır. Bu sınıflar sırasıyla, ios sınıfından türetilen istream, ostream ve iostream sınıflarından türetilmiş olduğundan, ios sınıfı içindeki tüm değişken ve fonksiyonlara erişim sağlayabilirler.

| Ana sınıf | Türetilmiş sınıf | Türetilenden türetilmiş sınıf |
| --- | --- | --- |
| ios | istream | ifstream |
| ios | ostream | ofstream |
| ios | iostream | fstream |

## Dosya açma ve kapama işlemleri

C++'da, bir dosyayı açmak için akışları kullanabiliriz. Giriş, çıkış ve giriş/çıkış olmak üzere üç tür akış vardır. Giriş akışı oluşturmak için akışı ifstream sınıfı olarak, çıkış akışı oluşturmak için akışı ofstream sınıfı olarak ve giriş ve çıkış işlemlerinin her ikisini gerçekleştirmek için akışı fstream sınıfı olarak bildirmemiz gerekir.

Aşağıdaki ifadeler bir adet giriş, bir adet çıkış ve bir adet hem giriş hem de çıkış işlemi yapan bir adet akış oluşturur:

```c++
ifstream in;  // Giriş akışı
ofstream out; // Çıkış akışı
fstream io;   // Giriş ve çıkış akışı

```

## Dosya açma işlemleri

Bir akış oluşturduktan sonra, akışı bir dosya ile ilişkilendirerek dosya açmak için, her üç akış sınıfının içinde ayrı ayrı tanımlanmış olan open() üye fonksiyonu kullanılır. Open() fonksiyonunun bildirimleri aşağıda gösterilmektedir:

`void ifstream::open(const char *dosya-adı, ios::openmode mode = ios::in);`

`void ofstream::open(const char *dosya-adı, ios::openmode mode = ios::out | ios::trunc);`

`void fstream::open(const char *dosya-adı, ios::openmode mode = ios::in | ios::out);`

Burada, dosya-adı ifadesi dosyanın adını göstermektedir. Bu ifade dosyasının yol tanımlamasını da içerebilir. İkinci parametre olan mode değeri dosyanın açılma yöntemini belirler.

CodeBlocks 17.12 sürümünde ios\_base.h başlık dosyasının içinde \_Ios\_Openmode isimli bir numaralandırma yapılmış ve typedef anahtar kelimesi ile openmode adlı bir veri türü tanımlanmıştır. Sonra, \_Ios\_Openmode içinde yer alan her bir değer için openmode veri türünden (numaralandırma) statik sabit bir değer oluşturulmuştur.

Dosya açılışında, open() fonksiyonunun ikinci parametresinde aşağıdaki değerlerden bir veya daha fazlası kullanılmalıdır.

Bildirim

```c++
// ios_base.h içeriğinde

enum _Ios_Openmode { 
   _S_app 		       = 1L << 0,
   _S_ate 		       = 1L << 1,
   _S_bin 		       = 1L << 2,
   _S_in 		       = 1L << 3,
   _S_out 		       = 1L << 4,
   _S_trunc 		   = 1L << 5,
   _S_ios_openmode_end = 1L << 16 
};

typedef _Ios_Openmode openmode;

static const openmode app =	_S_app;
static const openmode ate =	_S_ate;
static const openmode binary = _S_bin;
static const openmode in = _S_in;
static const openmode out =	_S_out;
static const openmode trunc = _S_trunc;	


```

Başlık dosyasında (ios\_base.h) yer alan sabit değerlerin kullanım amaçları aşağıdaki tabloda yer almaktadır:

| Mod | Açıklama |
| --- | --- |
| ios::app | Yazma amacıyla açılan bir dosyaya gönderilen tüm verilerin dosyanın sonuna eklenmesini sağlar.<br>Dosyaya yapılan her yazma işleminde, dosya konum göstergesi dosyanın sonunu gösterecek şekilde ayarlanır. <br> Dosya konum göstergesi farklı bir konuma ayarlanamaz. Daima dosya sonunu gösterir. <br> Tüm yazma işlemleri dosya sonuna eklenir. Dosya başka bir konumuna yazma işlemi yapılamaz. |
| ios::ate | <br> Dosya açılışında, dosya konum göstergesini dosya sonuna ayarlar. <br> Dosya konum göstergesi farklı bir konuma ayarlanabilir. |
| ios::binary | Dosyanın ikili modda açılmasını sağlar. |
| ios::in | Dosyayı veri okuma amacıyla açar. |
| ios::out | Dosyayı veri yazma amacıyla açar. |
| ios::trunc |  Önceden var olan aynı isme sahip bir dosya içeriğinin tamamen silinmesini ve dosya uzunluğunun sıfır değerine getirilmesini sağlar.<br> dosya açılırken ofstream parametresi kullanılırsa, aynı isme sahip bir dosya varsa, otomatik olarak içeriği silinir. |

Bu değerlerden iki veya daha fazlasını OR işlemcisi ile birleştirerek kullanabiliriz.

> Tüm dosyalar ön tanımlı olarak metin modunda açılır. Metin modunda, herhangi bir metin editörü ile oluşturulan DOS metin dosyaları ile kullanılır. Yani, metin modu ASCII karakterlerle birlikte kullanılır. C++ dilinde metin modu, metin dosyalarını satırları tek bir yeni satır karakteri (ASCII 10) ile ayrılmış olarak dikkate alır. Ancak, DOS metin dosyaları, her satırı arasında bir yeni satır (ASCII 10) ve bir satır başı (ASCII 13) karakteri olmak üzere toplam iki karakter ile, diske kaydedilir. C++ dili, metin modunda diskten bir dosya okurken yeni satır ve satır başı karakterlerini tek bir yeni satır karakterine çevirir. Metin akışından diske bir dosyayı kaydederken ise, tek bir yeni satır karakterini, yeni satır ve satır başı karakterlerine çevirir. Bu nedenle, metin akışına gönderilen ifadelerle dosyaya yazılan ifadeler tıpatıp aynı olmayabilir.
{: .prompt-tip }

İkili modda ise, herhangi bir karakter dönüşümü yapılmaz. Yani, ikili modda diske bir dosya kaydederken veya diskten ikili modda bir dosya aktarırken, dosya içinde yer alan karakterlerde herhangi bir değişiklik yapılmaz. Dosyadan okunan ifadelerle dosyaya gönderilen ifadeler tamamen birbirinin aynıdır.

## Dosya kapatma işlemleri

Dosya ile ilgili işlemleri tamamladıktan sonra bir dosyayı kapatmak için close() fonksiyonu kullanılır. Fonksiyonun genel yapısı aşağıdaki şekildedir:

`akış-adı.close();`

Fonksiyon herhangi parametre almaz ve herhangi bir değer geri döndürmez.

Dosya açma işlemlerini ifstream, ofstream ve fstream sınıfları içinde yer alan open() üye fonksiyonları veya doğrudan bu sınıfların constructor fonksiyonları ile yapabiliriz.

## Üye fonksiyonlarla dosya açma işlemleri

Dosya açma işlemini ifstream, ofstream ve fstream sınıfları içinde yer alan open() üye fonksiyonları ile yapabiliriz.

Şimdi, dosya açma ve kapatma işlemlerinin open() fonksiyonu ile yapılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>
#include <fstream>

using namespace std;

int main(void)
{
  ofstream outfile;           // Dosyaya yazma işlemi için akış oluşturma

  outfile.open("deneme.txt"); // Dosya açma (.exe dosyanın bulunduğu dizinde oluşturulur.)

  outfile.close();            // Dosya kapatma

  return 0;
}


```

Program, bir dosyaya yazma işlemi yapmak için, ofstream sınıfı türünden bir nesne oluşturur. Bu nesne yoluyla ostream sınıfı içindeki open() üye fonksiyonu ile deneme.txt adlı bir dosya oluşturur. Open() fonksiyonunun ikinci parametresinin ön tanımlı değeri ios::out \| ios::trunc olduğundan, dosya bu modda açılır. Herhangi bir işlem yapmadan dosyayı kapatır.

Program çalıştırıldığında, .exe dosyanın bulunduğu dizinde deneme.txt adlı bir dosya oluşturulur.

## Constructor fonksiyonlarıyla dosya açma işlemleri

Dosya açma işlemini ifstream, ofstream ve fstream sınıflarının constructor fonksiyonları ile yapabiliriz. Bu sınıfların constructor fonksiyonları open() üye fonksiyonları ile aynı parametreleri alırlar.

Şimdi, dosya açma ve kapatma işlemlerinin constructor fonksiyonları ile yapılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>
#include <fstream>

using namespace std;

int main(void)
{
  ofstream outfile("deneme.txt"); // Dosyaya yazma işlemi için akış oluşturma

  outfile.close();                // Dosya kapatma

  return 0;
}


```

Program, bir dosyaya yazma işlemi yapmak için, ofstream sınıfı türünden bir nesne oluşturur. Bu nesneyi oluştururken, ostream sınıfı içindeki constructor fonksiyonu ile deneme.txt adlı bir dosya oluşturur. Constructor() fonksiyonunun ikinci parametresinin ön tanımlı değeri ios::out \| ios::trunc olduğundan, dosya bu modda açılır. Herhangi bir işlem yapmadan dosyayı kapatır.

## Dosya açma işleminde hata kontrolü

Dosya açma işlemi esnasında herhangi bir hata meydana gelip gelmediğini kontrol etmek için, akış değişkeninin aldığı değeri kontrol edebiliriz. Akış değişkeni, dosya normal bir şekilde açılırsa doğru (true), aksi takdirde yanlış (false) bir değer alır.

Şimdi, constructor fonksiyonları ile yapılan dosya açma işlemlerinin hata konrolü ile yapılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>
#include <fstream>
#include <cstdlib>

using namespace std;

int main(void)
{
  ofstream outfile("deneme.txt");  // Dosyaya yazma işlemi için akış oluşturma

  if(!outfile) {                   // Dosya açma hata kontrolü
     cout << "deneme.txt dosyası açma hatası!";
	 exit(1);
  }

  outfile.close();                 // Dosya kapatma

  ifstream infile("deneme2.txt");  // Dosyadan okuma işlemi için akış oluşturma

  if(!infile) {                    // Dosya açma hata kontrolü
     cout << "deneme2.txt dosya açma hatası!";
     exit(1);
  }  
  
  infile.close();                  // Dosya kapatma (Bu işlem satırı hiç çalışmaz)

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

deneme2.txt dosya açma hatası!

```

Program, bir dosyaya yazma işlemi yapmak için, ofstream sınıfı türünden outfile adlı bir nesne oluşturur. Bu nesneyi oluşturduktan sonra, nesnenin false değeri taşıyıp taşımadığını kontrol eder. Dosya mevcut olduğundan, if koşulu gerçekleşmez ve dosyayı kapatır. Sonra, bir dosyadan okuma işlemi yapmak için, ifstream sınıfı türünden infile adlı bir nesne oluşturur. Bu nesneyi oluşturduktan sonra, nesnenin false değeri taşıyıp taşımadığını kontrol eder. Dosya mevcut olmadığından, if koşulu gerçekleşir ve koşul içindeki karakter dizisi ekrana yazılır ve programdan çıkış yapılır.

Dosya açma işlemi esnasında herhangi bir hata meydana gelip gelmediğini, fstream, ifstream ve ofstream sınıflarının üyesi olan ve aşağıda genel yapısı verilen is\_open() fonksiyonu ile de yapabiliriz:

`bool is_open();`

Oluşturulan akış nesnesi bir dosyaya bağlandığında doğru (true) aksi takdirde yanlış (false) bir değer geri döndürür.

Şimdi, dosya açma işlemlerinde is\_open() fonksiyonu ile hata konrolü yapılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>
#include <fstream>
#include <cstdlib>

using namespace std;

int main(void)
{
  ofstream outfile("deneme.txt");  // Dosyaya yazma işlemi için akış oluşturma

  // Dosya açma hata kontrolü
  if(outfile.is_open()) {
     cout << "deneme.txt dosyası başarıyla açıldı!" << endl;
  }
  else {
     cout << "deneme.txt dosya açma hatası!" << endl;
     exit(1);
  }

  outfile.close();                // Dosya kapatma

  ifstream infile("deneme2.txt"); // Dosyadan okuma işlemi için akış oluşturma

  // Dosya açma hata kontrolü
  if(infile.is_open()) {
     cout << "deneme2.txt dosyası başarıyla açıldı!" << endl;
  }
  else {
     cout << "deneme2.txt dosya açma hatası!" << endl;
     exit(1);
  }

  infile.close();                 // Dosya kapatma (Bu işlem satırı hiç çalışmaz)

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

deneme.txt dosyası başarıyla açıldı!
deneme2.txt dosya açma hatası!

```

Program, bir dosyaya yazma işlemi yapmak için, ofstream sınıfı türünden outfile adlı bir nesne oluşturur. Bu nesneyi oluşturduktan sonra, is\_open() fonksiyonu ile dosyanın başarıyla açılıp açılmadığını kontrol eder. Dosya mevcut olduğundan, if koşulu gerçekleşir ve karakter dizisini ekrana yazıp dosyayı kapatır. Sonra, bir dosyadan okuma işlemi yapmak için, ifstream sınıfı türünden infile adlı bir nesne oluşturur. Bu nesneyi oluşturduktan sonra, is\_open() fonksiyonu ile dosyanın başarıyla açılıp açılmadığını kontrol eder. Dosya mevcut olmadığından, if koşulu gerçekleşmez ve else kod bloğu içindeki karakter dizisini ekrana yazar ve exit() fonksiyonu ile program sona erer.

## Dosyaya yazma ve dosyadan okuma işlemleri

Bir metin dosyasına yazma ve okuma işlemleri, ekrana veri gönderirken ve klavyeden veri okurken kullandığımız, `<<` ve `>>`işlemcileri ile yapılır. Dosya işlemlerinde fstream, ifstream ve ofstream sınıflarından tanımlanan akış nesneleri bu işlemcilerle birlikte kullanılır.

## Dosyaya yazma işlemleri

Bir dosyaya veri yollamak için, önce ofstream sınıfından bir akış nesnesi tanımlayarak dosyayı açmak ve bu işlem esnasında constructor fonksiyonu yoluyla dosya adını belirtmek gerekir. Dosyaya yazma işlemi `<<` işlemcisi ile yapıldıktan sonra dosya kapatılır.

Şimdi, bir dosyaya yazma işlemi yapılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>
#include <fstream>
#include <cstdlib>

using namespace std;

int main(void)
{
  ofstream outfile("deneme.txt");  // Dosyaya yazma işlemi için akış oluşturma

  // Dosya açma hata kontrolü
  if(!outfile) {
     cout << "deneme.txt dosya açma hatası!" << endl;
     exit(1);
  }

  outfile << "Bilgisayar" << endl;
  outfile << 127 << endl;
  outfile << 54.789 << endl;

  outfile.close();                // Dosya kapatma

  return 0;
}


```

Program, bir dosyaya yazma işlemi yapmak için, dosya adını constructor fonksiyonuna geçirerek, ofstream sınıfı türünden outfile adlı bir akış nesnesi oluşturur. Nesneyi kontrol ederek dosya açma işleminin başarılı olup olmadığını kontrol eder. Dosya mevcut olduğundan, if koşulu gerçekleşmez ve program çalışmasına devam eder. Sonra, akış nesnesi ile `<<` işlemcisini kullanarak bir karakter dizisi, bir int ve bir float değeri dosyaya yazar. Yazma işlemi sona erdikten sonra, close() fonksiyonu ile dosyayı kapatır.

Programın çalışması sona erdikten sonra, bir metin editöründe açtığınızda dosya içeriği aşağıdaki şekilde olacaktır.

```

Bilgisayar
127
54.789

```

Programın çalışması sona erdikten sonra, bir hex editörde açtığınızda dosya içeriği aşağıdaki şekilde olacaktır.

![](cprog/dosya01.png)

Her satır arasında bir satır başı 0x0D (ASCII 13) ve bir yeni satır 0x0A (ASCII 10) karakteri yer alır.

## Dosyadan okuma işlemleri

Bir dosyadan veri okumak için, önce ifstream sınıfından bir akış nesnesi tanımlayarak dosyayı açmak ve bu işlem esnasında constructor fonksiyonu yoluyla dosya adını belirtmek gerekir. Dosyadan okuma işlemi >> işlemcisi ile yapıldıktan sonra dosya kapatılır.

\>> işlemcisi ile dosyadan veri okuma işlemi yapılırken boşluk karakteri (32 - 0x20) ile karşılaşıldığında, okuma işlemi sona erer.

Şimdi, dosya ile ilgili yazma ve okuma işlemlerinin yapılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>
#include <fstream>
#include <cstdlib>

using namespace std;

int main(void)
{
  ofstream outfile("deneme.txt");  // Dosyaya yazma işlemi için akış oluşturma

  // Dosya açma hata kontrolü
  if(!outfile) {
     cout << "Yazma amaçlı dosya açma hatası!" << endl;
     exit(1);
  }

  outfile << "Bilgisayar" << endl;
  outfile << 127 << endl;
  outfile << 54.789 << endl;

  outfile.close();                // Dosya kapatma

  ifstream infile("deneme.txt");  // Dosyaya yazma işlemi için akış oluşturma
  char cdizi[25];
  int id;
  float fd;

  // Dosya açma hata kontrolü
  if(!infile) {
     cout << "Okuma amaçlı dosya açma hatası!" << endl;
     exit(1);
  }

  infile >> cdizi;
  infile >> id;
  infile >> fd;

  cout << cdizi << endl << id << endl << fd;

  infile.close();                // Dosya kapatma

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Bilgisayar
127
54.789

```

Program, bir dosyaya yazma işlemi yapmak için, dosya adını constructor fonksiyonuna geçirerek, ofstream sınıfı türünden outfile adlı bir akış nesnesi oluşturur. Nesneyi kontrol ederek dosya açma işleminin başarılı olup olmadığını kontrol eder. Dosya mevcut olduğundan, if koşulu gerçekleşmez ve program çalışmasına devam eder. Sonra, akış nesnesi ile `<<` işaretçisini kullanarak bir karakter dizisi, bir int ve bir float değeri dosyaya yazar. Yazma işlemi sona erdikten sonra, close() fonksiyonu ile dosyayı kapatır.

> Program, bir dosyadan okuma işlemi yapmak için, dosya adını constructor fonksiyonuna geçirerek, ifstream sınıfı türünden infile adlı bir akış nesnesi oluşturur. Ayrıca, dosyadan okuyacağı değerleri atamak için bir karakter dizisi, bir int ve bir float değer oluşturur. Nesneyi kontrol ederek dosya açma işleminin başarılı olup olmadığını kontrol eder. Dosya mevcut olduğundan, if koşulu gerçekleşmez ve program çalışmasına devam eder. Sonra, akış nesnesi ile >> işlemcisini kullanarak bir karakter dizisi, bir int ve bir float değeri dosyadan okur ve daha önce oluşturduğu dizi ve değişkenlere atar. Okuduğu değerleri ekrana yazdıktan sonra, close() fonksiyonu ile dosyayı kapatır.
{: .prompt-tip }

Dosya içinde her satır arasında yer alan bir satır başı 0x0D (ASCII 13) ve bir yeni satır 0x0A (ASCII 10) karakteri, >> işlemcisi ile yapılan okuma esnasında dikkate alınmamaktadır.

## İkili sistem dosya giriş ve çıkış işlemleri

Metin dosyalarının yanı sıra, verileri ikili sistem olarak ta oluşturabiliriz. Bir dosyayı ikili sistem işlemler yapmak üzere açmak istediğimizde, ios::binary parametre değerini kullanmamız gerekir.

## İkili sistem dosyalarına tek karakter yazma ve okuma

Bir dosya ile ilgili yazma ve okuma işlemlerini tek bir karakter ile yapmak istediğimizde, ostream sınıfı içindeki put() fonksiyonunu ve istream sınıfı içindeki get() fonksiyonunu kullanabiliriz. Her iki fonksiyonun genel yapıları aşağıda gösterilmektedir:

```c++
ostream& put(char ch);

int get();

istream& get(char &ch);

istream& get(char *ptr, streamsize n);

istream& get(char *ptr, streamsize n, char delim);

istream& get(streambuf &sbuf);

istream& get(streambuf &sbuf, char delim);
```

ch: Akıştan okunacak karakterin atanacağı değişkeni gösterir.

ptr: Akıştan okunacak karakterlerin atanacağı bellek adresini gösterir.

n: En sonda yer alan NULL bir karakter de dahil olmak üzere, ptr ile gösterilen bellek adresine yazılacak olan azami karakter sayısını gösterir.

delim: Okuma işleminin sona ereceği karakterdir.

sbuf: Bir streambuf nesnesidir.

İlk başta yer alan get() fonksiyonu akıştan bir sonraki karakteri geri döndürür. Eğer dosya sonuna gelinmiş ise, EOF değerini geri döndürür.

İkinci sırada yer alan get() fonksiyonu, n-1 kadar karakter okunana, bir yeni satır karakteri veya dosya sonu karakteri ile karşılaşılana kadar, dosyadan okunan değerleri ptr ile gösterilen belleğe atar. Ptr ile gösterilen bellek adresi sonuna otomatik olarak NULL bir karakter eklenir. Giriş akışında yeni satır karakteriyle karşılaşılırsa, bu karaktere işlem yapılmaz.

Üçüncü sırada yer alan get() fonksiyonu, n-1 kadar karakter okunana, dosya sonu karakteri veya delim parametresi ile gösterilen karakterle karşılaşılana kadar, dosyadan okunan değerleri ptr ile gösterilen belleğe atar. Ptr ile gösterilen bellek adresi sonuna otomatik olarak NULL bir karakter eklenir. Giriş akışında delim parametresinde gösterilen karakterle karşılaşılırsa, bu karaktere işlem yapılmaz.

Görüldüğü gibi, put() fonksiyonunun tek bir kullanım şekli olmasına rağmen, get() fonksiyonunun karakter, karakter dizisi ve akış tamponları ile kullanılan farklı kullanım şekilleri vardır. Şimdilik, get() fonksiyonun sadece tek karakter okuma amaçlı olarak kullanacağız.

Şimdi, dosya ile ilgili yazma ve okuma işlemlerinin karakter bazında yapılmasında put() ve get() fonksiyonlarının kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>
#include <fstream>
#include <cstdlib>

using namespace std;

int main(void)
{
  ofstream outfile("deneme.txt", ios::out | ios::binary); // Dosyaya yazma işlemi için akış oluşturma
  char cd;

  // Dosya açma hata kontrolü
  if(!outfile) {
     cout << "Yazma amaçlı dosya açma hatası!" << endl;
     exit(1);
  }

  for(cd='A'; cd<='Z'; cd++) outfile.put(cd);

  outfile.close(); // Dosya kapatma

  ifstream infile("deneme.txt", ios::in | ios::binary); // Dosyaya yazma işlemi için akış oluşturma

  // Dosya açma hata kontrolü
  if(!infile) {
     cout << "Okuma amaçlı dosya açma hatası!" << endl;
     exit(1);
  }

  while(infile.get(cd)) { // Dosya sonuna erişildiğinde hata verir.
    cout << cd;
  }

  infile.close(); // Dosya kapatma

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

ABCDEFGHIJKLMNOPQRSTUVWXYZ

```

Program, bir ikili sistem dosyasına yazma işlemi yapmak için, dosya adını constructor fonksiyonuna geçirerek, ofstream sınıfı türünden outfile adlı bir akış nesnesi oluşturur. Nesneyi kontrol ederek dosya açma işleminin başarılı olup olmadığını kontrol eder. Dosya mevcut olduğundan, if koşulu gerçekleşmez ve program çalışmasına devam eder. Sonra, put() fonksiyonunu bir for döngüsü içinde kullanarak, A-Z arasındaki karakterleri dosyaya yazar. Yazma işlemi sona erdikten sonra, close() fonksiyonu ile dosyayı kapatır.

Program, bir ikili sistem dosyasından okuma işlemi yapmak için, dosya adını constructor fonksiyonuna geçirerek, ifstream sınıfı türünden infile adlı bir akış nesnesi oluşturur. Nesneyi kontrol ederek dosya açma işleminin başarılı olup olmadığını kontrol eder. Dosya mevcut olduğundan, if koşulu gerçekleşmez ve program çalışmasına devam eder. Sonra, get() fonksiyonunu bir while döngüsü içinde kullanarak, dosyadaki karakterleri sıra ile okuyarak ekrana yazar. Sonra, close() fonksiyonu ile dosyayı kapatır.

## İkili sistem dosyalarına çoklu karakter yazma ve okuma

C++'da, birden fazla byte değerinden oluşan dizi, yapı ve sınıf gibi blok halindeki verileri bir dosyaya yazmak ve okumak için, ostream sınıfı içindeki write() fonksiyonunu ve istream sınıfı içindeki read() fonksiyonunu kullanabiliriz. Her iki fonksiyonun genel yapıları aşağıda gösterilmektedir: 

ostream& write(const char \*ptr, streamsize num);

istream& read(char \*ptr, streamsize num);

ptr: Dosyadan okunan/yazılan verilerin yüklendiği tampon belleği gösterir.

num: Dosyadan okunan/yazılan verilerin boyutunu gösterir.

Write() fonksiyonu, num parametre değeri kadar karakteri ptr ile gösterilen bellek adresinden dosyaya (akışa) yazar. Read() fonksiyonu, dosyadan (akıştan) okuduğu num parametre değeri kadar karakteri ptr ile gösterilen bellek adresine yazar. Streamsize int veri türünden tanımlanmış bir veridir.

Şimdi, bir dosyaya dizi değerinin ile ilgili yazma ve okuma işlemlerinde, write() ve read() fonksiyonlarının kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>
#include <fstream>
#include <cstdlib>

using namespace std;

class personel {
  private:
    string adi;
    string soyadi;
    int yasi;

  public:
    personel(string padi, string psoyadi, int pyasi)
    {
      adi = padi;
      soyadi = psoyadi;
      yasi = pyasi;
    }
    void deger_ata(string padi, string psoyadi, int pyasi)
    {
      adi = padi;
      soyadi = psoyadi;
      yasi = pyasi;
    }
    void deger_goster(void)
    {
      cout << adi << " " << soyadi << " " << yasi << endl;
    }
};

int main(void)
{
  ofstream outfile("deneme.txt"); // Dosyaya yazma işlemi için akış oluşturma

  // Dosya açma hata kontrolü
  if(!outfile) {
     cout << "Yazma amaçlı dosya açma hatası!" << endl;
     exit(1);
  }

  // 4 adet nesne değerini dosyaya yazma
  personel per("Ahmet", "Sakin", 21);            // Nesne oluşturma
  outfile.write((const char*)&per, sizeof(per)); // Nesneyi dosyaya yazma
  per.deger_ata("Ayşe", "Saygılı", 35);          // Nesne değerlerini değiştirme
  outfile.write((const char*)&per, sizeof(per)); // Nesneyi dosyaya yazma
  per.deger_ata("Mehmet", "Efendi", 42);         // Nesne değerlerini değiştirme
  outfile.write((const char*)&per, sizeof(per)); // Nesneyi dosyaya yazma
  per.deger_ata("Fatma", "Kalender", 56);        // Nesne değerlerini değiştirme
  outfile.write((const char*)&per, sizeof(per)); // Nesneyi dosyaya yazma

  outfile.close(); // Dosya kapatma

  ifstream infile("deneme.txt"); // Dosyadan okuma işlemi için akış oluşturma

  // Dosya açma hata kontrolü
  if(!infile) {
     cout << "Okuma amaçlı dosya açma hatası!" << endl;
     exit(1);
  }

  // Dosyada kayıtlı nesne değerlerini sıra ile okuma
  while(infile.read((char*)&per, sizeof(per))) { // Dosya sonuna erişildiğinde hata verir.
    per.deger_goster();
  }

  infile.close(); // Dosya kapatma

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Ahmet Sakin 21
Ayşe Saygılı 35
Mehmet Efendi 42
Fatma Kalender 56

```

Program, önce personel adında bir sınıf bildirimi yapar. Bu sınıf içinde, adi ve soyadi adlı iki adet string ve yasi adlı bir adet int değişkenin private olarak bildirimini yapar. Ayrıca, değişkenlere değer atayan bir constructor() fonksiyonu ve deger\_ata() adlı bir fonksiyon ile değişken değerlerini ekranda gösteren deger\_goster() adlı bir fonksiyon tanımlar.

Bir ikili sistem dosyasına yazma işlemi yapmak için, dosya adını constructor fonksiyonuna geçirerek, ofstream sınıfı türünden outfile adlı bir akış nesnesi oluşturur. Nesneyi kontrol ederek dosya açma işleminin başarılı olup olmadığını kontrol eder. Dosya mevcut olduğundan, if koşulu gerçekleşmez ve program çalışmasına devam eder. Sonra, constructor fonksiyonunu kullanarak, personel sınıfından bir nesne oluşturur. Nesneye atanan değerleri dosyaya yazmak için write() fonksiyonunu kullanır. Nesne içindeki değişken değerlerini deger\_ata() fonksiyonu ile değiştirdikten sonra, nesne değerlerini tekrar dosyaya yazar. Bu işlemi üç defa tekrarlar. Yazma işlemi sona erdikten sonra, close() fonksiyonu ile dosyayı kapatır.

Program, bir ikili sistem dosyasından okuma işlemi yapmak için, dosya adını constructor fonksiyonuna geçirerek, ifstream sınıfı türünden infile adlı bir akış nesnesi oluşturur. Nesneyi kontrol ederek dosya açma işleminin başarılı olup olmadığını kontrol eder. Dosya mevcut olduğundan, if koşulu gerçekleşmez ve program çalışmasına devam eder. Sonra, read() fonksiyonunu bir while döngüsü içinde kullanarak, dosyadaki nesne değerlerini sıra ile okuyarak ekrana yazar. Sonra, close() fonksiyonu ile dosyayı kapatır.

## Dosyadan okunan karakter sayısını alma

C++'da, bir akış üzerinden dosyadan okunan karakter sayısını almak için gcount() fonksiyonunu kullanabiliriz. Fonksiyonun genel yapısı aşağıda gösterilmektedir: 

streamsize gcount();

Bu fonksiyon, son dosyadan okuma işleminde okunan karakter sayısını geri döndürür.

Şimdi, gcount() fonksiyonunun kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>
#include <fstream>
#include <cstdlib>

using namespace std;

class personel {
  private:
    string adi;
    string soyadi;
    int yasi;

  public:
    personel(string padi, string psoyadi, int pyasi)
    {
      adi = padi;
      soyadi = psoyadi;
      yasi = pyasi;
    }
    void deger_ata(string padi, string psoyadi, int pyasi)
    {
      adi = padi;
      soyadi = psoyadi;
      yasi = pyasi;
    }
    void deger_goster(void)
    {
      cout << adi << " " << soyadi << " " << yasi << endl;
    }
};

int main(void)
{
  ofstream outfile("deneme.txt"); // Dosyaya yazma işlemi için akış oluşturma

  // Dosya açma hata kontrolü
  if(!outfile) {
     cout << "Yazma amaçlı dosya açma hatası!" << endl;
     exit(1);
  }

  // 4 adet nesne değerini dosyaya yazma
  personel per("Ahmet", "Sakin", 21);            // Nesne oluşturma
  outfile.write((const char*)&per, sizeof(per)); // Nesneyi dosyaya yazma
  per.deger_ata("Ayşe", "Saygılı", 35);          // Nesne değerlerini değiştirme
  outfile.write((const char*)&per, sizeof(per)); // Nesneyi dosyaya yazma
  per.deger_ata("Mehmet", "Efendi", 42);         // Nesne değerlerini değiştirme
  outfile.write((const char*)&per, sizeof(per)); // Nesneyi dosyaya yazma
  per.deger_ata("Fatma", "Kalender", 56);        // Nesne değerlerini değiştirme
  outfile.write((const char*)&per, sizeof(per)); // Nesneyi dosyaya yazma

  outfile.close(); // Dosya kapatma

  ifstream infile("deneme.txt"); // Dosyadan okuma işlemi için akış oluşturma

  // Dosya açma hata kontrolü
  if(!infile) {
     cout << "Okuma amaçlı dosya açma hatası!" << endl;
     exit(1);
  }

  // Dosyada kayıtlı nesne değerlerini sıra ile okuma
  while(infile.read((char*)&per, sizeof(per))) { // Dosya sonuna erişildiğinde hata verir.
    cout << "Okunan karakter sayısı: " << infile.gcount() << " ";
	per.deger_goster();
  }

  infile.close(); // Dosya kapatma

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Okunan karakter sayısı: 52 Ahmet Sakin 21
Okunan karakter sayısı: 52 Ayşe Saygılı 35
Okunan karakter sayısı: 52 Mehmet Efendi 42
Okunan karakter sayısı: 52 Fatma Kalender 56

```

Program, önce personel adında bir sınıf bildirimi yapar. Bu sınıf içinde, adi ve soyadi adlı iki adet string ve yasi adlı bir adet int değişkenin private olarak bildirimini yapar. Ayrıca, değişkenlere değer atayan bir constructor() fonksiyonu ve deger\_ata() adlı bir fonksiyon ile değişken değerlerini ekranda gösteren deger\_goster() adlı bir fonksiyon tanımlar.

Bir ikili sistem dosyasına yazma işlemi yapmak için, dosya adını constructor fonksiyonuna geçirerek, ofstream sınıfı türünden outfile adlı bir akış nesnesi oluşturur. Nesneyi kontrol ederek dosya açma işleminin başarılı olup olmadığını kontrol eder. Dosya mevcut olduğundan, if koşulu gerçekleşmez ve program çalışmasına devam eder. Sonra, constructor fonksiyonunu kullanarak, personel sınıfından bir nesne oluşturur. Nesneye atanan değerleri dosyaya yazmak için write() fonksiyonunu kullanır. Nesne içindeki değişken değerlerini deger\_ata() fonksiyonu ile değiştirdikten sonra, nesne değerlerini tekrar dosyaya yazar. Bu işlemi üç defa tekrarlar. Yazma işlemi sona erdikten sonra, close() fonksiyonu ile dosyayı kapatır.

Program, bir ikili sistem dosyasından okuma işlemi yapmak için, dosya adını constructor fonksiyonuna geçirerek, ifstream sınıfı türünden infile adlı bir akış nesnesi oluşturur. Nesneyi kontrol ederek dosya açma işleminin başarılı olup olmadığını kontrol eder. Dosya mevcut olduğundan, if koşulu gerçekleşmez ve program çalışmasına devam eder. Sonra, read() fonksiyonunu bir while döngüsü içinde kullanarak, önce gcount() fonksiyonu ile okunan karakter sayısını, sonra dosyadaki nesne değerlerini ekrana yazar. Sonra, close() fonksiyonu ile dosyayı kapatır.

## getline() fonksiyonu

C++'da, bir dosyadaki verileri satır satır okumak için getline() fonksiyonunu kullanabiliriz. Fonksiyonun genel yapısı aşağıda gösterilmektedir:

std::getline (string)

istream& getline(istream &is, string &str);

istream& getline(istream &is, string &str, char delim);

is: Okuma yapılacak akışı gösterir.

str: Dosyadan okunan verilerin kaydedileceği string değişkenini gösterir.

delim: Okuma işleminin sona ereceği karakterdir.

std::istream::getline

istream& getline(char \*ptr, streamsize num);

istream& getline(char \*ptr, streamsize num, char delim);

ptr: Dosyadan okunan verilerin yüklendiği tampon belleği gösterir.

num: Dosyadan okunan verilerin boyutunu gösterir.

delim: Okuma işleminin sona ereceği karakterdir.

İlk sırada yer alan getline() fonksiyonu, n-1 kadar karakter okunana, bir yeni satır karakteri veya dosya sonu karakteri ile karşılaşılana kadar, dosyadan okunan değerleri ptr ile gösterilen belleğe atar. Ptr ile gösterilen bellek adresi sonuna otomatik olarak NULL bir karakter eklenir. Giriş akışında yeni satır karakteriyle karşılaşılırsa, dosyadan alınır fakat ptr içine aktarılmaz.

İkinci sırada yer alan getline() fonksiyonu, n-1 kadar karakter okunana, dosya sonu karakteri veya delim parametresi ile gösterilen karakterle karşılaşılana kadar, dosyadan okunan değerleri ptr ile gösterilen belleğe atar. Ptr ile gösterilen bellek adresi sonuna otomatik olarak NULL bir karakter eklenir. Giriş akışında delim parametresinde gösterilen karakterle karşılaşılırsa, dosyadan alınır fakat ptr içine aktarılmaz.

Getline() fonksiyonu, get() fonksiyonunun bazı kullanım şekilleri ile benzer işlemleri gerçekleştirmektedir. Ancak, getline() fonksiyonu okuma işlemini sona erdiren ve delim parametresi ile gösterilen değeri akıştan okuyup silerken, get() fonksiyonu bu işlemi yapmaz.

Şimdi, getline() fonksiyonunun kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>
#include <fstream>
#include <cstdlib>

using namespace std;

int main(void)
{
  ofstream outfile("deneme.txt");  // Dosyaya yazma işlemi için akış oluşturma

  // Dosya açma hata kontrolü
  if(!outfile) {
     cout << "Yazma amaçlı dosya açma hatası!" << endl;
     exit(1);
  }

  outfile << "Bilgisayar programlama" << " " << 275 << " " << 62.951 << endl;
  outfile << "C++ Programlama Dili" << " " << 351 << " " << 121.315 << endl;
  outfile << "Dosyadan veri okuma" << " " << 487 << " " << 542.249 << endl;
  outfile << "getline() fonksiyonu kullanımı" << " " << 592 << " " << 1024.514 << endl;

  outfile.close();                // Dosya kapatma

  ifstream infile("deneme.txt");  // Dosyaya yazma işlemi için akış oluşturma

  // Dosya açma hata kontrolü
  if(!infile) {
     cout << "Okuma amaçlı dosya açma hatası!" << endl;
     exit(1);
  }

  char cdizi[100];

  while (infile.getline(cdizi, 100)) {
    cout << cdizi << endl;
  }

  infile.close();                // Dosya kapatma

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Bilgisayar programlama 275 62.951
C++ Programlama Dili 351 121.315
Dosyadan veri okuma 487 542.249
getline() fonksiyonu kullanımı 592 1024.51

```

Program, bir dosyaya yazma işlemi yapmak için, dosya adını constructor fonksiyonuna geçirerek, ofstream sınıfı türünden outfile adlı bir akış nesnesi oluşturur. Nesneyi kontrol ederek dosya açma işleminin başarılı olup olmadığını kontrol eder. Dosya mevcut olduğundan, if koşulu gerçekleşmez ve program çalışmasına devam eder. Sonra, akış nesnesi ile << işaretçisini kullanarak, dört defa olmak üzere, bir karakter dizisi, bir int ve bir float değeri dosyaya yazar. Yazma işlemi sona erdikten sonra, close() fonksiyonu ile dosyayı kapatır.

Program, bir dosyadan okuma işlemi yapmak için, dosya adını constructor fonksiyonuna geçirerek, ifstream sınıfı türünden infile adlı bir akış nesnesi oluşturur. Ayrıca, dosyadan okuyacağı değerleri atamak için bir karakter dizisi, bir int ve bir float değer oluşturur. Nesneyi kontrol ederek dosya açma işleminin başarılı olup olmadığını kontrol eder. Dosya mevcut olduğundan, if koşulu gerçekleşmez ve program çalışmasına devam eder. Sonra, akış nesnesi ile getline() fonksiyonunu bir while döngüsü içinde kullanarak, dosyadan satır satır okuduğu bilgileri ekrana yazar ve close() fonksiyonu ile dosyayı kapatır.

Dosyadan getline() fonksiyonu ile okuma işlemi yapıldığında, boşluk karakteri okuma işleminin sona ermesine neden olmaz.

## Dosya sonuna erişimi tespit etme

C++'da, dosya ile ilgili işlemler yaparken, get(), read() ve getline() gibi istream sınıfından veri geri döndüren fonksiyonlar dosya sonuna geldiklerinde, yanlış bir değer geri döndürdüklerinden, dosya sonuna erişilip erişilmediğini belirlemek için kullanılabilirler.

Sadece bu amaç için oluşturulmuş olan ve aşağıda genel yapısı verilen eof() fonksiyonunu kullanabiliriz:

bool eof();

Dosya sonuna erişildiğinde doğru (true) bir değer, aksi takdirde yanlış (false) bir değer geri döndürür.

Şimdi, eof() fonksiyonunun kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>
#include <fstream>
#include <cstdlib>

using namespace std;

int main(void)
{
  ofstream outfile("deneme.txt");  // Dosyaya yazma işlemi için akış oluşturma

  // Dosya açma hata kontrolü
  if(!outfile) {
     cout << "Yazma amaçlı dosya açma hatası!" << endl;
     exit(1);
  }

  outfile << "Bilgisayar programlama" << " " << 275 << " " << 62.951 << endl;
  outfile << "C++ Programlama Dili" << " " << 351 << " " << 121.315 << endl;
  outfile << "Dosyadan veri okuma" << " " << 487 << " " << 542.249 << endl;
  outfile << "getline() fonksiyonu kullanımı" << " " << 592 << " " << 1024.514 << endl;

  outfile.close();                // Dosya kapatma

  ifstream infile("deneme.txt");  // Dosyaya yazma işlemi için akış oluşturma

  // Dosya açma hata kontrolü
  if(!infile) {
     cout << "Okuma amaçlı dosya açma hatası!" << endl;
     exit(1);
  }

  char cdizi[100];

  while (!infile.eof()) { // Dosya sonuna geldiğinde doğru (true) bir değer döndürür.
    infile.getline(cdizi, 100);
    cout << cdizi << endl;
  }

  infile.close();                // Dosya kapatma

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Bilgisayar programlama 275 62.951
C++ Programlama Dili 351 121.315
Dosyadan veri okuma 487 542.249
getline() fonksiyonu kullanımı 592 1024.51

```

Program, bir dosyaya yazma işlemi yapmak için, dosya adını constructor fonksiyonuna geçirerek, ofstream sınıfı türünden outfile adlı bir akış nesnesi oluşturur. Nesneyi kontrol ederek dosya açma işleminin başarılı olup olmadığını kontrol eder. Dosya mevcut olduğundan, if koşulu gerçekleşmez ve program çalışmasına devam eder. Sonra, akış nesnesi ile << işaretçisini kullanarak, dört defa olmak üzere, bir karakter dizisi, bir int ve bir float değeri dosyaya yazar. Yazma işlemi sona erdikten sonra, close() fonksiyonu ile dosyayı kapatır.

Program, bir dosyadan okuma işlemi yapmak için, dosya adını constructor fonksiyonuna geçirerek, ifstream sınıfı türünden infile adlı bir akış nesnesi oluşturur. Ayrıca, dosyadan okuyacağı değerleri atamak için bir karakter dizisi, bir int ve bir float değer oluşturur. Nesneyi kontrol ederek dosya açma işleminin başarılı olup olmadığını kontrol eder. Dosya mevcut olduğundan, if koşulu gerçekleşmez ve program çalışmasına devam eder. Sonra, akış nesnesi ile getline() fonksiyonunu bir while döngüsü içinde kullanarak ve dosya sonu kontrolünü eof() fonksiyonu ile yaparak, dosyadan satır satır okuduğu bilgileri ekrana yazar ve close() fonksiyonu ile dosyayı kapatır.

## Dosyadan okunan karakterlerin bir kısmının devre dışı bırakılması

C++'da, bir akıştan okuduğumuz verileri devre dışı bırakmak için, aşağıda genel yapısı verilen ignore() fonksiyonunu kullanabiliriz:

istream ignore(streamsize num=1, int\_type delim=EOF);

Fonksiyon, num parametre değeri kadar karakter veya delim parametresi ile gösterilen karakterle karşılaşılana kadar, akıştan karakterleri okur ve değerlendirmeden devre dışı bırakır.

Şimdi, ignore() fonksiyonunun kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>
#include <fstream>
#include <cstdlib>

using namespace std;

int main(void)
{
  ofstream outfile("deneme.txt");  // Dosyaya yazma işlemi için akış oluşturma

  // Dosya açma hata kontrolü
  if(!outfile) {
     cout << "Yazma amaçlı dosya açma hatası!" << endl;
     exit(1);
  }

  outfile << "Bilgisayar programlama" << " " << 275 << " " << 62.951 << endl;
  outfile << "C++ Programlama Dili" << " " << 351 << " " << 121.315 << endl;
  outfile << "Dosyadan veri okuma" << " " << 487 << " " << 542.249 << endl;
  outfile << "getline() fonksiyonu kullanımı" << " " << 592 << " " << 1024.514 << endl;

  outfile.close();                // Dosya kapatma

  ifstream infile("deneme.txt");  // Dosyaya yazma işlemi için akış oluşturma

  // Dosya açma hata kontrolü
  if(!infile) {
     cout << "Okuma amaçlı dosya açma hatası!" << endl;
     exit(1);
  }

  char cdizi[100];

  while (!infile.eof()) { // Dosya sonuna geldiğinde doğru (true) bir değer döndürür.
    infile.ignore(15, 'a');
    infile.getline(cdizi, 100);
    cout << cdizi << endl;
  }
  
  infile.close();                // Dosya kapatma

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

yar programlama 275 62.951
mlama Dili 351 121.315
dan veri okuma 487 542.249
iyonu kullanımı 592 1024.51

```

Program, bir dosyaya yazma işlemi yapmak için, dosya adını constructor fonksiyonuna geçirerek, ofstream sınıfı türünden outfile adlı bir akış nesnesi oluşturur. Nesneyi kontrol ederek dosya açma işleminin başarılı olup olmadığını kontrol eder. Dosya mevcut olduğundan, if koşulu gerçekleşmez ve program çalışmasına devam eder. Sonra, akış nesnesi ile << işaretçisini kullanarak, dört defa olmak üzere, bir karakter dizisi, bir int ve bir float değeri dosyaya yazar. Yazma işlemi sona erdikten sonra, close() fonksiyonu ile dosyayı kapatır.

Program, bir dosyadan okuma işlemi yapmak için, dosya adını constructor fonksiyonuna geçirerek, ifstream sınıfı türünden infile adlı bir akış nesnesi oluşturur. Ayrıca, dosyadan okuyacağı değerleri atamak için bir karakter dizisi, bir int ve bir float değer oluşturur. Nesneyi kontrol ederek dosya açma işleminin başarılı olup olmadığını kontrol eder. Dosya mevcut olduğundan, if koşulu gerçekleşmez ve program çalışmasına devam eder. Sonra, akış nesnesi ile getline() fonksiyonunu bir while döngüsü içinde kullanarak ve dosya sonu kontrolünü eof() fonksiyonu ile yaparak, dosyadan satır satır okuduğu bilgileri ekrana yazar. Ancak, getline() fonksiyonunu her çağrılmasından önce ignore() fonksiyonunu en fazla 15 karakter okumak üzere veya 'a' karakteri ile karşılaşılana akıştan karakter okumak üzere çağırır. Böylece her satırın bir kısmı okunur ve devre dışı bırakılır. İlk üç satırda 'a' karakteri ile karşılaşılana, dördüncü satırda ise 15 karakter okuyana kadar satır karakterleri okunur. Daha sonra, close() fonksiyonu ile dosyayı kapatır.

## Giriş akışından dosya aktif konumunu değiştirmeden bir karakter okuma

C++'da, bir akıştan bir karakteri silmeden ve dosya aktif konumunu değiştirmeden okumak için, aşağıda genel yapısı verilen peek() fonksiyonunu kullanabiliriz:

int\_type peek();

Fonksiyon, akışta bulunan bir sonraki karakteri silmeden okur. Karakter okunduktan sonra, akış konumu bir sonraki konuma ilerlemez. Akıştan okuduğu karakteri veya dosya sonuna erişilmiş ise, EOF değerini geri döndürür.

Şimdi, peek() fonksiyonunun kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>
#include <fstream>
#include <cstdlib>

using namespace std;

int main(void)
{
  ofstream outfile("deneme.txt");  // Dosyaya yazma işlemi için akış oluşturma

  // Dosya açma hata kontrolü
  if(!outfile) {
     cout << "Yazma amaçlı dosya açma hatası!" << endl;
     exit(1);
  }

  outfile << "peek() fonksiyonunun kullanımı";

  outfile.close();                // Dosya kapatma

  ifstream infile("deneme.txt");  // Dosyaya yazma işlemi için akış oluşturma

  // Dosya açma hata kontrolü
  if(!infile) {
     cout << "Okuma amaçlı dosya açma hatası!" << endl;
     exit(1);
  }

  int id = infile.peek();
  cout << (char) id << endl;

  char cdizi[100];
  infile.getline(cdizi, 100);
  cout << cdizi << endl;

  infile.close();                // Dosya kapatma

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

p
peek() fonksiyonunun kullanımı

```

Program, bir dosyaya yazma işlemi yapmak için, dosya adını constructor fonksiyonuna geçirerek, ofstream sınıfı türünden outfile adlı bir akış nesnesi oluşturur. Nesneyi kontrol ederek dosya açma işleminin başarılı olup olmadığını kontrol eder. Dosya mevcut olduğundan, if koşulu gerçekleşmez ve program çalışmasına devam eder. Sonra, akış nesnesi ile << işaretçisini kullanarak, bir karakter dizisini dosyaya yazar. Yazma işlemi sona erdikten sonra, close() fonksiyonu ile dosyayı kapatır.

Program, bir dosyadan okuma işlemi yapmak için, dosya adını constructor fonksiyonuna geçirerek, ifstream sınıfı türünden infile adlı bir akış nesnesi oluşturur. Nesneyi kontrol ederek dosya açma işleminin başarılı olup olmadığını kontrol eder. Dosya mevcut olduğundan, if koşulu gerçekleşmez ve program çalışmasına devam eder. Sonra, peek() fonksiyonunu kullanarak, dosyadan ilk karakteri okur, id adlı int değişkene atar ve değişken değerini ekrana yazar. Daha sonra, getline() fonksiyonu ile dosyadan bir satır okur ve ekrana yazar. Burada, getline() fonksiyonundan önce peek() fonksiyonunun kullanılması dosya aktif konumunu etkilemediğinden, getline() fonksiyonu dosyanın başından itibaren karakterleri okur. Daha sonra, close() fonksiyonu ile dosyayı kapatır.

## Giriş akışından okunan karakteri yerine koyma

C++'da, bir akıştan okunan bir karakteri akışa geri koymak için, aşağıda genel yapısı verilen putback() fonksiyonunu kullanabiliriz:

istream& putback(char ch);

Fonksiyon, akıştan okunan en son karakteri tekrar akışa gönderir. Akıştan okuduğu karakteri veya dosya sonuna erişilmiş ise, EOF değerini geri döndürür.

Şimdi, putback() fonksiyonunun kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>
#include <fstream>
#include <cstdlib>

using namespace std;

int main(void)
{
  ofstream outfile("deneme.txt");  // Dosyaya yazma işlemi için akış oluşturma

  // Dosya açma hata kontrolü
  if(!outfile) {
     cout << "Yazma amaçlı dosya açma hatası!" << endl;
     exit(1);
  }

  outfile << "putback() fonksiyonunun kullanımı";

  outfile.close();                // Dosya kapatma

  ifstream infile("deneme.txt");  // Dosyaya yazma işlemi için akış oluşturma

  // Dosya açma hata kontrolü
  if(!infile) {
     cout << "Okuma amaçlı dosya açma hatası!" << endl;
     exit(1);
  }

  char cd;
  infile.get(cd); // Akıştan bir karakter okur.

  cout << cd << endl;

  infile.putback(cd); // get() fonksiyonu ile okunan karakteri akışa geri yollar ve dosya aktif konumunu bir karakter geri alır.

  char cdizi[100];
  infile.getline(cdizi, 100);
  cout << cdizi << endl;

  infile.close();                // Dosya kapatma

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

p
putback() fonksiyonunun kullanımı

```

Program, bir dosyaya yazma işlemi yapmak için, dosya adını constructor fonksiyonuna geçirerek, ofstream sınıfı türünden outfile adlı bir akış nesnesi oluşturur. Nesneyi kontrol ederek dosya açma işleminin başarılı olup olmadığını kontrol eder. Dosya mevcut olduğundan, if koşulu gerçekleşmez ve program çalışmasına devam eder. Sonra, akış nesnesi ile << işaretçisini kullanarak, bir karakter dizisini dosyaya yazar. Yazma işlemi sona erdikten sonra, close() fonksiyonu ile dosyayı kapatır.

Program, bir dosyadan okuma işlemi yapmak için, dosya adını constructor fonksiyonuna geçirerek, ifstream sınıfı türünden infile adlı bir akış nesnesi oluşturur. Nesneyi kontrol ederek dosya açma işleminin başarılı olup olmadığını kontrol eder. Dosya mevcut olduğundan, if koşulu gerçekleşmez ve program çalışmasına devam eder. Sonra, get() fonksiyonunu kullanarak, dosyadan ilk karakteri okur, cd adlı char değişkene atar ve değişken değerini ekrana yazar. Akıştan okuduğu karakteri akışa geri koymak için, putback() fonksiyonunu kullanır. Daha sonra, getline() fonksiyonu ile dosyadan bir satır okur ve ekrana yazar. Burada, getline() fonksiyonundan önce get() fonksiyonunun kullanılması dosya aktif konumunu etkilediğinden, putback() fonksiyonu ile karakter akışa geri gönderildikten sonra, getline() fonksiyonu dosyanın başından itibaren karakterleri okur. Daha sonra, close() fonksiyonu ile dosyayı kapatır.

## Tampon bellek boşaltma

Bir akışa bağlı dosya gibi fiziksel aygıtlara yazma işlemi yapıldığında, veriler doğrudan dosyaya yazılmaz. Veriler önce sistemde tanımlı tampon belleğe aktarılır. Tampon bellek kapasitesi dolduğunda, veriler diske kaydedilir. Bir dosyayı kapattığımızda veya program sona erdiğinde tüm tampon bellekler temizlenerek diske kayıt yapılır.

Tampon belleğin dolmasını beklemeden, verilerin diske yazılmasını sağlamak için, aşağıda genel yapısı verilen flush() fonksiyonunu kullanabiliriz:

ostream& flush();

Önce, flush() fonksiyonu kullanılmadan, dosyaya karakter yazan ve okuyan örnek bir programı incelemeye çalışalım:

Örnek

```c++
#include <iostream>
#include <fstream>
#include <cstdlib>

using namespace std;

int main(void)
{
  ofstream outfile("deneme.txt"); // Dosyaya yazma işlemi için akış oluşturma
  char cd;

  // Dosya açma hata kontrolü
  if(!outfile) {
     cout << "Yazma amaçlı dosya açma hatası!" << "\n";
     exit(1);
  }

  // Karakterleri dosyaya yazma (Tampon belleğe yazılır)
  for(cd='A'; cd<='Z'; cd++) {
      outfile.put(cd);
  }

  // Dosyaya yazma için akış açık iken, dosyadan okuma için akış açma
  ifstream infile("deneme.txt");

  // Dosya açma hata kontrolü
  if(!infile) {
     cout << "Okuma amaçlı dosya açma hatası!" << "\n";
     exit(1);
  }

  // Veriler tampon bellekte yer aldığından ve dosyaya yazılmadığından
  // dosya içeriği henüz boştur. Bu nedenle herhangi bir değer okunamaz.
  cout << "İlk okuma: ";
  while(infile.get(cd)) { // Dosya sonuna erişildiğinde hata verir.
    cout << cd;
  }

  // Dosyaya yazma için kullanılan akışın kapatılması ile tampon bellekteki veriler dosyaya yazılır.
  outfile.close();

  // Dosya okuma için kullanılan akışın konum göstergesi başa alınır.
  // Dosyadan okuma için yeni bir akış açmak aynı sonucu verir.
  infile.clear();
  infile.seekg (0, ios::beg); // Dosya okuma işaretçisini dosya başına konumlandırma

  // Dosya içeriği dolu olduğundan veriler okunarak ekrana yazılır.
  cout << "\nİkinci okuma: ";
  while(infile.get(cd)) { // Dosya sonuna erişildiğinde hata verir.
    cout << cd;
  }

  infile.close(); // Dosya kapatma

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

İlk okuma: 
İkinci okuma: ABCDEFGHIJKLMNOPQRSTUVWXYZ

```

Program, bir metin dosyasına yazma işlemi yapmak için, dosya adını constructor fonksiyonuna geçirerek, ofstream sınıfı türünden outfile adlı bir akış nesnesi oluşturur. Nesneyi kontrol ederek dosya açma işleminin başarılı olup olmadığını kontrol eder. Dosya mevcut olduğundan, if koşulu gerçekleşmez ve program çalışmasına devam eder. Sonra, put() fonksiyonunu bir for döngüsü içinde kullanarak, A-Z arasındaki karakterleri dosyaya yazar. Yazma işlemi sona erdikten sonra, dosyaya yazma için oluşturulan akış açık iken, dosyadan okuma işlemi yapmak için, dosya adını constructor fonksiyonuna geçirerek, ifstream sınıfı türünden infile adlı bir akış nesnesi oluşturur. Nesneyi kontrol ederek dosya açma işleminin başarılı olup olmadığını kontrol eder. Dosya mevcut olduğundan, if koşulu gerçekleşmez ve program çalışmasına devam eder. Sonra, get() fonksiyonunu bir while döngüsü içinde kullanarak, dosyadaki karakterleri sıra ile okuyarak ekrana yazmaya çalışır. Ancak, veriler tampon bellekte yer aldığından ve dosyaya yazılmadığından, dosya içeriği henüz boştur. Bu nedenle herhangi bir değer okunamaz.

Sonra, dosyaya yazma için açılan akış kapatılır. Bu işlemle birlikte, tampon bellekteki veriler dosyaya yazılır. Dosyadan okuma için oluşturulan akışın konum göstergesi clear() ve seekg() fonksiyonları ile başa alınır. Sonra, tekrar get() fonksiyonunu bir while döngüsü içinde kullanarak, dosyadaki karakterleri sıra ile okuyarak ekrana yazmaya çalışır. Dosya içeriği dolu olduğundan veriler okunarak ekrana yazılır. Sonra, okuma işlemi için açılan akışı kapatır.

> Akışa yazılan verilerin dosyaya fiziksel olarak yazılmasını sağlayan akışın kapatılmasıdır. Akışın kapatılması ile birlikte tampon bellekte yer alan veriler dosyaya aktarılır.
{: .prompt-tip }

Şimdi, yukarıdaki programa, dosyaya her bir karakter yazılmasında kullanılmak üzere, flush() fonksiyonunu eklediğimizde, meydana gelen değişikliği incelemeye çalışalım:

Örnek

```c++
#include <iostream>
#include <fstream>
#include <cstdlib>

using namespace std;

int main(void)
{
  ofstream outfile("deneme.txt"); // Dosyaya yazma işlemi için akış oluşturma
  char cd;

  // Dosya açma hata kontrolü
  if(!outfile) {
     cout << "Yazma amaçlı dosya açma hatası!" << "\n";
     exit(1);
  }

  // Karakterleri doğrudan dosyaya yazma
  for(cd='A'; cd<='Z'; cd++) {
      outfile.put(cd);
	  outfile.flush(); // Bu işlem satırı her karakterin tampon bellek yerine doğrudan dosyaya yazılmasını sağlar.
  }

  // Dosyaya yazma için akış açık iken, dosyadan okuma için akış açma
  ifstream infile("deneme.txt");

  // Dosya açma hata kontrolü
  if(!infile) {
     cout << "Okuma amaçlı dosya açma hatası!" << "\n";
     exit(1);
  }

  // Veriler doğrudan dosyaya yazıldığından dosya içeriği doludur.
  // Bu nedenle tüm değerler okunur.
  cout << "İlk okuma: ";
  while(infile.get(cd)) { // Dosya sonuna erişildiğinde hata verir.
    cout << cd;
  }

  // Veriler doğrudan dosyaya yazıldığından, akışın kapatılmasının
  // tampon bellekteki verilerin dosyaya yazılmasına bir etkisi yoktur.
  outfile.close();

  // Dosya okuma için kullanılan akışın konum göstergesi başa alınır.
  // Dosyadan okuma için yeni bir akış açmak aynı sonucu verir.
  infile.clear();
  infile.seekg (0, ios::beg); // Dosya okuma işaretçisini dosya başına konumlandırma

  // Dosya içeriği dolu olduğundan veriler okunarak ekrana yazılır.
  cout << "\nİkinci okuma: ";
  while(infile.get(cd)) { // Dosya sonuna erişildiğinde hata verir.
    cout << cd;
  }

  infile.close(); // Dosya kapatma

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

İlk okuma: ABCDEFGHIJKLMNOPQRSTUVWXYZ
İkinci okuma: ABCDEFGHIJKLMNOPQRSTUVWXYZ

```

Program, bir metin dosyasına yazma işlemi yapmak için, dosya adını constructor fonksiyonuna geçirerek, ofstream sınıfı türünden outfile adlı bir akış nesnesi oluşturur. Nesneyi kontrol ederek dosya açma işleminin başarılı olup olmadığını kontrol eder. Dosya mevcut olduğundan, if koşulu gerçekleşmez ve program çalışmasına devam eder. Sonra, put() fonksiyonunu bir for döngüsü içinde kullanarak, A-Z arasındaki karakterleri dosyaya yazar. Her karakteri yazdıktan sonra flush() fonksiyonunu kullandığından, her karakter tampon bellek yerine doğrudan dosyaya yazılır. Yazma işlemi sona erdikten sonra, dosyaya yazma için oluşturulan akış açık iken, dosyadan okuma işlemi yapmak için, dosya adını constructor fonksiyonuna geçirerek, ifstream sınıfı türünden infile adlı bir akış nesnesi oluşturur. Nesneyi kontrol ederek dosya açma işleminin başarılı olup olmadığını kontrol eder. Dosya mevcut olduğundan, if koşulu gerçekleşmez ve program çalışmasına devam eder. Sonra, get() fonksiyonunu bir while döngüsü içinde kullanarak, dosyadaki karakterleri sıra ile okuyarak ekrana yazar.

Sonra, dosyaya yazma için açılan akış kapatılır. Dosyadan okuma için oluşturulan akışın konum göstergesi clear() ve seekg() fonksiyonları ile başa alınır. Sonra, tekrar get() fonksiyonunu bir while döngüsü içinde kullanarak, dosyadaki karakterleri sıra ile okuyarak ekrana yazar. Sonra, okuma işlemi için açılan akışı kapatır.

Akışa yazılan verilerin dosyaya fiziksel olarak yazılmasını sağlayan flush() fonksiyonudur.

## Giriş/Çıkış işlemlerinde durum kontrolü

C++'da, her giriş/çıkış işleminden sonra, sistem bir durum bilgisi sağlar. CodeBlocks 17.12 sürümünde ios\_base.h başlık dosyasının içinde \_Ios\_Iostate isimli bir numaralandırma yapılmış ve typedef anahtar kelimesi ile iostate adlı bir veri türü tanımlanmıştır. Sonra, \_Ios\_Iostate içinde yer alan her bir değer için iostate veri türünden (numaralandırma) statik sabit bir değer oluşturulmuştur. Giriş/çıkış sisteminin aktif durumu, bu sabit değerlerle ifade edilmektedir.

Bildirim

```c++
// ios_base.h içeriğinde

enum _Ios_Iostate { 
  _S_goodbit 		 = 0,
  _S_badbit 		 = 1L << 0,
  _S_eofbit 		 = 1L << 1,
  _S_failbit		 = 1L << 2,
  _S_ios_iostate_end = 1L << 16 
};
	
typedef _Ios_Iostate iostate;

static const iostate badbit = _S_badbit;
static const iostate eofbit = _S_eofbit;
static const iostate failbit = _S_failbit;
static const iostate goodbit = _S_goodbit;	


```

Başlık dosyasında (ios\_base.h) yer alan sabit değerlerin kullanım amaçları aşağıdaki tabloda yer almaktadır:

| Değer | Açıklama |
| --- | --- |
| badbit | Giriş/Çıkış işleminde okuma/yazma hatası |
| eofbit | Veri girişinde dosya sonuna erişildi. |
| failbit | Giriş/Çıkış işleminde mantıksal hata |
| goodbit | Hata yok (parametre değeri 0) |

Bu değerlerden iki veya daha fazlasını OR işlemcisi ile birleştirerek kullanabiliriz.

Giriş/çıkış sistemini hata flag değerlerinin tamamının aktif durumunu aşağıda genel yapısı verilen rdstate fonksiyonu ile alabiliriz:

iostate rdstate();

Fonksiyon hata flag değerlerinin aktif konumunu geri döndürür.

Her bir giriş/çıkış hata flag değerini ayrı ayrı almak için ise, aşağıda genel yapıları verilen bad, eof, fail ve good fonksiyonlarını kullanabiliriz:

bool bad();

bool eof();

bool fail();

bool good();

* Eğer badbit flag değeri ayarlanmış ise, bad() fonksiyonu doğru, aksi takdirde yanlış bir değer geri döndürür.
* Eğer eofbit flag değeri ayarlanmış ise, eof() fonksiyonu doğru, aksi takdirde yanlış bir değer geri döndürür.
* Eğer failbit flag değeri ayarlanmış ise, fail() fonksiyonu doğru, aksi takdirde yanlış bir değer geri döndürür.
* Eğer herhangi bir hata yoksa, good() fonksiyonu doğru, aksi takdirde yanlış bir değer geri döndürür.

Giriş/çıkış işlemlerinde hata durumlarını gösteren flag değerlerini belirlemek için ios sınıfı içinde yer alan ve genel yapısı aşağıda gösterilen clear() fonksiyonunu kullanabiliriz:

void clear(iostate state = goodbit);

Tüm giriş ve çıkış işlemlerine ait flag değerleri, fonksiyona geçirilen state parametre değerine göre değiştirilir. Eğer state değeri ön tanımlı değer olan goodbit (sıfır) değerini alırsa, fonksiyon parametresiz olarak çağrıldığında zaten bu değeri alacaktır, tüm hata flag değerleri sıfırlanır.

Clear() fonksiyonunun parametresinde iostate değerlerinden biri veya daha fazlası kullanılabilir.

Şimdi, giriş/çıkış işlemlerinde durum kontrolü yapılmasını ve flag değerlerinin belirlenmesini dosyaya karakter yazan ve okuyan örnek bir program üzerinden incelemeye çalışalım:

Örnek

```c++
#include <iostream>
#include <fstream>
#include <cstdlib>

using namespace std;

void deger_yaz(const char *cdeger, long int val)
{
  int bitsayi = 32;
  char *cdizi = (char*) malloc(bitsayi+1);
  cdizi[bitsayi] = '\0';

  unsigned long int u = *(unsigned long int*)&val
  unsigned long int mask = 1 << (bitsayi-1);
  int id;

  for (id=0; id<bitsayi; id++, mask >>= 1) {
       cdizi[id] = (u & mask) ? '1' : '0';
  }

  printf("%-8s %3ld : %s\n", cdeger, val, cdizi);
  free(cdizi);
}

void hata_durumu(ifstream &ifst)
{
  ios::iostate iosta = ifst.rdstate();

  deger_yaz((const char*) "iostate", iosta);

  if(iosta & ios::badbit) {  // ifst.bad()
     cout << "badbit flag değeri ayarlandı!" << "\n";
     deger_yaz((const char*) "badbit", ios::badbit);
  }
  if(iosta & ios::failbit) { // ifst.fail()
     cout << "failbit flag değeri ayarlandı!" << "\n";
     deger_yaz((const char*) "failbit", ios::failbit);
  }
  if(iosta & ios::eofbit) {  // ifst.eof()
     cout << "eofbit flag değeri ayarlandı!" << "\n";
     deger_yaz((const char*) "eofbit", ios::eofbit);
  }
}

int main(void)
{
  ios::iostate iosta;

  ifstream infile1("deneme.txt"); // Dosyadan okuma için akış açma

  // Dosya mevcut olmadığından failbit flag değeri ayarlanır.
  if(!infile1) {
     if (!infile1.good()) {
         cout << "iostate flag değerlerinden birisi ayarlandı!" << "\n";
         hata_durumu(infile1);
     }
  }

  cout << "\n";

  infile1.clear();
  infile1.close();

  iosta = infile1.rdstate();
  deger_yaz((const char*) "iostate", iosta);

  ofstream outfile("deneme.txt"); // Dosyaya yazma işlemi için akış oluşturma
  char cd;

  // Dosya açma hata kontrolü
  if(!outfile) {
     cout << "deneme.txt dosyası açma hatası!";
	 exit(1);
  }

  // Karakterleri dosyaya yazma (Tampon belleğe yazılır)
  for(cd='A'; cd<='Z'; cd++) {
      outfile.put(cd);
  }

  outfile.close();

  ifstream infile2("deneme.txt"); // Dosyadan okuma için akış açma

  // Dosya mevcut olduğundan flag değerleri ayarlanmaz.
  if(!infile2) {
     if (!infile2.good()) {
         cout << "iostate flag değerlerinden birisi ayarlandı!" << "\n";
         hata_durumu(infile2);
     }
  }

  cout << "\n";

  while(infile2.get(cd)) { // Dosya sonuna erişildiğinde hata verir.
    cout << cd;
  }

  cout << "\n";

  if (!infile2.good()) {
      cout << "iostate flag değerlerinden birisi ayarlandı!" << "\n";
      hata_durumu(infile2);
  }

  infile2.close();

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

iostate flag değerlerinden birisi ayarlandı!
iostate    4 : 00000000000000000000000000000100
failbit flag değeri ayarlandı!
failbit    4 : 00000000000000000000000000000100

iostate    4 : 00000000000000000000000000000100

ABCDEFGHIJKLMNOPQRSTUVWXYZ
iostate flag değerlerinden birisi ayarlandı!
iostate    6 : 00000000000000000000000000000110
failbit flag değeri ayarlandı!
failbit    4 : 00000000000000000000000000000100
eofbit flag değeri ayarlandı!
eofbit     2 : 00000000000000000000000000000010

```

Program, iostate veri türünden bir değişken oluşturur. Mevcut olmayan bir metin dosyasından veri okumak için infile1 adlı bir akış nesnesi oluşturur. Ancak, dosya mevcut olmadığından, failbit flag değeri ayarlanır. Önce, good() fonksiyonunu kullanarak, iostate flag değerlerinden birinin ayarlandığını ekrana yazar. Sonra, akış nesnesini parametre olarak geçirerek, hata\_durumu() fonksiyonunu çağırır. Bu fonksiyonun içinde, rdstate() fonksiyonunu kullanarak, sistem giriş/çıkış flag değerlerinin son durumunu alarak değerini onluk ve ikili sayı sisteminde ekran yazar. Bu değeri sıra ile flag değerleri ile karşılaştırarak, ayarlanmış flag değerlerini de ekrana yazar.

Tüm flag değerlerini clear fonksiyonu ile temizledikten sonra, akışı kapatır. Flag değerlerinin en son halini tekrar ekrana yazar.

Bir metin dosyasına yazma işlemi yapmak için, dosya adını constructor fonksiyonuna geçirerek, ofstream sınıfı türünden outfile adlı bir akış nesnesi oluşturur. Nesneyi kontrol ederek dosya açma işleminin başarılı olup olmadığını kontrol eder. Dosya mevcut olduğundan, if koşulu gerçekleşmez ve program çalışmasına devam eder. Sonra, put() fonksiyonunu bir for döngüsü içinde kullanarak, A-Z arasındaki karakterleri dosyaya yazar. Yazma işlemi sona erdikten sonra, dosyayı kapatır.

Artık mevcut olan bir metin dosyasından okuma işlemi yapmak için, dosya adını constructor fonksiyonuna geçirerek, ifstream sınıfı türünden infile2 adlı bir akış nesnesi oluşturur. Nesneyi kontrol ederek dosya açma işleminin başarılı olup olmadığını kontrol eder. Dosya mevcut olduğundan, if koşulu gerçekleşmez ve program çalışmasına devam eder. Sonra, get() fonksiyonunu bir while döngüsü içinde kullanarak, dosyadaki karakterleri sıra ile okuyarak ekrana yazar. Tekrar good() ve hata\_durumu() fonksiyonlarını kullanarak, flag değerlerini tekrar ekrana yazar.

## Dosya konumuna rastgele erişim

C++'da, dosyaların herhangi bir konumuna rastgele erişim sağlamak için, seekg() ve seekp() fonksiyonlarını kullanabiliriz. Fonksiyonların genel yapıları aşağıda gösterilmektedir:

ostream& seekp(off\_type offset, seekdir dir);

ostream& seekp(streampos pos);

istream& seekg(off\_type offset, seekdir dir);

istream& seekg(streampos pos);

pos: Akışın kesin konumunu gösterir.

dir: Akışın hangi konuma göre aranacağını gösterir.

offset: origin parametre değerine göre akışın kesin konumunu gösterir.

Her iki fonksiyonunun iki farklı kullanım şekli vardır.

Burada, off\_type veri türü ios sınıf içinde tanımlanan bir int veri türüdür.

CodeBlocks 17.12 sürümünde ios\_base.h başlık dosyasının içinde \_Ios\_Seekdir isimli bir numaralandırma yapılmış ve typedef anahtar kelimesi ile seekdir adlı bir veri türü tanımlanmıştır. Sonra, \_Ios\_Seekdir içinde yer alan her bir değer için seekdir veri türünden (numaralandırma) statik sabit bir değer oluşturulmuştur.

Örnek

```c++
// ios_base.h içeriğinde

enum _Ios_Seekdir { 
  _S_beg = 0,
  _S_cur = _GLIBCXX_STDIO_SEEK_CUR, // 1
  _S_end = _GLIBCXX_STDIO_SEEK_END, // 2
  _S_ios_seekdir_end = 1L << 16 
};
	
typedef _Ios_Seekdir seekdir;

// Akışın başlangıcına göre bir arama yapar.
static const seekdir beg = _S_beg;

// Aktif konuma göre bir arama yapar.
static const seekdir cur = _S_cur;

// Akışın sonuna göre bir arama yapar.
static const seekdir end = _S_end;	


```

C++'da, Giriş/Çıkış sistemi, bir dosya ile ilgili olarak iki işaretciyi kontrol eder. Biri, bir sonraki giriş işleminin dosyanın hangi konumunda gerçekleşeceğini, diğeri ise bir sonraki çıkış işleminin dosyanın hangi konumunda gerçekleşeceğini gösterir. Bir giriş veya çıkış işlemi her gerçekleştiğinde, uygun işaretçi otomatik olarak sıralı olarak ilerletilir.

Seekg() ve seekp() fonksiyonları ise, dosyanın herhangi bir konumuna doğrudan erişme olanağı sağlar. Seekg() fonksiyonu, işlem yapılan dosyanın giriş işlemi yapılacak konumunu gösteren işaretçisini, offset parametresi ile gösterilen değer kadar dir parametresi ile gösterilen dosya konumuna göre, taşır. Seekp() fonksiyonu, işlem yapılan dosyanın çıkış işlemi yapılacak konumunu gösteren işaretçisini, offset parametresi ile gösterilen değer kadar dir parametresi ile gösterilen dosya konumuna göre, taşır.

Bir dosya ile ilgili yazma ve okuma işlemlerini, sadece fstream sınıfından bir akış nesnesi tanımlayarak yapabiliriz. Ancak, fstream akış nesnesi ile << işlemcisini kullanarak dosyaya veri yazdıktan sonra, okuma işlemini baştan itibaren yapabilmek için, dosya konumunu başa almamız gerekir. Daha önce, dosya yazma ve okuma işlemleri için ofstream ve ifstream akış nesneleri birlikte kullanıldığında, ostream akış nesnesi ile dosyaya yazma işlemi sona erdikten sonra dosya kapatıldığından ve ifstream akış nesnesi ile yeniden açıldığından, dosya konumu otomatik olarak başa alınıyordu.

Sadece fstream akış nesnesini kullandığımızda, dosyaya veri yazdıktan sonra, okuma işlemini baştan itibaren yapabilmek için, clear() ve seekg() sistem fonksiyonlarını kullanabiliriz.

Şimdi, dosya ile ilgili yazma ve okuma işlemlerinin sadece fstream sınıfından bir akış nesnesi kullanılarak yapılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>
#include <fstream>
#include <cstdlib>

using namespace std;

int main(void)
{
  fstream oifile("deneme.txt");  // Dosyaya yazma ve okuma işlemi için akış oluşturma

  // Dosya açma hata kontrolü
  if(!oifile) {
     cout << "Yazma ve okuma amaçlı dosya açma hatası!" << endl;
     exit(1);
  }

  // Dosyaya yazma işlemleri
  oifile << "Bilgisayar" << endl;
  oifile << 127 << endl;
  oifile << 54.789 << endl;

  oifile.clear();
  oifile.seekg (0, ios::beg);    // Dosya okuma işaretçisini dosya başına konumlandırma

  // Dosyadan okuma işlemleri
  char cdizi[25];
  int id;
  float fd;

  oifile >> cdizi;
  oifile >> id;
  oifile >> fd;

  // Dosyadan okunan verileri ekrana yazma
  cout << cdizi << endl << id << endl << fd;

  oifile.close();                // Dosya kapatma

  return 0;
}


```

Program, bir dosya ile ilgili yazma ve okuma işlemleri yapmak için, dosya adını constructor fonksiyonuna geçirerek, fstream sınıfı türünden oifile adlı bir akış nesnesi oluşturur. Nesneyi kontrol ederek dosya açma işleminin başarılı olup olmadığını kontrol eder. Dosya mevcut olduğundan, if koşulu gerçekleşmez ve program çalışmasına devam eder. Sonra, akış nesnesi ile << işaretçisini kullanarak bir karakter dizisi, bir int ve bir float değeri dosyaya yazar. Clear() fonksiyonu ile giriş ve çıkış işlemleri durum flag değerlerini ilk haline getirir. Dosya okuma işaretçisini, seekg() fonksiyonu ile, dosya başına konumlandırır. Dosyadan okuyacağı değerleri atamak için bir karakter dizisi, bir int ve bir float değer oluşturur. Sonra, akış nesnesi ile >> işlemcisini kullanarak bir karakter dizisi, bir int ve bit float değeri dosyadan okur ve daha önce oluşturduğu dizi ve değişkenlere atar. Okuduğu değerleri ekrana yazdıktan sonra, close() fonksiyonu ile dosyayı kapatır.

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Bilgisayar
127
54.789

```

## Dosya aktif konumunu alma

C++'da, dosyanın aktif konumunu elde etmek için aşağıda fenel yapıları verilen tellg() ve tellp() fonksiyonlarını kullanabiliriz.

pos\_type tellg();

pos\_type tellp();

pos\_type: Her iki fonksiyonun geri döndürebileceği azami değeri gösterir.

Bu fonksiyonlar aktif dosya konumunu kaydederek, bu konumun daha sonra dosya işlemlerinde kullanılmasını sağlar.

Şimdi, tellg() fonksiyonunun kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>
#include <fstream>
#include <cstdlib>

using namespace std;

int main(void)
{
  fstream oifile("deneme.txt"); // Dosyaya yazma ve okuma işlemi için akış oluşturma
  char cd;

  // Dosya açma hata kontrolü
  if(!oifile) {
     cout << "Yazma ve okuma amaçlı dosya açma hatası!" << endl;
     exit(1);
  }

  for(cd='A'; cd<='Z'; cd++) oifile.put(cd);

  int length = oifile.tellg(); // Dosya sonu konumunu alma
  oifile.clear();
  oifile.seekg (0, ios::beg);  // Dosya okuma işaretçisini dosya başına konumlandırma

  char cdizi[length];
  oifile.read(cdizi, length);

  cout << cdizi;

  oifile.close(); // Dosya kapatma

  return 0;
}


```

```

ABCDEFGHIJKLMNOPQRSTUVWXYZ

```

Program, bir metin dosyasına yazma ve okuma işlemi yapmak için, dosya adını constructor fonksiyonuna geçirerek, fstream sınıfı türünden oifile adlı bir akış nesnesi oluşturur. Nesneyi kontrol ederek dosya açma işleminin başarılı olup olmadığını kontrol eder. Dosya mevcut olduğundan, if koşulu gerçekleşmez ve program çalışmasına devam eder. Sonra, put() fonksiyonunu bir for döngüsü içinde kullanarak, A-Z arasındaki karakterleri dosyaya yazar. Yazma işlemi sona erdikten sonra, tellg() fonksiyonunu kullanarak dosyanın aktif konumunu, bu durumda sonunu, alır ve length adlı değişkene yükler ve seekg() fonksiyonu ile dosya aktif konumunu başa alır. Sonra, length değerini read() fonksiyonu ile kullanarak, dosyanın tamamını okur ve verileri ekrana yazar. İşlemi bitirdikten sonra, close() fonksiyonu ile dosyayı kapatır.

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

ABCDEFGHIJKLMNOPQRSTUVWXYZ

```
