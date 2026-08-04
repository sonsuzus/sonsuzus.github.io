---
layout: post
title: "Enum Nedir? Sihirli Değerleri Anlamlı Sabitlere Dönüştürmek"
math: true
categories: 
  - Bilgi
tags: 
  - enum
  - veri yapıları
  - temiz kod
---

Bir siparişin durumunu `1`, kullanıcı rolünü `"A"`, haftanın gününü ise `4` ile temsil ettiğinizi düşünün. Bu değerler çalışır; fakat kodu aylar sonra okuyan geliştirici için küçük bir bilmeceye dönüşür: “1 hazırlanıyor mu, kargoda mı?” Enum, ilişkili sabitleri anlamlı isimlerden oluşan tek bir tür altında toplayarak bu bilmeceleri ortadan kaldırır.

``

## Enum mantığı

Enum, yani *enumeration* veya numaralandırma, alabileceği değerler önceden belirlenmiş kategorik bir veri türüdür. Bir `SiparisDurumu` değişkeni yalnızca `Bekliyor`, `Hazirlaniyor`, `Kargoda` ya da `TeslimEdildi` gibi tanımlanmış seçeneklerden birini taşır. Böylece hem insan hem de derleyici değişkenin anlamını bilir.

Matematiksel açıdan enum değerlerini sonlu bir küme gibi düşünebiliriz:

$$S = \{Bekliyor, Hazirlaniyor, Kargoda, TeslimEdildi\}$$

Bir sipariş durumu değişkeni için $d \in S$ koşulu geçerlidir. `Patates` gibi kümede bulunmayan bir değerin atanması tür güvenli bir dilde derleme hatası üretir. Enum’un temel avantajı tam olarak budur: Geçersiz durumları daha program çalışmadan yakalamak.

| Yaklaşım | Örnek | Okunabilirlik | Hata riski |
|---|---|---:|---:|
| Sihirli sayı | `durum == 2` | Düşük | Yüksek |
| Metin | `durum == "Kargoda"` | Orta | Yazım hatasına açık |
| Enum | `durum == SiparisDurumu.Kargoda` | Yüksek | Düşük |

## Temel kullanım

C# ile bir sipariş durumunu şöyle modelleyebiliriz:

```csharp
public enum SiparisDurumu
{
    Bekliyor = 1,
    Hazirlaniyor = 2,
    Kargoda = 3,
    TeslimEdildi = 4,
    IptalEdildi = 5
}

SiparisDurumu durum = SiparisDurumu.Kargoda;

if (durum == SiparisDurumu.Kargoda)
{
    Console.WriteLine("Siparişiniz yola çıktı!");
}
```

Buradaki sayısal karşılıklar depolama, veritabanı uyumluluğu veya dış sistemlerle iletişim için kullanılabilir. Ancak uygulama kodunda sayı yerine isim tercih edilir. `3` tek başına sessiz ve gizemliyken `SiparisDurumu.Kargoda` adeta megafonla ne olduğunu söyler.

Enum değerleri `switch` ifadeleriyle de oldukça uyumludur:

```csharp
string MesajOlustur(SiparisDurumu durum)
{
    return durum switch
    {
        SiparisDurumu.Bekliyor => "Sipariş onay bekliyor.",
        SiparisDurumu.Hazirlaniyor => "Mutfakta hareket var!",
        SiparisDurumu.Kargoda => "Paket yolda.",
        SiparisDurumu.TeslimEdildi => "Afiyet olsun!",
        SiparisDurumu.IptalEdildi => "Sipariş iptal edildi.",
        _ => "Bilinmeyen durum."
    };
}
```

Bu fonksiyon, her kategoriyi açıkça ele alır ve durum ile kullanıcı mesajı arasındaki ilişkiyi merkezi bir yerde tutar.

## Bayrak enum’ları

Bazı kategorilerde değişken aynı anda birden fazla seçeneği taşımalıdır. Dosya izinleri bunun klasik örneğidir. İkili sistemde her seçeneğe $2^n$ biçiminde bir değer verirsek seçenekleri bit düzeyinde birleştirebiliriz:

```csharp
[Flags]
public enum DosyaIzni
{
    Yok = 0,
    Oku = 1,      // 2^0
    Yaz = 2,      // 2^1
    Calistir = 4  // 2^2
}

DosyaIzni izin = DosyaIzni.Oku | DosyaIzni.Yaz;
bool yazabilir = izin.HasFlag(DosyaIzni.Yaz);
```

Burada birleşik değer $1 + 2 = 3$ olur; fakat kod hâlâ anlamlı isimlerle çalışır. Normal enum tek seçim, bayrak enum’u ise kontrollü çoklu seçim için uygundur.

| Enum türü | Kullanım alanı | Örnek |
|---|---|---|
| Standart enum | Birbirini dışlayan durumlar | Sipariş durumu |
| Bayrak enum’u | Birleşebilen seçenekler | Dosya izinleri |

## Ne zaman kullanılmamalı?

Seçenekler çalışma sırasında veritabanından ekleniyor, sık sık değişiyor veya kullanıcı tarafından yönetiliyorsa enum fazla katı kalabilir. Böyle durumlarda tablo, yapılandırma dosyası ya da sınıf tabanlı bir model daha uygundur. Ayrıca enum üyelerini silmek veya sayısal değerlerini değiştirmek, kayıtlı eski verilerle uyumsuzluk yaratabilir.

Özetle enum; sınırlı, kararlı ve anlamlı kategorileri modellemek için küçük ama etkili bir araçtır. Sihirli değerleri kovar, otomatik tamamlama desteği sunar, geçersiz atamaları azaltır ve kodu kendi kendini açıklayan bir belgeye dönüştürür.
