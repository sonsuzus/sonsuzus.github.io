---
layout: post
title: "Arayüzler ve Çok Biçimlilik: Kim Olduğun Değil, Ne Yapabildiğin Önemli"
math: true
categories: 
  - Bilgi
tags: 
  - arayüzler
  - çok biçimlilik
  - yazılım tasarımı
---

Yazılım dünyasında bazen nesnelere fazla kimlik sorarız: “Sen gerçekten User mısın, Admin misin, Robot musun?” Oysa esnek tasarımın daha havalı sorusu şudur: “Ne yapabiliyorsun?” Arayüzler, tam da bu bakış açısını kodun merkezine koyar. Bir nesnenin sınıf soy ağacına değil, sunduğu davranış sözleşmesine odaklanır. Böylece kodumuz daha az dedikoducu, daha çok iş bitirici olur.
``

Arayüzü teorik olarak bir **sözleşme** gibi düşünebiliriz. Bir arayüz, “Beni uygulayan her yapı şu metotları, özellikleri veya davranışları sağlayacak” der. Ancak bunu nasıl yapacağını söylemez. Matematiksel olarak bir arayüzü, nesneler kümesinden davranışlar kümesine kurulan bir beklenti ilişkisi gibi görebiliriz: $I = {b_1, b_2, b_3}$ ise, bu arayüzü uygulayan her nesne bu davranışları sağlamalıdır. Burada önemli olan nesnenin iç yapısı değil, dışarıdan gözlemlenebilen davranışıdır.

Çok biçimlilik yani polymorphism ise aynı mesajın farklı nesnelerde farklı şekillerde çalışabilmesidir. Örneğin `draw()` çağrısı bir daireyi yuvarlak, bir kareyi köşeli çizer. Çağıran kod için önemli olan şeklin gerçek sınıfı değil, çizilebilir olmasıdır. Bu yaklaşım $Kod -> Arayüz$ bağımlılığını güçlendirir, $Kod -> SomutSınıf$ bağımlılığını azaltır.

| Yaklaşım | Soru | Sonuç |
|---|---|---|
| Sınıfa odaklanmak | “Bu nesne hangi tür?” | Daha sıkı bağımlılık |
| Arayüze odaklanmak | “Bu nesne ne yapabilir?” | Daha esnek tasarım |
| Kalıtım merkezli tasarım | “Kimden türedi?” | Hiyerarşi baskısı |
| Davranış merkezli tasarım | “Hangi sözleşmeyi sağlar?” | Değişime açıklık |

Basit bir TypeScript örneği düşünelim:

```typescript
interface Payable {
  calculatePayment(): number;
}

class Employee implements Payable {
  constructor(private salary: number) {}

  calculatePayment(): number {
    return this.salary;
  }
}

class Freelancer implements Payable {
  constructor(private hourlyRate: number, private hours: number) {}

  calculatePayment(): number {
    return this.hourlyRate * this.hours;
  }
}

function printPayment(entity: Payable): void {
  console.log('Ödeme: ' + entity.calculatePayment());
}

printPayment(new Employee(40000));
printPayment(new Freelancer(750, 32));
```

Burada `printPayment` fonksiyonu, parametrenin `Employee` ya da `Freelancer` olmasını umursamaz. Tek şartı vardır: `Payable` davranışını sağlaması. Bu fonksiyonun zihni oldukça rahattır; CV sormaz, sadece ödeme hesaplayabiliyor musun diye bakar.

Bu tasarımın gücü, **Açık/Kapalı Prensibi** ile birleştiğinde ortaya çıkar. Yazılım birimleri genişletmeye açık, değiştirmeye kapalı olmalıdır. Yeni bir `Consultant` sınıfı eklediğimizde `printPayment` fonksiyonunu değiştirmiyorsak doğru yoldayız demektir. Teorik olarak bu, sistemin yeni türler karşısında kararlı kalmasıdır: $YeniTip + EskiArayüz = DahaAzKırılma$.

| Tasarım ilkesi | Arayüzle ilişkisi | Pratik fayda |
|---|---|---|
| Dependency Inversion | Üst seviye modüller somuta değil soyuta bağlıdır | Test edilebilirlik artar |
| Open/Closed | Yeni davranışlar mevcut kodu bozmadan eklenir | Bakım kolaylaşır |
| Liskov Substitution | Arayüzü uygulayan nesne beklenen davranışı bozmaz | Güvenilir polymorphism |
| Interface Segregation | Büyük arayüzler küçük parçalara ayrılır | Gereksiz bağımlılık azalır |

Ancak arayüz kullanmak her derde deva büyülü bir iksir değildir. Gereksiz arayüzler, projede “soyutlama sisi” oluşturabilir. Eğer sadece tek bir sınıfınız varsa ve değişim ihtimali düşükse, hemen arayüz üretmek erken mühendislik olabilir. İyi arayüz, gerçek bir değişim eksenini temsil eder. Yani “ileride farklı ödeme stratejileri olabilir” diyorsanız `Payable` anlamlıdır; ama “belki bir gün kahve makinesi de ödeme hesaplar” diyorsanız biraz sakinleşmek gerekebilir.

Arayüzlerin bir diğer güzelliği testlerde görülür. Somut veritabanı bağlantısı yerine `Repository` arayüzüne bağımlı kod, test sırasında sahte bir bellek içi nesneyle çalışabilir. Böylece kodun davranışını izole ederiz. Bu da yazılımı daha ölçülebilir yapar; çünkü test maliyeti kabaca $Maliyet = Kurulum + Bağımlılık + Bekleme$ ise, arayüzler özellikle bağımlılık ve bekleme kısmını azaltır.

Sonuç olarak arayüzler, yazılım tasarımında kimlik kontrolünden davranış kontrolüne geçiştir. Çok biçimlilikle birleştiğinde, aynı kodun farklı nesnelerle uyumlu çalışmasını sağlar. Bu yaklaşım, gelecekte gelecek yeni sınıflara kapıyı açık bırakırken mevcut kodu sakin ve kararlı tutar. Kısacası iyi tasarlanmış bir arayüz şunu söyler: “Bana nereden geldiğini anlatma, ne yapabildiğini göster.”
