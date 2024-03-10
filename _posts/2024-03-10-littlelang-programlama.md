---
title:  Little Lang Programlama
author: sonsuz
date: 2024-03-10 11:00:15 +0300
categories: [Program]
tags: [littlelang,programlama,ilginç,yazılım,dil]
---


## “Little Lang” programlama dili

Bu makalede, genelde grafik kullanıcı arayüzleri yapmak için kullanılan Tcl programlama dilini, daha da C’ye benzer yazma stiline uyarlamak için yapılmış bir programlama dili olan “Little Lang”ın tanıtımını, ve bazı örneklerini yapacağım.

“Little Lang”, ve önceki adıyla L, 2006 yılında Larry McVoy’un tasarımlarından esinlenerek küçük bir takım tarafından oluşturulmuş bir programlama dilidir. Yazım tipi C yazım tipine çok yakındır. Web sitesi ise hâlâ yayındadır ve https://www.little-lang.org/ alan adı altındadır.

Little Lang kurulumuna başlamanız için bir Linux ortamına sahip olmanız gerekmektedir. Bu makaleyi yazarken Pardus 23 işletim sistemini kullandım. Eğer bu adımları WSL ortamında denerseniz maalesef başarısız olacaktır.. Başlamak için, sitesinde verilen Git deposundan kaynak kodunu kopyalıyoruz. Aşağıda verilen kodu kopyalayıp mevcut uçbiriminize yapıştırıp çalıştırabilirsiniz.

`git clone --recursive https://github.com/bitkeeper-scm/little-lang.git`

Bu komut tamamlandıktan sonra aşağıdaki komutla mevcut dizini çektiğimiz klasör yapalım. 

`cd little-lang/`

Ardından aşağıda verilen komutu çalıştırarak Little Lang’ı derleyip yükleyebiliriz.

```sh
make 
make install
```

Eğer derlerken “Couldn’t find x” adlı bir hata karşınıza çıkarsa aşağıdaki komut ile gerekenleri yükleyebilirsiniz.

`sudo apt-get install bison flex libxft-dev`

Tüm gerekenler yapıldıktan sonra kendi ortamınızda L komutu ortam değişkenlerine eklenmiş olabilir, yani herhangi bir yerde uçbiriminize L yazdığınızda L konsolu açılabilir, ama bende ortam değişkenlerine eklenmediği için `/opt/little-lang/bin/L` komutunu kullanmam lazım.

Little Lang programlama dilini kullanmaya başlamak için ilk önce bir dosya oluşturmamız lazım. Bir dosya oluşturmak için kullanacağımız en kolay yol, herhangi bir dosya yaratıp başına çalıştırılabilir L dosyasının bulunduğu yolu yazmak olacaktır. Eğer sizin de L kurulumunuz benimkiyle aynı dizinde ise aynısını kendi dosyanıza geçirebilirsiniz.

`#!/opt/little-lang/bin/L`

Bu yazının altına yazdığımız her şey L programlama dilinde yazılması gerekiyor. Şimdi en basit olan konsola yazı yazma kısmından başlayalım. L programlama dilinde bir yazı yazmak için “puts” adlı fonksiyonu kullanıyoruz.

```
#!/opt/little-lang/bin/L 
puts(“General Mobile”); 
```

Göründüğü gibi kısa bir kod yazabiliriz. Basit programlama mantıklarını kavradıysanız çift tırnak veya tek tırnaklar arasına gelen kelimelere “string” adı verilir. Bu stringler içinde yazı taşırlar. Puts fonksiyonunun içine bir string koyarsak bu string’in içinde yazanları uçbirime yazacaktır. Son olarak da, puts fonksiyonundan sonra noktalı virgül koyup, bu satırın bittiğini belirtiyoruz. Bu dosyayı çalıştırmak için ilk önce uçbirimimizde bu dosyayı çalıştırılabilir yapmamız lazım. Aşağıdaki komutları kendi dosyanıza göre geçirip çalıştırabilirsiniz.

```
loongruige@pardus-e5470:~/Masaüstü$ chmod +x ./little loongruige@pardus-e5470:~/Masaüstü$ ./little 
General Mobile
```

Gördüğünüz üzere bu işlemleri yaparak ilk L programımızı çalıştırdık. Şimdi biraz daha gelişmiş kısımlara geçelim. C dilinin aksine, illaki yazdığınız kodları bir “main” fonksiyonu içerisine koymak zorunda değilsiniz. Ama eğer bir main fonksiyonu oluşturursanız, bu fonksiyon, dışındaki komutlar sonrasında çalıştırılacaktır. Bunu bir örnekle deneyelim.

```
#!/opt/little-lang/bin/L 
puts(“General Mobile GM 22”) 
void main() { 
puts(“General Mobile GM 22 Pro”); 
} 
puts(“General Mobile GM 22 Plus”); 
```

Bu komutu çalıştırınca karşımıza, yazdığımız sırada değil, ilk önce “main” dışındaki fonksiyonlar sırayla, ardından da main fonksiyonunun içerisindeki fonksiyonlar çalıştırılacak.

```
loongruige@pardus-e5470:~/Masaüstü$ ./little 
General Mobile GM 22 
General Mobile GM 22 Plus 
General Mobile GM 22 Pro 
```

Gördüğünüz üzere yazdığımız kod sıralı olmasa da başka yöntemlerle sıralayabildik.

## Little Lang Değişkenler ve Veri Türleri

