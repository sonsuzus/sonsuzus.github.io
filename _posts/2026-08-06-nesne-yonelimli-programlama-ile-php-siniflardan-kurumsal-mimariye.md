---
layout: post
title: "Nesne Yönelimli Programlama ile PHP: Sınıflardan Kurumsal Mimariye"
math: true
categories: 
  - Bilgi
tags: 
  - PHP
  - OOP
  - Yazılım Mimarisi
---

PHP ile birkaç sayfalık bir uygulama geliştirirken fonksiyonlar ve değişkenler yeterli görünebilir. Ancak proje büyüyüp kullanıcılar, siparişler, ödemeler ve raporlar devreye girdiğinde kod tabanı hızla spagettiye dönüşebilir. Nesne Yönelimli Programlama, yani OOP, bu karmaşayı gerçek dünyadaki varlıkları sınıflar ve nesneler biçiminde modelleyerek yönetmemizi sağlar.
``

## OOP mantığı: Sınıf plan, nesne üründür

Bir **sınıf**, belirli bir varlığın hangi verilere ve davranışlara sahip olacağını tanımlayan plandır. **Nesne** ise bu plandan oluşturulan somut örnektir. Örneğin `User` sınıfı bir mimari proje ise `$ayse` ve `$mehmet` bu projeye göre inşa edilmiş iki farklı ev gibidir.

Bir sınıfın durumunu özellikler, davranışlarını ise metotlar temsil eder. Bunu matematiksel olarak şöyle düşünebiliriz:

$$Nesne = Durum + Davranış$$

Durum; ad, e-posta veya bakiye gibi verilerden, davranış ise giriş yapma, ödeme gerçekleştirme veya bilgileri güncelleme gibi işlemlerden oluşur.

| Kavram | Görevi | PHP örneği |
|---|---|---|
| Sınıf | Nesnenin şablonunu tanımlar | `class User` |
| Nesne | Sınıftan üretilen örnektir | `new User()` |
| Özellik | Nesnenin verisini tutar | `$email` |
| Metot | Nesnenin davranışını tanımlar | `login()` |
| Constructor | İlk değerleri nesneye aktarır | `__construct()` |

## PHP ile ilk sınıfımız

Aşağıdaki sınıf, kullanıcı verisini ve kullanıcıya ait bir davranışı aynı yapı içerisinde toplar:

```php
<?php

class User
{
    public function __construct(
        private string $name,
        private string $email
    ) {}

    public function getEmail(): string
    {
        return $this->email;
    }

    public function introduce(): string
    {
        return "Merhaba, ben {$this->name}.";
    }
}

$user = new User("Ayşe", "ayse@example.com");
echo $user->introduce();
```

`__construct()` metodu nesne oluşturulurken otomatik çalışır. `private` özellikler dışarıdan doğrudan değiştirilemez; böylece nesnenin iç durumu korunur. `$this` ise çalışılan mevcut nesneyi ifade eder. Tip bildirimleri sayesinde yanlış veri kullanımı daha erken fark edilir.

## OOP’nin dört temel direği

OOP yalnızca kodu sınıflara bölmek değildir. Yaklaşımın arkasında dört önemli ilke bulunur:

1. **Kapsülleme:** Veriyi ve o veriyi işleyen metotları aynı yapıda toplar. İç ayrıntılar dış dünyadan saklanır.
2. **Kalıtım:** Bir sınıfın özellik ve davranışlarının başka bir sınıfa aktarılmasını sağlar.
3. **Çok biçimlilik:** Farklı sınıfların aynı arayüz üzerinden farklı davranış göstermesine imkân verir.
4. **Soyutlama:** Gereksiz ayrıntıları gizleyerek yalnızca kullanılacak sözleşmeyi öne çıkarır.

Ödeme sisteminde çok biçimlilik oldukça kullanışlıdır:

```php
interface PaymentMethod
{
    public function pay(float $amount): bool;
}

class CreditCardPayment implements PaymentMethod
{
    public function pay(float $amount): bool
    {
        // Banka servisine ödeme isteği gönderilir.
        return $amount > 0;
    }
}

class BankTransferPayment implements PaymentMethod
{
    public function pay(float $amount): bool
    {
        // Havale kaydı oluşturulur.
        return $amount > 0;
    }
}
```

Her iki sınıf da `PaymentMethod` sözleşmesine uyar. Uygulamanın geri kalanı ödemenin kartla mı yoksa havaleyle mi yapıldığını bilmek zorunda değildir. Yeni bir yöntem eklemek, mevcut kodu dağıtıp yeniden toplamaya dönüşmez.

| Prosedürel yaklaşım | Nesne yönelimli yaklaşım |
|---|---|
| Veri ve fonksiyonlar ayrıdır | Veri ve davranış birlikte modellenir |
| Küçük betiklerde pratiktir | Büyük projelerde daha sürdürülebilirdir |
| Bağımlılıklar kolayca karışabilir | Arayüzlerle bağımlılıklar azaltılabilir |
| Değişiklikler birçok dosyayı etkileyebilir | Sorumluluklar sınıflara dağıtılır |

## Kurumsal projelerde neden tercih edilir?

Kurumsal yazılımlar sürekli değişir. Bugün tek ödeme sağlayıcısı kullanan sistem yarın üç farklı sağlayıcıya bağlanabilir. OOP; **SOLID**, katmanlı mimari, bağımlılık enjeksiyonu ve tasarım desenleri gibi yaklaşımlara zemin hazırlar. Laravel ve Symfony gibi PHP framework’lerinin servis, controller, entity ve repository yapıları da bu temele dayanır.

Yine de her şeyi sınıfa çevirmek iyi mimari değildir. Her sınıfın tek ve anlaşılır bir sorumluluğu olmalı; devasa sınıflardan ve gereksiz kalıtımdan kaçınılmalıdır. Amaç daha fazla kod yazmak değil, değişikliğin maliyetini azaltmaktır. İyi modellenmiş bir PHP projesinde sınıflar yalnızca sözdizimi aracı değil, yazılımın iş dünyasını anlatan yaşayan bir haritadır.
