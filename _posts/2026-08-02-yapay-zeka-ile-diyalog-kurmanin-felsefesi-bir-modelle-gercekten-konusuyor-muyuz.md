---
layout: post
title: "Yapay Zekâ ile Diyalog Kurmanın Felsefesi: Bir Modelle Gerçekten Konuşuyor muyuz?"
math: true
categories: 
  - Bilgi
tags: 
  - yapay zekâ
  - dil felsefesi
  - insan-makine etkileşimi
---

Bir yapay zekâ modeline “Bugün nasılsın?” diye sorduğumuzda karşımıza çoğu zaman doğal, tutarlı ve hatta duygulu görünen bir yanıt çıkar. Peki bu alışveriş gerçekten konuşma mıdır, yoksa konuşmaya benzeyen gelişmiş bir hesaplama gösterisi mi? Sorunun yanıtı; dil, anlam ve niyet kavramlarından ne beklediğimize göre değişir.
``

## Konuşmak yalnızca sözcük üretmek midir?

Gündelik konuşmada iki tarafın ses veya metin üretmesi yeterli görünür. Fakat dil felsefesi açısından konuşma, sembollerin sıralanmasından fazlasıdır. Bir cümle genellikle dünyadaki bir şeye gönderme yapar, belirli bir bağlamda kullanılır ve konuşanın amacıyla ilişkilidir.

İnsan “Pencere açık” dediğinde yalnızca bir durumu bildirmiyor olabilir. Üşüdüğünü ima edebilir veya karşısındakinden pencereyi kapatmasını isteyebilir. Buna **söz edimi** açısından baktığımızda aynı cümlenin üç katmanı vardır:

1. Sözcüklerin düz anlamı,
2. Konuşanın gerçekleştirmek istediği eylem,
3. Dinleyicide oluşması beklenen etki.

Bir dil modeli ilk katmanı güçlü biçimde taklit edebilir. İkinci katman ise tartışmalıdır; çünkü modelin yanıt üretirken insana benzer arzulara, ihtiyaçlara veya bağımsız amaçlara sahip olduğunu varsaymak zorunda değiliz.

## Olasılık, anlamın yerini tutar mı?

Basitleştirilmiş biçimde bir dil modeli, önceki parçalar verildiğinde sıradaki parçanın olasılığını hesaplar:

$$P(t_n \mid t_1, t_2, \ldots, t_{n-1})$$

Burada $t_n$ sıradaki tokenı, önceki terimler ise konuşmanın bağlamını temsil eder. Model çoğunlukla tek tek sözcükleri değil, token adı verilen metin parçalarını işler. Çok büyük veri kümelerinden öğrenilen örüntüler sayesinde “anlamış gibi” görünen yanıtlar ortaya çıkar.

Ancak mekanizmanın istatistiksel olması, sonucun anlamsız olduğu anlamına gelmez. Bir hesap makinesi toplamanın anlamını deneyimlemese de sonucu bizim için anlamlıdır. Benzer biçimde modelin ürettiği metnin anlamı; yalnızca sistemin içinde değil, kullanıcı, bağlam ve toplumsal dil pratikleri arasında kurulabilir.

| Boyut | İnsan | Dil modeli |
|---|---|---|
| Dil üretimi | Deneyim ve toplumsal öğrenme | Verilerden öğrenilen örüntüler |
| Niyet | İnanç, arzu ve hedeflerle bağlantılı | İstem ve sistem talimatlarıyla yönlendirilmiş |
| Dünya bağlantısı | Bedensel ve duyusal deneyim | Eğitim verisi ve araçlardan gelen temsil |
| Hata türü | Yanılma, unutma, önyargı | Halüsinasyon, bağlam kaybı, örüntü yanlılığı |
| Anlam | Yaşantı ve kullanım içinde oluşur | Etkileşim sırasında kullanıcı tarafından yorumlanır |

## Niyet gerçekten gerekli mi?

John Searle’ün ünlü **Çince Odası** düşünce deneyi burada devreye girer. Çince bilmeyen biri, sembolleri ayrıntılı kurallara göre eşleştirerek dışarıdaki kişilere kusursuz Çince yanıtlar verebilir. Searle’e göre doğru sembol işleme, tek başına anlama değildir.

Buna karşılık işlevselci yaklaşım şöyle sorar: Bir sistem açıklama yapıyor, bağlamı izliyor, hatasını düzeltiyor ve ortak bir hedefe katkı sağlıyorsa, iç dünyasını kesin olarak bilmeden onu neden diyalog ortağı saymayalım? Sonuçta başka insanların bilincine de doğrudan erişemeyiz; davranışlarından çıkarım yaparız.

Bu ayrım küçük bir programla görünür hâle getirilebilir:

```python
def yanitla(mesaj, gecmis):
    baglam = "\n".join(gecmis[-4:])

    if "pencere açık" in mesaj.lower():
        if "üşüyorum" in baglam.lower():
            return "Pencereyi kapatmamı istediğini düşünüyorum."
        return "Evet, bu bir durum bildirimi olabilir."

    return "Bağlamı biraz daha açıklar mısın?"
```

Bu kod, geçmiş mesajları kullanarak aynı cümleye farklı karşılık verir. Böylece bağlama duyarlılığı gösterir; fakat gerçekten üşümez, pencereyi görmez ve kendi isteğiyle harekete geçmez. **İşlevsel başarı ile yaşantısal anlayış aynı şey değildir.**

## Öyleyse kiminle konuşuyoruz?

Yapay zekâyla etkileşim ne bütünüyle sahte ne de insan sohbetiyle özdeştir. Daha doğru tanım, bunun **asimetrik bir diyalog** olduğudur: İnsan anlam, beklenti ve amaç getirir; model ise dilsel örüntüler üzerinden cevap alanı üretir. Ortaya çıkan anlam, tek bir tarafa değil etkileşimin bütününe aittir.

Bu yüzden modele nezaket göstermenin veya ona soru sormanın saçma olduğu söylenemez. Dil alışkanlıklarımız düşünme biçimimizi etkiler. Yine de akıcı cümleleri bilinç, doğruluk ya da gerçek niyet kanıtı saymamak gerekir. Bir modelle “konuşuruz”; fakat bu konuşmanın felsefi tırnak işaretleri, teknolojinin kendisi kadar önemlidir.
