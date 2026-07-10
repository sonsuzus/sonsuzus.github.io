---
layout: post
title: "Python ile Asal Sayıları Bulan Programlar (12-14 Yaş İçin)"
math: true
categories: 
  - Program
tags: 
  - Python
  - Asal Sayılar
  - Başlangıç Seviyesi
  - Algoritma
---

# Python ile Asal Sayıları Bulan Programlar

Bu yazıda Python kullanarak **asal sayıları bulan programlar** yazacağız. Konu, 12-14 yaş seviyesine uygun olacak şekilde basit örneklerle anlatılmıştır.

## Asal Sayı Nedir?

**Asal sayı**, sadece **1'e** ve **kendisine** tam bölünebilen 1'den büyük doğal sayıdır.

Örnek asal sayılar:

```text
2, 3, 5, 7, 11, 13, 17, 19, 23
```

Asal olmayan sayılara **asal olmayan sayı** veya **bileşik sayı** denir.

Örneğin:

- 4 asal değildir çünkü 1, 2 ve 4'e bölünür.
- 9 asal değildir çünkü 1, 3 ve 9'a bölünür.
- 10 asal değildir çünkü 1, 2, 5 ve 10'a bölünür.

> Önemli bilgi: **1 asal sayı değildir.**

---

## 1. Bir Sayının Asal Olup Olmadığını Bulma

İlk olarak kullanıcıdan bir sayı alalım ve bu sayının asal olup olmadığını kontrol edelim.

```python
sayi = int(input("Bir sayı giriniz: "))

asal_mi = True

if sayi <= 1:
    asal_mi = False
else:
    for i in range(2, sayi):
        if sayi % i == 0:
            asal_mi = False
            break

if asal_mi:
    print(sayi, "asal sayıdır.")
else:
    print(sayi, "asal sayı değildir.")
```

### Program Nasıl Çalışır?

Bu programda şu adımlar gerçekleşir:

1. Kullanıcıdan bir sayı alınır.
2. Başlangıçta sayının asal olduğu varsayılır.
3. Eğer sayı 1 veya daha küçükse asal değildir.
4. Sayı, 2'den başlayarak kendisinden bir önceki sayıya kadar bölünmeye çalışılır.
5. Eğer tam bölünürse asal değildir.
6. Hiçbir sayıya tam bölünmezse asaldır.

### Örnek Çalışma

```text
Bir sayı giriniz: 7
7 asal sayıdır.
```

```text
Bir sayı giriniz: 12
12 asal sayı değildir.
```

---

## 2. Daha Kolay Anlamak İçin Bölme Kontrolü

Python'da `%` işareti **mod alma** anlamına gelir. Yani bölme işleminden kalan sayıyı verir.

Örnek:

```python
print(10 % 2)  # 0
print(10 % 3)  # 1
print(15 % 5)  # 0
```

Eğer bir sayının başka bir sayıya bölümünden kalan **0** ise, bu sayı tam bölünür.

Örneğin:

```python
12 % 3 == 0
```

Bu ifade doğrudur çünkü 12, 3'e tam bölünür.

---

## 3. Fonksiyon Kullanarak Asal Sayı Kontrolü

Şimdi aynı işlemi bir **fonksiyon** ile yapalım.

Fonksiyonlar, aynı kodu tekrar tekrar yazmamızı engeller.

```python
def asal_mi(sayi):
    if sayi <= 1:
        return False

    for i in range(2, sayi):
        if sayi % i == 0:
            return False

    return True

numara = int(input("Bir sayı giriniz: "))

if asal_mi(numara):
    print(numara, "asal sayıdır.")
else:
    print(numara, "asal sayı değildir.")
```

### Fonksiyon Ne İşe Yarar?

Bu bölümde `asal_mi` adında bir fonksiyon yazdık.

```python
def asal_mi(sayi):
```

Bu fonksiyon içine bir sayı gönderiyoruz. Fonksiyon bize `True` veya `False` döndürüyor.

| Sonuç | Anlamı |
|---|---|
| `True` | Sayı asaldır |
| `False` | Sayı asal değildir |

---

## 4. 1'den N'e Kadar Olan Asal Sayıları Bulma

Şimdi kullanıcıdan bir üst sınır alalım. Örneğin kullanıcı 50 girerse, 1'den 50'ye kadar olan asal sayıları ekrana yazdıralım.

