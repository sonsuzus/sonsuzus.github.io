---
title: Python Programlama Ders 1. Programlama Yolu
author: sonsuz
date: 2023-06-23 00:21:17 +0300
categories: [Program,Python]
tags: [python,programlama,bilgisayar,bilim,problem,ders]
---



Bu derslerin amacı size bir bilgisayar bilimcisi gibi düşünmeyi öğretmektir. Bu düşünme şekli matematiğin, mühendisliğin ve doğal bilimlerin bazı en iyi özelliklerini birleştirir. Matematikçiler gibi, bilgisayar bilimcileri fikirleri (özellikle hesaplamalar) göstermek için biçimsel dilleri kullanırlar. Mühendisler gibi şeyleri tasarlar, bileşenleri (parçaları) sistemler şeklinde birleştirir ve farklı alternatiflerin avantaj ve dezavantajlarını değerlendirirler. Bilim insanları gibi, karmaşık sistemlerin davranışlarını gözlemler, hipotezler oluşturur ve varsayımları (tahminleri) sınarlar.

Bir bilgisayar bilimcisi için tek ve en önemli yetenek **problem çözme**dir. Problem çözme problemleri formüle edebilme, çözümler hakkında yaratıcı düşünme ve bir çözümü açık ve kesin olarak ifade edebilme yeteneğidir. Görüleceği gibi, programlama öğrenme süreci problem çözme yeteneklerinin uygulamasını yapmak için mükemmel bir fırsattır. Bu bölüme bu yüzden, "Programlama yolu" adı verilmiştir.

Bir yönden programlamayı öğrenirken - ki kendisi yararlı bir yetenektir - bir başka yönden programlamayı sonuç için bir yol olarak kullanmayı öğreneceksiniz. İlerledikçe bu daha açık bir hale gelecektir.

## 1.1 Python programlama dili

Öğreneceğiniz programlama dili Python olacaktır. Python bir **yüksek seviyeli dil** örneğidir; yüksek seviyeli dillere örnek olarak daha önce duymuş olabileceğiniz C++, PHP ve Java verilebilir. 

"Yüksek seviyeli dil" ifadesinden çıkarabileceğiniz gibi, ayrıca **düşük seviyeli dil**ler de vardır, bunlar bazı durumlarda "makine dili" veya "birleştirici dili" şeklinde isimlendirilir. Basitçe söylersek, bilgisayarlar sadece düşük seviyeli dillerde yazılmış programları çalıştırabilirler. Bu yüzden, yüksek seviyeli dillerde yazılmış programlar çalıştırılmadan önce bir işlemden geçmelidir. Bu ek işlem biraz zaman alır, bu da yüksek seviyeli dillerin dezavantajıdır.

Ancak avantajları oldukça fazladır. İlk olarak, yüksek seviyeli dillerde programlamak oldukça kolaydır. Yüksek seviyeli dilde yazılmış programlar daha az sürede yazılır, daha kısadır, okuması daha kolay ve doğru olma ihtimalleri daha yüksektir. İkinci olarak, **yüksek seviyeli diller**dir, bunun anlamı farklı bilgisayarlarda az değişiklik veya değişiklik yapmadan çalıştırılabilirler. Düşük seviyeli programlar sadece tek bir bilgisayar çeşidinde çalışabilirler ve başka bir bilgisayarda çalışabilmesi için tekrar yazılmalıdır.

Yüksek seviyeli dilleri, düşük seviyeli dillere çevirmek için iki çeşit program kullanılmaktadır: **yorumlayıcılar** ve **derleyiciler**.Yorumlayıcılar yüksek seviyeli programı okur ve işletir, bunun anlamı program ne diyorsa onu yapar. Programı biraz biraz işler, satırları okur ve ilgili hesaplamaları gerekleştirir.

![](illustrations/interpret.png)

Derleyici programı okur ve programı çalıştırmadan önce tamamen başka bir şeye dönüştürür. Bu durumda yüksek seviyeli programa **kaynak kod**, çevrildiği programa ise **hedef kod** veya **çalıştırılabilir** denir. Program derlendikten sonra, daha fazla çevirme yapmadan tekrar tekrar çalıştırılabilir.

