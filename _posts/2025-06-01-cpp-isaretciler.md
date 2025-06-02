---
layout: post
title: C++ İşaretçiler (Pointers)
categories:
  - Program
tags:
  - cpp
  - c
  - pointer
  - işaretçi
  - bellek
  - dizi
---

İşaretçiler, C++ programlamada bellekteki diğer değişkenlerin adreslerini tutan özel değişkenlerdir. Bellek yönetimi, dinamik veri yapıları oluşturma ve fonksiyonlara argümanları referans yoluyla geçirme gibi birçok güçlü programlama tekniği için temel teşkil ederler.

## İşaretçi Nedir?

Bir işaretçi, bir veri türünün bellekteki konumunu (adresini) saklar. Bir değişkenin adresini bir işaretçide sakladığınızda, o işaretçi o değişkene "işaret eder".

## İşaretçi Tanımlama

Bir işaretçi, işaret edeceği veri türü ve ardından bir yıldız işareti (`*`) ile tanımlanır.

```cpp
int main() {
    int sayi = 10;
    int *ptr; // Bir integer işaretçisi tanımlama

    ptr = &sayi; // 'sayi' değişkeninin adresini 'ptr' işaretçisine atama

    return 0;
}
```

Yukarıdaki örnekte:

- `int sayi = 10;`: `sayi` adında bir integer değişkeni oluşturulur ve 10 değeri atanır.
- `int *ptr;`: `ptr` adında, bir integer değerinin adresini tutabilen bir işaretçi tanımlanır.
- `ptr = &sayi;`: `&` (adres operatörü) `sayi` değişkeninin bellek adresini alır ve bu adres `ptr` işaretçisine atanır. Artık `ptr`, `sayi` değişkenini işaret etmektedir.

## Adres Operatörü (`&`)

Adres operatörü (`&`), bir değişkenin bellekteki adresini döndürür.

```cpp
#include <iostream>

int main() {
    int sayi = 25;
    std::cout << "sayi değişkeninin değeri: " << sayi << std::endl;
    std::cout << "sayi değişkeninin bellek adresi: " << &sayi << std::endl; // &sayi, sayi'nin adresini verir

    int *ptr = &sayi;
    std::cout << "ptr işaretçisinin tuttuğu adres: " << ptr << std::endl;
    std::cout << "ptr işaretçisinin kendi bellek adresi: " << &ptr << std::endl; // İşaretçinin kendisi de bellekte bir yer tutar

    return 0;
}
```

## Dereferans Operatörü (`*`)

Dereferans operatörü (`*`), bir işaretçinin işaret ettiği adresteki değeri almak için kullanılır. "İçerik operatörü" olarak da bilinir.

```cpp
#include <iostream>

int main() {
    int sayi = 50;
    int *ptr = &sayi; // ptr, sayi'yi işaret ediyor

    std::cout << "sayi değişkeninin değeri (doğrudan): " << sayi << std::endl;
    std::cout << "ptr işaretçisinin tuttuğu adres: " << ptr << std::endl;
    std::cout << "ptr işaretçisinin işaret ettiği değer (*ptr): " << *ptr << std::endl; // *ptr, sayi'nin değerini verir

    *ptr = 100; // İşaretçi aracılığıyla 'sayi' değişkeninin değerini değiştirme
    std::cout << "Değişiklik sonrası sayi değişkeninin değeri: " << sayi << std::endl;
    std::cout << "Değişiklik sonrası *ptr: " << *ptr << std::endl;

    return 0;
}
```

Bu örnekte, `*ptr = 100;` ifadesi, `ptr`'nin işaret ettiği bellek konumundaki (yani `sayi` değişkeninin) değeri 100 olarak değiştirir.

## İşaretçi Aritmetiği

İşaretçiler üzerinde toplama ve çıkarma gibi aritmetik işlemler yapılabilir. Bir işaretçiye bir tam sayı eklediğinizde, işaretçi bellek adresini işaret ettiği veri türünün boyutu kadar artırır.

