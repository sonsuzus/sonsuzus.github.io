---
layout: post
title: "ES6 Sınıfları: JavaScript’in Prototiplerine Takım Elbise Giydirmek"
math: true
categories: 
  - Bilgi
tags: 
  - JavaScript
  - ES6
  - Nesne Yönelimli Programlama
---

JavaScript’te `class` anahtar sözcüğünü gördüğünüzde dilin prototipleri bırakıp C++ veya Java gibi tamamen sınıf tabanlı bir modele geçtiğini düşünebilirsiniz. Fakat perde arkasında hâlâ prototip zinciri çalışır. ES6 sınıfları, mevcut sistemi değiştiren yeni bir nesne modeli değil; yapıcıları, metotları ve kalıtımı daha okunabilir biçimde tanımlayan modern bir sözdizimidir.
``

## Nesne yönelimli düşüncenin temeli

Nesne yönelimli programlama, ilişkili **durum** ve **davranışları** aynı yapı içinde toplar. Örneğin bir banka hesabının bakiyesi durum, para yatırma işlemi ise davranıştır. Bunu kabaca şu şekilde ifade edebiliriz:

$$Nesne = Durum + Davranış$$

JavaScript’te nesneler başka bir nesneyi prototip olarak kullanabilir. Bir özellik nesnenin kendisinde bulunamazsa motor, prototip zincirinde yukarı doğru arama yapar. Zincirin derinliği $d$ ise en kötü durumdaki aramayı basitleştirilmiş biçimde $T(d)=O(d)$ olarak gösterebiliriz.

ES6 öncesinde yapıcı fonksiyon ve `prototype` kullanmak yaygındı:

```javascript
function Kullanici(ad, puan) {
  this.ad = ad;
  this.puan = puan;
}

Kullanici.prototype.selamla = function () {
  return `Merhaba, ben ${this.ad}!`;
};
```

Bu kod geçerlidir; ancak yapıcı ile prototip metotları farklı yerlerde tanımlandığı için yapı büyüdükçe takip edilmesi zorlaşabilir.

## Class ve constructor kullanımı

Aynı modeli ES6 sınıf sözdizimiyle daha toplu yazabiliriz:

```javascript
class Kullanici {
  constructor(ad, puan = 0) {
    this.ad = ad;
    this.puan = puan;
  }

  selamla() {
    return `Merhaba, ben ${this.ad}!`;
  }

  puanEkle(miktar) {
    this.puan += miktar;
  }
}

const ada = new Kullanici("Ada", 10);
ada.puanEkle(5);
console.log(ada.puan); // 15
```

`constructor`, `new` ile nesne oluşturulduğunda otomatik çalışan özel metottur. Başlangıç değerlerini nesneye yerleştirir. Sınıf gövdesindeki normal metotlar her nesne için yeniden kopyalanmaz; sınıfın `prototype` nesnesine eklenerek örnekler arasında paylaşılır.

| Özellik | Yapıcı fonksiyon | ES6 sınıfı |
|---|---|---|
| Tanımlama | `function` kullanır | `class` kullanır |
| Başlatma | Fonksiyon gövdesinde | `constructor` içinde |
| Metotlar | `prototype` üzerine eklenir | Sınıf gövdesinde yazılır |
| Kalıtım | Elle prototip bağlantısı gerekir | `extends` ve `super` kullanılır |
| Okunabilirlik | Dağınık hâle gelebilir | Daha düzenli ve tanıdıktır |

## Kalıtım: extends ve super

Bir sınıfın davranışlarını genişletmek için `extends` kullanılır. Alt sınıfın yapıcısında `this` kullanılmadan önce `super()` çağrılmalıdır; çünkü önce üst sınıfın nesne kurulumunu tamamlaması gerekir.

```javascript
class Yonetici extends Kullanici {
  constructor(ad, puan, yetki) {
    super(ad, puan);
    this.yetki = yetki;
  }

  selamla() {
    return `${super.selamla()} Yetkim: ${this.yetki}`;
  }
}

const linus = new Yonetici("Linus", 100, "sistem");
console.log(linus.selamla());
```

Burada `Yonetici.prototype`, dolaylı olarak `Kullanici.prototype` nesnesine bağlanır. Dolayısıyla kalıtımın motoru yine prototip zinciridir; `extends` yalnızca bu bağlantıyı güvenli ve anlaşılır biçimde kurar.

## Küçük ama önemli ayrıntılar

Sınıflar otomatik olarak strict mode içinde çalışır. Ayrıca sınıf bildirimi, fonksiyon bildiriminin aksine tanımlanmadan önce güvenle kullanılamaz. `static` ile yazılan metotlar örneklere değil doğrudan sınıfa aittir:

```javascript
class MatematikAraci {
  static ikiKat(sayi) {
    return sayi * 2;
  }
}

console.log(MatematikAraci.ikiKat(6)); // 12
```

Sonuç olarak ES6 sınıfları JavaScript’i klasik sınıf tabanlı bir dile dönüştürmez. Prototip modeline daha tanıdık, düzenli ve bakımı kolay bir arayüz sunar. Sihir yoktur; yalnızca prototiplerin üzerine giydirilmiş oldukça şık bir takım elbise vardır.
