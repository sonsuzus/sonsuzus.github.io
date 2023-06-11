---
title:  Python Programlamaya Giriş 2 – Sayılar, Aritmetik, Temel Veri Yapıları
author: sonsuz
date: 2023-06-12 00:25:50 +0300
categories: [Program,Python]
tags: [python,dizi,dize,liste,küme,sözlük,çokuz]
---






Yeni başlayanlar için Python programlamayı anlatan yazı dizimizin ikinci bölümünde sayıları, aritmetik işlemlerini, ve Python’daki temel veri tiplerini (listeler, çokuzlar, dizeler, sözlükler) işliyoruz.


Bu yazıda sadece kısa ve işlevsel bir giriş yapıyoruz. Sonraki bölümlerimizde veri yapılarının kullanımından daha fazla bahsedeceğiz.


# Sayılar ve aritmetik


Python’da öntanımlı (built-in) üç çeşit sayı var: *Tamsayılar*, *reel sayılar*, ve *karmaşık sayılar*. Reel sayılar bilgisayarda *kayan nokta* (floating point) biçiminde temsil edilir. Bilimsel hesaplama yapanlar için kayan nokta temsilini iyi anlamak çok mühim, ama bunu daha sonraya bırakalım.


Bu üç sayı tipiyle öntanımlı olarak yedi aritmetik işlem yapılabilir: Toplama (`+`), çıkarma (`-`), çarpma (`*`), bölme (`/`), tamsayı bölme (`//`), kalan (`%`), ve üs alma (`**`).







In [1]:




```
2 + 3


```








Out[1]:


```
5
```








In [2]:




```
7 - 12.4


```








Out[2]:


```
-5.4
```








In [3]:




```
5.25 * 6.25


```








Out[3]:


```
32.8125
```








In [4]:




```
25 / 8


```








Out[4]:


```
3.125
```








In [5]:




```
25 // 8


```








Out[5]:


```
3
```








In [6]:




```
25 % 8


```








Out[6]:


```
1
```








In [7]:




```
0.5 ** 1.2


```








Out[7]:


```
0.43527528164806206
```










Tamsayılarda üst sınır yoktur; bellek yettiğince büyük sayılara çıkılabilir.







In [8]:




```
3**1000


```








Out[8]:


```
1322070819480806636890455259752144365965422032752148167664920368226828597346704899540778313850608061963909777696872582355950954582100618911865342725257953674027620225198320803878014774228964841274390400117588618041128947815623094438061566173054086674490506178125480344405547054397038895817465368254916136220830268563778582290228416398307887896918556404084898937609373242171846359938695516765018940588109060426089671438864102814350385648747165832010614366132173102768902855220001
```










Reel sayılarda ise üst sınırı aşma (overflow) problemi, başka dillerde olduğu gibi mevcuttur.







In [9]:




```
2.9**1000


```











```
---------------------------------------------------------------------------

OverflowError                             Traceback (most recent call last)

<ipython-input-9-15b45604f3cd> in <module>()

----> 1 2.9**1000



OverflowError: (34, 'Numerical result out of range')
```










Karmaşık sayıları yazarken sanal birimi `1j` veya `1J` olarak yazarız. Ayrıca fonksiyon çağrısı `complex(a,b)` bize `a+bj` sayısını verir.







In [10]:




```
z = 1 + 3j

z ** 2


```








Out[10]:


```
(-8+6j)
```








In [11]:




```
z * 1j


```








Out[11]:


```
(-3+1j)
```








In [12]:




```
z - (3 - 1.3j)


```








Out[12]:


```
(-2+4.3j)
```








In [13]:




```
z - complex(3, -1.3)


```








Out[13]:


```
(-2+4.3j)
```










İki farklı tipte sayı aynı işlemde kullanılırsa, hangi tip daha genelse sonuç o tipte verilir. Tamsayı ve reel sayı kullanılırsa sonuç reeldir; reel sayı ve karmaşık sayı kullanılırsa sonuç karmaşıktır.







In [14]:




```
1 + 4


```








Out[14]:


```
5
```








In [15]:




```
1 + 4.0


```








Out[15]:


```
5.0
```








In [16]:




```
1 + 4 + 0j


```








Out[16]:


```
(5+0j)
```








In [17]:




```
type(1+4), type(1+4.0), type(1+4+0j)


```








Out[17]:


```
(int, float, complex)
```










## Değişken atamaları


Python’da değişkenlerin tiplerini (int, float, vs.) önceden beyan etmek gerekmez. Değişken isimleri, atamanın sağ tarafındaki ifadeye işaret eden bir isimdir sadece.







In [18]:




```
x = -2      # bir tamsayı

y = 3/4 * 2 # reel sayı

z = "Merhaba"+"Dünya" # dize

x,y,z


```








Out[18]:


```
(-2, 1.5, 'MerhabaDünya')
```










Çoklu atamalar yapmak mümkündür:







In [19]:




```
x, y, z = -2, 1.5, "Merhaba Dünya"

x,y,z


```








Out[19]:


```
(-2, 1.5, 'Merhaba Dünya')
```










Bu usulü kullanarak iki değişkenin değerini, bir ara değişken kullanmadan değiştokuş etmek mümkün olur.







In [20]:




```
x,y = y,x

x,y


```








Out[20]:


```
(1.5, -2)
```










Python 3 ile değişken isimlerinde herhangi Unicode karakterleri kullanabilirsiniz.







In [21]:




```
kağıt\_sayısı = 5

ölçü = 0.3


```










Bir değişkeni `del` komutuyla bellekten silebiliriz.







In [22]:




```
del z

print(z)


```











```
---------------------------------------------------------------------------

NameError                                 Traceback (most recent call last)

<ipython-input-22-aecf458f4776> in <module>()

 1 del z

----> 2 print(z)



NameError: name 'z' is not defined
```










## İşlem öncelikleri


İşlemlerin bazıları diğerlerinden daha önce yapılır. Önceliklerde okulda öğrendiğimiz kurallar genelikle geçerlidir. Aynı ifade içinde önce üs alma, sonra çarpma, bölme ve kalan bulma işlemleri, sonra da toplama ve çıkarma işlemi yapılır. Aynı öncelik sınıfında bulunan işlemler, soldan sağa sırayla yapılır. Öncelik sırasını değiştirmek için parantez kullanılır.







In [23]:




```
2 + 3*4, (2+3)*4


```








Out[23]:


```
(14, 20)
```








In [24]:




```
4 + 3**2, (4+3)**2


```








Out[24]:


```
(13, 49)
```








In [25]:




```
3*4/2*6, 3*4/(2*6)


```








Out[25]:


```
(36.0, 1.0)
```










