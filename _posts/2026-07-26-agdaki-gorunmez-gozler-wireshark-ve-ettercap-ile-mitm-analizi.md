---
layout: post
title: "Ağdaki Görünmez Gözler: Wireshark ve Ettercap ile MitM Analizi"
math: true
categories: 
  - Bilgi
tags: 
  - Wireshark
  - Ettercap
  - ağ güvenliği
---

Bir ağdan geçen veriler gerçekten görünmez mi? Ne yazık ki hayır. Özellikle şifrelenmemiş protokoller kullanıldığında paketler, aynı ağı paylaşan kötü niyetli kişiler tarafından okunabilir. Wireshark ve Ettercap, yalnızca izinli laboratuvar ortamlarında kullanıldığında bu riski gözlemlemek, paketlerin yapısını öğrenmek ve savunma yöntemlerini test etmek için oldukça güçlü araçlardır.

``

## Paket dinleme nasıl çalışır?

Bilgisayarlar iletişim kurarken veriyi küçük paketlere böler. Her pakette kaynak ve hedef adresleri, kullanılan protokol ve taşınan veri gibi alanlar bulunur. Ağ kartı normalde yalnızca kendisine gönderilen çerçeveleri işler. **Promiscuous mode** etkinleştirildiğinde ise erişebildiği diğer çerçeveleri de yakalama yazılımına iletebilir.

Yakalanan veri miktarı yaklaşık olarak

$$D = R \times t$$

şeklinde düşünülebilir. Burada $R$ saniyedeki ortalama trafik miktarını, $t$ dinleme süresini, $D$ ise incelenecek toplam veriyi temsil eder. Yoğun bir ağda kısa süreli kayıtların bile hızla büyümesinin nedeni budur.

| Özellik | Wireshark | Ettercap |
|---|---|---|
| Temel amaç | Paket yakalama ve ayrıntılı analiz | MitM senaryolarını laboratuvarda inceleme |
| Kullanım biçimi | Grafik arayüz ve görüntüleme filtreleri | Grafik veya terminal arayüzü |
| Güçlü yanı | Protokol çözümleme | Ağ uçları arasındaki akışı gözlemleme |
| Başlıca risk | Hassas verilerin kaydedilmesi | Aktif ağ müdahalesi ve bağlantı bozulması |

## Wireshark ile güvenli trafik analizi

Kendi bilgisayarınızda veya izole bir sanal laboratuvarda doğru ağ arayüzü seçilerek kayıt başlatılabilir. Wireshark yüzlerce protokolü tanıdığı için filtre kullanmak önemlidir. Aşağıdaki görüntüleme filtreleri mevcut kayıt içerisindeki paketleri daraltır; yeni bir saldırı gerçekleştirmez:

```text
http

dns

tcp.port == 80

ip.addr == 192.0.2.10
```

`http`, şifrelenmemiş HTTP paketlerini; `dns`, alan adı sorgularını gösterir. `tcp.port == 80` belirli bir TCP portuna, `ip.addr` ise dokümantasyon amacıyla ayrılmış örnek bir IP adresine odaklanır. Bir paket seçildiğinde Ethernet, IP, TCP ve uygulama katmanları ayrı ayrı açılarak başlık bilgileri incelenebilir.

Komut satırında yalnızca kendi arayüzünüzde temel bir protokol özeti görmek için TShark da kullanılabilir:

```bash
tshark -i <izinli-arayuz> -f "tcp port 80"
```

Bu komut HTTP içeriğini değiştirmez; belirtilen arayüzdeki 80 numaralı TCP portuna ait trafiği görüntüler. Yakalama dosyaları hassas bilgi içerebileceğinden paylaşılmadan önce anonimleştirilmelidir.

## Ettercap ve ortadaki adam mantığı

MitM saldırısında saldırgan, iki uç arasındaki iletişimin ortasına yerleşmeye çalışır. Yerel ağlarda bunun tarihsel örneklerinden biri, sahte ARP yanıtlarıyla cihazların IP–MAC eşleştirmelerini yanıltmaktır. Trafik saldırgan üzerinden geçerse şifrelenmemiş içerik okunabilir veya değiştirilebilir.

Ettercap bu davranışı eğitim laboratuvarlarında canlandırabilir; ancak aktif ARP manipülasyonu gerçek ağlarda kesintiye, veri ihlaline ve hukuki sonuçlara yol açabilir. Bu nedenle saldırı komutları üretim ağında denenmemeli; yalnızca sahibi olduğunuz, internetten ayrılmış sanal makinelerde ve açık izinle çalışılmalıdır.

## Şifreleme neden oyunu değiştirir?

HTTP kullanıldığında istek yolu, başlıklar ve form alanları açık biçimde görülebilir. HTTPS ise uygulama verisini TLS ile şifreler. Dinleyici IP adresleri, portlar ve paket boyutları gibi metaverileri görebilse de içerik uygun anahtar olmadan anlamlı değildir.

| Protokol | İçerik görünürlüğü | Tercih |
|---|---|---|
| HTTP, FTP, Telnet | Genellikle açık metin | Kullanılmamalı |
| HTTPS, SFTP, SSH | Şifreli | Önerilir |
| Güvensiz Wi-Fi | Dinlemeye daha açık | VPN ve HTTPS kullanılmalı |

Savunma için HTTPS zorunluluğu, güvenli DNS seçenekleri, VPN, dinamik ARP denetimi, istemci izolasyonu ve sertifika uyarılarının ciddiye alınması önemlidir. Wireshark ile olağan dışı ARP yanıtları veya tekrarlanan adres değişimleri araştırılabilir. Kısacası bu araçların en değerli kullanımı başkalarının verisini yakalamak değil, kendi ağımızın hangi koşullarda savunmasız kaldığını görüp şifrelemeyi doğru uygulamaktır.
