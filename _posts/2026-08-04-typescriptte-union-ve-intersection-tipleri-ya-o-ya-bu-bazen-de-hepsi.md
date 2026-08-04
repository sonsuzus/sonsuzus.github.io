---
layout: post
title: "TypeScript’te Union ve Intersection Tipleri: Ya O, Ya Bu… Bazen de Hepsi!"
math: true
categories: 
  - Bilgi
tags: 
  - TypeScript
  - Union Types
  - Intersection Types
---

TypeScript’in tip sistemi, değişkenleri tek bir kalıba hapsetmek yerine gerçek dünyadaki çeşitliliği modellememize yardımcı olur. Bir değerin alternatif tiplerden birini taşıyabildiği durumlarda **union**, farklı yapıların bütün özelliklerini aynı nesnede toplamak istediğimizde ise **intersection** tipleri devreye girer. İsimleri matematik dersini hatırlatsa da doğru kullanıldıklarında kodu hem güvenli hem de oldukça esnek hâle getirirler.
``
## Union tipi: Bu veya şu

Union, `|` operatörüyle oluşturulur ve bir değerin belirtilen tiplerden **en az birine** uygun olabileceğini anlatır. Matematiksel olarak iki tipin birleşimini şöyle gösterebiliriz:

$$U = A \cup B$$

Örneğin kullanıcı kimliği bazı sistemlerde sayı, bazılarında metin olabilir:

```typescript
type Kimlik = string | number;

function kimlikYazdir(kimlik: Kimlik): void {
  console.log(`Kullanıcı kimliği: ${kimlik}`);
}

kimlikYazdir(42);
kimlikYazdir("USR-42");
```

Bu fonksiyon hem `number` hem de `string` kabul eder. Ancak TypeScript, değerin o anda hangi tipe ait olduğunu bilmeden tipe özel işlemler yapılmasına izin vermez. Örneğin doğrudan `kimlik.toUpperCase()` çağırmak hatalıdır; çünkü sayıların böyle bir metodu yoktur.

Çözüm, **type narrowing**, yani tip daraltmadır:

```typescript
function kimlikBicimlendir(kimlik: string | number): string {
  if (typeof kimlik === "string") {
    return kimlik.toUpperCase();
  }

  return kimlik.toFixed(0);
}
```

`typeof` kontrolünden sonra TypeScript ilk dalda değerin `string`, diğer dalda ise `number` olduğunu anlar. Böylece esneklik uğruna tip güvenliğinden vazgeçilmez.

## Intersection tipi: Hem bu hem şu

Intersection, `&` operatörüyle tanımlanır. Oluşan tip, birleştirilen tiplerin **bütün gereksinimlerini aynı anda** karşılamalıdır:

$$I = A \cap B$$

Bir çalışanı hem kişi bilgileriyle hem de kurumsal yetkilerle modelleyelim:

```typescript
interface Kisi {
  ad: string;
  yas: number;
}

interface Calisan {
  departman: string;
  yetkiSeviyesi: number;
}

type KurumsalKullanici = Kisi & Calisan;

const kullanici: KurumsalKullanici = {
  ad: "Ada",
  yas: 28,
  departman: "Yazılım",
  yetkiSeviyesi: 3
};
```

`KurumsalKullanici`, iki arayüzden yalnızca birini seçmez; ikisinin alanlarını da zorunlu tutar. `departman` veya `yas` kaldırılırsa derleyici itiraz eder. Intersection’ı, farklı LEGO setlerini aynı modelde kullanmak gibi düşünebiliriz: Parçaların hiçbiri kaybolmaz.

## Temel farklar

| Özellik | Union (`A \| B`) | Intersection (`A & B`) |
|---|---|---|
| Anlam | A veya B | Hem A hem B |
| Amaç | Alternatif değerleri modellemek | Özellikleri tek yapıda toplamak |
| Güvenli erişim | Ortak üyeler kullanılabilir | Tüm üyeler kullanılabilir |
| Tip daraltma | Genellikle gerekir | Çoğunlukla gerekmez |
| Yaygın kullanım | API durumları, kimlikler, sonuçlar | Rol, yetki ve nesne bileşimi |

## Ayırt edilebilir union modeli

Union tiplerinin en güçlü kullanım alanlarından biri, her seçeneğe sabit bir ayırt edici alan eklemektir:

```typescript
type Sonuc =
  | { durum: "basarili"; veri: string[] }
  | { durum: "hatali"; mesaj: string };

function sonucuGoster(sonuc: Sonuc): void {
  switch (sonuc.durum) {
    case "basarili":
      console.log(sonuc.veri.join(", "));
      break;
    case "hatali":
      console.error(sonuc.mesaj);
      break;
  }
}
```

Buradaki `durum` alanı, union üyelerini ayırt eden etikettir. Başarılı sonuçta `veri`, hatalı sonuçta `mesaj` güvenle kullanılabilir. Bu yaklaşım API yanıtlarında ve durum makinelerinde sık görülür.

## Tehlikeli kesişimler

Her intersection mantıklı bir sonuç üretmez. Örneğin `string & number`, aynı değerin eş zamanlı olarak hem metin hem sayı olmasını ister. Böyle bir değer üretilemeyeceği için sonuç pratikte `never` tipidir:

```typescript
type Imkansiz = string & number; // never
```

Benzer şekilde, aynı isimli alanlar uyumsuz tiplerle kesiştirildiğinde ilgili alan kullanılamaz hâle gelebilir. Bu nedenle intersection oluştururken arayüzlerin çelişmediği kontrol edilmelidir.

Özetle union, “seçeneklerden biri”; intersection ise “gereksinimlerin tamamı” demektir. Alternatif akışları union ile, farklı yetenekleri taşıyan birleşik nesneleri intersection ile modellemek kodun niyetini görünür kılar. TypeScript de bu modelin dışına çıktığınız anda nazik ama kararlı bir bekçi gibi sizi uyarır.
