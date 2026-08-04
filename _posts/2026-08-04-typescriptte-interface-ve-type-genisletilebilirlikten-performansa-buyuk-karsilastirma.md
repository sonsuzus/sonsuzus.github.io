---
layout: post
title: "TypeScript'te Interface ve Type: Genişletilebilirlikten Performansa Büyük Karşılaştırma"
math: true
categories: 
  - Bilgi
tags: 
  - TypeScript
  - interface
  - type
---

TypeScript dünyasında `interface` ve `type`, nesnelerin biçimini tanımlarken sık sık aynı işi yapıyormuş gibi görünür. İkisi de özelliklerin türünü belirler, yeniden kullanılabilir modeller oluşturur ve editörün otomatik tamamlama yeteneklerini güçlendirir. Ancak konu genişletme, bildirim birleştirme ve karmaşık tür hesaplamalarına geldiğinde bu iki araç farklı karakterlere bürünür.

``

## Ortak temel: Yapısal tip sistemi

TypeScript, nominal değil **yapısal tipleme** kullanır. Yani bir değerin belirli bir türe uyup uymadığı adına değil, sahip olduğu yapıya bakılarak değerlendirilir. Bir türün gerekli özellik kümesini $R$, verilen nesnenin özellik kümesini $O$ ile gösterirsek temel uygunluk düşüncesi şöyle özetlenebilir:

$$R \subseteq O \Rightarrow O \text{, } R \text{ türüne atanabilir}$$

Bu nedenle aşağıdaki iki tanım, temel kullanım bakımından eşdeğerdir:

```ts
interface KullaniciArayuzu {
  id: number;
  ad: string;
}

type KullaniciTipi = {
  id: number;
  ad: string;
};

const ada: KullaniciArayuzu = { id: 1, ad: "Ada" };
const alan: KullaniciTipi = { id: 2, ad: "Alan" };
```

Her iki yapı da çalışma zamanında silinir; JavaScript çıktısında yer almaz. Dolayısıyla nesne oluşturma veya özellik okuma performansları arasında doğrudan fark bulunmaz.

## Genişletilebilirlik farkları

`interface`, `extends` anahtar sözcüğüyle açık ve okunabilir biçimde genişletilebilir. Aynı isimle tekrar tanımlandığında ise bildirimler otomatik olarak birleşir.

```ts
interface Calisan {
  ad: string;
}

interface Calisan {
  departman: string;
}

interface Yonetici extends Calisan {
  ekipBuyuklugu: number;
}

const yonetici: Yonetici = {
  ad: "Grace",
  departman: "Ar-Ge",
  ekipBuyuklugu: 8
};
```

Bu **declaration merging** özelliği, özellikle üçüncü taraf kütüphanelerin türlerini genişletirken değerlidir. `type` aynı adla yeniden tanımlanamaz; genişletme için kesişim kullanır:

```ts
type Calisan = {
  ad: string;
};

type Yonetici = Calisan & {
  ekipBuyuklugu: number;
};
```

Kesişimde iki özellik çelişirse sonuç şaşırtıcı olabilir. Örneğin `{ id: string } & { id: number }` ifadesindeki `id`, pratikte `never` olur. `interface extends` ise uyumsuz özellikleri genellikle tanım sırasında daha anlaşılır bir hata olarak bildirir.

| Özellik | `interface` | `type` |
|---|---|---|
| Nesne biçimi tanımlama | Evet | Evet |
| `extends` ile genişletme | Evet | Dolaylı |
| Bildirim birleştirme | Evet | Hayır |
| Union türleri | Hayır | Evet |
| Primitive için takma ad | Hayır | Evet |
| Tuple, mapped ve conditional türler | Sınırlı | Güçlü |

## Type ne zaman öne çıkar?

`type`, yalnızca nesne şeması değildir. Union, tuple, primitive takma adı ve koşullu türler gibi daha geniş bir araç kutusu sunar:

```ts
type Kimlik = string | number;
type Koordinat = [x: number, y: number];
type Durum = "bekliyor" | "tamamlandi" | "hata";

type SaltOkunur<T> = {
  readonly [K in keyof T]: T[K];
};
```

Buradaki `SaltOkunur<T>`, her özelliği dolaşan bir mapped type örneğidir. Böyle tür düzeyi hesaplamaları doğrudan `interface` ile ifade etmek uygun değildir.

## Performans gerçekten farklı mı?

Çalışma zamanı maliyeti iki yapı için de sıfırdır. Fark yalnızca TypeScript derleyicisinin tür kontrolü sırasında ortaya çıkabilir. Derleyici, interface ilişkilerini önbelleğe alma konusunda avantaj sağlayabilir; çok sayıda iç içe kesişim ise tekrar tekrar hesaplanarak editör ve derleme süresini artırabilir.

Kabaca tür kontrol maliyetini $C$, birleşen karmaşık tür sayısını $n$ kabul edersek bazı yoğun kesişim senaryolarında ilişki doğrusal olmaktan çıkabilir:

$$C(n) \approx O(n^2)$$

Bu kesin bir evrensel ölçüm değil, karmaşıklığın neden önemli olduğunu anlatan bir modeldir.

| Senaryo | Tercih |
|---|---|
| Genişletilecek nesne veya kütüphane API'si | `interface` |
| Union, tuple ya da koşullu tür | `type` |
| Bildirim birleştirme ihtiyacı | `interface` |
| Küçük ve kapalı veri modeli | İkisi de |
| Karmaşık kesişim zincirleri | Genellikle `interface` |

Sonuç olarak nesne odaklı, büyümeye açık sözleşmelerde `interface`; türleri birleştiren ve hesaplayan modellerde `type` daha doğal seçimdir. En iyi yaklaşım birini takım tutar gibi savunmak değil, veri modelinin ihtiyaçlarına göre doğru aracı seçmektir.
