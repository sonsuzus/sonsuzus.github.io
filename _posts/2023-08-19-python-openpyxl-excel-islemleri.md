---
title: Python openpyxl kütüphanesi ile excel dosyası oluşturma, veri okuma, veri yazma, kaydetme işlemleri
author: sonsuz
date: 2023-08-19 15:53:42 +0300
categories: [Program,Python]
tags: [python,programlama,excel,openpyxl,veri,data,okuma,yazma,excel işlemleri,satır,sütun]
---


## Excel ile ilgili dosya oluşturma, sayfa oluşturma, dosyaya veri yazma, verileri okuma ve kaydetme işlemleri

Excel ile ilgili dosya oluşturma, sayfa oluşturma, dosyaya veri yazma, verileri okuma ve kaydetme işlemleri için aşağıda bilgileri ve sanal ortamda kurulum komutları verilen kütüphaneyi kullanacağız:

Openpyxl kütüphanesi

Openpyxl Excel 2010 xlsx/xlsm/xltx/xltm dosyaları ile ilgili işlemleri gerçekleştiren bir Python kütüphanesidir.

```


pip install openpyxl


```

Bu kütüphane ile birlikte, et-xmlfile kütüphanesi otomatik olarak yüklenir.

Örnek

```py
from openpyxl import Workbook

liste = ["aaaaa", "bbbbb", "ccccc", "ddddd", "eeeee", "fffff", "ggggg", "hhhhh"]

wb = Workbook() # Dosya oluşturma

ws = wb.active # Dosyanın ilk sayfasını aktif hale getirme
ws.title = "Sayfa1"
ws = wb.create_sheet("Sayfa2")
ws = wb.create_sheet("Sayfa3")

print(wb.sheetnames) # Sayfa adlarını ekrana yazdırma

max_row = len(liste); # Liste eleman sayısını alma

# Liste elemanlarını for döngüsüyle ilk sayfanın ilk beş sütununa yazdırma
ws = wb["Sayfa1"]
# iter_cols(min_col=None, max_col=None, min_row=None, max_row=None, values_only=False)
for col in ws.iter_cols(1, 5, 1, max_row, False):
    list_index = 0;  
    for cell in col:
        cell.value = liste[list_index]
        list_index = list_index + 1

# Liste elemanlarını for döngüsüyle ikinci sayfanın ilk beş satırına yazdırma
ws = wb["Sayfa2"]
# iter_rows(min_row=None, max_row=None, min_col=None, max_col=None, values_only=False)
for row in ws.iter_rows(1, 5, 1, max_row, False):
    list_index = 0;  
    for cell in row:
        cell.value = liste[list_index]
        list_index = list_index + 1

# Liste elemanlarını for döngüsüyle üçüncü sayfanın ilk beş satırına yazdırma
ws = wb["Sayfa3"]
for col in range(5):
    for row in range(max_row):
        ws.cell(row+1, col+1, liste[row])	

# Sayfa3'de 5.satır ve 3.sütun (C5) değerini okuma
print(ws.cell(5, 3).value) # cell(row, column, value=None) 			
		
wb.save("deneme.xlsx")


```

Yukarıdaki örnekte, program aşağıdaki satırları ekrana yazar:

```

['Sayfa1', 'Sayfa2', 'Sayfa3']
eeeee

```

Programı çalıştırdığımızda, 8 elemanlı bir liste oluşturur. Workbook() fonksiyonu ile yeni bir dosya oluşturur. Dosyanın ilk sayfasını aktif hale getirdikten sonra, adını "Sayfa1" olarak değiştirir. İki sayfa daha oluşturarak, sırasıyla "Sayfa2" ve "Sayfa3" adlarını verir. Sayfa adlarını ekrana yazdırır. Liste elemanlarını ilk olarak bir for döngüsüyle ilk sayfanın ilk beş sütununa dikey olarak, sonra bir for döngüsüyle ikinci sayfanın ilk beş satırına yatay olarak ve son olarak bir for döngüsüyle üçüncü sayfanın ilk beş sütununa dikey olarak yazdırır. "Sayfa3" de 5.satır ve 3.sütun (C5) hücresinin değerini okuyarak ekrana yazar. Dosyayı "deneme.xlsx" adıyla bulunduğu dizine kaydeder.

## Excel dosyası açarak bir sayfa verilerini okuma işlemleri

Excel dosyası açarak bir sayfa verilerini okumak için aşağıda bilgileri ve sanal ortamda kurulum komutları verilen kütüphaneyi kullanacağız:

Openpyxl kütüphanesi

Openpyxl Excel 2010 xlsx/xlsm/xltx/xltm dosyaları ile ilgili işlemleri gerçekleştiren bir Python kütüphanesidir.

```


pip install openpyxl


```

Bu kütüphane ile birlikte, et-xmlfile kütüphanesi otomatik olarak yüklenir.

Bu örnekte, yukarıda oluşturulan deneme.xlsx adlı Excel dosyası kullanılmaktadır.

Örnek

