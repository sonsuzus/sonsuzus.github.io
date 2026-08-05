---
layout: post
title: "Diziden Kuyruğa: Veri Yapılarıyla Akıllı Problem Çözme"
math: true
categories: 
  - Bilgi
tags: 
  - veri yapıları
  - algoritmalar
  - python
---

Bir algoritmanın başarısı yalnızca doğru sonucu üretmesine değil, bunu ne kadar hızlı ve az bellek kullanarak yaptığına da bağlıdır. Diziler, bağlı listeler, yığınlar ve kuyruklar bu noktada programcının alet çantasındaki temel araçlardır. Doğru veri yapısını seçmek bazen yüzlerce satır kod yazmaktan daha değerlidir; yanlış seçim ise hızlı görünen bir çözümü kaplumbağaya çevirebilir.
``

## Veri yapısı seçimi neden önemlidir?

Bir veri yapısını değerlendirirken genellikle zaman ve alan karmaşıklığına bakarız. Bir algoritmanın çalışma süresi, girdi büyüklüğü $n$ arttıkça değişir. Örneğin bir dizinin bütün elemanlarını gezmek $T(n)=an+b$ biçiminde modellenebilir ve bu işlem $O(n)$ karmaşıklığındadır.

Sık kullanılan işlemlerin genel karşılaştırması şöyledir:

| Veri yapısı | İndeksle erişim | Başa ekleme | Sona ekleme | Tipik kullanım |
|---|---:|---:|---:|---|
| Dizi | $O(1)$ | $O(n)$ | $O(1)$ amortize | Hızlı erişim, sıralı veriler |
| Bağlı liste | $O(n)$ | $O(1)$ | $O(1)$* | Sık ekleme ve silme |
| Yığın | Yalnızca tepe | $O(1)$ | — | Geri alma, parantez kontrolü |
| Kuyruk | Yalnızca ön | — | $O(1)$ | İş sıralama, genişlik öncelikli arama |

\* Son düğümün adresi ayrıca tutuluyorsa.

## Diziler: Hızlı erişimin yıldızı

Diziler elemanları mantıksal olarak yan yana saklar. Bu nedenle $i$ numaralı elemana erişmek için başlangıç adresine belirli bir uzaklık eklemek yeterlidir:

$$adres(i)=başlangıç+i\times eleman\_boyutu$$

Bu hesaplama sabit zamanda yapılır. Sık sık “beşinci eleman nedir?” diye sorulan problemlerde dizi güçlü bir seçimdir. Buna karşılık dizinin başına eleman eklemek, diğer elemanların kaydırılmasını gerektirdiği için pahalıdır.

Örneğin iki işaretçi tekniği, sıralı bir dizide hedef toplamı ararken iç içe döngü ihtiyacını ortadan kaldırır:

```python
def hedef_cifti_bul(sayilar, hedef):
    sol, sag = 0, len(sayilar) - 1

    while sol < sag:
        toplam = sayilar[sol] + sayilar[sag]
        if toplam == hedef:
            return sayilar[sol], sayilar[sag]
        if toplam < hedef:
            sol += 1
        else:
            sag -= 1

    return None
```

Bu kod, sıralı dizinin iki ucundan ilerleyerek uygun çifti bulur. Kaba kuvvet yaklaşımının $O(n^2)$ maliyetini $O(n)$ seviyesine indirir.

## Bağlı listeler: Esnek vagonlar

Bağlı listeyi, her vagonun bir sonrakinin adresini taşıdığı tren gibi düşünebiliriz. Düğümler bellekte yan yana olmak zorunda değildir. Bir düğüm biliniyorsa araya yeni düğüm eklemek yalnızca bağlantıları değiştirdiği için $O(1)$ sürer.

Ancak belirli bir indekse doğrudan sıçranamaz; düğümler baştan itibaren gezilmelidir. Dolayısıyla rastgele erişimin yoğun olduğu bir problemde bağlı liste kullanmak, kitabın her sayfasını birinciden başlayarak aramaya benzer.

Bağlı listeler; müzik listeleri, tarayıcı geçmişi ve sık ekleme-silme yapılan koleksiyonlar için uygundur. Çift bağlı listeler ileri ve geri hareket sağlarken fazladan işaretçi belleği tüketir.

## Yığın: Son gelen ilk çıkar

Yığın, $LIFO$ yani “son giren ilk çıkar” ilkesini uygular. Tabakları üst üste koyduğunuzu düşünün: İlk olarak en üstteki tabağı alırsınız. Fonksiyon çağrıları, geri alma işlemleri ve sözdizimi denetimi yığının doğal kullanım alanlarıdır.

```python
def parantezler_dengeli_mi(metin):
    yigin = []
    eslesme = {')': '(', ']': '[', '}': '{'}

    for karakter in metin:
        if karakter in '([{':
            yigin.append(karakter)
        elif karakter in eslesme:
            if not yigin or yigin.pop() != eslesme[karakter]:
                return False

    return len(yigin) == 0
```

Burada açılan parantezler yığına eklenir; kapanış görüldüğünde en son açılan parantez çıkarılır. Her karakter bir kez işlendiğinden süre $O(n)$, en kötü durumdaki bellek kullanımı da $O(n)$ olur.

## Kuyruk: Sıraya kaynak yapmak yok

Kuyruk $FIFO$, yani “ilk giren ilk çıkar” düzeninde çalışır. Yazdırma görevleri, mesaj sistemleri ve genişlik öncelikli arama bu yapıyı kullanır. Bir grafikte başlangıç düğümüne en yakın noktaları önce keşfetmek istiyorsak kuyruğa komşuları ekler, önden sırayla çıkarırız.

Python’da listenin başından `pop(0)` kullanmak $O(n)$ maliyetlidir. Bunun yerine `collections.deque` tercih edilmelidir; `append` ve `popleft` işlemleri $O(1)$ zamanda gerçekleşir.

## Problem çözerken karar reçetesi

Önce problemin baskın işlemini belirleyin: İndeksle erişim gerekiyorsa dizi, sık bağlantı değişikliği varsa bağlı liste, en son eklenene dönülecekse yığın, geliş sırası korunacaksa kuyruk düşünün. Ardından en kötü durumu analiz edin ve $n$ iki katına çıktığında maliyetin nasıl değiştiğini sorun. Veri yapısı seçimi ezber değil, problemin davranışını doğru okuma sanatıdır.
