---
title:  SQL’de Alt Sorgu (Subquery) Kullanımı
author: sonsuz
date: 2023-09-18 19:36:41 +0300
categories: [Program,SQL]
tags: [sql,sorgu,query,subquery,veri,veritabanı,programlama]
image: sql/matruska-ic-ice-bebekler.png
---




İstanbul’dan Arjantin’in başkenti Buenos Aires’e nasıl gidersiniz?

Cevabınız ne olur bilemiyorum ama bu yazının yazıldığı Kasım 2022 itibari ile direkt bir uçağa atlayıp gidemezsiniz. Buenos Aires’e gidebilmek için önce Amsterdam, Frankfurt veya Napoli gibi şehirlerden birine gidip, oradan aktarma yapmanız gerekir.

**“Bir sorgu içerisinde yer alan sorgular”** diyerek basitçe tanımlayabileceğimiz alt sorgular, bir nevi aktarma uçuşların yaptığı görevi görür. Bir işlemi birden fazla adımda gerçekleştirmeniz gerektiğinde kullanışlıdırlar. 

Genellikle, istediğiniz bilgiyi elde etmek için seçme, filtreleme veya hesaplama yapmadan önce verileriniz üzerinde biraz çalışmanız gerekir. Alt sorgular, bu işi gerçekleştirmenin yollarından biridir.

Alt sorgular sayesinde dinamik sorgular oluşturabiliriz.

## SQL’de alt sorgu (subquery) nasıl çalışır?

Alt sorgular, **ana sorgunun (main query)** içinde yer alır. Ana sorguya **“dış sorgu”** ismi de verilir. Alt sorgular, ana sorgunun içerisinde olduğu için **“iç sorgu”** olarak isimlendirilir. Ana sorgu ve alt sorgu arasındaki ilişkiyi şu şekilde görselleştirebiliriz:

![](sql/alt-sorgu-soz-dizimi-syntax.png)

SQL kodu çalıştırılırken alt sorgu önceliğe sahiptir. Alt sorgu çalışır, işlem sonucunda bir değer üretir ve daha sonrasında bu değer ana sorgu tarafından kullanılır. 

## SQL’de alt sorgu (subquery) söz dizimi

Alt sorgular, sorgu içerisinde yer alan sorgular olduğu için, temel olarak SQL’de oluşturduğunuz herhangi bir sorgu alt sorgu olarak kullanılabilir. Bu nedenle, alt sorgu syntax’ı diye tanıtabileceğimiz özel bir syntax yoktur. Fakat, alt sorgu oluştururken dikkat edilmesi gereken **bazı kurallar** vardır:

* Alt sorgular mutlaka parantez içerisinde yer almalıdır.
* Alt sorgular başka tablolarla birleştirilebilir. Bu nedenle açıklayıcı ve dopru bir takma isim kullanılmalıdır.
* Alt sorgular iç içe (nested) kullanılabilir. Maksimum 32 seviye içeri gidebilirsiniz.
* Alt sorgular SELECT, WHERE, FROM, veya HAVING ifadeleri içerisinde kullanılabilir.

Alt sorguları yazarken öncelikle içteki sorguyu yazıp çalıştırıp, daha sonrasında ana sorguyu oluşturmak akıllı bir strateji olacaktır

## Alt sorgu (subquery) türleri nelerdir?

Alt sorgular **işlem sonucunda döndürdükleri sonuca** veya **işlem sırasındaki bağımlılıklarına** göre farklı sınıflara ayrılırlar:

### 1. **İşlem sonucunda döndürdükleri sonuca göre:**

Alt sorgular işlem sonucunda **tek bir sonuç (değer)** döndürebileceği gibi **bir veya birden çok satırlık bir** **tablo** da döndürebilir. 

#### 1.1 Tek kayıt döndüren alt sorgular (Scalar subquery)

İşlem sonucunda, dış sorgu için **sadece tek bir satır kayıt** ve **tek bir kolon** döndüren alt sorgulara tek kayıt döndüren alt sorgular adı verilir. 

Tek kayıt döndüren alt sorgular genellikle **WHERE** veya **HAVING** ifadeleri ve herhangi bir **karşılaştırma operatörü** **(=, >, >=, <, <=, and <>)** ile birlikte kullanılır.

