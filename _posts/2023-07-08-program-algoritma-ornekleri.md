---
title: Programlama ve algoritma ile problem çözme örnekleri
author: sonsuz
date: 2023-07-08 00:55:00 +0300
categories: [Program, Algoritma]
tags: [algoritma,soru,programlama,problem,teknik]
---

## Problem Çözme

Problem çözmede, soruna hemen girişmek yerine, dikkatli ve sistematik yaklaşım ilke olmalıdır. Problem iyice anlaşılmalı ve mümkün olduğu kadar küçük parçalara ayırılmaladır.

Descartes tarafından "Discourse on Method" isimli kitabında anlatılan problem çözme teknikleri;

1. Doğruluğu kesin olarak kanıtlanmadıkça, hiçbir şeyi doğru olarak kabul etmeyin; tahmin ve önyargılardan kaçının.
2. Karşılaştığınız her güçlüğü mümkün olduğu kadar çok parçaya bölün.
3. Düzenli bir biçimde düşünün; anlaşılması en kolay olan şeylerle başlayıp yavaş yavaş daha zor ve karmaşık olanlara doğru ilerleyiniz.
4. Olaya bakışınız çok genel, hazırladığınız ayrıntılı liste ise hiçbir şeyi dışarıda bırakmayacak kadar kusursuz ve eksiksiz olsun.

## Algoritmalar

Belirli bir görevi yerine getiren sonlu sayıdaki işlemler dizisidir.

İ.S. 9.yy da İranlı Musaoğlu Horzumlu Mehmet (Alharezmi adını araplar takmıştır) problemlerin çözümü için genel kurallar oluşturdu.    Algoritma Alharezmi'nin Latince okunuşu.

Her algoritma aşağıdaki kriterleri sağlamalıdır.

1. Girdi: Sıfır veya daha fazla değer dışarıdan verilmeli.
2. Çıktı: En azından bir değer üretilmeli.
3. Açıklık: Her işlem (komut) açık olmalı ve farklı anlamlar içermemeli.
4. Sonluluk: Her türlü olasılık için algoritma sonlu adımda bitmeli.
5. Etkinlik: Her komut kişinin kalem ve kağıt ile yürütebileceği kadar basit olmalıdır.

Not: Bir program için 4. özellik geçerli değil. işletim sistemleri gibi program sonsuza dek çalışırlar .

## Örnekler

- 1'den 100'e kadar olan sayıların toplamını veren algoritma.
    
    1. Toplam T, sayılar da i diye çağırılsın.
    2. Başlangıçta T'nin değeri 0 ve i'nin değeri 1 olsun.
    3. i'nin değerini T'ye ekle.
    4. i'nin değerini 1 arttır.
    5. Eğer i'nin değeri 100'den büyük değil ise 3. adıma git.
    6. T'nin değerini yaz.
	
Algoritmaların yazım dili değişik olabilir. Günlük konuşma diline yakın bir dil olabileceği gibi simgelere dayalı da olabilir.    
Akış şeması eskiden beri kullanıla gelen bir yapıdır. Algoritmayı yazarken farklı anlamlar taşıyan değişik şekildeki kutulardan yararlanılır.    Yine aynı amaç için kullanılan programlama diline yakın bir (sözde kod = pseudo code) dil , bu kendimize özgü de olabilir, kullanılabilir.

Aynı algoritmayı aşağıdaki gibi yazabiliriz.

1. T=0 ve i=0
2. i'nin değerini T'ye ekle.
3. i'yi 1 arttır.
4. i<101    ise    2.adıma git.
5. T'nin değerini yaz.

- İki tamsayının çarpma işlemini sadece toplama işlemi kullanarak gerçekleyin.

Girdi : iki tamsayı

Çıktı : sayıların çarpımı

1.  a ve b sayılarını oku
2.  c =0
3.  b>0 olduğu sürece tekrarla
    3.1. c=c + a
	3.2. b = b-1
4. c değerini yaz ve dur

- İki tamsayının bölme işlemini sadece çıkarma işlemi kullanarak gerçekleyin. Bölüm ve kalanın ne olduğu bulunacak.

1. a ve b değerlerini oku
2. m=0
3. a>=b olduğu sürece tekrarla
    3.1  a=a-b 
    3.2   m = m + 1
4. kalan a ve bölüm m 'yi yaz

- 100 tane sayıyı okuyup, ortalamasını bul
    1.  T=0,	i=0
    2.  i<101 olduğu sürece tekrarla
        2.1      m değerini oku
        2.2   T = T + m
        2.3   i = i + 1
    3.  T = T / 100
    4.  Ortalama T ‘yi yaz
    5.  Dur

- Bir sınava giren öğrencilerin not ortalamasının hesaplanması
    1.  Tüm sınav kağıtlarını inceleyip notların toplamını hesapla
    2.  Ortalamayı notların toplamını incelenen sınav kağıdına bölerek hesapla
    3.  Ortalamayı yaz.

    1.  Notların toplamını ve incelenen sınav kağıdı sayısını sıfır kabul et
    2.  Sıradaki sınav kağıdının notunu notların toplamına ekle 
    3.  İncelenen sınav kağıdı sayısını Bir arttır
    4.  İncelenecek sınav kağıdı var ise 2. Adıma git
    5.  Ortalamayı notların toplamını incelenen sınav kağıdına bölerek hasapla
    6.  Ortalamayı yaz

    1.  Notların toplamını ve incelenen sınav kağıdı sayısını sıfır kabul et
    2.  Her bir sınav kağıdı için
        2.1.  Sıradaki sınav kağıdının notunu notların toplamına ekle
        2.2.  İncelenen sınav kağıdı sayısını bir arttır
    3.  Ortalamayı notların toplamını incelenen sınav kağıdına bölerek hesapla
    4.  Ortalamayı yaz
