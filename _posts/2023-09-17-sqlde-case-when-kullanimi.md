---
title:  SQL’de CASE WHEN Kullanımı
author: sonsuz
date: 2023-09-17 00:36:56 +0300
categories: [Program,SQL]
tags: [sql,veri,veri tabanı,sorgu,case,when,karşılaştırma,süzme]
---




Gündelik hayatta elde ettiğimiz sonuçlar veya verdiğimiz kararlar sıklıkla **“koşullardan”** etkilenir. Örnek olarak hava yağmurluysa dışarı çıkarken şemsiyenizi alırsınız veya güneşliyse tişört giyerek dışarı çıkarsınız. Elinizdeki veriyi koşullara göre yeniden düzenleyebilmek ve sorgulayabilmek için SQL’de **CASE WHEN** ifadesi kullanılır.

## SQL’de CASE WHEN ifadesi ne iş yapar?

Veri tabanı ile konuşurken CASE WHEN ifadesi, birebir çeviri yapacak olursak **“durum bu olursa, o zaman** **şunu yap”** anlamına gelir. Bu ifade, sorgulayıcı tarafından verilmiş belirli koşullara göre her bir satırı değerlendirerek belli bir sonuç üretir.

Ehliyet almak için bir sürücü kursuna başvuran adayların kayıt edildiği bir veri tabanını düşünelim. Ehliyet almak için 18 yaşından büyük olmak gerekmektedir. Bu nedenle 18 yaşından küçükler ehliyet sınavına kayıt olmak için uygun değildir. Başvurular “uygunluğa” göre kategorize edilmelidir. Buradaki ifadeyi şu şekilde görselleştirebiliriz:

![](sql/kosullu-ifade-ornegi.png)

Yukarıdaki koşulu SQL’de CASE WHEN ifadesi ile yerine getirebiliriz. 

![](sql/basit-case-when-ornek.png)

CASE WHEN ifadesi ile oluşan değerler her zaman tablo içerisinde **yeni bir sütunda** tutulur.

## CASE WHEN ifadesinin söz dizimi (syntax)

SQL’de CASE WHEN ifadesinin söz dizimi aşağıdaki gibidir:

```sql
CASE kolon_adi
    WHEN kosul_1 THEN sonuc_1
    WHEN kosul_2 THEN sonuc_2
    .......
    .......
    WHEN kosul_n THEN sonuc_n
    ELSE diger_sonuc
END;

```

Yukarıdaki söz dizimini ve çalışma mantığını biraz daha yakından inceleyelim:

* CASE’den sonra gelen **ilk WHEN** **ifadesi** birinci durumu, **ikinci WHEN ifadesi** ise ikinci durumu ve sonraki gelen WHEN’ler sırasıyla **diğer durumları** temsil eder.
* THEN ifadesi ise aynı sırada bulunan koşulun gerçekleşmesi durumunda gerçekleşecek sonucu ifade eder. **İlk THEN ifadesi birinci** WHEN koşulunun gerçekleştiğinde alınacak sonucu, ikinci **THEN** **ifadesi** ikinci WHEN koşulunun gerçekleştiğinde alınacak sonucu temsil eder ve sırayla devam eder.
* CASE WHEN ifadesi yukarıdan aşağıya doğru, sütunda bulunan **her bir değer** için çalışır. Sütunda bulunan değer hangi koşula uyuyorsa, koşulun gerçekleştiğinde alınacak sonuç ifade edilir ve tabloda bulunan bir sonraki değer için aynı işlem tekrarlanır.
* Tabloda bulunan değer WHEN ile belirtilen koşullardan hiç birine uymadığı durumda **ELSE** ile ifade edilen sonuç gerçekleşir.
* CASE WHEN kalıbı **ELSE ifadesi olmadığında da herhangi bir hata vermeden çalışır.** Fakat, bu durumda WHEN ifadelerinde belirtilen durumlar gerçekleşmediğinde hücre değeri **“NULL”** yani boş değer olur.
* CASE WHEN kalıbında **en az** bir WHEN ifadesi kullanılabilir. WHEN ifadesi istenildiği kadar eklenebilir.
* CASE WHEN ifadeleri **END** ile bitirilir. İstenildiği zaman END’den sonra **AS** ifadesi (takma isim anlamına gelen “Alias” ifadesinin kısaltması) ile oluşan yeni sütuna bir isim verilebilir.

Yukarıda açıkladığımız çalışma mantığını şu şekilde de görselleştirebiliriz: 

![](sql/case-when-sql-nasil-calisir.png)

## SQL’de CASE WHEN kullanımı

SQL’de CASE WHEN ifadesi iki farklı şekilde kullanılmaktadır. Bunlar, **Basit CASE (Simple CASE)** ve **Aramalı CASE WHEN (Searched CASE)** olarak isimlendirilir.

### 1 – SELECT ifadesi ile basit CASE WHEN (Simple CASE) kullanımı

**Basit CASE** örneğinde hücre değeri ile koşul listesinden eşleşen değer yanıt olarak döner. CASE WHEN ifadesi günlük hayatta veri temizliği sırasında faydalıdır. Örnek olarak “Kadın”, “Bayan”, “K.” gibi metin değerlerinin hepsinin aslında “Kadın” olarak düzeltilmesi gerekmektedir.

