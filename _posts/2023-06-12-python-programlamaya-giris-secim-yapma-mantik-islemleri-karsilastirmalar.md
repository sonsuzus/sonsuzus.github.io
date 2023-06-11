---
title:  Python Programlamaya Giriş 3 – Seçim Yapma, Mantık işlemleri, Karşılaştırmalar
author: sonsuz
date: 2023-06-12 00:51:10 +0300
categories: [Program,Python]
tags: [python,karşılaştırma,if,else]
---



En basit programlarda bile sık sık “şu şart doğruysa şöyle yap, yoksa yapma”, veya “doğruysa şöyle yap, yanlışsa öbür türlü yap” şeklinde düzenlemelere ihtiyaç duyarız. Sözgelişi, “cevap doğruysa puanı bir arttır”, veya “yanlış sayısı dördün katıysa puanı bir azalt” gibi. Birçok dil gibi Python’da da seçim yapısı `if-else` komutlarıyla kurulur.

# if komutu

Karar yapılarının en basit hali, bir şartın doğruluğunu yoklamak ve doğruysa belli işlemler yapmaktır. Sözgelişi aşağıdaki programa bakalım. Hücreyi Shift-Enter ile çalıştırdığımızda tahminimizi soran bir kutu ortaya çıkacak. Kutuya bir cevap yazıp Enter’e basın.

In [2]:

```python
hedef = "42"

tahmin = input("Tahmininiz: ")

if tahmin == hedef:

    print("Doğru!")


```

```
Tahmininiz: 42

Doğru!


```

Sayı `hedef` değerine (`"42"`) eşitse ekrana `"Doğru!"` yazısını basacak, değilse birşey yapmayacak. Şarttan sonra iki nokta üstüste (`:`) koymayı da unutmayın.

(Bu hücredeki kodu kendi başına çalışan bir betik haline getirmek için, kodu kopyalayıp bir metin editörüne yapıştırın ve tahmin.py isimli bir dosya olarak kaydedin. Böylece komut satırında çalıştırabilirsiniz:

```python
$ python3 tahmin.py

Tahmininiz: 42

Doğru!


```

şeklinde bir çıktınız olmalı)

`if`‘den sonra `tahmin`‘in `hedef`‘e eşit olup olmadığını yoklayan bir mantık ifadesi var. Bunun değeri ya doğru (`True`) ya da yanlış (`False`) olacak. Eşitlik şartı için `==` (iki tane eşit işareti) kullanıldığına dikkat edin.

In [1]:

```
1 == 1


```

Out[1]:

```
True
```

In [2]:

```
1 == 2


```

Out[2]:

```
False
```

In [3]:

```
1 = 1


```

```
 File "<ipython-input-3-4c0a01f26144>", line 1

 1 = 1

         ^

SyntaxError: can't assign to literal


```

Şarttan sonraki satırlara, şart doğruysa çalıştırılacak kod parçası (*if bloku*) gelir. Burada Python’un kendine özgü bir kuralını görüyoruz: Bloktaki her ifade, `if` başlığına göre belli bir miktar sağa kaydırılmalıdır. Yorumlayıcı hangi komutların `if` blokuna ait olduğunu bu kaydırma sayesinde ayırt eder.

Meselâ şu iki ayrı programa bakalım:

```python
hedef = "42"

tahmin = input("Tahmininiz: ")

if tahmin == hedef:

    print("Doğru!")

    print("Bravo")


```

ve:

```python
hedef = "42"

tahmin = input("Tahmininiz: ")

if tahmin == hedef:

    print("Doğru!")

print("Bravo")




```

İkinci programdaki

```
print "Bravo"


```

komutu `if` blokunun dışında olduğu için, tahmin doğru olsa da olmasa da çalıştırılır. Deneyin.

`if` içindeki blokun kaç boşluk sağa kaydırılacağı önemli değildir; bir tek boşluk bile yeterlidir. Çoğu IDE otomatik olarak dört boşluk genişlikte bir sıçrama yapar; Python programcılık camiasında tavsiye edilen de budur. Sonraki satırlar da aynı kaydırma seviyesinde başlar. Bu yüzden, bloku bitirmek için yeni satıra geçtikten sonra geriye silme (Backspace) tuşuna basmalısınız.

# if-else komutu

Yukarıdaki program bize sadece tahminimiz doğruysa bir cevap veriyor. Tahminimizin yanlış olduğunu da söylemesini istersek `if-else` yapısını kullanırız.

In [4]:

```python
hedef = "42"

x = input("Tahmininiz: ")

if x == hedef:

    print("Doğru!")

else:

    print("Yanlış")


```

```
Tahmininiz: 43

Yanlış


```

`else` ifadesinden sonra herhangi bir şart gelmez, çünkü `else` bloku zaten sadece `if` şartı yanlışsa çalıştırılır. `else` kelimesinin, bağlı olduğu `if` ile aynı kaydırma seviyesinde olduğuna dikkat edin.

