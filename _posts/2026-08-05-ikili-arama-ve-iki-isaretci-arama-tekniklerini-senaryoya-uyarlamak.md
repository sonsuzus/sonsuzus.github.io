---
layout: post
title: "İkili Arama ve İki İşaretçi: Arama Tekniklerini Senaryoya Uyarlamak"
math: true
categories: 
  - Bilgi
tags: 
  - algoritmalar
  - ikili arama
  - iki işaretçi
---

Bir dizide değer bulmak kolay görünebilir; ancak veri büyüdükçe doğrusal arama, samanlıkta iğne aramaya dönüşür. İkili arama ve iki işaretçi tekniği, yalnızca ezberlenecek kod kalıpları değil, farklı problemlere uyarlanabilen düşünme biçimleridir. Biri arama uzayını sürekli yarıya indirirken diğeri iki konumu koordineli hareket ettirerek gereksiz denemeleri ortadan kaldırır.

``

## İkili aramanın temel mantığı

İkili arama, sıralı bir veri kümesinin ortasındaki elemanı inceler. Aranan değer daha küçükse sağ yarıyı, daha büyükse sol yarıyı eler. Her adımda problem boyutu yarıya indiği için zaman karmaşıklığı:

$$T(n)=T(n/2)+O(1)=O(\log n)$$

şeklindedir. Örneğin yaklaşık bir milyon elemanda doğrusal arama bir milyon karşılaştırma yapabilirken ikili arama yaklaşık $\log_2(1.000.000)\approx20$ adımda sonuca ulaşır.

```python
def binary_search(numbers, target):
    left, right = 0, len(numbers) - 1

    while left <= right:
        middle = left + (right - left) // 2

        if numbers[middle] == target:
            return middle
        if numbers[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1
```

Bu kod, sıralı dizide hedefin indeksini bulur. `left <= right` koşulu tek elemanlık son aralığın da kontrol edilmesini sağlar.

## Sadece eleman değil, sınır aramak

İkili arama çoğu zaman “değer var mı?” sorusundan fazlasını çözer. Tekrarlı elemanlarda ilk konumu, son konumu veya belirli bir koşulu sağlayan en küçük değeri bulabiliriz. Örneğin `[2, 4, 4, 4, 9]` dizisinde ilk `4` aranırken eşitlikte durmak yerine sonucu kaydedip sola devam ederiz.

```python
def first_position(numbers, target):
    left, right = 0, len(numbers) - 1
    answer = -1

    while left <= right:
        middle = (left + right) // 2
        if numbers[middle] >= target:
            if numbers[middle] == target:
                answer = middle
            right = middle - 1
        else:
            left = middle + 1

    return answer
```

Aynı fikir “en az kaç sunucu gerekli?” veya “bir işi tamamlamaya yeten minimum kapasite nedir?” gibi cevap üzerinde arama problemlerine uygulanır. Buradaki kritik şart, kontrol fonksiyonunun monoton olmasıdır: Bir kapasite yeterliyse daha büyük kapasiteler de yeterli olmalıdır. Böylece sonuçlar `yanlış, yanlış, doğru, doğru` biçiminde ayrılır ve geçiş noktası ikili aramayla bulunur.

## İki işaretçi tekniği

İki işaretçi, dizinin farklı bölgelerini temsil eden iki indeks kullanır. İşaretçiler karşılıklı yaklaşabilir veya aynı yönde farklı hızlarla ilerleyebilir.

| Senaryo | Başlangıç | Hareket | Kullanım |
|---|---|---|---|
| Sıralı dizide hedef toplam | İki uç | Birbirine doğru | İkili toplam |
| Tekrarları kaldırma | Aynı taraf | Aynı yönde | Yerinde düzenleme |
| Palindrom kontrolü | İki uç | Birbirine doğru | Simetri testi |
| Kayan pencere | Aynı taraf | Koşula göre | Alt dizi problemleri |

Sıralı dizide toplamı hedefe eşit iki sayı bulalım:

```python
def find_pair(numbers, target):
    left, right = 0, len(numbers) - 1

    while left < right:
        current = numbers[left] + numbers[right]
        if current == target:
            return numbers[left], numbers[right]
        if current < target:
            left += 1
        else:
            right -= 1

    return None
```

Toplam küçükse sol işaretçiyi ilerletmek toplamı büyütür; büyükse sağ işaretçiyi geriletmek toplamı küçültür. Böylece $O(n^2)$ olabilecek tüm çiftleri denemek yerine yalnızca $O(n)$ adım kullanılır.

## Hangisini seçmeliyiz?

| Özellik | İkili arama | İki işaretçi |
|---|---|---|
| Temel gereksinim | Sıralılık veya monotonluk | Düzenli hareket kuralı |
| Tipik karmaşıklık | $O(\log n)$ | $O(n)$ |
| Ana fikir | Arama alanını yarıya indirmek | Gereksiz çiftleri elemek |

Bir problemde önce “Sonuçlar monoton mu?” diye sorulmalıdır; cevap evetse ikili arama güçlü bir adaydır. “İki sınırı hareket ettirerek seçenekleri güvenle eleyebilir miyim?” sorusunun cevabı evetse iki işaretçi düşünülmelidir. Asıl ustalık kodu ezberlemek değil, hangi hareketin neden güvenli olduğunu kanıtlamaktır.
