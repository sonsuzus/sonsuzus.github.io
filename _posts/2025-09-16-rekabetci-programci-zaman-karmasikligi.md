---
layout: post
title: Rekabetçi Programcı Zaman Karmaşıklığı
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
  - zaman
  - karmaşıklık
  - sınıf
  - rekürsif
  - yarışma
  - rekabet
  - kodlama
  - matematik
  - kitap
redirect_from:
  - /posts/rekabetci-programci-zaman-karmasikligi/
---


Rekabetçi programlamada algoritmaların verimliliği önemlidir. Genelde soruyu çözen yavaş bir algoritma oluşturmak kolaydır ama asıl zorluk hızlı bir algoritma oluşturmaktır. Eğer algoritma çok yavaşsa ya sorudan kısmi puan alacaktır ya da hiç almayacaktır.

Zaman karmaşıklığı, bir algoritmanın bir girdi için tahmini olarak ne kadar süre gerektireceğini belirtir. Bunun amacı, girdinin boyutuna göre değişen ve algoritmanın verimliliğini gösteren bir fonksiyon oluşturmaktır. Zaman karmaşıklığını hesaplayarak, algoritmayı koda dökmeden önce yeterince hızlı olup olmadığını anlayabiliriz.

## 2.1 Hesaplama Kuralları

Bir algoritmanın zaman karmaşıklığı `O(...)` ile gösterilir. Genelde, girdi büyüklüğü olarak `n` değişkeni kullanılır. Örneğin sayılardan oluşan bir dizide `n` dizinin büyüklüğünü, eğer girdi bir yazı ise `n` yazının uzunluğunu verir.

### Döngüler

Algoritmanın yavaşlamasına neden olan genel sebeplerden biri, girdi üzerinde çalışan çok fazla döngü bulundurmasıdır. Bir algoritma ne kadar çok iç içe geçmiş döngü içerirse o kadar yavaşlar. Eğer `k` tane iç içe geçmiş döngü varsa zaman karmaşıklığı `O(n^k)` olur.

Örneğin aşağıdaki kodun zaman karmaşıklığı `O(n)`'dir:
```cpp
for (int i = 1; i <= n; i++) {
  // kod
}
```

Ve aşağıdaki kodun zaman karmaşıklığı ise `O(n^2)`'dir:
```cpp
for (int i = 1; i <= n; i++) {
  for (int j = 1; j <= n; j++) {
    // kod
  }
}
```

### Büyüklük Sırası (Order of Magnitude)

Zaman karmaşıklığı bize döngü içindeki kodun tam olarak kaç defa çalışacağını vermez. Örneğin aşağıdaki kodların hepsinin zaman karmaşıklığı `O(n)`'dir, ancak döngü sayıları farklıdır.
```cpp
for (int i = 1; i <= 3*n; i++) {
  // kod
}

for (int i = 1; i <= n+5; i++) {
  // kod
}

for (int i = 1; i <= n; i += 2) {
  // kod
}
```

### Aşamalar (Phases)

Eğer algoritma birden çok aşamadan oluşuyorsa, toplam zaman karmaşıklığı en yavaş aşamanın karmaşıklığına eşittir. Çünkü genelde en yavaş çalışan aşama, toplam süreyi domine eder.

### Çoklu Değişkenler

Bazen zaman karmaşıklığı birden çok faktöre bağlıdır. Bu durumda formül birden çok değişken içerir. Örneğin aşağıdaki kodun zaman karmaşıklığı `O(nm)`'dir:
```cpp
for (int i = 1; i < n; i++) {
  for (int j = 1; j <= m; j++) {
    // kod
  }
}
```

### Özyineleme (Recursion)

Özyinelemeli bir fonksiyonun zaman karmaşıklığı, fonksiyonun kaç kez çağrıldığı ile bir çağrının zaman karmaşıklığının çarpımına eşittir.

Örneğin, aşağıdaki `f(n)` fonksiyonu `n` kez çağrılır ve her çağrı `O(1)` sürdüğü için toplam karmaşıklık `O(n)`'dir.
```cpp
void f(int n) {
  if (n == 1) return;
  f(n-1);
}
```
Aşağıdaki `g(n)` fonksiyonunda ise her çağrı iki yeni çağrı oluşturur. Bu da toplamda `1 + 2 + 4 + ... + 2^(n-1) = 2^n - 1` çağrıya yol açar. Dolayısıyla zaman karmaşıklığı `O(2^n)`'dir.
```cpp
void g(int n) {
  if (n == 1) return;
  g(n-1);
  g(n-1);
}
```

