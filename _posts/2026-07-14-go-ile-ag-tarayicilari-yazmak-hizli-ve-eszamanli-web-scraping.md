---
layout: post
title: "Go ile Ağ Tarayıcıları Yazmak: Hızlı ve Eşzamanlı Web Scraping"
math: true
categories: 
  - Program
tags: 
  - go
  - web-scraping
  - concurrency
  - http
  - goroutine
---

İnternetteki veriler dağınık bir kütüphane gibidir: ürün fiyatları bir rafta, haber başlıkları başka rafta, açık veri tabloları ise bodrumda durur. Go ile yazılan bir web scraper, bu kütüphanede patenle gezen disiplinli bir arşivciye benzer. Hızlı HTTP istemcisi, goroutine yapısı ve channel mantığı sayesinde binlerce sayfayı kısa sürede ziyaret edip veriyi indeksleyebiliriz.
``
Web scraping temelde üç aşamadan oluşur: sayfayı indir, içeriği ayrıştır, anlamlı veriyi kaydet. Basit görünür ama işin teorik tarafında ağ gecikmesi, eşzamanlılık, hata toleransı ve etik sınırlar vardır. Bir isteğin toplam süresi yaklaşık olarak şöyle düşünülebilir: $T = T_{dns} + T_{tcp} + T_{tls} + T_{server} + T_{download}$. Tek tek çalışan bir tarayıcıda toplam süre $T_{seq} = n \times T$ olur. Eşzamanlı çalışan bir sistemde ise ideal durumda $T_{par} \approx \frac{n \times T}{w}$; burada $w$ worker sayısıdır. Elbette gerçek dünyada bant genişliği, hedef sunucu limitleri ve CPU bu denkleme biraz mizah katar.

Go bu iş için çok uygundur çünkü goroutine'ler hafiftir. Her URL için dev bir işletim sistemi thread'i açmak yerine, Go runtime binlerce işi verimli biçimde planlar. Channel'lar ise URL kuyruğu, sonuç akışı ve hata bildirimleri için temiz bir iletişim modeli sağlar.

| Yaklaşım | Avantaj | Dezavantaj | Uygun Senaryo |
|---|---|---|---|
| Sıralı istek | Basit, hata ayıklaması kolay | Çok yavaş | 10-20 sayfalık küçük işler |
| Sınırsız goroutine | İlk bakışta çok hızlı | Sunucuyu boğabilir, rate limit yer | Kontrollü olmayan deneyler, önerilmez |
| Worker pool | Dengeli, yönetilebilir | Biraz daha fazla kod | Gerçek projeler |
| Kuyruk + retry | Dayanıklı | Mimari karmaşıklık artar | Büyük ölçekli indeksleme |

Aşağıdaki örnekte kontrollü bir worker pool kuruyoruz. Amaç, URL listesini channel üzerinden worker'lara dağıtmak ve her sayfanın HTML uzunluğunu örnek olarak toplamaktır. Gerçek projede burada başlık, meta açıklama, ürün fiyatı veya linkler ayrıştırılabilir.

```go
package main

import (
    "fmt"
    "io"
    "net/http"
    "sync"
    "time"
)

type Result struct {
    URL    string
    Length int
    Err    error
}

func fetch(client *http.Client, url string) Result {
    resp, err := client.Get(url)
    if err != nil {
        return Result{URL: url, Err: err}
    }
    defer resp.Body.Close()

    body, err := io.ReadAll(resp.Body)
    if err != nil {
        return Result{URL: url, Err: err}
    }

    return Result{URL: url, Length: len(body)}
}

func worker(id int, client *http.Client, jobs <-chan string, results chan<- Result, wg *sync.WaitGroup) {
    defer wg.Done()
    for url := range jobs {
        fmt.Println("Worker", id, "işliyor:", url)
        results <- fetch(client, url)
    }
}

func main() {
    urls := []string{
        "https://example.com",
        "https://go.dev",
        "https://pkg.go.dev",
    }

    client := &http.Client{Timeout: 8 * time.Second}
    jobs := make(chan string)
    results := make(chan Result)

    var wg sync.WaitGroup
    workerCount := 3

    for i := 1; i <= workerCount; i++ {
        wg.Add(1)
        go worker(i, client, jobs, results, &wg)
    }

    go func() {
        for _, url := range urls {
            jobs <- url
        }
        close(jobs)
        wg.Wait()
        close(results)
    }()

    for r := range results {
        if r.Err != nil {
            fmt.Println("Hata:", r.URL, r.Err)
            continue
        }
        fmt.Println(r.URL, "boyut:", r.Length)
    }
}
```

Kodda `http.Client` için timeout vermek küçük ama hayati bir ayrıntıdır. Timeout yoksa bir istek sonsuza kadar asılı kalabilir ve scraper'ınız kahve molasından dönmeyen stajyer gibi ortadan kaybolur. `workerCount` değeri ise hız ile nezaket arasındaki dengedir. Çok düşük olursa yavaş kalırsınız, çok yüksek olursa hedef site sizi engelleyebilir.

HTML ayrıştırmak için standart kütüphane yeterli olmayabilir. Go ekosisteminde `goquery`, jQuery benzeri seçicilerle pratik bir çözüm sunar. Örneğin `h1`, `.price`, `a[href]` gibi seçicilerle veri çekilebilir. Fakat dinamik olarak JavaScript ile oluşan sayfalarda klasik HTTP isteği yetmez; bu durumda tarayıcı otomasyonu veya API keşfi gerekir.

| Konu | Dikkat Edilecek Nokta | İyi Uygulama |
|---|---|---|
| Robots.txt | Site taramaya izin vermeyebilir | Önce kontrol et |
| Rate limit | Çok sık istek engellenir | Gecikme ve worker limiti kullan |
| User-Agent | Varsayılan istemci şüpheli görünebilir | Açıklayıcı User-Agent gönder |
| Retry | Geçici ağ hataları olabilir | Üstel geri çekilme uygula |
| Veri temizliği | HTML gürültülüdür | Normalize et ve doğrula |

Sonuç olarak Go ile scraper yazmak sadece hızlı istek göndermek değildir; küçük bir dağıtık sistem tasarlamaktır. Kuyruklar, worker'lar, timeout'lar ve hata yönetimi bir araya geldiğinde saniyeler içinde binlerce sayfayı gezebilen sağlam bir indeksleyici ortaya çıkar. Hız güzel, ama kontrollü hız daha güzeldir.
