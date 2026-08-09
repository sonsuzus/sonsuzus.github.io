---
layout: post
title: "Diziler ve İşaretçi Aritmetiği: Bellekte Matematiksel Gezinme"
math: true
categories: 
  - Bilgi
tags: 
  - C
  - Diziler
  - İşaretçiler
  - Bellek Yönetimi
---

Bir C dizisi, sadece aynı türden değerlerin listesi değildir; bellekte art arda yerleştirilmiş sabit boyutlu fiziksel blokların ta kendisidir. İşaretçi aritmetiği ise bu blokların adresleri üzerinde güvenli ve anlamlı biçimde gezinmenin yoludur. İlk bakışta `p + 1` ifadesi bir adresi yalnızca bir artırıyormuş gibi görünür. Oysa C burada tür bilgisini kullanır ve bir sonraki elemana sıçrar. Bu küçük ayrıntı, dizilerin performanslı çalışmasının temelidir.

``

## Ardışık bellek fikri

`int sayilar[5]` tanımlandığında derleyici, beş `int` değerini yan yana saklayacak kadar yer ayırır. Eğer bir `int` 4 bayt ise, dizinin kapladığı alan teorik olarak $5 \times 4 = 20$ bayttır. İlk elemanın adresi $B$ ve eleman türünün boyutu $S$ ise, $i$. elemanın adresi şu formülle bulunur:

$$adres(dizi[i]) = B + i \times S$$

Bu nedenle `sayilar[3]`, aslında `*(sayilar + 3)` ile eşdeğerdir. Dizi adı çoğu ifadede ilk elemana işaretçiye dönüşür; yani `sayilar` pratikte `&sayilar[0]` gibi davranır. Ancak dizi adı değiştirilebilir bir işaretçi değildir: `sayilar++` geçersizdir, fakat `int *p = sayilar; p++;` tamamen geçerlidir.

| İfade | Anlamı | Sonuç türü |
|---|---|---|
| `dizi` | İlk elemanın adresi | `int *` benzeri işaretçi ifadesi |
| `dizi[i]` | `i`. elemana erişim | `int` |
| `*(dizi + i)` | İşaretçiyle `i`. elemana erişim | `int` |
| `&dizi[i]` | `i`. elemanın adresi | `int *` |
| `dizi + i` | `i`. elemanın başlangıç adresi | `int *` |

## İşaretçi neden bayt bayt ilerlemez?

Bir `char *` işaretçisinde `p + 1` tipik olarak 1 bayt ilerler; çünkü `char` bir bayttır. Buna karşılık `double *` için aynı işlem çoğu sistemde 8 baytlık bir sıçramadır. Bu davranış, kaynak kodunu hem okunabilir hem de tür güvenliği açısından daha anlamlı yapar. C'nin yaptığı hesap şudur:

$$p + n = adres(p) + n \times sizeof(*p)$$

Aşağıdaki örnek, indeksleme ile işaretçi aritmetiğinin aynı veriyi nasıl dolaştığını gösterir:

```c
#include <stdio.h>

int main(void) {
    int notlar[] = {72, 85, 91, 64, 78};
    size_t adet = sizeof notlar / sizeof notlar[0];
    int *p = notlar;
    int toplam = 0;

    for (size_t i = 0; i < adet; i++) {
        toplam += *(p + i);       // notlar[i] ile aynıdır
        printf("%zu. not: %d, adres: %p\n",
               i, *(p + i), (void *)(p + i));
    }

    printf("Ortalama: %.2f\n", (double)toplam / adet);
    return 0;
}
```

Burada `sizeof notlar / sizeof notlar[0]` kalıbı, sabit boyutlu dizideki eleman sayısını hesaplar. `p + i` her turda bir sonraki `int` bloğuna gider; `*` operatörü de o adresteki değeri okur. Adresler ekranda sayısal olarak ardışık görünmeyebilir, fakat aralarındaki fark `sizeof(int)` kadardır.

## Sınırlar: hızlı olmak, sınırsız olmak değildir

İşaretçi aritmetiği yalnızca aynı dizi nesnesinin sınırları içinde tanımlıdır. Dizinin son elemanından bir sonraki konumu gösteren `dizi + adet` adresini hesaplamak yasaldır; buna *one-past-the-end* denir. Fakat bu adresin içeriğini okumak, yani `*(dizi + adet)` yapmak tanımsız davranıştır. Aynı şekilde, farklı dizilere ait işaretçileri çıkarma veya karşılaştırma girişimleri taşınabilir değildir.

| İşlem | Durum | Neden |
|---|---|---|
| `p + 2` | Güvenli | Hedef aynı dizinin içindeyse |
| `p < dizi + adet` | Güvenli | Aynı dizi sınırında karşılaştırma |
| `dizi + adet` | Güvenli | Sadece sınır sonunu gösterir |
| `*(dizi + adet)` | Hatalı | Dizinin dışında okuma yapar |
| `p - dizi` | Güvenli | Aynı dizide eleman uzaklığı verir |

Özetle dizi, bellekteki düzenli blok planıdır; işaretçi ise bu planın koordinat aracıdır. İndeksleme çoğu zaman daha okunaklıdır, ancak işaretçi aritmetiğini anlamak fonksiyon parametreleri, tamponlar, metinler ve yüksek performanslı C kodu için vazgeçilmezdir.
