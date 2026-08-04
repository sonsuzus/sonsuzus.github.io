---
layout: post
title: "TypeScript Birebir Tipler: Değerleri Kesin Sınırlarla Yönetmek"
math: true
categories: 
  - Bilgi
tags: 
  - TypeScript
  - Literal Types
  - Tip Güvenliği
---

Bir fonksiyona “herhangi bir metin” vermek ile yalnızca `"başlat"` veya `"durdur"` değerlerinden birini vermek arasında büyük bir güvenlik farkı vardır. TypeScript’in birebir tipleri (literal types), değişkenlerin alabileceği değerleri kesin biçimde sınırlandırır. Böylece hem hatalar daha kod çalıştırılmadan yakalanır hem de editör önerileri çok daha anlamlı hâle gelir.
``
## Birebir tip nedir?

Normal bir tip, olası değerlerden oluşan geniş bir kümeyi temsil eder. Örneğin `string`, teorik olarak sonsuz sayıda metni kapsar. Birebir tip ise bu kümeyi tek bir değere indirger:

$$T = \{\text{"aktif"}\}$$

Burada `T` tipindeki bir değişkenin alabileceği tek değer `"aktif"` metnidir. Benzer şekilde `42` bir sayı birebir tipi, `true` ise bir boolean birebir tipi olabilir.

```ts
let durum: "aktif" = "aktif";
let cevap: 42 = 42;
let tamamlandi: true = true;

// durum = "pasif"; // Hata: "pasif", "aktif" tipine atanamaz.
```

İlk bakışta tek bir değere izin vermek gereksiz görünebilir. Asıl güç, birden fazla birebir tipin birleşim tipiyle bir araya getirilmesiyle ortaya çıkar.

## Birleşim tipleriyle seçenek listesi oluşturmak

Bir fonksiyonun kabul ettiği durumları matematiksel olarak şöyle tanımlayabiliriz:

$$Durum = \{\text{"bekliyor"}, \text{"çalışıyor"}, \text{"tamamlandı"}\}$$

TypeScript karşılığı ise oldukça okunaklıdır:

```ts
type GorevDurumu = "bekliyor" | "çalışıyor" | "tamamlandı";

function durumGuncelle(yeniDurum: GorevDurumu): void {
  console.log(`Yeni durum: ${yeniDurum}`);
}

durumGuncelle("çalışıyor"); // Geçerli
durumGuncelle("tamamlandı"); // Geçerli
// durumGuncelle("uyuyor");  // Derleme hatası
```

Bu fonksiyon artık rastgele bir metin değil, yalnızca tanımlanmış üç komuttan birini kabul eder. Yazım hatası yapılırsa problem üretime gitmeden görünür.

| Yaklaşım | Kabul edilen değerler | Yazım hatası kontrolü | Editör desteği |
|---|---|---|---|
| `string` | Her metin | Zayıf | Genel |
| Birebir birleşim | Belirlenen metinler | Güçlü | Otomatik tamamlama |
| `enum` | Tanımlı üyeler | Güçlü | Üye adı üzerinden |

## Tip genişlemesi ve `const` farkı

TypeScript, değişkenin sonradan değiştirilebileceğini hesaba katar. Bu nedenle `let` ile oluşturulan bir metin genellikle `string` tipine genişletilir. `const` ise değerin değişmeyeceğini bildirdiği için birebir tipi korur.

```ts
let tema1 = "koyu";   // Tip: string
const tema2 = "koyu"; // Tip: "koyu"

let sabitTema: "koyu" = "koyu";
// sabitTema = "açık"; // Hata
```

Nesnelerde `const` kullanmak tek başına alanları birebir tip yapmaz; çünkü nesnenin özellikleri değiştirilebilir. Bu durumda `as const` devreye girer:

```ts
const ayarlar = {
  tema: "koyu",
  yenilemeSuresi: 30
} as const;

// ayarlar.tema = "açık"; // Hata: özellik salt okunurdur.
```

`as const`, değerleri mümkün olan en dar tipe indirger ve özellikleri `readonly` yapar. Böylece `ayarlar.tema` tipi `string` değil, doğrudan `"koyu"` olur.

## Sayısal birebir tiplerle sınır koymak

Birebir tipler yalnızca metinlere özel değildir. Bir arayüzde izin verilen sütun sayısını sınırlandırabiliriz:

```ts
type SutunSayisi = 1 | 2 | 3 | 4;

function izgaraOlustur(sutun: SutunSayisi): string {
  return `${sutun} sütunlu ızgara oluşturuldu.`;
}

izgaraOlustur(3); // Geçerli
// izgaraOlustur(12); // Hata
```

Bu yaklaşım matematiksel olarak sonlu bir değer kümesi tanımlar:

$$S = \{1, 2, 3, 4\}, \quad sutun \in S$$

Ancak birebir tipler çalışma zamanında doğrulama yapmaz. API’den gelen bilinmeyen bir verinin güvenli olup olmadığını ayrıca kontrol etmek gerekir.

```ts
function temaMi(deger: string): deger is "açık" | "koyu" {
  return deger === "açık" || deger === "koyu";
}
```

## Ne zaman kullanılmalı?

Birebir tipler; HTTP metotları, kullanıcı rolleri, tema seçenekleri, işlem durumları ve sınırlı yapılandırma değerleri için idealdir. Kurallar değişken ve seçenekler çok fazlaysa daha genel tipler veya doğrulama kütüphaneleri tercih edilebilir.

Kısacası birebir tipler, “bu bir metindir” demek yerine “bu metin yalnızca şu değerlerden biridir” diyerek niyeti tipe dönüştürür. Sonuç; daha güvenli fonksiyonlar, daha iyi otomatik tamamlama ve sürprizleri azalan bir kod tabanıdır.
