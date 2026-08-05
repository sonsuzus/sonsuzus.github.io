---
layout: post
title: "Aralık Sorgularının İki Ustası: Segment Ağacı ve Fenwick Ağacı"
math: true
categories: 
  - Bilgi
tags: 
  - veri yapıları
  - segment ağacı
  - fenwick ağacı
---

Bir dizideki elemanlar sürekli değişirken belirli bir aralığın toplamını hızlıca bulmak istediğimizi düşünelim. Her sorguda aralığı baştan dolaşmak kolaydır; ancak veri büyüdüğünde işlemciniz küçük bir maraton koşmaya başlar. Segment ağacı ve Fenwick ağacı, aralık sorguları ile nokta güncellemelerini verimli biçimde birleştirerek bu sorunu çözer.

``

## Problem neden zor?

$n$ elemanlı bir dizide `a[i]` değerini değiştiren nokta güncellemeleri ve $[l,r]$ aralığının toplamını isteyen sorgular bulunsun. Doğrudan yaklaşımda güncelleme $O(1)$, sorgu ise $O(n)$ sürer. Prefix toplam dizisi kullanırsak sorguyu $O(1)$ yapabiliriz; fakat tek bir değişiklikten sonra birçok prefix değeri yenileneceği için güncelleme $O(n)$ olur.

İdeal hedef, iki işlemi de yaklaşık $O(\log n)$ zamanda gerçekleştirmektir. Dengeli ağaç mantığı burada devreye girer: Dizinin tamamını değil, değişiklikten etkilenen az sayıdaki özet bilgiyi güncelleriz.

| Yaklaşım | Aralık toplamı | Nokta güncelleme | Bellek |
|---|---:|---:|---:|
| Doğrudan dizi | $O(n)$ | $O(1)$ | $O(n)$ |
| Prefix toplam | $O(1)$ | $O(n)$ | $O(n)$ |
| Fenwick ağacı | $O(\log n)$ | $O(\log n)$ | $O(n)$ |
| Segment ağacı | $O(\log n)$ | $O(\log n)$ | $O(n)$ |

## Fenwick ağacı: Bitlerle çalışan kompakt çözüm

Binary Indexed Tree olarak da bilinen Fenwick ağacı, her hücrede belirli uzunluktaki bir aralığın toplamını saklar. Bir indeksin kapsadığı bölüm, en düşük anlamlı bitiyle belirlenir:

$$\operatorname{lowbit}(x)=x\mathbin{\&}(-x)$$

Örneğin `12` sayısının ikilik gösterimi `1100` olduğundan `lowbit(12)=4` olur. Güncelleme sırasında `i += lowbit(i)`, prefix sorgusunda ise `i -= lowbit(i)` adımları izlenir.

```cpp
class Fenwick {
    int n;
    vector<long long> bit;
public:
    Fenwick(int n) : n(n), bit(n + 1, 0) {}

    void add(int i, long long delta) {
        for (; i <= n; i += i & -i)
            bit[i] += delta;
    }

    long long prefixSum(int i) {
        long long result = 0;
        for (; i > 0; i -= i & -i)
            result += bit[i];
        return result;
    }

    long long rangeSum(int l, int r) {
        return prefixSum(r) - prefixSum(l - 1);
    }
};
```

Kod 1 tabanlı indeksleme kullanır. `[l,r]` toplamı, iki prefix toplamının farkıdır:

$$S(l,r)=S(1,r)-S(1,l-1)$$

Bir değeri `yeniDeger` yapmak için önce `delta = yeniDeger - eskiDeger` hesaplanıp `add(i, delta)` çağrılmalıdır.

## Segment ağacı: Daha esnek ağır iş makinesi

Segment ağacı, kökünde tüm diziyi; çocuklarında ise aralığın sol ve sağ yarılarını saklar. Yapraklar tek elemanları temsil eder. Bir düğümün değeri, toplama probleminde çocuklarının toplamıdır:

$$tree[v]=tree[2v]+tree[2v+1]$$

```cpp
long long query(int v, int tl, int tr, int l, int r) {
    if (l > r) return 0;
    if (l == tl && r == tr) return tree[v];

    int tm = (tl + tr) / 2;
    return query(v * 2, tl, tm, l, min(r, tm))
         + query(v * 2 + 1, tm + 1, tr, max(l, tm + 1), r);
}

void update(int v, int tl, int tr, int pos, long long value) {
    if (tl == tr) tree[v] = value;
    else {
        int tm = (tl + tr) / 2;
        if (pos <= tm) update(v * 2, tl, tm, pos, value);
        else update(v * 2 + 1, tm + 1, tr, pos, value);
        tree[v] = tree[v * 2] + tree[v * 2 + 1];
    }
}
```

Sorgu yalnızca hedef aralıkla kesişen düğümlere iner. Güncelleme de yapraktan köke kadar tek bir yol izler; ağacın yüksekliği $\log_2 n$ civarındadır.

## Hangisini seçmeliyiz?

Yalnızca toplam, XOR veya benzeri prefix farkıyla çözülebilen işlemler varsa Fenwick ağacı kısa, hızlı ve az bellek tüketen seçenektir. Minimum, maksimum, maksimum alt dizi toplamı ya da ileride lazy propagation ile aralık güncellemesi gerekiyorsa segment ağacı daha uygundur.

Kısacası Fenwick ağacı çevik bir motosiklet, segment ağacı ise donanımlı bir arazi aracıdır. Yol düzse motosiklet harikadır; sorgular çamurlanmaya başladığında arazi aracı gülümseyerek öne çıkar.
