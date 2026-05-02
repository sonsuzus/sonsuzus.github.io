---
layout: post
title: Rekabetçi Programcı Geometri
math: true
excerpt_separator: "``"
categories:
  - Program
tags:
  - geometri
  - geometry
  - karmaşık-sayılar
  - complex-numbers
  - vektörel-çarpım
  - cross-product
  - çokgen-alanı
  - shoelace-formula
  - pick-teoremi
  - manhattan-uzaklığı
  - oklid-uzaklığı
  - convex-hull
  - nokta-lokasyonu
  - çizgi-kesişimi
  - c
  - programlama
  - algoritma
  - olimpiyat
  - yarışma
  - kodlama
  - matematik
  - kitap
---

Geometri problemlerinde kolay koda dökülebilecek bir çözüm bulmak genellikle zordur; özel durum sayısı fazladır. İyi bir yaklaşım, özel durumları minimize eden matematiksel araçlar seçmektir. Bu bölümdeki temel araçlar **karmaşık sayılar** ve **vektörel çarpım** olacaktır.

**Örnek:** Bir dörtgenin alanı, köşeleri $s = (a+b+c)/2$ olmak üzere Heron Formülü ile iki üçgene bölerek hesaplanabilir; ama hangi köşegen seçileceği özel durumlar doğurur. Bunun yerine doğrudan genel formül:

$$\text{Alan} = \frac{|x_1 y_2 - x_2 y_1 + x_2 y_3 - x_3 y_2 + x_3 y_4 - x_4 y_3 + x_4 y_1 - x_1 y_4|}{2}$$

Bu formülün avantajı **hiç özel durum içermemesi** ve tüm çokgenlere genellenebilmesidir.
``

## 29.1 Karmaşık Sayılar

Bir **karmaşık sayı** $x + yi$ formundadır ($i = \sqrt{-1}$). Geometrik olarak $(x, y)$ noktasına ya da orijinden o noktaya uzanan vektöre karşılık gelir.

C++'ta `complex` sınıfı geometri problemlerini çözmek için güçlü bir araçtır:

```cpp
typedef long long C;
typedef complex<C> P;
#define X real()
#define Y imag()

P p = {4, 2};
cout << p.X << " " << p.Y << "\n"; // 4 2

P v = {3, 1}, u = {2, 2};
P s = v + u;
cout << s.X << " " << s.Y << "\n"; // 5 3
```

**Koordinat tipi seçimi:**
- `long long` → tam sayı koordinatlar; hesaplamalar **kesin**tir, tercih edilir.
- `long double` → reel koordinatlar; kayan nokta hatalarına dikkat! Eşitlik kontrolü için $|a - b| < \varepsilon$ kullanılır ($\varepsilon = 10^{-9}$ gibi).

### Hazır Fonksiyonlar

| Fonksiyon | Açıklama | Örnek |
|---|---|---|
| `abs(v)` | $v = (x,y)$ vektörünün uzunluğu $\sqrt{x^2+y^2}$ | `abs({3,-1} - {4,2})` $\approx 3.162$ |
| `arg(v)` | $v$'nin $x$ eksenine olan açısı (radyan) | `arg({4,2})` $\approx 0.4636$ |
| `polar(s, a)` | Uzunluğu $s$, açısı $a$ olan vektör | `polar(1.0, 0.5)` |

**Döndürme:** Bir vektörü $a$ radyan saat yönünün tersine döndürmek için $\text{polar}(1, a)$ ile çarpmak yeterlidir:

```cpp
P v = {4, 2};
cout << arg(v) << "\n";   // 0.463648
v *= polar(1.0, 0.5);
cout << arg(v) << "\n";   // 0.963648
```

## 29.2 Noktalar ve Çizgiler

### Vektörel Çarpım (Cross Product)

$a = (x_1, y_1)$ ve $b = (x_2, y_2)$ vektörlerinin **vektörel çarpımı**:

$$a \times b = x_1 y_2 - x_2 y_1$$

Bu değer, $a$'dan sonra $b$'nin hangi yöne döndüğünü söyler:

| Değer | Anlam |
|---|---|
| $a \times b > 0$ | $b$, $a$'nın **soluna** döner |
| $a \times b = 0$ | $a$ ve $b$ **aynı doğrultuda** |
| $a \times b < 0$ | $b$, $a$'nın **sağına** döner |

