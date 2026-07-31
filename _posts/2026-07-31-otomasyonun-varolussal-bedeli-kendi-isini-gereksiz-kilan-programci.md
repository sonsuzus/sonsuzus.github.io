---
layout: post
title: "Otomasyonun Varoluşsal Bedeli: Kendi İşini Gereksiz Kılan Programcı"
math: true
categories: 
  - Bilgi
tags: 
  - otomasyon
  - yazılım felsefesi
  - yapay zeka
---

Bir programcı, üç saatlik işi üç saniyeye indiren bir betik yazdığında önce kahraman gibi hisseder. Ardından rahatsız edici bir soru belirir: “Bu işlem artık bana ihtiyaç duymuyorsa ben neden buradayım?” Otomasyon, yazılım dünyasının en büyük başarı ölçütlerinden biridir; fakat başarıya ulaştıkça onu üreten kişinin görünürlüğünü azaltır. Böylece programcı yalnızca görevleri değil, görevler üzerinden kurduğu mesleki kimliği de otomatikleştirmeye başlar.

``

## Paradoksun çekirdeği

Ekonomik açıdan otomasyonun amacı açıktır: Aynı çıktıyı daha az zaman, hata ve maliyetle üretmek. Bir görevin elle tamamlanma süresi $T_e$, otomatik çalışma süresi $T_o$, otomasyonu geliştirme maliyeti ise $G$ olsun. İşlem $n$ kez tekrarlanıyorsa otomasyon şu koşulda kazançlıdır:

$$G + nT_o < nT_e$$

Buradan başabaş noktası şöyle bulunur:

$$n > \frac{G}{T_e-T_o}$$

Ne var ki denklem, insanın işinden aldığı anlamı ölçmez. Programcının karar verme yetkisi, ustalık hissi ve ekip içindeki konumu bir hücreye kolayca yazılamaz. Otomasyonun teknik getirisi ölçülebilirken varoluşsal maliyeti çoğunlukla görünmez kalır.

| Bakış açısı | Otomasyonun vaadi | Varoluşsal riski |
|---|---|---|
| Şirket | Daha düşük maliyet | İnsanları yalnızca gider olarak görmek |
| Kullanıcı | Daha hızlı hizmet | Muhatap ve kontrol kaybı |
| Programcı | Tekrardan kurtulmak | Yetkinliğinin görünmezleşmesi |
| Toplum | Daha yüksek üretkenlik | Kazancın adaletsiz paylaşılması |

## Kod yazmak mı, kendini silmek mi?

Marx’ın yabancılaşma düşüncesinde çalışan, ürettiği şey üzerindeki kontrolünü kaybedebilir. Programcı için tuhaf olan, bu kontrol kaybını bizzat kodlamasıdır. Dün kendisinin yürüttüğü süreci bugün bir servis, yarın ise kimsenin nasıl çalıştığını tam hatırlamadığı bir sistem yönetir. Kod yaşamaya devam ederken yazarı organizasyon şemasından silinebilir.

Sartre’ın varoluşçuluğu ise insanın hazır bir özle doğmadığını, seçimleriyle kendini kurduğunu söyler. Bu açıdan “Ben rapor hazırlayan kişiyim” demek kırılgan bir kimliktir. Rapor otomatikleştiğinde öz de çöker. Daha dayanıklı tanım şudur: “Ben sorunları fark eden, sistem tasarlayan ve sonuçların sorumluluğunu alan kişiyim.” Görev ortadan kalkabilir; muhakeme bütünüyle ortadan kalkmak zorunda değildir.

Basit bir otomasyon örneği bile bu ayrımı gösterir:

```python
from pathlib import Path


def eski_loglari_temizle(klasor, sinir):
    dosyalar = sorted(
        Path(klasor).glob("*.log"),
        key=lambda dosya: dosya.stat().st_mtime
    )

    for dosya in dosyalar[:-sinir]:
        print(f"Siliniyor: {dosya.name}")
        dosya.unlink()


eski_loglari_temizle("logs", 10)
```

Bu kod eski günlük dosyalarını silerek rutin bakım işini devralır. Ancak hangi kayıtların hukuki veya operasyonel açıdan saklanması gerektiğine karar vermez. Programcı parmak hareketlerini makineye aktarırken bağlamı, sınırları ve sorumluluğu elinde tutar. En azından sistem bilinçli tasarlanmışsa durum budur.

## Asıl sorun otomasyon değil, paylaşım

Teknoloji tarihindeki temel çatışma “makine mi, insan mı?” değildir. Daha doğru soru, makinenin yarattığı zamanın kime ait olduğudur. Sekiz saatlik iş iki saate düşüyor ama çalışanın hedefi dört katına çıkıyorsa özgürleşme gerçekleşmez; yalnızca koşu bandı hızlanır. Kazanılan altı saat eğitim, yaratıcılık veya dinlenme için kullanılabiliyorsa otomasyon insani kapasiteyi genişletir.

Bu nedenle etik bir otomasyon sürecinde programcı üç soruyu sormalıdır:

1. Ortadan kaldırdığım görev mi, yoksa bir insanın pazarlık gücü mü?
2. Sistemin hatasında sorumluluk kimde kalacak?
3. Kazanılan zaman ve değer kimler arasında paylaşılacak?

## Programcı kendini nereye koymalı?

Programcının güvenli yeri belirli bir araç, dil veya görev değildir. Bugünün vazgeçilmez framework’ü yarının nostaljik blog yazısı olabilir. Daha sağlam konum; problemi tanımlamak, varsayımları sorgulamak, insan sonuçlarını görmek ve gerektiğinde otomasyona “hayır” diyebilmektir.

Kendi işini otomatikleştirmek bu yüzden mesleki intihar olmak zorunda değildir. Eski rolün bilinçli biçimde terk edilmesi ve daha yüksek sorumluluğa geçiş olabilir. Fakat kurum yalnızca verimlilik kazancını sahiplenip insanı dışarıda bırakıyorsa paradoks acımasızlaşır: Programcı geleceği inşa eder, fakat gelecekte kendisine sandalye ayrılmadığını görür. Mesele kodun bizi gereksiz kılması değil; gereksizliğin ekonomik ve ahlaki tanımını kimin yazdığıdır.
