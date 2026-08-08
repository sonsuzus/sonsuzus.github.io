---
layout: post
title: "C ile Epoll Tabanlı Bloklamayan Web Sunucusu Yazmak"
math: true
categories: 
  - Proje
tags: 
  - C
  - epoll
  - asenkron-programlama
---

Bir web sunucusunun aynı anda binlerce istemciyle konuşabilmesi, her bağlantıya ayrı bir iş parçacığı tahsis etmekten çok daha akıllı bir yaklaşım gerektirir. Bu projede Linux üzerinde `epoll`, BSD ve macOS tarafında ise benzer görev üstlenen `kqueue` mantığını inceleyerek bloklamayan, olay güdümlü ve küçük ama öğretici bir HTTP sunucusunun temelini kuracağız.
``

## Neden klasik yaklaşım yetmez?

En basit sunucular `accept()` ile bağlantı kabul eder, ardından `read()` çağrısıyla veri bekler. Ancak bu fonksiyonlar bloklayan kipte çalışırsa yavaş bir istemci tüm yürütme akışını durdurabilir. Her bağlantı için yeni bir thread açmak sorunu kısmen çözer; fakat binlerce thread bellek tüketir, zamanlayıcıyı yorar ve bağlam değiştirme maliyeti oluşturur.

Yaklaşık bellek tüketimini şöyle düşünebiliriz:

$$M \approx N \times S$$

Burada $N$ bağlantı veya thread sayısını, $S$ ise her thread’in stack boyutunu temsil eder. 10.000 thread ve 1 MB stack kullanıldığında teorik ihtiyaç yaklaşık 10 GB olur. Olay döngüsünde ise az sayıda thread, binlerce soketi izleyebilir.

| Model | Ölçeklenebilirlik | Bellek maliyeti | Programlama zorluğu |
|---|---:|---:|---:|
| Bağlantı başına thread | Orta | Yüksek | Düşük |
| `select` / `poll` | Orta | Orta | Orta |
| `epoll` / `kqueue` | Yüksek | Düşük | Yüksek |

`select` her turda tüm dosya tanıtıcılarını tararken `epoll_wait`, yalnızca hazır olayları döndürür. Basitleştirilmiş maliyet karşılaştırması `select` için $O(N)$, hazır olay sayısı $K$ olan bir olay döngüsü için yaklaşık $O(K)$ şeklindedir.

## Soketleri bloklamayan kipe almak

Linux soketini `O_NONBLOCK` bayrağıyla yapılandırırız. Böylece hemen tamamlanamayan `accept`, `read` veya `write` işlemleri programı uyutmak yerine `EAGAIN` hatası döndürür.

```c
static int make_nonblocking(int fd) {
    int flags = fcntl(fd, F_GETFL, 0);
    if (flags == -1) return -1;
    return fcntl(fd, F_SETFL, flags | O_NONBLOCK);
}
```

Bu küçük yardımcı, hem dinleme soketine hem de kabul edilen istemci soketlerine uygulanmalıdır.

## Epoll olay döngüsü

Dinleme soketi oluşturulup `bind()` ve `listen()` çağrıları tamamlandıktan sonra bir epoll örneği açılır:

```c
int epfd = epoll_create1(0);

struct epoll_event ev = {
    .events = EPOLLIN,
    .data.fd = server_fd
};
epoll_ctl(epfd, EPOLL_CTL_ADD, server_fd, &ev);

for (;;) {
    struct epoll_event events[1024];
    int count = epoll_wait(epfd, events, 1024, -1);

    for (int i = 0; i < count; i++) {
        int fd = events[i].data.fd;

        if (fd == server_fd) {
            accept_clients(server_fd, epfd);
        } else if (events[i].events & EPOLLIN) {
            handle_request(fd, epfd);
        }
    }
}
```

`accept_clients` fonksiyonu tek bağlantı kabul edip dönmemelidir. Edge-triggered kullanımda `accept()` çağrısı `EAGAIN` verene kadar döngü sürmelidir. Aynı kural `read()` için de geçerlidir; aksi hâlde sokette veri kalmasına rağmen yeni bildirim alınmayabilir.

## HTTP yanıtı ve kısmi yazmalar

Minimal bir yanıt şu biçimdedir:

```c
const char *response =
    "HTTP/1.1 200 OK\r\n"
    "Content-Length: 13\r\n"
    "Connection: close\r\n"
    "\r\n"
    "Merhaba HTTP!";
```

Bloklamayan `send()` yanıtın yalnızca bir bölümünü yazabilir. Bu nedenle her bağlantı için tampon, gönderilen bayt sayısı ve ayrıştırma durumu tutulmalıdır. Yazma tamamlanamazsa soket `EPOLLOUT` olayına kaydedilir; tamamlanınca bu ilgi kaldırılır. Sürekli `EPOLLOUT` izlemek işlemciyi gereksiz yere meşgul eder.

## Epoll ve kqueue farkı

| Özellik | epoll | kqueue |
|---|---|---|
| Platform | Linux | BSD, macOS |
| Okuma olayı | `EPOLLIN` | `EVFILT_READ` |
| Yazma olayı | `EPOLLOUT` | `EVFILT_WRITE` |
| Edge-triggered seçenek | `EPOLLET` | `EV_CLEAR` |

Taşınabilirlik için olay kayıtlarını soyutlayan küçük bir arayüz yazılabilir. Güvenli bir gerçek dünya sunucusunda ayrıca zaman aşımı kuyruğu, maksimum istek boyutu, HTTP ayrıştırıcısı, TLS, sinyal yönetimi ve bağlantı başına geri basınç bulunmalıdır. Böylece oyuncak sunucu, internetin huysuz istemcilerine karşı dayanıklı bir altyapıya dönüşür.
