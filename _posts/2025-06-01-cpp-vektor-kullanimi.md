---
layout: post
title: C++ Programlama Dilinde Vektör Kullanımı
categories:
  - Program
tags:
  - cpp
  - vektör
  - stl
  - veri yapıları
  - programlama
  - dizi
  - dinamik dizi
redirect_from:
  - /posts/cpp-vektor-kullanimi/
---

Bu yazıda, C++ Standart Kütüphanesi'nin (STL - Standard Template Library) en güçlü ve sık kullanılan veri yapılarından biri olan **vektörleri (vectors)** detaylı bir şekilde inceleyeceğiz. Vektörler, C++ programcılarına dinamik boyutlu dizilerle çalışma imkanı sunarak bellek yönetimi ve veri depolama konularında büyük kolaylık sağlar. Gelin, vektörlerin ne olduğuna, nasıl kullanıldığına ve geleneksel C-stili dizilere göre avantajlarına birlikte göz atalım.

## Vektör Nedir?

C++'ta `std::vector`, elemanları aynı türden olan ve dinamik olarak yeniden boyutlandırılabilen bir dizi konteyneridir. Geleneksel C dizilerinin aksine, bir vektörün boyutu çalışma zamanında (runtime) artırılabilir veya azaltılabilir. Bu, programın ihtiyaçlarına göre esnek bir şekilde veri saklamamıza olanak tanır. Vektörler, bellek yönetimini kendileri üstlenirler, bu da programcıyı manuel bellek ayırma ve serbest bırakma zahmetinden kurtarır.

Vektörler, `vector` başlık dosyası (`#include <vector>`) altında tanımlanmıştır ve `std` isim alanı (namespace) içinde bulunurlar.

## Neden Vektör Kullanmalıyız?

Geleneksel C-stili dizilere kıyasla vektörlerin birçok avantajı vardır:

**Dinamik Boyutlandırma:** En önemli avantajıdır. Dizilerin boyutu derleme zamanında sabitken, vektörlerin boyutu çalışma zamanında değişebilir.

**Otomatik Bellek Yönetimi:** Vektörler, elemanlar eklendikçe veya çıkarıldıkça belleği otomatik olarak yönetir. Bu, `new` ve `delete` (veya `malloc` ve `free`) ile manuel bellek yönetimi ihtiyacını azaltır ve bellek sızıntıları (memory leaks) gibi hataların önüne geçer.

**Zengin Fonksiyon Seti:** Vektörler, eleman ekleme, silme, boyut sorgulama, kapasite yönetimi gibi birçok kullanışlı üye fonksiyona sahiptir.

**Güvenlik:** `at()` fonksiyonu ile sınırlı erişim kontrolü sağlayarak dizi sınırlarının aşılması (out-of-bounds access) durumunda istisna fırlatır.

**STL Algoritmaları ile Uyumluluk:** Vektörler, STL'deki sıralama, arama, dönüştürme gibi birçok algoritma ile sorunsuz bir şekilde kullanılabilir.

## Vektörlerin Temel Kullanımı

Şimdi vektörlerin C++ kodunda nasıl kullanıldığına dair temel adımlara bakalım.

### 1. Vektör Kütüphanesini Dahil Etme ve İsim Alanı

Bir vektör kullanmadan önce, programınıza `vector` başlık dosyasını dahil etmeniz gerekir:

```cpp
#include <vector>
```

`std` isim alanındaki `vector` ve diğer STL bileşenlerini daha kısa kullanmak için `using namespace std;` ifadesini programınızın başına (genellikle `#include` direktiflerinden sonra) ekleyebilirsiniz. Bu, her `vector` kullanımında `std::vector` yazmak yerine doğrudan `vector` yazmanıza olanak tanır.

```cpp
#include <vector>
#include <iostream> // Çıktı işlemleri için
#include <string>   // String işlemleri için

// std isim alanını kullanacağımızı belirtiyoruz
using namespace std;
```

**Not:** Büyük projelerde veya başlık dosyalarında (.h) `using namespace std;` kullanımı, isim çakışmalarına yol açabileceği için genellikle önerilmez. Ancak .cpp dosyalarında veya bu gibi örneklerde kodun okunabilirliğini artırmak için kullanılabilir.

