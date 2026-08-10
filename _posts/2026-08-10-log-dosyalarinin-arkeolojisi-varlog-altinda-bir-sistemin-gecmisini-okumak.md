---
layout: post
title: "Log Dosyalarının Arkeolojisi: /var/log Altında Bir Sistemin Geçmişini Okumak"
math: true
categories: 
  - Bilgi
tags: 
  - Linux
  - Sistem Yönetimi
  - Log Analizi
---

Bir bilgisayar sustuğunda bile geçmişi konuşmaya devam eder: log dosyaları, sistemin tuttuğu olay günlüğüdür. Başarısız bir SSH denemesi, gece yarısı yeniden başlayan bir servis, dolan disk ya da çöken bir uygulama; hepsi doğru katmanda iz bırakır. Bu nedenle `/var/log`, yalnızca hata ayıklama klasörü değil, dijital arkeoloğun kazı alanıdır. Amaç tek satırdaki hatayı bulmak değil; zaman, süreç ve neden-sonuç bağlamını birleştirerek sistemin hikâyesini yeniden kurmaktır.

``

## Log neden bir hafıza kaydıdır?

Bir log kaydı çoğunlukla üç temel bilgi taşır: **ne zaman** oldu, **hangi bileşen** bildirdi ve **ne** oldu. Basitleştirilmiş biçimiyle bir olay kaydını şöyle düşünebiliriz:

$$L = (t, s, h, m, p)$$

Burada $t$ zaman damgası, $s$ servis veya süreç, $h$ ana makine, $m$ mesaj ve $p$ önem derecesidir. Tek bir $L$ kaydı çoğu zaman belirsizdir; anlam, ardışık olayların korelasyonuyla ortaya çıkar. Örneğin uygulamanın 10:14'te veritabanı bağlantısını kaybetmesi, tek başına ağ sorunu demek değildir. Aynı dakikada `kernel` kayıtlarında ağ arabiriminin düşmesi ya da `auth.log` içinde yetkisiz yapılandırma değişikliği görülürse tablo değişir.

| Soru | İncelenecek kaynak | Arkeolojik yorum |
|---|---|---|
| Sistem neden yeniden başladı? | `syslog`, `journalctl`, `kern.log` | Kernel paniği, enerji kesintisi veya planlı reboot ayrıştırılır. |
| Kim erişmeye çalıştı? | `auth.log`, `secure` | Başarılı ve başarısız kimlik doğrulama izleri okunur. |
| Disk neden doldu? | `syslog`, uygulama logları | Hızla büyüyen dosya veya hatalı döngü tespit edilir. |
| Uygulama neden yanıt vermedi? | Uygulama logları, `journalctl -u` | Zaman aşımı, bağımlılık hatası ve çökme zinciri aranır. |

## Kazıya nereden başlanır?

Dağıtıma göre dosya adları değişse de Debian/Ubuntu tarafında `syslog` ve `auth.log`, RHEL ailesinde `messages` ve `secure` sık rastlanan kaynaklardır. Modern sistemlerde ise `systemd-journald`, kayıtları dosya yerine ikili journal biçiminde de tutabilir. Bu durumda `journalctl`, doğru fırçayı seçmek gibidir.

Aşağıdaki komut, belirli bir servisin belirli zaman aralığındaki günlüklerini inceler:

```bash
journalctl -u nginx \
  --since "2026-07-26 09:00:00" \
  --until "2026-07-26 10:00:00" \
  -p warning
```

Burada `-u nginx` olayları servise göre süzer; `--since` ve `--until` kazı alanını daraltır; `-p warning` ise yalnızca warning ve daha yüksek öncelikteki kayıtları getirir. Ancak filtreleme, bağlamı yok etmemelidir. Uyarıyı gördükten sonra birkaç dakika öncesi ve sonrasını mutlaka okuyun.

## Zaman çizelgesi kurmak: asıl dedektiflik

Log analizinde en değerli teknik, olayları ortak bir zaman çizgisine yerleştirmektir. Bir kök neden için basit bir ilişki modeli kurulabilir:

$$P(\text{kök neden} \mid \text{olaylar}) \propto P(\text{olaylar} \mid \text{kök neden}) \times P(\text{kök neden})$$

Bu, kesin bir istatistik hesabı yapmak zorunda olduğunuz anlamına gelmez. Pratik karşılığı şudur: Aynı anda görülen bağımsız işaretler, hipotezinizi güçlendirir. Önce disk doluluğu, ardından veritabanı yazma hataları ve son olarak uygulama çökmesi görünüyorsa; çökme neden değil, sonuç olabilir.

| Belirti | Aceleci yorum | Daha sağlam hipotez |
|---|---|---|
| `connection refused` | Uygulama bozuk | Hedef servis durmuş, port değişmiş veya ağ kuralı engelliyor olabilir. |
| `No space left on device` | Sadece disk dolu | inode tükenmesi, log patlaması ya da geçici dosya sızıntısı da mümkündür. |
| Çok sayıda `Failed password` | Sistem ele geçirildi | Brute-force girişimi olabilir; başarılı girişlerle doğrulanmalıdır. |

## Döndürme, bütünlük ve sessiz boşluklar

Eski kayıtların `syslog.1`, `syslog.2.gz` gibi dosyalara taşınması **log rotation** olarak adlandırılır. Sadece güncel dosyaya bakmak, kitabın son sayfasıyla roman çözmeye benzer. `zgrep` ile sıkıştırılmış arşivlerde arama yapabilirsiniz:

```bash
zgrep -h "Out of memory" /var/log/syslog*.gz
```

Son olarak saat senkronizasyonunu, zaman dilimini ve logların değiştirilme yetkilerini kontrol edin. Eksik kayıt her zaman “olay olmadı” demek değildir; servis loglamıyor, rotation yanlış çalışıyor veya saklama politikası geçmişi silmiş olabilir. İyi bir sistem yöneticisi logları yalnızca okuyan değil, merkezi toplama, erişim denetimi ve yeterli saklama süresiyle geleceğin hafızasını da koruyan kişidir.
