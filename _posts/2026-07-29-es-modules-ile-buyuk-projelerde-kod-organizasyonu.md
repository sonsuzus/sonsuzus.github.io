---
layout: post
title: "ES Modules ile Büyük Projelerde Kod Organizasyonu"
math: true
categories: 
  - Bilgi
tags: 
  - JavaScript
  - ES Modules
  - Kod Organizasyonu
---

Bir JavaScript projesi büyüdükçe tek dosyada yaşayan kod, çekmecesine ne bulursa atan bir geliştiricinin odasına dönüşebilir. Değişkenler çakışır, fonksiyonların nerede kullanıldığı belirsizleşir ve küçük bir değişiklik beklenmedik yerleri bozar. ES Modules, kodu anlamlı dosyalara bölerek bu karmaşayı yönetmemizi ve dosyalar arasındaki bağı açıkça tanımlamamızı sağlar.

``

## Modül Nedir?

Modül, belirli bir sorumluluğu yerine getiren ve kendi kapsamına sahip JavaScript dosyasıdır. Örneğin kullanıcı işlemleri `user.js`, matematik yardımcıları `math.js`, API iletişimi ise `api.js` içerisinde tutulabilir. Her dosya yalnızca dışarı açmak istediği değerleri `export` eder; başka dosyalar da bu değerleri `import` ile kullanır.

Bu yaklaşımın temelinde **kapsülleme** bulunur. Bir modülün içindeki değişkenler varsayılan olarak diğer modüllerin global alanına sızmaz. Böylece iki farklı dosyada `result` adında değişken bulunması sorun yaratmaz.

Kod karmaşıklığını kabaca şu şekilde düşünebiliriz: Dosya sayısı $n$ ve her dosyanın ortalama sorumluluk sayısı $s$ olsun. Tek dosyalı yapıda zihinsel yük yaklaşık $n \times s$ iken iyi ayrıştırılmış modüllerde geliştirici çoğunlukla yalnızca ilgili modülün $s$ sorumluluğuna odaklanır. Elbette bu matematiksel bir performans ölçümü değil, modülerliğin bilişsel faydasını anlatan basit bir modeldir.

## Named Export ve Default Export

ES Modules iki temel dışa aktarma yöntemi sunar:

| Özellik | Named Export | Default Export |
|---|---|---|
| Dosyadaki sayı | Birden fazla olabilir | Yalnızca bir tane olabilir |
| İçe aktarma adı | Aynı ad kullanılmalıdır | İstenilen ad verilebilir |
| Kullanım amacı | Yardımcı fonksiyonlar, sabitler | Modülün ana değeri |
| Yeniden adlandırma | `as` ile yapılır | Doğrudan yapılabilir |

Named export kullanan bir matematik modülü oluşturalım:

```js
// math.js
export const PI = 3.14159;

export function circleArea(radius) {
  return PI * radius ** 2;
}

function validateRadius(radius) {
  return radius >= 0;
}
```

Burada `PI` ve `circleArea` dışarı açılmıştır. `validateRadius` ise modülün özel uygulama detayı olarak kalır. İhtiyacımız olan değerleri başka bir dosyada seçerek alabiliriz:

```js
// app.js
import { circleArea, PI as circlePI } from "./math.js";

console.log(circleArea(5));
console.log(circlePI);
```

`as` anahtar kelimesi, içe aktarılan değerin yerel adını değiştirir. Böylece isim çakışmaları kontrollü biçimde çözülür.

Bir modül tek bir ana sınıf veya fonksiyon sunuyorsa default export tercih edilebilir:

```js
// UserService.js
export default class UserService {
  async getUser(id) {
    const response = await fetch(`/api/users/${id}`);
    return response.json();
  }
}
```

Bu sınıf `import UserService from "./UserService.js";` şeklinde alınabilir. Süslü parantez kullanılmaması, default import için önemli bir ayrıntıdır.

## Tarayıcıda ve Node.js'te Kullanım

Tarayıcıya bir dosyanın modül olduğunu söylemek için `type="module"` eklenir:

```html
<script type="module" src="./app.js"></script>
```

Modül betikleri otomatik olarak strict mode ile çalışır ve varsayılan olarak ertelenir. Node.js tarafında ise `package.json` dosyasına `"type": "module"` eklenebilir. Dosya yollarında uzantı kullanmak, ortamlar arası davranışı daha öngörülebilir hâle getirir.

## Dinamik Import ve Performans

Her modülü başlangıçta yüklemek zorunda değiliz. `import()` fonksiyonu bir Promise döndürerek kodun ihtiyaç anında indirilmesini sağlar:

```js
button.addEventListener("click", async () => {
  const { openEditor } = await import("./editor.js");
  openEditor();
});
```

Bu yöntem özellikle yönetim paneli, grafik editörü veya raporlama ekranı gibi ağır özelliklerde kullanışlıdır. Paketleyiciler ayrıca kullanılmayan named export'ları **tree shaking** ile üretim paketinden çıkarabilir.

## Sağlıklı Bir Modül Yapısı İçin İpuçları

Modülleri dosya boyutuna göre değil, sorumluluğa göre ayırın. Dairesel bağımlılıklardan kaçının; `a.js`, `b.js` dosyasını, `b.js` de tekrar `a.js` dosyasını içe aktarıyorsa mimariyi gözden geçirin. Ortak davranışları bağımsız bir yardımcı modüle taşımak genellikle çözüm olur.

Sonuç olarak ES Modules yalnızca dosya bölme yöntemi değildir. Açık bağımlılıklar, izole kapsam, yeniden kullanılabilirlik ve daha kolay test edilebilirlik sunan bir tasarım aracıdır. İyi organize edilmiş modüller sayesinde proje büyürken kod tabanı korkutucu bir labirente değil, tabelaları düzgün yerleştirilmiş bir şehre dönüşür.
