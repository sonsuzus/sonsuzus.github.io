---
layout: post
title: "Arayüzler: Nesne Yönelimli Tasarımın Görünmez Sözleşmeleri"
math: true
categories: 
  - Bilgi
tags: 
  - arayüzler
  - nesne yönelimli programlama
  - yazılım tasarımı
---

Bir orkestrada her müzisyen farklı bir enstrüman çalabilir; ancak şefin verdiği işaretlerin ne anlama geldiğini hepsi bilir. Nesne yönelimli programlamadaki **arayüzler (interfaces)** de benzer biçimde çalışır. Bir sınıfın iç dünyasını yönetmez, fakat dışarıya hangi özellikleri ve davranışları sunması gerektiğini açıkça bildirir. Böylece birbirinden farklı nesneler, ortak bir sözleşmeye uyarak aynı sistem içinde güvenle çalışabilir.
``

## Arayüz tam olarak nedir?

Arayüz, bir nesnenin **ne yapacağını** tanımlayan; bunu **nasıl yapacağını** ise uygulayıcı sınıfa bırakan soyut bir şablondur. Örneğin `OdemeYontemi` isimli bir arayüz, her ödeme yönteminin `ode()` metoduna sahip olmasını zorunlu kılabilir. Kredi kartı, banka havalesi veya dijital cüzdan bu işlemi farklı şekilde gerçekleştirir; önemli olan, dışarıdan bakıldığında hepsinin aynı davranışı sunmasıdır.

Bu düşünceyi küme mantığıyla ifade edebiliriz. Bir $I$ arayüzünün zorunlu tuttuğu davranış kümesi $B_I$, bir $C$ sınıfının sunduğu davranış kümesi ise $B_C$ olsun. Sınıfın sözleşmeyi sağlaması için şu koşul geçerlidir:

$$B_I \subseteq B_C$$

Yani sınıf, arayüzde belirtilen bütün üyeleri içermelidir; isterse bunlara yeni özellikler ve metotlar da ekleyebilir.

## Sınıf, soyut sınıf ve arayüz farkı

Bu üç yapı sıkça aynı çekmeceye atılsa da görevleri farklıdır:

| Yapı | Temel amacı | Uygulama kodu | Çoklu kullanım |
|---|---|---|---|
| Sınıf | Veri ve davranışı gerçekleştirmek | Tamdır | Genellikle tek kalıtım |
| Soyut sınıf | Ortak temel ve kısmi uygulama sunmak | Kısmi olabilir | Dile bağlıdır |
| Arayüz | Uyulacak sözleşmeyi tanımlamak | Genellikle davranış bildirir | Bir sınıf birden fazlasını uygulayabilir |

Arayüzü bir **priz standardı**, sınıfı ise o prize bağlanan cihaz gibi düşünebiliriz. Televizyon ile kahve makinesinin iç mekanizması aynı değildir; fakat ikisi de uygun fişe sahipse elektrik altyapısıyla iletişim kurabilir.

## TypeScript ile sözleşme oluşturmak

Aşağıdaki örnekte bütün bildirim servislerinin uyması gereken yapı tanımlanıyor:

```typescript
interface BildirimServisi {
  servisAdi: string;
  gonder(alici: string, mesaj: string): boolean;
}

class EpostaServisi implements BildirimServisi {
  servisAdi = "E-posta";

  gonder(alici: string, mesaj: string): boolean {
    console.log(`${alici} adresine gönderildi: ${mesaj}`);
    return true;
  }
}

function kullaniciyiBilgilendir(
  servis: BildirimServisi,
  alici: string
): void {
  servis.gonder(alici, "Siparişiniz hazır!");
}
```

Buradaki `kullaniciyiBilgilendir` fonksiyonu doğrudan `EpostaServisi` sınıfına bağımlı değildir. Yalnızca `BildirimServisi` sözleşmesini tanır. Daha sonra SMS veya mobil bildirim sınıfı eklendiğinde fonksiyonun değiştirilmesi gerekmez. Kodun yeni davranışlara açılırken mevcut yapıda değişiklik istememesi, **Açık/Kapalı Prensibi** ile uyumludur.

## Gevşek bağlılık neden değerlidir?

Bir sınıf başka bir somut sınıfa doğrudan bağımlıysa değişiklikler zincirleme etki yaratabilir. Arayüz kullanıldığında bağımlılık, uygulama ayrıntısına değil soyut sözleşmeye yönelir. Bu yaklaşım **Bağımlılıkların Tersine Çevrilmesi Prensibi**nin temelidir.

| Doğrudan bağımlılık | Arayüz tabanlı bağımlılık |
|---|---|
| Bileşenler sıkı bağlıdır | Bileşenler değiştirilebilir |
| Testlerde gerçek servis gerekebilir | Sahte servis kolayca yazılabilir |
| Değişiklik riski yüksektir | Etki alanı daha sınırlıdır |
| Yeniden kullanım zordur | Esneklik daha yüksektir |

Örneğin test sırasında gerçekten e-posta göndermek yerine aynı arayüzü uygulayan bir `SahteBildirimServisi` kullanılabilir. Böylece test hızlı, ücretsiz ve öngörülebilir olur.

## Her yere arayüz eklenmeli mi?

Hayır. Tek uygulaması bulunan ve değişme ihtimali düşük, küçük yapılara sırf “kurumsal görünsün” diye arayüz eklemek gereksiz karmaşıklık yaratabilir. Arayüzler özellikle birden fazla uygulama beklendiğinde, dış sistemler soyutlandığında veya bileşenlerin bağımsız test edilmesi gerektiğinde değerlidir.

Kısacası arayüzler yalnızca metot listeleri değildir; ekipler ve bileşenler arasında kurulmuş teknik anlaşmalardır. İyi tasarlanmış bir arayüz, nesnenin iç ayrıntılarını gizlerken beklentileri netleştirir. Kod değiştikçe sözleşme sabit kalabiliyorsa sistem daha esnek, test edilebilir ve sürdürülebilir hâle gelir.
