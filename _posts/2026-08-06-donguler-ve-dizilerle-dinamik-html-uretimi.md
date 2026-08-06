---
layout: post
title: "Döngüler ve Dizilerle Dinamik HTML Üretimi"
math: true
categories: 
  - Bilgi
tags: 
  - PHP
  - Diziler
  - Döngüler
---

Bir web sayfasındaki ürün kartlarını tek tek elle yazmak, aynı şarkıyı yüz kez başa sarmaya benzer: yapılabilir ama hiç eğlenceli değildir. Diziler verileri düzenli biçimde saklarken `for` ve `foreach` döngüleri bu verileri sırayla işler. Böylece birkaç satırlık PHP koduyla onlarca HTML bloğunu dinamik, tutarlı ve kolay güncellenebilir biçimde ekrana basabiliriz.

``

## Temel Mantık: Veri Ayrı, Görünüm Ayrı

Dizi, birden fazla değeri tek değişken altında tutan veri yapısıdır. İndeksli dizilerde elemanlara `0`, `1`, `2` gibi konumlarla; ilişkisel dizilerde ise `ad`, `fiyat` veya `stok` gibi anlamlı anahtarlarla erişilir.

Bir dizide $n$ eleman varsa bütün elemanları bir kez ziyaret eden döngünün çalışma maliyeti yaklaşık olarak:

$$T(n) = c \cdot n$$

şeklinde ifade edilir. Buradaki $c$, her eleman için yapılan sabit miktardaki işlemdir. Bu nedenle temel listeleme işleminin zaman karmaşıklığı $O(n)$ olur. Eleman sayısı iki katına çıktığında yapılacak iş de yaklaşık iki katına çıkar.

| Yapı | Kullanım biçimi | En uygun olduğu durum |
|---|---|---|
| İndeksli dizi | `$renkler[0]` | Basit ve sıralı değer listeleri |
| İlişkisel dizi | `$urun['ad']` | Özellikleri bulunan kayıtlar |
| `for` | Sayaç ve indeks kullanır | Konum bilgisi gerektiğinde |
| `foreach` | Elemanı doğrudan verir | Koleksiyonları okunaklı biçimde dolaşırken |

## `for` ile Sıralı Verileri Yazdırmak

`for` döngüsü başlangıç, koşul ve artış olmak üzere üç parçadan oluşur. Dizinin indeksine veya sıra numarasına ihtiyaç duyduğumuzda oldukça kullanışlıdır.

```php
<?php
$diller = ['PHP', 'JavaScript', 'Python', 'Go'];

for ($i = 0; $i < count($diller); $i++) {
    echo '<p>' . ($i + 1) . '. ' . $diller[$i] . '</p>';
}
?>
```

Burada `$i`, dizinin mevcut indeksini temsil eder. Diziler sıfırdan başladığı için kullanıcıya gösterilen sıra numarasında `$i + 1` kullanılır. Koşulun `$i <= count($diller)` biçiminde yazılması, olmayan son elemana erişmeye çalışacağı için klasik bir “bir adım fazla” hatası üretir.

Dizi boyutu sık değişmiyorsa `count()` sonucunu önceden saklamak da mümkündür:

```php
$toplam = count($diller);
for ($i = 0; $i < $toplam; $i++) {
    echo '<li>' . htmlspecialchars($diller[$i]) . '</li>';
}
```

`htmlspecialchars()` özel HTML karakterlerini dönüştürerek kullanıcı kaynaklı verilerin güvenli gösterilmesine yardımcı olur.

## `foreach` ile Ürün Kartları Oluşturmak

İlişkisel ve çok boyutlu dizilerde `foreach`, indeks yönetme zahmetini ortadan kaldırır. Aşağıdaki veri kümesindeki her ürün bir ilişkisel dizidir:

```php
<?php
$urunler = [
    ['ad' => 'Mekanik Klavye', 'fiyat' => 2450, 'stok' => 8],
    ['ad' => 'Kablosuz Fare', 'fiyat' => 980, 'stok' => 0],
    ['ad' => 'USB Mikrofon', 'fiyat' => 3150, 'stok' => 4]
];
?>

<section class="urun-listesi">
<?php foreach ($urunler as $urun): ?>
    <article class="urun-karti">
        <h2><?= htmlspecialchars($urun['ad']) ?></h2>
        <p><?= number_format($urun['fiyat'], 2, ',', '.') ?> TL</p>
        <strong>
            <?= $urun['stok'] > 0 ? 'Stokta var' : 'Tükendi' ?>
        </strong>
    </article>
<?php endforeach; ?>
</section>
```

Alternatif sözdizimindeki `foreach ... endforeach` yapısı, PHP ile HTML iç içeyken süslü parantezlere göre daha rahat okunur. `number_format()` fiyatı kullanıcı dostu hale getirirken üçlü koşul operatörü stok durumuna göre farklı metin üretir.

## Boş Listeyi Unutmayın

Gerçek uygulamalarda veri kümesi her zaman dolu olmayabilir. Boş bir alan göstermek yerine kullanıcıya açıklama sunmak daha iyi bir deneyimdir:

```php
<?php if (empty($urunler)): ?>
    <p>Henüz gösterilecek ürün bulunmuyor.</p>
<?php else: ?>
    <?php foreach ($urunler as $urun): ?>
        <div><?= htmlspecialchars($urun['ad']) ?></div>
    <?php endforeach; ?>
<?php endif; ?>
```

Özetle sıra numarası, belirli aralık veya indeks denetimi gerekiyorsa `for`; verileri doğrudan ve okunaklı şekilde dolaşmak gerekiyorsa `foreach` tercih edilmelidir. Veriyi dizide tutup HTML şablonunu döngüyle çoğaltmak, tekrarları azaltır ve yeni bir kayıt eklemeyi yalnızca diziye tek satır eklemek kadar kolaylaştırır.
