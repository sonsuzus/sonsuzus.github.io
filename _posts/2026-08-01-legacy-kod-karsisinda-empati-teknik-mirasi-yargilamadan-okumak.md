---
layout: post
title: "Legacy Kod Karşısında Empati: Teknik Mirası Yargılamadan Okumak"
math: true
categories: 
  - Bilgi
tags: 
  - legacy-code
  - yazılım-kültürü
  - teknik-borç
---

Bir gün yıllardır çalışan bir projeyi açar, 900 satırlık bir metotla karşılaşır ve refleks olarak “Bunu kim yazdı?” diye sorarsınız. Git geçmişi birkaç saniye sonra cevabı verir: Üç yıl önce siz! Legacy kod, yalnızca eski kod değildir; geçmiş kararların, teslim tarihlerinin, eksik bilgilerin ve değişen ihtiyaçların donmuş hâlidir. Bu nedenle onu anlamanın ilk adımı, suçlu aramak yerine dönemin koşullarını araştırmaktır.

``

## Legacy kod neden böyle görünür?

Bugünün standartlarıyla geçmişi değerlendirmek kolaydır. Ancak bir kararın kalitesi yalnızca ortaya çıkan kodla değil, karar verildiği anda mevcut olan bilgilerle ölçülmelidir. Bunu basitçe şöyle düşünebiliriz:

$$Karar\ Kalitesi = \frac{Mevcut\ Bilgi \times Kısıtlar\ Altındaki\ Fayda}{Maliyet + Risk}$$

Bugün bildiğimiz güvenlik açığı, performans sorunu veya tasarım deseni o gün bilinmiyor olabilir. Ekip küçük, teslim tarihi yakın, test altyapısı yetersiz ya da kullanılan framework henüz olgunlaşmamış olabilir. “Neden bunu düzgün yapmamışlar?” sorusu bu değişkenleri görmezden gelir.

| İlk tepki | Empatik soru | Sağladığı kazanım |
|---|---|---|
| “Bu kod korkunç.” | “Bu yapı hangi sorunu hızlıca çözmüş?” | Tarihsel amacı gösterir |
| “Neden test yok?” | “O dönemde test altyapısı var mıydı?” | Eksikliği bağlama yerleştirir |
| “Baştan yazalım.” | “Mevcut davranışın ne kadarını biliyoruz?” | Yeniden yazım riskini azaltır |
| “Yazan kişi beceriksizmiş.” | “Hangi kısıtlar altında çalışmış?” | Kişiyi karardan ayırır |

## Kod arkeolojisi yapmak

Legacy sistemde çalışmak biraz arkeolojiye benzer. Kod görünen eserdir; commit mesajları, hata kayıtları, eski dokümanlar ve ekip üyelerinin anıları ise kazı alanındaki ipuçlarıdır. Önce modülün ne yaptığını değil, neden var olduğunu öğrenmeye çalışın.

Örneğin aşağıdaki koşul gereksiz bir tekrar gibi görünebilir:

```javascript
function calculatePrice(order) {
  // Eski mobil istemciler indirim alanını göndermiyor.
  const discount = order.discount == null ? 0 : order.discount;

  if (order.clientVersion && order.clientVersion < 3) {
    return Math.max(0, order.total - discount);
  }

  return applyModernPricing(order, discount);
}
```

Buradaki sürüm kontrolünü hemen silmek kodu sadeleştirir; fakat eski istemcilerin fiyat hesaplamasını bozabilir. Yorum, davranışın tarihsel nedenini kısmen açıklıyor. Daha iyi yaklaşım; kullanım metriklerini incelemek, eski istemcilerin hâlâ aktif olup olmadığını doğrulamak ve kaldırma kararını testlerle güvenceye almaktır.

## Empati, kötü kodu korumak değildir

Empatik yaklaşım “Hiçbir şeye dokunmayalım” anlamına gelmez. Tam tersine, güvenli değişiklik yapabilmek için sistemi ciddiye almaktır. Kodu yazan kişiyi yargılamamakla teknik sorunları açıkça adlandırmak aynı anda mümkündür.

Sağlıklı bir iyileştirme süreci şu sırayı izleyebilir:

1. Mevcut davranışı karakterizasyon testleriyle kaydet.
2. Kodun çağrıldığı yerleri ve dış bağımlılıkları bul.
3. Küçük, geri alınabilir değişiklikler yap.
4. Gözlemlenebilirlik ekleyerek sonucu ölç.
5. Öğrenilen tarihsel bilgiyi dokümante et.

Risk kabaca değişikliğin büyüklüğü ve belirsizlikle artar:

$$Risk \approx Değişiklik\ Boyutu \times Belirsizlik \times Etki\ Alanı$$

Bu yüzden dev bir “temizlik” pull request’i yerine küçük adımlar genellikle daha güvenlidir. Önce test eklemek, ardından isimleri düzeltmek ve son olarak sorumlulukları ayırmak hem incelemeyi hem geri dönüşü kolaylaştırır.

## Dilden kültüre uzanan etki

Kod incelemesinde kullanılan dil ekip kültürünü belirler. “Bu saçma olmuş” yerine “Bu kararın arkasındaki kısıtı biliyor muyuz?” demek yalnızca daha nazik değildir; daha fazla teknik bilgi üretir. İnsanlar yargılanmayacaklarını bildiklerinde eski hataları, geçici çözümleri ve gizli riskleri daha rahat paylaşır.

Unutmayın: Bugünün modern mimarisi de yarının legacy sistemidir. Bize miras kalan kodu merakla okumak, gelecekte kendi kararlarımızın da bağlam içinde değerlendirilmesini istemektir. İyi mühendislik yalnızca temiz kod yazmak değil, kirli görünen kodun hangi fırtınadan çıktığını anlayabilmektir.
