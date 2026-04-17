---
layout: post
title: Rekabetçi Programcı Sayılar Teorisi
math: true
excerpt_separator: "``"
categories:
  - Program
tags:
  - sayılar-teorisi
  - number-theory
  - asal-sayı
  - prime
  - eratosten-kalburu
  - sieve-of-eratosthenes
  - öklid
  - gcd
  - lcm
  - euler-totient
  - modüler-aritmetik
  - modular-exponentiation
  - fermat
  - çin-kalan-teoremi
  - diyofantus
  - pisagor
  - wilson
  - c
  - programlama
  - algoritma
  - olimpiyat
  - yarışma
  - kodlama
  - matematik
  - kitap
---

Sayılar teorisi, matematiğin tam sayılarla ilgilenen alt dalıdır. İlginç bir konudur; çünkü tam sayı içeren pek çok soru ilk bakışta kolay görünse de çözümü son derece zor olabilir. Örneğin $x^3 + y^3 + z^3 = 33$ eşitliğini sağlayan üç tam sayı bulmak hâlâ açık bir matematik problemidir.

Bu bölümde sayılar teorisinin rekabetçi programlamada sık karşılaşılan temel kavramları ve algoritmaları ele alınmaktadır.
``

## 21.1 Asal Sayılar ve Bölenler

$a$ sayısı $b$ sayısını bölüyorsa $a$, $b$'nin **böleni** ya da **çarpanı** olarak adlandırılır; $a \mid b$ ile gösterilir. Örneğin 24'ün bölenleri $1, 2, 3, 4, 6, 8, 12, 24$'tür.

$n > 1$ olan bir sayı yalnızca $1$ ve kendisine bölünebiliyorsa **asal sayıdır**. Her $n > 1$ için **tekil bir asal çarpanlara ayrılma** mevcuttur:

$$n = p_1^{\alpha_1} p_2^{\alpha_2} \cdots p_k^{\alpha_k}$$

Örneğin $84 = 2^2 \cdot 3^1 \cdot 7^1$.

### Çarpan Sayısı, Toplamı ve Çarpımı

$n$'nin **çarpan sayısı:**

$$\tau(n) = \prod_{i=1}^{k} (\alpha_i + 1)$$

Örneğin $\tau(84) = 3 \cdot 2 \cdot 2 = 12$.

$n$'nin **çarpanlarının toplamı:**

$$\sigma(n) = \prod_{i=1}^{k} \frac{p_i^{\alpha_i + 1} - 1}{p_i - 1}$$

Örneğin $\sigma(84) = \dfrac{2^3 - 1}{2-1} \cdot \dfrac{3^2 - 1}{3-1} \cdot \dfrac{7^2 - 1}{7-1} = 7 \cdot 4 \cdot 8 = 224$.

$n$'nin **çarpanlarının çarpımı:**

$$\mu(n) = n^{\tau(n)/2}$$

Çarpanlar $\tau(n)/2$ çift oluşturur. Örneğin $84$'ün çarpanları $1 \cdot 84,\ 2 \cdot 42,\ 3 \cdot 28, \ldots$ çiftlerini oluşturur ve $\mu(84) = 84^6$.

Bir sayı $n = \sigma(n) - n$ ise **mükemmel sayıdır**; yani 1'den $n-1$'e kadar olan çarpanlarının toplamına eşittir. Örneğin $28 = 1 + 2 + 4 + 7 + 14$.

### Asal Sayıların Sayısı ve Yoğunluğu

Sonsuz sayıda asal sayı vardır. Bunu çelişkiyle kanıtlayabiliriz: sonlu sayıda asal olsaydı $p_1 p_2 \cdots p_n + 1$ bu listenin hiçbir elemanına bölünemeyecek yeni bir asal oluştururdu.

$\pi(n)$, 1 ile $n$ arasındaki asal sayı adedini gösterir. Asal sayıların yoğunluğu için şu yaklaşım geçerlidir:

$$\pi(n) \approx \frac{n}{\ln n}$$

