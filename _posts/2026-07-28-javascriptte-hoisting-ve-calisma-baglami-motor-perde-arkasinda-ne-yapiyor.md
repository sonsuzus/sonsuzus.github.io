---
layout: post
title: "JavaScript’te Hoisting ve Çalışma Bağlamı: Motor Perde Arkasında Ne Yapıyor?"
math: true
categories: 
  - Bilgi
tags: 
  - JavaScript
  - Hoisting
  - Execution Context
---

JavaScript kodu satır satır çalışan basit bir tarif gibi görünür; ancak motor, ilk satırı yürütmeden önce mutfağı çoktan düzenlemiştir. Değişken ve fonksiyon bildirimleri için bellek ayırır, kapsamları oluşturur ve erişim kurallarını belirler. **Hoisting** adı verilen davranış, bildirimlerin gerçekten kaynak kodun başına taşınması değil, çalışma bağlamının hazırlanma aşamasında belleğe kaydedilmesidir. Bu ayrım bilinmediğinde kod, küçük bir sihir gösterisinden hızla hata avına dönüşebilir.

``

## Çalışma bağlamının iki aşaması

JavaScript motoru global kodu veya bir fonksiyonu çalıştırırken bir **execution context**, yani çalışma bağlamı oluşturur. Bu süreç kavramsal olarak iki aşamada incelenebilir:

1. **Oluşturma aşaması:** Değişkenler, fonksiyonlar, kapsam zinciri ve `this` için gerekli kayıtlar hazırlanır.
2. **Yürütme aşaması:** İfadeler kaynak kodundaki sıraya göre değerlendirilir ve atamalar gerçekleştirilir.

Bunu basitçe şöyle gösterebiliriz:

$$Çalışma\ Bağlamı = Bellek\ Hazırlığı + Kodun\ Yürütülmesi$$

Hoisting ilk bölümün sonucudur. Motor, `var` bildirimlerini `undefined` ile başlatırken fonksiyon bildirimlerini gövdeleriyle birlikte belleğe koyar. `let` ve `const` için de kayıt açılır; fakat bildirim satırına ulaşılıncaya kadar bu kayıtlara erişilemez.

| Bildirim türü | Oluşturma aşamasındaki durum | Bildirimden önce erişim | Yeniden atanabilir mi? |
|---|---|---|---|
| `var` | `undefined` ile başlatılır | Evet, sonuç `undefined` | Evet |
| `let` | Başlatılmamış kayıt | Hayır, `ReferenceError` | Evet |
| `const` | Başlatılmamış kayıt | Hayır, `ReferenceError` | Hayır |
| Function declaration | Fonksiyon gövdesiyle hazırdır | Evet | İlgili bağlama göre |

## `var`: Sessiz ama tehlikeli

Aşağıdaki kod hata üretmez; bu durum her zaman iyi haber değildir:

```javascript
console.log(toplam); // undefined
var toplam = 42;
console.log(toplam); // 42
```

Motorun davranışı kabaca şu modele benzer:

```javascript
var toplam;
console.log(toplam);
toplam = 42;
console.log(toplam);
```

İlk çıktı `undefined` olduğu için sonraki bir hesaplama sessizce bozulabilir. Örneğin `undefined + 10` işleminin sonucu `NaN` olur. Böylece hata oluştuğu satır ile problemin fark edildiği satır birbirinden uzaklaşır.

$$undefined + 10 = NaN$$

`var` ayrıca blok kapsamına sahip değildir. Bir `if` veya `for` bloğunda tanımlansa bile içinde bulunduğu fonksiyonun tamamında görülebilir. Bu özellik, değişkenlerin beklenmedik biçimde ezilmesine yol açabilir.

## Temporal Dead Zone koruması

`let` ve `const`, kapsamın başlangıcı ile bildirim satırı arasındaki **Temporal Dead Zone** bölgesinde bulunur:

```javascript
console.log(kullanici); // ReferenceError
let kullanici = "Ada";
```

Buradaki hata bir eksiklik değil, koruma mekanizmasıdır. Motor, henüz anlamlı bir değer kazanmamış değişkenin kullanılmasını engeller. Böylece problem erken ve açık biçimde görünür.

## Fonksiyonlarda hoisting farkı

Fonksiyon bildirimi ile fonksiyon ifadesi aynı şekilde hazırlanmaz:

```javascript
selamla(); // Çalışır

function selamla() {
  console.log("Merhaba!");
}

hesapla(); // ReferenceError
const hesapla = function () {
  return 2 + 2;
};
```

İlk fonksiyon oluşturma aşamasında bütünüyle belleğe alınır. İkinci örnekte ise hoisting kuralları `hesapla` değişkenine uygulanır; fonksiyon değeri ancak atama satırında oluşturulur.

## Çalışma bağlamları ve kapsam zinciri

Her fonksiyon çağrısı yeni bir çalışma bağlamı üretir ve çağrı yığınına eklenir. Bir değişken yerel bağlamda bulunamazsa motor dış kapsamlara doğru ilerler. Arama maliyetini kavramsal olarak kapsam derinliği $d$ ile ilişkilendirirsek, en kötü durumda yaklaşık $O(d)$ karşılaştırma düşünülebilir. Modern motorlar bunu yoğun biçimde optimize etse de derin ve karmaşık kapsamlar okunabilirliği azaltır.

Hoisting kaynaklı yan etkileri azaltmak için `var` yerine `let` veya `const` tercih edilmeli, değişkenler kullanılacakları yere yakın tanımlanmalı ve fonksiyon bildirimi ile fonksiyon ifadesi arasındaki fark bilinmelidir. Hoisting’i “kod yukarı taşınıyor” diye değil, “motor yürütmeden önce bağlam hazırlıyor” şeklinde düşünmek, JavaScript’in sürprizlerini anlaşılır kurallara dönüştürür.