### 2. Vektör Tanımlama ve Başlatma

Vektörler farklı şekillerde tanımlanabilir ve başlatılabilir:

```cpp
#include <vector>
#include <iostream>
#include <string>

using namespace std;

int main() {
    // Boş bir integer vektörü tanımlama
    vector<int> sayilar;

    // Belirli bir boyutta (örneğin 5 elemanlı) ve varsayılan değerlerle (int için 0) başlatılmış bir vektör
    vector<int> sayilar_boyutlu(5); // [0, 0, 0, 0, 0]

    // Belirli bir boyutta ve belirli bir başlangıç değeriyle (örneğin 3 elemanlı, hepsi 10) başlatılmış bir vektör
    vector<int> sayilar_degerli(3, 10); // [10, 10, 10]

    // Başlatıcı listesi (initializer list) ile vektör tanımlama (C++11 ve sonrası)
    vector<int> sayilar_liste = {1, 2, 3, 4, 5};
    vector<string> kelimeler = {"merhaba", "dünya", "vektör"};

    // Başka bir vektörden kopyalayarak yeni bir vektör oluşturma
    vector<int> sayilar_kopya = sayilar_liste;

    // Örnek bir vektörün elemanlarını yazdırma
    cout << "sayilar_liste elemanları: ";
    for (int sayi : sayilar_liste) {
        cout << sayi << " ";
    }
    cout << endl;

    cout << "sayilar_degerli elemanları: ";
    for (int sayi : sayilar_degerli) {
        cout << sayi << " ";
    }
    cout << endl;

    return 0;
}
```

### 3. Vektöre Eleman Ekleme

Vektörlere eleman eklemenin en yaygın yolu `push_back()` fonksiyonudur. Bu fonksiyon, vektörün sonuna yeni bir eleman ekler.

```cpp
#include <vector>
#include <iostream>

using namespace std;

int main() {
    vector<int> v;
    v.push_back(10); // v: [10]
    v.push_back(20); // v: [10, 20]
    v.push_back(30); // v: [10, 20, 30]

    cout << "v elemanları: ";
    for (int eleman : v) {
        cout << eleman << " ";
    }
    cout << endl; // Çıktı: v elemanları: 10 20 30 

    return 0;
}
```

C++11 ile gelen `emplace_back()` fonksiyonu ise elemanı doğrudan vektörün içinde oluşturarak (in-place construction) bazı durumlarda `push_back()`'e göre daha verimli olabilir. Özellikle karmaşık nesnelerle çalışırken bu fark belirginleşebilir.

```cpp
#include <vector>
#include <iostream>
#include <string>
#include <utility> // pair için

using namespace std;

int main() {
    vector<pair<int, string>> veriler;
    // pair nesnesini doğrudan vektör içinde oluşturur
    veriler.emplace_back(1, "bir"); 
    veriler.emplace_back(2, "iki");

    cout << "Veriler:" << endl;
    for (const auto& p : veriler) {
        cout << "{" << p.first << ", \"" << p.second << "\"}" << endl;
    }
    // Çıktı:
    // Veriler:
    // {1, "bir"}
    // {2, "iki"}

    return 0;
}
```

### 4. Vektör Elemanlarına Erişme

Vektör elemanlarına birkaç farklı yolla erişilebilir:

#### `[]` Operatörü

Dizi benzeri erişim sağlar. Ancak sınır kontrolü yapmaz. Geçersiz bir indekse erişmeye çalışmak tanımsız davranışa (undefined behavior) yol açabilir.

```cpp
#include <vector>
#include <iostream>

using namespace std;

int main() {
    vector<int> sayilar = {10, 20, 30};
    cout << "İlk eleman: " << sayilar[0] << endl; // Çıktı: İlk eleman: 10
    sayilar[1] = 25;         // sayilar: [10, 25, 30]
    cout << "Değiştirilmiş ikinci eleman: " << sayilar[1] << endl; // Çıktı: Değiştirilmiş ikinci eleman: 25
    return 0;
}
```

#### `at()` Fonksiyonu

