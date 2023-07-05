---
title: Python Programlama Ders 12. Sözlükler
author: sonsuz
date: 2023-07-06 00:11:14 +0300
categories: [Program,Python]
tags: [python,programlama,sözlük,liste,tuple,küme]
---



Şimdiye kadar incelediğimiz tüm bileşik tipler -- karakter dizileri, listeler, ve çok öğeliler (tuple) -- ardışık tiplerdir, içerdikleri değerlere erişmek için tamsayılar indis olarak kullanılır.

**Sözlükler** farklı bileşik tiplerdir. Python'un yerleşik **eşleştirme tipi**dir. Değişmez, sabit olan **Anahtarları (key)** herhangi bir tipteki değerlere eşler, aynı çok öğeli veya listelerdeki değerler gibi.

Örnek olarak, Türkçe kelimeleri İspanyolca'ya çeviren bir sözlük yaratacağız. Bu sözlük için anahtarlar karakter dizisidir.

Sözlük yaratmanın bir yolu boş bir sözlükle başlamak ve daha sonra **anahtar-değer çiftleri** eklemektir. Boş sözlük `{}` ile gösterilmektedir:

```py
>>> tr2sp = {}
>>> tr2sp['bir'] = 'uno'
>>> tr2sp['iki'] = 'dos'
```

İlk atama `tr2sp` adında bir sözlük yaratır; diğer atamalar sözlüğe yeni anahtar-değer çiftlerini ekler. Sözlüğün geçerli değerini her zamanki gibi yazdırabiliriz:

```py
>>> print(tr2sp)
{'iki': 'dos', 'bir': 'uno'}
```

Sözlükteki anahtar-değer çiftleri virgülle ayrılmıştır. Her çift iki nokta üstüste ile ayrılmış bir anahtar ve değer içerir. 

Çiftlerin sırası beklendiği gibi olmayabilir. Python sözlükte anahtar-değer çiftlerinin nerede saklanacağını belirlemek için karmaşık algoritmalar kullanır. Amaçlarımız açısından bu sıralamanın önceden kestirilemeyen olduğunu düşünebiliriz

Sözlük yaratmanın bir diğer yolu önceki çıktıda gördüğümüz sözdiziminde anahtar-değer çiftlerinden oluşan bir liste sağlamaktır::

```py
>>> tr2sp = {'bir': 'uno', 'iki': 'dos', 'üç': 'tres'}
```

Çiftlerin yazılış sırasının önemi yoktur. Sözlükteki değerlere anahtarlarla erişilir, indislerle değil. Bu yüzden sıralamayla uğraşmaya gerek yoktur.

Aşağıdaki ilgili değeri bulmak için anahtarın nasıl kullanıldığını görebilirsiniz:

```py
>>> print(tr2sp['iki'])
'dos'
```

`'iki'` anahtarı `'dos'` değerini döndürmektedir.

## 12.1 Sözlük işlemleri

`del` ifadesi sözlükten anahtar-değer çiftini siler. Örneğin aşağıdaki sözlük meyve isimlerini ve her meyvenin stoktaki miktarını tutmaktadır:

```py
>>> stok = {'elma': 430, 'muz': 312, 'portakal': 525, 'erik': 217}
>>> print(stok)
{'portakal': 525, 'elma': 430, 'erik': 217, 'muz': 312}
```

Eğer birisi tüm erikleri satın alırsa, ilgili kaydı sözlükten silebiliriz:

```py
>>> del stok['erik']
>>> print(stok)
{'portakal': 525, 'elma': 430, 'muz': 312}

```

Eğer yakın zamanda daha fazla erik gelmesini bekliyorsak, sadece eriklerin değerini değiştiririz:

```py
>>> stok['erik'] = 0
>>> print(stok)
{'portakal': 525, 'elma': 430, 'erik': 0, 'muz': 312}
```

