---
layout: post
title: Rekabetçi Programcı Aralık Sorguları
math: true
categories:
  - Program
tags:
  - aralik-sorgusu
  - range-query
  - c
  - programlama
  - algoritma
  - olimpiyat
  - dizi
  - yarışma
  - segment-agaci
  - fenwick
  - prefix-toplam
  - veri-yapisi
  - kitap
---

Bir dizinin alt aralıklarında hızlıca sorgu yapmak rekabetçi programlamada sık karşılaşılan bir ihtiyaçtır. Bir **aralık sorgusunda** görev, bir dizinin belirli bir alt aralığında bir değeri hesaplamaktır. Tipik aralık sorguları şunlardır:

- `sumq(a, b)`: $[a, b]$ aralığındaki sayıların toplamını bul
- `minq(a, b)`: $[a, b]$ aralığındaki minimum sayıyı bul
- `maxq(a, b)`: $[a, b]$ aralığındaki maksimum sayıyı bul

Örneğin `[1, 3, 8, 4, 6, 1, 3, 4]` dizisinde $[3,6]$ aralığı için `sumq(3,6) = 14`, `minq(3,6) = 1`, `maxq(3,6) = 6` olur.

En basit yaklaşım aralık içindeki tüm elemanlara tek tek bakmaktır; bu $O(n)$ sürer. $q$ sorgu için toplam $O(nq)$ zaman gerekir. Hem $n$ hem de $q$ büyük olduğunda bu yavaş kalır. Neyse ki aralık sorgularını çok daha verimli yapmanın yolları vardır.

## 9.1 Statik Dizi Sorguları

Dizinin **statik** olduğu (sorgular sırasında değerlerin değişmediği) duruma ilk bakacağız. Bu durumda sorguları sabit zamanda yanıtlayan bir veri yapısı oluşturmak yeterlidir.

### Toplam Sorguları

Statik bir dizideki toplam sorgularını **prefix toplam dizisi** ile kolayca çözebiliriz. Prefix toplam dizisindeki $k$. konum, orijinal dizinin $[0, k]$ aralığının toplamına eşittir; yani `sumq(0, k)` değerini tutar. Bu dizi $O(n)$ zamanda oluşturulabilir.

Örneğin `[1, 3, 4, 8, 6, 1, 4, 2]` dizisine karşılık gelen prefix toplam dizisi:

```
1  4  8  16  22  23  27  29
0  1  2   3   4   5   6   7
```

Herhangi bir `sumq(a, b)` değerini $O(1)$ zamanda şu formülle bulabiliriz:

$$\text{sumq}(a, b) = \text{sumq}(0, b) - \text{sumq}(0, a-1)$$

$\text{sumq}(0, -1) = 0$ tanımlaması sayesinde formül $a = 0$ için de geçerlidir. Örneğin:

$$\text{sumq}(3, 6) = \text{sumq}(0, 6) - \text{sumq}(0, 2) = 27 - 8 = 19$$

Bu fikir daha fazla boyuta da genelleşir. İki boyutlu bir prefix toplam dizisi oluşturularak herhangi bir dikdörtgen alt dizi toplamı $O(1)$ zamanda hesaplanabilir. Gri alt dizinin toplamı, $S(X)$'in sol üst köşeden $X$ pozisyonuna gelen dikdörtgen alt dizi toplamı olduğu varsayılarak şu formülle bulunur:

$$S(A) - S(B) - S(C) + S(D)$$

### Minimum Sorgular

Minimum sorgular, toplam sorgularına göre daha zordur. Yine de $O(n \log n)$'lik bir ön işleme ile minimum sorguları $O(1)$ zamanda yanıtlanabilir[^1]. Minimum ve maksimum sorgular benzer şekilde ele alındığından yalnızca minimuma bakacağız.

**Fikir:** Uzunluğu ikinin kuvveti olan tüm `minq(a, b)` değerleri önceden hesaplanır. Örneğin `[1, 3, 4, 8, 6, 1, 4, 2]` dizisi için bu değerler uzunluk 1, 2 ve 4'lük aralıklar için aşağıdaki gibidir:

| a | b | minq(a,b) |   | a | b | minq(a,b) |   | a | b | minq(a,b) |
|---|---|-----------|---|---|---|-----------|---|---|---|-----------|
| 0 | 0 | 1         |   | 0 | 1 | 1         |   | 0 | 3 | 1         |
| 1 | 1 | 3         |   | 1 | 2 | 3         |   | 1 | 4 | 3         |
| 2 | 2 | 4         |   | 2 | 3 | 4         |   | 2 | 5 | 1         |
| 3 | 3 | 8         |   | 3 | 4 | 6         |   | 3 | 6 | 1         |
| 4 | 4 | 6         |   | 4 | 5 | 1         |   | 4 | 7 | 1         |
| 5 | 5 | 1         |   | 5 | 6 | 1         |   | 0 | 7 | 1         |
| 6 | 6 | 4         |   | 6 | 7 | 2         |   |   |   |           |
| 7 | 7 | 2         |   |   |   |           |   |   |   |           |

Toplam $O(n \log n)$ değer, aşağıdaki özyinelemeli formülle hesaplanır ($w = (b - a + 1)/2$):

$$\text{minq}(a, b) = \min(\text{minq}(a,\ a+w-1),\ \text{minq}(a+w,\ b))$$

Sorgu anında $b - a + 1$ değerini geçmeyen en büyük ikinin kuvveti $k$ alınır ve:

$$\text{minq}(a, b) = \min(\text{minq}(a,\ a+k-1),\ \text{minq}(b-k+1,\ b))$$

formülü $O(1)$ zamanda sonucu verir. Örneğin $[1, 6]$ aralığında uzunluk 6 için $k = 4$ seçilir; $[1,4]$ ve $[3,6]$ aralıklarının birleşimi olarak $\text{minq}(1,6) = \min(3, 1) = 1$ bulunur.

## 9.2 İkili İndisli Ağaç (Binary Indexed Tree)

**İkili indisli ağaç** ya da **Fenwick ağacı**[^2], prefix toplam dizisinin dinamik versiyonu olarak düşünülebilir. $O(\log n)$ zamanda iki operasyonu destekler: aralık toplamı sorgusu ve tek eleman güncellemesi. Prefix toplam dizisinden farkı, her güncellemeden sonra diziyi baştan oluşturmak yerine yalnızca ilgili konumları güncellemesidir.

### Yapı

Bu bölümde diziler 1'den indislenir. $p(k)$, $k$'yı tam bölen en büyük 2'nin kuvveti olsun. İkili indisli ağaç `tree` dizisinde şu şekilde tutulur:

$$\text{tree}[k] = \text{sumq}(k - p(k) + 1,\ k)$$

Yani her $k$ konumu, uzunluğu $p(k)$ olan ve $k$'da biten aralığın toplamını tutar. Örneğin $p(6) = 2$ olduğundan `tree[6]`, `sumq(5, 6)` değerini saklar.

`[1, 3, 4, 8, 6, 1, 4, 2]` dizisine karşılık gelen ikili indisli ağaç:

```
1  4  4  16  6  7  4  29
1  2  3   4  5  6  7   8
```

$[1, k]$ aralığı her zaman ağaçta toplamları tutulan $O(\log n)$ alt aralığa bölünebildiğinden `sumq(1, k)` değeri $O(\log n)$ zamanda hesaplanabilir. Örneğin:

$$\text{sumq}(1, 7) = \text{sumq}(1,4) + \text{sumq}(5,6) + \text{sumq}(7,7) = 16 + 7 + 4 = 27$$

$a > 1$ durumunda ise:

$$\text{sumq}(a, b) = \text{sumq}(1, b) - \text{sumq}(1, a-1)$$

### İmplementasyon

İkili indisli ağaç, bit operasyonları kullanılarak verimli biçimde kodlanabilir. $p(k)$ değeri şöyle hesaplanır:

$$p(k) = k\ \&\ {-k}$$

`sumq(1, k)` değerini hesaplayan fonksiyon:

```c
int sum(int k) {
    int s = 0;
    while (k >= 1) {
        s += tree[k];
        k -= k & -k;
    }
    return s;
}
```

$k$. pozisyondaki elemanı $x$ kadar artıran fonksiyon:

```c
void add(int k, int x) {
    while (k <= n) {
        tree[k] += x;
        k += k & -k;
    }
}
```

Her iki fonksiyon da $O(\log n)$ zamanda çalışır; her adımda $O(\log n)$ farklı konuma erişilir ve her hareket $O(1)$ zaman alır.

## 9.3 Segment Ağacı

**Segment ağacı**[^3] iki operasyonu destekleyen genel amaçlı bir veri yapısıdır: aralık sorgusu ve tek eleman güncellemesi. İkili indisli ağaca kıyasla daha geneldir; yalnızca toplam değil minimum, maksimum, EBOB, bit operasyonları (AND, OR, XOR) gibi pek çok sorguyu da $O(\log n)$ zamanda destekler. Bununla birlikte daha fazla bellek kullanır ve implementasyonu biraz daha karmaşıktır[^4].

### Yapı

Segment ağacı bir ikili ağaçtır; en alt seviyedeki yapraklar dizi elemanlarına, iç düğümler ise aralık sorgularına gereken bilgilere karşılık gelir. Dizinin boyutunun ikinin kuvveti olduğu ve sıfır tabanlı indis kullanıldığı varsayılır; gerekirse fazladan eleman eklenebilir.

Toplam sorgularını destekleyen `[5, 8, 6, 3, 2, 7, 2, 6]` dizisine karşılık gelen segment ağacı:

```
           39
       22      17
    13    9   9   8
   5 8  6 3  2 7 2 6
```

Her iç düğüm, kendisine karşılık gelen aralığın elemanlarının toplamını tutar ve bu değer sol ile sağ çocuklarının toplamına eşittir.

Herhangi bir $[a, b]$ aralığı, değerleri ağaç düğümlerinde bulunan $O(\log n)$ alt aralığa bölünebilir. Örneğin $[2, 7]$ aralığı için `sumq(2,7) = 9 + 17 = 26`. Her seviyeden en fazla iki düğüm kullanıldığından toplam düğüm sayısı $O(\log n)$ olur.

Bir dizi güncellemesinden sonra değişen düğümdeki yapraktan köke giden yoldaki tüm iç düğümler güncellenir; bu yol $O(\log n)$ düğüm içerir.

### İmplementasyon

Segment ağacı, $n$ elemanlı bir dizi için $2n$ elemanlı bir dizi içinde tutulur. `tree[1]` köke, `tree[2]` ve `tree[3]` köke bağlı çocuklara karşılık gelir. `tree[n]`'den `tree[2n-1]`'e kadar olan değerler yaprak düğümlerdir.

```
39 22 17 13  9  9  8  5  8  6  3  2  7  2  6
 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15
```

Bu gösterimde `tree[k]`'nin ebeveyni `tree[⌊k/2⌋]`, çocukları `tree[2k]` ve `tree[2k+1]` olur.

`sumq(a, b)` değerini hesaplayan fonksiyon:

```c
int sum(int a, int b) {
    a += n; b += n;
    int s = 0;
    while (a <= b) {
        if (a % 2 == 1) s += tree[a++];
        if (b % 2 == 0) s += tree[b--];
        a /= 2; b /= 2;
    }
    return s;
}
```

$k$. pozisyondaki elemanı $x$ kadar artıran fonksiyon:

```c
void add(int k, int x) {
    k += n;
    tree[k] += x;
    for (k /= 2; k >= 1; k /= 2) {
        tree[k] = tree[2*k] + tree[2*k+1];
    }
}
```

Her iki fonksiyon da $O(\log n)$ zamanda çalışır.

### Diğer Sorgular