`[]` operatörüne benzer şekilde elemana erişir, ancak ek olarak sınır kontrolü yapar. Eğer geçersiz bir indekse erişilmeye çalışılırsa `std::out_of_range` türünde bir istisna fırlatır. Bu, daha güvenli bir erişim yöntemidir.

```cpp
#include <vector>
#include <iostream>
#include <stdexcept> // out_of_range için

using namespace std;

int main() {
    vector<int> sayilar = {10, 20, 30};
    cout << "İlk eleman (at ile): " << sayilar.at(0) << endl; // Çıktı: İlk eleman (at ile): 10
    try {
        cout << sayilar.at(5) << endl; // Olmayan bir indeks
    } catch (const out_of_range& oor) {
        cerr << "Hata: Sınır dışı erişim! " << oor.what() << endl;
    }
    return 0;
}
```

#### `front()` Fonksiyonu

Vektörün ilk elemanına referans döndürür. Vektör boş olmamalıdır.

```cpp
#include <vector>
#include <iostream>

using namespace std;

int main() {
    vector<int> sayilar = {10, 20, 30};
    if (!sayilar.empty()) {
        cout << "İlk eleman (front): " << sayilar.front() << endl; // Çıktı: İlk eleman (front): 10
    }
    return 0;
}
```

#### `back()` Fonksiyonu

Vektörün son elemanına referans döndürür. Vektör boş olmamalıdır.

```cpp
#include <vector>
#include <iostream>

using namespace std;

int main() {
    vector<int> sayilar = {10, 20, 30};
    if (!sayilar.empty()) {
        cout << "Son eleman (back): " << sayilar.back() << endl; // Çıktı: Son eleman (back): 30
    }
    return 0;
}
```

### 5. Vektör Boyutunu ve Kapasitesini Öğrenme

#### `size()`

Vektördeki mevcut eleman sayısını döndürür.

```cpp
#include <vector>
#include <iostream>

using namespace std;

int main() {
    vector<int> v = {1, 2, 3};
    cout << "Boyut: " << v.size() << endl; // Çıktı: Boyut: 3
    return 0;
}
```

#### `empty()`

Vektörün boş olup olmadığını kontrol eder. Boşsa `true`, değilse `false` döndürür.

```cpp
#include <vector>
#include <iostream>

using namespace std;

int main() {
    vector<int> v_dolu = {1, 2, 3};
    vector<int> v_bos;
    if (v_dolu.empty()) {
        cout << "v_dolu boş." << endl;
    } else {
        cout << "v_dolu'da " << v_dolu.size() << " eleman var." << endl; // Çıktı: v_dolu'da 3 eleman var.
    }
    if (v_bos.empty()) {
        cout << "v_bos boş." << endl; // Çıktı: v_bos boş.
    }
    return 0;
}
```

#### `capacity()`

Vektörün, yeniden bellek ayırmadan (reallocation) depolayabileceği maksimum eleman sayısını döndürür. Kapasite genellikle boyuttan büyük veya eşittir.

```cpp
#include <vector>
#include <iostream>

using namespace std;

int main() {
    vector<int> v_kapasite;
    cout << "Başlangıç Kapasitesi: " << v_kapasite.capacity() << endl;
    for (int i = 0; i < 10; ++i) {
        v_kapasite.push_back(i);
        cout << "Boyut: " << v_kapasite.size() << ", Kapasite: " << v_kapasite.capacity() << endl;
    }
    return 0;
}
```

`push_back` ile eleman eklendiğinde, eğer mevcut kapasite yetersiz kalırsa, vektör genellikle kapasitesini (örneğin iki katına) artırır. Bu, yeni bir bellek bloğu ayırmayı ve mevcut elemanları yeni alana kopyalamayı içerir, bu da maliyetli bir işlem olabilir.

#### `reserve()`

Vektörün kapasitesini belirli bir değere yükseltmek için kullanılır. Eğer sık sık eleman ekleneceği biliniyorsa, baştan yeterli kapasite ayırmak performansı artırabilir, çünkü sürekli yeniden bellek ayırma işlemlerinin önüne geçilir.

```cpp
#include <vector>
#include <iostream>

using namespace std;

int main() {
    vector<int> v_reserve;
    v_reserve.reserve(100); // En az 100 elemanlık kapasite ayır
    cout << "Reserve sonrası Kapasite: " << v_reserve.capacity() << endl; // Genellikle 100 veya daha fazla
    return 0;
}
```

