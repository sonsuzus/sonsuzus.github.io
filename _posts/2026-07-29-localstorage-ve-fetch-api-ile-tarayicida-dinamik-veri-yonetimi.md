---
layout: post
title: "LocalStorage ve Fetch API ile Tarayıcıda Dinamik Veri Yönetimi"
math: true
categories: 
  - Bilgi
tags: 
  - JavaScript
  - LocalStorage
  - Fetch API
---

Modern web uygulamaları yalnızca ekranda bilgi göstermez; kullanıcı tercihlerini hatırlar, sunuculardan güncel veriler alır ve bağlantı kesildiğinde bile belirli işlevleri sürdürebilir. JavaScript’in **LocalStorage** ve **Fetch API** araçları, bu deneyimi oluşturmanın iki temel parçasıdır. Biri verileri tarayıcıda saklarken diğeri uygulamanın dış dünyayla konuşmasını sağlar.

``

## LocalStorage nasıl çalışır?

LocalStorage, aynı kaynağa ait verilerin tarayıcıda anahtar-değer çiftleri biçiminde tutulmasını sağlar. Buradaki “aynı kaynak”; protokol, alan adı ve port birleşiminin aynı olması demektir. Örneğin `https://ornek.com` ile `http://ornek.com` farklı depolama alanlarına sahiptir.

Veriler tarayıcı kapatılsa bile korunur. Ancak LocalStorage yalnızca **metin** saklayabilir. Bir nesneyi doğrudan kaydetmeye çalışırsak anlamlı içeriği yerine `[object Object]` sonucuyla karşılaşabiliriz. Bu nedenle nesneler `JSON.stringify()` ile metne çevrilmeli, okunurken `JSON.parse()` ile geri dönüştürülmelidir.

```javascript
const kullanici = {
  ad: "Ada",
  tema: "karanlik",
  bildirimler: true
};

// Nesneyi JSON metnine dönüştürerek saklar.
localStorage.setItem("kullanici", JSON.stringify(kullanici));

// Saklanan metni yeniden JavaScript nesnesine çevirir.
const kayit = localStorage.getItem("kullanici");
const okunanKullanici = kayit ? JSON.parse(kayit) : null;

console.log(okunanKullanici?.tema);
```

Temel işlemler oldukça sadedir: `setItem()` veri ekler veya günceller, `getItem()` okur, `removeItem()` belirli bir kaydı siler, `clear()` ise kaynağa ait bütün kayıtları temizler.

| Özellik | LocalStorage | Sunucu veritabanı |
|---|---|---|
| Veri konumu | Kullanıcının tarayıcısı | Uzak sunucu |
| Kalıcılık | Tarayıcı verisi silinene kadar | Sunucu politikasına bağlı |
| İnternet gereksinimi | Yok | Genellikle var |
| Güvenlik | Hassas veriler için uygun değil | Doğru yapılandırmayla daha güvenli |
| Veri tipi | Yalnızca metin | Çok sayıda veri tipi |

Tarayıcıların LocalStorage için genellikle birkaç megabaytlık sınırı bulunur. Yaklaşık kapasite hesabı $K \approx n \times b$ biçiminde düşünülebilir. Burada $n$ karakter sayısını, $b$ ise karakter başına kullanılan ortalama baytı temsil eder. Büyük dosyalar ve görseller bu alana doldurulmamalıdır.

## Fetch API ile sunucuya ulaşmak

Fetch API, HTTP isteklerini Promise tabanlı olarak gerçekleştirir. `fetch()` hemen nihai veriyi değil, gelecekte oluşacak sonucu temsil eden bir Promise döndürür. Bu yapı `async/await` ile daha okunabilir hâle gelir.

```javascript
async function kullanicilariGetir() {
  try {
    const yanit = await fetch("https://jsonplaceholder.typicode.com/users");

    if (!yanit.ok) {
      throw new Error(`HTTP hatası: ${yanit.status}`);
    }

    const kullanicilar = await yanit.json();
    localStorage.setItem("kullanicilar", JSON.stringify(kullanicilar));
    return kullanicilar;
  } catch (hata) {
    console.error("Veriler alınamadı:", hata);
    return JSON.parse(localStorage.getItem("kullanicilar") || "[]");
  }
}
```

Bu örnek önce sunucudan veri almaya çalışır. İstek başarısız olursa daha önce LocalStorage’a kaydedilmiş verileri kullanır. Böylece basit bir önbellek mekanizması elde edilir. Fetch yalnızca ağ hatalarında otomatik olarak reddedilir; `404` veya `500` gibi HTTP cevaplarında `response.ok` ayrıca kontrol edilmelidir.

| HTTP metodu | Amaç | Tipik kullanım |
|---|---|---|
| GET | Veri okumak | Ürün listesini almak |
| POST | Yeni veri oluşturmak | Kullanıcı kaydetmek |
| PUT/PATCH | Veriyi güncellemek | Profil düzenlemek |
| DELETE | Veriyi silmek | Yorumu kaldırmak |

```javascript
await fetch("https://api.example.com/tercihler", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ tema: "karanlik" })
});
```

## Güvenlik ve doğru kullanım

LocalStorage içeriğine sayfadaki JavaScript erişebilir. Bu nedenle parola, kredi kartı bilgisi veya uzun ömürlü erişim anahtarları burada saklanmamalıdır. Bir XSS açığı, kayıtlı verilerin saldırgan tarafından okunmasına yol açabilir. Sunucudan gelen içerik de doğrulanmadan `innerHTML` ile sayfaya basılmamalıdır.

En sağlıklı yaklaşım; LocalStorage’ı tema, dil ve geçici önbellek gibi düşük riskli bilgiler için kullanmak, önemli verileri sunucuda tutmak ve Fetch isteklerinde hata, zaman aşımı ve yüklenme durumlarını kullanıcıya açıkça göstermektir. Böylece uygulama hem hızlı hem dayanıklı olur; kullanıcı da boş ekrana bakıp internet tanrılarına dua etmek zorunda kalmaz.
