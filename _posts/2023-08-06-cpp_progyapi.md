---
title:  C++ Program yapısı
author: sonsuz
date: 2023-08-06 00:20:11 +0300
categories: [Program,C++]
tags: [cpp,programlama,yapı,kütüphane,sınıf,main]
---


## Bir C++ programının temel yapısı

Bir C++ programında, genel olarak aşağıda gösterilen bölümler sırayla yer alır. Başlık dosya bildiriminden sonraki sıralama değiştirilebilir. Programda mutlaka tanımlanması tek bölüm main() fonksiyonudur. Bunun dışındaki bölümlerin tanımlanması tamamen ihtiyaca bağlıdır.

* Başlık dosya bildirimleri
* Ana sınıf bildirimleri
* Ana sınıflardan türetilmiş sınıf bildirimleri
* Ana sınıf üye fonksiyon ana yapıları
* Türetilmiş sınıf üye fonksiyon ana yapıları
* Sınıf üyesi olmayan fonksiyon bildirimleri
* main() fonksiyonu
* Sınıf üyesi olmayan fonksiyon ana yapıları

Bir C++ programının temel yapısı aşağıda gösterilmektedir:

```cpp
// Başlık dosya bildirimleri
#include <başlık-dosya-adı>
.
.
.
#include <başlık-dosya-adı>

// ana-sınıf bildirimleri
class sinifana {
  private:
    ...
  protected:
    ...
  public:  
    ...
}

// türetilmiş-sınıf bildirimleri
class siniftur:sinifana {
  private:
    ...
  protected:
    ...
  public:  
    ...
}

// Sınıf üyesi fonksiyon yapıları
dönüş-değeri sinifana::fonk-adı(parametreler)
{
  işlem satırı;
  .
  .
  işlem satırı;
}

dönüş-değeri siniftur::fonk-adı(parametreler)
{
  işlem satırı;
  .
  .
  işlem satırı;
}

// Üye olmayan fonksiyon bildirimleri
dönüş-değeri fonk-adı(parametreler);

// Ana fonksiyon bildirimi
int main(void)
{
  işlem satırı;
  .
  .
  işlem satırı;
}

// Üye olmayan fonksiyon yapıları
dönüş-değeri fonk-adı(parametreler);
{
  işlem satırı;
  .
  .
  işlem satırı;
}
 

```

Bir C++ programının temelini fonksiyonlar oluşturmaktadır. Bir programda en az bir main() fonksiyonu bulunmalıdır.
