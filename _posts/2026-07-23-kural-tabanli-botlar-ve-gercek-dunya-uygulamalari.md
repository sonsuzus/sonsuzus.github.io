---
layout: post
title: "Kural Tabanlı Botlar ve Gerçek Dünya Uygulamaları"
math: true
categories: 
  - Bilgi
tags: 
  - kural tabanlı botlar
  - doğal dil işleme
  - karar destek sistemleri
---

Kural tabanlı botlar, yapay zekanın sihirli değneği gibi görünmeyebilir; ama gerçek dünyada birçok otomasyonun sessiz kahramanıdır. Bir metni okuyup sınıflandıran müşteri destek botu, başvuru formundaki riskleri işaretleyen karar destek sistemi veya moderasyon kuyruğuna mesaj düşüren filtreler çoğu zaman öğrenilmiş devasa modellerden önce mantık, koşul ve iyi tasarlanmış kurallar üzerine kurulur.

``

Temel fikir oldukça nettir: **Eğer belirli koşullar sağlanıyorsa, belirli bir eylem çalıştırılır.** Bu yapı programlamadaki `if-else` mantığının daha sistematik hâlidir. Bir kuralı basitçe $kosul -> eylem$ şeklinde düşünebiliriz. Örneğin bir mesajda hem acil kelimesi geçiyor hem de sipariş numarası bulunuyorsa, bot bunu öncelikli destek talebi olarak etiketleyebilir.

Kural tabanlı sistemlerin gücü, teorik olarak üç ana kavrama dayanır: sembolik temsil, mantıksal çıkarım ve karar akışı. Sembolik temsil, gerçek dünyadaki karmaşık ifadeleri daha işlenebilir parçalara ayırır. Mesela kullanıcının yazdığı metin; kelimeler, niyetler, anahtar ifadeler ve sayısal sinyaller olarak temsil edilir. Mantıksal çıkarım ise bu sinyallerden sonuç üretir: $skor = w1 * aciliyet + w2 * negatiflik - w3 * belirsizlik$ gibi basit bir formül bile karar destek sistemlerinde çok işe yarar.

| Yaklaşım | Avantaj | Dezavantaj | Uygun Senaryo |
|---|---|---|---|
| Kural tabanlı | Açıklanabilir, hızlı, kontrol edilebilir | Kurallar çoğalınca bakım zorlaşır | SSS botları, filtreleme, iş akışı |
| Makine öğrenmesi | Örüntüleri veriden öğrenir | Veri ister, açıklaması zor olabilir | Büyük ölçekli sınıflandırma |
| Hibrit sistem | Hem kontrol hem esneklik sağlar | Tasarım karmaşıktır | Kurumsal karar destek sistemleri |

Metin işleyen bir bot geliştirirken ilk adım, metni normalize etmektir. Büyük-küçük harf farkı, noktalama işaretleri ve gereksiz boşluklar kararları bozabilir. Ardından anahtar kelime, desen veya bağlam sinyalleri çıkarılır. Burada düzenli ifadeler, sözlükler ve puanlama fonksiyonları devreye girer.

Aşağıdaki örnek, müşteri destek mesajlarını basit kurallarla sınıflandırır. Kodun amacı; metindeki sinyalleri analiz edip destek ekibine hangi kuyruğa yönlendirme yapılacağını göstermektir.

```python
import re

RULES = [
    {
        'name': 'Acil sipariş problemi',
        'keywords': ['acil', 'gelmedi', 'kargo'],
        'queue': 'oncelikli_destek',
        'score': 8
    },
    {
        'name': 'İade talebi',
        'keywords': ['iade', 'geri göndermek', 'memnun değilim'],
        'queue': 'iade_ekibi',
        'score': 6
    },
    {
        'name': 'Fatura sorunu',
        'keywords': ['fatura', 'vergi', 'adres'],
        'queue': 'muhasebe',
        'score': 5
    }
]

def normalize(text):
    return re.sub(r'\s+', ' ', text.lower()).strip()

def classify(message):
    text = normalize(message)
    results = []

    for rule in RULES:
        hit_count = sum(1 for word in rule['keywords'] if word in text)
        if hit_count > 0:
            results.append({
                'rule': rule['name'],
                'queue': rule['queue'],
                'final_score': rule['score'] + hit_count
            })

    if not results:
        return {'queue': 'genel_destek', 'reason': 'Eşleşen kural yok'}

    return max(results, key=lambda item: item['final_score'])

print(classify('Kargom gelmedi, acil destek istiyorum.'))
```

Bu örnekte bot, makine öğrenmesi yapmıyor; fakat kararını açıklayabiliyor. Neden öncelikli destek kuyruğu seçildi? Çünkü metinde acil ve kargo gibi sinyaller bulundu. Gerçek dünyada bu açıklanabilirlik çok değerlidir. Özellikle finans, sağlık, hukuk ve insan kaynakları gibi alanlarda sistemin sadece karar vermesi değil, kararın gerekçesini sunması da gerekir.

| Kural Türü | Örnek | Kullanım Amacı |
|---|---|---|
| Anahtar kelime | Şifre, ödeme, iade | Hızlı niyet yakalama |
| Desen tabanlı | Sipariş no: 12345 | Yapısal bilgi çıkarma |
| Puanlama | Risk skoru > 70 | Önceliklendirme |
| Engelleme | Yasaklı kelime listesi | Moderasyon |

Ancak kural tabanlı botların karanlık tarafı da vardır: kural patlaması. Her yeni istisna için yeni bir kural yazıldığında sistem bir süre sonra spagettiye dönebilir. Bu yüzden kurallar kategorilere ayrılmalı, öncelik değerleri net tanımlanmalı ve çakışma yönetimi yapılmalıdır. Örneğin iki kural aynı anda çalışıyorsa en yüksek skor mu seçilecek, yoksa kritik etiket her zaman üstün mü gelecek? Bu kararlar baştan tasarlanmalıdır.

İyi bir mimaride kurallar kodun içine gömülmek yerine JSON, YAML veya veritabanında saklanabilir. Böylece yazılımcı olmayan alan uzmanları da kuralları güncelleyebilir. Ayrıca her karar için günlük kaydı tutulmalıdır: hangi metin geldi, hangi kurallar tetiklendi, sonuç ne oldu? Bu kayıtlar sistemin iyileştirilmesi için altın madeni gibidir.

Sonuç olarak kural tabanlı botlar, teorik mantık ile pratik yazılım mühendisliğinin eğlenceli buluşma noktasıdır. Doğru normalize edilmiş metin, iyi tasarlanmış koşullar, puanlama mantığı ve açıklanabilir karar akışı birleştiğinde küçük ama güçlü otomasyonlar ortaya çıkar. Büyük yapay zeka modellerinin çağında bile, bazen en iyi çözüm hâlâ şudur: açık, okunabilir ve test edilebilir bir kural.
