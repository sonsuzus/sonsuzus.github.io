---
layout: post
title: "SQL ve Tam Metin Arama: Forumlar İçin Mini Arama Motoru Mantığı"
math: true
categories: 
  - Bilgi
tags: 
  - SQL
  - Full-Text Search
  - Veritabanı
  - Arama Motoru
---

Bir forumda yüz binlerce tartışma, bir blogda yıllarca birikmiş yazılar olduğunu düşünün. Kullanıcı arama kutusuna sadece iki kelime yazar: SQL indeks. Beklentisi nettir: saniyeler değil, milisaniyeler içinde en alakalı sonuçlar gelsin. İşte SQL tabanlı tam metin arama, klasik LIKE sorgularının el feneriyle mağara gezmesine benzeyen dünyasından çıkıp, elimize projektör ve harita verdiğimiz yerdir.
``

## Neden LIKE Yetmez?

Klasik arama genellikle şöyle başlar:

```sql
SELECT *
FROM posts
WHERE content LIKE '%veritabanı%';
```

Bu sorgu küçük tabloda sevimlidir, ama milyon satırlık forumda kahve molası ister. Çünkü başında joker karakter olan `%kelime%` ifadesi çoğu durumda normal indeksi verimli kullanamaz. Veritabanı satır satır gezip metnin içinde kelime arar. Bu işlem yaklaşık olarak $O(n)$ maliyetlidir; yani veri büyüdükçe bekleme süresi de büyür.

Tam metin arama ise metni önceden parçalar, kelimeleri işler ve ters indeks denilen bir yapı kurar. Ters indeks mantığı basittir: kelimeden belgeye giden bir harita oluşturulur. Yani veritabanı artık belge içinde kelime aramaz; kelimenin geçtiği belgeleri doğrudan bulur.

| Yaklaşım | Nasıl Çalışır | Avantaj | Dezavantaj |
|---|---|---|---|
| LIKE | Metin içinde desen arar | Basit ve her yerde çalışır | Büyük veride yavaş |
| B-Tree indeks | Tam veya önek eşleşmelerde iyidir | ID, tarih, kategori için hızlı | Serbest metin için sınırlı |
| Full-Text Search | Kelime tabanlı indeks kullanır | Alaka sıralaması yapabilir | Dil ve yapılandırma ister |

## Arama Motoru Mantığının Temeli

Tam metin aramada ilk adım tokenization, yani metni anlamlı parçalara ayırmaktır. Örneğin Kullanıcılar hızlı arama istiyor cümlesi kullanıcılar, hızlı, arama, istiyor gibi kelimelere bölünür. Ardından stop word temizliği yapılabilir. Türkçede ve, ile, bir gibi çok sık geçen ama anlam değeri düşük kelimeler atılabilir.

Sonra stemming veya lemmatization devreye girer. Amaç arama, aramak, arandı gibi varyasyonları ortak köke yaklaştırmaktır. PostgreSQL gibi sistemlerde dil yapılandırması bu yüzden önemlidir.

Alaka puanı genellikle kelime sıklığına ve nadirliğine dayanır. Basit bir model şöyle düşünülebilir:

$score = tf * log(N / df)$

Burada $tf$ kelimenin ilgili belgede kaç kez geçtiğini, $N$ toplam belge sayısını, $df$ ise kelimenin kaç belgede bulunduğunu gösterir. Yani nadir ama aranan kelimeler daha değerli hale gelir. Forumda veritabanı kelimesi binlerce kez geçebilir, ama gin index daha az yerde geçiyorsa daha ayırt edici olabilir.

## PostgreSQL ile Örnek Kurgu

PostgreSQL, tam metin arama konusunda oldukça güçlüdür. `tsvector` metnin indekslenmiş halini, `tsquery` ise arama ifadesini temsil eder.

```sql
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    search_vector TSVECTOR
);
```

Bu tabloda `search_vector`, başlık ve içerikten üretilmiş arama alanı olarak kullanılabilir. Başlığa daha fazla ağırlık vermek de mümkündür:

```sql
UPDATE posts
SET search_vector =
    setweight(to_tsvector('turkish', title), 'A') ||
    setweight(to_tsvector('turkish', content), 'B');
```

Burada başlık A ağırlığında, içerik B ağırlığında değerlendirilir. Böylece aranan kelime başlıkta geçiyorsa sonuç daha yukarı çıkabilir. Arama için ise şöyle bir sorgu yazılabilir:

```sql
SELECT id, title,
       ts_rank(search_vector, plainto_tsquery('turkish', 'sql indeks')) AS rank
FROM posts
WHERE search_vector @@ plainto_tsquery('turkish', 'sql indeks')
ORDER BY rank DESC
LIMIT 10;
```

Bu sorgu, kullanıcının yazdığı ifadeyi arama sorgusuna dönüştürür, eşleşen kayıtları bulur ve alaka puanına göre sıralar. Yani artık sadece bulmakla kalmayız; en mantıklı sonuçları en üste taşırız.

Performans için GIN indeksi eklemek gerekir:

```sql
CREATE INDEX posts_search_idx
ON posts
USING GIN (search_vector);
```

GIN indeksi, çok değerli metin alanları için ters indeks mantığını verimli uygular. Büyük forumlarda fark dramatik olabilir.

## MySQL ve Diğerleri

MySQL tarafında da `FULLTEXT` indeksi kullanılabilir:

```sql
ALTER TABLE posts
ADD FULLTEXT INDEX post_fulltext_idx (title, content);

SELECT id, title,
       MATCH(title, content) AGAINST('sql indeks' IN NATURAL LANGUAGE MODE) AS score
FROM posts
WHERE MATCH(title, content) AGAINST('sql indeks' IN NATURAL LANGUAGE MODE)
ORDER BY score DESC;
```

| Özellik | PostgreSQL | MySQL | Elasticsearch |
|---|---|---|---|
| SQL içinde kullanım | Çok güçlü | Kolay | Harici servis |
| Dil işleme | Esnek | Orta | Çok gelişmiş |
| Ölçeklenebilirlik | İyi | İyi | Çok yüksek |
| Kurulum karmaşıklığı | Orta | Düşük | Daha yüksek |

## Pratik Tasarım İpuçları

Tam metin aramayı gerçek bir üründe kullanırken başlık, etiket ve içerik aynı öneme sahip olmamalıdır. Başlıkta geçen kelime genellikle daha değerlidir. Ayrıca arama kutusuna yazılan metni doğrudan karmaşık sorguya çevirmek yerine güvenli fonksiyonlar kullanmak gerekir.

Bir diğer önemli konu güncellemedir. Yazı değiştiğinde `search_vector` da güncellenmelidir. Bunun için trigger kullanılabilir veya uygulama katmanında kayıt güncellenirken arama alanı da yeniden oluşturulabilir.

Sonuç olarak SQL ile tam metin arama, küçük bir özellik gibi görünse de kullanıcı deneyimini doğrudan değiştirir. Doğru indeks, doğru ağırlıklandırma ve iyi bir alaka puanı ile forumunuz artık dev bir metin çöplüğü değil, kullanıcıların aradığını hızla bulduğu akıllı bir bilgi haritası olur.
