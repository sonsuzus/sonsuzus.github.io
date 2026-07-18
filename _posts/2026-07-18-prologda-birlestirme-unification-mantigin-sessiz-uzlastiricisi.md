---
layout: post
title: "Prolog’da Birleştirme (Unification): Mantığın Sessiz Uzlaştırıcısı"
math: true
categories: 
  - Bilgi
tags: 
  - Prolog
  - Mantıksal Programlama
  - Unification
---

Prolog yazarken bazen tek satırlık bir sorgu, sanki arka planda küçük bir dedektif ordusu çalışıyormuş gibi sonuç üretir. İşte bu dedektiflerin en çalışkanı birleştirme, yani unification sürecidir. Birleştirme; iki terimi, değişkeni veya yapıyı, mantıksal olarak aynı hale getirecek değer atamalarını bulma işlemidir. Prolog motoru bunu otomatik yapar ve çoğu zaman biz fark etmeden programın kaderini belirler.
``

Birleştirmeyi basit eşitlikten ayırmak önemlidir. Matematikte $2 + 3 = 5$ gibi bir eşitlik doğruluk kontrolüdür. Prolog’da ise `X = elma` dediğimizde çoğu zaman soru şu değildir: Bunlar zaten eşit mi? Asıl soru şudur: Bunları eşit yapmanın bir yolu var mı? Eğer varsa Prolog değişkenlere uygun değerleri bağlar.

Teorik olarak birleştirme, iki terim $T_1$ ve $T_2$ için bir yer değiştirme kümesi, yani $\sigma$ arar. Bu küme uygulandığında $T_1\sigma = T_2\sigma$ oluyorsa işlem başarılıdır. En iyi sonuç ise MGU, yani most general unifier olarak bilinir. Türkçesiyle en genel birleştirici. Bu, gereksiz kısıtlama koymadan iki ifadeyi eşitleyen en esnek çözümdür.

| Kavram | Ne yapar? | Prolog örneği |
|---|---|---|
| Eşleştirme | Yapıların uyumuna bakar | `kedi(X)` ile `kedi(mavis)` |
| Atama | Değişkeni değere bağlar | `X = mavis` |
| Birleştirme | İki tarafı aynı yapacak bağlamayı bulur | `anne(X)` ile `anne(ayse)` |
| Başarısızlık | Uyum mümkün değilse durur | `kedi(X)` ile `kopek(X)` |

Prolog terimleri üç ana grupta düşünülebilir: atomlar, değişkenler ve bileşik terimler. Atomlar sabit isimlerdir: `ali`, `kitap`, `mavi`. Değişkenler büyük harfle başlar: `X`, `Kisi`, `Sonuc`. Bileşik terimler ise functor ve argümanlardan oluşur: `seviyor(ali, kitap)` gibi. Birleştirme bu yapıları katman katman karşılaştırır.

```prolog
% Basit birleştirme örnekleri
?- X = elma.
% X = elma

?- kisi(ali, Yas) = kisi(ali, 30).
% Yas = 30

?- nokta(X, 5) = nokta(3, Y).
% X = 3, Y = 5
```

Bu örneklerde Prolog, yapıların adlarına ve argüman sayılarına bakar. `nokta(X, 5)` ile `nokta(3, Y)` aynı functor adına ve aynı arity değerine sahiptir. Bu yüzden argümanlar sırayla birleştirilir. Önce `X = 3`, sonra `5 = Y`; sonuçta iki değişken de uygun değerlere bağlanır.

| Karşılaştırma | Başarılı mı? | Neden |
|---|---:|---|
| `X = armut` | Evet | Değişken serbesttir |
| `ali = ali` | Evet | Aynı atomdur |
| `ali = veli` | Hayır | Farklı atomlardır |
| `f(X) = f(10)` | Evet | Aynı yapı, değişken bağlanır |
| `f(X) = g(X)` | Hayır | Functor adları farklıdır |
| `f(a,b) = f(a)` | Hayır | Argüman sayıları farklıdır |

Birleştirmenin en eğlenceli tarafı, sadece tek bir değişkeni değil, tüm yapıyı dönüştürebilmesidir. Mesela `aile(anne(X), baba(Y))` gibi iç içe terimler varsa Prolog en dıştan başlayıp içeri doğru ilerler. Her katmanda aynı soru sorulur: Bu iki şeyi aynı yapabilir miyim?

```prolog
% İç içe yapılarda birleştirme
?- aile(anne(X), baba(veli)) = aile(anne(ayse), baba(Y)).
% X = ayse,
% Y = veli
```

Burada `aile` yapısı eşleşir, sonra `anne(X)` ile `anne(ayse)` karşılaştırılır. Ardından `baba(veli)` ile `baba(Y)` birleştirilir. Sonuç, iki küçük bağlamanın birleşimidir: $\sigma = \{X/ayse, Y/veli\}$.

Bir noktaya dikkat: Prolog’daki `=` aritmetik hesap yapmaz, birleştirme yapar. Yani `X = 2 + 3` sorgusu `X` değişkenini `5` değerine değil, `2 + 3` terimine bağlar. Hesaplama için genellikle `is` kullanılır.

```prolog
?- X = 2 + 3.
% X = 2+3

?- X is 2 + 3.
% X = 5
```

| Operatör | Anlamı | Örnek sonuç |
|---|---|---|
| `=` | Birleştirme | `X = 2+3` |
| `is` | Aritmetik değerlendirme | `X is 5` |
| `==` | Aynı terim mi? | Bağlama yapmaz |
| `\=` | Birleştirilemez mi? | Uyum yoksa başarılı |

Özetle birleştirme, Prolog’un kalbidir. Kuralların çalışması, sorguların cevaplanması, değişkenlerin anlam kazanması hep bu süreçle olur. Eğer Prolog’u bir bulmaca oyunu gibi düşünürsek, unification parçaları masaya dizen, kenarlarını karşılaştıran ve uygun olanları sessizce birbirine kilitleyen mekanizmadır. Onu anladığınızda Prolog artık sihirli değil; mantıklı, sistemli ve oldukça keyifli görünmeye başlar.