![](illustrations/compile.png)

Çoğu modern dil her iki işlemi de kullanır. Programlar ilk önce daha düşük seviyeli bir dile derlenir, **byte kod**, ve daha sonra **sanal makine** adı verilen bir program tarafından yorumlanırlar. Python her iki işlemi de kullanır, ancak programcıların kendisiyle etkileşim yöntemi nedeniyle, daha çok **yorumlamalı dil** olarak kabul edilir.

Python yorumlayıcısının kullandığı iki yöntem vardır: *kabuk modu* ve *betik modu*. Kabuk modunda **Python kabuğu**na Python cümlelerini yazıp, yorumlayıcının hemen sonuçları üretmesi sağlanıyor:

```py
>>> print(1 + 1)
2
```

Bu örnekteki  >>> ile başlayan satır, **Python bilgi istemi**(prompt)dir. Yorumlayıcı bilgi istemini komutlar için hazır olduğunu belirtmek için kullanmaktadır. print(1+1) yazdık ve yorumlayıcı yanıt olarak 2 döndürdü.

Alternatif olarak, programı bir dosya içine yazıp yorumlayıcının dosya içeriğini çalıştırmasını sağlayabiliriz. Bu tip dosyaya **betik** adı verilmektedir. Örneğin, bir metin dzenleyicisi yardımıyla firstprogram.py adlı dosyayı aşağıdaki içerikle yarattığımızı varsayalım:

```py
print(1 + 1)
```

Bir kural (gelenek) olarak, Python programlarını içeren dosyalar .py uzantısıyla biter.

Programı çalıştırmak için, yorumlayıcıya dosyanın ismini vermemiz gerekir:

```py
$ python firstprogram.py
2
```

Bu örnekler Python'un komut satırından çalıştırılmasını göstermektedir. Diğer geliştirme ortamlarında, programları çalıştırma ayrıntıları farklılıklar gösterebilir. Ayrıca çoğu program bu verilen örnekten çok daha ilginçtir.

Bu derslerdeki örnekler Python yorumlayıcısı ve betikleri kullanır. Kabuk modu örnekleri hep bilgi istemiyle başlayacağı için örneklerin alıştırılmasında hangi yöntemin kullanılacağını rahatlıkla ayırdedebileceksiniz. Kabuk modunda çalışmak küçük kod parçalarını sınamak için geleneksel yöntemdir, çünkü anında geri beslemeyi almış olursunuz. Kabuk modunu (idle shell) karalama için kullanılan bir kağıt parçası gibi düşünebilirsiniz. Bir kaç satırdan uzun herşey betik içerisine koyulmalıdır.

## 1.2 Program nedir?

Program, hesaplamayı gerekleştirmek için gereken birbirini izleyen yönergelerden (komutlardan) oluşan yapıdır. Hesaplama matematiksel olabilir, örneğin bir eşitlikler sisteminin çözülmesi veya bir polinomun kökünü bulmak gibi, ama ayrıca sembolik bir hesaplama, bir belge içinde metin arama ve değiştirme veya program derleme (yeterince ilginç) gibi, olabilir.

Ayrıntılar farklı programlama dillerinde farklı gözükebilir, ancak bazı basit temel yönergeler her dilde gözükür:

girdi:
: Klavyeden, dosyadan veya başka bir aygıttan veriyi alma.

çıktı:
: Ekranda veriyi görüntüleme veya veriyi bir dosya ya da başka bir aygıta gönderme.

matematik:
: Toplama, çarpma gibi bazı temel matematiksel işlemleri gerçekleştirme.

koşullu yürütme: (karşılaştırma)
: Belirli durumlar için sınama yapma ve uygun cümle sırasını çalıştırma. 

tekrarlama: (döngü)
: Bazı eylemleri genellikle ufak tefek bazı değişikliklerle tekrar tekrar yürütme.

İnanın veya inanmayın, var olanların hepsi bu kadardır. Şu ana kadar kullandığınız her program, ne kadar karmaşık olursa olsun, yukarıdakilere benzeyen komutlarla yapılmıştır. Bu yüzden, programlamayı büyük ve karmaşık bir görevi, yukarıdaki temel komutlarla gerçekleştirilebilecek kadar basit olan daha küçük alt görevler şeklinde parçalama süreci olarak tanımlayabiliriz.

