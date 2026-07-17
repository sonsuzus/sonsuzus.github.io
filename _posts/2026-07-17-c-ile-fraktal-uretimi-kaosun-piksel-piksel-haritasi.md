---
layout: post
title: "C++ ile Fraktal Üretimi: Kaosun Piksel Piksel Haritası"
math: true
categories: 
  - Program
tags: 
  - C++
  - Fraktal
  - Mandelbrot
  - Kaos Teorisi
---

Fraktallar, matematiğin “az kural, çok karmaşa” diyen asi çocuklarıdır. C++ ile fraktal üretmek ise bu çocuklara bir tuval vermek gibidir: basit bir formül yazarsınız, bilgisayar milyonlarca kez tekrarlar ve ekranda sonsuz kıvrımlara benzeyen görsel bir evren belirir. Özellikle Mandelbrot kümesi, kaos teorisinin en popüler posteridir; çünkü minicik bir başlangıç farkı, bambaşka görsel sonuçlar doğurabilir.
``
Fraktal mantığının kalbinde yineleme, yani aynı işlemi tekrar tekrar uygulama fikri vardır. Mandelbrot için temel formül oldukça kısa görünür: $z_{n+1}=z_n^2+c$. Burada $z$ karmaşık bir sayıdır, $c$ ise ekrandaki her pikselin temsil ettiği noktadır. Başlangıçta $z_0=0$ alınır. Sonra bu formül belirli sayıda çalıştırılır. Eğer $|z_n| > 2$ olursa noktanın “kaçtığını” söyleriz; kaçmazsa Mandelbrot kümesinin içinde veya sınırında olabilir.

Bu basitlik aldatıcıdır. Çünkü her piksel için aynı işlem yapılmasına rağmen sonuçlar dramatik biçimde değişir. Bir piksel 10 yinelemede kaçarken komşusu 500 yineleme boyunca dayanabilir. İşte renkleri de genellikle bu kaçış hızına göre veririz.

| Kavram | Programdaki Karşılığı | Görsel Etki |
|---|---|---|
| Karmaşık sayı $c$ | Pikselin matematiksel koordinatı | Fraktalda konum belirler |
| Yineleme sayısı | Döngü limiti | Detay seviyesi artar |
| Kaçış koşulu $|z|>2$ | Döngüden çıkma şartı | Renk yoğunluğunu belirler |
| Yakınlaştırma | Koordinat aralığını daraltma | Sonsuz detay hissi verir |

Aşağıdaki C++ kodu, Mandelbrot kümesini PPM formatında bir görsele yazar. PPM seçmemizin nedeni eğlenceli derecede basit olmasıdır: dosyanın başına birkaç bilgi, ardından RGB değerleri. Yani kütüphane canavarı çağırmadan piksel piksel resim üretebiliriz.

```cpp
#include <fstream>
#include <complex>

int main() {
    const int width = 900;
    const int height = 600;
    const int maxIter = 300;

    std::ofstream out("mandelbrot.ppm");
    out << "P3\n" << width << " " << height << "\n255\n";

    for (int y = 0; y < height; ++y) {
        for (int x = 0; x < width; ++x) {
            double real = -2.5 + x * (3.5 / width);
            double imag = -1.2 + y * (2.4 / height);

            std::complex<double> c(real, imag);
            std::complex<double> z(0, 0);

            int iter = 0;
            while (std::abs(z) <= 2.0 && iter < maxIter) {
                z = z * z + c;
                ++iter;
            }

            int r = (iter * 9) % 256;
            int g = (iter * 5) % 256;
            int b = (iter * 13) % 256;

            if (iter == maxIter) {
                r = g = b = 0;
            }

            out << r << " " << g << " " << b << " ";
        }
        out << "\n";
    }
}
```

Kodda `real` ve `imag` değişkenleri, ekran koordinatını matematiksel düzleme çevirir. Yani `(x, y)` pikselini doğrudan çizmek yerine, onu karmaşık sayı düzlemindeki bir noktaya dönüştürürüz. Sonrasında `z = z * z + c` satırı fraktalın motorudur. Bu satır her piksel için yüzlerce kez çalışır; C++ burada hız avantajını gösterir.

Renk seçimi tamamen deney alanıdır. Yukarıdaki örnekte mod alma ile basit ama canlı bir palet oluşturduk. Daha yumuşak geçişler için logaritmik renklendirme kullanılabilir. Teorik olarak kaçış süresi $n$ ise, renk fonksiyonu $color=f(n)$ gibi düşünülebilir. Fonksiyon ne kadar yaratıcıysa fraktal o kadar “galaksi posteri” havasına bürünür.

| Ayar | Düşük Değer | Yüksek Değer |
|---|---|---|
| `maxIter` | Hızlı ama az detay | Yavaş ama keskin sınırlar |
| Çözünürlük | Küçük dosya | Daha temiz görüntü |
| Koordinat aralığı | Geniş bakış | Yakınlaştırılmış detay |
| Renk formülü | Düz görünüm | Sanatsal sonuç |

Fraktalların büyüsü, deterministik olmalarına rağmen organik görünmeleridir. Aynı formül, aynı başlangıç, aynı sonuç; fakat sonuç, doğadaki kıyı çizgilerini, bulutları ve damar yapılarını hatırlatır. Kaos teorisi burada “rastgelelik” değil, başlangıç koşullarına aşırı duyarlılık demektir.

Bu programı geliştirmek için yakınlaştırma parametreleri ekleyebilir, PNG çıktısı almak için `stb_image_write` kullanabilir veya çok çekirdekli işlem için pikselleri paralel hesaplatabilirsiniz. Sonuçta C++ ile fraktal üretimi sadece görsel bir oyuncak değildir; matematik, performans ve yaratıcılığın aynı döngüde buluştuğu küçük bir evrendir.