```cpp
#include <iostream>

int main() {
    int rakamlar[] = {10, 20, 30, 40, 50};
    int *ptr = rakamlar; // Dizinin ilk elemanını işaret eder (rakamlar == &rakamlar[0])

    std::cout << "İlk eleman: " << *ptr << std::endl; // 10

    ptr++; // İşaretçiyi bir sonraki integer adresine ilerlet
    std::cout << "İkinci eleman: " << *ptr << std::endl; // 20

    ptr = ptr + 2; // İşaretçiyi iki integer adresi daha ilerlet (mevcut konumdan)
    std::cout << "Dördüncü eleman (aslında): " << *ptr << std::endl; // 40 (20'den 2 ileri)

    return 0;
}
```

**Not:** İşaretçi aritmetiği dikkatli kullanılmalıdır, çünkü dizinin sınırlarının dışına çıkmak tanımsız davranışlara yol açabilir.

## İşaretçiler ve Diziler

Dizi isimleri, aslında dizinin ilk elemanının adresini tutan sabit bir işaretçi gibi davranır.

```cpp
#include <iostream>

int main() {
    int notlar[3] = {85, 90, 78};

    std::cout << "notlar[0] değeri: " << notlar[0] << std::endl;
    std::cout << "*notlar değeri: " << *notlar << std::endl; // notlar[0] ile aynı

    std::cout << "notlar[1] değeri: " << notlar[1] << std::endl;
    std::cout << "*(notlar + 1) değeri: " << *(notlar + 1) << std::endl; // notlar[1] ile aynı

    int *ptr = notlar; // ptr, notlar[0]'ı işaret eder
    std::cout << "ptr[2] değeri: " << ptr[2] << std::endl; // notlar[2] ile aynı (78)
    std::cout << "*(ptr + 2) değeri: " << *(ptr + 2) << std::endl; // notlar[2] ile aynı (78)

    return 0;
}
```

## Null İşaretçiler

Bir işaretçinin hiçbir şeyi işaret etmediğini belirtmek için ona `nullptr` (C++11 ve sonrası) veya `NULL` (eski C/C++ standardı) değeri atanabilir. Bir işaretçiyi dereferans etmeden önce null olup olmadığını kontrol etmek iyi bir pratiktir.

```cpp
#include <iostream>

int main() {
    int *ptr1 = nullptr; // C++11 ve sonrası için tercih edilen yöntem
    int *ptr2 = NULL;    // Eski yöntem

    if (ptr1 == nullptr) {
        std::cout << "ptr1 bir null işaretçidir." << std::endl;
    }

    // Null bir işaretçiyi dereferans etmek tanımsız davranışa (genellikle çökme) yol açar.
    // std::cout << *ptr1 << std::endl; // BU SATIR PROGRAMI ÇÖKERTEBİLİR!

    int x = 10;
    ptr1 = &x; // Şimdi ptr1 geçerli bir adresi işaret ediyor.
    if (ptr1 != nullptr) {
        std::cout << "ptr1'in işaret ettiği değer: " << *ptr1 << std::endl;
    }

    return 0;
}
```

## Dinamik Bellek Yönetimi (`new` ve `delete`)

Programın çalışma zamanında bellek ayırmak için `new` operatörü ve ayrılan belleği serbest bırakmak için `delete` operatörü kullanılır. Bu işlemler genellikle işaretçilerle yapılır.

### Tek Değişken İçin Dinamik Bellek

```cpp
#include <iostream>

int main() {
    int *ptr = nullptr;
    ptr = new int; // Bir integer için dinamik olarak bellek ayır

    if (ptr == nullptr) {
        std::cout << "Bellek ayrılamadı!" << std::endl;
        return 1; // Hata koduyla çık
    }

    *ptr = 2024; // Ayrılan belleğe değer ata
    std::cout << "Dinamik olarak ayrılan değer: " << *ptr << std::endl;

    delete ptr; // Ayrılan belleği serbest bırak
    ptr = nullptr; // İyi bir pratik: serbest bırakılan işaretçiyi null yap

    // delete ptr; // Aynı belleği iki kez silmek hataya yol açar!
    // *ptr = 10; // Serbest bırakılmış belleğe erişim tanımsız davranış!

    return 0;
}
```

