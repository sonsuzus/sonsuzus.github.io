---
layout: post
title: "Dosya Okuma ve Yazma İşlemleri: Ham Metinden Kalıcı Sonuçlara"
math: true
categories: 
  - Program
tags: 
  - dosya işlemleri
  - python
  - veri işleme
---

Bir programın dış dünyayla tokalaşmasının en klasik yolu dosyalardır. Kullanıcıdan gelen ham metinler, log kayıtları, CSV benzeri raporlar veya analizden sonra üretilen sonuç belgeleri; hepsi dosya okuma ve yazma işlemleriyle sisteme girer ya da sistemden çıkar. Kısacası dosya işlemleri, bellekte uçuşan veriyi kalıcı ve paylaşılabilir bilgiye dönüştüren köprüdür.
``
Dosya okuma ve yazma mantığını anlamak için önce iki temel kavramı ayıralım: **bellek** ve **kalıcı depolama**. Bellek, program çalışırken hızlıca eriştiğimiz geçici alandır. Dosya sistemi ise program kapansa bile verinin yaşamaya devam ettiği yerdir. Bir analiz programı düşünelim: Ham metni diskteki `veriler.txt` dosyasından okur, bellekte işler, sonra sonuçları `rapor.txt` dosyasına yazar.

Teorik olarak bu akış şöyle özetlenebilir:

$$Dosya \rightarrow Okuma \rightarrow Bellek \rightarrow İşleme \rightarrow Yazma \rightarrow Dosya$$

Dosya işlemlerinde en önemli noktalardan biri **mod** seçimidir. Bir dosyayı açarken programa niyetimizi söyleriz: okuyacak mıyız, sıfırdan mı yazacağız, yoksa sonuna mı ekleyeceğiz?

| Mod | Anlamı | Dosya Yoksa | Var Olan İçerik |
|---|---|---:|---|
| `r` | Okuma | Hata verir | Korunur |
| `w` | Yazma | Oluşturur | Siler, baştan yazar |
| `a` | Ekleme | Oluşturur | Sonuna ekler |
| `r+` | Okuma + yazma | Hata verir | Korunabilir ama dikkat ister |

Burada küçük ama kritik bir formül de performans için işimize yarar:

$$T = \frac{B}{t}$$

Bu formülde $T$ aktarım hızını, $B$ okunan/yazılan veri boyutunu, $t$ ise geçen süreyi ifade eder. Büyük dosyalarda tüm içeriği tek hamlede belleğe almak yerine satır satır okumak, belleği daha verimli kullanır.

Aşağıdaki Python örneği, dışarıdan sağlanan ham metin dosyasını satır satır okuyup basit bir analiz yapar: her satırdaki kelime sayısını hesaplar.

```python
from pathlib import Path

girdi_yolu = Path('ham_metin.txt')
sonuclar = []

with girdi_yolu.open('r', encoding='utf-8') as dosya:
    for satir_no, satir in enumerate(dosya, start=1):
        temiz_satir = satir.strip()
        kelimeler = temiz_satir.split()
        sonuclar.append((satir_no, len(kelimeler)))

print(sonuclar)
```

Bu kodda `with` kullanımı önemlidir. Çünkü dosyayı açtıktan sonra kapatmayı unutmak, özellikle uzun çalışan programlarda kaynak sızıntılarına yol açabilir. `with` bloğu bittiğinde dosya otomatik kapanır; yani programcıya küçük bir güvenlik kemeri takar.

Okuma stratejileri arasında da fark vardır:

| Yöntem | Kullanım | Avantaj | Risk |
|---|---|---|---|
| `read()` | Tüm dosyayı okur | Basit ve hızlıdır | Büyük dosyada belleği zorlar |
| `readline()` | Tek satır okur | Kontrollüdür | Döngü yönetimi gerekir |
| Dosya üzerinde döngü | Satır satır okur | Büyük dosyalar için idealdir | Satır bazlı işlem varsayar |

Şimdi analiz sonuçlarını kalıcı bir belgeye aktaralım. Bu kez amacımız bellekteki `sonuclar` listesini okunabilir bir rapora dönüştürmek.

```python
from pathlib import Path

cikti_yolu = Path('kelime_raporu.txt')

with cikti_yolu.open('w', encoding='utf-8') as rapor:
    rapor.write('Satır Bazlı Kelime Sayısı Raporu\n')
    rapor.write('-------------------------------\n')

    for satir_no, kelime_sayisi in sonuclar:
        rapor.write(f'Satır {satir_no}: {kelime_sayisi} kelime\n')
```

Burada `w` modu dosyayı baştan oluşturur. Eğer aynı rapora her analizden sonra yeni sonuç eklemek isteseydik `a` modunu kullanırdık. Örneğin günlük analiz sistemlerinde `append` yaklaşımı çok yaygındır; çünkü geçmiş kayıtların silinmesi istenmez.

Dosya işlemlerinde dikkat edilmesi gereken bir diğer konu **karakter kodlamasıdır**. Türkçe metinlerde `ç`, `ğ`, `ı`, `ö`, `ş`, `ü` gibi karakterlerin bozulmaması için çoğu zaman `encoding='utf-8'` belirtmek gerekir. Aksi halde dosyanız açılır ama metin ninja gibi kılık değiştirip `Ã§` benzeri garip karakterlere dönüşebilir.

Son olarak, sağlam programlar sadece mutlu yolu değil, hata ihtimallerini de düşünür. Dosya bulunamayabilir, yetki olmayabilir veya disk dolu olabilir. Bu yüzden kritik işlemlerde `try-except` kullanmak mantıklıdır.

```python
try:
    with open('ham_metin.txt', 'r', encoding='utf-8') as dosya:
        icerik = dosya.read()
except FileNotFoundError:
    print('Dosya bulunamadı. Lütfen dosya yolunu kontrol edin.')
except PermissionError:
    print('Bu dosyaya erişim izniniz yok.')
```

Özetle dosya okuma, dışarıdaki ham veriyi programın anlayacağı alana taşır; dosya yazma ise programın ürettiği bilgiyi kalıcı hale getirir. İyi seçilmiş mod, doğru kodlama, satır satır işleme ve hata kontrolü birleştiğinde dosya sistemi artık korkutucu bir karanlık klasör değil, verinizin düzenli arşivi olur.
