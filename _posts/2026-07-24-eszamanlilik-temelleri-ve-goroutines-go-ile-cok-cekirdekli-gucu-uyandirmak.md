---
layout: post
title: "Eşzamanlılık Temelleri ve Goroutines: Go ile Çok Çekirdekli Gücü Uyandırmak"
math: true
categories: 
  - Bilgi
tags: 
  - go
  - goroutines
  - eşzamanlılık
---

Bilgisayarlarımız artık tek bir hızlı çekirdekten ibaret değil; çoğu makinede birden fazla çekirdek sessizce iş bekliyor. Go dilinin goroutine yaklaşımı tam da burada devreye girer: işletim sistemi iş parçacıklarına göre çok daha hafif görevler başlatarak aynı anda birçok işi düzenli, okunabilir ve verimli biçimde yürütmemizi sağlar.
``
Eşzamanlılık, birden fazla işin aynı zaman aralığında ilerlemesi fikridir. Paralellik ise bu işlerin gerçekten aynı anda, farklı çekirdeklerde çalışmasıdır. Yani eşzamanlılık bir tasarım modeli, paralellik ise donanım desteğiyle gerçekleşen çalışma biçimidir. Go bu ayrımı çok güzel saklar: siz `go` anahtar kelimesiyle goroutine başlatırsınız, Go çalışma zamanı bunları uygun işletim sistemi thread’lerine dağıtır.

Basit bir matematiksel bakış atalım. Bir programın toplam süresi $T$ olsun. Eğer işin paralelleştirilebilir kısmı $p$, işlemci çekirdeği sayısı da $n$ ise Amdahl yasasına göre teorik hızlanma yaklaşık $Hiz = 1 / ((1-p)+p/n)$ olur. Yani her şeyi paralel yapamayız; ama doğru parçaları eşzamanlı tasarlarsak ciddi kazanç elde ederiz.

| Kavram | Ne Anlama Gelir? | Go’daki Karşılığı |
|---|---|---|
| Thread | İşletim sistemi tarafından yönetilen ağır yürütme birimi | OS thread |
| Goroutine | Go runtime tarafından yönetilen hafif görev | `go fonksiyon()` |
| Eşzamanlılık | İşlerin birlikte ilerlemesi | Goroutine + channel |
| Paralellik | İşlerin fiziksel olarak aynı anda çalışması | Çok çekirdek + scheduler |

Bir goroutine başlatmak şaşırtıcı derecede kolaydır. Aşağıdaki örnekte `selamVer` fonksiyonu ana akıştan bağımsız çalışır. `time.Sleep` burada sadece örneğin bitmeden goroutine’in çıktısını görebilmemiz için kullanılır; gerçek projelerde genellikle `sync.WaitGroup` tercih edilir.

```go
package main

import (
    "fmt"
    "time"
)

func selamVer(kim string) {
    for i := 1; i <= 3; i++ {
        fmt.Println("Merhaba", kim, i)
        time.Sleep(300 * time.Millisecond)
    }
}

func main() {
    go selamVer("Goroutine")

    fmt.Println("Ana program çalışıyor")
    time.Sleep(1 * time.Second)
}
```

Bu kodda `go selamVer(...)` satırı fonksiyonu yeni bir goroutine olarak çalıştırır. Ana program beklemek zorunda değildir; kendi yoluna devam eder. İşte goroutine’lerin hafifliği burada parlar: binlerce goroutine başlatmak, binlerce işletim sistemi thread’i açmaktan çok daha ekonomiktir.

Ancak süper güçlerin yan etkileri vardır. Birden fazla goroutine aynı veriye yazmaya çalışırsa yarış durumu, yani race condition oluşabilir. Mesela iki kişi aynı deftere aynı anda not almaya çalışırsa sonuç karışabilir. Go’da bu tür durumlar için `channel`, `mutex` ve `WaitGroup` gibi araçlar kullanılır.

```go
package main

import (
    "fmt"
    "sync"
)

func isYap(id int, wg *sync.WaitGroup) {
    defer wg.Done()
    fmt.Println("İş başladı:", id)
}

func main() {
    var wg sync.WaitGroup

    for i := 1; i <= 5; i++ {
        wg.Add(1)
        go isYap(i, &wg)
    }

    wg.Wait()
    fmt.Println("Tüm işler tamamlandı")
}
```

Burada `WaitGroup`, ana programın tüm goroutine’ler bitene kadar beklemesini sağlar. `wg.Add(1)` yeni bir iş eklendiğini, `defer wg.Done()` işin tamamlandığını, `wg.Wait()` ise herkes dönene kadar beklenmesi gerektiğini söyler.

| Durum | Kötü Yaklaşım | Daha Sağlıklı Yaklaşım |
|---|---|---|
| Ana program erken bitiyor | Rastgele `Sleep` kullanmak | `sync.WaitGroup` kullanmak |
| Ortak veri değişiyor | Kontrolsüz yazmak | `Mutex` veya channel kullanmak |
| Çok fazla iş var | Tek tek senkron çalıştırmak | Worker pool kurmak |
| Sonuçlar toplanacak | Global değişkene yazmak | Channel ile sonuç taşımak |

Go’nun scheduler’ı goroutine’leri işletim sistemi thread’leri üzerinde gezdirir. `GOMAXPROCS` değeri aynı anda kaç OS thread’in Go kodu çalıştırabileceğini belirler. Modern Go sürümlerinde bu değer genellikle makinedeki CPU çekirdeği sayısına göre otomatik ayarlanır. Yani çoğu zaman ayar yapmadan çok çekirdekli gücü kullanmaya başlarsınız.

Sonuç olarak goroutine, Go’nun en keyifli ve güçlü özelliklerinden biridir. Ama amaç her yere `go` yazmak değildir. Doğru soru şudur: Bu işler bağımsız mı, bekleme içeriyor mu, sonuçlar güvenli şekilde birleşiyor mu? Cevap evetse goroutine’ler uygulamanıza roket takabilir. Cevap hayırsa, roket yerine mutfakta havai fişek yakmış olabilirsiniz.
