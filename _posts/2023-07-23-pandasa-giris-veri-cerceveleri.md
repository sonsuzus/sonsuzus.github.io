---
title:  Pandas’a Giriş – Veri Çerçeveleri
author: sonsuz
date: 2023-07-23 22:19:51 +0300
categories: [Program,Python]
tags: [python,programlama,veri,veri analizi,pandas,numpy,sql,tablo,dataframe,join]
---



`Pandas` ile ilgili bu yazımızda veri çerçevesi (`DataFrame`) isimli veri yapısını ele alacağız. Önceki yazımızda etiketli verilerden oluşan [serileri](https://sonsuzus.github.io/posts/pandasa-giris-seriler/) görmüştük. Seriler tek boyutlu bir veri yapısıyken, veri çerçevelerini her sütunu bir seriden oluşan iki boyutlu bir matris olarak düşünebiliriz. Serilerde bahsettiğimiz birçok yöntemi veri çerçevelerinde de kullanmak mümkün. Ayrıca SQL tablolarında kullanılan tablo birleştirme (`JOIN`) gibi işlemleri de `Pandas` ile yapmak mümkün.

## Veri Çerçeveleri

Veri çerçevelerini birden fazla serinin bir araya gelmiş hali olarak düşünebiliriz. Veri çerçeveleri de seriler gibi etiketli bir veri yapısıdır, ancak serilerden farkı iki boyutlu olmasıdır. Serilerdeki gibi etiket değerlerine indeks (`index`) denir. Veri çerçeveleri `index` alanının yanında `columns` alanını da içeriyor. `columns` sütunların isimlerini içeren bir sıralı nesne.

Veri çerçevesi oluşturmak için serileri kullanmak mümkün. [Linkten](http://www.imf.org/external/pubs/ft/weo/2017/02/weodata/download.aspx) erişebileceğiniz IMF’nin gayrisafi yurt içi hasıla verisi ile ilk denemeyi yapabiliriz. 2016 ve 2017 yılları için serileri anlattığımız yazıdaki veri kümelerini oluşturalım.

In [1]:

```py
# Pandas paketini yükleyelim

import pandas as pd 
import numpy as np

# GSYİH değeri en yüksek olan 10 ülkenin değerlerini kullanacağız.

gdp_data_2017 = [19362.13, 11937.56, 4884.49, 3651.87, 2574.81, 2565.05, 2439.01, 2080.92, 1921.14, 1640.39]

# İndeks değerlerini içeren listeyi oluşturalım.

gdp_index_2017 = ['ABD', 'Çin', 'Japonya', 'Almanya', 'Fransa', 'Birleşik Krallık', 'Hindistan', 'Brezilya', 'İtalya', 'Kanada']

# Seriyi oluşturalım. İndeks değerini vermediğimizde, Pandas 0'dan başlayarak veriyi indeksler.

gdp_2017 = pd.Series(gdp_data_2017, index = gdp_index_2017, name = 'GDP_2017')

# Aynı işlemi 2016 yılı için yapalım.

d = {'ABD':18624.45,
'Çin':11232.11,
'Japonya':4936.54,
'Almanya':3479.23,
'Fransa':2466.47,
'Birleşik Krallık':2629.19,
'Hindistan':2263.79,
'Brezilya':1798.62,
'İtalya':1850.74,
'Kanada':1529.76,
'Kore':1411.04}

gdp_2016 = pd.Series(d, name = 'GDP_2016')

print(gdp_2016)
print(gdp_2017)
```

```py
ABD                 18624.45
Almanya              3479.23
Birleşik Krallık     2629.19
Brezilya             1798.62
Fransa               2466.47
Hindistan            2263.79
Japonya              4936.54
Kanada               1529.76
Kore                 1411.04
Çin                 11232.11
İtalya               1850.74
Name: GDP_2016, dtype: float64
ABD                 19362.13
Çin                 11937.56
Japonya              4884.49
Almanya              3651.87
Fransa               2574.81
Birleşik Krallık     2565.05
Hindistan            2439.01
Brezilya             2080.92
İtalya               1921.14
Kanada               1640.39
Name: GDP_2017, dtype: float64
```

Oluşturduğumuz serileri birleştirmek için iki yol kullanacağız. Bunlardan biri `pandas` altındaki `concat` fonksiyonu, diğeri ise serilerden oluşan bir sözlük tanımlamak olacak.

`concat` fonksiyonunu kullanırken sütunların isimlerini ayrıca belirtmemize gerek yok. Bunun yerine serilerin `name` alanı sütun isimleri olarak atanıyor. Bir seride olup diğerinde olmayan değerler (Kore gibi) `NaN` değeriyle gösterilir.

In [2]:

```py
df = pd.concat([gdp_2017, gdp_2016], axis = 1)
print(df)
```

```py
                  GDP_2017  GDP_2016
ABD               19362.13  18624.45
Almanya            3651.87   3479.23
Birleşik Krallık   2565.05   2629.19
Brezilya           2080.92   1798.62
Fransa             2574.81   2466.47
Hindistan          2439.01   2263.79
Japonya            4884.49   4936.54
Kanada             1640.39   1529.76
Kore                   NaN   1411.04
Çin               11937.56  11232.11
İtalya             1921.14   1850.74
```

Veri çerçevesindeki değerlerin serilerdeki yerinden bağımsız olarak indeks alanına göre eşleştirildiğini görüyoruz. Ondalık işaretini virgüle çevirmek için aşağıdaki yerel ayarları kullanabiliriz. Aşağıdaki kutucukta yerel ayarları değiştiriyoruz ve ondalıklı sayıları formatlıyoruz. Son satırdaki `grouping = False` binlik işaretini kullanmayacağımızı belirtiyor. Yerel ayarların formatlama konusunda [dizeler](https://sonsuzus.github.io/posts/python-programlamaya-giris-15-dize-metodlari/) için yazılan yazıları incelemenizi tavsiye ederim.

In [3]:

```py
import locale
loc = locale.getlocale()

# Yerel ayarları Türkiye standartlarına çeviriyoruz.

locale.setlocale(locale.LC_ALL, "Turkish_Turkey.1254")

# Küsuratlı sayıları virgülden sonra iki basamak içerecek şekilde formatlıyoruz.
# Binlik işaretini kullanmayacağız.

pd.set_option('display.float_format', lambda x: locale.format('%.2f', x, grouping = False))
```

Aşağıdaki örnekte, veri çerçevesini serilerden oluşan bir sözlük yardımıyla oluşturuyoruz. Sözlüğün anahtarı sütunun ismine atanır.

In [4]:

```py
d = {'2017' : gdp_2017,
     '2016' : gdp_2016}

df = pd.DataFrame(d)
print(df)
```

```py
                     2016     2017
ABD              18624,45 19362,13
Almanya           3479,23  3651,87
Birleşik Krallık  2629,19  2565,05
Brezilya          1798,62  2080,92
Fransa            2466,47  2574,81
Hindistan         2263,79  2439,01
Japonya           4936,54  4884,49
Kanada            1529,76  1640,39
Kore              1411,04      nan
Çin              11232,11 11937,56
İtalya            1850,74  1921,14
```

Ondalık işaretinin değiştiğini görebilirsiniz.

Sözlük listeleri de veri çerçevesi oluşturmak için kullanılabilir. Aşağıdaki örnekteki listedeki her bir sözlük bir ülkenin GSYİH değerine denk geliyor. Hangi ülkeler olduğunu ise veri çerçevesini oluştururken söylüyoruz. Belirtmediğimiz değerler de `NaN` değerini alıyor.

In [5]:

```py
data = [{'GDP_2016':3651.87, 'GDP_2017': 3479.23}, {'GDP_2016' : 2466.47}]
df = pd.DataFrame(data, index = ['Almanya', 'Fransa'])
print(df)
```

```py
         GDP_2016  GDP_2017
Almanya   3651,87   3479,23
Fransa    2466,47       nan
```

Veri çerçevelerinin matrisler gibi iki boyutlu bir veri yapısı olduğundan bahsetmiştik. Matrisler de veri çerçeveleri oluşturmak için kullanılabilir.

In [6]:

```py
# 2x2'lik rassal sayılardan oluşan bir matris oluşturalım.

data = np.random.rand(2,2)

# Index ve columns değerlerini veri çerçevesini oluştururken tanımlayabiliriz.

df = pd.DataFrame(data, index = ['1. satır', '2. satır'], columns=['1. sütun', '2. sütun'])
print(df)
```

```py
          1. sütun  2. sütun
1. satır      0,45      0,42
2. satır      1,00      0,96
```

Uygulamalarınızda kullanacağınız boyuttaki verileri bahsettiğimiz yöntemlerle veri çerçevesine atamanın zorluğunu farketmişsinizdir. Neyse ki `pandas` çeşitli formatlardaki dosyaları okumanızı sağlayacak fonksiyonlar içeriyor.

## Dosya okuma

`pandas` paketi csv, Excel, JSON formatlarındaki dosyaların yanında Stata, SAS programlarıyla oluşturulmuş dosyaları da okuyarak içeriğini bir veri çerçevesine atamanızı sağlayan fonksiyonlar içeriyor. Benim sıklıkla kullandığım `read_clipboard` fonksiyonu ise kopyaladığınız bir veriyi (örneğin bir Excel tablosunu) veri çerçevesine dönüştürüyor.

`read_csv` fonksiyonunda sıklıkla kullanabileceğiniz parametreleri aşağıda bulabilirsiniz:

* `sep`: kolonları ayıran karakter ya da kurallı ifade (varsayılan değer `','`),
* `header`: sütun isimlerini içeren satırın numarası (varsayılan değer 0, eğer böyle bir satır yoksa `None`),
* `index_col`: indeks değerlerini içeren sütunun numarası,
* `names`: sütun isimlerini içeren sıralı nesne.

`read_excel` fonksiyonunda ek olarak birden fazla sayfa içeren dokümanlarda hangi sayfaları okutacağınızı belirten `sheet_name` argümanını da kullanabilirsiniz. `sheet_name` değeri sayfanın adı, indeksi (ya da bunların bir listesi) olabilir. Ayrıca `None` değerini kullanmanız halinde bütün sayfaları okutabilirsiniz. Örnek olarak [linkten](http://archive.ics.uci.edu/ml/datasets/online+retail) indirebileceğiniz bir çevrimiçi alışveriş veri kümesini kullandım.

In [7]:

```py
# Dosya tek bir sayfa içerdiği için sheet_name'e ihtiyaç duymadık.
# Benim bilgisayarımda Excel dosyası ile Jupyter Notebook dosyası 
# aynı klasörde olduğundan adres belirtmedim.

df = pd.read_excel('Online Retail.xlsx', decimal = ',')
print(df.head())
```

```py
  InvoiceNo StockCode                          Description  Quantity  \
0    536365    85123A   WHITE HANGING HEART T-LIGHT HOLDER         6   
1    536365     71053                  WHITE METAL LANTERN         6   
2    536365    84406B       CREAM CUPID HEARTS COAT HANGER         8   
3    536365    84029G  KNITTED UNION FLAG HOT WATER BOTTLE         6   
4    536365    84029E       RED WOOLLY HOTTIE WHITE HEART.         6   

          InvoiceDate  UnitPrice  CustomerID         Country  

0 2010-12-01 08:26:00       2,55    17850,00  United Kingdom  
1 2010-12-01 08:26:00       3,39    17850,00  United Kingdom  
2 2010-12-01 08:26:00       2,75    17850,00  United Kingdom  
3 2010-12-01 08:26:00       3,39    17850,00  United Kingdom  
4 2010-12-01 08:26:00       3,39    17850,00  United Kingdom  
```

Kolonların isimlerini değiştirelim.

In [8]:

```py
df.columns = ['FaturaNo', 'UrunNo', 'Tanim', 'Adet', 'FaturaTarihi', 'BirimFiyat', 'MusteriNo', 'Ulke']
print(df.head())
```

```py
  FaturaNo  UrunNo                                Tanim  Adet  \
0   536365  85123A   WHITE HANGING HEART T-LIGHT HOLDER     6   
1   536365   71053                  WHITE METAL LANTERN     6   
2   536365  84406B       CREAM CUPID HEARTS COAT HANGER     8   
3   536365  84029G  KNITTED UNION FLAG HOT WATER BOTTLE     6   
4   536365  84029E       RED WOOLLY HOTTIE WHITE HEART.     6   

         FaturaTarihi  BirimFiyat  MusteriNo            Ulke  
0 2010-12-01 08:26:00        2,55   17850,00  United Kingdom  
1 2010-12-01 08:26:00        3,39   17850,00  United Kingdom  
2 2010-12-01 08:26:00        2,75   17850,00  United Kingdom  
3 2010-12-01 08:26:00        3,39   17850,00  United Kingdom  
4 2010-12-01 08:26:00        3,39   17850,00  United Kingdom  
```

## Temel Metotlar ve Erişim

Veri çerçevelerinde, serilerde gördüğümüz `dim`, `shape`, `size` alanlarını ve erişim için kullandığımız `loc` ve `iloc` fonksiyonları kullanabiliriz. Serilerden farklı olarak veri çerçeveleri iki boyutlu, `size` alanı da bu nedenle sütun ve satır sayısının çarpımına eşit.

In [9]:

```py
print('Boyut: {}'.format(df.ndim))
print('Şekil: {}'.format(df.shape))
print('Uzunluk: {}'.format(df.size))
print('Sütunlar: {}'.format(df.columns))
```

```py
Boyut: 2
Şekil: (541909, 8)
Uzunluk: 4335272
Sütunlar: Index(['FaturaNo', 'UrunNo', 'Tanim', 'Adet', 'FaturaTarihi', 'BirimFiyat', 'MusteriNo', 'Ulke'],
      dtype='object')
```

Erişim için de yine serilerde gördüğümüz `iloc` ve `loc` metotlarını kullanabiliriz. 

In [10]:

```py
print('Veri çerçevesinin 0,0 indeksindeki değer: {}'.format(df.iloc[0,0]))
print('Veri çerçevesinin ilk satırındaki değerler:\n{}'.format(df.iloc[0,:]))
```

```py
Veri çerçevesinin 0,0 indeksindeki değer: 536365
Veri çerçevesinin ilk satırındaki değerler:
FaturaNo                                    536365
UrunNo                                      85123A
Tanim           WHITE HANGING HEART T-LIGHT HOLDER
Adet                                             6
FaturaTarihi                   2010-12-01 08:26:00
BirimFiyat                                    2,55
MusteriNo                                 17850,00
Ulke                                United Kingdom
Name: 0, dtype: object
```

Verideki eksik değerler özel ilgi göstermemizi gerektirecek durumlara işaret edebilir. Şimdi sütunlardaki eksik değerlerin sayısına bakalım. `isnull` veri çerçevesinin boyutunda 0 ve 1 (`True`/`False`) değerlerinden oluşan bir veri çerçevesi döndürüyor. Bu veri çerçevesi `NaN` olan hücreler için `True`, diğer hücreler için `False` değerine sahip. Sütunlar üzerinden toplarsak eksik değer içeren hücre sayısını bulabiliriz.

In [11]:

```py
print('Eksik hücre sayısı')
print(df.isnull().sum())
```

```py
Eksik hücre sayısı
FaturaNo             0
UrunNo               0
Tanim             1454
Adet                 0
FaturaTarihi         0
BirimFiyat           0
MusteriNo       135080
Ulke                 0
dtype: int64
```

Müşteri numarası olmayan 135080 satır var. Bu satırları veri setinden çıkaralım.

In [12]:

```py
df = df[~df['MusteriNo'].isnull()]
print('Şekil: {}'.format(df.shape))
print('Eksik hücre sayısı')
print(df.isnull().sum())
```

```py
Şekil: (406829, 8)
Eksik hücre sayısı
FaturaNo        0
UrunNo          0
Tanim           0
Adet            0
FaturaTarihi    0
BirimFiyat      0
MusteriNo       0
Ulke            0
dtype: int64
```

Alternatif olarak eksik değerleri istediğiniz başka bir değerle değiştirmeniz de mümkün. Bu amaçla `fillna` fonksiyonunu kullanabilirsiniz. Örnek olarak eksik değerleri 0 değeriyle doldurmak için `df.fillna(0, inplace = True)` yazmanız yeterli. Buradaki `inplace` argümanı değişikliğin veri çerçevesi üzerinde yapılmasını sağlar. Bunu kullanmak istemezseniz bir atama yapmanız gerekecek (`df = df.fillna(0)`). İki seçeneği de kullanmamanız haline orijinal veri çerçevesi değişmeyecektir.

Müşteri numaraları tamsayı olması gerekirken ondalıklı olarak okunduğu için tamsayıya çevirelim.

In [13]:

```py
# Aşağıdaki satırda sütunlara ulaşmanın iki farklı yolunu görüyoruz. 
# Veri_çerçevesi['sütun_adı'] ve Veri_çerçevesi.Sütun_adı

df['MusteriNo'] = df.MusteriNo.astype('int')
print(df.head())
```

```py
  FaturaNo  UrunNo                                Tanim  Adet  \
0   536365  85123A   WHITE HANGING HEART T-LIGHT HOLDER     6   
1   536365   71053                  WHITE METAL LANTERN     6   
2   536365  84406B       CREAM CUPID HEARTS COAT HANGER     8   
3   536365  84029G  KNITTED UNION FLAG HOT WATER BOTTLE     6   
4   536365  84029E       RED WOOLLY HOTTIE WHITE HEART.     6   

         FaturaTarihi  BirimFiyat  MusteriNo            Ulke  
0 2010-12-01 08:26:00        2,55      17850  United Kingdom  
1 2010-12-01 08:26:00        3,39      17850  United Kingdom  
2 2010-12-01 08:26:00        2,75      17850  United Kingdom  
3 2010-12-01 08:26:00        3,39      17850  United Kingdom  
4 2010-12-01 08:26:00        3,39      17850  United Kingdom  
```

## Veri İşleme

Veri çerçevesinde ürünler için birim fiyat ve satın alınan adet değerleri var. Müşterilerin o ürün için toplam harcamasını içeren bir sütun ekleyelim. Yeni sütunun adı `Miktar` olsun.

In [14]:

```py
df['Miktar'] = df['BirimFiyat'] * df['Adet']
print(df.head())
```

```py
  FaturaNo  UrunNo                                Tanim  Adet  \
0   536365  85123A   WHITE HANGING HEART T-LIGHT HOLDER     6   
1   536365   71053                  WHITE METAL LANTERN     6   
2   536365  84406B       CREAM CUPID HEARTS COAT HANGER     8   
3   536365  84029G  KNITTED UNION FLAG HOT WATER BOTTLE     6   
4   536365  84029E       RED WOOLLY HOTTIE WHITE HEART.     6   

         FaturaTarihi  BirimFiyat  MusteriNo            Ulke  Miktar  
0 2010-12-01 08:26:00        2,55      17850  United Kingdom   15,30  
1 2010-12-01 08:26:00        3,39      17850  United Kingdom   20,34  
2 2010-12-01 08:26:00        2,75      17850  United Kingdom   22,00  
3 2010-12-01 08:26:00        3,39      17850  United Kingdom   20,34  
4 2010-12-01 08:26:00        3,39      17850  United Kingdom   20,34  
```

`FaturaNo` ve o faturaya ait toplam miktarı içeren yeni bir veri çerçevesi oluşturalım. `groupby` fonksiyonuyla her alışverişin toplam miktarını bulabiliriz. `Groupby` fonksiyonunun kullanımını [linkte](https://sonsuzus.github.io/posts/groupby/) anlatmıştık.

In [15]:

```py
df_fis = df.groupby(['FaturaNo']).agg({'Miktar' : 'sum'}).reset_index()
df_fis.columns = ['FaturaNo', 'ToplamMiktar']
print(df_fis.head())
```

```py
  FaturaNo  ToplamMiktar
0   536365        139,12
1   536366         22,20
2   536367        278,73
3   536368         70,05
4   536369         17,85
```

İlk veri çerçevesine `ToplamMiktar` sütununu eklemek için `pandas` paketinin sunduğu birleştirme işlemlerinden yararlanabiliriz. Bu amaçla `merge` fonksiyonunu kullanacağız.

`merge` işlemi için iki veri çerçevesinin hangi sütunlarının nasıl birleştirileceğini belirtmek gerekiyor. `merge` fonksiyonu SQL tablolarında kullanılan birleştirme (`JOIN`) işlemlerini destekliyor. İki veri çerçevesini birleştirmek için `FaturaNo` anahtarını kullanalım (`on = 'FaturaNo'`). Farklı isimlere sahip sütunlar üzerinden birleştirme yapmak için `right_on = ...` ve `left_on = ...` şeklinde veri çerçevelerindeki sütun isimlerini fonksiyona ekleyebilirsiniz.

`how` argümanı için kullanabileceğiniz değerler:

* “`inner`“: Sadece iki tabloda da bulunan anahtar değerlerini birleştirir. Bir tabloda olmayan değerler silinir.
* “`right`“: İlk tabloda bulunan değerler korunur ve ikinci tabloda eşleşen değerler tabloya eklenir. İkinci tabloda bulunmayan değerler `NaN` ile belirtilir.
* “`left`“: İkinci tabloda bulunan değerler korunur ve ilk tabloda eşleşen değerler tabloya eklenir. İlk tabloda bulunmayan değerler `NaN` ile belirtilir.
* “`outer`“: İki tablodan en az birinde bulunan değerler korunur. Bir tabloda olmayan eksik değerler `NaN` ile belirtilir.

In [16]:

```py
df_yeni = pd.merge(df,df_fis, how= 'inner', on = 'FaturaNo')
print(df_yeni.head())
print('Şekil: {}'.format(df_yeni.shape))
print(df_yeni[df_yeni['FaturaNo'] == 536365])
```

```py
  FaturaNo  UrunNo                                Tanim  Adet  \
0   536365  85123A   WHITE HANGING HEART T-LIGHT HOLDER     6   
1   536365   71053                  WHITE METAL LANTERN     6   
2   536365  84406B       CREAM CUPID HEARTS COAT HANGER     8   
3   536365  84029G  KNITTED UNION FLAG HOT WATER BOTTLE     6   
4   536365  84029E       RED WOOLLY HOTTIE WHITE HEART.     6   

         FaturaTarihi  BirimFiyat  MusteriNo            Ulke  Miktar  \
0 2010-12-01 08:26:00        2,55      17850  United Kingdom   15,30   
1 2010-12-01 08:26:00        3,39      17850  United Kingdom   20,34   
2 2010-12-01 08:26:00        2,75      17850  United Kingdom   22,00   
3 2010-12-01 08:26:00        3,39      17850  United Kingdom   20,34   
4 2010-12-01 08:26:00        3,39      17850  United Kingdom   20,34   

   ToplamMiktar  
0        139,12  
1        139,12  
2        139,12  
3        139,12  
4        139,12  
Şekil: (406829, 10)

  FaturaNo  UrunNo                                Tanim  Adet  \
0   536365  85123A   WHITE HANGING HEART T-LIGHT HOLDER     6   
1   536365   71053                  WHITE METAL LANTERN     6   
2   536365  84406B       CREAM CUPID HEARTS COAT HANGER     8   
3   536365  84029G  KNITTED UNION FLAG HOT WATER BOTTLE     6   
4   536365  84029E       RED WOOLLY HOTTIE WHITE HEART.     6   
5   536365   22752         SET 7 BABUSHKA NESTING BOXES     2   
6   536365   21730    GLASS STAR FROSTED T-LIGHT HOLDER     6   

         FaturaTarihi  BirimFiyat  MusteriNo            Ulke  Miktar  \
0 2010-12-01 08:26:00        2,55      17850  United Kingdom   15,30   
1 2010-12-01 08:26:00        3,39      17850  United Kingdom   20,34   
2 2010-12-01 08:26:00        2,75      17850  United Kingdom   22,00   
3 2010-12-01 08:26:00        3,39      17850  United Kingdom   20,34   
4 2010-12-01 08:26:00        3,39      17850  United Kingdom   20,34   
5 2010-12-01 08:26:00        7,65      17850  United Kingdom   15,30   
6 2010-12-01 08:26:00        4,25      17850  United Kingdom   25,50   

   ToplamMiktar  

0        139,12  
1        139,12  
2        139,12  
3        139,12  
4        139,12  
5        139,12  
6        139,12  
```

Tekrar eden verileri tekilleştirmek için `drop_duplicates` fonksiyonunu kullanabiliriz. Aşağıda müşteri numaralarını tekilleştirerek kaç müşteri olduğunu buluyoruz. Ben sütunları kopyalamayı tercih ettim. Bunu yapmamanız durumunda Python referans modelinden kaynaklı bir uyarı mesajı alacaksınız. Bu konu hakkında [referans modeli, sığ ve derin kopyalama](https://sonsuzus.github.io/posts/python-programlamaya-giris-18-python-referans-modeli-sig-ve-derin-kopyalama/) yazısını okumanızı tavsiye ederim.

In [17]:

```py
# Sadece ürün bilgilerini içeren sütunları alıyoruz.
# Burada copy işlemini kullanmazsak bir uyarı mesajı alıyoruz.

df_musteri = df[['MusteriNo']].copy()
df_musteri.drop_duplicates(inplace = True)
print(df_musteri.head())
print('Şekil: {}'.format(df_musteri.shape))
print('Müşteri sayısı: {}'.format(df_musteri.shape[0]))
```

```py
    MusteriNo
0       17850
9       13047
26      12583
46      13748
65      15100
Şekil: (4372, 1)

Müşteri sayısı: 4372
```

Veri çerçeveleri `scikit-learn`, `statsmodel` gibi bir çok paket tarafından destekleniyor. `Tensorflow` ve `lightgbm` gibi popüler paketlerle de veri çerçevelerini kullanabilirsiniz.
