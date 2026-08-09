---
layout: post
title: "Dosya İşlemleri ve Stream Mantığı: Veriyi Akışta Yönetmek"
math: true
categories: 
  - Bilgi
tags: 
  - dosya işlemleri
  - stream
  - binary
  - Node.js
  - veri akışları
---

Dosyalar, programların dış dünyayla kurduğu en kalıcı iletişim kanallarındandır. Bir günlük kaydı, CSV raporu, görsel ya da video; belleğe bir anda sığabilecek küçük bir metin de olabilir, gigabaytlarca süren ikili veri de. İşte stream (akış) yaklaşımı, verinin tamamını RAM'e yüklemek yerine onu küçük parçalar hâlinde sırayla işleyerek hem daha ölçeklenebilir hem de daha güvenli uygulamalar geliştirmeyi sağlar.
``

## Dosya ve bellek arasındaki temel ilişki

Sabit disk, SSD veya ağ depolaması **kalıcı depolama** sunar; RAM ise programın çalışırken kullandığı hızlı fakat geçici alandır. Bir dosyayı `readFile` benzeri bir yöntemle tamamen okumak basittir, ancak dosya boyutu büyüdükçe bellek maliyeti de büyür. Dosya boyutu $N$ ise, tüm dosyayı belleğe alma yaklaşımında yaklaşık bellek tüketimi $O(N)$ olur.

Akışlarda ise veri `chunk` denilen parçalarla taşınır. Parça boyutu $C$ olduğunda, ideal koşullarda çalışma belleği yaklaşık $O(C)$ düzeyinde kalabilir. Bu, 5 GB'lık bir videoyu işlemek için 5 GB RAM gerekmeyebileceği anlamına gelir. Elbette tamponlar ve uygulama mantığı ek maliyet oluşturur; ama ana fikir nettir: veriyi yutmak yerine yudumlamak.

| Yaklaşım | Bellek kullanımı | Uygun senaryo | Risk |
|---|---:|---|---|
| Dosyanın tamamını okumak | $O(N)$ | Küçük yapılandırma dosyaları | Büyük dosyada bellek taşması |
| Stream ile okumak | Yaklaşık $O(C)$ | Log, video, büyük CSV, ağ verisi | Olay ve hata yönetimi gerektirir |
| Satır satır okuma | Değişken | Metin tabanlı kayıtlar | Satır sonu biçimleri dikkate alınmalı |

## Metin ile binary veri aynı değildir

Metin dosyası aslında baytlardan oluşur; fakat bu baytların UTF-8, UTF-16 gibi bir karakter kodlamasıyla yorumlanması gerekir. Binary dosyalarda ise baytların doğrudan anlamı vardır: PNG başlığı, ses örnekleri veya sıkıştırılmış veri gibi. Bu nedenle metin akışına kodlama (`encoding`) vermek mantıklıyken, görsel ya da arşiv dosyasını `Buffer` olarak ele almak daha doğrudur.

Node.js dünyasında bir okuma akışı `Readable`, yazma akışı ise `Writable` olarak adlandırılır. Aradaki dönüştürme işi için `Transform` akışları kullanılır. Örneğin bir log dosyasını okurken satırları büyük harfe dönüştürüp başka bir dosyaya yazabiliriz.

```js
import fs from 'node:fs';
import { Transform } from 'node:stream';

const kaynak = fs.createReadStream('uygulama.log', {
  encoding: 'utf8',
  highWaterMark: 64 * 1024
});

const buyukHarf = new Transform({
  transform(chunk, encoding, callback) {
    callback(null, chunk.toUpperCase());
  }
});

const hedef = fs.createWriteStream('arsiv.log');

kaynak
  .on('error', console.error)
  .pipe(buyukHarf)
  .on('error', console.error)
  .pipe(hedef)
  .on('finish', () => console.log('Dosya başarıyla yazıldı.'));
```

Bu örnekte `highWaterMark`, akışın hedeflediği tampon boyutunu belirtir. Bu değer her zaman kesin parça boyutu değildir; daha çok akışın ne kadar veri tamponlayabileceğine ilişkin bir eştir. `pipe()` ise üreticiden tüketiciye veri aktarımını bağlar.

## Backpressure: Hızlı musluk, küçük kova problemi

Okuma tarafı veriyi yazma tarafından hızlı üretirse tamponlar şişer. Bu duruma **backpressure** denir. Matematiksel olarak üretim hızı $R_p$, tüketim hızı $R_c$ ise, $R_p > R_c$ olduğu sürece bekleyen veri miktarı artma eğilimindedir. `pipe()` mekanizması, yazma tarafı yavaşladığında okuma tarafını duraklatarak bu baskıyı otomatik yönetir.

| Kavram | Görevi | Gerçek hayattaki benzetme |
|---|---|---|
| Readable | Veri üretir | Açılan musluk |
| Writable | Veri tüketir | Kova |
| Transform | Veriyi değiştirir | Su filtresi |
| Backpressure | Hız dengesini korur | Kova dolunca musluğu kısmak |

Üretim kodlarında `error`, `finish` ve gerekirse `close` olaylarını ele almak önemlidir. Daha sağlam bir seçenek olarak `pipeline()` kullanılabilir; zincirdeki hataları tek noktadan yönetir ve kaynakları daha düzenli kapatır. Kısacası stream'ler sadece büyük dosyalar için değil, bellek disiplini, kesintisiz veri işleme ve güvenilir I/O tasarımı için de vazgeçilmezdir.
