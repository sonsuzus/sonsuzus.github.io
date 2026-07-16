---
layout: post
title: "SQL ile Davranışsal Analiz: Kullanıcı Yolculuğunu Sorgularla Okumak"
math: true
categories: 
  - Bilgi
tags: 
  - SQL
  - Davranışsal Analiz
  - Kişiselleştirme
---

Bir kullanıcının uygulamada attığı her adım, aslında küçük bir dijital ayak izidir: ana sayfayı açar, kategori gezer, ürüne bakar, sepete ekler, bazen de sessizce kaybolur. SQL ile davranışsal analiz, bu izleri düzenleyip anlamlı bir hikâyeye dönüştürme sanatıdır. Amaç sadece rapor çıkarmak değil; kullanıcının niyetini tahmin edip ona doğru zamanda doğru içerik, kampanya veya öneriyi sunmaktır.
``
Davranışsal analizin temelinde olay tabanlı veri modeli vardır. Klasik kullanıcı tablosu bize kullanıcının kim olduğunu söylerken, olay tablosu ne yaptığını anlatır. Genellikle `user_id`, `event_name`, `platform`, `event_time`, `session_id` ve ek özelliklerin tutulduğu bir yapı kullanılır. Burada kritik nokta zamandır; çünkü davranış, sıralama olmadan sadece dağınık noktalar kümesidir.

Matematiksel olarak kullanıcı yolculuğunu bir dizi gibi düşünebiliriz: $J_u = [e_1, e_2, e_3, ..., e_n]$. Burada $u$ kullanıcıyı, $e_i$ ise i. olayı temsil eder. Eğer kullanıcıların bir sonraki adımını tahmin etmek istiyorsak, basitçe şu olasılıkla ilgileniriz: $P(e_{i+1} \mid e_i)$. Yani kullanıcı ürün detayına baktıysa, bir sonraki adımının sepete ekleme olma ihtimali nedir?

| Analiz Türü | Sorduğu Soru | SQL Tekniği |
|---|---|---|
| Funnel analizi | Kullanıcılar hangi adımda düşüyor? | CTE, COUNT DISTINCT |
| Sıralı davranış | Bir olaydan sonra ne geliyor? | LAG, LEAD |
| Segmentasyon | Benzer kullanıcılar kimler? | CASE WHEN, GROUP BY |
| Kişiselleştirme | Kime ne önerelim? | Skorlama, JOIN |

Örneğin farklı platformlarda ürün görüntüleme sonrası sepete ekleme oranını ölçmek isteyelim. Aşağıdaki sorgu, kullanıcıların olay sırasını inceler ve `view_product` olayından sonra gelen adımı yakalar:

```sql
WITH ordered_events AS (
  SELECT
    user_id,
    platform,
    event_name,
    event_time,
    LEAD(event_name) OVER (
      PARTITION BY user_id, platform
      ORDER BY event_time
    ) AS next_event
  FROM events
  WHERE event_time >= CURRENT_DATE - INTERVAL '30 day'
), transitions AS (
  SELECT
    platform,
    COUNT(*) AS product_views,
    SUM(CASE WHEN next_event = 'add_to_cart' THEN 1 ELSE 0 END) AS cart_adds
  FROM ordered_events
  WHERE event_name = 'view_product'
  GROUP BY platform
)
SELECT
  platform,
  product_views,
  cart_adds,
  ROUND(cart_adds * 100.0 / NULLIF(product_views, 0), 2) AS conversion_rate
FROM transitions;
```

Bu sorgu bize örneğin mobilde ürün görenlerin daha fazla sepete eklediğini, webde ise kullanıcıların kararsız kaldığını gösterebilir. Böylece web kullanıcılarına karşılaştırma kartları, mobil kullanıcılara hızlı ödeme butonu sunmak mantıklı hale gelir.

Kişiselleştirme tarafında ise davranışları puanlamak çok işe yarar. Basit bir skor formülü şöyle kurulabilir:

$$score = 5 \times cart + 3 \times view + 2 \times favorite - 4 \times bounce$$

Bu formül mükemmel olmak zorunda değildir; başlangıç için sezgisel olması yeterlidir. SQL ile bunu hesaplayabiliriz:

```sql
SELECT
  user_id,
  category_id,
  SUM(
    CASE
      WHEN event_name = 'add_to_cart' THEN 5
      WHEN event_name = 'view_product' THEN 3
      WHEN event_name = 'favorite' THEN 2
      WHEN event_name = 'bounce' THEN -4
      ELSE 0
    END
  ) AS interest_score
FROM events
WHERE event_time >= CURRENT_DATE - INTERVAL '14 day'
GROUP BY user_id, category_id
HAVING SUM(
  CASE
    WHEN event_name = 'add_to_cart' THEN 5
    WHEN event_name = 'view_product' THEN 3
    WHEN event_name = 'favorite' THEN 2
    WHEN event_name = 'bounce' THEN -4
    ELSE 0
  END
) > 0;
```

Bu çıktıyı içerik tablosuyla birleştirerek kullanıcılara en yüksek skorlu kategorilerden öneriler gösterebilirsiniz. Mesela oyun laptoplarına bakan ama satın almayan kullanıcıya inceleme videosu, sepete ekleyip çıkan kullanıcıya sınırlı süreli indirim sunulabilir.

| Kullanıcı Davranışı | Olası Niyet | Önerilen İçerik |
|---|---|---|
| Çok görüntüleme, sepet yok | Araştırıyor | Rehber yazı, karşılaştırma |
| Sepete ekleme, satın alma yok | Tereddüt ediyor | Kupon, ücretsiz kargo |
| Favori ekleme | İlgileniyor | Stok bildirimi |
| Hızlı çıkış | Uyuşmadı | Alternatif kategori |

Elbette bu analizlerde dikkat edilmesi gereken iki büyük konu vardır: veri kalitesi ve gizlilik. Aynı kullanıcının farklı cihazlarda parçalanması, saat dilimi hataları veya yanlış event isimleri sonuçları bozabilir. Ayrıca kişiselleştirme yaparken kullanıcı rızası, anonimleştirme ve veri minimizasyonu unutulmamalıdır.

Sonuç olarak SQL, sadece veri çekme dili değil; kullanıcı davranışlarını anlamak için güçlü bir mercek gibidir. Doğru modellenmiş olay verisi, pencere fonksiyonları ve akıllı skorlama ile platformlarınız kullanıcıya ‘beni anlıyor’ hissi verebilir. Ve kabul edelim: İyi yazılmış bir SQL sorgusu, bazen en havalı yapay zekâ modelinden bile daha hızlı değer üretir.
