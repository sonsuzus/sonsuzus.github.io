---
layout: post
title: "API Entegrasyonundan Telegram Botuna: Kural Tabanlı Otomasyon Rehberi"
math: true
categories: 
  - Proje
tags: 
  - API
  - Telegram Bot
  - Otomasyon
---

Bir uygulamanın dış dünyayla konuşmasını istiyorsanız kapısını API’lere açmanız gerekir. Hava durumu, döviz kuru, haberler veya sensör verileri gibi bilgiler bir web servisinden alınabilir; algoritmalarla işlenip Telegram botu üzerinden kullanıcıya sunulabilir. Böylece değişkenler, koşullar, döngüler ve fonksiyonlar gerçek hayatta çalışan eğlenceli bir otomasyon projesine dönüşür.
``

## API entegrasyonunun temel mantığı

API, iki yazılım arasında önceden belirlenmiş kurallarla iletişim kurulmasını sağlayan bir arayüzdür. İstemci bir **HTTP isteği** gönderir, sunucu ise çoğunlukla JSON biçiminde bir **yanıt** döndürür. Bir hava durumu servisine şehir adı gönderildiğinde sıcaklık, nem ve rüzgâr bilgisi alınması buna örnektir.

En sık kullanılan HTTP metotları şunlardır:

| Metot | Amaç | Örnek kullanım |
|---|---|---|
| GET | Veri okumak | Güncel sıcaklığı almak |
| POST | Yeni veri göndermek | Bir kayıt oluşturmak |
| PUT/PATCH | Veriyi güncellemek | Kullanıcı ayarını değiştirmek |
| DELETE | Veriyi silmek | Eski bildirimi kaldırmak |

Başarılı bir istek genellikle `200` durum koduyla cevaplanır. `404` kaynağın bulunamadığını, `401` kimlik doğrulamanın başarısız olduğunu, `429` ise istek sınırının aşıldığını belirtir.

Bir servisin güvenilirliğini basitçe başarı oranıyla ölçebiliriz:

$$Başarı\ Oranı = \frac{Başarılı\ İstek\ Sayısı}{Toplam\ İstek\ Sayısı} \times 100$$

Bu değer düşükse hata yönetimi, zaman aşımı ve yeniden deneme stratejileri geliştirilmelidir.

## Kural tabanlı bot nasıl karar verir?

Kural tabanlı botlar makine öğrenmesi kullanmak zorunda değildir. Kararlar açıkça tanımlanan `if`, `elif` ve `else` koşullarıyla verilir. Örneğin sıcaklık $30^\circ C$ üzerindeyse bot kullanıcıyı sıvı tüketmesi için uyarabilir; sıcaklık $10^\circ C$ altındaysa mont önerebilir.

| Yaklaşım | Avantaj | Dezavantaj |
|---|---|---|
| Kural tabanlı sistem | Şeffaf ve kolay test edilir | Çok sayıda kural karmaşa yaratır |
| Makine öğrenmesi | Karmaşık örüntüleri keşfedebilir | Veri ve eğitim süreci gerektirir |
| Hibrit sistem | Kontrol ile esnekliği birleştirir | Tasarımı daha zordur |

Kurallar fonksiyonlara ayrıldığında kodun okunabilirliği artar:

```python
def hava_mesaji(sicaklik):
    if sicaklik >= 30:
        return "Hava çok sıcak, su içmeyi unutma!"
    elif sicaklik <= 10:
        return "Bugün mont iyi bir fikir olabilir."
    return "Hava oldukça dengeli görünüyor."
```

Bu fonksiyon sayısal sıcaklığı alır ve kullanıcıya gösterilecek mesajı üretir. Böylece veri çekme ve karar verme görevleri birbirinden ayrılır.

## Telegram botuna API bağlamak

Python tarafında `requests` ile dış servise, `python-telegram-bot` ile Telegram API’sine bağlanabiliriz. Aşağıdaki örnek, `/hava Ankara` benzeri bir komutu işler:

```python
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

API_KEY = "HAVA_DURUMU_ANAHTARI"
BOT_TOKEN = "TELEGRAM_BOT_TOKEN"

async def hava(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Kullanım: /hava Ankara")
        return

    sehir = " ".join(context.args)
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": sehir, "appid": API_KEY, "units": "metric", "lang": "tr"}

    try:
        yanit = requests.get(url, params=params, timeout=10)
        yanit.raise_for_status()
        sicaklik = yanit.json()["main"]["temp"]
        mesaj = f"{sehir}: {sicaklik}°C\n{hava_mesaji(sicaklik)}"
    except requests.RequestException:
        mesaj = "Servise şu anda ulaşılamıyor. Biraz sonra tekrar dene."

    await update.message.reply_text(mesaj)

uygulama = Application.builder().token(BOT_TOKEN).build()
uygulama.add_handler(CommandHandler("hava", hava))
uygulama.run_polling()
```

`timeout`, uygulamanın sonsuza kadar yanıt beklemesini önler; `raise_for_status()` ise başarısız HTTP cevaplarını hataya dönüştürür. Gerçek projede anahtarlar kaynak koda yazılmamalı, ortam değişkenlerinde saklanmalıdır.

## Otomatik veri çekme ve sağlamlık

Aynı yapı zamanlayıcıyla çalıştırılarak fiyat takipçisi, haber özetleyici veya stok alarmı yapılabilir. Ancak servislerin kullanım koşullarına, istek limitlerine ve `robots.txt` kurallarına uyulmalıdır. Gereksiz istekleri azaltmak için önbellekleme uygulanabilir. Başarısız denemelerde bekleme süresini $t_n = 2^n$ saniye artıran üstel geri çekilme yöntemi de servisin yükünü azaltır.

Sonuçta API veriyi getirir, algoritmik kurallar anlamlandırır, Telegram ise sonucu kullanıcıya ulaştırır. Bu üçlü birleştiğinde küçük bir kod parçası, günün her saati çalışan kullanışlı bir dijital asistana dönüşür.
