---
layout: post
title: "Struct'lar ile Veri Gruplama: Bellekte Düzenli Gerçek Dünya Modelleri"
math: true
categories: 
  - Bilgi
tags: 
  - struct
  - veri yapıları
  - bellek
  - c programlama
---

Programlamada gerçek dünya nesneleri nadiren tek bir değerden oluşur. Bir öğrencinin adı, numarası ve notu; bir oyun karakterinin koordinatları, canı ve seviyesi vardır. Bu bilgileri birbirinden kopuk değişkenlerde tutmak kısa örneklerde işe yarasa da uygulama büyüdükçe yönetilemez hale gelir. **Yapılar (structs)**, farklı türlerdeki verileri mantıksal olarak tek bir varlık altında toplayan temel veri iskeletleridir.
``
Bir struct, bellekte üyelerinin yan yana yer aldığı bir veri bloğu olarak düşünülebilir. Örneğin bir `Ogrenci` kaydı; metin, tamsayı ve ondalık sayı gibi birbirinden farklı tipleri aynı paket içinde taşır. Böylece program, üç ayrı değişkeni değil, tek bir öğrenciyi işler. Bu yaklaşımın özünde **veri modelleme** vardır: Kodun yapısı, temsil ettiği kavramın yapısına yaklaşır.

```c
#include <stdio.h>
#include <string.h>

typedef struct {
    char ad[40];
    int numara;
    float ortalama;
} Ogrenci;

int main(void) {
    Ogrenci ogrenci;

    strcpy(ogrenci.ad, "Deniz");
    ogrenci.numara = 1024;
    ogrenci.ortalama = 3.45f;

    printf("%s - %d - %.2f\n", ogrenci.ad,
           ogrenci.numara, ogrenci.ortalama);
    return 0;
}
```

Bu C örneğinde `typedef`, uzun `struct Ogrenci` yazımı yerine doğrudan `Ogrenci` türünü kullanmayı sağlar. Nokta (`.`) operatörü ise bir nesnenin alanına erişir. Struct burada yalnızca değerleri saklamaz; bu üç değerin aynı öğrenciye ait olduğu bilgisini de kodun içine taşır.

## Neden ayrı değişkenler yerine struct?

| Yaklaşım | Güçlü yönü | Zayıf yönü |
|---|---|---|
| Ayrı değişkenler | Çok küçük örneklerde hızlıdır | İlişkili veriler kolayca karışır |
| Paralel diziler | Aynı türden çok kayıt tutabilir | Dizilerin indeksleri senkron kalmalıdır |
| Struct dizisi | Her kayıt kendi verisini taşır | Tasarım aşamasında alanları planlamak gerekir |

Örneğin `adlar[3]`, `numaralar[3]` ve `notlar[3]` dizilerinde `i` indeksinin her zaman aynı kişiyi göstermesi gerekir. Struct dizisinde ise `ogrenciler[i]` başlı başına bir kayıttır. Bu, hataya açık eşleştirme yükünü azaltır.

## Bellek düzeni ve padding sürprizi

Bir struct'ın yaklaşık boyutu, üyelerinin boyutları toplamı gibi görünür:

$$S \approx \sum_{i=1}^{n} s_i$$

Ancak gerçek hayatta derleyici, işlemcinin hızlı erişim kuralları için aralara **padding** adı verilen boş baytlar ekleyebilir. Örneğin `char` sonrasında gelen `int`, 4 baytlık hizalamaya yerleştirilebilir. Bu nedenle çoğu durumda:

$$sizeof(struct) \geq \sum s_i$$

olur. Alanların sırası bellek tüketimini etkileyebilir. Büyük hizalama gerektiren alanları önce yazmak, bazı yapılarda dolgu miktarını azaltır. Fakat okunabilirlik de değerlidir; birkaç bayt kazanmak uğruna modeli anlaşılmazlaştırmak iyi bir takas değildir.

| Kavram | Anlamı | Pratik etkisi |
|---|---|---|
| Üye (field) | Struct içindeki her veri parçası | `ogrenci.numara` gibi erişilir |
| Hizalama | Verinin uygun adres sınırına konması | İşlemci erişimi verimli olur |
| Padding | Hizalama için eklenen boş alan | `sizeof` beklenenden büyük olabilir |
| Struct dizisi | Aynı modelden çok kayıt | Listeleme ve sıralama kolaylaşır |

Struct'lar, nesne yönelimli programlamadaki sınıfların hafif akrabası sayılabilir; fakat varsayılan olarak davranış değil, veri düzeni tanımlarlar. Fonksiyonları struct alanlarını işleyen araçlar gibi tasarlamak temiz bir alışkanlıktır. Örneğin öğrenci yazdırma, not güncelleme veya geçme durumu hesaplama işlerini ayrı fonksiyonlara vermek modeli büyütürken karmaşayı azaltır.

Sonuç olarak struct kullanmak, yalnızca değişkenleri aynı kutuya koymak değildir. Gerçek dünyadaki bir kavramın hangi özelliklerden oluştuğunu açıkça ifade etmektir. Kodunuzdaki `x`, `y`, `z` değişkenleri bir anda anlamlı bir `Konum`a; dağınık müşteri bilgileri ise güvenilir bir `Musteri` kaydına dönüşür. İşte veri gruplamanın küçük ama etkili süper gücü budur.
