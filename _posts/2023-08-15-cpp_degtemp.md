---
title:  C++ Değişken şablonları (C++ 14)
author: sonsuz
date: 2023-08-15 21:52:00 +0300
categories: [Program,C++]
tags: [cpp,programlama,değişken,şablonlar]
---


C++14 sürümü ile birlikte değişken şablonları oluşturma olanağı sağlandı.

Bir değişken şablonu template anahtar kelimesi ile oluşturulur. Değişken şablonu bildirimi için kullanılan genel yapı aşağıda gösterilmektedir:

```

template <typename T>
constexpr T değişken-adı = T(sabit değer veya ifade);

template <typename T>
constexpr T değişken-adı= sabit değer veya ifade;

```

Değişken şablonunu, template<> yapısını kullanarak, belirli bir veri türü için yeniden tanımlayabiliriz.

```

template <>
constexpr T değişken-adı <T> = sabit değer veya ifade;

```

Değişken şablonu oluşturulduktan sonra aşağıda gösterilen yapı ile program tarafından kullanılır.

```

değişken-adı<T>;

```

Şablon sınıfının kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include<iostream>

using namespace std;

// Değer gösteren değişken şablonunu tanımlama
template<typename t>
t x = 21.7564;

template<typename t>
t y = 75.2189;

template<typename t>
t z = t(5.25)*t(7.45);

int main(void)
{
  cout << x<int> << endl;   // x<int> değeri şablon tarafından belirlenen int bir değişkendir.
  cout << x<float> << endl; // x<float> değeri şablon tarafından belirlenen float bir değişkendir.

  cout << y<int> << endl;   // y<int> değeri şablon tarafından belirlenen int bir değişkendir.
  cout << y<float> << endl; // y<float> değeri şablon tarafından belirlenen float bir değişkendir.

  cout << z<int> << endl;   // z<int> değeri şablon tarafından belirlenen int bir değişkendir.
  cout << z<float> << endl; // z<float> değeri şablon tarafından belirlenen float bir değişkendir.

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

21
21.7564
75
75.2189
35
39.1125

```

Program, önce typename anahtar kelimesini kullanarak, x, y, ve z değişken ismine sahip üç farklı değişken şablonu oluşturur. Her şablonu sırasıyla int ve float veri türü ile çağırır. İlk şablon için yapılan int veri türü çağrısında x`<int>` değişkenine 21 değeri, float veri çağrısında x`<float>` değişkenine 21.7564 değeri atanır. İkinci şablon için yapılan int veri türü çağrısında y`<int>` değişkenine 75 değeri, float veri çağrısında y`<float>` değişkenine 75.2189 değeri atanır. üçüncü şablon için yapılan int veri türü çağrısında z`<int>` değişkenine 5 ve 5 sayısını çarpımı olan 35 değeri, float veri çağrısında z`<float>` değişkenine 5.25 ve 7.45 sayılarının çarpımı olan 39.1125 değeri atanır.

Tüm değişken şablon kullanımlarında belirtilen veri türü, ilgili şablona geçirilerek, şablon içindeki t ifadesinin yerini alır.

Şablon sınıfının tanımlandıktan sonra belirli bir veri türü için tekrar tanımlanmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include<iostream>

using namespace std;

// Değer gösteren değişken şablonunu tanımlama
template<typename t>
t x = t(5.25)*t(7.45);

// Değişken şablonunu int veri türü için yeniden tanımlama
template<>
int x<int> = 3*4;

int main(void)
{
  cout << x<int> << endl;   // x<int> değeri şablon tarafından belirlenen int bir değişkendir.
  cout << x<float> << endl; // x<float> değeri şablon tarafından belirlenen float bir değişkendir.

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

12
39.1125

```

Program, önce typename anahtar kelimesini kullanarak, x değişken ismine sahip bir değişken şablon oluşturur. Oluşturduğu şablonu int veri türü için yeniden tanımlar. Sonra, şablonu sırasıyla int ve float veri türü ile çağırır. İlk çağrıda int veri türü kullanıldığından, şablonun ikinci bildirimindeki atama devreye girer ve ekrana 12 değeri yazılır. İkinci çağrıda ise float veri türü kullanıldığından şablonun ilk bildirimindeki atama devreye girer ve ekrana 39.1125 değeri yazılır.
