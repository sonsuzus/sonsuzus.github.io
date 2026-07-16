---
layout: post
title: "Go ile Gerçek Zamanlı Sohbet Sunucusu: Binlerce Bağlantıya Hazır Minimal Mimari"
math: true
categories: 
  - Proje
tags: 
  - Go
  - WebSocket
  - Gerçek Zamanlı Uygulamalar
  - Backend
---

Bir sohbet uygulaması yazmak ilk bakışta “mesajı al, herkese gönder” kadar basit görünür; fakat işin içine binlerce aktif kullanıcı, kopan bağlantılar, eşzamanlı mesajlar ve düşük gecikme girince konu bir anda backend spor salonuna dönüşür. Go burada hafif goroutine’leri, kanal tabanlı iletişim modeli ve sade sözdizimiyle harika bir adaydır.
``

Gerçek zamanlı sohbetin temelinde HTTP’nin klasik “istek-cevap” modelinden farklı bir yaklaşım vardır. Normal HTTP’de istemci sunucuya sorar, sunucu cevaplar ve bağlantı kapanır. Sohbette ise bağlantının açık kalması, sunucunun da istediği an istemciye mesaj gönderebilmesi gerekir. Bu yüzden WebSocket kullanırız. WebSocket, tek bir TCP bağlantısı üzerinde çift yönlü iletişim sağlar.

Teorik olarak her bağlantı için bir iş parçacığı açmak pahalıdır. Go’nun goroutine modeli bu maliyeti azaltır. Kabaca düşünürsek klasik thread maliyeti $M_t$, goroutine maliyeti $M_g$ olsun. Genellikle $M_g \ll M_t$ olduğu için aynı RAM ile çok daha fazla eşzamanlı bağlantı yönetilebilir. Toplam bellek tüketimini basitçe şöyle düşünebiliriz:

$$M_{toplam} = n \times M_g + M_{uygulama}$$

Burada $n$ aktif bağlantı sayısıdır. Ama sadece hafif olmak yetmez; bağlantılar arasında güvenli mesaj aktarımı da gerekir. İşte burada Go kanalları ve merkezi bir “hub” yapısı devreye girer.

| Yaklaşım | Avantaj | Dezavantaj | Sohbet İçin Uygunluk |
|---|---|---|---|
| Klasik HTTP polling | Basit kurulum | Gereksiz istek yükü | Düşük |
| Long polling | Daha az gecikme | Bağlantı yönetimi karmaşık | Orta |
| WebSocket | Çift yönlü ve hızlı | Durum yönetimi gerekir | Yüksek |
| gRPC stream | Güçlü tip sistemi | Tarayıcı tarafı ek araç ister | Orta-Yüksek |

Minimal mimarimiz üç parçadan oluşacak: `Client`, `Hub` ve WebSocket handler. `Client` tek bir kullanıcı bağlantısını temsil eder. `Hub`, gelen mesajları tüm istemcilere dağıtan küçük trafik polisi gibidir.

```go
package main

import (
    "log"
    "net/http"

    "github.com/gorilla/websocket"
)

type Client struct {
    conn *websocket.Conn
    send chan []byte
}

type Hub struct {
    clients    map[*Client]bool
    broadcast  chan []byte
    register   chan *Client
    unregister chan *Client
}
```

Bu yapıların amacı nettir: `clients` aktif bağlantıları tutar, `broadcast` herkese gönderilecek mesajları taşır, `register` yeni gelenleri ekler, `unregister` ayrılanları siler. Kanallar sayesinde farklı goroutine’ler aynı veriye doğrudan saldırmaz; mesajlaşarak anlaşır.

Şimdi hub döngüsünü yazalım. Bu döngü sunucunun kalbidir; gelen olaya göre kullanıcı ekler, siler veya mesaj dağıtır.

```go
func (h *Hub) run() {
    for {
        select {
        case client := <-h.register:
            h.clients[client] = true

        case client := <-h.unregister:
            if _, ok := h.clients[client]; ok {
                delete(h.clients, client)
                close(client.send)
            }

        case message := <-h.broadcast:
            for client := range h.clients {
                select {
                case client.send <- message:
                default:
                    close(client.send)
                    delete(h.clients, client)
                }
            }
        }
    }
}
```

Buradaki `default` kısmı önemlidir. Eğer bir istemci mesajları okuyamayacak kadar yavaşsa, tüm sistemi kilitlemesine izin vermeyiz. Gerçek zamanlı sistemlerde “en yavaş kullanıcı herkesi bekletmemeli” kuralı altın değerindedir.

WebSocket yükseltmesini yapan handler ise HTTP bağlantısını kalıcı, çift yönlü bir kanala dönüştürür.

```go
var upgrader = websocket.Upgrader{
    CheckOrigin: func(r *http.Request) bool {
        return true
    },
}

func serveWs(hub *Hub, w http.ResponseWriter, r *http.Request) {
    conn, err := upgrader.Upgrade(w, r, nil)
    if err != nil {
        log.Println(err)
        return
    }

    client := &Client{conn: conn, send: make(chan []byte, 256)}
    hub.register <- client

    go client.writePump()
    go client.readPump(hub)
}
```

`readPump` istemciden gelen mesajları okur ve hub’a yollar. `writePump` ise hub’dan gelen mesajları istemciye yazar. Okuma ve yazmayı ayrı goroutine’lere bölmek, bağlantının aynı anda hem dinleyip hem konuşabilmesini sağlar.

```go
func (c *Client) readPump(hub *Hub) {
    defer func() {
        hub.unregister <- c
        c.conn.Close()
    }()

    for {
        _, message, err := c.conn.ReadMessage()
        if err != nil {
            break
        }
        hub.broadcast <- message
    }
}

func (c *Client) writePump() {
    defer c.conn.Close()

    for message := range c.send {
        if err := c.conn.WriteMessage(websocket.TextMessage, message); err != nil {
            break
        }
    }
}
```

Son olarak `main` fonksiyonu ile sistemi ayağa kaldırırız.

```go
func main() {
    hub := &Hub{
        clients:    make(map[*Client]bool),
        broadcast:  make(chan []byte),
        register:   make(chan *Client),
        unregister: make(chan *Client),
    }

    go hub.run()

    http.HandleFunc("/ws", func(w http.ResponseWriter, r *http.Request) {
        serveWs(hub, w, r)
    })

    log.Println("Sohbet sunucusu :8080 üzerinde çalışıyor")
    log.Fatal(http.ListenAndServe(":8080", nil))
}
```

Bu haliyle sunucu minimalisttir ama güçlü bir temel sunar. Üretim ortamında `CheckOrigin` kontrolünü sıkılaştırmalı, kullanıcı kimlik doğrulaması eklemeli, mesajlara oda bilgisi koymalı ve yatay ölçekleme için Redis Pub/Sub gibi bir ara katman kullanmalısınız. Yine de ana fikir değişmez: WebSocket bağlantıyı açık tutar, goroutine’ler hafif paralellik sağlar, hub ise mesaj trafiğini düzenler. Kısacası Go ile sohbet sunucusu yazmak, az kodla çok bağlantı yönetmenin en keyifli yollarından biridir.
