---
layout: post
title: "Kuantum Bilgisayarların Felsefi Kâbusu: Süperpozisyon Özgür İradeyi Kurtarabilir mi?"
math: true
categories: 
  - Bilgi
tags: 
  - kuantum bilgisayarlar
  - özgür irade
  - determinizm
---

Klasik bilgisayarların dünyasında bitler uslu çocuklardır: Ya 0’dırlar ya da 1. Kuantum bilgisayarlardaki kübitler ise ölçülene kadar her iki olasılığı da taşıyabilir. Bu tuhaflık, “Evren önceden yazılmış bir program mı?” sorusunu yeniden gündeme getiriyor. Fakat küçük bir uyarı: Bir kübitin kararsız görünmesi, insanın özgür olduğu anlamına otomatik olarak gelmez.

``

## Kübit gerçekten aynı anda 0 ve 1 mi?

Bir klasik bitin durumu yalnızca $0$ veya $1$ olabilir. Kübit ise şu biçimde gösterilir:

$$|psi> = alpha|0> + beta|1>$$

Buradaki $alpha$ ve $beta$, olasılık genlikleridir ve

$$|alpha|^2 + |beta|^2 = 1$$

koşulunu sağlar. Ölçüm yaptığımızda $|alpha|^2$ olasılıkla 0, $|beta|^2$ olasılıkla 1 elde ederiz. Kübit, ölçümden önce gizlice seçilmiş sıradan bir değeri cebinde taşımak zorunda değildir. Süperpozisyon, yalnızca “sonucu bilmiyoruz” demek değil; girişim deneylerinde fiziksel etkileri görülebilen bir kuantum durumudur.

| Özellik | Klasik bit | Kübit |
|---|---|---|
| Durum | 0 veya 1 | Durumların süperpozisyonu |
| Okuma | Değeri doğrudan verir | Olasılıksal sonuç üretir |
| Kopyalama | Kolayca kopyalanabilir | Bilinmeyen durum kusursuz kopyalanamaz |
| Evrim | Mantık kapılarıyla | Üniter kuantum kapılarıyla |

Burada önemli bir ayrıntı var: Kuantum durumunun ölçüm öncesindeki evrimi Schrödinger denklemi altında deterministiktir. Yani başlangıç durumu biliniyorsa dalga fonksiyonunun nasıl gelişeceği belirlenebilir. Belirsizlik özellikle ölçüm sonucunda karşımıza çıkar.

## Determinizmin çatlayan duvarı

Klasik determinizm, evrenin bir andaki bütün koşulları bilinse geleceğin hesaplanabileceğini savunur. Laplace’ın hayalî “cin”i, her parçacığın konumunu ve hızını bilerek yarını okuyabilirdi. Kuantum mekaniğinde ise Heisenberg belirsizlik ilkesi bu hayali sınırlar:

$$Delta x \cdot Delta p >= hbar/2$$

Bu eşitsizlik yalnızca ölçüm cihazlarımızın kötü olduğunu söylemez. Standart yoruma göre konum ve momentum gibi bazı nicelikler aynı anda sınırsız kesinliğe sahip değildir. Bell deneyleri de sonuçların basit, yerel ve önceden saklanmış değişkenlerle açıklanamayacağını güçlü biçimde göstermiştir.

Yine de kuantum teorisinin bütün yorumları aynı hikâyeyi anlatmaz:

| Yorum | Temel fikir | Determinizm durumu |
|---|---|---|
| Kopenhag | Ölçüm sonucu olasılıksaldır | Sonuçlar belirlenmez |
| Çoklu Dünyalar | Tüm sonuçlar farklı dallarda gerçekleşir | Evrensel evrim deterministiktir |
| Bohm mekaniği | Gizli değişkenler parçacıkları yönlendirir | Determinist ama yerel değildir |

Dolayısıyla “Kuantum fiziği determinizmi kesin olarak öldürdü” cümlesi biraz fazla cesurdur. Daha doğru ifade, klasik ve yerel determinizmin ciddi şekilde yara aldığıdır.

## Bir kübitlik yazı tura

Aşağıdaki Qiskit örneği, bir kübiti Hadamard kapısıyla eşit süperpozisyona getirip ölçer:

```python
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

circuit = QuantumCircuit(1, 1)
circuit.h(0)          # Kübiti eşit süperpozisyona hazırlar
circuit.measure(0, 0) # Kuantum durumunu klasik bite dönüştürür

simulator = AerSimulator()
result = simulator.run(circuit, shots=1000).result()
print(result.get_counts())
```

Sonuçlar yaklaşık olarak `{'0': 500, '1': 500}` dağılımına yaklaşır. Ancak her çalıştırmada tam olarak aynı sayıları görmeyiz. Kod bize kuantum olasılığını gösterir; bilinçli tercih yapan minik bir kübit göstermez.

## Rastgelelik özgürlük değildir

Bir kararın önceden belirlenmemiş olması, onun özgürce verildiğini kanıtlamaz. Seçiminiz nöronlardaki kuantum rastgeleliğinden kaynaklanıyorsa bu, kontrolün sizde değil kozmik bir zar atışında olduğu anlamına da gelebilir.

| Kavram | Anlamı |
|---|---|
| Determinizm | Gelecek, önceki durum ve yasalarca belirlenir |
| Rastgelelik | Sonuç önceden kesin değildir |
| Özgür irade | Eylemin özneye, nedenlere ve sorumluluğa bağlanmasıdır |

Kuantum hesaplama özgür iradeyi ne kanıtlar ne de çürütür. Fakat evreni kusursuz çalışan klasik bir saat gibi düşünmenin yetersiz olabileceğini gösterir. Belki felsefi kâbus kübitin hem 0 hem 1 olması değil; özgürlüğün yalnızca bu iki seçenekten birini rastgele seçmekten çok daha karmaşık olmasıdır.