Bu biraz belirsiz gelebilir, ancak bu konuya **algoritmalar** hakkında konuşurken tekrar geleceğiz.

## 1.3 Hata ayıklama (Debugging) nedir?

Programlama karmaşık bir süreçtir, ve insanlar tarafından yapıldığı için hatalara yol açabilir. Garip nedenlerden dolayı, programlama hatalarına bug adı verilmektedir, ve bu hataları belirleme ve düzeltme işlemine **debugging** adı verilmektedir ( Bug böcek anlamına gelir. Eski dönemlerde odayı kaplayan bilgisayarlarda böcek görülmesi üzerine kullanıldığına dair iddialar var. Türkçe'de hata ayıklama ifadesini kullanacağımız için aslında bu açıklamanın sadece ingilizce için geçerli olduğunu belirtmek gerekiyor).

Bir programda üç tür hata oluşabilir : sözdizimsel hatalar, çalışma zamanı hataları ve anlambilimsel hatalar. Bu hataları daha hızlı belirleyebilmek için ayırt edici özelliklerinin anlatılması önemlidir.

## 1.4 Sözdizimsel hatalar

Python bir programı eğer sözdizimsel olarak doğruysa çalıştırabilir; aksi halde, işlem başarısız olur ve bir hata mesajı döndürür. Sözdizimi programın yapısını kasteder ve bu yapı hakkındaki kuralları tanımlar. Örneğin, Türkçe'de bir cümle büyük harfle başlamalı ve nokta işaretiyle tamamlanmalıdır. bu cümle bir **sözdizimi hatası** içermektedir. Ayrıca bu cümle de

Çoğu okuyucu için, bazı sözdizimi hataları çok önemli değildir, bu yüzden bazı şiir örneklerini hata mesajları vermeden okuyabiliriz. Python bu kadar affedici değildir. Programın herhangi bir yerinde tek bir sözdizimi hatası olduğunda bile, bir hata mesajı verip çıkacaktır ve programı çalıştırmanız mümkün olmayacaktır. Programlama kariyerinizin ilk bir kaç haftasında, bu sözdizimi hatalarını belirlemek ve düzeltmek için oldukça fazla zaman harcayacaksınız. Deneyim kazandıkça, daha az hata yapmaya ve hataları daha hızlı belirleyip düzeltmeye başlayacaksınız.

## 1.5 Çalışma zamanı hataları

İkinci tür hatalar, **çalışma zamanı hataları**dır, bu ismin verilmesinin nedeni program çalıştırılana kadar bu hataların ortaya çıkmamasıdır. Bu hatalara ayrıca **istisna** adı da verilmektedir, çünkü istisnai (ve kötü) bir durumun ortaya çıktığını belirtirler. ilk bölümlerdeki basit programlarda çalışma zamanı hatalarıyla karşılaşmanız oldukça düşük ihtimallidir, bu hatalarla karşılaşana kadar biraz zaman geçebilir.

## 1.6 Anlambilimsel hatalar

Üçüncü hata tipi **anlambilimsel hata**lardır. Programda bir anlambilimsel hata varsa, başarılı bir şekilde çalışmayacaktır, bundan kastedilen bilgisayarın herhangi bir hata mesajı üretmeyeceği, ancak doğru şeyi yapmayacağıdır. Beklenilenden farklı bir şey yapacaktır. Bilgisayarlar siz ona ne derseniz, onu yapan aygıtlardır.

Sorun, yazdığınız program yazmak istediğiniz program değildir. Programın anlamı (anlambilimi) hatalıdır. Anlambilimsel hataları tanımlamak ustalık (beceri) ister, çünkü programın çıktısını inceleyerek geriye yönelik olarak takip etmenizi ve ne yaptığını anlamaya çalışmanızı gerektirir.

## 1.7 Deneysel hata ayıklama

Kazanabileceğiniz en önemli yeteneklerden biri hata ayıklamadır. Sinir bozucu olmasına rağmen, hata ayıklama programlamanın zihinsel zenginlik gerektiren, zorlayıcı ve ilginç bir parçasıdır.

Bazı durumlarda, hata ayıklama dedektif çalışması gibidir. İpuçlarıyla karşı karşıya kalmışsınızdır ve gördüğünüz sonuçlara yol açan süreçlerle eylemlerden sonuçlar ve anlamlar çıkarmanız gerekir.

Hata ayıklama deneysel bilim gibidir. Neyin hatalı gittiğine dair fikriniz oluştuğunda, programı değiştirerek tekrar tekrar denersiniz. Hipoteziniz doğru ise, değişikliğin sonucunu tahminleyebilir ve çalışan bir programa bir adım daha yaklaşmış olursunuz. Hipoteziniz yanlış ise, yeni bir hipotez üretmeniz gerekir. Sherlock Holmes'un söylediği gibi "imkansızı elediğinizde, elinizde kalan şey, her ne kadar görünmese de gerçek olmak zorundadır" (A. Conan Doyle, The Sign of Four)

Bazı kişiler için, programlama ve hata ayıklama aynı şeydir, programlama istediğiniz işi yapana kadar bir programda hata ayıklama sürecidir. Bu fikir programı yazmaya basit bir şekilde, temel bir şeyler yapan bir örnekle başlamanız gerektiğini söyler, ilerledikçe programda küçük değişiklikler yaparak, hataları ayıklayarak ilerlemenizi tavsiye eder. Bu yöntemle her zaman bir çalışan sürüme sahip olabilirsiniz.

Örneğin, Linux bir işletim sistemi çekirdeğidir ve binlerce satır kaynak kod içerir, ama Linus Torvalds tarafından Intel 80386 yongasını keşfetmek için basit bir program olarak başlatılmıştır. Larry Greenfield'a göre, "Linus'un erken projelerinden biri, AAAA ve BBBB arasında seçim yaparak ekrana yazdıran bir programdır, bu program daha sonra Linux'a evrilmiştir" ("The Linux Users' Guide version 1")

Kitabın sonraki bölümleri hata ayıklama ve diğer programlama pratikleri hakkında daha fazla önerilerde bulunacaktır.

## 1.8 Biçimsel (Formal) ve doğal diller

**Doğal diller** konuştuğumuz dillerdir, Türkçe, İngilizce, İspanyolca ve Fransızca gibi. İnsanlar tarafından tasarlanmamıştır (her ne kadar insanlar bunlar için kurallar koymaya çalışsa da), doğal olarak evrilmişlerdir.

**Biçimsel diller** insanlar tarafından bazı özel uygulamalar için geliştirilmiş dillerdir. Örneğin, matematikçilerin kullandığı gösterim sayılar ve semboller arasındaki ilişkiyi göstermek için iyi bir biçimsel dildir. Kimyacılar moleküllerin kimyasal yapısını göstermek için biçimsel bir dil kullanırlar. Ve en önemlisi:

> *Programlama dilleri hesaplamaları ifade etmek için tasarlanmış biçimsel dillerdir.*

Biçimsel diller sözdizimi açısından katı kurallara sahip olma eğilimindedir. Örneğin, `3+3=6` ifadesi matematiksel olarak sözdizimsel olarak doğru bir ifadedir, ancak `3=+6$` değildir. `H2O` sözdizimsel olarak doğru bir kimyasal isimdir, `2Zz` ifadesi değildir.

Sözdizimsel kurallar **token**lere ve yapıya ait olmak üzere iki şekildedir. Tokenler dilin temel öğeleridir, kelimeler, sayılar ve kimyasal elementler gibi. 3=+6$ ifadesiyle ilgili bir sorun $ işaretinin matematikte (bildiğimiz kadarıyla) geçerli bir token olmamasıdır. Benzer olarak 2Zz ifadesi de geçerli değildir çünkü Zz kısaltmasına sahip bir element yoktur.

İkinci tür sözdizim kuralı cümlelerin yapısıyla - tokenlerin nasıl dizildiği - ilgili kurallardır. 3=+6$ yapısal olarak geçersizdir çünkü eşittir işaretinden hemen sonra artı işareti gelemez. Benzer olarak, molekül formüllerinde de alt işaretler element isminden sonra gelmelidir, önce gelemezler.

Biçimsel bir dildeki veya Türkçe'deki bir cümleyi okuduğunuzda, cümlenin yapısını çözmek gerekir (doğal dillerde bunu bilinçsiz bir şekilde yaparız). Bu sürece **ayrıştırma** (parsing) adı verilmektedir.

Örneğin, "Ayaklarıma kara sular indi" cümlesini duyduğunuzda, "ayaklarıma"nın özne, "indi"'nin de yüklem olduğunu algılarsınız. Cümleyi ayrıştırdığınızda, ne anlama geldiğini (cümlenin anlambilimini) çözersiniz. "Ayak"ın ne olduğunu ve "indi" eylemini bildiğinizi varsayarsak, bu cümleyle kastedilen anlamı ortaya çıkarabilirsiniz.

Her ne kadar biçimsel ve doğal diller bir çok ortak özelliğe - tokenler, yapı, sözdizimi, anlambilim - sahip olsa da, bir çok farklılıkları da vardır:

belirsizlik:
: Doğal diller belirsizlikle doludur, kişiler bağlamsal ipuçları ve diğer bilgilerden yararlanarak bu belirsizliği aşarlar. Biçimsel diller neredeyse veya tamamen belirli olmak üzere tasarlanmıştır. Bunun anlamı cümlenin sadece bir anlamı vardır, bağlam ne olursa olsun.

fazlalık (redundancy):
: Belirsizliği önlemek ve yanlış anlamaları azaltmak için, doğal diller bir çok gereksiz içeriğe sahiptir. Bu yüzden bir çok fazlalık barındırır. Biçimsel diller fazlalık içermez, az ve öz olmalıdır.

gerçekçilik:
: Doğal diller deyim ve mecazlarla doludur. Eğer biri "Ayaklarıma kara sular indi" diyorsa, bu ayaklarına kara sular indi anlamına gelmez, gizli bir anlamı vardır ve yorgun olduğunu belirtir. Biçimsel dillerde cümlelerin gerçeği aynen yansıtması gerekir, anlamı yazılanla aynı olmalıdır.

Doğal bir dili konuşarak büyüyen kişiler - herkes - biçimsel dillere alışmakta zorlanabilirler. Bazı durumlarda, biçimsel dillerle doğal diller arasındaki farklar düzyazı ile şiir arasındaki farklar gibidir, ancak;

Şiir:
: Kelimeler anlamları olduğu kadar sesleri için de kullanılır, ve tüm şiir bir etki veya duygusal bir tepki yaratır. Belirsizlik yaygın olmasının yanında sıklıkla bir gerekliliktir.

Düzyazı:
: Kelimelerin gerçek anlamı daha önemlidir, ve yapı anlama daha fazla katkı sağlar. Düzyazının şiire göre çözümlemesi daha kolaydır ancak yine de belirsizlikler içerebilir.

Programlar:
: Bilgisayar programının anlamı belirli (tek anlamlı) ve gerçek olmalıdır, ve token ile yapının çözümlenmesiyle tamamen anlaşılmalıdır.

Programları (ve diğer biçimsel dilleri) okumak için bazı öneriler şu şekildir. İlk olarak, biçimsel dillerin doğal dillerden daha yoğun olduğunu hatırlamak gerekir, böylece onları okumak daha fazla zaman alacaktır. Ayrıca, yapı oldukça önemlidir, bu yüzden yukarıdan aşağıya soldan sağa okumak iyi bir fikir değildir, programı kafanızda ayrıştırmayı, tokenleri ve yapıyı belirleme ve tanımlamayı öğrenmeniz gerekir. Son olarak, ayrıntılar önemlidir. yazım yanlışları ve noktalama hataları gibi küçük şeyler, doğal dillerde bunları yok sayabilirsiniz, biçimsel dillerde büyük farklar ve sorunlar yaratabilir.

## 1.9 İlk program

Geleneksel olarak, yeni bir dilde yazılan ilk program "Merhaba, Dünya!" adı verilen programdır, çünkü ekranda "Merhaba, Dünya!" kelimelerini gösterir. Python'da aşağıdaki şekilde yazılmaktadır:

```py
print("Merhaba, Dünya!")
```

Bu **print cümlesinin** bir örneğidir. Bu cümle kağıt üstüne bir şey yazmaz, ekranda bir değer gösterir. Yukarıdaki örnekte, sonuç aşağıdaki kelimelerin ekranda gözükmesidir:

```py
Merhaba, Dünya!
```

Tırnak işaretleri programda bir değerin baş ve sonunu gösterir, ekrandaki sonuçta bu karakterler gözükmez. Bazı kişiler programlama dilinin kalitesini "Merhaba, Dünya!" programının basitliğiyle değerlendirirler. Bu standarta göre, Python oldukça iyi sonuç üretir.

## 1.10 Sözlük

algoritma:
: Bir problem kategorisini çözmek için bir genel süreç

bug:
: Programdaki bir hata

byte kod:
: Kaynak kod ve hedef kod arasındaki ara dildir. Çoğu modern programlama dili ilk olarak kaynak kodu, byte koda derler ve daha sonra bu byte kodu *sanal makine* adı verilen bir program ile yorumlarlar.

derleme:
: Yüksek seviyeli bir dilde yazılmış programı, daha sonra çalıştırmak üzere daha düşük seviyeli bir dile çevirme işlemidir.

hata ayıklama:
: Herhangi bir programlama hatasını bulma ve ortadan kaldırma sürecidir.

istisna:
: Çalışma zamanı hatasının bir diğer adı

çalıştırılabilir:
: Çalıştırılmaya hazır hedef kodun bir diğer adı

biçimsel dil:
: Bazı özel amaçlar için , matematiksel fikirlerin temsili veya bilgisayar programları gibi, insanlar tarafından tasarlanmış herhangi bir dildir. Tüm programlama dilleri biçimsel dillerdir.

yüksek seviyeli dil:
: İnsanlar tarafından rahatlıkla okunabilmesi, yazılması ve anlaşılması için geliştirilmiş Python benzeri programlama dili

yorumlama:
: Yüksek seviyeli dilde yazılmış bir programı satır satır çevirerek yürütme

düşük seviyeli dil:
: Bilgisayarın kolay bir şekilde yürütmesi için tasarlanmış programlama dili, "makine dili" veya "birleştirici dil" adı da verilmektedir.

doğal dil:
: Doğal olarak evrimleşmiş ve insanların konuşurken kullandığı herhangi bir dil

hedef kod:
: Derleyicinin programı (kaynak kodu) çevirmesiyle ortaya çıkan çıktı

ayrıştırma:
: Bir programı inceleme ve sözdizimsel yapısını çözümleme işlemi

taşınabilirlik:
: Bir programın birden fazla bilgisayar türünde yürütülebilmesi özelliği

print() cümlesi:
: Python yorumlayıcısının bir değeri ekranda göstermesini sağlayan yönerge (komut) cümlesi

problem çözme:
: Problemi formüle etme, çözüm bulma ve çözümü ifade etme süreci

program:
: Bilgisayar tarafından gerçekleştirilecek eylemleri ve hesaplamaları belirten art arda gelen komutlar

Python kabuğu:
: Python yorumlayıcısının etkileşimli kullanıcı arayüzü. Python kabuğu kullanıcısı bilgi isteminde (>>>) komutları yazar ve Giriş (Enter) tuşuna basarak komutları anında yorumlayıcıya işlenmeleri için gönderir.

çalışma zamanı hatası:
: Program çalıştırılana kadar ortaya çıkmayan, çalıştırıldıktan sonra oluşan ve programın çalışmasına devam etmesini engelleyen hata

betik:
: Bir dosyada saklanmış program (genellikle yorumlayıcıya verilecek olan)

anlambilimsel hata:
: Programın, programcının istediğinden farklı bir şey yapmasına neden olan hata

anlambilim:
: Programın anlamı

kaynak kod:
: Yüksek seviyeli bir dildeki programın derlemeden önceki hali

sözdizimi:
: Programın yapısı

sözdizimi hatası:
: Programın ayrıştırılmasını imkansız hale getiren hata (dolayısıyla yorumlanmasını da imkansız hale getirir)

token:
: Programın sözdizimsel yapısının temel öğelerinden biri, doğal dillerdeki kelimeye benzetilebilir.

## 1.11 Alıştırmalar

- Anlaşılabilir anlama sahip ama sözdizimsel olarak yanlış olan Türkçe bir cümle yazınız. Sözdizimsel olarak doğru ancak anlambilimsel hatalara sahip bir başka cümle yazınız.

- Python kabuğunu başlatın. `1 + 2` yazıp Giriş tuşuna basın. Python bu *ifadeyi değerlendirir*, sonucu ekranda gösterir ve başka bir bilgi istemi yazar. *\* çarpma işleci*dir, ve *\*\* üs alma işleci*dir. Farklı ifadeler girerek deneyin, Python yorumlayıcısının sonuçlarını kaydedin. */ işleci*ni kullandığınızda ne oluyor? Sonuçlar beklediğiniz gibi mi? Açıklayınız.

- `1 2` yazıp Giriş tuşuna basın. Python bu ifadeyi değerlendirmeye çalışır, ancak yapamaz çünkü bu ifade sözdizimsel olarak geçerli değildir. Yerine aşağıdaki hata mesajını gösterir: 
 
```py
  File "<stdin>", line 1
    1 2
      ^
SyntaxError: invalid syntax
```

Çoğu durumda, Python sözdizimi hatasının nerede olduğunu belirtir, ancak bu her zaman için doğru değildir, ve neyin yanlış olduğuna dair yeterince bilgi vermeyebilir. Bu yüzden, genellikle, sözdizimi kurallarını öğrenmek üzerinizdeki yüktür.

Bu örnekte, Python numaralar arasında işleç olmadığı için şikayet etmektedir. 

Python bilgi isteminde yazdığınızda hata mesajına neden olacak üç ifade örneği daha üretiniz. Her ürettiğiniz ifadenin Python sözdizimi açısından neden geçerli olmadığını açıklayınız.
 
- `print('merhaba')` yazınız. Python bu cümleyi yürütecektir, m-e-r-h-a-b-a harflerini ekranda göstermek gibi bir etkisi olacaktır. Ekranda gösterilen ifadede, cümlede kullandığınız tırnak işaretlerinin olmadığına dikkat edin.

 Şimdi `print('"merhaba"')` yazıp, sonucu tanımlayıp, açıklayınız.

- `print(peynir)` ifadesini tırnak işaretleri olmadan yazın. Çıktı aşağıdaki gibi bir şey olacaktır: 
 
```py
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
NameError: name 'peynir' is not defined
```

Bu bir çalışma zamanı hatasıdır, *NameError* hatasıdır, isimsel bir hatadır çünkü peynir ismi tanımlanmamıştır. Bu ne anlama geliyor bilmiyorsanız, yakında öğreneceksiniz.

- Python bilgi isteminde `'Bu bir testtir...'` yazıp Giriş tuşuna basın. Ne olduğunu kaydedin. Şimdi test1.py isminde bir betik oluşturun ve aşağıdaki içeriği betiğin içine yazın (çalıştırmadan önce kaydetmeyi unutmayın): 

```py
'Bu bir testtir...'
```

 Bu betiği çalıştırdığınızda ne oluyor? Şimdi içeriği aşağıdaki şekilde değiştirin: 
 
```py
print('Bu bir testtir...')
```

ve tekrar çalıştırın. Bu sefer ne oldu?
 
Ne zaman bir deyim Python bilgi istemine yazılırsa, değerlendirilir ve sonuç ekranda bir satır aşağıya yazılır. 'Bu bir testtir...' bir deyimdir, 'Bu bir testtir...' şeklinde değerlendirilir (42 deyiminin 42 şeklinde değerlendirilmesi gibi). Bir betikte ise, deyimlerin değerlendirilmesi program çıktısına gönderilmez, bu yüzden açıkça ekranda gösterilmesinin gerektiği belirtilmelidir.
