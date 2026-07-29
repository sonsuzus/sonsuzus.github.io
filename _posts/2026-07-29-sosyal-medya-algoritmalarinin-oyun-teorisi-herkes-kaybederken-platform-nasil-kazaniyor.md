---
layout: post
title: "Sosyal Medya Algoritmalarının Oyun Teorisi: Herkes Kaybederken Platform Nasıl Kazanıyor?"
math: true
categories: 
  - Bilgi
tags: 
  - oyun teorisi
  - sosyal medya algoritmaları
  - dikkat ekonomisi
---

Bir sosyal medya uygulamasını “yalnızca beş dakika” kullanmak için açıp kırk dakika sonra kendinizi hiç tanımadığınız insanların tartışmasını izlerken bulduysanız, bu sadece irade eksikliği değildir. Kullanıcılar, içerik üreticileri, reklamverenler ve platform aynı oyun masasında farklı ödüllerin peşindedir. Algoritma ise tarafsız bir krupiye değil; masanın kurallarını belirleyen ve oyun uzadıkça kazanan işletmecidir.
``

## Oyuncular ve Ödül Fonksiyonları

Oyun teorisinde oyuncuların olası davranışlarına **strateji**, sonuçlardan elde ettikleri değere ise **fayda** denir. Basitleştirilmiş bir sosyal medya oyununda kullanıcının faydasını şöyle yazabiliriz:

$$U_k = B - \alpha T - \beta S$$

Burada $B$, eğlence ve bilgi gibi kazanımları; $T$, harcanan zamanı; $S$ ise stres, kıyaslama ve dikkat dağınıklığı gibi psikolojik maliyetleri temsil eder. Kullanıcı kaydırmaya devam ederken anlık $B$ yüksek, uzun vadeli maliyetler ise görünmezdir.

Platformun faydası daha farklıdır:

$$U_p = rE - cM$$

$E$ etkileşim ve ekranda kalma süresi, $r$ bunların reklam gelirine dönüşme oranı, $M$ moderasyon ve altyapı maliyetidir. Kullanıcı “iyi vakit geçirmeyi” isterken platform çoğunlukla “daha uzun vakit geçirilmesini” ister. Bu hedefler aynı şey değildir.

| Oyuncu | Temel hedef | Rasyonel strateji | Muhtemel yan etki |
|---|---|---|---|
| Kullanıcı | Bilgi, eğlence, sosyallik | İlgi çekici içerik tüketmek | Zaman ve dikkat kaybı |
| Üretici | Görünürlük ve gelir | Daha sık, çarpıcı içerik üretmek | Sansasyon ve tükenmişlik |
| Reklamveren | Dönüşüm | En dikkat çekici mesajı vermek | Mahremiyet baskısı |
| Platform | Etkileşim ve gelir | Akışı kişiselleştirmek | Kutuplaşmanın ödüllendirilmesi |

## Dijital Mahkûmlar İkilemi

İçerik üreticileri açısından sistem, **Mahkûmlar İkilemi**ne benzer. Her üretici sakin, doğrulanmış ve kaliteli içerik yayımlarsa ekosistem güvenilir kalır. Fakat tek bir üretici abartılı başlık kullanırsa daha fazla tıklama elde edebilir. Diğerleri de görünmez olmamak için aynı stratejiye geçer.

| A / B | B kaliteli üretir | B sansasyon üretir |
|---|---:|---:|
| **A kaliteli üretir** | 6, 6 | 2, 9 |
| **A sansasyon üretir** | 9, 2 | 4, 4 |

Herkes için daha iyi sonuç $(6,6)$ iken bireysel teşvikler sistemi $(4,4)$ noktasına iter. Bu durum bir **Nash dengesi**dir: Hiçbir üretici tek başına strateji değiştirerek kazancını artıramaz. Topluca kaybedilir; ancak daha fazla içerik, yorum ve reklam gösterimi oluştuğundan platform kazanır.

## Algoritma Neden Öfkeyi Seviyor?

Algoritmanın gerçekten duyguları yoktur; ölçebildiği sinyaller vardır. Öfke, şaşkınlık ve korku genellikle yorum, paylaşım ve izleme süresi üretir. Eğer sıralama puanı

$$R = 0.4L + 0.3Y + 0.3C$$

şeklinde beğeni ($L$), paylaşım ($Y$) ve yorum ($C$) üzerinden hesaplanıyorsa doğru ama sakin bir gönderi, tartışmalı bir gönderinin gerisinde kalabilir. Algoritma “kötülüğü” seçmez; tanımlanan hedefi şaşırtıcı derecede iyi optimize eder.

Aşağıdaki küçük simülasyon, sansasyon stratejisinin yayılmasını gösterir:

```python
uretici_sayisi = 100
sansasyon_orani = 0.10

for tur in range(8):
    kaliteli_getiri = 6 - (sansasyon_orani * 3)
    sansasyon_getiri = 8 - (sansasyon_orani * 2)

    if sansasyon_getiri > kaliteli_getiri:
        sansasyon_orani = min(1, sansasyon_orani + 0.12)

    print(tur, round(sansasyon_orani, 2))
```

Kod, üreticilerin yüksek getirili davranışı taklit ettiğini varsayar. Gerçek platformlar elbette daha karmaşıktır; yine de ödül yapısı değişmedikçe iyi niyetin tek başına dengeyi düzeltemeyeceğini anlatır.

## Oyunun Kuralları Değişebilir mi?

Çözüm, kullanıcılara yalnızca “telefonu bırak” demek değildir. Kronolojik akış, paylaşım öncesi bekleme, günlük kullanım sınırları ve kaliteli içeriğe ağırlık veren ölçütler kazanç matrisini değiştirebilir. Platformların başarıyı yalnızca dakika ve tıklamayla değil, kullanıcı memnuniyetiyle ölçmesi gerekir.

Dikkat ekonomisinin temel numarası şudur: Ürün ücretsiz görünür, çünkü ödeme para yerine dikkatle yapılır. Oyun teorisi de sorunun kötü oyunculardan çok, kötü tasarlanmış teşviklerde olduğunu gösterir. Masadaki herkes daha hızlı oynamaya zorlanırken kasa, her turdan payını almaya devam eder.
