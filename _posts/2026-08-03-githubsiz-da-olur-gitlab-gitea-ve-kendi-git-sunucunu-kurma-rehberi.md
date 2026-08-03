---
layout: post
title: "GitHub’sız da Olur: GitLab, Gitea ve Kendi Git Sunucunu Kurma Rehberi"
math: true
categories: 
  - Proje
tags: 
  - git
  - self-hosted
  - devops
---

GitHub, açık kaynak dünyasının kalabalık meydanı olabilir; ancak bütün kodlarımızı tek bir ekosisteme emanet etmek zorunda değiliz. Gizlilik, maliyet, kurum politikaları, çevrim dışı çalışma veya eğitim ihtiyaçları nedeniyle kendi Git platformumuzu barındırabiliriz. GitLab ve Gitea gibi çözümler, sıradan bir bulut sunucusunu bağımsız bir yazılım geliştirme merkezine dönüştürür.

``

## Neden kendi Git sunucumuz?

Git dağıtık bir sürüm kontrol sistemidir. Her geliştiricinin bilgisayarındaki depo, projenin geçmişini taşıyan bağımsız bir kopyadır. GitHub, GitLab veya Gitea ise bu depoların paylaşılmasını kolaylaştıran web tabanlı bir **forge**, yani yazılım geliştirme platformudur.

Kendi platformunu barındırmak veri üzerindeki kontrolü artırır fakat bakım sorumluluğunu da bize verir. Basit bir değerlendirme modeli şöyle kurulabilir:

$$T = K + B + G + Y$$

Burada $T$ toplam sahip olma maliyetini, $K$ sunucu maliyetini, $B$ bakım emeğini, $G$ güvenlik çalışmalarını ve $Y$ yedekleme giderlerini temsil eder. Ücretsiz yazılım, sıfır maliyetli sistem demek değildir; sadece faturanın şekli değişir.

## Platformların karşılaştırılması

| Platform | Kaynak ihtiyacı | Güçlü yanı | Uygun senaryo |
|---|---:|---|---|
| GitLab Community Edition | Yüksek | CI/CD, kayıt sistemi ve kapsamlı DevOps araçları | Şirketler ve büyük ekipler |
| Gitea | Düşük | Hafif, hızlı ve kolay kurulum | Kişisel sunucu ve küçük ekipler |
| Forgejo | Düşük | Topluluk odaklı Gitea alternatifi | Bağımsız açık kaynak toplulukları |
| GitLab Education | Orta/Yüksek | Gruplar, ödev depoları ve CI ile otomatik test | Dersler ve laboratuvarlar |

GitLab, İsviçre çakısı gibidir: CI/CD, paket deposu, sorun takibi ve güvenlik taraması tek pakette gelir. Gitea ise cebinizdeki sağlam çakıdır; daha az kaynak tüketir ve temel işleri hızla tamamlar. Eğitim ortamında Gitea’ya Woodpecker CI eklenebilir veya GitLab CI kullanılarak her öğrenci gönderimi otomatik test edilebilir.

## Docker Compose ile Gitea kurulumu

En az 2 GB RAM bulunan güncel bir Linux sunucu başlangıç için yeterlidir. DNS üzerinde `git.ornek.com` adresini sunucunun IP adresine yönlendirdikten sonra aşağıdaki `compose.yaml` dosyası hazırlanabilir:

```yaml
services:
  gitea:
    image: gitea/gitea:latest
    restart: always
    ports:
      - 3000:3000
      - 2222:22
    volumes:
      - ./gitea-data:/data
```

Bu yapı, web arayüzünü 3000 ve Git SSH bağlantısını 2222 numaralı portta açar. Veriler `gitea-data` klasöründe kalıcı tutulur. Sistemi başlatmak için:

```bash
docker compose up -d
docker compose logs -f gitea
```

İlk komut konteyneri arka planda çalıştırır; ikincisi kurulum günlüklerini gösterir. Ardından tarayıcıdan `http://sunucu-ip:3000` adresine gidilerek yönetici hesabı oluşturulur. Gerçek kullanımda Nginx veya Caddy ile ters vekil kurulmalı ve HTTPS etkinleştirilmelidir.

## Güvenlik ve yedekleme

Bağımsızlık, “kur ve unut” anlamına gelmez. Yönetici hesabında iki faktörlü kimlik doğrulama kullanılmalı, kayıt özelliği gerekmedikçe kapatılmalı ve SSH erişimi anahtarlarla sınırlandırılmalıdır. Güncellemeler önce test ortamında denenmelidir.

Kullanılabilirlik yaklaşık olarak şu oranla ölçülebilir:

$$A = \frac{\text{çalışma süresi}}{\text{toplam süre}} \times 100$$

Yüzde 99 kullanılabilirlik iyi görünse de yılda yaklaşık 3,65 gün kesinti anlamına gelir. Bu nedenle veritabanı, depo dosyaları ve yapılandırmalar düzenli olarak farklı bir konuma yedeklenmelidir. Ayrıca geri yükleme işlemi denenmeyen yedek, Schrödinger’in yedeğidir: ihtiyaç anına kadar çalışıp çalışmadığı bilinmez.

Sonuç olarak kapsamlı DevOps süreçleri için GitLab, düşük kaynak tüketimi için Gitea veya Forgejo mantıklı seçimlerdir. Eğitim kurumları ise otomatik test, grup yönetimi ve sınıf şablonlarını merkeze almalıdır. Küçük bir sunucuyla başlayan bu yolculuk, kodun ve geliştirme kültürünün gerçekten size ait olduğu bağımsız bir ekosisteme dönüşebilir.