Öncelik sırası kavramı aritmetik işlem olsun olmasın, dildeki her türlü operatör için de geçerlidir. Tam bir liste için [Python referans sayfalarına](http://docs.python.org/2/reference/expressions.html#operator-precedence) bakabilirsiniz.


Atama (`=`) işlemi en düşük önceliğe sahiptir. Bir değişkene bir değer ataması yaparken önce eşit işaretinin sağ tarafının değeri hesaplanır. Değişkene değer atama işlemi en son yapılır. Python’da bir atama başka bir ifadenin parçası olamaz.







In [26]:




```
x = 1

x = 3*x + 5

x


```








Out[26]:


```
8
```








In [27]:




```
(x=3)*x+5


```











```
 File "<ipython-input-27-5aaaedf6169a>", line 1

 (x=3)*x+5

      ^

SyntaxError: invalid syntax


```










# Öntanımlı veri yapıları


Sayılara ek olarak, Python diline dahil birkaç öntanımlı veri yapısı var. Bunları daha sonraki bölümlerde daha ayrıntılı işleyeceğiz. Şimdilik, pratik kullanıma yetecek kadar tanıtalım.


## Dizeler


Bir *dize* (string), karakterlerin (harf, rakam, ve diğer işaretler) birleşiminden oluşur. Tek tırnak veya çift tırnak içinde olmalıdır.


Dizenin içindeki karakterlere indeksleme işlemi `[]` ile erişilebilir. İndeks değerleri sıfırdan başlar; birinci karakter için 0, ikinci karakter için 1, vs. Negatif indeksler sondan başlayarak saymak için kullanılabilir: Son karakter için -1, sondan bir önceki için -2, vs. gibi.







In [28]:




```
isim = "Albert Einstein"

isim[0] # İlk karakter


```








Out[28]:


```
'A'
```








In [29]:




```
isim[1] # İkinci karakter


```








Out[29]:


```
'l'
```








In [30]:




```
isim[-1] # Son karakter


```








Out[30]:


```
'n'
```








In [31]:




```
isim[-2] # Sondan bir önceki karakter


```








Out[31]:


```
'i'
```










## Çokuzlar


Bir çokuz (tuple) çeşitli nesneleri yuvarlak parantezler içinde birleştirir. Çokuz elemanlarının aynı tipten olması gerekmez. Dizelerde kullanılan indeksleme kuralları çokuzlarda da geçerlidir.







In [32]:




```
a = (3.14, 2, 'Albert', 3+4j, (7.25,-23))

a[0]  # birinci eleman


```








Out[32]:


```
3.14
```








In [33]:




```
a[-1][0] # Son elemanın birinci elemanı


```








Out[33]:


```
7.25
```










Çokuzlar atamada kullanılırsa, her eleman birebir eşleştirilerek atama yapılır.







In [34]:




```
(x, y, z) = (-1.25, 42, "Merhaba")


```








In [35]:




```
x


```








Out[35]:


```
-1.25
```








In [36]:




```
y


```








Out[36]:


```
42
```








In [37]:




```
z


```








Out[37]:


```
'Merhaba'
```










Virgülle ayrılmış bir ifade otomatik olarak çokuza dönüştürülür, yani yukarıdaki örneği



```
x, y, z = -1.25, 42, "Merhaba"


```

şeklinde de yazabilirsiniz. Yukarıda bahsettiğimiz çoklu atama bu şekilde çalışır.


Dizelerle çokuzların ortak özellikleri *değiştirilemez* (immutable) olmalarıdır. Elemanlarına yeni değerler atayamazsınız.







In [38]:




```
z = "Merhaba"

z[0] = "m"


```











```
---------------------------------------------------------------------------

TypeError                                 Traceback (most recent call last)

<ipython-input-38-f230cddd9827> in <module>()

 1 z = "Merhaba"

----> 2 z[0] = "m"



TypeError: 'str' object does not support item assignment
```








In [39]:




```
a = (1,2,3)

a[0] = -1


```











```
---------------------------------------------------------------------------

TypeError                                 Traceback (most recent call last)

<ipython-input-39-fd140231955b> in <module>()

 1 a = (1,2,3)

----> 2 a[0] = -1



TypeError: 'tuple' object does not support item assignment
```










## Listeler


Liste, köşeli parantez içinde, virgülle ayrılmış elemanları birleştiren br yapıdır. Çokuzlar gibi listelerde de elemanlar farklı tiplerde olabilir. Dizeler ve çokuzlar için geçerli olan eleman indeksleme işlemleri listelerde de aynen geçerlidir. Listelerin çokuzlardan farkı *değiştirilebilir* (mutable) olmalarıdır, yani elemanlarına tekrar atama yapılabilir.







In [40]:




```
liste = [5, "merhaba", (2,3,1), [-1,0,2]]

liste[0] = 4.1  # birinci elemanı değiştir

liste[-1][0] = 12 # son elemanın birinci elemanını değiştir

liste


```








Out[40]:


```
[4.1, 'merhaba', (2, 3, 1), [12, 0, 2]]
```








In [41]:




```
liste[1] = "naber" # İkinci elemana başka bir dize ata.

liste


```








Out[41]:


```
[4.1, 'naber', (2, 3, 1), [12, 0, 2]]
```








In [42]:




```
del liste[2] # Üçüncü elemanı sil

liste


```








Out[42]:


```
[4.1, 'naber', [12, 0, 2]]
```










Ancak, listenin bir elemanı değiştirilemez bir tipteyse, o elemanın alt elemanlarını silemez veya onlara atama yapamazsınız.







In [43]:




```
liste[1][0] = "h"


```











```
---------------------------------------------------------------------------

TypeError                                 Traceback (most recent call last)

<ipython-input-43-28d51272027e> in <module>()

----> 1 liste[1][0] = "h"



TypeError: 'str' object does not support item assignment
```










## Sözlükler


Dize, çokuz, ve liste tipleri *sıralı tip* (sequence type) olarak anılır, çünkü birinci elemandan son elemana kadar iyi tanımlanmış bir düzenleri mevcuttur. Sözlük (dictionary) tipi ise sıralı değildir. Sözlükler, listelerin genelleştirilmiş halidir: Listelerde elemanların referanslarının sıfırdan başlayan tamsayılar olması gerekirken, sözlüklerde ise çok değişik veri tipleri her şey referans olarak kullanılabilir. Bu tür veri tipleri *hash table*, *hash map*, veya *associative array* olarak da bilinirler.







In [44]:




```
d = {-1.75: "merhaba", "isim":"Einstein"}

d[-1.75]


```








Out[44]:


```
'merhaba'
```








In [45]:




```
d["isim"]


```








Out[45]:


```
'Einstein'
```








In [46]:




```
d[(2,3)] = [1,2,3.14159]

d


```








Out[46]:


```
{-1.75: 'merhaba', 'isim': 'Einstein', (2, 3): [1, 2, 3.14159]}
```








In [47]:




```
d[-2.25] = 3 + 5j

d[1+2j] = 42

d["isim"] = "Eisenstein"

d


```








Out[47]:


```
{-1.75: 'merhaba',

 'isim': 'Eisenstein',

 (2, 3): [1, 2, 3.14159],

 -2.25: (3+5j),

 (1+2j): 42}
```








In [48]:




```
del d["isim"]

d


```








Out[48]:


```
{-1.75: 'merhaba', (2, 3): [1, 2, 3.14159], -2.25: (3+5j), (1+2j): 42}
```










Sözlük yaratırken süslü parantezler `{}` kullanırız. Sözlük elemanlarına ise, çokuzlar ve listelerdeki gibi, köşeli parantez içinde referans değerini yazarak erişiriz. Yeni referans değerlerine sahip sözlük elementleri yaratabilir, istemediğimiz elemanları `del` komutuyla silebiliriz.


Sözlüklerde referans olarak sadece *değiştirilemez* tipler kullanılabilir (sayılar, dizeler, çokuzlar). Listeler kullanılamaz.







In [49]:




```
d[ [1,2,3] ] = 5


```











```
---------------------------------------------------------------------------

TypeError                                 Traceback (most recent call last)

<ipython-input-49-a6eaea156f9e> in <module>()

----> 1 d[ [1,2,3] ] = 5



TypeError: unhashable type: 'list'
```









