---
layout: post
title: "Bellek Sızıntılarının Psikanalizi: Kodun Bilinçdışında Biriken Nesneler"
math: true
categories: 
  - Bilgi
tags: 
  - bellek yönetimi
  - memory leak
  - hata ayıklama
---

Bir program bazen hiçbir şeyi unutamaz. Kullanıcı pencereyi kapatır, işlem tamamlanır, nesnenin hikâyedeki rolü biter; fakat kod, geçmişiyle bağını kesmez. Belleğin karanlık bir köşesinde duran bu nesneler, dijital bilinçdışının bastırılmış anıları gibidir. Uygulama çalışmayı sürdürürken onların kapladığı alan büyür ve sonunda sistem, konuşamadığı meseleleri RAM tüketerek ifade etmeye başlar.
``
## Bellek sızıntısı gerçekten nedir?

Bellek sızıntısı, artık işe yaramayan bir bellek bölgesinin serbest bırakılamaması durumudur. Buradaki kritik ayrım, belleğin yalnızca **kullanılıyor görünmesi** ile gerçekten **gerekli olması** arasındadır. Bir nesneye hâlâ erişilebiliyorsa çöp toplayıcı onu canlı kabul eder; nesnenin uygulama açısından hiçbir anlam taşımaması bu kararı değiştirmez.

Bir sürecin yaklaşık bellek davranışını şöyle düşünebiliriz:

$$M(t) = M_0 + A(t) - F(t)$$

Burada $M_0$ başlangıç belleği, $A(t)$ ayrılan toplam alan, $F(t)$ ise geri verilen alandır. İş yükü sabitlenmesine rağmen $A(t)-F(t)$ sürekli büyüyorsa ortada yalnızca yoğun kullanım değil, muhtemel bir sızıntı vardır.

| Psikanalitik metafor | Yazılımdaki karşılığı | Ortaya çıkan belirti |
|---|---|---|
| Bastırılmış anı | Serbest bırakılmamış bellek | RAM kullanımının büyümesi |
| Koparılamayan bağ | Gereksiz nesne referansı | Çöp toplayıcının nesneyi silememesi |
| Tekrarlama dürtüsü | Her istekte yeniden kaynak ayırma | Düzenli ve basamaklı artış |
| Terapi | Profiling ve hata ayıklama | Sızıntı kaynağının görünür olması |

## Manuel yönetim: Unutma sorumluluğu geliştiricide

C ve C++ gibi dillerde bellek ayırmak ile onu serbest bırakmak geliştiricinin sorumluluğundadır. Aşağıdaki fonksiyon, her çağrıda yeni bir alan oluşturur ancak bu alanı geri vermez:

```c
#include <stdlib.h>

void rapor_uret(void) {
    int *veriler = malloc(1000 * sizeof(int));
    if (veriler == NULL) return;

    veriler[0] = 42;
    // İşlem bitti, fakat free(veriler) çağrılmadı.
}
```

Fonksiyon sona erdiğinde `veriler` işaretçisi kaybolur. Ayrılan bölgeye artık erişilemez, dolayısıyla sonradan `free` çağırmak da mümkün değildir. Çözüm, sahiplik süresini açıkça belirlemektir:

```c
void rapor_uret(void) {
    int *veriler = malloc(1000 * sizeof(int));
    if (veriler == NULL) return;

    veriler[0] = 42;
    // Verilerle yapılan işlemler burada tamamlanır.

    free(veriler);
    veriler = NULL;
}
```

`free`, kaynağı sisteme iade eder. İşaretçiyi `NULL` yapmak ise yanlışlıkla aynı alanı yeniden kullanma riskini azaltır.

## Çöp toplayıcı her şeyi çözer mi?

JavaScript, Java ve C# gibi dillerde garbage collector erişilemeyen nesneleri otomatik olarak temizler. Ancak otomasyon, psikolojik bağları koparamaz; gereksiz bir referans korunuyorsa nesne hâlâ erişilebilir sayılır.

```javascript
const gecmisMesajlar = [];

function mesajiIsle(mesaj) {
  const analiz = {
    hamVeri: mesaj,
    zaman: Date.now(),
    sonuc: mesaj.toUpperCase()
  };

  gecmisMesajlar.push(analiz);
}
```

`gecmisMesajlar` sınırsız büyüdüğü için her analiz bellekte kalır. Burada sızıntı, unutulmuş bir `free` çağrısından değil, tasarımsal olarak bitmeyen saklama davranışından doğar. Sınırlı bir önbellek daha sağlıklıdır:

```javascript
const SINIR = 100;

gecmisMesajlar.push(analiz);
if (gecmisMesajlar.length > SINIR) {
  gecmisMesajlar.shift();
}
```

## Kodun terapi seansı

Sızıntıları bulmak için Chrome DevTools Heap Snapshot, Valgrind, AddressSanitizer veya VisualVM gibi araçlar kullanılabilir. Tek bir ölçüme bakmak yerine aynı senaryoyu defalarca çalıştırıp bellek eğrisini izlemek gerekir. İşlem bittikten sonra bellek başlangıç seviyesine yaklaşmıyorsa nesnelerin referans zincirleri incelenmelidir.

Sonuçta iyi bellek yönetimi, yalnızca alan boşaltmak değildir; bir kaynağın **kim tarafından**, **ne kadar süreyle** ve **hangi koşulda** tutulacağını bilmektir. İnsan geçmişiyle yüzleşerek, program ise referanslarını keserek hafifler. Bazen en etkili optimizasyon, koda nazikçe şunu söylemektir: Artık bunu bırakabilirsin.
