---
layout: post
title: Rekabetçi Programcı Yönlü Çizgeler
math: true
excerpt_separator: "``"
categories:
  - Program
tags:
  - çizge
  - graph
  - yönlü-çizge
  - directed-graph
  - dag
  - topolojik-sıralama
  - topological-sort
  - dinamik-programlama
  - ardıl-çizge
  - successor-graph
  - floyd
  - döngü-bulma
  - dfs
  - c
  - programlama
  - algoritma
  - olimpiyat
  - yarışma
  - kodlama
  - matematik
  - kitap
---

Bu bölümde yönlü çizgelerin iki türünden bahsedeceğiz:

- **Asiklik Çizgeler (Acyclic Graphs / DAG):** Çizgede hiçbir döngü yoktur; yani bir düğümden kendisine geri dönen bir yol mevcut değildir.
- **Varis Çizgeleri (Successor Graphs):** Her düğümden çıkan yalnızca 1 kenar vardır, yani her düğümün tam olarak bir ardılı vardır.

Her iki durumda da bu özellikler sayesinde çeşitli verimli algoritmalar tasarlanabilir.
``

## 16.1 Topolojik Sıralama

Topolojik sıralama, yönlü bir çizgenin düğümlerini belirli bir sıraya koymanın yoludur. Sıralamanın kuralı şudur: eğer $a$ düğümünden $b$ düğümüne bir yol varsa, $a$ sıralamada $b$'den önce yer alır.

Asiklik çizgelerde her zaman en az bir topolojik sıralama vardır. Ancak çizge döngü içeriyorsa topolojik sıralama yapmak mümkün değildir; çünkü döngüdeki hiçbir düğüm sıralamada diğerlerinden önce gelemez.

### Algoritma

Fikir, tüm düğümleri ziyaret edip işlenmemiş her düğümden derinlik öncelikli arama (DFS) başlatmaktır. Her düğümün üç olası durumu vardır:

- **0. durum (beyaz):** Düğüm henüz işlenmedi.
- **1. durum (açık gri):** Düğüm şu anda işleniyor.
- **2. durum (koyu gri):** Düğüm tamamen işlendi.

Başlangıçta tüm düğümler 0. durumdadır. Bir düğümde arama başladığında durumu 1'e geçer. Düğümün tüm devam düğümleri işlendiğinde durumu 2 olur ve düğüm bir listeye eklenir. **Topolojik sıralama, bu listenin tersidir.**

Çizge döngü içeriyorsa arama sırasında durumu 1 olan bir düğümle tekrar karşılaşılır; bu, topolojik sıralamanın yapılamayacağını gösterir.

### Örnek 1 (Asiklik Çizge)

Arama 1. düğümden başlayıp 6. düğüme ilerler. 6. düğüm işlenip listeye eklenir; ardından 3, 2 ve 1. düğümler sırasıyla eklenir: liste $[6, 3, 2, 1]$. Sonraki arama 4. düğümde başlar ve $[6, 3, 2, 1, 5, 4]$ listesi oluşur. Listenin tersi olan $[4, 5, 1, 2, 3, 6]$ topolojik sıralamayı verir.

Bir çizgede birden fazla geçerli topolojik sıralama bulunabilir.

### Örnek 2 (Döngülü Çizge)

Döngü içeren bir çizgede arama sırasında durumu 1 olan (işlenmekte olan) bir düğüme tekrar ulaşılır. Bu, çizgede topolojik sıralama yapılamayacağının kanıtıdır. Örneğin $2 \to 3 \to 5 \to 2$ döngüsü bunu engeller.

## 16.2 Dinamik Programlama

Yönlü çizge asiklik ise, dinamik programlama uygulanabilir. Bu teknikle aşağıdaki gibi sorular verimli biçimde cevaplanabilir:

- Başlangıçtan hedefe kaç farklı yol vardır?
- En kısa veya en uzun yol hangisidir?
- Bir yoldaki minimum veya maksimum kenar sayısı nedir?
- Hangi düğümler her yolda kesinlikle geçilir?

### Yol Sayısını Hesaplama

$\text{paths}(x)$, 1. düğümden $x$ düğümüne giden yol sayısını temsil etsin. Temel durum $\text{paths}(1) = 1$ olur. Diğer değerler şu özyinelemeyle hesaplanır:

$$\text{paths}(x) = \text{paths}(a_1) + \text{paths}(a_2) + \cdots + \text{paths}(a_k)$$

Burada $a_1, a_2, \ldots, a_k$, $x$ düğümüne doğrudan kenar gönderen düğümlerdir. Çizge asiklik olduğu için $\text{paths}(x)$ değerleri topolojik sırayı takip ederek hesaplanabilir.

Örneğin aşağıdaki çizgede 1. düğümden 6. düğüme 3 yol vardır ($1{\to}2{\to}3{\to}6$, $1{\to}4{\to}5{\to}2{\to}3{\to}6$, $1{\to}4{\to}5{\to}3{\to}6$) ve düğümlerin $\text{paths}$ değerleri topolojik sırayla şöyle hesaplanır:

| Düğüm | 1 | 4 | 5 | 2 | 3 | 6 |
|:-----:|:-:|:-:|:-:|:-:|:-:|:-:|
| $\text{paths}$ | 1 | 1 | 1 | 2 | 3 | 3 |

### Dijkstra Çıktısı Üzerinde DP

