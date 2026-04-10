---
layout: post
title: Rekabetçi Programcı Başlangıç
math: true
categories:
  - Program
tags:
  - c
  - programlama
  - algoritma
  - olimpiyat
  - yarışma
  - kodlama
  - matematik
  - kitap
  - girdi-çıktı
  - veri-tipleri
  - modüler-aritmetik
  - logaritma
  - küme-teorisi
  - ioc
  - icpc
---

**Rekabetçi programlama** iki temel konudan oluşur: uygun algoritmayı bulmak (algoritmanın tasarımı) ve bu algoritmayı doğru biçimde koda geçirmek (implementasyonu).

Algoritma tasarımı için soru çözmek ve matematiksel düşünme gerekir. Soruların analiz edilip yaratıcı bir şekilde çözülmesi önemlidir; algoritmanın hem doğru hem de verimli olması beklenir. Rekabetçi programcıların algoritmalar hakkında teorik bilgiye sahip olması gerekir. Tipik bir soru çözümü genelde bilinen tekniklerle yeni gözlemlerin birleşimidir.

İmplementasyon içinse iyi kodlama bilgisi şarttır. Çözümler belirli test durumlarıyla puanlandığından algoritmayı doğru biçimde koda geçirmek kritik önem taşır. Yarışmalarda kodların kısa ama anlaşılabilir olması, aynı zamanda hızlı yazılması gerekir. Klasik yazılım mühendisliğinin aksine, çözümler genellikle birkaç yüz satırı geçmez ve yarışma sonrası geliştirilmesi gerekmez.

## 1.1 Kodlama Dilleri

Rekabetçi programlamada en çok kullanılan diller **C++**, **Python** ve **Java**'dır. Google Code Jam 2017'de ilk 3000 yarışmacının %79'u C++, %16'sı Python, %8'i Java kullanmıştır.

Çoğu yarışmacı C++'ı en iyi seçenek olarak görür; neredeyse her yarışma sisteminde bulunur, çok hızlı ve verimlidir, kapsamlı bir standart kütüphanesi vardır. Yine de birkaç dilde uzmanlaşmakta fayda var. Örneğin çok büyük sayılar gerektiren problemlerde Python'ın yerleşik büyük sayı desteği işe yarayabilir.

> **Not:** TÜBİTAK Bilim Olimpiyatları'nda yalnızca C/C++ kullanılabilmektedir.

Bu kitaptaki örnek çözümler C++11 standardıyla yazılmıştır.

### C++ Kod Şablonu

```cpp
#include <bits/stdc++.h>

using namespace std;

int main() {
    // çözüm burada yazılır
}
```

`#include <bits/stdc++.h>` satırı, g++ derleyicisine özgü bir özellik olup `iostream`, `vector`, `algorithm` gibi tüm standart kütüphaneleri tek satırda ekler. `using namespace std;` ise `std::cout` yerine doğrudan `cout` yazılmasını sağlar.

Derleme komutu:

```bash
g++ -std=c++11 -O2 -Wall test.cpp -o test
```

Bu komut `test.cpp` dosyasından `test` adlı bir ikili (binary) dosya oluşturur; C++11'i etkinleştirir (`-std=c++11`), kodu optimize eder (`-O2`) ve olası hatalar için uyarı verir (`-Wall`).

## 1.2 Girdi ve Çıktı

Yarışmalarda girdi ve çıktı için standart C++ fonksiyonları `cin` ve `cout` kullanılır. C fonksiyonları `scanf` ve `printf` de tercih edilebilir.

```cpp
int a, b;
string x;
cin >> a >> b >> x;
```

Girdi elemanları arasında boşluk veya yeni satır farkı gözetilmez; yukarıdaki kod her iki girdi biçimini de doğru okur:

```
123 456 monkey
```

```
123    456
monkey
```

Çıktı için:

```cpp
int a = 123, b = 456;
string x = "monkey";
cout << a << " " << b << " " << x << "\n";
```

### Performans İpuçları

Girdi/çıktı işlemleri darboğaz oluşturabileceğinden aşağıdaki iki satır eklenebilir:

```cpp
ios::sync_with_stdio(0);
cin.tie(0);
```

`"\n"` ifadesi `endl`'den daha hızlıdır çünkü `endl` her çağrıda tampon boşaltma (flush) işlemi uygular.

