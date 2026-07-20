---
layout: post
title: "eBPF ile Çekirdeği Derlemeden TCP Bağlantı Histogramı Yazmak"
math: true
categories: 
  - Proje
tags: 
  - eBPF
  - Linux
  - Ağ Gözlemleme
  - Python
  - BCC
---

Linux çekirdeğinin içine küçük, güvenli ve olay odaklı programlar bırakabildiğinizi düşünün; üstelik kernel modülü yazmadan, sistemi yeniden başlatmadan ve çekirdeği yeniden derlemeden. İşte eBPF tam olarak bu büyülü tornavida. Bu yazıda gelen TCP bağlantı isteklerini anlık sayan ve saniyelik değerleri terminalde histogram olarak gösteren mini bir ağ trafiği gözlemcisi tasarlayacağız.
``

## Neden eBPF?

Klasik ağ gözlemleme araçları çoğu zaman paketleri kullanıcı uzayına kopyalar. Bu pratik ama pahalıdır. eBPF ise olayın olduğu yere, yani çekirdeğe yakın çalışır. Bir TCP SYN geldiğinde ilgili kernel fonksiyonuna bağlanıp yalnızca sayaç artırırız. Kullanıcı uzayı ise periyodik olarak bu sayacı okur.

Temel fikir şu:

$$\lambda = \frac{\Delta N}{\Delta t}$$

Burada $\Delta N$ belirli sürede gelen bağlantı sayısı, $\Delta t$ ise ölçüm aralığıdır. Biz $\Delta t = 1$ saniye seçersek, her satır doğrudan bağlantı/saniye değerini verir.

| Yaklaşım | Nerede Çalışır? | Artısı | Eksisi |
|---|---:|---|---|
| tcpdump | Kullanıcı uzayı | Esnek paket analizi | Yoğun trafikte maliyetli |
| Kernel modülü | Çekirdek | Çok güçlü | Riskli, derleme ve bakım ister |
| eBPF | Çekirdek içinde doğrulanmış VM | Güvenli, dinamik, hızlı | Kernel sembolleri değişebilir |

## Mimari

Gözlemcimiz iki parçadan oluşacak:

1. **eBPF programı:** TCP bağlantı isteği geldiğinde sayaç artırır.
2. **Python/BCC tarafı:** Sayacı her saniye okur, farkı hesaplar ve ASCII histogram basar.

Histogramda çubuk uzunluğunu basitçe şu şekilde düşünebiliriz:

$$bar = \min(x, W)$$

$x$ saniyedeki bağlantı sayısı, $W$ terminalde izin verdiğimiz maksimum genişliktir. Yani 120 bağlantı gelse bile ekranı duman etmemek için çubuğu kırparız.

| Ölçüm | Açıklama | Kullanım |
|---|---|---|
| Toplam sayaç | Başlangıçtan beri gelen istek | Genel trafik yükü |
| Saniyelik fark | Son ölçümden bu yana artış | Anlık yoğunluk |
| Histogram | Saniyelik farkın görsel hali | Desen ve patlama analizi |

## Örnek Kod

Aşağıdaki örnek BCC kullanır. Ubuntu/Debian tarafında genellikle `sudo apt install bpfcc-tools python3-bpfcc` yeterlidir. Program, IPv4 TCP bağlantı isteklerini yakalamak için `tcp_v4_conn_request` fonksiyonuna kprobe bağlar. Bazı kernel sürümlerinde sembol adı değişebileceğinden üretimde BTF/CO-RE yaklaşımı daha sağlamdır.

```python
from bcc import BPF
import time

program = r'''
#include <uapi/linux/ptrace.h>

BPF_ARRAY(counter, u64, 1);

int count_tcp(struct pt_regs *ctx) {
    u32 key = 0;
    u64 *value = counter.lookup(&key);
    if (value) {
        __sync_fetch_and_add(value, 1);
    }
    return 0;
}
'''

bpf = BPF(text=program)
bpf.attach_kprobe(event='tcp_v4_conn_request', fn_name='count_tcp')

counter = bpf.get_table('counter')
previous = 0
width = 60

print('Gelen TCP bağlantıları izleniyor. Çıkmak için Ctrl+C')

while True:
    time.sleep(1)
    key = counter.Key(0)
    current = counter[key].value if key in counter else 0
    delta = current - previous
    previous = current

    bar_len = min(delta, width)
    bar = '█' * bar_len
    print(f'{time.strftime('%H:%M:%S')} | {delta:5d}/sn | {bar}')
```

Kodun çekirdek tarafındaki işi kasıtlı olarak küçüktür: sadece atomik sayaç artırır. eBPF doğrulayıcısı döngüleri, bellek erişimlerini ve güvenliği kontrol eder. Kullanıcı tarafı ise görselleştirme ve örnekleme gibi daha rahat işleri üstlenir. Bu ayrım önemlidir; çekirdekte ne kadar az iş, o kadar az risk.

## Çalıştırma ve Test

Programı root yetkisiyle çalıştırın:

```bash
sudo python3 tcp_histogram.py
```

Başka bir makineden veya aynı makinede farklı terminalden test etmek için:

```bash
for i in $(seq 1 25); do nc -zv 127.0.0.1 8080; done
```

Eğer 8080 üzerinde dinleyen servis yoksa bağlantı tamamlanmayabilir; yine de SYN isteği seviyesinde bazı olayları görebilirsiniz. Daha temiz test için küçük bir HTTP sunucusu açabilirsiniz:

```bash
python3 -m http.server 8080
```

## Dikkat Edilecek Noktalar

Bu araç paket içeriğini okumaz; sadece bağlantı isteklerini sayar. Bu yüzden gizlilik açısından daha hafiftir. Ancak saldırı analizi için kaynak IP, hedef port veya cgroup bazlı kırılımlar eklenebilir. Örneğin ileride `BPF_HASH` ile port başına sayaç tutup histogramı servis bazında ayırabilirsiniz.

eBPF burada bize süper gücü verir: çalışan çekirdeğe mikroskop takmak. Doğru noktaya küçük bir prob yerleştirir, veriyi minimum maliyetle toplar ve kullanıcı uzayında anlaşılır hale getiririz. Sonuç: yeniden derleme yok, kernel panik ihtimali düşük, terminalde canlı ve eğlenceli bir TCP trafik radarımız var.
