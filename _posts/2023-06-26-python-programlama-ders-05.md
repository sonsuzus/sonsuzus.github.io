---
title: Python Programlama Ders 5. Değer döndüren fonksiyonlar
author: sonsuz
date: 2023-06-26 18:10:15 +0300
categories: [Program,Python]
tags: [fonksiyon,değer döndüren,değer,return,ürün,kod,ders,eğitim,arttırımsal geliştirme]
---



## 5.1 Geri dönüş değerleri

Şimdiye kadar kullandığımız `abs`, `pow` ve `max` benzeri içsel olarak tanımlı fonksiyonlar sonuç ürettiler, yani bir değer döndürdüler. Her bu fonksiyonları çağırmamız bir değer üretmektedir, bu üretilen değeri genellikle bir değişkene atama veya bir deyimin parçası haline getirdik.

```py
biggest = max(3, 7, 2, 5)
x = abs(3 - 11) + 10
```

Ancak şimdiye kadar kendi yazdığımız fonksiyonların hiçbiri bir değer üretip, döndürmedi.

Bu bölümde değer döndüren fonksiyonlar yazacağız, bunlara da **değer döndüren fonksiyonlar** veya **ürün veren (ürünlü) fonksiyonlar** adını, daha iyi anlamlı bir isim gereksinimden dolayı, vereceğiz. İlk örneğimiz `area` örneği, bu fonksiyon yarıçapı verilen bir dairenin alanını bize döndürecek:

```py
def area(radius):
    temp = 3.14159 * radius**2
    return temp
```

`return` cümlesini daha önce görmüştük, ancak ürün veren bir fonksiyonda `return` cümlesi bir **geri dönüş değeri** içerir. Bu cümlenin anlamı: Hemen çağrıldığın yere geri dön ve devamımdaki ifadeyi geri dönüş değeri olarak kullandır. Deyim isteğimize bağlı olarak karmaşık olabilir, örneğin yukarıdaki fonksiyonu aşağıdaki gibi de yazabiliriz:

```py
def area(radius):
    return 3.14159 * radius**2
```

Ancak, diğer taraftan `temp` gibi **geçici değerleri** kullanmak hata ayıklamayı kolaylaştırır.

Bazı durumlarda birden fazla geri dönüş cümlesine sahip olmak faydalıdır, her bir koşullu dallanmada bir geri dönüş yapılabilir. Bunu daha önce içsel tanımlı `abs` fonksiyonunda görmüştük, şimdi kendi örneğimizi yazalım::

```py
def absolute_value(x):
    if x < 0:
        return -x
    else:
        return x
```

`return` cümleleri farklı alternatif koşullarda olduğu için, aralarından sadece biri yürütülecektir. Biri yürütülür yürütülmez fonksiyon geri kalan cümlelerini çalıştırmadan sonlanacaktır.

Yukarıdaki fonksiyonu yazmanın başka bir yolu da `else`'i kaldırıp koşulunu ikinci `return` cümlesi olarak yazmaktır:

```py
def absolute_value(x):
    if x < 0:
        return -x
    return x
```

Yukarıdaki örnek hakkında düşünüp, aynen ilki gibi çalıştığına kendinizi ikna edin.

`return` cümlesinden sonra gelen herhangi bir kod veya yürütme akışı açısından erişilmez durumda olan kodlar **ölü kod** adını almaktadır.

Bir ürünlü fonksiyonda olası her yolda bir `return` cümlesinin olması iyi bir fikirdir. Aşağıdaki `absolute_value` sürümü bunu gerçekleştirmemektedir:

```py
def absolute_value(x):
    if x < 0:
        return -x
    elif x > 0:
        return x
```

Bu sürüm doğru bir sürüm değildir çünkü `x` 0 olduğunda hiç bir koşul doğru olmayacağı için, fonksiyon herhangi bir `return` cümlesine rastlamayacaktır. Bu durumda geri dönüş değeri özel bir değer olan **`None`** olacaktır:

