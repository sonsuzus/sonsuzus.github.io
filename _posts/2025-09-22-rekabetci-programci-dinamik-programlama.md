---
layout: post
title: Rekabetçi Programcı Dinamik Programlama (Dynamic Programming)
math: true 
categories: 
  - Program
tags: 
  - search
  - arama
  - c
  - programlama
  - algoritma
  - olimpiyat
  - dizi
  - yarışma
  - değişken
  - dinamik
  - bellek
  - kodlama
  - matematik
  - kitap
  - açgözlü
redirect_from:
  - /posts/rekabetci-programci-dinamik-programlama/
---

Dinamik programlama, tam bir aramanın doğruluğu ile açgözlü algoritmaların verimliliğini birleştiren bir tekniktir. Eğer bir problemde aynı alt problemler birkaç defa çözülüyorsa ve bu alt problemler bağımsız bir şekilde çözülebiliyorsa dinamik programlama kullanabiliriz.

Dinamik programlamanın iki temel kullanımı vardır:

* **Optimal bir çözüm bulmak:** Olabildiğince büyük veya küçük bir sonuç aradığımız durumlar.
* **Olası çözüm sayısını hesaplamak:** Toplam olası çözüm sayısını bulmak.

Bu bölüm, dinamik programlamanın temellerini ve klasik problemler üzerindeki uygulamalarını gösterecektir.

## 7.1 Para Problemi

Bölüm 6'da gördüğümüz para problemini tekrar ele alalım: `coins = {c_1, c_2, ..., c_k}` değerlerinden oluşan bir para kümesiyle, `n` toplamını oluşturan en az sayıda parayı bulmak. Açgözlü yaklaşımın her zaman çalışmadığını görmüştük. Şimdi bu problemi her para kümesi için çalışan dinamik programlama ile çözeceğiz.

### Özyinelemeli Formülleştirme

Problemin çözümünü daha küçük alt problemlerin çözümlerinden bulabiliriz. `solve(x)`, `x` toplamı için gereken minimum para sayısını ifade etsin.

Eğer `coins = {1, 3, 4}` ise, `x` toplamına ulaşmak için ilk seçtiğimiz para ya 1, ya 3, ya da 4 olabilir.

* Eğer 1 seçersek, geri kalan `x-1` toplamı için `solve(x-1)` kadar paraya ihtiyacımız olur.
* Eğer 3 seçersek, geri kalan `x-3` toplamı için `solve(x-3)` kadar paraya ihtiyacımız olur.
* Eğer 4 seçersek, geri kalan `x-4` toplamı için `solve(x-4)` kadar paraya ihtiyacımız olur.

Bu durumda özyineleme formülü şu şekilde olur:
`solve(x) = min(solve(x-1)+1, solve(x-3)+1, solve(x-4)+1)`
Temel durum `solve(0) = 0`'dır.

### Memoization

Yukarıdaki özyinelemeli fonksiyon, aynı `solve(x)` değerini tekrar tekrar hesapladığı için verimsizdir. **Memoization** tekniği ile, hesaplanan her `solve(x)` değerini bir dizide saklarız. Fonksiyon tekrar aynı `x` değeri için çağrıldığında, sonucu yeniden hesaplamak yerine doğrudan diziden alırız.

```cpp
// value[x], solve(x)'in hesaplanmış değerini tutar
// ready[x], solve(x)'in hesaplanıp hesaplanmadığını belirtir
int value[N];
bool ready[N];

int solve(int x) {
  if (x < 0) return INF;
  if (x == 0) return 0;
  if (ready[x]) return value[x];
  
  int best = INF;
  for (auto c : coins) {
    best = min(best, solve(x - c) + 1);
  }
  
  ready[x] = true;
  value[x] = best;
  return best;
}
```

Bu algoritmanın zaman karmaşıklığı $O(nk)$ olur (`n` hedef toplam, `k` para sayısı).

### Döngüsel (Iterative) Yaklaşım

Aynı çözümü özyineleme yerine döngü kullanarak da yazabiliriz. Bu genellikle daha kısa ve biraz daha verimlidir.

```cpp
value[0] = 0;
for (int x = 1; x <= n; x++) {
  value[x] = INF;
  for (auto c : coins) {
    if (x - c >= 0) {
      value[x] = min(value[x], value[x - c] + 1);
    }
  }
}
```

