---
layout: post
title: "Fonksiyonlar ve Yığın (Stack) Mimarisi: Çağrıların Bellekteki Yolculuğu"
math: true
categories: 
  - Bilgi
tags: 
  - fonksiyonlar
  - stack
  - bellek yönetimi
---

Fonksiyonlar, büyük bir programı yönetilebilir görevlere ayırır; yığın (stack) ise bu görevlerin kim tarafından, hangi parametrelerle ve nereye dönmek üzere çağrıldığını düzenler. Bir fonksiyon çağrısı yalnızca kodun başka bir satıra atlaması değildir: İşletim sistemi, derleyici ve işlemci birlikte çalışarak geçici veriler için düzenli bir bellek kaydı oluşturur. Bu mekanizma sayesinde iç içe çağrılar, özyineleme ve yerel değişkenler güvenle yönetilir.

<!--more-->

## Yığın neden gereklidir?

Programın belleği kavramsal olarak kod, global veri, heap ve stack gibi bölümlere ayrılır. Heap dinamik olarak oluşturulan ve ömrü programcının ya da çöp toplayıcının kontrolündeki nesneler içindir. Stack ise fonksiyon çağrılarının doğal **LIFO** (Last In, First Out — son giren ilk çıkar) düzenini izler. `main()` içinden `A()`, onun içinden de `B()` çağrılırsa, önce `B()` bitmek zorundadır.

Her çağrıda stack üzerinde bir **stack frame** (çağrı çerçevesi) oluşturulur. Bu çerçeve tipik olarak dönüş adresini, parametreleri, yerel değişkenleri, kaydedilmiş kayıtçıları ve hizalama için ayrılan alanı içerir. Stack işaretçisi `$SP`, yığının güncel tepesini; frame pointer ise çoğu mimaride mevcut çerçevenin sabit bir referans noktasını gösterir.

| Bellek bölgesi | Temel kullanım | Ömür | Yönetim |
|---|---|---|---|
| Kod bölgesi | Derlenmiş komutlar | Program boyunca | İşletim sistemi / yükleyici |
| Global veri | Global ve statik değişkenler | Program boyunca | Çalışma zamanı |
| Heap | Dinamik nesneler | İhtiyaca bağlı | `malloc/free` veya GC |
| Stack | Çağrılar ve yerel veriler | Fonksiyon bitene kadar | Otomatik |

## Bir çağrının anatomisi

Örneğin aşağıdaki C kodunda `topla`, iki parametre alır ve sonucu çağırana döndürür:

```c
int topla(int a, int b) {
    int araSonuc = a + b;
    return araSonuc;
}

int main(void) {
    int sonuc = topla(7, 5);
    return sonuc;
}
```

`main`, `topla(7, 5)` çağrısını hazırlarken parametreleri ilgili kayıtçılara veya mimarinin çağrı sözleşmesine göre stack'e yerleştirir. Ardından dönüş adresini saklayarak `topla` koduna dallanır. Fonksiyon kendi yerel alanını ayırır, toplamayı yapar ve dönüş değerini genellikle belirlenmiş bir kayıtçıyla iletir. Son olarak frame temizlenir; işlemci dönüş adresine gider.

Basitleştirilmiş yığın görünümü şöyledir:

```text
Yüksek adresler
+-------------------+
| main'in frame'i   |
+-------------------+
| dönüş adresi      |
| kaydedilmiş kayıt |
| yerel: araSonuc   | <- topla'nın frame'i
+-------------------+
Düşük adresler
```

Çoğu modern sistemde stack düşük adreslere doğru büyür. Bu evrensel bir zorunluluk değildir; önemli olan derleyici, ABI (Application Binary Interface) ve işlemcinin aynı sözleşmeyi izlemesidir. Bir frame için kabaca şu ilişki düşünülebilir:

$$S_{yeni} = S_{eski} - (P + L + R + A)$$

Burada $P$ parametre alanı, $L$ yerel değişkenler, $R$ saklanan kayıtçılar ve $A$ hizalama boşluğudur.

## Parametreler nasıl aktarılır?

Çağrı sözleşmesi, parametrelerin nerede duracağını ve kimin temizleme yapacağını belirler. Güncel 64-bit mimariler ilk birkaç parametreyi kayıtçılarla aktararak bellek erişimini azaltır; fazlası stack'e taşar. Kayıtçıların sınırlı olması, büyük yapıların veya çok sayıda argümanın stack kullanımını hâlâ gerekli kılar.

| Yaklaşım | Avantaj | Dikkat edilmesi gereken |
|---|---|---|
| Kayıtçı ile aktarım | Hızlı, az bellek erişimi | Kayıtçı sayısı sınırlıdır |
| Stack ile aktarım | Çok sayıda argümanı destekler | Daha fazla bellek trafiği |
| Değer ile aktarım | Çağıranın verisi korunur | Büyük veriler kopyalanabilir |
| Referans/işaretçi ile aktarım | Kopyalama maliyeti düşer | Yan etkiler oluşabilir |

Özyinelemeli fonksiyonlar stack'in önemini dramatik biçimde gösterir. Her `faktoriyel(n)` çağrısı ayrı bir frame açar; dolayısıyla bellek tüketimi yaklaşık olarak $O(n)$ olur. Kontrolsüz derinlik, **stack overflow** üretir. Ayrıca bir fonksiyondan yerel dizinin adresini döndürmek tehlikelidir: Fonksiyon bittiğinde frame geçersizdir.

Özetle stack, modüler programlamanın görünmez sahne amiridir. Fonksiyonlar arası geçişi, dönüşü ve geçici verileri disiplinli biçimde düzenler. Bu yapıyı anlamak; performans analizi, hata ayıklama, güvenli kod yazımı ve assembly seviyesindeki davranışı yorumlama için güçlü bir temel sağlar.
