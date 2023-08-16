---
title:  C++ Algoritmalar
author: sonsuz
date: 2023-08-16 21:13:59 +0300
categories: [Program,C++]
tags: [programlama,cpp,algoritma,konteyner]
---


## Algoritma hakkında

Algoritmalar konteynerler üzerinde işlem yaparlar. Her konteyner kendi temel işlemleri için gerekli fonksiyonları sağlar. Standart algoritmalar ise daha genişletilmiş veya karmaşık işlemler için aynı anda iki farklı tipte konteyner ile çalışmaya olanak sağlar.

STL içindeki algoritmaları kullanmak için, programlarımıza `<algorithm>` başlık dosyasını eklememiz gerekir.

Herhangi bir konteyner ile kullanılabilen ve tümünün bildirimi şablon olarak yapılmış olan STL algoritmalarının bir kısmı aşağıdaki tabloda yer almaktadır:

```c++
vector<int> v { 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4 }; // Range
vector<int> t1 { 1, 2, 3 };                           // Sequence  

find_end(v.begin(), v.end(), t1.begin(), t1.end());

find_end: finds the last sequence of elements in a certain range 


```

| Algoritma | Açıklama |
| --- | --- |
| adjacent\_find | Bir sıra içinde bitişik eşleşen elemanları arar ve ilk eşleşmeyi gösteren bir tekrarlayıcı geri döndürür. |
| binary\_search | Sıralı bir dizi içinde ikili sistem araması yapar. |
| copy | Bir diziyi kopyalar. |
| copy\_backward | copy ile aynı işlemi yapar. Tek fark, sondan başa doğru hareket eder. |
| count | Sıra içindeki eleman sayısını geri döndürür. |
| count\_if | Dizideki bazı koşulları karşılayan elemanların sayısını geri döndürür. |
| equal | İki aralığın aynı olup olmadığını belirler. |
| equal\_range | Sıralamayı bozmadan bir elemanın bir sıralamaya eklenebileceği bir aralık geri döndürür. |
| fill ve fill\_n | Belirli bir aralığı bir değerle doldurur. |
| find | Bir aralıkta bir değer için arama yapar arar ve elemanın ilk geçtiği yeri gösteren bir tekrarlayıcı geri döndürür. |
| find\_end | Bir değerin bir aralıktaki en son konumunu arar ve elemanın geçtiği yeri gösteren bir tekrarlayıcı geri döndürür. |
| find\_first\_of | Bir değerin bir sıralamadaki ilk konumunu arar. |
| find\_if | Kullanıcı tanımlı bir koşulun doğru olduğu bir eleman için bir aralığı arar. |
| for\_each | Bir fonksiyonu bir aralıktaki elemanlara uygular. |
| generate ve generate\_n | Bir fonksiyonun geri döndürdüğü değerleri bir aralıktaki elemanlara atar. |
| includes | Bir dizinin başka bir dizideki tüm elemanları içerip içermediğini belirler. |
| inplace\_merge | Bir aralığı başka bir aralıkla birleştirir. Her iki aralık da artan sıra ile sıralanmalıdır.Ortaya çıkan dizi sıralı olur. |
| iter\_swap | İki tekrarlayıcı parametre ile gösterilen değerleri değiştirir. |
| lexicographical\_compare | Bir diziyi diğeriyle alfabetik olarak karşılaştırır. |
| lower\_bound | Dizide belirtilen değerden daha az olmayan ilk noktayı bulur. |
| make\_heap | Bir diziden bir yığın oluşturur. |
| max | İki değerin büyük olanını geri döndürür. |
| max\_element | Bir aralıktaki en büyük elamanı gösteren bir tekrarlayıcı geri döndürür. |
| merge | İki eleman dizisini birleştirerek üçüncü bir eleman dizisine atar. |
| min | İki değerin küçük olanını geri döndürür. |
| min\_element | Bir aralıktaki en küçük elamanı gösteren bir tekrarlayıcı geri döndürür. |
| mismatch | İki eleman dizisi elemanları arasında ilk benzemeyenleri bulur ve bu elemanların adreslerini gösteren tekrarlayıcıları geri döndürür. |
| next\_permutation | Bir eleman dizisinin bir sonraki permütasyonunu oluşturur. |
| nth\_element | Bir dizi eleman içinde, belirli bir elemandan küçük olan tüm elemanlar bu elemandan önce ve büyük tüm elemanlar ondan sonra gelecek şekilde düzenleme yapar. |
| partial\_sort | Bir aralıktaki elemanları sıralar. |
| partial\_sort\_copy | Bir aralıktaki elemanları sıralar ve sonuç dizisinin alacağı kadarını kopyalar. |
| partition | Bir dizi elemanı, belirli bir koşulun doğru değer döndürdüğü elemanlar, yanlış değer geri döndürdüğü elemanlardan önce gelecek şekilde düzenler. |
| pop\_heap | Bir yığının ilk ve sondan bir önceki elemanlarını değitirir ve yığını yeniden oluşturur. |
| prev\_permutation | Bir eleman dizisinin bir önceki permütasyonunu oluşturur. |
| push\_heap | Yığının sonuna bir eleman ekler. |
| random\_shuffle | Bir dizi elemanı rastgele seçer. |
| remove, remove\_ifremove\_copy, remove\_copy\_if | Belirli bir aralıktaki elemanları siler. |
| replace, replace\_copyreplace\_if, replace\_copy\_if | Belirli bir aralıktaki elemanları değiştirir. |
| reverse and reverse\_copy | Belirli bir aralığın sırasını değiştirir. |
| rotate ve rotate\_copy | Belirli bir aralıktaki elemanları sola kaydıdır. |
| search | Bir eleman dizisinde bir alt eleman dizisini arar. |
| search\_n | Belirtilen sayıda benzer eleman dizisini arar. |
| set\_difference | İki sıralı eleman dizisi arasındaki farkı içeren bir eleman dizisi oluşturur. |
| set\_intersection | İki sıralı eleman dizisinin kesişimini içeren bir eleman dizisi oluşturur. |
| set\_symmetric\_difference | İki sıralı eleman dizisi arasındaki simetrik farkı içeren bir eleman dizisi oluşturur. |
| set\_union | İki sıralı eleman dizisinin birleşimini içeren bir eleman dizisi oluşturur. |
| sort | Bir eleman aralığını sıralar. |
| sort\_heap | Belirli bir aralıktaki yığını sıralar. |
| stable\_partition | Bir dizi elemanı, belirli bir koşulun doğru değer döndürdüğü elemanlar, yanlış değer geri döndürdüğü elemanlardan önce gelecek şekilde düzenler.Bölümleme işlemi kararlıdır. Bu, eleman dizisinin ilişkili sıralamasının korunduğunu gösterir. |
| stable\_sort | Bir eleman aralığını sıralar. Sıralama kararlı olup, eşit elemanların yeniden düzenlenmediğini gösterir. |
| swap | İki değeri birbiri ile değitirir. |
| swap\_ranges | Bir aralıktaki elemanları birbiri ile değiştirir. |
| transform | Bir aralıktaki elemanlara bir fonksiyon çağırır ve elde edilen çıktıyı yeni bir eleman dizisine kaydeder. |
| unique ve unique\_copy | Bir aralıktaki tekrar eden elemanları devere dışı bırakır. |
| upper\_bound | Bir değerden büyük olmayan bir eleman dizisindeki son noktayı bulur. |

