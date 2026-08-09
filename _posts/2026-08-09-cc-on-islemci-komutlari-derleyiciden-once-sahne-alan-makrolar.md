---
layout: post
title: "C/C++ Ön İşlemci Komutları: Derleyiciden Önce Sahne Alan Makrolar"
math: true
categories: 
  - Bilgi
tags: 
  - C
  - C++
  - Preprocessor
  - Derleme
  - Makro
---

C ve C++ kodu, derleyicinin eline doğrudan yazdığımız hâliyle ulaşmaz. Arada metin tabanlı ama etkisi büyük bir aşama vardır: **ön işlemci** (preprocessor). `#include`, `#define` ve `#ifdef` gibi satırlarla çalışan bu mekanizma, kaynak kodu derlenmeden hemen önce dönüştürür. Bunu bir tiyatro oyununun sahne arkası ekibi gibi düşünebilirsiniz: oyuncular (derleyici) sahneye çıkmadan dekorlar yerleşir, bazı replikler değiştirilir ve şartlara uymayan sahneler tamamen kaldırılır.

``

## Derleme zincirindeki yeri

Bir C/C++ programının yolculuğu kabaca dört adımdan oluşur. Ön işlemci ilk adımda kaynak metni düzenler; henüz tür kontrolü yapmaz, fonksiyon çağırmaz ve C++ sözdizimini derinlemesine analiz etmez. Temel olarak karakter dizileri üzerinde çalışır.

$$\text{Kaynak Kod} \xrightarrow{\text{Preprocess}} \text{Genişletilmiş Kod} \xrightarrow{\text{Compile}} \text{Nesne Dosyası} \xrightarrow{\text{Link}} \text{Çalıştırılabilir Dosya}$$

| Aşama | Girdi | Temel görev | Çıktı |
|---|---|---|---|
| Ön işleme | `.c`, `.cpp`, `.h` | Makro açma, dosya ekleme, koşullu kod seçme | Düzenlenmiş kaynak |
| Derleme | Düzenlenmiş kaynak | Sözdizimi ve tür kontrolü, makine koduna yakın üretim | `.o` / `.obj` |
| Bağlama | Nesne dosyaları, kütüphaneler | Sembolleri birleştirme | Uygulama |

Örneğin `#include <stdio.h>` yazdığınızda ön işlemci, ilgili başlık dosyasının içeriğini mantıksal olarak o satıra ekler. Bu yüzden başlık dosyalarında tekrar eden eklemeleri önlemek kritik önemdedir.

## `#define`: Metinsel kısayol, sihirli değnek değil

Nesne benzeri makrolar sabit metinleri değiştirir. Fonksiyon benzeri makrolar ise parametre alabilir:

```c
#include <stdio.h>

#define MAX_KULLANICI 100
#define KARE(x) ((x) * (x))

int main(void) {
    int sayi = 5;
    printf("Limit: %d, kare: %d\n", MAX_KULLANICI, KARE(sayi + 1));
}
```

Burada `KARE(sayi + 1)`, `((sayi + 1) * (sayi + 1))` biçimine dönüşür. Parantezler hayati ayrıntıdır. `#define KARE(x) x * x` olsaydı `KARE(2 + 3)` ifadesi `2 + 3 * 2 + 3` olur ve beklenen $25$ yerine $11$ üretirdi.

Makroların tür bilgisi yoktur; bu nedenle modern C++ kodunda sabitler için çoğu zaman `constexpr`, küçük işlevler için `inline` fonksiyonlar daha güvenlidir.

| İhtiyaç | Makro | Daha güvenli alternatif |
|---|---|---|
| Derleme zamanı sabiti | `#define PI 3.14` | `constexpr double pi = 3.14;` |
| Küçük hesaplama | `#define MIN(a,b)` | Şablon veya `inline` fonksiyon |
| Platform seçimi | `#ifdef _WIN32` | Ön işlemci genellikle uygundur |

## Koşullu derleme: Kodun hangi evrende yaşayacağını seçmek

`#if`, `#ifdef`, `#ifndef`, `#elif` ve `#endif`, belirli blokların ön işlemci tarafından korunmasını veya silinmesini sağlar. Özellikle hata ayıklama, özellik bayrakları ve işletim sistemi farkları için kullanılır.

```c
#include <stdio.h>

#define DEBUG_MODU

int main(void) {
#ifdef DEBUG_MODU
    printf("[DEBUG] Program baslatildi.\n");
#endif

#if defined(_WIN32)
    printf("Windows platformu\n");
#else
    printf("Windows disindaki bir platform\n");
#endif
    return 0;
}
```

`DEBUG_MODU` tanımlı değilse debug satırı derleyiciye hiç ulaşmaz. Bu, `if (false)` yazmaktan farklıdır: ikinci durumda kod hâlâ sözdizimsel olarak geçerli olmak zorundadır; koşullu derlemede ise blok kaynak çıktıdan tamamen çıkar.

Başlık dosyalarında klasik koruma deseni de aynı fikri kullanır:

```c
#ifndef HESAPLAYICI_H
#define HESAPLAYICI_H

int topla(int a, int b);

#endif
```

Bu yapı, dosya birden fazla kez eklense bile bildirimin yalnızca bir kez işlenmesini sağlar. Ön işlemci güçlüdür; fakat metinsel çalıştığı için dikkat ister. Makroları küçük, açık isimli ve zorunlu oldukları alanlarla sınırlı tutmak, derleme sahnesinin perde arkasını kontrol altında tutmanın en iyi yoludur.
