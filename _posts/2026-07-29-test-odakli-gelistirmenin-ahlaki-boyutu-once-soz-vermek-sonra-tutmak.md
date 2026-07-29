---
layout: post
title: "Test Odaklı Geliştirmenin Ahlaki Boyutu: Önce Söz Vermek, Sonra Tutmak"
math: true
categories: 
  - Bilgi
tags: 
  - TDD
  - yazılım etiği
  - test otomasyonu
---

Bir testi üretim kodundan önce yazmak, yalnızca teknik bir çalışma yöntemi değildir. Geliştirici önce sistemin nasıl davranması gerektiğini açıkça söyler, ardından bu sözü yerine getiren kodu üretir. Bu açıdan Test Odaklı Geliştirme (TDD), küçük ama tekrarlanan etik taahhütlerden oluşur: Beklentiyi görünür kıl, başarısızlığı saklama ve verdiğin sözü doğrulanabilir biçimde tut.

``

## TDD döngüsünü ahlaki bir sözleşme olarak okumak

Klasik TDD döngüsü üç adımdan oluşur: **Red, Green, Refactor**. Önce başarısız bir test yazılır; sonra testi geçirecek en küçük çözüm geliştirilir; son olarak davranış bozulmadan tasarım iyileştirilir.

Bu döngünün etik karşılığı şöyle okunabilir:

1. **Red — Söz ver:** Beklenen davranışı koddan önce tanımla.
2. **Green — Sözünü tut:** Yalnızca gerekli davranışı gerçekleştirecek kadar kod yaz.
3. **Refactor — Sözünü daha iyi taşı:** Dışarıya verilen güvenceyi bozmadan iç yapıyı düzelt.

Bir test, çalıştırılabilir bir iddiadır. Sistemin belirli bir girdi için beklenen çıktıyı üretmesi şu şekilde gösterilebilir:

$$f(x) = y$$

Test ise pratikte bu eşitliğin doğrulanmasıdır:

$$T(f, x, y) = \begin{cases}1, & f(x)=y \\ 0, & f(x)\neq y\end{cases}$$

Buradaki önemli nokta, geliştiricinin “çalışıyor” demesi yerine bu iddiayı başkalarının denetimine açmasıdır. Etik değer de tam burada doğar: **kanıtlanabilir dürüstlük**.

## Sonradan test etmekle önce söz vermek aynı mı?

| Yaklaşım | Temel soru | Etik risk | Sağladığı güvence |
|---|---|---|---|
| Testi sonra yazmak | “Yazdığım kod çalışıyor mu?” | Testin mevcut uygulamaya göre şekillenmesi | Regresyonlara karşı koruma |
| TDD uygulamak | “Kod hangi sözü yerine getirmeli?” | Yanlış veya eksik gereksinimi erkenden fark etme | Tasarım öncesi açık taahhüt |
| Testsiz geliştirmek | “Bence çalışıyor mu?” | Bilginin kişisel kanaate dayanması | Çoğunlukla manuel güven |

Sonradan yazılan testler değersiz değildir. Ancak geliştirici mevcut çözümü gördüğü için testleri farkında olmadan o çözüme uydurabilir. TDD, beklentiyi uygulamadan önce kayda geçirerek bu bilişsel yanlılığı azaltır.

## Küçük bir söz, çalışan bir örnek

Bir para transferinde negatif tutarın reddedilmesi gerektiğini düşünelim. Önce beklentiyi tanımlarız:

```javascript
import { describe, expect, it } from "vitest";
import { transfer } from "./transfer.js";

describe("transfer", () => {
  it("negatif transfer tutarını reddeder", () => {
    expect(() => transfer(1000, -50))
      .toThrow("Tutar pozitif olmalıdır");
  });

  it("geçerli tutarı bakiyeden düşer", () => {
    expect(transfer(1000, 250)).toBe(750);
  });
});
```

Bu testler yalnızca fonksiyonu sınamaz; ürünün iki davranışsal sözünü ilan eder. Ardından en küçük uygulama gelir:

```javascript
export function transfer(balance, amount) {
  if (amount <= 0) {
    throw new Error("Tutar pozitif olmalıdır");
  }

  if (amount > balance) {
    throw new Error("Yetersiz bakiye");
  }

  return balance - amount;
}
```

Kod, negatif tutarı ve yetersiz bakiyeyi reddederek finansal durumun sessizce bozulmasını önler. Testlerin yeşil olması mutlak doğruluk anlamına gelmez; yalnızca ifade edilen sözlerin tutulduğunu gösterir. Yazılmamış bir gereksinim hâlâ görünmezdir.

## Testler kime karşı sorumluluktur?

TDD, geliştiricinin yalnızca kendisine değil; ekip arkadaşlarına, kullanıcılara ve gelecekte sistemi sürdürecek kişilere karşı sorumluluğunu somutlaştırır. İyi bir test, “Bana güven” demez; “İddiamı istediğin zaman kontrol edebilirsin” der.

Bununla birlikte test kapsamını ahlaki bir puan tablosuna çevirmemek gerekir. Örneğin $\%100$ kapsam, $\%100$ güven demek değildir. Anlamlı güven yaklaşık olarak şöyle düşünülebilir:

$$Güven \approx Kapsam \times Senaryo\ Kalitesi \times Test\ Bağımsızlığı$$

Faktörlerden biri zayıfsa sonuç da zayıflar. TDD’nin gerçek ahlaki gücü test sayısından değil; beklentileri dürüstçe belirtmekten, başarısızlığı görünür tutmaktan ve değişikliklerin sonuçlarını üstlenmekten gelir. Kısacası önce test yazmak, makineye emir vermekten çok insanlara söz vermektir.
