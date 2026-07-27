---
layout: post
title: "Programcının Bilişsel Yükü: Bazı Kodlar Neden Beyni Daha Çok Yorar?"
math: true
categories: 
  - Bilgi
tags: 
  - bilişsel yük
  - kod okunabilirliği
  - çalışan bellek
---

Bir kod bloğunu okurken bazen her şey ilk bakışta yerine oturur; bazen de üç satır sonra değişkenlerin neyi temsil ettiğini unutup başa dönersiniz. Sorun her zaman algoritmanın karmaşıklığı değildir. Kod, bilgisayar için kusursuz çalışırken insan zihni için yorucu olabilir. Bunun nedeni, beynimizin aynı anda işleyebildiği bilgi miktarının sınırlı olmasıdır.

``

## Çalışan bellek: Zihnin küçük çalışma masası

Bilişsel psikolojide **çalışan bellek**, bilgiyi kısa süre boyunca tutup işlediğimiz zihinsel sistemdir. Bir telefon numarasını tuşlayana kadar akılda tutmak veya bir fonksiyonun akışını takip etmek çalışan belleği kullanır.

Kapasitesi sınırsız değildir. Modern çalışmalar kesin sayının göreve göre değiştiğini gösterse de insanın aynı anda yaklaşık $4 \pm 1$ anlamlı bilgi parçasını etkin biçimde yönetebildiği kabul edilir. Programcı bir kod bloğunu incelerken değişkenlerin değerlerini, koşulları, fonksiyon çağrılarını ve iş kurallarını bu küçük çalışma masasına yerleştirir.

Bilişsel yükü kabaca şöyle düşünebiliriz:

$$Y_{toplam} = Y_{içsel} + Y_{dışsal} + Y_{öğrenme}$$

- **İçsel yük**, problemin doğal karmaşıklığıdır. Dağıtık sistemler, tarih hesaplamasından doğası gereği daha zordur.
- **Dışsal yük**, kötü adlar, gereksiz iç içe koşullar ve dağınık akış gibi sunum kaynaklı yüktür.
- **Öğrenme yükü**, yeni ve yararlı zihinsel modeller kurmak için harcanan çabadır.

İçsel yükü her zaman azaltamayız; fakat dışsal yükü iyi tasarlanmış kodla ciddi biçimde düşürebiliriz.

## Aynı iş, farklı zihinsel maliyet

Aşağıdaki JavaScript kodu indirimli ve aktif ürünlerin toplamını hesaplıyor:

```javascript
let t = 0;
for (let i = 0; i < p.length; i++) {
  if (p[i].a === true) {
    if (p[i].s > 0) {
      t += p[i].pr * (1 - p[i].d);
    }
  }
}
```

Bilgisayar bunu kolayca yorumlar. İnsan ise `t`, `p`, `a`, `s`, `pr` ve `d` kısaltmalarını sürekli zihninde çevirmek zorundadır. İki iç içe koşul da akışın hangi dalında bulunduğumuzu hatırlatır.

Aynı işlem, niyeti görünür hâle getirilerek yazılabilir:

```javascript
const purchasableProducts = products.filter(
  product => product.isActive && product.stockCount > 0
);

const discountedTotal = purchasableProducts.reduce(
  (total, product) => total + product.price * (1 - product.discountRate),
  0
);
```

Burada ara değişken yalnızca veri saklamaz; zihinsel bir **parça**, yani anlamlı bir bütün oluşturur. Okur, ayrıntıları tek tek taşımak yerine “satın alınabilir ürünler” kavramını hatırlar.

| Özellik | Yüksek bilişsel yük | Düşük bilişsel yük |
|---|---|---|
| Değişken adları | `x`, `tmp`, `d` | `discountRate`, `totalPrice` |
| Kontrol akışı | Derin iç içe koşullar | Erken dönüşler |
| Soyutlama | Gizli iş kuralları | Niyeti anlatan fonksiyonlar |
| Fonksiyon boyutu | Birçok sorumluluk | Tek ve belirgin görev |
| Durum değişimi | Dağınık mutasyon | Sınırlı, görünür değişim |

## Erken dönüş neden rahatlatır?

İç içe koşullar, açık kalan zihinsel parantezlere benzer. Her seviye çalışan bellekte tutulur:

```python
def ship_order(order):
    if order is None:
        return 'Sipariş bulunamadı'
    if not order.is_paid:
        return 'Ödeme bekleniyor'
    if not order.items:
        return 'Sepet boş'

    create_shipment(order)
    return 'Kargo oluşturuldu'
```

Bu **guard clause** yaklaşımı, geçersiz durumları erkenden eleyerek ana senaryoyu düz bir çizgide bırakır. Okur, “ilk koşul doğruydu, şimdi ikinci dalın içindeyim” bilgisini taşımak zorunda kalmaz.

## Beyne uygun kod için pratik ilkeler

1. İsimleri kısa değil, anlamı açık olacak şekilde seçin.
2. Bir fonksiyonda tek soyutlama düzeyi kullanın.
3. Karmaşık ifadeleri açıklayıcı ara değişkenlere ayırın.
4. Gizli yan etkileri ve global durum değişimlerini azaltın.
5. Yorumlarla kötü kodu tercüme etmek yerine kodun niyetini görünür yapın.
6. Benzer işlemleri tutarlı kalıplarla yazın.

Okunabilirlik yalnızca estetik değildir; sınırlı bir bilişsel kaynağı yönetme problemidir. İyi kod, okurun hafızasını ayrıntılarla doldurmaz. Ona doğru kavramları, doğru sırada ve sindirilebilir parçalar hâlinde sunar. Kısacası temiz kod, bilgisayardan önce insan beynine yapılan bir optimizasyondur.
