---
layout: post
title: "Yapay Zekâya Satranç Öğretmek: Sezgi Algoritmaya Sığar mı?"
math: true
categories: 
  - Bilgi
tags: 
  - yapay zekâ
  - satranç
  - algoritma
---

Bir satranç ustası bazen tahtaya birkaç saniye bakıp “Bu konum tehlikeli” der. Hangi kareyi hesapladığını sorduğunuzda ise omuz silkip “Öyle hissettim” cevabını verebilir. Bilgisayarlar omuz silkeme konusunda henüz etkileyici değildir; onlara sezgiyi oluşturan ölçütleri, olasılıkları ve hedefleri açıkça vermek gerekir. İşte yapay zekâya satranç öğretmenin asıl güçlüğü budur: İnsan zihnindeki sessiz bilgiyi çalıştırılabilir bir algoritmaya dönüştürmek.

``

## Satranç Neden Yalnızca Kurallardan İbaret Değildir?

Satranç kuralları bütünüyle formeldir. Fil çapraz gider, şah tehdit altında bırakılamaz ve piyon geriye dönmez. Fakat kuralları bilmek, iyi oynamak anlamına gelmez. Kurallar hangi hamlelerin **mümkün** olduğunu söyler; strateji ise hangisinin **anlamlı** olduğunu belirler.

Bir konumdaki yasal hamleleri dallara ayırarak aramak mümkündür. Ortalama dallanma katsayısı $b$, incelenen derinlik $d$ ise kaba arama maliyeti

$$O(b^d)$$

olarak büyür. Satrançta $b$ çoğunlukla 30–40 civarındadır. Bu nedenle yalnızca birkaç hamle daha derine bakmak bile hesaplama miktarını patlatır. Evren, bilgisayara “Bütün ihtimalleri dene” diyebileceğimiz kadar sabırlı değildir.

## Sezgiyi Sayıya Çevirmek

Klasik satranç programları, aramanın sonundaki konumu bir değerlendirme fonksiyonuyla puanlar:

$$E(s)=w_mM+w_kK+w_pP+w_sS$$

Burada $M$ materyali, $K$ şah güvenliğini, $P$ piyon yapısını, $S$ ise taş etkinliğini temsil eder. $w$ katsayıları bu özelliklerin önemini belirler. Program, yüksek puanlı konumlara ulaşmaya çalışır.

```python
def evaluate(position):
    score = 0
    score += 1.0 * material_balance(position)
    score += 0.3 * king_safety(position)
    score += 0.2 * piece_activity(position)
    score -= 0.25 * pawn_weaknesses(position)
    return score
```

Bu kod bir konumu anlaşılır özelliklerle puanlar. Ancak insan ustanın “Bu fil kötü ama ileride canlanacak” düşüncesi, tek bir katsayıya kolayca sığmaz. Özellikler birbirini etkiler; bugün zayıflık görünen bir piyon yarın saldırının anahtarı olabilir.

| İnsan sezgisi | Klasik algoritma | Öğrenen sistem |
|---|---|---|
| Örüntüyü hızla tanır | Tanımlı özellikleri hesaplar | Veriden temsil öğrenir |
| Nedenini açıklamakta zorlanabilir | Kural ve katsayıları izlenebilir | Kararı çoğu zaman opaktır |
| Az sayıda adayı inceler | Çok sayıda dalı tarar | Olasılıklı hamlelere öncelik verir |
| Deneyim ve bağlama dayanır | Programcının modeline dayanır | Eğitim verisine dayanır |

## Minimax ve Makinenin “Öngörüsü”

Minimax algoritması, rakibin de en iyi cevabı vereceğini varsayar. Yapay zekâ kendi kazancını büyütürken rakibin bunu küçültmeye çalışacağını hesaplar. Alfa-beta budaması ise sonucu değiştirmeyecek dalları atar. Böylece makine daha seçici görünür; fakat bu seçicilik bilinçli bir sezgi değil, matematiksel elemedir.

Modern sistemlerde sinir ağları hangi hamlelerin umut verici olduğunu ve konumun kazanma ihtimalini öğrenebilir. AlphaZero benzeri yaklaşımlar, politika ağı ile aday hamleleri seçer; değer ağı ile konumu değerlendirir. Monte Carlo Ağaç Araması da hesaplama bütçesini daha umut verici bölgelere yönlendirir. Başka bir deyişle sezgi, açık kurallar listesinden çok öğrenilmiş bir olasılık dağılımına dönüşür:

$$\pi(a\mid s)=P(\text{hamle }a\mid\text{konum }s)$$

## Felsefi Sınır: Taklit Etmek, Anlamak mıdır?

Bir sistem ustalar gibi hamle yapıyorsa gerçekten “konumu hissediyor” mudur? İşlevselci bakış, doğru davranışın yeterli olduğunu savunabilir. Buna karşılık başka bir görüş, sembolleri başarıyla işlemenin anlamı kavramak olmadığını söyler. Makine şah kanadındaki baskıyı ölçebilir; fakat baskının ne olduğunu yaşantısal biçimde deneyimlemez.

Üstelik insan sezgisini formelleştirirken onu dönüştürürüz. Söze dökülemeyen deneyim, ölçülebilir özelliklere ayrıldığında daha denetlenebilir ama daha eksik hâle gelebilir. Derin öğrenme bu sorunu ortadan kaldırmaz; yalnızca kuralları insanların yazdığı kutudan, örüntüleri verinin şekillendirdiği daha karanlık bir kutuya taşır.

Sonuçta yapay zekâya satranç öğretmek, sezgiyi eksiksiz biçimde kopyalamak değildir. Amaç; arama, değerlendirme ve öğrenmeyle benzer kararlar üreten farklı bir bilişsel düzenek kurmaktır. Belki de en ilginç ders şudur: Sezgiyi algoritmaya sıkıştırmaya çalışırken yalnızca makineleri değil, insan düşüncesinin ne kadar örtük ve açıklanması zor olduğunu da keşfederiz.
