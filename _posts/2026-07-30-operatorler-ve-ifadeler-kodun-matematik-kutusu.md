---
layout: post
title: "Operatörler ve İfadeler: Kodun Matematik Kutusu"
math: true
categories: 
  - Bilgi
tags: 
  - operatörler
  - programlama temelleri
  - ifadeler
---

Bir programın karar vermesi, hesaplama yapması ve veriyi dönüştürmesi çoğunlukla operatörler sayesinde gerçekleşir. Fiyat hesaplayan bir e-ticaret uygulamasından oyuncunun canını kontrol eden bir oyuna kadar her yerde ifadelerle karşılaşırız. Operatörleri, veriler üzerinde çalışan küçük araçlar; ifadeleri ise bu araçlarla kurulan anlamlı cümleler gibi düşünebiliriz.
``

## Operatör ve ifade nedir?

Operatör, bir veya daha fazla değer üzerinde işlem yapan sembol ya da anahtar kelimedir. `+`, `>`, `==` ve `and` birer operatördür. Operatörün işlediği değerlere **operand** denir. Örneğin `8 + 2` ifadesinde `8` ve `2` operand, `+` ise operatördür.

Bir **ifade**, çalıştırıldığında sonuç üreten kod parçasıdır. Matematiksel olarak bunu şöyle gösterebiliriz:

$$sonuç = operand_1 \; operatör \; operand_2$$

`5 * 4` ifadesinin sonucu `20`, `10 > 3` ifadesinin sonucu ise `True` değeridir. Sonucun her zaman sayı olması gerekmez; mantıksal bir değer, metin veya başka bir veri türü de üretilebilir.

## Aritmetik operatörler

Aritmetik operatörler temel matematiksel hesaplamaları gerçekleştirir.

| Operatör | İşlem | Örnek | Sonuç |
|---|---|---|---|
| `+` | Toplama | `7 + 3` | `10` |
| `-` | Çıkarma | `7 - 3` | `4` |
| `*` | Çarpma | `7 * 3` | `21` |
| `/` | Bölme | `7 / 2` | `3.5` |
| `%` | Kalan bulma | `7 % 2` | `1` |
| `**` | Üs alma | `2 ** 3` | `8` |
| `//` | Tam bölme | `7 // 2` | `3` |

Örneğin indirimli fiyatın formülü $P_{son}=P-(P\times i)$ biçimindedir. Python ile bunu doğrudan ifade edebiliriz:

```python
fiyat = 800
indirim_orani = 0.15
indirimli_fiyat = fiyat - (fiyat * indirim_orani)

print(indirimli_fiyat)  # 680.0
```

Parantezler yalnızca okunabilirliği artırmaz, işlem sırasını da belirler. `2 + 3 * 4` işlemi `14` üretirken `(2 + 3) * 4` işlemi `20` üretir. Genel öncelik sırası parantez, üs alma, çarpma-bölme ve toplama-çıkarma şeklindedir.

## Karşılaştırma operatörleri

Karşılaştırmalar iki değerin ilişkisini inceler ve `True` ya da `False` üretir.

| Operatör | Anlamı | Örnek |
|---|---|---|
| `==` | Eşittir | `puan == 100` |
| `!=` | Eşit değildir | `durum != "pasif"` |
| `>` | Büyüktür | `yas > 18` |
| `<` | Küçüktür | `stok < 5` |
| `>=` | Büyük veya eşittir | `not >= 50` |
| `<=` | Küçük veya eşittir | `sicaklik <= 0` |

Burada `=` ile `==` karıştırılmamalıdır. `=` değişkene değer atar; `==` iki değerin eşitliğini sorgular. Bu küçük fark, büyük hataların klasik kaynağıdır.

## Mantıksal operatörler

Mantıksal operatörler birden fazla koşulu birleştirir. `and`, bütün koşullar doğruysa; `or`, koşullardan en az biri doğruysa `True` üretir. `not` ise sonucu tersine çevirir.

| Operatör | Gerekli durum | Günlük dilde karşılığı |
|---|---|---|
| `and` | Her iki koşul doğru | “Bu da, şu da” |
| `or` | En az bir koşul doğru | “Bu veya şu” |
| `not` | Koşulun tersi | “Böyle değilse” |

```python
yas = 22
uyelik_aktif = True
kupon_var = False

alisveris_izni = yas >= 18 and uyelik_aktif
avantaj_var = uyelik_aktif and (kupon_var or yas < 25)

print(alisveris_izni)  # True
print(avantaj_var)     # True
```

İlk ifade, kullanıcının hem yetişkin hem aktif üye olmasını ister. İkinci ifade ise aktif üyeliğe ek olarak kupon veya genç kullanıcı avantajından birini yeterli görür.

## Kısa devre değerlendirmesi

Mantıksal ifadeler çoğu dilde soldan sağa değerlendirilir. `False and işlem()` ifadesinde sonuç zaten yanlış olduğundan `işlem()` çağrılmayabilir. Benzer biçimde `True or işlem()` için ikinci bölüm gereksizdir. Buna **kısa devre değerlendirmesi** denir.

```python
kullanici = None

if kullanici is not None and kullanici["aktif"]:
    print("Hoş geldin!")
```

İlk koşul yanlışsa ikinci koşul çalıştırılmaz; böylece `None` değeri üzerinde veri okumaya çalışmaktan doğacak hata önlenir.

Operatörleri öğrenirken ezberden çok ifadeyi parçalara ayırmak faydalıdır: Önce operandları, sonra işlem önceliğini, en sonunda oluşacak veri türünü belirleyin. Kodun matematik kutusu doğru kullanıldığında hesaplamalar netleşir, koşullar okunabilir olur ve veri manipülasyonu şaşırtıcı ölçüde kolaylaşır.
