---
layout: post
title: "Mantıksal Karşılaştırma İşlemleri: Karar Mekanizmasının Dedektifleri"
math: true
categories: 
  - Bilgi
tags: 
  - programlama
  - mantıksal-operatörler
  - karşılaştırma
---

Programlamada bir uygulamanın “akıllı” görünmesini sağlayan şey çoğu zaman çok basit bir sorudur: “Bu doğru mu, değil mi?” Mantıksal karşılaştırma işlemleri; değişkenler veya sabit değerler arasında büyüklük, küçüklük, eşitlik ya da denklik gibi ilişkileri kontrol eder ve sonucu genellikle `true` veya `false` olarak üretir. Yani kod dünyasının trafik lambaları gibidirler: geç, dur, bekle!

``

## Karşılaştırma Operatörü Nedir?

Karşılaştırma operatörleri iki değeri yan yana koyup aralarındaki ilişkiyi test eder. Matematiksel olarak bunu bir önerme gibi düşünebiliriz. Örneğin $x = 10$ ve $y = 7$ ise $x > y$ önermesi doğrudur. Programlama dilinde bu ifade çoğunlukla `true` sonucunu verir.

Temel mantık şudur:

$$
karşılaştırma(a, b) \rightarrow \{true, false\}
$$

Yani iki değer girer, mantıksal bir sonuç çıkar. Bu sonuç daha sonra `if`, `while`, `for`, `switch` veya filtreleme gibi karar mekanizmalarında kullanılır.

| Operatör | Anlamı | Örnek | Sonuç |
|---|---|---|---|
| `>` | büyüktür | `10 > 5` | `true` |
| `<` | küçüktür | `3 < 1` | `false` |
| `>=` | büyük veya eşittir | `18 >= 18` | `true` |
| `<=` | küçük veya eşittir | `7 <= 4` | `false` |
| `==` | eşitlik kontrolü | `5 == '5'` | dile göre değişir |
| `===` | tip dahil denklik | `5 === '5'` | `false` |
| `!=` | eşit değildir | `8 != 9` | `true` |
| `!==` | tip dahil farklıdır | `8 !== '8'` | `true` |

## Eşitlik ve Denklik Aynı Şey mi?

Burada eğlenceli bir tuzak var: “eşit” olmak ile “aynı türden ve aynı değer” olmak her zaman aynı değildir. Özellikle JavaScript gibi dillerde `==` değeri karşılaştırırken tür dönüşümü yapabilir. `===` ise daha disiplinlidir; hem değerin hem de tipin aynı olmasını ister.

| İfade | Açıklama | Mantıksal Yorum |
|---|---|---|
| `5 == '5'` | sayı ve metin karşılaştırılır, dönüşüm olabilir | gevşek eşitlik |
| `5 === '5'` | sayı ve metin farklı tiptedir | sıkı denklik |
| `0 == false` | bazı dillerde `0`, `false` gibi yorumlanabilir | dikkat ister |
| `0 === false` | tipler farklıdır | daha güvenlidir |

Bu yüzden karar mekanizması yazarken “Ben sadece değer mi kontrol ediyorum, yoksa tip de önemli mi?” sorusu kritik hale gelir.

## Karar Mekanizmasına Dahil Etmek

Karşılaştırmalar tek başına test yapar; asıl güçleri karar yapılarıyla birleşince ortaya çıkar. Mesela bir kullanıcının sisteme giriş yapıp yapamayacağını düşünelim. Yaşı yeterli mi? Hesabı aktif mi? Deneme hakkı kaldı mı?

```javascript
const yas = 20;
const hesapAktif = true;
const denemeHakki = 3;

if (yas >= 18 && hesapAktif === true && denemeHakki > 0) {
  console.log('Giriş izni verildi.');
} else {
  console.log('Giriş reddedildi.');
}
```

Bu kodda üç farklı karşılaştırma vardır. `yas >= 18` kullanıcının reşit olup olmadığını kontrol eder. `hesapAktif === true` hesabın gerçekten aktif olup olmadığını tip güvenli biçimde denetler. `denemeHakki > 0` ise kullanıcının hâlâ giriş denemesi yapabileceğini gösterir. `&&` operatörü ise tüm koşulların doğru olmasını ister.

Mantıksal olarak bunu şöyle yazabiliriz:

$$
izin = (yas \ge 18) \land (hesapAktif = true) \land (denemeHakki > 0)
$$

Eğer bu üç parçadan biri bile `false` olursa genel karar da `false` olur.

## Karşılaştırmalar Sadece Sayılar İçin Değildir

Karşılaştırma deyince akla hemen sayılar gelse de metinler, tarihler, boole değerler ve nesneler de karşılaştırılabilir. Ancak her veri türünün kuralları farklıdır. Metinlerde alfabetik sıralama, tarihlerde zaman damgası, nesnelerde ise referans karşılaştırması devreye girebilir.

| Veri Türü | Karşılaştırma Mantığı | Dikkat Edilecek Nokta |
|---|---|---|
| Sayı | matematiksel büyüklük | tür dönüşümü hataları |
| Metin | alfabetik/sözlük sırası | büyük-küçük harf farkı |
| Tarih | zaman karşılaştırması | format ve saat dilimi |
| Boolean | `true` / `false` | gereksiz `== true` kullanımı |
| Nesne | referans karşılaştırması | içerik aynı olsa bile farklı olabilir |

## Mini Strateji: Okunabilir Koşullar Yazmak

Karmaşık kararlar yazarken karşılaştırmaları değişkenlere ayırmak kodu daha okunabilir yapar. Aşağıdaki örnek, iş kuralını neredeyse düz Türkçe gibi okutmayı hedefler:

```javascript
const sepetTutari = 1250;
const uyeMi = true;
const stokVarMi = true;

const indirimHakEder = sepetTutari >= 1000 && uyeMi === true;
const satinAlabilir = indirimHakEder && stokVarMi === true;

console.log(satinAlabilir);
```

Burada `indirimHakEder` ve `satinAlabilir` ara karar değişkenleridir. Böylece tek satırlık dev bir koşul yerine, mantığı parçalara bölen temiz bir yapı elde edilir.

Özetle karşılaştırma operatörleri, programların karar verme kaslarıdır. Doğru kullanıldıklarında kodunuz daha güvenilir, okunabilir ve tahmin edilebilir olur. Yanlış kullanıldıklarında ise “Neden bu kullanıcı içeri girdi?” gibi klasik yazılımcı dedektiflik hikâyeleri başlar.
