---
title:  C++  Switch kalıbı
author: sonsuz
date: 2023-08-08 00:48:26 +0300
categories: [Program,C++]
tags: [cpp,programlama,karşılaştırma,switch]
---


Programlarımızda, iki veya daha fazla seçenekli koşul kontrolü sağlayan bir sistemi oluşturmak için if deyimini kullanabiliriz. Seçeneğin fazla olduğu durumlarda, programın her durumda bütün if satırlarını tek tek kontrol etme zorunluluğundan dolayı, programın çalışmasını daha hızlı ve pratik bir duruma getirmek için if-else-if yapısını kullanabiliriz.

## Switch kalıbı

Şimdi, C++'da çok seçenekli bir sistem sağlayan switch kalıbını incelemeye çalışalım. yelim. switch kalıbı bir ifadenin sonucuna bağlı olarak içinde yer alan herhangi bir seçenekteki işlem satırlarını çalıştıran bir kalıptır. Bu kalıbın genel yapısını birlikte inceleyelim:

```cpp
switch(ifade) {
   case sabit1:
        işlem-satırı
        break;
   case sabit2:
        işlem-satırı;
        break;
        .
        .
        .
   default:
        işlem-satırı;
}


```

switch satırında yer alan ifade ile elde ettiğimiz değer mutlaka case terimlerinin bulunduğu satırlarda yer alan sabit değerlerle karşılaştırılabilecek bir değer olmalıdır. Buradaki ifade genellikle bir değişken değeri olmaktadır.

Koşul bölümünü oluşturan ifade, tek bir değişken değeri, iki değeri karşılaştıran tek bir ilişkisel işlem veya birden fazla ilişkişel işlemi birleştiren mantıksal işlemlerden oluşur.

Program, switch deyiminin bulunduğu satırda yer alan ifadenin sonucu ile switch kalıbının case satırlarında yer alan sabit değerleri karşılaştırır. Burada bahsi geçen sabit değerler ya bir char ya da bir int sabitidir. İfade sonucu ile aynı değeri taşıyan sabit değerin yer aldığı case bölümüne bağlı işlem satırını veya satırlarını çalıştırır. break deyimini görür görmez, switch kalıbının dışına çıkar ve bir sonraki işlem satırından çalışmasına devam eder.

> break deyimini, case yapıları içinde tanımlamak şart değildir. Değişken değeri ile aynı değeri taşıyan sabit değerin yer aldığı case bölümüne bağlı işlem satırı veya satırları çalıştığında, case yapısında bir break deyimi yer almaz ise, program hemen switch kalıbı dışına çıkmaz. Aksine, eğer aşağıda devam eden case yapıları varsa, herhangi bir koşul kontrolü yapmadan, bir sonraki case yapısındaki işlem satırlarını çalıştırır. Ancak, bütün case yapıları içinde break deyimini kullanırsak, switch kalıbı içinde yer alan sadece tek bir case yapısına bağlı işlem satırı ya da satırları çalışır.
{: .prompt-tip }

Koşul sağlanarak bir case yapısı içine girildiğinde çıkış ancak break deyimi ile ya da switch kalıbının sonuna gelmekle sağlanır.

case yapısı içinde break tanımı yapılmamışsa, herhangi bir koşul kontrolü yapmadan, bir sonraki case yapısındaki işlem satırları çalıştırılır.

Eğer, switch satırındaki değişken değeri case satırlarında yer alan sabit değerlerin herhangi biri ile aynı değeri taşımıyorsa, program default satırında yer alan işlem satırı veya satırlarını çalıştırır. default satırının tanımlanması tamamen isteğe bağlıdır. Yani, bu satır tanımlanmasa bile switch kalıbı normal olarak çalışır.

Program, switch kalıbı için tanımlanan değişken değeri ile aynı değeri taşıyan bir sabitin yer aldığı case satırı ile karşılaştığında, bir break ifadesi ile karşılaşana kadar o case satırında yer alan işlem satırlarının gereğini yerine getirir. Eğer son case satırı veya default satırı ile ilgili işlem satırlarının gereğini yerine getiriyorsa switch kalıbının sonuna geldiğinden işlemler otomatik olarak sona ermiş olur. Eğer, case satırlarında yer alan sabit değerlerinden hiçbiri değişken değeri ile aynı değilse ve switch kalıbı içinde default satırı tanımlanmamışsa, program switch kalıbında herhangi bir işlem yapmadan bir sonraki program işlem satırından çalışmasına devam eder.

Yukarıda anlattıklarımızı bir örnek üzerinde incelemeye çalışalım:

Örnek

```cpp
#include <iostream>

using namespace std;

int main(void)
{
  char cd;

  cout << "Bu harflerden birini giriniz : [A]  [B]  [C]" << "\n";

  cin >> cd;

  cd = toupper(cd);

  switch (cd) {
     case 'A' :
       cout << "A harfini girdiniz!";
       break;
     case 'B' :
       cout << "B harfini girdiniz!";
       break;
     case 'C' :
       cout << "C harfini girdiniz!";
       break;
     default :
       cout << "İstenen harflerden birini girmediniz!";
  }

  return 0;
}


```

Program A, B veya C harflerinden birisini girmenizi ister. Sonra, girdiğiniz harfi switch kalıbı için tanımlanmış olan cd değişkenine atayarak case satırlarında yer alan harflerle karşılaştırır. Girdiğiniz harf case satırlarından birinde tanımlanmışsa ilgili satırda yer alan karakter dizisini, aksi takdirde default satırında yer alan karakter dizisini ekrana yazar.

**switch kalıbı ile ilgili göz önünde bulundurulması gereken bazı önemli noktalar vardır:**

* Daha önce gördüğümüz gibi, if deyiminde koşul ifadesi herhangi bir veri türünden olabilir. Ancak, switch kalıbı sadece int ve char veri türleri ile çalışır.

* Switch kalıbında sadece eşitlik için kontrol yapılır.

* Aynı switch kalıbındaki farklı case satırlarında yer alan değişken değerleri birbirinin aynı olamaz. Bu şekilde hazırlanmış olan bir program derlenirken hata verir.

## Default deyimi kullanılmayan switch kalıpları

Switch kalıbını içinde default deyimini kullanmadan da kullanabiliriz. Normal koşullarda, switch satırındaki değişken değeri case satırlarında yer alan sabit değerlerin herhangi biri ile aynı değeri taşımıyorsa, program default satırında yer alan işlem satırı veya satırlarını çalıştırır. Ancak, bu durumda, default satırı tanımlanmamışsa, switch kalıbı içinde herhangi bir işlem yapılmaz.

Şimdi, bir örnek üzerinde bu özelliği incelemeye çalışalım:

Örnek

```cpp
#include <iostream>

using namespace std;

int main(void)
{
  char cd;
  int id;

  cout << "Ekrana yazdırmak istediğiniz harfi giriniz: [A] [B] [C]" << "\n";
  cin >> cd;
  cd = toupper(cd);

  cout << "Kaç kez yazdırmak istersiniz? [1] [3] [5]" << "\n";
  cin >> id;

  switch(id) {
     case 1:
        cout << cd;
        break;
     case 3:
        cout << cd << " " << cd << " " << cd;
        break;
     case 5:
        cout << cd << " " << cd << " " << cd << " " << cd << " " << cd;
        break;
  }

  return 0;
}


```

Yukarıdaki örnekte, program A, B veya C harflerinden birisini girmenizi ister. Program girdiğiniz harfi cd değişkenine atar. Sonra, harfi kaç kez ekran yazdırmak istediğinizi belirlemek için 1, 3 veya 5 sayılarından birini girmenizi ister ve girdiğiniz değeri id değişkenine atar. switch kalıbında id değişken değeri kadar girdiğiniz harfi ekrana yazar.

## Default ve break deyimi kullanılmayan switch kalıpları

Bir switch kalıbının sona ermesi için ya program bir break ifadesi ile karşılaşmalıdır ya da kalıbın sonu gelmiş olmalıdır. Şimdiye kadar gördüğümüz örneklerde switch kalıbında en sonda yer alan hariç bütün case satırları için break ifadesi tanımladık. Bu durumda, sadece switch kalıbının tek bir case satırıyla ilgili işlem satır veya satırları çalışır.

Bir switch kalıbında son case satırı dışındaki case satırlarından birinde break ifadesi tanımlanmazsa ve bu case satırında yer alan sabit değer switch kalıbının kontrol değişkeni ile aynı değeri taşıyorsa, bu case satırı ile ilgili işlemler tamamlandıktan sonra, break ifadesi olmadığından eğer varsa bir sonraki case satırı ile ilgili işlemler yapılır. Bu işlem program bir break ifadesi ile karşılaşana veya switch kalıbının sonu gelene kadar devam eder. Yani bu durumda, switch kalıbının birden fazla seçeneği içinde yer alan işlemler yerine getirilmiş olur. Şimdi, bu özelliği bir örnek üzerinde incelemeye çalışalım:

Örnek

