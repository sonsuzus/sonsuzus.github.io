---
title: Java ve moteJ kullanarak Nintendo Wii kumandalarından veri alma 
author: sonsuz
date: 2023-11-16 16:02:41 +0300
categories: [Program,Java]
tags: [veri,java,motej,nintendo wii]
---



Nintendo Wii, 2006 yılında tanıtılan bir ev tipi oyun konsoludur. Bu oyun konsolunun, ana makineyle Bluetooth kullanarak veri alışverişi yapan kumandaları vardır. Bu kumandada kızılötesi sensör ve ivmeölçer mevcuttur. Daha sonra, Nintendo tarafından tanıtılan Wii Sports Resort adlı oyunla beraber Wii Motion Plus adlı bir uzantı tanıtılmıştır. Bu uzantı, “Tuning fork gyroscope” adı verilen bir jiroskopa sahiptir ve bu jiroskop, daha hassas dönme bilgisi içerir. 2009’da Volker Fritzsch tarafından geliştirilen “motej” kütüphanesi ile bu kumandalara bağlantı sağlanabilir ve belirli veriler alınabilir. 
Daha önce yapmış olduğum “Roller Game” adlı projede motej kütüphanesini kullandım, ve bu sayede kumandalardan aldığım ivmeölçer verilerini LibGDX oyun motoru ile kullanarak basit bir oyun geliştirdim. Bu yazıda ise motej kütüphanesini en kolay şekilde nasıl kullanabileceğimizi açıklayacağım.

Başlamadan önce, bilgisayarınızda bir Bluetooth modülü olması lazım, ve bunun yanında Bluetooth sürücülerinizin L2CAP uyumlu olması lazım. Eğer Windows’ta Bluetooth modülünüzle uyumlu bir L2CAP sürücüsü, ya da generic bir L2CAP sürücüsü bulamadıysanız, bu projeyi Linux tabanlı bir işletim sisteminde yapmanızı öneririm. Ben bu projeyi yaparken Pardus 21 XFCE versiyonunu kullandım, ama siz istediğiniz herhangi bir distro’yu kullanabilirsiniz.

İlk önce SourceForge sayfasından gerekli JAR dosyasını yükleyelim. Ardından, eğer IntelliJ gibi bir IDE kullanılıyorsa proje ayarlarından, kullanılmıyorsa classpath şeklinde kütüphaneyi içe aktaralım. Bundan sonra basit bir kod çalıştırarak kütüphaneyi teyit edelim.

```java
MoteFinder bulucu = MoteFinder.getMoteFinder();
```

Eğer kütüphane doğru bir şekilde içe aktarıldı ise, bu kodun çalışması lazım. Çalışmaktan bahsettiğim ise hata vermeden çalışması. Çünkü şu an sadece bir kumanda bulucu tanımladık, ama başka bir şey eklemedik. Bununla kumandaları bulmak ve bağlanmak için ilk önce bu bulucuya bir dinleyici eklememiz gerekir. Bunu aşağıdaki şekilde ekleyebiliriz:


```java
ArrayList<Mote> kumandalar = new ArrayList<>(); 
MoteFinderListener dinleyici = new MoteFinderListener() { 
    public void moteFound(Mote mote) { 
    System.out.println("Kumanda bulundu."); 
    kumandalar.add(mote); 
    } 
};
```

İlk satırda, “kumandalar” adlı bir dizi oluşturuyoruz. Bu dizide, bağlanılan kumandaları tutacağız. Bir sonraki satırda yeni bir MoteFinderListener dinleyicisi tanımlıyoruz ve “moteFound” adlı fonksiyona, bu kumandayı bulduğunda dair bir mesaj bırakmasını, ve biraz önce oluşturduğumuz diziye bu kumandayı eklemesini yazıyoruz. Şimdi de bu dinleyiciyi tanımladığımız bulucuya ekleyelim.

```java
bulucu.addMoteFinderListener(dinleyici);
// Bu şekilde bulucumuza dinleyicimizi ekledik. Şimdi aramaya başlayabiliriz. 
bulucu.startDiscovery(); 
Thread.sleep(30000l); 
bulucu.stopDiscovery();
```

Burada ilk satırda Bluetooth keşfini başlatıyoruz. Böylece bulucu, etraftaki Bluetooth aygıtlarını tarayacak ve Wii kumandalarının kod adı ve aynı zamanda Bluetooth cihaz adı olan “Nintendo RVL CNT-001” adlı cihazları bulup, eklediğimiz dinleyicideki kodu çalıştıracak. Wii kumandalarının içinde Motion Plus uzantısı bulunduran 2. jenerasyon kumandaları (Wii Remote Plus) bulunca ise ismine ve bağlanınca geri döndürdüğü veriye göre otomatik olarak Motion Plus özelliklerini aktif ediyor. Aynı şekilde normal bir Wii kumandasına eklenen Motion Plus uzantısını yazılımsal bir şekilde kontrol edebilir ve bu şekilde Motion Plus özelliklerini kullanabilirsiniz. Tabii, ben bu yazıda çok detaya girmeyip yüzeysel ve basit özellikleri göstereceğim.

