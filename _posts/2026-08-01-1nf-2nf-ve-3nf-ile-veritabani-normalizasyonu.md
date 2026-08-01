---
layout: post
title: "1NF, 2NF ve 3NF ile Veritabanı Normalizasyonu"
math: true
categories: 
  - Bilgi
tags: 
  - veritabanı
  - normalizasyon
  - SQL
---

Bir veritabanı ilk bakışta düzenli görünebilir; fakat müşteri adı onlarca satırda tekrarlanıyor, bir ürünün fiyatını değiştirmek için yüzlerce kayıt güncelleniyorsa masanın altında veri canavarları saklanıyor demektir. Normalizasyon, tabloları belirli kurallara göre parçalayarak veri tekrarını azaltan, ilişkileri netleştiren ve veri bütünlüğünü koruyan sistematik bir tasarım yaklaşımıdır.

``

## Normalizasyon neden gereklidir?

Normalizasyonun merkezinde **fonksiyonel bağımlılık** bulunur. Bir $X$ niteliği, $Y$ niteliğini tekil biçimde belirliyorsa bu ilişki $X \rightarrow Y$ şeklinde gösterilir. Örneğin `MusteriID`, müşterinin adını belirliyorsa:

$$MusteriID \rightarrow MusteriAdi$$

Aynı müşteri adı her sipariş satırında saklanırsa gereksiz tekrar oluşur. Basit bir tekrar oranı şöyle düşünülebilir:

$$Tekrar\ Oranı = \frac{Toplam\ Yinelenen\ Değer}{Toplam\ Kayıt}$$

Bu oran büyüdükçe depolama maliyeti ve tutarsızlık ihtimali artar. Kötü tasarlanmış tablolar üç temel anomali üretir:

| Anomali | Ne olur? | Örnek |
|---|---|---|
| Ekleme | Başka bir bilgi olmadan kayıt eklenemez | Siparişi olmayan ürün kaydedilemez |
| Güncelleme | Aynı bilgi birçok yerde değiştirilir | Müşteri adresi bazı satırlarda eski kalır |
| Silme | Bir kayıt silinirken değerli bilgi de kaybolur | Son sipariş silinince müşteri bilgisi yok olur |

## Birinci Normal Form: 1NF

Bir tablo 1NF düzeyindeyse her hücre **atomik**, yani bölünemez tek bir değer taşır. Tek hücrede `Klavye, Fare, Monitör` gibi bir ürün listesi bulunmamalıdır. Ayrıca satırlar birincil anahtarla ayırt edilmelidir.

| 1NF öncesi | 1NF sonrası |
|---|---|
| `SiparisID: 10, Urunler: Fare, Klavye` | Her ürün ayrı sipariş satırındadır |
| Tek hücrede çoklu telefon | Telefonlar ayrı satır veya tabloda tutulur |

```sql
CREATE TABLE SiparisKalemi (
    SiparisID INT,
    UrunID INT,
    Adet INT NOT NULL,
    PRIMARY KEY (SiparisID, UrunID)
);
```

Bu yapı her sipariş-ürün eşleşmesini ayrı satırda tutarak sorgulamayı ve doğrulamayı kolaylaştırır.

## İkinci Normal Form: 2NF

2NF için tablo önce 1NF olmalı ve anahtar olmayan her sütun, bileşik anahtarın **tamamına** bağımlı olmalıdır. Yukarıdaki tabloda anahtar `(SiparisID, UrunID)` ikilisidir. Eğer `UrunAdi` eklenirse yalnızca `UrunID` değerine bağlı olur:

$$UrunID \rightarrow UrunAdi$$

Bu, kısmi bağımlılıktır. Çözüm ürün bilgisini ayırmaktır:

```sql
CREATE TABLE Urun (
    UrunID INT PRIMARY KEY,
    UrunAdi VARCHAR(100) NOT NULL,
    BirimFiyat DECIMAL(10, 2) NOT NULL
);
```

Böylece ürün adı bir kez saklanır; sipariş kalemleri ürüne yabancı anahtarla bağlanır. Tek sütunlu anahtara sahip 1NF tablolar ise kısmi bağımlılık barındıramadığından genellikle doğrudan 2NF koşulunu karşılar.

## Üçüncü Normal Form: 3NF

3NF, tabloyu 2NF’ye taşıdıktan sonra **geçişli bağımlılıkları** kaldırır. Anahtar olmayan bir sütun başka bir anahtar olmayan sütunu belirlememelidir. Şu ilişkiyi düşünelim:

$$MusteriID \rightarrow SehirID \rightarrow SehirAdi$$

`SehirAdi`, müşteri anahtarına doğrudan değil `SehirID` üzerinden bağlıdır. Şehir adı müşteri tablosunda tutulursa binlerce kez tekrarlanabilir. Ayrı bir şehir tablosu daha güvenlidir:

```sql
CREATE TABLE Sehir (
    SehirID INT PRIMARY KEY,
    SehirAdi VARCHAR(80) UNIQUE NOT NULL
);

CREATE TABLE Musteri (
    MusteriID INT PRIMARY KEY,
    MusteriAdi VARCHAR(120) NOT NULL,
    SehirID INT REFERENCES Sehir(SehirID)
);
```

## Formların kısa karşılaştırması

| Form | Temel kural | Ortadan kaldırdığı sorun |
|---|---|---|
| 1NF | Hücreler atomik olmalıdır | Çok değerli alanlar |
| 2NF | Kısmi bağımlılık olmamalıdır | Bileşik anahtara eksik bağımlılık |
| 3NF | Geçişli bağımlılık olmamalıdır | Anahtar dışı sütunlar arası bağımlılık |

Normalizasyon depolamayı ve bütünlüğü iyileştirir; ancak çok sayıda tablo, raporlama sorgularında daha fazla `JOIN` gerektirebilir. Bu nedenle işlem ağırlıklı sistemlerde 3NF güçlü bir başlangıç noktasıyken, analitik sistemlerde performans amacıyla kontrollü **denormalizasyon** uygulanabilir. Altın kural şudur: Önce doğru modeli kur, ardından ölçüm yap ve yalnızca gerçek bir darboğaz varsa bilinçli tekrar ekle.