```py
>>> print(absolute_value(0))
None
```

`None`, `NoneType` tipinin tekil değeridir.

```py
>>> type(None)
<type 'NoneType'>
```

Tüm Python fonksiyonları başka bir değer döndürmüyorlarsa, `None` değerini döndürürler.

## 5.2 Program geliştirme

Bu noktada, tamamlanmış fonksiyonlara bakarak ne yaptıklarını anlayabilmeniz ve anlatabilmeniz gerekmektedir. Ayrıca, eğer alıştırmaları yapıyorsanız, bazı küçük fonksiyonlar da yazmış olmanız gerekiyor. Daha büyük fonksiyonlar yazdıkça zorlanmaya başlarsınız, özellikle çalışma zamanı ve anlambilimsel hatalar artmaya başlar.

Artan bir şekilde karmaşık programlarla başa çıkmak için, bir teknik önereceğiz. Bu tekniğe **arttırımsal geliştirme** adı verilmektedir. Arttırımsal geliştirmenin hedefi uzun hata ayıklama süreçlerini kısaltmak için bir anda küçük bir kod parçası eklemek ve bu parçayı sınamaktır.

Örnek olarak iki nokta arasındaki uzaklığı bulmak istediğinizi varsayalım. Koordinatları verilmiş olan (x1,y1) ve (x2,y2) noktalarının arasındaki uzaklığı Pisagor teoremine göre şu şekilde hesaplarız:

![](illustrations/distance_formula.png)

İlk adım `distance` fonksiyonunun Python'da nasıl gözükeceğini düşünmektir. Başka bir ifadeyle, girdiler (parametreler) nedir ve çıktı (geri dönüş değeri) nedir sorularına cevap bulmaktır?

Bu örnekte, iki nokta girdilerimizdir ve bu girdileri dört parametre ile temsil edebiliriz. Geri dönüş değerimiz uzaklıktır, bu da kayan noktalı bir sayıdır.

Bu cevaplardan sonra fonksiyonumuzun ana hatlarını yazabiliriz:

```py
def distance(x1, y1, x2, y2):
    return 0.0
```

Açıkça görülmektedir, fonksiyonumuzun bu sürümü uzaklıkları hesaplamamaktadır; her zaman sıfır değerini döndürecektir. Ancak sözdizimsel olarak doğrudur ve çalışabilir. Bunun anlamı bu fonksiyonu daha fazla karmaşıklaştırmadan önce sınayabiliriz.

Yeni fonksiyonu sınamak için, örnek değerlerle çağıracağız:

```py
>>> distance(1, 2, 4, 6)
0.0
```

Bu değerleri seçmemizin nedeni yatay uzaklığın 3, dikey uzaklığın 4 olması sonucu iki nokta arasındaki uzaklığın 5 olmasıdır (3-4-5 üçgeninde hipotenüs). Fonksiyonu sınarken, doğru cevabı bilmek yararlıdır.

Bu noktada fonksiyonun sözdizimsel olarak doğru olduğunu onaylamış olduk, yeni kod satırları ekleyebiliriz. Her bir arttırımsal değişiklikten sonra fonksiyonu tekrar sınarız. Eğer herhangi bir noktada hata ile karşılaşırsak bulmamız kolay olacaktır. En son eklediğimiz kod olmalıdır (satır satır ilerlersek hatayı en son eklediğimiz satır yaratmıştır diyebiliriz).

Hesaplamadaki mantıksal ilk adım x2 - x1 ve y2 - y1 farklarını bulmaktır. Bu değerleri geçici değişkenlerde (`dx`, `dy`) saklarız ve ekranda görüntüleriz.

```py
def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    print("dx is", dx)
    print("dy is", dy)
    return 0.0
```

