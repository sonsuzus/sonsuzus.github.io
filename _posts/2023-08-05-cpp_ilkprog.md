---
title:  C++ İlk program
author: sonsuz
date: 2023-08-05 20:58:29 +0300
categories: [Program,C++]
tags: [cpp,programlama,namespace,fonksiyon]
---






C++ programlama dilinde büyük ve küçük harflere farklı işlem yapılmaktadır:

Örneğin: "Fonksiyon" ve "fonksiyon" kelimeleri tamamen farklı kabul edilir.

## İsim alanı kullanarak program oluşturma

Şimdi, en basit şekilde oluşturulmuş ilk C++ programımızı incelemeye çalışalım:

Örnek

```c++
#include <iostream> // Başlık dosyasını programa ekleme

using namespace std; // std isim alanını kullanıma açma 

int main(void) // Ana fonksiyon bildirimi
{
    cout << "C++ Programlama Dili"; // Ekrana bir karakter dizisi yazma
    
	return 0; // Programın normal bir şekilde sona erdiğini gösterir.
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

C++ Programlama Dili

```

İlk C++ programımızı çalıştırmış olduk. Programda // karakterleri ile başlayan ifadelere yorum adı verilir ve tamamen bilgi verme amaçlı olup, derleyici tarafından herhangi bir işlem yapılmaz.

Şimdi, programı satır satır incelemeye çalışalım.

```c++
#include <iostream>


```

C++'da, # karakteri ile başlayan satırlar önişlemci direktifi olup, program derlenmeden önce, önişlemci tarafından işlem yapılır. Yukarıdaki satırda, kullanılan #include önişlemci direktifi, sağ tarafında yer alan <iostream> adlı başlık dosyasını programa dahil eder. Böylece, <iostream> başlık dosyası içeriği program içinde yazılmış gibi kullanılabilir hale gelir.

Bu durumda, <iostream> başlık dosyasını programımıza dahil ederek, std isim alanını dolayısıyla da cout komutunu programımızda kullanabilme olanağına sahip oluyoruz.

```c++
using namespace std;


```

Yukarıdaki satır, <iostream> adlı başlık dosyasında bulunan std isim alanını kullanmamızı sağlar.

```c++
int main(void)


```

Bir C++ programı çalışmaya başladığında, ilk önce program içinde mutlaka bulunması gereken main() adlı fonksiyonu arar, bulur ve ilk işlem satırından itibaren çalıştırmaya başlar. { ve } işaretleri main() fonksiyon bloğunun başlangıç ve sonunu gösterir. main() ifadesinin sol tarafında yer alan int kelimesi main() fonksiyonunun bir tamsayı değeri geri döndürmesi gerektiğini ifade eder.

C++ dilinde, main ifadesinden sonraki parentezler içindeki void ifadesi, main() fonksiyonunun bir parametreye sahip olmadığını gösterir.

```c++
cout << "C++ Programlama Dili";


```

Yukarıda verilen satır main() fonksiyonu içinde ilk sırada yer alan ve "C++ Programlama Dili" ifadesini ekrana yazan bir işlem satırıdır.

İşlem satırı C++'ın bir defada yerine getirmesi gereken işlem olarak tanımlanabilir. C++'da, bütün işlem satırları noktalı virgül işareti ile sona erer. Yani işlem satırı sonu noktalı virgül (;) işareti ile belirlenir. İşlem satırı, dil bilgisinde görülen satır kavramından farklı olarak, aynı satıra birden fazla yazılabilir.

Burada, << işareti çıktı alma işlemcisi olarak çalışır. cout ifadesi ekran ile ilgili olup << işareti ile birlikte kullanılarak sağ tarafta yer alan ifadeyi ekrana yazmaya yarar.

```c++
return 0;


```

Yukarıdaki satır programın çalışmasının normal bir şekilde sona erdiğini gösteren 0 değerini kendisini çağıran ortama geri döndürür.

## İsim alanı kullanmadan program oluşturma

Aynı programı using namespace std; satırını kullanmadan yazdığımızda, cout komutunun önüne std:: ifadesi eklememiz gerekir. Bu satırı eklemediğimizde, <iostream> dosyasındaki std isim alanını kullanacağımızı bildirmemiş olduğumuzdan, isim alanındaki komutlara doğrudan erişim için isim alanı adını kullanıyoruz.

Örnek

```c++
#include <iostream>

int main()
{
    std::cout << "C++ Programlama Dili";
    return 0;
}


```

## Aynı satırda birden fazla işlem satırı kullanma

Şimdi, tek satırda iki işlem satırının kullanıldığı bir programı incelemeye çalışalım:

Örnek

```c++
#include <iostream>

using namespace std;

int main()
{
    cout << "C++ Programlama Dili" << endl; cout << "Nesneye Dayalı Programlama";
    return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, tek satırda yer alan iki adet işlem satırını çalıştırarak aşağıdaki cümleleri ekrana yazar:

```

C++ Programlama Dili
Nesneye Dayalı Programlama

```

> C++ bir satırda (;) işaretine rastladığında, bu işareti işlem satırı sonu olarak algılar.

İşlem satırı sonundaki endl ifadesi bir sonraki satıra geçisi sağlar ve akışı temizler.

Yukarıdaki iki adet işlem satırını tek satırda yazmakla aşağıda gösterildiği şekilde iki satır halinde yazmak arasında fark yoktur:

Örnek

```c++
#include <iostream>