C++ ile `complex` sınıfı kullanarak hesaplama:

```cpp
P a = {4, 2};
P b = {1, 2};
C cross = (conj(a) * b).Y; // 4*2 - 1*2 = 6
```

`conj(a)` → $(x_1, -y_1)$; bununla $b = (x_2, y_2)$ çarpılınca sonucun $Y$ bileşeni $x_1 y_2 - x_2 y_1$ verir.

### Nokta Lokasyonu

$s_1$ ve $s_2$ noktalarından geçen doğruya göre $p$ noktasının konumu:

$$\text{Konum} = (p - s_1) \times (p - s_2)$$

- **Pozitif** → $p$ çizginin **sol** tarafındadır
- **Negatif** → $p$ çizginin **sağ** tarafındadır
- **Sıfır** → $p$ çizgi üzerindedir

### Çizgi Kesişimi

$ab$ ve $cd$ parçalarının kesişip kesişmediğini kontrol etmek için **üç durum** vardır:

**1. Durum — Aynı doğru üzerinde:** Vektörel çarpım ile tüm noktaların aynı doğruda olduğu kontrol edilir; ardından çakışma sıra karşılaştırmasıyla belirlenir.

**2. Durum — Ortak köşe noktası:** Sadece 4 olasılık: $a=c$, $a=d$, $b=c$ veya $b=d$.

**3. Durum — İç kesişim:** $c$ ve $d$ noktaları, $a$'dan $b$'ye çizilen doğrunun farklı taraflarındaysa parçalar kesişir. Vektörel çarpımın işaretleri kontrol edilir.

### Çizgiye Nokta Mesafesi

$s_1$ ve $s_2$'den geçen doğruya $p$ noktasının en kısa mesafesi:

$$d = \frac{|(s_1 - p) \times (s_2 - p)|}{|s_2 - s_1|}$$

**Kanıt:** $s_1$, $s_2$, $p$ köşeli üçgenin alanı iki şekilde yazılabilir:
- $\frac{1}{2}|s_2 - s_1| \cdot d$
- $\frac{1}{2}|(s_1 - p) \times (s_2 - p)|$

Bunlar eşitlenerek $d$ elde edilir.

### Çokgen İçinde Nokta

Bir $p$ noktasının çokgenin içinde mi dışında mı olduğunu bulmak için **ışın atma** yöntemi kullanılır:

1. $p$'den rastgele bir yöne ışın gönder.
2. Işının çokgenin kenarlarıyla kaç kez kesiştiğini say.
3. **Tekse** → içeride; **çiftse** → dışarıda.

```
b (dışarıda) → ışın 0 veya 2 kez kesişir
a (içeride)  → ışın 1 veya 3 kez kesişir
```

## 29.3 Çokgen Alanı

### Ayakkabı Bağı Formülü (Shoelace Formula)

Köşeleri sırasıyla $p_1 = (x_1, y_1), p_2 = (x_2, y_2), \ldots, p_n = (x_n, y_n)$ olan bir çokgenin alanı:

$$\text{Alan} = \frac{1}{2} \left| \sum_{i=1}^{n-1} (x_i y_{i+1} - x_{i+1} y_i) \right|$$

($p_1 = p_n$ yani ilk ve son köşe aynıdır.)

**Örnek:** Köşeleri $(2,4), (5,5), (7,3), (4,1), (4,3)$ olan çokgen için:

$$\text{Alan} = \frac{|(2 \cdot 5 - 5 \cdot 4) + (5 \cdot 3 - 7 \cdot 5) + (7 \cdot 1 - 4 \cdot 3) + (4 \cdot 3 - 4 \cdot 1) + (4 \cdot 4 - 2 \cdot 3)|}{2} = \frac{17}{2}$$

**Formülün fikri:** Her kenar için $y = 0$ çizgisine uzanan bir yamuk düşünülür. Yamuğun işaretli alanı:

$$(x_{i+1} - x_i)\frac{y_i + y_{i+1}}{2}$$

