---
layout: post
title: "TypeScript’te any ve unknown: Esneklik mi, Tip Güvenliği mi?"
math: true
categories: 
  - Bilgi
tags: 
  - TypeScript
  - JavaScript
  - Tip Güvenliği
---

TypeScript kullanırken bazen elimizdeki değerin tipini gerçekten bilemeyiz. Bir API cevabı, kullanıcı girdisi veya eski bir JavaScript kütüphanesi her şeyi döndürebilir. İşte bu belirsizlik karşısında `any` ve `unknown` sahneye çıkar. İkisi de “Bu değerin tipi şimdilik belli değil” diyebilir; ancak biri güvenlik kapısını açık bırakırken diğeri kimlik kontrolü yapmadan kimseyi içeri almaz.
``
## `any`: TypeScript’e kısa bir mola verdirmek

`any`, TypeScript’in tip denetimini ilgili değer için büyük ölçüde kapatır. `any` tipindeki bir değişkene her tür değer atanabilir ve bu değişken üzerinde neredeyse her işlem gerçekleştirilebilir.

```ts
let veri: any = "TypeScript";

veri.toUpperCase(); // Çalışabilir
veri = 42;
veri.toFixed(2);    // Bu da çalışabilir
veri.olmayANMetot(); // Derleyici itiraz etmez!
```

Son satır TypeScript tarafından kabul edilir; fakat çalışma zamanında büyük olasılıkla `TypeError` oluşur. Yani `any`, JavaScript’in eski ve özgür dünyasına geçici bir dönüş bileti gibidir. Bilet eğlencelidir, fakat emniyet kemeri yanında verilmez.

Teorik olarak `any`, tip sistemi içinde hem üst hem alt tip gibi davranabilen özel bir kaçış mekanizmasıdır. Basitleştirilmiş biçimde, herhangi bir $T$ tipi için şu esneklik düşünülebilir:

$$any \rightarrow T \quad ve \quad T \rightarrow any$$

Bu çift yönlü geçiş, tip denetiminin sağladığı garantileri zayıflatır. Dolayısıyla `any`, bilinçli ve sınırlı kullanılmalıdır.

## `unknown`: Önce kontrol, sonra hareket

`unknown` da her tür değeri kabul eder. Fakat değeri kullanmadan önce tipini daraltmamızı, yani **type narrowing** yapmamızı zorunlu kılar.

```ts
let cevap: unknown = "Merhaba dünya";

// cevap.toUpperCase(); // Hata: Tip henüz bilinmiyor

if (typeof cevap === "string") {
  console.log(cevap.toUpperCase());
}
```

Burada `typeof` kontrolünden sonra TypeScript, `cevap` değişkeninin ilgili blok içinde `string` olduğunu bilir. Bu yaklaşımın mantığı şöyledir:

$$unknown + tip\ kontrolü = güvenli\ T$$

Başka bir ifadeyle `unknown`, belirsizliği saklamaz; onu çözme sorumluluğunu programcıya açıkça verir.

## Temel farklar

| Özellik | `any` | `unknown` |
|---|---|---|
| Her tür değer atanabilir mi? | Evet | Evet |
| Doğrudan metot çağrılabilir mi? | Evet | Hayır |
| Tip kontrolü zorunlu mu? | Hayır | Evet |
| Çalışma zamanı hatası riski | Yüksek | Daha düşük |
| Tip güvenliğini korur mu? | Hayır | Evet |
| Hızlı geçiş ve eski kod uyumu | Çok uygun | Daha kontrollü |

## Gerçek dünyada güvenli veri işleme

Dış kaynaklardan gelen JSON verileri, `unknown` için ideal bir kullanım alanıdır. Çünkü sunucunun sözleşmeye her zaman uyacağını varsaymak risklidir.

```ts
type Kullanici = {
  ad: string;
  yas: number;
};

function kullaniciMi(deger: unknown): deger is Kullanici {
  if (typeof deger !== "object" || deger === null) {
    return false;
  }

  const aday = deger as Record<string, unknown>;
  return typeof aday.ad === "string" &&
         typeof aday.yas === "number";
}

const hamVeri: unknown = JSON.parse('{"ad":"Ada","yas":28}');

if (kullaniciMi(hamVeri)) {
  console.log(`${hamVeri.ad}, ${hamVeri.yas} yaşında.`);
}
```

`kullaniciMi` fonksiyonu bir **type guard** oluşturur. Yalnızca nesne yapısı doğrulandığında veriye `Kullanici` gibi davranılır. Böylece API’den gelen sürpriz bir dizi, `null` veya eksik alanlı nesne uygulamayı kolayca sabote edemez.

## Hangisini seçmeliyiz?

Yeni kod yazarken varsayılan tercih `unknown` olmalıdır. `any`; tip tanımı bulunmayan eski kütüphaneleri bağlamak, aşamalı JavaScript dönüşümü yapmak veya kısa süreli prototip geliştirmek için kullanılabilir. Yine de mümkün olan en küçük alana hapsedilmelidir.

Kısacası `any`, “Ne yaptığımı biliyorum, bana karışma” der. `unknown` ise “Önce kanıtla, sonra devam et” yaklaşımını benimser. Büyük ve uzun ömürlü projelerde ikinci cümle genellikle daha az hata, daha iyi otomatik tamamlama ve daha huzurlu geliştiriciler anlamına gelir.
