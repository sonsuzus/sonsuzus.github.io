---
title:  Python Programlamaya Giriş 1 – İlk Adımlar
author: sonsuz
date: 2023-06-10 10:03:09 +0300
categories: [Program,Python]
tags: [python,temel,kurulum]
math: true
---
## Kurulum


Python programlarını yazmak için gereken şeyler çok az: Sadece bir metin editörüne (text editor) ve Python yorumlayıcısına ihtiyacınız var. Metin editörü ile programı yazarsınız, ve yorumlayıcıya bu dosyayı okuyup çalıştırmasını söylersiniz. Hepsi bu.


Metin editörü olarak notepad, emacs, gedit gibi programlar kullanılabilir. Ancak Word, LibreOffice Writer gibi kelime işlemcileri kullanamazsınız. Bunlar yazıları kendilerine özgü bir biçimde saklarlar ve Python yorumlayıcısı bu dosyaları okuyamaz.


Python yorumlayıcısını [Python resmi sayfasından](https://www.python.org/) indirip kolayca kurabilirsiniz. Her platformda (Windows, MacOS, Unix, Linux,…) çalışabilen bir Python derleyicisi vardır. Bir makinede yazdığınız bir Python programını, gerekli yorumlayıcının mevcut olduğu başka bir makinede, farklı bir işletim sistemi kullansa bile, çalıştırabilirsiniz.


Python yorumlayıcısı sisteminizde mevcut bile olabilir. Linux kullanıyorsanız zaten kuruludur çünkü birçok sistem programı Python kullanır. Ubuntu, Fedora vs gibi paket yönetim sistemi olan bir dağıtım kullanıyorsanız, paket yöneticisi aracılığıyla kurmanız daha iyi olabilir.


Bir editör ve yorumlayıcı, program yazmanız ve çalıştırmanız için yeterlidir. Gerisi teferruattır, ve başlangıç için şart değildir. Ama Python bazı geliştirme araçları size hız ve kolaylık sağlar. Söz gelişi IDLE, Spyder, PyCharm gibi bir IDE (bütünleşik geliştirme ortamı) kullanmayı tercih edebilirsiniz. Bunlardan daha sonra bahsedeceğiz.


Python kurmak için başka bir yol [Anaconda](https://www.anaconda.com/download/) veya [Canopy](https://www.enthought.com/product/canopy/) gibi Python dağıtımları. Bunların en büyük avantajı, ileri seviye kullanıcıların ihtiyaç duyduğu modüllerin, sürümleri birbiriyle uyumlu olacak şekilde düzenlenerek bir araya getirilmiş olmaları. Spyder, Jupyter Notebook gibi yazılımlar da bu dağıtımlara dahil. Tabii bu modülleri ayrı ayrı da kurabilirsiniz.

## Basit etkileşimli kullanım


Python’u işletim sisteminizin komut yorumlayıcısı ile (DOS command prompt veya shell/terminal) çalıştırıp etkileşimli olarak kullanabilirsiniz. Dolar ($) işareti komut yorumlayıcısının işareti. Aşağıdaki ekran görüntüsünde bazı örnekler görülüyor. `>>>` işareti Python’un bir komut beklediğini gösteriyor. Komutu yazdıktan sonra işlenmesi için Enter tuşuna basın.

Python etkileşimli halde çalışırken, bir ifadeyi yazıp Enter’a basmanız ifadenin değerinin ekrana yazılmasını sağlar. Meselâ “2+2” yazıp Enter’e bastığımızda “4” yazması sadece etkileşimli modda mümkün. Bir betiğin (programın) içinde “2+2” ifadesinin değeri hesaplanır, ama ekrana basılmaz. Betik içindeki bir ifadenin değerinin ekrana basılmasını istiyorsanız için `print()` fonksiyonunu kullanmalısınız.


Yorumlayıcıyı kapatmak için `quit()` yazabilir, ya da Ctrl-D (Linux) veya Ctrl-Z (Windows) tuşlarına basabilirsiniz.

## Program çalıştırma


Python programları, bir düz metin dosyasına yazılmış Python ifadelerinden ibarettir. Notepad, emacs, gedit gibi herhangi bir düz metin editörü açın ve aşağıdaki satırları yazın. Dosyayı *ortalama.py* ismiyle kaydedin.

```python
a = float(input("Bir sayı girin: "))

b = float(input("Bir sayı girin: "))

c = float(input("Bir sayı girin: "))

d = float(input("Bir sayı girin: "))


print("Ortalama:", (a+b+c+d)/4)
```

Komut terminalini açıp dosyayı kaydettiğiniz dizine geçin ve `python ortalama.py` yazıp Enter’a basın. (Windows’ta dosya ikonuna tıklamak yeterli olacaktır). Program çalışınca ayrı ayrı dört reel sayı yazıp Enter’a basın.


`a = float(input("Bir sayı girin: "))` satırında, `input()` fonksiyonu ekrana  

`Bir sayı girin:`  

yazısını çıkarır ve siz klavyeyle bir şey yazana kadar bekler. Sizden aldığı cevabı bir “dize”, yani yazı olarak geri verir. Bu dizeyi aritmetik işlemde kullanabilmek için önce sayısal değere çevirmemiz gerekir. `input()` çağrısının etrafına sarılı `float() fonksiyonu bu işi yapar.


Bunu adım adım şöyle düşünebilirsiniz:

```python
a = float(input("Bir sayı girin: "))

a = float("1.2")

a = 1.2

```

Alternatif olarak, kodumuzu şöyle de yazabilirdik:



```python
a = input("Bir sayı girin: ")

a = float(a)

b = input("Bir sayı girin: ")

b = float(b)

c = input("Bir sayı girin: ")

c = float(c)

d = input("Bir sayı girin: ")

d = float(d)



print("Ortalama:", (a+b+c+d)/4)

```

## Bütünleşik Geliştirme Ortamları (IDE)


Programlama için her ne kadar bir metin editörü yetse de, bir IDE’nin sağladığı kolaylıklar yabana atılamaz. Sözgelişi kod parçalarını renklendirerek okunurluğu artırmak, yazılan komutu otomatik tamamlayabilmek, çevrimiçi yardım belgelerine erişebilmek, bir çok dosya içeren yazılım projelerini organize edebilmek, hata ayıklayıcı ile editörü birleştirmek gibi imkânlar sağlarlar.


### IDLE


IDLE, Python’la birlikte gelen basit ve minimal bir IDE’dir. Çok fazla bir imkân sağlamasa da, hafifliği ve her yerde bulunabilirliği sebebiyle varlığının farkında olmakta fayda var.


IDLE’ı çalıştırdığınızda, önce Python yorumlayıcısını etkileşimli kullanabileceğiniz bir pencere çıkar. *File* menüsünden *New file* seçerek bir editör penceresi açılabilir, veya *Open…* seçerek editöre mevcut bir dosya yüklenebilir. Editördeki Python programı, F5 tuşuna basarak yorumlayıcı penceresinde çalıştırılabilir.




### Spyder


IDLE’yi kullandıkça bir çok amaç için yetersiz kaldığını göreceksiniz. Daha güçlü bir IDE olarak Spyder’ı tavsiye ederim. Spyder’da tek bir pencere içinde editör, komut penceresi, dizin ağacı, değişken listesi, ve çevrimiçi yardım bulunabilir.




## Jupyter Notebook


Etkileşimli hesaplamada başka bir yaklaşım kodu “defter” denilen biçimde düzenlemektir. *Jupyter notebook* kullandığınızda komutlar “hücreler” ile organize edilir. Her hücre çalıştırıldığında, hücredeki komutlar defterin bağlı olduğu “çekirdeğe” (yorumlayıcıya) gönderilir, geri gelen cevaplar hücrenin altına yazılır. Bu şekilde bir dizi işlemin çıktısını kaydeden bir rapor hazırlamak mümkün olur. Bir Jupyter defterinde yazı, kod, şekil, formül, HTML elemanları bir arada bulunabilir.


Bu yazı ve birçok başka yazımız Jupyter defteri olarak hazırlandı, `nbconvert` aracıyla HTML’ye çevrilerek doğrudan blogumuza aktarıldı.


Bir Jupyter defteri HTML ve JavaScript teknolojileri ile hazırlanmıştır. Tarayıcınızda çalışır, ama kullanmak için internet bağlantısına ihtiyacınız olmaz.




## Alıştırmalar


Python’a ısınmak için küçük işler yaparak işe başlayabilirsiniz.


1. Python yorumlayıcısını etkileşimli kullanarak aşağıdaki değerleri hesaplayın.
	* $$\frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \frac{1}{16}$$
	* $$(2.1^3 – 4.7^{-4.3}) / (2.5^{0.5} + 10^{0.25})$$
	* $$x=1,2,3$$ için $$x^3 – 3x^2 + 5x -1$$
2. Aritmetik ortalama alma programına ekleme yapın: Program girilen sayıların standart sapmasını, geometrik ortalamasını ve harmonik ortalamasını hesaplayıp ekrana yazsın. Karekök almak için $$\sqrt{x} = x^{0.5}$$ denkliğini kullanabilirsiniz.


