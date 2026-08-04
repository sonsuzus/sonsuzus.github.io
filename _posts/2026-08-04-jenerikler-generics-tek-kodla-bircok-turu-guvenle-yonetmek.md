---
layout: post
title: "Jenerikler (Generics): Tek Kodla Birçok Türü Güvenle Yönetmek"
math: true
categories: 
  - Bilgi
tags: 
  - generics
  - csharp
  - tip-güvenliği
---

Bir fonksiyonu `int` için yazıp ardından `string`, `double` ve kendi sınıflarımız için kopyalamak, yazılım dünyasının pek de eğlenceli olmayan tekrarlarından biridir. Jenerikler (generics), algoritmayı veri tipinden ayırarak aynı kodun farklı türlerle güvenli biçimde çalışmasını sağlar. C++ şablonlarını andıran bu yaklaşım, özellikle C#, Java ve TypeScript gibi dillerde yeniden kullanılabilir yapıların temelini oluşturur.

``

## Temel fikir: Türü şimdi değil, kullanırken belirle

Normal bir fonksiyon parametrelerinin türünü önceden bilir. Jenerik fonksiyon ise gerçek türün yerine `T` gibi bir **tür parametresi** kullanır. Buradaki `T`, “her şey serbest” anlamına gelmez; derleyicinin çağrı sırasında belirleyeceği bir tür değişkenidir.

Matematiksel olarak normal bir fonksiyonu $f: int → int$ biçiminde düşünürsek, jenerik karşılığı $f_T: T → T$ olur. Başka bir ifadeyle algoritma sabit kalırken tür değişebilir:

$$T \in \{int, string, Customer, Product, \ldots\}$$

Derleyici `T` yerine kullanılacak gerçek tipi izlediği için yanlış tür atamaları çalışma zamanına bırakılmaz. Böylece hem tekrar azalır hem de tip güvenliği korunur.

| Yaklaşım | Yeniden kullanım | Tip güvenliği | Dönüşüm ihtiyacı |
|---|---:|---:|---:|
| Her tür için ayrı kod | Düşük | Yüksek | Yok |
| `object` kullanmak | Orta | Düşük | Genellikle var |
| Jenerik kullanmak | Yüksek | Yüksek | Genellikle yok |

## Jenerik fonksiyon örneği

Aşağıdaki C# fonksiyonu, verilen iki değerin yerini türlerinden bağımsız olarak değiştirir:

```csharp
static void YerDegistir<T>(ref T sol, ref T sag)
{
    T gecici = sol;
    sol = sag;
    sag = gecici;
}

int x = 10;
int y = 20;
YerDegistir(ref x, ref y);

string ilk = "Ada";
string ikinci = "Linus";
YerDegistir(ref ilk, ref ikinci);
```

Fonksiyon iki kez çağrılır: ilkinde `T`, `int`; ikincisinde `string` olur. Aynı algoritma kullanılırken derleyici iki değerin de uyumlu türde olmasını denetler. Örneğin bir `int` ile `string` değerini yanlışlıkla değiştirmeye çalışmak derleme hatası üretir. Hata erkenden yakalanır; gece yarısı gelen sürpriz hata bildirimi başka güne kalır.

## Jenerik sınıflar ve kısıtlamalar

Jenerikler yalnızca fonksiyonlarda değil, sınıflarda ve arayüzlerde de kullanılabilir. Aşağıdaki depo, yalnızca kimliği bulunan sınıfları kabul eder:

```csharp
interface IEntity
{
    int Id { get; }
}

class Depo<T> where T : IEntity
{
    private readonly List<T> kayitlar = new();

    public void Ekle(T kayit) => kayitlar.Add(kayit);

    public T? Bul(int id)
    {
        return kayitlar.FirstOrDefault(x => x.Id == id);
    }
}
```

`where T : IEntity` ifadesi bir **jenerik kısıtlamadır**. Bu sayede derleyici, `T` nesnelerinde `Id` özelliğinin bulunduğunu bilir. Kısıtlama olmasaydı `x.Id` kullanımının güvenli olduğuna karar veremezdi.

| Özellik | C++ Template | C# Generic |
|---|---|---|
| Tür kontrolü | Şablon oluşturulurken | Derleme ve çalışma zamanı tür sistemiyle |
| Kısıtlama yaklaşımı | Concepts / ifadeler | `where` kısıtları |
| İlkel amaç | Genel algoritmalar | Güvenli ve yeniden kullanılabilir yapılar |

## Neden `object` yeterli değil?

Her değeri `object` olarak saklamak ilk bakışta kolay görünür. Ancak geri alırken tür dönüşümü gerekir ve yanlış dönüşüm çalışma zamanında patlayabilir. Değer tiplerinde kutulama ve kutudan çıkarma maliyeti de oluşabilir. Jenerikler, tür bilgisini koruyarak bu riskleri ve gereksiz dönüşümleri azaltır.

Yine de her yere `<T>` serpiştirmek iyi tasarım değildir. Algoritma gerçekten türden bağımsızsa jenerik kullanmak mantıklıdır. Türlere göre tamamen farklı davranışlar gerekiyorsa arayüz, kalıtım veya strateji deseni daha anlaşılır olabilir.

Özetle jenerikler, “bir kez yaz, birçok türle güvenle kullan” ilkesini hayata geçirir. Daha az kopya kod, daha erken hata tespiti ve daha temiz API’ler sağlar. Doğru kısıtlamalarla birleştiğinde `T`, belirsiz bir harf olmaktan çıkıp güçlü bir tasarım aracına dönüşür.
