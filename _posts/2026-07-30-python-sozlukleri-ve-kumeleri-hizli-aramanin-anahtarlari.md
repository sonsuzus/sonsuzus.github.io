---
layout: post
title: "Python Sözlükleri ve Kümeleri: Hızlı Aramanın Anahtarları"
math: true
categories: 
  - Bilgi
tags: 
  - Python
  - Veri Yapıları
  - Dictionary ve Set
---

Bir kullanıcıyı adına göre bulmak veya tekrar eden ürün kodlarını ayıklamak istediğinizde listeler işe yarar; ancak veri büyüdükçe tek tek arama yapmak yorucu hâle gelir. Python’ın sözlükleri (`dict`) ve kümeleri (`set`), hash tabanlı yapıları sayesinde arama, ekleme ve silme işlemlerini çoğu durumda son derece hızlı gerçekleştirir. Biri anahtarları değerlerle eşleştirirken diğeri yalnızca benzersiz elemanları saklar.
``
## Sözlük nedir?

Sözlük, verileri **anahtar-değer** çiftleri hâlinde tutar. Gerçek hayattaki bir telefon rehberini düşünün: kişinin adı anahtar, telefon numarası ise değerdir. Anahtarlar benzersiz olmalıdır fakat değerler tekrar edebilir.

```python
kullanici = {
    'ad': 'Ada',
    'yas': 28,
    'aktif': True
}

print(kullanici['ad'])       # Ada
kullanici['sehir'] = 'İzmir' # Yeni eşleşme ekler
kullanici['yas'] = 29        # Mevcut değeri günceller
```

Olmayan bir anahtara köşeli parantezlerle erişmek `KeyError` üretir. Daha güvenli bir okuma için `get()` kullanılabilir:

```python
rol = kullanici.get('rol', 'misafir')
print(rol)  # Anahtar yoksa misafir
```

## Kümeler neden farklıdır?

Küme, matematikteki küme kavramına benzer: her eleman yalnızca bir kez bulunur ve elemanların anlamlı bir sırası yoktur. Bu nedenle tekrarları temizlemek ve üyelik kontrolü yapmak için idealdir.

```python
etiketler = {'python', 'api', 'python', 'web'}
print(etiketler)  # python yalnızca bir kez bulunur

etiketler.add('veri')
etiketler.discard('api')  # Eleman yoksa hata üretmez
print('web' in etiketler)
```

Boş küme oluştururken `{}` kullanılamaz; bu ifade boş bir sözlük oluşturur. Doğru kullanım `set()` biçimindedir.

| Özellik | Sözlük (`dict`) | Küme (`set`) |
|---|---|---|
| Saklanan veri | Anahtar-değer çiftleri | Benzersiz elemanlar |
| Tekrar | Anahtar tekrarlanamaz | Eleman tekrarlanamaz |
| Değere erişim | Anahtar üzerinden | Değer saklamaz |
| Tipik kullanım | Profil, ayar, sayaç | Üyelik testi, tekrar temizleme |
| Boş oluşturma | `{}` | `set()` |

## Hızın arkasındaki fikir: hash tablosu

Her iki yapı da çoğunlukla **hash tablosu** kullanır. Python, anahtarın veya elemanın hash değerini hesaplayıp verinin yerleştirileceği bölgeyi belirler. Basitleştirilmiş biçimde konum şu şekilde düşünülebilir:

$$konum = hash(anahtar) \bmod kapasite$$

Bu yaklaşım, veriyi baştan sona taramak yerine doğrudan olası konuma gitmeyi sağlar. Ortalama durumda arama karmaşıklığı $O(1)$ olur. Bir listede arama ise genellikle $O(n)$ sürer. Hash çakışmaları ve yeniden boyutlandırma gibi nedenlerle en kötü durum $O(n)$ olabilir; fakat Python’ın uygulaması ortalama performansı oldukça güçlü tutar.

Anahtarlar hash değeri değişmeyen türlerden seçilmelidir. Sayılar, metinler ve uygun tuple’lar anahtar olabilirken listeler sözlük anahtarı veya küme elemanı olamaz.

## Küme cebiriyle pratik işlemler

Kümeler karşılaştırma yaparken özellikle eğlencelidir:

```python
backend = {'Python', 'SQL', 'Docker'}
frontend = {'JavaScript', 'CSS', 'Docker'}

print(backend & frontend)  # Kesişim: ortak beceriler
print(backend | frontend)  # Birleşim: tüm beceriler
print(backend - frontend)  # Fark: yalnızca backend
print(backend ^ frontend)  # Simetrik fark: ortak olmayanlar
```

Matematiksel olarak birleşim $A \cup B$, kesişim $A \cap B$ ve fark $A - B$ ile gösterilir. Böylece uzun koşullar yazmadan iki veri grubunu karşılaştırabiliriz.

## Birlikte kullanım

Sözlük ve küme birlikte de güçlüdür. Örneğin kelime sıklıklarını sayarken sözlük adetleri, küme ise benzersiz kelimeleri tutabilir:

```python
kelimeler = ['kod', 'veri', 'kod', 'python']
sayac = {}

for kelime in kelimeler:
    sayac[kelime] = sayac.get(kelime, 0) + 1

benzersiz = set(kelimeler)
print(sayac)
print(benzersiz)
```

Özetle, bir bilgiyi başka bir bilgiyle eşleştirecekseniz sözlük; tekrarları engellemek veya hızlı üyelik kontrolü yapmak istiyorsanız küme seçin. Doğru veri yapısı, çalışan kodu hızlı ve anlaşılır koda dönüştüren küçük ama etkili bir süper güçtür.
