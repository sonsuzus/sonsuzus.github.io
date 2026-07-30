---
layout: post
title: "Kalıtım ve Çok Biçimlilik: Nesne Yönelimli Dünyanın Aile Albümü"
math: true
categories: 
  - Bilgi
tags: 
  - OOP
  - Kalıtım
  - Çok Biçimlilik
---

Nesne yönelimli programlamada bazı sınıflar birbirine şaşırtıcı derecede benzer. Örneğin kedi de köpek de bir hayvandır; ikisinin de adı, yaşı ve ses çıkarma davranışı vardır. Ancak çıkardıkları sesler aynı değildir. Kalıtım ortak özellikleri tek bir temel sınıfta toplamamızı, çok biçimlilik ise ortak görünen davranışların nesneye göre farklı sonuç üretmesini sağlar. Böylece kodumuz hem tekrar etmekten kurtulur hem de yeni türlere daha kolay uyum sağlar.
``

## Kalıtımın Temel Mantığı

Kalıtım, bir **alt sınıfın** başka bir sınıfta tanımlanan özellik ve metotları devralmasıdır. Özellikleri aktaran sınıfa temel sınıf, üst sınıf veya ebeveyn sınıf denir. Bunları alan sınıf ise alt sınıf ya da çocuk sınıftır.

Örneğin `Hayvan` sınıfında `ad` özelliğini ve `bilgi_ver()` metodunu tanımlayabiliriz. `Kedi` ve `Kopek` sınıfları bu ortak üyeleri yeniden yazmadan kullanabilir. Bu ilişki genellikle “bir türüdür” testiyle anlaşılır: Kedi bir hayvan türüdür, dolayısıyla kalıtım burada mantıklıdır.

```python
class Hayvan:
    def __init__(self, ad):
        self.ad = ad

    def bilgi_ver(self):
        return f"Benim adım {self.ad}."


class Kedi(Hayvan):
    pass


tekir = Kedi("Tekir")
print(tekir.bilgi_ver())
```

`Kedi` sınıfının gövdesinde `bilgi_ver()` bulunmamasına rağmen `tekir` nesnesi bu metodu kullanabilir. Python metodu önce alt sınıfta arar, bulamazsa kalıtım zincirinde yukarı doğru ilerler.

Kalıtım sayesinde elde edilen basit kod kazancını yaklaşık olarak şöyle düşünebiliriz:

$$Kazanım = Tekrarlanan\ Kod - Ek\ Soyutlama\ Maliyeti$$

Kalıtım gereksiz yere kullanılırsa soyutlama maliyeti artar. Bu nedenle yalnızca kod tekrarını azaltmak için değil, sınıflar arasında gerçek bir tür ilişkisi bulunduğunda tercih edilmelidir.

| Kavram | Görevi | Günlük yaşam benzetmesi |
|---|---|---|
| Temel sınıf | Ortak yapıyı tanımlar | Aileden gelen ortak özellikler |
| Alt sınıf | Yapıyı devralır ve genişletir | Bireyin kendine özgü özellikleri |
| Metot ezme | Davranışı yeniden tanımlar | Aynı soruya farklı cevap vermek |
| Çok biçimlilik | Ortak arayüzle farklı sonuç üretir | Her müzisyenin aynı notayı farklı çalması |

## Metot Ezme ve Çok Biçimlilik

Alt sınıf, temel sınıftan gelen bir metodu aynı isimle yeniden tanımlayabilir. Buna **metot ezme** (`override`) denir. Çok biçimliliğin sihri de burada ortaya çıkar: Program aynı `ses_cikar()` çağrısını yapar, fakat çalıştırılan kod nesnenin gerçek türüne göre seçilir.

```python
class Hayvan:
    def __init__(self, ad):
        self.ad = ad

    def ses_cikar(self):
        return "Bilinmeyen bir ses"


class Kedi(Hayvan):
    def ses_cikar(self):
        return "Miyav!"


class Kopek(Hayvan):
    def ses_cikar(self):
        return "Hav hav!"


hayvanlar = [Kedi("Tekir"), Kopek("Karabaş")]

for hayvan in hayvanlar:
    print(hayvan.ad, hayvan.ses_cikar())
```

Döngü, listedeki nesnelerin türünü denetleyen uzun `if` blokları içermez. Her nesne nasıl ses çıkaracağını kendisi bilir. Bu yaklaşım, programa yeni bir `Kus` sınıfı eklendiğinde mevcut döngünün değiştirilmesine gerek bırakmaz.

## `super()` ile Temel Davranışı Korumak

Bazen üst sınıftaki davranışı tamamen silmek yerine genişletmek isteriz. `super()`, temel sınıfın metoduna kontrollü biçimde ulaşmamızı sağlar.

```python
class Kus(Hayvan):
    def __init__(self, ad, kanat_acikligi):
        super().__init__(ad)
        self.kanat_acikligi = kanat_acikligi

    def bilgi_ver(self):
        temel_bilgi = super().bilgi_ver()
        return f"{temel_bilgi} Kanat açıklığım {self.kanat_acikligi} cm."
```

Burada temel sınıfın kurucusu `ad` değerini hazırlar; alt sınıf yalnızca kendine özgü `kanat_acikligi` alanını ekler. Böylece ortak kurulum kodu kopyalanmaz.

## Ne Zaman Kullanılmalı?

Kalıtım güçlüdür ancak her ilişki kalıtım değildir. “Araba bir motordur” ifadesi yanlış olduğu için `Araba`, `Motor` sınıfından türetilmemelidir; araba bir motora **sahiptir**. Bu durumda bileşim daha uygundur.

Çok biçimlilik ise ödeme yöntemleri, dosya biçimleri, bildirim kanalları ve oyun karakterleri gibi ortak bir işlemin farklı uygulanabildiği sistemlerde parıldar. Kısacası kalıtım sınıfların ortak geçmişini, çok biçimlilik ise kendilerine özgü karakterlerini temsil eder. İyi tasarlandıklarında kod ailesinde herkes akrabadır, fakat kimse aynı şakaya aynı tepkiyi vermek zorunda değildir.