### Dizi İçin Dinamik Bellek

```cpp
#include <iostream>

int main() {
    int boyut;
    std::cout << "Dizi boyutunu girin: ";
    std::cin >> boyut;

    if (boyut <= 0) {
        std::cout << "Geçersiz boyut." << std::endl;
        return 1;
    }

    int *dizi_ptr = nullptr;
    dizi_ptr = new int[boyut]; // 'boyut' elemanlı bir integer dizisi için dinamik bellek ayır

    if (dizi_ptr == nullptr) {
        std::cout << "Bellek ayrılamadı!" << std::endl;
        return 1;
    }

    // Diziye değerler ata
    for (int i = 0; i < boyut; ++i) {
        dizi_ptr[i] = (i + 1) * 10;
    }

    // Diziyi yazdır
    std::cout << "Dinamik dizi elemanları: ";
    for (int i = 0; i < boyut; ++i) {
        std::cout << dizi_ptr[i] << " ";
    }
    std::cout << std::endl;

    delete[] dizi_ptr; // Dinamik olarak ayrılan diziyi serbest bırak (köşeli parantezlere dikkat!)
    dizi_ptr = nullptr;

    return 0;
}
```

**Önemli Not:** `new` ile ayrılan her bellek bloğu, karşılık gelen `delete` (tekil öğe için) veya `delete[]` (dizi için) ile serbest bırakılmalıdır. Aksi takdirde **bellek sızıntıları** (memory leaks) meydana gelir ve programınız zamanla gereksiz yere fazla bellek tüketebilir.

## Kapsamlı Örnek Kod

Aşağıda, yukarıda bahsedilen birçok kavramı bir araya getiren bir C++ programı bulunmaktadır:

