---
layout: post
title: "NoSQL ve MongoDB ile Doküman Tabanlı Veri Modelleme"
math: true
categories: 
  - Bilgi
tags: 
  - NoSQL
  - MongoDB
  - Veri Modelleme
---

Bir e-ticaret ürününün renkleri, kampanyaları, kullanıcı yorumları ve kategoriye göre değişen özellikleri olduğunu düşünün. Bu verileri ilişkisel tablolara dağıtmak mümkündür; ancak tablo sayısı ve JOIN işlemleri kısa sürede küçük bir yapboza dönüşebilir. Doküman tabanlı veritabanları, ilişkili bilgileri JSON benzeri tek bir yapı içinde saklayarak bu karmaşıklığa farklı bir çözüm sunar. MongoDB bu yaklaşımın en tanınmış temsilcilerindendir; fakat sunduğu esneklik, kuralsız veri depolamak anlamına gelmez.

``

## Tablo yerine doküman düşünmek

İlişkisel modelde veriler satır, sütun ve tablolarla temsil edilir. MongoDB ise verileri **collection** adı verilen koleksiyonlarda, BSON biçimindeki dokümanlar olarak saklar. BSON; JSON yapısını tarih, ondalık sayı ve ikili veri gibi ek türlerle genişletir.

Örnek bir ürün dokümanı şöyle olabilir:

```json
{
  "_id": "urun-42",
  "ad": "Mekanik Klavye",
  "fiyat": 2499.90,
  "stok": 18,
  "ozellikler": {
    "switch": "Brown",
    "baglanti": ["USB-C", "Bluetooth"]
  },
  "yorumlar": [
    {"kullanici": "Ada", "puan": 5}
  ]
}
```

Bu doküman, ürünün temel alanlarını, iç içe nesnelerini ve dizilerini birlikte taşır. Uygulama ürünü okuduğunda çoğu bilgiyi tek sorguyla elde edebilir.

| Özellik | İlişkisel SQL | Doküman tabanlı NoSQL |
|---|---|---|
| Yapı | Önceden tanımlı şema | Esnek doküman yapısı |
| İlişkiler | JOIN ve yabancı anahtar | Gömme veya referans |
| Ölçekleme | Genellikle dikey | Yatay ölçeklemeye uygun |
| Tutarlılık | Güçlü transaction geleneği | Kullanıma göre ayarlanabilir |
| İdeal kullanım | Düzenli, ilişkisel veriler | Değişken ve iç içe veriler |

## Şemasız, kuralsız demek değildir

MongoDB için sıkça “şemasız” ifadesi kullanılır. Daha doğru tanım **esnek şemalı**dır. Aynı koleksiyondaki dokümanlar farklı alanlar taşıyabilir; ancak uygulama kodu, indeksler ve doğrulama kuralları yine ortak bir veri sözleşmesine ihtiyaç duyar. Aksi hâlde `fiyat` alanı bir dokümanda sayı, diğerinde metin olabilir ve raporlama sırasında sürpriz yumurtaya dönüşebilir.

Veri doğrulama kurallarıyla bu risk azaltılabilir:

```javascript
db.createCollection("urunler", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["ad", "fiyat", "stok"],
      properties: {
        ad: { bsonType: "string" },
        fiyat: { bsonType: "double", minimum: 0 },
        stok: { bsonType: "int", minimum: 0 }
      }
    }
  }
})
```

Bu kod, zorunlu alanları ve kabul edilen veri türlerini belirleyerek esneklik ile güvenilirlik arasında denge kurar.

## Gömme mi, referans mı?

Doküman modellemenin kritik kararı, ilişkili veriyi ana dokümana **gömmek** veya başka koleksiyona koyup **referans vermektir**. Birlikte okunan ve sınırlı büyüyen veriler gömülebilir. Sürekli büyüyen, bağımsız güncellenen ya da birçok doküman tarafından paylaşılan veriler referanslanmalıdır.

| Durum | Tercih |
|---|---|
| Sipariş içindeki teslimat adresi | Gömme |
| Ürünün birkaç teknik özelliği | Gömme |
| Milyonlarca kullanıcı yorumu | Referans |
| Birçok üründe kullanılan marka | Referans |

Basit bir karar ölçüsü şöyle düşünülebilir:

$$Maliyet = Okuma\ Sayısı \times JOIN\ Yükü + Güncelleme\ Sayısı \times Tekrar\ Yükü$$

Gömme, okuma maliyetini azaltırken tekrarlanan verinin güncelleme maliyetini artırabilir. Referanslama ise tekrarı azaltır fakat ek sorgu veya `$lookup` gerektirebilir. Bu nedenle model, nesnelerden önce uygulamanın **erişim desenlerine** göre tasarlanmalıdır.

## Sorgulama ve indeksleme

İç içe alanlar nokta gösterimiyle sorgulanabilir:

```javascript
db.urunler.find({
  "ozellikler.baglanti": "Bluetooth",
  fiyat: { $lte: 3000 }
})
```

Sorgu Bluetooth destekleyen ve belirlenen fiyatın altındaki ürünleri getirir. Sık kullanılan alanlarda indeks oluşturmak performansı yükseltir:

```javascript
db.urunler.createIndex({
  "ozellikler.baglanti": 1,
  fiyat: 1
})
```

İndeksler okumayı hızlandırır; ancak disk kullanımı ile yazma maliyetini artırır. Dolayısıyla “her alana indeks” yaklaşımı, veritabanına gereksiz ağırlık bağlamak gibidir.

Sonuç olarak MongoDB, değişken yapılı ve hızla gelişen uygulamalarda güçlü bir seçenektir. Başarılı bir doküman modeli; veri ilişkilerini, büyüme hızını, atomik güncelleme sınırlarını ve sorgu alışkanlıklarını birlikte değerlendirir. NoSQL, SQL’in rakibi değil; doğru problemde kullanılan farklı bir araçtır.
