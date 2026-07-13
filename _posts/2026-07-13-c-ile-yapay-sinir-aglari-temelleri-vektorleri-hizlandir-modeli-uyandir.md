---
layout: post
title: "C++ ile Yapay Sinir Ağları Temelleri: Vektörleri Hızlandır, Modeli Uyandır"
math: true
categories: 
  - Program
tags: 
  - C++
  - Yapay Sinir Ağları
  - Optimizasyon
---

Yapay sinir ağları kulağa çoğu zaman Python kütüphanelerinin sihirli düğmeleri gibi gelir; fakat sahnenin arkasında olan şey oldukça “mekanik”tir: vektörler çarpılır, matrisler toplanır, türevler hesaplanır ve bellekten veri taşınır. C++ burada devreye girer; çünkü düşük seviyeli bellek kontrolü sayesinde yalnızca modeli değil, modelin öğrenirken yürüdüğü matematiksel yolu da optimize edebiliriz.
``
Bir yapay sinir ağını en sade haliyle düşünelim: Girdi vektörü $x$, ağırlık matrisi $W$, bias vektörü $b$ ve aktivasyon fonksiyonu $f$. Tek katmanlı bir ileri yayılım şu şekilde yazılır: $y = f(Wx + b)$. Burada “öğrenme” dediğimiz şey, $W$ ve $b$ değerlerini kayıp fonksiyonunu azaltacak şekilde güncellemektir. Örneğin ortalama kare hata için $L = \frac{1}{n}\sum (\hat{y}-y)^2$ kullanabiliriz.

C++ ile çalışırken kritik soru şudur: Bu matematiksel ifadeleri bellekte nasıl temsil edeceğiz? Çünkü CPU, veriye hızlı erişirse hesaplama da hızlanır. Dağınık `std::vector<std::vector<float>>` yapıları okunabilir olsa da satırlar bellekte parçalı durabilir. Tek boyutlu, ardışık bir dizi ise cache dostudur.

| Yaklaşım | Bellek Düzeni | Avantaj | Dezavantaj |
|---|---|---|---|
| `vector<vector<float>>` | Parçalı | Kolay anlaşılır | Cache kaçırma olasılığı yüksek |
| Tek boyutlu `vector<float>` | Ardışık | Hızlı erişim, SIMD’ye uygun | İndeks hesabı gerekir |
| Ham pointer / aligned buffer | Kontrollü | En yüksek optimizasyon alanı | Hata yapması kolay |

Bir matrisi tek boyutlu sakladığımızda $W_{ij}$ elemanına erişim formülü şöyledir: $index = i \times cols + j$. Bu küçük formül, C++ tarafında büyük performans farkları yaratabilir.

```cpp
#include <vector>
#include <cmath>

struct DenseLayer {
    int in, out;
    std::vector<float> W;
    std::vector<float> b;

    DenseLayer(int input, int output)
        : in(input), out(output), W(input * output), b(output) {}

    std::vector<float> forward(const std::vector<float>& x) const {
        std::vector<float> y(out, 0.0f);

        for (int i = 0; i < out; ++i) {
            float sum = b[i];
            const int row = i * in;
            for (int j = 0; j < in; ++j) {
                sum += W[row + j] * x[j];
            }
            y[i] = std::tanh(sum); // aktivasyon
        }
        return y;
    }
};
```

Bu kodda `W` matrisi tek boyutlu tutulur. `row + j` erişimi, satırdaki elemanları ardışık okuduğu için işlemci önbelleğiyle iyi anlaşır. Yani CPU’ya “al bakalım, sıradaki veriler tam yanında” demiş oluruz. Bu da özellikle büyük katmanlarda önemlidir.

Öğrenme aşamasında geri yayılım devreye girer. Temel fikir zincir kuralıdır: $\frac{\partial L}{\partial W} = \frac{\partial L}{\partial y} \cdot \frac{\partial y}{\partial W}$. Ardından ağırlıklar şu şekilde güncellenir: $W := W - \eta \frac{\partial L}{\partial W}$. Buradaki $\eta$ öğrenme oranıdır; çok büyükse model zıplar, çok küçükse kaplumbağa gibi ilerler.

| Kavram | Matematiksel Rol | C++ Optimizasyon Noktası |
|---|---|---|
| Ağırlık matrisi | Öğrenilen dönüşüm | Ardışık bellek, hizalama |
| Aktivasyon | Doğrusal olmayanlık | Hızlı fonksiyon seçimi |
| Gradyan | Güncelleme yönü | Geçici kopyaları azaltma |
| Batch | Paralel veri işleme | Döngü düzeni, SIMD, thread |

Performans için dikkat edilmesi gerekenlerden biri gereksiz kopyalardır. Büyük vektörleri fonksiyonlara değer ile geçirmek yerine `const reference` kullanmak gerekir. Ayrıca eğitim döngüsünde sürekli yeni bellek ayırmak pahalıdır; mümkünse buffer’lar önceden oluşturulmalı ve tekrar kullanılmalıdır.

Daha ileri seviyede `alignas(64)`, SIMD komutları, OpenMP veya BLAS kütüphaneleri kullanılabilir. Ancak temeli anlamadan bu araçlara atlamak, turbo motoru bisiklete takmaya benzer. Önce veri yerleşimi, döngü sırası ve matematiksel akış net olmalıdır.

C++ ile sinir ağı yazmak, hazır kütüphane kullanmaya göre daha zahmetlidir; fakat karşılığında modelin kalp atışını duyarsınız. Her çarpım, her toplama, her bellek erişimi sizin kontrolünüzdedir. İşte bu yüzden C++, yapay sinir ağlarını yalnızca kullanmak değil, gerçekten anlamak isteyenler için harika bir laboratuvardır.
