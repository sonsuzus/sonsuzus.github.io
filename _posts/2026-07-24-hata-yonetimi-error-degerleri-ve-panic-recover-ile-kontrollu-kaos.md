---
layout: post
title: "Hata Yönetimi: Error Değerleri ve Panic-Recover ile Kontrollü Kaos"
math: true
categories: 
  - Bilgi
tags: 
  - go
  - hata-yönetimi
  - panic-recover
---

Bir programın gerçek dünyayla ilk teması genellikle bir hatadır: dosya yoktur, ağ isteği zaman aşımına uğrar, kullanıcı sayı yerine “patates” yazar. Bazı diller bu anlarda istisna fırlatıp akışı dramatik biçimde keserken, Go gibi yaklaşımlar hatayı sıradan bir değer olarak masaya koyar. Yani hata, programın çökmesine çalışan bir canavar değil; kontrol edilmesi gereken bir dönüş değeridir.
``

## Hata bir olay değil, bir değerdir

Go’nun hata yönetimi felsefesi basittir: Fonksiyonlar başarılı sonucu ve hata bilgisini birlikte döndürebilir. Tipik imza şuna benzer:

```go
func Oku(path string) ([]byte, error) {
    data, err := os.ReadFile(path)
    if err != nil {
        return nil, fmt.Errorf("dosya okunamadı: %w", err)
    }
    return data, nil
}
```

Burada `error`, özel bir büyü değil; `Error() string` metoduna sahip bir arayüzdür. Matematiksel düşünürsek fonksiyon sonucu şöyle modellenebilir: $(T, E)$; burada $T$ beklenen veri, $E$ ise hata durumudur. Başarı halinde $E = nil$, hata halinde çoğu zaman $T$ kullanılmaz. Akış şu denklemle okunabilir: $P(başarı) + P(hata) = 1$. Yani fonksiyon ya düzgün sonuç üretir ya da neden üretemediğini açıkça bildirir.

## İstisna mı, değer mi?

| Yaklaşım | Akış Kontrolü | Okunabilirlik | Risk |
|---|---|---|---|
| Exception | Akış aniden başka bloğa zıplar | Kısa ama gizli yollar içerir | Yakalanmazsa çökme |
| Error value | Hata açıkça kontrol edilir | Daha fazla satır ama netlik yüksek | Kontrol unutulursa mantık hatası |
| Panic | Normal akışı durdurur | Acil durumlar için belirgin | Yanlış kullanımda sert çöküş |

Bu tablo Go’nun neden “hata varsa söyle, saklama” dediğini gösterir. Kod biraz daha uzun görünür; evet, `if err != nil` satırları çoğalır. Ama karşılığında fonksiyonun başarısız olabileceği yerler neon tabela gibi görünür.

## Error wrapping: Hatanın dedikodu zinciri

Hata mesajını sadece “olmadı” diye döndürmek, kullanıcıya “bir şeyler ters gitti” demek gibidir; doğru ama pek faydalı değildir. Go’da `%w` ile hata sarmalanabilir:

```go
func AyarYukle() error {
    err := VeritabaniBaglan()
    if err != nil {
        return fmt.Errorf("ayar yükleme başarısız: %w", err)
    }
    return nil
}
```

Bu sayede üst katman hem bağlamı görür hem de `errors.Is` veya `errors.As` ile kök hatayı inceleyebilir. Böylece hata, apartman dedikodusu gibi kat kat dolaşır ama kimden çıktığı da bellidir.

## Peki panic ne zaman?

`panic`, “bu fonksiyon beklenen bir hata yaşadı” demek değildir. Daha çok “programın varsayımları çöktü” anlamına gelir. Örneğin imkânsız olması gereken bir durum gerçekleştiyse, başlatma sırasında kritik yapılandırma yoksa veya bellek dışı tutarsızlık oluştuysa kullanılabilir.

| Durum | Tercih |
|---|---|
| Kullanıcı yanlış dosya yolu verdi | `error` döndür |
| API isteği timeout oldu | `error` döndür |
| Program başlarken zorunlu config yok | Duruma göre `panic` veya fatal log |
| Kodun asla ulaşmaması gereken dalı çalıştı | `panic` makul olabilir |

## Recover: Panik odasının yangın çıkışı

`recover`, yalnızca `defer` içinde çağrıldığında aktif bir `panic`i yakalayabilir. Bu mekanizma exception yakalamaya benzese de Go’da günlük hata yönetimi için önerilmez; daha çok sınır katmanlarında, örneğin HTTP sunucusunda tek bir isteğin tüm sistemi devirmesini engellemek için kullanılır.

```go
func GuvenliCalistir(fn func()) {
    defer func() {
        if r := recover(); r != nil {
            log.Printf("panic yakalandı: %v", r)
        }
    }()

    fn()
}
```

Bu kod, verilen fonksiyonu çalıştırır; içeride `panic` olursa program tamamen yere kapaklanmadan önce durumu loglar. Ancak dikkat: `recover` hatayı yok etmez, sadece kontrolü geri verir. Verinin tutarlı olup olmadığını hâlâ sen düşünmelisin.

## Pratik tasarım önerileri

1. Beklenen başarısızlıkları `error` olarak döndür.
2. Hatalara bağlam ekle: “bağlanamadı” yerine “kullanıcı profili yüklenirken veritabanına bağlanılamadı” daha değerlidir.
3. `panic`i kontrol akışı için kullanma; `if err != nil` sıkıcı olabilir ama güvenilirdir.
4. `recover`i uygulama sınırlarında kullan: HTTP middleware, worker supervisor, CLI komut sarmalayıcıları gibi.

Sonuç olarak Go’nun hata yönetimi şunu öğretir: Hata, utanılacak bir istisna değil, sistemin konuşma biçimidir. Onu değer olarak döndürdüğünde programın daha tahmin edilebilir, test edilebilir ve bakım yapılabilir olur. `panic` ise sahneye nadiren çıkan duman makinesi gibidir; doğru anda dramatik, yanlış anda tüm gösteriyi mahveder.
