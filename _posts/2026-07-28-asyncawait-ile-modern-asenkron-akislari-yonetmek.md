---
layout: post
title: "Async/Await ile Modern Asenkron Akışları Yönetmek"
math: true
categories: 
  - Bilgi
tags: 
  - JavaScript
  - Async/Await
  - Asenkron Programlama
---

Bir web servisine istek gönderirken, dosya okurken veya veritabanından kayıt beklerken uygulamanın tamamen durmasını istemeyiz. JavaScript’in `async/await` sözdizimi, arka planda asenkron çalışan bu işlemleri sanki adım adım ilerleyen senkron kodlarmış gibi yazmamızı sağlar. Sonuç; daha az iç içe fonksiyon, daha anlaşılır hata yönetimi ve geliştiricinin saç baş yolma ihtimalinde kayda değer bir azalmadır.
``
## Asenkron çalışma neden gereklidir?

Senkron bir programda her işlem, kendisinden önceki işlemin bitmesini bekler. Uzun süren bir ağ isteği bütün akışı engellerse kullanıcı arayüzü donabilir. Asenkron modelde ise bekleyen görev kenara alınır ve çalışma zamanı diğer işleri yürütmeye devam eder.

Bir işlemin toplam süresini kabaca şu şekilde düşünebiliriz:

$$T_{senkron} = T_1 + T_2 + \cdots + T_n$$

Bağımsız görevler paralel biçimde başlatıldığında ideal süre, görev sürelerinin toplamı yerine en uzun göreve yaklaşır:

$$T_{asenkron} \approx \max(T_1, T_2, \ldots, T_n)$$

Elbette JavaScript’in ana iş parçacığı aynı anda iki JavaScript komutu çalıştırmaz. Ağ, zamanlayıcı ve dosya sistemi gibi işlemler çalışma ortamına devredilir; tamamlanan görevlerin devamı olay döngüsü tarafından uygun zamanda yürütülür.

| Yaklaşım | Okunabilirlik | Hata yönetimi | Kullanım alanı |
|---|---:|---|---|
| Callback | Düşük veya orta | İç içe yapıda zor | Eski API’ler |
| Promise zinciri | Orta | `.catch()` ile | Fonksiyonel akışlar |
| Async/Await | Yüksek | `try/catch` ile | Karmaşık iş süreçleri |

## Async ve await ne yapar?

`async` ile işaretlenen bir fonksiyon her zaman `Promise` döndürür. Fonksiyon doğrudan bir değer döndürse bile bu değer çözülmüş bir Promise içine sarılır. `await` ise Promise sonuçlanana kadar yalnızca ilgili asenkron fonksiyonun ilerleyişini bekletir; uygulamanın tamamını kilitlemez.

```javascript
async function kullaniciGetir(id) {
  const yanit = await fetch(`/api/kullanicilar/${id}`);

  if (!yanit.ok) {
    throw new Error(`HTTP hatası: ${yanit.status}`);
  }

  return await yanit.json();
}
```

Bu fonksiyon önce HTTP yanıtını, ardından JSON dönüşümünü bekler. Kod yukarıdan aşağı okunur; fakat iki bekleme sırasında da çalışma ortamı başka görevlerle ilgilenebilir.

## Hataları kontrollü biçimde yakalamak

Asenkron işlemler ağ kesintisi, yetki problemi veya geçersiz veri nedeniyle başarısız olabilir. `try/catch/finally`, bu durumları senkron kodlara benzer şekilde yönetir.

```javascript
async function profiliGoster(id) {
  try {
    const kullanici = await kullaniciGetir(id);
    console.log(`${kullanici.ad} profili yüklendi.`);
  } catch (hata) {
    console.error("Profil yüklenemedi:", hata.message);
  } finally {
    console.log("Yükleme işlemi sona erdi.");
  }
}
```

`finally` bloğu başarıdan bağımsız olarak çalıştığı için yükleme göstergesini kapatmak veya kaynakları temizlemek açısından kullanışlıdır.

## Bağımsız görevleri sıraya dizmeyin

Her `await` ifadesini art arda kullanmak bazen gereksiz beklemeye yol açar. Birbirine bağlı olmayan görevler önce başlatılmalı, sonra birlikte beklenmelidir.

```javascript
async function paneliHazirla() {
  const kullaniciIstegi = fetch("/api/kullanici");
  const bildirimIstegi = fetch("/api/bildirimler");

  const [kullaniciYaniti, bildirimYaniti] = await Promise.all([
    kullaniciIstegi,
    bildirimIstegi
  ]);

  return {
    kullanici: await kullaniciYaniti.json(),
    bildirimler: await bildirimYaniti.json()
  };
}
```

`Promise.all`, işlemleri eşzamanlı başlatır; ancak içlerinden biri reddedilirse tamamı hata verir. Tüm sonuçları başarı veya hata durumlarıyla incelemek gerekiyorsa `Promise.allSettled` tercih edilebilir.

## Küçük ama önemli alışkanlıklar

`await` yalnızca gerçekten sonuca ihtiyaç duyulan yerde kullanılmalıdır. Hatalar sessizce yutulmamalı, mümkünse anlamlı bağlamla yeniden fırlatılmalıdır. Ayrıca uzun listelerde sınırsız sayıda isteği aynı anda başlatmak sunucuyu zorlayabilir; görevleri gruplara ayırmak veya eşzamanlılık sınırı uygulamak daha güvenlidir.

Async/await sihir değil, Promise tabanlı akışın daha okunabilir bir yüzüdür. Olay döngüsünü, bağımlı görevleri ve hata yayılımını anladığınızda karmaşık asenkron süreçler ürkütücü bir labirent olmaktan çıkıp düzenli bir yapılacaklar listesine dönüşür.
