---
layout: post
title: "Go Kanalları ve Senkronizasyon: Goroutine’ler Arasında Güvenli Veri Trafiği"
math: true
categories: 
  - Bilgi
tags: 
  - go
  - goroutine
  - channels
  - senkronizasyon
---

Go dünyasında goroutine’ler sahneye çıktığında ortalık bir anda kalabalıklaşır: aynı anda çalışan fonksiyonlar, paralel iş akışları ve bolca hız! Fakat hızın yanında klasik bir soru gelir: Bu çalışan parçalar birbirleriyle nasıl güvenli konuşacak? Go’nun cevabı nettir: Belleği paylaşarak iletişim kurma; iletişim kurarak belleği paylaş.
``
Bu felsefenin merkezinde **channels**, yani kanallar bulunur. Kanalı, iki goroutine arasında uzanan tip güvenli bir boru gibi düşünebilirsin. Bir goroutine boruya veri bırakır, diğeri o veriyi alır. Böylece aynı değişkene aynı anda erişme, kilit unutma, yarış durumu üretme gibi klasik eşzamanlılık kabusları ciddi ölçüde azalır.

Teorik olarak problem şudur: Birden fazla yürütme birimi aynı belleğe erişirse ve en az biri yazma yaparsa, sonuç zamana bağlı hale gelir. Buna **race condition** deriz. Basitçe ifade edersek, iki işlem $A$ ve $B$ için belirli bir sıra garanti edilmiyorsa sonuç $A \rightarrow B$ veya $B \rightarrow A$ olabilir. Kanallar ise bu sırayı veri alışverişi üzerinden tanımlar. Bir gönderme işlemi, ilgili alma işlemi tamamlanmadan anlamlı biçimde bitmez. Bu da Go bellek modelinde bir tür **happens-before** ilişkisi oluşturur: $send(x) \rightarrow receive(x)$.

| Yaklaşım | Temel fikir | Risk | Go’daki araç |
|---|---|---|---|
| Paylaşılan bellek | Herkes aynı değişkeni okur/yazar | Race condition, deadlock | `sync.Mutex`, `sync.RWMutex` |
| Mesajlaşma | Goroutine’ler veri gönderip alır | Yanlış kanal tasarımı, bloklanma | `chan`, `select` |
| Atomik işlemler | Çok küçük kritik işlemler | Okunabilirlik düşebilir | `sync/atomic` |

En basit kanal örneğiyle başlayalım:

```go
package main

import "fmt"

func main() {
    mesajlar := make(chan string)

    go func() {
        mesajlar <- "Merhaba kanal!"
    }()

    msg := <-mesajlar
    fmt.Println(msg)
}
```

Burada `make(chan string)` ifadesi string taşıyan bir kanal oluşturur. `mesajlar <- ...` gönderme, `<-mesajlar` ise alma işlemidir. Dikkat çekici nokta şudur: Varsayılan yani **unbuffered** kanal, gönderici ve alıcıyı buluşturur. Gönderen goroutine, biri veriyi alana kadar bekler. Bu davranış, kanalın yalnızca veri taşımasını değil, aynı zamanda senkronizasyon aracı olmasını sağlar.

Kanalları matematiksel olarak küçük bir kuyruk gibi düşünebiliriz. Kapasite $k$ ise kanalda aynı anda en fazla $k$ eleman bulunur. Unbuffered kanal için $k = 0$ kabul edilir; yani veri bekleme salonunda oturamaz, doğrudan teslim edilmelidir.

```go
package main

import "fmt"

func main() {
    kuyruk := make(chan int, 2)

    kuyruk <- 10
    kuyruk <- 20

    fmt.Println(<-kuyruk)
    fmt.Println(<-kuyruk)
}
```

Bu örnekte kanalın kapasitesi 2’dir. İlk iki gönderim bloklanmaz; çünkü tamponda yer vardır. Ancak üçüncü bir gönderim yapılsaydı ve kimse okumuyorsa program beklemeye başlardı. Bu noktada kanal tasarımı önem kazanır: tampon, performans için faydalıdır ama yanlış kullanılırsa hatayı sadece biraz geciktiren yumuşak bir yastığa dönüşebilir.

Birden fazla kanalı dinlemek için Go’nun eğlenceli kontrol kulesi `select` kullanılır:

```go
package main

import (
    "fmt"
    "time"
)

func main() {
    hizli := make(chan string)
    yavas := make(chan string)

    go func() {
        time.Sleep(500 * time.Millisecond)
        hizli <- "hızlı veri geldi"
    }()

    go func() {
        time.Sleep(1 * time.Second)
        yavas <- "yavaş veri geldi"
    }()

    for i := 0; i < 2; i++ {
        select {
        case msg := <-hizli:
            fmt.Println(msg)
        case msg := <-yavas:
            fmt.Println(msg)
        }
    }
}
```

`select`, hazır olan kanal işlemini seçer. Bu yapı özellikle timeout, iptal sinyali ve fan-in/fan-out desenlerinde çok kullanışlıdır. Örneğin bir işi sonsuza kadar beklemek yerine `time.After` ile süre sınırı koyabilirsin.

| Kanal türü | Davranış | Ne zaman kullanılır? |
|---|---|---|
| Unbuffered | Gönderici ve alıcı eşleşene kadar bekler | Sıkı senkronizasyon gerektiğinde |
| Buffered | Kapasite dolana kadar gönderim beklemez | Üretici-tüketici hız farkı varsa |
| Receive-only | Sadece okuma yapılır | API güvenliği için |
| Send-only | Sadece yazma yapılır | Sorumluluğu sınırlamak için |

Kanallar güçlüdür ama sihirli değnek değildir. Alıcısı olmayan kanala veri göndermek, göndericisi olmayan kanaldan okumak veya hiç kapanmayan kanalı `range` ile tüketmek deadlock’a yol açabilir. Kanalı kapatmak için `close(ch)` kullanılır; fakat kural basittir: Genellikle kanalı gönderen taraf kapatır, alan taraf değil.

Sonuç olarak Go kanalları, eşzamanlı programlamayı daha okunabilir bir hikâyeye çevirir. Mutex ile “bu veriye kim dokunuyor?” diye düşünürken, kanallarla “bu veri kime gidiyor?” diye sorarsın. Bu bakış açısı özellikle karmaşık sistemlerde zihinsel yükü azaltır. Goroutine’ler mini karakterlerse, kanallar onların telsiz hattıdır; doğru frekansı ayarlarsan ekip uyum içinde çalışır.
