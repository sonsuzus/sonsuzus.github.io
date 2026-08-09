---
layout: post
title: "Pointer’lar ve Bellek Adresleme: Veriye Değil, Konumuna Ulaşmak"
math: true
categories: 
  - Bilgi
tags: 
  - C
  - C++
  - Pointer
  - Bellek Yönetimi
  - Performans
---

Bir değişkeni düşünün: çoğu zaman onun değerini kullanırız, fakat bilgisayar açısından asıl önemli soru şudur: Bu değer RAM’in *neresinde* duruyor? İşaretçiler (pointer), verinin kendisini taşımak yerine o verinin bellekteki adresini saklayan değişkenlerdir. Böylece büyük bir diziyi, karmaşık bir nesneyi veya bir yapıyı kopyalamak yerine ona doğrudan erişebiliriz. Bu yaklaşım sistem programlama, oyun motorları, gömülü yazılımlar ve yüksek performanslı uygulamaların görünmez turbo düğmesidir.
``

Bir belleği numaralandırılmış evler bulunan uzun bir sokak gibi ele alalım. `int sayi = 42;` ifadesi, `42` değerini bir eve yerleştirir. `&sayi` operatörü o evin adresini verir. Pointer ise bu adresin yazılı olduğu bir not kâğıdıdır. C dilinde `int *p = &sayi;` yazdığımızda, `p` artık `sayi` değişkeninin bulunduğu konumu bilir. `*p` ise “bu adrese git ve oradaki değeri oku ya da değiştir” anlamına gelir.

Matematiksel olarak, bir değişkenin adresini $a$ ve o adresteki değeri $V(a)$ ile gösterelim. Pointer’ın tuttuğu değer $p = a$ ise dereference işlemi şu fikre karşılık gelir:

$$*p = V(p) = V(a)$$

Yani pointer değerin kendisi değil, değere ulaşan rotadır. Bu ayrım özellikle büyük veri yapılarında kritiktir. Boyutu $n$ olan bir yapıyı kopyalamanın maliyeti kabaca $O(n)$ iken, adresini kopyalamak çoğu modern mimaride sabit boyutlu bir adres olduğu için $O(1)$ maliyetlidir.

| İşlem | Değer Kopyalama | Pointer ile Aktarma |
|---|---:|---:|
| Büyük yapı gönderme | $O(n)$ | $O(1)$ |
| Bellek tüketimi | Yeni kopya gerekir | Sadece adres saklanır |
| Orijinali değiştirme | Genellikle etkilemez | Doğrudan etkileyebilir |
| Güvenlik riski | Daha düşük | Geçersiz adres riski vardır |

Aşağıdaki C örneği, değer ve adres arasındaki ilişkiyi netleştirir:

```c
#include <stdio.h>

void indirimUygula(double *fiyat, double oran) {
    *fiyat = *fiyat * (1.0 - oran);
}

int main(void) {
    double urunFiyati = 120.0;
    double *fiyatAdresi = &urunFiyati;

    indirimUygula(fiyatAdresi, 0.25);

    printf("Yeni fiyat: %.2f\n", urunFiyati);
    printf("Bellek adresi: %p\n", (void *)fiyatAdresi);
    return 0;
}
```

Burada `indirimUygula`, fiyatın kopyasını almak yerine adresini alır. Fonksiyon içindeki `*fiyat`, çağıranın belleğindeki gerçek `urunFiyati` değişkenidir; sonuç olarak değer `90.00` olur. Bu teknik, büyük `struct` nesnelerini fonksiyonlara iletirken gereksiz kopyalamayı önler.

Pointer aritmetiği de belleğin ardışık düzeninden yararlanır. Bir `int *p` için `p + 1`, adresi bir bayt değil, `sizeof(int)` kadar ilerletir. Genel ifade şöyledir:

$$\operatorname{adres}(p+i) = \operatorname{adres}(p) + i \times \operatorname{sizeof}(T)$$

Bu nedenle diziler ve pointer’lar yakın akrabadır: `dizi[i]` ifadesi kavramsal olarak `*(dizi + i)` ile eşdeğerdir. Ancak bu güç dikkat ister. Başlatılmamış pointer kullanmak, serbest bırakılmış belleğe erişmek (*dangling pointer*) veya dizi sınırının dışına taşmak tanımsız davranış üretir.

| İyi Uygulama | Neden Önemli? |
|---|---|
| Pointer’ı `NULL`/`nullptr` ile başlatmak | Rastgele adres kullanımını azaltır |
| Kullanımdan önce null kontrolü yapmak | Çökme riskini düşürür |
| Dinamik belleği doğru zamanda serbest bırakmak | Bellek sızıntısını önler |
| Sınırları korumak | Taşma ve güvenlik açıklarını engeller |

Özetle pointer, “veriyi taşıma” yerine “verinin yerini paylaşma” aracıdır. Doğru kullanıldığında performans ve esneklik kazandırır; dikkatsiz kullanıldığında ise programı mayın tarlasına çevirebilir. Adresi bilmek güçtür, ama o gücün yanında mutlaka sorumluluk da gelir.