#### `shrink_to_fit()` (C++11)

Vektörün kapasitesini, mevcut eleman sayısına (`size()`) düşürmek için bir istekte bulunur. Bu, gereksiz bellek kullanımını azaltabilir ancak her zaman kapasitenin küçüleceği garanti edilmez (kütüphane implementasyonuna bağlıdır).

```cpp
#include <vector>
#include <iostream>

using namespace std;

int main() {
    vector<int> v_shrink;
    v_shrink.reserve(100); // Önce büyük bir kapasite ayıralım
    v_shrink.push_back(1);
    v_shrink.push_back(2);
    cout << "Shrink öncesi Boyut: " << v_shrink.size() << ", Kapasite: " << v_shrink.capacity() << endl;
    v_shrink.shrink_to_fit();
    cout << "Shrink sonrası Boyut: " << v_shrink.size() << ", Kapasite: " << v_shrink.capacity() << endl;
    return 0;
}
```

### 6. Vektör Elemanları Üzerinde Gezinme (Iterating)

Vektör elemanları üzerinde gezinmek için birkaç yöntem vardır:

#### İndeks Tabanlı for Döngüsü

```cpp
#include <vector>
#include <iostream>

using namespace std;

int main() {
    vector<int> sayilar = {10, 20, 30, 40};
    cout << "İndeks tabanlı döngü: ";
    for (size_t i = 0; i < sayilar.size(); ++i) {
        cout << sayilar[i] << " ";
    }
    cout << endl; // Çıktı: İndeks tabanlı döngü: 10 20 30 40 
    return 0;
}
```

#### İteratörler (Iterators) ile for Döngüsü

İteratörler, konteyner elemanlarına işaretçi benzeri erişim sağlayan nesnelerdir. `begin()` fonksiyonu ilk elemana işaret eden bir iteratör, `end()` fonksiyonu ise son elemandan sonraki konuma işaret eden bir iteratör döndürür.

```cpp
#include <vector>
#include <iostream>

using namespace std;

int main() {
    vector<int> sayilar = {10, 20, 30, 40};
    cout << "İteratörlü döngü (klasik): ";
    for (vector<int>::iterator it = sayilar.begin(); it != sayilar.end(); ++it) {
        cout << *it << " "; // *it ile iteratörün işaret ettiği değere erişilir
    }
    cout << endl; // Çıktı: İteratörlü döngü (klasik): 10 20 30 40 

    // auto anahtar kelimesi ile daha kısa yazım (C++11)
    cout << "İteratörlü döngü (auto): ";
    for (auto it = sayilar.begin(); it != sayilar.end(); ++it) {
        cout << *it << " ";
    }
    cout << endl; // Çıktı: İteratörlü döngü (auto): 10 20 30 40 
    return 0;
}
```

#### Aralık Tabanlı for Döngüsü (Range-based for loop - C++11)

En modern ve genellikle en okunaklı yöntemdir.

```cpp
#include <vector>
#include <iostream>

using namespace std;

int main() {
    vector<int> sayilar = {10, 20, 30, 40};
    cout << "Aralık tabanlı döngü: ";
    for (int sayi : sayilar) {
        cout << sayi << " ";
    }
    cout << endl; // Çıktı: Aralık tabanlı döngü: 10 20 30 40 

    // Elemanları değiştirmek için referans kullanılabilir:
    cout << "Değiştirilmiş (referans ile): ";
    for (int &sayi : sayilar) {
        sayi *= 2; // Her elemanı iki katına çıkar
    }
    for (int sayi : sayilar) {
        cout << sayi << " ";
    }
    cout << endl; // Çıktı: Değiştirilmiş (referans ile): 20 40 60 80 
    return 0;
}
```

## Vektörleri Değiştirme

### 1. Eleman Silme

#### `pop_back()`

Vektörün son elemanını siler. Vektör boşsa bu fonksiyonu çağırmak tanımsız davranışa yol açar.

