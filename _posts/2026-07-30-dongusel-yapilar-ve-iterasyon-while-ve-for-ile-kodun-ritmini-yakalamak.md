---
layout: post
title: "Döngüsel Yapılar ve İterasyon: while ve for ile Kodun Ritmini Yakalamak"
math: true
categories: 
  - Bilgi
tags: 
  - döngüler
  - iterasyon
  - programlama temelleri
---

Programlamada aynı işlemi defalarca elle yazmak, yüz tabaklı bir sofrada her tabağı ayrı tarifle yıkamaya benzer. Döngüler bu zahmeti ortadan kaldırır: Bir koşul geçerli olduğu sürece veya bir koleksiyondaki bütün elemanlar işlenene kadar aynı kod bloğunu tekrar çalıştırırlar. Böylece daha kısa, okunabilir ve ölçeklenebilir programlar oluşturabiliriz.
``
## İterasyon Nedir?

**İterasyon**, bir işlemin adım adım tekrarlanmasıdır. Her tekrar bir iterasyon olarak adlandırılır. Örneğin 1’den 5’e kadar sayıları ekrana yazdıran bir döngü beş iterasyon gerçekleştirir.

Bir döngü genellikle üç temel parçaya sahiptir:

1. **Başlangıç durumu:** Sayaç veya başlangıç değeri belirlenir.
2. **Devam koşulu:** Döngünün çalışmayı sürdürüp sürdürmeyeceği kontrol edilir.
3. **Güncelleme:** Her turdan sonra durum değiştirilir.

Bir sayaç $i$ başlangıçta $0$ ise ve her adımda $1$ artıyorsa güncelleme şöyle ifade edilir:

$$i_{yeni} = i_{eski} + 1$$

Döngü $n$ defa çalışıyorsa ve her tur sabit süre alıyorsa yaklaşık zaman karmaşıklığı $O(n)$ olur. İç içe iki döngü ise çoğunlukla $O(n^2)$ maliyet üretir.

## while Döngüsü: Koşul Doğru Oldukça Devam

`while`, tekrar sayısının önceden kesin olarak bilinmediği durumlarda kullanışlıdır. Önce koşulu denetler, sonuç doğruysa gövdeyi çalıştırır.

```python
sayac = 1

while sayac <= 5:
    print(sayac)
    sayac += 1
```

Bu örnekte sayaç 1’den başlar. Koşul her turdan önce kontrol edilir ve sayaç 5’i geçtiğinde döngü sona erer. `sayac += 1` satırını unutursak koşul sürekli doğru kalabilir. Bunun sonucu, programcıların meşhur canavarı olan **sonsuz döngüdür**.

`while` özellikle kullanıcı doğru veri girene kadar beklemek, bir oyunu oyuncunun canı bitene kadar sürdürmek veya bir arama işlemini sonuç bulunana kadar çalıştırmak için uygundur.

## for Döngüsü: Koleksiyonların Düzenli Gezgini

`for`, bir liste, metin, demet veya belirli bir sayı aralığı üzerinde ilerlemek için tercih edilir.

```python
meyveler = ['elma', 'armut', 'muz']

for meyve in meyveler:
    print(meyve.upper())
```

Burada `meyve` değişkeni, her iterasyonda listenin sıradaki elemanını temsil eder. Kod, listedeki meyveleri büyük harflerle yazdırır. Eleman sayısını veya indeks yönetimini elle takip etmemiz gerekmez.

Sayısal tekrarlar için `range()` kullanılabilir:

```python
for sayi in range(1, 6):
    kare = sayi ** 2
    print(sayi, kare)
```

`range(1, 6)`, 1’den başlayıp 6 hariç olacak şekilde değer üretir. Her sayının karesi $x^2$ formülüyle hesaplanır.

## while ve for Karşılaştırması

| Özellik | `while` | `for` |
|---|---|---|
| Temel yaklaşım | Koşula bağlı tekrar | Koleksiyon üzerinde gezinme |
| Tekrar sayısı | Genellikle belirsiz | Genellikle belirli |
| Sayaç yönetimi | Çoğu zaman elle yapılır | Otomatik yapılabilir |
| Sonsuz döngü riski | Daha yüksek | Daha düşük |
| Tipik kullanım | Girdi bekleme, oyun döngüsü | Liste işleme, sayısal aralıklar |

## Döngü Akışını Yönetmek

`break`, döngüyü tamamen sonlandırır; `continue` ise yalnızca mevcut iterasyonu atlayarak sonraki tura geçer.

```python
for sayi in range(1, 11):
    if sayi == 8:
        break
    if sayi % 2 != 0:
        continue
    print(sayi)
```

Bu kod tek sayıları atlar, çift sayıları yazdırır ve 8’e ulaştığında döngüyü bitirir. `%` operatörü kalanı verdiği için $sayi \bmod 2 = 0$ koşulu çift sayıları belirler.

Döngü seçerken temel soru şudur: “Bir koşul gerçekleşene kadar mı bekliyorum, yoksa elimdeki elemanları mı geziyorum?” İlk durumda `while`, ikinci durumda `for` çoğunlukla daha doğal seçimdir. Doğru döngü; kodu yalnızca kısaltmaz, niyetini de okuyucuya açıkça anlatır.
