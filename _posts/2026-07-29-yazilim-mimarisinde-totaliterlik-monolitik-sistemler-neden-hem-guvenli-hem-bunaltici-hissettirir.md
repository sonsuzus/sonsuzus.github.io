---
layout: post
title: "Yazılım Mimarisinde Totaliterlik: Monolitik Sistemler Neden Hem Güvenli Hem Bunaltıcı Hissettirir?"
math: true
categories: 
  - Bilgi
tags: 
  - yazılım mimarisi
  - monolitik sistemler
  - siyaset felsefesi
---

Monolitik bir uygulamaya ilk kez giren geliştirici, kendisini devasa bir devlet dairesinde hissedebilir: Her şey aynı binadadır, kurallar merkezden belirlenir ve küçük bir değişiklik için bile sistemin bütünüyle konuşmak gerekir. Bu düzen güven verir; çünkü sınırlar, yetkiler ve sorumlular bellidir. Fakat aynı düzen zamanla bunaltıcı olabilir. Monolit ile siyasal totaliterlik arasındaki benzetme de tam burada başlar: İkisinde de koordinasyon kolaylığı ile özerklik kaybı arasında ciddi bir gerilim bulunur.
``

## Önce kavramları ayıralım

Monolitik mimari; kullanıcı arayüzü, iş kuralları ve veri erişimi gibi parçaların tek bir dağıtım birimi içinde çalıştığı yaklaşımdır. Bu, kodun mutlaka kötü veya tamamen düzensiz olduğu anlamına gelmez. İyi tasarlanmış bir monolit, kendi içinde modüllere ayrılabilir.

Siyaset felsefesinde totaliterlik ise iktidarın yalnızca yönetimi değil, toplumsal yaşamın mümkün olduğunca geniş bölümünü merkezi biçimde denetlemesidir. Dolayısıyla bu karşılaştırma birebir eşitlik değil, **merkezi kontrolün sonuçlarını düşünmek için kullanılan bir metafordur**. Yazılım sunucuları yurttaş değildir; başarısız bir dağıtım ile siyasal baskı aynı ahlaki ağırlığa sahip değildir.

| Boyut | Monolitik sistem | Merkezi siyasal düzen |
|---|---|---|
| Karar merkezi | Tek kod tabanı ve dağıtım hattı | Merkezi iktidar |
| Standartlaşma | Ortak dil, kütüphane ve kurallar | Ortak yasa ve kurumlar |
| Özerklik | Modüllerin bağımsızlığı sınırlı | Yerel aktörlerin yetkisi sınırlı |
| Kriz yönetimi | Tek noktadan hızlı müdahale | Merkezden hızlı karar |
| Temel risk | Tek hata alanının büyümesi | Gücün denetimsiz yoğunlaşması |

## Güvenlik hissi nereden geliyor?

Merkezileşme, belirsizliği azaltır. Tek depo, tek kimlik doğrulama mekanizması ve tek gözlemleme sistemi bulunduğunda geliştiriciler neyi nerede arayacaklarını bilir. Basit bir güvenlik modeli şöyle düşünülebilir:

$$R = P(ihlal) \times Etki$$

Monolitte güvenlik politikalarının tek yerde uygulanması, ihlal olasılığını düşürebilir. Ancak sistemin tamamı aynı süreçte çalışıyorsa başarılı bir ihlalin etkisi büyüyebilir. Yani merkezileşme $P(ihlal)$ değerini azaltırken **Etki** değerini artırabilir. Güvenli hissettiren şey, riskin yok olması değil, görünür ve yönetilebilir görünmesidir.

Aşağıdaki örnekte bütün istekler merkezi bir yetki kontrolünden geçer:

```javascript
function authorize(user, action) {
  const permissions = {
    admin: ["read", "write", "delete"],
    editor: ["read", "write"],
    viewer: ["read"]
  };

  if (!permissions[user.role]?.includes(action)) {
    throw new Error("Bu işlem için yetkiniz yok.");
  }
}

function deleteArticle(user, articleId) {
  authorize(user, "delete");
  return database.articles.remove(articleId);
}
```

Bu yaklaşımın avantajı tutarlılıktır: Herkes aynı yasaya tabidir. Dezavantajı ise `authorize` mekanizmasındaki bir hatanın bütün uygulamayı etkilemesidir. Sarayın kapısındaki muhafız uyursa yalnızca bir oda değil, bütün saray savunmasız kalabilir.

## Bunaltıcılık nasıl ortaya çıkar?

Monolit büyüdükçe ekipler teknik olarak ayrı görünse bile aynı yayın takvimine, veri modeline ve bağımlılıklara bağlanabilir. Küçük bir modül değişikliği yüzlerce testi çalıştırıyor, üç ekibin onayını gerektiriyor ve tüm uygulamanın yeniden dağıtılmasına yol açıyorsa yerel inisiyatif zayıflar.

Bunu kabaca şöyle ifade edebiliriz:

$$Özerklik \approx \frac{Bağımsız\ karar\ sayısı}{Zorunlu\ merkezi\ koordinasyon}$$

Payda büyüdükçe geliştirici, sistemin üreticisi olmaktan çok prosedür uygulayıcısına dönüşür. Siyaset felsefesindeki güçler ayrılığı fikri burada mimari karşılık bulur: Modül sınırları, açık arayüzler, bağımsız testler ve sahiplik kuralları merkezi gücü denetleyen kurumlar gibi çalışır.

## Çözüm hemen mikroservis mi?

Hayır. Bir monoliti sırf özgürlük sloganıyla onlarca servise bölmek, merkezi bürokrasiyi dağıtıp yerine diplomatik krizler çıkarabilir. Ağ hataları, veri tutarlılığı ve gözlemlenebilirlik maliyetleri artar. Daha dengeli başlangıç, **modüler monolit** yaklaşımıdır.

| Yaklaşım | Kontrol | Ekip özerkliği | Operasyon maliyeti |
|---|---:|---:|---:|
| Geleneksel monolit | Yüksek | Düşük | Düşük |
| Modüler monolit | Dengeli | Orta | Düşük-Orta |
| Mikroservisler | Dağıtık | Yüksek | Yüksek |

İyi mimari, merkezi kontrolü tamamen yok etmez; onu sınırlar, görünür kılar ve gerektiğinde sorgulanabilir hâle getirir. Monolitin güveni ile modüllerin özgürlüğü birlikte tasarlanabiliyorsa sistem ne başıboş bir konfederasyona ne de geliştiricilerin her değişiklikte izin kâğıdı doldurduğu dijital bir rejime dönüşür.
