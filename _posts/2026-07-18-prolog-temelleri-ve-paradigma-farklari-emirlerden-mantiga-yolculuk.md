---
layout: post
title: "Prolog Temelleri ve Paradigma Farkları: Emirlerden Mantığa Yolculuk"
math: true
categories: 
  - Bilgi
tags: 
  - Prolog
  - Mantıksal Programlama
  - Programlama Paradigmaları
---

Bir emirsel dilde bilgisayara adım adım ne yapacağını söylersin; Prolog gibi mantıksal bir dilde ise evrenin kurallarını tarif eder, sonra ona soru sorarsın. Bu küçük fark, programlama zihniyetinde büyük bir deprem yaratır: döngülerden, sayaçlardan ve durum güncellemelerinden uzaklaşıp olgular, kurallar ve çıkarımlar dünyasına gireriz.
``
Prolog, adını Programming in Logic ifadesinden alır ve temel fikri oldukça şiirseldir: Program, çalıştırılacak komut listesi değil, doğru kabul edilen bilgilerin ve bu bilgilerden türetilebilecek sonuçların bir kümesidir. Matematiksel olarak düşünürsek Prolog programını kabaca şöyle görebiliriz: $Program = Olgular + Kurallar$, çalıştırma ise $Sorgu \Rightarrow Kanıt arama$ sürecidir.

Emirsel dillerde geliştirici genellikle belleğin zaman içindeki durumunu yönetir. Değişkenler atanır, döngüler kurulur, koşullar dallanır. Mantıksal programlamada ise amaç, sonucu hangi adımlarla bulacağını tarif etmekten çok, sonucun hangi mantıksal koşullarda doğru olacağını belirtmektir. Bu yüzden Prolog kodu bazen programdan çok küçük bir bilgi tabanı gibi görünür.

| Özellik | Emirsel Yaklaşım | Mantıksal Yaklaşım |
|---|---|---|
| Temel soru | Nasıl yapılır? | Ne doğrudur? |
| Ana yapı | Komut, atama, döngü | Olgu, kural, sorgu |
| Kontrol | Programcı akışı belirler | Çıkarım motoru arar |
| Değişken | Bellekte değer tutar | Mantıksal bilinmeyendir |
| Hata tipi | Yanlış algoritma adımı | Eksik veya hatalı bilgi modeli |

Prolog’un en küçük yapı taşı olgudur. Olgu, dünyaya dair doğru kabul edilen basit bir cümledir. Örneğin aşağıdaki bilgi tabanı aile ilişkilerini tanımlar:

```prolog
% Olgular: Bunlar doğru kabul edilir.
ebeveyn(ayse, mehmet).
ebeveyn(mehmet, zeynep).
ebeveyn(zeynep, deniz).

% Kural: X, Y'nin atasıdır; eğer X, Y'nin ebeveyniyse.
ata(X, Y) :- ebeveyn(X, Y).

% Özyinelemeli kural: X, Z'nin atasıdır; eğer X, Y'nin ebeveyni
% ve Y de Z'nin atasıysa.
ata(X, Z) :- ebeveyn(X, Y), ata(Y, Z).
```

Burada `ata(X, Y)` klasik anlamda bir fonksiyon değildir. Daha çok, doğru olup olmadığı araştırılan bir ilişkidir. Prolog’a `ata(ayse, deniz).` diye sorduğumuzda motor, olguları ve kuralları kullanarak bir kanıt arar. Bu süreçte iki temel mekanizma devrededir: eşleme ve geri izleme.

Eşleme, Prolog’un iki ifadeyi birbirine uygun hale getirmesidir. Örneğin `ebeveyn(ayse, Kim)` sorgusunda `Kim = mehmet` sonucu bulunur. Geri izleme ise bir çözümden sonra başka çözüm var mı diye alternatif yolları denemesidir. Yani Prolog, küçük bir dedektif gibi ipuçlarını takip eder; çıkmaz sokağa girerse geri dönüp başka kapıyı çalar.

| Kavram | Kısa açıklama | Emirsel dünyadaki benzetme |
|---|---|---|
| Olgu | Doğru kabul edilen bilgi | Sabit veri kaydı |
| Kural | Koşullu mantıksal çıkarım | if bloğuna benzer ama bildirimsel |
| Sorgu | Cevabı aranan önerme | Fonksiyon çağrısı gibi görünür |
| Eşleme | Değişkenleri uygun değerlerle bağlama | Parametre eşleme |
| Geri izleme | Alternatif çözümleri deneme | Otomatik arama algoritması |

Bildirimsel felsefenin güzelliği burada ortaya çıkar. Diyelim ki bir liste içinde eleman aramak istiyoruz. Emirsel bir dilde sayaç açar, listenin sonuna kadar gider, karşılaştırma yaparız. Prolog’da ise ilişkinin tanımını yaparız:

```prolog
% Eleman, listenin başındaysa üyedir.
uye(X, [X|_]).

% Değilse, listenin kuyruğunda aranır.
uye(X, [_|Kuyruk]) :- uye(X, Kuyruk).
```

Bu iki satır şunu söyler: Bir şey listenin ilk elemanıysa üyedir; değilse geri kalanında üyeyse yine üyedir. Burada döngü yoktur, sayaç yoktur, indeks yoktur. Yine de Prolog bu tanımı kullanarak hem `uye(3, [1,2,3])` sorusuna doğru cevabını verebilir hem de `uye(X, [a,b,c])` sorgusuyla olası değerleri tek tek üretebilir.

Elbette Prolog sihirli değnek değildir. Sayısal hesaplama, grafik arayüz, sistem programlama gibi alanlarda emirsel diller daha doğal olabilir. Ancak kural tabanlı sistemler, uzman sistemler, doğal dil işleme, planlama, bulmaca çözme ve sembolik yapay zeka gibi konularda Prolog’un mantıksal modeli çok güçlüdür.

Sonuç olarak Prolog öğrenmek sadece yeni bir dil öğrenmek değildir; programlama hakkında düşünme biçimini genişletmektir. Emirsel paradigmada algoritmayı yürütürüz; mantıksal paradigmada gerçeği tarif ederiz. Birinde bilgisayara yolu çizeriz, diğerinde hedefin tanımını veririz. Ve bazen en zarif program, ne yapılacağını bağıran değil, neyin doğru olduğunu sakin sakin anlatandır.