Şimdi hızlıca değişkenlere geçelim. L’de 3 önemli değişken tipi vardır. String, int ve float. String yazıları, int tam sayıları ve float da virgüllü sayıları taşır. Aşağıda verilen küçük örnekle birkaç tane değişken atayalım ve uçbirime yazdıralım.

```
#!/opt/little-lang/bin/L 
void main() { 
string marka = “General Mobile”; 
int kurulus = 2005 
float milyar_kullanici = 7.924; 
puts(marka); 
puts(kurulus); 
puts(milyar_kullanici); 
}
```

Çıktı:

```
loongruige@pardus-e5470:~/Masaüstü$ ./little 
General Mobile 
2005 
7.924
```

Puts fonksiyonunda bir string yazarken içine bir değişken eklemek için yazacağımız stringin içinde dolar işareti ve süslü parantezler ${} içine yazarak hedefimize ulaşabiliriz. Şimdi, bunu yazdırdığımız değerlerin neye karşılık geldiğini belirtmek için uygulayalım.

```
#!/opt/little-lang/bin/L 
void main() { 
string marka = “General Mobile”; 
int kurulus = 2005; 
float milyar_kullanici = 7.924 
puts(“Marka: ${marka}”); 
puts(“Kuruluş tarihi: ${kurulus}”); 
puts(“Kullanıcı sayısı (2025): ${milyar_kullanici} milyar”); }
```

Çıktı:

```
loongruige@pardus-e5470:~/Masaüstü$ ./little 
Marka: General Mobile 
Kuruluş tarihi: 2005 
Kullanıcı sayısı (2025): 7.924 milyar
```

## Little Lang İşlemler

Böylece bunu da başarmış olduk. Şimdi size operatörlerin nasıl çalıştığını göstereceğim. L dilindeki operatörler diğer dillerdeki operatörlerle neredeyse aynı. eklemek için +, eksiltmek için - gibi.

```
#!/opt/little-lang/bin/L 
void main() { 
int kurulus = 2005; 
int bu_yil = kurulus + 19; 
int iki_yil_once = bu yil - 2; 
float baya_zaman_once = kurulus / 2.0; 
int baya_zaman_sonra = kurulus * 3; 
puts(kurulus); 
puts(bu_yil); 
puts(iki_yil_once); 
puts(baya_zaman_once); 
puts(baya_zaman_sonra); 
}
```

Çıktı:

```
loongruige@pardus-e5470:~/Masaüstü$ ./little 
2005 
2024 
2022 
1002.5 
6015
```

Bu örnekte, bir sayıya farklı işlemler uyguladık. Fark ettiyseniz bölüm işleminde 2 yerine 2.0 kullandık. Eğer bölme işlemlerinde noktalı sayı kullanmazsak değer otomatik olarak int sayılır.

## Little Lang Karşılaştırmalar

Karşılaştırma yapmak için if fonksiyonunun kullanılması gerekir. Bu karşılaştırmayı yapmak için `==, !=, => ve =<` gibi operatörler kullanabiliriz. Şimdi hemen küçük bir örnek yazalım.

```
#!/opt/little-lang/bin/L 
void main(){ 
int giris = 2005; 
if (giris < 0) { 
puts(“Sayı negatif.”); 
} 
else if (giris > 0) { 
puts(“Sayı pozitif.”); 
} 
else { 
puts(“Sayı sıfır.”); 
} 
if (giris % 2 == 0) { 
puts(“Sayı çift”); 
} 
else if (giris % 2 != 0) { 
puts(“Sayı tek.”); 
} 
}
```

Çıktı:

```
loongruige@pardus-e5470:~/Masaüstü$ ./little 
Sayı pozitif. 
Sayı tek.
```

Bu örnekte ilk önce bir sayı sıfırdan küçükse negatif olduğunu, sıfırdan büyükse pozitif olduğunu ve ikisi de değilse sayının sıfır olduğunu yazdırdık. Ardından ise eğer sayının iki ile bölümünden sıfır çıkıyorsa çift, sıfır çıkmıyorsa da tek olduğunu yazdırdık. Örnek olarak 2005 sayısını denediğimizde ise başarılı bir şekilde pozitif ve tek olduğunu yazdırdı.

## Little Lang Döngüler

Son olarak, döngülere bir göz atalım.

```
#!/opt/little-lang/bin/L 
void main(){ 
int i = 5 
while ( i > 0 ) { 
puts(i); 
i –; 
} 
}


#!/opt/little-lang/bin/L 
void main() { 
for (int i = 5; i > 0; i –) { 
puts(i); 
} 
}
```

Çıktı:

```
loongruige@pardus-e5470:~/Masaüstü$ ./little 
5 
4 
3 
2 
1
```

Yukarıda verilen şekilde aynı sonucu veren iki döngü yaptık. While döngüsünde, verilen koşul doğru olana kadar verilen kod çalışır. For döngüsü için ise değişken, ilk kısımda başlatılır. İkinci kısımda ise koşul belirtir. Üçüncü kısımda ise döngünün değişkeninin nasıl etkileneceği eklenir. Bu şekilde, L dilinde döngüler de yapmış olduk.

Bu aşırı yüzeysel yazımı okuduğunuz için teşekkürler. Eğer Little Lang hakkında daha fazla öğrenmek isterseniz https://www.little-lang.org/index.html adresinden daha fazla bilgi alabilirsiniz.

[Efe Timur Turan](https://www.github.com/loongruige)
