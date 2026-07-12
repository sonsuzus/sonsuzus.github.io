---
layout: post
title: "JavaScript ve NFC Etkileşimi: Web NFC ile Cebe Dokunan Uygulamalar"
math: true
categories: 
  - Program
tags: 
  - JavaScript
  - NFC
  - Web NFC
  - Mobil Web
---

Telefonunuzu bir etikete yaklaştırıp kapıyı açmak, Wi-Fi bilgisini almak ya da bir ürünün bakım geçmişini okumak kulağa biraz sihir gibi gelir; ama aslında sahnede NFC ve JavaScript vardır. Modern Android tarayıcılarında Web NFC API sayesinde web uygulamaları, yakın alan iletişimi sensörleriyle veri okuyup yazabilir. Yani bazen bir buton, bazen de 3 cm mesafe bütün deneyimi değiştirir.
``

NFC, Near Field Communication ifadesinin kısaltmasıdır ve çok kısa mesafede çalışan kablosuz iletişim teknolojisidir. Genellikle $d ≤ 4cm$ gibi yakın bir aralıkta anlamlıdır. Bunun sebebi güvenlik kadar fiziksel çalışma mantığıdır: NFC, radyo dalgasından çok manyetik alan eşleşmesine dayanır. Mesafe arttıkça alan etkisi yaklaşık $P ≈ 1/r^3$ gibi hızlı azalır; yani etiketi masanın öbür ucundan okumaya çalışmak, kedinize SQL öğretmeye benzer: teorik olarak konuşulur, pratikte zordur.

Web NFC tarafında ana karakterimiz `NDEFReader` sınıfıdır. NDEF, NFC Data Exchange Format anlamına gelir. Etiketin içinde metin, URL, MIME verisi veya uygulamaya özel kayıtlar saklanabilir. JavaScript burada donanıma doğrudan hükmetmez; tarayıcı, güvenlik izinleri ve işletim sistemi üzerinden kontrollü bir köprü kurar.

| Özellik | NFC | QR Kod | Bluetooth |
|---|---|---|---|
| Mesafe | Çok kısa | Kamera görüşü kadar | Daha uzun |
| Kullanıcı eylemi | Yaklaştırma | Kamerayla tarama | Eşleştirme gerekebilir |
| Veri yazma | Desteklenir | Basılıysa zordur | Cihaza bağlı |
| Web entegrasyonu | Web NFC ile mümkün | Çok yaygın | Web Bluetooth ile mümkün |

Web NFC kullanırken üç önemli koşul vardır: HTTPS üzerinde çalışmak, kullanıcıdan izin almak ve destekleyen bir tarayıcı kullanmak. Masaüstünde veya iOS Safari tarafında destek sınırlı olabilir. Bu yüzden üretim uygulamalarında özellik kontrolü yapmak şarttır.

```js
if ('NDEFReader' in window) {
  console.log('Bu cihaz Web NFC destekliyor.');
} else {
  console.log('NFC desteklenmiyor, alternatif akış göster.');
}
```

Bu küçük kontrol, uygulamanın panik butonudur. Destek yoksa kullanıcıya QR kod, manuel kod girişi veya Bluetooth gibi alternatifler sunabilirsiniz. İyi kullanıcı deneyimi, sadece çalışan cihazı değil, çalışmayan senaryoyu da düşünür.

Bir NFC etiketi okumak için `scan()` metodu kullanılır. Tarayıcı izin penceresi gösterebilir ve kullanıcı cihazını etikete yaklaştırdığında `reading` olayı tetiklenir.

```js
const reader = new NDEFReader();

async function startScan() {
  try {
    await reader.scan();
    console.log('NFC tarama başladı.');

    reader.addEventListener('reading', event => {
      const decoder = new TextDecoder();

      for (const record of event.message.records) {
        if (record.recordType === 'text') {
          console.log('Okunan metin:', decoder.decode(record.data));
        }
      }
    });
  } catch (error) {
    console.error('Tarama hatası:', error);
  }
}
```

Burada kodun yaptığı iş basit ama güçlüdür: okuyucu başlatılır, etiket algılanınca mesaj kayıtları dolaşılır ve metin verisi çözümlenir. NFC verisi ham baytlar halinde geldiği için `TextDecoder` kullanmak gerekir. Bu noktada JavaScript, küçük bir tercüman gibi davranır.

Yazma işlemi de benzer şekilde yapılır. Örneğin bir müze uygulaması, sergi salonundaki NFC etiketine eser kimliği yazabilir.

```js
async function writeTag() {
  const writer = new NDEFReader();

  try {
    await writer.write({
      records: [
        {
          recordType: 'text',
          data: 'eser:van-gogh-1889'
        }
      ]
    });

    console.log('Etikete veri yazıldı.');
  } catch (error) {
    console.error('Yazma başarısız:', error);
  }
}
```

Elbette her etikete sonsuz veri yazamayız. NFC etiketlerinin kapasitesi sınırlıdır; bazıları 144 bayt, bazıları birkaç kilobayt veri tutar. Bu nedenle etikete genellikle tüm veriyi değil, veritabanındaki kaydı temsil eden kısa bir anahtar yazılır. Yani etiket depo değil, kapı numarasıdır.

| Senaryo | Etikete Yazılacak Veri | Sunucuda Tutulacak Veri |
|---|---|---|
| Ürün takibi | `urun:3482` | Stok, tarihçe, bakım |
| Müze rehberi | `eser:12` | Sesli anlatım, görsel |
| Etkinlik girişi | `bilet:abc91` | Kullanıcı, yetki, süre |

Güvenlik tarafında en kritik ilke şudur: NFC’den gelen veriye asla körü körüne güvenmeyin. Etiket kopyalanabilir, değiştirilebilir veya kötü niyetli URL içerebilir. Okunan değerler sunucuda doğrulanmalı, hassas işlemler için kullanıcı oturumu ve yetki kontrolü yapılmalıdır. Matematiksel olarak düşünürsek, güvenlik sadece $veri + cihaz$ değil; $veri + cihaz + kullanıcı + sunucu doğrulaması$ birleşimidir.

Sonuç olarak Web NFC, mobil web uygulamalarına fiziksel dünya ile tatlı bir tokalaşma imkânı verir. Depo yönetimi, akıllı kartvizitler, müze deneyimleri, eğitim materyalleri ve hızlı yapılandırma ekranları için oldukça kullanışlıdır. Yeter ki tarayıcı desteğini kontrol edin, kullanıcı iznini saygıyla isteyin ve NFC etiketlerini minik ama güçlü anahtarlar gibi tasarlayın.
