---
layout: post
title: "JavaScript Prototipleri: Nesnelerin Birbirinden Miras Aldığı Dünya"
math: true
categories: 
  - Bilgi
tags: 
  - JavaScript
  - Prototipler
  - Kalıtım
---

JavaScript’te bir nesne kayıp bir özelliğini nerede arar? Cevap, klasik sınıf tabanlı dillerden biraz farklıdır: başka bir nesnede! JavaScript’in prototip tabanlı kalıtım sistemi, nesnelerin davranış ve özellikleri doğrudan diğer nesnelerden devralmasını sağlar. İlk bakışta gizemli görünen bu mekanizma; nesne metotlarından `class` sözdizimine kadar dilin önemli bir bölümünün perde arkasında çalışır.
``
## Prototip nedir?

Her sıradan JavaScript nesnesi, başka bir nesneye işaret eden dahili bir `[[Prototype]]` bağlantısına sahip olabilir. Bir özelliğe erişildiğinde JavaScript önce nesnenin kendi özelliklerine bakar. Özellik bulunamazsa prototipe, orada da bulunamazsa prototipin prototipine geçer. Bu yolculuk `null` değerine ulaşınca sona erer.

Bu bağlantılı yapı **prototip zinciri** olarak adlandırılır. Arama sürecini basitleştirerek şöyle gösterebiliriz:

$$nesne \rightarrow prototip_1 \rightarrow prototip_2 \rightarrow null$$

Zincirin uzunluğu $n$ ise en kötü durumdaki özellik arama maliyeti yaklaşık $O(n)$ olur. Modern JavaScript motorları çeşitli optimizasyonlar uygulasa da gereksiz derecede uzun zincirler tasarlamak iyi bir fikir değildir.

```javascript
const canli = {
  nefesAl() {
    return "Nefes alındı!";
  }
};

const kedi = Object.create(canli);
kedi.isim = "Tekir";
kedi.miyavla = function () {
  return "Miyav!";
};

console.log(kedi.isim);       // Kendi özelliği: Tekir
console.log(kedi.nefesAl());  // Prototipten gelir
```

Burada `Object.create(canli)`, prototipi `canli` olan yeni bir nesne üretir. `kedi` içinde `nefesAl` bulunmadığı için motor, aramaya `canli` nesnesinde devam eder.

## Sınıf tabanlı ve prototip tabanlı yaklaşım

| Özellik | Sınıf tabanlı model | JavaScript prototip modeli |
|---|---|---|
| Temel yapı | Sınıf | Nesne |
| Kalıtım | Sınıftan sınıfa | Nesneden nesneye |
| Örnek üretimi | Sınıf örneklenir | Nesne oluşturulur ve prototipe bağlanır |
| Davranış paylaşımı | Üst sınıf metotları | Prototip zincirindeki metotlar |
| Değişiklik esnekliği | Genellikle daha katı | Çalışma zamanında oldukça dinamik |

JavaScript’teki `class` sözdizimi bu modeli ortadan kaldırmaz. Yalnızca prototip mekanizmasını daha tanıdık ve okunabilir biçimde kullanmamızı sağlayan bir sözdizimsel kolaylıktır.

```javascript
class Hayvan {
  constructor(isim) {
    this.isim = isim;
  }

  tanit() {
    return `Ben ${this.isim}`;
  }
}

class Kopek extends Hayvan {
  havla() {
    return "Hav hav!";
  }
}

const karabas = new Kopek("Karabaş");
console.log(karabas.tanit());
```

Bu örnekte `tanit`, her nesneye ayrı ayrı kopyalanmaz. Metot `Hayvan.prototype` üzerinde tutulur ve örnekler tarafından paylaşılır. Kabaca bellek kullanımı, metodu her örneğe kopyalayan bir yaklaşımda $n \times m$ iken prototip paylaşımında $m + n \times r$ biçiminde düşünülebilir. Burada $m$ metot boyutunu, $r$ ise her örneğin kendi verisini temsil eder.

## `prototype` ile `[[Prototype]]` aynı şey mi?

Hayır; isim benzerliği sıkça kafa karıştırır. Fonksiyonların `prototype` özelliği, o fonksiyon `new` ile çağrıldığında oluşturulacak nesnelerin prototipini belirler. `[[Prototype]]` ise bir nesnenin başka bir nesneye olan dahili bağlantısıdır.

```javascript
function Kullanici(ad) {
  this.ad = ad;
}

Kullanici.prototype.selamla = function () {
  return `Merhaba, ben ${this.ad}`;
};

const ada = new Kullanici("Ada");

console.log(Object.getPrototypeOf(ada) === Kullanici.prototype); // true
console.log(ada.hasOwnProperty("ad"));       // true
console.log(ada.hasOwnProperty("selamla")); // false
```

Prototipi incelemek için standart `Object.getPrototypeOf()` kullanılmalıdır. Tarihsel `__proto__` erişimi yaygın görünse de yeni kodlarda önerilmez.

## Sağlam kullanım için ipuçları

Bir özelliğin doğrudan nesneye ait olup olmadığını kontrol etmek için `Object.hasOwn(nesne, "özellik")` tercih edilebilir. `for...in` döngüsünün prototipten gelen numaralandırılabilir özellikleri de dolaşabileceği unutulmamalıdır. Ayrıca yerleşik prototiplere, örneğin `Array.prototype` üzerine rastgele metot eklemek çakışmalara ve zor bulunan hatalara yol açabilir.

Özetle JavaScript kalıtımı, görünmez sınıf şablonlarından çok birbirine bağlanan nesneler üzerine kuruludur. Prototip zincirini anladığınızda `new`, `class`, `extends` ve metot paylaşımı sihir olmaktan çıkar; hepsi aynı mekanizmanın farklı yüzleri hâline gelir.
