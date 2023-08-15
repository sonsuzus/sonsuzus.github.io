---
title:  C++ Referanslar
author: sonsuz
date: 2023-08-15 20:39:29 +0300
categories: [Program,C++]
tags: [cpp,programlama,referans]
---


C++'da, referans değişken adı verilen bir değişken tanımlayarak oluşturduğumuz değişenlere farklı bir isim ile erişim sağlayabiliriz.

Referans bildirimi aşağıdaki şekilde yapılmaktadır:

`veri-türü& referans-adı = değişken-adı;`

`int id; // Değişken bildirimi`

`int& rid = id; // Referans bildirimi`

Yukarıdaki işlem satırları ile, önce bir adet id adlı int değişken, sonra bu değişkeni referans gösteren bir adet referans oluşturulur.

Referans oluşturulduğunda, bellekte herhangi bir değişiklik olmaz. Yani, rid referans değerini depolamak için bellek kullanılmaz. Referans rid aslında id değişkeni için ikinci bir isim olarak kullanılır. Bu durumda, referans değeri kullandığımızda değişken adını kullanmış gibi oluruz. id değerini değiştirmek rid değerini değiştirmek ve rid değerini değiştirmek id değerini değiştirmek anlamına gelir.

Referans değişkenlerinin bildirimi yapıldığında bir ilk değer verilmelidir. Ancak, bir sınıf içinde yer aldığında, bir fonksiyon parametresi veya bir fonksiyon geri dönüş değeri olarak kullanıldığında bu kural geçerli değildir.

Şimdi, referans kullanımını bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
// Başlık tanımlaması
#include <iostream>

using namespace std;

