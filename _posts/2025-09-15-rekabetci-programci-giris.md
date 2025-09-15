---
layout: post
title:  Rekabetçi Programcı Giriş
math: true 
categories: 
  - Program
tags: 
  - bilim
  - c
  - programlama
  - giriş
  - algoritma
  - olimpiyat
  - yarışma
  - rekabet
  - kodlama
  - matematik
  - kitap
---

# Bölüm 1: Başlangıç

Rekabetçi programlama iki konudan oluşur: uygun algoritmayı bulmak (algoritmanın dizaynı) ve uygun algoritmanın koda geçirilmesi (implementasyonu).

Uygun algoritmayı bulmak (dizayn) için soru çözmek ve matematiksel düşünme gerekir. Soruların analiz edilip yaratıcı bir şekilde çözülmesi önemlidir. Soruyu çözen algoritmanın hem doğru hem de verimli olması gerekir. Zaten genel olarak soruların temelinde verimli algoritmayı bulmak vardır.

Rekabetçi programcıların algoritmalar hakkında teorik bilgiye sahip olması gerekir. Tipik bir soru çözümü genelde bilinen tekniklerle yeni gözlemlerin birleşimidir. Rekabetçi programlamada çıkan teknikler aynı zamanda algoritmaların araştırma bazlı kısmının da temelini oluşturur.

Algoritmaların koda geçirilmesi (implementasyon) içinse iyi kodlama bilgisi gerekir. Rekabetçi programlamada çözümler belirli test caseler kullanılarak puanlanır. Bu yüzden sadece algoritmayı düşünerek bulmak yetmez, aynı zamanda bunun koda doğru bir şekilde geçirilmesi önemlidir.

Yarışmalarda yazılan kodların kısa ama aynı zamanda anlaşılabilir olması gerekir. Yarışmalarda verilen zamanın kısıtlı olması nedeniyle çözümlerin hızlı yazılması gerekir. Klasik yazılım mühendisliğinin aksine, çözümler kısa olup (çoğunlukla en fazla birkaç yüz satır kod) yarışma sonrası geliştirilmesi gerekmemektedir.

## 1.1 Kodlama Dilleri

Şu anda rekabetçi programlamada en çok kullanılan kodlama dilleri C++, Python ve Java'dır. Örneğin Google Code Jam 2017'de yarışmacıların ilk 3000'ünün 79%'u C++, 16%'sı Python ve 8%'i Java kullanmıştır[cite: 57]. Bazı yarışmacılar birden çok kodlama dilini kullandılar.

Çoğu yarışmacı C++ dilini rekabetçi programlama için en iyi dil olarak görüyor ve C++ neredeyse her yarışma sisteminde bulunmaktadır[^1]. [cite_start]C++11'in yararları arasında çok hızlı ve verimli bir dil olmasıyla beraber çeşitli veri yapıları ile algoritmaları kapsayan bir kütüphaneye sahip olması yer alır. [cite: 59, 60]

Yine de birkaç dilde uzmanlaşıp onların yararlarını bilmekte fayda var. [cite_start]Örneğin soruda çok büyük sayılar gerekiyorsa Python, büyük sayılar için işlemleri halihazırda `built-in` bulundurmasından dolayı uygun bir seçenek olabilir. [cite: 63, 64] [cite_start]Neyse ki yarışmalardaki çoğu soru, herhangi bir kodlama dilinin avantajı olmayacak şekilde hazırlanmaktadır. [cite: 65]

[cite_start]Bu kitaptaki örnek çözümler C++ ile yazılmış olup standart kütüphanedeki algoritma ve veri yapıları sıklıkla kullanılmıştır. [cite: 66] [cite_start]Çözümler C++11 formatında yazılmıştır ki bu format şu anki çoğu yarışmada kullanılabilmektedir. [cite: 67]

### C++ Kod Örneği

Klasik bir C++ kodu aşağıdaki gibi görünür.

```cpp
#include <bits/stdc++.h>

using namespace std;

int main() {
  // cozum burada yazilir.
}
```

[cite_start]Kodun başındaki `#include` satırı, `g++` derleyicisinin bir özelliği olup standart kütüphaneyi kodumuza eklememizi sağlar. [cite: 76] [cite_start]Böylece `iostream`, `vector`, `algorithm`, gibi kütüphaneleri elle teker teker yüklemek yerine hepsini otomatik bir şekilde eklemiş oluruz. [cite: 77]