Bahsettiğimiz örneği gerçekleştirelim.

Öncelikle ‘musteri’ adında hayali bir tablo oluşturalım ve bu tabloya hayali veriler girelim.

```sql
CREATE TABLE musteri (
 musteri_id int,
 cinsiyet varchar(255),
 toplam_harcama int
);

```

* CREATE TABLE fonksiyonunu kullanarak musteri adında bir tablo oluşturduk.
* Bu tabloya üç adet değişken/kolon tanımladık.
 + **musteri\_id:** Müşteri numarası
 + **cinsiyet:** Müşterinin cinsiyeti
 + **toplam\_harcama:** Müşterinin harcama tutarı
* musteri\_id ve toplam harcam\_harcama degiskenleri tam sayı (integer) veri tipine sahipken, cinsiyet karakter olarak tanımlandı.

Tablo hazır. Şimdi sırada bu tabloya yapay veriler gireceğiz.

```sql
INSERT INTO musteri(musteri_id, cinsiyet, toplam_harcama)
VALUES 
(1, 'Kadın', 10000),
(2, 'Erkek', 25000),
(3, 'Bayan', 30000),
(4, 'kadın', 45000),
(5, 'Ms.', 32500),
(6, 'Erkek', 16400);

```

* INSERT INTO fonksiyonunu kullanarak musteri tablosuna 6 yeni gözlem ekledik.
* INSERT INTO’dan sonra satır eklenecek tablo adını ve veri girilecek değişkenlerin isimlerini girdik.
* VALUES ile beraber ise yukarıda bahsettiğimiz değişkenler için tek tek değer girdik. İlk satırda müşteri numarası 1, cinsiyeti kadın ve toplam harcaması 10,000 TL olan bir kayıt yarattık. Bu işlemi farklı satırlar için tekrarladık.

![](sql/musteri-sql-tablo.png)

Artık basit CASE ifadesini kullanmak için hazırız. ‘cinsiyet’ değişkeninde yer alan değerleri standardize edeceğiz.

```sql
SELECT *,
 CASE cinsiyet 
  WHEN 'kadın' THEN 'KADIN'
  WHEN 'Ms.' THEN 'KADIN'
  WHEN 'Bayan' THEN 'KADIN'
  WHEN 'Kadın' THEN 'KADIN'
  ELSE 'ERKEK'
 END AS 'cinsiyet_yeni'
FROM musteri;

```

![](sql/musteri-sql-basit-case-when-ornek.png)

* **SELECT** ifadesi ile beraber **asteriks (\*)** kullanarak tabloda bulunan tüm sütunları çağırdık.
* **Basit CASE WHEN** kullanımında CASE’den sonra değerlerin aranacağı kolonun/değişkenin adını girdik. Örnekte cinsiyet değişkenini manipüle ettik.
* Daha sonra **WHEN – THEN** kalıbını kullanarak her eşleşme koşullarını yazdık.
* Hiç bir eşleşme olmaması durumunda, hücrenin alacağı değeri temsil eden **ELSE** koşulunda ise farklı yazıma sahip “kadın” değerleriyle eşleşmeyen kayıtlar için “ERKEK” değerini verdik.
* CASE WHEN kalıbını **END** ile bitirirken işlem sonucu oluşan yeni kolona, AS ifadesini kullanarak “cinsiyet\_yeni” adını verdik.
* Son olarak tüm bu işlemlerin gerçekleşeceği tablonun adını **FROM** ifadesi ile musteri olarak girdik.

### 2 – SELECT ifadesi ile Aramalı CASE WHEN (Searched CASE) kullanımı

Aramalı CASE WHEN kullanımında, basit CASE WHEN’e kıyasla eşleşmesi beklenen bir değer vermek yerine (Ör: WHEN ‘Bayan’ THEN ‘Kadın’) **gerçekleşmesi beklenilen bir koşul belirlenir.**  Aynı örnek üzerinden ilerlediğimizde cinsiyeti “Kadın” olan kayıtları WHEN cinsiyet = “Kadın” THEN “KADIN” kalıbını kullanarak düzenleyebiliriz. 

Basit ve Aramalı CASE ifadeleri arasındaki en belirgin fark, basit CASE’de üzerinde çalışmak istediğimiz kolonu CASE’den hemen sonra belirtmemiz gerekirken, Aramalı CASE de ise her bir ifade için değişken kolon adını belirtmeliyiz.

Yukarıda yaptığımız örneği Aramalı CASE ifadesine göre yeniden düzenleyelim:

```sql
SELECT *,
 CASE  
  WHEN cinsiyet = 'kadın' THEN 'KADIN'
  WHEN cinsiyet = 'Ms.' THEN 'KADIN'
  WHEN cinsiyet = 'Bayan' THEN 'KADIN'
  WHEN cinsiyet = 'Kadın' THEN 'KADIN'
  ELSE 'ERKEK'
 END AS 'cinsiyet_yeni'
FROM musteri;

```

