---
layout: post
title: "PHP ile Mikro Servis Mimarisi: Dev Sistemi Küçük Parçalara Bölmek"
math: true
categories: 
  - Bilgi
tags: 
  - PHP
  - Mikro Servis
  - Yazılım Mimarisi
---

Büyük bir PHP uygulaması zamanla dev bir apartmana dönüşebilir: kullanıcı yönetimi bir katta, ödeme sistemi başka katta, raporlama bodrumda, bildirimler ise çatı arasında çalışır. Her şey aynı kod tabanındaysa küçük bir değişiklik bile tüm binayı sallayabilir. Mikro servis mimarisi, bu apartmanı bağımsız küçük evlere ayırma fikridir. Her servis belirli bir iş yapar, kendi yaşam döngüsüne sahip olur ve gerektiğinde tek başına geliştirilip ölçeklenebilir.
``
Mikro servisleri anlamak için önce monolitik mimariyi hatırlayalım. Monolitik uygulamada kullanıcı kaydı, ürün yönetimi, sepet, ödeme ve e-posta gönderimi aynı proje içinde yer alır. Başlangıçta bu harikadır: tek repository, tek deployment, tek veritabanı. Ancak sistem büyüdükçe bağımlılıklar artar. Bir ödeme hatasını düzeltmek için tüm uygulamayı yeniden yayına almak gerekebilir.

Mikro servis yaklaşımında ise sistem $n$ adet küçük servise bölünür. Kabaca karmaşıklığı şöyle düşünebiliriz: monolitikte değişiklik etkisi çoğu zaman $O(n)$ modüle yayılırken, iyi ayrılmış servislerde etki alanı $O(1)$ veya sınırlı birkaç servise iner. Elbette bu sihirli bir değnek değildir; dağıtık sistem karmaşıklığı, ağ hataları ve veri tutarlılığı gibi yeni problemler getirir.

| Özellik | Monolitik PHP Uygulaması | Mikro Servis PHP Mimarisi |
|---|---|---|
| Deployment | Tüm uygulama birlikte yayınlanır | Her servis ayrı yayınlanabilir |
| Ölçekleme | Uygulamanın tamamı ölçeklenir | Sadece yoğun servis ölçeklenir |
| Kod bağımlılığı | Modüller sıkı bağlı olabilir | Servisler API ile konuşur |
| Hata etkisi | Tek hata geniş alanı etkileyebilir | Hata izole edilebilir |
| Başlangıç maliyeti | Daha düşüktür | Daha fazla planlama ister |

PHP ile mikro servis yazmak için illa devasa framework kullanmak zorunda değilsiniz. Laravel, Symfony veya Slim gibi frameworkler servis geliştirmeyi kolaylaştırır. Önemli olan servis sınırlarını doğru çizmektir. Örneğin bir e-ticaret sisteminde şu servisler olabilir:

- **User Service:** kullanıcı kaydı, giriş, yetkilendirme
- **Catalog Service:** ürün ve kategori yönetimi
- **Order Service:** sipariş oluşturma ve durum takibi
- **Payment Service:** ödeme alma ve doğrulama
- **Notification Service:** e-posta, SMS, push bildirimleri

Servisler genellikle HTTP/REST, gRPC veya mesaj kuyrukları üzerinden haberleşir. PHP tarafında basit bir REST endpoint şöyle görünebilir:

```php
<?php

require 'vendor/autoload.php';

use Slim\Factory\AppFactory;

$app = AppFactory::create();

$app->get('/users/{id}', function ($request, $response, $args) {
    $userId = (int) $args['id'];

    $data = [
        'id' => $userId,
        'name' => 'Ada Lovelace',
        'role' => 'admin'
    ];

    $response->getBody()->write(json_encode($data));
    return $response->withHeader('Content-Type', 'application/json');
});

$app->run();
```

Bu örnekte küçük bir kullanıcı servisi, `/users/{id}` adresinden JSON veri döndürür. Gerçek dünyada burada veritabanı bağlantısı, doğrulama, loglama ve hata yönetimi de bulunur. Ama temel fikir basittir: servis tek bir sorumluluğa odaklanır.

Mikro servislerde en kritik konulardan biri veri yönetimidir. Her servisin kendi veritabanına sahip olması önerilir. Çünkü ortak veritabanı kullanılırsa servisler görünmez şekilde birbirine bağlanır. Bu durum mikro servis görünümünde monolit üretir; yani tabelada mikro servis yazar ama içeride herkes aynı mutfağı kullanır.

| Veri Yaklaşımı | Avantaj | Risk |
|---|---|---|
| Ortak veritabanı | Başlangıçta kolaydır | Servis bağımsızlığını bozar |
| Servis başına veritabanı | Gevşek bağlılık sağlar | Veri senkronizasyonu gerekir |
| Event-driven yapı | Esnek ve ölçeklenebilir | İzleme ve hata ayıklama zorlaşır |

Örneğin ödeme tamamlandığında Payment Service, `payment.completed` adlı bir olay yayınlayabilir. Order Service bu olayı dinleyip sipariş durumunu günceller. Böylece servisler birbirini doğrudan çağırmak zorunda kalmaz. Bu modelde sistemin toplam güvenilirliği için basitçe $R_{sistem} = R_1 \times R_2 \times ... \times R_n$ gibi düşünebiliriz. Servis sayısı arttıkça gözlemleme, retry ve circuit breaker gibi mekanizmalar daha önemli hale gelir.

PHP ekosisteminde RabbitMQ, Redis Streams veya Kafka ile olay tabanlı iletişim kurulabilir. Docker ise her servisi ayrı konteyner olarak çalıştırmak için neredeyse standarttır. Böylece User Service PHP 8.3 ile, Notification Service farklı bağımlılıklarla çalışabilir.

Sonuç olarak PHP ile mikro servis mimarisi, büyük uygulamaları daha yönetilebilir hale getirmek için güçlü bir yaklaşımdır. Ancak her projeye otomatik olarak uygulanmamalıdır. Küçük bir uygulamada monolit daha hızlı ve ekonomiktir. Mikro servis, ekip büyüdüğünde, domain sınırları netleştiğinde ve bağımsız ölçekleme ihtiyacı doğduğunda parlamaya başlar. Kısacası önce problemi büyütün, sonra mimariyi bölün; yoksa mikro servis değil, mikro kaos üretirsiniz.
