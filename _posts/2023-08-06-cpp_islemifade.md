---
title:  C++ İşlem satırı ve ifade
author: sonsuz
date: 2023-08-06 15:05:15 +0300
categories: [Program,C++]
tags: [programlama,cpp,işlem,ifade]
---


## İşlem satırı

main() fonksiyonu ve diğer fonksiyonlarda yer alan ve noktalı virgül (;) karakteri ile sona eren satırlara işlem satırı adı verilir. Şimdi, işlem satırlarının hangi değerlerden oluşabileceğini incelemeye çalışalım:

İşlem satırı bir değişken bildirimi, değişkene bir değer atama, aritmetik bir ifade, bir fonksiyon çağrısı veya bir döngü içerebilir.

```cpp
int id1, id2, id3;  // Değişken bildirimi
id1 = 4;            // Değişkene değer atama
id2 = 5;            // Değişkene değer atama
id3 = id1 + id2;    // İfade
fonk();             // Fonksiyon çağrısı


```

İfade kavramından başlamak üzere, işlem satırında yer alabilecek kavramları sırasıyla incelemeye başlayabiliriz:

## İfade (Expression) kavramı

İfade işlem satırlarını oluşturan kavramlardan biridir. Matematik derslerinizden hatırlayacağımız gibi, bir ifade değişken ve sabitlere aritmetik işlemciler yoluyla bir işlem yapmaktır. Aşağıdaki satırda görüldüğü gibi y değişkeni ile 2 sabiti toplanıp matematiksel bir ifade oluşturulmuş ve elde edilen değer x değişkenine atanmıştır:

x = y + 2; (Matematiksel ifade)

C++ programlama dilinde ifadenin bundan bir farkı yoktur. C++ dilinde program tanımladığımız değişken ve sabit değerlere işlemcileri kullanarak gereken işlemleri yapar. Burada bahsi geçen değişken, sabit ve işlemci kavramlarının aynı işlem satırında kullanılmasına ifade adı verilir.

Bu tanımlama teorik olarak yeterli olsa da, konunun daha iyi anlaşılması için şimdi, ifade kavramı içinde kullanılan değişkenlerin tanımlanmasını, bu değişkenlere değer atanmasını ve bu şekilde ifadenin oluşturulması işlemlerini sıra ile incelemeye çalışalım:

C++'da ifade adı verilen kavram veri ve işlemcilerin birlikte kullanılmasından elde edilir. Veri ise değişken ve/veya sabitlerden oluşur.

ifade = veriler + işlemciler

veriler = değişkenler + sabitler

İfade adı verilen yapı içinde, program değişken ve sabitlerden oluşan verilere işlemciler yoluyla bir işlem yapar. Artık, ifadeleri oluşturan veri kavramını incelemeye başlayabiliriz.

Şimdi, işlem satırı ve ifade kavramlarını bir örnek üzerinde incelemeye çalışalım:

Örnek

```cpp
#include <iostream>

using namespace std;

void fonk(void)
{
  cout << "C++ Programlama Dili";
}

int main(void)
{
  int id1 = 7;     // int bir değişken bildirimi yapılırken sabit bir değer değişkene atanır.
  int id2;         // int bir değişken bildirimi yapılır.
  int id3, id4;    // İki adet int değişken bildirimi yapılır.

  id2 = 21;        // Sabit bir değer int bir değişkene atanır.

  id3 = id1 + id2; // İki değişken değeri toplanarak int bir değişkene atanır.
  id4 = id3 + 35;  // Bİr değişken değeri ve bir sabit değer toplanarak int bir değişkene atanır.

  cout << id1 << " " << id2 << "\n"; // id1 ve id2 değişken değerleri ekrana yazılır.
  cout << id3 << " " << id4 << "\n"; // id3 ve id4 değişken değerleri ekrana yazılır.

  fonk(); // Fonksiyon çağrısı yapılır.

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

7 21
28 63
C++ Programlama Dili

```

Program, id1 adlı int bir değişken bildirimi yaparken 7 sabit değerini değişkene atar. id2, id3 ve id4 adlı üç adet int değişken bildirimi yapar. id2 değişkenine 21 değerini atar. id1 ve id2 değişken değerlerini toplayarak, sonucu id3 değişkenine atar. id3 değişken değeri ile 35 sabit değerini toplayarak, sonucu id4 değişken değerine atar. Önce, id1 ve id2 değişken değerlerini sonra id3 ve id4 değişken değerlerini cout komutuyla ekrana yazar. fonk() adlı fonksiyonu çağırarak bir karakter dizisini ekrana yazar.
