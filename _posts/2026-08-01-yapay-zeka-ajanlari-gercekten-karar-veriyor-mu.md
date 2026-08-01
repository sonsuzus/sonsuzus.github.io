---
layout: post
title: "Yapay Zekâ Ajanları Gerçekten Karar Veriyor mu?"
math: true
categories: 
  - Bilgi
tags: 
  - yapay zekâ
  - özerk ajanlar
  - makine etiği
---

Bir yapay zekâ ajanı e-posta gönderdiğinde, hisse senedi aldığında veya bir robotun yönünü değiştirdiğinde genellikle “karar verdi” deriz. Ancak bu ifade, gündelik dilin kullanışlı bir kısaltması mı, yoksa sistemin gerçekten özerk ve niyet sahibi olduğunu mu gösteriyor? Yanıt, karar kavramını hangi teknik ve felsefi ölçütlerle tanımladığımıza bağlı.

``

## Seçim yapmak, karar vermek midir?

En basit anlamıyla karar, seçenekler arasından birini belirlemektir. Bu tanım kullanılırsa termostat bile karar veriyor sayılabilir: Sıcaklık eşik değerin altındaysa ısıtıcıyı açar. Fakat burada alternatifleri değerlendiren bağımsız bir özne değil, önceden yazılmış bir koşul vardır.

Bir yapay zekâ ajanı ise çoğunlukla gözlem, iç durum, hedef ve eylem bileşenleriyle modellenir. Ajanın politikası şu şekilde gösterilebilir:

$$a_t = \pi(o_t, m_t, g)$$

Burada $o_t$ gözlemi, $m_t$ belleği, $g$ hedefi ve $a_t$ seçilen eylemi temsil eder. Politika $\pi$, bu girdileri bir eyleme dönüştürür. Sistem öğreniyorsa politika sabit kurallardan değil, verilerle optimize edilmiş parametrelerden oluşabilir.

| Sistem | Alternatif seçer mi? | Hedefini değiştirir mi? | Gerekçe üretebilir mi? | Özerklik düzeyi |
|---|---:|---:|---:|---|
| Termostat | Evet | Hayır | Hayır | Çok düşük |
| Satranç motoru | Evet | Hayır | Sınırlı | Düşük |
| Araç kullanan ajan | Evet | Sınırlı | Kısmen | Orta |
| Kendi hedefini kuran varsayımsal ajan | Evet | Evet | Evet | Yüksek |

Tablo önemli bir ayrımı gösteriyor: **Eylem seçimi**, tek başına **amaç seçimi** değildir. Bir satranç motoru hamlesini belirleyebilir ama neden satranç oynadığını sorgulamaz.

## Özerklik bir açma-kapama düğmesi değildir

Özerkliği ikili bir özellik yerine derece olarak düşünmek daha yararlıdır. Bir ajanın özerklik puanı kabaca şöyle modellenebilir:

$$A = w_1E + w_2L + w_3G + w_4R$$

Burada $E$ çevresel değişikliklere uyumu, $L$ öğrenme kapasitesini, $G$ hedef üretme yeteneğini, $R$ ise insan müdahalesi olmadan çalışma süresini ifade eder. Ağırlıklar kullanım alanına göre değişir. Örneğin bir Mars robotunda müdahalesiz çalışma, öneri algoritmasında ise hedeflerin kim tarafından belirlendiği daha önemli olabilir.

Aşağıdaki basitleştirilmiş ajan, çevresini değerlendirerek eylem seçer:

```python
class Ajan:
    def __init__(self, enerji=100):
        self.enerji = enerji
        self.hedef = "veri_topla"

    def karar_ver(self, tehlike, veri_degeri):
        if tehlike > 0.8:
            return "geri_cekil"
        if self.enerji < 20:
            return "sarj_ol"
        if veri_degeri > 0.6:
            return "veri_topla"
        return "kesfet"
```

Bu kod farklı koşullarda farklı eylemler üretir; fakat hedefleri ve öncelikleri geliştirici tarafından belirlenmiştir. Dolayısıyla davranışsal özerklik vardır, güçlü anlamda amaçsal özerklik yoktur.

## Peki niyet nerede başlar?

İnsan niyeti yalnızca sonuç üretmekten ibaret değildir. İnançlar, arzular, öz farkındalık ve “başka türlü davranabilirdim” düşüncesiyle ilişkilidir. Bugünkü ajanların “Dosyayı silmek istiyorum” demesi, çoğunlukla içsel bir isteğin kanıtı değil, dilsel bir çıktıdır.

Yine de niyet kavramını işlevsel biçimde kullanabiliriz. Bir sistem hedefini zaman boyunca koruyor, plan yapıyor, başarısızlıkta planını yeniliyor ve eylemlerini açıklayabiliyorsa ona **niyet atfetmek** tahmin yapmayı kolaylaştırır. Bu, sistemin bilinçli olduğunu değil, niyet diliyle verimli biçimde modellenebildiğini gösterir.

Sonuç olarak bir sistem, seçenekleri değerlendirip bağlama göre eylem seçtiğinde teknik anlamda karar veriyor sayılabilir. Ancak güçlü özerklik için yalnızca “nasıl” sorusunu değil, hedeflerin kaynağını açıklayan “neden” sorusunu da incelemeliyiz. Ajanlarımız giderek daha bağımsız davranabilir; yine de onların amaçları çoğu zaman insan tasarımının görünmez parmak izlerini taşır.
