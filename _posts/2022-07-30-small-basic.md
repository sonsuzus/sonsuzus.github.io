---
title: Small Basic Programlama
author: Sonsuz
date: 2022-07-30 20:55:00 +0300
categories: [Program, Basic]
tags: [programlama,basic,small basic]
---

Bilgisayar Programlaması, programlama dilleri kullanılarak, bilgisayar yazılımlarının oluşturulması
süreci olarak tanımlanır. Tıpkı bizim İngilizce’yi, İspanyolca’yı veya Fransızca’yı konuşup anlamamız
gibi, bilgisayarlar da belirli dillerde yazılmış programları anlayabilirler. Bunlar programlama dilleri
olarak adlandırılır. Başlangıçta, yalnızca birkaç tane programlama dili vardı ve bunların öğrenilmesi
ve kavranması oldukça kolaydı. Ancak, bilgisayarlar ve yazılımlar giderek sofistike hale geldikçe,
programlama dilleri de hızla gelişti ve daha karmaşık kavramları içerir hale geldi. Bunun sonucu olarak,
şu anda çoğu programlama dilinin ve kavramlarının kavranması yeni başlayan birisi için oldukça zorlayıcı
durumdadır. Bu da, insanların bilgisayar programlamasını öğrenme veya gerçekleştirmeye yönelik
girişimlerinde cesaretlerini kırmaya başladı.

Small Basic, programlamayı yeni başlayanlar için son derece kolay, anlaşılır ve eğlenceli hale getirmek
üzere tasarlanmış olan bir programlama dilidir. Small Basic’in amacı, engeli aşağıya çekmek ve şaşırtıcı
bilgisayar programlaması dünyasına bir atlama taşı olarak görev yapmaktır.

## İlk Programımız
Artık Small Basic Ortamı ile tanıştığınıza göre, onu kullanarak programlama yapmaya başlayacağız.
Yukarıda söz ettiğimiz gibi, düzenleyici programlarımızı yazdığımız yerdir. Bunu yapmak için, önce
aşağıdaki satırı düzenleyiciye yazın.
```
TextWindow.WriteLine("Merhaba Dünya")
```

Bu bizim ilk Small Basic programımız.

Yeni programımızı yazdığımıza göre, şimdi onu çalıştıralım ve neler olduğunu görelim. Programımızı
araç çubuğu üzerindeki Run (Çalıştır) düğmesine basarak veya klavyenin üzerindeki F5 kısayol tuşunu
kullanarak çalıştırabiliriz. Her şey yolunda giderse, programımızın aşağıdaki sonucu verecek şekilde
çalışması beklenir.

Tebrikler! İlk Small Basic programınızı yazdınız
ve çalıştırdınız. Bu oldukça küçük ve basit bir
program, ancak yine de gerçek bir bilgisayar
programcısı olma yolunda büyük bir adım!
Şimdi, daha büyük programlar oluşturma
konusuna geçmeden önce, söz etmemiz gereken
bir detay daha var. Az önce neler olduğunu
anlamamız gerekiyor – bilgisayara tam olarak
ne dedik ve ne yapacağını nasıl bildi? Bir sonraki
bölümde, bunu anlayabilmek için, yazdığımız
programı analiz edeceğiz.

Artık ilk programımızı anladığınıza göre, buna bazı renkler ekleyerek daha süslü hale getirelim.
```
TextWindow.ForegroundColor = "Yellow"
TextWindow.WriteLine("Merhaba Dünya")
```

### Programımızda Değişkenlerin kullanılması
Programımız genel “Merhaba Dünya?” yerine kullanıcının ismiyle birlikte “Merhaba” deseydi, daha hoş
olmaz mıydı? Bunu yapmak için, önce kullanıcıya ismini sormamız ve sonra da bunu bir yerde saklayarak,
kullanıcının ismiyle birlikte “Merhaba” metnini yazdırmamız gerekir. Bunu nasıl yapabileceğimizi görelim:
```
TextWindow.Write("İsminizi Girin: ")
name = TextWindow.Read()
TextWindow.WriteLine("Merhaba " + name)
```

### Değişkenlerin isimlendirilmesi ile ilgili kurallar
Değişkenlerin onlarla bağlantılı isimleri vardır ve onları bu şekilde tanırsınız. Bu değişkenlerin
isimlendirilmeleriyle ilgili belirli basit kurallar ve gerçekten iyi kılavuz bilgiler vardır. Bunlar:

1. İsim bir harfle başlamalı ve if, for, then, vs. gibi kelimelerle çakışmamalıdır.
2. Bir isim, harflerin, sayıların ve altçizgilerin herhangi bir kombinasyonundan oluşabilir.
3. Değişkenleri anlamlı bir şekilde isimlendirmek faydalıdır – değişkenler istendiği kadar
uzun olabileceği için, amaçlarını açıklayan değişken isimleri kullanın.

### Sayılarla Oynamak
Biraz önce kullanıcının ismini saklamak için değişkenleri nasıl kullanabileceğinizi gördük. Bundan
sonraki birkaç programda, değişkenlerde sayıları nasıl saklayabileceğimizi ve işleyebileceğimizi
göreceğiz. Gerçekten basit bir programla başlayalım:
```
number1 = 10
number2 = 20
number3 = number1 + number2
TextWindow.WriteLine(number3)
```

Devamı için [Small Basic Kitabı](https://sonsuzus.github.io/dosya/Small_Basic%20kitap.pdf)