Dijkstra'nın Algoritması'nın yan ürünü olarak bir yönlü asiklik çizge elde edilir; bu çizge her düğüme ulaşan en kısa yolları gösterir. Bu çizge üzerinde dinamik programlama ile örneğin "en kısa yolların sayısı" gibi sorular cevaplanabilir.

### Herhangi Bir DP Sorusu Çizge Olarak Gösterilebilir

Her dinamik programlama sorusu, düğümlerin durumları ve kenarların geçişleri temsil ettiği yönlü asiklik bir çizge olarak modellenebilir. Örneğin $\{c_1, c_2, \ldots, c_k\}$ paralarıyla $n$ miktarını oluşturma problemi böyle bir çizgedir; 0. düğümden $n$. düğüme olan en kısa yol minimum para sayısını, yol sayısı ise toplam çözüm sayısını verir.

## 16.3 Ardıl Yollar

Ardıl çizgelerde her düğümden yalnızca 1 kenar çıkar. Böyle bir çizge bir veya birkaç parçadan oluşur ve her parça bir döngü ile ona götüren yolları içerir. Ardıl çizgeler bazen **fonksiyonel çizge** olarak da adlandırılır; çünkü her ardıl çizge, bir düğümü alıp ardılını döndüren bir fonksiyona karşılık gelir.

Örneğin:

| $x$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|:---:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| $\text{succ}(x)$ | 3 | 5 | 7 | 6 | 2 | 2 | 1 | 6 | 3 |

### $O(\log k)$ ile Ardıl Hesaplama

$\text{succ}(x, k)$, $x$ düğümünden tam olarak $k$ adım atıldığında ulaşılan düğümü verir. Örneğin $\text{succ}(4, 6) = 2$: $4 \to 6 \to 2 \to 5 \to 2 \to 5 \to 2$.

Naif yöntem $O(k)$ zaman alır. Ön işlemeyle tüm $\text{succ}(x, k)$ değerleri $k = 2^i$ kuvvetleri için önceden hesaplanırsa, herhangi bir sorgu $O(\log k)$ zamanda yanıtlanabilir. Özyineleme şöyle kurulur:

$$\text{succ}(x, k) = \begin{cases} \text{succ}(x) & k = 1 \\ \text{succ}(\text{succ}(x,\, k/2),\, k/2) & k > 1 \end{cases}$$

Ön işleme $O(n \log u)$ zaman alır; $u$ atılacak maksimum adım sayısıdır. Yukarıdaki çizge için ilk birkaç satır:

| $x$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|:---:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| $\text{succ}(x, 1)$ | 3 | 5 | 7 | 6 | 2 | 2 | 1 | 6 | 3 |
| $\text{succ}(x, 2)$ | 7 | 2 | 1 | 2 | 5 | 5 | 3 | 2 | 7 |
| $\text{succ}(x, 4)$ | 3 | 2 | 7 | 2 | 5 | 5 | 1 | 2 | 3 |
| $\text{succ}(x, 8)$ | 7 | 2 | 1 | 2 | 5 | 5 | 3 | 2 | 7 |

Herhangi bir $\text{succ}(x, k)$ için $k$, 2'nin kuvvetlerinin toplamı olarak ifade edilir. Örneğin $11 = 8 + 2 + 1$ olduğundan:

$$\text{succ}(x, 11) = \text{succ}(\text{succ}(\text{succ}(x, 8), 2), 1)$$

Örneğin $\text{succ}(4, 11) = 5$ bu şekilde $O(\log 11)$ adımda hesaplanır.

## 16.4 Döngü Bulma

Tek bir yolu olan ve bu yol bir döngüyle biten bir ardıl çizge düşünelim. Başlangıç düğümünden ilerlemeye başladığımızda şu sorular sorulabilir: Döngüdeki ilk düğüm hangisidir? Döngü kaç düğümden oluşur?

Örneğin $1 \to 2 \to 3 \to 4 \to 5 \to 6 \to 4 \to \cdots$ yolunda döngüye giren ilk düğüm 4'tür ve döngü $\{4, 5, 6\}$ olmak üzere üç düğümden oluşur.

Basit bir yöntem, çizgede ilerleyerek ziyaret edilen tüm düğümleri tutmak ve bir düğüm iki kez görüldüğünde döngünün başladığına karar vermektir. Bu yöntem $O(n)$ zaman ve $O(n)$ bellek kullanır.

### Floyd'un Algoritması

Floyd'un Algoritması da $O(n)$ zamanda çalışır; ancak yalnızca $O(1)$ ek bellek kullanır. İki işaretçi $a$ ve $b$ kullanılır; $a$ her adımda 1 ileri, $b$ ise 2 ileri gider:

```cpp
a = succ(x);
b = succ(succ(x));
while (a != b) {
    a = succ(a);
    b = succ(succ(b));
}
```

İki işaretçi buluştuğunda $a$ işaretçisi $k$ adım atmıştır ve $b$ işaretçisi $2k$ adım atmıştır. Bu noktada döngünün uzunluğu $k$'yi tam böler. Döngüye giren ilk düğümü bulmak için $a$'yı başlangıç noktasına geri alıp her iki işaretçiyi birer birer ilerletiriz:

```cpp
a = x;
while (a != b) {
    a = succ(a);
    b = succ(b);
}
first = a;
```

Son olarak döngünün uzunluğu şöyle hesaplanır:

```cpp
b = succ(a);
length = 1;
while (a != b) {
    b = succ(b);
    length++;
}
```
