---
title: Python Programlama Ders 2. Değişkenler, deyimler ve cümleler
author: sonsuz
date: 2023-06-23 00:45:31 +0300
categories: [Program,Python]
tags: [python,programlama,değişken,deyim,cümle,ders,tip,işlem,değer, veri tipleri, karakter dizisi, tamsayı, kayan nokta, sınıf, tür]
---



## 2.1 Değerler ve tipler

**Değer** programın işlediği temel şeylerden - harf veya rakam gibi - biridir. Şimdiye kadar gördüğümüz değerler `2` (`1 + 1` işleminin sonucu), ve `"Merhaba, Dünya!"`.

Bu değerler farklı **tiplere** aittir: `2` bir *tamsayı (integer)*dır, ve `"Merhaba, Dünya!"` bir *karakter dizisi (string)*dir, çünkü karakterlerden oluşan bir dizidir. Siz (ve yorumlayıcı) karakter dizilerini ayırtedebilir, çünkü tırnak işaretleri arasında yazılmıştır. Şimdilik *sınıf* (class) ve *type* (tür) kelimelerini birbirinin yerine kullanabilirsiniz. Sınıfın ne olduğunu daha iyi anlamak için ileriki bölümlerde geri döneceğiz.

print cümlesi tamsayılar için de çalışır.

```py
>>> print(4)
4 
```

Eğer bir değerin tipinden emin değilseniz, yorumlayıcı bunu size söyleyebilir.

```py
>>> type("Merhaba, Dünya!")
<type 'str'>
>>> type(17)
<type 'int'> 
```

 Sürpriz olmayacak şekilde, karakter dizisi **str** tipine ve tamsayılar da **int** tipine aittir. Ayrıca, ondalık basamağa sahip sayılar **float** adında bir tipe ait olacaktır, çünkü bu sayılar *kayan noktalı (floating point)* biçiminde temsil edilmektedir.

```py
>>> type(3.2)
<type 'float'> 
```

Peki `"17"` ve `"3.2"` şeklinde ifadelerin tipi nedir? Sayı gibi gözükmektedirler, ancak karakter dizileri gibi tırnak işaretleri arasındalar.

```py
>>> type("17")
<type 'str'>
>>> type("3.2")
<type 'str'> 
```

Onlar da karakter dizisidir.