using namespace std;

int main()
{
    cout << "C++ Programlama Dili" << endl;
    cout << "Nesneye Dayalı Programlama";
    return 0;
}


```

## Fonksiyon kullanarak program oluşturma

Fonksiyonları tanımlanma şekilleri açısından ikiye ayırabiliriz:

* Kütüphane fonksiyonları
* Kullanıcı tanımlı fonksiyonlar

Programlarımızda hazır kütüphane fonksiyonlarını kullanmak istediğimizde, kütüphaneye ait başlık dosyasını programın başında tanımladıktan sonra, sadece fonksiyon adını yazarak çağırmamız yeterlidir. Ancak kullanıcı tanımlı fonksiyonlar kullanmak istediğimizde, fonksiyonu çağırmadan önce, program içinde tanımlamamız gerekir. Şimdi, bir program içinde kullanıcı tanımlı bir fonksiyonu oluşturmanın yolunu incelemeye çalışalım. Fonksiyon C++ programlama dilinde aşağıdaki gibi genel bir yapı ile ifade edilir:

```c++
fonksiyon_adı(parametre1, paramtre2, ...)
{
  işlem satırı;
       .
       .
  işlem satırı;
}


```

Eğer fonksiyon genel yapısı main() fonksiyonundan sonra dosyaya dahil edilirse, main() fonksiyonundan önce aşağıdaki şekilde fonksiyon bildirimi yapılmalıdır.

```c++
fonksiyon_adı(parametre1, parametre2, ...); // fonksiyon bildirimi

int main(void)
{
  işlem satırı:
       .
       .
  işlem satırı;
}

fonksiyon_adı(parametre1, paramtre2, ...)  // fonksiyon yapısı
{
  işlem satırı;
       .
       .
  işlem satırı;
}


```

Fonksiyon tanımlamalarında fonksiyon adı tanımlayabileceğimiz herhangi bir ifade olabilir. Ancak, fonksiyon adı harflerden, rakamlardan ve (\_) işaretinden oluşan bir karakter dizisi olmalıdır. Fonksiyonda bir veya birden fazla işlem satırı bulunabilir.

Bir fonksiyonu yukarıda gösterildiği şekilde tanımladıktan sonra tıpkı kütüphane fonksiyonları gibi çağırabiliriz. Bir fonksiyon main() fonksiyonu veya diğer bir fonksiyon içinden adı kullanılarak çağrılabilir:

```c++
fonksiyon_adı();


```

Bir fonksiyona çağrı yapmak için işlem satırına önce fonksiyon adı ve hemen peşinden de parantez açma ve kapama işaretleri yazılır. İşlem satırı ise doğal olarak noktalı virgül ile sonlandırılır:

```c++
fonk1();


```

Programın farklı yerlerinde aynı işlem satırlarını tekrar etmemniz gerektiğinde, bu işlem satırlarını bir fonksiyon içine yerleştirirsek, her defasında aynı işlem satırlarını yazmak yerine sadece fonksiyonu çağırarak sonuca ulaşmamızı sağlar.

Bir fonksiyon adı kullanılarak çağrıldığında, fonksiyonun içinde yer alan bütün işlem satırları çağrıldığı işlem satırında yazılmış gibi işlem yapılır.

C++ yapısal bir programlama dilidir. Bu özelliğinden dolayı program yazılırken kolaylıkla anlaşılır ve kontrolü basit bir yapı elde edilir. Bu sistemi oluşturmak için C++ programlarının temelini oluşturan fonksiyonlar kullanılır. Bir C++ programında bir veya daha fazla fonksiyon bulunabilir. Ancak, bir programda kaç tane fonksiyon bulunursa bulunsun, bu fonksiyonlardan bir tanesi mutlaka main() adlı fonksiyon olmalıdır.

Yukarıda çalıştırdığımız program içinde yer alan main() fonksiyonu da diğer fonksiyonların özelliklerini içerir.

Program çalışmaya başladığında, direkt olarak main() fonksiyonuna giriş yaptığından ve ilk işlem satırından itibaren işlemleri gerçekleştirdiğinden bahsetmiştik. İşlem satırları açma yaylı parantezi ({) ile kapama yaylı parantezi (}) arasında yer alır:

```c++
int main(void)
{
  işlem satırı:
       .
       .
  işlem satırı;
}


```

Program, başlangıç işaretini ({) görür görmez ilk işlem satırından başlayarak, bütün işlem satırlarının gerektirdiği işlemleri yerine getirir. (}) işaretini görür görmez programın çalışmasını sona erdirir.

Program içinde main() fonksiyonu dışında fonksiyon kullanmak için, yukarıdaki programın aynısını fonksiyon kullanarak tekrar yazdığımızda, program aşağıdaki hale gelecektir:

Örnek

```c++
#include <iostream>

using namespace std;

void fonk(void);

int main(void)
{
  fonk();
  
  return 0;
}

void fonk(void)
{
  cout << "C++ Programlama Dili";
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

C++ Programlama Dili

```

Program, main() fonksiyonu içinde yer alan işlem satırı ile fonk() adlı fonksiyonu çağırır. Fonksiyon bir karakter dizisini ekrana yazar.