#### 1.2 Çoklu kayıt döndüren alt sorgular (Multiple row subquery)

İşlem sonucunda, dış sorguya birden fazla satır kayıt döndüren alt sorgulara **çoklu kayıt döndüren alt sorgular** denir. Bu tip alt sorgular **IN, NOT IN, ANY, ALL, EXISTS, veya NOT EXISTS** ifadeleri ile birlikte kullanılır.

Çoklu kayıt döndüren alt sorguların sonucunda dönen yanıtlar:

1. Tek bir kolon ve birden fazla satır,
2. Birden fazla kolon ve birden fazla satır içerebilir.

### 2. **İşlem sırasındaki bağımlılıklarına göre:**

Alt sorgular işlem sırasına göre dış sorgu ile **bağıntılı (correlated)** olarak çalışabilir.

#### 2.1 Bağıntılı alt sorgular (Correlated subquery)

İç sorgunun dış sorgudan elde edilen bilgilere dayalı olarak çalıştığı alt sorgulara **bağıntılı alt sorgular** adı verilir. Öncelikle dış sorgu çalışır ve işlemin sonucunda dönen bilgiye göre ana sorgu/iç sorgu çalışır.

Ana sorgu ile iç sorgu arasındaki karşılıklı bağımlılık nedeniyle, iç sorgu bağımsız bir sorgu olarak çalıştırılamaz.

## SQL’de alt sorgular hangi durumlarda kullanılır?

Alt sorgular SELECT, WHERE, HAVING veya FROM ifadeleri ile birlikte kullanılabilir. Alt sorgular, sorgu içerisinde **kullanıldığı yere göre farklı işler yapar.** Kullanıldığı bölüme göre özetleyecek olursak:

- **SELECT**
	+ Aynı veya diğer bir tablodan hesaplanmış ortalama, toplam vs. gibi bir değer ile tabloda bulunan değerlerin karşılaştırılması.
- **WHERE**
	+ İstenilen yanıtın tek seferde elde edilemediği veya elle hesaplandığı durumların otomatize edilmesi.
	+ Başka bir tablodaki verilere bağlı olan bir koşula sahip bir tablodan satır seçmek.
- **FROM**
	+ Tablonun yeniden şekillendirilmesi.
	+ Özet bilgi kümelerinin hesaplanması (İki toplama/gruplama fonksiyonunun iç içe kullanılması).
- **HAVING**
	+ Oluşan grupların belirli bir kural yardımı ile filtrelenmesi.

Yazının geri kalanında, teorik olarak kullanım alanlarından bahsettiğimiz alt sorguları gerçek senaryolar üzerinde uygulayacağız. Uygulama için Microsoft tarafından geliştirilen ve SQL eğitimlerinde sıkça kullanılan bir veri tabanı olan Northwind veri tabanının Türkçe versiyonunu kullanacağız.

---

**Örnek veri seti:** Northwind Veri Tabanı (Türkçe)

