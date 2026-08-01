---
layout: post
title: "Temel Veri Modelleme Kavramları: ER Diyagramından Veritabanı Tablolarına"
math: true
categories: 
  - Bilgi
tags: 
  - veri modelleme
  - ER diyagramı
  - veritabanı tasarımı
---

Bir veritabanı tasarlamak, gerçek dünyayı kutulara ve sütunlara sığdırma sanatıdır. Müşteriler, ürünler, siparişler veya öğrenciler gibi nesneleri doğru tanımlamazsak en hızlı veritabanı bile kısa sürede dijital bir çekmece karmaşasına dönüşebilir. Varlık-ilişki modeli, henüz SQL yazmadan önce bu dünyayı görselleştirmemizi ve olası tasarım hatalarını erkenden yakalamamızı sağlar.

``

## Kavramsal modelin temel parçaları

ER, yani **Entity-Relationship**, Türkçede **Varlık-İlişki** anlamına gelir. Modelin merkezinde üç temel kavram bulunur:

- **Varlık (Entity):** Hakkında veri saklanan, bağımsız biçimde tanımlanabilen nesnedir. `Müşteri`, `Ürün` ve `Sipariş` örnek gösterilebilir.
- **Nitelik (Attribute):** Varlığı açıklayan özelliktir. Bir müşterinin adı, e-posta adresi veya doğum tarihi birer niteliktir.
- **İlişki (Relationship):** Varlıkların birbirleriyle nasıl bağlantı kurduğunu gösterir. Örneğin müşteri bir sipariş verir.

Matematiksel açıdan bir varlık kümesini $E$, nitelikleri ise bu kümedeki elemanları açıklayan fonksiyonlar gibi düşünebiliriz. İki varlık arasındaki ilişki, $R \subseteq E_1 \times E_2$ biçiminde ifade edilebilir. Yani ilişki, iki varlık kümesinin Kartezyen çarpımından seçilmiş anlamlı eşleşmelerden oluşur.

| ER kavramı | Gerçek dünya örneği | İlişkisel karşılığı |
|---|---|---|
| Varlık | Müşteri | Tablo |
| Nitelik | E-posta adresi | Sütun |
| Varlık örneği | Ayşe Yılmaz | Satır |
| Anahtar | Müşteri numarası | Primary Key |
| İlişki | Müşteri sipariş verir | Foreign Key veya ara tablo |

## Anahtarlar neden önemlidir?

Her varlık örneğinin benzersiz biçimde ayırt edilmesi gerekir. Bu amaçla kullanılan niteliğe **birincil anahtar** denir. İki müşterinin adı aynı olabilir; fakat `musteri_id` değerleri aynı olamaz. Başka bir tabloya bağlanmak için taşınan anahtar ise **yabancı anahtar** adını alır.

Bir anahtar tek sütundan oluşabileceği gibi birden fazla sütunun birleşiminden de oluşabilir. İki sütunlu birleşik bir anahtarın benzersizlik koşulu kabaca $(a,b)_i \neq (a,b)_j$ şeklinde gösterilebilir. Burada tek tek değerlerin değil, ikilinin benzersiz olması yeterlidir.

## Çokluk ve ilişki türleri

Çokluk, bir varlık örneğinin karşı tarafta kaç örnekle bağlanabileceğini açıklar.

| İlişki | Gösterim | Örnek | Tabloya dönüşüm |
|---|---:|---|---|
| Bire bir | $1:1$ | Kişi–Pasaport | Taraflardan birine yabancı anahtar |
| Bire çok | $1:N$ | Müşteri–Sipariş | Çok tarafına yabancı anahtar |
| Çoka çok | $N:M$ | Sipariş–Ürün | Ara bağlantı tablosu |

Özellikle $N:M$ ilişkiler doğrudan tek bir yabancı anahtarla kurulamaz. Bir siparişte birçok ürün, bir ürün de birçok siparişte bulunabileceği için `SiparisKalemi` gibi bir ara varlık gerekir. Bu varlık miktar ve satış fiyatı gibi ilişkinin kendi niteliklerini de saklayabilir.

## ER modelini tablolara dönüştürmek

Örnek modelde müşteri sipariş verir, sipariş ise ürünleri içerir. Bunun mantıksal SQL karşılığı şöyle kurulabilir:

```sql
CREATE TABLE Musteri (
    musteri_id INT PRIMARY KEY,
    ad VARCHAR(100) NOT NULL,
    eposta VARCHAR(150) UNIQUE
);

CREATE TABLE Siparis (
    siparis_id INT PRIMARY KEY,
    musteri_id INT NOT NULL,
    tarih DATE NOT NULL,
    FOREIGN KEY (musteri_id) REFERENCES Musteri(musteri_id)
);

CREATE TABLE SiparisKalemi (
    siparis_id INT,
    urun_id INT,
    miktar INT NOT NULL CHECK (miktar > 0),
    birim_fiyat DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (siparis_id, urun_id)
);
```

Bu kodda `Siparis.musteri_id`, $1:N$ ilişkisinin çok tarafına yerleştirilmiştir. `SiparisKalemi` ise çoka çok ilişkiyi çözer; birleşik anahtarı aynı ürünün aynı siparişe yanlışlıkla iki kez eklenmesini önler.

## Sağlam model için kısa kontrol listesi

Tekrarlanan verileri azaltmak için her sütun tek bir gerçeği temsil etmeli, türetilebilen değerler gereksiz yere saklanmamalı ve yabancı anahtarlar bağlantı bütünlüğünü korumalıdır. Ayrıca opsiyonel ilişkiler ile zorunlu ilişkiler ayırt edilmelidir: Her siparişin müşterisi olmalıysa yabancı anahtar `NOT NULL` tanımlanır.

İyi bir ER diyagramı yalnızca güzel kutulardan oluşmaz; iş kurallarının görsel sözleşmesidir. Önce varlıkları, ardından anahtarları ve çoklukları belirlemek, SQL aşamasında daha tutarlı, genişletilebilir ve bakımı kolay bir veritabanı ortaya çıkarır.
