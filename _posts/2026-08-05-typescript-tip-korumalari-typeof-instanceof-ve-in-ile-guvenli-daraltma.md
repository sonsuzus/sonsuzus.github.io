---
layout: post
title: "TypeScript Tip Korumaları: typeof, instanceof ve in ile Güvenli Daraltma"
math: true
categories: 
  - Bilgi
tags: 
  - TypeScript
  - Type Guards
  - Narrowing
---

TypeScript’te bir değişken bazen birden fazla olası tipe sahip olabilir. Böyle durumlarda derleyici, hangi tipe özgü işlemin güvenli olduğunu kendiliğinden bilemez. Tip korumaları (type guards), programın akışındaki kontrolleri kullanarak olası tip kümesini küçültür. Bu işleme **tip daraltma (narrowing)** denir. Böylece kod hem güvenli hem de gereksiz tür dönüşümlerinden uzak hâle gelir.
``
## Daraltmanın temel mantığı

Bir değişkenin tipi `string | number` ise onu matematiksel olarak bir birleşim kümesi gibi düşünebiliriz:

$$T = \{string, number\}$$

`typeof value === "string"` kontrolünün doğru olduğu dalda TypeScript, olası tipleri filtreler:

$$T' = T \cap \{string\} = \{string\}$$

Başka bir ifadeyle çalışma zamanındaki bir koşul, derleme zamanındaki tip bilgisini daha kesin hâle getirir. Koşulun diğer dalında ise geriye `number` kalır.

```ts
function biçimlendir(value: string | number): string {
  if (typeof value === "string") {
    // value burada string olarak daraltılır.
    return value.trim().toUpperCase();
  }

  // String seçeneği elendiği için value artık number'dır.
  return value.toFixed(2);
}
```

Bu yaklaşım, riskli `as string` ifadeleriyle derleyiciyi susturmak yerine gerçekten doğrulanmış bilgi üretir.

## Üç temel koruma yöntemi

| Operatör | En uygun kullanım | Örnek kontrol | Daraltılan yapı |
|---|---|---|---|
| `typeof` | İlkel değerler | `typeof x === "number"` | `string`, `number`, `boolean` gibi tipler |
| `instanceof` | Sınıf örnekleri | `x instanceof Date` | Sınıf ve kalıtım zinciri |
| `in` | Nesne özellikleri | `"speed" in vehicle` | Belirli özelliği taşıyan nesne tipi |

### `typeof`: İlkel tiplerin bekçisi

`typeof`, özellikle union tipindeki ilkel değerlerde kullanışlıdır. Ancak JavaScript’in tarihî tuzaklarından biri unutulmamalıdır: `typeof null` sonucu `"object"` değeridir. Bu nedenle nesne kontrolünde ayrıca `value !== null` koşulu gerekir.

```ts
function uzunluk(value: string | string[] | null): number {
  if (value === null) return 0;

  if (typeof value === "string") {
    return value.trim().length;
  }

  return value.length; // Burada value string[] tipindedir.
}
```

### `instanceof`: Sınıfları ayırt etmek

`instanceof`, bir nesnenin belirli bir constructor’ın prototip zincirinden gelip gelmediğini çalışma zamanında sınar. Bu nedenle interface’lerle doğrudan kullanılamaz; interface’ler JavaScript çıktısında bulunmaz.

```ts
class Kedi {
  miyavla() {
    return "Miyav!";
  }
}

class Köpek {
  havla() {
    return "Hav hav!";
  }
}

function konuştur(hayvan: Kedi | Köpek): string {
  if (hayvan instanceof Kedi) {
    return hayvan.miyavla();
  }

  return hayvan.havla();
}
```

Burada TypeScript, ilk dalda `Kedi`, kalan dalda ise `Köpek` işlemlerine izin verir. Hayvanat bahçesi küçük, tip güvenliği büyüktür!

### `in`: Özelliğe bakarak seçim yapmak

`in` operatörü, bir özelliğin nesnede veya prototip zincirinde bulunup bulunmadığını kontrol eder. Özellikle farklı alanlara sahip nesne birleşimlerinde okunaklıdır.

```ts
type Araba = { marka: string; sür: () => void };
type Tekne = { ad: string; yüz: () => void };

function hareketEt(araç: Araba | Tekne): void {
  if ("sür" in araç) {
    araç.sür(); // araç artık Araba
  } else {
    araç.yüz(); // araç artık Tekne
  }
}
```

## Özel tip koruması yazmak

Karmaşık doğrulamaları tekrar kullanmak için dönüş tipi `değer is Tip` biçiminde olan fonksiyonlar yazılabilir:

```ts
type Kullanıcı = { id: number; ad: string };

function kullanıcıMı(value: unknown): value is Kullanıcı {
  return (
    typeof value === "object" &&
    value !== null &&
    "id" in value &&
    "ad" in value &&
    typeof value.id === "number" &&
    typeof value.ad === "string"
  );
}
```

Bu fonksiyon `true` döndürdüğünde çağıran kapsamda değer `Kullanıcı` olarak daraltılır. Yine de TypeScript bu söze güvenir; hatalı yazılmış bir koruma sahte güvenlik oluşturabilir. Sonuç olarak doğru koruma, “Ben bunun tipini biliyorum” demek değil, bunu çalışma zamanında kanıtlamaktır.