int main(void)
{
  int id;                 
  int &rid = id; // Referans tanımı
  
  id = 21;
  cout << id << " " << rid << endl;
  
  rid = 142;
  
  cout << id << " " << rid;
  
  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

21 21
142 142

```

Program, id adlı int bir değişken oluşturur. id değişkeni için rid adlı bir referans tanımlar. Değişken adı ve referans kullanarak id değişken değerini iki kez ekrana yazar. Referans değişkenine 142 değerini atar. Böylece id değişkenine de 142 değeri atanır. Değişken adı ve referans kullanarak id değişken değerini tekrar iki kez ekrana yazar.

Referans değişkenler oluşturulduğunda atanan değerler daha sonra değiştirilemez.

Şimdi, referans kullanımının bu özelliğini bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
// Başlık tanımlaması
#include <iostream>

using namespace std;

int main(void)
{
  int id1, id2;                 
  int &rid = id1; // Referans tanımı
  
  id1 = 36;
  id2 = 57;
  
  cout << id1 << " " << rid << endl;
  
  rid = id2; // id2 değişken değerini id1 değişkenine aktarır. id2 değişkeni için bir referans oluşturmaz.
  
  cout << id1 << " " << id2 << " " << rid;
  
  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

36 36
57 57 57

```

Program, önce iki adet int değişken oluşturur. id1 değişkeni için rid adlı bir referans tanımlar. Değişken adı ve referans kullanarak id1 değişken değerini iki kez ekrana yazar. Referans değişkenine id2 değişkenini atadığında, id2 değişkeni için bir referans oluşturmaz, sadece id2 değişken değerini id1 değişkenine atamış olur. Böylece her iki int değişkeni ve referans değişkeni aynı değeri gösterir.

## Referansların fonksiyon parametresi olarak kullanımı

Bir fonksiyona geçirilen parametreler değer veya referans yoluyla geçirilir. Bir değişkeni değer yoluyla parametre olarak geçirme yöntemi uygulandığında, fonksiyona değişkenin bir kopyası geçirildiğinden, fonksiyon içinde değişken üzerinde yapılan değişiklikler, fonksiyon sona erdiğinde devre dışı kalır. Referans youyla parametre olarak geçirme yöntemi uygulandığında ise, fonksiyona değişkenin adresi geçirildiğinden,fonksiyon içinde değişken üzerinde yapılan değişiklikler, fonksiyon sona erdiğinde de geçerliliğini korur.

Referans yoluyla parametre geçirme işlemini doğrudan işaretçi veya referans kullanarak gerçekleştirebiliriz.

## İşaretçi kullanarak referans yoluyla fonksiyona parametre geçirme

Referans yoluyla fonksiyona parametre geçirme işlemini işaretçi kullanarak yapmak için, fonksiyon parametresini tanımlarken işaretçi kullanmamız gerekir. 

Aşağıdaki program, kare\_al() fonksiyonunda işaretçi kullanarak referans yoluyla çağrılan bir parametre oluşturur. 

Örnek

```c++
// Başlık tanımlaması
#include <iostream>

using namespace std;

void kare_al(int *id);

int main(void)
{
  int id;                 
  
  id = 21;
  
  kare_al(&id); // İşaretçi kullanarak parametre geçirme (değişken adresi geçirilir)
  
  cout << "main() fonksiyonu içindeki id değişken değeri: " << id;
  
  return 0;
}

void kare_al(int *id)
{
  *id = (*id) * (*id);

  cout << "Bellek adresi: " << id << endl;
  cout << "kare_al() fonksiyonu içindeki değişken değeri: " << *id << endl;
}	


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Bellek adresi: 0x6dfeec
kare_al() fonksiyonu içindeki id değişken değeri: 441
main() fonksiyonu içindeki id değişken değeri: 441

```

Program, kare\_al() fonksiyonunu id değişkeninin bellek adresini geçirerek çağırır. Fonksiyon içinde değişkene erişim için \* işlemcisi kullanılır.

## Referans kullanarak referans yoluyla fonksiyona parametre geçirme

Referans yoluyla fonksiyona parametre geçirme işlemini referans kullanarak yapmak için, fonksiyon parametresini tanımlarken referans tanımlamamız gerekir. 

Aşağıdaki program, kare\_al() fonksiyonunda referans kullanarak referans yoluyla çağrılan bir parametre oluşturur. 

Örnek

```c++
// Başlık tanımlaması
#include <iostream>

using namespace std;

void kare_al(int &id);

int main(void)
{
  int id;                 
  
  id = 21;
  
  kare_al(id); // Referans kullanarak parametre geçirme
  
  cout << "main() fonksiyonu içindeki id değişken değeri: " << id;
  
  return 0;
}

void kare_al(int &id)
{
  id = id * id;

  cout << "Bellek adresi: " << &id << endl;
  cout << "kare_al() fonksiyonu içindeki değişken değeri: " << id << endl;
}	


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Bellek adresi: 0x6dfeec
kare_al() fonksiyonu içindeki id değişken değeri: 441
main() fonksiyonu içindeki id değişken değeri: 441

```

Bu yöntemde, fonksiyona geçirilen id değeri, main() fonksiyonu içindeki id değişkeni için doğrudan bir referans oluşturduğundan, fonksiyon içinde \* işaretçisi yerine bu değişken ismi kullanılarak yapılan tüm işlemler main() fonsiyonu içindeki id değişkenini doğrudan etkiler.

## Nesneleri fonksiyonlara referans yoluyla geçirme

Bir nesne bir fonksiyona referans yoluyla geçirildiğinde, doğrudan nesnenin kendisi aktarıldığından, fonksiyon içinde nesne üzerinde yapılan değişiklikler fonksiyonun sona ermesinden sonra da geçerli olur.

Şimdi, bu özelliği bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

class sinif {
  int id;

  public:
    sinif(int pid);
    ~sinif();
	void kare_al(sinif &nes)
	{
	  nes.id = nes.id * nes.id;
	  cout << nes.id << endl;
	}
    void deger_goster() { cout << id << endl; }
};

sinif::sinif(int pid)
{
  id = pid;
  cout << "Nesne oluşturuluyor: " << id << endl;
}

sinif::~sinif()
{
  cout << "Nesne yok ediliyor: " << id << endl;
}

int main()
{
  sinif nes(21);

  cout << "kare_al() fonksiyonu içindeki değer: ";
  nes.kare_al(nes);

  cout << "main() fonksiyonu içindeki değer: ";
  nes.deger_goster();

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Nesne oluşturuluyor: 21
kare_al() fonksiyonu içindeki değer: 441
main() fonksiyonu içindeki değer: 441
Nesne yok ediliyor: 441

```

Program main() fonksiyonu içinde bir nesne oluştururken constructor fonksiyonu yoluyla sınıf içindeki değişkene 21 değerini atar. Bu durumda, constructor fonksiyonu bir kez çağrılır. Sonra, oluşturduğu nesneyi kare\_al() fonksiyonuna referans yoluyla geçirir. Fonksiyon içinde id değişkeninin karesi alınarak değişkene atanır ve değişken değeri ekrana yazılır. Daha sonra, main() fonksiyonu içinde değişken değeri tekrar ekrana yazılır. Fonksiyon ve main() fonksiyonu içindeki değerler aynıdır.

## Fonksiyonlardan referans döndürme

C++'da, bir fonksiyon bir referans değeri geri döndürebilir. Bu özelliği bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

int idizi[5] = { 5, 17, 21, 52, 75 };

int& ref_al(int id) {
   // idizi dizisinin id değişkeni ile gösterilen indeksinde yer alan değerin referansını geri döndürür.
   return idizi[id];   
}

int main()
{
  cout << idizi[2] << endl;
  
  // idizi dizisinin 3.elemanının değerini değiştirir.
  ref_al(2) = 41; // idizi[2] = 41; işlem satırı ile aynı işlemi yapar.

  cout << idizi[2];
  
  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

21
41

```

Program 5 elemanlı bir int dizinin üçüncü elemanının değerini değiştirir. Bu işlemi gerçekleştirmek için, ref\_al() fonksiyonu ile dizinin değişecek olan elemanı için oluşturulan referans değerini geri döndürür. Fonksiyon tarafından geri döndürülen referans dizi değişkenine değer atmak için kullanılır.
