---
layout: post
title: "SSH, Mikrofon ve Hoparlör Üçgeninde Etik Akustik Geri Besleme"
math: true
categories: 
  - Bilgi
tags: 
  - ssh
  - ses sistemleri
  - linux
  - etik güvenlik
---

Uzaktaki bir makinenin mikrofonunu açıp hoparlöre yönlendirmek teknik olarak ses yönlendirme, gecikme ve kazanç yönetimi konularına dokunur; fakat aynı zamanda çok ciddi mahremiyet riski taşır. Bu nedenle bu yazı, bir odayı gizlice dinleten bir düzenek kurma rehberi değil; yalnızca yetkili laboratuvar, konferans odası testi veya kendi cihazında yapılan kapalı devre akustik doğrulama için teorik ve güvenli bir çerçevedir.
``

## Önce etik sınır: SSH anahtarın varsa her şeyi yapabilir misin?

Hayır. SSH erişimi teknik yetki verir, hukuki ve etik izin vermez. Mikrofon, kamera gibi algılayıcılar kişisel veri toplar. Bir makinede yönetici olsan bile ortamda bulunan herkesin açık rızası olmadan mikrofonu etkinleştirip odadan ses almak kabul edilemez. Güvenli yaklaşım şudur: cihaz sahibi, ortam kullanıcıları ve test zamanı önceden belli olmalı; kayıt yapılmamalı; test göstergesi görünür olmalı.

| Senaryo | Kabul edilebilir mi? | Not |
|---|---:|---|
| Kendi dizüstünde hoparlör-mikrofon gecikmesi ölçmek | Evet | Yerel ve kontrollü |
| Toplantı odasında anons sistemi testi | Evet | Katılımcılara haber verilirse |
| SSH ile kimseye haber vermeden mikrofonu açmak | Hayır | Mahremiyet ihlali |
| Sanal ses aygıtında test sinyali döndürmek | Evet | Gerçek ortam sesi toplanmaz |

## Akustik geri beslemenin mantığı

Mikrofondan alınan sinyal hoparlörden tekrar ortama verildiğinde bir döngü oluşur. Basitleştirilmiş model:

$$y(t)=G \cdot x(t-\tau)$$

Burada $G$ toplam kazanç, $\tau$ ise gecikmedir. Eğer belirli bir frekansta döngü kazancı $G(f) \ge 1$ olur ve faz yaklaşık $2\pi k$ hizasına gelirse sistem ıslık, uğultu veya çınlama üretir. Yani sorun sadece sesin yüksekliği değil; mikrofon-hoparlör mesafesi, oda yansımaları, ekolayzır ve gecikmedir.

| Kavram | Düşük değer | Yüksek değer |
|---|---|---|
| Kazanç $G$ | Daha stabil | Feedback riski artar |
| Gecikme $\tau$ | Doğal his | Yankı belirginleşir |
| Mikrofon-hoparlör mesafesi | Kaçak artabilir | Kaçak azalabilir |
| Oda yansıması | Kuru ses | Rezonans ve uğultu |

## SSH burada ne işe yarar?

SSH, ses kablosu değil; uzaktan yönetim kanalıdır. Güvenli kullanımda SSH ile cihaz durumu okunabilir, test servisleri başlatılabilir veya sanal ses aygıtları denetlenebilir. Örneğin aşağıdaki komutlar yalnızca ses altyapısını listeler; mikrofonu canlı dinlemeye açmaz:

```bash
ssh admin@lab-makinesi 'hostname; pactl info; pactl list short sources; pactl list short sinks'
```

Bu çıktılar PipeWire/PulseAudio üzerinde hangi giriş ve çıkışların bulunduğunu anlamaya yarar. Burada kritik nokta, gerçek mikrofon kaynağını hoparlöre bağlayan otomatik bir komut çalıştırmamaktır.

## Güvenli test: gerçek oda sesi yerine sanal kaynak

Akustik zinciri öğrenmek için önce sanal bir çıkış oluşturmak daha güvenlidir. Böylece gerçek ortam sesi toplanmaz:

```bash
pactl load-module module-null-sink sink_name=lab_sink sink_properties=device.description=Lab_Test_Sink
pactl list short sinks
```

Bu komut bir null sink oluşturur. Yani ses sistemi içinde hedef gibi görünen ama fiziksel hoparlöre gitmeyen bir test noktası üretir. Ardından kısa bir test tonu yerel makinede çalınabilir:

```bash
speaker-test -t sine -f 440 -l 1
```

440 Hz tonu, zincirin çalışıp çalışmadığını anlamak için klasik ve zararsız bir referanstır. Ölçüm yaparken ses seviyesini düşük tutmak kulak sağlığı açısından önemlidir.

## Basit güvenlik kapısı fikri

Yetkili laboratuvarlarda bile test komutlarının yanlışlıkla çalışmasını önlemek gerekir. Aşağıdaki örnek betik, açık rıza dosyası yoksa testi durdurur:

```bash
#!/usr/bin/env bash
set -euo pipefail

CONSENT_FILE='/tmp/audio-test-consent-ok'

if [ ! -f "$CONSENT_FILE" ]; then
  echo 'Onay dosyası yok. Ses testi başlatılmadı.'
  exit 1
fi

echo 'Onay bulundu. Sadece cihaz listesi okunuyor.'
pactl list short sources
pactl list short sinks
```

Bu betik bir güvenlik çözümü değil, iyi alışkanlık örneğidir. Asıl güvenlik; süreç, bilgilendirme ve erişim kontrolünden gelir.

## Sonuç

Mikrofonu hoparlöre döndürmek, sinyal işleme açısından eğitici bir konudur: kazanç, faz, gecikme ve oda akustiği aynı anda devreye girer. Fakat SSH üzerinden uzaktaki bir ortamın sesini dinlemek, izinsiz yapıldığında teknik meraktan çıkar ve mahremiyet ihlaline dönüşür. En doğru yol; sanal aygıtlarla öğrenmek, fiziksel testlerde açık rıza almak ve gerçek mikrofon verisini yalnızca gerekli, görünür ve kayıt dışı koşullarda kullanmaktır.
