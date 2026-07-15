---
layout: post
title: "Python ile Webhook Entegrasyonları: Sosyal Medyadan Otomatik Konu Açma"
math: true
categories: 
  - Proje
tags: 
  - python
  - webhook
  - otomasyon
  - api
---

Sosyal medyada biri markanızdan bahsettiğinde, yeni bir gönderi paylaştığında veya belirli bir etiketi kullandığında başka bir sitede otomatik konu açıldığını düşünün. İşte webhook entegrasyonları tam olarak bu küçük dijital domino taşlarını devirir: bir olay olur, Python dinler, doğrular, işler ve hedef sisteme aksiyon aldırır.
``
Webhook, klasik API sorgulamasının tersine çalışan bir bildirim mekanizmasıdır. Normalde siz API’ye sürekli “Yeni bir şey var mı?” diye sorarsınız; buna polling denir. Webhook’ta ise platform size “Bir şey oldu, al sana veri!” der. Bu yaklaşım hem daha hızlıdır hem de gereksiz istek trafiğini azaltır.

Basit akış şöyledir:

1. Sosyal medya platformunda olay gerçekleşir.
2. Platform, sizin belirlediğiniz URL’ye HTTP POST isteği gönderir.
3. Python uygulamanız imzayı ve veriyi doğrular.
4. Olay türüne göre hedef sitede konu açılır.
5. Sonuç loglanır, hata varsa tekrar deneme kuyruğuna alınır.

Teorik olarak bir webhook sistemini şu fonksiyon gibi düşünebiliriz:

$$f(event) = action$$

Burada $event$ sosyal medya hareketini, $action$ ise başka sitede konu açma işlemini temsil eder. Ancak gerçek dünyada iş biraz daha baharatlıdır: güvenlik, tekrar eden istekler, zaman aşımı, API limitleri ve veri eşleme gibi konular devreye girer.

| Yaklaşım | Nasıl Çalışır? | Avantaj | Dezavantaj |
|---|---|---|---|
| Polling | Belirli aralıklarla API sorgulanır | Kurulumu basit | Gereksiz trafik ve gecikme |
| Webhook | Olay olunca platform size istek atar | Anlık ve verimli | Güvenlik ve erişilebilirlik ister |
| Kuyruklu Webhook | Olay kuyruğa alınır, sonra işlenir | Dayanıklı ve ölçeklenebilir | Ek altyapı gerekir |

Güvenlik tarafında en önemli noktalardan biri imza doğrulamadır. Platform genellikle gövde verisini gizli anahtarla imzalar. Siz de aynı hesabı yapıp gelen imzayla karşılaştırırsınız:

$$signature = HMAC_{SHA256}(secret, payload)$$

Eğer imzalar eşleşmiyorsa istek reddedilmelidir. Çünkü internete açık bir endpoint, robotların ve meraklı kişilerin favori oyun alanıdır.

Aşağıdaki örnek Flask ile yazılmış orta düzey bir webhook alıcısıdır. Gelen olayı doğrular, aynı olayın iki kez işlenmesini engeller ve hedef foruma konu açmak için örnek bir POST isteği gönderir.

```python
import os
import hmac
import hashlib
import requests
from flask import Flask, request, abort, jsonify

app = Flask(__name__)

SECRET = os.environ.get('WEBHOOK_SECRET', 'dev-secret')
FORUM_API = os.environ.get('FORUM_API', 'https://forum.example.com/api/topics')
FORUM_TOKEN = os.environ.get('FORUM_TOKEN', 'demo-token')

processed_events = set()

def verify_signature(payload, received_signature):
    expected = hmac.new(
        SECRET.encode(),
        payload,
        hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(expected, received_signature or '')

def create_topic(event):
    username = event.get('username', 'bilinmeyen')
    text = event.get('text', '')
    platform = event.get('platform', 'sosyal medya')

    data = {
        'title': f'{platform} üzerinde yeni hareket: {username}',
        'body': f'Kullanıcı: {username}\n\nİçerik:\n{text}',
        'category': 'Sosyal Medya'
    }

    headers = {
        'Authorization': f'Bearer {FORUM_TOKEN}'
    }

    response = requests.post(FORUM_API, json=data, headers=headers, timeout=10)
    response.raise_for_status()
    return response.json()

@app.post('/webhooks/social')
def social_webhook():
    payload = request.get_data()
    signature = request.headers.get('X-Signature')

    if not verify_signature(payload, signature):
        abort(401)

    event = request.get_json()
    event_id = event.get('id')

    if event_id in processed_events:
        return jsonify({'status': 'duplicate_ignored'})

    processed_events.add(event_id)

    if event.get('type') == 'mention':
        result = create_topic(event)
        return jsonify({'status': 'topic_created', 'result': result})

    return jsonify({'status': 'ignored'})
```

Bu kodda `processed_events` örnek amaçlı bellekte tutuluyor. Gerçek projede Redis, PostgreSQL veya benzeri kalıcı bir sistem kullanmak daha doğrudur. Çünkü uygulama yeniden başlarsa bellek sıfırlanır ve aynı olay tekrar konu açabilir. Bu probleme idempotency denir: aynı isteğin birden fazla kez gelmesi durumunda sistemin aynı sonucu üretmesi gerekir.

Veri eşleme de önemlidir. Sosyal medya olayı doğrudan forum konusuna dönüşmez; arada anlamlı bir çeviri katmanı gerekir.

| Webhook Alanı | Forum Alanı | Dönüşüm Mantığı |
|---|---|---|
| `username` | Konu başlığı | Hareketi yapan kişiyi belirtir |
| `text` | Konu içeriği | Paylaşım veya yorum metni eklenir |
| `platform` | Etiket | Kaynağın neresi olduğu anlaşılır |
| `created_at` | Zaman bilgisi | Konunun bağlamını güçlendirir |

Hata yönetimi tarafında üstel geri çekilme kullanabilirsiniz. Örneğin tekrar deneme süresi şu şekilde büyüyebilir:

$$delay = min(2^n, 300)$$

Burada $n$ deneme sayısıdır, üst sınır ise 300 saniyedir. Böylece hedef site kısa süreli çökerse sisteminiz panikle spam atmaz.

Sonuç olarak Python ile webhook entegrasyonu, sadece bir endpoint yazmaktan ibaret değildir. Güvenli doğrulama, idempotency, veri dönüştürme, loglama ve tekrar deneme stratejileriyle birleşince ortaya sosyal medya hareketlerini otomatik aksiyona dönüştüren sağlam bir tetikleyici mekanizma çıkar. Küçük başlar, sonra bir bakmışsınız forumunuz sosyal medyanın nabzını gerçek zamanlı tutan mini bir haber merkezine dönüşmüş!
