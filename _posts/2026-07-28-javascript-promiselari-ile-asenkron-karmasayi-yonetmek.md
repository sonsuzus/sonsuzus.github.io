---
layout: post
title: "JavaScript Promise’ları ile Asenkron Karmaşayı Yönetmek"
math: true
categories: 
  - Bilgi
tags: 
  - JavaScript
  - Promise
  - Asenkron Programlama
---

Bir API isteğinin ne zaman tamamlanacağını, dosyanın ne zaman okunacağını veya kullanıcının konum bilgisinin ne zaman geleceğini önceden bilemeyiz. JavaScript bu bekleme süresinde uygulamayı durdurmak yerine diğer işleri yürütür. Ancak sonuçları callback fonksiyonlarıyla takip etmeye çalışmak, kısa sürede girintilerle dolu bir “callback cehennemine” dönüşebilir. Promise nesneleri, gelecekte tamamlanacak işlemleri düzenli, zincirlenebilir ve güvenilir biçimde temsil ederek bu karmaşaya çözüm sunar.

``

## Promise nedir?

Promise, henüz elimizde olmayan fakat gelecekte elde edilmesi beklenen bir değerin temsilcisidir. Gerçek hayatta restorandan aldığımız sipariş fişine benzetilebilir: Yemek henüz hazır değildir, ancak fiş işlemin başarılı şekilde tamamlanacağını veya bir sorun oluşacağını takip etmemizi sağlar.

Bir Promise üç durumdan birinde bulunur:

| Durum | Anlamı | Sonraki adım |
|---|---|---|
| `pending` | İşlem devam ediyor | Beklenir |
| `fulfilled` | İşlem başarıyla tamamlandı | Değer kullanılır |
| `rejected` | İşlem başarısız oldu | Hata işlenir |

Bir Promise yalnızca bir kez sonuçlanır. `fulfilled` veya `rejected` durumuna geçtikten sonra tekrar değiştirilemez. Durum geçişini matematiksel olarak $pending \rightarrow fulfilled$ veya $pending \rightarrow rejected$ biçiminde gösterebiliriz. Ancak $fulfilled \rightarrow pending$ gibi bir geri dönüş mümkün değildir.

## İlk Promise’imizi oluşturalım

Promise kurucusu, `resolve` ve `reject` fonksiyonlarını alan bir yürütücü fonksiyon bekler:

```javascript
function siparisHazirla(stokVarMi) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (stokVarMi) {
        resolve({ urun: "Kahve", durum: "Hazır" });
      } else {
        reject(new Error("Kahve çekirdeği kalmadı!"));
      }
    }, 1000);
  });
}
```

Burada `setTimeout`, bir saniye süren asenkron işlemi taklit eder. İşlem başarılıysa `resolve` sonuç değerini iletir; başarısızsa `reject` bir hata üretir. Gerçek projelerde aynı yapı ağ istekleri, veritabanı sorguları veya dosya işlemleri için kullanılabilir.

Promise sonucunu `then`, `catch` ve `finally` metotlarıyla yönetebiliriz:

```javascript
siparisHazirla(true)
  .then((siparis) => {
    console.log(siparis.durum);
    return `${siparis.urun} müşteriye götürülüyor`;
  })
  .then((mesaj) => console.log(mesaj))
  .catch((hata) => console.error(hata.message))
  .finally(() => console.log("Sipariş işlemi sona erdi"));
```

Her `then` yeni bir Promise döndürür. Böylece sonuçlar sırayla aktarılır ve iç içe callback’ler yerine düz bir zincir kurulur. Zincirin herhangi bir noktasında hata oluşursa kontrol en yakın `catch` bloğuna gider. `finally` ise sonuç ne olursa olsun çalışır; yükleniyor göstergesini kapatmak gibi temizlik işleri için idealdir.

## Callback ve Promise karşılaştırması

| Özellik | Callback yaklaşımı | Promise yaklaşımı |
|---|---|---|
| Okunabilirlik | İç içe yapılar oluşabilir | Doğrusal zincir kurulur |
| Hata yönetimi | Her seviyede ayrı kontrol gerekebilir | Tek `catch` zinciri yakalayabilir |
| Birleştirme | Elle koordinasyon gerekir | Hazır yardımcı metotlar vardır |
| Sonuç aktarımı | Parametrelerle yapılır | `return` ile zincire iletilir |

## Birden fazla işlemi yönetmek

Bağımsız görevleri paralel başlatmak için `Promise.all` kullanılabilir:

```javascript
const profil = fetch("/api/profil");
const bildirimler = fetch("/api/bildirimler");

Promise.all([profil, bildirimler])
  .then(([profilYaniti, bildirimYaniti]) => {
    console.log("İki istek de tamamlandı");
  })
  .catch((hata) => console.error("İsteklerden biri başarısız", hata));
```

İşlemlerin süreleri $t_1$ ve $t_2$ ise paralel toplam süre yaklaşık $T = \max(t_1, t_2)$ olur. Sıralı çalıştırmada ise süre yaklaşık $T = t_1 + t_2$ olacaktır. Bununla birlikte `Promise.all`, tek bir işlem reddedildiğinde hemen reddedilir. Bütün sonuçları başarı veya hata ayrımıyla görmek için `Promise.allSettled`; ilk tamamlanan sonucu almak için `Promise.race`; ilk başarılı sonucu almak için `Promise.any` tercih edilebilir.

Promise’lar işlemleri sihirli biçimde hızlandırmaz; asıl güçleri zamanlamayı ve hata akışını düzenlemeleridir. Modern `async/await` sözdizimi de temelde Promise’lar üzerinde çalışır. Bu nedenle Promise mantığını öğrenmek, yalnızca eski callback zincirlerinden kurtulmayı değil, JavaScript’in modern asenkron dünyasını sağlam bir temelle anlamayı sağlar.
