---
layout: post
title: Rekabetçi Programcı Giriş
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
redirect_from:
  - /posts/rekabetci-programci-giris/
---

Rekabetçi programlama iki konudan oluşur: uygun algoritmayı bulmak (algoritmanın dizaynı) ve uygun algoritmanın koda geçirilmesi (implementasyonu). Uygun algoritmayı bulmak (dizayn) için soru çözmek ve matematiksel düşünme gerekir. Soruların analiz edilip yaratıcı bir şekilde çözülmesi önemlidir. Soruyu çözen algoritmanın hem doğru hem de verimli olması gerekir. Zaten genel olarak soruların temelinde verimli algoritmayı bulmak vardır. Rekabetçi programcıların algoritmalar hakkında teorik bilgiye sahip olması gerekir. Tipik bir soru çözümü genelde bilinen tekniklerle yeni gözlemlerin birleşimidir. Rekabetçi programlamada çıkan teknikler aynı zamanda algoritmaların araştırma bazlı kısmının da temelini oluşturur.

Algoritmaların koda geçirilmesi (implementasyon) içinse iyi kodlama bilgisi gerekir. Rekabetçi programlamada çözümler belirli test caseler kullanılarak puanlanır. Bu yüzden sadece algoritmayı düşünerek bulmak yetmez, aynı zamanda bunun koda doğru bir şekilde geçirilmesi önemlidir.

Yarışmalarda yazılan kodların kısa ama aynı zamanda anlaşılabilir olması gerekir. Yarışmalarda verilen zamanın kısıtlı olması nedeniyle çözümlerin hızlı yazılması gerekir. Klasik yazılım mühendisliğinin aksine, çözümler kısa olup (çoğunlukla en fazla birkaç yüz satır kod) yarışma sonrası geliştirilmesi gerekmemektedir.

## 1.1 Kodlama Dilleri

Şu anda rekabetçi programlamada en çok kullanılan kodlama dilleri C++, Python ve Java'dır. Örneğin Google Code Jam 2017'de yarışmacıların ilk 3000'ünün 79%'u C++, 16%'sı Python ve 8%'i Java kullanmıştır. Bazı yarışmacılar birden çok kodlama dilini kullandılar.

Çoğu yarışmacı C++ dilini rekabetçi programlama için en iyi dil olarak görüyor ve C++ neredeyse her yarışma sisteminde bulunmaktadır[^1]. C++11'in yararları arasında çok hızlı ve verimli bir dil olmasıyla beraber çeşitli veri yapıları ile algoritmaları kapsayan bir kütüphaneye sahip olması yer alır. 

Yine de birkaç dilde uzmanlaşıp onların yararlarını bilmekte fayda var. Örneğin soruda çok büyük sayılar gerekiyorsa Python, büyük sayılar için işlemleri halihazırda `built-in` bulundurmasından dolayı uygun bir seçenek olabilir.  Neyse ki yarışmalardaki çoğu soru, herhangi bir kodlama dilinin avantajı olmayacak şekilde hazırlanmaktadır. 

Bu kitaptaki örnek çözümler C++ ile yazılmış olup standart kütüphanedeki algoritma ve veri yapıları sıklıkla kullanılmıştır.  Çözümler C++11 formatında yazılmıştır ki bu format şu anki çoğu yarışmada kullanılabilmektedir. 

### C++ Kod Örneği

Klasik bir C++ kodu aşağıdaki gibi görünür.

```cpp
#include <bits/stdc++.h>

using namespace std;

int main() {
  // cozum burada yazilir.
}
```

Kodun başındaki `#include` satırı, `g++` derleyicisinin bir özelliği olup standart kütüphaneyi kodumuza eklememizi sağlar.  Böylece `iostream`, `vector`, `algorithm`, gibi kütüphaneleri elle teker teker yüklemek yerine hepsini otomatik bir şekilde eklemiş oluruz. 