Örneğin $\pi(10^6) = 78498$ iken $10^6 / \ln 10^6 \approx 72382$.

### Ünlü Konjektürler

Kanıtlanamamış fakat doğru olduğu güçlü biçimde düşünülen açık problemler:

- **Goldbach'ın Konjektürü:** Her $n > 2$ çift sayısı iki asal sayının toplamı olarak yazılabilir.
- **İkiz Asal Konjektürü:** $p$ ve $p+2$'nin her ikisinin de asal olduğu sonsuz sayıda $\{p, p+2\}$ çifti vardır.
- **Legendre'nin Konjektürü:** Her pozitif $n$ için $n^2$ ile $(n+1)^2$ arasında en az bir asal sayı bulunur.

### Asal Sayı Testi ve Çarpanlara Ayırma

$n$ asal değilse $a \cdot b = n$ çarpımında $a \leq \sqrt{n}$ ya da $b \leq \sqrt{n}$ olmak zorundadır. Bu gözlem $O(\sqrt{n})$ zamanlı basit algoritmaların temelini oluşturur.

```cpp
bool prime(int n) {
    if (n < 2) return false;
    for (int x = 2; x * x <= n; x++) {
        if (n % x == 0) return false;
    }
    return true;
}
```

```cpp
vector<int> factors(int n) {
    vector<int> f;
    for (int x = 2; x * x <= n; x++) {
        while (n % x == 0) {
            f.push_back(x);
            n /= x;
        }
    }
    if (n > 1) f.push_back(n);
    return f;
}
```

Örneğin $24 = 2^3 \cdot 3$ için `factors(24)` sonucu `[2, 2, 2, 3]` olur.

### Eratosten Kalburu

**Eratosten Kalburu (Sieve of Eratosthenes)**, $2 \ldots n$ arasındaki her sayının asal olup olmadığını ve değilse bir asal çarpanını $O(n \log \log n)$ zamanda bulan ön işleme algoritmasıdır.

`sieve[k] = 0` ise $k$ asaldır; `sieve[k] != 0` ise `sieve[k]`, $k$'nın asal çarpanlarından biridir.

```cpp
for (int x = 2; x <= n; x++) {
    if (sieve[x]) continue;
    for (int u = 2 * x; u <= n; u += x) {
        sieve[u] = x;
    }
}
```

Örneğin $n = 20$ için dizi:

| 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| 0 | 0 | 2 | 0 | 3 | 0 | 2 | 3 | 5  | 0  | 3  | 0  | 7  | 5  | 2  | 0  | 3  | 0  | 5  |

İç döngü yalnızca $x$ asal olduğunda çalıştığından gerçek karmaşıklık $O(n \log \log n)$'dir; bu değer $O(n)$'e çok yakındır.

### Öklid'in Algoritması

$\gcd(a, b)$, hem $a$ hem $b$'yi bölen en büyük sayıdır. $\text{lcm}(a, b)$ ise her ikisi tarafından bölünebilen en küçük sayıdır. İkisi arasındaki ilişki:

$$\text{lcm}(a, b) = \frac{ab}{\gcd(a, b)}$$

Öklid'in Algoritması M.Ö. 300'lere uzanan, bilinen en eski algoritmalardan biridir:

$$\gcd(a, b) = \begin{cases} a & b = 0 \\ \gcd(b,\ a \bmod b) & b \neq 0 \end{cases}$$

```cpp
int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}
```

Algoritma $O(\log \min(a, b))$ zamanda çalışır. En kötü durum ardışık Fibonacci sayılarının girdi olarak verilmesidir; örneğin $\gcd(13, 8) = \gcd(8, 5) = \gcd(5, 3) = \cdots = 1$.

### Euler'in Totient Fonksiyonu

$\gcd(a, b) = 1$ ise $a$ ve $b$ **aralarında asaldır**. **Euler'in Totient Fonksiyonu** $\varphi(n)$, $1$'den $n$'e kadar $n$ ile aralarında asal olan sayıların adedini verir. Asal çarpanlardan hesaplama formülü:

$$\varphi(n) = \prod_{i=1}^{k} p_i^{\alpha_i - 1}(p_i - 1)$$

Örneğin $\varphi(12) = 2^1 \cdot (2-1) \cdot 3^0 \cdot (3-1) = 4$. $n$ asal ise $\varphi(n) = n - 1$.

## 21.2 Modüler Aritmetik

Modüler aritmetikte sayılar $0, 1, 2, \ldots, m-1$ aralığına sıkıştırılır; her $x$ sayısı $x \bmod m$ ile temsil edilir. Temel işlem özellikleri:

$$\begin{aligned}
(x + y) \bmod m &= (x \bmod m + y \bmod m) \bmod m \\
(x - y) \bmod m &= (x \bmod m - y \bmod m) \bmod m \\
(x \cdot y) \bmod m &= (x \bmod m \cdot y \bmod m) \bmod m \\
x^n \bmod m &= (x \bmod m)^n \bmod m
\end{aligned}$$

### Modüler Üs Alma

$x^n \bmod m$ değerini $O(\log n)$ zamanda hesaplamak için hızlı kuvvet alma kullanılır:

$$x^n = \begin{cases} 1 & n = 0 \\ x^{n/2} \cdot x^{n/2} & n \text{ çift} \\ x^{n-1} \cdot x & n \text{ tek} \end{cases}$$

```cpp
int modpow(int x, int n, int m) {
    if (n == 0) return 1 % m;
    long long u = modpow(x, n / 2, m);
    u = (u * u) % m;
    if (n % 2 == 1) u = (u * x) % m;
    return u;
}
```

### Fermat'ın Teoremi ve Euler'in Teoremi

$m$ asal ve $\gcd(x, m) = 1$ iken **Fermat'ın Küçük Teoremi**:

$$x^{m-1} \bmod m = 1$$

Bu aynı zamanda $x^k \bmod m = x^{k \bmod (m-1)} \bmod m$ bağıntısını verir. Daha genel haliyle **Euler'in Teoremi**, $\gcd(x, m) = 1$ iken:

$$x^{\varphi(m)} \bmod m = 1$$

Fermat'ın Teoremi bu sonucun $m$ asal olduğundaki özel durumudur çünkü $\varphi(m) = m - 1$.

### Modüler Çarpımsal Ters

$x$ sayısının $m$ modülündeki **çarpımsal tersi** $x^{-1}$, şu koşulu sağlayan sayıdır:

$$x \cdot x^{-1} \bmod m = 1$$

Bu ters, $x$ ile $m$ aralarında asal olduğunda her zaman mevcuttur. Örneğin $x = 6$, $m = 17$ için $x^{-1} = 3$ çünkü $6 \cdot 3 \bmod 17 = 1$. Modüler ters, modüler aritmetikte bölme işlemini mümkün kılar: $x$'e bölmek $x^{-1}$ ile çarpmaya eşdeğerdir.

Euler'in Teoreminden çarpımsal ters şöyle türetilir:

$$x^{-1} = x^{\varphi(m) - 1}$$

$m$ asal ise $x^{-1} = x^{m-2}$ olur. `modpow` ile verimli hesaplanır:

$$6^{-1} \bmod 17 = 6^{15} \bmod 17 = 3$$

**C++ notu:** `unsigned int` türü $2^{32}$ ile doğal sarılma yapar; bu özellik bilinçli olarak modüler aritmetik hesaplamalarda kullanılabilir:

```cpp
unsigned int x = 123456789;
cout << x * x << "\n";  // 123456789^2 mod 2^32 = 2537071545
```

## 21.3 Eşitlikleri Çözmek

### Diyofantus Eşitlikleri

**Diyofantus eşitliği**, tam sayı çözüm aranan $ax + by = c$ biçimindeki denklemdir. Çözülebilmesi için gerekli ve yeterli koşul $\gcd(a, b) \mid c$'dir.

Çözüm **genişletilmiş Öklid algoritması** ile bulunur: önce $ax + by = \gcd(a, b)$ formu çözülür, ardından $c / \gcd(a, b)$ ile ölçeklenir.

