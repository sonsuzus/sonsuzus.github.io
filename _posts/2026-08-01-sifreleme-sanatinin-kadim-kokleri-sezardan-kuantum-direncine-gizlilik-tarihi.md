---
layout: post
title: "Şifreleme Sanatının Kadim Kökleri: Sezar’dan Kuantum Direncine Gizlilik Tarihi"
math: true
categories: 
  - Bilgi
tags: 
  - kriptografi
  - siber güvenlik
  - kuantum bilişim
---

Mahremiyet, akıllı telefonlarla ortaya çıkmış modern bir endişe değil. İnsanlar; savaş planlarını, ticari sırlarını ve kişisel düşüncelerini başkalarının meraklı gözlerinden korumaya binlerce yıldır çalışıyor. Kil tabletten bulut sunucusuna uzanan bu hikâyede araçlar değişse de temel soru aynı kaldı: Bir mesajı yalnızca doğru kişinin anlayabilmesini nasıl sağlarız?
``
## İlk sırlar: Yerine koyma sanatı

Bilinen erken örneklerden biri, Antik Yunan’daki **skytale** yöntemidir. Bir deri şerit belirli kalınlıktaki sopaya sarılır, mesaj şeridin üzerine yazılırdı. Şerit açıldığında harfler anlamsız görünür; aynı çaptaki sopaya yeniden sarıldığında mesaj okunurdu. Bu yöntem, şifrelemenin yalnızca harflerle değil, fiziksel düzenle de yapılabileceğini gösteriyordu.

Roma dünyasında ise Jül Sezar’ın adıyla özdeşleşen **Sezar şifresi** kullanıldı. Mantık basitti: Alfabedeki her harf belirli miktarda kaydırılır. Harfleri sayılarla temsil edersek işlem şöyle yazılabilir:

$$E(x) = (x + k) \bmod 26$$

Burada $x$ açık harfin konumu, $k$ gizli anahtar, $E(x)$ ise şifreli harftir. Çözme işlemi ters yönde ilerler:

$$D(x) = (x - k) \bmod 26$$

Aşağıdaki Python kodu, İngiliz alfabesi üzerinde bu fikri uygular:

```python
def caesar(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

secret = caesar("Meet at dawn", 3)
print(secret)                 # Phhw dw gdzq
print(caesar(secret, -3))     # Meet at dawn
```

Kod, harfleri sayısal konumlarına dönüştürür ve modüler aritmetik sayesinde alfabenin sonundan başına döner. Eğlenceli bir deneydir; ancak yalnızca 26 olası kaydırma bulunduğundan gerçek güvenlik sağlamaz.

## Şifre kırıcıların yükselişi

Dokuzuncu yüzyılda El-Kindî, harflerin kullanım sıklığını inceleyerek **frekans analizini** sistemleştirdi. Örneğin bir dilde en sık görülen şifreli sembolün, o dilin en yaygın harfini temsil etmesi muhtemeldi. Böylece kriptografi ile kriptoanaliz arasında bugün hâlâ süren bir yarış başladı.

| Dönem | Yaklaşım | Ana fikir | Temel zayıflık |
|---|---|---|---|
| Antik Çağ | Skytale | Fiziksel yer değiştirme | Uygun çubuk tahmin edilebilir |
| Roma | Sezar şifresi | Sabit harf kaydırma | Anahtar uzayı çok küçük |
| Rönesans | Vigenère | Birden fazla kaydırma | Tekrarlayan anahtar örüntüsü |
| 20. yüzyıl | Enigma | Elektromekanik dönüşüm | Operasyon hataları ve örüntüler |
| Modern çağ | AES ve RSA | Matematiksel zorluk | Uygulama hataları, kuantum tehdidi |

## Makineler, savaşlar ve modern matematik

İkinci Dünya Savaşı’nda Enigma, rotorları kullanarak her tuş vuruşunda farklı bir dönüşüm üretiyordu. Alan Turing ve Bletchley Park ekibinin çalışmaları, güçlü görünen sistemlerin bile matematik, mühendislik ve kullanıcı hatalarının birleşimiyle çözülebileceğini gösterdi.

1970’lerden sonra iki büyük yaklaşım belirginleşti. **Simetrik şifrelemede** aynı anahtar hem kilitlemek hem açmak için kullanılır; AES bunun hızlı ve yaygın örneğidir. **Asimetrik şifrelemede** ise açık ve özel anahtar çifti bulunur. RSA’nın güvenliği, büyük sayıların çarpanlarına ayrılmasının klasik bilgisayarlar için zor olmasına dayanır.

| Özellik | Simetrik şifreleme | Asimetrik şifreleme |
|---|---|---|
| Anahtar | Tek ve gizli | Açık–özel anahtar çifti |
| Hız | Yüksek | Daha düşük |
| Kullanım | Büyük verileri şifreleme | Anahtar paylaşımı, imza |
| Örnek | AES | RSA, eliptik eğriler |

## Kuantum sonrası yeni perde

Yeterince güçlü bir kuantum bilgisayar, Shor algoritmasıyla RSA ve eliptik eğri sistemlerini tehdit edebilir. Bu nedenle araştırmacılar; **kafes tabanlı**, **kod tabanlı**, özet tabanlı ve çok değişkenli yapılar üzerinde çalışıyor. NIST’in standartlaştırdığı ML-KEM gibi algoritmalar, kuantum saldırılarına karşı dayanıklı anahtar paylaşımını hedefliyor.

Bu geçiş yalnızca yeni algoritma kurmak değildir. Bugün ele geçirilen şifreli veriler gelecekte çözülebilir; buna “şimdi topla, sonra çöz” tehdidi denir. Dolayısıyla kuantum dirençli sistemlere geçiş, gelecekteki bir bilgisayarı beklemeden başlamalıdır.

Kil tabletlerden matematiksel kafeslere kadar şifreleme tarihi bize aynı dersi veriyor: Mutlak ve sonsuz güvenlik yoktur. Mahremiyet; iyi matematik, doğru uygulama, güvenli anahtar yönetimi ve değişen tehditlere uyum sağlama sanatıdır.
