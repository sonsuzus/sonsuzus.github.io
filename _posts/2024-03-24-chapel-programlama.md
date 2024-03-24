---
title:  Chapel Programlama
author: sonsuz
date: 2024-03-24 10:00:15 +0300
categories: [Program]
tags: [chapel,programlama,ilginç,yazılım,dil]
---


Chapel, yüksek performanslı ve paralel hesaplama problemlerini çözmek için tasarlanmıştır. Cray Inc. (şimdi HPE) tarafından 2004 yılında başlatılan bir araştırma projesi olarak ortaya çıktı. Bu proje, Cascade adı verilen bir programlama dili üzerinde çalıştı. Cascade'in temelleri atıldıktan sonra, Chapel'in tasarımı ve geliştirilmesi odak noktası haline geldi.

2010 yılında Chapel'in ilk sürümü, Cray Inc. tarafından yayımlandı ve araştırmacılar tarafından kullanılmak üzere sunuldu. Chapel, 2015 yılında açık kaynaklı hale getirildi ve GitHub üzerinde bir halka açık depoya taşındı. Bu adım, topluluk katılımını teşvik etti ve dilin daha geniş bir kullanıcı tabanına ulaşmasını sağladı.

Chapel, sürekli olarak geliştirilmekte ve iyileştirilmektedir. Kullanıcı geri bildirimleri ve topluluk katkıları, dilin gelişimine önemli katkılarda bulunmaktadır. Bugün, Chapel, bilimsel hesaplamalar, simülasyonlar, büyük veri analizi ve paralel hesaplama gibi alanlarda geniş bir kullanıcı kitlesi tarafından tercih edilmektedir.

(Cray Inc., bilgisayar mimarisi ve yüksek performanslı bilgi işlem sistemleri alanında uzmanlaşmış bir Amerikan şirketidir. 1972 yılında Seymour Cray tarafından kurulmuştur. Şirket, süper bilgisayarların geliştirilmesinde öncü bir rol oynamıştır ve birçok önemli bilimsel ve mühendislik uygulaması için yüksek performanslı hesaplama sistemleri sağlamıştır.

Cray, tarih boyunca süper bilgisayarlar ve paralel hesaplama alanında birçok yeniliğe imza atmıştır. Özellikle, vektörel işleme ve paralel hesaplama teknolojilerinin geliştirilmesinde öncü bir rol oynamıştır. Cray'in süper bilgisayarları, genellikle büyük bilimsel kurumlar, araştırma laboratuvarları ve askeri kurumlar gibi kuruluşlar tarafından, karmaşık simülasyonlar, hava ve iklim modelleri, nükleer silah simülasyonları gibi büyük ölçekli hesaplama gerektiren uygulamalarda kullanılmıştır.

2019 yılında, Cray Inc. HPE (Hewlett Packard Enterprise) tarafından satın alındı. Bu birleşme, yüksek performanslı hesaplama ve veri merkezi çözümlerini bir araya getirerek, geniş bir müşteri tabanına daha kapsamlı hizmetler sunmalarını sağladı.)


