---
layout: post
title: "Web Uygulama Güvenliği Analizi: Burp Suite ve OWASP ZAP ile Zayıflık Avı"
math: true
categories: 
  - Bilgi
tags: 
  - web-guvenligi
  - burp-suite
  - owasp-zap
  - sqli
  - xss
---

Bir web uygulamasını güvenli sanmak, kapıyı kilitleyip pencereyi açık bırakmaya benzer. Burp Suite ve OWASP ZAP gibi proxy araçları, tarayıcı ile sunucu arasına oturarak HTTP trafiğini görünür kılar; böylece SQL enjeksiyonu, XSS ve yetkilendirme hataları gibi mimari zayıflıkları kontrollü ve izinli ortamlarda analiz edebiliriz.
``
Önce etik sınırı kalın çizelim: Bu araçlar yalnızca kendi sistemlerinizde, eğitim laboratuvarlarında veya açıkça yetki verilen testlerde kullanılmalıdır. Amaç “bir siteyi kırmak” değil, yazılımın hangi varsayımlar üzerine kurulduğunu görmek ve o varsayımlar bozulduğunda neler olabileceğini anlamaktır.

Proxy mantığı basittir: Tarayıcınız isteği doğrudan sunucuya göndermek yerine Burp veya ZAP’a yollar. Araç, isteği yakalar, başlıkları, çerezleri, gövdeyi ve parametreleri gösterir. İsterseniz isteği değiştirmeden geçirir, isterseniz test ortamında varyasyonlar deneyerek uygulamanın davranışını gözlemlersiniz. Bu, yazılımcı için adeta “HTTP mikroskobu”dur.

Web güvenliğinde risk çoğu zaman şu sezgisel modelle düşünülür: $Risk = Olasılık \times Etki$. Bir açık çok kolay tetikleniyor ama etkisi düşükse orta risk olabilir; nadir tetiklenen fakat veritabanı sızıntısına yol açan bir hata ise kritik sayılabilir. Proxy araçları bu iki değişkeni ölçmemize yardım eder: Hata tekrar üretilebiliyor mu, hangi veri etkileniyor, kimlik doğrulama atlanıyor mu?

| Araç | Güçlü Yanı | Tipik Kullanım | Not |
|---|---|---|---|
| Burp Suite | Manuel test akışı ve eklenti ekosistemi | İstek yakalama, tekrar gönderme, oturum analizi | Community sürümü öğrenmek için yeterlidir |
| OWASP ZAP | Açık kaynak ve otomasyon dostu yapı | Pasif tarama, CI/CD güvenlik kontrolleri | Başlangıç için çok erişilebilirdir |
| Tarayıcı DevTools | Hızlı istemci tarafı inceleme | DOM, network ve console analizi | Proxy kadar derin manipülasyon sunmaz |

SQL enjeksiyonunun kökü, kullanıcı girdisinin SQL komutunun parçası gibi ele alınmasıdır. Yani veri ile komut ayrımı kaybolur. Güvensiz bir yaklaşım şu şekilde görünür:

```js
// Eğitim amaçlı kötü örnek: kullanıcı girdisi sorguya doğrudan ekleniyor
const userId = req.query.id;
const sql = 'SELECT * FROM users WHERE id = ' + userId;
db.query(sql);
```

Burada uygulama, `id` değerinin gerçekten sayı olduğunu varsayar. Oysa güvenli tasarımda sorgu şablonu ile veri ayrı taşınmalıdır:

```js
// Daha güvenli yaklaşım: parametreli sorgu
const userId = req.query.id;
const sql = 'SELECT * FROM users WHERE id = ?';
db.query(sql, [userId]);
```

Parametreli sorgular, veriyi komut olarak yorumlamaz. Ek olarak giriş doğrulama, en az yetkili veritabanı kullanıcısı, ayrıntılı hata mesajlarını kapatma ve log analizi savunmayı güçlendirir.

XSS tarafında problem, kullanıcının sağladığı verinin HTML, JavaScript veya URL bağlamında güvenli biçimde kodlanmadan sayfaya basılmasıdır. Saklanan XSS yorum alanında kalıcı olabilir; yansıyan XSS URL parametresinden dönebilir; DOM tabanlı XSS ise tarayıcıdaki JavaScript’in veriyi yanlış işlemesiyle doğar.

| Saldırı Vektörü | Temel Hata | Savunma | Proxy ile Gözlem |
|---|---|---|---|
| SQLi | Veri-komut ayrımının bozulması | Parametreli sorgu, doğrulama | Parametre değişince hata/yanıt farkı |
| XSS | Çıktının bağlama göre kodlanmaması | HTML escape, CSP, şablon motoru güvenliği | Yanıtta girdinin nerede göründüğü |
| Yetki hatası | Kimlik ile izin kontrolünün karışması | Sunucu tarafı erişim kontrolü | Çerez veya ID değişiminde davranış |

Burp veya ZAP ile iyi bir analiz akışı şöyle kurulabilir: Önce uygulamada normal kullanıcı gibi gezinip trafik haritası çıkarılır. Sonra pasif bulgular incelenir: eksik güvenlik başlıkları, güvensiz çerez bayrakları, fazla konuşkan hata mesajları. Ardından yalnızca test ortamında, belirli parametrelerin sunucu davranışını nasıl değiştirdiği gözlenir. Bulgular “kanıt, etki, çözüm” formatında raporlanır.

Mimari açıdan en önemli ders şudur: Güvenlik, sonradan eklenen bir eklenti değil, veri akışının tasarım ilkesidir. Her giriş şüphelidir, her çıktı bağlama göre kodlanmalıdır, her erişim sunucuda doğrulanmalıdır. Proxy araçları ise bu prensiplerin gerçekten uygulanıp uygulanmadığını görmemizi sağlayan eğlenceli ama ciddi laboratuvar arkadaşlarıdır.
