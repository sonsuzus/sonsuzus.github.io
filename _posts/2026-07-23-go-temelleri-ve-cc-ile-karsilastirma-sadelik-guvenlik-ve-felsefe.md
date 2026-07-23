---
layout: post
title: "Go Temelleri ve C/C++ ile Karşılaştırma: Sadelik, Güvenlik ve Felsefe"
math: true
categories: 
  - Bilgi
tags: 
  - Go
  - C++
  - Programlama Dilleri
  - Sözdizimi
---

Go, yani Gopher’ların neşeli dünyası, ilk bakışta C ailesinden gelmiş gibi görünür: süslü parantezler, tipler, fonksiyonlar... Fakat birkaç satır yazınca anlarız ki Go’nun derdi yalnızca kod çalıştırmak değil, geliştiriciyi karmaşadan korumaktır. C/C++ bize büyük güç ve büyük sorumluluk verirken, Go daha çok “ekipçe okunabilir, hızlı derlenebilir, güvenli varsayılanlara sahip yazılım” fikrini merkeze alır.
``

Go’nun sözdizimi C’ye benzer ama felsefesi farklıdır. C ve C++ tarihsel olarak donanıma yakınlık, performans ve düşük seviyeli kontrol üzerine kuruludur. Go ise modern sunucu yazılımları, ağ programlama, eşzamanlılık ve bakım kolaylığı için tasarlanmıştır. Bu farkı kabaca şöyle düşünebiliriz: C/C++ programcıya motorun tüm parçalarını verir; Go ise iyi ayarlanmış bir araç sunar ve gereksiz kolları panelden kaldırır.

Teorik olarak bir dilin karmaşıklığını $K$ ile, üretkenliği $U$ ile gösterirsek basit bir sezgisel ilişki kurabiliriz: $U \approx \frac{Okunabilirlik + Araçlama}{Karmaşıklık}$. Go, bu denklemde karmaşıklık paydasını küçültmeye çalışır. Örneğin header dosyaları yoktur, sınıf hiyerarşisi yoktur, kalıtım yerine arayüzler ve bileşim tercih edilir.

| Konu | C | C++ | Go |
|---|---|---|---|
| Derleme modeli | Header + kaynak dosya | Header, template, linker karmaşası | Paket tabanlı, hızlı derleme |
| Nesne yaklaşımı | Yok | Sınıf ve kalıtım | Struct + interface |
| Bellek yönetimi | Manuel | Manuel/RAII/akıllı pointer | Çöp toplayıcı |
| Eşzamanlılık | Kütüphane bağımlı | Thread, async, future | Goroutine ve channel |
| Felsefe | Donanıma yakınlık | Esneklik ve performans | Sadelik ve okunabilirlik |

Go’da değişken tanımlama oldukça yalındır. C/C++’ta tip genelde soldadır; Go’da ise isim önce gelir. Bu küçük fark, özellikle karmaşık tiplerde okunabilirliği artırır.

```go
package main

import "fmt"

func main() {
    name := "Ada"
    age := 32
    fmt.Println(name, age)
}
```

Burada `:=` kısa değişken tanımlama operatörüdür. Derleyici tipleri çıkarır; `name` string, `age` int olur. C++ tarafında `auto` benzer bir kolaylık sunar ama Go bu yaklaşımı dilin doğal parçası haline getirir. Yine de Go tamamen dinamik değildir; tipler derleme zamanında bellidir. Yani $tip\ güvenliği + kısa\ yazım$ hedeflenir.

Fonksiyonlarda dönüş değerleri de Go’nun karakteristik alanlarından biridir. Birden fazla değer döndürmek olağandır; hata yönetimi çoğunlukla `error` değeriyle yapılır.

```go
func divide(a, b float64) (float64, error) {
    if b == 0 {
        return 0, fmt.Errorf("sıfıra bölme")
    }
    return a / b, nil
}
```

C’de hata kodları, C++’ta exception mekanizması sık görülür. Go ise hatayı görünür kılar: fonksiyonu çağıran kişi hatayı açıkça kontrol eder. Bu bazen fazla satır yazdırır ama üretim sistemlerinde “hata nereden geldi?” dedektifliğini azaltır.

| Hata yaklaşımı | Avantaj | Dezavantaj |
|---|---|---|
| C hata kodu | Basit, düşük maliyetli | Kontrol unutulabilir |
| C++ exception | Akışı temiz tutabilir | Gizli kontrol akışı oluşturur |
| Go error değeri | Açık ve okunabilir | Daha fazla tekrar üretir |

Go’nun C++’tan en belirgin ayrımlarından biri kalıtımı reddetmesidir. C++’ta `class Dog : public Animal` gibi hiyerarşiler kurulabilir. Go’da ise “bir şeyin ne olduğundan çok, ne yapabildiği” önemlidir. Interface’ler örtük uygulanır; bir struct gerekli metotlara sahipse o interface’i sağlamış olur.

```go
type Speaker interface {
    Speak() string
}

type Robot struct{}

func (r Robot) Speak() string {
    return "bip bip"
}
```

`Robot`, açıkça `Speaker` olduğunu ilan etmez; `Speak()` metoduna sahip olduğu için Speaker gibi kullanılabilir. Bu yaklaşım ördek tiplemesine benzer ama statiktir: Eğer $Nesne \rightarrow Davranış$ eşleşmesi derleme zamanında tutarlıysa kod güvenle çalışır.

Bellek tarafında C/C++ daha keskin bıçaktır. `malloc/free`, `new/delete`, pointer aritmetiği ve yaşam süresi yönetimi güçlüdür; fakat dangling pointer, double free ve memory leak gibi canavarları da davet eder. Go pointer kullanır ama pointer aritmetiği sunmaz; ayrıca garbage collector ile çoğu yaşam süresi sorununu üstlenir. Bedeli, bazı durumlarda GC gecikmesi ve C kadar deterministik bellek kontrolü sağlayamamasıdır.

Eşzamanlılıkta Go’nun yıldızı parlar. C++ thread tabanlı düşünürken Go “goroutine” ile çok daha hafif görevler oluşturur. Channel yapısı, veriyi paylaşarak iletişim kurmak yerine iletişim kurarak veriyi paylaşma fikrini teşvik eder. Bu, CSP modeline dayanır ve kabaca $iş\ parçacığı \neq mantıksal\ görev$ ayrımını pratikleştirir.

Sonuç olarak Go, C/C++’ın mirasını tamamen reddetmez; sözdizimsel olarak onlardan esinlenir. Ancak felsefi olarak daha az özellik, daha net araçlar ve daha okunabilir ekip kodu ister. Eğer C/C++ bir laboratuvar dolusu gelişmiş cihazsa, Go düzenli bir atölyedir: Her şey elinizin altındadır, bazı çılgın deneyler yasaktır ama işinizi hızlı, temiz ve güvenli biçimde bitirme ihtimaliniz yüksektir.