### Satır Okuma ve Bilinmeyen Miktarda Girdi

Boşluk içerebilecek tam bir satırı okumak için:

```cpp
string s;
getline(cin, s);
```

Girdi miktarı bilinmiyorsa:

```cpp
while (cin >> x) {
    // kod
}
```

### Dosya Yönlendirme

Bazı yarışmalarda girdi/çıktı dosya üzerinden yapılır. Kodu değiştirmeden dosyaya yönlendirmek için:

```cpp
freopen("input.txt", "r", stdin);
freopen("output.txt", "w", stdout);
```

## 1.3 Sayılarla Çalışmak

### Tam Sayılar

En çok kullanılan tam sayı tipi **`int`**'tir (32-bit): $-2^{31} \ldots 2^{31} - 1$, yaklaşık $\pm 2 \cdot 10^9$ aralığı. Bu aralık yetmediğinde **`long long`** (64-bit) kullanılır: $-2^{63} \ldots 2^{63} - 1$, yaklaşık $\pm 9 \cdot 10^{18}$ aralığı.

```cpp
long long x = 123456789123456789LL;
```

Sayının sonundaki `LL` son eki, değerin `long long` türünde olduğunu belirtir.

**Sık yapılan hata:** `long long` kullanılıyor olsa bile aritmetik işlemde `int` değişkenler varsa sonuç `int` olarak hesaplanır:

```cpp
int a = 123456789;
long long b = a * a;   // YANLIŞ: a*a ifadesi int taşması yapar
cout << b << "\n";     // -1757895751
```

Düzeltme: `(long long)a * a` veya `a` değişkenini `long long` olarak tanımlamak.

### Modüler Aritmetik

$x \bmod m$, $x$'in $m$'ye bölümünden kalan değeri verir. Örneğin $17 \bmod 5 = 2$ çünkü $17 = 3 \cdot 5 + 2$.

Büyük sayılarla çalışırken her işlem sonrasında mod almak gerekebilir. Temel özellikler:

$$
(a + b) \bmod m = (a \bmod m + b \bmod m) \bmod m
$$
$$
(a - b) \bmod m = (a \bmod m - b \bmod m) \bmod m
$$
$$
(a \cdot b) \bmod m = (a \bmod m \cdot b \bmod m) \bmod m
$$

$n!$ değerini $\bmod m$ ile hesaplamak:

```cpp
long long x = 1;
for (int i = 2; i <= n; i++) {
    x = (x * i) % m;
}
cout << x % m << "\n";
```

Çıkarma işlemi nedeniyle kalan negatif çıkabilir; bunu önlemek için:

```cpp
x = x % m;
if (x < 0) x += m;
```

### Kayan Noktalı Sayılar

Yarışmalarda genellikle 64-bit **`double`** yeterlidir; g++ ayrıca 80-bit `long double` sunar. Belirli ondalık basamakla yazdırmak için:

```cpp
printf("%.9f\n", x);
```

Yuvarlama hatalarına dikkat etmek gerekir:

```cpp
double x = 0.3 * 3 + 0.1;
printf("%.20f\n", x);  // 0.99999999999999988898
```

Bu nedenle kayan noktalı sayıları `==` ile karşılaştırmak yerine küçük bir $\varepsilon$ toleransı kullanmak daha güvenlidir ($\varepsilon = 10^{-9}$):

```cpp
if (abs(a - b) < 1e-9) {
    // a ve b eşit
}
```

## 1.4 Kodu Kısaltmak

### Tür İsimlendirme (`typedef`)

`typedef` ile uzun tür isimlerine kısa takma adlar verilebilir:

```cpp
typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pi;
```

### Makrolar (`#define`)

Makrolar, derleme öncesinde belirli kod parçalarını değiştirir:

```cpp
#define F first
#define S second
#define PB push_back
#define MP make_pair
```

Döngüleri kısaltmak için parametreli makro:

```cpp
#define REP(i, a, b) for (int i = a; i <= b; i++)
```

**Dikkat:** Makrolar beklenmedik hatalara yol açabilir. Örneğin:

```cpp
#define SQ(a) a * a
cout << SQ(3 + 3) << "\n";  // 3+3*3+3 = 15 (YANLIŞ)
```

Parantez ekleyerek düzeltilir:

```cpp
#define SQ(a) (a) * (a)
cout << SQ(3 + 3) << "\n";  // (3+3)*(3+3) = 36 (DOĞRU)
```

