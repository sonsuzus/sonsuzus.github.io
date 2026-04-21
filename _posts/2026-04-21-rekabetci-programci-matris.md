---
layout: post
title: Rekabetçi Programcı Matris
math: true
excerpt_separator: "``"
categories:
  - Program
tags:
  - matris
  - matrix
  - matris-çarpımı
  - matris-kuvveti
  - determinant
  - ters-matris
  - linear-tekrar
  - fibonacci
  - komşuluk-matrisi
  - kirchhoff
  - laplacian
  - kapsayan-ağaç
  - c
  - programlama
  - algoritma
  - olimpiyat
  - yarışma
  - kodlama
  - matematik
  - kitap
---

**Matris**, programlamadaki iki boyutlu dizinin matematikteki karşılığıdır. $m \times n$ büyüklüğündeki bir matris $m$ satır ve $n$ sütundan oluşur; $A[i, j]$ gösterimi $i$. satır ve $j$. sütundaki elemanı verir. Özel bir durum olarak $n \times 1$ büyüklüğündeki matrise **vektör** denir.

$A$ matrisinin **transpozu** $A^T$, satırlar ile sütunların yer değiştirmesinden elde edilir: $A^T[i, j] = A[j, i]$. Satır ve sütun sayısı eşit olan matris **kare matristir**.
``

## 23.1 Operasyonlar

### Toplama ve Skaler Çarpma

Aynı boyuttaki $A$ ve $B$ matrislerinin toplamı $A + B$, karşılıklı elemanların toplamından oluşur:

$$
\begin{bmatrix} 6 & 1 & 4 \\ 3 & 9 & 2 \end{bmatrix}
+
\begin{bmatrix} 4 & 9 & 3 \\ 8 & 1 & 3 \end{bmatrix}
=
\begin{bmatrix} 10 & 10 & 7 \\ 11 & 10 & 5 \end{bmatrix}
$$

Bir matrisi $x$ skaleriyle çarpmak, her elemanı $x$ ile çarpar:

$$
2 \cdot \begin{bmatrix} 6 & 1 & 4 \\ 3 & 9 & 2 \end{bmatrix}
=
\begin{bmatrix} 12 & 2 & 8 \\ 6 & 18 & 4 \end{bmatrix}
$$

### Matris Çarpımı

$A$ matrisi $a \times n$, $B$ matrisi $n \times b$ boyutunda ise $AB$ çarpımı tanımlıdır ve $a \times b$ boyutunda bir matris üretir:

$$AB[i, j] = \sum_{k=1}^{n} A[i, k] \cdot B[k, j]$$

Her eleman, $A$'nın ilgili satırı ile $B$'nin ilgili sütununun nokta çarpımına eşittir. Örneğin:

$$
\begin{bmatrix} 1 & 4 \\ 3 & 9 \\ 8 & 6 \end{bmatrix}
\cdot
\begin{bmatrix} 1 & 6 \\ 2 & 9 \end{bmatrix}
=
\begin{bmatrix} 9 & 42 \\ 21 & 99 \\ 20 & 102 \end{bmatrix}
$$

Matris çarpımı **birleşme** özelliğine sahiptir ($A(BC) = (AB)C$) ama **değişme** özelliğine sahip değildir ($AB \neq BA$ olabilir).

**Birim matris** $I$, köşegenleri 1, diğer tüm elemanları 0 olan kare matristir. Herhangi bir $A$ için $AI = IA = A$ geçerlidir.

$n \times n$ iki matrisin çarpımı düz algoritmada $O(n^3)$ zamanda hesaplanır. Strassen (1969) gibi daha verimli algoritmalar teorik açıdan ilginç olmakla birlikte rekabetçi programlamada genellikle gerekli değildir.

### Matris Kuvveti

$A$ kare matrisi ise $A^k$, $A$'nın kendisiyle $k$ defa çarpılmasıdır; $A^0 = I$. Modüler üs almanın analogu olan hızlı kuvvet yöntemiyle $A^k$, $O(n^3 \log k)$ zamanda hesaplanır:

$$A^8 = A^4 \cdot A^4, \qquad A^4 = A^2 \cdot A^2, \quad \ldots$$

Örneğin:

$$
\begin{bmatrix} 2 & 5 \\ 1 & 4 \end{bmatrix}^3
=
\begin{bmatrix} 48 & 165 \\ 33 & 114 \end{bmatrix}
$$

### Determinant

$A$ kare matrisi için **determinant** $\det(A)$, özyinelemeli olarak hesaplanır. $1 \times 1$ matris için $\det(A) = A[1,1]$. Daha büyük matrisler için:

$$\det(A) = \sum_{j=1}^{n} A[1, j] \cdot C[1, j]$$

Burada $C[i, j] = (-1)^{i+j} \det(M[i,j])$ **kofaktördür** ve $M[i,j]$, $A$'dan $i$. satır ile $j$. sütun çıkarılarak elde edilir. Örneğin:

$$
\det\begin{pmatrix} 3 & 4 \\ 1 & 6 \end{pmatrix} = 3 \cdot 6 - 4 \cdot 1 = 14
$$

$$
\det\begin{pmatrix} 2 & 4 & 3 \\ 5 & 1 & 6 \\ 7 & 2 & 4 \end{pmatrix}
= 2 \det\begin{pmatrix}1&6\\2&4\end{pmatrix}
- 4 \det\begin{pmatrix}5&6\\7&4\end{pmatrix}
+ 3 \det\begin{pmatrix}5&1\\7&2\end{pmatrix}
= 81
$$

### Ters Matris

$\det(A) \neq 0$ ise $A \cdot A^{-1} = I$ koşulunu sağlayan **ters matris** $A^{-1}$ mevcuttur:

$$A^{-1}[i, j] = \frac{C[j, i]}{\det(A)}$$

Örneğin:

$$
\begin{pmatrix} 2 & 4 & 3 \\ 5 & 1 & 6 \\ 7 & 2 & 4 \end{pmatrix}
\cdot
\frac{1}{81}\begin{pmatrix} -8 & -10 & 21 \\ 22 & -13 & 3 \\ 3 & 24 & -18 \end{pmatrix}
=
\begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}
$$

## 23.2 Lineer Tekrar (Linear Recurrences)

**Lineer tekrar**, $f(n)$ fonksiyonunun ilk $k$ değeriyle tanımlandığı ve büyük değerlerin şu formülle hesaplandığı bir yapıdır:

$$f(n) = c_1 f(n-1) + c_2 f(n-2) + \cdots + c_k f(n-k)$$

Dinamik programlamayla tüm değerleri soldan sağa hesaplamak $O(kn)$ zaman alır. Ancak $k$ küçükse matris işlemleriyle $f(n)$, $O(k^3 \log n)$ zamanda hesaplanabilir.

### Fibonacci Sayıları

Fibonacci tekrarı $k = 2$, $c_1 = c_2 = 1$ olan özel bir lineer tekrardır:

$$f(0) = 0, \quad f(1) = 1, \quad f(n) = f(n-1) + f(n-2)$$

$2 \times 2$ boyutundaki $X$ matrisiyle şu ilişki kurulur:

$$X \cdot \begin{bmatrix} f(i) \\ f(i+1) \end{bmatrix} = \begin{bmatrix} f(i+1) \\ f(i+2) \end{bmatrix}$$

Bu dönüşümü gerçekleştiren matris:

$$X = \begin{bmatrix} 0 & 1 \\ 1 & 1 \end{bmatrix}$$

Dolayısıyla:

$$\begin{bmatrix} f(n) \\ f(n+1) \end{bmatrix} = X^n \cdot \begin{bmatrix} 0 \\ 1 \end{bmatrix}$$

$X^n$ matrisi $O(\log n)$ zamanda hesaplandığından $f(n)$ de $O(\log n)$ zamanda bulunur. Örneğin:

$$\begin{bmatrix} 0 & 1 \\ 1 & 1 \end{bmatrix} \cdot \begin{bmatrix} 5 \\ 8 \end{bmatrix} = \begin{bmatrix} 8 \\ 13 \end{bmatrix}$$

### Genel Durum

Genel $k$'lı lineer tekrar için $k \times k$ boyutundaki dönüşüm matrisi:

$$X = \begin{bmatrix}
0 & 1 & 0 & 0 & \cdots & 0 \\
0 & 0 & 1 & 0 & \cdots & 0 \\
0 & 0 & 0 & 1 & \cdots & 0 \\
\vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\
0 & 0 & 0 & 0 & \cdots & 1 \\
c_k & c_{k-1} & c_{k-2} & c_{k-3} & \cdots & c_1
\end{bmatrix}$$

İlk $k-1$ satır her değeri bir sonrakiyle kaydırır; son satır tekrarın katsayılarını taşır. Bu matrisle:

$$\begin{bmatrix} f(n) \\ f(n+1) \\ \vdots \\ f(n+k-1) \end{bmatrix} = X^n \cdot \begin{bmatrix} f(0) \\ f(1) \\ \vdots \\ f(k-1) \end{bmatrix}$$

Bu formül $O(k^3 \log n)$ zamanda çalışır.

## 23.3 Çizgeler ve Matrisler

### Yolları Saymak

Ağırlıksız bir çizgenin **komşuluk matrisi** $V$ için, $V^n$ matrisinin $V^n[i,j]$ elemanı $i$'den $j$'ye tam $n$ kenarlık yolların sayısını verir.

Örneğin 6 düğümlü bir çizgenin komşuluk matrisi $V$'yi hesaplayıp $V^4$'ü bulursak:

$$V^4[2,5] = 2$$

Bu, 2. düğümden 5. düğüme 4 kenarlı iki farklı yol bulunduğunu söyler: $2 \to 1 \to 4 \to 2 \to 5$ ve $2 \to 6 \to 3 \to 2 \to 5$.

### En Kısa Yollar

Aynı fikir ağırlıklı çizgelerde **en kısa yol** bulmak için de kullanılabilir. Standart matris çarpımındaki toplam ve çarpım işlemleri aşağıdaki gibi değiştirilir:

$$AB[i,j] = \min_{k=1}^{n} \bigl(A[i,k] + B[k,j]\bigr)$$

Başlangıç değerleri olarak komşuluk matrisinde kenar ağırlıkları, kenar olmayan yerlerde $\infty$ kullanılır. Bu yapıyla $V^n[i,j]$, $i$'den $j$'ye tam $n$ kenarlık yolların en kısa uzunluğuna eşittir.

Örneğin ağırlıklı bir çizgede:

$$V^4[2,5] = 8$$

Bu değer, $2 \to 1 \to 4 \to 2 \to 5$ yoluna karşılık gelir.

### Kirchhoff'un Teoremi

**Kirchhoff'un Teoremi**, bir çizgenin toplam kapsayan ağaç sayısını **Laplacian matrisin** determinantı yardımıyla hesaplar.

**Laplacian matris** $L$ şöyle tanımlanır:

$$L[i, j] = \begin{cases} \deg(i) & i = j \\ -1 & i \neq j \text{ ve } (i,j) \text{ kenarı var} \\ 0 & \text{aksi hâlde} \end{cases}$$

Toplam kapsayan ağaç sayısı, $L$'den herhangi bir satır ve sütun çıkarıldıktan sonra kalan matrisin determinantına eşittir; hangi satır-sütun çıkarılırsa çıkarılsın sonuç değişmez.

**Örnek:** 4 düğümlü tam çizgede (her düğüm çifti arasında kenar var) kapsayan ağaçların sayısını bulalım. Laplacian matris:

$$L = \begin{pmatrix} 3 & -1 & -1 & -1 \\ -1 & 1 & 0 & 0 \\ -1 & 0 & 2 & -1 \\ -1 & 0 & -1 & 2 \end{pmatrix}$$

İlk satır ve sütun çıkarıldıktan sonra:

$$\det\begin{pmatrix} 1 & 0 & 0 \\ 0 & 2 & -1 \\ 0 & -1 & 2 \end{pmatrix} = 3$$

Gerçekten bu çizgenin 3 farklı kapsayan ağacı vardır.

**Cayley'in Formülüyle bağlantı:** $n$ düğümlü tam çizgenin Laplacian matrisinin herhangi bir $(n-1) \times (n-1)$ alt determinantı $n^{n-2}$ olduğundan, Cayley'in Formülü Kirchhoff'un Teoreminin özel bir durumudur.
