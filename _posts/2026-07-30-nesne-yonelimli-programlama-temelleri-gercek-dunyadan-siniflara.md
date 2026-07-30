---
layout: post
title: "Nesne Yönelimli Programlama Temelleri: Gerçek Dünyadan Sınıflara"
math: true
categories: 
  - Bilgi
tags: 
  - OOP
  - Nesne Yönelimli Programlama
  - Sınıflar
---

Bir otomobili yazılımla temsil etmek istediğimizi düşünelim. Otomobilin rengi, hızı ve yakıt miktarı gibi verileri; hızlanma veya fren yapma gibi davranışları vardır. Nesne Yönelimli Programlama (Object-Oriented Programming — OOP), birbiriyle ilişkili bu verileri ve davranışları tek bir yapı içinde toplamamızı sağlar. Böylece kodumuz, gerçek dünyadaki kavramlara benzeyen, anlaşılır ve yeniden kullanılabilir parçalardan oluşur.

``

## Sınıf ve nesne arasındaki fark

OOP'nin merkezinde **sınıf** ve **nesne** bulunur. Sınıf, nesnelerin hangi özelliklere ve metotlara sahip olacağını belirleyen bir şablondur. Nesne ise bu şablondan üretilmiş somut bir örnektir.

Bunu kurabiye kalıbına benzetebiliriz: Kalıp sınıf, kalıpla hazırlanan her kurabiye ise ayrı bir nesnedir. Kurabiyelerin şekli aynı olsa da renkleri veya süslemeleri farklı olabilir.

| Kavram | Görevi | Otomobil örneği |
|---|---|---|
| Sınıf | Genel şablonu tanımlar | `Otomobil` |
| Nesne | Sınıftan üretilen örnektir | Kırmızı otomobil |
| Özellik | Nesnenin durumunu saklar | Renk, hız, yakıt |
| Metot | Nesnenin davranışını tanımlar | Hızlan, fren yap |

Bir nesnenin durumunu matematiksel olarak özellikler kümesiyle gösterebiliriz:

$$Nesne = Durum + Davranış$$

Örneğin bir otomobilin durumu $D = \{renk, hız, yakıt\}$, davranışları ise $B = \{hızlan, fren\}$ biçiminde düşünülebilir.

## İlk sınıfımızı oluşturalım

Aşağıdaki Python sınıfı, otomobilin verilerini saklar ve hızını kontrollü biçimde değiştiren metotlar sunar:

```python
class Otomobil:
    def __init__(self, marka, renk, yakit):
        self.marka = marka
        self.renk = renk
        self.yakit = yakit
        self.hiz = 0

    def hizlan(self, miktar):
        gereken_yakit = miktar * 0.05

        if gereken_yakit <= self.yakit:
            self.hiz += miktar
            self.yakit -= gereken_yakit
        else:
            print("Yeterli yakıt yok!")

    def fren_yap(self, miktar):
        self.hiz = max(0, self.hiz - miktar)

    def bilgileri_goster(self):
        return f"{self.marka}: {self.hiz} km/sa, {self.yakit:.1f} litre"
```

`__init__`, nesne oluşturulurken otomatik çalışan **kurucu metottur**. `self`, işlem yapılan mevcut nesneyi temsil eder. `hizlan` metodu hem hızı hem de yakıtı değiştirirken `fren_yap`, hızın sıfırın altına düşmesini engeller.

Şimdi aynı sınıftan bağımsız iki nesne üretelim:

```python
araba_1 = Otomobil("Volvo", "Mavi", 40)
araba_2 = Otomobil("Toyota", "Beyaz", 25)

araba_1.hizlan(50)
araba_2.hizlan(30)
araba_2.fren_yap(10)

print(araba_1.bilgileri_goster())
print(araba_2.bilgileri_goster())
```

Her nesne kendi `hiz` ve `yakit` değerlerini saklar. `araba_1` üzerinde gerçekleştirilen işlem, `araba_2` nesnesini etkilemez. Bu ayrım, büyük uygulamalarda veri karmaşasını önleyen önemli bir avantajdır.

## OOP'nin dört temel ilkesi

OOP yalnızca sınıf yazmaktan ibaret değildir. Sağlam tasarımlar genellikle dört temel ilkeye dayanır:

| İlke | Temel amaç | Kısa örnek |
|---|---|---|
| Kapsülleme | Veriyi kontrol altında tutmak | Hızın metotla değiştirilmesi |
| Kalıtım | Ortak davranışları devralmak | `ElektrikliOtomobil`, `Otomobil` sınıfını genişletir |
| Çok biçimlilik | Aynı çağrıya farklı tepki vermek | Her aracın farklı `hareket_et` metodu |
| Soyutlama | Gereksiz ayrıntıları gizlemek | Sürücünün motor hesabını bilmemesi |

**Kapsülleme**, nesnenin iç durumuna rastgele müdahale edilmesini sınırlar. **Kalıtım**, mevcut sınıfların özelliklerini yeni sınıflarda kullanmayı sağlar. **Çok biçimlilik**, aynı metot adının nesne türüne göre farklı çalışabilmesidir. **Soyutlama** ise kullanıcıya yalnızca ihtiyaç duyduğu arayüzü gösterir.

## Neden OOP kullanalım?

OOP; banka hesapları, kullanıcılar, oyun karakterleri veya siparişler gibi belirgin varlıklara sahip sistemlerde oldukça etkilidir. İlgili veri ve davranışlar aynı yerde tutulduğu için kodun okunması, test edilmesi ve genişletilmesi kolaylaşır. Ancak her küçük problem için onlarca sınıf oluşturmak da gereksiz karmaşıklık yaratabilir.

Özetle sınıf bir plan, nesne bu planın çalışan örneğidir. İyi tasarlanmış bir nesne neyi bildiğini özellikleriyle, neler yapabildiğini ise metotlarıyla anlatır. Kod konuşabilseydi muhtemelen şöyle derdi: “Verimi bana bırak, davranışımı metotlarımdan iste!”
