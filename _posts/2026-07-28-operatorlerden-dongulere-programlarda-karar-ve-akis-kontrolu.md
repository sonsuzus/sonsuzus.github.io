---
layout: post
title: "Operatörlerden Döngülere: Programlarda Karar ve Akış Kontrolü"
math: true
categories: 
  - Bilgi
tags: 
  - operatörler
  - akış kontrolü
  - döngüler
---

Bir programı yalnızca sırayla çalışan komutlar bütünü olmaktan çıkaran şey, karar verebilmesi ve belirli işlemleri tekrarlayabilmesidir. Operatörler verileri işlerken akış kontrol yapıları programın hangi yoldan ilerleyeceğini belirler. Kısacası operatörler mutfaktaki araçlar, koşullar ve döngüler ise şefin tarif planıdır.
``

## Operatörlerin Temel Mantığı

Operatör, bir veya daha fazla değer üzerinde işlem yapan semboldür. Örneğin `5 + 3` ifadesinde `+` operatör, `5` ve `3` ise operand olarak adlandırılır. Matematiksel açıdan bu işlem $f(a,b)=a+b$ biçiminde düşünülebilir.

### Aritmetik operatörler

Aritmetik operatörler sayısal hesaplamalarda kullanılır:

| Operatör | İşlem | Örnek | Sonuç |
|---|---|---|---|
| `+` | Toplama | `8 + 2` | `10` |
| `-` | Çıkarma | `8 - 2` | `6` |
| `*` | Çarpma | `8 * 2` | `16` |
| `/` | Bölme | `8 / 2` | `4` |
| `%` | Kalan | `8 % 3` | `2` |
| `**` | Üs alma | `2 ** 3` | `8` |

Kalan operatörü özellikle bir sayının çift olup olmadığını anlamakta kullanışlıdır. Bir $n$ sayısı için $n \bmod 2=0$ ise sayı çifttir.

```javascript
const sayi = 14;
const ciftMi = sayi % 2 === 0;
console.log(ciftMi); // true
```

Bu kod, bölme işleminin sonucuna değil kalanına bakarak sayı hakkında karar verir.

### Karşılaştırma ve mantıksal operatörler

Karşılaştırma operatörleri `true` veya `false` üretir. Mantıksal operatörler ise birden fazla koşulu birleştirir.

| Tür | Operatörler | Anlam |
|---|---|---|
| Karşılaştırma | `>`, `<`, `>=`, `<=` | Büyüklük ilişkisi |
| Eşitlik | `===`, `!==` | Değer ve tür eşitliği/eşitsizliği |
| Mantıksal VE | `&&` | Tüm koşullar doğru olmalı |
| Mantıksal VEYA | `\|\|` | En az bir koşul doğru olmalı |
| Mantıksal DEĞİL | `!` | Sonucu tersine çevirir |

`A && B` ifadesi yalnızca iki koşul da doğruysa doğrudur. `A || B` için tek bir doğru yeterlidir. Bu davranışlar sırasıyla matematikteki $A \land B$ ve $A \lor B$ ifadelerine karşılık gelir.

## Karar Yapıları

`if-else`, koşula göre farklı kodların çalıştırılmasını sağlar:

```javascript
const yas = 20;
const biletiVar = true;

if (yas >= 18 && biletiVar) {
  console.log("Etkinliğe girebilirsiniz.");
} else if (yas < 18) {
  console.log("Yaş sınırı karşılanmıyor.");
} else {
  console.log("Bilet gerekli.");
}
```

Burada koşullar yukarıdan aşağıya değerlendirilir ve ilk doğru dal çalıştırılır. Çok sayıda sabit değerin karşılaştırıldığı durumlarda `switch-case` daha okunaklı olabilir:

```javascript
const rol = "editor";

switch (rol) {
  case "admin":
    console.log("Tam yetki verildi.");
    break;
  case "editor":
    console.log("İçerik düzenleme yetkisi verildi.");
    break;
  default:
    console.log("Salt okunur erişim verildi.");
}
```

`break`, eşleşen bölüm tamamlandıktan sonra diğer seçeneklere geçilmesini önler.

## Döngü Mekanizmaları

Döngüler, bir işlemi koşul sağlandığı sürece tekrarlar. `for`, tekrar sayısı biliniyorsa; `while`, tekrarın bir koşula bağlı olduğu durumlarda tercih edilir.

```javascript
let toplam = 0;

for (let i = 1; i <= 5; i++) {
  toplam += i;
}

console.log(toplam); // 15
```

Bu döngü $1+2+3+4+5=15$ toplamını hesaplar. Aynı fikir `while` ile şöyle kurulabilir:

```javascript
let enerji = 3;

while (enerji > 0) {
  console.log(`Kalan enerji: ${enerji}`);
  enerji--;
}
```

Döngülerde koşulun bir noktada yanlış olması gerekir; aksi hâlde sonsuz döngü oluşur. `break` döngüyü tamamen sonlandırırken `continue` yalnızca mevcut turu atlar. Doğru operatörü doğru kontrol yapısıyla birleştirmek, hem okunabilir hem de hatalara karşı dayanıklı programların temelidir.