```python
def asal_mi(sayi):
    if sayi <= 1:
        return False

    for i in range(2, sayi):
        if sayi % i == 0:
            return False

    return True

ust_sinir = int(input("Üst sınırı giriniz: "))

print("Asal sayılar:")

for sayi in range(1, ust_sinir + 1):
    if asal_mi(sayi):
        print(sayi)
```

### Örnek Çalışma

```text
Üst sınırı giriniz: 20
Asal sayılar:
2
3
5
7
11
13
17
19
```

Bu program 1'den başlayıp kullanıcının girdiği sayıya kadar tüm sayıları kontrol eder.

---

## 5. Asal Sayıları Liste İçinde Saklama

Bazen asal sayıları sadece ekrana yazdırmak yerine bir listede saklamak isteyebiliriz.

```python
def asal_mi(sayi):
    if sayi <= 1:
        return False

    for i in range(2, sayi):
        if sayi % i == 0:
            return False

    return True

ust_sinir = int(input("Üst sınırı giriniz: "))
asal_sayilar = []

for sayi in range(1, ust_sinir + 1):
    if asal_mi(sayi):
        asal_sayilar.append(sayi)

print("Asal sayılar:", asal_sayilar)
print("Toplam asal sayı adedi:", len(asal_sayilar))
```

### Örnek Çalışma

```text
Üst sınırı giriniz: 30
Asal sayılar: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
Toplam asal sayı adedi: 10
```

Burada iki yeni şey kullandık:

- `append()` listeye yeni eleman ekler.
- `len()` listenin kaç elemanlı olduğunu verir.

---

## 6. Daha Hızlı Asal Sayı Kontrolü

Bir sayının asal olup olmadığını anlamak için her zaman 2'den sayının kendisine kadar kontrol yapmamıza gerek yoktur.

Örneğin 36 sayısını düşünelim:

```text
1 x 36
2 x 18
3 x 12
4 x 9
6 x 6
9 x 4
12 x 3
18 x 2
36 x 1
```

Gördüğün gibi çarpanlar bir noktadan sonra tekrar etmeye başlıyor. Bu yüzden bir sayının kareköküne kadar kontrol etmek yeterlidir.

Basitçe söylemek gerekirse:

> Bir sayı asal değilse, en az bir böleni karekökünden küçük veya ona eşittir.

Python'da karekök almak için `** 0.5` kullanabiliriz.

```python
def asal_mi(sayi):
    if sayi <= 1:
        return False

    for i in range(2, int(sayi ** 0.5) + 1):
        if sayi % i == 0:
            return False

    return True

sayi = int(input("Bir sayı giriniz: "))

if asal_mi(sayi):
    print(sayi, "asal sayıdır.")
else:
    print(sayi, "asal sayı değildir.")
```

### Neden Daha Hızlı?

Diyelim ki sayı 100 olsun.

İlk yöntemde 2'den 99'a kadar kontrol yapılır.

Daha hızlı yöntemde ise sadece 2'den 10'a kadar kontrol yapılır çünkü:

```text
100'ün karekökü = 10
```

Bu yöntem büyük sayılarda daha hızlı çalışır.

---

## 7. Belirli Bir Aralıktaki Asal Sayıları Bulma

Şimdi kullanıcıdan başlangıç ve bitiş değerleri alalım. Bu iki sayı arasındaki asal sayıları bulalım.

```python
def asal_mi(sayi):
    if sayi <= 1:
        return False

    for i in range(2, int(sayi ** 0.5) + 1):
        if sayi % i == 0:
            return False

    return True

baslangic = int(input("Başlangıç sayısını giriniz: "))
bitis = int(input("Bitiş sayısını giriniz: "))

print(baslangic, "ile", bitis, "arasındaki asal sayılar:")

for sayi in range(baslangic, bitis + 1):
    if asal_mi(sayi):
        print(sayi)
```

### Örnek Çalışma

```text
Başlangıç sayısını giriniz: 10
Bitiş sayısını giriniz: 50
10 ile 50 arasındaki asal sayılar:
11
13
17
19
23
29
31
37
41
43
47
```

---

## 8. İlk N Tane Asal Sayıyı Bulma

Bu kez kullanıcı kaç tane asal sayı görmek istediğini girsin.

Örneğin kullanıcı 10 girerse, ilk 10 asal sayıyı yazdıralım.

