---
layout: post
title: "Gerçek Zamanlı Veri Akışı ve Apache Kafka ile Kayıpsız İşleme"
math: true
categories: 
  - Bilgi
tags: 
  - Apache Kafka
  - streaming
  - gerçek zamanlı veri
---

Bir web sitesindeki tıklamalar, sunucu logları veya fabrikadaki sıcaklık sensörleri kimsenin “Kaydet” düğmesine basmasını beklemez. Veriler saniyede yüzlerce, hatta milyonlarca olay hâlinde kesintisiz akar. Gerçek zamanlı veri akışı, bu olayları oluştukları anda yakalayıp güvenilir biçimde taşıma ve gecikmeyi mümkün olduğunca düşük tutarak işleme yaklaşımıdır. Apache Kafka ise bu yoğun veri trafiğinin ortasında çalışan dayanıklı bir dijital konveyör bandı gibidir.

``

## Streaming neden farklıdır?

Geleneksel toplu işlemede veriler önce biriktirilir, ardından belirli aralıklarla işlenir. Streaming sistemlerinde ise teorik olarak sonu bulunmayan bir olay dizisi vardır:

$$S = \{e_1, e_2, e_3, \ldots\}$$

Her olayın bir değeri, zaman damgası ve çoğunlukla anahtarı bulunur. Sistem, olayları bekletmeden işlerken ani trafik artışlarına da dayanmalıdır. Üretim hızı $P$, tüketim hızı $C$ ile gösterilirse sürdürülebilir çalışma için genel beklenti şudur:

$$C \geq P$$

Eğer $P > C$ olursa olaylar hemen kaybolmak zorunda değildir; Kafka bunları diskte tutar. Ancak tüketicinin geride kaldığı miktar, yani **consumer lag**, büyür. Bu tamponlama yeteneği üreticilerle tüketicilerin birbirinden bağımsız ölçeklenmesini sağlar.

| Özellik | Batch işleme | Streaming işleme |
|---|---|---|
| Veri yapısı | Sonlu veri kümesi | Sürekli olay dizisi |
| Gecikme | Dakika veya saat | Milisaniye veya saniye |
| Kullanım | Günlük rapor | Anlık alarm, dolandırıcılık tespiti |
| Zorluk | Büyük hacimli hesaplama | Sıralama, tekrar ve gecikmiş olaylar |

## Kafka’nın temel parçaları

Kafka’da üreticiler (**producer**) olayları **topic** adı verilen mantıksal kanallara gönderir. Topic’ler ölçeklenebilmek için **partition** bölümlerine ayrılır. Her partition yalnızca sonuna ekleme yapılan sıralı bir kayıttır. Olaylar silinmek yerine yapılandırılmış saklama süresi boyunca diskte korunur.

Bir olayın anahtarı aynı kaldığında genellikle aynı partition seçilir. Böylece örneğin aynı sensöre ait ölçümlerin sırası korunabilir. Fakat Kafka tüm topic genelinde mutlak sıra garantisi vermez; garanti partition düzeyindedir.

| Kavram | Görevi | Benzetme |
|---|---|---|
| Producer | Olay yayımlar | Kargo gönderen kişi |
| Topic | Olayları sınıflandırır | Kargo hattı |
| Partition | Paralellik ve sıralama sağlar | Ayrı taşıma şeridi |
| Broker | Veriyi saklayan Kafka sunucusudur | Dağıtım merkezi |
| Consumer group | İş yükünü paylaşır | Teslimat ekibi |
| Offset | Okuma konumunu belirtir | Kitap ayracı |

## Basit bir sensör üreticisi

Aşağıdaki Python kodu, sıcaklık ölçümlerini JSON olarak Kafka’ya yollar. `sensor_id` anahtar olarak kullanıldığı için aynı sensörün olayları aynı partition’da sıralanabilir.

```python
import json
import random
import time
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda value: json.dumps(value).encode("utf-8")
)

while True:
    event = {
        "sensor_id": "sensor-42",
        "temperature": round(random.uniform(20, 35), 2),
        "timestamp": time.time()
    }
    producer.send(
        "temperature-events",
        key=event["sensor_id"].encode("utf-8"),
        value=event
    )
    time.sleep(1)
```

`send` işlemi asenkrondur; yüksek performans için olaylar paketlenebilir. Kritik sistemlerde `acks="all"` kullanmak, lider ve gerekli replikalar doğrulamadan gönderimi başarılı saymamak açısından önemlidir.

## Kayıpsızlık gerçekten ne demek?

Kafka veriyi çoğaltarak broker arızalarına karşı korur, fakat uçtan uca güvenilirlik yalnızca Kafka ayarı değildir. Üretici tekrar denemeleri, `acks`, replikasyon faktörü ve tüketicinin offset yönetimi birlikte tasarlanmalıdır.

- **At-most-once:** Olay en fazla bir kez işlenir; kayıp mümkündür.
- **At-least-once:** Kayıp önlenir, fakat tekrar işleme olabilir.
- **Exactly-once:** İşlem sonucu mantıksal olarak yalnızca bir kez uygulanır.

Pratikte `at-least-once` ve **idempotent** tüketiciler güçlü bir çözümdür. Aynı `event_id` ikinci kez geldiğinde veritabanı işlemi sonucu değiştirmiyorsa tekrarlar zararsızlaşır. Kafka Transactions ve Kafka Streams ise uygun senaryolarda exactly-once semantiğini destekler.

Sonuç olarak Kafka yalnızca hızlı bir mesaj kuyruğu değil; olayları kalıcı biçimde saklayan, yeniden oynatılabilir ve dağıtık bir olay günlüğüdür. Web loglarından sensör alarmlarına kadar sağlam bir streaming mimarisi; partition planı, lag takibi, replikasyon, şema yönetimi ve idempotent işleme birlikte düşünüldüğünde gerçekten güvenilir hâle gelir.
