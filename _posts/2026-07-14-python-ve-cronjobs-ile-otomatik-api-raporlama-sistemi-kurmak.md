---
layout: post
title: "Python ve Cronjobs ile Otomatik API Raporlama Sistemi Kurmak"
math: true
categories: 
  - Program
tags: 
  - python
  - cronjob
  - otomasyon
  - api
  - raporlama
---

Sunucunuzun her sabah siz kahvenizi almadan önce API'lerden veri çekip rapor hazırladığını hayal edin. İşte Python ve cronjobs ikilisi tam olarak bu küçük dijital asistanı kurmanızı sağlar: Python işi yapar, cron ise doğru zamanda düğmeye basar.
``
Cronjob, Unix/Linux sistemlerde belirli zamanlarda komut çalıştıran zamanlayıcıdır. Python ise API istekleri, veri işleme, dosya üretme ve e-posta gönderme gibi görevlerde oldukça rahattır. Bu ikiliyle örneğin her gün saat 09:00'da satış API'sinden veri çekebilir, toplam geliri hesaplayabilir ve CSV raporu oluşturabilirsiniz.

## Temel Mantık

Cron'u bir çalar saat, Python scriptini de o alarm çalınca mutfağa gidip kahve yapan robot gibi düşünebiliriz. Cron sadece zamanı bilir; işin detayını Python yapar. Matematiksel olarak periyodik bir görevi şöyle ifade edebiliriz: $T = n \times \Delta t$. Burada $\Delta t$ çalıştırma aralığı, $n$ tekrar sayısıdır. Örneğin 24 saat boyunca her 1 saatte bir çalışan görev için $T = 24 \times 1$ olur.

Raporlama tarafında ise genellikle bir özet değer hesaplarız. Örneğin günlük toplam satış: $R = \sum_{i=1}^{n} tutar_i$. Python bu toplamı API'den gelen JSON verisi üzerinden kolayca çıkarabilir.

| Bileşen | Görevi | Örnek |
|---|---|---|
| Cron | Zamanlama yapar | Her gün 09:00 |
| Python | Veriyi çeker ve işler | API isteği, CSV üretimi |
| API | Ham veri sağlar | Satış, stok, kullanıcı verisi |
| Rapor | Sonuçları sunar | CSV, JSON, e-posta |

## Python ile API'den Veri Çekme

Aşağıdaki örnek, sahte bir satış API'sinden veri çeker, toplam satış miktarını hesaplar ve günlük raporu CSV dosyasına yazar. Gerçek projelerde API anahtarını doğrudan koda yazmak yerine ortam değişkeni kullanmak daha güvenlidir.

```python
import csv
import os
from datetime import datetime
import requests

API_URL = 'https://api.example.com/sales'
API_KEY = os.getenv('SALES_API_KEY')

headers = {
    'Authorization': f'Bearer {API_KEY}'
}

response = requests.get(API_URL, headers=headers, timeout=20)
response.raise_for_status()

data = response.json()
items = data.get('sales', [])

total_amount = sum(item.get('amount', 0) for item in items)
report_date = datetime.now().strftime('%Y-%m-%d')

with open(f'report_{report_date}.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['date', 'sale_count', 'total_amount'])
    writer.writerow([report_date, len(items), total_amount])

print(f'Rapor hazır: {report_date}, toplam: {total_amount}')
```

Bu kodda `requests.get` API çağrısını yapar, `response.raise_for_status` hatalı HTTP durumlarında scriptin sessizce devam etmesini engeller. `sum` fonksiyonu ise gelen kayıtların `amount` alanlarını toplar. Yani küçük ama işlevsel bir raporlama hattı kurmuş oluruz.

## Cron İfadesini Okumak

Cron satırları beş zaman alanı ve bir komuttan oluşur:

```bash
# dakika saat gün ay haftanın_günü komut
0 9 * * * /usr/bin/python3 /home/app/reports/daily_report.py
```

Bu örnek her gün saat 09:00'da scripti çalıştırır. Yıldız karakteri tüm değerler anlamına gelir. Yani gün, ay ve haftanın günü fark etmez.

| Cron İfadesi | Anlamı |
|---|---|
| `*/15 * * * *` | Her 15 dakikada bir |
| `0 * * * *` | Her saatin başında |
| `0 9 * * *` | Her gün 09:00'da |
| `30 23 * * 5` | Her cuma 23:30'da |

Cron ayarlamak için terminalde şu komutu kullanabilirsiniz:

```bash
crontab -e
```

Ardından cron satırınızı ekleyip kaydedersiniz. Scriptin çalıştığından emin olmak için log yönlendirmesi yapmak akıllıca olur:

```bash
0 9 * * * /usr/bin/python3 /home/app/reports/daily_report.py >> /home/app/logs/report.log 2>&1
```

Buradaki `>>` çıktıyı log dosyasına ekler, `2>&1` ise hata mesajlarını da aynı dosyaya gönderir. Böylece sorun çıktığında dedektif gibi terminal geçmişi aramak zorunda kalmazsınız.

## Dikkat Edilmesi Gerekenler

| Problem | Çözüm |
|---|---|
| Ortam değişkeni cron içinde görünmez | Crontab içinde değişken tanımlayın veya `.env` okuyun |
| Script elle çalışır ama cron'da çalışmaz | Mutlak dosya yolları kullanın |
| API bazen cevap vermez | Timeout, retry ve hata loglama ekleyin |
| Sunucu saat dilimi farklıdır | `timedatectl` ile timezone kontrol edin |

Sonuç olarak Python ve cronjobs, düşük maliyetli ama güçlü bir otomasyon altyapısı sunar. Büyük bir veri platformu kurmadan önce, basit bir script ve iyi ayarlanmış bir cron satırıyla günlük raporlarınızı otomatikleştirebilirsiniz. Küçük başlar, loglarınızı izler, hata yönetimini güçlendirirseniz bu yapı zamanla güvenilir bir mini veri operasyonuna dönüşür.
