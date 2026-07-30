---
layout: post
title: "Python’da Koşullu Durumlar: if-elif-else ile Akışı Yönetmek"
math: true
categories: 
  - Bilgi
tags: 
  - Python
  - Akış Kontrolü
  - Koşullu İfadeler
---

Bir programın yalnızca komutları sırayla çalıştırması çoğu zaman yeterli değildir. Kullanıcının yaşına göre farklı mesaj göstermek, hatalı girişleri engellemek veya bir oyundaki karakterin canı sıfıra düştüğünde macerayı bitirmek için programın karar vermesi gerekir. Python’daki `if`, `elif` ve `else` blokları, kodumuza tam olarak bu karar mekanizmasını kazandırır.

``

## Koşul Nedir?

Koşul, sonucu doğru veya yanlış olan bir ifadedir. Programlama dilinde bu iki sonuç `True` ve `False` değerleriyle temsil edilir. Örneğin `puan >= 50` ifadesi, puan 50 veya daha büyükse doğru; aksi durumda yanlıştır.

Bu mantık matematiksel olarak bir karar fonksiyonu şeklinde düşünülebilir:

$$
f(x) = \begin{cases}
\text{Geçti}, & x \geq 50 \\
\text{Kaldı}, & x < 50
\end{cases}
$$

Buradaki $x$, öğrencinin puanıdır. Koşullu bloklar, bu matematiksel ayrımı çalıştırılabilir koda dönüştürür.

## if, elif ve else Görevleri

| Anahtar kelime | Ne zaman çalışır? | Kullanım amacı |
|---|---|---|
| `if` | İlk koşul doğruysa | Karar zincirini başlatmak |
| `elif` | Önceki koşullar yanlış, kendi koşulu doğruysa | Alternatif durumları sınamak |
| `else` | Diğer koşulların tamamı yanlışsa | Geriye kalan durumları yakalamak |

Basit bir not değerlendirme sistemi oluşturalım:

```python
puan = 76

if puan >= 85:
    print("Pekiyi")
elif puan >= 70:
    print("İyi")
elif puan >= 50:
    print("Geçer")
else:
    print("Kaldı")
```

Python koşulları yukarıdan aşağıya kontrol eder. `puan >= 70` doğru olduğunda ekrana `İyi` yazdırılır ve zincirin geri kalanı değerlendirilmez. Bu nedenle koşulların sırası önemlidir. Önce daha genel olan `puan >= 50` yazılsaydı 76 puan, yanlışlıkla yalnızca `Geçer` olarak sınıflandırılırdı.

## Karşılaştırma ve Mantıksal Operatörler

Koşullar oluşturulurken karşılaştırma operatörlerinden yararlanılır:

| Operatör | Anlamı | Örnek |
|---|---|---|
| `==` | Eşittir | `rol == "admin"` |
| `!=` | Eşit değildir | `durum != "kapalı"` |
| `>` / `<` | Büyük / küçüktür | `sicaklik > 30` |
| `>=` / `<=` | Büyük-eşit / küçük-eşit | `yas >= 18` |

Birden fazla şartı birleştirmek için `and`, `or` ve `not` kullanılır. `and` bütün şartların, `or` ise en az bir şartın doğru olmasını bekler. `not`, mantıksal sonucu tersine çevirir.

```python
yas = 22
bileti_var = True

if yas >= 18 and bileti_var:
    print("Etkinliğe giriş yapabilirsiniz.")
elif yas >= 18 and not bileti_var:
    print("Önce bilet almalısınız.")
else:
    print("Yaş sınırı nedeniyle giriş yapılamaz.")
```

Bu kod hem yaş hem de bilet bilgisini değerlendirerek akışı dinamik biçimde yönlendirir. Gerçek uygulamalarda kullanıcı yetkilendirme, ödeme kontrolü ve form doğrulama gibi pek çok süreç aynı mantığa dayanır.

## İç İçe Koşullar mı, Birleşik Koşullar mı?

Bir `if` bloğunun içine başka bir `if` yazılabilir. Buna iç içe koşul denir. Ancak gereksiz katmanlar kodu merdivene dönüştürebilir:

```python
kullanici_aktif = True
rol = "admin"

if kullanici_aktif:
    if rol == "admin":
        print("Yönetim paneli açıldı.")
```

Aynı kontrol, `if kullanici_aktif and rol == "admin":` biçiminde daha sade yazılabilir. Yine de ikinci kontrol yalnızca ilk koşul gerçekleştiğinde anlamlıysa iç içe yapı tercih edilebilir.

## Yaygın Hatalar ve İpuçları

Python’da bloklar süslü parantezle değil, girintilerle belirlenir. Bu yüzden koşul altındaki satırlar aynı miktarda girintilenmelidir. Ayrıca değer atayan `=` ile karşılaştırma yapan `==` birbirine karıştırılmamalıdır.

Koşulları yazarken en özel durumdan en genel duruma ilerlemek, beklenmeyen girişler için bir `else` dalı bırakmak ve karmaşık ifadeleri anlamlı değişkenlere ayırmak okunabilirliği artırır. Kısacası `if-elif-else`, programın yol ayrımlarındaki trafik ışığıdır: Doğru tasarlanırsa akış düzenli ilerler; yanlış sıralanırsa kod kendini beklenmedik bir mahallede bulabilir.