```python
def asal_mi(sayi):
    if sayi <= 1:
        return False

    for i in range(2, int(sayi ** 0.5) + 1):
        if sayi % i == 0:
            return False

    return True

adet = int(input("Kaç tane asal sayı yazdırılsın? "))
bulunan = 0
sayi = 2

while bulunan < adet:
    if asal_mi(sayi):
        print(sayi)
        bulunan += 1

    sayi += 1
```

### Bu Programda Ne Öğrendik?

Bu programda `while` döngüsü kullandık.

`while` döngüsü, bir koşul doğru olduğu sürece çalışır.

```python
while bulunan < adet:
```

Bu satırın anlamı şudur:

> Bulunan asal sayı miktarı, istenen adetten küçük olduğu sürece devam et.

---

## 9. Mini Proje: Asal Sayı Menüsü

Şimdi öğrendiklerimizi küçük bir programa dönüştürelim. Kullanıcı menüden seçim yapsın.

```python
def asal_mi(sayi):
    if sayi <= 1:
        return False

    for i in range(2, int(sayi ** 0.5) + 1):
        if sayi % i == 0:
            return False

    return True

while True:
    print("\n--- Asal Sayı Programı ---")
    print("1 - Bir sayının asal olup olmadığını kontrol et")
    print("2 - 1'den N'e kadar asal sayıları yazdır")
    print("3 - Belirli aralıktaki asal sayıları yazdır")
    print("4 - Çıkış")

    secim = input("Seçiminiz: ")

    if secim == "1":
        sayi = int(input("Sayı giriniz: "))
        if asal_mi(sayi):
            print(sayi, "asal sayıdır.")
        else:
            print(sayi, "asal sayı değildir.")

    elif secim == "2":
        ust_sinir = int(input("Üst sınır giriniz: "))
        for sayi in range(1, ust_sinir + 1):
            if asal_mi(sayi):
                print(sayi)

    elif secim == "3":
        baslangic = int(input("Başlangıç sayısı: "))
        bitis = int(input("Bitiş sayısı: "))
        for sayi in range(baslangic, bitis + 1):
            if asal_mi(sayi):
                print(sayi)

    elif secim == "4":
        print("Programdan çıkılıyor...")
        break

    else:
        print("Hatalı seçim yaptınız.")
```

Bu mini proje ile şunları kullanmış olduk:

- `if-elif-else`
- `for` döngüsü
- `while` döngüsü
- fonksiyonlar
- listeler ve sayılarla işlem yapma

---

## Sık Yapılan Hatalar

### 1. 1 Sayısını Asal Kabul Etmek

Yanlış:

```python
if sayi == 1:
    print("Asal")
```

Doğru:

```python
if sayi <= 1:
    print("Asal değil")
```

### 2. `break` Kullanmayı Unutmak

Bir sayı asal değilse, bölen bulunduğu anda döngüyü durdurabiliriz.

```python
if sayi % i == 0:
    asal_mi = False
    break
```

Bu programı daha hızlı yapar.

### 3. Girilen Değeri Sayıya Çevirmemek

`input()` her zaman metin yani string döndürür. Matematik işlemleri için `int()` kullanmalıyız.

```python
sayi = int(input("Sayı giriniz: "))
```

---

## Alıştırmalar

Aşağıdaki alıştırmaları yaparak konuyu daha iyi öğrenebilirsin:

1. Kullanıcıdan 5 sayı alıp hangilerinin asal olduğunu yazdıran program yaz.
2. 1 ile 100 arasındaki asal sayıları bir listeye ekle ve listeyi yazdır.
3. Kullanıcının girdiği iki sayı arasındaki asal sayıların toplamını bulan program yaz.
4. İlk 20 asal sayıyı ekrana yazdır.
5. Asal sayıları yan yana yazdıran bir program yaz.

Örnek yan yana yazdırma:

```python
print(sayi, end=" ")
```

---

## Sonuç

Bu yazıda Python ile asal sayıları bulmayı öğrendik. Önce bir sayının asal olup olmadığını kontrol ettik, sonra belirli aralıklardaki asal sayıları bulduk ve en sonunda menülü küçük bir program yaptık.

Asal sayı programları, algoritma mantığını geliştirmek için çok güzel örneklerdir. Çünkü bu programlarda döngüler, koşullar, fonksiyonlar ve listeler birlikte kullanılır.
