---
layout: post
title: "Jenerikler ile Tek Kod, Birçok Tip: Esnek ve Tekrarsız Programlama"
math: true
categories: 
  - Bilgi
tags: 
  - generics
  - swift
  - temiz kod
---

Aynı işlemi `Int`, `String` ve özel veri tipleri için ayrı ayrı yazdığınızı düşünün. Kod çalışır; fakat proje büyüdükçe kopyalanmış fonksiyonlar küçük bir klon ordusuna dönüşür. Jenerikler (Generics), fonksiyonları, yapıları ve enum’ları belirli bir tipe kilitlemeden tanımlamamızı sağlar. Böylece tip güvenliğinden vazgeçmeden daha esnek, yeniden kullanılabilir ve bakımı kolay kod üretiriz.

``

## Jeneriklerin Temel Mantığı

Jenerik programlamada somut bir tip yerine **tip parametresi** kullanılır. Genellikle `T`, `U`, `Element` veya `Value` gibi isimlerle gösterilen bu parametre, kod kullanılırken gerçek bir tipe dönüşür.

Örneğin iki değerin yerini değiştiren işlemi her veri tipi için ayrı yazmak gereksizdir. Swift ile jenerik sürümü şöyle tanımlanabilir:

```swift
func yerDegistir<T>(_ ilk: inout T, _ ikinci: inout T) {
    let gecici = ilk
    ilk = ikinci
    ikinci = gecici
}

var x = 10
var y = 20
yerDegistir(&x, &y)

var ad1 = "Ada"
var ad2 = "Linus"
yerDegistir(&ad1, &ad2)
```

Buradaki `T`, çağrı sırasında Swift tarafından belirlenir. İlk çağrıda `Int`, ikinci çağrıda `String` olur. Fonksiyonun gövdesi ise yalnızca bir kez yazılmıştır.

Kod tekrarının yaklaşık maliyetini $C_{tekrar} = n \times m$ şeklinde düşünebiliriz. Burada $n$ desteklenen tip sayısı, $m$ ise her uygulamanın bakım maliyetidir. Jenerik yaklaşımda bu maliyet ideal olarak $C_{jenerik} \approx m$ seviyesine iner.

## Jenerik ve Geleneksel Yaklaşım

| Özellik | Tipe Özel Kod | Jenerik Kod |
|---|---|---|
| Kod tekrarı | Yüksek | Düşük |
| Tip güvenliği | Var | Var |
| Yeniden kullanım | Sınırlı | Yüksek |
| Bakım kolaylığı | Tip sayısıyla azalır | Merkezi yapı sayesinde artar |
| İlk okuma kolaylığı | Daha basit | Biraz soyutlama bilgisi ister |

Jenerikler, `Any` kullanmakla aynı şey değildir. `Any`, farklı tipleri kabul ederken tip hakkındaki bilgiyi büyük ölçüde çalışma zamanına bırakır. Jenerikler ise derleme zamanında gerçek tipi korur. Bu nedenle yanlış tip kullanımları program çalışmadan yakalanabilir.

## Jenerik Yapılar

Bir yığın veri yapısı yalnızca sayılarla çalışmak zorunda değildir. Kitaplar, kullanıcılar veya uzay gemileri de aynı yığına eklenebilir; tabii aynı örnek içinde eleman tipi tutarlı olmak şartıyla.

```swift
struct Yigin<Element> {
    private var elemanlar: [Element] = []

    mutating func ekle(_ eleman: Element) {
        elemanlar.append(eleman)
    }

    mutating func cikar() -> Element? {
        elemanlar.popLast()
    }
}

var sayilar = Yigin<Int>()
sayilar.ekle(42)
sayilar.ekle(7)

var diller = Yigin<String>()
diller.ekle("Swift")
diller.ekle("Rust")
```

`Element`, yığının saklayacağı tipi temsil eder. Aynı yapı tanımıyla sınırsız sayıda tip için güvenli yığınlar oluşturulabilir.

## Enum’larda Jenerik Gücü

Ağ işlemlerinde başarı durumunda veri, başarısızlık durumunda hata taşımak yaygın bir ihtiyaçtır. Jenerik enum bu iki değerin tipini dışarıdan alabilir:

```swift
enum APIResult<Success, Failure> {
    case success(Success)
    case failure(Failure)
}

struct User {
    let id: Int
    let name: String
}

enum NetworkError {
    case timeout
    case unauthorized
}

let result: APIResult<User, NetworkError> =
    .success(User(id: 1, name: "Grace"))
```

Bu model, başarılı sonucun `User`, hatanın ise `NetworkError` olduğunu açıkça belirtir. Böylece belirsiz sözlükler veya zorunlu tip dönüşümleri ortadan kalkar.

## Tip Kısıtlamaları

Her jenerik işlem bütün tiplerle çalışamaz. Örneğin iki değerin eşitliğini kontrol etmek için tipin `Equatable` protokolüne uyması gerekir:

```swift
func ayniMi<T: Equatable>(_ sol: T, _ sag: T) -> Bool {
    sol == sag
}

print(ayniMi(5, 5))
print(ayniMi("Swift", "Kotlin"))
```

`T: Equatable` ifadesi, “Herhangi bir tip olabilir ama eşitlik karşılaştırmasını desteklemeli” demektir. Kısıtlamalar jenerikleri daraltmaz; aksine hangi yeteneklere güvenilebileceğini açıkça tanımlar.

Jenerikler doğru kullanıldığında kod tabanını küçültür, hataları derleme aşamasına taşır ve soyutlamaları güçlendirir. Ancak yalnızca bir yerde kullanılacak basit kodu gereksiz yere jenerikleştirmek okunabilirliği azaltabilir. Altın kural şudur: Aynı davranış birden fazla tip için gerçekten anlamlıysa jenerikler sahneye çıkmalı; aksi hâlde soyutlama pelerinini dolapta bırakmalıdır.
