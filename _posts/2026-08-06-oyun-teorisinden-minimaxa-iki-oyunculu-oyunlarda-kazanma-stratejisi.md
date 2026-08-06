---
layout: post
title: "Oyun Teorisinden Minimax’a: İki Oyunculu Oyunlarda Kazanma Stratejisi"
math: true
categories: 
  - Bilgi
tags: 
  - oyun teorisi
  - minimax
  - algoritma
---

Satrançta rakibin vezirini tehdit ettiğinde neden hemen sevinmemelisin? Çünkü rakibin de plan yapıyor! Oyun teorisi, kararlarımızın sonucunun yalnızca bize değil, başka oyuncuların seçimlerine de bağlı olduğu durumları matematiksel olarak inceler. Minimax algoritması ise bu fikirleri bilgisayarların anlayabileceği bir oyun ağacına dönüştürerek mümkün olan en güvenli hamleyi seçmelerini sağlar.
``

## Oyun teorisinin temel bileşenleri

Bir oyun; **oyuncular**, oyuncuların seçebileceği **stratejiler**, oyunun mevcut **durumu** ve sonuçları değerlendiren **kazanç fonksiyonundan** oluşur. İki oyunculu sıfır toplamlı bir oyunda bir tarafın kazancı, diğer tarafın kaybıdır. Kazançlar $u_1$ ve $u_2$ ile gösterilirse:

$$u_1 + u_2 = 0$$

Satranç, dama ve tic-tac-toe bu modele oldukça uygundur. Bu oyunlarda oyuncular sırayla hareket eder, oyun durumu herkes tarafından görülür ve şans faktörü bulunmaz. Böyle oyunlara **deterministik, tam bilgili oyunlar** denir.

| Kavram | Açıklama | Tic-tac-toe örneği |
|---|---|---|
| Durum | Oyunun belirli andaki görünümü | Tahtadaki X ve O işaretleri |
| Hamle | Bir durumdan diğerine geçiş | Boş hücreye X koymak |
| Terminal durum | Oyunun sona erdiği durum | Kazanma veya beraberlik |
| Fayda değeri | Sonucun sayısal karşılığı | Kazanma: $1$, beraberlik: $0$, kayıp: $-1$ |

## Minimax nasıl düşünür?

Minimax algoritmasında bir oyuncuya **MAX**, diğerine **MIN** adı verilir. MAX en yüksek skoru seçmeye, MIN ise bu skoru mümkün olduğunca düşürmeye çalışır. Algoritma, rakibin hata yapacağını ummaz; tam tersine, rakibin her zaman en iyi hamleyi oynayacağını varsayar. Biraz karamsardır ama hazırlıksız yakalanmaz!

Bir $s$ durumu için minimax değeri şöyle tanımlanabilir:

$$V(s) = \max V(s') \quad \text{MAX sırasındaysa}$$

$$V(s) = \min V(s') \quad \text{MIN sırasındaysa}$$

Buradaki $s'$, mevcut durumdan ulaşılabilen çocuk durumlardan biridir. Terminal durumda ise değer doğrudan kazanç fonksiyonundan alınır.

## Python ile minimax uygulaması

Aşağıdaki fonksiyon, önceden oluşturulmuş bir oyun ağacını dolaşır. Yaprak düğümler sayısal sonuçları, listeler ise olası hamleleri temsil eder:

```python
def minimax(node, maximizing):
    # Sayıya ulaştıysak oyun bitmiştir.
    if isinstance(node, int):
        return node

    scores = [minimax(child, not maximizing) for child in node]

    # MAX en büyük, MIN en küçük sonucu seçer.
    return max(scores) if maximizing else min(scores)

# MAX oyuncusunun üç farklı hamlesi
 game_tree = [
    [3, 5, 2],
    [9, 1, 4],
    [6, 7, 8]
]

print(minimax(game_tree, True))  # Çıktı: 6
```

MIN her dalda en düşük değeri seçeceği için dalların değerleri sırasıyla $2$, $1$ ve $6$ olur. MAX da bunların en büyüğü olan $6$ değerli üçüncü hamleyi tercih eder. Böylece karar formülü $\max(2,1,6)=6$ olur.

## Kazanma stratejisi nasıl hesaplanır?

Öncelikle geçerli tüm hamleler üretilir ve her hamle için oluşacak durum hesaplanır. Oyun sonuna ulaşılabiliyorsa gerçek fayda değeri kullanılır. Satranç gibi ağacı devasa olan oyunlarda ise belirli bir derinlikte durularak taş üstünlüğü, hareketlilik ve şah güvenliği gibi ölçütlerden oluşan bir **sezgisel değerlendirme fonksiyonu** çalıştırılır.

| Yaklaşım | Avantaj | Dezavantaj |
|---|---|---|
| Tam minimax | Kesin sonucu bulabilir | Büyük ağaçlarda çok yavaştır |
| Derinlik sınırlı minimax | Daha hızlıdır | Değerlendirme hatası yapabilir |
| Alfa-beta budama | Gereksiz dalları atlar | Hamle sıralamasına duyarlıdır |

Alfa-beta budama, sonucu değiştirmeyeceği kesinleşen dalları incelemez. İyi bir hamle sıralamasıyla minimax’ın pratik performansını ciddi biçimde artırır. Sonuç olarak kazanma stratejisi; rakibin en güçlü cevabını hesaba katmak, en kötü sonucu güvenceye almak ve hesaplama sınırları varsa durumları doğru değerlendirmek üzerine kuruludur.
