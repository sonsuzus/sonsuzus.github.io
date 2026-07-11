---
layout: post
title: "Go'nun Eşzamanlılık Mimarisi: Goroutine ile Hafif ve Hızlı Servisler"
math: true
categories: 
  - Program
tags: 
  - golang
  - concurrency
  - goroutine
  - backend
---

Go’da eşzamanlılık, “aynı anda çok iş yapıyormuş gibi” görünen kod yazmaktan daha fazlasıdır; dilin tasarım felsefesine gömülü bir üretkenlik süper gücüdür. Binlerce arka plan görevini, ağ isteğini, kuyruk işini veya zamanlayıcıyı klasik thread maliyetlerine boğulmadan yönetmek istiyorsanız, goroutine’ler tam olarak bu sahneye davul zurna ile girer.
``

Go’nun concurrency yaklaşımını anlamanın ilk adımı şu ayrımı netleştirmektir: **Concurrency** aynı zaman aralığında birden fazla işle ilerleyebilme yeteneğidir; **parallelism** ise gerçekten aynı anda, farklı CPU çekirdeklerinde çalışmaktır. Yani concurrency bir tasarım modeli, parallelism ise donanımın sunduğu fiziksel imkândır.

Basitçe ifade edersek:

| Kavram | Anlamı | Go’daki karşılığı |
|---|---|---|
| Concurrency | İşleri bağımsız parçalara bölmek | Goroutine, channel, select |
| Parallelism | İşleri aynı anda CPU’da yürütmek | Çok çekirdek + scheduler |
| Thread | İşletim sistemi düzeyinde ağır yürütme birimi | OS thread |
| Goroutine | Go runtime tarafından yönetilen hafif görev | `go func()` |

Go runtime içinde ünlü **M:P:G modeli** çalışır. Burada `G` goroutine’i, `M` işletim sistemi thread’ini, `P` ise işlemci bağlamını temsil eder. Kabaca ilişkiyi şöyle düşünebiliriz: $G \rightarrow P \rightarrow M$. Eğer $N$ adet goroutine’iniz ve $P$ adet işlemci bağlamınız varsa, Go scheduler bu goroutine’leri uygun thread’lere dağıtarak verimli çalıştırır. Bu yüzden binlerce goroutine açmak çoğu senaryoda binlerce OS thread açmaktan çok daha ucuzdur.

Goroutine başlatmak şaşırtıcı derecede kolaydır:

```go
package main

import (
    "fmt"
    "time"
)

func sendEmail(user string) {
    time.Sleep(500 * time.Millisecond)
    fmt.Println("E-posta gönderildi:", user)
}

func main() {
    users := []string{"ada", "linus", "grace"}

    for _, user := range users {
        go sendEmail(user)
    }

    time.Sleep(1 * time.Second)
}
```

Bu örnekte her kullanıcı için ayrı bir goroutine başlatılır. `sendEmail` fonksiyonu bloklansa bile ana akış diğer işleri başlatmaya devam eder. Ancak gerçek projelerde `time.Sleep` ile beklemek pek yakışıklı değildir; bu, restoranda garsona “yemekler herhalde gelir” deyip göz kararı beklemek gibidir.

Daha kontrollü bir yapı için `channel` kullanırız. Channel’lar goroutine’ler arasında güvenli veri aktarımı sağlar. Go’nun meşhur sözü burada devreye girer: **Belleği paylaşarak iletişim kurma; iletişim kurarak belleği paylaş.**

```go
package main

import (
    "context"
    "fmt"
    "time"
)

func worker(ctx context.Context, jobs <-chan string, results chan<- string) {
    for {
        select {
        case <-ctx.Done():
            return
        case job, ok := <-jobs:
            if !ok {
                return
            }
            time.Sleep(300 * time.Millisecond)
            results <- fmt.Sprintf("İş tamamlandı: %s", job)
        }
    }
}

func main() {
    ctx, cancel := context.WithTimeout(context.Background(), 2*time.Second)
    defer cancel()

    jobs := make(chan string)
    results := make(chan string)

    for i := 0; i < 3; i++ {
        go worker(ctx, jobs, results)
    }

    go func() {
        defer close(jobs)
        for i := 1; i <= 5; i++ {
            jobs <- fmt.Sprintf("görev-%d", i)
        }
    }()

    for i := 1; i <= 5; i++ {
        fmt.Println(<-results)
    }
}
```

Burada üç worker goroutine’i aynı `jobs` kanalından görev alır ve sonuçları `results` kanalına gönderir. `context` ise servis kapanışı, timeout veya iptal sinyalleri için temiz bir kontrol mekanizması sunar. Bu yapı, e-posta gönderimi, görsel işleme, log toplama veya webhook tüketimi gibi arka plan servislerinde sıkça kullanılır.

Performans açısından bakarsak, goroutine’lerin başlangıç stack’i küçüktür ve ihtiyaç oldukça büyür. Klasik thread’lerde stack maliyeti megabaytlarla ifade edilebilirken, goroutine’lerde başlangıç maliyeti kilobayt seviyesindedir. Teorik olarak toplam bellek tüketimini şöyle düşünebiliriz: $ToplamBellek \approx n \times s$. Burada $n$ görev sayısı, $s$ ise görev başına stack maliyetidir. $s$ küçüldükçe aynı makinede daha fazla eşzamanlı iş yönetebilirsiniz.

| Yaklaşım | Avantaj | Dezavantaj |
|---|---|---|
| Tek thread | Basit akış | Bloklanınca her şey yavaşlar |
| OS thread havuzu | Paralel çalışma | Daha yüksek bellek maliyeti |
| Goroutine | Hafif, hızlı, okunabilir | Yanlış channel kullanımı deadlock doğurabilir |

Tabii goroutine açmak bedava değildir; sadece ucuzdur. Sonsuz sayıda goroutine başlatmak, mutfağa sınırsız sipariş yollayıp aşçıdan mucize beklemek gibidir. Bu nedenle worker pool, rate limit, context cancellation ve buffer’lı channel gibi tekniklerle sisteminize sınır koymalısınız.

Sonuç olarak Go’nun concurrency mimarisi, basit sözdizimiyle güçlü bir runtime mühendisliğini birleştirir. Goroutine’ler sayesinde arka plan servisleri hem okunabilir hem de yüksek verimli olabilir. Eğer kuyruk tüketen, API çağrılarını paralelleştiren veya binlerce bağlantıyı yöneten bir servis yazıyorsanız, Go size “thread açalım mı?” diye sormaz; zarifçe `go` anahtar kelimesini uzatır ve “hadi işi bölelim” der.
