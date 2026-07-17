---
layout: post
title: "Go ile Blokzincir Temelleri: Hash’lerle Değiştirilemez Zincir Kurmak"
math: true
categories: 
  - Program
tags: 
  - Go
  - Blockchain
  - Kriptografi
---

Blokzincir kulağa bazen uzay teknolojisi gibi gelir; ama temel fikir oldukça nettir: Verileri bloklar halinde sakla, her bloğu bir öncekinin kriptografik iziyle bağla ve zincirin ortasından bir parçayı değiştirmeyi neredeyse imkânsız hale getir. Bu yazıda Go kullanarak küçük ama öğretici bir blokzincir modeli kuracağız; amaç coin üretmek değil, değiştirilemezlik fikrini programlayarak anlamak.
``

Blokzincirin kalbinde **kriptografik özetleme fonksiyonu** yani hash vardır. Bir hash fonksiyonu, herhangi uzunluktaki girdiyi sabit uzunlukta bir çıktıya dönüştürür. Örneğin SHA-256 çıktısı 256 bittir. Matematiksel olarak şöyle düşünebiliriz:

$$H(x) = y$$

Burada $x$ veri, $y$ ise özet değerdir. İyi bir hash fonksiyonunda küçük bir değişiklik bile sonucu tamamen farklılaştırır. Buna **çığ etkisi** denir. Yani `Merhaba` ile `MerhabA` aynı görünse de hash açısından bambaşka evrenlerdir.

| Özellik | Normal Kontrol Toplamı | Kriptografik Hash |
|---|---|---|
| Amaç | Hata yakalama | Bütünlük ve güvenlik |
| Çıktı | Genelde kısa | Sabit ve güçlü |
| Çakışmaya direnç | Zayıf olabilir | Çok güçlü olmalıdır |
| Küçük değişime tepki | Sınırlı | Büyük, tahmin edilemez |

Bir blok genellikle şu alanlardan oluşur: veri, zaman damgası, kendi hash değeri ve önceki bloğun hash değeri. İşin sihri son alandadır. Çünkü her blok, kendinden öncekinin özetini taşır. Böylece üçüncü bloğu değiştirmek isterseniz sadece üçüncü bloğun hash’i değil, dördüncü, beşinci ve devamındaki tüm bloklar bozulur.

Basit formülümüz şu olabilir:

$$BlockHash = SHA256(Index + Timestamp + Data + PreviousHash)$$

Şimdi Go tarafına geçelim. Aşağıdaki kod, minimal bir blok yapısı tanımlar ve SHA-256 ile hash üretir:

```go
package main

import (
    "crypto/sha256"
    "encoding/hex"
    "fmt"
    "time"
)

type Block struct {
    Index        int
    Timestamp    string
    Data         string
    PreviousHash string
    Hash         string
}

func calculateHash(b Block) string {
    record := fmt.Sprintf("%d%s%s%s", b.Index, b.Timestamp, b.Data, b.PreviousHash)
    sum := sha256.Sum256([]byte(record))
    return hex.EncodeToString(sum[:])
}
```

Burada `calculateHash`, bloğun anlamlı alanlarını tek bir metne çevirir ve SHA-256’dan geçirir. `hex.EncodeToString` ise ham byte çıktısını okunabilir onaltılık formata dönüştürür.

Şimdi yeni blok üretelim:

```go
func createBlock(index int, data string, previousHash string) Block {
    block := Block{
        Index:        index,
        Timestamp:    time.Now().String(),
        Data:         data,
        PreviousHash: previousHash,
    }
    block.Hash = calculateHash(block)
    return block
}
```

Bu fonksiyon bloğu oluşturur, ardından hash değerini hesaplayıp bloğun içine yazar. İlk bloğa genellikle **genesis block** denir. Çünkü zincirin başlangıç noktasıdır ve önceki bloğu yoktur.

```go
func main() {
    genesis := createBlock(0, "Genesis Block", "")
    second := createBlock(1, "Ali -> Ayşe: 10 token", genesis.Hash)
    third := createBlock(2, "Ayşe -> Mehmet: 4 token", second.Hash)

    blockchain := []Block{genesis, second, third}

    for _, block := range blockchain {
        fmt.Println("Index:", block.Index)
        fmt.Println("Data:", block.Data)
        fmt.Println("Prev:", block.PreviousHash)
        fmt.Println("Hash:", block.Hash)
        fmt.Println("---")
    }
}
```

Bu programı çalıştırdığınızda her bloğun, bir önceki bloğun hash değerini taşıdığını görürsünüz. Zincir fikri tam olarak budur: Her halka, kendinden önceki halkanın dijital parmak izini saklar.

Peki biri ikinci bloğun verisini değiştirirse ne olur? Mesela `Ali -> Ayşe: 10 token` yerine `Ali -> Ayşe: 1000 token` yazarsa, ikinci bloğun hash’i değişir. Ancak üçüncü blok hâlâ eski ikinci hash’e bağlıdır. Böylece zincir tutarsız hale gelir.

Bunu kontrol etmek için basit bir doğrulama fonksiyonu yazabiliriz:

```go
func isChainValid(chain []Block) bool {
    for i := 1; i < len(chain); i++ {
        current := chain[i]
        previous := chain[i-1]

        if current.Hash != calculateHash(current) {
            return false
        }
        if current.PreviousHash != previous.Hash {
            return false
        }
    }
    return true
}
```

Bu fonksiyon iki şeyi denetler: Bloğun kendi hash’i gerçekten içeriğinden mi üretilmiş, ayrıca önceki bloğa doğru şekilde mi bağlanmış? İkisinden biri bozulursa zincir geçersizdir.

| Kavram | Go’daki Karşılığı | Ne İşe Yarar? |
|---|---|---|
| Blok | `struct` | Veriyi paketler |
| Hash | `sha256.Sum256` | Dijital parmak izi üretir |
| Zincir | `[]Block` | Blokları sıralı tutar |
| Doğrulama | `isChainValid` | Müdahaleyi yakalar |

Gerçek blokzincirlerde buna ek olarak dağıtık ağ, mutabakat algoritmaları, proof of work, imzalar ve cüzdanlar bulunur. Ancak çekirdek düşünce değişmez: Geçmişi değiştirmek pahalı, görünür ve pratikte sürdürülemez olmalıdır.

Özetle Go ile yazdığımız bu mini zincir, blokzincirin büyüsünü sadeleştirir: veri + önceki hash + kriptografik özet = birbirine kilitlenmiş kayıtlar. Gerçek dünyadaki dev sistemlerin altında da bu basit ama güçlü fikir yatar.
