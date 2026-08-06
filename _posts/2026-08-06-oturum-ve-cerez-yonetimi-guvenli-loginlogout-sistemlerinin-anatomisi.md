---
layout: post
title: "Oturum ve Çerez Yönetimi: Güvenli Login/Logout Sistemlerinin Anatomisi"
math: true
categories: 
  - Bilgi
tags: 
  - session
  - cookie
  - kimlik doğrulama
---

Bir kullanıcı giriş yaptığında uygulamanın onu sonraki istekte hatırlaması gerekir. HTTP ise doğası gereği durumsuzdur; yani sunucu, arka arkaya gelen iki isteğin aynı kişiye ait olduğunu kendiliğinden bilmez. Oturum ve çerez mekanizmaları bu hafıza problemini çözer. Biri bilgiyi çoğunlukla sunucuda, diğeri tarayıcıda taşır; doğru kullanıldıklarında güvenli ve akıcı bir kullanıcı deneyimi oluştururlar.

``

## HTTP Neden Kullanıcıyı Hatırlamaz?

Her HTTP isteği bağımsız değerlendirilir. Kullanıcı `/login` adresinde doğru parolayı girdikten sonra `/profile` sayfasına geçtiğinde tarayıcının kimliğini yeniden kanıtlaması gerekir. Teorik olarak doğrulama maliyetini şöyle düşünebiliriz:

$$T_{toplam} = n \times T_{doğrulama}$$

Her istekte parola doğrulamak yerine ilk doğrulamada bir oturum oluşturulursa yaklaşık maliyet şu hâle gelir:

$$T_{toplam} = T_{login} + n \times T_{sessionKontrolü}$$

Oturum kontrolü, parola özeti hesaplamaktan çok daha hızlıdır. Üstelik parola her istekte ağ üzerinde dolaşmaz.

## Cookie ve Session Arasındaki Fark

Cookie, tarayıcının sakladığı ve uygun isteklerle sunucuya gönderdiği küçük bir anahtar-değer verisidir. Session ise kullanıcıya ait geçici durumun sunucuda saklanmasıdır. Tarayıcı genellikle yalnızca tahmin edilmesi zor bir oturum kimliği taşır.

| Özellik | Cookie | Session |
|---|---|---|
| Saklama yeri | Tarayıcı | Sunucu, Redis veya veritabanı |
| Veri kapasitesi | Yaklaşık 4 KB | Altyapıya bağlı |
| Hassas veri | Saklanmamalı | Daha uygun |
| Sunucu yükü | Düşük | Kullanıcı sayısıyla artar |
| Tipik kullanım | Tema, dil, session ID | Kullanıcı kimliği, yetkiler |

Örneğin `theme=dark` doğrudan cookie içinde tutulabilir. Ancak `role=admin` değerine güvenmek tehlikelidir; kullanıcı tarayıcı araçlarıyla bunu değiştirebilir. Yetki bilgisi sunucuda doğrulanmalıdır.

## Express ile Login ve Logout

Aşağıdaki örnek, oturum verisini sunucuda tutar ve tarayıcıya yalnızca oturum kimliğini içeren cookie gönderir:

```javascript
import express from "express";
import session from "express-session";
import bcrypt from "bcrypt";

const app = express();
app.use(express.json());

app.use(session({
  secret: process.env.SESSION_SECRET,
  resave: false,
  saveUninitialized: false,
  cookie: {
    httpOnly: true,
    secure: process.env.NODE_ENV === "production",
    sameSite: "lax",
    maxAge: 1000 * 60 * 30
  }
}));

app.post("/login", async (req, res) => {
  const user = await findUserByEmail(req.body.email);
  const valid = user && await bcrypt.compare(req.body.password, user.passwordHash);

  if (!valid) return res.status(401).json({ error: "Geçersiz bilgiler" });

  req.session.regenerate(error => {
    if (error) return res.sendStatus(500);
    req.session.userId = user.id;
    res.json({ message: "Giriş başarılı" });
  });
});

app.post("/logout", (req, res) => {
  req.session.destroy(error => {
    if (error) return res.sendStatus(500);
    res.clearCookie("connect.sid");
    res.sendStatus(204);
  });
});
```

`httpOnly`, JavaScript'in cookie değerini okumasını engelleyerek XSS saldırılarının etkisini azaltır. `secure`, cookie'nin yalnızca HTTPS üzerinden gönderilmesini sağlar. `sameSite`, başka sitelerden başlatılan istekleri sınırlayarak CSRF riskini düşürür. Login sonrasında `regenerate` kullanılması ise saldırganın önceden bildiği bir kimliği kurbana kullandırdığı session fixation saldırısına karşı önemlidir.

## Tercihler Nerede Saklanmalı?

| Veri | Önerilen yer | Gerekçe |
|---|---|---|
| Tema ve dil | Cookie veya localStorage | Hassas değildir |
| Sepet kimliği | İmzalı cookie/session | Bütünlük gerekir |
| Kullanıcı ID | Session | İstemciye güvenilmez |
| Parola | Hiçbiri | Yalnızca hash saklanır |
| Erişim yetkileri | Sunucu | Her istekte doğrulanmalıdır |

Gerçek projelerde varsayılan bellek tabanlı session deposu kullanılmamalıdır; süreç yeniden başlayınca oturumlar kaybolur ve birden fazla sunucu arasında paylaşılmaz. Redis gibi süre sonu destekleyen merkezi bir depo daha uygundur.

Son olarak logout yalnızca arayüzde kullanıcıyı giriş sayfasına göndermek değildir. Sunucudaki oturum gerçekten yok edilmeli, cookie temizlenmeli ve hassas işlemlerde gerekirse tüm cihazlardaki oturumları iptal edebilmek için kullanıcı bazlı bir oturum listesi tutulmalıdır. Kısacası iyi bir giriş sistemi, kapıyı açmayı bildiği kadar kapatmayı da bilmelidir.