Eğer fonksiyon çalışıyorsa, çıktılar 3 ve 4 olmalıdır. Eğer sonuç böyleyse fonksiyon parametreleri doğru alıp, ilk hesaplamayı doğru yapıyordur. Eğer bir hata varsa kontrol edilecek satır sayısı azdır.

Daha sonra `dx` ve `dy` değişkenlerinin karelerini toplarız:

```py
def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    print("dsquared is: ", dsquared)
    return 0.0
```

Dikkat ederseniz `print` cümlelerini kaldırdık. Bu tip kodlara **iskele (scaffolding)** adı verilmektedir, son ürünümüzün bir parçası değildir ancak programı yazarken yararlıdır.

Bu aşamada programı tekrar çalıştırıp çıktıyı kontrol ederiz (25 olmalıdır).

Son olarak, kesirsel üs `0.5`'i kullanarak kare kökü hesaplar ve sonuç olarak geri döndürürüz:

```py
def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = dsquared**0.5
    return result
```

Eğer bu doğru çalışırsa, işimiz bitmiştir. Çalışmazsa, `result` değişkenini geri döndürmeden önce ekranda görüntülememiz gerekebilir.

Başladığınızda, bir anda sadece bir iki satırlık kod eklemeniz gerekir. Deneyim kazandıkça kendinizi daha büyük parçalar yazıp, sınayıp, hata ayıklar durumda bulacaksınız. Her şekilde, arttırımlı geliştirme süreci sizi sıkıntılı fazla hata ayıklama zamanından kurtaracaktır.

Sürecin anahtar hatları şunlardır:

1. Çalışan bir programla başlayıp küçük artımlı değişikler yapın. Herhangi bir noktada bir hata varsa hatanın nerede olduğunu bileceksiniz.
2. Ara değerleri tutmak için geçici değişkenler kullanın böylece bu değerleri ekran gösterip kontrol edebilirsiniz.
3. Program çalışır hale gelince, iskelet kodlarının bazılarını kaldırmanız ve birden fazla cümleyi bileşik deyimler haline getirmeniz gerekebilir, elbette bu birleştirme işlemini programın okunabilirliğini zorlaştırmıyorsa yapmanız gerekir.

## 5.3 Kompozisyon

Şimdiye kadar farkedeceğiniz gibi, bir fonksiyonu bir başka fonksiyondan çağırabilirsiniz. Bu yeteneğe **kompozisyon** (bileşim) adı verilmektedir.

Örnek olarak, iki nokta alan (dairenin merkezi ve çevrenin üzerinde bir nokta) bir fonksiyon yazıp dairenin alanını hesaplayacağız.

Merkez noktanın `xc` ve `yc` değişkenlerinde, ve çevre üzerindeki noktada `xp` ve `yp` değişkenlerinde saklandığını varsayalım. İlk adım dairenin yarıçapını bulmaktır. Bu da verilen iki nokta arasındaki uzaklıktır. Daha önce yazmış olduğumuz `distance` fonksiyonunu bu iki nokta arasındaki uzaklığı hesaplamak için kullanabiliriz. Ne de olsa bu iş yazılmış, sadece kullanmamız yeterli:

```py
radius = distance(xc, yc, xp, yp)
```

İkinci adım ise bulduğumuz bu yarıçapı kullanarak dairenin alanını hesaplayıp geri döndürmektir. Yine daha önce yazdığımız fonksiyonları kullanacağız:

```py
result = area(radius)
return result
```

Bu kodları bir fonksiyon içine yazarsak:

```py
def area2(xc, yc, xp, yp):
    radius = distance(xc, yc, xp, yp)
    result = area(radius)
    return result
```

Bu fonksiyona `area2` adını `area` fonksiyonundan ayırtetmek için kullandık. Bir modül içerisinde bir isimde sadece tek bir fonksiyon olabilir. Aynı modülde aynı isimden fonksiyonlar yer alamaz.

Geçici `radius` ve `result` değişkenleri geliştirme ve hata ayıklama için yararlıdır, ancak fonksiyon çağrılarını birleştirirsek daha kısa ve öz bir ifade elde ederiz:

