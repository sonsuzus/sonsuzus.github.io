---
layout: post
title: "Temel Veri Tipleriyle Güvenli Kodun Temelleri"
math: true
categories: 
  - Bilgi
tags: 
  - veri tipleri
  - TypeScript
  - tip güvenliği
---

Bir programın dünyayı nasıl algıladığını hiç düşündünüz mü? Bizim için yaş, isim ve ışığın açık olup olmadığı farklı kavramlardır. Bilgisayar açısından da bunlar sırasıyla sayı, metin ve mantıksal değer olarak temsil edilir. Temel veri tipleri, verinin anlamını belirleyerek yanlış değerlerin daha kod çalışmadan yakalanmasını sağlar. Kısacası tipler, değişkenlerin kapısında bekleyen seçici güvenlik görevlileridir.

``

## Temel veri tipi nedir?

Bir veri tipi, bellekte saklanan değerin nasıl yorumlanacağını ve üzerinde hangi işlemlerin yapılabileceğini tanımlar. Örneğin `10` sayısına `5` eklemek matematiksel toplama üretirken, `"10"` metnine `"5"` eklemek çoğu dilde `"105"` sonucunu verir.

Bir değişkeni matematiksel olarak değer kümesiyle ifade edebiliriz. `boolean` tipindeki bir $b$ değişkeninin alabileceği değerler şöyledir:

$$b \in \{true, false\}$$

Benzer biçimde, 0 ile 120 arasında sınırlandırılmış bir yaş değeri için hedeflenen küme şudur:

$$yas \in \mathbb{Z}, \quad 0 \le yas \le 120$$

Tip sistemi ilk bölümde değerin sayı olmasını garanti edebilir. Aralık gibi daha özel iş kuralları ise doğrulama kodları veya gelişmiş tip teknikleri gerektirir.

## En yaygın temel tipler

| Tip | Örnek | Kullanım alanı | Uygun olmayan değer |
|---|---|---|---|
| `number` | `42`, `3.14` | Yaş, fiyat, puan | `"kırk iki"` |
| `string` | `"Ada"` | İsim, açıklama, adres | Sayısal hesaplama |
| `boolean` | `true` | Açık/kapalı durumları | `"belki"` |
| `null` | `null` | Bilinçli olarak boş değer | Gerçek veri |
| `undefined` | `undefined` | Henüz atanmamış değer | Kesin sonuç |
| `bigint` | `9007199254740993n` | Çok büyük tam sayılar | Ondalıklı işlemler |
| `symbol` | `Symbol("id")` | Benzersiz anahtarlar | Kullanıcı metni |

`null` ve `undefined` birbirine benzese de aynı şeyi anlatmaz. `null`, geliştiricinin bilinçli biçimde “burada değer yok” demesidir. `undefined` ise değerin henüz tanımlanmadığını belirtir. Bu ayrım, özellikle API yanıtlarında oldukça önemlidir.

## Tip kısıtlaması neden güvenlidir?

Dinamik tipli JavaScript'te aşağıdaki değişken önce sayı, ardından metin olabilir:

```javascript
let puan = 90;
puan = "doksan";
```

Kod sözdizimi açısından geçerlidir; ancak daha sonra `puan / 2` işlemi yapılırsa beklenmeyen bir sonuç oluşabilir. TypeScript ile değişkenin kabul edeceği değer türü baştan belirtilir:

```typescript
let puan: number = 90;
puan = 100;       // Geçerli
// puan = "doksan"; // Derleme hatası

const basariliMi: boolean = puan >= 50;
const mesaj: string = basariliMi ? "Tebrikler!" : "Tekrar dene";
```

Burada `puan` yalnızca sayı, `basariliMi` yalnızca mantıksal değer ve `mesaj` yalnızca metin kabul eder. Hatalı atama yorumdan çıkarılırsa TypeScript, program çalıştırılmadan geliştiriciyi uyarır. Böylece hata üretim ortamında kullanıcıyla tanışmadan önce yakalanır.

## Tip çıkarımı ve açık tanımlama

TypeScript her zaman tipin açıkça yazılmasını istemez:

```typescript
let kullaniciAdi = "deniz"; // string olarak çıkarılır
let girisSayisi = 3;        // number olarak çıkarılır
let aktif = true;           // boolean olarak çıkarılır
```

Bu mekanizmaya **tip çıkarımı** denir. Başlangıç değeri tip hakkında yeterli bilgi veriyorsa kısa ve okunaklı kod sağlar. Fonksiyon parametrelerinde ise açık tip kullanmak daha güvenlidir:

```typescript
function indirimliFiyat(fiyat: number, oran: number): number {
  return fiyat * (1 - oran);
}

const sonuc = indirimliFiyat(500, 0.2); // 400
```

Formül $F_{son} = F \times (1-r)$ şeklindedir. Tipler `fiyat` ve `oran` değerlerinin metin olmasını engeller; fakat oranın 0 ile 1 arasında olduğunu tek başına doğrulamaz. Bu nedenle çalışma zamanı kontrolleri tip sisteminin tamamlayıcısıdır.

## Sonuç

Temel veri tipleri yalnızca sözdizimsel ayrıntılar değildir; programın veri sözleşmesini oluşturur. Doğru tip seçimi otomatik tamamlama kalitesini artırır, yeniden düzenlemeyi kolaylaştırır ve hataları erkenden görünür kılar. Değişkene “her şeyi kabul et” demek pratik görünebilir, fakat güvenli yazılım çoğu zaman doğru yerde nazikçe “hayır” diyebilen yazılımdır.
