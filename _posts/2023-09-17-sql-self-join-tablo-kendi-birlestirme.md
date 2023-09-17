---
title:  SQL’de Self Join Kullanımı (Tabloyu Kendisi ile Birleştirme İşlemi)
author: sonsuz
date: 2023-09-17 22:06:45 +0300
categories: [Program,SQL]
tags: [programlama,sql,join,veri,veri tabanı,tablo,birleştirme]
image: sql/petronas-twin-towers.png
---


İlişkisel veri tabanları ile çalışırken veriler tek bir tabloda olabildiği gibi birden fazla tabloda da bulunabilir. JOIN işlemleri ile birden fazla tablo, ortak bulunan kolonlar yardımı ile birleştirilerek sorgulama işlemleri yapılabilmektedir. 

Self Join ifadesi SQL’de bulunan **özel bir JOIN** işlemidir. Birbirinden farklı iki veya daha çok tablonun birleştirildiği diğer JOIN metotlarının aksine, Self Join işleminde **tek bir tablo vardır ve bu tablo kendisi ile birleştirilir.** Join işlemi tablo ve tablonun bir kopyası ile gerçekleşir.

![](sql/sql-join-tipleri.png)

[SQL’de Join Tipleri](https://www.educba.com/joins-in-mysql/)

## Self Join söz dizimi (syntax)

SQL’de Self Join işleminin syntax’ı şu şekildedir:

```sql
SELECT 
         t1.kolon_1, 
         t1.kolon_2, 
         t2.kolon_3, 
         ............
         t2.kolon_n
FROM tablo1 t1, 
INNER JOIN tablo1 t2 
ON t1.ortak_kolon = t2.ortak_kolon;

```

* Klasik bir join işleminde iki farklı tablo ile birleştirme işlemi olacağı için, **FROM** ifadesinde birleşme işlemine girecek ilk tablo, **JOIN** ifadesinde ise ikinci tablo ismi verilir. Self Join işleminde tablo kendisi ile birleşeceği için FROM ve JOIN ifadelerinde aynı tablonun adı yer alır ve karmaşa olmaması adına her iki tablo için de **ayrı bir** **takma isim (alias)** verilir.
* **SELECT** ifadesi ile tablodan seçilecek olan kolonlar girilir. Kolonlar seçilirken tabloların takma isimleri de kullanılır.
* ON ifadesinde ise tablonun takma isimleri kullanılarak tablonun birleşeceği kolonlar belirtilir.

## SQL’de Self Join ifadesi hangi durumlarda kullanılır?

Self Join ifadesi sık karşılaşılmasa da bilinmesi faydalı ve spesifik kullanımları olan bir yapıdır. İlk başta kulağa biraz farklı gelen bu konsept, bir tablo içerisinde yer alan hiyerarşik verileri sorgulamak veya satırları karşılaştırmak için kullanışlıdır. 

Yazının geri kalanında teorik olarak bahsettiğimiz self join ifadesini gerçek senaryolar üzerinde uygulayacağız. Uygulama için Microsoft tarafından geliştirilen ve SQL eğitimlerinde sıkça kullanılan bir veri tabanı olan Northwind veri tabanının Türkçe versiyonunu kullanacağız.

---

**Örnek veri seti:** Northwind Veri Tabanı (Türkçe)

[Örnek Veriyi İndir](https://sonsuzus.github.io/dosya/Northwind.rar)

---

### Hiyerarşiye sahip verileri sorgulamak.

Self Join ifadesinin ilk kullanım alanı, aynı tabloda bulunan hiyerarşik veriler için sorgulama yapmaktır. Hiyerarşik veriye:

* Bir e-ticaret şirketinin satış verilerinin olduğu tabloda bulunan ürünler ve ürün kategorileri,
* Bir şirketin çalışanlarının bulunduğu tabloda yer alan çalışanlar ve departman yöneticileri,
* Futbol takımları ile ilgili bilgilerin bulunduğu bir tabloda yer alan takım ve takımların katıldığı ligler örnek olarak gösterilebilir.

Buradaki kilit nokta, **her iki öğenin de (çalışan ve departman yöneticileri) ay****nı kolon içerisinde** yer almasıdır. 

Northwind veri tabanında bulunan Personeller (Employees) tablosunda, hayali bir şirkette çalışanların bilgileri yer alır. Personeller tablosunda, çalışanların adı, soyadı, kime bağlı çalıştıkları, ünvanları gibi bilgiler bulunur. Bu tabloyu daha yakından tanımak için önce tüm kolonlarını çağıralım.

```sql
SELECT *
FROM dbo.Personeller;

```

![](sql/northwind-personeller-tablosu.png)

Personeller tablosunda PersonalID, çalışanın adı, soyadı, doğum tarihi, adresi vs. gibi bir sürü bilgi bulunmaktadır.

Bu tabloda bulunan personellerin PersonalID, adı, soyadı, ünvanı ve bağlı çalıştıkları yöneticiyi sorgulayalım.

```sql
SELECT PersonelID, Adi, SoyAdi, Unvan, BagliCalistigiKisi
FROM dbo.Personeller;

```

![](sql/personeller-northwind-ozet-1.png)

* Personeller tablosunda bulunan her bir kişinin unvanından, bu tablonun aslında bir satış ekibi ve üyelerinden oluştuğunu anlıyoruz.
* Her bir çalışanın en sağında ise bağlı olduğu yönetici bulunuyor.
* Örnek olarak, ilk sırada bulunan 1 numaralı kayıt Nancy Davolio’nun yöneticisi 2 numaralı kayıt olan Andrew Fuller’dır.
* Listede Andrew Fuller hariç tüm kişilerin bir yöneticisi bulunuyor. Andrew Fuller bu organizasyonda en tepede bulunduğu için bir yöneticisi bulunmuyor.

**Her bir çalışan ve çalışanın bağlı olduğu yöneticinin adını nasıl sorgulayabiliriz?**

Bu sorguyu yapabilmek için Self Join işlemi yapmamız gerekmektedir.

```sql
SELECT p1.Adi + ' ' + p1.SoyAdi AS calisan, p2.Adi + ' ' + p2.SoyAdi AS yonetici
FROM dbo.Personeller p1
INNER JOIN dbo.Personeller p2
ON p1.BagliCalistigiKisi = p2.PersonelID;

```

![](sql/calisan-yonetici-self-join.png)

* Self Join işleminde tablonun kendi kopyası ile birleşme işlemine girdiğini söylemiştik. Bunu akılda tutmakta fayda var.
* **FROM ve INNER JOIN** ifadelerinde tablo adını belirttik. Tablonun kendisine ve kopyasına ihtiyaç duyduğumuz için karışıklık olmaması adına orijinal tabloya p1, kopyaya ise p2 takma adını verdik. Bu örnekte ilk tablo bizim için **“çalışanlar”**, ikinci tablo da **“yöneticiler”** listesi gibi hizmet edecek desek yanlış olmaz.
* **ON** ifadesinde birleşme işleminin yapılacağı her iki tabloda ortak bulunan kolonun adını girmemiz gerekiyor. Burada kritik olan bir nokta ise **bağlantının nasıl yapılacağı.**
* Yapmak istediğimiz işlem ilk tablodaki **“BagliCalistigiKisi”** kolonundaki değerlerle, ikinci tablodan **“PersonalID”** kolonundaki değerleri eşleştirmek.
* **SELECT** ifadesinde ise her iki tablodan da ad ve soyad değerlerini listeledik. Metin ifadeleri birleştirmek için **“+ (toplama)”** operatörünü kullandık. Okuma kolaylığı olmasını açısından **‘ ‘ (boşluk)** ekledik. İlk tablodan gelen ad-soyadı çalışan, ikinci tablodan gelenleri ise yönetici olarak isimlendirdik.

![](sql/calisan-yonetici-self-join-1.png)

Yukarıdaki örnekte kullandığımız bağlantı mantığını şu şekilde görselleştirebiliriz:

![](sql/self-join-personeller-1.png)

Dikkatinizi çektiğini umduğum bir nokta var. Personeller tablosundaki tüm kayıtları listelediğimde tabloda 9 kayıt vardı. Birleştirme işleminden sonra ise oluşan tabloda sadece 8 kayıt var. Peki neden bir kayıt eksik?

Personeller tablosunu tanıtırken, Andrew Fuller isimli bir personelden bahsetmiştik. Bu personelin, satış organizasyonunun başında olduğu için yöneticisi olmadığını belirtmiştik. 

* Self Join işleminde birleştirme biçimi olarak **“INNER JOIN”** yapısını kullanmıştık. Inner Join her iki tabloda da ortak eşleşme olduğu durumda birleştirme işlemini gerçekleştirir.
* Andrew Fuller isimli personelin BagliCalistigiKisi kolonundaki değeri “NULL”dır.
* Bu nedenle, eşleşme yapılamadığı için Andrew Fuller’ı tabloda görememekteyiz.

Bu sorunu aşmak için Self Join işleminde **“LEFT JOIN”** birleşme yapısını kullanacağız. Left Join işleminde, soldaki yani birinci tabloda bulunan tüm kayıtlar, eşleşme bulunamadığı durumda bile listelenecektir. Eşleşme olmayan kayıtlar için ise **“NULL” değeri otomatik olarak** atanacaktır.

```sql
SELECT p1.Adi + ' ' + p1.SoyAdi AS calisan, p2.Adi + ' ' + p2.SoyAdi AS yonetici
FROM dbo.Personeller p1
LEFT JOIN dbo.Personeller p2
ON p1.BagliCalistigiKisi = p2.PersonelID;

```

![](sql/calisan-yonetici-self-join-left.png)

Bir önceki işlem için yazdığım kodun sadece “INNER JOIN” bölümünü “LEFT JOIN” olarak güncelledim. Yeni oluşan tabloda Andrew Fuller da eklendi. Herhangi bir eşleşme olmadığı için yönetici kolonundaki değeri “NULL” oldu.

### Bir tablo içindeki satırları karşılaştırmak.

Self Join işlemi bir tablo içerisindeki satırları karşılaştırmak için kullanılabilir. Mesela bir tablo içerisinde şirketlere ait bilgilerin olduğunu varsayalım. Bu şirketlerden aynı şehirde bulunanları bulmak için self join işlemi kullanılmalıdır. 

Northwind veri tabanında bulunan bir diğer tablo ise Müşteriler tablosudur. Bu tablo içerisinde müşteri olarak kayıtlı şirketler ve bu şirketlere ait ülke, adres, temsilci gibi bilgiler yer alır.

```sql
SELECT *
FROM dbo.Musteriler;

```

![](sql/northwind-musteriler-tablosu.png)

Bu tabloda yer alan ve aynı ülkede bulunan müşterileri yani şirketleri sorgulayalım.

```sql
SELECT  m1.MusteriID, m1.Ulke, m2.MusteriID, m2.Ulke
FROM dbo.Musteriler m1
INNER JOIN dbo.Musteriler m2
ON m1.Ulke = m2.Ulke AND (m1.MusteriID <> m2.MusteriID);

```

![](sql/musteriler-self-join.png)

* FROM ve INNER JOIN ifadelerinde tabloyu ve kopyasını **m1** ve **m2** olarak belirttik.
* **Aynı ülkedeki şirketleri** listelemek istediğimiz için tabloları **“Ülke”** kolonu üzerinden birleştirdik.
* **Her bir şirketin kendiyle eşleşmemesi** için bir **tekillik koşuluna** ihtiyacımız var. Bunun için de birleşecek kolonları belirttiğimiz **ON** ifadesinden sonra **AND** ifadesi ile her iki tablodaki eşleşen kayıtların MusteriID değerlerinin eşit olmamasını **(<> – eşit değildir)** istediğimizi yazdık.
