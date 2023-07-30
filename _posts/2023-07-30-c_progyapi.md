---
title:  C Program yapısı
author: sonsuz
date: 2023-07-30 21:41:44 +0300
categories: [Program,C]
tags: [programlama,c]
---


## Bir C programının temel yapısı

Bir C programında, genel olarak aşağıda gösterilen bölümler sırayla yer alır. Başlık dosya bildiriminden sonraki sıralama değiştirilebilir. Programda mutlaka tanımlanması tek bölüm main() fonksiyonudur. Bunun dışındaki bölümlerin tanımlanması tamamen ihtiyaca bağlıdır.

* Başlık dosya bildirimleri
* Fonksiyon bildirimleri
* main() fonksiyonu
* Fonksiyon ana yapıları

Bir C++ programının temel yapısı aşağıda gösterilmektedir:

```c
// Başlık dosya bildirimleri
#include <başlık-dosya-adı>
.
.
.
#include <başlık-dosya-adı>

// Fonksiyon bildirimleri
dönüş-değeri fonk-adı(parametreler);

// Ana fonksiyon bildirimi
int main(void)
{
  işlem satırı;
  .
  .
  işlem satırı;
}

// Fonksiyon yapıları
dönüş-değeri fonk-adı(parametreler);
{
  işlem satırı;
  .
  .
  işlem satırı;
}
 

```

Bir C programının temelini fonksiyonlar oluşturmaktadır. Bir programda en az bir main() fonksiyonu bulunmalıdır.
