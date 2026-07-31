---
layout: post
title: "Merkeziyetsiz İnternetin Ütopyası: Web3 Gerçekte Kimin Elinde?"
math: true
categories: 
  - Bilgi
tags: 
  - Web3
  - merkeziyetsizlik
  - blokzincir
---

Web3; kullanıcıların verilerine, kimliklerine ve dijital varlıklarına sahip olduğu, aracıların yerini açık protokollerin aldığı bir internet vaat ediyor. Kulağa dijital bir ütopya gibi geliyor. Ancak cüzdan adreslerinin arkasındaki sermayeyi, doğrulayıcıları ve altyapı şirketlerini takip ettiğimizde rahatsız edici bir soruyla karşılaşıyoruz: Merkeziyetsiz internet gerçekten kullanıcıların mı, yoksa yalnızca yeni merkezlerin mi elinde?
``

## İdeal: Güvenmek Yerine Doğrulamak

Geleneksel internette kullanıcılar bir platformun kurallarına uyar. Hesabınız kapatılabilir, içeriğiniz silinebilir veya verileriniz satılabilir. Web3 yaklaşımında ise kurallar akıllı sözleşmelerle tanımlanır ve ağdaki birçok düğüm tarafından uygulanır.

Teorik olarak güven, tek bir kuruma değil dağıtık uzlaşmaya dayanır. Bir blokzincirde saldırganın sistemi değiştirebilmesi için yeterli doğrulama gücünü, token miktarını veya madencilik kapasitesini kontrol etmesi gerekir. Basitleştirilmiş biçimde saldırı maliyetini şöyle düşünebiliriz:

$$Saldırı\ Maliyeti = Kontrol\ Edilmesi\ Gereken\ Pay \times Ağın\ Toplam\ Ekonomik\ Değeri$$

Dağılım ne kadar dengeliyse sistemi ele geçirmek o kadar zorlaşır. Fakat düğüm sayısının fazla olması, gücün otomatik olarak eşit dağıldığı anlamına gelmez.

| İdeal Web3 | Pratikte Karşılaşılan Durum |
|---|---|
| Her kullanıcı kendi verisini kontrol eder | Kullanıcılar merkezi cüzdan ve borsalara bağımlı kalabilir |
| Kararlar topluluk tarafından alınır | Büyük token sahipleri oylamaları belirleyebilir |
| Uygulamalar sansüre dayanıklıdır | Arayüzler ve RPC servisleri engellenebilir |
| Ağ bağımsız düğümlerden oluşur | Düğümler aynı bulut sağlayıcılarda kümelenebilir |

## Token Demokrasisi mi, Dijital Plütokrasi mi?

DAO sistemlerinde sık kullanılan model, bir tokenın bir oy sayılmasıdır. Bu yöntem kolaydır; ancak demokratik değildir. Çok token sahibi olan yatırımcı, sıradan binlerce kullanıcıdan daha fazla söz hakkı kazanabilir. Böylece zincir üzerinde şeffaf olan yönetim, ekonomik açıdan yoğunlaşmış kalır.

Bu yoğunluğu ölçmek için Herfindahl–Hirschman Endeksi kullanılabilir:

$$HHI = \sum_{i=1}^{n} s_i^2$$

Buradaki $s_i$, her katılımcının toplam güç içindeki payıdır. Sonuç büyüdükçe güç daha az elde toplanmış demektir. Ayrıca **Nakamoto katsayısı**, sistemi bozmak için anlaşması gereken en az aktör sayısını gösterir. Binlerce doğrulayıcı bulunmasına rağmen üç büyük havuz çoğunluğu kontrol ediyorsa anlamlı sayı üçtür.

Aşağıdaki Python kodu token dağılımını inceleyerek HHI değerini ve yüzde 51'e ulaşan en küçük koalisyonu hesaplar:

```python
def guc_analizi(bakiyeler):
    toplam = sum(bakiyeler)
    paylar = sorted((b / toplam for b in bakiyeler), reverse=True)

    hhi = sum(pay ** 2 for pay in paylar)
    birikim = 0

    for aktor_sayisi, pay in enumerate(paylar, start=1):
        birikim += pay
        if birikim >= 0.51:
            return hhi, aktor_sayisi

bakiyeler = [420, 250, 140, 90, 60, 40]
hhi, koalisyon = guc_analizi(bakiyeler)
print(f'HHI: {hhi:.3f}, kritik koalisyon: {koalisyon}')
```

Kod, görünen katılımcı sayısına aldanmak yerine ekonomik kontrolü ölçer. Yine de bir kişinin birden fazla cüzdan kullanabilmesi veya farklı adreslerin aynı kuruma ait olması analizi zorlaştırır.

## Görünmeyen Merkezler

Merkeziyetsizlik yalnızca blokzincir katmanında değerlendirilmemelidir. Kullanıcının işlemini ağa taşıyan RPC sağlayıcısı, cüzdan uygulaması, alan adı servisi, stablecoin ihraççısı ve borsa hâlâ merkezi olabilir. Akıllı sözleşme durdurulamasa bile ona ulaşan web arayüzü kapatılabilir.

| Katman | Güç Yoğunlaşması Riski |
|---|---|
| Konsensüs | Büyük doğrulayıcılar ve staking havuzları |
| Altyapı | Bulut ve RPC sağlayıcıları |
| Finans | Stablecoin şirketleri ve merkezi borsalar |
| Yönetişim | Balinalar, delegeler ve düşük katılım |
| Kullanıcı deneyimi | Popüler cüzdanlar ve tekil web arayüzleri |

## Ütopyadan Kullanışlı Bir Gerçekliğe

Web3 bütünüyle merkeziyetsiz değildir; fakat bütünüyle sahte de değildir. Açık kaynak istemciler, kendi düğümünü çalıştırma imkânı ve izinsiz işlem yapabilme önemli kazanımlardır. Asıl hata, merkeziyetsizliği bir açma-kapama düğmesi gibi görmektir.

Daha sağlıklı sistemler için doğrulayıcı çeşitliliği, karesel oylama, zaman kilitli yönetişim, açık kaynak arayüzler ve alternatif RPC bağlantıları desteklenmelidir. Sonuçta mesele merkezin tamamen yok olması değil, gücün denetlenebilir, terk edilebilir ve rekabete açık olmasıdır. Web3'ün gerçek sahibi de logosu en büyük proje değil; protokolü gerektiğinde kimseye izin sormadan kullanabilen topluluktur.
