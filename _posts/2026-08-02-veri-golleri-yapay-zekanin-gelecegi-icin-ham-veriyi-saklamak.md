---
layout: post
title: "Veri Gölleri: Yapay Zekânın Geleceği İçin Ham Veriyi Saklamak"
math: true
categories: 
  - Bilgi
tags: 
  - veri gölü
  - yapay zeka
  - makine öğrenmesi
---

Bir şirketin ürettiği metinleri, görselleri, sensör kayıtlarını, uygulama loglarını ve ses dosyalarını henüz nasıl kullanacağını bilmeden sakladığını düşünün. İlk bakışta bu yaklaşım dijital istifçilik gibi görünebilir. Oysa doğru yönetilen bir **veri gölü (data lake)**, gelecekte geliştirilecek yapay zekâ modellerine zengin ve yeniden işlenebilir bir veri kaynağı sunar.

``

## Veri gölü tam olarak nedir?

Veri gölü; yapılandırılmış, yarı yapılandırılmış ve yapılandırılmamış verilerin özgün biçimleriyle merkezi bir depoda tutulduğu mimaridir. Bir ilişkisel veritabanına veri yazmadan önce tablo ve sütunları belirlemek gerekirken veri gölünde ham veri önce saklanabilir, kullanım şeması daha sonra oluşturulabilir. Bu yaklaşıma **schema-on-read**, yani “okuma sırasında şema” denir.

Örneğin aynı gölde şu veriler bulunabilir:

- JSON biçimindeki uygulama olayları,
- CSV satış kayıtları,
- Müşteri destek konuşmaları,
- Ürün ve güvenlik kamerası görselleri,
- IoT sensörlerinin zaman serileri,
- Sunucuların sıkıştırılmış log dosyaları.

Temel fikir basittir: Bugün gereksiz görünen bir kayıt, yarın dolandırıcılık tespiti veya talep tahmini modelinin en değerli özelliğine dönüşebilir.

## Veri ambarından farkı

| Özellik | Veri Gölü | Veri Ambarı |
|---|---|---|
| Veri biçimi | Ham ve çok çeşitli | Temizlenmiş, yapılandırılmış |
| Şema | Okuma sırasında | Yazma sırasında |
| Ana kullanıcı | Veri bilimci, ML mühendisi | Analist, yönetici |
| Tipik kullanım | Keşif, model eğitimi | Raporlama, iş zekâsı |
| Maliyet | Büyük ölçekte görece düşük | İşleme ve modelleme nedeniyle daha yüksek |

Bu iki sistem rakip olmak zorunda değildir. Veri gölü geniş bir hammadde alanı, veri ambarı ise düzenli rafları bulunan bir mağaza gibi düşünülebilir.

## Yapay zekâ hazırlığı neden önemlidir?

Bir modelin başarısı yalnızca algoritmaya bağlı değildir. Basitleştirilmiş biçimde model kalitesini şöyle düşünebiliriz:

$$Q \approx f(V, D, C, G)$$

Burada $V$ veri hacmini, $D$ çeşitliliği, $C$ veri doğruluğunu ve $G$ yönetişim kalitesini temsil eder. Milyarlarca kayıt toplamak tek başına yeterli değildir; hatalı etiketler, eksik zaman damgaları ve belirsiz erişim izinleri model performansını düşürür.

Yapay zekâya hazır bir veri gölünde veri kataloglama, sürümleme, köken takibi ve kalite ölçümü bulunmalıdır. Böylece bir özelliğin hangi kaynaktan geldiği ve hangi işlemlerden geçtiği izlenebilir. Özellikle kişisel veriler için maskeleme, şifreleme ve rol tabanlı erişim uygulanmalıdır.

## Basit bir veri alma örneği

Aşağıdaki Python kodu, JSON satırlarından oluşan ham olay dosyasını okuyup tarih bazlı Parquet dosyalarına dönüştürür. Parquet sütun tabanlı olduğu için analitik sorgularda daha az veri okunmasını sağlar.

```python
import pandas as pd

logs = pd.read_json('events.jsonl', lines=True)
logs['event_time'] = pd.to_datetime(logs['event_time'])
logs['event_date'] = logs['event_time'].dt.date

for date, partition in logs.groupby('event_date'):
    path = f'lake/events/date={date}/events.parquet'
    partition.to_parquet(path, index=False)
```

Bu işlem ham dosyayı tamamen silmek yerine genellikle ayrı bir **işlenmiş katmana** yazar. Böylece gerektiğinde özgün veriye dönülebilir.

## Gölü bataklığa çevirmemek

Katalogsuz, sahipsiz ve kalitesi ölçülmeyen bir veri gölü kısa sürede **data swamp**, yani veri bataklığı olur. Bunu önlemek için ham, temizlenmiş ve kullanıma hazır veriler ayrı katmanlarda tutulmalıdır. Her veri kümesine sahip, açıklama, saklama süresi ve kalite puanı atanmalıdır.

Sonuç olarak veri gölü, “her şeyi atalım, bir gün kullanırız” deposu değildir. Doğru mimari ve yönetişimle kurumun deney yapma hızını artıran stratejik bir yapay zekâ altyapısıdır. İyi korunan bir göl model ekiplerini besler; bakımsız bırakılan gölde ise en cesur veri bilimci bile yönünü kaybedebilir.
