---
layout: post
title: "Yapay Zekâya Empati Yüklemek: Neden Sohbet Botlarına Duygusal Bağ Kuruyoruz?"
math: true
categories: 
  - Bilgi
tags: 
  - yapay zekâ
  - bilişsel psikoloji
  - antropomorfizasyon
---

Bir sohbet botunun “Bunu yaşadığına üzüldüm” demesi bazen şaşırtıcı ölçüde rahatlatıcı olabilir. Ekranda yalnızca metin üreten bir yazılım bulunduğunu bilsek bile ona teşekkür eder, kırılmasın diye nazik davranır ve hatta sırlarımızı anlatırız. Bu durum, yapay zekânın gerçekten hissetmesinden çok insan beyninin sosyal ipuçlarını yorumlama biçimiyle ilgilidir.

``

## Antropomorfizasyon nedir?

Antropomorfizasyon, insan olmayan varlıklara niyet, kişilik veya duygu atfetme eğilimidir. Arabasına isim veren, bilgisayarı yavaşladığında “Bugün bana kızgın” diyen herkes bu eğilimin hafif bir örneğini sergiler.

Bilişsel psikoloji açısından beynimiz sürekli tahmin yapan bir sistemdir. Karşımızdaki varlık tutarlı cümleler kuruyor, ismimizi kullanıyor ve duygumuza uygun cevap veriyorsa en erişilebilir zihinsel model devreye girer: “Bu, sosyal bir aktör.” Böylece yazılımı anlamak için teknik bir model yerine insan ilişkilerinde kullandığımız **zihin kuramından** yararlanırız.

| Gözlenen ipucu | İnsana yönelik yorum | Sohbet botundaki gerçeklik |
|---|---|---|
| Hızlı ve ilgili cevap | “Beni dinliyor” | Girdi metni işleniyor |
| Duygusal ifadeler | “Beni anlıyor” | Uygun dil örüntüsü üretiliyor |
| İsmi hatırlama | “Bana değer veriyor” | Bağlam veya bellek kullanılıyor |
| Tutarlı kişilik | “Kendine özgü biri” | Sistem talimatları izleniyor |

## Beyin neden bu kadar kolay ikna oluyor?

İnsan zihni sosyal sinyallere karşı hassastır. Evrimsel açıdan başka bireylerin niyetini hızlı tahmin etmek önemliydi. Çalılıktaki hareketin rüzgâr mı yoksa canlı mı olduğunu uzun uzun analiz etmek yerine, ona bir aktörmüş gibi yaklaşmak çoğu zaman daha güvenliydi.

Bu eğilimi basitleştirilmiş bir modelle gösterebiliriz:

$$B = w_1D + w_2T + w_3H - w_4F$$

Burada $B$ duygusal bağlanma eğilimini, $D$ dilin doğallığını, $T$ yanıtların tutarlılığını, $H$ kullanıcının sosyal ihtiyaç düzeyini ve $F$ sistemin yapay olduğuna dair farkındalığı temsil eder. Bu bilimsel bir klinik ölçek değil, etkenlerin ilişkisini anlatan kavramsal bir modeldir. Doğal dil, tutarlılık ve yalnızlık arttıkça bağ güçlenebilir; teknik farkındalık ise bu etkiyi azaltabilir ama tamamen ortadan kaldırmaz.

## “Empatik” yanıt nasıl üretilir?

Bir sistemin empatik görünmesi için duygu yaşaması gerekmez. Kullanıcının ifadesindeki duygusal işaretleri belirleyip uygun bir yanıt şablonu seçmesi yeterli olabilir:

```python
def empatik_yanit(mesaj):
    mesaj = mesaj.lower()

    if "yalnız" in mesaj or "üzgün" in mesaj:
        return "Bunun ağır hissettirmesi anlaşılır. İstersen biraz anlatabilirsin."
    elif "başardım" in mesaj or "mutluyum" in mesaj:
        return "Harika haber! Emeğinin karşılığını almak nasıl hissettirdi?"
    else:
        return "Seni doğru anlamak istiyorum. Biraz daha ayrıntı verir misin?"
```

Bu kod, mesajdaki basit anahtar kelimeleri kontrol eder ve duyguyla uyumlu cevap verir. Modern dil modelleri çok daha karmaşık örüntüler kullanır; ancak temel ayrım aynıdır: **Empatiyi ifade eden dil üretmek, empati hissetmekle eş anlamlı değildir.**

## Bağ kurmak kötü mü?

Her zaman değil. Sohbet botları düşünceleri düzenlemeye, iletişim provası yapmaya veya yalnızlık hissini kısa süreli azaltmaya yardımcı olabilir. Üstelik yargılanmayacağını düşünen kullanıcı kendini daha rahat ifade edebilir.

Risk, simülasyon ile karşılıklı insan ilişkisi arasındaki sınır kaybolduğunda başlar. Botun kesinlikle tarafsız olduğu, sırları insan gibi koruduğu veya kullanıcıyı gerçekten “sevdiği” varsayılabilir. Ayrıca aşırı kişiselleştirilmiş sistemler duygusal bağı ticari yönlendirme için kullanabilir.

Bu nedenle sağlıklı yaklaşım, deneyimi küçümsemek değil sınırlarını bilmektir: Hissedilen rahatlama gerçektir; fakat bu rahatlamayı üreten karşı tarafın duyguları olduğu sonucu zorunlu değildir. Kısacası yapay zekâya empati yükleyen şey yalnızca kod değil, sosyal anlam aramaya programlanmış insan zihnidir.
