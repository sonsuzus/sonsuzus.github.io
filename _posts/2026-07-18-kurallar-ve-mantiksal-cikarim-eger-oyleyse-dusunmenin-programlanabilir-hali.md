---
layout: post
title: "Kurallar ve Mantıksal Çıkarım: Eğer-Öyleyse Düşünmenin Programlanabilir Hali"
math: true
categories: 
  - Bilgi
tags: 
  - mantıksal çıkarım
  - kural tabanlı sistemler
  - yapay zeka
---

Bilgisayara akıl yürütmeyi öğretmek ilk bakışta bilim kurgu gibi durabilir; ama işin temelinde oldukça tanıdık bir yapı vardır: eğer bir koşul doğruysa, o koşuldan yeni bir sonuç çıkar. Kurallar ve mantıksal çıkarım, önceden tanımlanmış gerçekleri referans alarak yeni bilgiler üretmemizi sağlar. Yani sistem, elindeki bilgi kartlarını karıştırır, eşleşenleri bulur ve mantıklı yeni kartlar üretir.
``
Günlük hayatta bunu sürekli yaparız. Eğer gökyüzü kapalıysa ve hava serinse, yağmur yağabilir diye düşünürüz. Eğer yağmur yağıyorsa, zeminin ıslak olacağını tahmin ederiz. Kural tabanlı sistemlerde bu düşünce biçimi daha resmi hale getirilir. Bir kural genellikle şu biçimdedir:

$A \rightarrow B$

Burada $A$ koşul, $B$ ise sonuçtur. Anlamı şudur: Eğer $A$ doğruysa, $B$ de doğru kabul edilebilir. Daha karmaşık kurallarda birden fazla koşul bulunabilir:

$$A \land B \rightarrow C$$

Bu ifade, hem $A$ hem de $B$ doğruysa $C$ sonucuna ulaşılır demektir. Buradaki $\land$ sembolü mantıksal ve anlamına gelir.

| Kavram | Anlamı | Örnek |
|---|---|---|
| Gerçek | Sistemin doğru bildiği bilgi | hava_yağmurlu |
| Kural | Koşul-sonuç ilişkisi | hava_yağmurlu ise zemin_ıslak |
| Çıkarım | Yeni bilgi üretme süreci | zemin_ıslak sonucuna varmak |
| Bilgi tabanı | Gerçekler ve kurallar bütünü | tüm kurallar listesi |

Mantıksal çıkarımın iki popüler yöntemi vardır: ileri zincirleme ve geri zincirleme. İleri zincirleme, eldeki gerçeklerden başlayıp mümkün olan tüm sonuçları üretmeye çalışır. Geri zincirleme ise hedef bir sonucun doğru olup olmadığını kanıtlamaya çalışır. Dedektif benzetmesiyle düşünürsek, ileri zincirleme olay yerindeki tüm ipuçlarını inceleyip sonuçlara gider; geri zincirleme ise önce şüpheliyi seçer, sonra kanıt arar.

| Yöntem | Başlangıç Noktası | Kullanım Alanı | Mantık |
|---|---|---|---|
| İleri zincirleme | Mevcut gerçekler | Simülasyon, uzman sistem | Bildiklerimden ne çıkar? |
| Geri zincirleme | Hedef sonuç | Tanı sistemleri, sorgulama | Bu sonucu kanıtlayabilir miyim? |

Basit bir ileri zincirleme motoru Python ile şöyle modellenebilir:

```python
facts = {'hava_yagmurlu', 'bulutlu'}

rules = [
    ({'hava_yagmurlu'}, 'zemin_islak'),
    ({'zemin_islak'}, 'kayma_riski'),
    ({'bulutlu', 'hava_yagmurlu'}, 'semsiye_gerekli')
]

def forward_chain(facts, rules):
    changed = True
    while changed:
        changed = False
        for conditions, result in rules:
            if conditions.issubset(facts) and result not in facts:
                facts.add(result)
                changed = True
                print('Yeni sonuc:', result)
    return facts

final_facts = forward_chain(facts, rules)
print(final_facts)
```

Bu kodda `facts` başlangıçta doğru kabul edilen bilgileri tutar. `rules` listesinde ise her kuralın koşulları ve sonucu vardır. `issubset` kontrolü, kuralın tüm koşullarının mevcut gerçekler içinde olup olmadığını denetler. Eğer koşullar sağlanıyorsa sonuç bilgi tabanına eklenir. Döngü, artık yeni bilgi üretilemeyene kadar devam eder.

Bu yaklaşımın en güzel tarafı açıklanabilir olmasıdır. Bir sinir ağı bazen neden öyle karar verdiğini anlatmakta zorlanırken, kural tabanlı sistemlerde karar zinciri izlenebilir: Yağmur yağdı, bu yüzden zemin ıslandı; zemin ıslandı, bu yüzden kayma riski oluştu. Gayet dedikoducu ama şeffaf bir sistem!

Elbette kuralların da sınırları vardır. Çok fazla kural olduğunda çakışmalar ortaya çıkabilir. Örneğin bir kural klima aç derken başka bir kural pencere aç diyebilir. Bu durumda önceliklendirme, ağırlıklandırma veya çatışma çözme stratejileri gerekir. Bazen kurallara güven derecesi de eklenir. Mesela $P(yağmur)=0.8$ gibi olasılıksal ifadelerle sistem daha esnek hale getirilebilir.

Sonuç olarak kurallar ve mantıksal çıkarım, yapay zekanın en anlaşılır yapı taşlarından biridir. Veriyi ezberlemek yerine, bilgiden bilgi üretmeyi sağlar. Küçük bir eğer-öyleyse cümlesi, doğru bağlandığında koca bir karar mekanizmasına dönüşebilir. Yazılım dünyasında bu yapı; uzman sistemlerden oyun yapay zekasına, iş kurallarından otomasyon senaryolarına kadar birçok yerde sessizce çalışır.
