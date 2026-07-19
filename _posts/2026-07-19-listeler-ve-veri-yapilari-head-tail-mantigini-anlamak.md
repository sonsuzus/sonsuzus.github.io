---
layout: post
title: "Listeler ve Veri Yapıları: Head-Tail Mantığını Anlamak"
math: true
categories: 
  - Bilgi
tags: 
  - listeler
  - veri-yapıları
  - programlama-temelleri
---

Birden fazla veriyi tek tek değişkenlerde taşımak, market poşetlerini tek parmakla taşımaya benzer: mümkün ama gereksiz acı verici. Listeler, verileri köşeli parantezler içinde tek bir bütün gibi saklamamızı sağlar: `[10, 20, 30]`. Daha önemlisi, bu bütünün ilk elemanını **baş** yani **head**, geri kalan kısmını ise **kuyruk** yani **tail** olarak düşünebiliriz.
``
Liste dediğimiz yapı, temelde sıralı bir koleksiyondur. Yani elemanların yalnızca varlığı değil, **hangi sırada durdukları** da önemlidir. Matematiksel olarak bir listeyi şöyle düşünebiliriz: $L = [x_1, x_2, x_3, ..., x_n]$. Burada listenin uzunluğu $n$ ile gösterilir. Eğer $n = 0$ ise elimizde boş liste vardır: `[]`. Eğer $n > 0$ ise listenin başı $x_1$, kuyruğu ise `[x_2, x_3, ..., x_n]` olur.

Bu ayrım özellikle fonksiyonel programlamada çok güçlüdür. Çünkü bir listeyi işlemek için genellikle şu soru sorulur: “Liste boş mu?” Boş değilse, baş elemanı alırız ve geri kalan kuyruk üzerinde aynı işlemi tekrarlarız. Bu yaklaşım, özyineleme yani recursion mantığının da temel taşlarından biridir.

| Kavram | Anlamı | Örnek |
|---|---|---|
| Liste | Sıralı veri koleksiyonu | `[3, 5, 8]` |
| Head | İlk eleman | `3` |
| Tail | İlk eleman dışındaki liste | `[5, 8]` |
| Boş liste | Elemanı olmayan liste | `[]` |

Klasik dizilerle listeler çoğu dilde birbirine benzer görünür, fakat düşünme biçimi farklı olabilir. Özellikle head-tail yaklaşımı, listeyi parçalara ayırarak anlamayı kolaylaştırır.

| Yaklaşım | Odak Noktası | Tipik Kullanım |
|---|---|---|
| İndeks tabanlı | `liste[0]`, `liste[1]` gibi erişim | Döngüler, rastgele erişim |
| Head-tail tabanlı | İlk eleman + kalan liste | Özyineleme, veri ayrıştırma |
| Yığın mantığı | Son giren ilk çıkar | Undo sistemi, çağrı yığını |
| Kuyruk mantığı | İlk giren ilk çıkar | Mesaj sırası, görev planlama |

Python’da köşeli parantezlerle liste oluşturmak oldukça basittir:

```python
sayilar = [4, 7, 11, 18]

head = sayilar[0]
tail = sayilar[1:]

print(head)  # 4
print(tail)  # [7, 11, 18]
```

Bu kodda `sayilar[0]` listenin ilk elemanını verir. `sayilar[1:]` ise bir dilimleme işlemidir ve birinci indeksten sona kadar olan kısmı yeni bir liste olarak döndürür. Yani elimizdeki listeyi “ilk lokma” ve “tabakta kalanlar” diye ayırmış oluruz.

Python’da daha zarif bir ayrıştırma yöntemi de vardır:

```python
meyveler = ['elma', 'armut', 'kiraz', 'muz']

head, *tail = meyveler

print(head)  # elma
print(tail)  # ['armut', 'kiraz', 'muz']
```

Buradaki `*tail` ifadesi, geri kalan tüm elemanları toplar. Kodun yaptığı şey şudur: “İlk elemanı `head` değişkenine koy, kalanları da `tail` listesi olarak sakla.” Bu, head-tail mantığını doğrudan ifade ettiği için okunması da oldukça rahattır.

Ancak dikkat: boş liste üzerinde head almaya çalışmak hataya yol açar. Çünkü $L = []$ iken $x_1$ diye bir eleman yoktur. Bu yüzden güvenli işlem yapmak için önce listenin boş olup olmadığı kontrol edilmelidir.

```python
def listeyi_yaz(liste):
    if not liste:
        return

    head, *tail = liste
    print('Baş:', head)
    listeyi_yaz(tail)

listeyi_yaz([10, 20, 30])
```

Bu örnekte fonksiyon önce listenin boş olup olmadığını kontrol eder. Boş değilse baş elemanı yazdırır ve kuyruğu aynı fonksiyona tekrar gönderir. Böylece liste adım adım küçülür. Her adımda problem boyutu $n$ değerinden $n - 1$ değerine iner. Bu da algoritmanın doğal bir sonlanma noktasına sahip olmasını sağlar.

Performans açısından da düşünmek önemlidir. Bir listenin ilk elemanına erişmek çoğu modern dilde $O(1)$ kabul edilir. Fakat `liste[1:]` gibi kuyruk üretmek bazı dillerde yeni liste oluşturduğu için $O(n)$ maliyetli olabilir. Bu yüzden teoriyi bilmek güzel, ama kullandığın dilin veri yapısı davranışlarını bilmek daha da güzeldir.

Sonuç olarak listeler yalnızca “yan yana yazılmış değerler” değildir. Onlar, veriyi sıraya koymanın, parçalamanın ve anlamlı biçimde işlemenin temel araçlarındandır. Head-tail mantığı ise bu araç kutusundaki İsviçre çakısı gibidir: basit görünür, ama doğru yerde kullanıldığında kodu hem sadeleştirir hem de düşünme biçimini keskinleştirir.