```py
def area2(xc, yc, xp, yp):
    return area(distance(xc, yc, xp, yp))
```

## 5.4 Boolean fonksiyonlar

Fonksiyonlar boolean değerler de döndürebilir, bu kullanışlı karmaşık sınamaları fonksiyonların içerisine saklamak için yararlıdır. Örneğin:

```py
def is_divisible(x, y):
    if x % y == 0:
        return True 
    else:
        return False
```

Bu fonksiyonun ismi `is_divisible`'dır. **Boolean fonksiyon**lara evet/hayır cevapları gibi isimler vermek yaygındır. `is_divisible`, `x`'in `y` tarafından bölünebilir olup olmadığına dair `True` veya `False` döndürecektir. 

Fonksiyonu `if` cümlesinin de boolean bir deyim olduğu gerçeğinden yararlanarak daha kısa ve öz bir hale getirebiliriz. Doğrudan deyimi döndürerek, `if` cümlesinin kendisinden kurtulabiliriz:

```py
def is_divisible(x, y):
    return x % y == 0
```

Aşağıda bu yeni fonksiyonun nasıl kullanıldığını görebilirsiniz:

```py
>>> is_divisible(6, 4)
False
>>> is_divisible(6, 3)
True
```

Boolean fonksiyonlar genellikle koşul cümlelerinde kullanılır:

```py
if is_divisible(x, y):
    print("x y tarafından bölünebilir")
else:
    print("x y tarafından bölünemez")
```

Aşağıdaki gibi bir şey yazmak isteyebilirsiniz:

```py
if is_divisible(x, y) == True:
```

Ancak ek karşılaştırma tamamen gereksizdir.

## 5.5 `function` tipi

Fonksiyonlar Python'da farklı bir tiptir. Bu tip `int`, `float`, `str`, `bool` ve `NoneType`'i kapsar.

```py
>>> def func():
...    return "fonksiyon func çağrıldı..."
...
>>> type(func)
<type 'function'>
>>>
```

Diğer tiplerde olduğu gibi, fonksiyonlar başka fonksiyonlara argüman olarak geçirilebilir:

```py
def f(n):
    return 3*n - 6

def g(n):
    return 5*n + 2

def h(n):
    return -2*n + 17

def doto(value, func):
    return func(value)
    
print(doto(7, f))
print(doto(7, g))
print(doto(7, h))

```

`doto` üç kere çağrılmıştır. 7 her sefer için fonksiyonun `value` argümanıdır; `f`, `g` ve `h` `func` argümanı olarak geçirilmektedir. Bu betiğin çıktısı şu şekildedir:

```py
15
37
3
```

Bu örnek her ne kadar yapmacık bir örnek olsa da, ileride bir fonksiyona fonksiyonun geçirilmesinin yararlı olduğu durumlar karşımıza çıkacaktır.

## 5.6 Program yazım kuralları

Okunabilirlik programcılar açısında çok önemlidir, çünkü pratikte programların yazılmasından ziyade okunup değiştirildikleri daha sık karşılaşılan bir durumdur. Bu kitaptaki tüm örnekler Python topluluğu tarafından geliştirilen yazım rehberi ile tutarlı olacaktır.

Yazım kuralları konusunda programlarımız karmaşıklaştıkça söyleyeceklerimiz artacaktır, ancak şimdiden bir kaç noktayı açıklamak yararlı olacaktır:

* girintiler için 4 boşluk karakteri kullanın
* içe aktarmalar (import) dosyaların en üstünde yer almalıdır
* fonksiyon tanımlamaları arasında iki boş satır olmalıdır
* fonksiyon tanımlamaları bir arada olmalıdır
* en üst seviye cümleler, fonksiyon çağrımları da dahil olmak üzere, birlikte programın en altında tutun

## 5.7 Üçlü tırnaklı karakter dizileri

