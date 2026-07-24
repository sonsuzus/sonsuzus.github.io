---
layout: post
title: "Go’da Metotlar ve Receiver Mantığı: Struct’lara Davranış Kazandırmak"
math: true
categories: 
  - Bilgi
tags: 
  - golang
  - methods
  - struct
  - receiver
  - nesne-yönelimli-programlama
---

Go’da bir `struct` yalnızca veri taşımak zorunda değildir; ona metotlar bağlayarak belirli davranışlar kazandırabiliriz. Bu yaklaşım, klasik sınıf tabanlı nesne yönelimli programlamadan farklıdır: Go’da `class`, kalıtım veya `this` yoktur; bunun yerine sade, açık ve güçlü bir `receiver` mantığı vardır.
``

Go’da metot, teknik olarak bir fonksiyondur; fakat özel bir parametreye sahiptir: **receiver**. Receiver, metodun hangi tipe aitmiş gibi çağrılacağını belirler. Matematiksel olarak düşünürsek, normal bir fonksiyon şöyle modellenebilir: $f(x) \rightarrow y$. Metotta ise fonksiyon, belirli bir veri tipinin bağlamında çalışır: $T.f(x) \rightarrow y$. Buradaki $T$, örneğin bir `User`, `Account` veya `Rectangle` struct’ı olabilir.

Basit bir örnekle başlayalım:

```go
package main

import "fmt"

type Rectangle struct {
    Width  float64
    Height float64
}

func (r Rectangle) Area() float64 {
    return r.Width * r.Height
}

func main() {
    box := Rectangle{Width: 10, Height: 5}
    fmt.Println(box.Area())
}
```

Burada `(r Rectangle)` kısmı receiver’dır. Yani `Area` metodu, `Rectangle` tipine bağlanmıştır. Artık `Area(box)` yazmak yerine daha doğal bir şekilde `box.Area()` yazarız. Kodun okunabilirliği artar; çünkü davranış, ilgili veri yapısının yanında durur.

| Yaklaşım | Örnek | Okunabilirlik | Go’daki Yeri |
|---|---|---|---|
| Normal fonksiyon | `Area(rect)` | Orta | Geçerli ve sık kullanılır |
| Metot | `rect.Area()` | Yüksek | Struct davranışları için idealdir |
| Class metodu | `rect.area()` | Dile bağlı | Go’da class yoktur |

Receiver iki şekilde tanımlanabilir: **value receiver** ve **pointer receiver**. Value receiver, struct’ın bir kopyası üzerinde çalışır. Pointer receiver ise orijinal veriye erişir ve onu değiştirebilir.

```go
type Account struct {
    Owner   string
    Balance float64
}

func (a Account) CurrentBalance() float64 {
    return a.Balance
}

func (a *Account) Deposit(amount float64) {
    if amount <= 0 {
        return
    }
    a.Balance += amount
}
```

`CurrentBalance` yalnızca okuma yaptığı için value receiver yeterlidir. `Deposit` ise bakiyeyi değiştirdiği için pointer receiver kullanır. Eğer para yatırma işlemini formülle ifade edersek: $bakiye_{yeni} = bakiye_{eski} + miktar$. Bu işlemde eski değerin gerçekten güncellenmesi gerekir; kopya üzerinde çalışmak işe yaramaz.

| Receiver Türü | Tanım | Veriyi Değiştirir mi? | Ne Zaman Kullanılır? |
|---|---|---|---|
| Value receiver | `(a Account)` | Hayır, kopya üzerinde çalışır | Küçük struct’lar, salt okuma işlemleri |
| Pointer receiver | `(a *Account)` | Evet, orijinali değiştirebilir | Güncelleme, büyük struct, performans |

Go’nun burada sunduğu güzellik şudur: Nesne yönelimli programlamadaki “nesne davranış taşır” fikrini alır, ama sınıf hiyerarşisi karmaşasını dayatmaz. Bir struct veri modelini temsil eder, metotlar ise bu veri modeline ait davranışları ifade eder. Yani Go şunu der: “Veriyi ayrı düşün, davranışı açıkça bağla.”

Klasik OOP ile Go yaklaşımını karşılaştıralım:

| Kavram | Klasik OOP | Go Yaklaşımı |
|---|---|---|
| Sınıf | Temel yapı taşıdır | Yoktur |
| Nesne | Class örneğidir | Struct değeri olabilir |
| Metot | Class içinde tanımlanır | Herhangi bir tipe receiver ile bağlanır |
| Kalıtım | Sınıflar arası aktarım | Composition tercih edilir |
| Polymorphism | Inheritance veya interface | Interface ile örtük uygulanır |

Receiver adı genellikle kısa seçilir: `u User`, `r Rectangle`, `a Account` gibi. Go topluluğu `this` veya `self` benzeri isimler kullanmayı önermez. Çünkü receiver zaten bağlamı açıkça gösterir. Ayrıca aynı tipe ait metotlarda receiver adını tutarlı seçmek kodun ritmini güzelleştirir.

Biraz daha gerçekçi örnek düşünelim:

```go
type Task struct {
    Title     string
    Completed bool
}

func (t *Task) Complete() {
    t.Completed = true
}

func (t Task) Status() string {
    if t.Completed {
        return "tamamlandı"
    }
    return "bekliyor"
}
```

Bu örnekte `Task`, sadece iki alanlı basit bir veri yapısıdır. Ancak `Complete` ve `Status` metotlarıyla birlikte artık küçük bir davranış modeline dönüşür. Kod başka bir yerde `task.Complete()` gördüğünde niyet hemen anlaşılır: görev tamamlanıyor.

Sonuç olarak Go’daki metot ve receiver sistemi, nesne yönelimli düşüncenin pratik tarafını korur: veriyle ilişkili davranışları bir araya getirir. Fakat bunu sınıf, kalıtım ve karmaşık hiyerarşiler olmadan yapar. Eğer bir struct’ın “ne olduğunu” alanları belirliyorsa, “ne yapabildiğini” de metotları belirler. Go’nun felsefesi de tam burada parlar: az sihir, çok netlik.
