---
layout: post
title: "Dinamik Programlamanın Kalbi: Alt Problemler, Durumlar ve Memoization"
math: true
categories: 
  - Bilgi
tags: 
  - dinamik programlama
  - algoritmalar
  - memoization
---

Bazı algoritmalar aynı hesabı tekrar tekrar yaparak işlemciyi küçük bir hamster çarkına sokar. Dinamik programlama, bu gereksiz tekrarları fark edip sonuçları saklayan güçlü bir problem çözme yaklaşımıdır. Temel fikir; büyük bir problemi daha küçük alt problemlere ayırmak, her alt problemi doğru biçimde temsil eden durumları tanımlamak ve hesaplanan sonuçları yeniden kullanmaktır.

``

## Dinamik programlama ne zaman kullanılır?

Bir problemi parçalara bölmek tek başına dinamik programlama değildir. Yaklaşımın etkili olabilmesi için genellikle iki özellik aranır:

1. **Örtüşen alt problemler:** Aynı alt problem farklı hesaplama yollarında tekrar ortaya çıkar.
2. **Optimal alt yapı:** Büyük problemin en iyi çözümü, alt problemlerin en iyi çözümlerinden oluşturulabilir.

Örneğin Fibonacci dizisi şu bağıntıyla tanımlanır:

$$F(n) = F(n-1) + F(n-2)$$

ve başlangıç durumları şöyledir:

$$F(0)=0, \qquad F(1)=1$$

Saf özyinelemeli çözümde `F(n-2)` gibi değerler birçok kez hesaplanır. Çağrı ağacı büyüdükçe çalışma süresi yaklaşık $O(2^n)$ seviyesine çıkar. Dinamik programlama sayesinde her değer yalnızca bir kez hesaplanarak süre $O(n)$ olur.

## Birinci adım: Alt problemleri belirlemek

Büyük problemin daha küçük sürümleri alt problem olarak seçilir. Fibonacci örneğinde “`n` sayısının Fibonacci değerini bulmak” ana problemse `F(n-1)` ve `F(n-2)` onun alt problemleridir.

Daha gerçekçi bir örnek olan sırt çantası probleminde ise alt problem yalnızca kaç eşyanın incelendiğiyle açıklanamaz. Kalan kapasite de sonucu etkiler. Bu nedenle alt problemleri tanımlarken gelecekteki kararları etkileyen bütün bilgileri korumak gerekir.

## İkinci adım: Durumu tanımlamak

**Durum**, bir alt problemi benzersiz biçimde ifade eden en küçük bilgi kümesidir. İyi durum tanımı, dinamik programlamanın en kritik bölümüdür.

Sırt çantası problemi için şu durum kullanılabilir:

$$DP(i, c) = \text{İlk } i \text{ eşya ve } c \text{ kapasiteyle elde edilen en yüksek değer}$$

Burada `i` hangi eşyalara bakabildiğimizi, `c` ise kalan kapasiteyi belirtir. Gereksiz bilgi eklemek durum sayısını artırır; eksik bilgi kullanmak ise farklı alt problemleri yanlışlıkla aynı kabul eder.

| Kavram | Sorduğu soru | Fibonacci örneği |
|---|---|---|
| Alt problem | Daha küçük hangi problemi çözüyorum? | `F(n-1)` |
| Durum | Alt problemi hangi bilgiler tanımlar? | `n` |
| Geçiş | Sonraki sonuç nasıl üretilir? | `F(n-1) + F(n-2)` |
| Başlangıç | Hesaplamayı nerede durdururum? | `F(0)` ve `F(1)` |

## Üçüncü adım: Memoization ile tekrarları önlemek

Memoization, yukarıdan aşağıya çalışan özyinelemeli çözümün sonuçlarını bir önbellekte saklar. Fonksiyon aynı durumla yeniden çağrıldığında hesap yapmak yerine kayıtlı sonuç döndürülür.

```python
def fibonacci(n, memo=None):
    # Sözlük, daha önce çözülen durumların sonuçlarını saklar.
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

print(fibonacci(40))
```

Bu kodda sözlüğün anahtarı durumu, yani `n` değerini temsil eder. Her durum bir kez çözüldüğü için toplam $n+1$ farklı durum bulunur. Her durumdaki işlem sabit zamanlı olduğundan karmaşıklık $O(n)$ zaman ve $O(n)$ bellek olur.

## Memoization ve tabulation farkı

| Özellik | Memoization | Tabulation |
|---|---|---|
| Yön | Yukarıdan aşağıya | Aşağıdan yukarıya |
| Yapı | Özyineleme | Döngü |
| Hesaplanan durumlar | Yalnızca ihtiyaç duyulanlar | Genellikle tüm tablo |
| Risk | Çağrı yığını taşabilir | Sıralama hatası yapılabilir |

Dinamik programlama ezberlenecek bir kod kalıbı değil, düşünme disiplinidir: Önce alt problemleri keşfet, sonra durumu mümkün olduğunca sade tanımla, geçiş bağıntısını kur ve tekrarları saklayarak ortadan kaldır. Bu adımlar oturduğunda korkutucu görünen pek çok algoritma, düzenli doldurulan bir tabloya dönüşür.