```cpp
#include <vector>
#include <iostream>

using namespace std;

int main() {
    vector<int> v = {1, 2, 3, 4};
    cout << "pop_back öncesi: ";
    for(int x : v) cout << x << " ";
    cout << endl;

    if (!v.empty()) {
        v.pop_back(); 
    }

    cout << "pop_back sonrası: ";
    for(int x : v) cout << x << " "; // v: [1, 2, 3]
    cout << endl;
    return 0;
}
```

#### `erase()`

Belirli bir pozisyondaki veya belirli bir aralıktaki elemanları siler. İteratörler alır.

```cpp
#include <vector>
#include <iostream>

using namespace std;

void print_vec(const vector<int>& vec, const string& msg) {
    cout << msg;
    for (int x : vec) cout << x << " ";
    cout << endl;
}

int main() {
    vector<int> v_erase = {10, 20, 30, 40, 50};
    print_vec(v_erase, "Başlangıç: ");

    // Tek bir elemanı silme (örneğin ikinci elemanı, indeksi 1 olan)
    if (v_erase.size() > 1) {
        v_erase.erase(v_erase.begin() + 1); 
        print_vec(v_erase, "İkinci eleman silindi: "); // v_erase: [10, 30, 40, 50]
    }

    // Bir aralıktaki elemanları silme (örneğin yeni ikinci elemandan (30) üçüncü elemana (40) kadar)
    // v_erase.begin() + 1, ikinci elemanı işaret eder (30)
    // v_erase.begin() + 3, dördüncü elemanı işaret eder (50). erase son iteratörü dahil etmez.
    // Yani [v_erase.begin() + 1, v_erase.begin() + 3) aralığı silinir.
    if (v_erase.size() >= 3) {
         // Şu an v_erase: [10, 30, 40, 50]
         // Silinecek aralık: 30, 40 (indeks 1 ve 2)
        v_erase.erase(v_erase.begin() + 1, v_erase.begin() + 3); 
        print_vec(v_erase, "Aralık silindi: "); // v_erase: [10, 50]
    }
    return 0;
}
```

`erase()` fonksiyonu, silinen elemandan sonraki elemanın iteratörünü döndürür. Bu, döngü içinde eleman silerken kullanışlıdır.

#### `clear()`

Vektördeki tüm elemanları siler. Boyut 0 olur, ancak kapasite genellikle değişmez.

```cpp
#include <vector>
#include <iostream>

using namespace std;

int main() {
    vector<int> v_clear = {1, 2, 3};
    cout << "Clear öncesi boyut: " << v_clear.size() << ", Kapasite: " << v_clear.capacity() << endl;
    v_clear.clear();
    cout << "Clear sonrası boyut: " << v_clear.size() << endl; // Çıktı: 0
    cout << "Clear sonrası Kapasite: " << v_clear.capacity() << endl; // Kapasite genellikle aynı kalır
    return 0;
}
```

### 2. Eleman Ekleme (Araya)

#### `insert()`

Vektörün belirli bir pozisyonuna bir veya daha fazla eleman ekler. İteratörler alır.

```cpp
#include <vector>
#include <iostream>

using namespace std;

void print_vec_insert(const vector<int>& vec, const string& msg) {
    cout << msg;
    for (int x : vec) cout << x << " ";
    cout << endl;
}

int main() {
    vector<int> v_insert = {10, 20, 40, 50};
    print_vec_insert(v_insert, "Başlangıç: ");

    // Tek bir eleman ekleme (üçüncü pozisyona (indeks 2) 30 ekle)
    v_insert.insert(v_insert.begin() + 2, 30); 
    print_vec_insert(v_insert, "30 eklendi: "); // v_insert: [10, 20, 30, 40, 50]

    // Birden fazla aynı elemanı ekleme (ilk pozisyona 3 tane 5 ekle)
    v_insert.insert(v_insert.begin(), 3, 5); 
    print_vec_insert(v_insert, "Başa 3 tane 5 eklendi: "); // v_insert: [5, 5, 5, 10, 20, 30, 40, 50]

    // Başka bir konteynırdan eleman aralığı ekleme
    vector<int> eklenecekler = {100, 200};
    v_insert.insert(v_insert.end(), eklenecekler.begin(), eklenecekler.end());
    print_vec_insert(v_insert, "Sona {100, 200} eklendi: "); 
    // v_insert: [5, 5, 5, 10, 20, 30, 40, 50, 100, 200]
    return 0;
}
```

