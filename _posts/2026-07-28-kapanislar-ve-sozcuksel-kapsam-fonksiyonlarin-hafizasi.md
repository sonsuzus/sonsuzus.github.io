---
layout: post
title: "Kapanışlar ve Sözcüksel Kapsam: Fonksiyonların Hafızası"
math: true
categories: 
  - Bilgi
tags: 
  - closures
  - sözcüksel kapsam
  - JavaScript
---

Bir fonksiyon çalışmasını tamamladığında yerel değişkenlerinin ortadan kaybolmasını bekleriz. Ancak kapanışlar, iç içe geçmiş fonksiyonlara şaşırtıcı bir yetenek kazandırır: İç fonksiyon, onu oluşturan dış fonksiyon çoktan sona ermiş olsa bile dış kapsamdaki değişkenlere erişebilir. Bu davranış sihir değil; sözcüksel kapsam, fonksiyon değerleri ve çalışma zamanı ortamlarının birlikte çalışmasının sonucudur.
``

## Sözcüksel kapsam nedir?

Sözcüksel ya da leksik kapsam, bir değişkenin nereden erişilebilir olduğunun program çalıştırılırken değil, kodun **yazıldığı yapıya** göre belirlenmesidir. İçteki fonksiyon kendi yerel değişkenlerini, dış fonksiyonun değişkenlerini ve küresel kapsamı görebilir.

```javascript
const birim = "TL";

function fiyatEtiketi(fiyat) {
  const vergi = 0.20;

  function hesapla() {
    return `${fiyat * (1 + vergi)} ${birim}`;
  }

  return hesapla;
}
```

Burada `hesapla`, kendi kapsamında bulunmayan `fiyat`, `vergi` ve `birim` isimlerini dış çevrelerde arar. Bu arama ilişkisi, fonksiyonun çağrıldığı yere göre değişmez. Fonksiyon hangi sözcüksel çevrede **tanımlandıysa** o çevreyle bağlantılıdır.

| Özellik | Sözcüksel kapsam | Dinamik kapsam |
|---|---|---|
| Değişken arama ölçütü | Kodun tanımlanma yapısı | Çağrı zinciri |
| Ne zaman belirlenir? | Büyük ölçüde yazım/derleme sırasında | Çalışma sırasında |
| Öngörülebilirlik | Genellikle yüksektir | Çağırana bağlıdır |
| Modern JavaScript | Kullanılır | Kullanılmaz |

## Kapanış nasıl oluşur?

Teorik olarak bir fonksiyon yalnızca çalıştırılabilir kod değildir. Fonksiyon değeri, kod ile tanımlandığı çevrenin birleşimi olarak düşünülebilir:

$$\text{Closure} = \text{Function Code} + \text{Lexical Environment}$$

Bir başka gösterimle fonksiyon değerini $(\lambda x.e, \rho)$ çifti şeklinde modelleyebiliriz. Burada $\lambda x.e$ fonksiyonun gövdesini, $\rho$ ise serbest değişkenlerin çözümleneceği ortamı temsil eder. Bir değişken fonksiyonun parametresi veya yerel tanımı değilse **serbest değişken** sayılır.

Yukarıdaki `hesapla` fonksiyonu açısından `fiyat`, `vergi` ve `birim` serbest değişkenlerdir. Çalışma zamanı bu isimleri ilgili çevre kayıtlarıyla ilişkilendirir. Dış fonksiyon bitince çevre hemen silinmez; döndürülen iç fonksiyon ona hâlâ ulaşabildiği için çöp toplayıcı bu ortamı canlı tutar.

## Hafızası olan fonksiyon üretmek

Kapanışların klasik kullanım alanlarından biri, özel durumu koruyan fonksiyonlar üretmektir:

```javascript
function sayacOlustur(baslangic = 0) {
  let deger = baslangic;

  return function artir(miktar = 1) {
    deger += miktar;
    return deger;
  };
}

const ziyaretSayaci = sayacOlustur(10);
console.log(ziyaretSayaci());  // 11
console.log(ziyaretSayaci(3)); // 14
```

`sayacOlustur` ilk çağrıdan sonra tamamlanır; fakat `artir` fonksiyonu `deger` değişkenini kullanmaya devam eder. Üstelik kapanış yalnızca eski değerin fotoğrafını saklamaz. Saklanan şey, değişkenin bulunduğu çevreye erişimdir; bu nedenle `deger` her çağrıda güncellenebilir.

Aynı üreticiden iki sayaç oluşturulursa bağımsız çevreler elde edilir:

```javascript
const a = sayacOlustur();
const b = sayacOlustur(100);

a(); // 1
b(); // 101
```

| Yaklaşım | Durumun konumu | Dışarıdan erişim | Tipik kullanım |
|---|---|---|---|
| Küresel değişken | Küresel kapsam | Kolay ve riskli | Basit betikler |
| Nesne özelliği | Nesne üzerinde | Genellikle açık | Veri modelleri |
| Kapanış | Sözcüksel çevrede | Kontrollü | Sayaçlar, fabrikalar, önbellek |

## Güçlü ama sınırsız değil

Kapanışlar veri gizleme, olay işleyicileri, kısmi uygulama ve önbellekleme için çok kullanışlıdır. Yine de büyük nesneleri gereksiz yere yakalayan uzun ömürlü fonksiyonlar bellek tüketimini artırabilir. Özellikle olay dinleyicileri kaldırılmadığında ilgili çevreler de erişilebilir kalabilir.

Özetle kapanış, dış fonksiyonun çalışmasını sonsuza kadar sürdürmez; yalnızca ihtiyaç duyulan sözcüksel çevrenin yaşam süresini uzatır. Fonksiyon böylece kod taşıyan bir kutudan fazlasına dönüşür: Nerede doğduğunu hatırlayan, kontrollü ve durum sahibi bir davranış birimi olur.
