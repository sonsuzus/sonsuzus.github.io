---
layout: post
title: "Haritalar (Maps) ile Anahtar-Değer Eşleşmesi"
math: true
categories: 
  - Bilgi
tags: 
  - map
  - veri-yapilari
  - javascript
---

Bir veri koleksiyonunu düşün: Elinde bir öğrenci listesi var ama öğrencileri 0, 1, 2 gibi indekslerle değil, okul numarası, e-posta adresi veya kullanıcı adı gibi anlamlı anahtarlarla bulmak istiyorsun. İşte haritalar, yani Maps, tam bu noktada sahneye çıkar. Map yapısı, veriyi anahtar-değer çifti olarak saklar ve arama, ekleme, silme gibi işlemleri oldukça okunabilir hale getirir.
``

## Map Mantığı Nedir?

Map, temel olarak şu fikre dayanır: Her değerin bir anahtarı vardır. Matematiksel olarak bunu bir eşleme fonksiyonu gibi düşünebiliriz:

$f: K \rightarrow V$

Burada $K$ anahtarlar kümesini, $V$ ise değerler kümesini temsil eder. Örneğin bir kullanıcı sisteminde `kullaniciAdi -> profilBilgisi` şeklinde bir ilişki kurabiliriz.

Dizilerde verilere genellikle indeksle ulaşırız:

```js
const renkler = ['kirmizi', 'mavi', 'yesil'];
console.log(renkler[1]); // mavi
```

Ama indeksler her zaman anlamlı değildir. `renkler[1]` ifadesi çalışır, fakat 1 sayısı bize iş kuralı hakkında pek bir şey söylemez. Map ile anahtarları kendimiz belirleyebiliriz.

```js
const renkKodlari = new Map();
renkKodlari.set('hata', 'kirmizi');
renkKodlari.set('basari', 'yesil');
renkKodlari.set('uyari', 'sari');

console.log(renkKodlari.get('basari')); // yesil
```

Burada `basari` anahtarı, `yesil` değerine karşılık gelir. Kod artık yalnızca çalışmakla kalmaz, aynı zamanda hikâye anlatır.

## Dizi, Nesne ve Map Karşılaştırması

| Özellik | Dizi | Nesne | Map |
|---|---|---|---|
| Anahtar tipi | Sayısal indeks | Genellikle string/symbol | Her tür olabilir |
| Sıralama | İndekse bağlı | Kurallara bağlı | Ekleme sırası korunur |
| Boyut öğrenme | `length` | Ek işlem gerekir | `size` |
| Sık kullanım | Sıralı listeler | Basit kayıtlar | Dinamik anahtar-değer koleksiyonları |
| Silme işlemi | `splice` vb. | `delete` | `delete` metodu |

Map yapısının güzel tarafı, anahtar olarak yalnızca string değil, nesne, fonksiyon hatta başka bir Map bile kullanabilmesidir. Bu, özellikle cache, kullanıcı oturumu, ayar yönetimi ve oyun içi envanter gibi senaryolarda çok işe yarar.

## Temel İşlemler: Ekleme, Arama, Silme

Bir Map üzerinde en sık kullanılan işlemler şunlardır:

```js
const sepet = new Map();

// Ekleme veya güncelleme
sepet.set('elma', 3);
sepet.set('muz', 5);
sepet.set('elma', 4); // elma miktarı güncellendi

// Arama
console.log(sepet.has('muz')); // true
console.log(sepet.get('elma')); // 4

// Silme
sepet.delete('muz');

// Boyut
console.log(sepet.size); // 1
```

`set` metodu hem yeni kayıt ekler hem de aynı anahtar varsa değeri günceller. `get` değeri getirir, `has` anahtarın varlığını kontrol eder, `delete` ise eşleşmeyi kaldırır.

## Performans Açısından Neden Önemli?

Map yapıları çoğu programlama dilinde hash table benzeri bir altyapıyla uygulanır. Bu nedenle ortalama durumda arama, ekleme ve silme işlemleri yaklaşık olarak $O(1)$ karmaşıklığındadır. Yani koleksiyon büyüse bile işlem süresi genellikle dramatik biçimde artmaz.

Elbette bu teorik bir ortalamadır. Kötü hash dağılımı gibi özel durumlarda maliyet artabilir. Ancak pratikte Map, özellikle sık arama yapılan yapılarda diziye göre daha uygun olabilir. Bir dizide elemanı bulmak için tek tek dolaşmak gerekirse maliyet $O(n)$ olur.

| İşlem | Dizi ile yaklaşım | Map ile yaklaşım |
|---|---|---|
| Kullanıcıyı ID ile bulma | Tüm listeyi gezmek gerekebilir | `get(id)` |
| Kayıt var mı kontrolü | `find` veya `some` | `has(key)` |
| Kayıt silme | İndeksi bul, sonra sil | `delete(key)` |

## Küçük Bir Örnek: Kullanıcı Oturumları

```js
const oturumlar = new Map();

function oturumAc(token, kullanici) {
  oturumlar.set(token, {
    ad: kullanici,
    baslangic: Date.now()
  });
}

function oturumKontrol(token) {
  if (!oturumlar.has(token)) {
    return 'Oturum bulunamadi';
  }

  const oturum = oturumlar.get(token);
  return `${oturum.ad} aktif`;
}

function oturumKapat(token) {
  return oturumlar.delete(token);
}

oturumAc('abc123', 'Ada');
console.log(oturumKontrol('abc123'));
oturumKapat('abc123');
```

Bu örnekte token anahtar, kullanıcı oturum bilgisi ise değerdir. Böylece her oturuma hızlıca erişebiliriz.

## Ne Zaman Map Kullanmalı?

Eğer verilerin doğal bir anahtarı varsa, sık sık arama yapıyorsan veya anahtarların string dışında türler olmasını istiyorsan Map iyi bir seçimdir. Sadece sıralı bir liste tutuyorsan dizi daha uygundur. Sabit yapılı bir veri modeli için ise nesne veya sınıf daha okunabilir olabilir.

Kısacası Map, veriye anlamlı bir kapı etiketi takmaktır. İndekslerin soğuk apartman numaralarından sıkıldıysan, anahtar-değer dünyasına hoş geldin!
