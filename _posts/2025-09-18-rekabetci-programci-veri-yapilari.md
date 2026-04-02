---
layout: post
title: Rekabetçi Programcı Veri Yapıları
math: true 
categories: 
  - Program
tags: 
  - küme
  - vektör
  - c
  - programlama
  - algoritma
  - olimpiyat
  - dizi
  - yarışma
  - değişken
  - veri
  - bellek
  - kodlama
  - matematik
  - kitap
redirect_from:
  - /posts/rekabetci-programci-veri-yapilari/
---

Veri yapısı, bilgisayarın hafızasında veri saklamak için bir yoldur. Ele alınan problem için uygun bir veri yapısı seçimi yapmak önemlidir çünkü her veri yapısının kendine göre avantajları ve dezavantajları bulunmaktadır. Bu noktada cevaplanması gereken ana soru, hangi işlemlerin seçtiğimiz veri yapısında verimli olacağıdır.

Bu bölümde C++ standart kütüphanesindeki en önemli veri yapıları tanıtılacaktır. Standart kütüphane zamandan tasarruf sağlayacağı için mümkün olduğunca onu kullanmaya özen gösterilmelidir.

## 4.1 Dinamik Diziler

Dinamik dizi, programın çalışması sırasında boyutu değiştirilebilen bir dizidir. C++'daki en popüler dinamik dizi `vector` yapısıdır.

Aşağıdaki kod, boş bir vektör oluşturur ve bu vektöre üç eleman ekler:
```cpp
vector<int> v;
v.push_back(3); // [3]
v.push_back(2); // [3,2]
v.push_back(5); // [3,2,5]
```

Elemanlara sıradan bir dizideki gibi erişilebilir:
```cpp
cout << v[0] << "\n"; // 3
```

`size()` fonksiyonu vektördeki eleman sayısını döndürür. Vektördeki elemanları yazdırmak için:
```cpp
for (int i = 0; i < v.size(); i++) {
  cout << v[i] << "\n";
}
// Veya daha kısa bir yol:
for (auto x : v) {
  cout << x << "\n";
}
```
`back()` fonksiyonu son elemanı döndürürken, `pop_back()` son elemanı siler.

Vektörler başlangıç değerleriyle de oluşturulabilir:
```cpp
// 5 elemanlı bir vektör
vector<int> v1 = {2, 4, 2, 5, 1};

// 10 elemanlı ve tüm değerleri 0 olan bir vektör
vector<int> v2(10);

// 10 elemanlı ve tüm değerleri 5 olan bir vektör
vector<int> v3(10, 5);
```
`push_back` operasyonunun ortalama zaman karmaşıklığı `O(1)`'dir[^1].

`string` veri yapısı da `vector` gibi kullanılabilen bir dinamik dizidir ve ek olarak `+` ile birleştirme, `substr` ile alt string alma gibi özelliklere sahiptir.

## 4.2 Küme (Set) Yapıları

Küme, elemanlar topluluğu barındıran bir veri yapısıdır. Eleman ekleme, arama ve silme işlemlerini destekler.

* `set`: Dengeli bir ikili ağaç (balanced binary tree) üzerine kuruludur ve işlemleri $O(\log n)$ sürede çalışır. Elemanları sıralı tutar.
* `unordered_set`: Kıyım (hashing) kullanır ve işlemleri ortalama olarak $O(1)$ sürede çalışır. Elemanlar sırasızdır.

```cpp
set<int> s;
s.insert(3);
s.insert(2);
s.insert(5);
cout << s.count(3) << "\n"; // 1 (var)
cout << s.count(4) << "\n"; // 0 (yok)
s.erase(3);
cout << s.count(3) << "\n"; // 0
```
Kümelerin önemli bir özelliği, bütün elemanlarının farklı olmasıdır. Bir eleman birden fazla kez eklenemez.

`multiset` ve `unordered_multiset` ise bir elemanın birden fazla kopyasını barındırabilen küme türleridir.

`erase` fonksiyonu bir `multiset`'ten bir elemanın tüm kopyalarını siler. Sadece bir kopyayı silmek için `s.erase(s.find(5));` gibi bir kullanım gerekir.

## 4.3 Map Yapıları

