---
layout: post
title: "Otomasyonun İşgücü Üzerindeki Sosyolojisi: Hangi Meslekler Gerçekten Risk Altında?"
math: true
categories: 
  - Bilgi
tags: 
  - otomasyon
  - işgücü
  - yapay zeka
---

Bir robotun kahve hazırlaması, yapay zekânın sözleşme özetlemesi veya yazılımın faturaları işlemesi aynı soruyu gündeme getiriyor: “Mesleğim elimden gidecek mi?” Ancak otomasyon, meslekleri tek hamlede yok eden teknolojik bir kötü karakter değildir. Tarih, çoğunlukla mesleklerin değil, mesleklerin içindeki belirli görevlerin otomatikleştiğini; işgücü piyasasının da sınıf, eğitim, gelir ve pazarlık gücü eksenlerinde yeniden şekillendiğini gösteriyor.

``

## Otomasyonun Eski Bir Hikâyesi Var

18. yüzyılın mekanik dokuma tezgâhları zanaatkârların üretim üzerindeki kontrolünü azalttı. 20. yüzyılın montaj hatları üretimi küçük ve tekrarlanabilir adımlara böldü. 1980’lerden itibaren bilgisayarlar büro işlerini dönüştürürken internet bazı aracı meslekleri zayıflattı, yepyeni uzmanlıklar doğurdu. Günümüzde üretken yapay zekâ ise yalnızca fiziksel veya rutin görevleri değil, metin yazma, analiz ve görsel üretme gibi bilişsel işleri de etkiliyor.

| Otomasyon dalgası | Temel teknoloji | En çok etkilenen işler | Ortaya çıkan ihtiyaçlar |
|---|---|---|---|
| Sanayi Devrimi | Buhar gücü, makineler | Dokumacılık, el üretimi | Makine operatörlüğü, bakım |
| Fordist dönem | Montaj hattı | Zanaata dayalı üretim | Teknisyenlik, kalite kontrol |
| Dijitalleşme | Bilgisayar, internet | Sekreterlik, veri girişi | Yazılım, ağ yönetimi |
| Yapay zekâ dönemi | Makine öğrenmesi | İçerik, analiz, destek görevleri | Veri denetimi, AI yönetişimi |

Bu karşılaştırma önemli bir gerçeği ortaya çıkarır: Teknoloji iş miktarını azaltabileceği gibi üretimi ucuzlatıp talebi büyüterek yeni iş de yaratabilir. Sonucu teknoloji tek başına değil; şirket stratejileri, sendikalar, eğitim sistemi ve kamu politikaları belirler.

## Meslek Değil, Görev Riskine Bakmak

Bir mesleğin otomasyon riskini değerlendirirken onu görevlerine ayırmak gerekir. Örneğin muhasebecilik; veri girişi, mevzuat yorumlama, müşteri iletişimi ve stratejik danışmanlık içerir. Yazılım ilk görevi kolayca üstlenebilirken belirsiz mevzuatı yorumlamak veya güven ilişkisi kurmak daha zordur.

Basitleştirilmiş bir risk modeli şöyle kurulabilir:

$$R = 0.35T + 0.25D + 0.20P - 0.20S$$

Burada $T$ tekrarlanabilirliği, $D$ görevin dijital veriyle yapılabilmesini, $P$ öngörülebilirliği ve $S$ sosyal etkileşim gereksinimini temsil eder. Değerler 0 ile 1 arasındadır. Bu denklem bilimsel bir kehanet değil, düşünmeyi düzenleyen bir araçtır.

```python
def otomasyon_riski(tekrar, dijitallik, ongorulebilirlik, sosyal_beceri):
    puan = (0.35 * tekrar +
            0.25 * dijitallik +
            0.20 * ongorulebilirlik -
            0.20 * sosyal_beceri)
    return round(max(0, min(1, puan)), 2)

print(otomasyon_riski(0.9, 0.9, 0.8, 0.2))  # Örnek: veri girişi
print(otomasyon_riski(0.3, 0.4, 0.2, 0.9))  # Örnek: psikolojik danışmanlık
```

Bu kod, görev özelliklerini ağırlıklandırarak karşılaştırmalı bir puan üretir. Gerçek araştırmalarda ücret, regülasyon, teknoloji maliyeti ve hata toleransı gibi değişkenler de modele eklenmelidir.

## Kimler Gerçekten Risk Altında?

| Daha yüksek risk | Daha düşük risk |
|---|---|
| Veri girişi ve standart raporlama | Bakım ve onarım |
| Basit müşteri destek talepleri | Sağlık ve bakım hizmetleri |
| Tekrarlı üretim ve depo görevleri | Müzakere ve liderlik |
| Şablon içerik üretimi | Belirsiz ortamlarda saha çalışması |

Yüksek risk, mutlaka işsizlik anlamına gelmez. İşverenler çalışan sayısını azaltabilir, aynı çalışanlardan daha fazla çıktı bekleyebilir veya işi “algoritmik yönetime” bağlayabilir. Böylece otomasyonun sosyolojik etkisi yalnızca iş kaybı değil; çalışma temposunun artması, becerilerin değersizleşmesi ve denetimin yoğunlaşması olabilir.

## Asıl Ayrım Teknolojiye Erişimde

Yeni dönemin kazananları sadece kod yazanlar olmayacak. Alan bilgisiyle teknolojiyi birleştiren, çıktıları doğrulayan, etik riskleri değerlendiren ve insanlarla güven kurabilen çalışanlar avantaj sağlayacak. Buna karşılık yeniden eğitim fırsatına erişemeyenler dönüşüm maliyetini daha ağır taşıyacak.

Dolayısıyla doğru soru “Robotlar işlerimizi alacak mı?” değil, “Verimlilik kazancını kim paylaşacak?” sorusudur. Çalışma süresinin kısaltılması, yaşam boyu eğitim, güçlü sosyal güvenlik ve çalışanların teknoloji kararlarına katılması sağlanırsa otomasyon toplumsal refah üretebilir. Aksi durumda son derece akıllı makineler, oldukça eski eşitsizlikleri büyütebilir.
