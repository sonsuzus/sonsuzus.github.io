---
layout: post
title: "Go ile JSON İşlemleri ve Veri Serileştirme"
math: true
categories: 
  - Program
tags: 
  - Go
  - JSON
  - Serileştirme
---

Modern yazılımlar artık tek başına yaşayan küçük adacıklar değil; API’ler, mikroservisler, mobil uygulamalar ve üçüncü parti sistemlerle sürekli konuşan sosyal kelebekler. Go tarafında bu sohbetin en popüler dili JSON’dır. Bir Go yapısını JSON’a çevirmek, valize kıyafet yerleştirmeye benzer: veriyi dış dünyaya taşınabilir, okunabilir ve standart bir forma sokarız. Gelen JSON’u tekrar Go struct’ına çözmek ise valizi açıp eşyaları doğru çekmecelere yerleştirmektir.
``

## JSON ve serileştirmenin teorisi

Serileştirme, bellekte duran bir veri yapısını aktarılabilir bir biçime dönüştürme işlemidir. Go’da buna çoğunlukla **marshal**, tersine ise **unmarshal** denir. Matematiksel düşünürsek, serileştirmeyi bir dönüşüm fonksiyonu gibi görebiliriz: $f: GoStruct \rightarrow JSON$. Ters işlem ise $f^{-1}: JSON \rightarrow GoStruct$ şeklindedir. Elbette pratikte $f^{-1}$ her zaman mükemmel değildir; eksik alanlar, tip uyuşmazlıkları veya beklenmeyen değerler yüzünden hata alabiliriz.

JSON’un avantajı basit olmasıdır: string, number, boolean, array, object ve null. Go ise daha zengin tiplere sahiptir. Bu yüzden iki dünya arasında çeviri yaparken tip eşleşmelerini iyi bilmek gerekir.

| JSON Tipi | Go Karşılığı | Not |
|---|---|---|
| string | string | Tarihler genellikle string taşınır |
| number | int, float64 | Varsayılan interface{} çözümünde float64 olur |
| boolean | bool | Doğrudan eşleşir |
| array | slice | Örn: []string |
| object | struct veya map | API modellerinde struct tercih edilir |
| null | pointer, sql.Null* | Yokluğu temsil etmek için kullanılır |

## Struct tag: JSON pasaport kontrolü

Go’da alan adları dışa açılmak için büyük harfle başlamalıdır. Ancak JSON alan isimleri genellikle küçük harfli veya snake_case olur. İşte struct tag burada devreye girer.

```go
package main

import (
    "encoding/json"
    "fmt"
)

type User struct {
    ID       int    `json:"id"`
    FullName string `json:"full_name"`
    Email    string `json:"email,omitempty"`
}

func main() {
    user := User{ID: 7, FullName: "Ada Lovelace"}

    data, err := json.MarshalIndent(user, "", "  ")
    if err != nil {
        panic(err)
    }

    fmt.Println(string(data))
}
```

Bu örnekte `MarshalIndent`, JSON’u okunabilir biçimde üretir. `omitempty` ise alan boşsa JSON’a yazma anlamına gelir. Yani e-posta yoksa gereksiz bir `email` alanı gönderilmez. API tüketen sistemlerin “Bu niye boş geldi?” diye trip atmasını engeller.

## Gelen JSON’u Go yapısına çözmek

Dış sistemden veri geldiğinde `json.Unmarshal` kullanırız. Burada önemli detay, hedef değişkenin adresini vermektir; çünkü Go’nun o değişkenin içini doldurması gerekir.

```go
package main

import (
    "encoding/json"
    "fmt"
)

type Product struct {
    Code  string  `json:"code"`
    Price float64 `json:"price"`
    Stock int     `json:"stock"`
}

func main() {
    raw := []byte(`{"code":"KB-42","price":129.90,"stock":15}`)

    var product Product
    err := json.Unmarshal(raw, &product)
    if err != nil {
        fmt.Println("JSON hatası:", err)
        return
    }

    fmt.Printf("%s ürünü %.2f TL\n", product.Code, product.Price)
}
```

Buradaki fiyat alanı için `float64` kullandık. Para işlemlerinde kayan nokta hassasiyetine dikkat etmek gerekir. Örneğin $0.1 + 0.2 \neq 0.3$ gibi görünen sonuçlar bilgisayar temsilinden kaynaklanabilir. Finansal uygulamalarda kuruşu `int` olarak saklamak daha güvenlidir.

## Struct mı map mi?

Her JSON için struct yazmak zorunda değilsiniz. Dinamik veya şeması belirsiz verilerde `map[string]interface{}` kullanılabilir. Ancak bu esneklik, tip güvenliğinden ödün verir.

| Yaklaşım | Avantaj | Dezavantaj |
|---|---|---|
| struct | Tip güvenli, okunabilir, IDE dostu | Şema değişirse güncelleme ister |
| map[string]interface{} | Esnek, hızlı prototiplenir | Tip kontrolü zahmetlidir |
| json.RawMessage | Parçalı çözümleme sağlar | Daha ileri seviye yönetim ister |

## Hata yönetimi ve sözleşme bilinci

JSON işlemlerinde en büyük hata, “Karşı taraf doğru gönderir ya” rahatlığıdır. Göndermez. Alan eksik gelir, sayı string gelir, null gelir, hatta bazen HTML hata sayfası JSON sanılıp parse edilmeye çalışılır. Bu yüzden her `Marshal` ve `Unmarshal` çağrısında hata kontrolü yapılmalıdır.

Ayrıca JSON, sistemler arası bir sözleşmedir. Bu sözleşmenin maliyetini basitçe şöyle düşünebiliriz: $Toplam\ Risk = Veri\ Belirsizliği \times Entegrasyon\ Sayısı$. Entegrasyon arttıkça küçük tip hataları bile büyük problemlere dönüşür.

## Sonuç

Go’nun `encoding/json` paketi, dış sistemlerle konuşmak için sade ama güçlü bir araçtır. Struct tag’leriyle alan adlarını kontrol eder, `Marshal` ile veriyi dışarı yollar, `Unmarshal` ile gelen veriyi güvenli şekilde içeri alırız. İyi modellenmiş struct’lar, dikkatli hata yönetimi ve tip farkındalığı sayesinde JSON iletişimi kaotik bir mesajlaşma grubu olmaktan çıkar, düzenli bir protokole dönüşür.
