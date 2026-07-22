---
layout: post
title: "Netfilter ile Kedi Görsellerini Ters Çeviren HTTP Proxy Modülü"
math: true
categories: 
  - Proje
tags: 
  - linux
  - netfilter
  - proxy
  - http
  - kernel
---

Bazen yazılım projeleri ciddi bir problemi çözer; bazen de ağdan geçen kedi fotoğraflarını baş aşağı çevirerek ekip arkadaşlarını hafifçe şaşırtır. Bu yazıda Linux ağ alt sistemindeki netfilter kancalarına takılan, giden HTTP trafiğini yakalayan ve kedi görseli dönen yanıtları kullanıcı alanındaki küçük bir proxy ile ters çeviren deneysel bir modül tasarlıyoruz. Not: HTTPS şifreli olduğu için bu oyun yalnızca düz HTTP ve laboratuvar ortamı içindir.
``
Önce küçük bir gerçeklik kontrolü yapalım: Giden HTTP isteğinin içinde genellikle resim yoktur; istemci sadece `GET /cat.jpg` der. Resim, sunucudan gelen HTTP yanıtında bulunur. Bu yüzden mimarimiz iki parçalı olacak: kernel tarafında netfilter hook paketi işaretler veya kuyruğa alır, kullanıcı alanındaki proxy ise yanıt gövdesini okuyup gerekiyorsa görseli ters çevirir.

Netfilter, Linux kernel içinde paketlerin geçtiği kontrol noktaları sunar. Basitleştirilmiş akış şöyle düşünülebilir: paket üretildiğinde `LOCAL_OUT`, yönlendirilirken `FORWARD`, makineye girerken `LOCAL_IN` gibi kancalar devreye girer. Biz yerel makineden çıkan HTTP isteklerini hedeflediğimiz için `NF_INET_LOCAL_OUT` iyi bir başlangıçtır.

| Katman | Görev | Neden burada? |
|---|---|---|
| Netfilter hook | TCP/80 paketini yakalar | Kernel seviyesinde hızlı karar |
| NFQUEUE veya mark | Paketi proxy yoluna sokar | Kernelde resim işlemek pahalıdır |
| Kullanıcı alanı proxy | HTTP yanıtını değiştirir | Pillow gibi araçlar kullanılabilir |
| Tarayıcı | Değişmiş resmi görür | Kullanıcıya sihir gibi gelir |

Teorik olarak karar fonksiyonumuzu şöyle yazabiliriz: $F(p) = 1$ ise paket proxyye gider, $F(p) = 0$ ise normal akar. Pratikte $F(p)$, hedef portun 80 olup olmadığına bakar. Kedi tespiti ise daha yukarı katmanda yapılır: URL içinde `cat`, `kitten`, `kedi` geçmesi veya `Content-Type: image/jpeg` gibi başlıkların görülmesi. Basit skor mantığıyla $P(cat|url) = score/total$ diyebiliriz; eşik üstündeyse görsel çevrilir.

Kernel tarafındaki iskelet kod, paketin TCP ve hedef portunun 80 olup olmadığını kontrol eder. Aşağıdaki örnek tam bir modül değil, mantığı gösteren orta seviye bir kesittir:

```c
#include <linux/module.h>
#include <linux/netfilter.h>
#include <linux/netfilter_ipv4.h>
#include <linux/ip.h>
#include <linux/tcp.h>

static unsigned int cat_hook(void *priv,
    struct sk_buff *skb,
    const struct nf_hook_state *state) {

    struct iphdr *iph;
    struct tcphdr *tcph;

    if (!skb) return NF_ACCEPT;
    iph = ip_hdr(skb);
    if (!iph || iph->protocol != IPPROTO_TCP) return NF_ACCEPT;

    tcph = tcp_hdr(skb);
    if (!tcph) return NF_ACCEPT;

    if (ntohs(tcph->dest) == 80) {
        skb->mark = 0xC47;
    }

    return NF_ACCEPT;
}
```

Bu işaret daha sonra `iptables` veya `nftables` ile yerel proxyye yönlendirilebilir. Örneğin işaretli paketleri 8080 portuna almak gibi. Kernel içinde HTTP ayrıştırmaya çalışmak cazip görünse de parçalanmış TCP akışı, checksum güncelleme, bellek güvenliği ve performans nedeniyle kullanıcı alanı çok daha sağlıklı bir yerdir.

Proxy tarafında mantık şudur: isteği gerçek sunucuya gönder, yanıt başlıklarını oku, gövde bir görselse belleğe al, ters çevir, `Content-Length` değerini güncelle ve istemciye dön. Python ile minik bir örnek:

```python
from io import BytesIO
from PIL import Image

def flip_if_cat(url, headers, body):
    ctype = headers.get('Content-Type', '')
    looks_like_cat = any(x in url.lower() for x in ['cat', 'kitten', 'kedi'])

    if not looks_like_cat:
        return headers, body

    if not ctype.startswith('image/'):
        return headers, body

    img = Image.open(BytesIO(body))
    flipped = img.transpose(Image.Transpose.FLIP_TOP_BOTTOM)

    out = BytesIO()
    fmt = img.format or 'PNG'
    flipped.save(out, format=fmt)
    new_body = out.getvalue()

    headers['Content-Length'] = str(len(new_body))
    return headers, new_body
```

Buradaki en önemli ayrıntı, HTTP yanıtının sıkıştırılmış olabileceğidir. `Content-Encoding: gzip` varsa önce açmak, işlemden sonra tekrar sıkıştırmak gerekir. Ayrıca büyük görselleri tamamen belleğe almak yerine akış tabanlı işlemek daha güvenlidir. Deney ortamında ise `curl --proxy localhost:8080 http://site/cat.jpg` komutu ile hızlıca test yapılabilir.

| Problem | Basit çözüm | Üretim yaklaşımı |
|---|---|---|
| HTTPS görünmez | Sadece HTTP test et | Kurumsal izinli MITM gerekir |
| Büyük dosya | Boyut limiti koy | Streaming pipeline kullan |
| Yanlış pozitif | URL anahtarı ara | Hafif ML sınıflandırıcı ekle |

Sonuç olarak bu proje, netfilterın paket seviyesindeki gücü ile kullanıcı alanındaki esnekliği eğlenceli bir şekilde birleştiriyor. Kernel sadece trafiği seçiyor, proxy ise HTTP ve görsel işleme gibi karmaşık işleri üstleniyor. Böylece hem Linux ağ mimarisini öğreniyor hem de internetin kedilerini kısa süreliğine baş aşağı izliyoruz.
