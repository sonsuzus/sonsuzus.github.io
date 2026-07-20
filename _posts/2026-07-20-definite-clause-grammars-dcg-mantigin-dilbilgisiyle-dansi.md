---
layout: post
title: "Definite Clause Grammars (DCG): Mantığın Dilbilgisiyle Dansı"
math: true
categories: 
  - Bilgi
tags: 
  - prolog
  - dcg
  - doğal dil işleme
  - mantıksal programlama
---

Bir cümleyi okurken beynimiz kelimeleri tek tek saymaz; özne nerede, yüklem ne söylüyor, hangi sözcük hangi görevi üstlenmiş gibi yapısal ilişkileri hızla kurar. Definite Clause Grammars, yani DCG, tam da bu sezgisel süreci mantıksal kurallara dökmenin zarif bir yoludur. Özellikle Prolog dünyasında DCG, insan dilini parçalamak, cümleleri çözümlemek ve sembolik doğal dil işleme sistemleri kurmak için küçük ama güçlü bir laboratuvar gibidir.
``
DCG fikrinin temeli şudur: Bir dil, rastgele kelime dizilerinden değil, kurallı yapılardan oluşur. Örneğin Türkçede basit bir cümle için kabaca $Cümle \rightarrow Özne\ Yüklem$ diyebiliriz. İngilizce örnekte ise klasik gösterim $S \rightarrow NP\ VP$ şeklindedir. Burada S cümleyi, NP isim öbeğini, VP fiil öbeğini temsil eder. DCG bu üretim kurallarını Prolog cümleciklerine çevirir ve böylece dilbilgisi, sorgulanabilir bir mantık programına dönüşür.

| Kavram | Klasik Gramer | DCG Yaklaşımı |
|---|---|---|
| Kural | $S \rightarrow NP\ VP$ | `s --> np, vp.` |
| Girdi | Kelime dizisi | Liste: `[the, cat, sleeps]` |
| Çıktı | Ayrıştırma ağacı | Mantıksal başarı veya yapı |
| Çalışma biçimi | Teorik üretim | Prolog ile arama ve eşleme |

DCG, görünüşte basit bir sözdizimi sunar. Aşağıdaki mini gramer, İngilizce küçük cümleleri tanır:

```prolog
sentence --> noun_phrase, verb_phrase.

noun_phrase --> determiner, noun.
verb_phrase --> verb.

determiner --> [the].
determiner --> [a].

noun --> [cat].
noun --> [dog].

verb --> [sleeps].
verb --> [runs].
```

Bu kodda `sentence --> noun_phrase, verb_phrase.` kuralı, bir cümlenin önce isim öbeği sonra fiil öbeğinden oluştuğunu söyler. Köşeli parantez içindeki ifadeler ise doğrudan tüketilecek kelimelerdir. Prolog tarafında şu sorgu çalıştırılabilir:

```prolog
?- phrase(sentence, [the, cat, sleeps]).
true.
```

Burada `phrase/2`, verilen kelime listesinin gramer tarafından tamamen ayrıştırılıp ayrıştırılamadığını kontrol eder. Eğer liste kurallara uyuyorsa sonuç `true` olur. Uymuyorsa Prolog başka kural yollarını dener; bulamazsa başarısız olur. Bu noktada DCG’nin güzelliği ortaya çıkar: Ayrıştırma, aslında mantıksal çıkarımdır.

İşin teorik tarafında DCG, bağlamdan bağımsız gramerlere oldukça yakındır; fakat Prolog’un değişkenleri ve hedefleri sayesinde daha esnektir. Örneğin yalnızca cümleyi tanımak değil, aynı zamanda bir ayrıştırma ağacı üretmek de mümkündür:

```prolog
sentence(s(NP, VP)) --> noun_phrase(NP), verb_phrase(VP).

noun_phrase(np(Det, Noun)) --> determiner(Det), noun(Noun).
verb_phrase(vp(Verb)) --> verb(Verb).

determiner(det(the)) --> [the].
noun(n(cat)) --> [cat].
verb(v(sleeps)) --> [sleeps].
```

Sorgu şöyle olur:

```prolog
?- phrase(sentence(Tree), [the, cat, sleeps]).
Tree = s(np(det(the), n(cat)), vp(v(sleeps))).
```

Bu ağaç, cümlenin yalnızca geçerli olduğunu değil, hangi parçalarının hangi dilbilgisel rolleri üstlendiğini de gösterir. Yani DCG, kelimeleri boncuk gibi dizmekten çok, onlardan anlamlı bir iskelet çıkarır.

| Özellik | Basit Regex | DCG |
|---|---|---|
| İç içe yapı | Zayıf | Güçlü |
| Dilbilgisel rol | Genellikle yok | Açıkça modellenir |
| Geri izleme | Sınırlı | Prolog ile doğal |
| Anlam bilgisi ekleme | Zor | Değişkenlerle kolay |

DCG’nin perde arkasında fark listeleri bulunur. Prolog, `s --> np, vp.` gibi bir kuralı aslında giriş ve kalan listeyi taşıyan bir yapıya çevirir. Mantıksal olarak amaç şuna benzer: $phrase(Gramer, Girdi, Kalan)$. Eğer `Kalan = []` ise tüm cümle başarıyla tüketilmiştir. Bu sayede ayrıştırma verimli ve deklaratif kalır.

Elbette insan dili karmaşıktır: ekler, belirsizlikler, devrik cümleler, çok anlamlılık ve bağlam gibi canavarlar pusudadır. Yine de DCG, bu canavarlarla savaşmak için harika bir başlangıç kılıcıdır. Küçük bir sözlük, birkaç kural ve Prolog’un arama mekanizmasıyla kendi mini ayrıştırıcınızı yazabilirsiniz. Sonuçta DCG bize şunu öğretir: Dil yalnızca kelimelerden değil, kurallardan; programlama ise yalnızca komutlardan değil, ilişkilerden oluşur.
