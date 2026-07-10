---
layout: post
title: "JavaScript ile Tarayıcı Üzerinde Sosyolojik Deneyler"
math: true
categories: 
  - Proje
tags: 
  - JavaScript
  - DOM Manipülasyonu
  - Kullanıcı Davranışı
  - Psikoloji Testleri
---

Tarayıcı, sadece butonlara tıkladığımız bir ekran değil; aynı zamanda küçük ölçekli davranış deneyleri yapabileceğimiz harika bir laboratuvardır. JavaScript sayesinde kullanıcıların seçimlerini, tepki sürelerini, dikkat kaymalarını ve karar örüntülerini analiz eden etkileşimli psikoloji ya da zeka testleri tasarlayabiliriz. Elbette burada amaç “insanı çözmek” değil; etik sınırlar içinde, anonim ve öğretici deneyimler üretmektir.
``

Bu tür uygulamaların temelinde üç kavram vardır: **uyaran**, **tepki** ve **ölçüm**. Uyaran; ekranda gösterilen soru, görsel, renk ya da görevdir. Tepki; kullanıcının tıklaması, yazması, sürüklemesi veya beklemesidir. Ölçüm ise bu tepkinin zamana, doğruluğa veya tutarlılığa göre sayısallaştırılmasıdır. Basit bir modelle kullanıcı davranış skoru şöyle düşünülebilir: $S = w_1 x_1 + w_2 x_2 + w_3 x_3$. Burada $x$ değerleri davranış ölçümlerini, $w$ değerleri ise bu ölçümlerin ağırlıklarını temsil eder.

Daha genel biçimde, bir test puanını şu şekilde ifade edebiliriz:

$$S = \sum_{i=1}^{n} w_i x_i$$

Bu formül bize şunu söyler: Her cevap aynı önemde olmak zorunda değildir. Örneğin bir hafıza testinde doğru cevap kadar cevap verme süresi de anlamlı olabilir.

| Ölçüm Türü | Ne Anlatır? | JavaScript ile Nasıl Yakalanır? |
|---|---|---|
| Tepki süresi | Karar hızı | `performance.now()` |
| Tıklama seçimi | Tercih yönelimi | `click` event |
| Hata sayısı | Dikkat veya bilgi düzeyi | Sayaç değişkenleri |
| Sıralama davranışı | Öncelik algısı | Drag & drop olayları |

Dinamik DOM manipülasyonu burada sahnenin ışıkçısı gibidir. Kullanıcı bir soruya cevap verdiğinde yeni soru gösterilir, renkler değişir, sonuç ekranı oluşturulur veya zorluk seviyesi artırılır. Böylece sayfa yenilenmeden akıcı bir deney tasarlanır.

Aşağıdaki örnek, basit bir dikkat testi mantığını gösterir. Kullanıcıdan ekranda beliren hedef renge mümkün olduğunca hızlı tıklaması istenir:

```js
const app = document.querySelector('#app');
const colors = ['red', 'blue', 'green', 'purple'];
let startTime = 0;
let results = [];

function newRound() {
  const target = colors[Math.floor(Math.random() * colors.length)];
  startTime = performance.now();

  app.innerHTML = `
    <p>Hedef renk: <strong>${target}</strong></p>
    <div class='grid'>
      ${colors.map(color => `<button class='box' data-color='${color}' style='background:${color}'></button>`).join('')}
    </div>
  `;

  document.querySelectorAll('.box').forEach(button => {
    button.addEventListener('click', () => {
      const reaction = performance.now() - startTime;
      const correct = button.dataset.color === target;
      results.push({ reaction, correct });
      showFeedback(correct, reaction);
    });
  });
}

function showFeedback(correct, reaction) {
  app.innerHTML = `
    <p>${correct ? 'Doğru!' : 'Yanlış!'}</p>
    <p>Tepki süresi: ${Math.round(reaction)} ms</p>
    <button id='next'>Yeni Tur</button>
  `;
  document.querySelector('#next').addEventListener('click', newRound);
}

newRound();
```

Bu kodda `performance.now()` milisaniye hassasiyetinde zaman ölçer. Kullanıcının doğru renge tıklayıp tıklamadığı `dataset` üzerinden kontrol edilir. DOM, her turda yeniden çizilerek testin akışı yönetilir.

| Yaklaşım | Avantaj | Risk |
|---|---|---|
| Sabit sorular | Kolay analiz | Ezberlenebilir |
| Rastgele uyaran | Daha doğal veri | Karşılaştırma zorlaşır |
| Zaman ölçümü | Hızlı içgörü | Cihaz farklarından etkilenir |
| Kişiselleştirme | Etkileşim artar | Gizlilik sorumluluğu doğar |

Sosyolojik veya psikolojik deneylerde en kritik konu **etik tasarım**dır. Kullanıcıdan açık rıza alınmalı, veriler anonimleştirilmeli ve sonuçlar kesin tanı gibi sunulmamalıdır. “Zekan 142 çıktı” demek yerine “Bu mini testte hızlı örüntü tanıma eğilimi gösterdin” demek çok daha sağlıklıdır.

Sonuç ekranı da davranış analizi kadar önemlidir. Kullanıcıya grafikler, ortalama tepki süresi ve doğru cevap oranı gösterilebilir. Örneğin doğruluk oranı $D = doğru / toplam$ formülüyle hesaplanır. Bu basit oran, anlaşılır bir geri bildirim üretir.

JavaScript ile tarayıcı üzerinde böyle deneyler tasarlamak; DOM, event yönetimi, veri modelleme ve kullanıcı deneyimi bilgisini aynı projede buluşturur. Küçük başlayın: üç soru, bir sayaç ve basit bir skor ekranı yeterli. Sonra rastgeleleştirme, grafikler, localStorage ve erişilebilirlik ekleyerek projenizi gerçek bir interaktif araştırma aracına dönüştürebilirsiniz.
