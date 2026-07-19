---
layout: post
title: "Özyineleme ile Döngüsel Kontrol: Döngüsüz Tekrarın Zekice Yolu"
math: true
categories: 
  - Bilgi
tags: 
  - özyineleme
  - recursion
  - algoritma
---

Bir listeyi gezmek, bir dizindeki dosyaları taramak ya da ardışık adımlarla sonuca ulaşmak denince akla genellikle for ve while döngüleri gelir. Özyineleme ise aynı işi farklı bir zihinsel modelle yapar: Bir kural, problemin daha küçük bir sürümünü çözmek için kendini yeniden çağırır. Yani kontrol akışı dışarıdan dönen bir çark gibi değil, iç içe açılan matruşka bebekleri gibi ilerler.
``

## Özyinelemenin Temel Fikri

Özyineleme, bir fonksiyonun veya kuralın kendi kendini çağırmasıdır. Ancak bu, sonsuza kadar süren sihirli bir ayna koridoru değildir. Sağlıklı bir özyinelemeli yapı iki parçaya dayanır:

| Parça | Görevi | Basit Soru |
|---|---|---|
| Temel durum | Çağrıları durdurur | Artık cevap belli mi? |
| Özyinelemeli adım | Problemi küçültür | Aynı sorunun daha küçük hali nedir? |

Matematiksel olarak bunu şöyle düşünebiliriz: Bir listenin toplamı için $S(n)$, ilk $n$ elemanın toplamı olsun. O zaman:

$$S(n) = S(n-1) + a_n$$

ve temel durum:

$$S(0) = 0$$

Bu tanımda döngü yoktur ama tekrar vardır. Her çağrı, problemi bir adım küçültür. Liste bittiğinde sonuç geriye doğru taşınır.

## Döngü mü, Özyineleme mi?

Geleneksel döngüler kontrolü açıkça yönetir: sayaç artırılır, koşul kontrol edilir, gövde çalıştırılır. Özyineleme ise kontrolü çağrı zincirine bırakır. Bu yüzden özellikle ağaçlar, klasör yapıları, grafik aramaları ve parçala-fethet algoritmalarında çok doğal görünür.

| Yaklaşım | Kontrol Mantığı | Güçlü Olduğu Yer | Risk |
|---|---|---|---|
| Döngü | Sayaç ve koşul ile ilerler | Düz listeler, basit tekrarlar | Karmaşık iç içe koşullar |
| Özyineleme | Fonksiyon kendini çağırır | Ağaç, alt problem, hiyerarşi | Sonsuz çağrı veya stack taşması |

Örneğin bir listedeki sayıların toplamını özyinelemeyle hesaplayalım:

```js
function toplam(liste, index = 0) {
  if (index === liste.length) return 0;
  return liste[index] + toplam(liste, index + 1);
}

const sonuc = toplam([4, 8, 15, 16]);
console.log(sonuc); // 43
```

Bu kodda `index === liste.length` temel durumdur. Liste bittiğinde sıfır döner. Aksi halde mevcut eleman alınır ve listenin geri kalanı için aynı fonksiyon tekrar çağrılır. Bir döngü yazmadık ama listeyi baştan sona gezdik.

## Çağrı Yığını: Görünmeyen Merdiven

Özyineleme çalışırken her fonksiyon çağrısı bellekte çağrı yığınına eklenir. Bunu bir merdiven gibi düşünebiliriz. Önce aşağı inilir, temel duruma ulaşılır, sonra cevaplar yukarı çıkarken birleşir.

`toplam([4, 8, 15], 0)` çağrısı kabaca şöyle açılır:

```txt
4 + toplam(index 1)
4 + 8 + toplam(index 2)
4 + 8 + 15 + toplam(index 3)
4 + 8 + 15 + 0
```

Zaman karmaşıklığı her elemanı bir kez ziyaret ettiği için $O(n)$ olur. Ancak bellek tarafında da çağrı yığını kullanılır; bu nedenle ek bellek maliyeti genellikle $O(n)$ kabul edilir. Döngüsel çözümde ise çoğu zaman bellek $O(1)$ olabilir.

## Kural Tabanlı Düşünmek

Özyinelemeyi güçlü yapan şey, işlemi emir listesi gibi değil, kural gibi yazmamızdır. Mesela bir listede ilk çift sayıyı bulalım:

```js
function ilkCift(liste, index = 0) {
  if (index >= liste.length) return null;
  if (liste[index] % 2 === 0) return liste[index];
  return ilkCift(liste, index + 1);
}

console.log(ilkCift([3, 7, 10, 12])); // 10
```

Burada strateji nettir: Eğer liste bittiyse yoktur. Mevcut eleman çiftse cevap odur. Değilse aynı aramayı bir sonraki elemandan başlat. Bu ifade biçimi, özellikle kuralların kendi kendini genişlettiği mantıksal programlama, ayrıştırıcılar ve yapay zeka arama problemlerinde çok okunaklıdır.

## Ne Zaman Dikkatli Olmalı?

Özyineleme şık olabilir ama her yere serpilmiş algoritmik pul biber gibi kullanılmamalıdır. Temel durum unutulursa fonksiyon sonsuza kadar kendini çağırır. Çok büyük listelerde çağrı yığını dolabilir. Bazı diller kuyruk özyinelemesini optimize eder, bazıları etmez.

Kuyruk özyinelemesinde son işlem doğrudan özyinelemeli çağrıdır:

```js
function toplamKuyruk(liste, index = 0, acc = 0) {
  if (index === liste.length) return acc;
  return toplamKuyruk(liste, index + 1, acc + liste[index]);
}
```

Burada `acc`, yani biriktirici, ara sonucu taşır. Teorik olarak bu yapı daha kolay optimize edilebilir.

Sonuç olarak özyineleme, döngülerin rakibi değil; tekrar eden işlemleri farklı bir soyutlama katmanında ifade etmenin yoludur. Problem doğal olarak alt problemlere ayrılıyorsa, özyineleme kodu hem daha kısa hem daha açıklayıcı hale getirebilir. Yeter ki şu üç soruyu unutmayalım: Nerede duruyorum, problemi nasıl küçültüyorum ve çağrılar bellekte ne kadar yer kaplıyor?