## Bir konteyner içinde belirli bir değere sahip veya belirli bir koşulu sağlayan eleman sayısını bulma

Bir konteyner içindeki eleman sayısını bulmak için size() fonksiyonu kullanılır. Bir konteyner içinde belli bir değere sahip eleman sayısını bulmak için count() fonksiyonunu, belli bir koşulu sağlayan eleman sayısını bulmak için ise, count\_if() fonksiyonunu kullanabiliriz. Her iki fonksiyonun genel yapısı aşağıda gösterilmektedir:

```c++
template <class InIter, class T> ptrdiff_t count(InIter start, InIter end, const T &val);
template <class InIter, class UnPred> ptrdiff_t count_if(InIter start, InIter end, UnPred pfn);


```

ptrdiff\_t: int bir değerdir.

Şimdi, oluşturulan bir vektör içinde, count() ve count\_if() fonksiyonlarını kullanarak, belli bir değere sahip eleman sayısını ve belli bir koşulu sağlayan eleman sayısını bulma işlemlerini bir örnek üzerinde incelemeye çalışalım:

Örnek

```c++
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool buyuk_dort(int id)
{
  return (id>4);
}

int main(void)
{
  // 10 elemanlı bir int vektör bildirimi yapar.
  vector<int> iv = { 1, 2, 3, 3, 4, 4, 4, 5, 6, 7 }; // C++11
  int id;

  // Vektör içeriğini ekrana yazma
  cout << "Vektör içeriği: ";
  for(id=0; id<(int)iv.size(); id++) cout << iv[id] << " ";

  cout << endl;

  // iv vektörünün eleman sayısını yazar.
  cout << "iv vektör eleman sayısı: " << iv.size() << endl;

  // Vektördeki belirli değere sahip eleman sayısını ekrana yazma
  cout << "Vektörde 3 değerine sahip eleman sayısı: " << count(iv.begin(), iv.end(), 3) << "\n";
  cout << "Vektörde 4 değerine sahip eleman sayısı: " << count(iv.begin(), iv.end(), 4) << "\n";

  // Vektörde 4'den büyük değere sahip eleman sayısını ekrana yazma
  cout << "Vektörde 4'den büyük değere sahip eleman sayısı: " << count_if(iv.begin(), iv.end(), buyuk_dort);

  return 0;
}


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Vektör içeriği: 1 2 3 3 4 4 4 5 6 7 
iv vektör eleman sayısı: 10
Vektörde 3 değerine sahip eleman sayısı: 2
Vektörde 4 değerine sahip eleman sayısı: 3
Vektörde 4'den büyük değere sahip eleman sayısı: 3

```
