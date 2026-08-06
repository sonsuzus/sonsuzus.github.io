---
layout: post
title: "Geometrik Algoritmalar: Dışbükey Örtüden Tarama Doğrusuna"
math: true
categories: 
  - Bilgi
tags: 
  - geometri
  - algoritma
  - dışbükey örtü
---

Haritadaki noktaları çevreleyen en kısa çiti bulmak, kesişen yol parçalarını tespit etmek veya bir çokgenin alanını hesaplamak… Bilgisayarlı geometrinin bu klasik problemleri, birkaç temel işlem üzerine kurulur. Nokta, doğru ve çokgenleri matematiksel olarak temsil etmeyi öğrendiğimizde dışbükey örtü ve tarama doğrusu gibi ilk bakışta ürkütücü görünen algoritmalar oldukça anlaşılır hâle gelir.
``

## Geometrinin yapı taşları

İki boyutlu düzlemde bir noktayı $P=(x,y)$ biçiminde gösteririz. İki noktanın farkı ise bir vektördür: $AB=B-A$. Uzaklık hesabında Öklid formülü kullanılır:

$$d(A,B)=\sqrt{(x_B-x_A)^2+(y_B-y_A)^2}$$

Geometrik algoritmaların gizli kahramanı çapraz çarpımdır. $A$, $B$ ve $C$ noktaları için yönelim değeri şöyledir:

$$cross(A,B,C)=(B_x-A_x)(C_y-A_y)-(B_y-A_y)(C_x-A_x)$$

Sonucun işareti, üç noktanın dönüş yönünü söyler:

| Sonuç | Geometrik anlam | Algoritmadaki kullanım |
|---|---|---|
| $cross>0$ | Sola dönüş | Saat yönünün tersinde ilerleme |
| $cross<0$ | Sağa dönüş | Uygun olmayan noktayı çıkarma |
| $cross=0$ | Noktalar doğrusal | Çakışma ve sınır kontrolü |

Bu işlem yalnızca çarpma ve çıkarma içerdiği için açı hesaplamaktan daha hızlıdır. Tamsayı koordinatlarda kayan nokta hatalarını da önler.

```cpp
struct Point {
    long long x, y;
};

long long cross(Point a, Point b, Point c) {
    return (b.x - a.x) * (c.y - a.y)
         - (b.y - a.y) * (c.x - a.x);
}
```

Bu fonksiyon; dönüş yönü, doğru parçalarının kesişimi ve dışbükeylik kontrolü gibi birçok işlemin ortak motorudur.

## Çokgen alanı ve yönü

Köşeleri sırayla verilen basit bir çokgenin alanı, ayakkabı bağı formülüyle bulunabilir:

$$2A=\left|\sum_{i=0}^{n-1}(x_i y_{i+1}-y_i x_{i+1})\right|$$

İndisler döngüseldir; yani son noktadan sonra yeniden ilk nokta gelir. Mutlak değer alınmadan önce toplamın işareti, köşelerin saat yönünde mi yoksa ters yönde mi sıralandığını da gösterir.

## Dışbükey örtü: Noktaların etrafına lastik geçirmek

Dışbükey örtü, verilen bütün noktaları kapsayan en küçük dışbükey çokgendir. Sezgisel olarak noktaların çevresine bir lastik geçirip bıraktığımızda oluşan sınırdır. Monotonic Chain algoritması önce noktaları $(x,y)$ sırasına göre sıralar, ardından alt ve üst zincirleri kurar.

```cpp
vector<Point> convexHull(vector<Point> p) {
    sort(p.begin(), p.end(), [](Point a, Point b) {
        return a.x != b.x ? a.x < b.x : a.y < b.y;
    });

    vector<Point> h;
    for (int pass = 0; pass < 2; pass++) {
        size_t start = h.size();
        for (Point q : p) {
            while (h.size() >= start + 2 &&
                   cross(h[h.size()-2], h.back(), q) <= 0)
                h.pop_back();
            h.push_back(q);
        }
        h.pop_back();
        reverse(p.begin(), p.end());
    }
    return h;
}
```

Sıralama $O(n\log n)$, zincirleri oluşturma ise $O(n)$ sürer. `cross <= 0` kullanımı, aynı kenar üzerindeki ara noktaları örtüden çıkarır. Bu noktalar da sonuçta isteniyorsa koşul problem tanımına göre değiştirilmelidir.

## Tarama doğrusu: Olayları sırayla işle

Tarama doğrusu yaklaşımında hayali bir doğru düzlem boyunca hareket eder. Algoritma bütün geometrik şekilleri sürekli incelemek yerine yalnızca başlangıç, bitiş ve kesişim gibi **olaylarda** işlem yapar.

| Yaklaşım | Temel fikir | Tipik karmaşıklık |
|---|---|---|
| Tüm çiftleri deneme | Her doğru parçasını diğerleriyle karşılaştır | $O(n^2)$ |
| Tarama doğrusu | Olayları sırala, aktif elemanları tut | Genellikle $O(n\log n)$ |
| Dışbükey örtü | Gereksiz iç noktaları ele | $O(n\log n)$ |

Örneğin yatay doğru parçalarının çakışmasını ararken başlangıç noktası aktif kümeye eklenir, bitiş noktası geldiğinde çıkarılır. Dikey bir parça işlendiğinde aktif kümede onun $y$ aralığına düşen parçalar sorgulanır. Dengeli bir arama ağacı kullanılırsa ekleme, silme ve arama işlemleri $O(\log n)$ zamanda yapılabilir.

Tarama doğrusu uygulamalarındaki kritik ayrıntı, aynı koordinattaki olayların sırasıdır. Bir parçanın bitişi, diğerinin başlangıcıyla çakışıyorsa kesişimin sayılıp sayılmayacağına göre olay öncelikleri belirlenmelidir. Geometride şeytan ayrıntıda, hata ise çoğunlukla eşitlik durumundadır!