`len` işlemi sözlüklerde de çalışır; anahtar-değer çiftlerinin sayısını döndürür:

```py
>>> len(stok)
4
```

## 12.2 Sözlük metotları

Sözlükler bazı yararlı yerleşik metotlara sahiptir.

`keys` metotu bir sözlük parametresi alır ve o sözlüğün anahtarlarını döndürür.

```py
>>> tr2sp.keys()
['üç', 'iki', 'bir']
```

Karakter dizileri ve listelerde gördüğümüz gibi, sözlük metotları da nokta gösterimini kullanır. Noktanın sağına metotun ismi yazılır ve noktanın solundaki değişkene ilgili metotu uygular. Parantezler bu metotun parametre almadığını belirtir.

Metot çağrımına **çağırma (invocation)** adı verilir, `tr2sp` nesnesinde `keys` metodunu çağırdığımızı söyleriz. Nesne yönelimli programlama ile ilgili bölümü incelediğimizde, nesnenin çağrılan metotunun, metotun ilk argümanı olduğunu da göreceğiz.

`values` metotu benzerdir; sözlükteki değerlerin bir listesini döndürür

```py
>>> tr2sp.values()
['tres', 'dos', 'uno']
```

`items` metotu hem anahtarları hem de değerleri, çok öğeli (tuple) liste şeklinde döndürür:

```py
>>> tr2sp.items()
[('üç', 'tres'), ('iki', 'dos'), ('bir', 'uno')]
```

`has_key` metotu argüman olarak bir anahtar alır ve eğer sözlük anahtarı içeriyorsa`True` içermiyorsa `False` değerini döndürür:

```py
>>> tr2sp.has_key('bir')
True
>>> tr2sp.has_key('deux')
False
```

Bu metot çok yararlı olabilir, çünkü sözlükte olmayan bir anahtara erişmek çalışma zamanı hatasına yol açar:

```py
>>> tr2esp['dog']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'dog'
>>> 
```

## 12.3 Rumuz ve kopyalama

Sözlükler değiştirilebilir olduğu için rumuz kullanımına karşı dikkatli olmalısınız. Ne zaman iki değişken aynı nesneyi gösterirse, herhangi birine yapılan değişiklikler diğerini de etkiler.

Eğer sözlüğünüzü değiştirmek ama asılın bir kopyasını saklamak istiyorsanız, `copy` metotunu kullanmalısınız. Örneğin, `karsitlar` karşıt çiftleri içeren bir sözlük olsun:

```py
>>> karsitlar = {'up': 'down', 'right': 'wrong', 'true': 'false'}
>>> rumuz = karsitlar
>>> kopya = karsitlar.copy()
```

`rumuz` ve `karsitlar` aynı nesneyi göstermektedir;
`kopya` ise aynı sözlüğün yeni bir kopyasını göstermektedir. Eğer `rumuzu` değiştirirsek, `karsitlar` da değişecektir:

```py
>>> rumuz['right'] = 'left'
>>> karsitlar['right']
'left'
```

Eğer `kopya`yı değiştirirsek, `karsitlar` değişmeyecektir:

```py
>>> kopya['right'] = 'privilege'
>>> karsitlar['right']
'left'
```

## 12.4 Dağınık matrisler

