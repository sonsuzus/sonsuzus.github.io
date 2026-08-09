---
layout: post
title: "Kontrol Yapıları: if-else, switch ve Döngülerin Makine Seviyesindeki Maliyeti"
math: true
categories: 
  - Bilgi
tags: 
  - kontrol yapıları
  - performans
  - runtime
  - assembly
  - algoritmalar
---

Yüksek seviyeli bir dilde yazılan `if`, `switch` veya `for` satırları zararsız görünür; ancak işlemci bunları doğrudan "karar" olarak algılamaz. Arka planda karşılaştırmalar, koşullu sıçramalar (branch), bellek erişimleri ve bazen tablo üzerinden dolaylı atlamalar çalışır. Bu nedenle kontrol yapısının maliyeti yalnızca kaynak koddaki satır sayısıyla değil, veri dağılımı, derleyici optimizasyonu ve CPU’nun dal tahmin başarısıyla belirlenir.
``

## Kararın atomu: karşılaştırma ve sıçrama

Bir `if-else` yapısı çoğunlukla iki temel makine işlemi üretir: bir karşılaştırma ve bunun sonucuna göre koşullu sıçrama. Kavramsal assembly karşılığı şöyledir:

```asm
cmp eax, 10        ; eax ile 10'u karşılaştır
jl  small_value    ; eax < 10 ise etikete atla
; else gövdesi
jmp end_if
small_value:
; if gövdesi
end_if:
```

Buradaki maliyet sabit görünse de modern işlemciler paralel çalışan boru hatlarına sahiptir. İşlemci, `jl` sonucunu beklemeden hangi yolun çalışacağını **tahmin eder**. Tahmin doğruysa sıçrama neredeyse ucuzdur; yanlışsa yanlış yola ait işler iptal edilir ve boru hattı yeniden doldurulur. Bu ceza mimariye göre değişse de yaklaşık 10–20 çevrim olabilir.

Bir koşulun beklenen maliyetini basitleştirerek şöyle düşünebiliriz:

$$E[C] = C_{base} + P_{miss} \times C_{penalty}$$

Burada $C_{base}$ karşılaştırma ve doğru tahmin edilen sıçramanın maliyeti, $P_{miss}$ yanlış tahmin olasılığı, $C_{penalty}$ ise boru hattı temizleme cezasıdır. Örneğin rastgele dağılan bir boolean veri, tahminci için düzenli bir veriden daha pahalı olabilir.

| Yapı | Tipik düşük seviye karşılık | Güçlü yanı | Olası maliyet |
|---|---|---|---|
| `if-else` | Karşılaştırma + koşullu branch | Az sayıda koşulda nettir | Yanlış branch tahmini |
| `else if` zinciri | Ardışık karşılaştırmalar | Seyrek ve öncelikli durumlar | Geç eşleşmede çok test |
| `switch` | Branch zinciri veya jump table | Çoklu sabit seçenekler | Tablo erişimi / dolaylı atlama |
| `?:` ternary | Branch veya koşulsuz seçim | Küçük ifadelerde kompakt | Derleyiciye ve türe bağlı |

## switch-case ne zaman sıçrama tablosuna dönüşür?

`switch-case`, her zaman sihirli biçimde $O(1)$ değildir. Case değerleri seyrekse derleyici çoğu zaman bir karşılaştırma zinciri ya da ikili arama ağacı üretir. Değerler yoğun bir aralıktaysa, bir **jump table** oluşturmak mantıklı hale gelir. Girdi değeri tablonun indeksine çevrilir ve uygun adrese dolaylı atlama yapılır.

```c
int puan_ver(int seviye) {
    switch (seviye) {
        case 1: return 100;
        case 2: return 250;
        case 3: return 500;
        case 4: return 1000;
        default: return 0;
    }
}
```

Bu kod, yoğun `1..4` aralığı nedeniyle jump table adayıdır. Ancak sadece `case 1`, `case 1000` ve `case 900000` olsaydı devasa ve boşluklarla dolu bir tablo anlamsız olurdu. Derleyici sürümü, optimizasyon seviyesi ve hedef işlemci bu kararı etkiler.

| Case dağılımı | Muhtemel strateji | Yaklaşık arama davranışı |
|---|---|---|
| Az sayıda case | Karşılaştırma zinciri | $O(n)$ |
| Sıralı, orta sayıda seyrek case | İkili arama ağacı | $O(\log n)$ |
| Yoğun sayısal aralık | Jump table | Ortalama $O(1)$ |

## Döngülerin görünmeyen masrafı

Bir döngüde her turda yalnızca gövde çalışmaz. Sayaç artırılır, sınır kontrol edilir ve geri sıçrama yapılır. Basit bir toplama örneği:

```c
long toplam(const int *veri, int n) {
    long sonuc = 0;
    for (int i = 0; i < n; i++) {
        sonuc += veri[i];
    }
    return sonuc;
}
```

Teorik karmaşıklık $T(n) = an + b$ olduğundan çalışma $O(n)$’dir. Fakat pratikte asıl sınırlandırıcı unsur branch olmayabilir: `veri[i]` bellekten gelir ve önbellek kaçırmaları işlemciyi bekletebilir. Düzenli erişimli bu örnekte CPU öngetiricisi başarılıdır; düzensiz pointer takibi yapan döngülerde ise bellek gecikmesi baskın hale gelir.

Döngü koşulu genellikle son tur dışında kolay tahmin edilir: branch çoğu kez "devam et", bir kez "çık" sonucunu verir. Buna karşılık döngü içindeki rastgele `if` koşulları tahminciyi zorlayabilir. Performans kritik kodda önce ölçüm yapmak, sonra gerekirse veriyi gruplayarak branch öngörülebilirliğini artırmak en sağlıklı yaklaşımdır. Kısacası iyi kontrol akışı, yalnızca doğru yolu seçmez; işlemcinin o yolu önceden sezmesine de yardım eder.
