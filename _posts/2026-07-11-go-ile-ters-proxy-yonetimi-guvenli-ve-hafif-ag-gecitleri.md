---
layout: post
title: "Go ile Ters Proxy Yönetimi: Güvenli ve Hafif Ağ Geçitleri"
math: true
categories: 
  - Program
tags: 
  - go
  - reverse-proxy
  - load-balancing
  - networking
---

Modern web sistemlerinde istemci ile servisler arasına akıllı bir kapı koymak çoğu zaman hayat kurtarır. Go ile yazılmış hafif bir ters proxy, gelen HTTP trafiğini uygun backend servisine yönlendirebilir, temel güvenlik kontrolleri yapabilir ve yükü birden fazla sunucuya dağıtabilir. Üstelik Go’nun standart kütüphanesindeki `net/http` ve `httputil` paketleri sayesinde bunu devasa framework’lere ihtiyaç duymadan kurabilirsiniz.
``

Ters proxy, istemcinin gerçek uygulama sunucularıyla doğrudan konuşmasını engelleyen aracı katmandır. İstemci `api.ornek.com` adresine istek atar; ters proxy bu isteği arkadaki `service-1`, `service-2` veya `service-3` gibi sunuculara iletir. Böylece güvenlik, gözlemlenebilirlik, önbellekleme, TLS sonlandırma ve yük dengeleme tek noktadan yönetilebilir.

Temel farkı şöyle özetleyebiliriz:

| Özellik | Forward Proxy | Reverse Proxy |
|---|---|---|
| Kimi temsil eder? | İstemciyi | Sunucuyu |
| Kullanım amacı | İnternete kontrollü çıkış | Servislere kontrollü giriş |
| Gizlenen taraf | Kullanıcı/istemci | Backend sunucular |
| Örnek | Kurumsal internet proxy’si | API Gateway, Nginx, Traefik |

Yük dengelemenin mantığı ise basit ama kritiktir. Elimizde $n$ adet backend varsa ve gelen toplam istek sayısı $R$ ise ideal durumda her sunucunun yaklaşık yükü şu olur: $R_i \approx \frac{R}{n}$. Gerçekte CPU, bellek, ağ gecikmesi ve hata oranları farklı olduğundan bu dağılım her zaman eşit değildir. Bu yüzden round-robin, weighted round-robin veya least-connections gibi algoritmalar kullanılır.

| Algoritma | Mantık | Avantaj | Dezavantaj |
|---|---|---|---|
| Round Robin | Sırayla dağıtır | Basit ve hızlı | Sunucu gücünü dikkate almaz |
| Weighted Round Robin | Ağırlığa göre dağıtır | Güçlü sunucuya daha çok trafik verir | Ağırlık ayarı gerekir |
| Least Connections | En az bağlantılıya yollar | Dinamik yüke duyarlı | Takip maliyeti vardır |

Go’da en yalın ters proxy örneği `httputil.NewSingleHostReverseProxy` ile yazılabilir. Aşağıdaki kod, gelen isteği tek bir backend’e aktarır; ayrıca `X-Forwarded-Host` başlığıyla orijinal host bilgisini korur.

```go
package main

import (
    "log"
    "net/http"
    "net/http/httputil"
    "net/url"
)

func main() {
    target, err := url.Parse("http://localhost:8081")
    if err != nil {
        log.Fatal(err)
    }

    proxy := httputil.NewSingleHostReverseProxy(target)

    originalDirector := proxy.Director
    proxy.Director = func(req *http.Request) {
        originalDirector(req)
        req.Header.Set("X-Forwarded-Host", req.Host)
        req.Header.Set("X-Gateway", "go-reverse-proxy")
    }

    log.Println("Proxy :8080 üzerinde çalışıyor")
    log.Fatal(http.ListenAndServe(":8080", proxy))
}
```

Bu kodda `Director`, isteğin backend’e gitmeden önce nasıl değiştirileceğini belirler. Örneğin path yeniden yazılabilir, header eklenebilir veya belirli istekler engellenebilir. Pratikte burada kimlik doğrulama, IP filtreleme ya da rate limit kontrolü de uygulanabilir.

Şimdi bunu küçük bir round-robin yük dengeleyiciye çevirelim:

```go
package main

import (
    "log"
    "net/http"
    "net/http/httputil"
    "net/url"
    "sync/atomic"
)

type Backend struct {
    URL   *url.URL
    Proxy *httputil.ReverseProxy
}

type LoadBalancer struct {
    backends []Backend
    counter  uint64
}

func (lb *LoadBalancer) ServeHTTP(w http.ResponseWriter, r *http.Request) {
    index := atomic.AddUint64(&lb.counter, 1) % uint64(len(lb.backends))
    backend := lb.backends[index]
    r.Header.Set("X-Selected-Backend", backend.URL.String())
    backend.Proxy.ServeHTTP(w, r)
}

func main() {
    addresses := []string{
        "http://localhost:8081",
        "http://localhost:8082",
        "http://localhost:8083",
    }

    lb := &LoadBalancer{}
    for _, addr := range addresses {
        u, err := url.Parse(addr)
        if err != nil {
            log.Fatal(err)
        }
        lb.backends = append(lb.backends, Backend{
            URL:   u,
            Proxy: httputil.NewSingleHostReverseProxy(u),
        })
    }

    log.Println("Load balancer :8080 üzerinde hazır")
    log.Fatal(http.ListenAndServe(":8080", lb))
}
```

Burada `atomic.AddUint64`, eşzamanlı isteklerde sayaç yarışını engeller. Her istek farklı backend’e gönderilir. Matematiksel olarak seçim `index = counter \bmod n` şeklindedir. Yani sayaç büyür, backend listesi döngüsel biçimde kullanılır.

Güvenlik tarafında birkaç noktayı atlamamak gerekir. Proxy’niz dış dünyaya açık olduğu için header spoofing, yavaş istek saldırıları ve büyük body gönderimleriyle karşılaşabilir. `http.Server` yapılandırmasında timeout değerleri vermek iyi bir başlangıçtır.

```go
server := &http.Server{
    Addr:              ":8080",
    Handler:           lb,
    ReadHeaderTimeout: 5 * time.Second,
    ReadTimeout:       10 * time.Second,
    WriteTimeout:      15 * time.Second,
    IdleTimeout:       60 * time.Second,
}
```

Sonuç olarak Go, ters proxy yazmak için şaşırtıcı derecede güçlü bir araçtır. Küçük bir kod tabanıyla trafik yönlendirme, servis gizleme ve basit yük dengeleme yapabilirsiniz. Üretim ortamında buna health check, loglama, metrik toplama, TLS ve circuit breaker eklediğinizde kendi mini API gateway’inizi inşa etmiş olursunuz. Kısacası: Go ile ağ geçidi yazmak, hem öğretici hem de oldukça keyifli bir mühendislik egzersizidir.
