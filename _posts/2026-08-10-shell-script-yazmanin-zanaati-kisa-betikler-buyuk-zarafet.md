---
layout: post
title: "Shell Script Yazmanın Zanaatı: Kısa Betikler, Büyük Zarafet"
math: true
categories: 
  - Bilgi
tags: 
  - Shell Script
  - Bash
  - Yazılım Zanaatkarlığı
---

Bir shell betiği bazen yalnızca üç satırdır: bir dosyayı bulur, dönüştürür ve sonucu kaydeder. Buna rağmen iyi yazılmış bir betik, iyi kurulmuş kısa bir şiir gibi hissedebilir. Her kelime iş yapar, her boşluk okunabilirliğe katkı sunar ve gereksiz hiçbir hareket yoktur. Shell script zanaatı; komutları art arda dizmekten çok, belirsizliği azaltma, niyeti görünür kılma ve gelecekteki kullanıcıya saygı duyma pratiğidir.
``

## Zanaatkârlık: Az Satır, Çok Düşünce

Kısalık tek başına erdem değildir. `rm -rf "$hedef"` kısa olabilir; ama `hedef` değişkeninin boş gelmesi, kısa bir komutu uzun bir felakete dönüştürebilir. Zarafet, satır sayısını körlemesine azaltmak değil, her satırın taşıdığı riski ve anlamı yönetmektir.

Bir betiğin kalitesini kabaca şu ilişkiyle düşünebiliriz:

$$\text{Değer} = \frac{\text{Doğruluk} \times \text{Okunabilirlik} \times \text{Güvenlik}}{\text{Gereksiz Karmaşıklık}}$$

Bu bir mühendislik ölçümü değil, düşünme aracıdır. Özellikle shell dünyasında komutların varsayılan davranışları, boşluk içeren dosya adları ve hata kodları görünmez karmaşıklık üretir. Zanaatkâr programcı, bu görünmez ayrıntıları betiğin tasarımının parçası sayar.

| Yaklaşım | Kısa vadeli görünüm | Uzun vadeli sonuç |
|---|---|---|
| Tek satırda her şey | Hızlı ve etkileyici | Hata ayıklaması zor |
| Açıklamalı küçük fonksiyonlar | Biraz daha uzun | Niyeti ve bakımı kolay |
| Varsayımlara güvenmek | Az yazı | Beklenmedik veride kırılganlık |
| Girdiyi doğrulamak | Birkaç ek satır | Daha güvenli otomasyon |

## Sessizlik Değil, Anlamlı Sadelik

İyi bir betik, kullanıcıya gereksiz gürültü çıkarmaz; ancak önemli bir şey olduğunda da susmaz. Örneğin yedekleme betiği başarıyla bitince nereye yazdığını belirtmeli, başarısız olduğunda ise anlaşılır bir hata vermelidir. Bu denge, komut satırı araçlarının kullanıcı deneyimidir.

Aşağıdaki örnek, bir dizini tarih damgalı arşive dönüştürür. Orta düzeyde görünmesinin nedeni, argüman denetimi, güvenli kabuk seçenekleri ve anlamlı çıktı içermesidir:

```bash
#!/usr/bin/env bash
set -euo pipefail

kaynak=${1:-}
hedef_dizin=${2:-./yedekler}

if [[ -z "$kaynak" || ! -d "$kaynak" ]]; then
  echo "Kullanım: $0 <kaynak-dizin> [hedef-dizin]" >&2
  exit 1
fi

mkdir -p "$hedef_dizin"
tarih=$(date +%Y-%m-%d_%H-%M-%S)
arsiv="$hedef_dizin/$(basename "$kaynak")_$tarih.tar.gz"

tar -czf "$arsiv" -C "$(dirname "$kaynak")" "$(basename "$kaynak")"
echo "Yedek oluşturuldu: $arsiv"
```

Buradaki `set -euo pipefail` üç farklı kazayı engellemeye çalışır: başarısız komuttan sonra devam etmek, tanımsız değişken kullanmak ve boru hattındaki ara hataları saklamak. Çift tırnaklar ise dosya adındaki boşlukları korur. Bunlar süs değildir; betiğin işçiliğidir.

## Tekrarı Değil, Niyeti Soyutlayın

Shell betiklerinde erken soyutlama da bir tuzaktır. Her iki satır için genel bir framework kurmak, çekiçle vida sıkmaya benzer. Fakat aynı doğrulama veya günlükleme üç kez görünüyorsa, küçük bir fonksiyon anlamlı olabilir. Ölçüt şudur: Fonksiyon, kodu daha az değil daha anlaşılır yapıyor mu?

| İşaret | Tercih |
|---|---|
| Mantık yalnızca bir kez kullanılıyor | Doğrudan ve açık yazın |
| Aynı hata denetimi tekrarlanıyor | Fonksiyona taşıyın |
| Komutun yan etkisi büyük | Önce kontrol, sonra işlem yapın |
| Kullanıcı verisi işleniyor | Tırnaklayın ve doğrulayın |

Sonuçta güzel shell script, zekâ gösterisi değildir. Başka birinin — hatta altı ay sonraki sizin — güvenle okuyup değiştirebildiği bir araçtır. Şiir gibi hissettirmesinin sebebi de budur: Kısıtlı bir dilde, az sayıda sözcükle açık, ritmik ve güvenilir bir anlam kurar.