```cpp
#include <iostream>

using namespace std;

int main(void)
{
  int id;

  cout << "Bir sayı giriniz [1-5]" << "\n";
  cin >> id;

  switch (id) {
    case 1:
      cout << "Bir ";
    case 2:
      cout << "İki ";
    case 3:
      cout << "Üç ";
    case 4:
      cout << "Dört ";
    case 5:
      cout << "Beş ";
  }

  return 0;
}


```

Program, 1 ile 5 arasında bir sayı girmenizi ister. Girilen değeri id değişkenine atar. id değişkeni ile switch kalıbını kontrol eder ve değişken değeri ile aynı değeri taşıyan sabit değerin bulunduğu case satırından itibaren switch kalıbının sonuna kadar olan bütün case satırlarındaki işlem satırlarının gereğini yerine getirir. Yani, 1 ile 5 arasında girdiğiniz sayıdan 5'e kadar olan sayıları yazı ile ekrana yazar. Eğer 2 değerini girerseniz aşağıdaki satırı ekrana yazar:

```

İki Üç Dört Beş

```

## İç içe switch kalıpları

switch kalıplarını birbiri içinde kullanabiliriz. Yani, bir switch kalıbına ait bir case satırı ile ilgili işlem satırları yerine başka bir switch kalıbı tanımlayabiliriz. Aşağıda birbiri içinde tanımlanmış 2 switch kalıbı gösterilmektedir:

```cpp
switch(değişken1) {
   case sabit1:
        switch(değişken2) {
           case sabit1:
                işlem satırı;
                break;
           case sabit2:
                işlem satırı;
                break;
           case sabit3:
                işlem satırı;
                break;
        }
   case sabit2:
        işlem satırı;
        break;
   .
   .
   .
   default:
       işlem satırı;
}


```

Şimdi, bu özelliği bir örnek üzerinde incelemeye çalışalım:

Örnek

```cpp
#include <iostream>

using namespace std;

void fonk1(void);
void fonk2(void);

int main(void)
{
  int id;
  char cd;

  cout << "Bu sayılardan birini giriniz: [1] [2] [3]" << "\n";
  cin >> id;

  switch (id) {
     case 1 :
        cout << "Bu harflerden birini giriniz: [A] [B]" << "\n";
        cin >> cd;
        cd = toupper(cd);
        switch (cd) {
           case 'A':
              fonk1();
              break;
           case 'B':
              fonk2();
              break;
           default :
              cout << "Belirtilen harflerden birini girmediniz!" << "\n";
        }
        break;
     case 2 :
        cout << "2 numaralı seçeneği seçtiniz!" << "\n";
        break;
     case 3 :
        cout << "3 numaralı seçeneği seçtiniz!" << "\n";
        break;
     default :
        cout << "Verilen seçeneklerden birini girmediniz!" << "\n";
  }

  return 0;
}

void fonk1(void)
{
  cout << "1 numaralı seçenek içinde A harfini girdiniz!" << "\n";
}

void fonk2(void)
{
  cout << "1 numaralı seçenek içinde B harfini girdiniz!" << "\n";
}
}


```

Program, 1, 2 veya 3 sayılarından birinin girilmesini ister. Girilen değeri id değişkenine atar. İlk switch kalıbını id değişken değeri ile çalıştırır. Eğer girilen değer, 1, 2 veya 3 sayılarından biri değilse, case satırlarında yer alan sabit değerlerin hiçbiri girilen değer ile aynı olmadığından, sadece switch kalıbı içinde yer alan default satırındaki aşağıdaki cümleyi ekrana yazar:

```

Verilen seçeneklerden birini girmediniz!

```

Eğer 1 sayısını girersek, ilk case satırında koşul sağlandığı için program 'A' veya 'B' harflerinden birisini girilmesini ister. Eğer 'A' harfini girersek, program fonk1() fonksiyonunu, 'B' harfini girersek fonk2() fonksiyonunu çalıştırarak ilgili fonksiyonlarda yer alan karakter dizilerini ekrana yazar. Eğer, başlangıçta 2 sayısını girersek, program ikinci case satır koşulu sağlandığı için "2 numaralı seçeneği seçtiniz!" ifadesini, 3 sayısını girersek, üçüncü case satır koşulu sağlandığı için "3 numaralı seçeneği seçtiniz!" ifadesini ekrana yazar. Eğer girilen değer 'A' veya 'B' harflerinden farklı ise sadece switch kalıbı içinde yer alan default satırındaki aşağıdaki cümleyi ekrana yazar:

```

Belirtilen harflerden birini girmediniz!

```