[cite_start]`using namespace std;` satırı, standart kütüphanedeki sınıfların ve fonksiyonların herhangi bir indikatör koymadan direkt olarak kullanılabileceğini söyler. [cite: 78] [cite_start]Eğer `using` ifadesini kullanmazsak `cout` ifadesini `std::cout` şeklinde yazmamız gerekir. [cite: 79]

Kod aşağıdaki komutla derlenebilir:
[cite_start]`g++ -std=c++11 -O2 -Wall test.cpp -o test` [cite: 81]

[cite_start]Bu komut, `test.cpp`'den `test` adlı bir binary dosyası oluşturur. [cite: 82] [cite_start]Bu derleyici C++11'i kullanıp (`-std=c++11`) kodu optimize edip (`-O2`) olası hatalar hakkında uyarı verir (`-Wall`). [cite: 83]

## 1.2 Girdi ve Çıktı

[cite_start]Çoğu yarışmada girdi ve çıktı almak için klasik fonksiyonlar kullanılır. [cite: 85] [cite_start]C++'da bu klasik fonksiyonlar girdi için `cin` ve çıktı için `cout`'dur. [cite: 86] [cite_start]Bunlarla beraber C fonksiyonları olan `scanf` ve `printf` de kullanılabilir. [cite: 87]

[cite_start]Program için olan girdiler genel olarak birbirlerinden boşluk veya yeni satır karakterleriyle ayrılmış sayılar ve stringlerdir. [cite: 88] [cite_start]Bu girdiler `cin` ifadesiyle aşağıdaki gibi alınabilir: [cite: 89]

```cpp
int a, b;
string x;
cin >> a >> b >> x;
```

Bazen girdi ve çıktılar programı yavaşlatacak birer darboğaz (bottleneck) halini alabilir. [cite_start]Aşağıdaki iki satırı koda eklemek girdi ve çıktıyı daha verimli hale getirir: [cite: 103, 104]

```cpp
ios::sync_with_stdio(0);
cin.tie(0);
```

[cite_start]Yeni satır için `"\n"` ifadesinin `endl`'e göre daha hızlı çalıştığına dikkat edin çünkü `endl` her zaman `flush` operasyonu uygular. [cite: 106]

[cite_start]Eğer girdinin miktarı bilinmiyorsa aşağıdaki gibi bir döngü yararlı olabilir: [cite: 117]

```cpp
while (cin >> x) {
  // kod
}
```

[cite_start]Bu döngü, girdide okunmamış eleman kalmayana kadar elemanları okumaya devam eder. [cite: 122]

## 1.3 Sayılarla Çalışmak

### Tam Sayılar

[cite_start]Rekabetçi Programlamada en çok kullanılan tam sayı tipi 32-bit olan `int`'tir. [cite: 130] [cite_start]Bu tip $-2 \cdot 10^9 ... 2 \cdot 10^9$ arası tam sayıları tutabilir. [cite: 131]

[cite_start]Eğer `int` yeterli değilse, 64-bit `long long` kullanılabilir. [cite: 132] [cite_start]`long long`, $-9 \cdot 10^{18} ... 9 \cdot 10^{18}$ arası tam sayıları tutabilir. [cite: 133]

```cpp
long long x = 123456789123456789LL;
```

`long long` tipi kullanılırken sıkça yapılan hata `int` tipinin hala kodda bir yerde kullanılmasıdır. [cite_start]Örneğin, aşağıdaki kodda `a*a` işlemi `int` sınırlarını aştığı için taşma (overflow) olur ve sonuç yanlış çıkar: [cite: 137, 138]

```cpp
int a = 123456789;
long long b = a*a;
cout << b << "\n"; // -1757895751
```

[cite_start]Bu sorun, `a` değişkeninin tipini `long long` yaparak veya ifadeyi `(long long)a * a` şeklinde cast ederek düzeltilebilir. [cite: 144]

### Modüler Aritmetik

[cite_start]Bazen bir sorunun çözümü çok büyük olduğunda, çözümü "modulo m" (örneğin, "modulo $10^9+7$") yazdırmamız istenebilir. [cite: 151] [cite_start]Kalanın önemli özelliklerinden biri, toplama, çıkarma ve çarpma gibi işlemlerde operasyon öncesi alınabilmesidir: [cite: 153]

- [cite_start]`(a+b) mod m = ((a mod m) + (b mod m)) mod m` [cite: 154, 155]
- [cite_start]`(a-b) mod m = ((a mod m) - (b mod m)) mod m` [cite: 156, 157]
- [cite_start]`(a*b) mod m = ((a mod m) * (b mod m)) mod m` [cite: 158, 159]

[cite_start]Böylece her operasyondan sonra ifadenin kalanını alarak tutulan sayının çok büyük olması engellenebilir. [cite: 160]

