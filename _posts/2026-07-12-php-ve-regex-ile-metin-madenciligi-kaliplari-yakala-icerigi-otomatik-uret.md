---
layout: post
title: "PHP ve Regex ile Metin Madenciliği: Kalıpları Yakala, İçeriği Otomatik Üret"
math: true
categories: 
  - Program
tags: 
  - php
  - regex
  - metin-isleme
---

Sunucu tarafında çalışan küçük bir PHP betiği, doğru düzenli ifadelerle birleştiğinde devasa log dosyalarını, kullanıcı yorumlarını, haber metinlerini veya HTML parçalarını akıllı bir içerik fabrikasına çevirebilir. Regex, metnin içinde saklanan düzeni bulma sanatıdır; PHP ise bu sanatı otomasyona bağlayan pratik mutfaktır.
``

Düzenli ifadeleri bir tür metin mikroskobu gibi düşünebiliriz. Normal arama işlemi sadece birebir kelime bulurken, regex belirli bir şekle uyan metinleri yakalar. Örneğin e-posta adresleri farklı kullanıcı adlarına ve alan adlarına sahip olabilir; ama çoğu benzer bir forma uyar: kullanıcı, `@`, alan adı ve uzantı. Bu yüzden regex, tek tek kelime değil, kalıp arar.

Teorik olarak bir regex deseni, karakter kümeleri ve tekrar kurallarıyla tanımlanır. Basitçe şöyle düşünebiliriz: bir metin $T$, bir desen $P$ ile taranır ve eşleşme fonksiyonu $M(T, P)$ bize bulunan parçaları döndürür. Eğer amaç filtreleme ise sonuç doğru/yanlış olabilir; eğer amaç içerik üretimi ise bulunan parçalar yeni bir yapıya dönüştürülür.

| İhtiyaç | Regex Yaklaşımı | PHP Fonksiyonu |
|---|---|---|
| Metinde kalıp var mı? | Deseni test et | `preg_match` |
| Tüm eşleşmeleri bul | Global yakalama | `preg_match_all` |
| Zararlı ifadeleri sil | Eşleşeni değiştir | `preg_replace` |
| Metni parçalara böl | Ayraç deseni kullan | `preg_split` |

PHP tarafında regex işlemleri çoğunlukla PCRE motoru ile yapılır. Desenler genellikle `/.../` sınırlandırıcıları arasına yazılır. Sona eklenen `i`, büyük-küçük harf duyarsızlığı sağlar. Örneğin `/php/i`, hem `PHP` hem `php` hem de `Php` ifadelerini yakalayabilir.

```php
<?php
$text = 'İletişim: destek@example.com veya satis@site.com.tr';
$pattern = '/\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b/i';

preg_match_all($pattern, $text, $matches);

foreach ($matches[0] as $email) {
    echo $email . PHP_EOL;
}
```

Bu kodun yaptığı iş basit ama güçlüdür: metin içindeki e-posta biçimine benzeyen tüm parçaları toplar. `\b` kelime sınırını, `[A-Z0-9._%+-]+` kullanıcı adını, `@` zorunlu karakteri, devamındaki bölüm ise alan adını temsil eder. Buradaki `+` operatörü en az bir tekrar anlamına gelir. Yani matematiksel olarak `x+`, $x$ karakterinin $n \ge 1$ kez tekrar etmesi demektir.

Regex öğrenirken en kritik konu açgözlülük davranışıdır. `.*` mümkün olan en uzun eşleşmeyi almaya çalışır. Bu bazen çok kullanışlı, bazen de tam bir metin canavarıdır.

| Desen | Davranış | Örnek Sonuç |
|---|---|---|
| `<h2>.*</h2>` | Açgözlü | İlk `<h2>`den son `</h2>`ye kadar alabilir |
| `<h2>.*?</h2>` | Tembel | En yakın `</h2>`de durur |
| `<h2>(.*?)</h2>` | Yakalama gruplu | Sadece başlık içeriği ayrıca alınabilir |

Şimdi küçük bir otomatik içerik çıkarıcı yazalım. Diyelim ki elimizde ham HTML benzeri bir metin var ve içindeki başlıkları listeleyerek mini bir özet üretmek istiyoruz.

```php
<?php
$html = '<h2>Regex Nedir?</h2><p>Kalıp arama tekniğidir.</p><h2>PHP ile Kullanımı</h2>';
$pattern = '/<h2>(.*?)<\/h2>/i';

preg_match_all($pattern, $html, $matches);

$summary = [];
foreach ($matches[1] as $title) {
    $summary[] = '- ' . trim(strip_tags($title));
}

echo implode(PHP_EOL, $summary);
```

Burada `(.*?)` kısmı yakalama grubudur. `preg_match_all` sonucunda `$matches[0]` tam eşleşmeleri, `$matches[1]` ise parantez içindeki özel bölümü verir. Böylece etiketleri değil, sadece başlık içeriğini kullanarak otomatik özet çıkarabiliriz.

Filtreleme tarafında ise `preg_replace` oldukça pratiktir. Örneğin yorumlardan telefon numarası gibi hassas verileri maskeleyebilirsiniz.

```php
<?php
$comment = 'Beni 0555 123 45 67 numarasından ara.';
$clean = preg_replace('/\b0\d{3}\s\d{3}\s\d{2}\s\d{2}\b/', '[telefon gizlendi]', $comment);

echo $clean;
```

Bu yaklaşım özellikle moderasyon sistemlerinde, log temizleme işlemlerinde ve veri anonimleştirmede işe yarar. Yine de regex her sorunun çekici değildir. HTML ayrıştırma için karmaşık yapılarda DOMDocument daha güvenlidir; parola doğrulamada regex yardımcıdır ama tek başına güvenlik politikası değildir.

Sonuç olarak PHP ve regex ikilisi, metin yığınları içinde düzen arayan geliştiriciler için hızlı, ekonomik ve güçlü bir araç setidir. Mantığı kavradığınızda, bir log satırından hata kodu çekmek de, makalelerden otomatik etiket üretmek de aynı temel fikre dayanır: kalıbı tanımla, eşleşmeyi yakala, sonucu anlamlı bir çıktıya dönüştür.
