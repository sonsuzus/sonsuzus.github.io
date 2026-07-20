---
layout: post
title: "Dinamik Veri Tabanı Yönetimi: Assert ve Retract ile Yaşayan Kurallar"
math: true
categories: 
  - Bilgi
tags: 
  - prolog
  - yapay-zeka
  - veritabani-yonetimi
  - mantiksal-programlama
---

Bir programın çalışırken fikrini değiştirebilmesi kulağa biraz bilim kurgu gibi gelir, değil mi? Dinamik veri tabanı yönetimi tam olarak bunu sağlar: sistem, bellekte tuttuğu gerçekleri ve kuralları çalışma anında ekler, siler ve yeni duruma göre farklı sonuçlar üretir. Özellikle Prolog gibi mantıksal programlama dillerinde `assert` ve `retract`, programı sabit bir tarif defteri olmaktan çıkarıp mutfakta karar değiştirebilen bir şefe dönüştürür.
``
Klasik programlama yaklaşımında kod ve veri çoğu zaman ayrı düşünülür. Veritabanı değişir, ama programın kuralları genellikle sabittir. Mantıksal programlamada ise bilgi tabanı, yani knowledge base, gerçeklerden ve kurallardan oluşur. Basitçe şöyle yazabiliriz: $KB_t = F_t \cup R_t$. Burada $F_t$ belirli bir andaki gerçekler kümesini, $R_t$ ise kurallar kümesini temsil eder. Dinamik yönetimde amaç, $t$ anındaki bu yapıyı $t+1$ anında güncelleyebilmektir: $KB_{t+1} = KB_t + \Delta_{ekle} - \Delta_{sil}$.

Bu fikir özellikle uzman sistemlerde, oyun yapay zekasında, kural motorlarında ve interaktif asistanlarda çok değerlidir. Çünkü dünya değişir. Kullanıcı yeni bir bilgi verir, sensör farklı bir değer okur, oyunda karakterin canı azalır ya da bir stok ürünü tükenir. Sistem bu değişikliği yalnızca kaydetmekle kalmaz, çıkarım mekanizmasına da hemen yansıtır.

| Yaklaşım | Veri/Kural Durumu | Avantaj | Risk |
|---|---|---|---|
| Statik bilgi tabanı | Program başında tanımlanır | Basit ve tahmin edilebilir | Değişen dünyaya uyum zayıf |
| Dinamik bilgi tabanı | Çalışma anında değişir | Esnek ve etkileşimli | Tutarsızlık yönetimi gerekir |
| Harici veritabanı | Program dışı saklanır | Kalıcı ve büyük ölçekli | Mantıksal çıkarımla entegrasyon zor olabilir |

Prolog tarafında `assert` yeni bir gerçeği veya kuralı belleğe ekler. `retract` ise eşleşen bir bilgiyi siler. Mini bir örnekle görelim:

```prolog
:- dynamic hasta/2.
:- dynamic riskli/1.

% Yeni bir hasta bilgisi ekler
hasta_ekle(Isim, Yas) :-
    assert(hasta(Isim, Yas)).

% Yaşı 65 üstü olanları riskli olarak işaretler
risk_degerlendir(Isim) :-
    hasta(Isim, Yas),
    Yas >= 65,
    assert(riskli(Isim)).

% Hasta kaydı silinir
hasta_sil(Isim) :-
    retract(hasta(Isim, _)),
    retractall(riskli(Isim)).
```

Bu kodda `:- dynamic hasta/2.` bildirimi önemlidir. Prolog’a bu ilişkinin çalışma zamanında değiştirilebileceğini söyler. `hasta_ekle(ayse, 70).` çağrıldığında belleğe yeni bir gerçek eklenir. Ardından `risk_degerlendir(ayse).` çalıştırılırsa sistem Ayşe için `riskli(ayse).` bilgisini üretir. Yani program yalnızca veri saklamaz; yeni veriye göre kendi bilgi tabanını genişletir.

Ancak burada tatlı bir tehlike var: Kontrolsüz `assert` kullanımı bilgi tabanını çorba yapabilir. Aynı gerçeği defalarca eklemek, eski bilgiyi silmeden yenisini yazmak veya çelişkili kuralları birlikte tutmak çıkarımları bozabilir. Örneğin hem `aktif(kullanici1)` hem de `pasif(kullanici1)` varsa sistemin ne yapacağı tasarıma bağlıdır. Bu yüzden dinamik sistemlerde tutarlılık kuralları gerekir. Mantıksal olarak bir çelişkiyi şöyle düşünebiliriz: $aktif(x) \land pasif(x) \rightarrow \bot$. Buradaki $\bot$, kabul edilemez durumu temsil eder.

| Komut | Görev | Tipik Kullanım | Dikkat Edilecek Nokta |
|---|---|---|---|
| `assert/1` | Bilgi ekler | Yeni olay, kullanıcı tercihi | Tekrarlı kayıt oluşabilir |
| `retract/1` | İlk eşleşen bilgiyi siler | Geçersizleşen durum | Yanlış eşleşme silinebilir |
| `retractall/1` | Tüm eşleşmeleri siler | Temizlik, sıfırlama | Fazla geniş desen risklidir |
| `dynamic/1` | Değişebilir ilişki tanımlar | Dinamik predikatlar | Bildirilmezse hata alınabilir |

Daha güvenli bir güncelleme için önce eski bilgiyi temizleyip sonra yenisini eklemek yaygın bir taktiktir:

```prolog
:- dynamic konum/2.

% Bir varlığın konumunu günceller
konum_guncelle(Nesne, YeniKonum) :-
    retractall(konum(Nesne, _)),
    assert(konum(Nesne, YeniKonum)).

% Örnek sorgu:
% konum_guncelle(robot1, depo).
% konum(robot1, Nerede).
```

Burada amaç robotun aynı anda hem mutfakta hem depoda görünmesini engellemektir. Önce robotun eski konumu silinir, ardından güncel konumu eklenir. Bu desen, oyun karakterleri, IoT cihazları veya oturum yönetimi gibi birçok alanda işe yarar.

Sonuç olarak dinamik veri tabanı yönetimi, programa hafıza ve refleks kazandırır. `assert` ile öğrenen, `retract` ile unutan sistemler kurabiliriz. Ama her güçlü araç gibi bunun da disiplini vardır: değiştirilebilir predikatları açıkça tanımla, tutarsızlıkları engelle, eski bilgiyi temizle ve güncelleme kurallarını sade tut. Böylece programın sadece çalışan değil, yaşayan bir bilgi sistemine dönüşür.