`insert()` fonksiyonu, eklenen ilk elemanın iteratörünü döndürür.

#### `emplace()` (C++11)

`insert()` gibi belirli bir pozisyona eleman ekler, ancak elemanı doğrudan vektör içinde oluşturur (in-place construction), bu da `insert()`'e göre daha verimli olabilir.

```cpp
#include <vector>
#include <iostream>
#include <string> // pair için
#include <utility>

using namespace std;

int main() {
    vector<pair<int, char>> v_emplace;
    // İlk pozisyona {1, 'a'} çiftini oluşturur
    auto it = v_emplace.emplace(v_emplace.begin(), 1, 'a'); 
    v_emplace.emplace(it, 0, 'z'); // 'it'in gösterdiği yere (yeni eklenenin önüne) {0, 'z'} ekler

    cout << "v_emplace elemanları:" << endl;
    for(const auto& p : v_emplace) {
        cout << "{" << p.first << ", '" << p.second << "'}" << endl;
    }
    // Çıktı:
    // v_emplace elemanları:
    // {0, 'z'}
    // {1, 'a'}
    return 0;
}
```

### 3. Vektörü Yeniden Boyutlandırma

#### `resize()`

Vektörün boyutunu değiştirir.

- Eğer yeni boyut mevcut boyuttan büyükse, sona varsayılan değerlerle (veya belirtilen bir değerle) yeni elemanlar eklenir.
- Eğer yeni boyut mevcut boyuttan küçükse, sondaki elemanlar silinir.

```cpp
#include <vector>
#include <iostream>

using namespace std;

void print_vec_resize(const vector<int>& vec, const string& msg) {
    cout << msg;
    for (int x : vec) cout << x << " ";
    cout << endl;
}

int main() {
    vector<int> v_resize = {1, 2, 3, 4, 5};
    print_vec_resize(v_resize, "Başlangıç: ");

    v_resize.resize(8); // Yeni elemanlar 0 ile doldurulur
    print_vec_resize(v_resize, "Resize (8): "); // v_resize: [1, 2, 3, 4, 5, 0, 0, 0] 

    v_resize.resize(10, 100); // Yeni elemanlar 100 ile doldurulur
    print_vec_resize(v_resize, "Resize (10, 100): "); // v_resize: [1, 2, 3, 4, 5, 0, 0, 0, 100, 100] 

    v_resize.resize(3); // Sondaki elemanlar silinir
    print_vec_resize(v_resize, "Resize (3): "); // v_resize: [1, 2, 3] 
    return 0;
}
```

### 4. İki Vektörün İçeriğini Takas Etme

#### `swap()`
İki vektörün içeriğini verimli bir şekilde takas eder. Bu işlem genellikle çok hızlıdır çünkü sadece iç işaretçiler ve boyut/kapasite bilgileri takas edilir, elemanların kendileri kopyalanmaz.

```cpp
#include <vector>
#include <iostream>

using namespace std;

void print_vec_swap(const vector<int>& vec, const string& name) {
    cout << name << " elemanları: ";
    for (int x : vec) cout << x << " ";
    cout << endl;
}

int main() {
    vector<int> v1 = {1, 2, 3};
    vector<int> v2 = {10, 20};

    print_vec_swap(v1, "v1 (önce)");
    print_vec_swap(v2, "v2 (önce)");

    v1.swap(v2); // veya std::swap(v1, v2); (utility başlık dosyası gerekebilir)

    print_vec_swap(v1, "v1 (sonra)"); // Şimdi v1: [10, 20]
    print_vec_swap(v2, "v2 (sonra)"); // ve v2: [1, 2, 3]
    return 0;
}
```


#### Vektörler ile İlgili Bazı Diğer Yararlı Fonksiyonlar

`assign()`: Vektöre yeni içerik atar, mevcut içeriği değiştirir. Farklı şekillerde kullanılabilir:

