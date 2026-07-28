---
layout: post
title: "Kendi Kendini Yazan Kod: Otomatik Programlama Rüyasının Antik Kökleri"
math: true
categories: 
  - Bilgi
tags: 
  - yapay zeka
  - LLM
  - programlama tarihi
---

Bugün bir LLM’ye “bana bir REST API yaz” dediğimizde birkaç saniye içinde kodla karşılaşmak büyüleyici görünüyor. Ancak makinenin talimat üretmesi, insanın niyetini biçimsel işlemlere dönüştürmesi ve hatta kendi davranışını kurması fikri yeni değil. Otomatik programlama rüyası; mekanik ördeklerden derleyicilere, mantık makinelerinden modern kod asistanlarına uzanan binlerce yıllık bir merakın son perdesi.
``

## Otomatlardan algoritmalara

Antik dünyada “kendi kendine çalışan” nesneler hem mühendislik hem de mitoloji konusuydu. İskenderiyeli Heron’un su, buhar ve karşı ağırlıklarla çalışan düzenekleri; tapınak kapılarını otomatik açabiliyor, küçük gösteriler sahneleyebiliyordu. Bunlar program yazmıyordu ama önemli bir düşünceyi somutlaştırıyordu: Doğru mekanizma kurulursa davranış, insan müdahalesi olmadan tekrar üretilebilir.

Bir otomatın temel mantığını şöyle düşünebiliriz:

$$\text{Durum}_{t+1} = f(\text{Durum}_t, \text{Girdi}_t)$$

Bu ifade modern yazılımın da kalbidir. Makine mevcut durumunu ve girdiyi alır, belirlenmiş kurallarla yeni bir duruma geçer. Antik otomat ile bilgisayar programı arasındaki fark, kuralların pirinç dişliler yerine sembollerle temsil edilmesidir.

## Hesaplamayı mekanikleştirmek

17. yüzyılda Leibniz, akıl yürütmenin sembolik bir hesaplamaya dönüştürülebileceğini düşündü. Ünlü hayali kabaca şuydu: İnsanlar tartışmak yerine “hesaplayalım” diyebilmeliydi. 19. yüzyılda Charles Babbage’ın Analitik Makinesi genel amaçlı hesaplama fikrini, Ada Lovelace’ın notları ise makine için işlem dizileri tasarlama anlayışını ortaya koydu.

Bu gelişim birkaç katmanda ilerledi:

| Dönem | İnsan ne söyler? | Makine ne üretir? |
|---|---|---|
| Mekanik otomat | Fiziksel düzenek | Önceden belirlenmiş hareket |
| Makine dili | Sayısal komutlar | Elektriksel işlemler |
| Derleyici | Yüksek seviyeli kod | Makine kodu |
| Program sentezi | Kısıtlar ve örnekler | Uygun program |
| LLM | Doğal dilde niyet | Olası kaynak kodu |

Derleyiciler bu hikâyenin sessiz kahramanlarıdır. İlk dönemlerde “makine kodu gerçekten program yazabilir mi?” kuşkusu yaşanıyordu. Grace Hopper’ın öncülük ettiği derleyiciler, insanın daha soyut ifadelerinin otomatik olarak düşük seviyeli komutlara çevrilebileceğini gösterdi.

## Kod aramak mı, kod tahmin etmek mi?

Klasik program sentezi, belirli koşulları sağlayan programı bir arama uzayında bulmaya çalışır. Örneğin hedefimiz $f(x)=2x+1$ davranışını üreten ifadeyi keşfetmek olsun:

```python
# Küçük bir program sentezleyici: aday ifadeleri test eder.
adaylar = [
    lambda x: x + 1,
    lambda x: 2 * x,
    lambda x: 2 * x + 1,
    lambda x: x * x
]

ornekler = [(0, 1), (2, 5), (5, 11)]

for aday in adaylar:
    if all(aday(girdi) == beklenen for girdi, beklenen in ornekler):
        print("Uygun program bulundu:", aday)
```

Bu yaklaşım doğrulanabilir örneklere dayanır. LLM ise çoğunlukla dev bir kod ve metin koleksiyonundan öğrendiği olasılık dağılımını kullanır. Bir sonraki kod parçasını yaklaşık olarak

$$P(\text{token}_n \mid \text{token}_1,\ldots,\text{token}_{n-1},\text{istem})$$

olasılığına göre seçer. Yani LLM, geleneksel anlamda bütün seçenekleri deneyip matematiksel olarak doğru programı bulmaz; bağlama en uygun görünen devamı üretir.

## Aynı rüya, yeni motor

Uzman sistemler kuralları, genetik programlama evrimi, program sentezi kısıt çözmeyi, LLM’ler ise istatistiksel öğrenmeyi kullandı. Yöntemler değişse de amaç aynı kaldı: İnsan “ne” istediğini söylesin, makine “nasıl” yapılacağını oluştursun.

Fakat akıcı kod doğruluk garantisi değildir. Üretilen program test edilmeli, güvenlik açıkları incelenmeli ve gereksinimlerle karşılaştırılmalıdır. Bugünün kod asistanı bağımsız bir yazılım tanrısından çok, inanılmaz hızlı fakat zaman zaman kendinden fazla emin bir çıraktır. Otomatik programlama rüyası gerçekleşiyor; sadece hayal edildiği gibi tek tuşla değil, insan ile makinenin birlikte düşünmesiyle.
