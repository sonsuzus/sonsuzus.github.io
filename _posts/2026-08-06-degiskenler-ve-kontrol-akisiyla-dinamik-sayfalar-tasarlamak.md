---
layout: post
title: "Değişkenler ve Kontrol Akışıyla Dinamik Sayfalar Tasarlamak"
math: true
categories: 
  - Bilgi
tags: 
  - değişkenler
  - kontrol akışı
  - javascript
---

Bir web sayfasının kullanıcıya göre farklı davranmasını sağlayan temel güç, değişkenler ve kontrol akış yapılarından gelir. Değişkenler verileri hafızada tutarken `if-else` ve `switch-case` gibi yapılar programın hangi kod yolunu izleyeceğine karar verir. Kısacası değişkenler sahnedeki oyuncuları, kontrol yapıları ise senaryoyu temsil eder.

``

## Değişkenler Neden Gereklidir?

Değişken, bir değeri program çalışırken saklayabilmek ve daha sonra kullanabilmek için verilen isimdir. Kullanıcının adı, ürün fiyatı, oturum durumu veya sepetteki ürün sayısı birer değişkende tutulabilir.

JavaScript'te modern değişken tanımlama işlemleri genellikle `let` ve `const` ile gerçekleştirilir:

```javascript
const kullaniciAdi = 'Ada';
let sepetAdedi = 2;
let oturumAcik = true;

sepetAdedi = sepetAdedi + 1;
console.log(`${kullaniciAdi} kullanıcısının sepetinde ${sepetAdedi} ürün var.`);
```

Burada `const`, yeniden atanmayacak bir değişken oluşturur. `let` ise değeri sonradan değiştirilebilen veriler için kullanılır. Sepete yeni ürün eklendiğinde `sepetAdedi` güncellenebilir; ancak kullanıcının o işlem boyunca değişmeyen adı `const` ile tanımlanabilir.

| Anahtar kelime | Yeniden atanabilir mi? | Kapsam | Önerilen kullanım |
|---|---:|---|---|
| `const` | Hayır | Blok | Varsayılan tercih |
| `let` | Evet | Blok | Değişecek değerler |
| `var` | Evet | Fonksiyon | Eski kodlarla uyumluluk |

Değişkenlerin hafızadaki davranışı veri türüne göre farklılaşabilir. Sayı ve boolean gibi ilkel değerler doğrudan değer mantığıyla kullanılırken nesneler referans üzerinden yönetilir. Bu nedenle bir nesneyi başka değişkene atamak her zaman bağımsız bir kopya üretmez.

## Koşulların Matematiksel Mantığı

Kontrol akışının merkezinde sonucu `true` veya `false` olan ifadeler bulunur. Örneğin yaş değişkeni $y$ ise yetişkinlik koşulu $y \geq 18$ biçiminde gösterilebilir. İki şartın birlikte sağlanması gerekiyorsa mantıksal VE, alternatiflerden biri yeterliyse mantıksal VEYA kullanılır.

| Mantıksal işlem | JavaScript | Sonucun doğru olma durumu |
|---|---|---|
| VE | `A && B` | İki koşul da doğruysa |
| VEYA | `A \|\| B` | En az bir koşul doğruysa |
| DEĞİL | `!A` | A yanlışsa |

## `if-else` ile Sayfa Akışını Yönetmek

`if-else`, farklı ve esnek koşulları değerlendirmek için idealdir. Bir üyelik sayfasının kullanıcı durumuna göre mesaj göstermesi şöyle sağlanabilir:

```javascript
const yas = 22;
const oturumAcik = true;

if (!oturumAcik) {
  console.log('Lütfen önce giriş yapın.');
} else if (yas >= 18) {
  console.log('Yetişkin içerik alanına hoş geldiniz.');
} else {
  console.log('Bu bölüm için yaşınız uygun değil.');
}
```

Program koşulları yukarıdan aşağıya değerlendirir ve doğru olan ilk bloğu çalıştırır. Bu nedenle daha özel koşulları üstte, genel koşulları altta konumlandırmak hatalı yönlendirmeleri önler.

## `switch-case` Ne Zaman Kullanılır?

Tek bir değişkenin birçok sabit değerle karşılaştırıldığı durumlarda `switch-case` daha okunaklı olabilir. Örneğin kullanıcının rolüne göre panel seçilebilir:

```javascript
const rol = 'editor';
let hedefSayfa;

switch (rol) {
  case 'admin':
    hedefSayfa = '/yonetim';
    break;
  case 'editor':
    hedefSayfa = '/icerikler';
    break;
  case 'uye':
    hedefSayfa = '/profil';
    break;
  default:
    hedefSayfa = '/giris';
}

console.log(`Yönlendirilecek adres: ${hedefSayfa}`);
```

`break` kullanılmazsa program sonraki `case` bloklarına da geçebilir. Bazen bilinçli olarak kullanılan bu davranış, çoğu başlangıç hatasının da kaynağıdır. `default` ise hiçbir eşleşme bulunmadığında güvenli bir varsayılan yol sağlar.

## Hangisini Seçmeliyiz?

Aralıklar, birleşik mantıksal ifadeler ve karmaşık kurallar için `if-else`; tek bir değerin belirli seçeneklerle eşleştirilmesi için `switch-case` tercih edilmelidir. Koşullar büyüdükçe karar mantığını küçük fonksiyonlara ayırmak kodun test edilmesini kolaylaştırır. Böylece sayfa akışı bir labirente değil, tabelaları düzgün yerleştirilmiş eğlenceli bir yolculuğa dönüşür.