Her `else` bir `if`‘e bağlı olmalıdır, ama tersi doğru değildir. Her `if`‘e bir `else` gerekmez.

# if-elif-else komutu

`if` kullanımının en genel hali budur. `elif` kelimesi `else if`‘in kısaltmasıdır.

In [5]:

```python
x = int(input("Kaç tane? "))

if x>2000:

    print("Binlerce")

elif x>200:

    print("Yüzlerce")

elif x>10:

    print("Çok")

elif x>0:

    print("Birkaç")

else:

    print("Yok")


```

```
Kaç tane? 87

Çok


```

Aynı programı `elif` kullanmadan ancak şöyle yazabiliriz:

In [ ]:

```python
x = int(input("Kaç tane? "))

if x>2000:

    print("Binlerce")

else:

    if x>200:

        print("Yüzlerce")

    else:

        if x>10:

            print("Çok")

        else:

            if x>0:

                print("Birkaç")

            else:

                print("Yok")


```

Görüldüğü gibi `elif` kullanmak programı sadeleştiriyor.

# Karşılaştırmalar

`if`‘den sonra, mantıksal olarak doğru veya yanlış sayılacak ifadeler gelmelidir. Eşitlikten yukarıda bahsettik. Ayrıca `>` (büyük), `<` (küçük), `>=` (büyük veya eşit), `<=` (küçük veya eşit) ve `!=` (eşit değil) işlemleri kullanılabilir.

In [6]:

```
2 > 3, 2 >= 3, 2 < 3, 2 <= 3, 2 != 3


```

Out[6]:

```
(False, False, True, True, True)
```

Sayı olmayan veri yapıları da karşılaştırmalarda kullanılabilirler. O durumda, eşitsizliklerin değerlendirilmesinde alfabetik sıra kullanılır.

In [7]:

```
"hello" == "Hello", "hello" > "Hello", "hello" < "jello"


```

Out[7]:

```
(False, True, True)
```

In [8]:

```
[1,2,3] < [1,20,3], [1,2,3] < [11,2,3]


```

Out[8]:

```
(True, True)
```

Bir veri yapısı içinde belli bir eleman veya alt grubun bulunup bulunmadığını `in` kelimesiyle test edebilirsiniz. Şartı ters çevirmek için `not in` kullanılır.

In [9]:

```
L = [12,3,4,[5,6]]

3 in L, [3,4] in L, [5,6] in L, [5,6] not in L


```

Out[9]:

```
(True, False, True, False)
```

In [10]:

```
s = "merhaba"

"a" in s, "erh" in s


```

Out[10]:

```
(True, True)
```

Sözlüklerde `in` kelimesi sadece referanslar içinde yoklama yapar.

In [11]:

```python
d = {"abc": 54, (1,2): -45.1}

"abc" in d, 54 in d, (1,2) in d


```

Out[11]:

```
(True, False, True)
```

# Doğru ve yanlış sabitleri

`True` ve `False`, aslında 1 ve 0 sayılarına verilen yeni isimlerdir. Ayrıca,

```
[], {}, "", None, 0, 0.0, False


```

ifadelerinin her biri mantıksal yanlış anlamı taşır. Tersine olarak da, sıfırdan farklı her sayı veya boş olmayan herhangi bir liste/çokuz/dize/sözlük `if` yapılarında mantıksal doğru olarak yorumlanırlar.

In [12]:

```python
L=[]

if L:

    print("Liste dolu")

else:

    print("Liste boş.")


```

```
Liste boş.


```

In [13]:

```python
s = "abc"

if s:

    print(s)

else:

    print("Boş")


```

```
abc


```

# Mantıksal işlemler

Birden fazla şartı Boole işlemleri (`and`, `or`, `not`) ile biraraya getirerek, daha karmaşık şartlar oluşturmak mümkün olur.

* `X and Y` : Hem `X` hem `Y` doğruysa doğru; `X` ve `Y`‘den en az biri yanlışsa yanlış.
* `X or Y` : `X` ve `Y`‘den en az biri doğruysa doğru; hem `X` hem `Y` yanlışsa yanlış.
* `not X` : `X`‘in doğruluk değerinin tersi.

In [14]:

```
1 < 2 and 3==3


```

Out[14]:

```
True
```

In [15]:

```
1 < 2 and 3==4


```

Out[15]:

```
False
```

In [16]:

```
1 < 2 or 3==4


```

Out[16]:

```
True
```

In [17]:

```
1 > 2 or 3==4


```

Out[17]:

```
False
```

In [18]:

```
not 1>2


```

Out[18]:

```
True
```

In [19]:

```
not 3==3


```

Out[19]:

```
False
```

