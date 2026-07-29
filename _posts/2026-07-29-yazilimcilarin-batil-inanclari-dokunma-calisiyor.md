---
layout: post
title: "Yazılımcıların Batıl İnançları: Dokunma, Çalışıyor!"
math: true
categories: 
  - Bilgi
tags: 
  - yazılım kültürü
  - teknik borç
  - antropoloji
---

Bir yazılım ekibinde yeterince uzun süre kalırsanız şu cümleyi mutlaka duyarsınız: “O satırı silmeyin; neden çalıştığını kimse bilmiyor.” Bu uyarı bazen yorum satırında, bazen ekip sohbetinde, bazen de yıllardır şirkette çalışan bir geliştiricinin ciddi bakışlarında yaşar. Kod artık yalnızca teknik bir yapı değildir; etrafında tabular, ritüeller ve kuşaktan kuşağa aktarılan efsaneler oluşmuştur.
``
Antropolojik açıdan batıl inanç, belirsizlik karşısında kontrol hissi üreten davranıştır. Yağmur duası ile dağıtım öncesinde belirli bir kupadan kahve içmek aynı bilimsel değere sahip olmayabilir; fakat psikolojik işlevleri benzerdir. Yazılım sistemleri büyüdükçe tek bir kişinin bütünü anlaması zorlaşır. Bir değişikliğin riskini kabaca

$$R = P(\text{hata}) \times E(\text{etki})$$

olarak düşünürsek eski, belgesiz ve kritik bir modülde hem hata olasılığı hem de etkinin büyüklüğü yüksek algılanır. Bilgi eksikliği bu hesabı ölçülebilir olmaktan çıkarır; boşluğu ise söylentiler doldurur.

## Kabile Hafızası ve Kutsal Kod

Ekiplerin “kutsal” kabul ettiği kod genellikle geçmişte büyük bir arızayla ilişkilidir. Bir geliştirici satırı değiştirmiş, üretim sistemi çökmüş ve olayın ayrıntıları zamanla unutulmuştur. Geriye yalnızca yasak kalır. Antropolojide buna kültürel aktarım diyebiliriz: Gerekçe kaybolsa bile davranış yaşamaya devam eder.

| Ritüel veya inanç | Görünür gerekçe | Muhtemel teknik köken |
|---|---|---|
| Cuma günü dağıtım yapılmaz | “Kesin sistem çöker” | Hafta sonu destek ekibi eksikliği |
| Eski fonksiyona dokunulmaz | “Denge bozulur” | Test ve dokümantasyon eksikliği |
| Sunucu yeniden başlatılır | “Kendine gelir” | Bellek sızıntısı veya kilitlenme |
| Belirli sırayla komut çalıştırılır | “Başka türlü olmuyor” | Gizli durum ve bağımlılıklar |

Bu davranışlar tamamen anlamsız değildir. Çoğu, gerçek bir tehlikenin kaba biçimde kodlanmış hatırasıdır. Sorun, geçici önlemin zamanla açıklanamaz bir dogmaya dönüşmesidir.

## Totem Olarak Yorum Satırı

Aşağıdaki yorum birçok kod tabanının mağara duvarı resmidir:

```javascript
// DOKUNMA: Bu gecikme kaldırılırsa ödeme işlemi bazen iki kez çalışıyor.
await sleep(500);
await processPayment(order);
```

Buradaki `sleep`, muhtemelen bir yarış durumunu tesadüfen bastırır. Ancak yorum neden-sonuç ilişkisini açıklamadığı için ekip gecikmeyi koruyan bir ritüel geliştirir. Daha mühendisçe yaklaşım, işlemi benzersiz bir anahtarla idempotent hâle getirmektir:

```javascript
async function processPayment(order) {
  const key = `payment:${order.id}`;
  if (await paymentExists(key)) return;

  await createPayment({ key, orderId: order.id });
}
```

Bu sürümde aynı sipariş yeniden işlense bile ikinci ödeme oluşturulmaz. Ritüelin yerine doğrulanabilir bir kural konmuştur.

## Şamanlar, Kıdemliler ve Bilgi Tekelleri

Bazı ekiplerde yalnızca bir kişi üretim sunucusunu “sakinleştirmeyi” bilir. Bu kişi modern bir sistem şamanına dönüşür: Hangi servisin önce başlatılacağını, hangi logun kötü alamet sayıldığını ve hangi betiğin yalnızca salı günleri çalıştığını bilir. Bu uzmanlık kısa vadede değerlidir; uzun vadede ise otobüs faktörünü düşürür. Sistemi bilen kişi sayısını $n$ ile gösterirsek, $n=1$ durumu teknik olduğu kadar örgütsel bir risktir.

Sağlıklı ekipler kişiyi küçümsemek yerine bilgisini görünür kılar. Olay sonrası değerlendirmeler suçlama amacıyla değil, efsaneyi kanıta dönüştürmek için yapılmalıdır. Karakterizasyon testleri mevcut davranışı kaydeder; gözlemlenebilirlik araçları gizli bağımlılıkları açığa çıkarır; küçük ve geri alınabilir değişiklikler korkuyu azaltır.

## Büyüyü Mühendisliğe Dönüştürmek

“Dokunmayın” uyarısıyla karşılaştığınızda kodu kahramanca silmek de başka bir irrasyonel ritüeldir. Önce geçmiş olayları araştırın, log ve metrik ekleyin, davranışı testlerle sabitleyin ve değişikliği kademeli yayımlayın. Amaç ekip folklorunu yok etmek değil, içindeki teknik sinyali ayıklamaktır.

Sonuçta yazılımcı batıl inançları cehaletten çok belirsizliğin ürünüdür. İyi mühendislik, insanlara “korkmayın” demekle yetinmez; korkunun yerine deney, ölçüm ve geri dönüş planı koyar. Böylece kutsal kod sıradan koda, şaman bilgisi dokümantasyona, gizemli ritüeller de anlaşılır süreçlere dönüşür.