## 2.2 Karmaşıklık Sınıfları (Complexity Classes)

| Karmaşıklık    | Açıklama                                                                                                   |
|----------------|------------------------------------------------------------------------------------------------------------|
| `O(1)`         | **Sabit Zaman:** Girdi büyüklüğünden bağımsızdır.                                                          |
| `O(log n)`     | **Logaritmik:** Girdiyi her adımda bölen algoritmalardır (örn. ikili arama).                                  |
| `O(sqrt(n))`   | **Karekök:** `O(log n)`'den yavaş, `O(n)`'den hızlıdır.                                                      |
| `O(n)`         | **Lineer:** Girdi üzerinden sabit sayıda geçiş yapar. Genelde en iyi karmaşıklıktır.                         |
| `O(n log n)`   | Genellikle verimli sıralama algoritmalarının karmaşıklığıdır.                                                |
| `O(n^2)`       | **Karesel:** Genellikle iki iç içe döngü içerir. Girdideki tüm eleman çiftlerini gezer.                       |
| `O(n^3)`       | **Kübik:** Genellikle üç iç içe döngü içerir. Girdideki tüm üçlüleri gezer.                                  |
| `O(2^n)`       | Genellikle girdinin tüm alt kümelerini gezen algoritmalardır.                                                |
| `O(n!)`        | Genellikle girdinin tüm permütasyonlarını gezen algoritmalardır.                                             |

Zaman karmaşıklığı en fazla `O(n^k)` (k sabit) olan bir algoritma **polinom**dur. `O(2^n)` ve `O(n!)` dışındaki yukarıdaki karmaşıklıklar polinomdur.

## 2.3 Verimliliği Tahmin Etme

Girdinin büyüklüğüne göre, 1 saniyelik zaman limitinde beklenen zaman karmaşıklığı aşağıdaki gibidir:

| Girdi Büyüklüğü `n` | Gerekli Zaman Karmaşıklığı |
|---------------------|----------------------------|
| $n \le 10$          | `O(n!)`                    |
| $n \le 20$          | `O(2^n)`                   |
| $n \le 500$         | `O(n^3)`                   |
| $n \le 5000$        | `O(n^2)`                   |
| $n \le 10^6$        | `O(n log n)` veya `O(n)`   |
| `n` çok büyük       | `O(1)` veya `O(log n)`     |

## 2.4 En Büyük Alt Dizi Toplamı

Problem: n elemanlı bir dizide, elemanları ardışık olan ve toplamı en büyük olan alt dizinin toplamını bulmak.

Örneğin, `[-1, 2, 4, -3, 5, 2, -5, 2]` dizisi için en büyük alt dizi toplamı `[2, 4, -3, 5, 2]` alt dizisinden gelen 10'dur.

### 1. Algoritma: $O(n^3)$

Tüm olası alt dizileri üç iç içe döngü ile deneyen kaba kuvvet çözümü.
```cpp
int best = 0;
for (int a = 0; a < n; a++) {
  for (int b = a; b < n; b++) {
    int sum = 0;
    for (int k = a; k <= b; k++) {
      sum += array[k];
    }
    best = max(best, sum);
  }
}
cout << best << "\n";
```

### 2. Algoritma: $O(n^2)$

İçteki döngülerden birini kaldırarak iyileştirilmiş çözüm.
```cpp
int best = 0;
for (int a = 0; a < n; a++) {
  int sum = 0;
  for (int b = a; b < n; b++) {
    sum += array[b];
    best = max(best, sum);
  }
}
cout << best << "\n";
```

### 3. Algoritma: $O(n)$ (Kadane'in Algoritması)

Her pozisyonda biten en büyük alt dizi toplamını bularak ilerleyen verimli çözüm.
```cpp
int best = 0, sum = 0;
for (int k = 0; k < n; k++) {
  sum = max(array[k], sum + array[k]);
  best = max(best, sum);
}
cout << best << "\n";
```
Bu, problem için mümkün olan en iyi zaman karmaşıklığıdır.

