---
layout: post
title: "Aircrack-ng ile Kablosuz Ağ Güvenlik Testleri: WEP, WPA ve WPA2"
math: true
categories: 
  - Bilgi
tags: 
  - Aircrack-ng
  - Wi-Fi Güvenliği
  - Sızma Testi
---

Kablosuz ağ güvenlik testi, yalnızca parolayı “kırmayı” denemek değildir; kullanılan protokolün güvenlik modelini, istemci davranışlarını ve parola politikasını birlikte değerlendirmektir. Aircrack-ng paketi bu süreçte trafiği izleme, paket yakalama ve parola dayanıklılığını çevrimdışı sınama gibi görevler sunar. Bu çalışmaları yalnızca sahibi olduğunuz veya test iznini yazılı olarak aldığınız, izole bir laboratuvar ağında gerçekleştirmelisiniz.

``

## Önce yetki, sonra terminal

Gerçek bir Wi-Fi ağına izinsiz bağlanmaya çalışmak, paket toplamak veya istemcilerin bağlantısını bozmak hukuki ve etik sonuçlar doğurabilir. Güvenli bir laboratuvar için ayrı bir erişim noktası, test amaçlı istemci, monitor mode destekleyen USB adaptör ve internete yönlendirilmeyen bir ağ kullanılabilir. “Yetkisiz erişim simülasyonu” burada gerçek bir üçüncü taraf ağına saldırmak değil, kontrollü ortamda zayıf yapılandırmanın oluşturacağı sonucu gözlemlemek anlamına gelir.

## Protokollerin teorik farkları

WEP, RC4 akış şifrelemesini kısa bir başlangıç vektörüyle kullanır. 24 bitlik IV alanı nedeniyle yoğun trafikte tekrarların oluşması kaçınılmazdır. Doğum günü paradoksuna benzer şekilde, $N$ olası değer arasındaki çakışma ihtimali yaklaşık olarak

$$P \approx 1-e^{-k(k-1)/(2N)}$$

ile ifade edilir. Yeterli paket toplandığında IV tekrarları anahtar hakkında istatistiksel bilgi sızdırabilir. Bu, güçlü görünen bir WEP parolasını bile güvenli yapmaz.

WPA, geçiş çözümü olarak TKIP’i; WPA2 ise çoğunlukla AES tabanlı CCMP’yi kullanır. WPA/WPA2-Personal testlerinde genellikle şifreleme matematiği doğrudan kırılmaz. Yakalanan kimlik doğrulama verisi üzerinden aday parolalar çevrimdışı denenir. Yaklaşık çalışma maliyeti $T=D/R$ şeklindedir; burada $D$ aday sayısı, $R$ ise saniyede test edilen aday miktarıdır. Uzun ve rastgele parola, $D$ değerini dramatik biçimde büyütür.

| Protokol | Temel teknoloji | Başlıca risk | Güvenlik kararı |
|---|---|---|---|
| WEP | RC4 ve 24 bit IV | IV tekrarları, yapısal zayıflıklar | Kesinlikle kullanılmamalı |
| WPA | TKIP | Eski tasarım, zayıf parola | Devre dışı bırakılmalı |
| WPA2 | AES-CCMP | Tahmin edilebilir PSK, yanlış yapılandırma | Güçlü parolayla kabul edilebilir |

## Kontrollü Aircrack-ng laboratuvarı

Önce adaptörün monitor mode desteği doğrulanır ve izleme arayüzü başlatılır:

```bash
sudo airmon-ng start wlan0
iw dev
```

İkinci komut, oluşan arayüzü ve çalışma modunu gösterir. Ardından yalnızca laboratuvar erişim noktasının BSSID ve kanalı hedeflenerek kayıt alınır:

```bash
sudo airodump-ng --channel <KANAL> \
  --bssid <LAB_BSSID> --write lab-kaydi wlan0mon
```

Bu komut paketleri `lab-kaydi-01.cap` benzeri bir dosyada saklar. WPA/WPA2 laboratuvarında kendi test istemcinizi normal biçimde ağa bağlayarak kimlik doğrulama kaydının oluşmasını bekleyin; başka istemcileri zorla düşüren yöntemlerden kaçının.

Parola politikasını denetlemek için yalnızca laboratuvar parolalarını içeren küçük ve izinli bir aday listesi kullanılabilir:

```bash
aircrack-ng -w ./izinli-test-listesi.txt \
  -b <LAB_BSSID> lab-kaydi-01.cap
```

Aircrack-ng burada ağa tekrar tekrar bağlanmaz; yakalanan doğrulama verisine karşı çevrimdışı aday kontrolü yapar. Parolanın listede bulunması, protokolün otomatik olarak kırıldığı anlamına değil, parola seçiminin tahmin edilebilir olduğuna işaret eder. WEP testinde ise paket sayısı arttıkça istatistiksel çözüm olasılığının yükselmesi doğrudan protokolün tasarım kusurunu gösterir.

## Bulguları savunmaya dönüştürmek

Rapor; kapsamı, cihazları, protokolü, yakalama süresini ve sonucun tekrar üretilebilirliğini içermelidir. WEP ve WPA-TKIP kapatılmalı, WPA2-AES veya mümkünse WPA3 seçilmeli, uzun ve benzersiz parolalar kullanılmalı, WPS devre dışı bırakılmalı ve erişim noktası yazılımı güncellenmelidir. Başarılı testin amacı ağa gizlice girmek değil, gerçek bir saldırgandan önce zayıflığı görüp düzeltmektir.
