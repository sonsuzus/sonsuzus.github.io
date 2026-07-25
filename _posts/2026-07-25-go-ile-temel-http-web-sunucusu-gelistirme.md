---
layout: post
title: "Go ile Temel HTTP Web Sunucusu Geliştirme"
math: true
categories: 
  - Program
tags: 
  - go
  - http
  - web-sunucusu
  - standart-kutuphane
---

Go ile web sunucusu yazmak, mutfağa girip “Ben bugün internet pişireceğim” demek gibidir: az malzemeyle şaşırtıcı derecede doyurucu sonuç alırsın. Go’nun standart kütüphanesindeki `net/http` paketi, harici framework kurmadan HTTP isteklerini dinleyen, yönlendiren ve yanıtlayan sade ama güçlü bir sunucu ayağa kaldırmamızı sağlar.
``

## HTTP Mantığını Kısaca Isıtalım

HTTP, istemci ile sunucu arasında yapılan istek-yanıt tabanlı bir protokoldür. Tarayıcı istemcidir; Go ile yazdığımız uygulama ise sunucudur. İstemci “Bana `/` adresini ver” der, sunucu da “Buyur, içerik burada” diye yanıt döner.

Bu model basitçe şöyle düşünülebilir:

$$İstek + İşleyici = Yanıt$$

Daha teknik bir bakışla yanıt süresi şu şekilde modellenebilir:

$$T_{yanıt} = T_{ağ} + T_{işleme} + T_{veri}$$

Yani iyi bir web sunucusu yalnızca çalışmakla kalmaz; istekleri doğru yakalar, hızlı işler ve anlaşılır yanıt üretir.

| Kavram | Ne İşe Yarar? | Go’daki Karşılığı |
|---|---|---|
| Client | İstek gönderen taraf | Tarayıcı, Postman, curl |
| Server | İstekleri dinleyen uygulama | `http.ListenAndServe` |
| Route | URL yoluna göre yönlendirme | `/`, `/api`, `/hello` |
| Handler | İsteğe cevap veren fonksiyon | `http.HandleFunc` |
| Response | İstemciye dönen çıktı | `http.ResponseWriter` |

## İlk Go HTTP Sunucusu

Aşağıdaki örnek, kök adrese gelen HTTP isteklerini karşılayan sade bir Go web sunucusudur:

```go
package main

import (
    "fmt"
    "log"
    "net/http"
)

func homeHandler(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintln(w, "Merhaba! Go HTTP sunucusu çalışıyor.")
}

func main() {
    http.HandleFunc("/", homeHandler)

    log.Println("Sunucu http://localhost:8080 üzerinde çalışıyor...")
    err := http.ListenAndServe(":8080", nil)
    if err != nil {
        log.Fatal(err)
    }
}
```

Bu kodda `http.HandleFunc`, belirli bir URL yolunu fonksiyona bağlar. `/` yoluna istek geldiğinde `homeHandler` çalışır. `http.ResponseWriter`, istemciye yanıt yazmamızı sağlar. `*http.Request` ise gelen isteğin metodunu, başlıklarını, yolunu ve gövdesini taşır.

Programı çalıştırmak için:

```bash
go run main.go
```

Ardından tarayıcıda `http://localhost:8080` adresine gittiğinde mesajı görürsün. Tebrikler, artık kendi mini web sunucun var!

## İstek Metodunu Kontrol Etmek

HTTP’de her istek aynı değildir. `GET` veri okumak, `POST` veri göndermek için kullanılır. Handler içinde metodu kontrol ederek daha bilinçli davranabiliriz:

```go
func helloHandler(w http.ResponseWriter, r *http.Request) {
    if r.Method != http.MethodGet {
        http.Error(w, "Sadece GET desteklenir", http.StatusMethodNotAllowed)
        return
    }

    name := r.URL.Query().Get("name")
    if name == "" {
        name = "Gopher"
    }

    fmt.Fprintf(w, "Merhaba, %s!", name)
}
```

Bu fonksiyon `/hello?name=Ayse` gibi bir istek aldığında kişiselleştirilmiş yanıt üretir. Boş gelirse varsayılan olarak `Gopher` der. Küçük ama üretim mantığına yakın bir davranış!

| Yaklaşım | Avantaj | Ne Zaman Kullanılır? |
|---|---|---|
| Sadece `/` handler | Çok basit ve hızlı | Deneme, prototip |
| Çoklu route | Daha düzenli yapı | Küçük API’ler |
| Method kontrolü | Güvenli davranış | REST mantığı |
| JSON yanıt | Modern istemcilerle uyum | API geliştirme |

## JSON Yanıt Döndürmek

Web sunucuları çoğu zaman HTML değil JSON döndürür. Go’da bu da standart kütüphane ile mümkündür:

```go
func statusHandler(w http.ResponseWriter, r *http.Request) {
    w.Header().Set("Content-Type", "application/json")
    fmt.Fprintln(w, `{"status":"ok","message":"Sunucu ayakta"}`)
}
```

Header ayarı önemlidir; istemciye “Benim yanıtım JSON formatında” demiş oluruz. Bu küçük detay, API tüketen uygulamaların doğru davranmasını sağlar.

## Sonuç

Go ile temel HTTP sunucusu geliştirmek, web’in çalışma mantığını öğrenmek için harika bir başlangıçtır. Framework kullanmadan route, handler, request, response ve method gibi temel kavramları çıplak gözle görürsün. Bu sayede ileride Gin, Echo veya Fiber gibi framework’lere geçtiğinde arka planda neler döndüğünü çok daha iyi anlarsın. Kısacası Go’nun `net/http` paketi, küçük projeler için yeterince sade; büyük fikirler içinse yeterince güçlüdür.
