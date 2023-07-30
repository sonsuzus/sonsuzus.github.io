---
title:  Program oluşturma
author: sonsuz
date: 2023-07-30 21:32:39 +0300
categories: [Program,C]
tags: [programlama,c,ide]
---


## Bir C programının oluşturulması, derlenmesi ve çalıştırılması

Tercih ettiğimiz bir IDE (Entegre Geliştirme Ortamı)'yi bilgisayarımıza kurarak sistemi hazır hale getirdikten sonra, çalışan .exe uzantılı bir program elde edebilmemiz için, programı yazılması, derlenmesi ve kütüphane dosyaları ile birleştirilmesi işlemlerini gerçekleştirmemiz gerekir:

Bu safhaları sıra ile ele almadan önce, .exe uzantılı bir program ifadesini kısaca açıklamaya çalışalım:

İşletim sistemi, uzantısı .EXE, .COM ve .BAT olan dosyaları, komut satırında iken adını yazıp ENTER tuşuna bastığımızda veya Windows Gezgini benzeri bir ara yüz üzerinde çift tıkladığımızda çalıştırır. Diğer uzantılı dosyalara ise çift tıkladığımızda ilgili program yoluyla açar.

Yukarıdaki üç safhayı gerçekleştirdiğimizde .EXE uzantılı çalışan bir dosya elde edebiliriz.

## Programın yazılması

İlk safha olan program yazımını gerçekleştirmek için, bilgisayarımıza yüklediğimiz IDE'nin içinde bulunan metin düzenleyicisini veya farklı bir metin düzenleyicisi kullanarak program kodlarını bir dosyaya yazmamız gerekir. Bu dosya ilk bakışta normal bir metin dosyası ile aynı nitelikleri taşır. Bir C programı içeren bu dosyaya kaynak dosya adı verilir. Bu dosyayı .c uzantısı ile kaydetmemiz gerekir. Çünkü, C programlama dilinde bütün kaynak dosyaları .c uzantılıdır. Eğer IDE'nin içindeki metin düzenleyici ile programı yazarsak, uzantı vermesek bile, program otomatik olarak dosyaya .c uzantısı verir. Bu safhada, elimizde program kodlarını içeren bir dosya hazırlanmış durumdadır.

CodeBlocks IDE kullandığımızda yazdığımız basit bir programın ekran görüntüsü aşağıdaki şekilde olacaktır:

![](cprog/progolus01.png)

Bilgisayarımızda, deneme adlı bir proje oluşturduğumuzda, proje dizin görüntüsü ve içeriği aşağıdaki şekilde olacaktır:

![](cprog/progolus02.png)

## Programın derlenmesi

İkinci safha programınızın derlenme safhasıdır. Kaynak dosya IDE derleyicisi (Compiler) ile derlendiğinde, programımız makine kodlarına çevrilerek .o uzantılı ikinci bir dosya oluşturulur. Bu dosya da henüz çalıştırılmaya hazır değildir.

![](cprog/progolus03.png)

Proje dizini altında main.o dosyasının yer aldığı dizin aşağıda gösterilmektedir:

![](cprog/progolus04.png)

## Programın kütüphane dosyaları ile birleştirilmesi

Üçüncü ve son safha ile elde edilen .o uzantılı dosyanın kütüphane dosyaları ile birleştirilmesi safhasıdır. Bu safhada, IDE içinde bulunan bağlayıcı (Linker) .o uzantılı dosya ile kütüphane fonksiyonlarının bulunduğu dosyaları birleştirerek .EXE uzantılı üçüncü bir dosya oluşturur. Bağlayıcı, derleyici tarafından object dosyasına çevrilen dosya veya dosyalar arasında bir bağ oluşturarak çalıştırılabilen tek bir .exe dosya elde eder.

Günümüzde yaygın olarak kullanılan IDE'lerde, derleme ve bağlama işlemleri sadece tek bir komutla ("Build") gerçekleştirilmektedir.

![](cprog/progolus05.png)

Sonuç olarak, yazılan tek bir program için IDE üç farklı dosya oluşturur. Eğer main.c adlı bir kaynak dosya oluşturur ve gerekli işlemleri tamamlarsak, aşağıda gösterilen 3 dosyayı elde ederiz:

```c
main.c
main.o
deneme.exe
```

C kodlarının yer aldığı main.c dosyası ile aynı isme sahip main.o adlı bir object dosyası oluşturulurken, elde edilen deneme.exe dosyası adını proje isminden almaktadır.

## Programın çalıştırılması

Oluşturulan .exe dosyasını direkt olarak derleyicinin içinden, Windows Explorer üzerinden çift tıklayarak veya dosya adını komut satırında yazarak 3 farklı yöntemle çalıştırabiliriz.

1. Direkt olarak derleyicinin içinden çalıştırma

![](cprog/progolus06.png)

2. Windows Explorer üzerinde çift tıklayarak çalıştırma

![](cprog/progolus07.png)

3. Komut satırından çalıştırma

Komut istemi penceresinde, programın bulunduğu dizine geçiş yaptıktan sonra, .exe dosyası adı olan deneme.exe adını yazıp ENTER tuşuna basarak programı çalıştırabiliriz.

![](cprog/progolus08.png)

## Derleme, bağlama ve çalışma zamanı hataları

Kaynak dosya yazılırken herhangi bir hata yazım hatası yapılırsa, program derlendiğinde derleyici hata mesajı verir. Bu hata mesajları genellikle C dilinin kurallarına aykırı olan yazım hatalarıdır. Sonunda noktalı virgül (;) olmayan bir işlem satırı, fonksiyonların başlangıcını ve sonunu gösteren ({}) işaretlerinin eksikliği, komutların hatalı olarak yazılması ve tırnak işareti (") ile kapatılmamış bir karakter dizisi bu hatalara örnek olarak gösterilebilir.

Bazen derleyici programımızı derler, ancak derleme işleminden sonra size uyarı mesajları verir. Bu mesajlar programın çalışmayacağını göstermez, ancak programcı olarak bu mesajları inceleyerek çalışma anında bir sorun yaratıp yaratmayacağı konusunda karara varmamızda fayda vardır.

Program bazen hatasız olarak derlenir, ancak bağlayıcı hatası verebilir. Bununda değişik sebepleri olabilir. Ancak bu hatalarda kolaylıkla düzeltilebilir.

En zor olarak tespit edilen hatalar, derleme ve bağlama işlemi normal olarak sonuçlandıktan sonra, elde edilen .exe dosya çalıştırılmak istendiğinde meydana gelen ve çalışma zamanı hataları (runtime error) olarak adlandırılan hatalardır.

C programlama dilinde çalışma zamanı hataları kontrolü yoktur. Bu hataların kontrolü programlayıcı tarafından yapılmalıdır.

Yazılan programların kaynak kodları kısa olduğu ve derleme süresi az olduğu sürece, kodlar tek bir dosyada yer alır. Ancak, kod satırları ve derleme süresi artınca, kodların birden fazla kaynak dosyada sınıflandırılarak düzenlenmesi, hem programın okunurluğunun artması hem de tek bir dosya üzerinde yapılan değişikliğin derlenmesi ile derleme zamanının kısaltılması açısından daha faydalıdır.