İlk olarak 2. Bölümde gördüğümüz tek ve çift tırnaklı karakter dizilerine ek olarak, *üç tırnaklı karakter dizileri*'da Python'da vardır:

```py
>>> type("""Bu bir üç çift tırnaklı karakter dizisidir""")
<type 'str'>
>>> type('''Bu bir üç tek tırnaklı karakter dizisidir''')
<type 'str'>
>>>
```

Üç tırnaklı karakter dizileri hem tek hem de çift tırnakları içerisinde barındırabilir:

```py
>>> print('''"Oh hayır", diye bağırdı, "Ben'in bisikleti bozuldu!"''')
"Oh hayır", diye bağırdı, "Ben'in bisikleti bozuldu!"
>>>
```

Son olarak, üç tırnaklı karakter dizileri bir kaç satıra bölünebilir:

```py
>>> message = """Bu mesaj
... bir kaç satıra
... bölünecektir."""
>>> print(message)
Bu mesaj
bir kaç satıra
bölünecektir.
>>>

```

## 5.8 `doctest` ile birim sınama (unit test)

Bu günlerde yazılım geliştirmede kaynak kodun otomatik **birim sınama**sını yapmak yaygın bir pratiktir. Birim sınama, fonksiyonlar gibi bağımsız kod parçalarının otomatik olarak doğru çalıştığını onaylamak için bir yol sağlar. Bu daha sonra fonksiyonun gerçekleştirimini değiştirmeyi ve yine de bekleneni yapmasını olanaklı kılar.

Python `doctest` isimli kolay birim sınama için bir modül barındırır. Doctestler fonksiyon gövdesinin veya betiğin *ilk satırın*da üç tırnaklı karakter dizileri içerisinde yazılabilir. Bunlar bir Python bilgi istemine girdileri ve beklenen çıktıyı örnekleyen yorumlayıcı oturumları şeklindedir.

`doctest` modülü `>>>` ile başlayan herhangi bir cümleyi otomatik olarak çalıştırarak, takip eden cümleyi yorumlayıcının çıktısıyla karşılaştırır.

Bunun nasıl çalıştığını görmek için aşağıdaki kodları `myfunctions.py` isimli bir betiğe koyup deneyiniz:

```py
def is_divisible_by_2_or_5(n):
    """
 >>> is_divisible_by_2_or_5(8)
 True
 """


if __name__ == '__main__':
    import doctest
    doctest.testmod()
```

Son üç satır `doctest`in çalışmasını sağlayan satırlardır. Bu satırları doctestleri içeren herhangi bir dosyanın en altına koymalısınız. Nasıl çalıştıklarını 10. bölümde modülleri anlatırken açıklayacağız.

Yukarıdaki betiği çalıştırmanız aşağıdaki çıktıyı üretecektir:

```py
$ python myfunctions.py 
**********************************************************************
File "myfunctions.py", line 3, in __main__.is_divisible_by_2_or_5
Failed example:
    is_divisible_by_2_or_5(8)
Expected:
    True
Got nothing
**********************************************************************
1 items had failures:
   1 of   1 in __main__.is_divisible_by_2_or_5
***Test Failed*** 1 failures.
$

```

Yukarıdaki bir *çöken test* örneğidir. Bu test "eğer `is_divisible_by_2_or_5(8)`'i çalıştırırsanız sonuç `True` olmalıdır" demektedir. Yazılmış olan `is_divisible_by_2_or_5` fonksiyonu herhangi bir şey döndürmediği için, test çöker ve doctest bize beklenenin `True` olduğunu ama bir şey dönmediğini bildirir.

Bu testi, fonksiyonu `True` döndürecek şekilde yazarak geçerli hale getirebiliriz:

```py
def is_divisible_by_2_or_5(n):
    """
 >>> is_divisible_by_2_or_5(8)
 True
 """
    return True


if __name__ == '__main__':
    import doctest
    doctest.testmod()
```