`using namespace std;` satırı, standart kütüphanedeki sınıfların ve fonksiyonların herhangi bir indikatör koymadan direkt olarak kullanılabileceğini söyler.  Eğer `using` ifadesini kullanmazsak `cout` ifadesini `std::cout` şeklinde yazmamız gerekir. 

Kod aşağıdaki komutla derlenebilir:
`g++ -std=c++11 -O2 -Wall test.cpp -o test` 

Bu komut, `test.cpp`'den `test` adlı bir binary dosyası oluşturur.  Bu derleyici C++11'i kullanıp (`-std=c++11`) kodu optimize edip (`-O2`) olası hatalar hakkında uyarı verir (`-Wall`). 

## 1.2 Girdi ve Çıktı

Çoğu yarışmada girdi ve çıktı almak için klasik fonksiyonlar kullanılır.  C++'da bu klasik fonksiyonlar girdi için `cin` ve çıktı için `cout`'dur.  Bunlarla beraber C fonksiyonları olan `scanf` ve `printf` de kullanılabilir. 

Program için olan girdiler genel olarak birbirlerinden boşluk veya yeni satır karakterleriyle ayrılmış sayılar ve stringlerdir.  Bu girdiler `cin` ifadesiyle aşağıdaki gibi alınabilir: 

```cpp
int a, b;
string x;
cin >> a >> b >> x;
```

Bazen girdi ve çıktılar programı yavaşlatacak birer darboğaz (bottleneck) halini alabilir. Aşağıdaki iki satırı koda eklemek girdi ve çıktıyı daha verimli hale getirir: 

```cpp
ios::sync_with_stdio(0);
cin.tie(0);
```

Yeni satır için `"\n"` ifadesinin `endl`'e göre daha hızlı çalıştığına dikkat edin çünkü `endl` her zaman `flush` operasyonu uygular. 

Eğer girdinin miktarı bilinmiyorsa aşağıdaki gibi bir döngü yararlı olabilir: 

```cpp
while (cin >> x) {
  // kod
}
```

Bu döngü, girdide okunmamış eleman kalmayana kadar elemanları okumaya devam eder. 

## 1.3 Sayılarla Çalışmak

### Tam Sayılar

Rekabetçi Programlamada en çok kullanılan tam sayı tipi 32-bit olan `int`'tir.  Bu tip $-2 · 10^9 ... 2 · 10^9$ arası tam sayıları tutabilir. 

Eğer `int` yeterli değilse, 64-bit `long long` kullanılabilir.  `long long`, $-9 · 10^{18} ... 9 · 10^{18}$ arası tam sayıları tutabilir. 

```cpp
long long x = 123456789123456789LL;
```

`long long` tipi kullanılırken sıkça yapılan hata `int` tipinin hala kodda bir yerde kullanılmasıdır. Örneğin, aşağıdaki kodda `a*a` işlemi `int` sınırlarını aştığı için taşma (overflow) olur ve sonuç yanlış çıkar: 

```cpp
int a = 123456789;
long long b = a*a;
cout << b << "\n"; // -1757895751
```

Bu sorun, `a` değişkeninin tipini `long long` yaparak veya ifadeyi `(long long)a * a` şeklinde cast ederek düzeltilebilir. 

### Modüler Aritmetik

Bazen bir sorunun çözümü çok büyük olduğunda, çözümü "modulo m" (örneğin, "modulo $10^9+7$") yazdırmamız istenebilir.  Kalanın önemli özelliklerinden biri, toplama, çıkarma ve çarpma gibi işlemlerde operasyon öncesi alınabilmesidir: 

- `(a+b) mod m = ((a mod m) + (b mod m)) mod m` 
- `(a-b) mod m = ((a mod m) - (b mod m)) mod m` 
- `(a*b) mod m = ((a mod m) * (b mod m)) mod m` 

Böylece her operasyondan sonra ifadenin kalanını alarak tutulan sayının çok büyük olması engellenebilir. 