```py
from openpyxl import load_workbook

# Dosyayı yükleme
wb = load_workbook('deneme.xlsx')

# Sayfa isimlerini ekrana yazma
print(wb.sheetnames)

ws = wb["Sayfa1"] # "Sayfa1" sayfasını alma

print('Max sütun sayısı:', ws.max_column) # Veri bulunan max sütun sayısı
print('Max satır sayısı:', ws.max_row) # Veri bulunan max satır sayısı

print('B4 hücre değeri:', ws['B4'].value) # Hücre değeri
print('B4 hücre değeri:', ws.cell(row=4, column=2).value) # Hücre değeri
print('B4 sütun değeri:', ws['B4'].column) # Hücre sütun değeri
print('B4 satır değeri:', ws['B4'].row) # Hücre satır değeri
print('B4 koordinat değeri:', ws['B4'].coordinate) # Hücre koordinat değeri

# Üçüncü sütundaki değerleri okuyarak ekrana yazma
print('Sayfa1 3.sütun değerleri')
for deg in range(8):
    print(deg+1, ws.cell(row=deg+1, column=3).value)

# İkinci satırdaki değerleri okuyarak ekrana yazma
print('Sayfa1 2.satır değerleri')
for deg in range(5):
    print(deg+1, ws.cell(row=2, column=deg+1).value)


```

Yukarıdaki örnekte, program aşağıdaki satırları ekrana yazar:

```

['Sayfa1', 'Sayfa2', 'Sayfa3']
Max sütun sayısı: 5
Max satır sayısı: 8
B4 hücre değeri: ddddd
B4 hücre değeri: ddddd
B4 sütun değeri: 2
B4 satır değeri: 4
B4 koordinat değeri: B4
Sayfa1 3.sütun değerleri
1 aaaaa
2 bbbbb
3 ccccc
4 ddddd
5 eeeee
6 fffff
7 ggggg
8 hhhhh
Sayfa1 2.satır değerleri
1 bbbbb
2 bbbbb
3 bbbbb
4 bbbbb
5 bbbbb

```

Programı çalıştırdığımızda, load\_workbook() fonksiyonu ile "deneme.xlsx" adlı mevcut bir Excel dosyası açılır. Sayfa isimleri ekrana yazılır. Dosyanın ilk sayfasındaki veri bulunan maksimum sütun ve satır sayısı ekrana yazılır. B4 hücre değeri iki farklı yöntemle ekrana yazılır. B4 hücresinin sütun, satır ve koordinat değerleri ekrana yazılır. Sonra, sırasıyla üçüncü sütundaki değerler ile ikinci satırdaki değerler okunarak ekrana yazılır.

## Excel dosyası açarak sütun ve satır silme ve ekleme işlemleri

Excel dosyası açarak sütun ve satır silme ve ekleme için aşağıda bilgileri ve sanal ortamda kurulum komutları verilen kütüphaneyi kullanacağız:

Openpyxl kütüphanesi

Openpyxl Excel 2010 xlsx/xlsm/xltx/xltm dosyaları ile ilgili işlemleri gerçekleştiren bir Python kütüphanesidir.

```


pip install openpyxl


```

Bu kütüphane ile birlikte, et-xmlfile kütüphanesi otomatik olarak yüklenir.

Bu örnekte, yukarıda oluşturulan deneme.xlsx adlı Excel dosyası kullanılmaktadır.

Örnek

```py
from openpyxl import load_workbook

# Dosyayı yükleme
wb = load_workbook('deneme.xlsx')

# Sayfa isimlerini ekrana yazma
print(wb.sheetnames)

ws = wb["Sayfa1"] # "Sayfa1" sayfasını alma

ws.delete_cols(3, amount=1) # 3.sütundan itibaren tek sütun silme
ws.delete_rows(2, amount=1) # 2.satırdan itibaren tek satır silme

ws.insert_cols(3, amount=3) # 3.sütundan itibaren 3 boş sütun ekleme
ws.insert_rows(2, amount=4) # 2.satırdan itibaren 4 boş satır ekleme

# Son satırdan sonra, ilk 5 sütun içeriği verisi tanımlanmış olarak bir satır ekleme
ws.append(['kkkkk', 'kkkkk', 'kkkkk', 'kkkkk', 'kkkkk'])

wb.save("deneme.xlsx") # Dosyayı kaydetme


```

Yukarıdaki örnekte, program aşağıdaki satırları ekrana yazar:

```

['Sayfa1', 'Sayfa2', 'Sayfa3']

```

Programı çalıştırdığımızda, load\_workbook() fonksiyonu ile "deneme.xlsx" adlı mevcut bir Excel dosyası açılır. Sayfa isimleri ekrana yazılır. Dosyanın ilk sayfasında, 3.sütundan itibaren tek sütun silme ve 2.satırdan itibaren tek satır silme işlemleri, 3.sütundan itibaren 3 boş sütun ekleme ve 2.satırdan itibaren 4 boş satır ekleme işlemleri, son satırdan sonra, ilk 5 sütun içeriği verisi tanımlanmış olarak bir satır ekleme işlemi gerçekleştirilir.