Segment ağaçları, bir aralığı iki parçaya bölmenin mümkün olduğu tüm sorgular için kullanılabilir: minimum/maksimum, EBOB, AND/OR/XOR gibi bit operasyonları. Örneğin minimum sorgularını destekleyen ağaçta her düğüm, ilgili aralığın minimumunu tutar.

Segment ağacının ikili ağaç yapısı, ikili arama uygulamasına da olanak tanır. Örneğin minimum sorgularını destekleyen bir ağaçta en küçük değere sahip eleman $O(\log n)$ zamanda bulunabilir; kökten yapraklara doğru inen yolda minimum değer izlenerek bu eleman tespit edilir.

## 9.4 Ek Teknikler

### İndis Sıkıştırması

Bu bölümdeki veri yapıları ardışık sayılardan oluşan diziler üzerine kuruludur. Büyük indisler gerektiğinde (örneğin $10^9$ indisi) bellek yetersizliği sorunu ortaya çıkar. Bu sınır **indis sıkıştırması** ile aşılabilir.

Buradaki fikir, orijinal indisleri $1, 2, 3, \ldots$ gibi ardışık indislerle değiştirmektir. Bunun için algoritma çalışmaya başlamadan önce tüm indislerin bilinmesi gerekir. Sıkıştırma fonksiyonu $c$ sıralamayı korumalıdır: eğer $a < b$ ise $c(a) < c(b)$ olmalıdır. Bu sayede indisler sıkıştırılmış olsa bile sorgular doğru çalışır.

Örneğin orijinal indisler $8$, $555$ ve $10^9$ ise yeni indisler:

$$c(8) = 1, \quad c(555) = 2, \quad c(10^9) = 3$$

### Aralık Güncellemeleri

Şimdiye kadar aralık sorguları yapıp tek eleman güncelleyebilen yapılar incelendi. Tam tersi durumda — aralık güncelleyip tek eleman okumada — **fark dizisi** kullanılır. Fark dizisindeki her değer, mevcut değer ile orijinal değer arasındaki farkı tutar; dolayısıyla orijinal dizi, fark dizisinin prefix toplam dizisidir.

Örneğin `[3, 3, 1, 1, 1, 5, 2, 2]` dizisinin fark dizisi:

```
3  0  -2  0  0  4  -3  0
0  1   2  3  4  5   6  7
```

Fark dizisinin avantajı, orijinal dizideki bir aralığı yalnızca iki elemanı değiştirerek güncelleyebilmesidir. Örneğin $[1, 4]$ aralığındaki tüm değerleri 5 artırmak için fark dizisindeki 1. konumu 5 artırıp 5. konumu 5 azaltmak yeterlidir:

$$\text{Sonuç:}\quad 3 \; 5 \; {-2} \; 0 \; 0 \; {-1} \; {-3} \; 0$$

Genel olarak $[a, b]$ aralığını $x$ kadar artırmak için $a$. konumu $x$ artırıp $b+1$. konumu $x$ azaltırız. Tek eleman güncellemesi ve toplam sorgusunun birlikte gerektiği bu yapı için ikili indisli ağaç veya segment ağacı kullanılır.

Hem aralık sorgularını hem de aralık güncellemelerini bir arada destekleyen daha gelişmiş yapılar Bölüm 28'de ele alınacaktır.

[^1]: Bu teknik sparse table metodu olarak da bilinir. Daha gelişmiş teknikler mevcuttur; ön işleme $O(n)$ zamanda tamamlanabilir, fakat bu yöntemler rekabetçi programlamada nadiren gereklidir.
[^2]: İkili indisli ağaç yapısı P. M. Fenwick tarafından 1994'te tanıtılmıştır.
[^3]: Bu bölümdeki aşağıdan yukarıya implementasyon, 1970'lerin sonlarında geometri problemleri için kullanılan benzer yapılardan esinlenilmiştir.
[^4]: Aslında iki tane ikili indisli ağaç kullanılarak minimum sorguları da yapılabilir; ancak bu yöntem segment ağacına kıyasla daha karmaşıktır.
