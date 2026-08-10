---
layout: post
title: "Linux ve Özgürlük Metaforu: Özgür Yazılım Gerçekte Neyin Özgürlüğüdür?"
math: true
categories: 
  - Bilgi
tags: 
  - Linux
  - Özgür Yazılım
  - Richard Stallman
  - Siyaset Felsefesi
  - GPL
---

Linux denince çoğu kişinin zihninde terminal ekranları, penguen maskotları ve “bedava işletim sistemi” fikri belirir. Richard Stallman’ın savunduğu özgür yazılım ise bunlardan daha büyük, hatta politik bir iddiadır: Yazılımı kullanan insan, onu üreten kurumun pasif müşterisi olmamalıdır. Buradaki özgürlük, fiyat etiketiyle değil; bireyin teknoloji karşısındaki iradesiyle ilgilidir.

``

Stallman’ın Özgür Yazılım Vakfı (FSF) aracılığıyla formüle ettiği yaklaşım dört temel özgürlüğe dayanır: programı herhangi bir amaçla çalıştırmak; nasıl çalıştığını incelemek ve değiştirmek; kopyalarını paylaşmak; değiştirilmiş sürümleri dağıtmak. Bu çerçevede kaynak koduna erişim lüks değil, özgürlüğün teknik önkoşuludur. Kaynak kodu kapalıysa, kullanıcı programın ne yaptığını doğrulayamaz; yalnızca üreticinin beyanına güvenmek zorunda kalır.

Siyaset felsefesinde bu fikir, Isaiah Berlin’in özgürlük ayrımına yaklaştırılabilir. **Negatif özgürlük**, dış müdahalenin yokluğudur: Kimse sizi belirli bir yazılımı kullanmaya zorlamaz. **Pozitif özgürlük** ise kişinin kendi yaşamını yönlendirebilme kapasitesidir: Kullandığınız yazılımı anlayabilir, değiştirebilir veya topluluğun bunu yapmasına katılabilirsiniz. Stallman’ın vurgusu ikinci alandadır. “İstersen başka uygulama seç” cevabı yeterli değildir; alternatiflerin tamamı kapalıysa kullanıcı yine teknik iktidarın sınırları içinde kalır.

| Soru | Mülkiyetçi yazılım yaklaşımı | Özgür yazılım yaklaşımı |
|---|---|---|
| Kullanıcı ne alır? | Çalıştırma izni | İnceleme, değiştirme ve paylaşma yetkileri |
| Kaynak kodu | Genellikle gizlidir | Erişilebilir olmalıdır |
| Güven ilişkisi | Şirkete güven esastır | Denetim ve topluluk doğrulaması esastır |
| Güç dağılımı | Üreticide yoğunlaşır | Kullanıcılar ve geliştiriciler arasında paylaşılır |

Bu nedenle “özgür” sözcüğü İngilizcedeki *free* kelimesinin iki anlamı arasında sıkışır: ücretsiz olmak ve hür olmak. Stallman özellikle ikinci anlamı savunur. Bir programın fiyatı $0$ olabilir ama lisansı değişiklik yapmayı ve paylaşmayı yasaklıyorsa, özgür değildir. Buna karşılık ücretli dağıtılan bir GNU/Linux desteği veya özgür lisanslı ticari ürün, kullanıcının dört özgürlüğünü koruyabilir. Basitçe ifade edersek:

$$Özgürlük \neq Ücretsiz\lik$$

Daha kavramsal bir modelle, yazılım üzerindeki kullanıcı özerkliğini $A$ ile gösterelim. Çalıştırma, inceleme, değiştirme ve paylaşma haklarını sırasıyla $r, i, d, p$ olarak alırsak:

$$A = r + i + d + p$$

Mülkiyetçi lisanslar çoğu zaman yalnızca $r$ hakkını verir. Özgür yazılım lisansı ise tüm bileşenleri hedefler. Elbette bu matematik gerçek hukuki ve toplumsal ilişkileri tek başına açıklamaz; fakat Stallman’ın “kullanıcı egemenliği” fikrini görünür kılar.

GNU Genel Kamu Lisansı (GPL) bu düşünceyi yalnızca ahlaki çağrı olarak bırakmaz. **Copyleft** mekanizmasıyla, özgür koddan türetilen dağıtımların da aynı özgürlükleri korumasını ister. Lisansın ruhu kabaca şöyle özetlenebilir:

```text
Eğer yazılımı dağıtıyorsan:
  kaynak kodunu erişilebilir kıl
  değişiklikleri incelemeye izin ver
  alıcının paylaşım özgürlüğünü kısıtlama
```

Bu model, klasik liberal mülkiyet anlayışıyla ilginç bir gerilim taşır. Özgür yazılım telif hakkını reddetmez; tersine telif hukukunu, paylaşım hakkını koruyacak biçimde kullanır. Yani “kimsenin hiçbir hakkı olmasın” demez. “Bir kişinin yazılım üzerindeki kontrolü, diğerlerinin bilgiye erişim ve işbirliği kapasitesini bütünüyle yok etmesin” der.

Linux da bu metaforun güçlü sembolüdür; ancak teknik olarak Linux çekirdeği, daha geniş GNU araçları ve sayısız özgür bileşenle birlikte anlam kazanır. Özgür yazılımın asıl sorusu şudur: Teknoloji bizi sadece verimli tüketicilere mi dönüştürüyor, yoksa onu birlikte şekillendiren yurttaşlar olmamıza izin veriyor mu? Stallman için özgürlük, ekrandaki seçeneklerden birini seçmek değil; gerektiğinde seçenekleri yazabilme hakkıdır.
