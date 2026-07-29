---
layout: post
title: "Regex'in Karanlık Tarafı: Okunabilirlik ile Güç Arasındaki Ebedi Çatışma"
math: true
categories: 
  - Bilgi
tags: 
  - regex
  - okunabilirlik
  - yazılım geliştirme
---

Düzenli ifadeler, yani regex, programcının araç çantasındaki İsviçre çakısı gibidir: Metin arar, veriyi ayıklar, biçimi doğrular ve bazen tek satırda küçük bir mucize gerçekleştirir. Ne var ki bu mucizeyi altı ay sonra yeniden gören geliştirici, kendisini antik bir yazıtı çözmeye çalışırken bulabilir. Regex’in aynı anda hem sevilmesinin hem de nefret edilmesinin temelinde tam olarak bu çelişki vardır: Olağanüstü ifade gücü, kolayca okunabilirliğin düşmanına dönüşebilir.
``
## Regex neden bu kadar güçlü?

Teorik olarak düzenli ifadeler, **düzenli dilleri** tanımlamak için kullanılır. Klasik regex yapıları sonlu durum makineleriyle modellenebilir. Bir metin $n$ karakterden oluşuyorsa ve motor deterministik bir sonlu otomat gibi çalışıyorsa arama maliyeti çoğunlukla yaklaşık olarak

$$T(n) = O(n)$$

seviyesindedir. Başka bir deyişle motor, metni soldan sağa tarar ve her karakter için sınırlı miktarda iş yapar.

Örneğin basit bir kullanıcı adı kuralı şöyle yazılabilir:

```regex
^[a-zA-Z][a-zA-Z0-9_]{2,15}$
```

Bu ifade, kullanıcı adının harfle başlamasını ve toplam uzunluğunun 3 ile 16 karakter arasında olmasını sağlar. Kısa, güçlü ve elle yazılmış onlarca koşuldan daha özlüdür. Sorun, kurallar çoğaldığında başlar.

## Gücün faturası: Bilişsel yük

Regex soldan sağa okunan doğal bir cümle değildir. Nokta, yıldız, soru işareti ve parantez gibi sembollerin her biri bağlama göre farklı davranır. Bu nedenle karakter sayısının az olması, kodun basit olduğu anlamına gelmez.

| Yaklaşım | Güçlü yanı | Zayıf yanı | Uygun kullanım |
|---|---|---|---|
| Tek ve yoğun regex | Kısa, hızlı uygulanabilir | Okuması ve değiştirmesi zor | Basit, sabit kurallar |
| Parçalara ayrılmış regex | Niyet daha görünürdür | Biraz daha uzun kod üretir | Karmaşık doğrulamalar |
| Normal programlama kodu | Hata mesajları ve akış nettir | Daha fazla satır gerektirir | İş kuralları ve ayrıntılı doğrulama |
| Ayrıştırıcı kütüphanesi | Yapısal veride güvenilirdir | Ek bağımlılık getirir | HTML, SQL veya programlama dilleri |

Örneğin JavaScript’te tarih parçalarını yakalayan ifadeye doğrudan saldırmak yerine parçaları adlandırabiliriz:

```javascript
const year = "(?<year>\\d{4})";
const month = "(?<month>0[1-9]|1[0-2])";
const day = "(?<day>0[1-9]|[12]\\d|3[01])";

// Parçaları birleştirerek YYYY-MM-DD biçimini kontrol eder.
const datePattern = new RegExp(`^${year}-${month}-${day}$`);
const match = datePattern.exec("2026-07-16");

console.log(match?.groups);
```

Bu yöntem birkaç satır daha uzundur; fakat okuyucu hangi bölümün neyi temsil ettiğini hemen anlayabilir. Ayrıca adlandırılmış gruplar, `$1` ve `$2` gibi unutulmaya mahkûm referanslardan daha açıklayıcıdır.

## Backtracking: Karanlık tarafın gerçek patronu

Bazı regex motorları eşleşme başarısız olduğunda önceki kararlarına dönerek başka yollar dener. Buna **backtracking** denir. İç içe nicelik belirteçleri, denenen yolların sayısını dramatik biçimde artırabilir:

```regex
^(a+)+$
```

Bu ifade yalnızca `a` karakterlerinden oluşan metinlerde masum görünür. Ancak sonuna farklı bir karakter eklenen uzun bir girdi, motoru çok sayıda olasılığı denemeye zorlayabilir. Kötü durumda süre yaklaşık

$$T(n) = O(2^n)$$

seviyesine yaklaşabilir. Bu durum yalnızca performans sorunu değildir; saldırganların özel girdilerle uygulamayı yavaşlattığı **ReDoS** güvenlik açığına dönüşebilir.

## Regex ne zaman bırakılmalı?

Regex; e-posta içinden alan adı ayıklamak, log satırlarını süzmek veya sabit biçimleri doğrulamak için harikadır. Fakat iç içe geçmiş HTML, dengeli parantezler ya da bağlama bağlı iş kuralları söz konusuysa uygun bir ayrıştırıcı daha güvenlidir. Bir ifade yorum satırı olmadan açıklanamıyorsa onu parçalara ayırmak, testlerle belgelemek veya tamamen normal koda taşımak gerekir.

Sonuçta regex kötü değildir; yalnızca yoğunlaştırılmış güçtür. İyi kullanıldığında zarif bir neşter, ölçüsüz kullanıldığında ise bakım ekibine bırakılmış sembolik bir mayın tarlasıdır. En iyi regex, sadece çalışan değil, bir sonraki geliştiricinin de korkmadan değiştirebildiği regex’tir.
