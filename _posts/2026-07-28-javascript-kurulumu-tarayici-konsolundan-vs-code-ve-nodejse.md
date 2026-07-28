---
layout: post
title: "JavaScript Kurulumu: Tarayıcı Konsolundan VS Code ve Node.js’e"
math: true
categories: 
  - Bilgi
tags: 
  - JavaScript
  - Node.js
  - VS Code
---

JavaScript öğrenmeye başlamak için devasa bir kurulum sihrine ihtiyacınız yoktur; modern bir tarayıcı bile ilk programınızı çalıştırmaya yeter. Ancak gerçek projeler geliştirmek istediğinizde tarayıcı konsolu, Node.js, VS Code ve canlı sunucu araçlarından oluşan düzenli bir çalışma ortamı kurmak büyük rahatlık sağlar. Gelin JavaScript atölyemizin ışıklarını birlikte açalım.
``
## JavaScript nerede çalışır?

JavaScript kodunu çalıştıran temel bileşene **JavaScript motoru** denir. Google Chrome ve Node.js, V8 motorunu kullanır. Firefox ise SpiderMonkey adlı farklı bir motora sahiptir. Motor, yazdığımız kaynak kodunu bilgisayarın işleyebileceği komutlara dönüştürür.

Bir programın yaklaşık çalışma süresini teorik olarak şöyle düşünebiliriz:

$$T_{toplam} = T_{ayrıştırma} + T_{derleme} + T_{çalıştırma}$$

Modern motorlar, sık kullanılan kodları çalışma sırasında optimize eden **JIT (Just-in-Time)** derleme yöntemlerinden yararlanır. Dolayısıyla JavaScript yalnızca “satır satır okunan basit bir betik dili” değildir.

| Ortam | Temel kullanım | Tarayıcı API’leri | Dosya sistemi erişimi |
|---|---|---:|---:|
| Tarayıcı konsolu | Deneme ve hata ayıklama | Var | Kısıtlı |
| HTML içindeki JavaScript | Web arayüzleri | Var | Kısıtlı |
| Node.js | Sunucu ve komut satırı uygulamaları | Yok | Var |

## Tarayıcı konsoluyla ilk buluşma

Chrome, Edge veya Firefox’ta `F12` tuşuna basarak geliştirici araçlarını açın ve **Console** sekmesine geçin. Burada herhangi bir dosya oluşturmadan JavaScript çalıştırabilirsiniz:

```javascript
const ad = 'Ada';
const dersSayisi = 3;

console.log(`Merhaba ${ad}! Bugün ${dersSayisi} ders var.`);
console.table({ ad, dersSayisi });
```

`console.log` değerleri görüntülerken `console.table`, nesneleri tablo biçiminde sunar. Konsol hızlı deneyler için harikadır; fakat yazdığınız komutlar kalıcı bir proje düzeni oluşturmaz.

## Node.js kurulumu

Node.js, JavaScript’i tarayıcı dışında çalıştıran bir çalışma zamanıdır. Resmî Node.js sitesinden **LTS** sürümünü indirin. LTS, uzun süre desteklenen ve yeni başlayanlar için daha güvenli olan sürümdür. Kurulumla birlikte paket yöneticisi **npm** de gelir.

Terminalde kurulumu doğrulayın:

```bash
node --version
npm --version
```

Ardından `merhaba.js` adlı bir dosya oluşturup şu kodu yazın:

```javascript
const sayilar = [4, 8, 15, 16, 23, 42];
const toplam = sayilar.reduce((sonuc, sayi) => sonuc + sayi, 0);

console.log('Toplam:', toplam);
```

Dosyayı terminalden `node merhaba.js` komutuyla çalıştırabilirsiniz. Buradaki toplam işleminin matematiksel gösterimi şöyledir:

$$S = \sum_{i=1}^{n} x_i$$

## VS Code’u hazırlamak

VS Code’u kurduktan sonra bir proje klasörü açın. Daha konforlu kod yazmak için şu eklentiler yararlıdır:

| Eklenti | Görevi |
|---|---|
| ESLint | Olası kod hatalarını ve kurallara aykırılıkları gösterir |
| Prettier | Kod biçimini otomatik olarak düzenler |
| Live Server | HTML dosyasını yerel sunucuda açar ve yeniler |
| Error Lens | Hataları editör içinde görünür hâle getirir |

Prettier kurulduktan sonra ayarlardan **Format On Save** seçeneğini etkinleştirebilirsiniz. Böylece dosyayı her kaydettiğinizde girintiler ve boşluklar otomatik düzeltilir.

## Canlı sunucuyla küçük proje

Proje klasöründe `index.html` ve `app.js` dosyaları oluşturun. HTML dosyanızın kapanış `body` etiketinden önce JavaScript’i bağlayın:

```html
<button id="dugme">Tıkla</button>
<script src="app.js"></script>
```

`app.js` içinde düğmeye davranış kazandırın:

```javascript
const dugme = document.querySelector('#dugme');
let sayac = 0;

dugme.addEventListener('click', () => {
  sayac += 1;
  dugme.textContent = `${sayac} kez tıklandı`;
});
```

`index.html` dosyasına sağ tıklayıp **Open with Live Server** seçeneğini kullanın. Sayfa genellikle `localhost:5500` adresinde açılır ve kaydettiğiniz değişiklikler otomatik yenilenir. Artık konsol deneylerinden dosya tabanlı projelere geçmeye hazırsınız: tarayıcı arayüzü yönetir, Node.js araçları çalıştırır, VS Code ise tüm ekibi aynı masada buluşturur.
