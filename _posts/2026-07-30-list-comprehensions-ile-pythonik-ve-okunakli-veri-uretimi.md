---
layout: post
title: "List Comprehensions ile Pythonik ve Okunaklı Veri Üretimi"
math: true
categories: 
  - Bilgi
tags: 
  - Python
  - List Comprehension
  - Pythonik Kod
---

Python’da bir listedeki verileri dönüştürmek veya belirli koşullara göre süzmek için uzun döngüler yazmak zorunda değilsiniz. **List comprehension**, klasik `for` döngülerini daha kısa, çoğu zaman daha okunaklı ve verimli bir ifadeye dönüştürür. Fakat mesele yalnızca satır sayısını azaltmak değildir; asıl amaç, yeni listenin nasıl üretildiğini doğrudan anlatan Pythonik bir sözdizimi kullanmaktır.
``
## List Comprehension Nedir?

List comprehension, yinelenebilir bir kaynaktan yeni bir liste oluşturan sözdizimsel bir yapıdır. Temel biçimi şöyledir:

```python
[yeni_deger for eleman in kaynak]
```

Matematiksel olarak bunu bir küme dönüşümüne benzetebiliriz. Bir $A$ veri kümesindeki her $x$ elemanına $f$ fonksiyonu uygulanıyorsa sonuç şöyle gösterilebilir:

$$B = \{f(x) \mid x \in A\}$$

Örneğin sayıların karelerini üretelim:

```python
sayilar = [1, 2, 3, 4, 5]
kareler = [sayi ** 2 for sayi in sayilar]

print(kareler)  # [1, 4, 9, 16, 25]
```

Buradaki ifade soldan sağa okunabilir: “`sayilar` içindeki her `sayi` için `sayi ** 2` değerini listeye ekle.” Aynı işlemin klasik döngüyle karşılığı daha uzundur:

```python
kareler = []
for sayi in sayilar:
    kareler.append(sayi ** 2)
```

| Özellik | Klasik döngü | List comprehension |
|---|---|---|
| Satır sayısı | Genellikle daha fazla | Genellikle tek satır |
| Listeye ekleme | `append()` açıkça çağrılır | Otomatik gerçekleştirilir |
| Okunabilirlik | Karmaşık işlemlerde avantajlı | Basit dönüşümlerde avantajlı |
| Performans | Ek metot çağrıları içerebilir | Çoğunlukla biraz daha hızlıdır |

## Koşulla Veri Süzme

İfadenin sonuna `if` ekleyerek yalnızca belirli elemanları seçebiliriz. Örneğin çift sayıların karelerini üretelim:

```python
sayilar = range(1, 11)
cift_kareler = [x ** 2 for x in sayilar if x % 2 == 0]

print(cift_kareler)  # [4, 16, 36, 64, 100]
```

Koşulun matematiksel karşılığı şu şekilde düşünülebilir:

$$B = \{x^2 \mid x \in A,\ x \bmod 2 = 0\}$$

Burada önce `x % 2 == 0` filtresi uygulanır, ardından koşulu geçen sayıların karesi hesaplanır. Böylece filtreleme ve dönüştürme tek bir ifadede birleşir.

## `if-else` Kullanımında Sıra Değişir

Her elemanı listeye almak, ancak koşula göre farklı bir değer üretmek istiyorsak `if-else` bölümü `for` ifadesinden önce yazılır:

```python
etiketler = ["çift" if x % 2 == 0 else "tek" for x in range(1, 6)]
print(etiketler)  # ['tek', 'çift', 'tek', 'çift', 'tek']
```

| Amaç | Sözdizimi |
|---|---|
| Elemanları filtrelemek | `[x for x in liste if kosul]` |
| Koşula göre dönüştürmek | `[a if kosul else b for x in liste]` |
| Tüm elemanları dönüştürmek | `[f(x) for x in liste]` |

Bu ayrım başlangıçta küçük bir Python bilmecesi gibi görünse de mantığı basittir: Sondaki `if`, elemanın listeye girip girmeyeceğine; baştaki `if-else` ise hangi değerin üretileceğine karar verir.

## İç İçe Döngüler

List comprehension birden fazla döngü de içerebilir. Aşağıdaki kod iki listenin tüm sayı çiftlerini üretir:

```python
harfler = ["A", "B"]
sayilar = [1, 2, 3]

eslesmeler = [(harf, sayi) for harf in harfler for sayi in sayilar]
print(eslesmeler)
```

Döngüler, klasik iç içe döngülerdeki sırayla yazılır. Yine de üç veya daha fazla döngü ve çok sayıda koşul eklemek okunabilirliği hızla düşürür. Tek satır yazabilmek, her zaman tek satır yazmanız gerektiği anlamına gelmez.

## Performans ve Pythonik Denge

List comprehensions, `append()` çağrısını Python seviyesinde tekrar tekrar çalıştırmadığı için klasik döngülerden çoğunlukla daha hızlıdır. Ancak bütün sonuçları bellekte tutar. Çok büyük veri akışlarında köşeli parantez yerine parantez kullanan **generator expression** tercih edilebilir:

```python
toplam = sum(x ** 2 for x in range(1_000_000))
```

Generator, değerleri ihtiyaç oldukça üretir; yaklaşık bellek yaklaşımı liste için $O(n)$, generator için ise çoğu senaryoda $O(1)$ düzeyindedir.

Sonuç olarak list comprehension; kısa dönüşüm, filtreleme ve eşleştirme işlemlerinde güçlü bir araçtır. Altın kural şudur: İfade ilk bakışta anlaşılabiliyorsa Pythoniktir; çözmek için dedektif şapkası gerekiyorsa klasik döngü daha iyi seçimdir.
