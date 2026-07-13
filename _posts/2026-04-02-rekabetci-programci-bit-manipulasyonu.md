---
layout: post
title: Rekabetçi Programcı Bit Manipülasyonu
math: true
categories:
  - Program
tags:
  - bit
  - bit-manipulasyonu
  - c
  - programlama
  - algoritma
  - olimpiyat
  - dizi
  - yarışma
  - dinamik-programlama
  - altküme
  - optimizasyon
  - kodlama
  - matematik
  - kitap
redirect_from:
  - /posts/rekabetci-programci-bit-manipulasyonu/
---

Bilgisayar programlarındaki tüm veriler bit olarak yani 0 ve 1 sayıları biçiminde tutulur. Bu bölüm tam sayıların bit gösterimlerini açıklayıp bit operasyonlarının kullanıldığı örneklere değinecektir. Algoritma programlamasında bit manipülasyonunu kullanmanın pek çok farklı yolu vardır.

## 10.1 Bit Gösterimi

Programlamada bir $n$ bitlik tamsayı, $n$ bitten oluşan bir binary sayısı olarak tutulur. Örneğin C++'da `int` 32-bit olup her `int` sayısı 32 bitten oluşur.

`int 43` sayısının [bit gösterimi](https://sonsuzus.github.io/search.html?q=bit%20g%C3%B6sterimi):

```
00000000000000000000000000101011
```

Gösterimdeki bitler sağdan sola sıralanır. Bit gösterimi $b_k \cdots b_2 b_1 b_0$ olan bir sayıya dönüştürmek için:

$$b_k 2^k + \ldots + b_2 2^2 + b_1 2^1 + b_0 2^0$$

Örneğin $1 \cdot 2^5 + 1 \cdot 2^3 + 1 \cdot 2^1 + 1 \cdot 2^0 = 43$.

### Signed ve Unsigned Gösterim

Bir sayının bit gösterimi ya **signed** ya da **unsigned** olur.

**Signed** gösterimde hem negatif hem pozitif sayılar tutulabilir. $n$ bitlik bir signed değişken $-2^{n-1}$ ile $2^{n-1}-1$ arasındaki herhangi bir tamsayıyı tutabilir. C++'da `int` signed'dır; $-2^{31}$ ile $2^{31}-1$ arasındaki değerleri alabilir. Signed gösterimde ilk bit işaret bitidir (negatif olmayan sayılar için 0, negatifler için 1). Negatifler **ikinin tümleyeni** (Two's Complement) ile gösterilir: tüm bitler tersine çevrilir ve 1 eklenir. Örneğin `int -43` sayısının bit gösterimi:

```
11111111111111111111111111010101
```

**Unsigned** gösterimde yalnızca negatif olmayan sayılar kullanılır; buna karşın üst sınır daha yüksektir. $n$ bitlik bir unsigned değişken $0$ ile $2^n - 1$ arasındaki değerleri tutabilir. C++'da `unsigned int` değişkeni $0$ ile $2^{32}-1$ arasında olabilir.

İki gösterim arasındaki ilişki: bir signed sayı $-x$, unsigned sayı $2^n - x$'e eşittir.

```cpp
int x = -43;
unsigned int y = x;
cout << x << "\n"; // -43
cout << y << "\n"; // 4294967253
```

### Overflow

Bir sayı bit gösteriminin üst sınırını aşarsa **[overflow](https://sonsuzus.github.io/search.html?q=overflow)** oluşur. Signed gösterimde $2^{n-1}-1$'den sonraki sayı $-2^{n-1}$ olur; unsigned gösterimde $2^n - 1$'den sonraki sayı $0$ olur.

```cpp
int x = 2147483647; // 2^31 - 1
x++;
cout << x << "\n"; // -2147483648
```

## 10.2 Bit Operasyonları

### Ve (AND) Operasyonu

`x & y`, hem $x$'te hem $y$'de 1 olan bitlerde 1, diğerlerinde 0 içerir. Örneğin $22\ \&\ 26 = 18$:

```
  10110  (22)
& 11010  (26)
= 10010  (18)
```

AND operasyonu ile bir $x$ sayısının çift olup olmadığını kontrol edebiliriz: $x$ çiftse `x & 1 = 0`, tekse `x & 1 = 1`. Genel olarak `x & (2^k - 1) = 0` ise $x$, $2^k$'ya bölünebiliyordur.

### Veya (OR) Operasyonu

`x | y`, $x$ veya $y$'den en az birinde 1 biti olan pozisyonlarda 1 içerir. Örneğin $22\ |\ 26 = 30$:

```
  10110  (22)
| 11010  (26)
= 11110  (30)
```

### XOR Operasyonu

`x ^ y`, $x$ ya da $y$'den yalnızca birinde 1 bulunan pozisyonlarda 1 içerir. Örneğin $22\ \hat{}\ 26 = 12$:

```
  10110  (22)
^ 11010  (26)
= 01100  (12)
```

### Ters (NOT) Operasyonu

`~x`, $x$'in tüm bitlerini tersine çevirir. $\sim x = -x - 1$ formülü geçerlidir. Örneğin `~29 = -30`. 32-bit `int` için:

```
 x =  29   00000000000000000000000000011101
~x = -30   11111111111111111111111111100010
```

### Bit Kaydırması

Sol kaydırma `x << k`, sayıya $k$ tane 0 biti ekler ($x \cdot 2^k$). Sağ kaydırma `x >> k`, sayıdan son $k$ biti çıkarır ($\lfloor x / 2^k \rfloor$). Örneğin $14 \ll 2 = 56$ (`1110` → `111000`) ve $49 \gg 3 = 6$ (`110001` → `110`).

### Uygulamalar

`1 << k` formundaki sayı, yalnızca $k$. pozisyonda 1 biti içerir; bu sayede tek bitlere erişebiliriz. $x$'in $k$. biti, `x & (1 << k)` sıfır olmadığında 1'dir. Aşağıdaki kod bir `int x` sayısının bit gösterimini yazdırır:

```cpp
for (int i = 31; i >= 0; i--) {
    if (x & (1 << i)) cout << "1";
    else cout << "0";
}
```

Benzer fikirlerle bitleri değiştirmek de mümkündür:

| İşlem | Formül |
|---|---|
| $k$. biti 1'e çevir | `x \| (1 << k)` |
| $k$. biti 0'a çevir | `x & ~(1 << k)` |
| $k$. biti tersine çevir | `x ^ (1 << k)` |
| Son 1 bitini sıfırla | `x & (x-1)` |
| Son 1 biti hariç tümünü sıfırla | `x & -x` |

`x & (x-1) = 0` ise $x$ pozitif sayısı ikinin kuvvetidir.

### g++ Yerleşik Fonksiyonları

g++ derleyicisi bit sayımı için hazır fonksiyonlar sunar:

```cpp
int x = 5328; // 00000000000000000000010100110100000
cout << __builtin_clz(x)      << "\n"; // 19  (baştaki 0 sayısı)
cout << __builtin_ctz(x)      << "\n"; // 4   (sondaki 0 sayısı)
cout << __builtin_popcount(x) << "\n"; // 5   (1 bit sayısı)
cout << __builtin_parity(x)   << "\n"; // 1   (1 bitlerinin tek/çift paritesi)
```

`long long` sayılar için aynı fonksiyonların `ll` ön ekli versiyonları kullanılır: `__builtin_popcountll` vb.

## 10.3 Kümeleri Göstermek

$\{0, 1, 2, \ldots, n-1\}$ kümesinin her alt kümesi, $n$ bitten oluşan bir tamsayıyla gösterilebilir. 1 bitleri alt kümeye ait elemanları belirtir. Bu yöntem son derece verimlidir: her eleman yalnızca bir bit hafıza gerektirir ve küme operasyonları doğrudan bit operasyonlarına dönüşür.

Örneğin `int` 32-bit olduğundan bir `int` sayısı, $\{0, 1, \ldots, 31\}$ kümesinin herhangi bir alt kümesini gösterebilir. $\{1, 3, 4, 8\}$ kümesinin bit gösterimi:

```
00000000000000000000000100011010
```

Bu $2^8 + 2^4 + 2^3 + 2^1 = 282$ sayısına karşılık gelir.

### Küme İmplementasyonu

```cpp
int x = 0;
x |= (1 << 1);  // {1}
x |= (1 << 3);  // {1, 3}
x |= (1 << 4);  // {1, 3, 4}
x |= (1 << 8);  // {1, 3, 4, 8}
cout << __builtin_popcount(x) << "\n"; // 4
```

Kümeye ait elemanları yazdırmak:

```cpp
for (int i = 0; i < 32; i++) {
    if (x & (1 << i)) cout << i << " ";
}
// çıktı: 1 3 4 8
```

### Küme Operasyonları

| Küme işlemi | Bit işlemi |
|---|---|
| Kesişim $a \cap b$ | `a & b` |
| Birleşim $a \cup b$ | `a \| b` |
| Tümlayan $\bar{a}$ | `~a` |
| Fark $a \setminus b$ | `a & (~b)` |

Örneğin $x = \{1,3,4,8\}$ ve $y = \{3,6,8,9\}$ için birleşim $z = x \cup y = \{1,3,4,6,8,9\}$:

```cpp
int x = (1<<1)|(1<<3)|(1<<4)|(1<<8);
int y = (1<<3)|(1<<6)|(1<<8)|(1<<9);
int z = x | y;
cout << __builtin_popcount(z) << "\n"; // 6
```

### Altkümelerden Geçmek

$\{0, 1, \ldots, n-1\}$ kümesinin tüm alt kümelerinden geçmek:

```cpp
for (int b = 0; b < (1 << n); b++) {
    // b alt kümesini işle
}
```

Tam $k$ elemanlı alt kümelerden geçmek:

```cpp
for (int b = 0; b < (1 << n); b++) {
    if (__builtin_popcount(b) == k) {
        // b alt kümesini işle
    }
}
```

Bir $x$ kümesinin tüm alt kümelerinden geçmek:

```cpp
int b = 0;
do {
    // b alt kümesini işle
} while (b = (b - x) & x);
```

## 10.4 Bit Optimizasyonu

Çoğu algoritma bit operasyonları ile optimize edilebilir. Bu optimizasyonlar zaman karmaşıklığını değiştirmez; ancak gerçek çalışma süresinde büyük fark yaratabilir.

### Hamming Mesafeleri

**Hamming mesafesi** $\text{hamming}(a, b)$, eşit uzunluktaki $a$ ve $b$ yazılarının farklı olduğu konum sayısıdır. Örneğin $\text{hamming}(01101,\ 11001) = 2$.

Her biri $k$ uzunluğunda $n$ adet bit yazısından oluşan bir listede minimum Hamming mesafesini bulmak istersek naif çözüm $O(n^2 k)$ sürer:

```cpp
int hamming(string a, string b) {
    int d = 0;
    for (int i = 0; i < k; i++) {
        if (a[i] != b[i]) d++;
    }
    return d;
}
```

$k \leq 32$ ise yazıları `int` olarak tutup XOR + popcount ile çok daha hızlı hesaplayabiliriz:

```cpp
int hamming(int a, int b) {
    return __builtin_popcount(a ^ b);
}
```

XOR operasyonu, $a$ ve $b$'nin farklı olduğu pozisyonlarda 1 içeren bir sayı üretir; `__builtin_popcount` ise bu 1 bitlerini sayar.

30 uzunluğundaki 10.000 rastgele bit yazısından oluşan bir listede bu iki yaklaşım karşılaştırılmış; naif yöntem 13.5 saniye, bit optimize versiyonu ise yalnızca **0.5 saniye** sürmüştür. Yaklaşık **27 kat** hızlanma.

### Alt Izgaraları Saymak

$n \times n$'lik bir ızgarada her kare ya siyah (1) ya da beyaz (0) olsun. Tüm köşeleri siyah olan alt ızgara sayısını bulmak istiyoruz.

Naif $O(n^3)$ çözümde tüm $O(n^2)$ satır çifti $(a, b)$ için her iki satırda aynı anda siyah olan sütunları sayıp $\binom{\text{count}}{2}$ ile çarpıyoruz:

```cpp
int count = 0;
for (int i = 0; i < n; i++) {
    if (color[a][i] == 1 && color[b][i] == 1) count++;
}
```

Bit optimizasyonunda ızgarayı $N$ sütunluk bloklara bölüp her satırı $N$-bitlik tamsayı listesi olarak tutarız. Böylece $N$ sütunu aynı anda AND + popcount ile işleyebiliriz:

```cpp
int count = 0;
for (int i = 0; i <= n / N; i++) {
    count += __builtin_popcount(color[a][i] & color[b][i]);
}
```

Bu sayede algoritma $O(n^3/N)$ zamana düşer. $2500 \times 2500$ rastgele ızgarada yapılan karşılaştırmada: orijinal kod 29.6 saniye, $N=32$ (int) ile 3.1 saniye, $N=64$ (long long) ile **1.7 saniye** sürmüştür.

## 10.5 Dinamik Programlama

Bit operasyonları, elemanların alt kümelerini içeren dinamik programlama algoritmalarını hem verimli hem de temiz biçimde yazmamızı sağlar; çünkü durumları birer sayı olarak tutabiliriz.

### Optimal Seçim

$k$ ürünün $n$ gündeki fiyatları verildiğinde her ürünü tam bir kez ve günde en fazla bir ürün alarak minimum toplam ücret nedir?

$\text{price}[x][d]$, $x$ ürününün $d$. gündeki fiyatı olsun. $\text{total}(S, d)$ ise $S$ alt kümesindeki ürünleri $d$. güne kadar almayı sağlayan minimum toplam ücret olsun. Hedef $\text{total}(\{0 \ldots k-1\},\ n-1)$ değeridir.

Temel durumlar: $\text{total}(\emptyset, d) = 0$ ve $\text{total}(\{x\}, 0) = \text{price}[x][0]$. Genel özyineleme:

$$\text{total}(S, d) = \min\!\Bigl(\text{total}(S, d-1),\ \min_{x \in S}\bigl(\text{total}(S \setminus \{x\}, d-1) + \text{price}[x][d]\bigr)\Bigr)$$

Dinamik programlama ile implementasyon:

```cpp
int total[1 << K][N];

// d = 0 başlangıç durumları
for (int x = 0; x < k; x++) {
    total[1 << x][0] = price[x][0];
}

// DP geçişi
for (int d = 1; d < n; d++) {
    for (int s = 0; s < (1 << k); s++) {
        total[s][d] = total[s][d - 1];
        for (int x = 0; x < k; x++) {
            if (s & (1 << x)) {
                total[s][d] = min(total[s][d],
                    total[s ^ (1 << x)][d - 1] + price[x][d]);
            }
        }
    }
}
```

Algoritmanın zaman karmaşıklığı $O(n \cdot 2^k \cdot k)$ olur.

### Permütasyonlardan Altkümelere

Permütasyonlar yerine altkümelere bakmak büyük avantaj sağlayabilir: $n = 20$ için $n! \approx 2.4 \times 10^{18}$ iken $2^n \approx 10^6$'dır[^1].

Örnek problem: Maksimum kapasitesi $x$ olan bir asansörle $n$ insanı en az kaç turda taşıyabiliriz?

$\text{rides}(S)$ = $S$ alt kümesini taşımak için gereken minimum tur sayısı, $\text{last}(S)$ = son turdaki minimum toplam ağırlık olsun. Hedef $\text{rides}(\{0 \ldots n-1\})$.

```cpp
pair<int,int> best[1 << N];
best[0] = {1, 0};

for (int s = 1; s < (1 << n); s++) {
    best[s] = {n + 1, 0};
    for (int p = 0; p < n; p++) {
        if (s & (1 << p)) {
            auto option = best[s ^ (1 << p)];
            if (option.second + weight[p] <= x) {
                // p'yi mevcut tura ekle
                option.second += weight[p];
            } else {
                // p için yeni tur oluştur
                option.first++;
                option.second = weight[p];
            }
            best[s] = min(best[s], option);
        }
    }
}
```

Döngü, $S_1 \subseteq S_2$ olduğunda $S_1$'i her zaman $S_2$'den önce işler; bu sayede DP değerleri doğru sırada hesaplanır. Zaman karmaşıklığı $O(2^n \cdot n)$.

### Altkümeleri Saymak

Her $S \subseteq X$ alt kümesi için bir $\text{value}[S]$ tamsayısı tanımlansın. Her $S$ için alt kümelerinin değer toplamını hesaplamak istiyoruz:

$$\text{sum}(S) = \sum_{A \subseteq S} \text{value}[A]$$

Naif çözüm tüm $O(2^{2n})$ alt küme çiftlerini dener. Daha akıllı yaklaşım için $\text{partial}(S, k)$, $S$'ten yalnızca $0 \ldots k$ elemanlarının çıkarılabildiği durumdaki toplamı versin:

$$\text{partial}(S, k) = \begin{cases} \text{value}[S] & k \notin S \text{ veya } k = -1 \\ \text{partial}(S, k-1) + \text{partial}(S \setminus \{k\}, k-1) & k \in S \end{cases}$$

$\text{sum}(S) = \text{partial}(S, n-1)$ olduğundan dinamik programlama ile aşağıdaki $O(2^n \cdot n)$ implementasyon elde edilir:

```cpp
int sum[1 << N];

for (int s = 0; s < (1 << n); s++) {
    sum[s] = value[s];
}

for (int k = 0; k < n; k++) {
    for (int s = 0; s < (1 << n); s++) {
        if (s & (1 << k)) sum[s] += sum[s ^ (1 << k)];
    }
}
```

Her $k$ adımında `sum` dizisi yeniden kullanılır; böyle verimli ve sade bir implementasyon elde edilir.

[^1]: Bu teknik 1962 yılında M. Held ve R. M. Karp tarafından bulunmuştur.