[Örnek Veriyi İndir](https://sonsuzus.github.io/dosya/Northwind.rar)

---

### SELECT ifadesi içerisinde alt sorgu kullanımı

SELECT ifadesi içerisinde kullanılan alt sorgular özetlenmiş (aggregated) tek bir değer döndürür. Burada kullanılan alt sorgular SUM, COUNT, MIN veya MAX gibi **toplama/gruplama fonksiyonları (aggregated)** ile birlikte kullanılır.

> Bir kolon üzerinde hesaplama yaparak tek bir değer üreten fonksiyonlara **toplama/gruplama *fonksiyonları*** (aggregated) denir.

Alt sorgular, aynı veya diğer bir tablodan özet bir değere ihtiyaç duyulduğu zaman SELECT ifadesi içerisinde kullanılır.

#### Aynı veya diğer bir tablodan hesaplanmış ortalama, toplam vs. gibi bir değer ile tabloda bulunan değerlerin karşılaştırılması.

SELECT ifadesi içerisinde alt sorguları kullanarak, daha karmaşık işlemlerde kullanmak üzere **“özel kolonlar”** oluşturabiliriz. Daha sonrasında da bu oluşturduğumuz özel kolonları kullanarak farklı hesaplamalar yapabilir veya tabloda bulunan değerler ile karşılaştırabiliriz.

Şöyle bir örnek senaryo üzerinden ilerleyelim:

* Dünya üzerinde birçok ülkeye satış yapan bir firmasınız ve satış yaptığınız her bir ülke için de farklı farklı nakliye ücretleri ödüyorsunuz. **Yaptığınız her bir satış için ortalama nakliye maliyetinizden ne kadar fazla ödediğinizi nasıl bulabilirsiniz?**

Bu sorunun cevabını alt sorgu kullanmadan iki adımda bulabilirsiniz:  
1- Ortalama nakliye ücretini hesapla.  
2- Her bir satırdan ortalama nakliye ücretini çıkar.

Northwind veri tabanında bulunan “Satışlar” tablosundan ortalama nakliye ücretini hesapladık:

```sql
SELECT AVG(NakliyeUcreti) AS ort_nakliye
FROM dbo.Satislar;

```

```
78,2442
```

Daha sonrasında da bulduğumuz ortalama ücreti tüm Nakliye Ücreti kolonundan çıkardık:

```sql
SELECT NakliyeUcreti, NakliyeUcreti - 78.2442 AS Ortalama_Farki
FROM dbo.Satislar;

```

![](sql/ortalama-farki-satislar-tablosu.png)

Bu iki adımı tek bir sorguda alt sorgu yardımı ile gerçekleştirebiliriz:

```sql
SELECT 
	NakliyeUcreti, 
	(SELECT AVG(NakliyeUcreti) FROM dbo.Satislar) AS ort_nakliye,
	NakliyeUcreti - (SELECT AVG(NakliyeUcreti) FROM dbo.Satislar) AS Ortalama_Farki
FROM dbo.Satislar;

```

![](sql/alt-sorgu-ortalama-farki-satislar.png)

* SELECT ifadesi içerisinde NakliyeUcreti kolonunu çağırdık.
* Daha sonrasında ortalama nakliye ücretini hesapladığımız sorguyu yazarak “ort\_nakliye” adını verdiğimiz özel bir kolon oluşturduk. Bu alt sorgu sayesinde tüm satırlarda ortalama nakliye ücretini içeren bir kolona sahip olduk.
* Son olarak da NakliyeUcreti kolonunda bulunan değerlerden alt sorgu ile hesapladığımız ortalama nakliye ücretini çıkardık ve “Ortalama\_Farki” adını verdiğimiz yeni bir kolon oluşturduk.

Yukarıdaki örnek sorguda aslında ikinci kolona ihtiyacımız yoktu. Yazılan alt sorgunun nasıl bir değer ürettiğini göstermek için ekledim.

**Peki, ortalama nakliye ücretini hesaplamak ve “tüm kolona eklemek için” neden alt sorguya ihtiyaç duyduk?**

Çünkü, gruplama/toplama fonksiyonları, grup oluşturmayan bir sorgu üzerinde çalışmaz. GROUP BY ifadesi olmadan toplama fonksiyonlarını grup oluşturmayan bir sorguda kullandığımız zaman **hata** alırız. SELECT ifadesi içerisinde kullanılan alt sorgular bu hatadan kaçınmanın yollarından biridir.

```sql
SELECT NakliyeUcreti, AVG(NakliyeUcreti) AS ort_nakliye
FROM dbo.Satislar;

```

```
Column 'dbo.Satislar.NakliyeUcreti' is invalid in the select list because it is not contained in either an aggregate function or the GROUP BY clause.
```

**SELECT ifadesi içerisinde alt sorgu kullanırken bazı kurallara dikkat edilmelidir:**

* SELECT ifadesi içerisinde kullanılan alt sorgu sonuç olarak **mutlaka tek bir değer döndürmelidir.** Tek bir değer yerine bir tablo döndürdüğü zaman, bu sonuç her bir satıra uygulanamayacağı/atanamayacağı için hata alınır.
* Ana sorguya uygulanan filtre işlemleri alt sorguya, alt sorguya işlenen filtre işlemleri de **ana sorguya geçerli olmaz.** Bu nedenle, tüm sorgulara uygulanacak filtreler ayrı ayrı hem ana sorguya hem de alt sorguya uygulanmalıdır. Örneğin, Amerika’ya yapılan satışları ana sorgudan filtreler fakat alt sorgudan filtrelemezsek, hesapladığımız ortalama nakliye ücreti tutarında Amerika’ya yapılan satışlar da yer alacaktır.

### FROM ifadesi içinde alt sorgu kullanımı

Alt sorgular SELECT ifadesinde kullanılabildiği gibi FROM ifadesi içerisinde de kullanılabilir. 

FROM ifadesi içerisinde kullanılan alt sorgular, SELECT ifadesi ile doğrudan kullanılabilen veya diğer tablolarla birleştirilip daha sonra kullanılabilen bir **ara tablo** oluşturur. Bu ara tablo, işlevsel olarak **“geçici tablolara (temporary table)”** benzer ve ana sorgu tarafından sorgulanmak için kullanılabileceği gibi başka bir tablo ile de birleştirilebilir.

FROM ifadesi içerisinde kullanılan alt sorgular genelde eldeki tabloyu dönüştürmek yani farklı bir formata getirmek için kullanılır.

#### Tablonun yeniden şekillendirilmesi.

Alt sorgular FROM ifadesi içerisinde en yaygın olarak tabloları **yeniden düzenlemek/şekillendirmek** için kullanılır. 

Şöyle bir örnek senaryo üzerinden ilerleyelim:

* Bir önceki örnekten hatırladığımız, dünyanın her yerine satış yapan şirketimizin stoklarını inceliyoruz. **Her bir ürün kategorisinde kaç adet ürün bulunduğunu, kategori adı ile birlikte nasıl bulabiliriz?**

Herhangi bir kod yazmadan önce hangi tablolara ihtiyaç olduğunu bulmamız gerekiyor. Northwind veri tabanında ürünler ve ürün kategorileri ile ilgili bilgileri saklayan **Kategoriler** ve **Ürünler** adında, birbirine **“KategoriID”** kolonu ile bağlı iki farklı tablomuz var. Önce bu iki tabloya hızlıca göz atalım:

```sql
SELECT *
FROM dbo.Kategoriler;

SELECT *
FROM dbo.Urunler;

```

![](sql/northwind-urunler-kategoriler-tablo.png)

Ürünler tablosunda her bir ürün ile ilgili detaylı bilgi mevcut. Bu tabloyu kullanarak her bir kategoride kaç adet tekil ürün olduğunu hesaplayabiliriz:

```sql
SELECT KategoriID, COUNT(DISTINCT UrunID) as Adet 
FROM dbo.Urunler 
GROUP BY KategoriID;

```

![](sql/kategori-urun-sayisi.png)

Her bir kategoride kaç adet ürün bulunduğunu hesapladık. Rakamlar doğru olsa da bu tablo bize kategorilerin isimleri ile ilgili bilgi vermiyor. Her bir kategorinin adını ihtiyacımız var. Bu bilgiyi “Kategoriler” tablosundan elde etmek zorundayız. 

Bir önceki adımda oluşturduğumuz sonucu bir ara tablo gibi kullanarak, kategoriler tablosu ile birleştirebiliriz. Bunun için yukarıdaki sorguyu FROM ifadesinde yer alacak bir alt sorguya dönüştürmeliyiz.

```sql
SELECT k.KategoriAdi, u.Adet
FROM (
	SELECT KategoriID, COUNT(DISTINCT UrunID) as Adet 
	FROM dbo.Urunler 
	GROUP BY KategoriID) AS u
INNER JOIN dbo.Kategoriler AS k
ON u.KategoriID = k.KategoriID; 

```

![](sql/alt-sorgu-kategori-urun-adeti.png)

* Yukarıda oluşturduğumuz her bir kategorideki ürün sayısını sayan sorguyu FROM ifadesi içerisine ekledik ve “u” takma adını verdik.
* Daha sonrasında INNER JOIN kullanarak bu tabloyu “k” takma adını verdiğimiz Kategoriler tablosu ile “KategoriID” kolonunu kullanarak birleştirdik.
* Yeni oluşan tablo için “u” tablosundan ürün adet sayısını temsil eden “Adet” kolonunu, “k” tablosundan ise Kategori adını çağırdık.

**Peki, bu sonuca sadece JOIN işlemi kullanarak ulaşamaz mıydık?**

Evet, ulaşabilirdik. Aynı matematik problemlerinde olduğu gibi SQL problemlerinde de doğru sonuç tek olsa da o sonuca götürebilecek birden çok yol vardır. Önemli olan, ilgili tüm teknikleri öğrenip karşılaşacağınız duruma göre en uygun (sorgu performansı, kod okunabilirliği vs.) aracı kullanarak sonuca ulaşmaktır. 

Yukarıdaki sorunun JOIN ile nasıl yapılacağını merak edenler için: 

```sql
SELECT k.KategoriAdi, COUNT(DISTINCT u.UrunID) as Adet
FROM dbo.Kategoriler AS k
RIGHT JOIN dbo.Urunler AS u
ON k.KategoriID = u.KategoriID
GROUP BY k.KategoriAdi;

```

![](sql/alt-sorgu-kategori-urun-adeti.png)

#### Özet bilgi kümelerinin hesaplanması (İki toplama/gruplama fonksiyonunun iç içe kullanılması)

SQL’de toplama/gruplama fonksiyonlarının bir kolon değeri, ortalama, toplam gibi tek bir özet değere çevirdiğinden bahsetmiştik. SQL’de iki toplama fonksiyonu ile **iç içe kullanarak** işlem yapmak istediğinizde hata alırsınız. Bu sorunu aşmak için alt sorgulardan faydalanırız.

Her şeyin daha da netleşmesi için örnek bir senaryo üzerinden ilerleyelim:

* Şirketimizin satış verisini inceliyoruz. **Ortalama satış fiyatı en yüksek ilk üç ürün kategorisinin ortalama ürün fiyatını nasıl hesaplayabiliriz?**

Bu soruyu yanıtlamak için Ürünler tablosuna ihtiyacımız var. İlk akla gelen ve mantıklı gibi görünen çözüm şöyle olabilir:

```sql
SELECT TOP 3 KategoriID, AVG(AVG(BirimFiyati)) AS Ort
FROM dbo.Urunler
GROUP BY KategoriID
ORDER BY KategoriID DESC;

```

```
Cannot perform an aggregate function on an expression containing an aggregate or a subquery.
```

- Ürünler tablosundan:
	+ BirimFiyatı kolonunun ortalamasını hesapladık.
	+ Bu kolonu **GROUP BY** fonksiyonunu kullanarak KategoriID’ye göre gruplandırdık.
	+ **ORDER BY** fonksiyonu ve **DESC** ifadesi ile değerleri büyükten küçüğe sıraladık.
	+ **TOP 3** ifadesini kullanarak da ortalama değeri en yüksek ilk 3 kategori numarasını sınırladık.

Her iki toplama fonksiyonunu iç içe kullanmak istediğimiz için SQL Server yukarıda gördüğümüz hatayı verdi. Bu sorunu aşmak için alt sorguları kullanacağız. 

Alt sorguları oluştururken adım adım ilerlemek gerekiyor. Öncelikle, en yüksek ortalama ürün fiyatına sahip ilk 3 kategoriyi bulalım:

```sql
SELECT TOP 3 KategoriID, AVG(BirimFiyati) AS Ort
FROM dbo.Urunler
GROUP BY KategoriID
ORDER BY 2 DESC;

```

![](sql/alt-sorgu-ortalama-urun-fiyati.png)

En yüksek 3 ortalama ürün fiyatına sahip kategoriyi hesapladık. Bir sonraki adımda bu üç kategorideki değerlerin ortalamasını hesaplayacağız. Bir önceki adımda yazdığımız sorgu, bizim için geçici bir tablo görevi görecek ve bu nedenle FROM ifadesi içerisinde yer alacak.

```sql
SELECT AVG(s.Ort) AS ilk_uc_ortalama
FROM 
	(SELECT TOP 3 KategoriID, AVG(BirimFiyati) AS Ort
	FROM dbo.Urunler
	GROUP BY KategoriID
	ORDER BY 2 DESC) AS s;

```

```
41,4519
```

* Bir önceki adımda oluşturduğumuz alt sorguyu FROM ifadesi içerisine yerleştirdik ve bu geçici tablo gibi işlen gören yapıya “s” takma adını verdik.
* SELECT ifadesi içerisinde de bu “s” tablosunda bulunan ortalamaların yer aldığı “Ort” kolonunun ortalamasını aldık ve yeni oluşan kolona da “ilk\_uc\_ortalama” adını verdik.
* En yüksek ilk 3 ortalama ürün fiyatına sahip kategorinin ürün fiyatı ortalaması 41,4519’dur.

FROM ifadesindeki alt sorgular, verilerinizi yeniden yapılandırmak ve dönüştürmek için kullanışlı bir araçtır. Yaptığımız örnekte, diğer alt sorgu örneklerinde olduğu gibi birden fazla işlem yaptık. Diğer örneklerden farkı ise; istediğimiz sonuca gidebilmek için kullandığımız tablo (Ürünler tablosu) doğrudan sorgulamak için gerekli formatta değildi ve analize hazırlanmak için bazı ek işlemler gerektirdi.

**FROM ifadesi içerisinde alt sorgu kullanırken bazı kurallara dikkat edilmelidir:**

* FROM ifadesi içerisinde birden fazla alt sorgu kullanılabilir ve bu alt sorguların oluşturduğu tablolar veri tabanında bulunan başka tablolar ile birleştirilebilir. Birleştirme işlemi sırasında karmaşa olmaması için her bir alt tabloya doğru ve uygun takma isimler verilmelidir.
* Yeni oluşturulan geçici tabloların hafızada (memory) indeks kullanmamasından dolayı oluşabilecek performans sorunların nedeniyle alt sorguları FROM ifadesi içerisinde kullanmaktan olabildiğince kaçınmanızı tavsiye ederim.

### WHERE ifadesi içerisinde alt sorgu kullanımı

Alt sorgular, **en yaygın olarak** WHERE ifadesinin içerisinde kullanılır. WHERE ifadesi içerisinde kullanılan alt sorgular, sonuçları **belli bir kurala göre filtrelemek için** kullanılır.

#### İstenilen yanıtı tek seferde elde edecek kadar yeterli bilgi olmaması veya bu bilginin elle hesaplanmak zorunda olması.

WHERE içerisinde kullanılan alt sorguların genel görevi sonuçları filtrelemektir. Bazı durumlarda, sorgu ile ulaşmak istenilen veriyi elde edecek yeterli bilgi yoktur yada bu bilgiyi elle/manuel olarak hesaplamak gerekiyordur. Bu gibi durumlarda alt sorgular kullanışlıdır.

Örnek bir durum üzerinden konuyu irdeleyelim: 

* Çalıştığınız şirketin anlaşmalı tedarikçilerinden birinde bir gümrük sorunu yaşandı ve mallarınıza gümrükte el kondu.
* Bu tedarikçi ile aynı ülkede bulunan tedarikçilerle de aynı sorunu yaşamaktan endişeleniyorsunuz.
* Sorun yaşadığınız tedarikçi ile aynı ülkede hizmet veren diğer tedarikçilerinizin listesine ihtiyacınız var.
* Fakat sorun şu ki, sorun yaşadığınız tedarikçinin hangi ülkede faaliyet gösterdiğini bilmiyorsunuz.
* Sorun yaşama potansiyeliniz olan diğer tedarikçileri bulabilmek için öncelikle sorun yaşadığınız tedarikçinin ülkesine ihtiyacınız var.

Bu bilgiyi **alt sorgu yardımı** ile elde edebilirsiniz. Ayrıca, yarın şirketinizde başka bir gümrük problemi yaşadığınız zaman, oluşturduğunuz sorguda tedarikçi ismini değiştirerek hızlıca ilerleyebilirsiniz.

İlk önce Tedarikçiler tablosundan, sorun yaşanılan tedarikçinin (Bu örnek için adı Exotic Liquids olsun.) ülkesini bulalım:

```sql
SELECT Ulke
FROM dbo.Tedarikciler
WHERE SirketAdi = 'Exotic Liquids';

```

```
UK
```

Exotic Liquids şirketinin bulunduğu ülkenin İngiltere (UK) olduğunu öğrendik. Şimdi de İngiltere’de bulunan diğer anlaşmalı tedarikçileri bulalım:

```sql
SELECT *
FROM dbo.Tedarikciler
WHERE Ulke = (SELECT Ulke
FROM dbo.Tedarikciler
WHERE SirketAdi = 'Exotic Liquids');

```

![](sql/alt-sorgu-tedarikci-sorgulama.png)

Sorguya göre İngiltere’de bulunan 2 adet tedarikçimiz var. Birisi Exotic Liquids şirketi diğeri de Specialty Biscuits şirketi.

**NOT:** Ana sorguda bulunan WHERE ifadesinde ülke kolonu ile Exotic Liquids şirketinin bulunduğu ülkeyi eşleştirirken **“= (eşittir)”** ifadesini kullandık. Bu örnek için çok uygun olmasa da, bazen birden fazla değer ile eşleştirme yapmak isteyebiliriz. Öteki tablodan elde edilen bilgiler, ana sorguda filtreleme işlemi için kullanılacak bir liste görevi görür. Bu durumda eşittir yerine **“IN”** ifadesi kullanılmalıdır.

#### Başka bir tablodaki verilere bağlı olan bir koşula sahip bir tablodan satır seçmek.

Bazı durumlarda sorgulama için başka tabloda yer alan verilere ihtiyaç duyulur. Ana sorgu, çalışabilmek için alt sorgunun diğer bir tablodan elde ettiği bilgiye ihtiyaç duyar. 

Örnek bir vaka üzerinden ilerleyelim:

* **Hangi satışlardaki ödediğimiz nakliye ücreti, şirketin ortalama satış gelirinden daha fazla olmuştur?**

Satışlar ve Satışlara ait detaylar iki farklı tabloda bulunuyor. Satışlar tablosunda her bir satıştaki nakliye ücreti bilgisi mevcutken, Satış Detayları tablosunda ise her bir satış kaydı için kaç adet ürün sipariş edildiği ve ürün fiyatı bilgisi bulunuyor.

Yine adım adım ilerleyeceğiz. Öncelikle şirketin her bir satıştan ortalama kazancını hesaplayalım:

```sql
SELECT AVG(Miktar * BirimFiyati) AS ort_gelir
FROM dbo.SatisDetaylari;

```

Satış Detayları tablosunda bulunan miktar ve Birim Fiyatı kolonlarını çarptığımız zaman her bir satış için geliri hesaplayabiliriz. Bu yeni kolonun ortalamasını aldığımız zaman ise şirketin ortalama satış değerini buluruz. Bu bilgiyi alt sorgu olarak kullanarak NakliyeUcreti ile karşılaştıracağız:

```sql
SELECT *
FROM dbo.Satislar
WHERE NakliyeUcreti > (SELECT AVG(Miktar * BirimFiyati) AS ort_gelir
FROM dbo.SatisDetaylari); 

```

![](sql/alt-sorgu-ortalama-gelir-nakliye-ucreti.png)

9 farklı satış işleminde ödenilen nakliye ücretinin ortalama satış gelirinden yüksek olduğunu bulduk.

WHERE içerisinde kullanılan alt sorgular aynı veya başka bir tablodaki verilere bağlı bir koşula sahip bir tablodan satır seçmek için yararlıdır. 

### HAVING ifadesi içinde alt sorgu kullanımı

Alt sorguların kullanılabildiği diğer bir alan ise HAVING ifadesi içerisindedir. HAVING ifadesi, GROUP BY fonksiyonu ile oluşturulan grupların filtrelenmesi için kullanılır. 

#### Oluşan grupların belirli bir kural yardımı ile filtrelenmesi.

HAVING ifadesi içerisinde kullanılan alt sorgular, belirli bir kural yardımı ile oluşan grup sayısını azaltmak için kullanılır. Bu sayede, gruplama fonksiyonları (AVG, SUM, COUNT vs.) ile birlikte grupları veri setinden elde edilen özet değerlere göre filtreleyebilirsiniz. Örneğin, bir grubun ortalamasını genel ortalamayla karşılaştırmak artık mümkün. Aynı WHERE ifadesinde olduğu gibi karşılaştırmak için kullanılacak değeri alt sorgu yardımı ile hesaplayabilirsiniz.

Diğer önceki tüm başlıklarda olduğu gibi bu bölümde de gerçek bir senaryo üzerinden ilerleyelim.

* **Hangi ülkeler için ödenilen ortalama nakliye ücreti şirket nakliye ücreti ortalamasından en az %50 daha fazladır?**

Öncelikle, şirketin ödediği ortalama nakliye ücretini hesaplayacağız:

```sql
SELECT AVG(NakliyeUcreti) 
FROM dbo.Satislar;

```

```
78,2442
```

Şirket ortalama olarak 78.24 TRY yada dolar ortalama nakliye ücreti ödüyor. Hangi ülkelerde bu rakamdan en az %50 fazla nakliye ücreti ödeniyor?

```sql
SELECT SevkUlkesi, AVG(NakliyeUcreti) AS ort_nakliye
FROM dbo.Satislar
GROUP BY SevkUlkesi
HAVING AVG(NakliyeUcreti) * 0.5 > (SELECT AVG(NakliyeUcreti) FROM dbo.Satislar);

```

![](sql/alt-sorgu-ortalama-nakliye-ucreti-ulke.png)

* Satışlar tablosundan SevkUlkesi, Nakliye Ücreti kolonlarını çağırdık.
* Nakliye Ücretini AVG fonksiyonu ile ortalamasını aldık ve “ort\_nakliye” ismini verdik.
* Daha sonrasında ortalama nakliye ücretini GROUP BY fonksiyonu ile her bir ülke için grupladık.
* Ortalama nakliye ücretinden %50 daha fazla ücret ödenen ülkeleri bulabilmek/filtrelemek için HAVING fonksiyonunu kullanarak, ortalama nakliye ücretinin %50 fazlası ile her bir ülkenin ortalama nakliye ücretini kıyasladık.
* Yukarıdaki kıyasa uyan tek ülke eldeki verilere göre Avusturya oldu.

## Alt sorgu kullanmanın avantajları nelerdir?

SQL ile sorgulama yaparken alt sorguların sunduğu bazı faydalar vardır. Alt sorgular, sorguyu ifadenin her bir parçasını izole edecek şekilde mantıksal bir işlem sırası ile yapılandırırlar. Bu sayede:

* JOIN işlemlerine kıyasla, sorguların okunabilirliğini arttırır.
* Alt sorguları okumak ve anlamak görece daha kolaydır.
* Karmaşık JOIN ve UNION işlemleri yerine kullanılabilir.

## Alt sorgu kullanmanın dezavantajları nelerdir?

Her bir konunun olduğu gibi alt sorguların da bazı dezavantajları vardır:

* Alt sorgular, aynı sorgu içerisinde bir tabloyu hem değiştirip hem de aynı tablodan bir seçim yapamaz.
* Alt sorguların veri tabanında işlenmesi, JOIN işlemine kıyasla daha uzun sürer. Bu nedenle, eğer bir alt sorgu yerine JOIN ifadesi ile yeniden yazılabiliyorsa daha hızlı çalışacaktır.

## Alt sorgular ve JOIN işlemleri arasındaki farklar nelerdir? (Subquery vs. JOIN)

Birçok alt sorgu JOIN işlemleri, birçok JOIN işlemi de alt sorgular kullanarak yeniden yazılabilir. Alt sorgular ve JOIN işlemlerinin birbirine kıyasla bazı avantaj ve dezavantajları vardır. Alt sorgular ve JOIN işlemlerini **okunabilirlik**, **hız** ve **anlaşılabilirlik** açısından birbiriyle kıyaslayabiliriz.

| Özellik | Alt Sorgu | JOIN |
| --- | --- | --- |
| **Okunabilirlik** | Sorgularının okunabilirliğini arttırır. | Sorgularının okunabilirliğini azaltır. |
| **Hız** | JOIN işlemlerine kıyasla yavaştır. | Alt sorgulara kıyasla hızlıdır. |
| **Anlaşılabilirlik** | Kolay okunur ve anlaşılabilir. | Anlaşılması daha zordur. |

Birçok alt sorgunun JOIN işlemleri kullanılarak yeniden yazılabildiğinden bahsetmiştik. Alt sorgu kullanmaya ihtiyacınız olup olmadığına karar verirken, kullandıınız her bir alt sorgunun ek bilgi işlem gücü gerektirdiğini bilmek önemlidir. 

Alt sorgu kullanımına karar verirken çalıştığınız veri tabanının büyüklüğünü ve sorgu sonucunda döndürdüğünüz kayıt sayısını göz önünde bulundurmanızı tavsiye ederim.
