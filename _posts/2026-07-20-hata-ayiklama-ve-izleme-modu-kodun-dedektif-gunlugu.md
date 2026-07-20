---
layout: post
title: "Hata Ayıklama ve İzleme Modu: Kodun Dedektif Günlüğü"
math: true
categories: 
  - Bilgi
tags: 
  - debugging
  - trace
  - programlama
---

Kod yazmak bazen yemek tarifi uygulamak gibidir: Malzemeler doğru, fırın çalışıyor, ama kek yine de çöker. İşte hata ayıklama ve özellikle izleme yani trace modu, bu çöküşün hangi adımda başladığını görmemizi sağlar. Programın satır satır nasıl ilerlediğini, değişkenlerin hangi değerleri aldığını ve mantığın nerede ters köşe yaptığını takip ederek “bence çalışmalıydı” cümlesini “şurada yanlış düşünmüşüm” seviyesine taşırız.
``
Trace, bir programın çalışması sırasında bıraktığı ayak izleridir. Normal çalıştırmada programı sadece sonuç üzerinden değerlendiririz: çıktı doğru mu, hata verdi mi, beklenen veri geldi mi? İzleme modunda ise sonucu değil, süreci inceleriz. Bu yaklaşımı matematiksel olarak şöyle düşünebiliriz: Programın herhangi bir andaki durumu $S=(satır, değişkenler, çağrıYığını)$ olsun. Her komut çalıştığında yeni durum $S_{i+1}=f(S_i)$ oluşur. Trace, bu durumların sıralı kaydıdır: $S_0, S_1, S_2, ... S_n$.

Bu yüzden trace yalnızca “hata nerede?” sorusunu değil, “program neden oraya geldi?” sorusunu da cevaplar. Özellikle döngüler, koşullu ifadeler, recursive fonksiyonlar ve asenkron işlemler gibi akışın dallandığı yerlerde paha biçilmezdir.

| Yöntem | Ne Gösterir? | Ne Zaman Kullanılır? | Avantajı |
|---|---|---|---|
| Print/log yazdırma | Seçilen değişken değerleri | Hızlı kontrol gerektiğinde | Basit ve pratiktir |
| Debugger breakpoint | Belirli satırdaki anlık durum | IDE ile detaylı incelemede | Adım adım kontrol sağlar |
| Trace modu | Akışın tamamına yakın geçmişi | Mantık karmaşıklaştığında | Zaman çizelgesi sunar |
| Test çıktıları | Beklenen/gerçek sonuç farkı | Fonksiyon doğrulamada | Otomasyon sağlar |

Basit bir JavaScript örneğiyle bakalım. Amacımız, listedeki çift sayıları toplamak olsun:

```javascript
function ciftleriTopla(liste) {
  let toplam = 0;

  for (let i = 0; i <= liste.length; i++) {
    console.log('TRACE', { i, eleman: liste[i], toplam });

    if (liste[i] % 2 === 0) {
      toplam += liste[i];
    }
  }

  return toplam;
}

console.log(ciftleriTopla([2, 5, 8]));
```

Buradaki trace çıktısı bize kritik bir şeyi gösterir: Döngü koşulu `i <= liste.length` olduğu için son turda `liste[3]` okunur ve değer `undefined` olur. Program bazen patlamaz, ama mantık bulanıklaşır. Doğrusu `i < liste.length` olmalıdır. İzleme satırı olmasaydı, sadece “garip bir sonuç” ile baş başa kalabilirdik.

Trace kullanırken değişken eşleşmelerini görmek de önemlidir. Örneğin bir filtreleme işleminde `kullanici.id === siparis.userId` karşılaştırması bekleneni vermiyorsa, sadece iki değeri değil türlerini de yazdırmalıyız:

```javascript
console.log('MATCH TRACE', {
  kullaniciId: kullanici.id,
  kullaniciIdTipi: typeof kullanici.id,
  siparisUserId: siparis.userId,
  siparisUserIdTipi: typeof siparis.userId,
  esitMi: kullanici.id === siparis.userId
});
```

Bu çıktı, `42` ile `'42'` arasındaki meşhur JavaScript dramını yakalayabilir. Değerler aynı görünür, ama biri sayı diğeri metindir. Yani hata algoritmada değil, veri tipindedir.

Trace’in gücü kadar tehlikesi de vardır. Her yere log koymak, gece vakti çantadan çıkan kablo yığını gibi karmaşa üretir. Bu yüzden izleme bilinçli yapılmalıdır.

| İyi Trace | Kötü Trace |
|---|---|
| Anlamlı etiket taşır | Sadece `console.log(x)` yazar |
| Kritik karar noktalarındadır | Her satırı boğar |
| Değer ve tür bilgisini verir | Bağlam vermez |
| Geçici veya seviyelidir | Üretimde unutulur |

Daha düzenli bir yaklaşım için küçük bir yardımcı trace fonksiyonu yazabiliriz:

```javascript
const TRACE_AKTIF = true;

function trace(adim, veri) {
  if (!TRACE_AKTIF) return;
  console.log(`[TRACE] ${adim}`, {
    zaman: new Date().toISOString(),
    ...veri
  });
}

function indirimHesapla(fiyat, oran) {
  trace('baslangic', { fiyat, oran });

  const indirim = fiyat * oran;
  trace('indirim_hesaplandi', { indirim });

  const sonuc = fiyat - indirim;
  trace('sonuc', { sonuc });

  return sonuc;
}
```

Bu yapı, trace kayıtlarını merkezi hale getirir. İsterseniz sonra dosyaya yazabilir, seviyelendirebilir veya üretim ortamında kapatabilirsiniz. Büyük sistemlerde benzer mantık logger kütüphaneleri, distributed tracing araçları ve request id kullanımıyla genişletilir.

Sonuç olarak trace modu, programcıya mikroskop verir. Hata ayıklama yalnızca bozuk satırı bulmak değildir; kodun düşünce biçimini izlemektir. Değişkenler ne zaman değişiyor, koşullar hangi dala giriyor, fonksiyonlar hangi sırayla çağrılıyor? Bu soruların cevabı görünür hale geldiğinde, hata artık sisli bir canavar değil, üstüne gidilebilir küçük bir mantık pürüzüdür.
