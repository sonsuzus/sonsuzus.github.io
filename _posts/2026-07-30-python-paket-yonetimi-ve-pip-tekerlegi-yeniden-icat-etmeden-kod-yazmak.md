---
layout: post
title: "Python Paket Yönetimi ve PIP: Tekerleği Yeniden İcat Etmeden Kod Yazmak"
math: true
categories: 
  - Bilgi
tags: 
  - Python
  - PIP
  - Paket Yönetimi
---

Bir projede HTTP isteği göndermek, Excel dosyası okumak veya görsel işlemek istediğinizi düşünün. Bunların tamamını sıfırdan geliştirmek mümkün olsa da pek mantıklı değildir. Python modülleri ve paket yönetimi, başkalarının test edilmiş çözümlerini projemize güvenli ve düzenli biçimde dahil etmemizi sağlar. Böylece enerjimizi tekerleği yeniden icat etmeye değil, gerçekten özgün problemlere ayırabiliriz.
``
## Modül, paket ve kütüphane nedir?

Python'da `.py` uzantılı ve yeniden kullanılabilir kod içeren her dosya bir **modül** olarak düşünülebilir. Birden fazla modülün belirli bir dizin yapısında bir araya gelmesiyle **paket** oluşur. Kütüphane ise genellikle belli bir problemi çözmek için hazırlanmış modül ve paketler bütünüdür.

Bir modülü kullanmanın temel yolu `import` ifadesidir:

```python
import math

yaricap = 5
alan = math.pi * yaricap ** 2
print(alan)
```

Bu kodda Python ile birlikte gelen `math` modülü sisteme dahil edilir. Dairenin alanı $A = pi r^2$ formülüyle hesaplanır. Buradaki önemli ayrıntı, `import` işleminin bir paketi internetten indirmemesidir; yalnızca mevcut Python ortamında bulunan modülü programa yükler.

## Standart kütüphane mi, harici paket mi?

Python birçok kullanışlı araçla beraber gelir. Ancak her ihtiyacın standart kütüphanede karşılanması beklenemez.

| Özellik | Standart kütüphane | Harici paket |
|---|---|---|
| Kurulum | Python ile gelir | Genellikle PIP ile kurulur |
| Örnek | `json`, `math`, `datetime` | `requests`, `pandas`, `numpy` |
| İnternet gereksinimi | Yok | İlk kurulumda çoğunlukla var |
| Güncelleme | Python sürümüne bağlı | Bağımsız güncellenebilir |
| Risk | Görece düşük | Kaynak ve sürüm incelenmelidir |

Harici paketlerin büyük bölümü **PyPI** adlı Python Paket İndeksi üzerinde yayımlanır. **PIP**, bu paketleri PyPI gibi depolardan indirip kuran paket yöneticisidir.

## PIP ile paket kurmak

Önce PIP'in kullanılabilir olduğunu doğrulayabiliriz:

```bash
python -m pip --version
```

Bir HTTP istemcisi olan `requests` paketini kurmak için şu komut kullanılır:

```bash
python -m pip install requests
```

Ardından paket kod içinde içe aktarılabilir:

```python
import requests

yanit = requests.get("https://example.com", timeout=10)
print(yanit.status_code)
```

`timeout` değeri, isteğin sonsuza kadar beklemesini önler. Burada PIP kurulumu gerçekleştirirken `import`, kurulmuş paketin özelliklerini çalışan programa dahil eder.

## Sürüm yönetimi neden önemlidir?

Paketler zamanla değişir. Yeni bir sürüm eski fonksiyonları kaldırabilir veya davranışlarını değiştirebilir. Bu nedenle sürüm kısıtları kullanılabilir:

```bash
python -m pip install "requests>=2.31,<3.0"
```

Bu ifade, en az 2.31 olan fakat 3.0'dan küçük bir sürüm ister. Bir projenin doğrudan bağımlılık sayısı $D$, bu paketlerin getirdiği geçişli bağımlılıkların sayısı $G$ ise toplam bağımlılık yaklaşık olarak $T = D + G$ şeklinde düşünülebilir. Proje büyüdükçe sürümleri kayıt altında tutmak daha kritik hâle gelir.

```bash
python -m pip freeze > requirements.txt
python -m pip install -r requirements.txt
```

İlk komut ortamda kurulu paketleri dosyaya yazar; ikinci komut aynı bağımlılıkları başka bir ortamda kurar.

## Sanal ortamla projeleri ayırmak

Her projenin paketleri ve sürüm ihtiyaçları farklı olabilir. Bir proje `Django 4` isterken diğeri `Django 5` kullanabilir. Paketleri sistem geneline kurmak bu nedenle çakışma çıkarabilir.

```bash
python -m venv .venv
```

Sanal ortam Windows'ta `.venv\Scripts\activate`, macOS ve Linux'ta `source .venv/bin/activate` komutuyla etkinleştirilir. Bundan sonra yapılan PIP kurulumları yalnızca ilgili projeyi etkiler.

## Güvenli kullanım için kısa kontrol listesi

- Paketin adını yazım hatalarına karşı kontrol edin.
- Güncel, belgelenmiş ve aktif paketleri tercih edin.
- Sürümleri sabitleyin veya anlamlı aralıklarla sınırlandırın.
- Kullanılmayan bağımlılıkları kaldırın.
- `requirements.txt` ya da `pyproject.toml` dosyasını sürüm kontrolüne ekleyin.
- Kaynağı belirsiz paketleri sırf adı havalı diye kurmayın.

Doğru paket yönetimi yalnızca birkaç komut ezberlemek değildir; yeniden üretilebilir, güvenli ve bakımı kolay projeler tasarlama alışkanlığıdır. PIP alet çantanız, sanal ortam çalışma masanız, paketler de daha önce üretilmiş kaliteli parçalardır. İyi bir geliştirici her vidayı kendisi üretmez; doğru parçayı seçip doğru yere takar.