Bu fonksiyonda keşif başladıktan sonra Thread kullanarak yarım dakika bekliyor ve ardından keşfi durduruyor. Bu şekilde kodu bloke edeceği için bu keşif fonksiyonlarını başka bir Thread’da yapıp onu çalıştırabilirsiniz. Şimdi, keşif bittikten sonra kumandaların 1. ve 3. ışığını yakıp kumandayı titreştirici kısa bir kod yazalım. Burası, “stopDiscovery” fonksiyonundan sonra gelecek.

```java
for (i = 0; i < kumandalar.size(); i++) { 
    kumandalar.get(i).setPlayerLeds([true, false, true, false]); 
    kumandalar.get(i).rumble(2000l); 
}
```

Bu kod parçası ile bağlanan tüm kumandalar, yan, “kumandalar” adlı dizinin boyutu kadar bir için döngüsü oluşturuyoruz, ve bu döngüde, sırası gelen kumandanın birinci ve üçüncü LED ışığını bir Boolean dizisi kullanarak açacağız. Ardından 2000 milisaniye boyunca kumandayı titreştireceğiz. Son olarak ise kumandalardan buton verileri alıp, üzerindeki butonlar basılınca konsola birşey yazdırmasını yapacağız.

```java
CoreButtonListener anaDugmeDinleyici = new CoreButtonListener(CoreButtonEvent olay) { if (olay.isButtonAPressed()) { 
System.out.println("A düğmesi basıldı!"); 
} 
if (olay.isButtonBPressed()){ 
    System.out.println("B düğmesi basıldı"); 
} 
if (olay.isDPadUpPressed()){ 
    System.out.println("D-Pad yukarı basıldı!"); 
} 
// ( . . . ) 
} 
kumandalar.get(0).addCoreButtonListener(anaDugmeDenetleyici);
```

İlk önce, argümanı “CoreButtonEvent” olan bir CoreButtonListener tanımlıyoruz. CoreButtonEvent, içinde o olayda basılan ana düğmeleri bulunduruyor. Bu dinleyicinin içinde ise farklı “if” karşılaştırmaları kullanarak basılan butonlara göre konsola yazı yazdırıyoruz. Tek bir eğer karşılaştırmasında “else if” kullanmamamızın sebebi ise, aynı anda birden fazla düğme basıldığında, sadece ilk karşılaştırmadaki düğmenin mesajının yazılmasıdır. Bu kod sadece ilk basıldığında mesaj yazmayacaktır, düğme bırakılıncaya kadar mesaj yazmaya devam edecektir, bu yüzden basılan butonlar için bir sınıf oluşturup daha önce basıldığını ve şimdi basılıp basılmadığını kontrol eden bir kod parçası
yazabilirsiniz. Ardından, bu CoreButtonListener’i kumandalardan birine ekliyoruz. Bir için döngüsüyle bu dinleyiciyi kumandaların hepsine de ekleyebilirsiniz, ama bu sadece örnek olduğu için bir tanesine ekledim. Böylece kumanda objesi, kumandadan gelen düğme sinyallerine tepki verecek ve ardından yazdığımız kod çalışacaktır.


Böylece, moteJ kütüphanesinin temellerini anlatmış bulunuyorum. Şu ana kadar yazılmış kod:

```java
ArrayList<Mote> kumandalar = new ArrayList<>(); 
MoteFinderListener dinleyici = new MoteFinderListener() { 
public void moteFound(Mote mote) { 
    System.out.println("Kumanda bulundu."); 
    kumandalar.add(mote); 
    } 
}; 
CoreButtonListener anaDugmeDinleyici = new CoreButtonListener(CoreButtonEvent olay) { if (olay.isButtonAPressed()) { 
    System.out.println("A düğmesi basıldı!"); 
} 
if (olay.isButtonBPressed()){ 
    System.out.println("B düğmesi basıldı"); 
} 
if (olay.isDPadUpPressed()){ 
    System.out.println("D-Pad yukarı basıldı!"); 
} 
// ( . . . ) 
} 
MoteFinder bulucu = MoteFinder.getMoteFinder(); 
bulucu.addMoteFinderListener(dinleyici); 
bulucu.startDiscovery(); 
Thread.sleep(30000l); 
bulucu.stopDiscovery(); 
for (i = 0; i < kumandalar.size(); i++) { 
    kumandalar.get(i).setPlayerLeds([true, false, true, false]); 
    kumandalar.get(i).rumble(2000l); 
    kumandalar.get(i).addCoreButtonListener(anaDugmeDinleyici); 
} 
```