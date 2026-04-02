---
layout: post
title: Go Programlama
categories:
  - Program
tags:
  - go
  - golang
  - programlama dili
  - backend
redirect_from:
  - /posts/go-programlama/
---

Go, Google tarafından geliştirilen, açık kaynaklı bir programlama dilidir. Hız, basitlik ve güvenilirlik üzerine odaklanmıştır. Özellikle sistem programlama, ağ programlama ve büyük ölçekli yazılım projeleri için uygundur.

### Go'nun Özellikleri

Go'nun bazı temel özellikleri şunlardır:

* **Basitlik:** Go'nun sözdizimi temiz ve anlaşılırdır, bu da öğrenmeyi ve kod yazmayı kolaylaştırır.
* **Hız:** Go, derlenen bir dildir ve yüksek performans sunar.
* **Eşzamanlılık:** Go, goroutine'ler ve kanallar aracılığıyla eşzamanlı programlamayı kolaylaştırır.
* **Güvenlik:** Go, bellek güvenliği konusunda titizdir ve çöp toplama özelliği sayesinde bellek sızıntılarını önler.
* **Statik Tiplendirme:** Go, statik tiplendirme ile derleme zamanında hataları yakalar.
* **Platform Bağımsızlığı:** Go, farklı işletim sistemlerinde (Windows, macOS, Linux) çalışabilir.

### Go'nun Kullanım Alanları

Go, çeşitli alanlarda yaygın olarak kullanılır:

* **Web Geliştirme:** Go, web uygulamaları ve API'ler geliştirmek için popüler bir seçimdir.
* **Sistem Programlama:** Go, işletim sistemi düzeyinde programlar ve araçlar geliştirmek için kullanılabilir.
* **Ağ Programlama:** Go, ağ sunucuları ve istemcileri geliştirmek için uygundur.
* **Bulut Bilişim:** Go, bulut tabanlı uygulamalar ve mikro hizmetler geliştirmek için tercih edilir.
* **Veri Bilimi:** Go, veri işleme ve analiz uygulamaları için kullanılabilir.

### Go ile İlk Program

Aşağıda, Go ile yazılmış basit bir "Merhaba, Dünya!" programı bulunmaktadır:

```go
package main

import "fmt"

func main() {
    fmt.Println("Merhaba, Dünya!")
}
```

Bu programı çalıştırmak için, aşağıdaki adımları izleyin:

1.  `main.go` adında bir dosya oluşturun ve yukarıdaki kodu içine yapıştırın.
2.  Terminali açın ve dosyanın bulunduğu dizine gidin.
3.  `go run main.go` komutunu çalıştırın.

Bu komut, programı derleyecek ve çalıştıracaktır. Sonuç olarak, terminalde "Merhaba, Dünya!" çıktısını göreceksiniz.

### Go'da Temel Kavramlar

* **Paketler:** Go programları paketler halinde düzenlenir. `main` paketi, programın giriş noktasını içerir.
* **İçe Aktarma:** `import` anahtar kelimesi, diğer paketlerin işlevlerini kullanmak için kullanılır.
* **Fonksiyonlar:** Fonksiyonlar, belirli bir görevi yerine getiren kod bloklarıdır. `main` fonksiyonu, programın başladığı yerdir.
* **Değişkenler:** Değişkenler, veri saklamak için kullanılır. Go'da değişkenler `var` anahtar kelimesiyle tanımlanır.
* **Veri Tipleri:** Go, çeşitli veri tiplerini destekler, örneğin:
    * `int`: Tam sayılar
    * `float64`: Kayan noktalı sayılar
    * `string`: Metin
    * `bool`: boolean (true/false)
* **Kontrol Yapıları:** Go, programın akışını kontrol etmek için çeşitli yapılar sunar, örneğin:
    * `if`, `else if`, `else`: Koşullu ifadeler
    * `for`: Döngüler
    * `switch`: Çoklu dallanma

### Go'da Eşzamanlılık

Go, eşzamanlılığı desteklemek için goroutine'ler ve kanallar sağlar. Goroutine, hafif bir iş parçacığıdır ve Go'da eşzamanlı olarak çalışan fonksiyonlardır. Kanallar, goroutine'ler arasında veri alışverişi yapmak için kullanılır.

```go
package main

import (
    "fmt"
    "time"
)

func selam(mesaj string) {
    fmt.Println(mesaj)
}

func main() {
    go selam("Merhaba!")
    go selam("Dünya!")
    time.Sleep(1 * time.Second)
}
```

Bu örnekte, `selam` fonksiyonu iki kez goroutine olarak çağrılır. `time.Sleep` fonksiyonu, goroutine'lerin tamamlanmasını beklemek için kullanılır.

### Go Modülleri

Go modülleri, bağımlılık yönetimini kolaylaştırmak için kullanılır. Bir modül, bir veya daha fazla Go paketinden oluşan bir koleksiyondur. Modüller, projenizin bağımlılıklarını belirtmenizi ve yönetmenizi sağlar.

Yeni bir modül oluşturmak için, aşağıdaki komutu kullanabilirsiniz:

```bash
go mod init <modül_adı>
```

Örneğin:

```bash
go mod init [github.com/kullaniciadi/projeadi](https://github.com/kullaniciadi/projeadi)
```

Bu komut, projenizin kök dizininde `go.mod` adında bir dosya oluşturur.

### Go ile Web Geliştirme

Go, web uygulamaları geliştirmek için güçlü bir dildir. `net/http` paketi, HTTP sunucuları ve istemcileri oluşturmak için kullanılabilir. Ayrıca, birçok popüler web çerçevesi (örneğin, Gin, Echo, Fiber) Go ile web geliştirmeyi daha da kolaylaştırır.

```go
package main

import (
    "fmt"
    "net/http"
)

func handleAnaSayfa(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintln(w, "Merhaba, Dünya!")
}

func main() {
    http.HandleFunc("/", handleAnaSayfa)
    http.ListenAndServe(":8080", nil)
}
```

Bu örnekte, bir HTTP sunucusu oluşturulur ve "/" yoluna gelen istekler `handleAnaSayfa` fonksiyonu tarafından işlenir. Sunucu, 8080 portunda dinlenir.

### Go Kaynakları

* [Resmi Go Web Sitesi](https://go.dev/): Go hakkında kapsamlı bilgi, dökümantasyon ve öğreticiler içerir.
* [Go Tour](https://go.dev/tour/welcome/1): Go'yu etkileşimli olarak öğrenmek için harika bir kaynaktır.
* [Go by Example](https://gobyexample.com/): Go'yu örneklerle öğrenmek için kullanışlıdır.
* [Effective Go](https://go.dev/doc/effective_go): Go kodu yazarken dikkat edilmesi gereken stil ve en iyi uygulamaları açıklar.

Bu Markdown belgesi, Go programlama diline genel bir bakış sunar. Go'nun temel özelliklerini, kullanım alanlarını ve bazı temel kavramlarını ele alır. Go ile ilk programınızı nasıl yazacağınızı ve eşzamanlılığı nasıl kullanacağınızı gösterir. Ayrıca, Go modüllerini ve web geliştirmeyi de tanıtır. Son olarak, Go öğrenmek için bazı yararlı kaynaklar sunar.
