---
layout: post
title: "Değişkenler ve Atama Mantığı: Büyük Harfli Sembollerin Gizli Dedektifliği"
math: true
categories: 
  - Bilgi
tags: 
  - değişkenler
  - mantıksal-programlama
  - prolog
---

Bir programlama dilinde değişken deyince aklımıza çoğu zaman kutular, etiketler ve bellekte duran değerler gelir. Mantıksal programlamada, özellikle Prolog tarzı dillerde ise değişken biraz daha dedektif gibidir: Büyük harfle başlayan bir sembol, sorgu anında henüz bilinmeyen bir değeri temsil eder ve sistem arka planda onu uygun gerçeklerle eşleştirmeye çalışır.
``
Bu yaklaşımın kalbinde atama değil, daha doğru adıyla eşleştirme yani unification vardır. Klasik dillerde x = 5 dediğimizde x isimli yere 5 değerini koyarız. Mantıksal programlamada ise X = 5 ifadesi, X bilinmiyorsa onu 5 ile uyumlu hale getirir. Eğer X zaten başka bir değerle eşleşmişse, sistem bu eşleşmenin çelişip çelişmediğine bakar.

Basitçe düşünelim: elimizde bazı bilgiler olsun.

```prolog
seviyor(ali, kahve).
seviyor(ayse, cay).
seviyor(ali, kitap).
```

Burada `ali`, `kahve`, `ayse` gibi küçük harfle başlayan ifadeler sabit değerlerdir. Yani sistem için bunlar zaten bilinen şeylerdir. Ama `X` ya da `Ne` gibi büyük harfle başlayan semboller değişkendir. Şu sorguyu yazdığımızda:

```prolog
seviyor(ali, X).
```

sistem şunu sorar: Ali neyi seviyor? Arka planda tüm `seviyor` kayıtlarını dolaşır ve birinci konumu `ali` olanları bulur. Sonuçlar sırayla şöyle eşleşir:

| Sorgu | Eşleşen gerçek | Değişkenin değeri |
|---|---|---|
| `seviyor(ali, X)` | `seviyor(ali, kahve)` | `X = kahve` |
| `seviyor(ali, X)` | `seviyor(ali, kitap)` | `X = kitap` |

Yani değişken, tek bir sihirli cevap değil, mümkün olan cevaplar kümesidir. Matematiksel olarak bunu şöyle düşünebiliriz: Bir ilişki $R(kisi, nesne)$ olsun. `seviyor(ali, X)` sorgusu aslında $R(ali, X)$ koşulunu sağlayan tüm $X$ değerlerini arar. Sonuç kümesi $\{kahve, kitap\}$ olur.

Bu mantık, klasik atamadan önemli ölçüde farklıdır:

| Özellik | Klasik Değişken | Mantıksal Değişken |
|---|---|---|
| Başlangıç durumu | Genelde değer atanır | Bilinmeyen olabilir |
| İşlem tipi | Atama | Eşleştirme |
| Yön | Soldan sağa düşünülür | İlişki yönsüz çalışabilir |
| Örnek | `x = 5` | `X = 5` |
| Amaç | Değeri saklamak | Uygun değeri bulmak |

Daha eğlenceli bir örnek yapalım. Diyelim ki aile ilişkilerimiz var:

```prolog
ebeveyn(aylin, zeynep).
ebeveyn(murat, zeynep).
ebeveyn(zeynep, deniz).

anne_baba(X, Y) :- ebeveyn(X, Y).
```

Burada `anne_baba(X, Y)` kuralı, X kişisinin Y kişisinin ebeveyni olduğunu söyler. Şu sorgu:

```prolog
anne_baba(Kim, zeynep).
```

sisteme şunu dedirtir: Zeynep’in ebeveyni kim? Cevaplar `Kim = aylin` ve `Kim = murat` olur. Değişkenin adı `Kim` seçildiği için insan gözüyle de okunaklıdır; fakat sistem için önemli olan büyük harfle başlamasıdır.

Eşleştirme süreci kabaca şöyle işler:

1. Sorgudaki yapı ile veritabanındaki yapı karşılaştırılır.
2. Sabitler aynı mı diye bakılır.
3. Değişken varsa uygun değerle bağlanır.
4. Çelişki yoksa çözüm üretilir.
5. Başka olasılık varsa geri izleme ile yeni çözüm aranır.

Örneğin:

```prolog
seviyor(Kisi, kahve).
```

Bu sorguda `Kisi` bilinmeyendir. Sistem kahveyi sevenleri arar. Eğer `seviyor(ali, kahve)` varsa `Kisi = ali` sonucu çıkar. Burada değişken yalnızca boşluk doldurmaz; sorgunun yönünü de esnetir. Aynı ilişkiyle hem Ali’nin ne sevdiğini hem de kahveyi kimin sevdiğini sorabiliriz.

Bu fikri denklem çözmeye benzetebiliriz. $X + 2 = 5$ denkleminde $X$ bilinmeyendir ve $X = 3$ bulunur. Mantıksal programlamada da `seviyor(ali, X)` ifadesi, ilişki tablosunda X’i tamamlayacak değerleri arar. Ancak burada tek bir sayı yerine sembolik bilgiler ve birden fazla olası cevap olabilir.

Sonuç olarak büyük harfle başlayan değişkenler, mantıksal programlamanın en güçlü parçalarındandır. Onlar bellekteki sıradan kutular değil, soru işaretleridir. Programcı olarak siz ilişkiyi tanımlarsınız; motor ise bilinmeyenleri uygun değerlerle eşleştirir. Küçük harfli sabitler sahnedeki oyuncularsa, büyük harfli değişkenler dedektif şapkası takıp sahne arkasında kimin kimle eşleştiğini bulan zeki yardımcılarımızdır.
