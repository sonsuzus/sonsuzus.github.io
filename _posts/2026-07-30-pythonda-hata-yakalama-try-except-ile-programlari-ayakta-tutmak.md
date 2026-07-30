---
layout: post
title: "Python’da Hata Yakalama: Try-Except ile Programları Ayakta Tutmak"
math: true
categories: 
  - Bilgi
tags: 
  - Python
  - Hata Yakalama
  - İstisnalar
---

Bir programın doğru kodlanmış olması, çalışırken asla sorun yaşamayacağı anlamına gelmez. Kullanıcı sayı yerine metin girebilir, beklenen dosya silinmiş olabilir veya uzak sunucu kısa süreliğine yanıt vermeyebilir. Python’daki `try-except` yapısı, bu beklenmedik durumları programı aniden çökertmeden yakalamamızı ve kontrollü biçimde yönetmemizi sağlar.

``

## Hata ve istisna aynı şey mi?

Programlamada hatalar genel olarak iki gruba ayrılır. **Sözdizimi hataları**, kod Python kurallarına uygun yazılmadığında daha program başlamadan ortaya çıkar. **İstisnalar** ise sözdizimi doğru olan kod çalıştırılırken meydana gelir.

```python
# SyntaxError: Parantez kapatılmamış
print("Merhaba"

# ZeroDivisionError: Kod çalışırken oluşur
sonuc = 10 / 0
```

İkinci örnekte Python, matematiksel olarak tanımsız olan bir işlemle karşılaşır. Bölme işlemini $a / b$ şeklinde düşünürsek geçerli koşul $b \neq 0$ olmalıdır. Payda sıfır olduğunda Python bir `ZeroDivisionError` istisnası üretir.

| Durum | Ortaya çıkma zamanı | Örnek | `try-except` ile yakalanabilir mi? |
|---|---|---|---|
| Sözdizimi hatası | Program başlamadan önce | Eksik parantez | Genellikle hayır |
| Mantık hatası | Program çalışırken | Yanlış formül | Otomatik olarak hayır |
| İstisna | Çalışma zamanında | Sıfıra bölme | Evet |
| Sistem hatası | Kaynağa erişirken | Dosyanın bulunamaması | Evet |

## `try-except` nasıl çalışır?

Riskli kod `try` bloğuna yazılır. Python burada bir istisna üretirse normal akışı durdurur ve eşleşen `except` bloğuna geçer. İstisna çıkmazsa `except` bölümü atlanır.

```python
try:
    sayi = int(input("Bir sayı girin: "))
    sonuc = 100 / sayi
    print("Sonuç:", sonuc)
except ValueError:
    print("Lütfen geçerli bir tam sayı girin.")
except ZeroDivisionError:
    print("Sıfıra bölme yapılamaz.")
```

Bu örnekte iki farklı problem ayrı ayrı yönetilir. Böylece kullanıcıya belirsiz bir hata dökümü göstermek yerine anlaşılır geri bildirim sunulur. Akışı basitçe şöyle modelleyebiliriz:

$$\text{Sonraki Adım} = \begin{cases}
\text{Normal Akış}, & \text{istisna yoksa} \\
\text{Hata Yönetimi}, & \text{istisna varsa}
\end{cases}$$

## `else` ve `finally` sahneye çıkıyor

`else`, yalnızca hata oluşmadığında; `finally` ise sonuç ne olursa olsun çalışır. Özellikle dosya, ağ bağlantısı veya veritabanı gibi kaynakların kapatılmasında `finally` oldukça değerlidir.

```python
dosya = None
try:
    dosya = open("ayarlar.txt", "r", encoding="utf-8")
    icerik = dosya.read()
except FileNotFoundError:
    print("Ayar dosyası bulunamadı.")
else:
    print("Dosya başarıyla okundu:", icerik)
finally:
    if dosya is not None:
        dosya.close()
    print("Dosya işlemi tamamlandı.")
```

| Blok | Ne zaman çalışır? | Temel görevi |
|---|---|---|
| `try` | Her denemede | Riskli işlemi yürütmek |
| `except` | Eşleşen istisnada | Hatayı yönetmek |
| `else` | İstisna oluşmadığında | Başarılı sonucu işlemek |
| `finally` | Her durumda | Temizlik yapmak |

## Kendi istisnamızı üretelim

Bazen teknik olarak geçerli bir değer, uygulamanın iş kurallarına aykırıdır. Böyle durumlarda `raise` ile bilinçli olarak istisna oluşturabiliriz.

```python
class YetersizBakiyeHatasi(Exception):
    pass


def para_cek(bakiye, miktar):
    if miktar <= 0:
        raise ValueError("Miktar pozitif olmalıdır.")
    if miktar > bakiye:
        raise YetersizBakiyeHatasi("Bakiye yetersiz.")
    return bakiye - miktar

try:
    yeni_bakiye = para_cek(500, 750)
except YetersizBakiyeHatasi as hata:
    print(hata)
```

Özel istisna, problemin kaynağını açıkça ifade eder ve büyük projelerde hata yönetimini okunabilir kılar.

## Her şeyi yakalamak neden tehlikeli?

`except Exception:` kullanmak mümkün olsa da bunu her yerde uygulamak gerçek programlama hatalarını gizleyebilir. Çıplak `except:` ise klavye kesintisi gibi beklenmeyen durumları bile yakalayabilir. En iyi yaklaşım, beklenen istisnaları özel sınıflarıyla yakalamak, kullanıcıya anlamlı mesaj vermek ve gerekirse hatayı bir kayıt sistemine yazmaktır.

İyi hata yönetimi, hataları yok saymak değil; neyin ters gidebileceğini öngörerek programın güvenli biçimde devam etmesini veya kontrollü şekilde sonlanmasını sağlamaktır. Kısacası `try-except`, programınıza görünmez bir kask takar: kazayı engellemeyebilir ama hasarı ciddi ölçüde azaltır.