Boole ifadelerinde ikiden fazla bileşen de kullanılabilir. Önce `not` işlemi, sonra `and` işlemi, sonra da `or` işlemi yapılır. Aynı işlem yapılıyorsa, bileşenler soldan sağa çifter çifter alınır.

In [20]:

```
1 == 2 or 3 > 4 or 5 < 8


```

Out[20]:

```
True
```

In [21]:

```
1 != 2 and not 3 > 4 and 5 < 8


```

Out[21]:

```
True
```

In [22]:

```
1 != 2 and 3 <= 4 or 5 > 10 and 7 > 8


```

Out[22]:

```
True
```

# “Kısa devre” işlemler

Mantıksal işlemlerin yan etkileri vardır: Mantıksal `or` (veya) işleminde, işlenen değerlerden sadece birisinin doğru olması işlem sonucunun doğru olması için yeterlidir. Bu yüzden, Python `X or Y` işlemini yaparken `X`‘in doğru olduğunu görürse `Y`‘ye hiç bakmaz, onu değerlemez, ve işlem sonucu olarak `X`‘in değerini geri verir. Buna *kısa devre hesaplama* adı verilir. Eğer `X` doğru değilse, `Y` ne olursa olsun, `Y`‘yi verir.

Kısa devre özelliği hesaplama verimliliği de sağlar. Bazen bu işlemlerin bileşenleri karmaşık işlemlerle elde ediliyor olabilir. Sözgelişi `Y` yerine, bir fonksiyon çağrısı koyuyor olabiliriz, ve bu fonksiyon ağır işlemler yapıyor olabilir. Böyle durumlarda kısa devre işlemler hesaplamada verimlilik sağlarlar, `Y`‘yi boş yere hesaplamazlar.

Aşağıdaki örnekte, `"abc"` doğru sayıldığı için, `print` işlemi hiç yapılmadan `"abc"` geri verilir.

In [29]:

```
"abc" or print("mrb")


```

Out[29]:

```
'abc'
```

Aşağıdaki örnekte, `or` işleminin değerini anlamak için `print` komutu işlenir. Bunun yan etkisi olarak `"mrb"` yazılır. Ama `print` çağrısı `None` verir, o yüzden `or` işlemi de `None` sonucu verir.

In [34]:

```
False or print("mrb")


```

```
mrb


```

In [28]:

```
0 or 3


```

Out[28]:

```
3
```

Benzer bir durum `X and Y` işlemi için de geçerlidir. Eğer `X` mantıksal olarak yanlışsa, `Y`ne olursa olsun bütün ifade yanlış olur, böylece `X` değeri geri verilir. Ama `X` doğruysa, işlemin doğruluk değeri `Y`‘ye bağlıdır, ve `Y`değeri geri verilir.

In [35]:

```
2 and 3


```

Out[35]:

```
3
```

In [36]:

```
3 and print("mrb")


```

```
mrb


```

In [39]:

```
0 and 2


```

Out[39]:

```
0
```

In [40]:

```
[] and False


```

Out[40]:

```
[]
```

Bu özellik çeşitli “hack”ler için kullanılabilir. Sözgelişi

```
X = A or B or C or None


```

ifadesi, `X`‘in, `A`, `B`, `C` arasında boş olmayan ilk nesneye atanmasını, veya `None` olmasını sağlar. Aynı şeyi `if-elif-else` kullanarak yapmak daha uzun bir kod gerektirir.

```python
if A:

    X = A

elif B:

    X = B

elif C:

    X = C

else:

    X = None
```

# Üçlü if-else ifadesi

Birçok durumda, bir değişkene, bir şartın doğru veya yanlış olmasına göre farklı değerler atarız. Sözgelişi, `x` mantık ifadesinin doğru olması halinde `a`‘ya `y` değeri verelim, aksi takdirde `z` verelim.

```python
if x:

    a = y

else:

    a = z


```

Üçlü `if-else` ifadesiyle aynısını daha kısa olarak şöyle yazabiliriz:

```
a = y if x else z


```

Örnek olarak, `m`‘ye `x`‘in mutlak değerini atayalım.

In [42]:

```python
x = float(input("Bir sayı girin: "))

m = x if x>0 else -x

print(m)


```

```
Bir sayı girin: -1.4

1.4


```

En baştaki örneği de şöyle yazabiliriz.

In [43]:

```python
hedef = "42"

x = input("Tahmininiz: ")

print("Doğru!" if x == hedef else "Yanlış")


```

```
Tahmininiz: 43

Yanlış


```

Bir `if-elif-else` blokunu üçlü `if-else` ifadesi olarak yazabiliriz. Sözgelişi

```python
if rating > 100:

    sinif = "A"

elif rating > 50:

    sinif = "B"

else:

    sinif = "C"


```

yerine

```python
sinif = "A" if rating > 100 else "B" if rating > 50 else "C"


```

yazılabilir. Ama aşırıya kaçırırsanız programın okunması zorlaşır.
