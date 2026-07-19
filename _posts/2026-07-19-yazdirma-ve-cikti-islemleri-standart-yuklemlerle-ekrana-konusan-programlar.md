---
layout: post
title: "Yazdırma ve Çıktı İşlemleri: Standart Yüklemlerle Ekrana Konuşan Programlar"
math: true
categories: 
  - Bilgi
tags: 
  - Prolog
  - çıktı işlemleri
  - standart yüklemler
---

Bir programın kullanıcıyla ilk selamlaşması çoğu zaman ekrana yazdırdığı küçücük bir metinle başlar. Mantıksal programlama dünyasında, özellikle Prolog gibi dillerde, bu iş “fonksiyon çağırmak”tan çok “yüklem çalıştırmak” şeklinde düşünülür. Yani ekrana metin basmak, değişkenin değerini görmek veya satır atlamak için sisteme gömülü standart yüklemlerden yararlanırız.
``

Prolog’da çıktı işlemlerini anlamak için önce şu fikri netleştirelim: Prolog programı, doğruluğu araştırılan ilişkilerden oluşur. Ancak bazen yalnızca “sonuç doğru mu?” sorusunu değil, “bu sonucu kullanıcıya nasıl gösteririm?” sorusunu da cevaplamak isteriz. İşte `write/1`, `writeln/1`, `nl/0` ve `format/2` gibi yüklemler bu noktada sahneye çıkar.

Teorik olarak çıktı, bir terimin standart çıktı akışına gönderilmesidir. Bunu küçük bir modelle düşünebiliriz:

$Program \rightarrow Standart\ Çıktı \rightarrow Ekran$

Eğer elimizde `X = 42` gibi bir değişken bağlaması varsa, `write(X)` çağrısı artık ekrana `42` değerini taşır. Prolog’da değişkenler başlangıçta bilinmeyen varlıklardır; değerleri birleştirme, yani unification süreciyle belirlenir. Kısaca:

$X = Değer \Rightarrow write(X) = Değerin\ gösterimi$

Aşağıdaki tablo temel çıktı yüklemlerini karşılaştırır:

| Yüklem | Görevi | Yeni satır ekler mi? | Tipik kullanım |
|---|---|---:|---|
| `write/1` | Terimi ekrana yazar | Hayır | Değişken veya metin göstermek |
| `writeln/1` | Terimi yazar ve satır atlar | Evet | Okunabilir listeleme |
| `nl/0` | Sadece yeni satıra geçer | Evet | Satır düzeni kurmak |
| `format/2` | Şablonlu çıktı üretir | İsteğe bağlı | Raporlama, hizalama |

En basit örnekle başlayalım:

```prolog
selamla :-
    write('Merhaba Prolog!'),
    nl,
    write('Bugun cikti islemlerini ogreniyoruz.').
```

Bu kodda `selamla/0` adlı bir yüklem tanımlıyoruz. İlk `write/1` metni ekrana basar, `nl/0` imleci bir alt satıra indirir, ikinci `write/1` ise yeni satırdan devam eder. Burada önemli nokta şudur: `write/1` yazdırır ama satır sonunu kendiliğinden eklemez. Bu yüzden `nl` küçük ama kahraman bir yardımcıdır.

Değişken değerlerini göstermek için de aynı mantık geçerlidir:

```prolog
not_goster(Isim, Not) :-
    write(Isim),
    write(' isimli ogrencinin notu: '),
    write(Not),
    nl.
```

`not_goster('Ayse', 95).` sorgusu çalıştırıldığında ekranda okunabilir bir cümle oluşur. Burada Prolog, `Isim` ve `Not` değişkenlerini çağrı sırasında aldığı değerlere bağlar. Böylece çıktı yalnızca sabit metinden değil, çalışma zamanında gelen bilgilerden oluşur.

Daha düzenli ve profesyonel çıktılar için `format/2` oldukça kullanışlıdır. `format/2`, bir şablon ve bu şablona yerleştirilecek değerler listesiyle çalışır:

```prolog
rapor(Isim, Puan) :-
    format('Ogrenci: ~w~nPuan: ~w~n', [Isim, Puan]).
```

Buradaki `~w`, verilen değeri yazdırır; `~n` ise yeni satır anlamına gelir. Yani `format/2`, `write` ve `nl` ikilisini daha kontrollü bir biçimde kullanmamızı sağlar. Özellikle birden fazla değeri aynı çıktıda göstermek istediğimizde kod daha okunur hale gelir.

| Amaç | Daha basit yaklaşım | Daha düzenli yaklaşım |
|---|---|---|
| Tek metin yazmak | `write('Selam')` | `writeln('Selam')` |
| Satır atlamak | `nl` | `format('~n', [])` |
| Değişkenli cümle | Çoklu `write/1` | `format/2` |
| Rapor üretmek | Uzun ve parçalı kod | Şablonlu çıktı |

Bir mini örnekle konuyu bağlayalım:

```prolog
urun_etiketi(Ad, Fiyat, Stok) :-
    ToplamDeger is Fiyat * Stok,
    format('Urun: ~w~n', [Ad]),
    format('Birim fiyat: ~w TL~n', [Fiyat]),
    format('Stok: ~w adet~n', [Stok]),
    format('Toplam stok degeri: ~w TL~n', [ToplamDeger]).
```

Bu yüklem, ürün bilgilerini hesaplayıp okunabilir biçimde gösterir. `is/2` aritmetik hesaplama yapar; ardından `format/2` sonucu ekrana taşır. Matematiksel olarak hesaplanan değer şudur:

$ToplamDeger = Fiyat \times Stok$

Sonuç olarak çıktı işlemleri, programın dış dünyaya açılan penceresidir. `write/1` hızlı ve basittir, `nl/0` satır düzenini sağlar, `writeln/1` pratiklik sunar, `format/2` ise ciddi raporların yıldızıdır. Kodunuz doğru çalışabilir; ama iyi biçimlendirilmiş çıktı, kullanıcının “Evet, bu program ne yaptığını biliyor!” demesini sağlar.
