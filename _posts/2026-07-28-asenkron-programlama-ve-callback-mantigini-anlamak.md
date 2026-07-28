---
layout: post
title: "Asenkron Programlama ve Callback Mantığını Anlamak"
math: true
categories: 
  - Bilgi
tags: 
  - JavaScript
  - Asenkron Programlama
  - Callback
---

Bir web sayfası veri indirirken düğmeler çalışmıyor, animasyonlar takılıyor ve kullanıcı boş boş ekrana bakıyorsa tarayıcı muhtemelen uzun bir işlem tarafından meşgul edilmiştir. Asenkron programlama; ağ isteği, zamanlayıcı veya dosya okuma gibi sonucu hemen hazır olmayan işleri beklerken ana akışın çalışmaya devam etmesini sağlar. Callback, yani geri çağırım fonksiyonu ise işlem tamamlandığında “Bitti, şimdi ne yapayım?” sorusuna verilen cevaptır.
``

## Senkron ve asenkron çalışma

JavaScript temel olarak **tek iş parçacıklı** çalışır. Başka bir ifadeyle aynı anda yalnızca bir JavaScript komutu yürütülür. Senkron kodda her işlem, sıradaki işlemin başlamasından önce tamamlanmalıdır. Uzun süren bir görev bu sırayı bloke ederse kullanıcı arayüzü de yanıt veremez.

Asenkron yapıda ise JavaScript, bekleme gerektiren görevi tarayıcının Web API sistemine teslim eder ve diğer komutları yürütür. Görev tamamlandığında ilgili callback kuyruğa eklenir. Buradaki önemli ayrıntı şudur: Callback hemen çalışmaz; **call stack**, yani çağrı yığını boşaldığında çalışabilir.

| Özellik | Senkron çalışma | Asenkron çalışma |
|---|---|---|
| İşlem sırası | Bir görev bitmeden diğeri başlamaz | Bekleyen görev sırasında akış sürer |
| Arayüz etkisi | Uzun işlem ekranı dondurabilir | Bekleme işlemlerinde arayüz kullanılabilir |
| Sonuç yönetimi | Sonuç doğrudan alınır | Callback, Promise veya `async/await` kullanılır |
| Uygun örnek | Basit matematik hesabı | Veri çekme, zamanlayıcı, kullanıcı olayı |

Bir işlemin toplam bekleme süresini kabaca şu şekilde düşünebiliriz:

$$T_{toplam} = T_{başlatma} + T_{bekleme} + T_{callback}$$

Asenkronluk $T_{bekleme}$ değerini yok etmez. Yalnızca JavaScript’in bu süre boyunca başka işlerle ilgilenebilmesini sağlar.

## Callback nasıl çalışır?

Callback, başka bir fonksiyona argüman olarak verilen ve uygun zamanda çağrılan fonksiyondur. En bilinen örneklerden biri `setTimeout` kullanımıdır:

```javascript
console.log("Sipariş alındı");

setTimeout(() => {
  console.log("Sipariş hazır!");
}, 2000);

console.log("Bu sırada başka müşteriye bakılıyor");
```

Çıktıda “Sipariş hazır!” mesajı en son görünür. `setTimeout`, callback’i iki saniye sonra doğrudan çalıştırmaz; en az iki saniye geçtikten sonra görev kuyruğuna gönderir. Event loop, çağrı yığını boş olduğunda bu görevi yürütür. Dolayısıyla yoğun bir JavaScript işlemi varsa callback daha geç başlayabilir.

## Veri çekme senaryosu

Aşağıdaki fonksiyon, veri isteğinin sonucunu bir callback üzerinden dışarı iletir:

```javascript
function kullaniciGetir(id, tamamlandi) {
  fetch(`https://jsonplaceholder.typicode.com/users/${id}`)
    .then(response => {
      if (!response.ok) {
        throw new Error("Kullanıcı bulunamadı");
      }
      return response.json();
    })
    .then(data => tamamlandi(null, data))
    .catch(error => tamamlandi(error, null));
}

kullaniciGetir(1, (hata, kullanici) => {
  if (hata) {
    console.error(hata.message);
    return;
  }

  console.log(`Merhaba ${kullanici.name}!`);
});
```

Burada `tamamlandi` fonksiyonu **error-first callback** yaklaşımını kullanır: İlk parametre hata, ikinci parametre başarılı sonuçtur. Ağ isteği sürerken tarayıcı diğer olayları işlemeye devam eder. İstek sonuçlandığında callback uygun kuyruğa alınır.

## Her uzun işlem asenkron değildir

Ağ istekleri tarayıcı altyapısına devredilebilir; fakat milyonlarca elemanı hesaplayan yoğun bir döngü otomatik olarak arka plana taşınmaz. Böyle bir CPU işlemi ana iş parçacığını yine dondurur. Ağır hesaplamalar için **Web Worker**, görevleri parçalara bölme veya sunucu tarafında işleme gibi çözümler gerekir.

Callback’ler küçük senaryolarda anlaşılırdır; ancak iç içe kullanıldıklarında “callback hell” adı verilen karmaşık bir yapı oluşturabilir. Modern JavaScript’te Promise ve `async/await`, aynı asenkron mantığı daha okunabilir biçimde ifade eder. Yine de event loop ve callback temelini anlamak, bu modern yapıların perde arkasında neden ve nasıl çalıştığını kavramanın en sağlam yoludur.
