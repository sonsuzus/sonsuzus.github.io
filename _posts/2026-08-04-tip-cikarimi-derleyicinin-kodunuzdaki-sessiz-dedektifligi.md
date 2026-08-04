---
layout: post
title: "Tip Çıkarımı: Derleyicinin Kodunuzdaki Sessiz Dedektifliği"
math: true
categories: 
  - Bilgi
tags: 
  - tip çıkarımı
  - derleyici
  - statik tipleme
---

Bir değişken tanımlarken veri türünü yazmadığınız hâlde editörünüzün onun sayı mı, metin mi yoksa daha karmaşık bir nesne mi olduğunu bilmesi sihir gibi görünebilir. Aslında perde arkasında çalışan mekanizma **tip çıkarımıdır**. Derleyici, atanan ifadeyi inceleyerek uygun türü belirler; böylece kod kısalırken statik tip güvenliği büyük ölçüde korunur.
``

## Tip çıkarımı tam olarak nedir?

Tip çıkarımı, derleyicinin bir ifadenin veri türünü programcının açık bildirimine ihtiyaç duymadan hesaplamasıdır. Basit bir modelle değişkenin türünü şöyle gösterebiliriz:

$$T(x) = T(e)$$

Burada $x$ değişkeni, $e$ ise ona atanan ifadedir. Örneğin `x = 42` ifadesinde derleyici, `42` sabitinin türünü inceler ve dile bağlı olarak `int`, `Int` veya benzeri bir tür seçer.

Bu işlem çoğunlukla **derleme zamanında** gerçekleşir. Yani program çalışırken tür tahmini yapılmaz; derleyici daha çalıştırılabilir dosya üretilmeden önce kararını verir. Bu nedenle tip çıkarımı, dinamik tiplemeyle aynı şey değildir.

| Özellik | Tip çıkarımı | Dinamik tipleme | Açık statik tipleme |
|---|---|---|---|
| Tür ne zaman belirlenir? | Derleme zamanında | Çalışma zamanında | Programcı yazarken |
| Türü kim belirtir? | Derleyici | Çalışan program | Geliştirici |
| Sonradan farklı tür atanabilir mi? | Genellikle hayır | Genellikle evet | Hayır |
| Kod uzunluğu | Kısa | Kısa | Daha uzun |
| Erken hata yakalama | Güçlü | Daha sınırlı | Güçlü |

## Derleyici nasıl karar verir?

Derleyici önce sağ taraftaki ifadeyi analiz eder. Sabitleri, fonksiyonların dönüş türlerini, operatörleri ve varsa genel tür kısıtlarını değerlendirir. Ardından bulunan türü değişkenle eşleştirir.

C# dilindeki şu örneğe bakalım:

```csharp
var puan = 95;             // Derleyici türü int olarak çıkarır.
var mesaj = "Başarılı";   // Tür string olur.
var oran = 0.85;           // Varsayılan olarak double seçilir.
```

Buradaki `var`, değişkenin türsüz olduğu anlamına gelmez. `puan`, derleme sonrasında kesin biçimde `int` kabul edilir. Bu yüzden aşağıdaki atama geçersizdir:

```csharp
var puan = 95;
puan = "Doksan beş"; // Hata: string, int değişkenine atanamaz.
```

Derleyicinin ilk değerden hareket etmesi, türün daha sonra sürekli değişebileceği anlamına gelmez. İlk ifade yalnızca başlangıçtaki **kanıttır**; ulaşılan tür ise değişkenin kapsamı boyunca geçerli sözleşmedir.

## Fonksiyonlarda ve koleksiyonlarda çıkarım

Tip çıkarımı yalnızca basit değişkenlerle sınırlı değildir. Genel fonksiyon çağrılarında tür parametreleri de argümanlardan bulunabilir:

```typescript
function ilkEleman<T>(liste: T[]): T {
  return liste[0];
}

const sonuc = ilkEleman([10, 20, 30]);
// T, number olarak çıkarılır; sonuc da number olur.
```

Derleyici burada dizinin elemanlarını inceler ve şu ilişkiyi kurar:

$$T([10,20,30]) = number[] \Rightarrow T = number$$

Bu yaklaşım, genel ve yeniden kullanılabilir kod yazmayı kolaylaştırır. Programcı her çağrıda `<number>` yazmak zorunda kalmaz.

## Ne zaman açık tür yazılmalı?

Tip çıkarımı faydalı olsa da her yerde kullanmak okunabilirliği artırmaz. Değer türü ilk bakışta belliyse çıkarım idealdir. Karmaşık API dönüşlerinde, değişkenin niyetini vurgulamak gerektiğinde veya daha geniş bir tür hedeflendiğinde açık bildirim daha anlaşılır olabilir.

```csharp
IEnumerable<int> puanlar = new List<int> { 70, 85, 100 };
```

Burada `var` kullanmak mümkün olsa da açık tür, kodun yalnızca `List<int>` uygulamasına değil `IEnumerable<int>` sözleşmesine dayandığını anlatır.

Kısacası tip çıkarımı, geliştiricinin yerine rastgele karar veren bir mekanizma değil; ifadelerden, kısıtlardan ve dil kurallarından mantıksal sonuç üreten bir derleyici özelliğidir. Doğru kullanıldığında kodu sadeleştirir, tekrarları azaltır ve tip güvenliğinden vazgeçmeden daha akıcı programlama sağlar.