Şimdi çalıştırdığımız, herhangi bir çıktı olmayacaktır. Bunun anlamı tüm testlerin başarılı olduğudur. Tekrar etmek gerekir ki, doctest karakter dizileri hemen fonksiyon tanımlaması başlığından sonra yazılmalıdır.

Daha ayrıntılı çıktı görebilmek için betiği `-v` komut satırı seçeneğiyle çalıştırabilirsiniz:

```py
$ python myfunctions.py -v
Trying:
    is_divisible_by_2_or_5(8)
Expecting:
    True
ok
1 items had no tests:
    __main__
1 items passed all tests:
   1 tests in __main__.is_divisible_by_2_or_5
1 tests in 2 items.
1 passed and 0 failed.
Test passed.
$

```

Her ne kadar testimiz geçerli olsa da, bizim yazdığımız testler yetersizdir. Çünkü `is_divisible_2_or_5` herşey için `True` döndürmektedir. Aşağıda daha kapsamlı testler içeren ve bu testleri geçerli hale getiren tamamlanmış bir sürüm görebilirsiniz:

```py
def is_divisible_by_2_or_5(n):
    """
 >>> is_divisible_by_2_or_5(8)
 True
 >>> is_divisible_by_2_or_5(7)
 False
 >>> is_divisible_by_2_or_5(5)
 True
 >>> is_divisible_by_2_or_5(9)
 False
 """
    return n % 2 == 0 or n % 5 == 0 


if __name__ == '__main__':
    import doctest
    doctest.testmod()
```

Bu betiği `-v` komut satırı seçeneğiyle çalıştırın ve sonucu inceleyin.

## 5.9 Sözlük

ürün veren fonksiyon:
: Geri dönüş değeri üreten fonksiyondur.

geri dönüş değeri:
: Bir fonksiyon çağrısı sonucu olarak sağlanan değer.

geçici değişken:
: Karmaşık hesaplamalarda ara değerleri saklamak için kullanılan değişken.

ölü kod:
: Programların, genellikle `return` cümlesinden sonra geldiği için hiç bir zaman çalıştırılamaz olan parçaları.

`None`:
: Geri dönüş cümleleri içermeyen veya argümansız geri dönüş cümleleri içeren fonksiyonlar tarafından döndürülen özel Python değeri.
`None` `NoneType`'ın tek değeridir.

arttırımlı geliştirme:
: Hata ayıklamayı kolaylaştırmak ve mümkün olduğunca azaltmak için yapılan ve bir anda az kod ekleme ve bu ekleneni hemen sınama şeklinde gerçekleştirilen bir programlama geliştirme yöntemidir.

iskele:
: Program geliştirmede kullanılan ama son program sürümünün parçası olmayan kod.

boolean fonksiyon:
: Boolean değer döndüren fonksiyon.

kompozisyon (fonksiyonların):
: Bir fonksiyon gövdesinden başka bir fonksiyon çağırmak veya bir fonksiyonun geri dönüş değerini diğerinin çağrımına argüman olarak aktarmak.

birim sınama:
: Bağımsız kod parçalarını doğrulamak için kullanılan otomatik yordamlar. Python `doctest` modülünü bu amaç için barındırmaktadır.

## 5.10 Alıştırmalar

- İki değeri birbiriyle karşılaştıran ve `a > b` ise `1`, `a == b` ise `0` ve `a < b` ise `-1` değerlerini döndüren `compare` isminde bir fonksiyon yazınız.

```py
def compare(a, b):
    """
 >>> compare(5, 4)
 1
 >>> compare(7, 7)
 0
 >>> compare(2, 3)
 -1
 >>> compare(42, 1)
 1
 """
    # Fonksiyon govdesi burada baslamalidir
```

- Arttırımsal geliştirme yöntemini kullanarak iki kenarının uzunluğu verilen bir dik üçgenin hipotenüsünü bulan `hypotenuse` isimli bir fonksiyon yazın. İlerledikçe yaptığınız arttırımlı geliştirme sürecinin her aşamasını kaydedin.