Yaptığımız örnek metin veri tipine sahip bir değişken üzerinden ilerlediği için her defasında değişken adını tanımlamak yerine basit CASE kalıbını kullanmak daha mantıklı görünüyor. Fakat, özellikle sayısal değerler üzerinde çalışırken searched CASE kalıbı kullanışlıdır.

Biraz önceki örnek tablo üzerinden, toplam harcama tutarı 30 bin liradan fazla olan müşterileri “Özel Müşteri”, geri kalanları ise “Standart Müşteri” olarak kategorize edelim:

```sql
SELECT *,
 CASE  
  WHEN toplam_harcama >30000 THEN 'Özel Müşteri'
  ELSE 'Standart Müşteri'
 END AS 'musteri_tipi'
FROM musteri;

```

![](sql/ozel-musteri-searched-case-ornek.png)

* Bir önceki örnekteki gibi SELECT \* ile tüm satır ve sütunları çağırdık.
* CASE’den sonra basit CASE’deki gibi kolon adı belirtmedik.
* WHEN ifadesine koşul olarak toplam harcamanın 30,000 liradan fazla olması gerektiğini belirttik. Bu koşulun doğru olduğu durumda, müşterinin “Özel Müşteri”, olmadığı durumda ise “Standart Müşteri” değerini alması gerektiğini yazdık.
* CASE WHEN ifadesini kapatırken END AS ile yeni oluşturduğumuz sütuna “musteri\_tipi” adını verdik.

Değişkende bulunan tüm sayısal değerleri tek tek manuel olarak eşleştirmek hem mümkün hem de mantıklı olmayacaktır. Bu nedenle, searched CASE kalıbı bu senaryoda gayet kullanışlıdır.

### SQL’de iç içe CASE WHEN kullanımı (Nested CASE WHEN)

SQL’de CASE WHEN ifadeleri iç içe geçerek de kullanılabilir. İç içe kullanan ifadelerden dışta kalan ilk koşul **‘dış ifade’**, içeride yer alan koşul ise **‘iç ifade’** olarak isimlendirilir.

İç içe CASE WHEN ifadelerinin çalışma mantığı ise dışarıdan içeriye olacak şekildedir. Eğer dışarıdaki ilk koşul doğru ise sıra içerideki koşula gelir. 

![](sql/ic-ice-case-when-nested.png)