Tüm yamuklardan bu alanlar toplandığında eşdeğer formül elde edilir. Mutlak değer alınmasının nedeni: toplam, köşelerin dolaşım yönüne göre (saat/saat tersi) pozitif ya da negatif olabilir.

### Pick'in Teoremi

Tüm köşeleri **tamsayı koordinatlarda** olan bir çokgenin alanı:

$$\text{Alan} = a + \frac{b}{2} - 1$$

- $a$: Çokgenin **içindeki** tamsayı nokta sayısı
- $b$: Çokgenin **sınırındaki** tamsayı nokta sayısı

**Örnek:** Önceki çokgen için $a = 6$, $b = 7$:

$$\text{Alan} = 6 + \frac{7}{2} - 1 = \frac{17}{2} \checkmark$$

> Pick Teoremi, ayakkabı bağı formülünün tamsayı koordinatlardaki özel halidir ve ikisi her zaman aynı sonucu verir.

## 29.4 Uzaklık Fonksiyonları

### Öklid ve Manhattan Uzaklığı

İki nokta $(x_1, y_1)$ ve $(x_2, y_2)$ arasında:

$$d_{\text{Öklid}} = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$

$$d_{\text{Manhattan}} = |x_1 - x_2| + |y_1 - y_2|$$

**Örnek:** $(2, 1)$ ve $(5, 2)$ noktaları için:

$$d_{\text{Öklid}} = \sqrt{3^2 + 1^2} = \sqrt{10} \approx 3.162$$

$$d_{\text{Manhattan}} = |2-5| + |1-2| = 4$$

Geometrik yorum: Öklid uzaklığındaki "1 birim bölge" bir **daire**, Manhattan uzaklığında ise 45° döndürülmüş bir **kare** (elmas) şeklindedir.

### Koordinat Döndürme ile Manhattan → Çebyşev

Bazı problemler Manhattan uzaklığı ile çalışırken koordinatları 45° döndürmek işleri basitleştirir. Dönüşüm:

$$(x, y) \;\longrightarrow\; (x + y,\; y - x)$$

Bu dönüşümün temel özelliği:

$$|x_1 - x_2| + |y_1 - y_2| = \max\bigl(|x_1' - x_2'|,\; |y_1' - y_2'|\bigr)$$

Yani **Manhattan uzaklığı**, döndürülmüş koordinatlarda **Çebyşev uzaklığına** dönüşür. Bu sayede $x$ ve $y$ koordinatları birbirinden bağımsız ele alınabilir.

**Örnek — Maksimum Manhattan Uzaklığı:**

$n$ nokta arasındaki maksimum Manhattan uzaklığını bulmak:

1. Her $(x, y)$ noktasını $(x+y, y-x)$'e dönüştür.
2. $\max(|x_1' - x_2'|, |y_1' - y_2'|)$ değerini bul.
3. Bu değer ya $x'$ koordinatlarının, ya da $y'$ koordinatlarının maksimum farkından gelir.
4. Her eksen için fark $(\max - \min)$ olarak hesaplanır → **$O(n)$**.

Örneğin $p_1 = (1, 0)$ ve $p_2 = (3, 3)$: Döndürülmüş koordinatlar $p_1' = (1, -1)$, $p_2' = (6, 0)$:

$$|1-3| + |0-3| = \max(|1-6|, |-1-0|) = 5$$

---

> **Özet Tablo**

| Kavram | Formül / Yöntem | Karmaşıklık |
|---|---|---|
| Vektörel çarpım | $x_1 y_2 - x_2 y_1$ | $O(1)$ |
| Nokta lokasyonu | $(p-s_1) \times (p-s_2)$ işareti | $O(1)$ |
| Çizgiye mesafe | $|(s_1-p)\times(s_2-p)| / |s_2-s_1|$ | $O(1)$ |
| Çokgen içinde nokta | Işın atma, kesişim sayısı | $O(n)$ |
| Çokgen alanı | Ayakkabı bağı formülü | $O(n)$ |
| Çokgen alanı (tamsayı) | Pick Teoremi: $a + b/2 - 1$ | $O(n)$ |
| Max Manhattan mesafesi | 45° döndür + Çebyşev | $O(n)$ |

---

> **Kaynak:** *Rekabetçi Programcı* (Competitive Programmer's Handbook — Antti Laaksonen), Bölüm 29.
