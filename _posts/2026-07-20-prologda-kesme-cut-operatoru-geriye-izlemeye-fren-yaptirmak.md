---
layout: post
title: "Prolog’da Kesme (Cut - !) Operatörü: Geriye İzlemeye Fren Yaptırmak"
math: true
categories: 
  - Program
tags: 
  - prolog
  - cut-operator
  - mantıksal-programlama
  - optimizasyon
---

Prolog dünyasında program yazmak biraz labirentte akıllı bir dedektif gezdirmeye benzer: Dedektif her kapıyı dener, çıkmaz sokak görünce geri döner ve başka bir kapıya yönelir. Bu mekanizmaya geriye izleme denir. Kesme operatörü, yani `!`, dedektife şunu söyler: Buraya kadar geldiysen artık önceki kapıları kurcalama, bu yoldan devam et. Doğru kullanıldığında arama uzayını küçültür, performansı artırır ve programın niyetini daha net ifade eder.
``

## Geriye izleme neden pahalıdır?

Prolog, bir hedefi kanıtlamak için kuralları sırayla dener. Her alternatif bir seçim noktası oluşturur. Eğer daha sonra başarısızlık yaşanırsa Prolog bu seçim noktalarına geri döner. Teorik olarak arama maliyeti kabaca dallanma faktörü ve derinliğe bağlıdır: $T = b^d$. Burada $b$ her adımda denenebilecek alternatif sayısı, $d$ ise arama derinliğidir. Cut, bazı seçim noktalarını silerek etkili dallanma faktörünü düşürür: $T_{cut} \lt T$.

| Kavram | Cut olmadan | Cut ile |
|---|---|---|
| Arama davranışı | Tüm alternatifleri dener | Belirli noktadan önceki alternatifleri atar |
| Performans | Gereksiz denemeler olabilir | Daha odaklı çalışır |
| Okunabilirlik | Mantıksal olarak daha saf | Niyet doğruysa daha net olabilir |
| Risk | Daha yavaş sonuç | Yanlış yerde kullanılırsa eksik sonuç |

## Cut nasıl çalışır?

`!` tek başına her zaman başarılı olan özel bir hedeftir. Fakat yan etkisi büyüktür: İçinde bulunduğu kural çağrıldığından beri oluşan seçim noktalarını keser. Yani Prolog artık o kuralın önceki alternatiflerine dönmez.

Aşağıdaki örnek, bir sayının işaretini sınıflandırır:

```prolog
% sign(Number, Result) sayının işaretini belirler.
sign(X, positive) :-
    X > 0, !.
sign(X, zero) :-
    X =:= 0, !.
sign(_, negative).
```

Burada `X > 0` doğruysa cut çalışır ve Prolog diğer kuralları denemez. Böylece pozitif bir sayı için `zero` veya `negative` seçenekleri gereksiz yere kontrol edilmez. Bu, özellikle büyük veri üzerinde tekrar tekrar çalışan sorgularda hissedilir bir kazanç sağlar.

## Yeşil cut ve kırmızı cut

Cut kullanırken en önemli ayrım yeşil cut ve kırmızı cut kavramlarıdır. Yeşil cut, programın mantıksal anlamını değiştirmez; sadece hızlandırır. Kırmızı cut ise hangi cevapların üretileceğini değiştirir. Kırmızı cut bazen bilinçli kullanılır, ama hataya çok açıktır.

| Tür | Mantıksal sonucu değiştirir mi? | Kullanım hissi | Örnek durum |
|---|---:|---|---|
| Yeşil cut | Hayır | Güvenli optimizasyon | Zaten dışlayıcı koşullar |
| Kırmızı cut | Evet | Dikkat ister | Varsayılan değer, ilk eşleşme |

Yeşil cut örneği:

```prolog
% max2(A, B, Max) iki sayıdan büyüğünü bulur.
max2(A, B, A) :-
    A >= B, !.
max2(_, B, B).
```

Eğer `A >= B` doğruysa ikinci kuralın denenmesine gerek yoktur. Koşullar birbirini mantıksal olarak dışladığı için cut sonucu bozmaz.

Kırmızı cut örneği ise daha sinsidir:

```prolog
% discount(User, Rate) kullanıcı indirimini belirler.
discount(vip, 30) :- !.
discount(student, 20) :- !.
discount(_, 0).
```

Bu kod ilk uygun rolü seçer. Eğer bir kullanıcı hem `vip` hem `student` gibi modellenmiş olsaydı, cut sonraki olasılıkları sustururdu. Bu istenen davranış olabilir, ama artık mantık değil öncelik sırası konuşuyordur.

## Cut ile if-then-else düşünmek

Prolog’da cut çoğu zaman koşullu karar ağacı kurmak için kullanılır. Fakat modern Prolog sistemlerinde `-> ;` yapısı niyeti daha okunur gösterebilir:

```prolog
% grade(Score, Grade) puana göre harf notu verir.
grade(S, a) :- S >= 90, !.
grade(S, b) :- S >= 75, !.
grade(S, c) :- S >= 60, !.
grade(_, f).
```

Bu örnekte not aralıkları yukarıdan aşağıya önceliklidir. Cut olmazsa Prolog gereksiz yere diğer kuralları da yoklamaya hazır bekler. Cut sayesinde her puan için ilk doğru aralık bulunduğunda arama durur.

## Ne zaman kullanmalı?

Cut, performans vitamini gibidir: doğru dozda faydalı, rastgele kullanılırsa kafa karıştırıcıdır. Önce programı saf mantıkla yazmak, sonra profil çıkarıp gereksiz geriye izlemeleri belirlemek iyi yaklaşımdır. Eğer koşullar matematiksel olarak dışlayıcıysa, örneğin $X > 0$, $X = 0$, $X < 0$ gibi, cut çoğunlukla güvenlidir.

Kısacası `!`, Prolog’un arama motoruna çekilen bilinçli bir settir. Her kapıyı denemek yerine doğru koridora girdikten sonra arkanıza bakmamayı sağlar. Ama unutmayın: Cut dedektifi hızlandırır, fakat yanlış kapıyı kilitlerseniz gerçeği de dışarıda bırakabilirsiniz.
