---
layout: post
title: "Yapay Zekâya Mat Olmak: Satranç Tahtasında Rekabet, Ego ve Makine"
math: true
categories: 
  - Bilgi
tags: 
  - yapay zekâ
  - satranç
  - insan-makine etkileşimi
---

Bir insana karşı satranç kaybettiğimizde rakibimizin yüzündeki ifadeyi, hamleler arasındaki tereddüdü ve zafer sevincini görürüz. Yapay zekâya yenildiğimizdeyse karşımızda sevinen biri yoktur; yalnızca soğuk bir değerlendirme puanı ve kaçırdığımız hamleyi gösteren acımasız bir ok vardır. Buna rağmen yenilgi bazen daha ağır gelir. Çünkü makine bizi küçümsemese bile kendi zihnimiz bunu başarıyla yapabilir.
``

## Rekabet için iki taraf gerekir mi?

Rekabeti genellikle iki bilinçli öznenin aynı hedefe ulaşma çabası olarak düşünürüz. Oysa satranç motorunun amacı insan anlamında “kazanmak” değildir. Motor; konumu sayısal olarak değerlendirir, olası hamleleri araştırır ve en yüksek faydayı sağlayan seçeneği bulur.

Basitleştirilmiş biçimde bir motorun tercihi şöyle gösterilebilir:

$$m^* = \arg\max_{m \in M} V(s_m)$$

Burada $M$ mümkün hamleleri, $s_m$ hamleden sonra oluşan konumu, $V$ ise konumun tahmini değerini temsil eder. İnsan “Bu fedayla rakibimi şaşırtayım” diyebilir. Makine ise şaşırtmak istemez; yalnızca hesapladığı değeri yükseltir.

| Özellik | İnsana karşı oyun | Yapay zekâya karşı oyun |
|---|---|---|
| Rakibin motivasyonu | Kazanmak, öğrenmek, eğlenmek | Değerlendirme fonksiyonunu iyileştirmek |
| Psikolojik baskı | Blöf, zaman sıkışması, beden dili | Derin hesaplama ve istikrar |
| Yenilginin yorumu | “Rakibim bugün daha iyiydi.” | “Zekâm yetersiz mi?” |
| Rövanş duygusu | Kişisel ve sosyal | Teknik ve tek taraflı |

Bu fark, karşılaşmanın nesnel yapısını değiştirmese de duygusal anlamını değiştirir. Biz makineyi rakip olarak insanlaştırırız; makine ise bizi bir kişi olarak bile modellemek zorunda değildir.

## Ego neden daha farklı yaralanıyor?

Satranç, zekâyla güçlü biçimde ilişkilendirildiği için sonuçları kolayca kimliğimize bağlarız. “Kötü oynadım” cümlesi kısa sürede “Yeterince zeki değilim” düşüncesine dönüşebilir. Bir insana kaybettiğimizde sonucu deneyim, dikkat veya şans gibi değişkenlerle açıklayabiliriz. Güçlü bir motora karşıysa bahanelerimiz azalır.

Bununla birlikte karşılaştırma adil değildir. Bir satranç motoru milyonlarca konumu inceleyebilir, yorulmaz ve morali bozulmaz. İnsan performansını kabaca

$$P = f(B, D, Y, Z)$$

şeklinde düşünebiliriz. Burada $B$ bilgi, $D$ dikkat, $Y$ yorgunluk ve $Z$ zaman baskısıdır. Makinede bu değişkenlerin karşılığı donanım, arama derinliği ve süre sınırıdır. Dolayısıyla yenilgi, insan zekâsının değersizliğini değil, iki farklı bilişsel sistemin farklı koşullarda yarıştığını gösterir.

## Motor aslında ne yapıyor?

Aşağıdaki küçük Python örneği gerçek bir satranç motoru değildir; makinenin hamlelere duygusal değil, sayısal yaklaşmasını gösteren sade bir modeldir:

```python
moves = {
    "At f5": 0.35,
    "Vezir d3": -0.20,
    "Filxh7+": 1.10
}

def choose_move(options):
    # En yüksek konum puanına sahip hamleyi seçer.
    return max(options, key=options.get)

best_move = choose_move(moves)
print(best_move, moves[best_move])
```

Kod, hamlelerin hikâyesini veya estetiğini anlamaz. `max` fonksiyonu yalnızca en yüksek puanı seçer. Modern motorlar elbette çok daha karmaşıktır; arama ağaçları, sinir ağları ve olasılıksal değerlendirmeler kullanabilirler. Temel ayrım yine aynıdır: İnsan anlam üretir, makine optimizasyon yapar.

## Yenilgiyi yeniden çerçevelemek

Yapay zekâya karşı oynamanın en sağlıklı yolu onu egonun hâkimi değil, geri bildirim aracı olarak görmektir. Motorun “+3.2” değerlendirmesi karakter notu değildir; belirli bir konumdaki avantaj tahminidir. Kaybedilen oyun, kimliğimiz hakkında hüküm değil, kararlarımız hakkında veri sunar.

İşin ironik yanı şudur: Makine zaferiyle gururlanmaz, fakat insan yenilgiden utanabilir. Demek ki mücadelenin önemli bölümü tahtada değil, zihnimizde gerçekleşir. Yapay zekâ bize yalnızca daha iyi hamleleri değil, rekabeti neden kişiselleştirdiğimizi de gösterebilir. Bazen en öğretici oyun, mat olduğumuz değil; matı egomuza açıklamayı başardığımız oyundur.
