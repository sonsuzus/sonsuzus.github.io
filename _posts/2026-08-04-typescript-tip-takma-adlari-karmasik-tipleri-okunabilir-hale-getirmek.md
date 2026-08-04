---
layout: post
title: "TypeScript Tip Takma Adları: Karmaşık Tipleri Okunabilir Hale Getirmek"
math: true
categories: 
  - Bilgi
tags: 
  - TypeScript
  - Type Aliases
  - Tip Güvenliği
---

Bir projede aynı uzun tip tanımını üçüncü kez yazarken parmaklarınız “Bunun daha kısa bir yolu olmalı!” diye isyan ediyorsa, TypeScript’in **tip takma adları** yardımınıza yetişir. Type alias, karmaşık veya sık kullanılan bir tipe anlamlı bir isim vererek kodun okunabilirliğini artırır; üstelik bunu çalışma zamanına ek yük getirmeden yapar.
``
## Type alias nedir?

TypeScript’te `type` anahtar sözcüğü, mevcut bir tip ifadesine yeni bir ad verir. En basit örnekle başlayalım:

```ts
type UserId = string;

const activeUserId: UserId = "usr_42";
```

Burada `UserId`, teknik olarak hâlâ `string` tipidir. Ancak değişkenin sıradan bir metin değil, kullanıcı kimliği taşıdığı artık çok daha açıktır. Type alias yeni bir çalışma zamanı değeri veya sınıf üretmez; yalnızca derleme aşamasında kullanılır ve JavaScript çıktısından silinir.

Bunu matematiksel olarak $A = B$ biçiminde düşünebiliriz: `UserId` ile `string` farklı adlara sahip olsa da aynı değer kümesini temsil eder. Dolayısıyla TypeScript’in yapısal tip sisteminde her `string`, aksi yönde özel bir marka oluşturulmadıkça `UserId` olarak kabul edilebilir.

## Karmaşık nesneleri sadeleştirmek

Takma adların asıl gücü, iç içe geçmiş nesne tiplerinde ortaya çıkar:

```ts
type Address = {
  city: string;
  district: string;
  postalCode?: string;
};

type User = {
  id: string;
  name: string;
  address: Address;
};

function printUser(user: User): void {
  console.log(`${user.name} - ${user.address.city}`);
}
```

`Address` ayrı bir kavram olarak tanımlandığı için hem tekrar önlenir hem de `User` tipi daha kolay okunur. Adres yapısı değiştiğinde onlarca fonksiyon imzasını düzenlemek yerine tek bir merkezi tanım güncellenir.

| Doğrudan tip yazımı | Type alias kullanımı |
|---|---|
| Tekrar üretir | Tekrarı azaltır |
| Fonksiyon imzalarını uzatır | İmzaları sadeleştirir |
| Değişiklikleri zorlaştırır | Merkezi güncelleme sağlar |
| Alanın amacını gizleyebilir | İş alanını görünür kılar |

## Birleşim ve kesişim tipleri

Type alias yalnızca nesnelere isim vermek için kullanılmaz. Birleşim, kesişim, tuple ve fonksiyon tipleri de adlandırılabilir:

```ts
type RequestStatus = "idle" | "loading" | "success" | "error";
type Coordinates = [latitude: number, longitude: number];
type Logger = (message: string, level?: "info" | "warn") => void;

type Timestamped = { createdAt: Date };
type Product = { id: number; name: string };
type StoredProduct = Product & Timestamped;
```

Birleşim tipi $T = A \cup B$ yaklaşımıyla, değerin izin verilen kümelerden birine ait olmasını sağlar. `RequestStatus` örneğinde rastgele bir metin yerine yalnızca dört durum kabul edilir. Kesişim tipi $T = A \cap B$ ise bir değerin iki tipin özelliklerini birlikte taşımasını ister.

## Generic takma adlarla yeniden kullanılabilirlik

Generic yapılar, farklı veri tipleri için aynı şablonu kullanmamızı sağlar:

```ts
type ApiResponse<T> = {
  data: T | null;
  error: string | null;
  statusCode: number;
};

type UserResponse = ApiResponse<User>;
```

Buradaki `T`, daha sonra yerleştirilecek tip için parametredir. Böylece kullanıcı, ürün veya sipariş yanıtlarında aynı API yapısını tekrar yazmak gerekmez. Bir yapının $n$ farklı veri modeli için kullanıldığını düşünürsek, tekrar miktarı yaklaşık $n \times k$ satırdan tek bir `k` satırlık şablona indirilebilir.

## Type alias mı, interface mi?

| Özellik | `type` | `interface` |
|---|---|---|
| Nesne tanımlama | Evet | Evet |
| Union ve tuple | Evet | Hayır |
| Declaration merging | Hayır | Evet |
| Genişletme | Kesişim ile | `extends` ile |
| Primitive tipe ad verme | Evet | Hayır |

Nesne odaklı ve sonradan genişletilecek genel API sözleşmelerinde `interface`; union, tuple, fonksiyon veya birleşik tiplerde `type` genellikle daha uygundur. Bu kesin bir savaş değil, doğru aleti seçme meselesidir.

Son olarak takma adları `Data`, `Info` veya `Thing` gibi belirsiz isimlerle doldurmayın. `CheckoutResult`, `AuthenticatedUser` ve `ProductFilter` gibi niyeti anlatan adlar seçin. İyi bir type alias kodu yalnızca kısaltmaz; geliştiriciye sistemin iş kurallarını sessizce anlatan küçük bir belgeye dönüşür.
