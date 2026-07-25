---
layout: post
title: "Paket Yönetimi ve Go Modules: Go Projelerini Düzenli, Güvenli ve Tekrarlanabilir Tutmak"
math: true
categories: 
  - Bilgi
tags: 
  - Go
  - Go Modules
  - Paket Yönetimi
  - Bağımlılık Yönetimi
---

Bir Go projesi büyüdükçe kodu tek dosyada tutmak, mutfakta tüm malzemeleri aynı çekmeceye atmaya benzer: başta pratik görünür, sonra tarçınla tornavidayı karıştırırsın. Paket yönetimi ve Go Modules, kodu yeniden kullanılabilir parçalara ayırmayı, dış kütüphaneleri doğru sürümle projeye dahil etmeyi ve aynı projenin farklı makinelerde aynı şekilde çalışmasını sağlar.
``

Go'da temel organizasyon birimi **package** kavramıdır. Aynı amaca hizmet eden fonksiyonlar, tipler ve değişkenler bir paket altında toplanır. Örneğin `payment`, `user`, `logger` gibi paketler hem okunabilirliği artırır hem de kodun tekrar kullanılmasını kolaylaştırır. Daha büyük ölçekte ise **module**, bir veya daha fazla paketi içeren ve kökünde `go.mod` dosyası bulunan sürümlenebilir proje birimidir.

Teorik olarak şöyle düşünebiliriz: Paket, kodun mantıksal bölmesidir; modül ise bu bölmelerin sürüm ve bağımlılık kimliğidir. Eğer projenin bağımlılık kümesini $D$ ve her bağımlılığın seçilen sürümünü $v_i$ olarak düşünürsek, modülün derlenebilir durumu kabaca şöyle ifade edilebilir: $M = \{(d_i, v_i) \mid d_i \in D\}$. Yani sadece hangi kütüphaneyi kullandığın değil, **hangi sürümünü** kullandığın da önemlidir.

| Kavram | Ne işe yarar? | Örnek |
|---|---|---|
| Package | Kodları mantıksal gruplara ayırır | `package auth` |
| Module | Projenin bağımlılık ve sürüm sınırını belirler | `module github.com/ali/app` |
| `go.mod` | Gerekli modülleri ve Go sürümünü tutar | `require` satırları |
| `go.sum` | İndirilen bağımlılıkların doğrulama izlerini saklar | checksum kayıtları |

Yeni bir Go modülü başlatmak için genellikle şu komut kullanılır:

```bash
go mod init github.com/kullanici/proje
```

Bu komut projenin kökünde `go.mod` dosyası üretir. Basit bir `go.mod` şöyle görünebilir:

```go
module github.com/kullanici/proje

go 1.22

require github.com/google/uuid v1.6.0
```

Burada `module` satırı projenin kimliğini, `go` satırı hedef Go sürümünü, `require` satırı ise dış bağımlılığı belirtir. `github.com/google/uuid v1.6.0` ifadesi, projede UUID üretmek için kullanılan paketin belirli bir sürümünü kilitler. Böylece bugün çalışan kodun yarın gizemli biçimde bozulma ihtimali azalır.

Go'da paketleri kullanmak oldukça doğaldır. Diyelim ki `internal/logger` adlı bir paket yazdık:

```go
package logger

import "fmt"

func Info(message string) {
    fmt.Println("[INFO] " + message)
}
```

Ana uygulamada bu paketi şöyle çağırabiliriz:

```go
package main

import "github.com/kullanici/proje/internal/logger"

func main() {
    logger.Info("Uygulama başladı")
}
```

Buradaki `internal` klasörü özel bir anlama sahiptir: Go, bu klasör altındaki paketlerin yalnızca ilgili modül içinde kullanılmasına izin verir. Bu da mimari sınırları korumak için harika bir yöntemdir. Kısacası `internal`, paketin kapısına asılmış nazik ama kararlı bir “personel harici giremez” tabelasıdır.

Sürümleme tarafında Go Modules, semantik sürümleme yaklaşımını destekler. Genel biçim $MAJOR.MINOR.PATCH$ şeklindedir. Örneğin `v1.6.0` için $MAJOR=1$, $MINOR=6$, $PATCH=0$ olur.

| Değişim türü | Anlamı | Örnek |
|---|---|---|
| PATCH | Hata düzeltmesi, API bozulmaz | `v1.6.0` → `v1.6.1` |
| MINOR | Yeni özellik, geriye uyumlu | `v1.6.0` → `v1.7.0` |
| MAJOR | Kırıcı değişiklik olabilir | `v1.6.0` → `v2.0.0` |

Bağımlılık eklemek için çoğu zaman ayrıca dosya düzenlemeye gerek yoktur. Şu komut yeterlidir:

```bash
go get github.com/google/uuid@v1.6.0
```

Ardından kullanılmayan bağımlılıkları temizlemek ve eksikleri tamamlamak için şu komut çalıştırılır:

```bash
go mod tidy
```

`go mod tidy`, projenin oda toparlayan robot süpürgesi gibidir: gereksizleri kaldırır, eksikleri yerine koyar. CI/CD süreçlerinde de bu dosyaların tutarlı olması önemlidir. `go.mod` ve `go.sum` dosyaları mutlaka sürüm kontrolüne eklenmelidir; çünkü ekip arkadaşlarının ve sunucuların aynı bağımlılık ağacını kurmasını sağlar.

Sonuç olarak Go Modules, sadece “kütüphane indirme aracı” değildir. Kodun sınırlarını çizen, bağımlılıkları matematiksel bir kesinlikle sürümlere bağlayan ve projeyi taşınabilir hale getiren bir sistemdir. Paketler kodu okunabilir kılar, modüller ise projeyi güvenilir yapar. İyi organize edilmiş bir Go projesinde her paket kendi işini bilir, her bağımlılığın sürümü bellidir ve geliştirici de hata ayıklamak yerine keyifle üretmeye odaklanır.