Daha önce bir matrisi temsil etmek için listelerden oluşan liste kullanmıştık. Bu genellikle sıfırdan farklı değerler içeren matrisler için iyi bir çözümdür, ancak aşağıdaki gibi bir [dağınık matris](http://en.wikipedia.org/wiki/Sparse_matrix)i düşünün:

![](illustrations/sparse.png)

Liste temsili çok sayıda sıfır içerecektir:

```py
matris = [[0, 0, 0, 1, 0],
          [0, 0, 0, 0, 0],
          [0, 2, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 3, 0]]
```

Alternatif bir yöntem sözlük kullanmaktır. Anahtarlar için satır ve sütun numalarını içeren tuple kullanabiliriz. Aşağıda aynı matrisin sözlük gösterimini görebilirsiniz:

```py
matris = {(0, 3): 1, (2, 1): 2, (4, 3): 3}
```

Sadece üç anahtar-değer çiftine sahibiz, matriste sıfır olmayan her bir öğe için. Her bir anahtar iki tamsayı içeren bir tuple'dan oluşuyor.

Matrisin öğelerine erişmek için, `[]` işlecini kullanabiliriz:

```py
matris[(0, 3)]
1
```

Dikkat ederseniz sözlük gösterimi söz dizimi içiçe liste sözdiziminden farklıdır. İki farklı tamsayı indis yerine, bir indisimiz, tamsayılardan oluşan tuple indisimiz var.

Ancak bir sorunumuz var. Eğer sıfır olan bir öğeyi belirtmek istersek, hatayla karşılaşırız, çünkü sözlükte o anahtarın girdisi yok:

```py
>>> matris[(1, 3)]
KeyError: (1, 3)
```

`get` metotu bu sorunu çözer:

```py
>>> matris.get((0, 3), 0)
1
```

İlk argüman anahtardır; ikinci argüman ise anahtarın sözlükte olmaması durumunda `get` tarafından geri döndürülecek değerdir:

```py
>>> matris.get((1, 3), 0)
0
```

`get` dağınık matrise erişmenin sözdizimini bariz bir şekilde iyileştirir.

## 12.5 İpuçları

Son bölümdeki `fibonacci` fonksiyonuyla biraz uğraşırsanız, daha büyük argümanların fonksiyonun çalışmasını daha da uzattığını görürsünüz. Çalışma zamanı oldukça hızlı bir şekilde artmaktadır. Bir makinemize, `fibonacci(20)` anında biterken, `fibonacci(30)` yaklaşık olarak 1 sn, ve `fibonacci(40)` ise neredeyse sonsuz süre almaktadır.

Bunun neden olduğunu anlamak için, `fibonacci` fonksiyonunun `n = 4` için **çağrı çizge**sini incelemek lazım:

![](illustrations/fibonacci.png)

Çağrı çizgesi fonksiyon çerçeve kümeleriyle, her çerçeveyi çağırdığı fonksiyonun çerçevelerine bağlayan doğruları gösterir. Çizgenini tepesinde `fibonacci` `n = 4` ve `fibonacci` `n = 3`'ü çağırmaktadır. `fibonacci` `n = 3`'te `fibonnaci` `n = 2` ve `fibonnaci` `n = 1`'i çağırmaktadır. Bu böyle devam eder.

`fibonacci(0)` ve `fibonacci(1)`'in kaç kere çağrıldığını sayın. Bu problemin verimsiz bir çözümüdür, ve problemin argümanı büyüdükçe çözüm kötüleşmektedir.

İyi bir çözüm daha önceden hesaplanmış değerlerin bir sözlükte saklanmasıdır. Sonradan çağrılmak üzere saklanmış önceden hesaplanmış bir değer **ipucu (hint)** adını almaktadır. Aşağıda `fibonacci` fonksiyonunun ipuçlarıyla gerçekleştirimini görebilirsiniz:

```py
onceki = {0: 0, 1: 1}
   
def fibonacci(n):
    if onceki.has_key(n):
        return onceki[n]
    else:
        yeni_deger = fibonacci(n-1) + fibonacci(n-2)
        onceki[n] = yeni_deger
        return yeni_deger
```

`onceki` adını verdiğimiz sözlük, hali hazırda bildiğimiz Fibonacci sayılarını tutmaktadır. Sadece iki çiftle başlarız: 0 1'e eşlenir ve 1 1'e eşlenir.

Her ne zaman`fibonacci` çağrılırsa, önce sözlükte değer var mı diye kontrol eder. Eğer değer varsa, herhangi özyineli bir çağrım yapmadan fonksiyon değeri döndürebilir. Eğer yoksa, yeni değeri hesaplaması gerekir. Yeni değer fonksiyon değer döndürmeden önce sözlüğe eklenir.

Bu `fibonacci` sürümünü kullanarak, makinelerimizin bir göz kırpımında `fibonacci(100)`'ü hesaplamasını sağlayabiliriz.

```py
>>> fibonacci(100)
354224848179261915075L
```

Numaranın sonundaki `L` ifadesi değerin bir `uzun tamsayı` olduğunu belirtmektedir.

## 12.6 Uzun tamsayılar

Python herhangi bir büyüklükteki (elbette makinenizin belleğiyle sınırlıdır :) ) tamsayıyı desteklemek için `long` (uzun tamsayı) tipini sunmaktadır.

