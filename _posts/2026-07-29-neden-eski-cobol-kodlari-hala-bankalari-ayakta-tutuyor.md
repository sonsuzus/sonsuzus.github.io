---
layout: post
title: "Neden Eski COBOL Kodları Hâlâ Bankaları Ayakta Tutuyor?"
math: true
categories: 
  - Bilgi
tags: 
  - COBOL
  - miras sistemler
  - bankacılık teknolojileri
---

Bir banka kartıyla kahve aldığınızda, işleminizin arkasında sizden, baristadan ve muhtemelen kahve makinesinden daha yaşlı bir kod çalışıyor olabilir. 1959’da geliştirilen COBOL, modern görünmemesine rağmen hesap bakiyelerinden maaş ödemelerine kadar kritik finansal süreçleri yönetmeye devam ediyor. Bu durum yalnızca teknik bir nostalji değil; toplumun görünmez biçimde eski yazılımlara bağlandığını gösteren devasa bir mühendislik hikâyesidir.

``

## COBOL neden bu kadar uzun yaşadı?

COBOL, **Common Business-Oriented Language** ifadesinin kısaltmasıdır. Dil; ticari kayıtların işlenmesi, rapor üretimi ve yüksek hacimli finansal işlemler için tasarlandı. Sözdizimi bugünün dillerine göre uzun görünür, fakat okunabilirliği dönemine göre önemli bir avantajdı.

Basitleştirilmiş bir işlem mantığı şöyle yazılabilir:

```cobol
IF ACCOUNT-BALANCE >= PAYMENT-AMOUNT
    SUBTRACT PAYMENT-AMOUNT FROM ACCOUNT-BALANCE
    MOVE "APPROVED" TO TRANSACTION-STATUS
ELSE
    MOVE "DECLINED" TO TRANSACTION-STATUS
END-IF.
```

Bu kod, bakiye yeterliyse ödeme tutarını hesaptan düşer ve işlemi onaylar. Gerçek bankacılık sistemleri elbette çok daha karmaşıktır; eşzamanlı işlemler, günlük kayıtları, güvenlik kontrolleri ve geri alma mekanizmaları içerir. Yine de temel fikir aynıdır: Veriyi doğru, tutarlı ve hızlı biçimde işlemek.

COBOL sistemlerinin önemli bölümü **mainframe** adı verilen yüksek güvenilirlikli bilgisayarlarda çalışır. Bu makineler saniyede binlerce işlemi yönetebilir ve yıllarca kesintisiz hizmet verebilir. Başka bir deyişle mesele yalnızca eski kod değildir; kod, donanım, veri biçimleri ve operasyon ekipleri birlikte çalışan bir ekosistemdir.

| Özellik | COBOL ve mainframe | Modern bulut uygulaması |
|---|---|---|
| Temel öncelik | İşlem tutarlılığı | Esneklik ve hızlı geliştirme |
| Ölçekleme | Güçlü merkezi sistem | Dağıtık kaynaklar |
| Değişiklik riski | Genellikle yüksek | Mimariye göre değişken |
| Uzman erişimi | Giderek azalıyor | Görece daha yaygın |
| Kanıtlanmış çalışma süresi | On yıllar | Çoğunlukla daha kısa |

## Çalışıyorsa neden değiştirmiyoruz?

Bir bankanın çekirdek sistemini yenilemek, telefon uygulamasını güncellemeye benzemez. Milyonlarca müşterinin bakiyesi, kredi planı, faiz hesabı ve geçmiş işlemi yeni sisteme eksiksiz taşınmalıdır. Küçük bir yuvarlama farkı bile büyük ölçekte ciddi sonuçlar doğurabilir.

Örneğin $N$ hesapta oluşan ortalama hata $e$ ise toplam parasal sapma kabaca

$$E = N \times e$$

şeklinde düşünülebilir. On milyon hesapta yalnızca $0{,}01$ TL hata oluşması, toplamda $100.000$ TL tutarsızlık demektir. Üstelik finansal sistemlerde sorun sadece para değildir; denetim kayıtları ve hukuki yükümlülükler de korunmalıdır.

Risk basitçe şu bileşenlerle modellenebilir:

$$R = P(\text{arıza}) \times \text{etki}$$

Eski sistemlerde arıza olasılığı bakım zorlukları nedeniyle artabilir. Ancak plansız bir dönüşümün etkisi de çok büyük olduğundan bankalar çoğu zaman “kontrollü yaşlandırma” yaklaşımını seçer.

## Asıl kırılganlık koddan ibaret değil

COBOL kodunun eski olması otomatik olarak kötü olduğu anlamına gelmez. Asıl tehlike, sistemi anlayan uzmanların emekli olması ve kurumsal bilginin belgelenmemesidir. Bazı kurallar yalnızca kodun içinde saklıdır: otuz yıl önce eklenmiş bir vergi istisnası, artık kimsenin hatırlamadığı bir ürün veya gece yarısı çalışan özel bir mutabakat süreci gibi.

Bu bağımlılık toplumsaldır. Bankalar durduğunda maaşlar yatmaz, kartlar çalışmaz, işletmeler ödeme alamaz ve kamu transferleri aksar. Dolayısıyla COBOL bakımı özel bir şirketin teknik borcu olmaktan çıkarak ekonomik altyapı meselesine dönüşür.

## Çözüm: Bir gecede yeniden yazmak değil

En güvenli yaklaşım genellikle kademeli modernizasyondur. Önce test kapsamı artırılır, sistem davranışları belgelenir ve COBOL uygulamasının önüne API katmanları eklenir. Ardından düşük riskli işlevler parça parça yeni platformlara taşınır. Eski ve yeni sistem bir süre paralel çalıştırılarak sonuçları karşılaştırılır.

COBOL bugün bankaları ayakta tutuyor çünkü başarısız değil, aksine fazlasıyla başarılı oldu. Fakat bu başarı sonsuz güvence sağlamıyor. Geleceğin görevi eski kodla alay etmek değil; onun taşıdığı bilgiyi kaybetmeden, toplumu sarsmadan ve dijital ekonominin fişini çekmeden dönüşümü gerçekleştirmektir.
