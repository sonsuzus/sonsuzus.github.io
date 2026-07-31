---
layout: post
title: "Skinner’ın Güvercinlerinden Yapay Zekâ Ajanlarına: Pekiştirmeli Öğrenmenin Davranışçı Kökleri"
math: true
categories: 
  - Bilgi
tags: 
  - pekiştirmeli öğrenme
  - davranışçılık
  - yapay zekâ
---

Bir güvercinin doğru düğmeyi gagalamasıyla bir yapay zekâ ajanının oyunda puan toplaması arasında gerçekten bağlantı olabilir mi? Şaşırtıcı biçimde evet! B. F. Skinner’ın davranışçı psikoloji deneyleri ile modern pekiştirmeli öğrenme algoritmaları, zekânın iç dünyasından çok davranışların sonuçlarına odaklanan benzer bir mantık kullanır.
``
## Skinner kutusunda öğrenmek

Davranışçılığa göre öğrenmeyi açıklamak için zihnin görünmeyen süreçleri hakkında tahmin yürütmek şart değildir. Organizmanın hangi durumda ne yaptığını ve ardından neyle karşılaştığını gözlemlemek yeterlidir. Skinner’ın **edimsel koşullanma** yaklaşımında bir davranış olumlu sonuç doğuruyorsa tekrarlanma olasılığı artar; olumsuz sonuç doğuruyorsa azalır.

Skinner kutusundaki bir güvercin, belirli bir ışık yandığında düğmeyi gagalayıp yem kazanabilir. Başlangıçta rastgele davranır. Fakat yemle sonuçlanan hareketler zaman içinde sıklaşır. Burada güvercine açıkça “ışık yanınca düğmeye bas” denmez; doğru davranış sonuçları aracılığıyla biçimlendirilir.

| Davranışçılık kavramı | Pekiştirmeli öğrenmedeki karşılığı | Örnek |
|---|---|---|
| Organizma | Ajan | Güvercin veya oyun botu |
| Çevre | Ortam | Skinner kutusu veya simülasyon |
| Uyarıcı/durum | State | Işığın yanması veya oyundaki konum |
| Davranış | Action | Gagalamak veya sağa gitmek |
| Pekiştireç | Reward | Yem veya puan |

## Ajanın matematiksel Skinner kutusu

Pekiştirmeli öğrenmede ajan, bulunduğu $s_t$ durumunda bir $a_t$ eylemi seçer. Ortam bunun ardından $r_{t+1}$ ödülünü ve yeni $s_{t+1}$ durumunu üretir. Ajanın amacı yalnızca anlık ödülü değil, gelecekte elde edebileceği ödülleri de büyütmektir:

$$G_t = r_{t+1} + \gamma r_{t+2} + \gamma^2 r_{t+3} + \cdots$$

Buradaki $\gamma$, gelecekteki ödüllerin ne kadar önemsendiğini belirleyen **iskonto katsayısıdır**. Değer sıfıra yakınsa ajan sabırsız, bire yakınsa uzun vadeli düşünmeye yatkındır. Güvercinin hemen verilen yeme daha hızlı tepki vermesi gibi, algoritmalar da yakın ödülleri daha güçlü değerlendirebilir.

Basit Q-learning güncellemesi bu davranış-sonuç bağını sayısallaştırır:

$$Q(s,a) \leftarrow Q(s,a) + \alpha[r + \gamma \max_{a'}Q(s',a') - Q(s,a)]$$

Formüldeki $Q(s,a)$, belirli durumda yapılan eylemin beklenen değeridir. $\alpha$ öğrenme hızını, köşeli parantez içindeki bölüm ise beklenti ile gerçekleşen sonuç arasındaki farkı temsil eder. Beklenenden iyi bir ödül gelirse eylemin değeri yükselir.

```python
# Tek bir deneyimden Q değerini günceller.
def q_guncelle(q, durum, eylem, odul, yeni_durum,
               alpha=0.1, gamma=0.95):
    mevcut = q[durum][eylem]
    en_iyi_gelecek = max(q[yeni_durum])
    hata = odul + gamma * en_iyi_gelecek - mevcut
    q[durum][eylem] += alpha * hata
```

Bu kod, ajanın yaşadığı tek bir deneyimi hafızasındaki davranış değerine dönüştürür. Yem geldiyse ilgili “gagalama” seçeneği güçlenir; ceza geldiyse zayıflar.

## Benzerlik nerede sona eriyor?

| Skinner’ın yaklaşımı | Modern pekiştirmeli öğrenme |
|---|---|
| Biyolojik organizmayı inceler | Matematiksel ajanı optimize eder |
| Deneyler fiziksel ve görece yavaştır | Milyonlarca simülasyon çalıştırılabilir |
| Pekiştireç biyolojik anlam taşıyabilir | Ödül, tasarımcının belirlediği sayıdır |
| Davranış gözlemle açıklanır | İç değerler ve politikalar hesaplanır |

En önemli fark, yapay ajanın ödülü gerçekten “istememesidir”. Ödül onun için haz değil, optimizasyon sinyalidir. Üstelik yanlış tanımlanan bir ödül fonksiyonu beklenmedik davranışlar doğurabilir. Ajan oyunu kazanmak yerine sonsuz puan veren bir hatayı keşfedebilir. Bu durum, güvercinlerin rastlantısal ödüller sonucunda batıl davranışlar geliştirmesini hatırlatır.

Sonuç olarak pekiştirmeli öğrenme, davranışçılığın dijital bir kopyası değildir; fakat onun güçlü sezgisini taşır: Karmaşık davranışlar, eylemler ile sonuçları arasındaki geri bildirim döngüsünden doğabilir. Skinner’ın kutusu bugün sanal ortamlara dönüşmüş olsa da temel soru aynıdır: **Hangi sonuç, hangi davranışı güçlendiriyor?**
