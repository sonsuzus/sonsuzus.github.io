---
layout: post
title: "SQL ile Mitolojik Soy Ağaçları: Tanrıları, Kahramanları ve Ejderhaları Modelle"
math: true
categories: 
  - Proje
tags: 
  - SQL
  - veritabanı tasarımı
  - mitoloji
  - recursive CTE
---

Mitoloji, veritabanı tasarımcıları için adeta boss seviyesi bir problemdir: Zeus hem baba, hem eş, hem de bazen kuğu kılığına giren kaotik bir kayıt üreticisidir. İskandinavlarda Loki’nin aile ilişkileri türler arası sınırları zorlar; Türk destanlarında soy, kutsal kurt ya da göksel kökenlerle birleşir. Bu yüzden antik tanrılar ve destan karakterleri için bir SQL soy ağacı kurmak, sadece tablo açmak değil, belirsizlikleri, kültürel kaynakları ve çoklu ilişki tiplerini modellemektir.
``

Temel fikir şudur: Mitolojik karakterleri düğüm, aralarındaki bağları kenar kabul ederiz. Yani elimizde küçük bir grafik vardır: $G=(V,E)$. Burada $V$ kişiler, tanrılar, canavarlar veya yarı tanrılar; $E$ ise ebeveynlik, eşlik, kardeşlik, yaratılma ya da lanetlenme gibi ilişkilerdir. Klasik soy ağacında ilişki genelde $parent \rightarrow child$ biçimindedir; fakat mitolojide aynı varlık birden fazla kaynağa göre farklı ebeveynlere sahip olabilir. Bu nedenle kaynak bilgisini ayrı tutmak altın kuraldır.

| Modelleme Yaklaşımı | Avantaj | Dezavantaj | Mitolojiye Uygunluk |
|---|---|---|---|
| Tek tabloda anne_id, baba_id | Basit ve hızlı | Tanrısal doğum, belirsizlik ve çoklu kaynak zayıf kalır | Düşük |
| İlişki tablosu | Esnek, çoklu ebeveyn destekler | Sorgular biraz karmaşıklaşır | Yüksek |
| Grafik veritabanı | Doğal akrabalık gezintisi | SQL ekosisteminden uzaklaşabilir | Çok yüksek |

SQL tarafında ilişkisel ama grafik tadında bir şema kurabiliriz:

```sql
CREATE TABLE beings (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  culture TEXT NOT NULL,
  being_type TEXT CHECK (being_type IN ('god','human','hero','monster','titan','spirit')),
  notes TEXT
);

CREATE TABLE sources (
  id INTEGER PRIMARY KEY,
  title TEXT NOT NULL,
  tradition TEXT,
  reliability_score NUMERIC CHECK (reliability_score BETWEEN 0 AND 1)
);

CREATE TABLE relationships (
  id INTEGER PRIMARY KEY,
  from_id INTEGER REFERENCES beings(id),
  to_id INTEGER REFERENCES beings(id),
  relation_type TEXT NOT NULL,
  source_id INTEGER REFERENCES sources(id),
  certainty NUMERIC CHECK (certainty BETWEEN 0 AND 1)
);
```

Bu yapıda `relationships` tablosu ana sahnedir. Örneğin `from_id = Zeus`, `to_id = Athena`, `relation_type = parent` diyebiliriz. Ancak Athena’nın doğumu sıradan olmadığı için `notes` veya ayrı bir olay tablosu ile kafadan doğma gibi anlatıları saklayabiliriz. Matematiksel olarak her ilişkinin ağırlığı $w \in [0,1]$ olabilir; burada $w$ kesinlik değeridir. Böylece tartışmalı soylar için veritabanı dogmatik davranmaz.

Örnek veri ekleyelim:

```sql
INSERT INTO beings VALUES
(1, 'Zeus', 'Greek', 'god', 'Olympian sky god'),
(2, 'Athena', 'Greek', 'god', 'Born from Zeus according to common tradition'),
(3, 'Odin', 'Norse', 'god', 'All-father figure'),
(4, 'Thor', 'Norse', 'god', 'Thunder god'),
(5, 'Loki', 'Norse', 'god', 'Trickster with complex kinship');

INSERT INTO sources VALUES
(1, 'Theogony', 'Greek', 0.90),
(2, 'Poetic Edda', 'Norse', 0.85);

INSERT INTO relationships VALUES
(1, 1, 2, 'parent', 1, 0.95),
(2, 3, 4, 'parent', 2, 0.90),
(3, 5, 4, 'ally', 2, 0.60);
```

Asıl eğlence recursive CTE ile başlar. Bir karakterin tüm atalarını bulmak için:

```sql
WITH RECURSIVE ancestry(depth, ancestor_id, descendant_id) AS (
  SELECT 1, from_id, to_id
  FROM relationships
  WHERE relation_type = 'parent' AND to_id = 2

  UNION ALL

  SELECT a.depth + 1, r.from_id, a.descendant_id
  FROM relationships r
  JOIN ancestry a ON r.to_id = a.ancestor_id
  WHERE r.relation_type = 'parent'
)
SELECT depth, b.name AS ancestor
FROM ancestry
JOIN beings b ON b.id = ancestry.ancestor_id;
```

Bu sorgu Athena’nın ebeveyninden başlayıp yukarı doğru tırmanır. `depth` değeri nesil uzaklığını gösterir: $depth=1$ ebeveyn, $depth=2$ büyükanne veya büyükbaba gibi düşünülebilir. Eğer döngü ihtimali varsa, yani bir mitolojik anlatıda karakter kendi soyuna garip şekilde bağlanıyorsa, ziyaret edilen düğümleri takip eden ek bir kolon kullanmak gerekir.

| İlişki Türü | Yönlü mü? | Örnek | Sorgu Notu |
|---|---:|---|---|
| parent | Evet | Odin → Thor | Atalık sorgularında kullanılır |
| spouse | Genelde çift yönlü | Hera ↔ Zeus | İki kayıt veya normalize edilmiş çift gerekir |
| sibling | Türetilmiş olabilir | Apollo ↔ Artemis | Aynı ebeveynden hesaplanabilir |
| created_by | Evet | İnsan → Prometheus | Soy değil, yaratılış bağıdır |

Kültürler arası bağlantı kurarken aynı karakterin varyantlarını da düşünmeliyiz. Roma Jüpiter’i ile Yunan Zeus’u birebir aynı kayıt mı olmalı, yoksa `equivalent_to` ilişkisiyle mi bağlanmalı? Genelde ikinci yaklaşım daha sağlıklıdır; çünkü $Zeus \neq Jupiter$ demek tarihsel bağlamı korur, ama `equivalent_to` ile benzerliği sorgulanabilir yapar.

Sonuçta bu proje, SQL öğrenmek için harika bir oyun alanıdır. Normalizasyon, yabancı anahtarlar, çoktan çoğa ilişkiler, recursive sorgular ve belirsizlik modelleme aynı kazanda kaynar. Üstelik test verisi sıkıcı müşteri tabloları değil; titanlar, yarı tanrılar, devler ve kader tanrıçalarıdır. Bir sonraki adım olarak ilişkilere tarihsel dönem, coğrafya ve anlatı varyantı ekleyip kendi mitolojik bilgi grafiğinizi küçük bir dijital Olimpos’a dönüştürebilirsiniz.