```cpp
#include <iostream> // Giriş/çıkış işlemleri için
#include <string>   // String işlemleri için (dinamik bellek örneğinde kullanılabilir)

// Fonksiyon prototipi (işaretçi argümanı alıyor)
void degeriArtir(int *sayi_ptr) {
    if (sayi_ptr != nullptr) {
        (*sayi_ptr)++; // İşaretçinin gösterdiği değeri bir artır
    }
}

// Fonksiyon prototipi (işaretçi döndürüyor)
int* maksimumBul(int *a, int *b) {
    if (a == nullptr || b == nullptr) return nullptr;
    if (*a > *b) {
        return a;
    } else {
        return b;
    }
}

int main() {
    // Temel İşaretçi İşlemleri
    int var = 20;
    int *ptr_var; // Integer işaretçisi

    ptr_var = &var; // var'ın adresini ptr_var'a ata

    std::cout << "--- Temel İşaretçi İşlemleri ---" << std::endl;
    std::cout << "var değişkeninin değeri: " << var << std::endl;
    std::cout << "var değişkeninin adresi (&var): " << &var << std::endl;
    std::cout << "ptr_var işaretçisinin tuttuğu adres: " << ptr_var << std::endl;
    std::cout << "ptr_var'ın işaret ettiği değer (*ptr_var): " << *ptr_var << std::endl;

    *ptr_var = 30; // İşaretçi aracılığıyla var'ın değerini değiştir
    std::cout << "Değişiklik sonrası var'ın değeri: " << var << std::endl;
    std::cout << std::endl;

    // İşaretçiler ve Diziler
    std::cout << "--- İşaretçiler ve Diziler ---" << std::endl;
    int dizi[] = {100, 200, 300};
    int *ptr_dizi = dizi; // Dizinin ilk elemanını işaret et (dizi == &dizi[0])

    std::cout << "Dizinin ilk elemanı (*ptr_dizi): " << *ptr_dizi << std::endl;
    std::cout << "Dizinin ikinci elemanı (*(ptr_dizi + 1)): " << *(ptr_dizi + 1) << std::endl;
    std::cout << "Dizinin üçüncü elemanı (ptr_dizi[2]): " << ptr_dizi[2] << std::endl;
    std::cout << std::endl;

    // İşaretçiler ve Fonksiyonlar
    std::cout << "--- İşaretçiler ve Fonksiyonlar ---" << std::endl;
    int sayi = 5;
    std::cout << "Fonksiyondan önce sayi: " << sayi << std::endl;
    degeriArtir(&sayi); // sayi'nin adresini fonksiyona gönder
    std::cout << "Fonksiyondan sonra sayi: " << sayi << std::endl;

    int val1 = 10, val2 = 20;
    int *maks_ptr = maksimumBul(&val1, &val2);
    if (maks_ptr != nullptr) {
        std::cout << "Maksimum değer: " << *maks_ptr << std::endl;
    }
    std::cout << std::endl;

    // Null İşaretçi
    std::cout << "--- Null İşaretçi ---" << std::endl;
    int *null_ornek_ptr = nullptr;
    if (null_ornek_ptr == nullptr) {
        std::cout << "null_ornek_ptr şu anda null." << std::endl;
    }
    // *null_ornek_ptr = 5; // HATA! Null işaretçiyi dereferans etme.

    null_ornek_ptr = &var; // Şimdi geçerli bir adresi işaret ediyor.
    std::cout << "null_ornek_ptr şimdi var'ı işaret ediyor, değeri: " << *null_ornek_ptr << std::endl;
    std::cout << std::endl;

    // Dinamik Bellek Yönetimi (Tek Değişken)
    std::cout << "--- Dinamik Bellek (Tek Değişken) ---" << std::endl;
    int *dinamik_sayi_ptr = new int; // Dinamik olarak bir integer için bellek ayır
    if (dinamik_sayi_ptr == nullptr) {
        std::cerr << "Tek değişken için bellek ayrılamadı!" << std::endl;
        return 1;
    }
    *dinamik_sayi_ptr = 77;
    std::cout << "Dinamik olarak ayrılan sayi: " << *dinamik_sayi_ptr << std::endl;
    delete dinamik_sayi_ptr; // Belleği serbest bırak
    dinamik_sayi_ptr = nullptr; // İyi pratik
    std::cout << std::endl;

    // Dinamik Bellek Yönetimi (Dizi)
    std::cout << "--- Dinamik Bellek (Dizi) ---" << std::endl;
    int dizi_boyutu = 3;
    int *dinamik_dizi_ptr = new int[dizi_boyutu]; // Dinamik olarak bir integer dizisi için bellek ayır
    if (dinamik_dizi_ptr == nullptr) {
        std::cerr << "Dizi için bellek ayrılamadı!" << std::endl;
        return 1;
    }

    dinamik_dizi_ptr[0] = 11;
    dinamik_dizi_ptr[1] = 22;
    dinamik_dizi_ptr[2] = 33;

    std::cout << "Dinamik dizi elemanları: ";
    for (int i = 0; i < dizi_boyutu; ++i) {
        std::cout << dinamik_dizi_ptr[i] << " ";
    }
    std::cout << std::endl;

    delete[] dinamik_dizi_ptr; // Dizi için ayrılan belleği serbest bırak
    dinamik_dizi_ptr = nullptr; // İyi pratik
    std::cout << std::endl;

    std::cout << "Program başarıyla tamamlandı." << std::endl;

    return 0; // Başarılı çıkış
}
```

Bu kapsamlı örnek, işaretçilerin C++'da nasıl kullanıldığına dair temel ve bazı ileri düzey kavramları göstermektedir. İşaretçiler güçlü araçlardır ancak dikkatli kullanılmaları gerekir; yanlış kullanımları (örneğin, null bir işaretçiyi dereferans etmek veya belleği serbest bırakmayı unutmak) programın çökmesine veya bellek sızıntılarına yol açabilir.
