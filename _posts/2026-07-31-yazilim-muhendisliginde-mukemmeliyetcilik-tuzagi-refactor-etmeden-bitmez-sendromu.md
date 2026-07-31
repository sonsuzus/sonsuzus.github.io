---
layout: post
title: "Yazılım Mühendisliğinde Mükemmeliyetçilik Tuzağı: “Refactor Etmeden Bitmez” Sendromu"
math: true
categories: 
  - Bilgi
tags: 
  - yazılım mühendisliği
  - mükemmeliyetçilik
  - refactoring
---

Bir özellik testlerden geçiyor, gereksinimleri karşılıyor ve kullanıcıya değer sunuyor. Yine de içimizdeki küçük yazılım mimarı fısıldıyor: “Şu sınıfı da bölelim, isimleri düzeltelim, hatta altyapıyı baştan yazalım.” Böylece iki saatlik görev, üç günlük mimari yolculuğa dönüşüyor. Refactoring yararlı bir pratik olsa da kusursuzluk arayışının bahanesine dönüştüğünde teslim tarihlerini, ekip güvenini ve geliştiricinin psikolojik dayanıklılığını tehdit edebilir.
``
## Refactoring ne zaman tuzağa dönüşür?

Refactoring, yazılımın dış davranışını değiştirmeden iç yapısını iyileştirmektir. Amaç okunabilirliği, bakım kolaylığını ve değiştirilebilirliği artırmaktır. Sorun refactoring yapmak değil, “yeterince iyi” noktasını tanımlayamamaktır.

Mükemmeliyetçi geliştirici çoğu zaman kod kalitesi peşinde olduğunu düşünür. Psikolojik açıdan ise davranışın arkasında hata yapma korkusu, eleştirilmekten kaçınma veya kontrol ihtiyacı bulunabilir. Kod henüz teslim edilmediyse gerçek kullanıcı tarafından değerlendirilemez; dolayısıyla geliştirici de başarısızlıkla yüzleşmez. Bitirmemek, paradoksal biçimde güvenli hissettirebilir.

Bu döngüyü basitçe şöyle gösterebiliriz:

$$Kaygı → Daha\ fazla\ düzenleme → Geçici\ rahatlama → Gecikme → Daha\ fazla\ kaygı$$

Her düzenleme kısa süreli rahatlama sağlar. Ancak teslim tarihi yaklaştıkça baskı büyür ve geliştirici, kontrol hissini geri kazanmak için yeniden koda yönelir.

## Kalite ile kusursuzluk aynı şey değildir

| Sağlıklı kalite yaklaşımı | Mükemmeliyetçilik tuzağı |
|---|---|
| Kullanıcı değerini ölçer | Estetik kusurlara takılır |
| Net bir bitiş ölçütü vardır | Sürekli yeni kusur bulur |
| Teknik borcu bilinçli yönetir | Her borcu hemen kapatmaya çalışır |
| Geri bildirimi erken alır | Eleştiriden kaçınmak için teslimi erteler |
| Küçük ve güvenli değişiklikler yapar | Büyük yeniden yazımlara yönelir |

Ekonomik açıdan da her iyileştirme mantıklı değildir. Bir refactoring kararının yaklaşık değeri şu şekilde düşünülebilir:

$$Net\ Değer = Beklenen\ Gelecek\ Kazancı - Refactoring\ Maliyeti - Gecikme\ Maliyeti$$

Kodun altı ay boyunca değişmeyecek bir bölümünü üç gün boyunca güzelleştirmek, düşük getiri sağlayabilir. Buna karşılık her sprint değiştirilen karmaşık bir modülü sadeleştirmek oldukça değerlidir. Kalite bağlama bağlıdır; soyut bir saflık yarışması değildir.

## “Bitti” tanımını koddan önce yazın

Mükemmeliyetçiliğe karşı en etkili araçlardan biri Definition of Done kullanmaktır. Göreve başlamadan önce test, güvenlik, performans ve dokümantasyon beklentileri açıkça belirlenmelidir. Sonradan akla gelen her iyileştirme mevcut görevin zorunlu parçası sayılmamalıdır.

Aşağıdaki küçük JavaScript örneği, refactoring kararını duygudan çıkarıp ölçütlere bağlayan basit bir kontrol sunar:

```javascript
function refactorGerekliMi({ testlerGeciyor, kritikRisk, sikDegisiyor }) {
  if (!testlerGeciyor) return true;       // Önce doğruluğu sağla
  if (kritikRisk) return true;             // Güvenlik veya veri riski beklemez
  if (sikDegisiyor) return true;           // Gelecekteki bakım maliyetini azalt
  return false;                            // İyileştirmeyi backlog'a taşı
}
```

Bu fonksiyon evrensel bir kalite formülü değildir. Asıl amacı “Kod hoşuma gitmedi” hissini; risk, değişim sıklığı ve doğruluk gibi tartışılabilir ölçütlere çevirmektir.

## Zihinsel fren mekanizmaları

Öncelikle refactoring için zaman kutusu belirleyin: “Bu alanı 45 dakika iyileştireceğim, sonra pull request açacağım.” İkinci olarak kusurları saklamak yerine backlog’a yazın. Böylece zihniniz, problemin unutulmayacağını bilir. Üçüncü olarak küçük pull request’ler açarak geri bildirimi erken alın. Son olarak ekip içinde “yeterince iyi” örneklerini konuşun; kalite standardı bireysel kaygının değil, ortak kararların ürünü olsun.

Profesyonellik kusursuz kod üretmek değil, doğru zamanda doğru kalite seviyesini seçebilmektir. Bazen en iyi refactoring, bugün yapılmayan ama gerekçesi belgelenen refactoring’dir. Yazılım kullanıcıya ulaşmadıkça yalnızca potansiyeldir; teslim edilen, ölçülen ve gerektiğinde geliştirilen yazılım ise gerçek değer üretir.
