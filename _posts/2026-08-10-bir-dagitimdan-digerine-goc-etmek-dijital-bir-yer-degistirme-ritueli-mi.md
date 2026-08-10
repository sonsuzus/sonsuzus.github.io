---
layout: post
title: "Bir Dağıtımdan Diğerine Göç Etmek: Dijital Bir Yer Değiştirme Ritüeli mi?"
math: true
categories: 
  - Bilgi
tags: 
  - Linux
  - dağıtım
  - dijital kimlik
  - alışkanlıklar
  - sistem yönetimi
---

Bir Linux dağıtımından diğerine geçmek, çoğu zaman yalnızca paket yöneticisini değiştirmek değildir. Fedora’dan Debian’a, Arch’tan NixOS’a ya da Ubuntu’dan openSUSE’ye giden kişi; komutlarını, hata çözme reflekslerini, masaüstü düzenini ve hatta bilgisayarıyla kurduğu güven ilişkisini yeniden müzakere eder. Bu nedenle sistem göçü, teknik bir kurulum işlemi olmanın yanında küçük ölçekli bir dijital yer değiştirme ritüelidir.

``

Bir işletim sistemi, kullanıcı için bir tür **bilişsel ev** üretir. Dosyaların nerede durduğunu bilmek, `apt` yazınca ne olacağını sezmek veya bir sorun çıktığında hangi topluluğa danışacağını tahmin etmek görünmez konfor alanlarıdır. Alışkanlık gücünü basitçe şöyle düşünebiliriz:

$$A = f(T, R, C)$$

Burada $A$ alışkanlık bağını; $T$ kullanım süresini, $R$ tekrar sıklığını ve $C$ ise çevresel tutarlılığı temsil eder. Yıllarca aynı dağıtımı kullanmak, bu değişkenleri artırır. Yeni dağıtıma geçildiğinde teknik bilgi kaybolmaz; fakat bilgiye ulaşma yolları, yani refleksler geçici olarak boşa düşer.

| Eski sistemdeki güven hissi | Yeni sistemdeki karşılığı | Kullanıcının duygusu |
|---|---|---|
| Bilinen paket yöneticisi | Yeni komut sözdizimi | Tereddüt |
| Ezberlenmiş dosya yolları | Farklı varsayılanlar | Yön kaybı |
| Tanıdık topluluk ve wiki | Yeni dokümantasyon kültürü | Yabancılık |
| Oturmuş masaüstü akışı | Yeniden yapılandırma | Kontrol arayışı |

Örneğin `apt`, `dnf` ve `pacman` aynı temel işi yapar: paketleri yönetir. Yine de kullanıcının zihninde bunlar eşdeğer düğmeler değildir. Her biri farklı çıktı biçimleri, çözümleme davranışları ve hata mesajlarıyla ayrı bir karakter kazanır. Bu yüzden göç sırasında yaşanan sürtünme, sadece öğrenme maliyeti değil, **alışılmış geri bildirimlerin kaybıdır**.

Aşağıdaki küçük betik, geçiş öncesi kişisel yapılandırmaları yedeklemek için kullanılabilir. Teknik olarak basit görünse de ritüel değeri yüksektir: Eski dijital evden taşınacak eşyaları seçer.

```bash
#!/usr/bin/env bash
# Temel kullanıcı yapılandırmalarını tarih damgalı bir arşive alır.
set -e

DATE=$(date +%Y-%m-%d)
BACKUP="$HOME/migration-backup-$DATE"
mkdir -p "$BACKUP"

for item in .bashrc .gitconfig .config .ssh; do
  if [ -e "$HOME/$item" ]; then
    cp -a "$HOME/$item" "$BACKUP/"
    echo "Yedeklendi: $item"
  fi
done

tar -czf "$BACKUP.tar.gz" -C "$HOME" "$(basename "$BACKUP")"
echo "Arşiv hazır: $BACKUP.tar.gz"
```

Ancak her şeyi taşımak her zaman iyi fikir değildir. Eski yapılandırmalar, yeni sistemin felsefesiyle çatışabilir. Özellikle NixOS gibi bildirgesel yapılandırmayı önceleyen sistemlerde, yıllarca birikmiş elle yapılmış ayarlar yerine tekrarlanabilir bir konfigürasyon tanımlamak daha değerlidir. Göçün başarısı, eski düzeni kusursuz kopyalamakla değil; hangi alışkanlıkların gerçekten gerekli olduğunu ayırt etmekle ölçülür.

| Göç yaklaşımı | Avantajı | Riski |
|---|---|---|
| Bire bir kopyalama | Hızlı tanışıklık hissi | Eski sorunları taşımak |
| Sıfırdan kurulum | Temiz ve tutarlı başlangıç | Üretkenlikte geçici düşüş |
| Seçici taşıma | Esneklik ve bilinçli sadeleşme | Daha fazla karar verme yükü |

Kimlik boyutu burada belirginleşir. “Arch kullanıcısıyım” ya da “Debian kararlılığını severim” cümleleri, araç tercihinden fazlasını anlatır: öğrenme biçimi, risk toleransı ve toplulukla ilişki biçimi hakkında ipucu verir. Dağıtım değiştirmek bazen bu kimlik etiketini bırakmak, bazen de onu daha bilinçli yeniden kurmaktır.

Sonuçta dijital göçte kaybedilen şey çoğunlukla dosyalar değil, otomatikleşmiş küçük davranışlardır. Kazanılan şey ise yeni bir sistemden çok, kendi çalışma düzenine dışarıdan bakabilme fırsatıdır. En iyi geçiş planı; yedek alan, not tutan, eski alışkanlıkları sorgulayan ve ilk hafta biraz kaybolmayı normal kabul eden plandır.