### Kayan Noktalı Sayılar

Rekabetçi programlamadaki kayan noktalı tipler genelde 64-bit `double`'dır.  `g++` derleyicisinde ek olarak 80-bit `long double` tipi de vardır. Çoğu durumda `double` yeterli olacaktır. 

Kayan noktalı sayıları `==` operatörüyle karşılaştırmak risklidir çünkü yuvarlama hataları olabilir.  Bunun yerine, iki sayının mutlak farkının `ε` gibi küçük bir sayıdan (örneğin $10^{-9}$) daha az olup olmadığını kontrol etmek daha güvenlidir: 

```cpp
if (abs(a-b) < 1e-9) {
  // a ve b eşit kabul edilir
}
```

## 1.4 Kodu Kısaltmak

### Tip İsimleri
`typedef` komutunu kullanarak bir veri tipine daha kısa bir isim verilebilir. Örneğin, `long long` için `ll` gibi: 

```cpp
typedef long long ll;
ll a = 123456789;
```

### Makrolar
Kodu kısaltmanın bir diğer yolu da `#define` ile makro tanımlamaktır: 

```cpp
#define PB push_back
#define MP make_pair

v.PB(MP(y1, x1)); // v.push_back(make_pair(y1, x1)) yerine
```

## 1.5 Matematik

### Toplam Formülleri

- Aritmetik Dizi: $a + (a+d) + ... + b = \frac{n(a+b)}{2}$ 
- Geometrik Dizi: $a + ak + ak^2 + ... + b = \frac{bk-a}{k-1}$ 
- $1+2+4+...+2^{n-1} = 2^n - 1$ 
- Harmonik Toplam: $\sum_{k=1}^{n}\frac{1}{k} \approx \ln(n)$

### Küme Teorisi

- Kesişim ($A \cap B$): Hem A hem de B'de bulunan elemanlar. 
- Birleşim ($A \cup B$): A'da veya B'de bulunan elemanlar. 
- Alt küme ($A \subset S$): A'nın her elemanı S'de de bulunur. 

### Fonksiyonlar

- Taban (Floor): $\lfloor x \rfloor$ fonksiyonu, x sayısını en yakın küçük veya eşit tam sayıya yuvarlar. 
- Tavan (Ceil): $\lceil x \rceil$ fonksiyonu, x sayısını en yakın büyük veya eşit tam sayıya yuvarlar. 
- Faktöriyel: $n! = 1 \cdot 2 \cdot ... \cdot n$, ve $0! = 1$. 
- Fibonacci Sayıları: $f(0)=0, f(1)=1, f(n) = f(n-1)+f(n-2)$. 

## 1.6 Yarışmalar ve Kaynaklar

### IOI

Uluslararası Bilgisayar Olimpiyatı (International Olympiad in Informatics - IOI), lise öğrencilerinin katıldığı yıllık bir yarışmadır.  Her ülke 4 kişilik bir takım gönderebilir.  IOI, 5 saatlik iki yarışmadan oluşur ve her yarışmada 3 algoritma problemi çözülmesi istenir. 

### ICPC

Uluslararası Üniversite Programlama Yarışması (International Collegiate Programming Contest - ICPC), üniversite öğrencileri için yıllık düzenlenen bir yarışmadır.  Her takım üç öğrenciden oluşur ve tek bir bilgisayar kullanırlar. 

### Online Yarışmalar

Herkesin katılabileceği online yarışmalar da vardır. En aktif yarışma sitelerinden bazıları şunlardır:
* Codeforces
* AtCoder
* HackerRank
* Topcoder

Ayrıca Facebook Hacker Cup ve Google Code Jam gibi şirketlerin düzenlediği yarışmalar da bulunur. 

[^1]: Çevirmen Notu (Ç.N.): TÜBİTAK Bilim Olimpiyatları'nda sadece C/C++ kullanılabilmektedir.
