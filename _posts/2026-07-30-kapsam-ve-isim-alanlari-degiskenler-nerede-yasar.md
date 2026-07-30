---
layout: post
title: "Kapsam ve İsim Alanları: Değişkenler Nerede Yaşar?"
math: true
categories: 
  - Bilgi
tags: 
  - scope
  - isim alanları
  - python
---

Bir değişkeni tanımlamak, ona yalnızca bir değer vermek değildir; aynı zamanda bu ismin programın hangi bölümlerinde görülebileceğini de belirlemektir. Kapsam (scope), bir isme erişilebilen kod bölgesini; isim alanı (namespace) ise isimlerle nesneler arasındaki eşleşmelerin tutulduğu yapıyı ifade eder. Özellikle Python gibi girintinin blok yapısını belirlediği dillerde bu iki kavramı anlamak, beklenmedik hataları önlemenin anahtarıdır.
``
## Kapsam ve isim alanı aynı şey mi?

Bu kavramlar yakın akraba olsalar da aynı değildir. İsim alanını bir sözlük, kapsamı ise o sözlüğe hangi noktadan erişilebildiğini belirleyen kurallar bütünü gibi düşünebiliriz.

Matematiksel olarak bir isim alanını şu eşleme ile gösterebiliriz:

$$N: \text{İsimler} \rightarrow \text{Nesneler}$$

Örneğin `x = 42` ifadesi, ilgili isim alanında $N(x)=42$ eşleşmesini oluşturur. Program `x` ismini kullandığında yorumlayıcı, geçerli kapsamları belirli bir sırayla araştırır.

| Kavram | Temel soru | Örnek |
|---|---|---|
| İsim alanı | İsim hangi nesneye bağlı? | `x` ismi `42` nesnesine bağlıdır |
| Kapsam | Bu isme nereden erişilebilir? | `x`, yalnızca fonksiyon içinde görülebilir |
| Yaşam süresi | Nesne veya bağ ne kadar yaşar? | Fonksiyon çağrısı tamamlanana kadar |

## Python'da LEGB arama sırası

Python, bir ismi çözümlerken **LEGB** kuralını kullanır:

1. **Local:** Çalışan fonksiyonun yerel isim alanı.
2. **Enclosing:** İç içe fonksiyonlarda dış fonksiyonların alanları.
3. **Global:** Modül seviyesinde tanımlanan isimler.
4. **Built-in:** `len`, `print` ve `range` gibi hazır isimler.

Bu arama sırasını $L \rightarrow E \rightarrow G \rightarrow B$ biçiminde özetleyebiliriz. İlk eşleşme bulunduğunda arama durur. Dolayısıyla yerel bir `print` değişkeni tanımlarsanız yerleşik `print()` fonksiyonunu gölgeleyebilirsiniz. Program çalışır gibi görünürken bir anda “`str` nesnesi çağrılamaz” hatası vermesi, Python'ın küçük bir şakası değildir; isim gölgelemenin sonucudur.

```python
message = "Global mesaj"

def show_message():
    message = "Lokal mesaj"
    print(message)

show_message()  # Lokal mesaj
print(message)  # Global mesaj
```

Fonksiyon içindeki atama yeni bir lokal isim üretir. Dışarıdaki `message` değişkeni değişmez; iki isim farklı isim alanlarında bulunur.

## Girinti her zaman yeni kapsam oluşturmaz

Python'da fonksiyonlar, sınıflar ve modüller isim alanı oluşturur. Ancak `if`, `for` ve `while` blokları girintili olmalarına rağmen ayrı bir lokal kapsam meydana getirmez.

```python
if True:
    result = 25

print(result)  # 25

for number in range(3):
    squared = number ** 2

print(squared)  # 4
```

Bu davranış JavaScript'teki `let` veya C ailesindeki blok kapsamından farklıdır.

| Yapı | Python'da yeni kapsam? | Not |
|---|---:|---|
| Fonksiyon | Evet | Parametreler de lokaldir |
| Sınıf | Evet | Sınıf isim alanı oluşturur |
| `if` bloğu | Hayır | Tanımlanan isim dışarıdan görülebilir |
| `for` döngüsü | Hayır | Döngü değişkeni bloktan sonra kalır |
| Liste üreteci | Evet | Döngü değişkeni dışarı sızmaz |

## `global` ve `nonlocal` anahtar sözcükleri

Bir fonksiyon içinde global değişkeni yeniden bağlamak için `global` gerekir. İç içe fonksiyonlarda dış fonksiyonun değişkenini değiştirmek içinse `nonlocal` kullanılır.

```python
counter = 0

def create_incrementer():
    step = 1

    def increment():
        global counter
        nonlocal step
        counter += step
        step += 1
        return counter

    return increment
```

Burada `counter` modül alanında, `step` ise çevreleyen fonksiyon alanındadır. Her çağrıda artış miktarının korunması, closure adı verilen yapının sonucudur.

## Sağlam tasarım için öneriler

Global değişkenler kolay erişim sağlar fakat fonksiyonların gizli bağımlılıklar taşımasına yol açar. Bu nedenle değerleri parametre olarak geçirmek ve sonucu `return` ile döndürmek genellikle daha test edilebilir bir tasarım üretir. Ayrıca yerleşik fonksiyon adlarını değişken olarak kullanmamak, kısa ama belirsiz isimlerden kaçınmak ve kapsamı mümkün olduğunca dar tutmak önemlidir.

Özetle kapsam, bir değişkenin “nereden görüldüğünü”; isim alanı ise “hangi nesneyi temsil ettiğini” açıklar. LEGB sırasını ve girintili her bloğun yeni kapsam oluşturmadığını bilmek, değişkenlerin program içinde saklambaç oynamasını büyük ölçüde engeller.