## 1.5 Matematik

### Toplam Formülleri

$\sum_{x=1}^{n} x^k$ formundaki her toplam, $k+1$ derecesinde bir polinom olan kapalı form formülüne sahiptir:

$$\sum_{x=1}^{n} x = 1 + 2 + 3 + \cdots + n = \frac{n(n+1)}{2}$$

$$\sum_{x=1}^{n} x^2 = 1^2 + 2^2 + \cdots + n^2 = \frac{n(n+1)(2n+1)}{6}$$

**Aritmetik ilerleme:** Ardışık elemanlar arasındaki fark sabittir (örn. $3, 7, 11, 15$). Toplam formülü:

$$\underbrace{a + \cdots + b}_{n \text{ eleman}} = \frac{n(a + b)}{2}$$

Örnek: $3 + 7 + 11 + 15 = \dfrac{4 \cdot (3 + 15)}{2} = 36$

**Geometrik ilerleme:** Ardışık elemanlar arasındaki oran sabittir (örn. $3, 6, 12, 24$, oran $k = 2$). Toplam formülü:

$$a + ak + ak^2 + \cdots + b = \frac{bk - a}{k - 1}$$

Örnek: $3 + 6 + 12 + 24 = \dfrac{24 \cdot 2 - 3}{2 - 1} = 45$

Özel durum: $1 + 2 + 4 + \cdots + 2^{n-1} = 2^n - 1$

**Harmonik toplam:**

$$\sum_{x=1}^{n} \frac{1}{x} = 1 + \frac{1}{2} + \frac{1}{3} + \cdots + \frac{1}{n}$$

Üst sınırı $\log_2(n) + 1$'dir.

### Küme Teorisi

Bir **küme** elemanların grubudur. Temel notasyonlar: $\emptyset$ boş küme, $|S|$ kümenin eleman sayısı, $x \in S$ eleman üyeliği.

Temel küme işlemleri:

- **Kesişim** $A \cap B$: Hem $A$ hem $B$'de bulunan elemanlar. $\{1,2,5\} \cap \{2,4\} = \{2\}$
- **Birleşim** $A \cup B$: $A$ veya $B$'de bulunan elemanlar. $\{3,7\} \cup \{2,3,8\} = \{2,3,7,8\}$
- **Tamlayan** $\bar{A}$: $A$'da bulunmayan elemanlar (evrensel kümeye göre).
- **Fark** $A \setminus B = A \cap \bar{B}$: $A$'da olup $B$'de olmayan elemanlar.

$|S|$ elemanlı bir kümenin $2^{|S|}$ alt kümesi vardır. Örneğin $\{2, 4, 7\}$ kümesinin alt kümeleri: $\emptyset, \{2\}, \{4\}, \{7\}, \{2,4\}, \{2,7\}, \{4,7\}, \{2,4,7\}$.

Sık kullanılan kümeler: $\mathbb{N}$ (doğal sayılar), $\mathbb{Z}$ (tamsayılar), $\mathbb{Q}$ (rasyonel sayılar), $\mathbb{R}$ (reel sayılar).

Kural gösterimiyle küme tanımlama: $X = \{2n : n \in \mathbb{Z}\}$ bütün çift sayıları içerir.

### Mantık

Temel mantık operatörleri:

| $A$ | $B$ | $\lnot A$ | $\lnot B$ | $A \land B$ | $A \lor B$ | $A \Rightarrow B$ | $A \Leftrightarrow B$ |
|:---:|:---:|:---------:|:---------:|:-----------:|:----------:|:-----------------:|:---------------------:|
| 0   | 0   | 1         | 1         | 0           | 0          | 1                 | 1                     |
| 0   | 1   | 1         | 0         | 0           | 1          | 1                 | 0                     |
| 1   | 0   | 0         | 1         | 0           | 1          | 0                 | 0                     |
| 1   | 1   | 0         | 0         | 1           | 1          | 1                 | 1                     |

**Predicate** parametreye bağlı doğru/yanlış ifadelerdir. Örneğin $P(x)$ "$x$ asaldır" olarak tanımlanırsa $P(7)$ doğru, $P(8)$ yanlıştır.

**Niceleyiciler:** $\forall$ (her) ve $\exists$ (bazı/var). Örnek:

$$\forall x \left( \exists y \left( y < x \right) \right)$$