### Kayan Noktalı Sayılar

[cite_start]Rekabetçi programlamadaki kayan noktalı tipler genelde 64-bit `double`'dır. [cite: 173] `g++` derleyicisinde ek olarak 80-bit `long double` tipi de vardır. [cite_start]Çoğu durumda `double` yeterli olacaktır. [cite: 173]

[cite_start]Kayan noktalı sayıları `==` operatörüyle karşılaştırmak risklidir çünkü yuvarlama hataları olabilir. [cite: 184] [cite_start]Bunun yerine, iki sayının mutlak farkının `ε` gibi küçük bir sayıdan (örneğin $10^{-9}$) daha az olup olmadığını kontrol etmek daha güvenlidir: [cite: 185]

```cpp
if (abs(a-b) < 1e-9) {
  // a ve b eşit kabul edilir
}
```

## 1.4 Kodu Kısaltmak

### Tip İsimleri
`typedef` komutunu kullanarak bir veri tipine daha kısa bir isim verilebilir. [cite_start]Örneğin, `long long` için `ll` gibi: [cite: 197, 198]

```cpp
typedef long long ll;
ll a = 123456789;
```

### Makrolar
[cite_start]Kodu kısaltmanın bir diğer yolu da `#define` ile makro tanımlamaktır: [cite: 212, 213]

```cpp
#define PB push_back
#define MP make_pair

v.PB(MP(y1, x1)); // v.push_back(make_pair(y1, x1)) yerine
```

## 1.5 Matematik

### Toplam Formülleri

- [cite_start]Aritmetik Dizi: $a + (a+d) + ... + b = \frac{n(a+b)}{2}$ [cite: 266]
- [cite_start]Geometrik Dizi: $a + ak + ak^2 + ... + b = \frac{bk-a}{k-1}$ [cite: 274]
- [cite_start]$1+2+4+...+2^{n-1} = 2^n - 1$ [cite: 283]
- Harmonik Toplam: $\sum_{k=1}^{n}\frac{1}{k} \approx \ln(n)$

### Küme Teorisi

- [cite_start]Kesişim ($A \cap B$): Hem A hem de B'de bulunan elemanlar. [cite: 300]
- [cite_start]Birleşim ($A \cup B$): A'da veya B'de bulunan elemanlar. [cite: 301]
- [cite_start]Alt küme ($A \subset S$): A'nın her elemanı S'de de bulunur. [cite: 307]

### Fonksiyonlar

- [cite_start]Taban (Floor): $\lfloor x \rfloor$ fonksiyonu, x sayısını en yakın küçük veya eşit tam sayıya yuvarlar. [cite: 341]
- [cite_start]Tavan (Ceil): $\lceil x \rceil$ fonksiyonu, x sayısını en yakın büyük veya eşit tam sayıya yuvarlar. [cite: 341]
- Faktöriyel: $n! = 1 \cdot 2 \cdot ... \cdot n$, ve $0! [cite_start]= 1$. [cite: 347, 349]
- [cite_start]Fibonacci Sayıları: $f(0)=0, f(1)=1, f(n) = f(n-1)+f(n-2)$. [cite: 352, 353, 355]

## 1.6 Yarışmalar ve Kaynaklar

### IOI

[cite_start]Uluslararası Bilgisayar Olimpiyatı (International Olympiad in Informatics - IOI), lise öğrencilerinin katıldığı yıllık bir yarışmadır. [cite: 381] [cite_start]Her ülke 4 kişilik bir takım gönderebilir. [cite: 382] [cite_start]IOI, 5 saatlik iki yarışmadan oluşur ve her yarışmada 3 algoritma problemi çözülmesi istenir. [cite: 383]

### ICPC

[cite_start]Uluslararası Üniversite Programlama Yarışması (International Collegiate Programming Contest - ICPC), üniversite öğrencileri için yıllık düzenlenen bir yarışmadır. [cite: 393] [cite_start]Her takım üç öğrenciden oluşur ve tek bir bilgisayar kullanırlar. [cite: 394]

### Online Yarışmalar

Herkesin katılabileceği online yarışmalar da vardır. En aktif yarışma sitelerinden bazıları şunlardır:
* Codeforces
* AtCoder
* HackerRank
* Topcoder

[cite_start]Ayrıca Facebook Hacker Cup ve Google Code Jam gibi şirketlerin düzenlediği yarışmalar da bulunur. [cite: 405]

[^1]: Çevirmen Notu (Ç.N.): TÜBİTAK Bilim Olimpiyatları'nda sadece C/C++ kullanılabilmektedir.