```cpp
#include <vector>
#include <iostream>

using namespace std;

void print_vec_assign(const vector<int>& vec, const string& msg) {
    cout << msg;
    for (int x : vec) cout << x << " ";
    cout << endl;
}

int main() {
    vector<int> v_assign;
    v_assign.assign(5, 10); // v_assign: [10, 10, 10, 10, 10] (5 tane 10)
    print_vec_assign(v_assign, "assign (5, 10): ");

    vector<int> kaynak = {1, 2, 3};
    v_assign.assign(kaynak.begin(), kaynak.end()); // v_assign: [1, 2, 3]
    print_vec_assign(v_assign, "assign (kaynaktan): ");
    return 0;
}
```

`data()`: Vektörün altında yatan C-stili diziye (elemanların depolandığı bellek bloğuna) bir işaretçi döndürür. Bu, C API'leriyle etkileşimde bulunurken veya doğrudan bellek erişimi gerektiğinde kullanışlı olabilir.

```cpp
#include <vector>
#include <iostream>

using namespace std;

int main() {
    vector<int> v_data = {1, 2, 3};
    if (!v_data.empty()) {
        int* p_data = v_data.data();
        cout << "İlk eleman (data() ile): " << *p_data << endl; // Çıktı: 1
        // p_data[1] ikinci elemanı verir (2)
        cout << "İkinci eleman (data() ile): " << p_data[1] << endl; // Çıktı: 2
    }
    return 0;
}
```

Dikkat: Vektör yeniden boyutlandırıldığında (örneğin push_back kapasiteyi aşarsa veya resize, insert, erase çağrılırsa) bu işaretçi geçersiz hale gelebilir.

**Örnek Bir Uygulama**

Aşağıda, şimdiye kadar öğrendiğimiz bazı vektör işlemlerini bir arada kullanan basit bir örnek bulunmaktadır:

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm> // std::sort için

// std isim alanını kullanacağımızı belirtiyoruz
using namespace std;

void print_vector(const string& message, const vector<int>& v) {
    cout << message;
    for (int x : v) {
        cout << x << " ";
    }
    cout << endl;
}

int main() {
    // Bir integer vektörü oluştur
    vector<int> sayilarim;

    // Eleman ekle
    sayilarim.push_back(30);
    sayilarim.push_back(10);
    sayilarim.push_back(50);
    sayilarim.emplace_back(20); // C++11
    print_vector("Başlangıç vektörü: ", sayilarim); // 30 10 50 20

    // Araya eleman ekle (üçüncü pozisyona (indeks 2) 40)
    if (sayilarim.size() >= 2) { // Güvenli ekleme için kontrol
        sayilarim.insert(sayilarim.begin() + 2, 40);
    }
    print_vector("40 eklendikten sonra: ", sayilarim); // 30 10 40 50 20

    // Eleman sil (ilk elemanı)
    if (!sayilarim.empty()) {
        sayilarim.erase(sayilarim.begin());
    }
    print_vector("İlk eleman silindikten sonra: ", sayilarim); // 10 40 50 20

    // Vektörü sırala (STL algoritması kullanarak)
    sort(sayilarim.begin(), sayilarim.end());
    print_vector("Sıralandıktan sonra: ", sayilarim); // 10 20 40 50

    // Boyut ve kapasiteyi kontrol et
    cout << "Boyut: " << sayilarim.size() << endl;
    cout << "Kapasite: " << sayilarim.capacity() << endl;

    // Vektörü temizle
    sayilarim.clear();
    cout << "Temizlendikten sonra boş mu? " << (sayilarim.empty() ? "Evet" : "Hayır") << endl;

    return 0;
}
```

## Sonuç

C++'ta `std::vector`, dinamik dizilere ihtiyaç duyduğunuzda başvuracağınız temel araçlardan biridir. Sunduğu esneklik, otomatik bellek yönetimi ve zengin fonksiyon seti sayesinde hem geliştirme sürecini hızlandırır hem de daha güvenli ve bakımı kolay kodlar yazmanıza yardımcı olur. Geleneksel C-stili dizilerin yerine vektörleri tercih etmek, modern C++ programlamanın önemli bir adımıdır.
Umarım bu yazı, C++ vektörlerini anlamanıza ve projelerinizde etkin bir şekilde kullanmanıza yardımcı olmuştur. Vektörler hakkında daha fazla detay ve ileri düzey kullanımlar için C++ referansları incelenebilir.
