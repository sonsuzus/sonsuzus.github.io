---
layout: post
title: "TypeScript Utility Types: Partial, Pick ve Omit ile Akıllı Veri Modelleri"
math: true
categories: 
  - Bilgi
tags: 
  - TypeScript
  - Utility Types
  - Tip Güvenliği
---

Bir kullanıcı modeliniz olduğunu ve kayıt, güncelleme, listeleme gibi her işlem için neredeyse aynı arayüzü tekrar tekrar yazdığınızı düşünün. TypeScript’in yerleşik yardımcı tipleri tam bu noktada devreye girer. `Partial`, `Pick` ve `Omit`, mevcut bir veri modelini kopyalamadan dönüştürmemizi sağlar; böylece hem kod tekrarı azalır hem de modeller arasındaki ilişki derleyici tarafından korunur.
``
## Yardımcı tiplerin temel mantığı

Utility Type adı verilen bu araçlar, çalışma zamanında çalışan JavaScript fonksiyonları değildir. Yalnızca TypeScript’in tip sistemi içinde işlem yaparlar ve derleme sonrasında üretilen JavaScript kodunda görünmezler. Başka bir deyişle görevleri veriyi değil, verinin kabul edilen **şeklini** dönüştürmektir.

Bir arayüzdeki özellikler kümesini $K$, elde edilen yeni tipi ise $T'$ olarak düşünelim. Yardımcı tipler kabaca şu dönüşümleri gerçekleştirir:

- `Partial<T>`: $T$ içindeki bütün özellikleri isteğe bağlı yapar.
- `Pick<T, K>`: Yalnızca $K$ kümesindeki özellikleri seçer.
- `Omit<T, K>`: $K$ kümesindeki özellikleri modelden çıkarır.

| Yardımcı tip | Gerçekleştirdiği işlem | Yaygın kullanım |
|---|---|---|
| `Partial<T>` | Tüm alanları opsiyonel yapar | Güncelleme verisi |
| `Pick<T, K>` | Belirtilen alanları seçer | Özet veya liste modeli |
| `Omit<T, K>` | Belirtilen alanları dışarıda bırakır | Oluşturma formu, güvenli çıktı |

Örneklerimizde kullanacağımız ana modeli tanımlayalım:

```ts
interface Kullanici {
  id: number;
  ad: string;
  email: string;
  sifre: string;
  aktif: boolean;
}
```

## Partial: Her alan zorunlu olmak zorunda değil

Bir kullanıcı güncellenirken bütün alanları yeniden göndermek anlamsızdır. Sadece değişen alanları kabul etmek için `Partial` kullanılabilir:

```ts
type KullaniciGuncelleme = Partial<Kullanici>;

function kullaniciGuncelle(
  id: number,
  veri: KullaniciGuncelleme
) {
  console.log(id, veri);
}

kullaniciGuncelle(7, { ad: "Ada", aktif: true });
```

Bu dönüşümden sonra alanların tipleri korunur fakat her biri `?` ile tanımlanmış gibi isteğe bağlı hâle gelir. Yani `aktif` alanına yanlışlıkla metin vermek hâlâ hatadır. `Partial`, tip güvenliğini kaldırmaz; yalnızca zorunluluğu gevşetir.

## Pick: İhtiyacın olanı seç

Bir kullanıcı kartında şifreye, hatta çoğu zaman e-posta adresine ihtiyaç yoktur. `Pick`, ana modelden yalnızca belirtilen anahtarları toplar:

```ts
type KullaniciKarti = Pick<Kullanici, "id" | "ad" | "aktif">;

const kart: KullaniciKarti = {
  id: 7,
  ad: "Ada",
  aktif: true
};
```

Buradaki anahtar birleşimi $K = \{id, ad, aktif\}$ şeklinde düşünülebilir. Sonuç modelinde yalnızca bu kümedeki alanlar bulunur. Ana arayüzde `ad` tipinin değişmesi durumunda türetilen tip de otomatik olarak güncellenir.

## Omit: İstenmeyen alanları çıkar

`Pick` dahil edilecekleri, `Omit` ise hariç tutulacakları belirtir. Yeni kullanıcı oluşturulurken `id` sunucu tarafından üretilecekse aşağıdaki model pratiktir:

```ts
type YeniKullanici = Omit<Kullanici, "id" | "aktif">;

const yeniKayit: YeniKullanici = {
  ad: "Linus",
  email: "linus@example.com",
  sifre: "guclu-bir-sifre"
};
```

Matematiksel açıdan sonuç anahtarları $Keys(T) - K$ olarak ifade edilebilir. Özellikle API yanıtlarından `sifre` gibi hassas alanları ayırırken bu yaklaşım oldukça okunaklıdır. Yine de bunun yalnızca tip düzeyinde koruma sağladığını unutmayın: `Omit`, çalışma zamanında nesneden alan silmez.

## Yardımcı tipleri birlikte kullanmak

Bu araçlar iç içe geçirilerek daha özel modeller üretilebilir:

```ts
type ProfilDegisikligi = Partial<
  Pick<Kullanici, "ad" | "email">
>;

const degisiklik: ProfilDegisikligi = {
  email: "yeni@example.com"
};
```

Burada önce `ad` ve `email` seçilir, ardından ikisi de isteğe bağlı yapılır. Okuma sırası içten dışadır: önce `Pick`, sonra `Partial` çalışır.

Utility Types, ana modeli tek bir doğruluk kaynağı hâline getirir. Küçük projelerde birkaç satır kazandırırken büyük projelerde tutarsız modelleri, unutulan alanları ve zahmetli yeniden düzenlemeleri önler. Kısacası yeni bir arayüzü kopyalayıp budamadan önce şu soruyu sorun: Bu model `Partial`, `Pick` veya `Omit` ile türetilebilir mi?
