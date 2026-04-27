---
layout: post
title: Rekabetçi Programcı Yazı Algoritmaları
math: true
excerpt_separator: "``"
categories:
  - Program
tags:
  - yazı-algoritmaları
  - string-algorithms
  - trie
  - z-algoritması
  - string-hashing
  - polinom-hashleme
  - örüntü-bulma
  - çarpışma
  - doğum-günü-paradoksu
  - c
  - programlama
  - algoritma
  - olimpiyat
  - yarışma
  - kodlama
  - matematik
  - kitap
---

**Yazı algoritmaları**, metinleri verimli şekilde işlemek için kullanılır. Pek çok yazı problemi $O(n^2)$'de kolayca çözülse de asıl hedef $O(n)$ veya $O(n \log n)$'e inmektir. Temel örnek **örüntü bulma** problemidir: $n$ uzunluğundaki yazıda $m$ uzunluğundaki örüntü nerede geçiyor?
``

## 26.1 Yazı Terminolojisi

$n$ uzunluğundaki $s$ yazısı **sıfır tabanlı** indislenir: $s[0], s[1], \ldots, s[n-1]$.

| Kavram | Tanım | Örnek (`ABCD`) |
|---|---|---|
| **Alt dize** (substring) | Ardışık karakterler; $s[a \ldots b]$ | `A`, `AB`, `ABC`, `ABCD`, … |
| **Alt dizi** (subsequence) | Ardışık olmak zorunda değil | `A`, `AC`, `BD`, … |
| **Ön ek** (prefix) | Baştan başlayan alt dize | `A`, `AB`, `ABC`, `ABCD` |
| **Son ek** (suffix) | Sonla biten alt dize | `D`, `CD`, `BCD`, `ABCD` |
| **Rotasyon** | Karakterleri sağa/sola kaydırma | `ABCD`, `BCDA`, `CDAB`, `DABC` |
| **Periyot** (period) | Yazıyı tekrarla oluşturan ön ek | `ABCABCA`'nın en kısa periyodu `ABC` |
| **Sınır** (border) | Hem ön ek hem son ek olan alt dize | `ABACABA`'nın sınırları: `A`, `ABA`, `ABACABA` |

Sözlük sıralaması (lexicographical order): $x < y$ için ya $x \neq y$ ve $x$, $y$'nin ön ekidir; ya da $x[k] < y[k]$ olan ilk $k$ pozisyonu vardır.

## 26.2 Trie Yapısı

**Trie**, bir yazı kümesini tutan köklü ağaçtır. Ortak ön ekli yazılar aynı dalı paylaşır.

Örnek: $\{\text{CANAL, CANDY, THE, THERE}\}$ kümesi için trie:

```
(kök)
├── C → A → N → A → L *
│             └── D → Y *
└── T → H → E *
               └── R → E *
```

`*` o noktada bir yazının bittiğini gösterir (THE, THERE gibi iç içe yazılar için gereklidir).

**İşlemler:**
- $n$ uzunluğunda yazı **arama:** $O(n)$
- $n$ uzunluğunda yazı **ekleme:** $O(n)$
- Bir yazının **en uzun ön eki** kümede mi? → $O(n)$
- Her düğümde sayaç tutularak ön eke sahip yazı sayısı da bulunabilir

**Dizi temsili:**

```c
int trie[N][A];
// N: maksimum düğüm sayısı, A: alfabe büyüklüğü
// trie[s][c]: s düğümünden c karakteriyle gidilen sonraki düğüm
// Kök düğüm: 0
```

## 26.3 Yazı Hashleme

**Yazı hashleme**, iki yazının aynı olup olmadığını verimli şekilde belirler: karakterleri tek tek karşılaştırmak yerine **hash değerlerini** karşılaştırırız.

### Hash Değeri Hesaplama (Polinom Hashleme)

$n$ uzunluğundaki $s$ yazısının hash değeri:

$$H(s) = \Bigl(s[0] \cdot A^{n-1} + s[1] \cdot A^{n-2} + \cdots + s[n-1] \cdot A^0\Bigr) \bmod B$$

$A$ ve $B$ önceden seçilen sabitlerdir. Örneğin `ALLEY` için karakter kodları $65, 76, 76, 69, 89$; $A=3$, $B=97$ ile:

$$H = (65 \cdot 3^4 + 76 \cdot 3^3 + 76 \cdot 3^2 + 69 \cdot 3^1 + 89 \cdot 3^0) \bmod 97 = 52$$

### Ön İşleme ile $O(1)$ Alt Dize Hashi

$h[k] = H(s[0 \ldots k])$ ve $p[k] = A^k \bmod B$ dizileri $O(n)$'de oluşturulur:

$$h[0] = s[0], \qquad h[k] = (h[k-1] \cdot A + s[k]) \bmod B$$
$$p[0] = 1, \qquad p[k] = (p[k-1] \cdot A) \bmod B$$

$a > 0$ için $s[a \ldots b]$ alt dizesinin hash değeri $O(1)$'de:

$$H(s[a \ldots b]) = \bigl(h[b] - h[a-1] \cdot p[b-a+1]\bigr) \bmod B$$

