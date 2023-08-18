---
title: Python Fonksiyonlar
author: sonsuz
date: 2023-08-18 19:14:37 +0300
categories: [Program,Python]
tags: [python,programlama,fonksiyon]
---




Python'da, fonksiyon bir veya daha fazla işlem satırından oluşan kodların bir kod bloğu şeklinde yapılandırılması ile oluşturulur. Fonksiyonlar oluşturulduktan sonra programın herhangi bir yerinden sadece fonksiyon adı kullanılarak çağrılabilir. Bu sayede, çok fazla sayıda işlem satırı tek bir isim kullanılarak çalıştırılmış olur.

Bir fonksiyon tanımlarken isteğe bağlı olarak fonksiyona parametre değerleri geçirebilir veya fonksiyon tarafından bir değer geri döndürülmesini sağlayabiliriz.

## Fonksiyon bildirimi

Python'da bir fonksiyon kullanılmadan önce mutlaka bildirimi yapılmalıdır. Fonksiyonların bildirimi def anahtar kelimesi ile aşağıda gösterilen yapı kullanılarak yapılır:

```

def fonksiyon-adı(param1=ön-tanımlı-değer1, param2=ön-tanımlı-değer2, ...)
{
  işlem satırı
  .
  .
  işlem satırı
 
  return ifade;
}

```

Fonksiyon yapısında 5 temel eleman vardır. Bu elemanlardan def nahtar kelimesi, fonksiyon-adı ve işlem satırı mutlaka bulunmalıdır. Ancak, parametreler ve return ifadelerinin tanımlanması programcının ihtiyaçları doğrultusunda isteğe bağlıdır. Parametre yerine argüman ifadesi de kullanılmaktadır.

Fonksiyon bildiriminde parametreler için ön tanımlı bir değer verildiğinde, fonksiyon parametresiz olarak çağrılsa bile, fonksiyon ön tanımlı değer atanmış parametre ile çağrılmış gibi işlem görür.

def 
: Fonksiyon bildiriminde kullanılan anahtar kelime

fonksiyon-adı 
: Fonksiyon adını gösterir.

parametreler 
: Fonksiyona geçirilen ve isteğe bağlı olarak tanımlanan verileri gösterir.

İşlem satırı 
: Fonksiyon içindeki işlem satırlarını gösterir.

return 
: Verileri geri döndürmeye yarar. Son satırda kullanılması şart değildir.

ifade 
: Değişken, sabit ve işlemciler kullanılarak oluşturulan veridir.

Fonksiyon, kendisine geçirilen parametrelerin değerlerini, işlem durumuna bağlı olarak, değiştirerek veya değiştirmeden kullanabilir.

Fonksiyon, eğer varsa, kendisine geçirilen parametreleri de kullanarak kod bloğu içindeki işlem satırları ile bir takım işlemler yaparak bir sonuç elde eder. Elde edilen sonuç, ihtiyaca bağlı olarak, fonksiyon içinde ya da return komutu ile geri döndürüldükten sonra program içinde kullanılır.

## Fonksiyon kullanımı

Python'da bir fonksiyonun bildirimi yapıldıktan sonra, aşağıda gösterildiği şekilde fonksiyon adını kullanarak fonksiyonu çağırabiliriz:

```

fonksiyon-adı(parametreler)

```

Parametre yoksa parantezlerin arası boş bırakılır.

Şimdi, fonksiyonların kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
def liste_yazdir():
    liste = ["aaa", "bbb", "ccc", "ddd"]

    for deg in liste:
        print(deg, end=' ')

print('liste_yazdir() fonksiyonunu çağırma!')		
liste_yazdir()
print('liste_yazdir() fonksiyon işlemleri sona erdi!')		


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

liste_yazdir() fonksiyonunu çağırma!
aaa bbb ccc ddd 
liste_yazdir() fonksiyon işlemleri sona erdi!

```

Program, liste adı bir liste tanımlayarak, bu listenin elemanlarını ekrana yazan liste\_yazdir() adlı bir fonksiyon bildirimi yapar. Fonksiyonu çağrısından önce ve sonra ekrana birer karakter dizisi yazar.

## Fonksiyonların parametre ile kullanımı

Bir fonksiyona bir veya daha fazla parametre geçirerek çağırabiliriz:

Şimdi, fonksiyonların tek bir parametre ile kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
liste = ["aaa", "bbb", "ccc", "ddd"]

def liste_yazdir(list_par):
    for deg in list_par:
        print(deg, end=' ')

liste_yazdir(liste)


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

aaa bbb ccc ddd 

```

