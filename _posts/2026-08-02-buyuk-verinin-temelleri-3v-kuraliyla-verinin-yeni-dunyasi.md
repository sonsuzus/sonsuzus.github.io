---
layout: post
title: "Büyük Verinin Temelleri: 3V Kuralıyla Verinin Yeni Dünyası"
math: true
categories: 
  - Bilgi
tags: 
  - Büyük Veri
  - 3V Kuralı
  - Veri Mühendisliği
---

Bir e-ticaret sitesindeki tıklamalar, akıllı saatlerin ölçtüğü nabız değerleri, sosyal medya paylaşımları ve fabrikalardaki sensör kayıtları… Modern dünyada veri yalnızca çoğalmıyor; hızlanıyor ve biçim değiştiriyor. **Büyük Veri (Big Data)**, tek başına “çok fazla veri” anlamına gelmez. Geleneksel sistemlerin makul süre ve maliyetle saklamakta, işleyip analiz etmekte zorlandığı veri kümelerini ve bu sorunu çözmek için geliştirilen yöntemleri ifade eder.
``
## Büyük Veri Neden “Büyük”tür?

Bir veri kümesinin büyüklüğü mutlak değildir. Dün büyük sayılan birkaç terabayt, bugün sıradan bir şirketin günlük üretimi olabilir. Bu nedenle Büyük Veri’yi yalnızca gigabayt veya petabayt üzerinden tanımlamak yanıltıcıdır. Asıl soru şudur: **Mevcut altyapı, veriyi kabul edilebilir sürede ve maliyetle işleyebiliyor mu?**

Basitleştirilmiş biçimde işleme süresini şöyle düşünebiliriz:

$$T \approx \frac{D}{R \times N} + O$$

Burada $D$ veri miktarını, $R$ tek bir düğümün işleme hızını, $N$ paralel çalışan düğüm sayısını, $O$ ise ağ iletişimi ve koordinasyon maliyetini temsil eder. Daha fazla makine eklemek teoride süreyi azaltır; ancak dağıtık sistemlerde koordinasyon bedeli nedeniyle kazanç doğrusal değildir.

## 3V Kuralı

Büyük Verinin doğasını açıklayan klasik model üç temel özelliğe dayanır: **Volume, Velocity ve Variety**.

| Boyut | Temel soru | Örnek | Oluşturduğu ihtiyaç |
|---|---|---|---|
| Volume | Ne kadar veri var? | Milyarlarca işlem kaydı | Dağıtık depolama ve paralel hesaplama |
| Velocity | Veri ne hızla geliyor? | Canlı ödeme hareketleri | Akış işleme ve düşük gecikme |
| Variety | Veri hangi biçimlerde? | JSON, video, tablo, metin | Esnek şema ve farklı veri modelleri |

### Volume: Hacim

Hacim, tek bir sunucunun disk ve işlem kapasitesini aşan veri miktarıdır. Geleneksel yaklaşım daha güçlü bir makine satın almak, yani **dikey ölçekleme** yapmaktır. Büyük Veri sistemleri ise çoğunlukla yeni makineler ekleyerek **yatay ölçekleme** uygular. Veriler parçalara ayrılır, farklı düğümlerde saklanır ve hata ihtimaline karşı çoğaltılır.

### Velocity: Hız

Bazı verilerin değeri zamanla hızla azalır. Bir kredi kartı dolandırıcılığını ertesi gün bulmak faydalıdır; işlemi gerçekleşirken yakalamak ise çok daha değerlidir. Bu nedenle toplu işleme yerine Kafka veya Pulsar gibi mesajlaşma altyapılarıyla beslenen gerçek zamanlı veri akışları kullanılır.

Saniyede gelen olay sayısı $\lambda$, sistemin işleyebildiği olay sayısı $\mu$ ise sürdürülebilir bir akış için genel beklenti şöyledir:

$$\lambda < \mu$$

Aksi durumda kuyruk sürekli büyür; gecikme artar ve sistem sonunda nefessiz kalır.

### Variety: Çeşitlilik

İlişkisel veritabanları düzenli satır ve sütunları sever. Oysa gerçek dünya CSV dosyaları, iç içe JSON belgeleri, fotoğraflar, loglar ve ses kayıtları üretir. Bu çeşitlilik; belge veritabanları, nesne depoları ve veri gölleri gibi esnek çözümleri gerekli kılar.

Aşağıdaki Python örneği, farklı yapıdaki olayları ortak bir işleme adımında normalize eder:

```python
from datetime import datetime

def normalize(event):
    return {
        "user_id": event.get("user_id", "anonymous"),
        "event_type": event.get("type", "unknown"),
        "timestamp": event.get("timestamp", datetime.now().isoformat()),
        "payload": event.get("payload", {})
    }
```

Bu fonksiyon eksik alanlara varsayılan değerler atar ve değişken kaynaklardan gelen kayıtları ortak bir biçime yaklaştırır. Gerçek sistemlerde buna doğrulama, şema sürümleme ve hatalı kayıt yönetimi de eklenir.

## Geleneksel Sistemden Yeni Nesil Mimariye

| Geleneksel yaklaşım | Büyük Veri yaklaşımı |
|---|---|
| Tek ve güçlü sunucu | Dağıtık makine kümesi |
| Önceden tanımlı katı şema | Gerektiğinde yorumlanan esnek şema |
| Periyodik toplu sorgular | Toplu ve gerçek zamanlı işleme |
| Merkezi hata noktası | Çoğaltma ve hata toleransı |

Hadoop, Spark, Kafka ve NoSQL sistemleri birer moda sözcük değil; 3V’nin oluşturduğu teknik baskılara verilmiş farklı cevaplardır. Bununla birlikte her proje Büyük Veri projesi değildir. Küçük bir veri kümesini karmaşık kümelerde çalıştırmak, roketle markete gitmeye benzer. Doğru yaklaşım; hacmi, gecikme beklentisini, veri biçimlerini ve maliyeti ölçerek en sade yeterli mimariyi seçmektir. Büyük Verinin özü teknoloji yığını değil, verinin doğasına uygun ölçeklenebilir düşünme biçimidir.
