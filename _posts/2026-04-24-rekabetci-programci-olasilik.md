---
layout: post
title: Rekabetçi Programcı Olasılık
math: true
excerpt_separator: "``"
categories:
  - Program
tags:
  - olasılık
  - probability
  - kombinatorik
  - beklenen-değer
  - markov-zinciri
  - monte-carlo
  - las-vegas
  - rastgele-algoritma
  - quickselect
  - dağılım
  - c
  - programlama
  - algoritma
  - olimpiyat
  - yarışma
  - kodlama
  - matematik
  - kitap
---

**Olasılık**, rastgele bir sürecin sonuçlarını sayısal olarak ifade eder. $0$ ile $1$ arasında bir değer olan $P(A)$, $A$ olayının gerçekleşme ihtimalini verir; $P(A) = 0$ imkânsızı, $P(A) = 1$ kesinliği temsil eder.

Zar atma örneğiyle:

- $P(\text{"sonuç 4"}) = 1/6$
- $P(\text{"sonuç 6 değil"}) = 5/6$
- $P(\text{"sonuç çift"}) = 1/2$
``

## 24.1 Hesaplama

Bir olayın olasılığını hesaplamak için iki temel yöntem kullanılır.

**1. Yöntem — Kombinatorik:** Olasılık şu formülle bulunur:

$$P(A) = \frac{\text{istenen durum sayısı}}{\text{toplam olası durum sayısı}}$$

Örneğin karıştırılmış 52 kartlık desteden aynı değerde 3 kart seçme olasılığı:

$$\frac{13 \cdot \binom{4}{3}}{\binom{52}{3}} = \frac{1}{425}$$

çünkü 13 kart değeri vardır, her değerden 4 kart arasından 3 seçilir ve toplamda 52 karttan 3 seçilir.

**2. Yöntem — Simülasyon (Adım adım çarpım):** Her adımı sırayla düşünürüz:

- 1. kart: herhangi bir kart → olasılık $1$
- 2. kart: kalan 51 kart arasında aynı değerde 3 kart → olasılık $3/51$
- 3. kart: kalan 50 kart arasında aynı değerde 2 kart → olasılık $2/50$

$$1 \cdot \frac{3}{51} \cdot \frac{2}{50} = \frac{1}{425}$$

## 24.2 Olaylar

Olasılık teorisinde bir **olay** $A$, tüm olası durumlar kümesi $X$'in bir alt kümesidir: $A \subset X$.

Zar örneğinde $X = \{1,2,3,4,5,6\}$ ve "çift sayı gelme" olayı $A = \{2,4,6\}$'dır. Her $x$ durumuna bir $p(x)$ olasılığı atanır; olayın olasılığı:

$$P(A) = \sum_{x \in A} p(x)$$

Tüm olası durumların olasılıkları toplamı her zaman $P(X) = 1$ olmalıdır.

### Temel İşlemler

Olaylar birer küme olduğundan standart küme işlemleri uygulanır:

- **Tümleyen** $\bar{A}$: "$A$ gerçekleşmeyecek". $P(\bar{A}) = 1 - P(A)$
- **Birleşim** $A \cup B$: "$A$ veya $B$ gerçekleşecek". $P(A \cup B) = P(A) + P(B) - P(A \cap B)$
- **Kesişim** $A \cap B$: "$A$ ve $B$ birlikte gerçekleşecek". $P(A \cap B) = P(A)\,P(B \mid A)$

**Tümleyen ile zıt problem çözme:** 10 defa zar attığımızda en az bir kez 6 gelme olasılığı doğrudan hesaplamak yerine tümleyenle bulunur:

$$P(\text{en az bir 6}) = 1 - \left(\frac{5}{6}\right)^{10}$$

**Birleşim örneği:** Zar atarken $A = $ "çift sayı" ve $B = $ "4'ten küçük" olayları için:

$$P(A \cup B) = \frac{1}{2} + \frac{1}{2} - \frac{1}{6} = \frac{5}{6}$$

Eğer $A \cap B = \emptyset$ (ayrık olaylar) ise $P(A \cup B) = P(A) + P(B)$.

### Koşullu Olasılık

$B$ olayının gerçekleşeceği bilindiğinde $A$'nın olasılığı:

$$P(A \mid B) = \frac{P(A \cap B)}{P(B)}$$

### Bağımsız Olaylar

$A$ ve $B$ olayları, birinin gerçekleşmesi diğerini etkilemiyorsa **bağımsızdır**: $P(A \mid B) = P(A)$ ve $P(B \mid A) = P(B)$. Bu durumda:

$$P(A \cap B) = P(A)\,P(B)$$

Örneğin desteden kart çekerken $A = $ "sinek" ve $B = $ "değeri 4" bağımsızdır:

$$P(\text{sinek 4}) = \frac{1}{4} \cdot \frac{1}{13} = \frac{1}{52}$$

## 24.3 Rastgele Değişkenler

**Rastgele değişken**, rastgele bir süreçten üretilen sayısal değerdir. $P(X = x)$ ifadesi $X$'in $x$ değerini alma olasılığını verir.

Örneğin iki zar atıldığında $X = $ "toplamları" için $P(X = 10) = 3/36$; zira [4,6], [5,5] ve [6,4] kombinasyonları 10 toplamını verir.

### Beklenen Değer

**Beklenen değer** $E[X]$, $X$'in ağırlıklı ortalamasıdır:

$$E[X] = \sum_{x} P(X = x) \cdot x$$

Tek zar için: $E[X] = \frac{1}{6}(1+2+3+4+5+6) = \frac{7}{2}$

**Beklenen değerin doğrusallığı:** Değişkenler bağımlı olsa bile:

$$E[X_1 + X_2 + \cdots + X_n] = E[X_1] + E[X_2] + \cdots + E[X_n]$$

İki zar için: $E[X_1 + X_2] = 7/2 + 7/2 = 7$.

**Uygulama:** $n$ topun rastgele $n$ kutuya yerleştirildiğinde boş kutu sayısının beklenen değeri nedir? Tek bir kutunun boş kalma olasılığı $\left(\frac{n-1}{n}\right)^n$ olduğundan, doğrusallık ile:

$$E[\text{boş kutu sayısı}] = n \cdot \left(\frac{n-1}{n}\right)^n$$

### Dağılımlar

Bir rastgele değişkenin **dağılımı**, alabileceği her değerin olasılığını gösterir. Önemli dağılımlar:

**Sürekli (Uniform) dağılım:** $a, a+1, \ldots, b$ arasındaki $n$ değerden her birinin olasılığı $1/n$'dir.

$$E[X] = \frac{a+b}{2}$$

Zar için: $E[X] = (1+6)/2 = 7/2$.

**Binom dağılım:** $n$ denemeden her birinin başarı olasılığı $p$ iken tam $x$ başarının olasılığı:

$$P(X = x) = \binom{n}{x} p^x (1-p)^{n-x}, \qquad E[X] = pn$$

Örneğin 10 zar atışında tam 3 kez 6 gelme olasılığı: $\binom{10}{3}(1/6)^3(5/6)^7$.

**Geometrik dağılım:** İlk başarıya ulaşmak için gereken deneme sayısı ($p$ başarı olasılığı):

$$P(X = x) = (1-p)^{x-1} p, \qquad E[X] = \frac{1}{p}$$

Örneğin 6 gelene kadar zar atarken 4 denemede başarı olasılığı: $(5/6)^3 \cdot 1/6$.

## 24.4 Markov Zincirleri

**Markov zinciri**, durumlar ve aralarındaki geçiş olasılıklarından oluşan rastgele bir süreçtir. Bir çizge olarak gösterilir: düğümler durumları, kenarlar geçişleri temsil eder.

**Örnek:** $n$ katlı binada her adımda bir kat yukarı ya da aşağı yürünüyor (1. kattan sadece yukarı, $n$. kattan sadece aşağı). $n = 5$ için çizge:

$$1 \xrightarrow{1} 2 \underset{1/2}{\overset{1/2}{\rightleftharpoons}} 3 \underset{1/2}{\overset{1/2}{\rightleftharpoons}} 4 \underset{1/2}{\overset{1/2}{\rightleftharpoons}} 5 \xrightarrow{1} 4 \quad \cdots$$

**Olasılık dağılımı** $[p_1, p_2, \ldots, p_n]$ vektörü ile tutulur; $p_k$ şu anki durumun $k$ olma ihtimalidir, $\sum p_k = 1$.