( Cascade, Cray Inc. tarafından geliştirilen bir programlama dili araştırma projesidir. Bu proje, yüksek performanslı ve paralel hesaplama problemlerini çözmek için tasarlanmış bir dizi dilin prototiplerini içeriyordu. Cascade'in amacı, karmaşık hesaplama problemlerini daha kolay ve etkili bir şekilde çözmek için yeni programlama dili özelliklerini araştırmak ve geliştirmekti.

Cascade projesi kapsamında, bilim insanları ve mühendisler, paralel hesaplama için tasarlanmış modern programlama dili özelliklerini test ettiler ve bu özelliklerin kullanılabilirliğini ve performansını değerlendirdiler. Cascade'in tasarımı ve özellikleri, daha sonra Chapel adı verilen yeni bir programlama dilinin geliştirilmesinde temel oluşturdu.

Cascade, yüksek performanslı bilgi işlem problemlerini ele almak için tasarlanmış olan yeni dil özelliklerinin ve paradigmalarının keşfi ve değerlendirmesi için bir platform sağladı. Chapel'in gelişiminde önemli bir rol oynayan bu araştırma projesi, daha sonraki yıllarda paralel programlama alanındaki yenilikleri desteklemeye devam etti. )
 
## INPUT

Chapel'de kullanıcıdan girdi almak biraz farklıdır ve bir standart "input" fonksiyonu yoktur. Chapel'de kullanıcı girdisini almak için genellikle komut satırı argümanları veya dosyalardan okuma gibi yöntemler kullanılır.

Örneğin, bir Chapel programı yazdığınızda, programı çalıştırırken komut satırında argümanlar verebilirsiniz. Programınız bu argümanları alabilir ve işleyebilir. Ancak, çalışma zamanında programın durmasını ve kullanıcıdan girdi almasını istiyorsanız, bu Chapel'de doğrudan yapılamaz.

Bununla birlikte, bazı durumlarda kullanıcı girdisine benzer bir işlevsellik sağlayabilirsiniz. Örneğin, kullanıcıdan belirli bir dosyanın adını alabilir ve sonra bu dosyayı okuyabilirsiniz. Ancak, bu girdinin dinamik bir şekilde çalışma zamanında alınması anlamına gelmez. Chapel daha çok paralel hesaplama, yüksek performanslı hesaplama gibi alanlarda kullanılan bir dil olduğu için, interaktif kullanıcı girdisi alma işlevselliği genellikle dikkate alınmaz.

Ancak, Chapel'in gücü genellikle paralel hesaplamalar ve yüksek performanslı işlemler üzerine yoğunlaştığı için, kullanıcı girdisi alma işlevselliği genellikle bu tür programlarda kullanılmaz. Bunun yerine, genellikle dosyalardan veya başka kaynaklardan veri okuma ve işleme üzerine yoğunlaşılır.

## OUTPUT

Chapel'de çıktı almak için writeln() fonksiyonu kullanılır. Bu fonksiyon, ekrana bir metin veya değer yazdırmak için kullanılır. 
Örneğin, 

```
writeln("Merhaba, dünya!");
```

Yukarıdaki kod, "Merhaba, dünya!" metnini ekrana yazdırır.

Değişkenlerin değerlerini veya ifadelerin sonuçlarını da ekrana yazdırmak için de writeln() fonksiyonunu kullanabilirsiniz. Örneğin:

```
var x = 10;
var y = 20;
writeln("x değeri: ", x, ", y değeri: ", y);
```

Bu kod, "x değeri: 10, y değeri: 20" gibi bir çıktı üretir. writeln() fonksiyonu, birden fazla argüman alabilir ve bunları aralarına virgül koyarak ekrana yazdırır.

Chapel'de ayrıca write() fonksiyonu da bulunur. Bu fonksiyon, writeln() fonksiyonu gibi çalışır ancak bir satır sonu karakteri eklemek yerine sadece yazılan metni ekrana yazar.

## DEĞİŞKENLER (VARIABLES)

Chapel'de değişkenlere atama yapmak oldukça basittir. Değişkenler, var anahtar kelimesi ile tanımlanır ve isteğe bağlı olarak bir değer ile başlatılabilir. Değişken ataması yapıldığında, atanan değer değişkenin bellek konumuna kopyalanır.

Chapel'de operasyonlar, genellikle matematiksel işlemleri ifade etmek için kullanılır. Temel operasyonlar aritmetik, mantıksal ve karşılaştırma operasyonlarını içerir. İşte Chapel'de kullanılan temel operasyonlar:

### Aritmetik Operasyonlar:

Toplama (+): İki sayının toplamını verir.

Çıkarma (-): Bir sayıyı diğerinden çıkarır.

Çarpma (*): İki sayının çarpımını verir.

Bölme (/): Bir sayıyı diğerine böler.

Mod (%) : Bir sayının diğer sayıya bölümünden kalanı verir.

```
var x = 5;
var y = 3;
var toplam = x + y;   // 5 + 3 = 8
var fark = x - y;     // 5 - 3 = 2
var carpim = x * y;   // 5 * 3 = 15
var bolum = x / y;    // 5 / 3 = 1.66666666667
var kalan = x % y;    // 5 % 3 = 2
```


### Mantıksal Operasyonlar:

Ve (and): İki koşul da doğruysa sonuç doğrudur.

Veya (or): İki koşuldan en az biri doğruysa sonuç doğrudur.

Değil (not): Koşulun tersini alır.

```
var x = true;
var y = false;
var veSonuc = x and y;   // true and false = false
var veyaSonuc = x or y;  // true or false = true
var degilSonuc = not x;  // not true = false
```

### Karşılaştırma Operasyonları:

Eşit (==): İki değerin birbirine eşit olup olmadığını kontrol eder.

Eşit Değil (!=): İki değerin birbirine eşit olmadığını kontrol eder.

Büyük (>), Küçük (<), Büyük Eşit (>=), Küçük Eşit (<=): İki değerin ilişkisini kontrol eder.


```
var x = 5;
var y = 3;
var esit = x == y;         // 5 == 3 = false
var esitDegil = x != y;    // 5 != 3 = true
var buyuk = x > y;         // 5 > 3 = true
var kucuk = x < y;         // 5 < 3 = false
var buyukEsit = x >= y;    // 5 >= 3 = true
var kucukEsit = x <= y;    // 5 <= 3 = false
```

## DÖNGÜLER 

Chapel programlama dilinde döngüler,
  _  for
  _  while ve 
  _  repeat anahtar kelimeleriyle kullanılır.


### 1. for Döngüsü:

for döngüsü belirli bir aralıkta (genellikle bir sayı dizisi veya bir koleksiyon) dolaşmak için kullanılır.

```
for i in 1..5 do 
   writeln(i);
```

### 2. while Döngüsü:

while döngüsü belirli bir koşul sağlandığı sürece tekrarlanır

```
var i = 1; 
while i <= 5 do { 
   writeln(i);
   i += 1; 
}
```

### 3.repeat Döngüsü:

repeat döngüsü belirli bir koşul sağlanana kadar bir bloğu tekrar tekrar çalıştırır.	

```
var i = 1; 
repeat { 
  writeln(i); 
  i += 1; 
} until i > 5;
```

### 4. foreach Döngüsü:

foreach döngüsü bir koleksiyonun her elemanı üzerinde dolaşmak için kullanılır.

```
var dizi = [1, 2, 3, 4, 5];
foreach eleman in dizi do 
    writeln(eleman);  
```

### 5. forall Döngüsü:

forall döngüsü paralel iterasyonu kolaylaştırmak için kullanılır.

```
var dizi = [1, 2, 3, 4, 5]; 
forall i in dizi do 
   writeln(i);
```

## Chapel ile Python benzerlikleri

Kullanım Kolaylığı:
: Hem Chapel hem de Python, okunması ve kullanılması kolay bir sözdizimine sahiptir.

Koleksiyon Tipleri:
: Her iki dil de listeler, diziler, demetler ve sözlükler gibi çeşitli koleksiyon tiplerini destekler.

Modüler Yapı:
: Hem Chapel hem de Python, modüler programlama yapısını destekler, bu da kodu daha organize ve yeniden kullanılabilir hale getirir.

Kullanıcı Tanımlı Fonksiyonlar:
: Her iki dil de kullanıcı tanımlı fonksiyonları destekler, bu da kodun parçalara ayrılmasını ve yeniden kullanılabilirliğini artırır.

Dokümantasyon ve Topluluk Desteği:
: Hem Chapel hem de Python, zengin bir dokümantasyon ve büyük bir kullanıcı topluluğuna sahiptir, bu da sorunları çözmeyi kolaylaştırır.

Bu basit benzerlikler, Chapel ve Python'un bazı ortak noktalarını gösterir. Her iki dil de kullanıcı dostu bir yapıya sahiptir ve çeşitli programlama görevlerini yerine getirmek için kullanılabilirler.


## Chapel ile Python arasındaki  farklar:

Tür Sistemi:
: Chapel'de değişkenlerin türleri önceden belirlenir ve değişmez. Python'da ise değişkenlerin türleri çalışma zamanında belirlenir ve değişebilir.

Paralel Programlama:
: Chapel, birden fazla işi aynı anda yapmak için tasarlanmıştır. Python ise bu konuda Chapel kadar güçlü değildir ve paralel programlama yapmak için ek kütüphanelere ihtiyaç duyar.

Performans:
: Chapel, hızlı bilimsel hesaplamalar ve büyük veri işleme için optimize edilmiştir. Python ise daha genel amaçlıdır ve performansı Chapel kadar yüksek değildir.

Kullanım Alanları:
: Chapel, genellikle bilimsel hesaplamalar ve paralel programlama gibi spesifik alanlarda kullanılırken, Python daha geniş bir kullanım alanına sahiptir ve web geliştirme, veri analizi gibi birçok alanda kullanılabilir.

Sözdizimi:
: Chapel ve Python'un yazım şekilleri birbirinden farklıdır. Chapel, daha geleneksel bir yapıya sahipken, Python daha basit ve okunabilir bir sözdizimine sahiptir.

Bu şekilde Chapel ile Python arasındaki farkları daha basit bir şekilde anlayabilirsiniz. Chapel, belirli bir amaca hizmet ederken, Python daha genel ve esnek bir dildir.
