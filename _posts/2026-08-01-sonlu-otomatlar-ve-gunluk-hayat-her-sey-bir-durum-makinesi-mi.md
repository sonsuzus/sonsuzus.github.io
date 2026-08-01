---
layout: post
title: "Sonlu Otomatlar ve Günlük Hayat: Her Şey Bir Durum Makinesi mi?"
math: true
categories: 
  - Bilgi
tags: 
  - sonlu otomatlar
  - teorik bilgisayar bilimi
  - durum makineleri
---

Sabah alarmı çalar, ertelersin, yeniden çalar ve sonunda yataktan kalkarsın. Kavşakta kırmızı söner, yeşil yanar; bir süre sonra sıra sarıya gelir. Bu olaylar farklı görünse de ortak bir fikir taşır: Sistem, bulunduğu **duruma** ve aldığı **girdiye** göre başka bir duruma geçer. Teorik bilgisayar biliminde bu davranışı modellemek için sonlu otomatlardan yararlanırız.
``
## Sonlu otomat nedir?

Sonlu otomat, sınırlı sayıda duruma sahip soyut bir hesaplama modelidir. Bir deterministik sonlu otomat, matematiksel olarak şu beşliyle gösterilir:

$$M=(Q,\Sigma,\delta,q_0,F)$$

Burada:

- $Q$, mümkün durumların sonlu kümesidir.
- $\Sigma$, sistemin kabul ettiği girdilerin alfabesidir.
- $\delta$, geçiş fonksiyonudur.
- $q_0$, başlangıç durumudur.
- $F$, kabul durumlarının kümesidir.

Geçiş fonksiyonu ise mevcut durum ile girdiyi yeni duruma bağlar:

$$\delta:Q\times\Sigma\rightarrow Q$$

Yani otomat, “Geçmişte tam olarak neler yaşandı?” diye bütün hikâyeyi saklamaz. Karar vermek için yalnızca mevcut durumunda kodlanmış sınırlı bilgiyi kullanır. Bu özellik, modeli hem güçlü hem de sınırlı yapar.

## Trafik ışığı: Klasik durum makinesi

Basitleştirilmiş bir trafik ışığının üç durumu olsun: kırmızı, yeşil ve sarı. Zamanlayıcı sinyali geldiğinde sistem bir sonraki duruma geçsin.

| Mevcut durum | Girdi | Sonraki durum | Eylem |
|---|---|---|---|
| Kırmızı | Süre doldu | Yeşil | Araçlara geçiş ver |
| Yeşil | Süre doldu | Sarı | Geçişin biteceğini bildir |
| Sarı | Süre doldu | Kırmızı | Araçları durdur |

Bu model deterministiktir; aynı durumda aynı girdi her zaman aynı sonucu üretir. Gerçek kavşaklarda yaya düğmeleri, sensörler ve acil araç sinyalleri bulunduğundan geçiş tablosu büyür. Yine de temel mantık değişmez.

Aşağıdaki JavaScript kodu bu çevrimi canlandırır:

```javascript
const transitions = {
  kirmizi: "yesil",
  yesil: "sari",
  sari: "kirmizi"
};

let state = "kirmizi";

function timerExpired() {
  state = transitions[state];
  console.log(`Yeni durum: ${state}`);
}

setInterval(timerExpired, 2000);
```

`transitions` nesnesi geçiş fonksiyonunu temsil eder. `timerExpired` çağrıldığında mevcut durum okunur ve karşılık gelen yeni durum atanır. Böylece koşul yığınları yerine modelin yapısı doğrudan kodda görünür.

## Alışkanlıklar da otomat olabilir mi?

Bir çalışma alışkanlığını “boşta”, “hazırlanıyor”, “odaklanmış” ve “mola” durumlarıyla modelleyebiliriz. Masaya oturmak hazırlığı, zamanlayıcıyı başlatmak odaklanmayı, sürenin dolması ise molayı tetikleyebilir.

| Özellik | Trafik ışığı | İnsan alışkanlığı |
|---|---|---|
| Durumlar | Açık ve ölçülebilir | Yoruma açık olabilir |
| Geçişler | Büyük ölçüde sabit | Duygu ve çevreden etkilenir |
| Aynı girdinin sonucu | Genellikle aynıdır | Kişiye ve güne göre değişebilir |
| Bellek ihtiyacı | Sınırlıdır | Geçmiş deneyimler önemli olabilir |

İşte kritik ayrım burada ortaya çıkar: Trafik ışığı iyi tanımlanmış bir makinedir; insan ise her zaman deterministik değildir. “Bildirim geldi” girdisi bir gün dikkati dağıtırken başka bir gün görmezden gelinebilir. Bunu modellemek için olasılıklı geçişler kullanılabilir. Örneğin odaklanmış durumdan dağınık duruma geçiş olasılığı $P(D\mid B)=0.35$ olarak tanımlanabilir.

## Her şey gerçekten durum makinesi mi?

Birçok sistemi durum makinesi **olarak modelleyebiliriz**, fakat bu onların bütünüyle sonlu otomat olduğu anlamına gelmez. Otomatlar; kullanıcı arayüzleri, oyun karakterleri, sipariş süreçleri, turnikeler ve iletişim protokolleri için mükemmeldir. Buna karşılık sınırsız sayma, derin bağlam veya sürekli değerler gerektiren problemler daha güçlü modellere ihtiyaç duyar.

Örneğin sonlu otomat dengeli parantezleri sınırsız uzunlukta doğrulayamaz; kaç parantezin açık kaldığını hatırlamak için yığıt gerekir. Bu görevde **yığıtlı otomat** daha uygundur.

Sonlu otomatların gündelik hayata uygulanmasındaki asıl kazanç, insanı robota indirgemek değildir. Kazanç; karmaşık bir süreci durumlara, girdilere ve geçişlere ayırarak daha net düşünmektir. Bir dahaki sefere “Neden yine erteledim?” diye sorduğunda belki de suçlu karakterin değil, yanlış tasarlanmış geçiş fonksiyonundur!
