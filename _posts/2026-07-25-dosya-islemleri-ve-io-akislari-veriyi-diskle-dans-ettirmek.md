---
layout: post
title: "Dosya İşlemleri ve I/O Akışları: Veriyi Diskle Dans Ettirmek"
math: true
categories: 
  - Bilgi
tags: 
  - dosya-islemleri
  - io-akislari
  - programlama
---

Bir programın dış dünyayla konuşmasının en eski ama en vazgeçilmez yolu dosyalardır. Günlük tutan bir uygulama, JSON ayarı okuyan bir oyun, CSV raporu üreten bir analiz aracı ya da büyük veri parçasını satır satır işleyen bir servis... Hepsi aslında aynı soruyu sorar: Veriyi güvenli, hızlı ve anlaşılır biçimde nasıl okur/yazarım?
``
Dosya işlemlerini sadece open-read-write-close ezberi gibi görmek büyük haksızlık olur. Arka planda işletim sistemi, disk, bellek, tamponlar ve akışlar arasında minik bir lojistik şirketi çalışır. Programımız dosyanın tamamını çoğu zaman doğrudan diske gidip almaz; işletim sistemi veriyi parça parça getirir, tamponlar, gerektiğinde diske yazar. Bu yüzden I/O yani Input/Output işlemlerinde performansın anahtarı, veriyi doğru boyutta ve doğru biçimde taşımaktır.

Temel kavram akıştır. Akış, verinin bir kaynaktan hedefe sıralı şekilde aktığı soyut kanaldır. Dosya, terminal, ağ soketi veya bellek tamponu birer akış gibi düşünülebilir. Matematiksel olarak okuma maliyetini basitçe şöyle düşünebiliriz: $T = \frac{B}{R} + L$. Burada $B$ taşınan bayt sayısı, $R$ aktarım hızı, $L$ ise gecikmedir. Küçük küçük binlerce okuma yapmak $L$ değerini tekrar tekrar ödetir; parçalı ama dengeli okumak genelde daha verimlidir.

| Yaklaşım | Ne zaman kullanılır? | Avantaj | Risk |
|---|---|---|---|
| Tüm dosyayı okumak | Küçük metinler, ayar dosyaları | Basit kod | Büyük dosyada bellek şişer |
| Satır satır okumak | Log, CSV, rapor | Bellek dostu | Rastgele erişim zayıf |
| Parça parça okumak | Büyük ikili dosya | Performans kontrolü | Kod biraz uzar |
| Yapılandırılmış okuma | JSON, YAML, CSV | Anlamlı veri modeli | Hatalı format patlatabilir |

Metin dosyalarında kodlama konusu da kritik. UTF-8 bugün varsayılan kahramanımızdır; Türkçe karakterlerin bozulmaması için dosya açarken kodlamayı açıkça belirtmek iyi alışkanlıktır. İkili dosyalarda ise karakter değil bayt okuruz; resim, ses veya sıkıştırılmış dosyalar bu kategoriye girer.

Aşağıdaki örnek, bir JSON ayar dosyasını okumayı; dosya yoksa varsayılan içerikle oluşturmayı gösterir:

```python
from pathlib import Path
import json

path = Path('ayarlar.json')

try:
    with path.open('r', encoding='utf-8') as f:
        config = json.load(f)
except FileNotFoundError:
    config = {'tema': 'dark', 'sayfa_boyutu': 20}
    with path.open('w', encoding='utf-8') as f:
        json.dump(config, f, ensure_ascii=False, indent=2)

print(config['tema'])
```

Burada `with` bloğu çok önemlidir. Dosyayı açar, iş bitince otomatik kapatır. Eğer istisna oluşursa bile kaynak sızıntısı yaşanmaz. Bu fikir genelde RAII veya context management mantığıyla açıklanır: Kaynağı kim aldıysa, düzenli biçimde geri bırakmalıdır.

Yazma işlemlerinde bir başka hassas konu atomikliktir. Program dosyayı yazarken çökerse yarım kalmış, bozuk bir dosya bırakabilir. Daha güvenli yaklaşım önce geçici dosyaya yazmak, sonra hedef dosyayla atomik olarak değiştirmektir.

```python
from pathlib import Path
import os, tempfile

def guvenli_yaz(hedef: Path, veri: str):
    klasor = hedef.parent
    with tempfile.NamedTemporaryFile('w', encoding='utf-8', dir=klasor, delete=False) as tmp:
        tmp.write(veri)
        tmp.flush()
        os.fsync(tmp.fileno())
        gecici_ad = tmp.name
    os.replace(gecici_ad, hedef)

guvenli_yaz(Path('rapor.txt'), 'Merhaba dosya sistemi!')
```

`flush()` veriyi kullanıcı alanı tamponundan işletim sistemine iter; `fsync()` ise diske yazılmasını daha güçlü biçimde talep eder. Her zaman gerekli değildir, çünkü pahalıdır; ama para transferi, kritik ayar veya işlem günlüğü gibi durumlarda değerlidir.

| İşlem | Kullanım | Performans notu |
|---|---|---|
| `read()` | Tam içerik | Küçük dosyada ideal |
| `readline()` | Tek satır | Etkileşimli akışlarda kullanışlı |
| `for line in f` | Satır satır | Log işlemede favori |
| `write()` | Metin/bayt yazma | Tamponlanır |
| `fsync()` | Diske zorlama | Güvenli ama yavaş |

Son olarak, dosya yolu güvenliğini unutmayın. Kullanıcıdan gelen dosya adını doğrudan birleştirmek path traversal gibi sorunlara yol açabilir. Ayrıca eşzamanlı çalışan programlarda kilitleme, izinler ve yarış koşulları düşünülmelidir. Kısacası dosya I/O, basit bir kapı kolu gibi görünür; ama arkasında bellek yönetimi, işletim sistemi çağrıları ve veri bütünlüğüyle dolu koca bir makine odası vardır. Doğru akış modelini seçerseniz, veriniz de programınız da huzurla yaşar.