### Çözüm Sayısını Hesaplamak

Minimum para sayısı yerine, bir toplamı oluşturmanın kaç farklı yolu olduğunu saymak istiyorsak, özyineleme formülündeki `min` işlemini toplama ile değiştiririz:
`solve(x) = solve(x-1) + solve(x-3) + solve(x-4)`
Temel durum `solve(0) = 1`'dir (boş küme bir yoldur).

```cpp
count[0] = 1;
for (int x = 1; x <= n; x++) {
  for (auto c : coins) {
    if (x - c >= 0) {
      count[x] += count[x - c];
      count[x] %= m; // Genellikle sonuç modulo m istenir
    }
  }
}
```

## 7.2 En Uzun Artan Altdizi (Longest Increasing Subsequence)

n elemanlı bir dizide, elemanları soldan sağa doğru artan sırada olan en uzun altdiziyi bulma problemidir. Elemanların ardışık olması gerekmez.

`length(k)`, `k` pozisyonunda biten en uzun artan altdizinin uzunluğunu belirtsin. `length(k)`'yı hesaplamak için, `array[i] < array[k]` koşulunu sağlayan tüm `i < k` pozisyonları arasındaki en büyük `length(i)` değerini buluruz ve buna 1 ekleriz.

[Görsel: 6,2,5,1,7,4,8,3 dizisinde en uzun artan altdizinin (2,5,7,8) gösterimi]

```cpp
for (int k = 0; k < n; k++) {
  length[k] = 1;
  for (int i = 0; i < k; i++) {
    if (array[i] < array[k]) {
      length[k] = max(length[k], length[i] + 1);
    }
  }
}
```

Bu çözümün zaman karmaşıklığı $O(n^2)$'dir. Bu problem $O(n \log n)$ zamanda da çözülebilir.

## 7.3 Düzlemde Yollar

`n x n` bir ızgarada, her hücrede pozitif bir sayı varken, sol üst köşeden sağ alt köşeye sadece sağa ve aşağı hareket ederek gidilebilen ve hücrelerdeki sayıların toplamını maksimize eden yolu bulma problemidir.

[Görsel: 5x5'lik bir düzlemde optimal yolu gösteren şema]

`sum(y, x)`, `(y, x)` hücresine ulaşan en yüksek puanlı yolun toplamını versin. Özyineleme formülü:
`sum(y, x) = max(sum(y, x-1), sum(y-1, x)) + value[y][x]`

Bu problem, $O(n^2)$'lik bir dinamik programlama çözümü ile çözülebilir.

## 7.4 Knapsack Problemleri

Knapsack (sırt çantası) problemleri, bir obje kümesinden belirli özelliklere sahip bir alt küme seçmeyi içerir. Klasik bir versiyonu, verilen ağırlıklarla oluşturulabilecek tüm olası toplam ağırlıkları bulmaktır.

Eğer `possible(x, k)` ilk `k` ağırlıkla `x` toplamını oluşturmanın mümkün olup olmadığını belirtirse, özyineleme formülü şu şekildedir:
`possible(x, k) = possible(x - w_k, k-1) OR possible(x, k-1)`

Bu, `k`. ağırlığı (`w_k`) ya kullandığımız ya da kullanmadığımız anlamına gelir. Bu da $O(nW)$'lik bir dinamik programlama çözümü ile çözülebilir (`W` toplam ağırlık).

## 7.5 Değişiklik Farkı (Edit Distance)

Değişiklik farkı (veya Levenshtein farkı[^1]), bir kelimeyi diğerine dönüştürmek için gereken minimum karakter ekleme, silme veya değiştirme sayısını verir. Örneğin, "LOVE" ve "MOVIE" arasındaki fark 2'dir (L->M, sonra V'den sonra I ekle).

`distance(a, b)`, `x` kelimesinin ilk `a` karakteri ile `y` kelimesinin ilk `b` karakteri arasındaki farkı versin. Formül şu şekildedir:
`distance(a, b) = min(distance(a, b-1)+1, distance(a-1, b)+1, distance(a-1, b-1)+cost)`
Burada `cost`, eğer `x[a]` ve `y[b]` aynı ise 0, değilse 1'dir. Bu problem $O(nm)$'lik 2 boyutlu bir DP tablosu ile çözülebilir.

[^1]: Bu kavram V. I. Levenshtein'dan ismini almıştır.