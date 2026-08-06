---
layout: post
title: "Try-Catch ve Loglama ile Hataları Sessizce Yönetmek"
math: true
categories: 
  - Bilgi
tags: 
  - try-catch
  - loglama
  - veritabanı
---

Bir uygulamanın hiç hata üretmemesi güzel bir hayaldir; ancak gerçek dünyada ağ bağlantıları kopar, veritabanları kısa süreliğine erişilemez olur ve kullanıcılar sayısal alana “patates” yazabilir. Profesyonel yazılımın amacı hataları tamamen yok etmekten çok, oluşan hataları kontrollü biçimde yönetmek, kullanıcıya güvenli bir mesaj göstermek ve geliştiriciye sorunu araştırabileceği kayıtlar bırakmaktır.
``

## Hata yakalamanın temel mantığı

`try-catch`, çalışma sırasında hata üretme ihtimali bulunan kodu denetimli bir alan içinde çalıştırır. `try` bloğunda hata oluşursa normal akış durur ve uygun `catch` bloğuna geçilir. Hata oluşmazsa `catch` çalıştırılmaz.

Bir işlemin başarısız olma olasılığını $P(H)$, hatanın kontrolsüz kalması durumundaki maliyeti $M$ ile gösterirsek beklenen risk kabaca şöyle modellenebilir:

$$R = P(H) \times M$$

Loglama hata olasılığını azaltmaz; fakat teşhis süresini ve dolayısıyla maliyeti düşürür. Başka bir deyişle, log dosyası uygulamanın kara kutusudur.

| Yaklaşım | Kullanıcı ne görür? | Geliştirici ne elde eder? | Sonuç |
|---|---|---|---|
| Hata yakalanmaz | Teknik hata veya kapanan uygulama | Eksik bilgi | Kötü deneyim |
| Sadece `catch` kullanılır | Genel mesaj | Çok az ayrıntı | Sorun gizlenebilir |
| `catch` ve loglama kullanılır | Güvenli, anlaşılır mesaj | Zaman, konum ve hata ayrıntısı | Kontrollü yönetim |

## Basit bir C# örneği

Aşağıdaki metot, riskli bir bölme işlemini yakalar ve teknik ayrıntıları kullanıcıya göstermeden dosyaya kaydeder:

```csharp
public static double GuvenliBolme(double sayi, double bolen)
{
    try
    {
        if (bolen == 0)
            throw new DivideByZeroException("Bölen sıfır olamaz.");

        return sayi / bolen;
    }
    catch (DivideByZeroException ex)
    {
        LogYaz(ex, "GuvenliBolme");
        Console.WriteLine("İşlem tamamlanamadı. Değerleri kontrol edin.");
        return 0;
    }
}
```

Burada kullanıcı yalnızca anlaşılır bir uyarı görür. İstisnanın mesajı, türü ve çağrı zinciri ise geliştirici için saklanır. `catch (Exception)` bütün hataları yakalayabilir; ancak mümkün olduğunda önce `SqlException`, `IOException` gibi özel türler ele alınmalıdır.

## Dosyaya log yazmak

Basit projelerde aşağıdaki yardımcı metot yeterli olabilir:

```csharp
public static void LogYaz(Exception hata, string kaynak)
{
    string klasor = Path.Combine(AppContext.BaseDirectory, "logs");
    Directory.CreateDirectory(klasor);

    string dosya = Path.Combine(klasor, "hatalar.log");
    string kayit = $"[{DateTime.UtcNow:O}] " +
                   $"Kaynak: {kaynak}\n" +
                   $"Tür: {hata.GetType().Name}\n" +
                   $"Mesaj: {hata.Message}\n" +
                   $"Detay: {hata.StackTrace}\n---\n";

    File.AppendAllText(dosya, kayit);
}
```

`UtcNow` kullanmak, farklı saat dilimlerindeki sunucuların kayıtlarını karşılaştırmayı kolaylaştırır. `StackTrace` ise hataya giden metot zincirini gösterir. Bununla birlikte parola, bağlantı parolası, erişim anahtarı veya kişisel veri kesinlikle loglanmamalıdır.

## Veritabanı bağlantısını güvenli yönetmek

```csharp
try
{
    using SqlConnection baglanti = new(connectionString);
    await baglanti.OpenAsync();

    using SqlCommand komut = new(
        "SELECT Ad FROM Urunler WHERE Id = @id", baglanti);
    komut.Parameters.AddWithValue("@id", urunId);

    object? sonuc = await komut.ExecuteScalarAsync();
}
catch (SqlException ex)
{
    LogYaz(ex, "UrunGetir-Veritabani");
    Console.WriteLine("Bilgilere şu anda ulaşılamıyor. Lütfen tekrar deneyin.");
}
```

`using`, işlem başarılı olsa da hata oluşsa da bağlantının kapatılmasını sağlar. Aynı amaçla `finally` bloğu da kullanılabilir. `finally`, istisna yakalansın veya yakalanmasın mutlaka çalışır; bu nedenle geçici dosya, bağlantı ve benzeri kaynakların temizlenmesi için uygundur.

## İyi logun küçük kontrol listesi

Bir log kaydında zaman, hata türü, güvenli hata mesajı, işlem adı ve izleme kimliği bulunmalıdır. Üretim projelerinde elle dosya yazmak yerine Serilog, NLog veya Microsoft.Extensions.Logging tercih edilebilir. Bu araçlar log seviyeleri, günlük dosya döndürme ve merkezi izleme desteği sunar.

Son olarak, hatayı yakalayıp tamamen unutmak en tehlikeli yaklaşımdır. Kullanıcıyı teknik ayrıntılardan koruyun; fakat geliştiriciyi karanlıkta bırakmayın. İyi yönetilen hata sessizdir, iyi yazılmış log ise oldukça konuşkandır.
