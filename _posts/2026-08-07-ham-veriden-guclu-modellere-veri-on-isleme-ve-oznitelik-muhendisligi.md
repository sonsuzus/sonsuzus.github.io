---
layout: post
title: "Ham Veriden Güçlü Modellere: Veri Ön İşleme ve Öznitelik Mühendisliği"
math: true
categories: 
  - Bilgi
tags: 
  - veri ön işleme
  - öznitelik mühendisliği
  - makine öğrenmesi
---

Bir makine öğrenmesi modelinin başarısı yalnızca seçilen algoritmaya bağlı değildir. Çoğu zaman modelden daha kritik olan şey, modele verilen verinin kalitesidir. Gürültülü, eksik veya tutarsız verilerle en gelişmiş algoritma bile bocalarken; iyi temizlenmiş ve anlamlı özniteliklerle zenginleştirilmiş bir veri kümesi, daha basit modelleri bile yıldız oyuncuya dönüştürebilir.

``

## Veri ön işleme neden gereklidir?

Gerçek dünya verileri nadiren kullanıma hazır gelir. Yaş sütununda negatif değerler, şehir bilgisinde farklı yazımlar, sensör kayıtlarında boş hücreler veya gelir değişkeninde uç değerler bulunabilir. Veri ön işleme, bu sorunları model eğitilmeden önce sistematik biçimde düzeltme sürecidir.

Temel amaç, gözlenen veriyi gerçek olguyu daha iyi temsil eden bir forma dönüştürmektir. Bir ölçümün şu şekilde oluştuğunu düşünebiliriz:

$$x_{gözlenen} = x_{gerçek} + hata$$

Temizleme işlemleri hata bileşenini azaltmaya çalışır. Ancak aşırı temizlik de bilgi kaybına yol açabilir. Örneğin yüksek tutarlı bir alışveriş kaydı veri hatası değil, gerçekten önemli bir müşteri davranışı olabilir.

| Sorun | Yaygın çözüm | Olası risk |
|---|---|---|
| Eksik değer | Ortalama, medyan veya modelle tahmin | Dağılımın bozulması |
| Uç değer | Sınırlandırma veya dönüşüm | Nadir olayların kaybedilmesi |
| Farklı ölçekler | Standardizasyon | Yorumlanabilirliğin azalması |
| Kategorik veri | One-hot encoding | Çok fazla sütun oluşması |
| Tutarsız metin | Normalleştirme | Anlamlı ayrımların silinmesi |

## Eksik değerleri akıllıca yönetmek

Eksik değerleri doğrudan silmek pratik görünse de veri azsa pahalı bir seçimdir. Sayısal değişkenlerde ortalama kullanılabilir; fakat uç değerlere karşı daha dayanıklı olduğu için medyan çoğu zaman güvenlidir. Kategorik alanlarda en sık sınıf veya `Bilinmiyor` gibi ayrı bir kategori tercih edilebilir.

Eksikliğin kendisi de bilgi taşıyabilir. Örneğin gelir bilgisini paylaşmayan müşterilerin davranışları farklı olabilir. Bu durumda hem değeri doldurmak hem de `gelir_eksik_mi` adlı ikili bir öznitelik oluşturmak yararlıdır.

```python
import pandas as pd

veri['gelir_eksik_mi'] = veri['gelir'].isna().astype(int)
veri['gelir'] = veri['gelir'].fillna(veri['gelir'].median())
```

Bu kod, eksikliği işaretler ve gelir sütunundaki boşlukları medyanla doldurur. Böylece model hem sayısal değeri kullanabilir hem de eksiklik davranışını öğrenebilir.

## Ölçekleme ve kategorik dönüşümler

Mesafe veya gradyan tabanlı algoritmalar değişken ölçeklerinden etkilenir. Bir sütun 0–1, diğeri 0–100.000 aralığındaysa büyük değerli değişken modele gereğinden fazla yön verebilir. Standardizasyon şu formülle yapılır:

$$z = (x - μ) / σ$$

Burada $μ$ ortalama, $σ$ standart sapmadır. Sonuçta değişken yaklaşık sıfır ortalamaya ve birim standart sapmaya taşınır.

Kategorik veriler ise doğrudan sayısal sıraya çevrilmemelidir. İstanbul, Ankara ve İzmir'i 1, 2 ve 3 yapmak, modelde sahte bir büyüklük ilişkisi oluşturur. Sırasız kategoriler için one-hot encoding; doğal sırası bulunan eğitim seviyesi gibi alanlar için ordinal encoding daha uygundur.

## Öznitelik mühendisliği: Veriye anlam katmak

Öznitelik mühendisliği, mevcut sütunlardan problemi daha iyi açıklayan yeni bilgiler üretmektir. Doğum tarihinden yaş, sipariş tarihinden hafta sonu bilgisi veya fiyat ve miktardan toplam harcama türetilebilir:

```python
veri['toplam_harcama'] = veri['fiyat'] * veri['miktar']
veri['siparis_saati'] = veri['siparis_tarihi'].dt.hour
veri['hafta_sonu'] = veri['siparis_tarihi'].dt.dayofweek.isin([5, 6]).astype(int)
```

İyi bir öznitelik yalnızca matematiksel değil, alan bilgisine dayalıdır. Finans uygulamasında gelirden çok borç/gelir oranı anlamlı olabilir:

$$borç\ oranı = toplam\ borç / aylık\ gelir$$

## En kritik tehlike: Veri sızıntısı

Ön işleme adımları yalnızca eğitim verisi üzerinde öğrenilmelidir. Tüm veri kümesinin ortalamasını kullanmak, test verisinden eğitim sürecine bilgi sızdırır. Bu nedenle önce eğitim-test ayrımı yapılmalı; doldurma, ölçekleme ve kodlama işlemleri bir pipeline içinde uygulanmalıdır.

Sonuç olarak kaliteli veri hazırlama; temizleme, eksik değer yönetimi, uygun dönüşüm ve yaratıcı öznitelik üretiminin birleşimidir. Modeli değiştirmeden önce veriye bakmak çoğu zaman en güçlü optimizasyondur: Çünkü iyi özellikler, algoritmanın dünyayı daha anlaşılır görmesini sağlar.
