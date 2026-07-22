---
layout: post
title: "Linux ile Kötü Ağ Simülatörü: Sanal Arayüzde %5 Paket Kaybı ve Rastgele Gecikme"
math: true
categories: 
  - Program
tags: 
  - linux
  - networking
  - tc-netem
  - devops
  - test
---

Uygulamanız lokal makinede ışık hızında çalışıyor olabilir; peki kullanıcı metroda, otel Wi‑Fi’ında ya da yağmurlu bir günde 4G’deyken ne olacak? Bu yazıda Linux üzerinde sanal bir ağ arayüzü oluşturup gelen paketlere yapay olarak %5 paket kaybı ve rastgele gecikme ekleyen küçük ama çok faydalı bir “kötü ağ simülatörü” kuracağız.
``

Bunun için Linux çekirdeğinin trafik kontrol sistemi olan `tc` ve onun meşhur `netem` modülünü kullanacağız. `netem`, network emulator demektir; paketleri geciktirebilir, düşürebilir, çoğaltabilir, bozabilir veya yeniden sıralayabilir. Bizim hedefimiz şu: izole bir test alanı oluşturmak, uygulamayı bu alanın içinden çalıştırmak ve dış dünyaya çıkan/gelen trafiği bozmak.

Teorik olarak paket kaybını şöyle düşünebiliriz: Her paketin düşme olasılığı $p = 0.05$ ise, bir paketin başarıyla ulaşma olasılığı $1-p = 0.95$ olur. Art arda $n$ paketin tamamının ulaşma olasılığı ise:

$$P(başarı) = (0.95)^n$$

Yani 100 paketlik küçük bir aktarımda bile tamamının sorunsuz ulaşma ihtimali yaklaşık $0.95^{100} \approx 0.0059$ olur. Kısacası %5 kulağa az gelir ama protokoller ve kullanıcı deneyimi üzerinde ciddi etkisi vardır.

| Kavram | Ne yapar? | Bizim senaryodaki rolü |
|---|---|---|
| `veth` | İki uçlu sanal ethernet kablosu oluşturur | Host ile test alanını bağlar |
| Network namespace | Ayrı ağ yığını sağlar | Uygulamayı izole çalıştırır |
| `tc` | Trafik kontrol aracıdır | Kuralları uygular |
| `netem` | Ağ davranışı taklit eder | Kaybı ve gecikmeyi üretir |

Önce gerekli araçların kurulu olduğundan emin olalım. Debian/Ubuntu için:

```bash
sudo apt update
sudo apt install iproute2 iputils-ping -y
```

Şimdi bir network namespace ve iki uçlu sanal arayüz oluşturalım. `bad0` host tarafında, `eth0` ise kötü ağ simülasyonunun içinde kalacak.

```bash
# Test namespace oluştur
sudo ip netns add badnet

# Sanal ethernet çifti oluştur
sudo ip link add bad0 type veth peer name eth0

# eth0 ucunu namespace içine taşı
sudo ip link set eth0 netns badnet

# IP adreslerini ver
sudo ip addr add 10.10.0.1/24 dev bad0
sudo ip netns exec badnet ip addr add 10.10.0.2/24 dev eth0

# Arayüzleri ayağa kaldır
sudo ip link set bad0 up
sudo ip netns exec badnet ip link set eth0 up
sudo ip netns exec badnet ip link set lo up
```

Bu noktada host ile namespace birbirini görebilir. Test edelim:

```bash
sudo ip netns exec badnet ping -c 3 10.10.0.1
```

Şimdi işin eğlenceli kısmı: paket kaybı ve gecikme. Gelen trafiği simüle etmek için host tarafındaki `bad0` arayüzünün namespace’e doğru gönderdiği paketlere kural ekleyeceğiz. Yani namespace açısından bu trafik “gelen paket” gibi davranır.

```bash
sudo tc qdisc add dev bad0 root netem loss 5% delay 120ms 60ms distribution normal
```

Bu komut şunu söyler: `bad0` üzerinden çıkan paketlerin %5’ini düşür, kalanlara ortalama 120 ms gecikme ekle, bu gecikmeyi 60 ms sapmayla rastgele dağıt. Basitçe gecikmeyi şöyle modelleyebiliriz:

$$D = 120ms + X$$

Burada $X$, normal dağılıma benzeyen rastgele bir sapmadır. Böylece her paket aynı sürede gelmez; gerçek ağlardaki “jitter” hissi oluşur.

| Ayar | Etki | Ne zaman kullanılır? |
|---|---|---|
| `loss 5%` | Paketlerin bir kısmı kaybolur | Mobil ağ, zayıf Wi‑Fi testi |
| `delay 120ms` | Sabit gecikme ekler | Uzak sunucu simülasyonu |
| `60ms` | Gecikmeyi rastgeleleştirir | Jitter testi |
| `distribution normal` | Daha doğal dağılım sağlar | Gerçekçi testler |

Eğer namespace içindeki bir uygulamanın internete çıkmasını istiyorsanız IP forwarding ve NAT da ekleyebilirsiniz:

```bash
sudo sysctl -w net.ipv4.ip_forward=1
sudo ip netns exec badnet ip route add default via 10.10.0.1

# eth0 yerine internete çıkan gerçek arayüzünüzü yazın; örn: wlan0 veya enp3s0
sudo iptables -t nat -A POSTROUTING -s 10.10.0.0/24 -o wlan0 -j MASQUERADE
```

Artık kötü ağın içinden komut çalıştırabilirsiniz:

```bash
sudo ip netns exec badnet curl https://example.com
sudo ip netns exec badnet ping -c 20 8.8.8.8
```

Sonuçlarda zaman zaman paket kaybı ve değişken ping süreleri görmelisiniz. Web API istemciniz burada timeout, retry, circuit breaker ve kullanıcıya hata gösterme davranışları açısından güzelce sınanır.

Kuralları görmek için:

```bash
tc qdisc show dev bad0
```

Simülasyonu kaldırmak için:

```bash
sudo tc qdisc del dev bad0 root
sudo ip netns del badnet
sudo ip link del bad0 2>/dev/null || true
```

Bu kurulum küçük görünür ama gerçek hayatta çok değerlidir. Çünkü iyi yazılım sadece hızlı ağda çalışan yazılım değildir; paketler kaybolduğunda sakin kalabilen, gecikmede paniklemeyen ve kullanıcıya düzgün geri bildirim verebilen yazılımdır. Kısacası artık bilgisayarınızda minik, kontrollü ve biraz da huysuz bir internet servis sağlayıcınız var.