Uzun tamsayı değeri oluşturmanın üç yolu vardır. İlki normal bir tamsayıya sığmayacak çok büyük değer üreten bir aritmetik deyim hesaplamaktadır. Bunu daha önce `fibonacci(100)` örneğinde gördük. Bir başka yöntem tamsayının sağına `L` harfini koymaktır:

```py
>>> type(1L)
<type 'long'>

```

Üçüncü yöntem çevrilecek olan argümanla `long`'u çağırmaktır. `long` aynı `int` ve `float`'t olduğu gibi tamsayıları, kayan noktalıları ve hatta rakamlardan oluşan karakter dizisini uzun tamsayıya çevirir:

```py
>>> long(7)
7L
>>> long(3.9)
3L
>>> long('59')
59L
```

## 12.7 Harfleri saymak

[7.bölümde](https://sonsuzus.github.io/posts/python-programlama-ders-07/), bir karakter dizisindeki harfleri sayan bir fonksiyon yazmıştık. Bu problemin daha genel bir biçimi karakter dizisindeki her bir harfin ne kadar yer aldığını gösteren bir sıklık grafiğinin (histogram) oluşturulmasıdır.

Bu şekildeki bir sıklık grafiği bir metin dosyasının sıkıştırılmasında yararlı olacaktır. Çünkü farklı harfler farklı sıklıklarla yer alacaktır, böylece sık karşılaşılan harfler için daha kısa kodlar, seyrek harfler için daha uzun kodlar kullanabiliriz.

Sıklık grafiği oluşturmak için sözlükler şık bir yol sunarlar:

```py
>>> harf_sayilari = {}
>>> for harf in "Mississippi":
...   harf_sayilari[harf] = harf_sayilari.get(harf, 0) + 1
...
>>> harf_sayilari
{'M': 1, 's': 4, 'p': 2, 'i': 4}
```

Boş bir sözlükle başlarız. Karakter dizisindeki her bir harf için, sözlükteki o anki sayıyı bulur (eğer yoksa sıfırdır), o sayıyı arttırırız. Sonda, sözlüğümüzde harflerin anahtar, değerlerin de harf sayıları olduğu durumu elde ederiz.

Sıklık grafiğini alfabetik sıraya göre görüntülemek daha çekici olabilir. Bunu `items` ve `sort` metotlarıyla yapabiliriz:

```py
>>> harfler = harf_sayilari.items()
>>> harfler.sort()
>>> print(harfler)
[('M', 1), ('i', 4), ('p', 2), ('s', 4)]
```

## 12.8 Sözlük

sözlük
: Anahtar-değer çiftlerinde oluşan, anahtarları değerlere eşleyen veri tipidir. Anahtarlar herhangi bir değiştirilemez tip olabilir, değerler ise herhangi bir tip olabilir.

eşleme tipi
: Anahtar ve ilişkili değerlerin kolleksiyonlarından oluşan veri tipidir. Python'un yerleşik tep eşleme tipi sözlüktür. Sözlükler [ilişkili dizi](http://en.wikipedia.org/wiki/Associative_array) soyut veri tipini gerçekleştirmektedir.

anahtar
: Sözlükte bir değere *eşlenen* veri öğesidir. Anahtarlar sözlükteki değerlere bakmak, erişmek için kullanılmaktadır. 

anahtar-değer çifti
: Sözlükteki öğelerin bir çiftidir. Sözlükteki değerlere anahtarlarla erişilir.

ipucu
: Tekrar hesaplamayı önlemek üzere önceden hesaplanmış değerlerin geçici saklanmasıdır.

olay
: Klavye tuşuna basma, fare tıklaması veya bir başka programdan mesaj gibi sinyallerdir.

olay güdümlü program
: Olayları algılayan, işleyen ve kotaran programlardır. Olayları işlemek için kotarıcılar (handler) vardır.

olay döngüsü
: Olayları bekleyen ve onları işleyen programlama yapısı

taşma
: Nümerik biçimde gösterilemeyecek kadar büyük nümerik sonuçtur.

## 12.9 Alıştırmalar

- Komut satırından karakter dizisi okuyan ve alfabedeki harflerin tablosunu girilen karakter dizisindeki bulunma sayısıyla birlikte listeleyen bir program yazınız. Küçük-büyük farkı yok sayılmalıdır. Programın örnek bir çalıştırması aşağıdaki olmalıdır:

```sh
$ python harf_sayilari.py "ThiS is String with Upper and lower case Letters."
a  2
c  1
d  1
e  5
g  1
h  2
i  4
l  2
n  2
o  1
p  2
r  4
s  5
t  5
u  1
w  2
$
```

- Aşağıdaki yorumlayıcı oturumlarındaki sorgular için sonuçları üretin:

	1. Soru 1
    
    ```py
	  >>> d = {'apples': 15, 'bananas': 35, 'grapes': 12} 
	  >>> d['banana']  
	```

	2. Soru 2
    
    ```py	
	  >>> d['oranges'] = 20
	  >>> len(d)   
	```

	3. Soru 3
    
    ```py	
	  >>> d.has_key('grapes')	  
	```
	
    4. Soru 4
    
    ```py	
	  >>> d['pears']	  
	```

	5. Soru 5

    ```py	
	  >>> d.get('pears', 0)	  
	```
	
    6. Soru 6

    ```py	
	  >>> fruits = d.keys()
	  >>> fruits.sort()
	  >>> print(fruits)	  
	```

	7. Soru 7

    ```py	
	  >>> del d['apples']
	  >>> d.has_key('apples')   
	```

Her bir sonucun neden olduğunu da iyi anlamayı unutmayın. Öğrendiklerinizi aşağıda fonksiyon gövdesini doldurmak için kullanın:

```py
def add_fruit(inventory, fruit, quantity=0):
    """
 Adds quantity of fruit to inventory. 

 >>> new_inventory = {}
 >>> add_fruit(new_inventory, 'strawberries', 10)
 >>> new_inventory.has_key('strawberries')
 True
 >>> new_inventory['strawberries']
 10
 >>> add_fruit(new_inventory, 'strawberries', 25)
 >>> new_inventory['strawberries'] 
 """

```

Çözümünüz doctestleri geçmelidir.

- `alice_words.py` isminde bir program yazın, programınız [alice_in_wonderland.txt](https://sonsuzus.github.io/dosya/alice_in_wonderland.txt) dosyasındaki tüm kelimelerin alfabetik listesini her bir kelimenin kaç kere yer aldığıyla birlikte `alice_words.txt` adındaki metin dosyasına yazsın. Çıktınızın ilk 10 satırı aşağıdakine benzeyecektir:

```
Kelime            Adet
=======================
a                 631
a-piece           1
abide             1
able              1
about             94
above             3
absence           1
absurd            2
```

`alice` kelimesi kitapta kaç kere yer almaktadır?

- Alice in Wonderland (Alice Harikalar Diyarında)'ki en uzun kelime hangisidir? Kelime kaç karakter içermektedir??