[İç içe CASE WHEN ifadesi söz dizimi](https://towardsdatascience.com/optimize-sql-queries-with-case-expressions-in-unexpected-ways-52a8641814c5)

Yukarıdaki örnekte harcama tutarı 30,000 liradan fazla olan müşterileri özel, geri kalanlarını ise standart müşteri olarak kategorize etmiştik.

Standart müşterileri de kendi arasında cinsiyete göre kategorize etmek isteyebiliriz. Bu durumda iç içe CASE WHEN ifadesine ihtiyaç duyarız.

* Gerçekleşmesini istediğimiz ilk koşul harcama **tutarıdır**:
 + Eğer harcama tutarı 30,000 üzerindeyse müşteri özeldir ve burada bir değişikliğe ihtiyaç yoktur. Eğer harcama tutarı 30,000 altındaysa müşteri standarttır ve cinsiyete göre kategorize edilecektir.
* Gerçekleşmesini istediğimiz ikinci koşul ise **cinsiyettir**:
 + Harcama tutarı 30,000 altında olan ve cinsiyeti kadın olan müşteriler “Standart kadın müşteri”,
 + Harcama tutarı 30,000 altında olan ve cinsiyeti erkek olan müşteriler ise “Standart erkek müşteri” olmalıdır.

Yukarıdaki mantığı SQL koduna çevirmeden önce çalışma şeklini anlamak için şu görseli inceleyebilirsiniz:

![](sql/ic-ice-case-when-nested.png)

Şimdi de buradaki durumun SQL kodunu yazalım.

```sql
SELECT *, 
 CASE 
  WHEN toplam_harcama > 30000 THEN 'Ozel Müşteri'
 ELSE
  CASE 
   WHEN cinsiyet = 'KADIN' THEN 'Standart Kadın Müşteri'
   ELSE 'Standart Erkek Müşteri'
  END
 END AS 'musteri_tipi'
FROM musteri;

```

![](sql/ic-ice-case-when-ornek-uygulama.png)

* İlk CASE WHEN ifadesi ile harcama tutarı 30,000’den fazla olanları Özel Müşteri olarak isimlendirdik.
* ELSE ifadesinin içerisinde yeni bir CASE WHEN ifadesi kullanarak harcama tutarı 30,000’in altında kalanları, cinsiyeti KADIN ise ‘Standart Kadın Müşteri’ değilse ‘Standart Erkek Müşteri’ olarak adlandırdık ve END ifadesi ile iç koşulu kapattık.
* Bir alt satırda ise END ile dış CASE WHEN koşulunu kapattık ve AS ile yeni oluşan kolona musteri\_tipi takma adını verdik.

> İç içe CASE WHEN ifadelerini yazarken dikkat edilmesi gereken nokta END ifadeleridir. END ifadelerini doğru şekilde kullandığınızdan emin olmalısınız.
{: .prompt-tip }

**Not:** Oluşturduğumuz örnek müşteri tablosundaki cinsiyet kolonunda bulunan değerler örnek açısından farklı şekillerde yazılmış birçok değer içeriyordu. İç içe CASE WHEN ifadesi örneğinin karmaşıklaşmaması için bu tabloda bulunan değerleri KADIN ve ERKEK olarak standardize ettim.

```sql
UPDATE musteri
SET cinsiyet = (
 CASE  
  WHEN cinsiyet = 'kadın' THEN 'KADIN'
  WHEN cinsiyet = 'Ms.' THEN 'KADIN'
  WHEN cinsiyet = 'Bayan' THEN 'KADIN'
  WHEN cinsiyet = 'Kadın' THEN 'KADIN'
  ELSE 'ERKEK'
 END);

```

## CASE WHEN ifadesi hangi durumlarda kullanılır?

CASE WHEN ifadesi farklı farklı senaryolarda çözümler için kullanılır. Yazının devamında gerçek bir veri seti üzerinden uygulamalar ile ilerleyeceğiz. 

Uygulama için Amerika’daki bazı lise öğrencilerinin matematik, okuma ve yazma sınavlarından aldığı notların olduğu bir veri setini kullanacağız. 

---

**Örnek veri seti:** Amerikan Lise Öğrencilerinin Sınav Notları

[Örnek Veriyi İndir](https://www.kaggle.com/spscientist/students-performance-in-exams)

---

İlgili veri setini SQL Server’a yükledikten sonra bu dosya üzerinde çalışmaya hazırız. Öncelikle, veri setini tanımak adına bu tabloda bulunan tüm kayıtları çağıracağız.

```sql
SELECT *
FROM StudentsPerformance;
```

![](sql/ogrenci-notlari-ornek.png)

* Veri setinde 8 adet kolon yani değişken bulunuyor.
* Öğrencilere dair cinsiyet, etnik grup, ebeveynlerin eğitim durumu, notlar gibi bilgiler yer alıyor.

CASE WHEN ifadesinin hangi durumlarda kullanıldığına yakından göz atalım.

### 1 – Veri standardizasyonu ile veri temizliği

Gerçek dünyadaki veri setleri çoğunlukla düzenli ve temiz değildir. Veri setlerinin kalitesini düşüren en yaygın problemlerden bir tanesi ise veri girişi sırasında yapılan hatalardan dolayı aynı değere sahip fakat farklı farklı yazılan versiyonlara sahip gözlemlerin oluşmasıdır.

Online formlarda ve anketlerde cinsiyet, yaşanılan şehir gibi demografik sorular sıklıkla sorulur. Bu ve buna benzer, metin veri tipinde yanıt girilen alanların kontrol edilmemesi durumunda birçok farklı yazım hatası meydana gelir. “İstanbul”, “IstaNbul, “ISTANBUL”, “istanbul” ifadelerinin hepsi aslında tek bir şekilde yazılmalıdır.

Herhangi bir veri analizine başlanmadan önce bu değerler tekilleştirilmeli yani **veri standardize edilmelidir.**

Örnek veri setinde yer alan cinsiyet değişkeninin değerlerini ilk harfi büyük olacak şekilde güncelleyeceğiz.

```sql
SELECT gender,
 CASE gender
 WHEN 'female' THEN 'Female'
 ELSE 'Male'
 END AS 'gender_upd'
FROM StudentsPerformance;

```

![](sql/ogrenciler-cinsiyet-case-when.png)

* CASE WHEN ifadesi ile ‘female’ olan kayıtları ‘Female’, diğer kayıtları ise ‘Male’ olarak güncelledik.
* Bu sefer tüm tabloyu seçmek yerine, SELECT ile sadece ‘gender’ sütununu seçtik.
* CASE WHEN ifadesi sonucunda oluşan yeni sütun da ‘gender’ değişkeninin yanında otomatik olarak çağrılmış oldu.

### 2- Bölme işlemlerinde sıfır ile bölme hatasının önlenmesi.

Herhangi bir bölme işleminde payda “0 (sıfır)” olduğu zaman tüm programlama dilleri hata verir. SQL’de bu hata **“Divide by zero error”** olarak karşımıza çıkar. CASE WHEN ifadesini kullanarak, bölme işleminde paydanın sıfır olabileceği durumda SQL’in nasıl davranması gerektiğini söyleyebiliriz.

Örnek veri setinde öğrencilere dair sınav notları bulunuyor. Öğretmen olarak okuma ve yazma notlarını oranlamak istiyoruz. Diyelim ki, bir öğrenci yazma sınavına girmedi ve sınavdan sıfır puan aldı. Bu durumda okuma ve yazma skorlarını birbirine oranladığımız zaman ‘Divide by zero error’ hatası alacağız.

Bu senaryoyu gerçekleştirmek için öncelikle tablomuza duruma uygun yeni bir kayıt ekleyeceğiz.

```sql
INSERT INTO StudentsPerformance(gender, race_ethnicity, parental_level_of_education, lunch, test_preparation_course, math_score, reading_score, writing_score)
VALUES 
('male', 'group A', 'high school', 'standard', 'completed', 0, 50, 0);

```

* **INSERT INTO** fonksiyonunu kullanarak önce kayıt ekleyeceğimiz tabloyu ve sütunlarını, **VALUES** ile de bu sütunlara girilecek değerleri girdik.
* Yeni öğrencimizin okuma notu 50 iken yazma notu 0’dır.

Şimdi de okuma ve yazma skorlarını oranlayacağız.

```sql
SELECT reading_score/writing_score AS 'reading_writing'
FROM StudentsPerformance;

```

```sql
Msg 8134, Level 16, State 1, Line 16
Divide by zero error encountered.
```

SELECT ifadesini kullanarak sütunların birbiriyle veya herhangi bir rakamla matematiksel dört işlemleri uygulayabiliriz. Sorgunun sonucunda **‘Divide by zero error’** hatasını aldık. 

CASE WHEN ifadesini kullanarak bu hatanın oluşmasını engelleyeceğiz.

```sql
SELECT reading_score, writing_score, 
 CASE
  WHEN writing_score = 0 THEN NULL
  ELSE CAST(reading_score * 1.0 /writing_score AS decimal(6, 2)) 
 END AS 'reading_writing'
FROM StudentsPerformance;

```

![](sql/case-when-sql-null.png)

* Bu işlemde temel olarak yaptığımız şey, CASE WHEN kullanarak paydada yer alan değerin sıfır olduğu durumda sıfır yerine hangi değerin olması gerektiğini söylemek oldu.
* SELECT ifadesi ile reading\_score, writing\_score değişkenlerini çağırdık.
* CASE WHEN ifadesinde paydada yer alan writing\_score değişkeninin sıfır olması durumunda NULL değer olması gerektiğini ifade ettik. SQL’de herhangi bir rakamı NULL ile böldüğümüzde cevap NULL olacaktır.
* Bölme işlemi için kullandığımız değerler tam sayı (integer) formundadır. SQL, iki tam sayının bölme işleminin sonucunda da tam sayı olarak yanıt döner.
* Veri tipi dönüşümü yapmak yerine ilk değişkeni ‘1.0’ yani 1 ile çarparak ondalık (decimal) formata çevirdik.
* Daha sonrasında da **CAST** fonksiyonunu kullanarak bölme işleminin sonucunda oluşan değerin decimal veri tipinde olacağını ve toplamda 6 basamaktan oluşurken virgülden sonra ise 2 basamağın görünmesini istediğimizi belirttik.
* Ekran görüntüsündeki son iki kayıtta da görüldüğü üzere paydası sıfır olan değerlere ait bölme işlemi sonucunu NULL oldu.

### 3 – Koşul bazlı sıralama (ORDER BY ifadesi ile CASE WHEN kullanımı)

SQL’de bir sorgunun sonuçlarını **ORDER BY** fonksiyonu ile büyükten küçüğe (descending order – DESC) veya küçükten büyüğe (ascending order – ASC) sıralayabiliriz.

CASE WHEN ifadesi ORDER BY ile birlikte kullanıldığı zaman **koşul bazlı sıralama** yapma imkanı sağlar. Peki, gündelik hayatta bu imkan ne işimize yarar? Koşul bazlı sıralamayı nasıl kullanabiliriz?

Koşul bazlı sıralama yardımı ile: 

1. NULL değerleri sıralamada en sona atabiliriz.
2. Kendi içerisinde bir hiyerarşiye sahip olan fakat sıralamada kullanılamayacak (Ör: Şirket içerisindeki yönetici pozisyonları) özelliklere göre sıralama yapabiliriz.
3. Bir sütun içerisindeki değerleri belirli bir koşula göre hem büyükten küçüğe hem de küçükten büyüğe göre sıralayabiliriz.
4. Bir sütun içerisindeki değerleri, belirli bir koşul ile iki farklı sütuna göre sıralayabiliriz.

#### NULL değerleri sıralama

SQL’de ORDER BY ile herhangi bir kolondaki değerler sıralandığında, NULL değerler en tepede yer alır. Bu durumu gösterebilmek adına StudentsPerformance tablosundaki gender değişkenine NULL değeri olan yeni bir kayıt ekledik.

Şimdi de ORDER BY komutunu kullanarak gender kolonuna göre sıralama yapacağız.

```sql
SELECT *
FROM StudentsPerformance
ORDER BY gender;

```

![](sql/gender-null-degerler.png)

Görselden de anlaşılacağı üzere gender kolonunun ilk satırındaki değer NULL olarak yer alıyor.

CASE WHEN ifadesini kullanarak NULL değeri sıralamada sütunun en altında gelecek şekilde düzenleyeceğiz.

```sql
SELECT *
FROM StudentsPerformance
ORDER BY CASE WHEN gender IS NULL THEN 1 ELSE 0 END, gender;

```

![](sql/gender-case-when-null-degerler.png)

* SELECT \* kalıbı ile tüm tabloyu seçtik.
* FROM ifadesinde hangi tablo üzerinde işlem yaptığımızı belirttik.
* ORDER BY komutunda CASE WHEN ifadesini kullanarak, eğer kolondaki herhangi bir değer NULL olursa 1, değilse 0 olacak şekilde değer alması gerektiğini ifade ettik. Bu mantığı kullanarak boş değerlerin 0, diğerlerinin ise 1 olduğu yapay bir kolon elde ettik ve 0 değerine sahip hücreler önce, 1 değerine sahip hücreler ise sonra gelecek şekilde **küçükten büyüğe (ascending order)** bir sıralama yaptık.
* Tam tersi şekilde ilerleyip boş değerlere 0, diğer değerlere 1 atasaydık NULL değerler sıralamada en tepede yer alacaktı.
* Bu işlemi yapabilmek için SQL’deki fonksiyonlardan biri olan **IS NULL**‘ı kullandık. IS NULL bir hücrenin değerinin NULL olup olmadığını kontrol eder.
* CASE WHEN ifadesinden sonra ise gender değişkenine göre bir sıralama yaptık.
* Yeni tablonun ekran görüntüsünde de belli olduğu gibi gender değişkenindeki NULL değer sıralamada en sona yerleşti.

#### Hiyerarşiye sahip metin değerleri hiyerarşiye göre sıralama

Metin (text veya string) değerlere sahip bazı değişkenlerin değerleri kendi içerisinde hiyerarşiye sahiptir. Bu durumun en güzel örneği bir şirketteki pozisyonlardır. Örneğin CEO direktörden, direktör ise yöneticiden önce gelir. 

Aynı şekilde **sıralı (ordinal) veri tipine sahip** değişkenlerde de aynı durum görülebilir. Örneğin, öğrenim durumunda yüksek lisans eğitimi lisanstan, lisans eğitimi ise liseden önce gelir.

Örnek veri setimizde, öğrencilerin etnik grubuna dair bilgiler barındıran race\_ethnicity değişkeni bulunuyor. Bu değişkenin değerlerinin Grup A, B, C, D, E diyerek ilerlediğini biliyoruz. 

Tabloda bulunan değerleri etnik grubuna göre A’dan Z’ye sıralarken, eğitim durumuna göre de en yüksekten en düşüğe göre sıralamak istiyoruz. Bunu **ORDER BY** ile yapmaya çalışalım.

```sql
SELECT race_ethnicity, parental_level_of_education
FROM StudentsPerformance
ORDER BY race_ethnicity, parental_level_of_education DESC;

```

![](sql/etnik-grup-egitim-seviyesi-order-by.png)

ORDER BY ifadesi ile etnik grubu A-Z’ye gidecek şekilde, ebeveyn eğitim seviyesini ise tam tersi şekilde Z-A’ya gidecek şekilde sıraladık. Ebeveyn eğitim seviyesinde en tepede yer alan değer “lise” oldu. Bu değişkende lisans, yüksek lisans gibi daha üst eğitim seviyelerinin bulunduğunu hatırlatalım. 

ORDER BY komutu metin değerler için alfabetik sıralama yaptığı için kategoriler arasındaki ilişkiyi hesaba katamaz. Bu nedenle istediğimiz sıralamayı CASE WHEN ifadesi ile yapmak zorundayız. CASE WHEN ifadesi ile kategorilerin doğru sıralanabilmesi için yapay değerler atayacağız.

```sql
SELECT race_ethnicity, parental_level_of_education
FROM StudentsPerformance
ORDER BY CASE WHEN parental_level_of_education = 'master''s degree' THEN 0
     WHEN parental_level_of_education = 'bachelor''s degree' THEN 1
     WHEN parental_level_of_education = 'associate''s degree' THEN 2
     WHEN parental_level_of_education = 'some high school' THEN 3
     WHEN parental_level_of_education = 'high school' THEN 3
     ELSE 4
     END, race_ethnicity;

```

![](sql/case-when-order-by-kullanimi-ornek.png)

* Ebeveyn öğretim seviyesini şu şekilde kategorize ettik:
 + Yüksek lisans = 0
 + Lisans = 1
 + Ön lisans = 2
 + Lise = 3
 + Geriye kalanlar (Kolej) = 4
* Metin değerleri ifade ederken tırnak işareti kullanırız. Örnekteki değişkende bachelor’s degree gibi kendi içerisinde tırnak işareti olan değerler vardı. SQL’da hata almamak için kaçış işareti (escape character) olarak çift tırnak işareti kullandık.
* NULL değerleri sıralamada en sona atarken kullandığımız mantığı kullandığımızı fark etmişsinizdir. Kendi kategori değerlerimizi yaratarak yapay bir kolon elde ettik. Bu değerler kendi içerisinde küçükten büyüğe göre sıralandı.
* Daha sonrasında ise etnik gruba göre küçükten büyüğe yani A’dan Z’ye sıraladık.

**Koşula göre aynı sütun içerisinde iki farklı sıralama** 

Bir kolon içerisindeki değerleri belirli bir koşula göre hem büyükten küçüğe hem de küçükten büyüğe göre sıralayabiliriz. Örnek olarak, matematik notu 70’in üzerindeki öğrencileri notuna göre büyükten küçüğe sıralarken, 70’ten az alan öğrencileri ise aldıkları nota göre küçükten büyüğe doğru sıralayabiliriz.

```sql
SELECT gender, math_score
FROM StudentsPerformance
ORDER BY 
CASE WHEN math_score >= 70 THEN math_score END DESC,
CASE WHEN math_score < 70 THEN math_score END;

```

![](sql/order-by-case-when-ayni-kolon-siralama.png)

* StudentsPerformance tablosundan gender ve math\_score değişkenlerini seçtik.
* ORDER BY’dan sonra iki farklı CASE WHEN ifadesi oluşturduk.
* İlk ifadede math\_score değeri 70 ve üzeri olanları büyükten küçüğe, diğer ifadede ise 70’ten küçük olanları küçükten büyüğe göre sıraladık.
* CASE WHEN’de koşuldan sonra değeri manipüle etmek istemediğimiz için olduğu gibi bıraktık. Yani, değişkenin adını verdik.
* Büyükten küçüğe sıralama için DESC (descending order) fonksiyonunu kullandık.

**NOT:** Sıralama işleminin doğru yapılabilmesi için sıralama yapmadanönce math\_score değişkeninin veri tipini karakter veri tipi **varchar**‘dan tam sayı veri tipi olan **integer’a** değiştirdim. Bu değişikliği yapmadığınız taktirde, 70’e kadar notların düzenli şekilde azaldığını fakat daha sonra 100 notuna sahip öğrencileri göreceksiniz.

```sql
ALTER TABLE StudentsPerformance
ALTER COLUMN math_score INTEGER;

```

****Koşula göre farklı sütuna göre sıralama****

CASE WHEN ile ORDER BY komutlarını beraber kullanarak bir kolon içerisindeki değerleri, belirli bir koşul ile iki farklı sütuna göre de sıralayabiliriz. 

Yukarıdaki örnekte, değerleri matematik skoruna göre kendi içerisinde sıralamıştık. Aynı örneği bu sefer 70’ten yüksek alanları matematik puanı (math\_score), 70’ten düşük alanları ise okuma puanına (reading\_score) göre sıralayarak tekrarlayalım.

```sql
SELECT *
FROM StudentsPerformance
ORDER BY 
 CASE 
  WHEN math_score > 90 THEN math_score
  ELSE reading_score
 END;

```

![](sql/order-by-case-when-farkli-kolon-siralama.png)

* ORDER BY ifadesinde matematik skoru 90 olan öğrencileri matematik skoruna, 90’dan düşük olan öğrencileri ise okuma skoruna göre sıraladık.

ORDER BY ile CASE WHEN kullanarak farklı kolonlara sıralama yaparken dikkat edilmesi gereken nokta ise sıralamanın yapılacağı kolonların ikisinin de **aynı veri tipine sahip olması gerekmektedir.**

Yukarıdaki örneği, matematik skoru 90’dan düşük olanları cinsiyete göre sıralamayı deneyelim.

```sql
SELECT *
FROM StudentsPerformance
ORDER BY 
 CASE 
  WHEN math_score > 90 THEN math_score
  ELSE gender
 END;

```

```
Conversion failed when converting the nvarchar value 'female' to data type int.
```

Bu işlemi denediğimizde hata aldık. Aynı işlemi, metin değerlere sahip iki değişken üzerinde deneyelim.

```sql
SELECT *
FROM StudentsPerformance
ORDER BY 
 CASE 
  WHEN race_ethnicity = 'Group A' THEN race_ethnicity
  ELSE gender
 END;

```

![](sql/order-by-case-when-ayni-veri-tipi.png)

Her iki kolonun veri tipi de aynı olduğu için etnik grubu A olan öğrencileri etnik grubu, diğer etnik gruba sahip öğrencileri de cinsiyete göre sıralayabildik.

### 4 – Özel kategoriler oluşturma/Gruplama (GROUP BY ile CASE WHEN kullanımı)

**Toplama fonksiyonlar (Aggregate functions)**, kolondaki değerleri ortalama, toplam gibi tek bir değere dönüştüren fonksiyonlardır. Toplama fonksiyonları çoğunlukla GROUP BY fonksiyonu ile beraber kullanılır. GROUP BY fonksiyonu kolonda bulunan benzer değerleri kategorilere ayırır.

CASE WHEN ile Toplama fonksiyonları kullanarak **kendi özel GROUP BY ifadelerimizi** oluşturabiliriz.

Öncelikle GROUP BY ifadesinin nasıl çalıştığını anlamak için basit bir örnek yapalım. 

```sql
SELECT lunch, COUNT(*)
FROM StudentsPerformance
GROUP BY lunch;

```

![](sql/lunch-group-by.png)

GROUP BY ifadesi ile COUNT() fonksiyonunu kullanarak her bir öğlen yemeği kategorisinde ne kadar öğrenci bulunduğunu hesapladık. Tablodan da görüleceği üzere standart ve ücretsiz olarak iki farklı değer mevcut. 

Peki, yukarıda örneklerini yaptığımız gibi sayısal bir değişkeni gruplamak istersek ne yapacağız?

```sql
SELECT  
 CASE 
  WHEN math_score > 90 THEN 'A'
  WHEN (math_score > 70 AND math_score < 90) THEN 'B'
  WHEN (math_score > 50 AND math_score < 70) THEN 'C'
  ELSE 'D'
  END AS 'math_cat', COUNT(*) AS 'ogrenci_sayisi'
FROM StudentsPerformance
GROUP BY CASE 
  WHEN math_score > 90 THEN 'A'
  WHEN (math_score > 70 AND math_score < 90) THEN 'B'
  WHEN (math_score > 50 AND math_score < 70) THEN 'C'
  ELSE 'D'
  END;

```

![](sql/ozel-group-by-case-when-kullanimi.png)

* CASE WHEN ifadesini kullanarak öğrencileri matematik skoruna göre harf notları atadık.
 + 90 üzeri alan öğrenciler A,
 + 70 ile 90 arası alan öğrenciler B,
 + 50 ile 70 arası alan öğrenciler C ve
 + 50’den aşağı notu olan öğrencilere D harfini atadık.
* Daha sonrasında COUNT() fonksiyonu ile her bir kategoride bulunan öğrenci sayısını saydırarak ‘ogrenci\_sayisi’ adı verilen yeni bir sütun oluşturduk.
* Yukarıda yazdığımız CASE WHEN ifadesini aynı şekilde GROUP BY ifadesinde de kullanarak grupların nasıl olacağını belirledik.

### 5 – Pivot Tablo yapımı (Toplama fonksiyonlar – Aggregate Functions – ile CASE WHEN kullanımı)

CASE WHEN ifadesi, toplama fonksiyonlarının içerisinde ve GROUP BY ifadesi ile kullanılarak pivot tablolar oluşturulabilir. Eğer Excel kullanıcıysanız pivot tablolara aşinasınızdır. Aşina olmayanlar için ise pivot tabloyu kısaca **“elinizdeki ham veri setinden oluşturulmuş özet tablo”** olarak tanımlayabiliriz. Tanımdan da anlaşılacağı üzere pivot tablolar veri setini organize etmek, özetlemek ve düzenlemek için kullanışlıdır.

Elimizdeki örnek veri setinde öğrencilere dair etnik grup, cinsiyet gibi bilgiler yer alıyor. GROUP BY ifadesi ve toplama fonksiyonları kullanarak bir değişkeni kategorilerine ayırıp, her bir kategori için kayıt sayısı (count), toplam (sum) veya ortalama değer (average) gibi bazı istatistikleri hesaplayabiliyorduk. 

Peki GROUP BY fonksiyonu ile her bir etnik gruptaki kız ve erkek öğrencilerin sayısını nasıl hesaplayabiliriz?

```sql
SELECT race_ethnicity, gender,  COUNT(*) AS ogrenci_sayisi
FROM StudentsPerformance
GROUP BY race_ethnicity, gender
ORDER BY race_ethnicity;

```

![](sql/group-by-race-gender.png)

* StudentsPerformance tablosunda bulunan race\_ethnicity, gender kolonlarını önce race\_ethnicity sonra da gender olacak şekilde grupladık.
* SELECT ifadesi ile race\_ethnicity, gender kolonlarını seçtik ve her bir kategori için öğrenci sayısını COUNT fonksiyonu ile saydırdık ve bu kolona da ‘ogrenci\_sayisi’ adını verdik.
* ORDER BY fonksiyonu ile de race\_ethnicity kolonuna göre A-Z’ye olacak şekilde sıralama yaptık.

Yukarıda bulunan tabloda da görüleceği üzere her bir kategori için cinsiyet kırılımına göre öğrenci sayısını görebiliyoruz. Dikkatinizi çekmiş olmalıdır ki bu tablo okuma ve anlama açısından zordur. Bu noktada pivot tablo yapmaya ihtiyaç duyarız. 

Aynı tabloyu CASE WHEN ifadesi ile pivot tabloya dönüştüreceğiz.

```sql
SELECT race_ethnicity, 
 SUM(CASE WHEN gender = 'female' THEN 1 ELSE 0 END) AS female,
 SUM(CASE WHEN gender = 'male' THEN 1 ELSE 0 END) AS male
FROM StudentsPerformance
GROUP BY race_ethnicity
ORDER BY race_ethnicity; 

```

![](sql/case-when-pivot-table.png)

* CASE WHEN ifadesini kullanarak ‘female’ olan kayıtlara 1, olmayanlara 0 atadık ve SUM() fonksiyonu ile 1’leri topladık. Bu bize gender değişkenindeki kız öğrencilerin sayısını verdi ve bunu da ‘female’ adını verdiğimiz bir kolona atadık.
* Aynı işlemi erkekler için de tekrarladık.
* GROUP BY ifadesi ile de etnik gruba göre grupladık ve daha sonrasında ORDER BY ile A-Z’ye bir sıralama işlemi gerçekleştirdik.

Pivot tablo yardımı ile veriyi okumak ve anlamak daha da kolaylaştı. Bu sayede hangi etnik grupta ne kadar kız ve erkek öğrenci olduğunu kolayca inceleyebiliriz.

## SQL’de CASE WHEN kullanımının dezavantajları

### Sorgu performansı

CASE WHEN ifadesinde teorik olarak dilediğiniz kadar WHEN koşulu ekleyebilirsiniz. WHEN **koşul sayısı arttıkça**, CASE WHEN ifadesini içeren sorgular her bir satır için eşleme bulana kadar tüm WHEN ifadelerini kontrol edeceği için sorgu performansını olumsuz etkileyecektir.