tamsayılar için doğrudur (her $x$'ten küçük bir $y$ vardır) fakat doğal sayılar için yanlıştır.

### Fonksiyonlar

- $\lfloor x \rfloor$: Aşağı yuvarlama. $\lfloor 3/2 \rfloor = 1$
- $\lceil x \rceil$: Yukarı yuvarlama. $\lceil 3/2 \rceil = 2$
- $\min(x_1, \ldots, x_n)$ ve $\max(x_1, \ldots, x_n)$: En küçük ve en büyük değer.

**Faktöriyel:**

$$n! = \prod_{x=1}^{n} x = 1 \cdot 2 \cdot 3 \cdots n, \qquad 0! = 1$$

**Fibonacci sayıları** özyinelemeli olarak tanımlanır:

$$f(0) = 0, \quad f(1) = 1, \quad f(n) = f(n-1) + f(n-2)$$

İlk Fibonacci sayıları: $0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, \ldots$

Binet'in kapalı form formülü:

$$f(n) = \frac{(1+\sqrt{5})^n - (1-\sqrt{5})^n}{2^n \sqrt{5}}$$

### Logaritmalar

$\log_k(x) = a$ eşdeğeri $k^a = x$'tir. $\log_k(x)$, $x$'i 1'e indirmek için $k$'ye kaç defa böleceğimizi gösterir. Örneğin $\log_2(32) = 5$ çünkü:

$$32 \to 16 \to 8 \to 4 \to 2 \to 1$$

Temel özellikler:

$$\log_k(ab) = \log_k(a) + \log_k(b)$$
$$\log_k(x^n) = n \cdot \log_k(x)$$
$$\log_k\!\left(\frac{a}{b}\right) = \log_k(a) - \log_k(b)$$
$$\log_u(x) = \frac{\log_k(x)}{\log_k(u)}$$

**Doğal logaritma** $\ln(x)$, tabanı $e \approx 2{,}71828$ olan logaritmadır. $b$ tabanındaki $x$ sayısının basamak sayısı $\lfloor \log_b(x) \rfloor + 1$'dir. Örneğin $\lfloor \log_2(123) \rfloor + 1 = 7$ ve $123_{10} = 1111011_2$.

## 1.6 Yarışmalar ve Kaynaklar

### IOI

**International Olympiad in Informatics (IOI)** lise öğrencileri için yıllık düzenlenen bir yarışmadır. Her ülke 4 kişilik takım gönderebilir; yaklaşık 80 ülkeden 300 katılımcı yer alır.

IOI, 2 adet 5 saatlik yarışmadan oluşur. Her yarışmada farklı zorlukta 3 algoritma problemi bulunur. Problemler alt görevlere ayrılmıştır ve bireysel olarak yarışılır. IOI müfredatı bu kitabın hemen tamamını kapsamaktadır. Türkiye'de temsil seçimi TÜBİTAK Bilim Olimpiyatları aracılığıyla yapılır.

Bölgesel yarışmalar arasında Baltic Olympiad in Informatics (BOI), Central European Olympiad in Informatics (CEOI) ve Asia-Pacific Informatics Olympiad (APIO) sayılabilir.

### ICPC

**International Collegiate Programming Contest (ICPC)** üniversite öğrencileri için düzenlenen bir yarışmadır. 3 kişilik takımlar halinde 1 bilgisayarla yarışılır. Her yarışmada 10 algoritma sorusu 5 saatte çözülmeye çalışılır. IOI'a kıyasla matematik bilgisi daha ön plandadır.

### Online Yarışmalar

En aktif platform **Codeforces**'tur; haftalık Div1/Div2/Div3/Div4 yarışmaları düzenlenmektedir. Diğer önemli platformlar: AtCoder, CS Academy, HackerRank ve Topcoder. Şirket yarışmaları olarak Facebook Hacker Cup, Google Code Jam ve Yandex.Algorithm öne çıkar.

### Kitaplar

- S. S. Skiena & M. A. Revilla — *Programming Challenges*
- S. Halim & F. Halim — *Competitive Programming 3*
- K. Diks et al. — *Looking for a Challenge?* (ileri düzey)
- T. H. Cormen et al. — *Introduction to Algorithms*
- J. Kleinberg & É. Tardos — *Algorithm Design*
- S. S. Skiena — *The Algorithm Design Manual*
