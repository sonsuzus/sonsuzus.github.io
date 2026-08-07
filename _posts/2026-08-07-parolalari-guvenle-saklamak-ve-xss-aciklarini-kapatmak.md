---
layout: post
title: "Parolaları Güvenle Saklamak ve XSS Açıklarını Kapatmak"
math: true
categories: 
  - Bilgi
tags: 
  - web güvenliği
  - parola hashleme
  - XSS
---

Bir web uygulamasında güvenlik, kapıya pahalı bir kilit takıp anahtarı paspasın altında bırakmamaktır. Kullanıcı parolalarını düz metin olarak saklamak tam da böyle bir hatadır. Veritabanı sızdırıldığında saldırganlar yalnızca uygulamadaki hesaplara değil, parola tekrar kullanılmışsa başka servislere de erişebilir. Benzer şekilde XSS açıkları, güvenilmeyen içeriğin tarayıcıda kod gibi çalışmasına izin vererek kullanıcı oturumlarını ve verilerini tehlikeye atar.
``
## Şifreleme ile hashleme aynı şey değildir

Şifreleme, doğru anahtara sahip olan kişinin veriyi geri çözebilmesi için tasarlanmıştır. Parolalarda ise uygulamanın özgün metni öğrenmesine gerek yoktur. Bu nedenle parola **şifrelenmemeli**, tek yönlü bir parola türetme fonksiyonuyla hashlenmelidir.

| Yöntem | Geri döndürülebilir mi? | Parola saklamaya uygun mu? | Örnek |
|---|---:|---:|---|
| Düz metin | Zaten okunabilir | Hayır | `deneme123` |
| Şifreleme | Anahtarla evet | Genellikle hayır | AES-GCM |
| Hızlı hash | Pratikte hayır | Hayır | SHA-256 |
| Parola hashleme | Pratikte hayır | Evet | Argon2id, scrypt, bcrypt |

SHA-256 kriptografik olarak güçlü olsa da çok hızlıdır. Saldırganların saniyede milyonlarca parola tahmini yapabilmesi burada avantaj değil, felakettir. Argon2id gibi algoritmalar zaman ve bellek maliyetini yükselterek tahmin saldırılarını pahalılaştırır.

Bir parola $P$, rastgele salt $S$ ve maliyet parametreleri $m$, $t$, $p$ ile şöyle işlenebilir:

$$H = \operatorname{Argon2id}(P, S, m, t, p)$$

**Salt**, her kullanıcı için rastgele üretilir ve hash ile birlikte saklanabilir. Böylece aynı parolayı seçen iki kullanıcının hashleri farklı olur; hazır gökkuşağı tabloları da etkisizleşir.

## Node.js ile güvenli parola işleme

Aşağıdaki örnek, `argon2` paketiyle hash üretir ve giriş sırasında doğrulama yapar:

```javascript
import argon2 from "argon2";

export async function createPasswordHash(password) {
  return argon2.hash(password, {
    type: argon2.argon2id,
    memoryCost: 19456,
    timeCost: 2,
    parallelism: 1
  });
}

export async function verifyPassword(storedHash, candidate) {
  return argon2.verify(storedHash, candidate);
}
```

Üretilen değer salt ve algoritma parametrelerini de taşır. Veritabanına parola yerine bu çıktı kaydedilir. Parametreler sunucunun kapasitesine göre ölçülmeli; giriş işlemini kabul edilebilir düzeyde tutarken toplu tahminleri yavaşlatmalıdır. Ayrıca giriş uç noktalarına hız sınırlama ve çok faktörlü kimlik doğrulama eklenmelidir.

## XSS nasıl ortaya çıkar?

XSS, kullanıcı girdisinin HTML veya JavaScript olarak yorumlanmasıdır. Örneğin bir yorum doğrudan `innerHTML` ile sayfaya basılırsa saldırgan `<script>` etiketi ya da olay işleyicisi enjekte edebilir.

| Riskli yaklaşım | Güvenli yaklaşım |
|---|---|
| `element.innerHTML = input` | `element.textContent = input` |
| Elle karakter değiştirme | Bağlama duyarlı çıktı kodlama |
| Her HTML etiketine izin verme | Güvenilir kütüphaneyle sanitizasyon |
| Satır içi script kullanma | CSP ve harici script dosyaları |

```javascript
const message = document.querySelector("#message");
message.textContent = userInput;
```

`textContent`, girdiyi çalıştırılabilir HTML yerine metin olarak ekler. Zengin HTML kabul edilmesi gerçekten gerekiyorsa DOMPurify gibi bakımı sürdürülen bir sanitizasyon kütüphanesi kullanılmalıdır. URL, HTML niteliği, JavaScript ve CSS bağlamlarının farklı kodlama kuralları olduğu unutulmamalıdır.

Ek savunma olarak sunucu bir Content Security Policy gönderebilir:

```http
Content-Security-Policy: default-src 'self'; script-src 'self'; object-src 'none'; base-uri 'self'
```

CSP tek başına açığı düzeltmez; başarılı bir enjeksiyonun etkisini sınırlar. Güvenli şablon motorları, `HttpOnly`, `Secure` ve `SameSite` çerezleri de savunmayı katmanlandırır. Özetle parolalarda Argon2id gibi yavaş hash fonksiyonları, XSS tarafında bağlama uygun kodlama, sanitizasyon ve CSP birlikte kullanılmalıdır. Güvenlik tek bir sihirli fonksiyon değil, birbirini tamamlayan kontrollere dayanan bir süreçtir.