1. kattan başlayınca ilk dağılım $[1, 0, 0, 0, 0]$, sonraki $[0, 1, 0, 0, 0]$, ondan sonra $[1/2, 0, 1/2, 0, 0]$ şeklinde ilerler.

**Hesaplama yöntemleri:**

- **Dinamik programlama:** Dağılım vektörünü adım adım güncelleyerek $O(n^2 m)$ sürede $m$ adım hesaplanır.
- **Matris kuvveti:** Geçişler bir $n \times n$ geçiş matrisi $T$ ile ifade edilir. $m$ adım sonraki dağılım $T^m \cdot [p_1, \ldots, p_n]^T$ ile bulunur ve $O(n^3 \log m)$ sürer.

$n = 5$ için geçiş matrisi:

$$T = \begin{pmatrix} 0 & 1/2 & 0 & 0 & 0 \\ 1 & 0 & 1/2 & 0 & 0 \\ 0 & 1/2 & 0 & 1/2 & 0 \\ 0 & 0 & 1/2 & 0 & 1 \\ 0 & 0 & 0 & 1/2 & 0 \end{pmatrix}$$

## 24.5 Rastgele Algoritmalar

**Rastgele algoritma**, probleme özgü rastgelelik olmasa bile kendi iç rastgeleliğini kullanan algoritmadır. İki ana türü vardır:

- **Monte Carlo algoritması:** Kesin doğru cevap garantisi yoktur, küçük bir hata olasılığı kabul edilir; buna karşın çalışma süresi deterministiktir.
- **Las Vegas algoritması:** Her zaman doğru cevabı verir; çalışma süresi rastgeledir ama beklenen süre verimlidir.

### Sıra İstatistikleri (Quickselect)

$n$ elemanlı bir dizinin $k$. en küçük elemanını bulmak için diziyi tamamen sıralamak şart değildir. **Hızlı Seçme (Quickselect)** bir Las Vegas algoritmasıdır:

1. Diziden rastgele bir $x$ öğesi (pivot) seç.
2. $x$'ten küçükleri sola, büyükleri sağa yerleştir ($O(n)$ sürer).
3. Sol kısımda $a$ eleman varsa:
   - $a = k-1$ ise $x$ cevaptır.
   - $a \geq k$ ise sol kısımda ara.
   - $a < k-1$ ise sağ kısımda $(k-a-1)$. sırayı ara.

Beklenen süre:

$$n + n/2 + n/4 + \cdots < 2n = O(n)$$

En kötü durum $O(n^2)$ olmakla birlikte pratikte bu durum son derece nadirdir.

### Matris Çarpımını Doğrulama (Freivalds Algoritması)

$n \times n$ boyutlu $A$, $B$, $C$ matrisleri için $AB = C$ mi sorusunu $O(n^2)$'de doğrulamak mümkündür (doğrudan $AB$ çarpmak $O(n^3)$ sürer):

1. Rastgele bir $n$ boyutlu $X$ vektörü seç.
2. $A(BX)$ ve $CX$ matrislerini hesapla (her biri $O(n^2)$).
3. $A(BX) = CX$ ise $AB = C$ de; değilse $AB \neq C$ de.

Algoritma (Freivalds, 1977) $AB \neq C$ olduğu hâlde yanlış "eşit" diyebilir; fakat bu olasılık çok küçüktür ve testi farklı rastgele $X$'lerle tekrarlamak hata ihtimalini üstel hızda azaltır.

### Çizge Boyaması

$n$ düğüm ve $m$ kenardan oluşan bir çizgeyi iki renkle öyle boyamak istiyoruz ki en az $m/2$ kenarda uç noktaların renkleri farklı olsun.

**Las Vegas yaklaşımı:** Her düğümü $1/2$ olasılıkla bağımsız olarak renklendir. Tek bir kenarın uç noktalarının farklı renkli olma olasılığı $1/2$'dir. Doğrusallık gereği beklenen "farklı uçlu kenar" sayısı $m/2$'dir. Yani rastgele bir boyama beklenen değerde geçerlidir; dolayısıyla geçerli bir boyama genellikle hızla bulunur.


