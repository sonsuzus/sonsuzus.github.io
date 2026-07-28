---
layout: post
title: "Nesneler ve JSON: Gerçek Dünyayı Anahtar-Değerlerle Modellemek"
math: true
categories: 
  - Bilgi
tags: 
  - nesneler
  - JSON
  - veri modelleme
---

Bir kullanıcıyı, otomobili veya kahve makinesini yazılım dünyasına taşımak istediğimizde yalnızca birkaç bağımsız değişken kullanmak kısa sürede karmaşaya yol açar. Nesneler, bir varlığa ait bilgileri anlamlı bir bütün hâlinde toplar. JSON ise bu anahtar-değer düzenini sistemler arasında aktarılabilen standart bir metne dönüştürür.
``
## Nesne nedir?

Nesne, ilişkili verileri ve bazı programlama dillerinde bu veriler üzerinde çalışan davranışları bir arada tutan yapıdır. Örneğin gerçek dünyadaki bir otomobilin markası, hızı ve rengi vardır; ayrıca hızlanabilir veya fren yapabilir. Yazılım modelinde özellikler **anahtar-değer çiftleriyle**, davranışlar ise metotlarla temsil edilebilir.

Matematiksel açıdan basitleştirilmiş bir nesneyi, anahtarlar kümesinden değerlere yapılan bir eşleme gibi düşünebiliriz:

$$O: K \rightarrow V$$

Burada $K$ anahtarlar kümesini, $V$ ise olası değerleri gösterir. Örneğin `renk` anahtarı `kırmızı` değerine eşlenebilir. Bir nesnedeki çiftlerin sayısı $n$ ise yapı kabaca şöyle ifade edilir:

$$O = \{(k_1,v_1),(k_2,v_2),\ldots,(k_n,v_n)\}$$

JavaScript ile basit bir otomobil nesnesi oluşturalım:

```javascript
const otomobil = {
  marka: "Volta",
  renk: "kırmızı",
  hiz: 0,
  elektrikli: true,
  hizlan(miktar) {
    this.hiz += miktar;
  }
};

otomobil.hizlan(30);
console.log(otomobil.hiz); // 30
```

Bu kodda `marka`, `renk`, `hiz` ve `elektrikli` birer özellik; `hizlan` ise nesnenin durumunu değiştiren bir metottur. `this.hiz`, işlemin ilgili otomobil nesnesinin hızına uygulanmasını sağlar. Böylece veri ile davranış aynı model altında buluşur.

## Anahtar-değer yaklaşımının gücü

Düz değişkenler kullansaydık `otomobilMarka`, `otomobilRenk` ve `otomobilHiz` gibi giderek uzayan isimlere ihtiyaç duyardık. Nesne yapısı, bu bilgileri ortak bir bağlamda toplar.

| Yaklaşım | Düzen | Genişletilebilirlik | Kullanım örneği |
|---|---|---|---|
| Bağımsız değişkenler | Dağınık olabilir | Yeni alanlarda zorlaşır | Küçük hesaplamalar |
| Dizi | Sıraya bağlıdır | İndeksleri hatırlatır | Benzer değer listeleri |
| Nesne | Anahtarlarla anlamlıdır | Yeni özellik eklemek kolaydır | Varlık modelleme |

Nesneler iç içe de geçebilir. Bir kullanıcının adresi başka bir nesne, siparişleri ise nesnelerden oluşan bir dizi olabilir. Bu sayede karmaşık ilişkiler, ağaç benzeri bir yapı kazanır.

```javascript
const kullanici = {
  id: 42,
  ad: "Ada",
  adres: {
    sehir: "İzmir",
    postaKodu: "35000"
  },
  roller: ["editor", "yazar"]
};

console.log(kullanici.adres.sehir); // İzmir
```

Nokta gösterimi, iç içe geçmiş verilere okunabilir biçimde erişir. Dinamik bir anahtar kullanılacaksa `kullanici[alanAdi]` biçimindeki köşeli parantez gösterimi tercih edilir.

## JSON ile yapısal bağ

JSON, açılımıyla **JavaScript Object Notation**, nesne benzeri verileri metin olarak temsil eden bağımsız bir veri formatıdır. Bir API’nin sunucudan tarayıcıya kullanıcı bilgisi göndermesi buna tipik örnektir.

```json
{
  "id": 42,
  "ad": "Ada",
  "aktif": true,
  "roller": ["editor", "yazar"],
  "adres": {
    "sehir": "İzmir"
  }
}
```

JSON ile JavaScript nesnesi akrabadır fakat aynı şey değildir:

| Özellik | JavaScript nesnesi | JSON |
|---|---|---|
| Anahtarlar | Tırnaksız olabilir | Çift tırnak zorunludur |
| Metotlar | Bulunabilir | Bulunamaz |
| Yorum satırı | Kullanılabilir | Standartta desteklenmez |
| Amaç | Program içinde çalışmak | Veri saklamak ve aktarmak |
| Veri türleri | Çok geniştir | Metin, sayı, boolean, null, dizi ve nesne |

Bir nesneyi JSON metnine çevirmeye **serileştirme**, JSON metnini yeniden kullanılabilir nesneye dönüştürmeye **ayrıştırma** denir:

```javascript
const jsonMetni = JSON.stringify(kullanici);
const geriDonenNesne = JSON.parse(jsonMetni);

console.log(geriDonenNesne.ad); // Ada
```

Bu dönüşüm sırasında fonksiyonlar ve `undefined` gibi JSON tarafından desteklenmeyen değerler korunmaz. Ayrıca güvenilmeyen bir kaynaktan gelen verinin biçimi mutlaka doğrulanmalıdır; geçerli JSON olması, içeriğinin güvenli veya iş kurallarına uygun olduğu anlamına gelmez.

Sonuç olarak nesneler gerçek dünya varlıklarını anlamlı özelliklerle modeller, anahtar-değer düzeni verilere isim kazandırır, JSON ise bu yapıyı farklı diller ve sistemler arasında taşınabilir hâle getirir. Kısacası nesne sahnedeki oyuncuysa JSON onun seyahat çantasıdır.
