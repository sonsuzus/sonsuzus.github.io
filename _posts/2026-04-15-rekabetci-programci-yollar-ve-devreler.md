---
layout: post
title: Rekabetçi Programcı Yollar ve Devreler
math: true
excerpt_separator: "``"
categories:
  - Program
tags:
  - çizge
  - graph
  - euler-yolu
  - euler-devresi
  - hamilton-yolu
  - hierholzer
  - de-bruijn
  - atın-turu
  - warnsdorf
  - np-hard
  - geri-izleme
  - dinamik-programlama
  - c
  - programlama
  - algoritma
  - olimpiyat
  - yarışma
  - kodlama
  - matematik
  - kitap
---

Bu bölümde çizgeler üzerindeki iki temel yol türü inceleniyor:

- **Euler Yolu:** Çizgedeki her kenardan tam olarak bir kez geçen yol.
- **Hamilton Yolu:** Çizgedeki her düğümü tam olarak bir kez ziyaret eden yol.

İlk bakışta birbirine benzer görünen bu iki kavram aslında tamamen farklı zorluktadır. Bir çizgenin Euler yolu içerip içermediğini belirlemek ve varsa bulmak çok verimli biçimde yapılabilir. Hamilton yolu ise **NP-hard** bir problemdir; bunu verimli çözen bilinen bir algoritma yoktur.
``

## 19.1 Euler Yolu

**Euler yolu**, çizgedeki her kenardan tam olarak bir kez geçen yoldur. Euler, bu tür yolları 1736'da Königsberg Köprüleri sorusunu araştırırken keşfetmiştir; bu olay çizge teorisinin doğuş noktası olarak kabul edilir.

Bir Euler yolunun aynı düğümde başlayıp bitmesi durumuna **Euler devresi** denir.

### Euler Yolu Varlık Koşulları

#### Yönsüz Çizgeler

Tüm kenarlar aynı bağlı bileşende olduğu varsayılarak:

- **Her düğümün derecesi çiftse** → Euler devresi vardır (yani her Euler yolu aynı zamanda devredir).
- **Tam olarak iki düğümün derecesi tekse, kalanlar çiftse** → Euler yolu vardır fakat devre yoktur; yol tek dereceli iki düğüm arasında uzanır.

Başka hiçbir durumda Euler yolu mevcut değildir.

Örneğin 1, 3 ve 4. düğümlerin derecesi 2 (çift), 2 ve 5. düğümlerin derecesi 3 (tek) olan bir çizgede 2. düğümden 5. düğüme bir Euler yolu bulunur; ancak Euler devresi mevcut değildir.

#### Yönlü Çizgeler

Tüm kenarlar aynı bileşende olduğu varsayılarak:

- **Her düğümde iç derece = dış derece** → Euler devresi vardır.
- **Bir düğümde dış derece = iç derece + 1** (başlangıç), **bir düğümde iç derece = dış derece + 1** (bitiş), **geri kalanlar eşit** → Euler yolu vardır, devre yoktur.

Örneğin 1, 3 ve 4. düğümlerin hem iç hem dış derecesi 1 olan; 2. düğümün iç derecesi 1, dış derecesi 2 olan; 5. düğümün iç derecesi 2, dış derecesi 1 olan bir çizge, 2. düğümden 5. düğüme bir Euler yolu içerir.

### Hierholzer'in Algoritması

**Hierholzer'in Algoritması**, Euler devresi bulmak için $O(n + m)$ zamanda çalışan verimli bir yöntemdir. Çizgenin Euler devresi içermesi gerekir; aksi hâlde algoritma çalışmaz. Çizgede yalnızca Euler *yolu* varsa, iki tek dereceli düğüm arasına yapay bir kenar eklenerek Euler devresine dönüştürülüp algoritma uygulanabilir.

Algoritma şu şekilde ilerler:

1. Başlangıç düğümünden hareket ederek çizgenin bir kısmını kapsayan bir devre oluştur.
2. Devrede yer alıp henüz devreye katılmamış komşusu bulunan bir $x$ düğümü bul.
3. $x$ düğümünden başlayıp devrede olmayan kenarlarla ilerle; sonunda $x$'e geri dönerek bir alt devre oluştur.
4. Bu alt devreyi ana devreye ekle.
5. Tüm kenarlar devreye girinceye kadar tekrarla.

#### Örnek

Aşağıdaki çizgede algoritma adım adım şöyle ilerler:

```
        1
      / | \
     2  3  4
     |  |  |
     5  6  7
```

- **Adım 1:** 1. düğümden $1 \to 2 \to 3 \to 1$ devresi oluşturulur.
- **Adım 2:** 2. düğümünden $2 \to 5 \to 6 \to 2$ alt devresi ana devreye eklenir.
- **Adım 3:** 6. düğümünden $6 \to 3 \to 4 \to 7 \to 6$ alt devresi ana devreye eklenir.

Tüm kenarlar devreye eklendiğinden Euler devresi başarıyla elde edilir.

## 19.2 Hamilton Yolları

