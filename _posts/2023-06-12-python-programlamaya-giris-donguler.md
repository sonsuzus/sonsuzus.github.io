---
title:  Python Programlamaya Giriş 4 – Döngüler
author: sonsuz
date: 2023-06-12 01:41:25 +0300
categories: [Program,Python]
tags: [python,programlama,döngü,while,for]
---

Döngüler, daha önce bahsettiğimiz karar yapısı `if` ile benzer bir yapıya sahiptir. Blok kaydırma yapısı ve mantıksal şartlara aşina değilseniz önce [python mantık işlemleri ve karşılaştırmaları](https://sonsuzus.github.io/posts/python-programlamaya-giris-secim-yapma-mantik-islemleri-karsilastirmalar/) okumanız iyi olur.

# while döngüsü

`while` döngüleri, bir mantıksal şart mantıksal “doğru” değerine sahip olduğu sürece tekrarlanır. Döngünün sona ermesi için şartın eninde sonunda yanlış hale gelmesi gerekir. Bunun için döngünün içinde değişkenler uygun şekilde güncellenir. Bu güncellemeyi unutursak sonsuz döngü içine düşeriz ve programımız biz zorla kapatmadıkça durmaz.

Basit bir örnekle başlayalım: 10’a kadar olan sayıları sırayla ekrana yazan bir program yazalım.

In [1]:

```python
a=1

b=10

while a<b:

    print(a, end=" ")

    a += 1  # a = a + 1 ile aynı


```

```
1 2 3 4 5 6 7 8 9
```

Gördüğünüz gibi `while` komutunun yapısı `if`‘e benziyor: İkisi de bir şarttan sonra iki nokta üstüste (`:`) ile bir blok başlatıyor, ve blok içeri doğru kaydırılıyor.

Yukarıdaki örnekte önce `a` ve `b` değişkenlerine ilk değerler veriyoruz. Ardından `while` blokunun başında `a<b` şartının doğru olup olmadığı yoklanıyor. Doğruysa blokun içindeki kod çalıştırılır. `if` yapısındaki gibi, döngü bloku kaydırma ile belli edilir. Blok bitince başa dönülür, şartın hâlâ doğru olup olmadığı tekrar yoklanır, doğruysa blok tekrar çalıştırılır. Döngü bloku üzerinden her bir geçişe bir *iterasyon* deriz.

`print` fonksiyonuna verdiğimiz `end=" "` parametresi, `a` değeri ekrana basıldıktan sonra satırbaşı yapmak yerine aynı satırda bir boşluk bırakmasını sağlar. Böylece sayıları tek bir satıra yazabiliriz.

Döngü blokundaki `a += 1` ifadesi, `a` değişkeninin değerini bir artırmak için kullanılan kısa bir yazım tarzı. Diğer aritmetik işlemlerde de aynı kestirme yol geçerli (meselâ `a -= 2` iki azaltır, `a *= 3` üçle çarpar). Bu işlem döngü içinde tekrarlanınca sonunda `a` değişkeni 10 değerine ulaşıyor, `a<b` şartı yanlış hale geliyor, ve döngü bir daha çalıştırılmıyor. Döngü bittiğinde `a`‘nın 10 değerine sahip olduğuna, ama ekranda 10 sayısının yazılmadığına dikkat edin.

Döngü içinde `a += 1` ifadesi olmasaydı, `a` hep aynı değerde kalacağı için döngü sonsuza kadar devam ederdi. Yeni başlayanlar bu hataya çok düşer (ben de sık sık yaparım). Sonsuz döngüyü kırmak için programı zorla durdurmanız gerekir. Jupyter defterinde *Interrupt Kernel* düğmesine tıklayarak, Linux komut satırında Ctrl-C basarak, Windows komut satırında Ctrl-Z basarak programı durmaya zorlayabilirsiniz.

---

**Alıştırma.** Yukarıdaki programı değiştirerek (a) 4’den 29’a beşer beşer, (b) 10’dan 1’e geriye doğru birer birer saydırın.

---

Başka bir örnek olarak, 1’den 10’a kadar sayıların toplamını hesaplayan bir program yazalım.

In [2]:

```python
a=1

b=10

toplam=0

while a<=b:

    toplam += a

    a += 1

print(toplam)


```

```
55


```

Bu programda `toplam` isimli bir değişken yaratıyoruz ve döngünün içinde her `a` değerini `toplam`‘a ekliyoruz. Bu döngünün çalışmasını aşağıdaki tabloda adım adım görebiliriz.

| iterasyon | a | a <= b | toplam |
| --- | --- | --- | --- |
| 1 | 1 | Doğru | 1 |
| 2 | 2 | Doğru | 3 |
| 3 | 3 | Doğru | 6 |
| 4 | 4 | Doğru | 10 |
| … | … | … | … |
| 10 | 10 | Doğru | 55 |
| 11 | 11 | Yanlış | 55 |

Bu programda `print()` komutunun döngünün dışında olduğuna dikkat edin (kaydırma seviyesi `while` kelimesiyle aynı hizada). Bu komut döngü blokunun içinde olsaydı ne olurdu? Deneyin.

Döngü tekrarlama şartında küçükeşit kullandık (`a<=b`). Önceki örnek programda olduğu gibi küçük (`a<b`) kullansaydık ne olurdu? Deneyin.

---

**Alıştırma.** Yukarıdaki programı değiştirerek şu toplamları hesaplatın.

1. $1 + 3 + 5 + \cdots + 101$
2. $\frac{1}{2} + \frac{1}{4}+ \cdots + \frac{1}{2^a} + \cdots + \frac{1}{1024}$
3. $1 + 4 + 9 + \cdots + a^2 + \cdots + 100$

---

## İç içe döngüler

Bir döngü blokunun içine istediğiniz her türlü kodu koyabilirsiniz. Başka bir döngü koymak da buna dahil. Sözgelişi, iki ayrı parametre üzerinden döngü yapmak istediğinizde bir döngü içinde başka bir döngü kullanırsınız.

Örnek olarak, $1^p + 2^p + \cdots + 10^p$ toplamını, $p$’nin 1-6 arasındaki değerleri için ekrana yazacak bir program yazalım. Yukarıda böyle bir seri toplamın bir döngü içinde nasıl hesaplandığını gördük. Her bir $p$ için ayrıca bir hesap yapacağız. Demek ki toplamı hesaplama döngüsünü, $p$’nin 1 ile 6 arasında değiştiği bir döngünün içine koymalıyız.

İçiçe döngüler yazmanın en kolay yolu, dış döngüdeki parametreleri sabit tutup en içteki döngüyle başlamaktır. İlk aşamada $1^p + 2^p + \cdots + 10^p$ toplamını sadece $p=1$ için hesaplayalım.

In [3]:

```python
p=1

a=1

b=10

toplam=0

while a<=b:

    toplam += a\*\*p

    a += 1

print("p =",p,", 1^p + ... + 10^p =", toplam)


```

```
p = 1 , 1^p + ... + 10^p = 55


```

Şimdi yapmamız gereken bunu $p=2,3,4,5,6$ için tekrarlamak. Tembel işi yapıp, aynı kodu altı kere yapıştırıp $p$ değerlerini değiştirebiliriz.

In [4]:

```python
p=1

a=1

b=10

toplam=0

while a<=b:

    toplam += a\*\*p

    a += 1

print("p =",p,", 1^p + ... + 10^p =", toplam)



p=2

a=1

b=10

toplam=0

while a<=b:

    toplam += a\*\*p

    a += 1

print("p =",p,", 1^p + ... + 10^p =", toplam)



p=3

a=1

b=10

toplam=0

while a<=b:

    toplam += a\*\*p

    a += 1

print("p =",p,", 1^p + ... + 10^p =", toplam)



p=4

a=1

b=10

toplam=0

while a<=b:

    toplam += a\*\*p

    a += 1

print("p =",p,", 1^p + ... + 10^p =", toplam)



p=5

a=1

b=10

toplam=0

while a<=b:

    toplam += a\*\*p

    a += 1

print("p =",p,", 1^p + ... + 10^p =", toplam)



p=6

a=1

b=10

toplam=0

while a<=b:

    toplam += a\*\*p

    a += 1

print("p =",p,", 1^p + ... + 10^p =", toplam)


```

```python
p = 1 , 1^p + ... + 10^p = 55

p = 2 , 1^p + ... + 10^p = 385

p = 3 , 1^p + ... + 10^p = 3025

p = 4 , 1^p + ... + 10^p = 25333

p = 5 , 1^p + ... + 10^p = 220825

p = 6 , 1^p + ... + 10^p = 1978405


```

İstediğimizi yapıyor, ama güzel bir çözüm yöntemi değil. Birincisi, programımız gereksiz derecede uzuyor ve okuması zorlaşıyor. İkincisi, $p$ için farklı değerlerle hesabı tekrarlamak istediğimizde hepsini elden geçirmemiz, silmemiz veya eklememiz gerekiyor. Aynı hesabı $p$’yi -100 ile 100 arasında tekrarladığınızı düşünün!

Muhtemelen bu aşamada en güzel çözümün kodun etrafına bir dış döngü sarmak olduğunu gördünüz bile.

In [5]:

```python
p=1

while p<=6:

    a=1

    b=10

    toplam=0

    while a<=b:

        toplam += a\*\*p

        a += 1

    print("p =",p,", 1^p + ... + 10^p =", toplam)

    p += 1


```

```python
p = 1 , 1^p + ... + 10^p = 55

p = 2 , 1^p + ... + 10^p = 385

p = 3 , 1^p + ... + 10^p = 3025

p = 4 , 1^p + ... + 10^p = 25333

p = 5 , 1^p + ... + 10^p = 220825

p = 6 , 1^p + ... + 10^p = 1978405


```

# break: Döngüyü bitirmek

Bir döngünün, döngü şartı yanlış hale geldiğinde sona erdiğini gördük. Ancak bazı durumlarda döngü bloku içinde bir çıkış sağlamak daha kolay olabilir, ve bazen kodun daha okunaklı olmasını sağlar.

Bir döngü bloku içinde verilen bir `break` komutu, döngünün hemen o anda bitirilmesine yol açar. Program akışı döngü blokunun dışına atlar, ve ardından gelen komutlarla devam eder. Örnek olarak, kullanıcının verdiği sayıları toplayan bir program yazalım. Kullanıcı -99 girene kadar sayıları toplama eklemeye devam etsin.

In [6]:

```python
toplam = 0

while True:   # Şart hep doğru - sonsuz döngü

    x = int(input("Bir sayı girin (bitirmek için -99): "))

    if x == -99:

        break

    toplam += x

print("Toplam:", toplam)


```

```python
Bir sayı girin (bitirmek için -99): 5

Bir sayı girin (bitirmek için -99): -7

Bir sayı girin (bitirmek için -99): -99

Toplam: -2


```

`break` sadece döngüler içinde ve bir `if` şartı altında bir mânâ ifade eder. Eğer `if` kullanmazsanız Python yorumlayıcısı döngünün ilk iterasyonunda `break`‘e rastlayarak döngüyü tamamlar, blokun geri kalanını hiç işlemez.

Yukarıdaki programda döngünün tekrarlama şartı `True` olduğu için, bu bir sonsuz döngü. Döngünün bitmesi için kullanıcının -99 yazması gerek. Hiç `break` kullanmamak teorik olarak mümkündür, ama bazı karmaşık durumlarda `break` sayesinde programınız sadeleşir, okunması kolaylaşır.

---

**Alıştırma.** Yukarıdaki programı `break` kullanmadan yazın.

---

# continue: Döngünün kalanını atlamak

`continue` komutu da, aynı `break` gibi, sadece bir döngü içinde ve bir `if` şartı altında mânâ ifade eder. `continue` döngü blokunun işlemesini yarıda keser ve başa döner. `break`‘den farkı, programın döngünün dışına çıkmaması, ama döngünün başına dönmesi ve tekrar başlatmasıdır. Bu arada döngü şartının doğru olup olmadığı da kontrol edilir.

Örnek olarak, yukarıdaki programı, sadece 0 ve 100 arası değerleri kabul edecek şekilde şöyle yazabiliriz:

In [7]:

```python
toplam = 0

while True:

    x = int(input("Bir sayı girin (bitirmek için -99): "))

    if x == -99:

        break

    if x < 0 or x > 100:

        print("0-100 arası olmalı.")

        continue

    toplam += x

print("Toplam:", toplam)


```

```python
Bir sayı girin (bitirmek için -99): 78

Bir sayı girin (bitirmek için -99): 103

0-100 arası olmalı.

Bir sayı girin (bitirmek için -99): -5

0-100 arası olmalı.

Bir sayı girin (bitirmek için -99): 11

Bir sayı girin (bitirmek için -99): -99

Toplam: 89


```

Programda 0-100 aralığı dışındaki girdiler `continue`‘ya takılıyor, o yüzden toplama eklenmiyorlar. Programı -99’la bitirmek hâlâ mümkün çünkü bunun yoklaması daha önce yapılıyor. İki `if` blokunun sırasını değiştirirseniz bu özellik bozulur, program sonsuz döngüde kalır.

# else

Python dilinde `while` ve `for` döngülerinde bir `else` bloku bulunabilmesi mümkündür. Bu özellik, C’de ve birçok başka dilde bulunmaz.

Bir while döngüsünün Python sözdizimindeki genel yapısı şöyledir:

```python
while <şart>:

    <komutlar 1>

else:

    <komutlar 2>


```

`else` bloku altındaki <`komutlar 2>` kısmı sadece döngü şartı yanlışsa çalıştırılır. Kendi başına bu o kadar da gerekli değil; `<komutlar 2>` kısmını `else` kelimesi olmadan döngü blokunun dışına koysanız da aynı etkiyi yapar. `else`‘i işe yarar kılan şey şu: `<komutlar 1>` kısmında bir `break` komutu çalıştırılırsa, döngünün `else` kısmını da atlar. Yani, döngünüz `break` ile bitmediği zaman çalışamasını istediğiniz komutları `else` altına koyarsınız.

Somut bir örnek olarak, bir sıralı veri yapısı içinde bir arama yaptığımızı düşünelim. Veride belli bir değere sahip bir eleman olup olmadığını bulmaya çalışıyoruz. Bunun klasik yolu “bayrak” (flag) adı verilen Boolean (doğru/yanlış) değişkenler kullanmaktır. Başlangıçta bayrak değeri “yanlış”tır. Veriyi eleman eleman tarar, aradığımız değeri bulursak bayrağı “doğru” değere getirir ve döngüden çıkarız. Döngü bittiğinde bayrağın durumu bize sonucu verir.

In [8]:

```python
data = [1,2,4,-1,3,4,-5,1]

i = 0

aranan = 3



bulduk = False

while i<len(data) and not bulduk:

    if data[i] == aranan:

        bulduk = True

    else:

        i += 1



if bulduk:

    print("Aranan", aranan, "değeri", i, "pozisyonunda.")

else:

    print("Bulamadık")


```

```
Aranan 3 değeri 4 pozisyonunda.


```

`while` ile birlikte `else` kullanmak bu programı biraz sadeleştirir.

In [9]:

```python
data = [1,2,4,-1,3,4,-5,1]

i = 0

aranan = int(input("Aranan değer: "))



while i<len(data):

    if data[i] == aranan:

        print ("Aranan", aranan, "değeri", i, "pozisyonunda.")

        break;

    i += 1

else:

    print("Bulamadık")


```

```
Aranan değer: 5

Bulamadık


```

İkinci programdaki `else`‘in `if`‘e değil `while`‘a ait olduğuna dikkat edin. Burada bayrak değişkeni `bulduk`‘a ihtiyaç kalmıyor.

Başka bir örnek olarak, verilen bir sayının asal olup olmadığını belirleyelim. Bunun için, verilen sayının daha küçük sayılara bölünebilir olup olmadığına bakacağız. Verilen sayıyı bölen daha küçük bir sayı bulursak, gerisine bakmadan sayının asal olduğunu söyleyebiliriz. Sayı asalsa, bütün muhtemel bölenlere bakmamız gerekecek.

Bir $x$ sayısının asal olup olmadığını anlamak için $x$’den küçük bütün sayılara bakmaya lüzum yok; 2 ile $\sqrt{x}$ arasındaki sayıları test etmek yeterli.

Döngü `else`‘ini kullanmadan şöyle yapabiliriz:

In [10]:

```python
x = int(input("Bir pozitif tamsayı girin: "))

asal = True

i = 2

while i\*i <= x and asal:

    if x % i==0:

        asal = False

    else:

        i += 1



if asal:

    print("Asal.")

else:

    print("Asal değil,", i, "böler.")


```

```
Bir pozitif tamsayı girin: 87236849

Asal değil, 7 böler.


```

(Karekök alma işlemi CPU’yu fazla kullandığı için, döngü şartını $i \leq \sqrt{x}$ yerine $i^2 \leq x$ olarak yazdım.)

Aynı programı döngü `else`‘ini kullanarak şöyle yazabiliriz:

In [11]:

```python
x = int(input("Bir pozitif tamsayı girin: "))

i = 2

while i\*i <= x:

    if x % i == 0:

        print("Asal değil,", i, "böler.")

        break

    i += 1

else:

    print("Asal.")


```

```python
Bir pozitif tamsayı girin: 98731

Asal.


```

# for: Sıralı nesneler üzerinde döngü

C, Java ve benzeri dillere aşinaysanız, `for` ve `while` döngülerinin tamamen denk olduğunu bilirsiniz. Python’da `for` başka bir görev üstlenmiştir: Liste, dize, çokuz gibi sıralı bir nesnedeki elemanları sırayla tek tek alır ve döngü blokunda işler.

In [12]:

```python
for s in ["fındık", "fıstık", "ceviz"]:

    print(s)


```

```
fındık

fıstık

ceviz


```

Aynısını bir `while` döngüsünde şöyle yaparız:

In [13]:

```
L = ["fındık","fıstık","ceviz"]

i=0

while i < len(L):

    print(L[i])

    i += 1


```

```
fındık

fıstık

ceviz


```

Burada `len(L)` bize `L` listesinin eleman sayısı olan 3’ü verir. `while` kullandığımızda listenin indeksini takip eden bir `i` değişkeni kullanmamız gerekiyor. `for` ile buna gerek yok, ve döngü bloku çok daha sade.

`range(n)` fonksiyon çağrısı sıfırdan başlayarak `n-1`‘e kadar tamsayılar verir.

In [14]:

```
list(range(11))


```

Out[14]:

```
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

Bunu kullanarak 0-10 arasındaki sayıları ve karelerini ekrana yazalım.

In [15]:

```python
for x in range(11):

    print(x, x\*\*2)


```

```
0 0

1 1

2 4

3 9

4 16

5 25

6 36

7 49

8 64

9 81

10 100


```

`for` döngüsü, bir dizeyi de bir liste gibi eleman eleman alabilir. Dizenin elemanları onu oluşturan karakterlerdir.

In [16]:

```python
for c in "Merhaba":

    print(c,end=",")


```

```
M,e,r,h,a,b,a,
```

Bir çokuzdaki elemanların toplamını bulalım.

In [17]:

```python
toplam=0

for x in (4, 5, 2, -4, 1, 10):

    toplam += x

print(toplam)


```

```
18


```

Elimizde sayı çiftlerinden oluşan bir liste olsun ve bu çiftlerin toplamlarının listesini elde etmek istiyoruz diyelim.

In [18]:

```python
L = [(1,2), (2,4), (3,8)]

for e in L:  # her e'nin iki elemanı vardır

    print (e[0], e[1], e[0]+e[1])


```

```
1 2 3

2 4 6

3 8 11


```

Aynısını çokuz atamalarından faydalanarak yazmak kodu sadeleştirir.

In [19]:

```
L = [(1,2), (2,4), (3,8)]

for a,b in L:

    print (a,b,a+b)


```

```
1 2 3

2 4 6

3 8 11


```

---

**Alıştırma.** Yukarıdaki örnekleri `while` döngüsü kullanarak yazın.

---

`break`, `continue`, `else` komutları `for` döngülerinde de, yukarıda `while` için bahsedilen şekilde çalışırlar. Bu komutların `for` ile kullanılışına ayrıca örnek vermeyeceğiz.