Program, liste adı bir liste tanımlar. Kendisine parametre olarak geçirilen bir listenin elemanlarını ekrana yazan liste\_yazdir() adlı bir fonksiyon bildirimi yapar. Listeyi parametre olarak geçirerek fonksiyonu çağırır ve liste elemanlarını ekrana yazar.

Şimdi, fonksiyonların iki parametre ile kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
def topla(deg1, deg2):
    return deg1 + deg2

# Fonksiyonun geri verdiği sonucu ekrana yazma
print('Sabit değerlerin toplamı: ', topla(7, 21))


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Sabit değerlerin toplamı: 28

```

Program, kendisine parametre olarak geçirilen iki değerin toplamını geri döndüren topla() adlı bir fonksiyon bildirimi yapar. Fonksiyon, 7 ve 21 değerlerinin toplamını geri döndürür.

## Fonksiyonların ön tanımlı parametre ile kullanımı

Bir fonksiyon bildiriminde bir parametre için ön tanımlı parametre kullanıldığında, fonksiyon çağrılırken o parametre için herhangi bir değer geçirilmezse, ön tanımlı değer parametreye atanır.

Şimdi, fonksiyonların ön tanımlı parametreler ile kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
def kare_al(deg=5):
    return deg*deg

print(kare_al(7))
print(kare_al(21))
print(kare_al()) # Ön tanımlı değer olan 5 değeri kullanılır.


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

49
441
25

```

Program, kendisine parametre olarak geçirilen bir değerin karesini geri döndüren ve parametresi ön tanımlı olarak 5 değerini alan kare\_al() adlı bir fonksiyon bildirimi yapar. Fonksiyon, önce 7 ve 21 değerleri ile sonra parametre değeri verilmeden çağrılır. Parametresiz olarak çağrıldığında, fonksiyon içinde ön tanımlı değer olan 5 değeri kullanılır.

## Fonksiyonlarda sayısı belirsiz parametre tanımlama

Bir fonksiyona kaç adet parametre geçirileceğini bilmediğimizde, fonksiyon bildiriminde parametre adından önce \* karakteri kullanabiliriz.

Şimdi, fonksiyonların belirsiz sayıda parametre ile kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
def topla(*deg_par):
    deg_top=0 
    for deg in deg_par:
        deg_top += deg 
    return deg_top	

print(topla(5, 43))
print(topla(9, 17, 26))
print(topla(7, 15, 21, 35))


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

48
52
78

```

Program, kendisine parametre olarak geçirilen bir veya daha fazla değerin toplamını geri döndüren topla() adlı bir fonksiyon bildirimi yapar. Fonksiyonu, sırasıyla iki, üç ve dört parametre ile çağırarak geri döndürülen sonuçları ekrana yazar.

## Lambda fonksiyonları

Python'da, basit sonuçlar elde edeceğimiz normal fonksiyonlar kullanmak yerine, Lambda adı verilen küçük ve isimsiz fonksiyonlar kullanabiliriz. Lambda fonksiyonları tek bir ifadeden oluşur ve bir veya birden fazla parametre alabilir.

Lambda fonksiyonlarının bildirimi aşağıda gösterildiği şekilde yapılır:

```

lambda-fonksiyon-çağrı-adı = lambda param1, param2, ... : ifade

```

Şimdi, lambda fonksiyonlarının kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
# Tek parametreli lambda fonksiyonu 
lambda1 = lambda deg : deg*deg
print(lambda1(21)) 

# İki parametreli lambda fonksiyonu
lambda2 = lambda deg1, deg2 : deg1*deg2
print(lambda2(7, 15)) 


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

441
105

```

Program, biri tek diğeri iki parametreli olmak üzere iki adet lambda fonksiyon bildirimi yapar. İlk fonksiyon parametre olarak geçirilen değerin karesini, ikinci fonksiyon ise parametre olarak geçirilen değerlerin çarpımını geri döndürür. Her iki dönüş değerini ekrana yazar.
