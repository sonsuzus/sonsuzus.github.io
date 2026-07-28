---
layout: post
title: "JavaScript’te this Anahtar Kelimesi: Bağlamı Çağrı Anında Çözmek"
math: true
categories: 
  - Bilgi
tags: 
  - JavaScript
  - this
  - fonksiyonlar
---

JavaScript’te `this`, ilk bakışta “fonksiyonun sahibi” gibi görünür; ancak gerçekte değeri fonksiyonun nerede tanımlandığından çok **nasıl çağrıldığına** bağlıdır. Aynı fonksiyon bir çağrıda kullanıcı nesnesini, başka bir çağrıda global nesneyi, hatta `undefined` değerini gösterebilir. Bu yüzden `this`, değişmez bir adres etiketi değil, çalışma zamanında çözülen dinamik bir bağlam referansıdır.

``

## Zihinsel Model: Fonksiyon Değil, Çağrı Önemlidir

Normal fonksiyonlarda JavaScript motoru kabaca şu ilişkiyi değerlendirir:

$$this = f(çağrı\ biçimi, strict\ mode, bağlama\ yöntemi)$$

Buradaki kritik fikir şudur: `this` değerini anlamak için fonksiyon tanımına bakmak yetmez; çağrının sol tarafını ve kullanılan operatörü incelemek gerekir. “Bu fonksiyon nerede yazıldı?” yerine “Bu fonksiyon şu anda nasıl çalıştırıldı?” sorusu daha yararlıdır.

| Çağrı biçimi | `this` değeri | Örnek |
|---|---|---|
| `nesne.metot()` | Noktanın solundaki nesne | `kullanici.selamla()` |
| Bağımsız `fonksiyon()` | Strict modda `undefined` | `selamla()` |
| `call` veya `apply` | Açıkça verilen nesne | `selamla.call(kullanici)` |
| `new Fonksiyon()` | Yeni oluşturulan nesne | `new Kullanici()` |
| Ok fonksiyonu | Dış sözcüksel kapsamın `this` değeri | `() => this.deger` |

## Metot Çağrısı ve Bağlamın Kaybolması

Bir fonksiyon nesnenin özelliği üzerinden çağrıldığında `this`, o nesneyi gösterir:

```javascript
const kullanici = {
  ad: 'Ada',
  tanit() {
    console.log(`Merhaba, ben ${this.ad}`);
  }
};

kullanici.tanit(); // Merhaba, ben Ada
```

Fakat fonksiyonu değişkene aktarmak, nesneyle olan çağrı ilişkisini koparır:

```javascript
'use strict';

const tanit = kullanici.tanit;
tanit(); // TypeError: this, undefined olduğu için
```

Fonksiyon hâlâ aynıdır; değişen şey çağrı biçimidir. İlk örnekte çağrı noktası `kullanici.tanit()`, ikincisinde yalnızca `tanit()` şeklindedir. JavaScript dedektifliğinin büyüteci tam olarak burada kullanılmalıdır.

## call, apply ve bind ile Kontrolü Ele Almak

`call` ve `apply`, fonksiyonu seçilen bağlamla hemen çalıştırır. Aralarındaki fark argümanların aktarılma şeklidir. `bind` ise yeni ve kalıcı olarak bağlanmış bir fonksiyon üretir.

```javascript
function bilgiVer(sehir, rol) {
  return `${this.ad}, ${sehir} şehrinde ${rol} olarak çalışıyor.`;
}

const kisi = { ad: 'Linus' };

console.log(bilgiVer.call(kisi, 'Helsinki', 'geliştirici'));
console.log(bilgiVer.apply(kisi, ['Helsinki', 'geliştirici']));

const bagliBilgi = bilgiVer.bind(kisi);
console.log(bagliBilgi('Helsinki', 'geliştirici'));
```

| Yöntem | Hemen çalıştırır mı? | Argüman biçimi | Sonuç |
|---|---:|---|---|
| `call` | Evet | Ayrı ayrı | Fonksiyonun dönüş değeri |
| `apply` | Evet | Dizi | Fonksiyonun dönüş değeri |
| `bind` | Hayır | Ayrı ayrı | Yeni fonksiyon |

## Ok Fonksiyonlarının Farkı

Ok fonksiyonları kendi `this` bağlamlarını üretmez. Bunun yerine yazıldıkları dış kapsamın `this` değerini sözcüksel olarak devralırlar. Bu davranış zamanlayıcılarda oldukça kullanışlıdır:

```javascript
const sayac = {
  deger: 0,
  baslat() {
    setInterval(() => {
      this.deger++;
      console.log(this.deger);
    }, 1000);
  }
};
```

Buradaki ok fonksiyonu, `baslat` metodunun `this` değerini korur. Aynı yerde normal fonksiyon kullanılsaydı bağlam çağrı mekanizmasına göre yeniden belirlenirdi. Buna karşılık nesne metotlarını gelişigüzel ok fonksiyonu olarak yazmak tehlikelidir; çünkü ok fonksiyonu nesneyi otomatik olarak `this` yapmaz.

## new ile Yeni Bağlam

Bir fonksiyon `new` ile çağrıldığında JavaScript yeni bir nesne oluşturur, bu nesneyi `this` olarak bağlar ve prototip bağlantısını kurar:

```javascript
function Arac(marka) {
  this.marka = marka;
}

const arac = new Arac('Volvo');
console.log(arac.marka);
```

Özet çözüm sırası şöyledir: Önce `new` kullanımını, sonra `bind`, `call` veya `apply` bağlamasını, ardından metot çağrısını kontrol edin. Hiçbiri yoksa strict mod durumuna bakın. Ok fonksiyonunda ise çağrı biçimini değil, dış kapsamı inceleyin. Böylece `this`, gizemli bir JavaScript büyüsü olmaktan çıkıp kuralları olan bir bağlam sistemi hâline gelir.