**Örnek:** $39x + 15y = 12$. $\gcd(39, 15) = 3$ ve $3 \mid 12$ olduğundan çözülebilir. Öklid adımları:

$$39 - 2 \cdot 15 = 9, \quad 15 - 1 \cdot 9 = 6, \quad 9 - 1 \cdot 6 = 3$$

Geri izleyerek $39 \cdot 2 + 15 \cdot (-5) = 3$ elde edilir; $4$ ile çarpılırsa:

$$39 \cdot 8 + 15 \cdot (-20) = 12$$

Bir çözüm bulunduğunda sonsuz çözüm elde edilir. $(x, y)$ bir çözümse, her tam sayı $k$ için şu çift de çözümdür:

$$\left(x + \frac{kb}{\gcd(a,b)},\quad y - \frac{ka}{\gcd(a,b)}\right)$$

### Çin Kalan Teoremi

**Çin Kalan Teoremi (CRT)**, ikili aralarında asal modüllere sahip eşitlik sistemini çözer:

$$x \equiv a_1 \pmod{m_1}, \quad x \equiv a_2 \pmod{m_2}, \quad \ldots, \quad x \equiv a_n \pmod{m_n}$$

$X_k = m_1 m_2 \cdots m_n / m_k$ ve $X_k^{-1}$, $X_k$'nın $m_k$ modülündeki çarpımsal tersi olmak üzere çözüm:

$$x = a_1 X_1 X_1^{-1} + a_2 X_2 X_2^{-1} + \cdots + a_n X_n X_n^{-1}$$

**Örnek:**

$$x \equiv 3 \pmod{5}, \quad x \equiv 4 \pmod{7}, \quad x \equiv 2 \pmod{3}$$

$$x = 3 \cdot 21 \cdot 1 + 4 \cdot 15 \cdot 1 + 2 \cdot 35 \cdot 2 = 263$$

Bir çözüm bulunduğunda $x + m_1 m_2 \cdots m_n$ biçimindeki tüm sayılar da çözümdür.

## 21.4 Diğer Sonuçlar

### Lagrange'ın Teoremi

Her pozitif tam sayı en fazla **dört tam karenin toplamı** olarak ifade edilebilir:

$$n = a^2 + b^2 + c^2 + d^2$$

Örneğin $123 = 8^2 + 5^2 + 5^2 + 3^2$.

### Zeckendorf'un Teoremi

Her pozitif tam sayı, birbirini takip etmeyen **farklı Fibonacci sayılarının toplamı** olarak tek türlü yazılabilir. Örneğin $74 = 55 + 13 + 5 + 1$.

### Pisagor Üçlüleri

$a^2 + b^2 = c^2$ bağıntısını sağlayan $(a, b, c)$ tam sayı üçlüsüne **Pisagor üçlüsü** denir. $(a, b, c)$ Pisagor üçlüsüyse her $k > 1$ için $(ka, kb, kc)$ de Pisagor üçlüsüdür. $a$, $b$ ve $c$ aralarında asal ise üçlü **basittir** (primitive). Tüm basit Pisagor üçlüleri **Öklid'in formülü** ile oluşturulur:

$$\left(n^2 - m^2,\ 2nm,\ n^2 + m^2\right)$$

Burada $0 < m < n$, $n$ ve $m$ aralarında asal ve en az biri çifttir. Örneğin $m = 1$, $n = 2$ için $(3, 4, 5)$ elde edilir.

### Wilson'un Teoremi

$n$ sayısı asal olmak ve ancak olmak üzere:

$$(n-1)! \bmod n = n - 1$$

Örneğin $10! \bmod 11 = 10$ olduğundan 11 asaldır; $11! \bmod 12 = 0 \neq 11$ olduğundan 12 asal değildir. Pratikte $(n-1)!$ büyük $n$ için hesaplanamaz; bu nedenle asal testi açısından teorik önemi büyük olsa da pratik kullanımı sınırlıdır.
