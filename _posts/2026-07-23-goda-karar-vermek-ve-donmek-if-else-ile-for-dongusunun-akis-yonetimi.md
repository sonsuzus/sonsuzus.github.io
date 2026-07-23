---
layout: post
title: "Go’da Karar Vermek ve Dönmek: if-else ile for Döngüsünün Akış Yönetimi"
math: true
categories: 
  - Bilgi
tags: 
  - go
  - kontrol-yapıları
  - for-döngüsü
---

Bir programı ilginç yapan şey yalnızca komutları sırayla çalıştırması değil, koşullara göre karar verebilmesi ve gerektiğinde aynı işi tekrar tekrar yapabilmesidir. Go dilinde bu akış yönetiminin iki ana kahramanı vardır: karar almak için `if-else`, tekrar etmek için ise neredeyse her role bürünen `for` döngüsü.
``

## Akış yönetimi neden önemlidir?

Bilgisayar programını küçük bir karar makinesi gibi düşünebiliriz. Elimizde bir durum, yani değişkenler vardır; program bu durumlara bakar ve hangi yoldan ilerleyeceğine karar verir. Matematiksel olarak bir koşul çoğu zaman şu mantıksal ifadeye benzer:

$sonuc = (yas \ge 18) \land (puan > 50)$

Burada ifade `true` ise bir blok, `false` ise başka bir blok çalışır. Go’da koşullar parantez içine alınmaz; bu, dilin sade ve okunabilir olma tercihidir.

```go
package main

import "fmt"

func main() {
    puan := 72

    if puan >= 85 {
        fmt.Println("Harika!")
    } else if puan >= 50 {
        fmt.Println("Geçtin, ama kahveye devam.")
    } else {
        fmt.Println("Tekrar deneme zamanı.")
    }
}
```

Bu örnekte program, `puan` değerine göre yalnızca bir yolu seçer. `if` ilk doğru koşulu yakaladığında devamındaki `else if` bloklarına bakmaz. Yani akış, gereksiz kontrol yapmadan ilerler.

| Yapı | Ne zaman kullanılır? | Go’daki not |
|---|---|---|
| `if` | Tek bir koşul kontrol edilecekse | Koşul parantezsiz yazılır |
| `else if` | Birden fazla alternatif varsa | Sıralama önemlidir |
| `else` | Hiçbir koşul sağlanmazsa | Varsayılan yol gibidir |

## if içinde kısa değişken tanımlama

Go’nun tatlı özelliklerinden biri, `if` satırında küçük bir hazırlık yapabilmektir. Bu özellikle hata kontrolünde çok görülür.

```go
package main

import "fmt"

func main() {
    if sayi := 42; sayi%2 == 0 {
        fmt.Println("Çift sayı:", sayi)
    } else {
        fmt.Println("Tek sayı:", sayi)
    }
}
```

Burada `sayi` yalnızca `if-else` bloğunun içinde yaşar. Bu sayede değişkenin kapsamı dar tutulur. Daha az kapsam, daha az kafa karışıklığı demektir.

## Go’da tek döngü: for

Go’da `while` veya `do-while` anahtar kelimeleri yoktur. İlk bakışta eksiklik gibi görünür, ama `for` o kadar esnektir ki hepsinin görevini üstlenir. Klasik kullanım üç parçadan oluşur:

$baslangic \rightarrow kosul \rightarrow guncelleme$

```go
package main

import "fmt"

func main() {
    toplam := 0

    for i := 1; i <= 5; i++ {
        toplam += i
    }

    fmt.Println("Toplam:", toplam)
}
```

Bu kodda `i` değeri 1’den 5’e kadar ilerler ve toplam hesaplanır. Döngünün çalışma maliyetini kabaca $O(n)$ olarak düşünebiliriz; çünkü tekrar sayısı, veri boyutu ile doğru orantılıdır.

| Döngü biçimi | Örnek | Benzer olduğu yapı |
|---|---|---|
| Klasik `for` | `for i := 0; i < n; i++` | C tarzı döngü |
| Koşullu `for` | `for x < 10` | `while` |
| Sonsuz `for` | `for {}` | Sonsuz döngü |
| `range` ile `for` | `for i, v := range liste` | Koleksiyon gezme |

## while gibi for kullanımı

Go’da sadece koşul yazarak `while` benzeri bir döngü oluşturabiliriz.

```go
package main

import "fmt"

func main() {
    enerji := 3

    for enerji > 0 {
        fmt.Println("Kod yazılıyor... enerji:", enerji)
        enerji--
    }

    fmt.Println("Mola zamanı!")
}
```

Bu tarz, koşulun ne zaman bozulacağını dışarıdan kontrol etmek istediğimiz durumlarda okunaklıdır.

## range ile koleksiyon gezmek

Diziler, dilimler, map’ler ve string’ler üzerinde dolaşmak için `range` kullanılır.

```go
package main

import "fmt"

func main() {
    diller := []string{"Go", "Python", "Rust"}

    for indeks, dil := range diller {
        fmt.Println(indeks, dil)
    }
}
```

`range`, her turda indeks ve değeri verir. Eğer indekse ihtiyacımız yoksa `_` ile görmezden gelebiliriz. Bu, Go’nun açık niyetli kod yazma felsefesine uygundur.

## break ve continue: döngünün trafik levhaları

`break` döngüyü tamamen bitirir, `continue` ise mevcut turu atlayıp sonraki tura geçer.

```go
for i := 1; i <= 10; i++ {
    if i == 7 {
        break
    }
    if i%2 == 0 {
        continue
    }
    fmt.Println(i)
}
```

Bu kod 7’ye gelince durur, çift sayıları ise yazdırmadan geçer. Yani çıktı yalnızca 1, 3 ve 5 olur.

Özetle Go’da akış yönetimi sade ama güçlüdür. `if-else` programın karar mekanizmasını kurar; `for` ise tekrar eden işleri tek bir esnek yapı altında toplar. Bu iki aracı iyi kavramak, Go’da okunabilir ve kontrollü programlar yazmanın temelidir.
