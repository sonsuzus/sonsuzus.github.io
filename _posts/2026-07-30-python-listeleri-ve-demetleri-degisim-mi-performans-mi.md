---
layout: post
title: "Python Listeleri ve Demetleri: Değişim mi, Performans mı?"
math: true
categories: 
  - Bilgi
tags: 
  - Python
  - Listeler
  - Demetler
---

Python’da sıralı verileri saklamak istediğimizde karşımıza çoğunlukla iki güçlü seçenek çıkar: listeler (`list`) ve demetler (`tuple`). İlk bakışta ikisi de elemanları sırayla tutar, indekslenebilir ve döngülerde kullanılabilir. Ancak perde arkasında önemli bir ayrım vardır: Listeler değiştirilebilirken demetler oluşturulduktan sonra sabit kalır. Bu fark; güvenlikten performansa, bellek tüketiminden kodun okunabilirliğine kadar pek çok kararı etkiler.

``

## Ortak temel: Sıralı veri yapıları

Liste ve demetler, elemanların eklenme sırasını korur. Her iki yapıda da indeksler sıfırdan başlar. $n$ elemanlı bir koleksiyonun geçerli indeks aralığı şu şekilde ifade edilir:

$$0 \leq i < n$$

Negatif indeksler ise sondan erişim sağlar. Örneğin `-1` son elemanı, `-2` sondan ikinci elemanı temsil eder. İndeks üzerinden okuma işlemi iki yapıda da genellikle $O(1)$ zaman karmaşıklığına sahiptir.

```python
liste = ["Python", "JavaScript", "Go"]
demet = ("Python", "JavaScript", "Go")

print(liste[0])   # Python
print(demet[-1])  # Go
```

Bu kod, iki veri yapısında da indeksleme mantığının aynı olduğunu gösterir. Fakat koleksiyonu değiştirmeye çalıştığımızda yollar ayrılır.

## Değiştirilebilirlik: Listenin süper gücü

Listeler **mutable**, yani değiştirilebilir yapılardır. Eleman ekleyebilir, silebilir veya mevcut bir değeri güncelleyebiliriz. Bu nedenle kullanıcı sepeti, görev listesi ya da sürekli büyüyen sensör verileri gibi dinamik senaryolarda idealdir.

```python
gorevler = ["Kod yaz", "Test yap"]

gorevler.append("Belgele")       # Sona yeni görev ekler
gorevler[0] = "Temiz kod yaz"    # İlk görevi günceller
gorevler.remove("Test yap")      # Belirtilen görevi siler

print(gorevler)
```

Bir listenin sonuna `append()` ile eleman eklemek ortalama $O(1)$ maliyetlidir. Buna karşılık listenin başına eleman eklemek, diğer elemanların kaydırılmasını gerektirdiği için $O(n)$ maliyetine ulaşabilir.

Demetler ise **immutable**, yani değiştirilemez yapılardır:

```python
koordinat = (41.0082, 28.9784)
# koordinat[0] = 40.0  # TypeError üretir
```

Buradaki “sabitlik”, demetin tuttuğu referansların değiştirilememesi anlamına gelir. Demetin içinde bir liste bulunuyorsa o listenin içeriği yine değiştirilebilir. Kısacası demet koruyucu bir kasa gibidir; ancak kasanın içine koyduğunuz nesnenin kendi davranışı ayrıca değerlendirilmelidir.

## Karşılaştırma tablosu

| Özellik | Liste (`list`) | Demet (`tuple`) |
|---|---|---|
| Yazım | `[1, 2, 3]` | `(1, 2, 3)` |
| Değiştirilebilirlik | Evet | Hayır |
| Eleman ekleme/silme | Desteklenir | Desteklenmez |
| Bellek kullanımı | Genellikle daha fazla | Genellikle daha az |
| Sözlük anahtarı olabilme | Hayır | Elemanları uygunsa evet |
| Uygun senaryo | Dinamik koleksiyonlar | Sabit kayıtlar |

## Demetler neden daha performanslı olabilir?

Python listeleri gelecekte eklenecek elemanlar için fazladan kapasite ayırabilir. Bu yaklaşım ekleme işlemlerini hızlandırır, fakat ek bellek kullanır. Demetlerin boyutu baştan belli olduğu için daha kompakt bir bellek düzeni kullanılabilir. Ayrıca değişmeyecekleri bilindiğinden bazı işlemler daha az kontrol gerektirir.

```python
import sys

liste = [1, 2, 3, 4, 5]
demet = (1, 2, 3, 4, 5)

print(sys.getsizeof(liste))
print(sys.getsizeof(demet))
```

Bu örnek, aynı elemanları içeren yapıların yüzeysel bellek boyutlarını karşılaştırır. Sonuçlar Python sürümüne ve platforma göre değişse de demet çoğunlukla daha az yer kaplar. Yine de küçük koleksiyonlarda performans farkı için okunabilirliği feda etmek pek mantıklı değildir.

## Paketleme ve parçalama

Demetler, bir fonksiyondan birden fazla değer döndürürken oldukça kullanışlıdır:

```python
def min_max(sayilar):
    return min(sayilar), max(sayilar)

en_kucuk, en_buyuk = min_max([8, 3, 12, 5])
print(en_kucuk, en_buyuk)
```

Fonksiyon gerçekte iki değeri bir demet içinde paketler; atama sırasında bu demet parçalanır. Böylece kod hem kısa hem de anlamlı olur.

## Hangisini seçmeliyiz?

Veriler zamanla değişecekse liste seçmek en doğal yaklaşımdır. Koordinat, RGB rengi, tarih bileşenleri veya veritabanından gelen sabit bir kayıt gibi elemanların değişmemesi gerekiyorsa demet daha güçlü bir niyet beyanıdır. Özetle liste “üzerimde çalış” derken demet “beni bir bütün olarak koru” der. Doğru seçim yalnızca birkaç nanosaniye kazanmak değil, kodun gelecekteki okuyucusuna verinin nasıl davranması gerektiğini açıkça anlatmaktır.
