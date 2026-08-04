---
layout: post
title: "TypeScript’te İsteğe Bağlı ve Varsayılan Parametreler"
math: true
categories: 
  - Bilgi
tags: 
  - TypeScript
  - Fonksiyonlar
  - Tip Güvenliği
---

Bir fonksiyonun her çağrıda aynı miktarda bilgiye ihtiyaç duymaması oldukça doğaldır. Kullanıcı adını zorunlu tutarken selamlama biçimini çağırana bırakmak isteyebiliriz. TypeScript’in isteğe bağlı ve varsayılan parametreleri, bu esnekliği tip güvenliğinden vazgeçmeden sağlar. Böylece fonksiyonlarımız hem rahat kullanılır hem de “Bu değer acaba var mı?” sürprizleri kontrol altında tutulur.
``
## İsteğe bağlı parametre nedir?

Bir parametrenin adından sonra `?` koymak, argümanın gönderilmeyebileceğini belirtir. TypeScript bu parametrenin tipini örtük olarak `undefined` ile birleştirir:

```ts
function kullaniciBul(id: number, alan?: string): void {
  console.log(id, alan);
}

kullaniciBul(42);
kullaniciBul(42, "e-posta");
```

Buradaki `alan` parametresinin gerçek tipi `string | undefined` şeklindedir. Bunu kümelerle düşünürsek kabul edilen değerler şu birleşimi oluşturur:

$$T_{alan} = T_{string} \cup \{undefined\}$$

Dolayısıyla parametreyi doğrudan bir `string` gibi kullanamayız. Önce değer bulunup bulunmadığını denetlemeliyiz:

```ts
function etiketiYaz(etiket?: string): void {
  if (etiket !== undefined) {
    console.log(etiket.toUpperCase());
  }
}
```

Bu kontrol, çalışma zamanında oluşabilecek hatayı daha kod çalıştırılmadan görünür hâle getirir. TypeScript burada adeta kapıdaki güvenlik görevlisidir: Biletsiz `undefined`, `toUpperCase()` eğlencesine giremez.

## Varsayılan parametre nasıl çalışır?

Varsayılan parametre, argüman verilmediğinde kullanılacak değeri fonksiyon tanımında belirtir:

```ts
function selamla(ad: string, mesaj: string = "Merhaba"): string {
  return `${mesaj}, ${ad}!`;
}

selamla("Ece");            // Merhaba, Ece!
selamla("Ece", "Günaydın"); // Günaydın, Ece!
```

`mesaj` için çağrı sırasında argüman zorunlu değildir; ancak fonksiyon gövdesinde değer artık `string` kabul edilir. Çünkü argüman `undefined` olduğunda varsayılan değer devreye girer. Başka bir ifadeyle:

$$sonuc = \begin{cases} varsayilan, & arguman = undefined \\ arguman, & arguman \neq undefined \end{cases}$$

Önemli ayrıntı şudur: `null`, varsayılan değeri etkinleştirmez. `null` bilinçli olarak boş değer gönderildiğini, `undefined` ise değerin sağlanmadığını ifade eder.

## İki yaklaşımın karşılaştırması

| Özellik | İsteğe bağlı parametre | Varsayılan parametre |
|---|---|---|
| Sözdizimi | `deger?: string` | `deger = "örnek"` |
| Gövdedeki tip | `string \| undefined` | `string` |
| Kontrol gerekli mi? | Genellikle evet | Genellikle hayır |
| Argüman verilmezse | `undefined` kalır | Varsayılan değer atanır |
| Uygun kullanım | Yokluk anlamlıysa | Makul bir standart varsa |

## Parametre sırası ve tip çıkarımı

İsteğe bağlı bir parametre, zorunlu parametreden önce yazılamaz. Aksi hâlde hangi argümanın hangisine ait olduğu belirsizleşir:

```ts
// Hatalı: Zorunlu parametre isteğe bağlı parametreden sonra geliyor.
function raporla(format?: string, baslik: string): void {}
```

Varsayılan parametrelerde ise TypeScript, tipi başlangıç değerinden çıkarabilir. Aşağıdaki `adet` parametresi otomatik olarak `number` kabul edilir:

```ts
function sepetOzeti(urun: string, adet = 1): string {
  return `${urun}: ${adet} adet`;
}
```

Varsayılan parametre zorunlu bir parametreden önce de bulunabilir; fakat sonraki argümana ulaşmak için açıkça `undefined` göndermek gerekir:

```ts
function bildirim(sesli = true, metin: string): void {
  console.log({ sesli, metin });
}

bildirim(undefined, "Yeni mesajınız var");
```

Bu kullanım geçerli olsa da okunabilirliği azaltabilir. Genellikle zorunlu parametreleri başa, isteğe bağlı veya varsayılan parametreleri sona koymak daha temizdir.

## Nesne parametreleriyle ölçeklenmek

Seçenek sayısı arttığında uzun parametre listeleri yerine nesne kullanmak daha anlaşılırdır:

```ts
type BaglantiAyarlari = {
  adres: string;
  port?: number;
  guvenli?: boolean;
};

function baglan({
  adres,
  port = 443,
  guvenli = true
}: BaglantiAyarlari): void {
  console.log(`${adres}:${port}`, { guvenli });
}

baglan({ adres: "api.example.com" });
```

Bu modelde zorunlu ve isteğe bağlı alanlar açıkça görülür; varsayılanlar da destructuring sırasında atanır. Kısacası yokluğun anlam taşıdığı yerde `?`, güvenli bir standart değer bulunduğunda `=` kullanın. Böylece API’niz esnekleşirken TypeScript’in koruyucu kalkanı yerinde kalır.
