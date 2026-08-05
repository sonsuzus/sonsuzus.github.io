---
layout: post
title: "Sıralama Algoritmalarının İç İşleyişi: Hangi Durumda Hangisi Daha Hızlı?"
math: true
categories: 
  - Bilgi
tags: 
  - sıralama algoritmaları
  - algoritma analizi
  - performans optimizasyonu
---

Bir veri kümesini sıralamak, programlamanın “çorapları renklerine göre ayırma” problemidir: sonuç basit görünür, fakat doğru yöntem seçilmezse işlem gereksiz yere uzar. Bubble Sort, Merge Sort, Quick Sort ve Heap Sort aynı çıktıyı üretse de bunu yaparken farklı miktarda zaman, bellek ve karşılaştırma harcar. Optimizasyon sorularını çözebilmek için algoritmaların yalnızca karmaşıklıklarını ezberlemek değil, içeride nasıl çalıştıklarını anlamak gerekir.
``
## Performansı nasıl ölçeriz?

Bir sıralama algoritmasının maliyeti çoğunlukla karşılaştırma ve yer değiştirme sayısıyla değerlendirilir. Girdi boyutu $n$ ise iki iç içe döngü kullanan basit algoritmalar genellikle

$$T(n) \approx \frac{n(n-1)}{2} = O(n^2)$$

karşılaştırma yapar. Böl ve yönet yaklaşımında veri her adımda iki parçaya ayrılır. Yaklaşık $\log_2 n$ seviye oluşur ve her seviyede $n$ eleman işlendiği için maliyet $O(n\log n)$ olur.

| Algoritma | En iyi | Ortalama | En kötü | Ek bellek | Kararlı mı? |
|---|---:|---:|---:|---:|---|
| Bubble Sort | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | Evet |
| Insertion Sort | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | Evet |
| Merge Sort | $O(n\log n)$ | $O(n\log n)$ | $O(n\log n)$ | $O(n)$ | Evet |
| Quick Sort | $O(n\log n)$ | $O(n\log n)$ | $O(n^2)$ | $O(\log n)$ | Genellikle hayır |
| Heap Sort | $O(n\log n)$ | $O(n\log n)$ | $O(n\log n)$ | $O(1)$ | Hayır |

Kararlılık, eşit anahtara sahip elemanların başlangıçtaki sırasının korunmasıdır. Örneğin çalışanları önce ada, sonra departmana göre sıralıyorsanız kararlı algoritma önceki düzeni kaybetmez.

## Algoritmalar içeride ne yapıyor?

**Bubble Sort**, komşu elemanları karşılaştırır ve yanlış sıradaysa yer değiştirir. Büyük değerler köpük gibi sona çıkar. Dizi zaten sıralıysa bir `swapped` bayrağı sayesinde erkenden durabilir.

**Insertion Sort**, her elemanı soldaki sıralı bölge içinde uygun konuma yerleştirir. Küçük veya neredeyse sıralı dizilerde az sayıda kaydırma yaptığı için teorik olarak daha güçlü görünen algoritmaları geçebilir.

**Merge Sort**, diziyi tek elemanlı parçalara kadar böler ve parçaları sıralı biçimde birleştirir. Tahmin edilebilir performansı güçlüdür; ancak yardımcı dizi nedeniyle bellek tüketir.

**Quick Sort**, bir pivot seçerek küçük değerleri sola, büyükleri sağa taşır. Pivot dengeli bölme yaparsa hızlıdır. Sürekli en küçük ya da en büyük elemanın seçilmesi ise bölümleri $0$ ve $n-1$ boyutlarına ayırarak $O(n^2)$ sonucunu doğurur.

Aşağıdaki kod, rastgele pivot kullanarak bu riski azaltır:

```python
import random

def quick_sort(values):
    if len(values) <= 1:
        return values

    pivot = random.choice(values)
    small = [x for x in values if x < pivot]
    equal = [x for x in values if x == pivot]
    large = [x for x in values if x > pivot]

    return quick_sort(small) + equal + quick_sort(large)
```

Kod okunaklıdır ve rastgele pivot kötü durum olasılığını düşürür. Bununla birlikte yeni listeler oluşturduğu için klasik yerinde Quick Sort uygulamasından daha fazla bellek kullanır.

## Optimizasyon sorularına yaklaşım

**Soru 1: Bir milyon rastgele eleman ve sınırlı bellek varsa ne seçilir?**  
Merge Sort’un $O(n)$ ek belleği sorun olabilir. Heap Sort, $O(1)$ yardımcı bellek ve garantili $O(n\log n)$ süresiyle güvenli seçimdir. Pratikte iyi uygulanmış yerinde Quick Sort da önbellek dostu yapısıyla daha hızlı olabilir.

**Soru 2: Dizi yüzde 95 sıralıysa?**  
Insertion Sort değerlendirilmelidir. Çalışma süresi terslik sayısıyla ilişkilidir: $O(n+k)$. Buradaki $k$, yanlış sıradaki eleman çiftlerinin sayısıdır. $k$ küçükse algoritma doğrusal zamana yaklaşır.

**Soru 3: Eşit kayıtların sırası korunmalıysa?**  
Kararlı Merge Sort uygundur. Quick Sort seçilecekse kararlılığı ayrıca sağlamak gerekir; bu da bellek ve uygulama karmaşıklığı getirir.

Sonuç olarak “en hızlı sıralama algoritması” diye evrensel bir şampiyon yoktur. Girdi boyutu, mevcut düzen, bellek sınırı, kararlılık ihtiyacı ve en kötü durum garantisi birlikte değerlendirilmelidir. İyi optimizasyon, yalnızca Big-O seçmek değil, verinin davranışını tanımaktır.
