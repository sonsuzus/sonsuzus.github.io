---
layout: post
title: "JavaScript Olay Dinleyicileri: Arayüzün Nabzını Tutmak"
math: true
categories: 
  - Bilgi
tags: 
  - JavaScript
  - Event Listeners
  - Asenkron Programlama
---

Bir web sayfası kullanıcıya yalnızca bilgi gösteriyorsa dijital bir afişten pek farklı değildir. Onu gerçek bir arayüze dönüştüren şey; tıklamaları, tuşları, kaydırmaları ve form girişlerini algılayıp uygun tepkiler verebilmesidir. JavaScript'teki olay dinleyicileri, tarayıcı ile kullanıcı arasındaki bu konuşmayı yönetir.

``

## Olay dinleyicisi nedir?

Olay dinleyicisi, belirli bir DOM elemanında belirli bir olay gerçekleştiğinde çalıştırılmak üzere kaydedilen fonksiyondur. Temel yöntem `addEventListener()` metodudur:

```javascript
const buton = document.querySelector("#kaydet");

buton.addEventListener("click", () => {
  console.log("Kaydet düğmesine tıklandı!");
});
```

Bu kod sürekli çalışan bir döngüyle butonu kontrol etmez. Tarayıcı, dinleyiciyi kaydeder ve tıklama gerçekleştiğinde geri çağırım fonksiyonunu görev kuyruğuna ekler. Böylece gereksiz işlemci kullanımı önlenir.

Bunu basitçe şu maliyet karşılaştırmasıyla düşünebiliriz. Sürekli kontrol yaklaşımında saniyede $n$ kontrol yapılıyorsa yaklaşık maliyet $O(n)$ olur. Olay tabanlı yaklaşımda ise yalnızca gerçekleşen $k$ olay işlenir ve maliyet $O(k)$ seviyesindedir. Genellikle $k \ll n$ olduğundan olay tabanlı tasarım daha verimlidir.

| Yaklaşım | Çalışma biçimi | Avantajı | Dezavantajı |
|---|---|---|---|
| Sürekli kontrol | Durumu tekrar tekrar sorgular | Mantığı basittir | Kaynak tüketebilir |
| Olay dinleme | Olay gerçekleşince çalışır | Verimli ve ölçeklenebilir | Olay akışını anlamak gerekir |
| HTML içi olay | `onclick` niteliği kullanır | Hızlı prototip sağlar | HTML ile JavaScript'i karıştırır |

## Event loop ve asenkron tepki

JavaScript çoğunlukla tek bir ana iş parçacığında çalışır. Buna rağmen kullanıcı etkileşimleri, zamanlayıcılar ve ağ istekleri birbirini tamamen kilitlemeden yönetilebilir. Tarayıcı olayları izler; hazır geri çağırımları kuyruğa koyar. Event loop, çağrı yığını boşaldığında sıradaki görevi çalıştırır.

Bir tıklama içinde `fetch()` kullanıldığında ağ yanıtı beklenirken arayüzün donmamasının nedeni budur:

```javascript
const durum = document.querySelector("#durum");

buton.addEventListener("click", async () => {
  durum.textContent = "Kaydediliyor...";
  buton.disabled = true;

  try {
    const yanit = await fetch("/api/kaydet", { method: "POST" });
    if (!yanit.ok) throw new Error("Sunucu hatası");
    durum.textContent = "Kayıt tamamlandı.";
  } catch (hata) {
    durum.textContent = `İşlem başarısız: ${hata.message}`;
  } finally {
    buton.disabled = false;
  }
});
```

Burada dinleyici `async` olarak tanımlanır. `await`, ağ işleminin sonucunu beklerken JavaScript motorunun diğer olayları ele alabilmesine izin verir. Düğmenin geçici olarak devre dışı bırakılması da art arda gönderilen istekleri engeller.

## Olay nesnesi ve klavye kontrolü

Dinleyiciye aktarılan olay nesnesi, etkileşim hakkında ayrıntılar taşır. Klavye olaylarında basılan tuş `event.key`, tıklamalarda hedef eleman ise `event.target` üzerinden okunabilir:

```javascript
const arama = document.querySelector("#arama");

arama.addEventListener("keydown", (event) => {
  if (event.key === "Enter") {
    console.log("Aranan ifade:", event.target.value);
  }
});
```

Klavye desteği erişilebilirlik açısından kritiktir. Yalnızca fare tıklamasına göre tasarlanan bir arayüz, klavye veya yardımcı teknoloji kullanan kişileri dışarıda bırakabilir.

## Yayılma ve olay delegasyonu

Bir olay hedef elemanda doğar ve varsayılan olarak üst elemanlara doğru yayılır; buna **bubbling** denir. Bu davranış, olay delegasyonu için kullanılabilir. Yüzlerce liste öğesine ayrı dinleyici eklemek yerine üst kapsayıcı dinlenir:

```javascript
const liste = document.querySelector("#gorevler");

liste.addEventListener("click", (event) => {
  const silButonu = event.target.closest(".sil");
  if (!silButonu) return;

  silButonu.closest("li").remove();
});
```

Bu yöntem sonradan eklenen öğelerde de çalışır ve dinleyici sayısını azaltır. Gerekirse `event.stopPropagation()` yayılmayı durdurur; ancak gelişigüzel kullanılması başka bileşenlerin olayları görememesine yol açabilir.

Son olarak, artık gerekmeyen dinleyiciler `removeEventListener()` ile kaldırılmalıdır. Özellikle tek sayfa uygulamalarında temizlik yapılmaması bellek sızıntılarına ve aynı tepkinin birden fazla çalışmasına neden olabilir. İyi tasarlanmış olay yönetimi; hızlı, erişilebilir ve kullanıcıya gerçekten cevap veren arayüzlerin görünmez kahramanıdır.