**Hamilton yolu**, çizgedeki her düğümü tam olarak bir kez ziyaret eden yoldur. Aynı düğümde başlayıp bitiyorsa **Hamilton devresi** adını alır.

### Varlık Koşulları

Bir çizgenin Hamilton yolu içerip içermediğini verimli biçimde belirlemenin yolu yoktur; bu problem **NP-hard**'dır. Yine de bazı özel durumlarda Hamilton yolunun varlığı garantilenebilir:

- **Tam çizgeler:** Her iki düğüm arasında kenar varsa Hamilton yolu her zaman mevcuttur.
- **Dirac'ın Teoremi:** Her düğümün derecesi en az $n/2$ ise çizge Hamilton yolu içerir.
- **Ore'nin Teoremi:** Komşu olmayan her düğüm çiftinin derece toplamı en az $n$ ise çizge Hamilton yolu içerir.

Bu teoremlerin ortak paydası şudur: çizge ne kadar çok kenar içerirse Hamilton yolu bulunma olasılığı o kadar artar. Teoremler yalnızca yeterlilik koşulu sunar; tersinin garantisi yoktur.

### Hamilton Yolunun Bulunması

Varlığı bile verimli belirlenemeyen Hamilton yolunu bulmak da aynı şekilde zorludur. İki yaklaşım vardır:

**Geri izleme (backtracking):** Tüm olası düğüm sıralamaları denenir. Zaman karmaşıklığı $O(n!)$'dir; küçük $n$ değerleri için kullanılabilir.

**Dinamik programlama:** $\text{possible}(S, x)$ fonksiyonu, $S$ düğüm alt kümesini dolaşıp $x$ düğümünde biten bir Hamilton yolunun var olup olmadığını gösterir. $S$ bir bit maskesiyle temsil edilir ve fonksiyon aşağıdaki özyinelemeyle hesaplanır:

$$\text{possible}(S, x) = \bigvee_{y \in S,\, y \neq x,\, (y,x) \in E} \text{possible}(S \setminus \{x\}, y)$$

Bu yaklaşım $O(2^n n^2)$ zamanda çalışır; geri izlemeye kıyasla çok daha hızlıdır (bkz. Bölüm 10.5).

## 19.3 De Bruijn Dizileri

**De Bruijn dizisi**, $k$ karakterden oluşan alfabe üzerinde $n$ uzunluğundaki her alt yazıyı tam olarak bir kez içeren dairesel bir dizdir. Doğrusal biçimde yazıldığında uzunluğu $k^n + n - 1$ olur.

Örneğin $n = 3$, $k = 2$ için bir De Bruijn dizisi:

$$\texttt{0001011100}$$

Bu dizi $\{0, 1\}$ alfabesi üzerindeki tüm 3 bitlik dizileri tam birer kez içerir: $000, 001, 010, 011, 100, 101, 110, 111$.

### Euler Yolu Bağlantısı

De Bruijn dizisi inşa etmek, bir çizgede Euler yolu bulmaya indirgenir. Çizgenin düğümleri $n - 1$ karakterlik tüm yazılara, kenarlar ise bu yazılara bir karakter ekleyerek elde edilen $n$ karakterlik geçişlere karşılık gelir.

Örneğin $n = 3$, $k = 2$ için dört düğüm vardır: $00, 01, 10, 11$. $00$ düğümünden $0$ karakteri eklenince $00$ düğümüne ($000$), $1$ eklenince $01$ düğümüne ($001$) gidilir. Bu çizgedeki her Euler yolu tüm $n$ uzunluğundaki alt yazıları tam birer kez kapsar.

Yazının uzunluğu: başlangıç düğümünün $n - 1$ karakteri ile $k^n$ kenardaki karakterlerin toplamından $k^n + n - 1$ olur.

## 19.4 Atın Turları

**Atın turu**, bir satranç atının $n \times n$ tahtada her kareyi tam bir kez ziyaret ettiği hareket dizisidir. At başladığı kareye dönüyorsa **kapalı tur**, dönmüyorsa **açık tur** denir.

Örneğin $5 \times 5$ tahtadaki bir açık at turu:

```
 1  4 11 16 25
12 17  2  5 10
 3 20  7 24 15
18 13 22  9  6
21  8 19 14 23
```

At turu, kareler düğüm ve at hareketiyle ulaşılabilecek kareler kenar olarak modellenen bir çizgede **Hamilton yoluna** karşılık gelir.

### Warnsdorf'un Kuralı

Warnsdorf'un Kuralı, at turu bulmak için basit ve etkili bir **sezgisel (heuristic)** yöntemdir (1823). Temel fikir şudur: **atı her adımda, oradan yapılabilecek hareket sayısı en az olan kareye götür.**

Örneğin beş farklı kare arasından seçim yapılacak bir durumda, birinden yalnızca 1 hamle yapılabiliyorsa Warnsdorf kuralı atı o kareye yönlendirir; böylece "çıkmaz sokak" riski en aza indirilir.

Bu yaklaşım büyük tahtalarda dahi pratik sürelerde tur bulmayı mümkün kılar. At turu için polinom zamanlı algoritmalar da geliştirilmiştir; ancak bunlar çok daha karmaşıktır.
