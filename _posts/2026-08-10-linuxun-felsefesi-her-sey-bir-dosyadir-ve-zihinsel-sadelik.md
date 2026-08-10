---
layout: post
title: "Linux’un Felsefesi: “Her Şey Bir Dosyadır” ve Zihinsel Sadelik"
math: true
categories: 
  - Bilgi
tags: 
  - Linux
  - Unix felsefesi
  - bilişsel ekonomi
---

Linux terminalinde bir aygıtla konuşmak, bir günlük kaydını izlemek ve bir yapılandırmayı değiştirmek çoğu zaman aynı tanıdık araçlarla yapılır: `cat`, `echo`, `grep`, `read`, `write`. Bunun arkasındaki güçlü fikir, Unix dünyasının meşhur ilkesi olan **“her şey bir dosyadır”** yaklaşımıdır. Elbette bu ifade teknik olarak mutlak değildir; süreçler, soketler ve aygıtlar farklı çekirdek nesneleridir. Ancak kullanıcı alanında bunların önemli bir bölümü dosya benzeri arayüzlerle temsil edilir. Bu temsil tercihi, yalnızca mühendislik zarafeti değil, bilişsel ekonominin de başarılı bir örneğidir.
``
Bilişsel ekonomi, zihnin sınırlı dikkat, bellek ve karar verme kapasitesini mümkün olan en az maliyetle kullanma eğilimidir. Yeni bir sistem öğrenirken her nesne türü için ayrı bir etkileşim modeli öğrenmek pahalıdır. Linux ise farklı kaynakları ortak bir soyutlamada buluşturarak zihinsel model sayısını azaltır. Kullanıcının temel fikri şudur: “Bir şeye erişmek istiyorsam, önce onun yolunu bulur; sonra okur, yazar veya filtrelerim.”

Bu sadeleştirmenin kaba bir maliyet modeli şöyle düşünülebilir:

$$C_{öğrenme} \approx N_{model} \times C_{model} + N_{istisna} \times C_{istisna}$$

Burada $N_{model}$ öğrenilmesi gereken etkileşim modeli sayısını, $N_{istisna}$ ise özel durumları ifade eder. Unix, her şeyi gerçekten aynı yapıya zorlamak yerine, kullanıcıya görünen katmanda $N_{model}$ değerini düşürmeyi hedefler. Sonuç: daha az komut ezberi, daha hızlı keşif ve araçlar arasında daha kolay bilgi transferi.

| Kaynak türü | Linux’taki yaygın temsil | Tanıdık işlem | Zihinsel kazanç |
|---|---|---|---|
| Metin günlükleri | `/var/log/...` | `tail`, `grep` | Olayları dosya gibi tarama |
| Donanım aygıtı | `/dev/...` | okuma/yazma | Aygıta ortak arayüz |
| Süreç bilgisi | `/proc/...` | `cat`, `less` | Sistem durumunu inceleme |
| Sistem ayarları | `/sys/...` | `read`, `echo` | Yapılandırmayı keşfetme |

Örneğin çalışan süreçlerin CPU istatistiklerine bakmak için özel bir grafik arayüz zorunlu değildir. `/proc` sanal dosya sistemi, çekirdeğin anlık bilgisini dosya görünümünde sunar:

```bash
# İşlemci hakkında çekirdek tarafından sunulan bilgileri gösterir
cat /proc/cpuinfo | grep "model name" | head -n 1

# Bellek özetini insan tarafından okunabilir biçimde filtreler
grep -E "MemTotal|MemAvailable" /proc/meminfo
```

Bu komutların orta düzeydeki güzelliği, veriyi üretme, filtreleme ve sunma sorumluluklarını ayırmasıdır. `cat` veriyi okur, `grep` ilgilenilen satırları seçer, `head` ise çıktıyı sınırlar. Unix felsefesindeki “bir işi iyi yap” ilkesi burada devreye girer. Büyük, her şeyi yapan tek bir uygulama yerine küçük programlar boru hattıyla birleşir:

```bash
# Son hata kayıtlarını seçer, zaman sırasını ters çevirir ve ilk 10 sonucu gösterir
journalctl -p err --no-pager | tail -n 50 | grep -i "error" | head -n 10
```

Boru hattı (`|`), bilişsel açıdan bir cümle kurmaya benzer: önce veri gelir, sonra sıfatlar ve sınırlamalar eklenir. Her adım gözlemlenebilir olduğundan hata ayıklama da kolaylaşır. Komutun tamamı beklenmedik davranırsa ara parçaları tek tek çalıştırabilirsiniz.

Yine de ilkenin sınırları vardır. Bir aygıta `echo` ile yazmak her zaman güvenli değildir; `/sys` altındaki değerler donanım davranışını değiştirebilir. Ayrıca modern Linux’ta ağ soketleri, DBus servisleri ve konteyner katmanları dosya metaforunun ötesine geçen soyutlamalar sunar. Ama metafor hâlâ güçlüdür: karmaşıklığı yok etmez, onu yönetilebilir bir yüzeye taşır.

Linux’un minimalizmi, az özellik sunmak demek değildir. Asıl amaç, çok sayıda özelliği az sayıda tekrar eden fikirle kavranabilir kılmaktır. “Her şey bir dosyadır” ilkesi de bu yüzden bir teknik sloganın ötesindedir: zihnin sistemi daha az sürprizle, daha çok merakla keşfetmesini sağlayan bir tasarım sözleşmesidir.
