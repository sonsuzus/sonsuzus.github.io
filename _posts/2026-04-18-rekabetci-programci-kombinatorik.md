---
layout: post
title: Rekabetçi Programcı Kombinatorik
math: true
excerpt_separator: "``"
categories:
  - Program
tags:
  - kombinatorik
  - combinatorics
  - binom-katsayısı
  - binomial-coefficient
  - katalan-sayısı
  - pascal-üçgeni
  - içerme-dışarma
  - inclusion-exclusion
  - düzensizlik
  - derangement
  - burnside
  - cayley
  - prüfer-kodu
  - multinomial
  - c
  - programlama
  - algoritma
  - olimpiyat
  - yarışma
  - kodlama
  - matematik
  - kitap
---

Kombinatorik, nesnelerin kombinasyonlarını sayma yöntemlerini araştırır. Genelde amaç her kombinasyonu ayrı ayrı oluşturmadan toplam sayıyı hesaplamaktır.

Örneğin toplamı $n$ olan tam sayı dizisi sayısı gibi problemler özyinelemeli formüllerle ele alınır. $f(n)$, $n$'yi toplam olarak yazma yollarının sayısı olsun:

$$f(n) = \begin{cases} 1 & n = 0 \\ f(0) + f(1) + \cdots + f(n-1) & n > 0 \end{cases}$$

İlk değerler: $f(0)=1,\ f(1)=1,\ f(2)=2,\ f(3)=4,\ f(4)=8$. Bu durumda kapalı form $f(n) = 2^{n-1}$'dir; çünkü $n-1$ boşluktan istediğimizi seçip $+$ ya da hiç koyabiliriz.
``

## 22.1 Binom Katsayıları

$\binom{n}{k}$, $n$ elemanlı bir kümeden $k$ elemanlı alt küme seçme sayısıdır. Örneğin $\binom{5}{3} = 10$ çünkü $\{1,2,3,4,5\}$ kümesinin 3 elemanlı alt kümeleri şunlardır:

$$\{1,2,3\},\ \{1,2,4\},\ \{1,2,5\},\ \{1,3,4\},\ \{1,3,5\},\ \{1,4,5\},\ \{2,3,4\},\ \{2,3,5\},\ \{2,4,5\},\ \{3,4,5\}$$

### 1. Formül: Özyineleme

Kümedeki bir $x$ elemanı sabitlenir. $x$ alt kümede ya var ya yoktur:

$$\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$$

Temel durumlar:

$$\binom{n}{0} = \binom{n}{n} = 1$$

### 2. Formül: Faktöriyel

$n$ elemanın $n!$ permütasyonu arasından ilk $k$'sını alt kümeye eklersek, sıralama önemli olmadığından $k!$ ve $(n-k)!$'e böleriz:

$$\binom{n}{k} = \frac{n!}{k!\,(n-k)!}$$

### Özellikler

$$\binom{n}{k} = \binom{n}{n-k}$$

Tüm binom katsayılarının toplamı:

$$\sum_{k=0}^{n} \binom{n}{k} = 2^n$$

Binom teoremi:

$$(a+b)^n = \sum_{k=0}^{n} \binom{n}{k} a^{n-k} b^k$$

**Pascal'ın Üçgeni:** Her değer, üstündeki iki değerin toplamıdır:

```
            1
          1   1
        1   2   1
      1   3   3   1
    1   4   6   4   1
   ...  ...  ... ...  ...
```

### Kutular ve Toplar

$k$ topu $n$ kutuya yerleştirme probleminin üç farklı varyantı vardır:

**1. Durum — Her kutu en fazla 1 top alır:** Çözüm sayısı doğrudan $\dbinom{n}{k}$'dır.

**2. Durum — Bir kutu birden fazla top alabilir:** Topları "o" ve kutu geçişlerini "→" ile sembolize edersek her çözüm $k$ adet "o" ve $n-1$ adet "→" içeren bir diziye karşılık gelir:

$$\binom{k + n - 1}{k}$$

**3. Durum — Her kutu en fazla 1 top alır ve ardışık iki kutu aynı anda dolu olamaz:** $k$ topu önce $k$ ayrı kutuya yerleştirip aralarına birer boş kutu koyarız; kalan $n - 2k + 1$ kutuyu dağıtmak için 2. senaryonun formülünü uygularız:

$$\binom{n - k + 1}{k}$$

### Çok Terimli Katsayılar

$n$ nesneyi $k_1, k_2, \ldots, k_m$ büyüklüklü gruplara ayırma sayısı:

$$\binom{n}{k_1, k_2, \ldots, k_m} = \frac{n!}{k_1!\, k_2!\, \cdots\, k_m!}$$

Bu, binom katsayısının $m = 2$ özel durumudur.

## 22.2 Katalan Sayıları

$C_n$, $n$ sol ve $n$ sağ parantezden oluşan **geçerli parantez ifadelerinin** sayısıdır. Örneğin $C_3 = 5$:

$$()()(), \quad (())(), \quad ()(()),\quad ((())),\quad (()())$$

### Geçerli Parantez İfadesi

Bir ifade geçerlidir ancak ve ancak:
- Her ön ekinde sağ parantez sayısı sol parantez sayısını geçmiyorsa,
- Toplam sol ve sağ parantez sayıları eşitse.

### 1. Formül: Özyineleme

İfadeyi iki parçaya böleriz; ilk parça mümkün olduğunca küçük tutulur:

$$C_n = \sum_{i=0}^{n-1} C_i \cdot C_{n-i-1}, \qquad C_0 = 1$$

Herhangi bir $i$ için ilk bölüm $i+1$ parantez çifti, ikinci bölüm $n-i-1$ parantez çifti içerir.

### 2. Formül: Binom Katsayısı

$$C_n = \frac{1}{n+1}\binom{2n}{n}$$

**Türetme:** $n$ sol ve $n$ sağ parantezden oluşan toplam $\binom{2n}{n}$ dizi vardır. Bunlardan geçersiz olanlar, ilk geçersizleştiği noktadan sonraki kısmın sembollerini ters çevirince $n+1$ sol ve $n-1$ sağ parantezli bir diziye dönüşür; bu tür dizi sayısı $\binom{2n}{n+1}$'dir. Dolayısıyla:

$$C_n = \binom{2n}{n} - \binom{2n}{n+1} = \frac{1}{n+1}\binom{2n}{n}$$

### Ağaçlarla Bağlantı

Katalan sayıları ağaç sayma problemlerinde de ortaya çıkar:

- $n$ düğümden oluşan **ikili ağaç** sayısı $C_n$'dir.
- $n$ düğümden oluşan **köklü ağaç** sayısı $C_{n-1}$'dir.

Örneğin $C_3 = 5$ için 5 farklı ikili ağaç ve $C_2 = 2$ için 2 farklı köklü ağaç vardır.

## 22.3 İçerme-Dışarma

**İçerme-dışarma ilkesi**, kesişim büyüklüklerini kullanarak birleşim büyüklüğünü (ya da tersini) hesaplamamızı sağlar.

İki küme için:

$$|A \cup B| = |A| + |B| - |A \cap B|$$

Üç küme için:

$$|A \cup B \cup C| = |A| + |B| + |C| - |A \cap B| - |A \cap C| - |B \cap C| + |A \cap B \cap C|$$

Genel kural: Tek sayıda kümenin kesişimi **eklenir**, çift sayıda kümenin kesişimi **çıkarılır**.

Simetrik olarak kesişim büyüklükleri de birleşimden hesaplanabilir. Örneğin:

$$|A \cap B| = |A| + |B| - |A \cup B|$$

$$|A \cap B \cap C| = |A| + |B| + |C| - |A \cup B| - |A \cup C| - |B \cup C| + |A \cup B \cup C|$$

### Düzensizlikler (Derangements)

$\{1, 2, \ldots, n\}$ elemanlarının **düzensizliği**, hiçbir elemanın kendi konumunda bulunmadığı permütasyondur. Örneğin $n = 3$ için $(2,3,1)$ ve $(3,1,2)$ olmak üzere yalnızca 2 düzensizlik vardır.

**İçerme-dışarma ile:** $X_k$, $k$. pozisyonda $k$ elemanını içeren permütasyon kümesi olsun. Düzensizlik sayısı:

$$n! - |X_1 \cup X_2 \cup \cdots \cup X_n|$$

$n = 3$ için:

$$|X_1 \cup X_2 \cup X_3| = 2 + 2 + 2 - 1 - 1 - 1 + 1 = 4$$

Düzensizlik sayısı $= 3! - 4 = 2$.

**Özyineleme ile:** $f(n)$, $n$ elemanlı kümenin düzensizlik sayısı olsun. 1. elemanın hangi $x$ ile yer değiştirdiğine göre iki seçenek vardır:

1. $x$ de 1. elemanın konumuna geçer → $n-2$ elemanlık düzensizlik: $f(n-2)$ yol.
2. $x$, 1. elemana değil başka bir konuma geçer → $n-1$ elemanlık düzensizlik: $f(n-1)$ yol.

$$f(n) = \begin{cases} 0 & n = 1 \\ 1 & n = 2 \\ (n-1)\bigl(f(n-2) + f(n-1)\bigr) & n > 2 \end{cases}$$

## 22.4 Burnside'ın Lemma'sı

**Burnside'ın Lemma'sı**, simetriler dikkate alındığında birbirinden gerçekten farklı kombinasyon sayısını hesaplamamızı sağlar. $n$ farklı dönüşüm (pozisyon değiştirme yolu) varsa ve $k$. dönüşüm uygulandığında $c(k)$ kombinasyon değişmeden kalıyorsa, toplam farklı kombinasyon sayısı:

$$\frac{1}{n} \sum_{k=1}^{n} c(k)$$

### Örnek: Renkli Kolye

$n$ inciden oluşan, her incinin $m$ farklı rengi olabileceği bir kolyede, döndürme simetrileri dikkate alındığında kaç farklı kolye vardır?

Kolyeyi $0, 1, \ldots, n-1$ adım döndürebiliriz ($n$ farklı dönüşüm). $k$ adım döndürüldüğünde sabit kalan kolye sayısı:

$$m^{\gcd(k, n)}$$

Bunun nedeni $\gcd(k,n)$ büyüklüğündeki inci bloklarının birbirinin yerine geçmesidir. Burnside'ın Lemma'sına göre farklı kolye sayısı:

$$\frac{1}{n} \sum_{i=0}^{n-1} m^{\gcd(i,n)}$$

**Örnek:** $n = 4$, $m = 3$ için:

$$\frac{3^4 + 3^1 + 3^2 + 3^1}{4} = \frac{81 + 3 + 9 + 3}{4} = \frac{96}{4} = 24$$

## 22.5 Cayley'in Formülü

**Cayley'in Formülü**, $n$ etiketli düğüm üzerinde oluşturulabilecek farklı ağaç sayısının $n^{n-2}$ olduğunu söyler. Düğümler $1, 2, \ldots, n$ ile etiketlenir; hem yapısı hem etiketi farklı olan ağaçlar sayılır.

Örneğin $n = 4$ için toplam etiketli ağaç sayısı $4^{4-2} = 16$'dır.

### Prüfer Kodu

Cayley'in Formülü, **Prüfer kodu** ile kanıtlanır. Prüfer kodu, etiketli bir ağacı $n-2$ sayıdan oluşan bir diziye dönüştürür.

**Kodlama algoritması:** $n-2$ kez tekrarlanır:
1. Ağaçtaki en küçük etiketli yaprak kaldırılır.
2. Bu yaprağın tek komşusunun etiketi koda eklenir.

**Örnek:** 5 düğümlü bir ağaçta adımlar şöyle ilerler:

- 1. düğüm (yaprak) kaldırılır → komşu 4 koda eklenir: `[4]`
- 3. düğüm (yaprak) kaldırılır → komşu 4 koda eklenir: `[4, 4]`
- 4. düğüm (yaprak) kaldırılır → komşu 2 koda eklenir: `[4, 4, 2]`

Prüfer kodu: $[4, 4, 2]$.

**Neden $n^{n-2}$?** Her etiketli ağacın benzersiz bir Prüfer kodu vardır ve her Prüfer kodundan orijinal ağaç benzersiz biçimde yeniden oluşturulabilir. $\{1, 2, \ldots, n\}$ üzerindeki $n-2$ uzunluklu dizi sayısı $n^{n-2}$ olduğundan etiketli ağaç sayısı da $n^{n-2}$'dir.
