---
layout: post
title: "Python’da Karakter Dizileri: Metinleri Dilimle, Dönüştür ve Yönet"
math: true
categories: 
  - Bilgi
tags: 
  - Python
  - String
  - Metin İşleme
---

Programlama dünyasında isimlerden e-posta adreslerine, kullanıcı mesajlarından dosya içeriklerine kadar pek çok veri metin biçiminde karşımıza çıkar. Python, bu metinleri `str` yani karakter dizisi türüyle temsil eder. String’leri yalnızca ekrana yazdırılan cümleler olarak değil, indekslenebilen ve güçlü metotlarla dönüştürülebilen karakter koleksiyonları olarak düşünmek gerekir.
``
## String Nedir?

Python’da tek, çift veya üç tırnak arasına yazılan değerler string kabul edilir. Her string, sıralı bir karakter dizisidir:

```python
mesaj = "Python eğlencelidir!"
print(type(mesaj))  # <class 'str'>
```

Bir string’in uzunluğu `len()` fonksiyonuyla bulunur. Matematiksel olarak uzunluğu $n$ olan bir string’in geçerli pozitif indeksleri $0$ ile $n-1$ arasındadır. Python ayrıca sondan erişim için negatif indeksleri destekler; son karakterin indeksi $-1$ olur.

```python
kelime = "Python"

print(len(kelime))  # 6
print(kelime[0])    # P
print(kelime[5])    # n
print(kelime[-1])   # n
print(kelime[-2])   # o
```

| İfade | Anlamı | Sonuç |
|---|---|---|
| `kelime[0]` | İlk karakter | `P` |
| `kelime[2]` | Üçüncü karakter | `t` |
| `kelime[-1]` | Son karakter | `n` |
| `len(kelime)` | Karakter sayısı | `6` |

Var olmayan bir indekse erişmek `IndexError` üretir. Örneğin altı karakterli bir string’de `kelime[6]` kullanılamaz.

## Slicing: Metni Dilimlemek

Dilimleme söz dizimi `metin[başlangıç:bitiş:adım]` biçimindedir. Başlangıç dahil, bitiş hariçtir. Başlangıç $a$, bitiş $b$ olduğunda ve adım bir olduğunda seçilen karakter sayısı genel olarak $b-a$ kadardır.

```python
metin = "Programlama"

print(metin[0:7])   # Program
print(metin[:7])    # Program
print(metin[7:])    # lama
print(metin[::2])   # Pormaa
print(metin[::-1])  # amalmargorP
```

`[::-1]` ifadesi string’i tersten okumak için kullanılan kısa ve eğlenceli bir yöntemdir. Palindrom kontrolünde de işe yarar:

```python
def palindrom_mu(metin):
    temiz = metin.lower().replace(" ", "")
    return temiz == temiz[::-1]

print(palindrom_mu("Nalan"))  # True
```

Bu fonksiyon önce harfleri küçültür, boşlukları kaldırır ve metni ters hâliyle karşılaştırır.

## String Metotlarıyla Dönüşüm

String’ler değiştirilemez, yani **immutable** yapılardır. Bir metot mevcut string’i yerinde değiştirmez; yeni bir string üretir. Sonucu korumak için bir değişkene atamak gerekir.

```python
ad = "  ada lovelace  "
sonuc = ad.strip().title()
print(sonuc)  # Ada Lovelace
```

| Metot | Görevi | Örnek sonuç |
|---|---|---|
| `lower()` | Harfleri küçültür | `python` |
| `upper()` | Harfleri büyütür | `PYTHON` |
| `title()` | Kelime başlarını büyütür | `Merhaba Dünya` |
| `strip()` | Kenar boşluklarını siler | `metin` |
| `replace(a, b)` | Parçaları değiştirir | Yeni metin |
| `split()` | String’i listeye böler | `['a', 'b']` |
| `join()` | Parçaları birleştirir | `a-b` |

```python
cumle = "Python hızlı ve okunaklıdır"
kelimeler = cumle.split()
print(kelimeler)

yeni_cumle = "-".join(kelimeler)
print(yeni_cumle)  # Python-hızlı-ve-okunaklıdır
```

`split()` metni parçalarken `join()` parçaları yeniden bir araya getirir. Özellikle CSV verileri, etiketler ve kullanıcı girdileri işlenirken bu ikili adeta metin mutfağının bıçak ve kesme tahtasıdır.

## Arama ve Kontrol İşlemleri

Bir parçanın metinde bulunup bulunmadığı `in` operatörüyle kontrol edilebilir. `find()` konumu döndürür; eşleşme yoksa `-1` verir. `startswith()` ve `endswith()` ise başlangıç ya da bitiş denetimi yapar.

```python
dosya = "rapor_2026.pdf"

print("2026" in dosya)          # True
print(dosya.find("rapor"))      # 0
print(dosya.startswith("rapor")) # True
print(dosya.endswith(".pdf"))    # True
```

Sonuç olarak indeksleme tek karaktere erişmeyi, slicing belirli aralıkları çıkarmayı, yerleşik metotlar ise metni temizleyip dönüştürmeyi sağlar. Bu araçları birlikte kullanmak; doğrulama, arama, veri temizleme ve doğal dil işleme gibi daha büyük problemlerin temelini oluşturur.