Bu sayede kaba kuvvet örüntü eşleştirme $O(n^2)$'den $O(n)$'e iner.

**Ek uygulama:** Hashleme + ikili arama ile iki yazının sözlük sırası $O(\log n)$'de bulunur (ortak ön ek uzunluğu ikili aramayla bulunur).

### Çarpışmalar ve Parametre Seçimi

Farklı iki yazının aynı hash değerini almasına **çarpışma** denir ve yanlış sonuç üretir.

Üç senaryo ($n = 10^5$ için çarpışma olasılıkları):

| $B$ sabiti | 1 karşılaştırma | $x$ vs $y_1 \ldots y_n$ | Tüm çiftler |
|---|---|---|---|
| $10^3$ | 0.001 | 1.000 | 1.000 |
| $10^6$ | 0.000001 | 0.632 | 1.000 |
| $10^9$ | $\approx 0$ | $\approx 0$ | **0.393** |
| $10^{12}$ | $\approx 0$ | $\approx 0$ | 0.0005 |

3. senaryo **doğum günü paradoksudur**: Tüm çiftler karşılaştırıldığında $B \approx 10^9$ ile çarpışma olasılığı yaklaşık %39'dur!

**Önerilen sabitler:**
```
A = 911382323
B = 972663749
```

**Güvenli kullanım:** İki farklı $(A, B)$ çiftiyle paralel hash — çarpışma ihtimali $\approx 10^{-18}$.

> ⚠️ $B = 2^{32}$ veya $B = 2^{64}$ gibi 2'nin kuvvetlerini **kullanmayın**; bu parametrelerle her zaman çarpışma üretebilen girdiler oluşturmak mümkündür.

## 26.4 Z-Algoritması

$n$ uzunluğundaki $s$ yazısının **Z-dizisi** $z$, her $k$ için $k$ pozisyonundan başlayan ve aynı zamanda $s$'nin ön eki olan en uzun alt dizenin uzunluğunu verir:

$$z[k] = p \iff s[0 \ldots p-1] = s[k \ldots k+p-1]$$

**Örnek:** `ACBACDACBACBACDA` için Z-dizisi:

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A | C | B | A | C | D | A | C | B | A | C | B | A | C | D | A |
| – | 0 | 0 | 2 | 0 | 0 | **5** | 0 | 0 | **7** | 0 | 0 | 2 | 0 | 0 | 1 |

Örneğin $z[6] = 5$ çünkü `ACBAC` ($= s[6 \ldots 10]$) yazının ön ekidir ama `ACBACB` değil.

### Algoritmanın Çalışması

Z-algoritması bir $[x, y]$ aralığı tutar: $s[x \ldots y]$, $s$'nin bir ön ekidir ve $y$ mümkün olduğunca büyük tutulur.

Her $k$ pozisyonu için:
1. $z[k-x]$ değerine bakılır.
   - $k + z[k-x] < y$ ise → $z[k] = z[k-x]$ (karaktere bakmaya gerek yok).
   - $k + z[k-x] \geq y$ ise → $y$'den devam ederek karakter karakter karşılaştır.
2. Gerekirse $[x, y]$ güncellenir.

Her karakter en fazla bir kez yeni karşılaştırmaya girer → **toplam süre $O(n)$**.

### Örüntü Bulma ile Kullanım

$p$ örüntüsünün $s$ yazısında geçtiği yerleri bulmak için:

$$t = p \# s$$

oluşturulur; `#` karakteri ne $p$'de ne $s$'de geçer. $t$'nin Z-dizisinde $|p|$ değerine eşit olan pozisyonlar örüntünün başlangıç noktalarıdır.

**Örnek:** $s = \text{HATTIVATTI}$, $p = \text{ATT}$

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A | T | T | # | H | A | T | T | I | V | A | T | T | I |
| – | 0 | 0 | 0 | 0 | **3** | 0 | 0 | 0 | 0 | **3** | 0 | 0 | 0 |

5. ve 10. pozisyonlar $z = 3 = |p|$ → `ATT`, `HATTIVATTI`'da 1. ve 6. indislerde geçer.

### Implementasyon

```cpp
vector<int> z(string s) {
    int n = s.size();
    vector<int> z(n);
    int x = 0, y = 0;
    for (int i = 1; i < n; i++) {
        z[i] = max(0, min(z[i-x], y-i+1));
        while (i+z[i] < n && s[z[i]] == s[i+z[i]]) {
            x = i; y = i+z[i]; z[i]++;
        }
    }
    return z;
}
```

### Hashleme vs Z-Algoritması

| | Yazı Hashleme | Z-Algoritması |
|---|---|---|
| **Hız** | $O(n)$ ön işleme, $O(1)$ sorgu | $O(n)$ tek geçiş |
| **Güvenlik** | Çarpışma riski var | Her zaman doğru |
| **Kod kolaylığı** | Daha basit | Daha karmaşık |
| **Esneklik** | İkili arama ile sözlük sırası | Yalnızca ön ek eşleşmeleri |

---

> **Kaynak:** *Rekabetçi Programcı* (Competitive Programmer's Handbook — Antti Laaksonen), Bölüm 26.
