---
layout: post
title: "İşaretçiler ve Bellek Modeli: Go’da Güvenli Adreslerle Dans"
math: true
categories: 
  - Bilgi
tags: 
  - Go
  - Pointers
  - Garbage Collector
  - Bellek Yönetimi
---

Programlama dünyasında işaretçiler, belleğin haritasını elinize alıp “şu adrese git, oradaki değeri getir” demenin yoludur. C ve C++ tarafında bu harita bazen hazineye, bazen de mayın tarlasına çıkar; Go ise aynı fikri daha güvenli korkuluklarla sunar. Yani adresleri görebiliriz, değerleri dolaylı yoldan değiştirebiliriz ama rastgele bellek aritmetiğiyle sistemi yakmamıza izin verilmez.
``

Belleği kabaca büyük bir apartman gibi düşünebiliriz. Her dairenin bir numarası, yani adresi vardır. Bir değişken de bu dairelerden birinde oturan veridir. Matematiksel olarak bellek, adreslerden değerlere giden bir fonksiyon gibi düşünülebilir: $M: A \rightarrow V$. Burada $A$ adres kümesini, $V$ ise değerleri temsil eder. Bir işaretçi ise doğrudan değeri değil, o değerin yaşadığı adresi tutar.

Go’da bir değişkenin adresini almak için `&`, işaretçinin gösterdiği değere erişmek için `*` kullanılır:

```go
package main

import "fmt"

func main() {
    x := 42
    p := &x // x değişkeninin adresini tutar

    fmt.Println(x)
    fmt.Println(p)
    fmt.Println(*p)

    *p = 100 // p üzerinden x değerini değiştirir
    fmt.Println(x)
}
```

Bu örnekte `p`, `x` değişkeninin adresini saklar. `*p = 100` dediğimizde “p’nin gösterdiği adresteki değeri 100 yap” deriz. Sonuçta değişen şey `p` değil, `x` olur. İşte işaretçilerin gücü burada başlar: veriyi kopyalamadan, aynı bellek konumuna erişmek.

| Kavram | Anlamı | Go’daki Operatör |
|---|---|---|
| Değer | Bellekte saklanan gerçek veri | `x` |
| Adres | Verinin bellekteki konumu | `&x` |
| İşaretçi | Adresi tutan değişken | `p := &x` |
| Dereference | Adresteki değere erişme | `*p` |

Peki bu neden önemli? Çünkü büyük veri yapıları kopyalanmak yerine adres üzerinden taşınabilir. Diyelim ki elimizde büyük bir `struct` var. Bunu fonksiyona değer olarak verirsek kopya oluşur. İşaretçiyle verirsek aynı nesne üzerinde çalışırız.

```go
type User struct {
    ID    int
    Score int
}

func increaseScore(u *User) {
    u.Score += 10
}

func main() {
    user := User{ID: 1, Score: 50}
    increaseScore(&user)
    fmt.Println(user.Score)
}
```

Burada `increaseScore` fonksiyonu `*User` alır. Yani bir kullanıcı kopyası değil, kullanıcının adresi fonksiyona gider. Go, `u.Score` yazımına izin vererek `(*u).Score` ifadesini bizim için sadeleştirir. Küçük ama tatlı bir ergonomi hediyesi!

Go’nun bellek modeli stack ve heap kavramlarıyla çalışır. Stack, fonksiyon çağrıları için hızlı ve düzenli bir alandır. Heap ise yaşam süresi daha belirsiz olan nesneler için kullanılır. Derleyici, escape analysis denen analizle bir değişkenin fonksiyon dışına “kaçıp kaçmadığını” inceler. Eğer kaçıyorsa heap’e taşınabilir.

| Özellik | Stack | Heap |
|---|---|---|
| Hız | Çok hızlı | Görece yavaş |
| Yönetim | Otomatik, fonksiyon bitince temizlenir | Garbage collector tarafından izlenir |
| Kullanım | Yerel ve kısa ömürlü veriler | Paylaşılan veya uzun ömürlü veriler |
| Go kararı | Derleyici analiz eder | Derleyici ve GC birlikte yönetir |

Örneğin bir fonksiyon yerel değişkenin adresini döndürürse, Go bunu tehlikeli kabul edip çökmez; derleyici değişkeni heap’e taşıyabilir:

```go
func newCounter() *int {
    count := 0
    return &count
}
```

C dilinde benzer bir durum büyük bir probleme dönüşebilirken Go, yaşam süresini analiz eder. Çünkü Go’da amaç, işaretçilerin performans avantajını verirken “dangling pointer” gibi klasik hataları azaltmaktır.

Garbage collector, heap üzerindeki artık erişilemeyen nesneleri temizleyen arka plan görevlisidir. Basitçe köklerden, yani global değişkenlerden, stack’teki referanslardan ve aktif goroutine’lerden başlar; erişilebilen nesneleri işaretler. Erişilemeyenler çöp kabul edilir. Bunu grafik gibi düşünebiliriz: Eğer bir nesneye giden yol yoksa, $reachable(obj) = false$ olur ve temizlik adayıdır.

Go’nun işaretçileri güvenlidir çünkü pointer arithmetic desteklenmez. Yani `p + 1` diyerek keyfi adrese zıplayamayız. Bu, bellek modelini daha öngörülebilir yapar. Elbette `unsafe` paketiyle bu sınırlar aşılabilir; fakat adı üstünde, orası emniyet kemerini çıkarıp viraja hızlı girmek gibidir.

Sonuç olarak Go’da işaretçiler, belleği doğrudan yönetmenin kontrollü bir yoludur. Adresleri kullanırız, kopyaları azaltırız, fonksiyonlar arasında veriyi etkili biçimde paylaşırız. Arka planda derleyicinin escape analysis mekanizması ve garbage collector ikilisi, çoğu bellek temizliği yükünü bizden alır. Kısacası Go, işaretçileri bir testere gibi değil, güvenlik kilitli bir İsviçre çakısı gibi sunar: güçlü, pratik ve dikkatli kullanıldığında oldukça keyifli.
