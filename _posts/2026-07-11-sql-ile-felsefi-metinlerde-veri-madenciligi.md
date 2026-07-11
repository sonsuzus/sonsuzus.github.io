---
layout: post
title: "SQL ile Felsefi Metinlerde Veri Madenciliği"
math: true
categories: 
  - Program
tags: 
  - SQL
  - Veri Madenciliği
  - Doğal Dil İşleme
---

Felsefi metinler bazen bir veritabanı gibi davranır: kavramlar tablolar, alıntılar ilişkiler, kelimeler de satırlar gibidir. Platon’dan Kant’a, İbn Sînâ’dan Nietzsche’ye uzanan devasa bir külliyatı SQL ile sorguladığınızda yalnızca kaç kez akıl kelimesi geçtiğini değil, hangi kökten gelen kelimelerin hangi düşünürlerde birlikte yoğunlaştığını da görebilirsiniz.

Bu işin teorik temeli üç katmandan oluşur: ilişkisel model, dilsel ön işleme ve semantik yakınlık. İlişkisel modelde her metin; yazar, eser, bölüm, cümle ve token gibi parçalara ayrılır. Dilsel ön işlemede kelimeler küçük harfe çevrilir, noktalama temizlenir, kök veya lemma bulunur. Semantik yakınlıkta ise kelimelerin aynı bağlamlarda görünme sıklığı ölçülür. Basit fikir şudur: İki kavram benzer cümlelerde sık görünüyorsa anlam uzayında birbirine yakındır.
``

Matematiksel olarak birlikte görünme oranını şöyle düşünebiliriz: $P(a,b)=\frac{count(a,b)}{N}$, burada $count(a,b)$ iki kelimenin aynı pencere içinde kaç kez geçtiğini, $N$ ise toplam pencere sayısını gösterir. Daha kullanışlı bir ölçü olan PMI ise $PMI(a,b)=\log\frac{P(a,b)}{P(a)P(b)}$ formülüyle beklenenden güçlü ilişkileri yakalar. Örneğin töz ve nitelik sıradan sıklıkta görünse bile birlikte görünmeleri beklenenden fazlaysa felsefi açıdan anlamlı bir bağ oluşur.

| Yaklaşım | Ne Ölçer? | Avantaj | Risk |
|---|---|---|---|
| Kelime sıklığı | Bir terimin kaç kez geçtiği | Hızlı ve basit | Bağlamı kaçırır |
| Kök analizi | Aynı kökten türeyen biçimler | Etimolojik iz sürer | Hatalı kök eşleşebilir |
| Birlikte görünme | Kavramların yakınlığı | Semantik ağ kurar | Uzun metinlerde gürültü üretir |
| PMI | Beklenmedik güçlü bağlar | Derin ilişkileri gösterir | Nadir kelimeleri abartabilir |

Örnek bir şema şöyle tasarlanabilir: `authors`, `works`, `sentences`, `tokens`, `roots` ve `co_occurrences`. Token tablosu her kelimeyi satır olarak tutar; root tablosu ise etimolojik veya morfolojik kökeni saklar. Böylece hem metinsel hem de tarihsel sorgular yazabiliriz.

```sql
-- Aynı kökten gelen kelimelerin filozoflara göre dağılımı
SELECT
  a.name AS philosopher,
  r.root_text AS root,
  COUNT(*) AS usage_count
FROM tokens t
JOIN sentences s ON s.id = t.sentence_id
JOIN works w ON w.id = s.work_id
JOIN authors a ON a.id = w.author_id
JOIN roots r ON r.id = t.root_id
WHERE r.root_text IN ('logos', 'ratio', 'nous')
GROUP BY a.name, r.root_text
ORDER BY usage_count DESC;
```

Bu sorgu, farklı dillerde akıl, söz, düzen veya ilke anlamlarına yaklaşan kökleri filozof bazında karşılaştırır. Elbette burada felsefi yorum SQL’den çıkmaz; SQL yalnızca izleri görünür kılar. Yorum, araştırmacının tarihsel ve kavramsal bilgisinde başlar.

Daha heyecanlı kısım semantik ağdır. Cümle içinde beş kelimelik bir pencere düşünelim. Eğer özgürlük ile zorunluluk aynı pencerede sık görülüyorsa aralarında kenar oluşur. Aşağıdaki sorgu bu ilişkiyi kabaca çıkarır:

```sql
-- Aynı cümlede geçen kavram çiftlerini bulma
SELECT
  t1.lemma AS concept_a,
  t2.lemma AS concept_b,
  COUNT(*) AS co_count
FROM tokens t1
JOIN tokens t2
  ON t1.sentence_id = t2.sentence_id
 AND t1.position < t2.position
 AND ABS(t1.position - t2.position) <= 5
WHERE t1.pos IN ('NOUN', 'ADJ')
  AND t2.pos IN ('NOUN', 'ADJ')
  AND t1.lemma <> t2.lemma
GROUP BY t1.lemma, t2.lemma
HAVING COUNT(*) >= 10
ORDER BY co_count DESC;
```

Burada `position` kelimenin cümledeki sırasıdır. `ABS` ile pencere sınırı belirlenir. Böylece bütün metni torbaya atmak yerine yakın bağlamı dikkate alırız. Bu, Aristoteles’te form-madde çiftini, Spinoza’da töz-kip ilişkisini, Kant’ta deneyim-akıl gerilimini daha görünür hâle getirebilir.

Performans için indeksler şarttır. Devasa metinlerde `sentence_id`, `lemma`, `root_id` ve `position` alanlarına indeks eklemek sorgu süresini dramatik biçimde azaltır. Ayrıca sık kullanılan sonuçlar materialized view olarak saklanabilir.

```sql
CREATE INDEX idx_tokens_sentence_position
ON tokens(sentence_id, position);

CREATE MATERIALIZED VIEW concept_edges AS
SELECT t1.lemma AS source, t2.lemma AS target, COUNT(*) AS weight
FROM tokens t1
JOIN tokens t2 ON t1.sentence_id = t2.sentence_id
WHERE t1.position < t2.position
GROUP BY t1.lemma, t2.lemma;
```

Sonuçta SQL, felsefeyi otomatikleştiren sihirli bir değnek değildir; daha çok karanlık bir arşivde güçlü bir el feneridir. Hangi kavramların hangi köklerden beslendiğini, hangi eserlerde yoğunlaştığını ve hangi semantik komşularla gezdiğini gösterir. Filozoflar argüman kurar, SQL ise bu argümanların metin içindeki ayak izlerini sabırla sayar.