```py
def hypotenuse(a, b):
    """
 >>> hypotenuse(3, 4)
 5.0
 >>> hypotenuse(12, 5)
 13.0
 >>> hypotenuse(7, 24)
 25.0
 >>> hypotenuse(9, 12)
 15.0
 """
```

- (x1,y1) ve (x2,y2) noktalarından geçen doğrunun eğimini hesaplayan `slope` fonksiyonunu yazın. Gerçekleştiriminizin aşağıdaki doctestleri geçerli yaptığını doğrulayın:

```py
def slope(x1, y1, x2, y2):
    """
 >>> slope(5, 3, 4, 2)
 1.0
 >>> slope(1, 2, 3, 2)
 0.0
 >>> slope(1, 2, 3, 3)
 0.5
 >>> slope(2, 4, 1, 2)
 2.0
 """

```

Daha sonra `slope` fonksiyonuna `intercept(x1,y1,x2,y2)` fonksiyonu içerisinde bir çağrı yaparak, doğrunun `(x1,y1)` ve `(x2,y2)` noktalarından geçen y-kesişimini bulun.

```py
def intercept(x1, y1, x2, y2):
    """
 >>> intercept(1, 6, 3, 12)
 3.0
 >>> intercept(6, 1, 1, 6)
 7.0
 >>> intercept(4, 6, 12, 8)
 5.0
 """

```

`intercept` fonksiyonu yukarıdaki doctestleri geçmelidir.

- İsmi `is_even(n)` olan ve tamsayı argüman alan bir fonksiyon yazın. Bu fonksiyon argüman **çift sayı** ise `True` ve **tek sayı** ise `False` döndürmelidir. Bu fonksiyona kendi doctestlerinizi de ekleyip doğrulamaları yapın.

- Şimdi de `is_odd(n)` isimli, `n` tek sayı ise `True`, çift sayı ise `False` değer döndüren fonksiyonu yazınız. Fonksiyonu yazma sürecinde doctestleri de ekleyin. Daha sonra fonksiyonu girilen argümanı değerlendirmek için kullanmak üzere `is_even` fonksiyonunu çağıracak şekilde değiştirin.

- Bölünebiliyor mu şeklinde bir fonksiyon yazın.

```py
def is_factor(f, n):
    """
 >>> is_factor(3, 12)
 True
 >>> is_factor(5, 12)
 False
 >>> is_factor(7, 14)
 True
 >>> is_factor(2, 14)
 True
 >>> is_factor(7, 15)
 False
 """
```

- fahrenheit, celcius dönüşümü

```py
def f2c(t):
    """
 >>> f2c(212)
 100
 >>> f2c(32)
 0
 >>> f2c(-40)
 -40
 >>> f2c(36)
 2
 >>> f2c(37)
 3
 >>> f2c(38)
 3
 >>> f2c(39)
 4
 """
```

`f2c` fonksiyon tanımlaması için bir gövde yazın. Fonksiyon Fahrenheit olarak verilmiş olan sıcaklığı en yakın Celcius tamsayı değerini döndürecek şekilde çalışmalıdır. (*ipucu:* Python tarafından sağlanan `round` fonksiyonunu kullanmak isteyebilirsiniz. Python kabuğunda `round.__doc__` yazarak ve iyice anlayana kadar `round` fonksiyonunu deneyerek denemeler yapabilirsiniz.)

- celcius, fahrenheit dönüşümü

```py
def c2f(t):
    """
 >>> c2f(0)
 32
 >>> c2f(100)
 212
 >>> c2f(-40)
 -40
 >>> c2f(12)
 54
 >>> c2f(18)
 64
 >>> c2f(-48)
 -54
 """

```

`c2f` fonksiyonu gövdesini Celcius'tan Fahrenheit'a çevirim yapacak şekilde doldurun.
