---
layout: post
title: "LUKS İçin Sahte Masaüstü Tuzak Sistemi: Savunmacı Aldatma Tasarımı"
math: true
categories: 
  - Proje
tags: 
  - LUKS
  - Linux Güvenliği
  - Honeypot
---

Bir saldırganın cihazınızı ele geçirdiğini ve LUKS parolasını denediğini düşünün. Normalde yanlış parola yalnızca “erişim yok” demektir; fakat savunmacı aldatma yaklaşımında sistem, belirli sayıda hatadan sonra sanki parola kabul edilmiş gibi davranıp izole bir sahte masaüstü başlatabilir. Bu yazıda bunu kötüye kullanım değil, yalnızca kendi cihazınızda ve laboratuvar ortamında uygulanacak bir güvenlik tasarımı olarak ele alacağız.
``

Önce kritik gerçeği netleştirelim: LUKS yanlış parolayla gerçek diski açamaz. Kriptografik olarak “yanlış ama yine de açılmış gibi” yapmak mümkün değildir; çünkü anahtar türetme sonucu bambaşka olur. Basitçe:

$$K = KDF(parola, salt)$$

Doğru parola için $K = K_{gerçek}$ olurken, yanlış parola için pratikte rastgele bir $K'$ oluşur. Yani sahte masaüstü, gerçek veriyi açmak yerine ayrı ve izole bir “decoy” sistemden başlatılmalıdır.

## Genel mimari

Tasarlayacağımız sistem üç parçadan oluşur:

1. **Gerçek LUKS bölüm**: Asıl işletim sistemi ve veriler burada durur.
2. **Decoy işletim sistemi**: Ayrı bir bölümde veya salt-okunur imajda bulunan sahte masaüstü.
3. **Initramfs karar katmanı**: Boot sırasında parola denemelerini yönetir; başarısızlık eşiği aşılırsa decoy sisteme geçer.

| Bileşen | Görev | Güvenlik Notu |
|---|---|---|
| LUKS gerçek bölüm | Asıl veriyi korur | Yanlış parola ile asla açılmaz |
| Decoy root | Sahte masaüstü sağlar | Gerçek verilere erişimi olmamalıdır |
| Initramfs hook | Karar mekanizmasıdır | Parolaları kaydetmemelidir |
| Audit kaydı | Olay sayacı tutar | Hassas bilgi içermemelidir |

Bu tasarımın en önemli ilkesi şudur: Decoy ortam “inandırıcı” olabilir, ama saldırgana zarar vermemeli, parola toplamamalı ve üçüncü taraf sistemlere saldırı yapmamalıdır. Amaç alarm üretmek ve gerçek veriyi korumaktır.

## Eşik mantığı

Sistem, örneğin üç başarısız denemeden sonra decoy ortamı açabilir. Yanlışlıkla kendi kendinizi decoy’a düşürme ihtimali de hesaplanmalıdır. Eğer her denemede doğru girme olasılığınız $q$ ise, $N$ başarısız denemeden sonra decoy’a düşme olasılığı yaklaşık:

$$P_{decoy} = (1-q)^N$$

Örneğin $q=0.9$ ve $N=3$ için:

$$P_{decoy} = 0.1^3 = 0.001$$

Yani binde bir. Bu yüzden eşik değeri güvenlik ile kullanılabilirlik arasında dengelenmelidir.

| Strateji | Avantaj | Dezavantaj |
|---|---|---|
| Tek hatada decoy | Hızlı tepki | Kullanıcı hatasında riskli |
| 3 hatada decoy | Dengeli | Saldırgana birkaç deneme verir |
| Panik parolası | Kontrollü tetikleme | Parola yönetimi karmaşıklaşır |
| Ayrı decoy disk | Temiz izolasyon | Kurulum maliyeti artar |

## Karar akışı

Aşağıdaki örnek gerçek sisteme doğrudan kopyalanacak üretim kodu değil, mantığı göstermek için yazılmış güvenli bir iskelettir. Gerçek uygulamada bunu `initramfs-tools` veya `dracut` hook yapısına uyarlamak gerekir.

```bash
MAX_FAILS=3
fails=0
REAL_DEV=/dev/nvme0n1p3
DECOY_BOOT=/dev/nvme0n1p4

while true; do
  echo 'LUKS parolasını girin:'

  if cryptsetup open --test-passphrase $REAL_DEV; then
    echo 'Doğrulama başarılı, gerçek sistem açılıyor.'
    exec /sbin/boot-real-root
  fi

  fails=$((fails + 1))
  echo 'Parola doğrulanamadı.'

  if [ $fails -ge $MAX_FAILS ]; then
    echo 'Sistem hazırlanıyor...'
    exec /sbin/boot-decoy-root $DECOY_BOOT
  fi

  sleep 2
done
```

Burada dikkat edilmesi gereken nokta, script’in parolayı dosyaya yazmamasıdır. Ayrıca decoy’a geçerken kullanılan bölüm gerçek LUKS bölümünden tamamen bağımsız olmalıdır.

## Decoy masaüstünü inandırıcı yapmak

Decoy sistemin amacı saldırganı oyalamak değil, gerçek veriye ulaştığını düşündürürken hiçbir kritik bilgi sunmamaktır. Örneğin:

- Sahte belgeler ve örnek proje klasörleri bulunabilir.
- Tarayıcı geçmişi gerçek hesaplara bağlı olmamalıdır.
- Ağ erişimi kısıtlanmalı veya yalnızca güvenli bir izleme ağına açılmalıdır.
- Sistem salt-okunur imajdan başlatılıp her açılışta temizlenmelidir.

```ini
[decoy]
root_mode=readonly
network=restricted
audit=metadata_only
reset_on_boot=true
```

Bu yapılandırma fikri, decoy ortamın her açılışta temiz bir duruma dönmesini sağlar. Böylece saldırganın bıraktığı dosyalar kalıcı olmaz; yalnızca zaman, deneme sayısı ve cihaz durumu gibi zararsız metaveriler kaydedilir.

## Son söz

LUKS tabanlı bir sahte masaüstü tuzağı, kriptografiyi kırmaya çalışmaz; aksine kriptografinin sağlamlığını kabul edip aldatma katmanını boot sürecine ekler. En güvenli yaklaşım, gerçek veriyi hiçbir koşulda decoy ortama bağlamamak, parola toplamamak ve sistemi önce sanal makinede test etmektir. Doğru tasarlandığında bu yöntem, dizüstü bilgisayarınızı yalnızca kilitleyen değil, aynı zamanda saldırı davranışını görünür kılan akıllı bir savunma katmanına dönüştürür.