Python'da karakter dizileri tek tırnak (') veya çift tırnak (") arasına alınabilir:

```py
>>> type('Bu bir karakter dizisidir.')
<type 'str'>
>>> type("Bu da öyle.")
<type 'str'> 
```

Çift tırnaklı karakter dizileri `"Emre'nin sakalı"` örneğinde olduğu gibi tek tırnak, ve tek tırnaklı karakter dizileri `'"Ni!" söyleyen şövalyeler'` örneğindeki gibi çift tırnak içerebilir.

 Büyük bir tamsayı yazdığınızda, üçlü rakam grupları arasında `1,000,000` örneğinde olduğu gibi virgül kullanmak isteyebilirsiniz. Bu Python için geçerli bir tamsayı gösterimi değildir, ancak geçerli bir ifadedir:

```py
>>> print(1,000,000)
1 0 0 
```

 Bu beklediğimiz bir sonuç değil! Python `1,000,000` ifadesini üç öğe içeren bir demet şeklinde yorumlar ve o şekilde ekranda görüntüler. Bu yüzden tamsayılarda rakamlar arasında virgül kullanmamayı unutmamalısınız.

## 2.2 Değişkenler

Programlama dilinin en güçlü özelliklerinden birisi **değişkenleri** değiştirebilme (adından anlaşılacağı gibi ) yeteneğidir. Bir değişken bir değeri tutan bir isimdir.

**Atama cümlesi** yeni bir değişken yaratır ve değerlerini atar:

```py
>>> mesaj = "Naber, doktor?"
>>> n = 17
>>> pi = 3.14159 
```

Bu örnek üç atama gerçekleştirmektedir. İlk atama `mesaj` isimli yeni yarattığı bir değişkene `"Naber, doktor?"` karakter dizisini atar. İkinci atama `n` değişkenine, `17` tamsayı değerini ve son atama `pi` değişkenine `3.14159` kayan noktalı sayı değerini verir.

**Atama işleci**, `=`, "eşittir" işaretiyle (aynı karakteri kullansa da) karıştırılmamalıdır. Atama işleçleri *isim* , işlecin sol tarafı, ve *değer* , işlecin sağ tarafı, ifadelerini birbirine bağlar. Bu yüzden aşağıdaki ifadeyi yazdığınızda hata mesajıyla karşılaşırsınız:

```py
 >>> 17 = n 
      
```

Değişkenleri kağıt üstünde göstermenin genel bir yolu değişken isminden bir ok çıkarıp değerini işaret etmektir. Bu çeşit gösterime **durum diyagramı** denilir, çünkü her bir değişkenin durumunu gösterir (değişkenin ruh hali olarak da düşünebilirsiniz). Bu diyagram atama cümlelerinin sonuçlarını gösterir:

![](illustrations/state2.png)

print cümlesi değişkenlerle de çalışır.

```py
>>> print(mesaj)
Naber, doktor?
>>> print(n)
17
>>> print(pi)
3.14159
      
```

Her bir durumda sonuç değişkenin o an ki değeridir. Değişkenler de tiplere sahiptir; yorumlayıcıya tiplerini sorabiliriz.

```py
>>> type(mesaj)
<type 'str'>
>>> type(n)
<type 'int'>
>>> type(pi)
<type 'float'> 
      
```

Değişkenin tipi referans ettiği değerin tipidir.

## 2.3 Değişken isimleri ve anahtar kelimeler

Programcılar değişkenleri için genellikle anlamlı isimler seçerler, böylece kullandıkları değişkenleri ne için kullanıldıklarına dair belgelendirmiş olurlar.

**Değişken isimleri** isteğe bağlı olarak uzun olabilir. Hem harf hem de rakam içerebilir, ancak mutlaka bir harfle başlamaları gerekir. Her ne kadar büyük harf kullanmak geçerli olsa da, geleneksel olarak kullanmayız. Unutulmaması gereken harfin büyük veya küçük olması farklı şeylerdir.`Emre` ve `emre` farklı değişkenlerdir.

 Altçizgi karakteri (`_`) bir isimde yeralabilir. Genellikle birden fazla harf içeren kelimelerde kullanılmaktadır, `benim_ismim` veya `cinde_cayin_fiyati` şeklinde.

 Eğer değişkene geçerli olmayan bir isim verirseninz, bir sözdizimi hatasıyla karşılaşırsınız:

```py
 >>> 76trombones = "big parade"
SyntaxError: invalid syntax
>>> more$ = 1000000
SyntaxError: invalid syntax
>>> class = "Computer Science 101"
SyntaxError: invalid syntax 
      
```

`76trombones` geçersizdir çünkü harf ile başlamamaktadır. `more$` geçersizdir çünkü geçersiz bir karakter içermektedir, dolar işareti. Peki `class` isminin sorunu nedir?

`class` isminin Python tarafından kullanılan **anahtar kelimeler**den biri olduğu ortadadır. Anahtar kelimeler genellikle dilin kural ve yapısını tanımlarlar, ve değişken isimleri olarak kullanılamazlar.

 Python otuzdan fazla anahtar kelimeye sahiptir ve güncelleme geldikçe bunlara ilave olacaktır. (bu kelimeleri değişken ismi olarak kullanamazsınız):

|  |    |    |    |    |
| --- | --- | --- | --- | --- |
| and | del | from| not | while  |
| as  | elif| global | or | with  |
| assert | else | if  | pass  | yield  |
| break  | except  | import  | print  | True |
| class  | exec  | in  | raise  | False |
| continue  | finally  | is  | return  |  |
| def  | for  | lambda  | try  |  |

Bu listeyi akılda tutmalı veya gerektiğinde erişebileceğiniz bir yerde olmalıdır. Eğer yorumlayıcı değişkenlerinizden birinin isminden şikayet eder ve siz nedenini bulamazsanız, bir de değişkenlerinizi bu listeye göre kontrol edersiniz. 

> Python’u yeni öğrenenler, “insanlara anlamlı gelen” değişkenlerin “bilgisayarlara da anlamlı” geleceğini sanabilirler. Örnek olarak bir değişkeninin ismini ortalama veya pi olarak isimlendirdiklerinde, bunların bir sihirbazlıkla ortalamayı hesaplıyacağını veya pi‘nin değerinin 3.14159 olabileceğini düşünebilirler. Bilgisayar kafanızda değişkene verdiğiniz anlamı bilmez. Bazı öğretmenlerin yeni başlayanlara Python’u öğretirken bilerek anlamlı değişken ismi seçmemelerinin nedeni iyi bir alışkanlık olmadığından değil, fakat öğrenenlerin ortalamayı hesaplaması için mutlaka bir program yazması veya pi‘ye mutlaka bir değer aktarması gerektiğini pekiştirmeye çalışmaktır.
{: .prompt-warning }

### 2.31 Anahtar kelimelerin anlamları

and
: Mantıksal işlemci

as
: Bağlantı oluşturmak iiçn kullanılır.

assert
: Hata ayıklama amacıyka kullanılır.

class
: Sınıf bildirimi yapmak için kullanılır.

continue
: Bir döngüde bir sonraki tekrara doğrudan geiş için kullanılır.

def
: Bir fonksiyon tanımlamak için kullanılır.

del
: Bir nesneyi silmek için kullanılır.

elif
: Koşula bağlı yapılarda kullanılır.

else
: Koşula bağlı yapılarda kullanılır.

except
: Bir istisna meydana geldiğinde, yapılacak işlemi tanımlamak için kullanılır.

False
: Karşılaştırma işlemlerinde yanlış değeri gösterir.

finally
: İstisnalar ile birlikte kullanılır ve bir istisna meydana gelip gelmediğine bakılmaksızın çalışan kodları gösterir

for
: Bir for döngüsü oluşturmak için kullanılır.

from
: Bir modülün belirli parçalarını almak için kullanılır.

global
: Global bir değişken tanımlamak için kullanılır.

if
: Koşula bağlı bir yapı tanımlamak için kullanılır.

import
: Bir modül almak için kullanılır.

in
: Bir değişkenin bir listede yer alıp almadığını kontrol etmek için kullanılır.

is
: İki değişkenin eşit olup omadığını belirlemek için kullanılır.

lambda
: Anonim bir fonksiyon oluşturmak için kullanılır.

None
: Null bir değeri temsil eder.

nonlocal
: Lokal olmayan bir değişken tanımlar.

not
: Mantıksal bir işlemcidir.

or
: Mantıksal bir işlemcidir.

pass
: Null bir ifadedir. Hiç bir işlem yapmaz.

raise
: Bir istisna tanımlar.

return
: Bir fonksiyondan çıkış yapar ve bir değer geri döndürür.

True
: Karşılaştırma işlemlerinde doğru değeri gösterir.

try
: Bir try...except yapısı tanımlar.

while
: Bir while döngüsü oluşturmak için kullanılır.

with
: İstisna işlemini kolaylaştırmak için kullanılır.

yield
: Bir fonksiyonu sona erdirir ve bir generator geri döndürür.

## 2.4 Cümleler

**Cümle** Python yorumlayıcısı tarafından işlenebilecek bir yönergedir (komuttur). Şimdiye kadar iki cümle gördük: print ve atama cümleleri.

 Bir cümleyi komut satırına yazdığınızda, Python cümleyi yürütür ve sonucu gösterir, eğer bir sonuç varsa. print cümlesinin sonucu bir değerdir. Atama cümleleri herhangi bir sonuç üretmez.

 Betik genellikle peşpeşe gelen cümlelerden oluşur. Eğer birden fazla cümle varsa, sonuçlar cümleler teker teker işlendiği için teker teker gözükürler (ilgili cümle yürütülünce ilgili sonuç - eğer varsa - görüntülenir)

 Örneğin, aşağıdaki betik:

```py
print(1)
x = 2
print(x)
      
```

 şu çıktıyı üretir:

```py
1
2 
      
```

 Yine tekrar etmek gerekir, atama cümlesi herhangi bir çıktı üretmez.

## 2.5 Deyimleri değerlendirme

 Bir **deyim** değerlerden, değişkenlerden ve işleçlerden oluşan bir yapıdır. Eğer bir deyimi komut satırına yazarsanız, yorumlayıcı deyimi **değerlendirir** ve sonucu gösterir:

```py
>>> 1 + 1
2 
      
```

*Deyimi değerlendirme* bir değer üretir, bu nedenle deyimler atama işlecinin sağ tarafından kullanılabilir. Değer de basit bir deyimdir, değişken de öyle.

```py
>>> 17
17
>>> x
2 
      
```

 Karıştırmamak gerekir, bir deyimi değerlendirmek, değeri ekranda göstermek ile aynı şey değildir.

```py
>>> message = "Naber, doktor?"
>>> mesaj
"Naber, doktor?"
>>> print(mesaj)
Naber, doktor? 
      
```

 Python kabuğu bir deyimin değerini ekranda gösterirken, değer girmek için kullanacağınız aynı biçimi kullanır. Karakter dizileri kullandığınızı varsayarsak, görüntülemede tırnak işaretlerini kullandığını görebiliriz. Ancak print cümlesi deyimin değerini ekranda gösterir, bu durumda karakter dizisinin içeriğini gösterecektir.

 Betik içerisinde, deyim kendi başına geçerli bir cümledir, ancak hiçbir şey yapmaz. Betik

```py
17
3.2
"Merhaba, Dünya!"
1 + 1      
```

 herhangi bir çıktı üretmez. Bu betiği nasıl değiştirmeliyiz ki, bu dört deyimin değeri ekranda gösterilsin?

## 2.6 İşleçler ve işlenenler

**İşleçler** toplama, çarpma, vb. hesaplamaları temsil eden özel sembollerdir. İşleçler tarafından kullanılan değerler **işlenen** adını almaktadır.

`+`, `-`, ve `/` sembolleri ve gruplama için parantez kullanımı Python'da da matematikteki anlamlarıyla kullanılmaktadır. Yıldız işareti (`*`) çarpmanın ve `**` işareti de üs almanın sembolleridir. Tam bölüm yapmak istediğinizde ise `//` kullanabilirsiniz.

 Bir işlenenin yerinde değişkenin ismi yer aldığında, işlem yapılmadan önce bu değişken değeriyle değiştirilir.

 Toplama, çıkarma, çarpma ve üs alma işlemleri neyi bekliyorsanız onu yapan işlemlerdir. Ancak bölme işlemine şaşırabilirsiniz. Aşağıdaki örnek beklemediğiniz bir sonuç üretecektir:

```py
>>> dakika = 59
>>> dakika//60
0 
      
```

`dakika`'nın değeri 59'dur ve 59, 60 ile bölündüğünde sonuç 0.98333 olmalıdır, 0 değil. Python'da bu farklı sonucun ortaya çıkmasının nedeni yukarıdaki örnekte **tamsayı tam bölme** işleminin uygulanmasıdır.

 Eğer her iki işlenen de tamsayı ise, sonucun tam sayı çıkması için tam bölme kullanılır, ve geleneksel olarak tam bölme işlemi her zaman *aşağı* yuvarlanır, hatta örnekte olduğu gibi tamsayıların birbirine çok yakın olduğu durumlarda dahi.

 Bu soruna olası bir çözüm tam bölme yerine normal bölme yapmtaktır:

```py
>>> dakika/60
0.98333
      
```

 Bir başka çözüm noktalı kayan (floating-point) bölme işlemini kullanmaktır. Dördüncü bölümde tamsayı değerleri ve değişkenleri kayan noktalı değerlere dönüştürmeyi göreceğiz. Ama artık yeni python sürümlerinde bölüm işlemi bu işi görüyor.

## 2.7 İşleçlerin sırası

 Eğer bir deyim içerisinde birden fazla işleç varsa, bu işleçlerin değerlendirilme sırası **öncelik kurallarına** göre belirlenir. Python matematikteki öncelik sırası kurallarının aynısını kullanır. PÜÇBTÇ (komik olduğunu biliyorum) kısaltması bu kuralları hatırlamak için kullanılabilecek bir kısaltmadır:

1. **P**arantezler en yüksek önceliğe sahiptir ve deyimlerin hangi sırada değerlendirilmesine yönelik ayarlamaları yapmanızı sağlarlar. Parantez içerisindeki deyimler daha önce değerlendirildiği için, `2 * (3-1)` 4, ve `(1+1)**(5-2)` 8'dir. Parantezleri ayrıca deyimleri daha kolay okumak için kullanabilirsiniz, `(minute * 100) / 60` örneğinde olduğu gibi, sonucu da değiştirmemiş olursunuz.

2. **Ü**s alma daha az önceliğe sahiptir, `2**1+1` ifadesi 3'tür 4 değil, ve `3*1**3` ifadesi de 3'tür 27 değil.

3. **Ç**arpma ve **B**ölme aynı önceliğe sahiptir, ve **T**oplama ve **Ç**ıkarmadan (ki bunlar da aynı önceliğe sahiptir) yüksek önceliklidir. `2*3-1` ifadesi 4 yerine 5 üretir, ve `2//3-1` ifadesi -1'dir, 1 değil.

4. Aynı önceliğe sahip işleçlerin değerlendirilmesinde soldan sağa kuralı izlenir. `dakika*100//60` ifadesinde, çarpma işlemi önceliklidir 5900//60 sonucuna yol açar, bu ifade de 98'i üretir. Eğer işleçler sağdan sola değerlendirilecek olsaydı sonuç `59*1` olacaktır, bu da 59'u, yanlış bir sonucu üretecekti.

## 2.8 Karakter dizisi üzerindeki işlemler

 Genel olarak, karakter dizileri üzerinde matematiksel işlemler uygulanamaz, her ne kadar karakter dizileri sayı gibi gözükse de. Aşağıdaki deyimler geçersiz deyimlerdir (`mesaj`'ın `karakter dizisi (string)` tipinde olduğunu varsayalım):

```py
 mesaj-1   "Merhaba"/123   mesaj*"Merhaba"   "15"+2       
```

 Ancak, `+` işleci karakter dizileriyle çalışmaktadır, ancak beklediğiniz sonucu üretmemektedir. Karakter dizileri için, `+` işleci **birleştirme (concatenation)** , bunun anlamı iki karakter dizisini uç uca bağlamaktır, işlemini yapacaktır. Örneğin:

```py
meyve = "muz"
iyi_pisirilmis = " fındık ekmeği"
print(meyve + iyi_pisirilmis)      
```

 Bu programın çıktısı `muz fındık ekmeği` olacaktır. `fındık`'tan önceki boşluk karakter dizisinin bir parçasıdır, ve birleştirme işleminde birleştirilen karakter dizileri arasında boşluk olmasını sağlıyor.

`*` işleci de karakter dizileri üzerinde çalışır. Tekrarlama işlemini gerçekleştirir. Örneğin `'Eğlence'*3` ifadesi `'EğlenceEğlenceEğlence'` sonucunu üretecektir. İşlenenlerden biri karakter dizisi, diğeri de tamsayı olmalıdır.

 Diğer taraftan, `+` ve `*` işleçleri toplama ve çarpma benzerliğiyle daha rahat anlaşılabilir. `4*3` örneğinin `4+4+4` ifadesine eşit olması gibi, karakter dizilerinde de `'Eğlence'*3` ifadesinin `'Eğlence'+'Eğlence'+'Eğlence'` ifadesine eşit olmasını bekliyoruz ve eşittir. Ancak, karakter dizisi birleştirme ve tekrarlamasının tamsayı toplama ve çarpmasına göre önemli bir farkı vardır. Toplama ve çarpma işleminin sahip olduğu ancak karakter dizisi birleştirme ve tekrarlama işleminin sahip olmadığı bir özellik düşünebiliyor musunuz?

## 2.9 Girdi

 Klavyeden girdi alabilmek için Python içerisinde tanımlı iki fonksiyon vardır:

```py
n = input("Lütfen isminizi giriniz: ")
print (n)
n = int(input("Nümerik bir ifade giriniz: "))
print (n)      
```

 Bu betiğin çalıştırılması aşağıdaki gibi bir sonuç üretecektir:

```py
$ python tryinput.py
Lütfen isminizi giriniz: Arthur, İngiltere Kralı
Arthur, İngiltere Kralı
Nümerik bir ifade giriniz: 7 * 3
21      
```

Her bir fonksiyon parantez içerisinde verilmiş ifadenin *gösterilmesini* sağlar.

## 2.10 Kompozisyon

 Şimdiye kadar programın öğelerini - değişkenler, deyimler, ve cümleler - ayrı ayrı inceledik, bunları nasıl birleştireceğimizden bahsetmedik.

 Programlama dillerinin en kullanışlı özelliklerinden biri küçük yapısal blokları üretmek ve bunları `birleştirebilme (kompozisyon)` özelliğidir. Örneğin, sayıları nasıl ekleyeceğimizi ve ekranda değeri nasıl göstereceğimizi biliyoruz; bu ikisini birleştirerek aynı anda gerçekleştirebiliriz:

```py
>>>  print (17 + 3)
20       
```

 Gerçekte, toplama işlemi görüntülemeden önce yapılmalıdır, bu yüzden eylemler aynı anda olmamaktadır. Buradaki önemli nokta; sayıları, karakter dizilerini ve değişkenleri içeren herhangi bir deyim print cümlesi içinde kullanılabilir. Bunun örneklerini daha önce görmüştünüz:

```py
print("Geceyarısından beri geçen dakika: ", saat*60+dakika)      
```

 İsteğe bağlı olarak bazı deyimleri atama cümlesinin sağında kullanabilirsiniz:

```py
yuzde = (dakika * 100) // 60      
```

 Bu özellik şu an etkileyici görünmeyebilir, ilerleyen süreçte kompozisyonun ne kadar etkili olabileceğini karmaşık hesaplamaları temiz ve kısaca yapabildiğinizde göreceksiniz.

 Uyarı: Bazı deyimleri kullanmanıza yönelik olarak kısıtlamalar vardır. Örneğin, atama cümlesinin sol tarafı mutlaka *değişken* ismi olmalıdır, deyim olamaz. Bu yüzden, aşağıdaki geçersiz bir ifadedir: `dakika + 1 = saat`.

## 2.11 Yorumlar

 Programlar büyüyüp, karmaşıklaştıkça okunması zorlaşmaktadır. Biçimsel diller yoğundur ve kaynak kodun bir parçasına bakıp ne yaptığını veya neden bunu yaptığını anlamak oldukça zordur.

 Bu nedenle, programlara kodu açıklayan doğal dilde notlar ve açıklamalar yazmak iyi bir fikirdir. Bu notlara **yorumlar** adı verilmektedir, ve `#` işaretiyle belirtilir:

```py
# gecen saatin yuzdesini hesaplayalim 
yuzde = (dakika * 100) // 60      
```

 Bu durumda yorum bir satır şeklinde gözükür. Yorumlar ayrıca satır sonuna da yerleştirilebilir:

```py
yuzde = (dakika * 100) // 60 # dikkat: tamsayi bolme      
```

`#` işaretinden itibaren satır sonuna kadar her şey yoksayılır - program üzerinde bir etkisi yoktur-. Yorumların amacı ileride programı okuyacak ve inceleyecek programcılar içindir. Bu durumda, okuyucuya tamsayı bölme durumunu hatırlatma görevi üstlenmiştir.

## 2.12 Sözlük

değer:
: Bir değişkende saklanabilecek veya bir deyimde hesaplanacak bir sayı veya karakter dizisidir (veya daha sonra isimlendirilecek bir şey).

tip:
: Değerler kümesidir. Bir değerin tipi, deyimler içerisinde nasıl kullanabileceğini belirler. Şu ana kadar gördüğünüz değerler tamsayılar (`int` tipi), kayan noktalı sayılar (`float` tipi) ve karakter dizileridir (`string` tipi).

int:
: Pozitif ve negatif tam sayıları tutan Python veri tipidir.

str:
: Karakter dizisi (string) tutan Python veri tipidir.

float:
: *Kayan noktalı* sayıları saklayan Python veri tipidir. Kayan noktalı sayılar içsel olarak iki parça şeklinde saklanır: bir *taban* ve bir *üst*. Standart biçimde görüntülendiğinde, ondalık sayılar gibi gözükürler. `float` kullandığınızda yuvarlama hatalarına dikkat etmeniz gerekmektedir, ve yaklaşık değer barındırırlar.

değişken:
: Bir değeri temsil eden isimdir.

atama cümlesi:
: Bir isime (değişkene) değer atayan cümledir. Atama işlecinin , `=`, sol tarafı bir isimdir. Atama işlecinin sağ tarafı ise Python yorumlayıcısı tarafından değerlendirilecek ve isime atanacak değeri üretecek deyimdir. Atama işlecinin sol ve sağ taraflar arasındaki fark genellikle yeni programcıların kafasını karıştırabilir. Aşağıdaki atamada:

```py

n = n + 1
          
```

`n` değişkeni `=` işlecinin iki tarafında farklı görevler üstlenir. Sağ tarafta bir *değerdir* ve Python yorumlayıcısı tarafından sol taraftaki isme atanmadan önce değerlendirilecek *deyimin* bir kısmını oluşturur.

atama işleci:
: `=` Python'un temel atama işlecidir, aynı işareti kullanan matematiksel karşılaştırma işleci ile karıştırılmamalıdır.

durum diyagramı:
: Değişkenlerin ve referans ettikleri değerlerin grafiksel bir gösterimidir.

değişken ismi:
: Bir değişkene verilen isimdir. Python'da değişken isimleri bir harf ile başlayan harf (a..z, A..Z ve \_) ve sayılardan (0..9) serilerinden oluşur. En iyi programlama pratiğinde değişken isimleri program içerisindeki kullanımlarını anlatacak şekilde seçilir, böylece program için *öz belgeleme* yapmış olur.

anahtar kelime:
: Derleyici tarafından programı ayrıştırmak için ayrılmış kelimelerdir; anahtar kelimelerini - `if`, `def`, ve `while` gibi - değişken isimleri olarak kullanamazsınız.

cümle:
: Python yorumlayıcı tarafından yürütülebilecek yönergedir (komuttur). Cümlelerin örnekleri atama cümleleri ve print cümlesini içerir.

deyim:
: Tek bir sonuç değeri temsil eden değişken, işleç ve değerlerin bir kombinasyonudur.

değerlendirme:
: Bir deyimi basitleştirmek ve tek bir değer üretmek için sırasıyla işlemleri gerçekleştirmektir.

işleç:
: Toplama, çarpma veya karakter dizisi birleştirme gibi tek bir hesaplamayı temsil eden özel işarettir.

işlenen:
: İşlecin üzerinde işlem yaptığı değerlerden biridir.

tamsayı bölme:
: Bir tamsayıyı başka bir tamsayı ile bölüp, tamsayı değer üreten işlemdir. Tamsayı bölme sadece bölünenin bölende kaç kere geçtiğini bulan tam sayılar üretir, kalanı yoksayar. Yeni python programlama dilinde tamsayı bölmek için `//` kullanmalısınız.

öncelik kuralları:
: Çok sayıda işleç ve işlenen içeren deyimlerin değerlendirilme sırasını belirleyen kurallar kümesidir.

birleştirme:
: İki işlenen uç uca eklemedir.

kompozisyon:
: Basit deyimleri ve cümleleri, karmaşık hesaplamaları temsil etmek için bir araya getirip bileşik cümleler ve deyimler oluşturma özelliğidir.

yorum:
: Program içerisinde diğer programcılar (veya kaynak kodu okuyan herhangi biri için) yazılmış olan bilgilerdir ve programın çalışması üzerinde bir etkisi yoktur.

## 2.13 Alıştırmalar

- Aşağıdaki atama cümlelerini çalıştırdığınızda olanları kaydedin:

```py
 >>> print(n = 7)
            
```

 Peki bu?

```py
 >>> print (7 + 5)
            
```

 Ya bu?

```py
 >>> print (5.2, "bu", 4 - 2, "şu", 5/2.0 )
            
```

`print` cümlesi için genel bir kural düşünebiliyor musunuz? `print` cümlesi ne döndürmektedir?

- *Tüm iş ve oyun oynamama Mustafa'yı anlayışsız yapmaktadır* cümlesini ele alın ve her kelimeyi farklı bir değişkende saklayın, son olarak cümleyi tek bir print cümlesi yardımıyla tek satırda yazdırın.

- `6*1-2` ifadesine parantez ekleyerek değerini 4'ten -6'ya dönüştürün.

- Daha önce çalışmış bir koda yorum ekleyerek tekrar çalıştırın, ve sonucu inceleyin.

- Python yorumlayıcısını başlatın ve `bruce+4` ifadesini bilgi istemine girin. Bu size bir hata verecektir:

```py
 NameError: name 'bruce' is not defined 
            
```

`bruce` ismine bir değer atayın, böylece `bruce + 4`, `10` değerini üretebilsin.

- Kullanıcıya iki tam sayı sorulur ve arasında dört işlem yaptırılıp ekrana yazdırılır.

- Kullanıcıya havanın sıcaklığı santigrat cinsinden sorulur ve fahrenayta çevrilir. (F = 9C/5 + 32 )

- Kullanıcıya hikayesindeki karakterlerin isimleri sorulur ve o isimlerle hikaye yazdırılır.

- Kullanıcıya yaşı sorulur ve doğum tarihi hesaplanır.

- Kullanıcıya çap sorulur ve dairenin çevresi ve alanı hesaplanır. (alan = pi r^2) (cevre = 2pi r) (r = R/2)

- Kullanıcıya elindeki türk parası miktarı sorulur, gelen yanıta göre ne kadar dolar ve euro alacağı söylenir.

- Saate bakıyorsunuz ve öğleden sonra 2 olduğunu görüyorsunuz. Alarmınızı 51 saat sonrasına kuruyorsunuz. Hangi saatte alarmınız çalışır? Programlayınız

- Yukarıdaki programı çözecek genel bir Python programı yazın. Kullanıcıya saat cinsinden şimdiki zamanı ve kaç saat beklenmesini soran bir program yazınız. Programınız, alarm çaldığında saatin kaç olduğunu gösteren bir çıkış vermelidir.
