---
layout: post
title: "Fonksiyonel Programlamanın Budist Yanı: Yan Etkisiz Bir Hayat Mümkün mü?"
math: true
categories: 
  - Bilgi
tags: 
  - fonksiyonel programlama
  - saf fonksiyonlar
  - değişmezlik
---

Bir fonksiyonun dış dünyaya tutunmadan yalnızca aldığı değerlerle çalışması, zihnin geçmişe ve beklentilere tutunmadan ânı gözlemlemesine şaşırtıcı biçimde benzer. Fonksiyonel programlama ile Budist düşünce aynı şey değildir; fakat **saflık**, **değişmezlik** ve **bağımlılıkların farkında olma** kavramları üzerinden verimli bir benzetme kurabiliriz. Belki aydınlanmaya ulaşamayız ama en azından üretimde gizemli biçimde değişen global değişkenlerden kurtulabiliriz.

``

## Saf fonksiyon: Karması kolay hesaplama

Saf fonksiyon, aynı girdiye her zaman aynı çıktıyı verir ve fonksiyonun dışındaki dünyayı değiştirmez. Matematiksel olarak bunu şöyle düşünebiliriz:

$$f(x) = y$$

Eğer $x$ değişmiyorsa $y$ de değişmez. Fonksiyon; dosyaya yazmaz, global değişken güncellemez veya gizlice ağ isteği göndermez. Böylece sonucunu anlamak için evrenin bütün geçmişini bilmemiz gerekmez.

```javascript
const indirimliFiyat = (fiyat, oran) => fiyat * (1 - oran);

console.log(indirimliFiyat(1000, 0.20)); // Her zaman 800
```

Bu fonksiyon yalnızca parametrelerine bağlıdır. Test etmek için veritabanı, sahte sunucu ya da dolunay gerekmez. Budist düşüncedeki eylem-sonuç ilişkisine benzetirsek, girdiler koşulları; dönüş değeri ise bu koşullardan doğan sonucu temsil eder.

Buna karşılık aşağıdaki fonksiyon dış duruma bağımlıdır:

```javascript
let vergiOrani = 0.20;

function toplamFiyat(fiyat) {
  console.log("Fiyat hesaplandı"); // Gözlemlenebilir yan etki
  return fiyat * (1 + vergiOrani);
}
```

Sonucu anlamak için `vergiOrani` değişkeninin o andaki değerini bilmeliyiz. Üstelik konsola yazmak da hesaplamanın dışında bir etki üretir. Yan etki mutlaka kötü değildir; programların kullanıcıya ulaşması için ekrana yazması, veri kaydetmesi ve ağla konuşması gerekir. Önemli olan yan etkileri **tanımak, sınırlamak ve yönetmektir**.

| Yaklaşım | Saf fonksiyon | Yan etkili fonksiyon |
|---|---|---|
| Aynı girdide sonuç | Daima aynı | Dış duruma göre değişebilir |
| Test edilebilirlik | Kolay | Ek kurulum gerekebilir |
| Durumla ilişki | Açık parametreler | Gizli bağımlılıklar olabilir |
| Felsefi benzetme | Berrak neden-sonuç | Birbirine bağlı koşullar ağı |

## Değişmezlik: Bırakmak mı, kopyalamak mı?

Değişmezlik, bir veri oluşturulduktan sonra onu yerinde değiştirmemektir. Güncelleme gerektiğinde eski değeri bozmak yerine yeni bir değer üretiriz. Bu yaklaşım, “hiçbir şey değişmez” demez. Tam tersine değişimin sürekli olduğunu kabul eder; fakat geçmiş durumun üzerine kontrolsüzce yazmaz.

```javascript
const sepet = Object.freeze([
  { ad: "Çay", adet: 1 }
]);

const yeniSepet = sepet.map(urun =>
  urun.ad === "Çay" ? { ...urun, adet: urun.adet + 1 } : urun
);
```

Burada `sepet` korunur, `yeniSepet` ise değişimi temsil eder. Böylece zaman içindeki durumları karşılaştırmak, hatayı geri almak ve eşzamanlı işlemleri güvenle yürütmek kolaylaşır.

| Değiştirilebilir durum | Değişmez veri |
|---|---|
| Aynı nesne güncellenir | Yeni bir değer oluşturulur |
| Geçmiş bilgi kaybolabilir | Önceki sürüm korunabilir |
| Paylaşım yarış koşulu doğurabilir | Paralel kullanım daha güvenlidir |
| “Bu ne zaman değişti?” sorusu zordur | Veri akışı daha görünürdür |

## Bağımlı oluş ve fonksiyon bileşimi

Budist felsefedeki bağımlı oluş düşüncesi, olayların tek başına değil koşullarla ortaya çıktığını vurgular. Fonksiyonel programlamada da büyük bir sonucu küçük dönüşümlerin bileşimi olarak ifade edebiliriz:

$$h(x) = (g \circ f)(x) = g(f(x))$$

```javascript
const temizle = metin => metin.trim().toLowerCase();
const selamla = ad => `Merhaba, ${ad}!`;
const mesajOlustur = ad => selamla(temizle(ad));
```

Her adım açık, bağımsız ve sınanabilirdir. Karmaşık davranış, gizli mutasyonlardan değil küçük fonksiyonların düzenli ilişkisinden doğar.

## Yan etkisiz hayat mümkün mü?

Tamamen yan etkisiz bir program, kullanıcıdan veri alamaz ve sonuç gösteremez; tamamen etkisiz bir hayat da pek hayat sayılmazdı. Fonksiyonel yaklaşımın hedefi dünyadan kaçmak değil, dünya ile temas edilen sınırları görünür kılmaktır. Hesaplamaları saf merkezde tutup ağ, dosya ve arayüz işlemlerini dış katmanlara taşıyabiliriz.

Sonuçta iyi kod da dengeli bir zihin gibi davranır: Neye bağlı olduğunu bilir, geçmişi gizlice değiştirmez ve ürettiği etkinin sorumluluğunu taşır. Nirvana garanti değil; fakat daha öngörülebilir testler ve daha huzurlu hata ayıklama oldukça gerçekçidir.
