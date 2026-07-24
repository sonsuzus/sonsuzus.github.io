---
layout: post
title: "Yapılar (Structs) ve Veri Odaklı Tasarım: Veriyi Kahraman Yapmak"
math: true
categories: 
  - Bilgi
tags: 
  - struct
  - veri-odaklı-tasarım
  - programlama
---

Programlamada bazen bir şeyi nesne gibi davranışlarıyla değil, taşıdığı verilerle düşünmek daha doğrudur. İşte yapılar, yani structs, tam bu noktada sahneye çıkar. Bir koordinat, renk, sağlık değeri, tarih aralığı veya fiziksel hız vektörü düşünün: Bunlar genellikle küçük, anlamlı ve birlikte taşınması gereken veri paketleridir. Struct, farklı tiplerdeki alanları mantıksal bir bütün halinde gruplar ve özellikle veri odaklı tasarımda gereksiz soyutlama sisini dağıtarak işlemciye daha dost bir programlama modeli sunar.
``

## Struct nedir?

Struct, birden fazla veriyi tek bir özel tip altında toplamanızı sağlayan bir yapıdır. Sınıfa benzer görünür; alanları, metotları ve özellikleri olabilir. Ancak birçok dilde struct kavramsal olarak daha hafif, daha doğrudan ve veri merkezlidir. Özellikle C, C++, C# ve Rust gibi dillerde struct, bellekteki verinin düzenini anlamak açısından çok önemlidir.

Basit bir örnekle başlayalım:

```csharp
public struct Health
{
    public int Current;
    public int Maximum;

    public float Ratio
    {
        get { return (float)Current / Maximum; }
    }
}
```

Bu struct, bir karakterin can bilgisini taşır. `Current` ve `Maximum` ayrı ayrı değişkenler olabilirdi; fakat birlikte anlamlı oldukları için tek bir tip altında toplanmaları kodu daha okunabilir yapar.

## Struct ile class arasındaki temel farklar

Her dilde ayrıntılar değişebilir ama genel düşünce şudur: class çoğu zaman kimlik ve davranış odaklıdır, struct ise veri odaklıdır.

| Özellik | Struct | Class |
|---|---|---|
| Ana fikir | Veri gruplama | Nesne ve davranış modelleme |
| Kullanım alanı | Küçük, anlamlı veri paketleri | Karmaşık iş kuralları ve ilişkiler |
| Bellek yaklaşımı | Daha düz ve kompakt olabilir | Referanslar ve dolaylı erişim yaygındır |
| Zihinsel model | Bu veri ne? | Bu nesne ne yapar? |

Örneğin bir oyun motorunda `Position`, `Velocity`, `Health` gibi tipler struct olmaya çok uygundur. Buna karşılık `InventoryManager` veya `PaymentService` gibi davranış yönü ağır bileşenler class olarak daha anlamlıdır.

## Veri odaklı tasarımın mantığı

Veri odaklı tasarım, programı önce verinin şekline ve işlenme biçimine göre düşünmektir. Geleneksel nesne yönelimli yaklaşımda sıkça şu soru sorulur: Bu nesnenin hangi metotları var? Veri odaklı yaklaşım ise şunu sorar: Hangi veriyi, hangi sırayla, ne kadar sık işleyeceğim?

Performans açısından kritik nokta bellek erişimidir. Modern işlemciler veriyi tek tek sihirli şekilde değil, cache line denilen bloklarla okur. Basitçe düşünürsek:

$T \approx N \times C_{access}$

Burada $N$ erişilen veri sayısı, $C_{access}$ ise her erişimin maliyetidir. Eğer veriler bellekte dağınıksa $C_{access}$ artar. Veriler ardışık ve kompakt ise işlemci cache daha verimli çalışır.

| Tasarım | Veri düzeni | Avantaj | Dezavantaj |
|---|---|---|---|
| Nesne odaklı | Dağınık referanslar olabilir | Modelleme kolaydır | Cache kaçırma artabilir |
| Veri odaklı | Ardışık diziler yaygındır | Yüksek performans | Başta daha fazla plan ister |

## Struct ile daha düzenli veri modeli

Diyelim ki çok sayıda karakterin sağlık bilgisini güncelliyoruz:

```csharp
public struct PlayerStats
{
    public int Health;
    public int Armor;
    public float Speed;
}

public static void ApplyDamage(ref PlayerStats stats, int damage)
{
    int reduced = damage - stats.Armor;
    if (reduced < 0) reduced = 0;
    stats.Health -= reduced;
}
```

Burada `PlayerStats`, karaktere ait temel sayısal değerleri bir araya getirir. `ApplyDamage` fonksiyonu ise struct üzerinde işlem yapar. `ref` kullanımı, bazı dillerde veya senaryolarda kopyalama maliyetini azaltmak için tercih edilir. Çünkü struct değer gibi taşındığında kopyalanabilir; küçük structlarda bu harika, büyük structlarda ise dikkat gerektirir.

## Struct seçerken dikkat edilmesi gerekenler

Struct kullanmak her derde deva değildir. Küçük ve değişmez veri tiplerinde çok güçlüdür; fakat devasa veri paketleri oluşturursanız kopyalama maliyeti can sıkabilir. Pratik bir sezgi olarak, struct veri taşımalı; karmaşık yaşam döngüsü, miras hiyerarşisi veya yoğun davranış gerekiyorsa class düşünülmelidir.

| Durum | Struct iyi fikir mi? | Neden |
|---|---:|---|
| 2D nokta, renk, para miktarı | Evet | Küçük ve anlamlı veri |
| 50 alanlı kullanıcı profili | Genelde hayır | Kopyalama ve karmaşıklık artar |
| Oyun bileşen verisi | Evet | Veri odaklı sistemlere uygundur |
| Servis sınıfı | Hayır | Davranış ve bağımlılık baskındır |

## Sonuç

Structs, programlamada veriyi ciddiye almanın zarif yollarından biridir. Sınıflar dünyayı nesneler ve davranışlarla anlatırken, structlar küçük veri gerçekliklerini net ve kompakt biçimde ifade eder. Veri odaklı tasarımda amaç, kodu sadece güzel göstermek değil, verinin bellekte nasıl yaşadığını da hesaba katmaktır. Kısacası: Eğer programınız bir mutfaksa, classlar aşçı olabilir; structlar ise düzenli kesilmiş malzemelerdir. Lezzetli ve hızlı yemek için ikisine de ihtiyaç vardır, ama hangi malzemenin nerede durduğunu bilmek oyunu değiştirir.
