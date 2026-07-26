---
layout: post
title: "Kali Linux Kurulumu ve Live USB Kullanımı: Diske Yerleşmek mi, İz Bırakmadan Gezmek mi?"
math: true
categories: 
  - Bilgi
tags: 
  - Kali Linux
  - Live USB
  - Linux Kurulumu
---

Kali Linux, siber güvenlik araçlarıyla dolu bir İsviçre çakısı gibidir; ama bu çakıyı cebine kalıcı olarak mı koyacaksın, yoksa gerektiğinde USB’den çıkarıp kullanacak mısın? Bu yazıda Kali’yi diske kurma ve canlı sistem olarak çalıştırma seçeneklerini teorik altyapısıyla inceleyeceğiz. Ama küçük not: Kali güçlü araçlar içerir; yalnızca kendi sistemlerinde, izinli laboratuvarlarda ve etik amaçlarla kullanılmalıdır.
``

## Kurulum Mantığı: İşletim Sistemi Nereye Yaşar?

Bir işletim sistemi çalışırken çekirdek, dosya sistemi, kullanıcı alanı programları ve donanım sürücülerini birlikte yönetir. Kalıcı kurulumda bu bileşenler diskteki bölümlere yazılır. Live kullanımda ise sistem çoğunlukla USB’den okunur ve RAM üzerinde çalışır.

Basitçe düşünürsek performans ve kalıcılık ilişkisi şöyle modellenebilir: $Deneyim = f(Hız, Kalıcılık, Taşınabilirlik)$. Kalıcı kurulumda $Hız$ ve $Kalıcılık$ artarken, live sistemde $Taşınabilirlik$ ve iz bırakmama avantajı öne çıkar.

| Özellik | Kalıcı Kurulum | Live USB |
|---|---|---|
| Veri kalıcılığı | Varsayılan olarak var | Genelde yok, persistence ile eklenebilir |
| Performans | Daha yüksek | USB hızına bağlı |
| Risk | Disk bölümleri etkilenebilir | Ana diske dokunmadan çalışabilir |
| Kullanım amacı | Günlük lab, eğitim, sürekli çalışma | Hızlı test, taşınabilir analiz, geçici oturum |

## ISO Dosyasını Doğrulamak

Kuruluma başlamadan önce Kali ISO dosyasının bozulmadığını doğrulamak önemlidir. Hash kontrolü, dosyanın parmak izi gibidir. Eğer indirilen dosyanın özeti beklenen değerle aynıysa, $H_{indirilen} = H_{resmi}$ koşulu sağlanır.

```bash
sha256sum kali-linux.iso
```

Bu komut ISO dosyasının SHA-256 özetini üretir. Kali’nin resmi sitesindeki değerle karşılaştırarak indirme sırasında hata veya oynama olup olmadığını anlayabilirsin.

## Live USB Hazırlama

Live USB için en pratik araçlar Rufus, Balena Etcher veya Linux tarafında dd komutudur. dd güçlüdür ama dikkatsiz kullanılırsa yanlış diski silebilir; yani Linux dünyasının motorlu testeresi diyebiliriz.

```bash
sudo dd if=kali-linux.iso of=/dev/sdX bs=4M status=progress oflag=sync
```

Burada if kaynak ISO dosyasını, of hedef USB aygıtını belirtir. /dev/sdX yerine doğru USB aygıtı yazılmalıdır. Bu komut ISO içeriğini USB’ye ham biçimde yazar ve USB’yi önyüklenebilir hale getirir.

## Live Sistem Kullanımı

Bilgisayarı USB’den başlatmak için BIOS veya UEFI menüsünden boot sırası değiştirilir. Kali açılış menüsünde Live seçeneği seçildiğinde sistem RAM üzerinde çalışır. Bu modda yaptığın çoğu değişiklik yeniden başlatınca kaybolur. Bu, gizemli bir ninja gibi gelip gitmek isteyenler için idealdir.

Ancak bazı durumlarda notları, araç ayarlarını veya raporları saklamak isteyebilirsin. Bunun için persistence bölümü oluşturulur. Mantık şudur: sistem live çalışır ama belirli bir USB bölümü kalıcı depo gibi bağlanır.

| Live Mod | Ne Zaman Mantıklı? |
|---|---|
| Standart Live | İz bırakmadan hızlı test |
| Live Persistence | USB üzerinde ayar ve dosya saklama |
| Forensic Mode | Diskleri otomatik bağlamadan inceleme |

## Kalıcı Kurulum Süreci

Kalıcı kurulumda Kali disk üzerine yazılır. Bu yöntem sanal makinede ya da ayrı bir test bilgisayarında daha güvenlidir. Kurulum adımları genel olarak dil, klavye, ağ, kullanıcı, disk bölümlendirme ve önyükleyici seçiminden oluşur.

Disk bölümlendirme en kritik aşamadır. Tüm diski kullan seçeneği basittir ama mevcut verileri silebilir. Çift işletim sistemi kurulacaksa boş alan ayırmak gerekir. Linux tarafında temel bölümler genelde kök dizin /, isteğe bağlı /home ve takas alanıdır. Takas için eski pratik kural $Swap \approx RAM$ olsa da modern sistemlerde kullanım senaryosu daha belirleyicidir.

```bash
lsblk
```

Bu komut diskleri ve bölümleri listeler. Kurulumdan önce hangi diskin hangisi olduğunu görmek için çok faydalıdır. Yanlış diske kurulum yapmak, kahveyi klavyeye dökmek kadar üzücü olabilir.

## Hangisini Seçmeli?

Eğer Kali’yi öğreniyor, araçları düzenli kullanıyor ve laboratuvar ortamı kuruyorsan kalıcı kurulum veya sanal makine daha konforludur. Eğer amacın taşınabilir analiz, geçici oturum veya ana sisteme dokunmadan deneme yapmaksa Live USB daha akıllıca olabilir.

Özetle: kalıcı kurulum ev kurmak, Live USB ise kamp çadırı taşımak gibidir. Ev rahattır ama yer ister; çadır hafiftir ama her sabah yeniden toparlanırsın. En güvenli başlangıç ise çoğu kullanıcı için sanal makine ya da Live USB ile deneme yapmak, ardından ihtiyaç netleşince kalıcı kuruluma geçmektir.
