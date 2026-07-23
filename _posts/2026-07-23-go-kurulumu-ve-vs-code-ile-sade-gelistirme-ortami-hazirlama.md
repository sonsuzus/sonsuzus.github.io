---
layout: post
title: "Go Kurulumu ve VS Code ile Sade Geliştirme Ortamı Hazırlama"
math: true
categories: 
  - Program
tags: 
  - go
  - golang
  - vscode
  - kurulum
  - geliştirme ortamı
---

Go öğrenmeye başlamak, yeni bir müzik aleti almak gibidir: önce akort edersin, sonra şarkı çalmaya başlarsın. Bu yazıda Go derleyicisini kurup VS Code üzerinde sade, hızlı ve teoriyi pratiğe çevirmeye uygun bir geliştirme ortamı hazırlayacağız. Amacımız “her şeyi kurdum ama neden çalışmıyor?” paniğini azaltmak ve ilk Go programını güvenle koşturmak.
``
Go, Google tarafından geliştirilen derlenebilir, statik tipli ve sade söz dizimine sahip bir programlama dilidir. Derlenebilir olması şu anlama gelir: yazdığınız `.go` dosyaları doğrudan makineye daha yakın çalıştırılabilir programa dönüştürülür. Kabaca süreç şöyle düşünülebilir: kaynak kod $K$, derleyici $D$ tarafından işlenir ve çalıştırılabilir çıktı $C$ üretilir: $D(K) = C$. Bu model, Go’nun hızlı çalışmasına ve dağıtımının kolay olmasına katkı sağlar.

Kuruluma başlamadan önce birkaç temel kavramı netleştirelim:

| Kavram | Ne işe yarar? | Kısaca benzetme |
|---|---|---|
| Go derleyicisi | Kodunuzu çalıştırılabilir hale getirir | Tercüman |
| GOROOT | Go’nun kurulu olduğu ana dizindir | Fabrikanın kendisi |
| GOPATH | Eski çalışma alanı yaklaşımıdır | Eski usul depo |
| Go Modules | Modern bağımlılık yönetimidir | Proje bazlı paket çantası |
| gopls | VS Code’a Go zekâsı kazandırır | Kod editörünün gözlüğü |

İlk adım Go’yu kurmak. Resmî site olan `https://go.dev/dl/` adresine gidin ve işletim sisteminize uygun paketi indirin. Windows kullanıyorsanız `.msi` kurulum dosyası genellikle yeterlidir. macOS tarafında `.pkg` dosyası veya Homebrew ile `brew install go` kullanılabilir. Linux’ta paket yöneticinizden kurabilir ya da resmî arşivi `/usr/local` altına açabilirsiniz.

Kurulumdan sonra terminali açıp şu komutu çalıştırın:

```bash
go version
```

Bu komut size kurulu Go sürümünü göstermelidir. Örneğin `go version go1.22 linux/amd64` gibi bir çıktı görüyorsanız tebrikler, derleyici sahneye çıktı! Eğer komut bulunamıyorsa sorun büyük ihtimalle PATH ayarındadır. PATH, işletim sisteminin komutları nerede arayacağını belirleyen listedir. Matematiksel düşünürsek çalıştırılabilir dosya arama işlemi bir küme üzerinde yapılır: $PATH = \{d_1, d_2, d_3, ...\}$. Go’nun `bin` klasörü bu kümeye eklenmelidir.

Şimdi VS Code tarafına geçelim. VS Code’u açın, Extensions bölümüne girin ve Microsoft tarafından sağlanan `Go` eklentisini kurun. Bu eklenti tek başına güzeldir ama asıl sihir `gopls` ile gelir. Bir `.go` dosyası açtığınızda VS Code genellikle eksik araçları kurmak isteyecektir. Onay verin; otomatik tamamlama, hata işaretleme, biçimlendirme ve tanıma özellikleri aktif olacaktır.

Aşağıdaki tablo, sade bir Go geliştirme ortamında hangi parçanın ne kattığını özetler:

| Araç | Zorunlu mu? | Sağladığı fayda |
|---|---:|---|
| Go SDK | Evet | Derleme, çalıştırma, test |
| VS Code | Hayır ama önerilir | Hafif editör deneyimi |
| Go eklentisi | Evet, VS Code için | Dil desteği |
| gopls | Çok önerilir | Akıllı tamamlama, analiz |
| Git | Önerilir | Sürüm kontrolü ve modül kullanımı |

Artık küçük bir proje oluşturalım. Terminalde şu adımları uygulayın:

```bash
mkdir merhaba-go
cd merhaba-go
go mod init example.com/merhaba-go
```

Buradaki `go mod init`, projeniz için bir `go.mod` dosyası üretir. Bu dosya, projenin kimliği ve bağımlılıkları için merkezdir. Modern Go geliştirmede proje formülü kabaca şöyledir: proje = kaynak kod + `go.mod` + bağımlılıklar.

Şimdi `main.go` dosyasını oluşturun:

```go
package main

import "fmt"

func main() {
    mesaj := "Merhaba Go, ben geldim!"
    fmt.Println(mesaj)
}
```

Bu kodda `package main`, çalıştırılabilir bir program yazdığımızı söyler. `import "fmt"`, ekrana yazı basmak için standart kütüphaneden `fmt` paketini getirir. `main` fonksiyonu ise programın başlangıç noktasıdır. `mesaj :=` ifadesi Go’nun kısa değişken tanımlama biçimidir; derleyici türü kendisi çıkarır.

Programı çalıştırmak için:

```bash
go run .
```

Derlemek isterseniz:

```bash
go build
```

`go run` hızlı denemeler için idealdir; `go build` ise çalıştırılabilir çıktı üretir. Yani `go run` mutfakta tadım yapmak, `go build` ise yemeği tabağa koymaktır.

Son olarak VS Code ayarlarında `Format On Save` seçeneğini açmanızı öneririm. Go kültüründe biçimlendirme tartışması minimumdur; `gofmt` ne derse o olur. Bu da ekip içinde “süslü parantez sağda mı solda mı?” savaşlarını bitirir.

Özetle: Go SDK’yı kurduk, PATH kontrolünü yaptık, VS Code’a Go eklentisini ve `gopls` desteğini ekledik, modül tabanlı bir proje başlattık ve ilk programı çalıştırdık. Artık teoriyi pratiğe dökecek temiz bir masanız var. Bundan sonrası değişkenler, fonksiyonlar, paketler ve bol bol “aa bu dil baya sadeymiş” anı!
