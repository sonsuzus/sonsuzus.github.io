---
layout: post
title: "Bit Maskeleme: Küçücük Bitlerle Kümeler, Durumlar ve Altkümeler"
math: true
categories: 
  - Bilgi
tags: 
  - bit-maskeleme
  - bitsel-operatorler
  - algoritmalar
---

Bir grup anahtarı, özelliği veya seçimi tek bir tamsayı içinde saklamak kulağa sihir gibi gelebilir. Bit maskeleme tam olarak bunu yapar: Her biti bir elemanın varlığına ya da bir durumun açık olup olmadığına ayırır. Böylece klasik veri yapılarına göre daha az bellek kullanabilir, küme işlemlerini birkaç işlemci komutuyla gerçekleştirebilir ve özellikle kombinasyon problemlerini zarif biçimde çözebiliriz.

``

## Temel fikir: Her bit bir eleman

$n$ elemanlı bir kümenin her altkümesi, $n$ bitlik bir sayı ile temsil edilebilir. Sağdan $i$. bit 1 ise $i$. eleman kümede, 0 ise kümede değildir. Örneğin `{A, B, C, D}` evreninde `0101` maskesi `{A, C}` kümesini gösterir.

$n$ bit ile ifade edilebilen farklı durum sayısı:

$$2^n$$

olur. Bu nedenle bit maskeleri genellikle $n$ değerinin küçük olduğu, fakat çok sayıda durumun incelendiği algoritmalarda kullanılır.

| Operatör | Anlamı | Küme yorumu |
|---|---|---|
| `&` | Bitsel VE | Kesişim |
| `\|` | Bitsel VEYA | Birleşim |
| `^` | Bitsel XOR | Simetrik fark |
| `~` | Bitsel DEĞİL | Tümleyen |
| `<<` | Sola kaydırma | İstenen bit için maske üretme |
| `>>` | Sağa kaydırma | Bitleri konumlandırma veya okuma |

## Eleman ekleme, silme ve sorgulama

Bir elemanın biti `1 << i` ifadesiyle oluşturulur. Ardından standart küme işlemleri birkaç satıra iner:

```cpp
int mask = 0;
int i = 2;

mask |= (1 << i);      // 2 numaralı elemanı ekler
bool var = mask & (1 << i); // Eleman kümede mi?
mask &= ~(1 << i);     // Elemanı siler
mask ^= (1 << i);      // Varlık durumunu tersine çevirir
```

Birleşim için `a | b`, kesişim için `a & b`, fark için ise `a & ~b` kullanılabilir. Tümleyen alınırken tamsayının kullanılmayan üst bitleri de ters döneceğinden, sonucu evrenle sınırlamak gerekir:

```cpp
int full = (1 << n) - 1;
int tumleyen = (~mask) & full;
```

`full`, ilk $n$ biti 1 olan evrensel kümedir. Bu küçük ayrıntı unutulursa masum görünen tümleyen işlemi bitlerden oluşan bir canavara dönüşebilir.

## Durum sıkıştırma

Bit maskeleri yalnızca kümeler için değildir. Açık-kapalı seçenekler de tek sayıda saklanabilir. Bir oyunda kapının açık olması, oyuncunun anahtarı taşıması ve alarmın çalışması ayrı bitlerle temsil edilebilir.

| Yaklaşım | Bellek | Karşılaştırma | Uygun kullanım |
|---|---:|---:|---|
| Ayrı `bool` değişkenleri | Görece yüksek | Alan alan yapılır | Okunabilir iş mantığı |
| `vector<bool>` | Dinamik | Döngü gerekebilir | Çok sayıda özellik |
| Bit maskesi | Çok düşük | Tek tamsayı işlemi | Küçük ve yoğun durum uzayı |

Örneğin dinamik programlamada `dp[mask]`, `mask` tarafından belirtilen seçimlere ulaşıldığında elde edilen en iyi sonucu tutabilir. Gezgin satıcı problemindeki yaygın durum $dp[mask][v]$ biçimindedir: Ziyaret edilen şehirler `mask`, son şehir ise $v$ ile gösterilir. Yaklaşık durum sayısı $O(2^n n)$ olur.

## Bütün altkümeleri üretmek

`0` ile $2^n-1$ arasındaki her sayı farklı bir altkümedir:

```cpp
for (int mask = 0; mask < (1 << n); ++mask) {
    for (int i = 0; i < n; ++i) {
        if (mask & (1 << i)) {
            // i numaralı eleman bu altkümede bulunur.
        }
    }
}
```

Bu yöntem $O(n2^n)$ zamanda çalışır. Yalnızca belirli bir `mask` kümesinin altkümelerini gezmek için daha şık bir numara vardır:

```cpp
for (int sub = mask; sub; sub = (sub - 1) & mask) {
    // sub, mask kümesinin boş olmayan bir altkümesidir.
}
// Boş altküme gerekiyorsa ayrıca işlenir.
```

`sub - 1`, en sağdaki 1 bitini düşürüp sağını değiştirir; `& mask` ise maskeye ait olmayan bitleri temizler. Tüm maskeler ve onların altmaskeleri birlikte gezildiğinde toplam karmaşıklık $O(3^n)$ olur.

Bit maskeleme ilk bakışta sayıların içinde saklambaç oynamak gibidir. Ancak bitleri eleman olarak düşünmeye başladığınızda küme işlemleri, durum sıkıştırma ve altküme tarama aynı güçlü fikrin farklı yüzlerine dönüşür.
