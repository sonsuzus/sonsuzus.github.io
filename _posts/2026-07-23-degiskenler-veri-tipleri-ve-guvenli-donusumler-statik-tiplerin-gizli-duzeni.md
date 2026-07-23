---
layout: post
title: "Değişkenler, Veri Tipleri ve Güvenli Dönüşümler: Statik Tiplerin Gizli Düzeni"
math: true
categories: 
  - Bilgi
tags: 
  - değişkenler
  - veri tipleri
  - type inference
  - statik tip
  - tip dönüşümü
---

Programlamada değişkenler, veriyi sakladığımız küçük kutular gibi anlatılır; ama işin arka tarafında derleyicinin yürüttüğü ciddi bir kimlik kontrolü vardır. Bir değerin sayı mı, metin mi, mantıksal sonuç mu olduğunu bilmek; hataları erken yakalamak, belleği doğru kullanmak ve kodun niyetini açık göstermek için kritiktir.

``

Statik tip sisteminde bir değişkenin tipi çalışma zamanında rastgele değişmez; çoğu karar derleme aşamasında verilir. Yani program henüz çalışmadan önce derleyici şunu sorar: “Bu değişkene gerçekten bu değer atanabilir mi?” Eğer cevap hayırsa, program daha başlangıç çizgisine gelmeden uyarı alırız. Bu, özellikle büyük projelerde süper güç gibidir; çünkü hatayı kullanıcı değil, derleyici yakalar.

Basit düşünelim: `int` tam sayıları, `double` ondalıklı sayıları, `string` metinleri, `bool` ise doğru/yanlış değerlerini taşır. Matematiksel olarak bir tipin alabileceği değerleri bir küme gibi düşünebiliriz. Örneğin 32 bitlik işaretli bir tam sayı yaklaşık olarak şu aralıktadır: $-2^{31}$ ile $2^{31}-1$ arası. Bu aralığın dışındaki bir değeri `int` içine koymaya çalışmak, küçük bir bavula piyano sığdırmaya benzer.

| Kavram | Açıklama | Örnek |
|---|---|---|
| Değişken | Bellekte isimlendirilmiş veri alanı | `age` |
| Veri tipi | Değerin biçimini ve sınırlarını belirler | `int`, `string` |
| Statik tip | Tip derleme zamanında bilinir | `int count = 5;` |
| Dinamik tip | Tip çalışma zamanında değişebilir | Bazı script dilleri |

Statik tipli dillerde tipleri her zaman uzun uzun yazmak zorunda değiliz. Burada otomatik tip belirleme, yani type inference devreye girer. Derleyici sağ taraftaki değere bakarak sol taraftaki değişkenin tipini çıkarır. Ancak bu, değişkenin tipsiz olduğu anlamına gelmez; sadece tipi bizim yerimize derleyici yazar.

```csharp
var count = 10;        // Derleyici bunu int olarak belirler
var price = 19.99;     // double
var name = "Ada";      // string
var isActive = true;   // bool

// count = "on";       // Hata: count artık int kabul edilir
```

Bu örnekte `var`, “ne olursa olsun kabul et” demek değildir. Daha çok “tipi sağ taraftan anla ama sonra sıkı denetle” demektir. Yani type inference, statik tip sistemini zayıflatmaz; sadece daha az klavye mesaisi sağlar.

Tip dönüşümleri ise iki ana gruba ayrılır: örtük ve açık dönüşüm. Örtük dönüşüm güvenli kabul edilen, veri kaybı beklenmeyen durumlarda yapılır. Açık dönüşümde ise programcı sorumluluğu üstlenir: “Evet, bunun riskli olabileceğini biliyorum.”

| Dönüşüm Türü | Güvenlik | Örnek | Risk |
|---|---:|---|---|
| Örtük dönüşüm | Yüksek | `int` → `long` | Genelde yok |
| Açık dönüşüm | Orta | `double` → `int` | Ondalık kısım kaybolur |
| Parse işlemi | Girdiye bağlı | `string` → `int` | Geçersiz metin |
| TryParse | Daha güvenli | Kontrollü parse | Hata yönetilebilir |

```csharp
int small = 42;
long big = small; // Örtük dönüşüm: int değeri long içine rahatça sığar

double ratio = 9.75;
int roundedDown = (int)ratio; // Açık dönüşüm: sonuç 9 olur
```

Buradaki dönüşümde $9.75 \rightarrow 9$ olur; yani bilgi kaybı yaşanır. Bu yüzden açık dönüşümler kodda küçük bir sarı ikaz levhası gibi okunmalıdır. “Burada bilinçli bir karar var” mesajı verir.

Kullanıcıdan veya dosyadan gelen veriler genellikle metindir. Bu metni sayıya çevirmek için doğrudan parse etmek yerine güvenli yöntemler tercih edilmelidir.

```csharp
string input = "123";

if (int.TryParse(input, out int number))
{
    int result = number * 2;
    Console.WriteLine(result);
}
else
{
    Console.WriteLine("Geçerli bir sayı girilmedi.");
}
```

`TryParse`, programı patlatmadan sonucu kontrol etmemizi sağlar. Kullanıcı `abc` yazarsa uygulama dramatik bir tiyatro sahnesi gibi çökmez; sadece uygun mesajı verir.

Bazı diller taşma kontrolleri için özel mekanizmalar sunar. Örneğin çok büyük bir sayıyı küçük tipe çevirirken değer aralığı aşılabilir. Bu durumda $x \notin [min, max]$ ise dönüşüm güvenli değildir.

```csharp
checked
{
    int max = int.MaxValue;
    // int overflow = max + 1; // Taşma hatası üretir
}
```

Özetle değişkenler veriyi taşır, veri tipleri bu verinin kurallarını belirler, statik tip sistemi de oyunun hakemi gibi yanlış pasları erkenden düdükler. Type inference kodu sadeleştirirken güvenliği korur. Tip dönüşümlerinde ise temel soru hep aynıdır: “Bu değer hedef tipe kayıpsız ve anlamlı biçimde sığar mı?” Bu soruyu alışkanlık haline getirmek, daha sağlam ve okunabilir programlar yazmanın en pratik yollarından biridir.