Bir `map`, anahtar-değer çiftlerinden (key-value pairs) oluşan genelleştirilmiş bir dizidir.

* `map`: Dengeli ikili ağaç yapısındadır, anahtarları sıralı tutar ve erişim $O(\log n)$'dir.
* `unordered_map`: Hashleme kullanır, anahtarlar sırasızdır ve erişim ortalama $O(1)$'dir.

```cpp
map<string, int> m;
m["monkey"] = 4;
m["banana"] = 3;
cout << m["banana"] << "\n"; // 3
```
Eğer istenen anahtar map'te bulunmuyorsa, otomatik olarak varsayılan bir değerle (sayılar için 0) eklenir. `count` fonksiyonu bir anahtarın map'te olup olmadığını kontrol etmek için kullanılabilir.

## 4.4 İteratörler ve Aralıklar (Iterators and Ranges)

İteratör, bir veri yapısındaki bir elemanı gösteren bir değişkendir. `begin()` iteratörü ilk elemanı, `end()` iteratörü ise son elemandan *sonraki* pozisyonu gösterir.

Bu iteratörler `sort`, `reverse`, `random_shuffle` gibi birçok standart kütüphane fonksiyonunda kullanılır:
```cpp
sort(v.begin(), v.end());
```
`set` gibi veri yapılarının elemanlarına erişmek için iteratörler kullanılır:
```cpp
set<int> s = {2, 5, 6, 8};
auto it = s.begin();
cout << *it << "\n"; // 2 (en küçük eleman)

it = s.end();
it--;
cout << *it << "\n"; // 8 (en büyük eleman)
```
`set` için `find(x)`, `lower_bound(x)` ve `upper_bound(x)` gibi fonksiyonlar da iteratör döndürür.

## 4.5 Diğer Yapılar

* **`bitset`**: Her değeri 0 ya da 1 olan sabit boyutlu bir dizidir. Hafıza açısından verimlidir ve bit operasyonları (`&`, `|`, `^`) ile hızlıca manipüle edilebilir.
    ```cpp
    bitset<10> s;
    s[1] = 1;
    s[3] = 1;
    cout << s.count() << "\n"; // 1 olan bit sayısı
    ```
* **`deque`**: Hem başından hem de sonundan eleman eklenip çıkarılabilen (`push_front`, `pop_front`, `push_back`, `pop_back`) dinamik bir dizidir. Ortalama `O(1)` zamanda çalışır.
* **`stack`**: Sadece en üstten eleman eklenen (push) ve çıkarılan (pop) bir "LIFO" (Last-In, First-Out) yapısıdır.
* **`queue`**: Sonuna eleman eklenen (push) ve başından eleman çıkarılan (pop) bir "FIFO" (First-In, First-Out) yapısıdır.
* **`priority_queue`**: Her zaman en büyük (veya en küçük) elemana hızlı erişim sağlayan bir yapıdır. Eleman ekleme ve çıkarma $O(\log n)$ sürer.
    ```cpp
    priority_queue<int> q;
    q.push(3);
    q.push(5);
    q.push(2);
    cout << q.top() << "\n"; // 5
    q.pop();
    cout << q.top() << "\n"; // 3
    ```

## 4.6 Sıralama ile Karşılaştırma

Bir problemi hem sıralama hem de veri yapıları ile çözmek mümkün olabilir. Zaman karmaşıklıkları aynı olsa bile (`O(n log n)` gibi), pratik performansları farklılık gösterebilir. Örneğin, iki listedeki ortak eleman sayısını bulma probleminde, sıralama tabanlı bir çözüm genellikle `set` veya `map` tabanlı bir çözümden daha hızlı çalışır çünkü sıralama basit bir işlemdir ve sadece bir kez yapılırken, `set` gibi yapılar her işlemde daha karmaşık bir ağaç yapısını yönetir.

[^1]: (Ç.N.) İnternet sistemleri dizayn edilirken kullanılan standart kütüphanelerdeki dinamik dizilerin boyutunun hangi değerde artacağı kamuya açık bir bilgi olduğundan bazı hacker'ların bu duruma hoş olmayan bir istisna oluşturduğunu söyleyebiliriz.