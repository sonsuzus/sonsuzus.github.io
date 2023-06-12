---
title:  Python Programlamaya Giriş 6 – Döngü Alıştırmaları
author: sonsuz
date: 2023-06-12 21:02:31 +0300
categories: [Program,Python]
tags: [python,döngü]
math: true
---





1. En uzun Collatz zinciri
2. Üstel fonksiyon Taylor serisi
3. Karekök bulma
4. Machin formülüyle pi’yi bulma
5. Lojistik fonksiyon ve kaos
6. SIR salgın modeli


## En uzun Collatz zinciri


Collatz dizisinden önceki bölümde bahsetmiştik. Diziyi $n$ sayısıyla başlatırsak, sonraki sayıyı şu bulma kuralla buluruz:


* $n_i$ çift sayıysa: $n_{i+1} = n_i/2$
* $n_i$ tek sayıysa: $n_{i+1} = 3n_i+1$
* $n_i=1$ ise dizi sonlanır.


Meselâ 13 ile başlarsak, on eleman uzunlukta olan 13, 40, 20, 10, 5, 16, 8, 4, 2, 1 dizisini elde ederiz. Bu dizinin uzunluğu 10’dur.


Sorumuz şu: Bir milyonun altındaki bütün başlangıç değerleri içinde hangisi **en uzun** Collatz dizisini verir? (Başlangıçtan sonraki değerler bir milyonun üzerine çıkabilir.)


(Kaynak: Euler Project, [14. problem](http://projecteuler.net/problem=14))


## Üstel fonksiyon için Taylor serisi


Üstel fonksiyonun $x=0$ çevresinde bir sonsuz seri ile gösterilebileceğini temel analiz derslerinden biliyoruz.


$$e^x = \sum_{n=0}^{\infty} \frac {x^n}{n!} = 1 + x + \frac{1}{2}x^2 + \frac{1}{6}x^3 + \cdots$$


Bu seri bütün $x$ değerleri için yakınsar, yani her $x$ değeri için yeterince terim ekleyerek $e^x$ değerini istediğimiz hassasiyette hesaplayabiliriz.


$x$ değerini kullanıcıdan sorarak, yukarıdaki seriyle $e^x$ değerini veren bir program yazın. Programın içinde `tol` isimli bir tolerans değişkeni tanımlayın ve $10^{-10}$ değeri verin. Bir döngü içinde, son terimin mutlak değeri `tol`‘den küçük olana kadar seriye yeni terimler ekleyin.


Her terimi sıfırdan hesaplamak gereksiz yük bindirecektir. Eklenecek yeni terimi hesaplarken, bir önceki terimi $x$ ile çarpıp, iterasyon değişkeni olan $n$’ye bölmek daha verimli olur.


Çeşitli $x$ ve `tol` değerleri kullanarak $e^x$ değerlerini, kaç terim gerektiğini, ve son terimi ekrana bastırın.


Örnek çıktı:



```python
x değerini girin: 3.0

e^x ~  20.0855369232

22 terim kullanıldı

Son terim = 2.79190741015e-11


```

Matematik kütüphanesindeki fonksiyonla karşılaştırmak isterseniz `math.exp()` fonksiyonunu kullanabilirsiniz.


## Babil yöntemiyle karekök bulma


Verilen bir $N$ sayısının karekökünü bulmak için Babil döneminden beri kullanılan tekrarlamalı (iteratif) bir yöntem vardır: Önce, karekök için bir tahminde bulunun ve buna $x_0$ deyin. Bir sonraki tahminimiz  

$$x_1 = \frac{1}{2}\left(x_0 + N/x_0\right)$$  

olacak. Genel olarak,  

$$x_{n+1} = \frac{1}{2}\left(x_n + N/x_n\right)$$  

kuralıyla ardışık iterasyonlar yaparsak, $x_n$ değerleri hızlıca $N$’nin kareköküne yakınsayacaktır.


Bu yöntem, fonksiyon köklerini bulmak için kullanılan en iyi algoritmalardan biri olan Newton yönteminin özel bir durumudur.


Bu yöntemi kullanarak karekök değerini hesaplayan bir program yazın. 

Program kullanıcıya karekökü alınacak sayıyı ve ilk tahmini sorsun. 

Bir döngü içinde, hata değeri $|x_n^2 – N|$ programda belirlenen bir toleranstan (sözgelişi $10^{-10}$) küçük olana kadar iterasyonlar tekrarlansın. 

Program karekökün tahmini değerini ve sonuca ulaşmak için kaç iterasyon gerektiğini ekrana bassın.


Örnek çıktı:



```python
Karekökü alınacak sayı: 135.646

İlk tahmin: 10

Karekök ~  11.6467162754

4 iterasyon




```

## Pi sayısı ve Machin formülü


Pi’yi hesaplamak için [tarih boyunca çeşitli yöntemler geliştirildi](http://www.acikbilim.com/2013/03/dosyalar/pi-gunu-kutlu-olsun.html). Önceki bir örnekte kullandığımız Leibniz formülü $\arctan$ fonksiyonunun Taylor açılımına dayanır:


$$\arctan x = x – \frac{1}{3}x^3 + \frac{1}{5}x^5 – \frac{1}{7} x^7 + \cdots$$


Bu formülde $x=1$ koyarak Leibniz formülünü elde ederiz:


$$\frac{\pi}{4} = 1 – \frac{1}{3} + \frac{1}{5} – \frac{1}{7} + \ldots$$


Bu formül, onu ilk defa 14. yüzyılın sonunda keşfeden dâhi Hintli matematikçi Madhava’nın, ve astronom James Gregory’nin de adı eklenerek, Madhava-Gregory-Leibniz serisi olarak da anılır.


Daha önce gördüğümüz gibi, $x=1$ için bu seri çok yavaş yakınsar. Ancak, $x$’in birden küçük olduğu değerlerde yakınsama hızlı olur. 1706’da John Machin $\pi$ için hızlı yakınsayan, böylelikle az sayıda terimle yüksek doğruluk sağlayan bir formül yayınladı.


$$\pi = 16 \arctan \frac{1}{5} – 4 \arctan \frac{1}{239}$$


Buradaki her bir terim, $\arctan$ fonksiyonunun yukarıda verilen açılımıyla hesaplanabilir.


Bu formülle Machin, $\pi$’yi o dönem için bir rekor olan 100 basamağa kadar hesaplayabilmişti. $\pi$’nin birkaç $\arctan$ teriminin toplamı olarak ifade edildiği formüllere [*Machin benzeri*](http://en.wikipedia.org/wiki/Machin-like_formula) adı verilir. Bu algoritmalar, $\pi$’yi trilyon basamağa kadar hesaplarken bile kullanılabilecek kadar verimlidirler.


Machin formülüyle $\pi$’yi hesaplayacak bir program yazın. Programda $\arctan$ fonksiyonlarının değerlerini yine bir döngü içinde, serinin son terimi belli bir hata payı değerinin altında olacak şekilde hesaplatın.


## Lojistik fonksiyon ve kaos


Matematiksel kaosun gözlendiği en basit sistemlerden biri, [*lojistik fonksiyon*](https://www.wikizero.com/en/Logistic_map) denen fonksiyonun iterasyonlarında bulunur. Lojistik dizinin her yeni terimi $x_{t+1}$, bir önceki terim $x_t$’den şu formülle elde edilir.:


$$x_{t+1} = r x_t (1-x_t)$$


Burada $x_t$ 0 ile 1 arasında kalan dinamik değişken, $r$ ise 0 ile 4 arasında bir parametredir. Parametre bir kere belirlendikten sonra dizi içinde değişmez.


1. $x_0 = 0.1$ değerinden başlayarak, kullanıcıdan alınan bir $r$ değerini kullanarak ardışık $x_0\ldots x_{100}$ değerlerini ekrana yazan bir program yazın. Programı, $r$ parametresine sırayla 2.1, 3.1, 3.4, 3.5 değerleri vererek çalıştırın. Elde edilen $x_t$ değerlerinin uzun vadeli davranışını inceleyin (sabit bir noktaya mı yakınsıyor, periyodik bir döngüye mi oturuyor?)  

Örnek çıktı:

```python
r parametresi (0-4): 2.1

0.1

0.189

0.3218859

0.4583782715

0.521362026605

0.524041694021

...

0.52380952381

0.52380952381

0.5238095238


```
2. $r $= 3.5 için dizi, periyotu dört olan bir salınıma oturur. Deneme yanılma ile, dört periyotlu salınım veren en düşük ve en yüksek $r$ değerlerini belirleyin.
3. *Kaos*‘un alametifarikası, birbirine çok yakın yerden başlayan iki yörüngenin hızla (üstel olarak) birbirinden uzaklaşmasıdır. Bunu görmek için programı biraz değiştirelim: Programı iki ayrı değerle başlayan dizileri, iki ayrı sütunda basacak şekilde değiştirin. Başlangıç değerleri 0.1 ve 0.10001 olsun. Bu programı $r=$ 3.1, 3.5, 3.57, 3.7 ve 4.0 için çalıştırın.
	* Hangi $r$ değerleri için uzun vadede iki sütundaki sayılar eşitleniyor? (Kaos olmayan durum)
	* Hangi değerlerde sütunlardaki sayılar birbirine yakın başlamasına rağmen sonunda çok farklı hale geliyorlar?
	* Sütunlardaki sayıların arasındaki farkın belli bir miktar açılması için gereken zaman $r$ ile nasıl değişiyor?


## Salgın hastalıklar – SIR modeli


[SIR (susceptible-infected-recovered) modeli](https://www.wikizero.com/en/Compartmental_models_in_epidemiology), salgın hastalıkların yayılmasını incelemekte kullanılan modellerin en sadelerindendir. Modelde bir topluluk üç kategoriye ayrılır: Şimdilik sağlıklı olan ama hastalığa yakalanması mümkün olanlar (S), hastalığa yakalanmış ve S’lere bulaştırabilecek olanlar (I), ve hastalanıp iyileşmiş, tekrar hastalanmayacak ve hastalığı başkasına bulaştıramayacak olanlar (R). Belli bir $t$ anında bu üç kategoride bulunanların nüfustaki oranlarını sırayla $S_t, I_t, R_t$ olarak gösterelim. O zaman, ayrık zaman adımlarında modelin denklemleri şöyle yazılabilir:


$$\begin{array}{rcl}S_{t+1} &=& S_t – a I_t S_t \\ I_{t+1} &=& I_t + a I_t S_t – b I_t \\ R_{t+1} &=& R_t + bI_t \end{array}$$


Burada $a$ parametresi, kullanılan zaman birimi içinde (gün, hafta, ay) hastalıkla temas sıklığı veya bulaşma olasılığı, $b$ parametresi ise ortalama iyileşme oranıdır. Buna göre 1/$b$ değeri hastalığın iyileşmesi için bir zaman ölçeği sağlar, bu bilgiyle de $b$ için bir tahmin yapılabilir.


SIR modelini kullanarak her zaman adımında S, I, ve R kategorisindekilerin oranını listeleyen bir program yazın. Veriler hasta olanların oranı %0.1’in üzerinde olduğu sürece, ama en fazla 100 zaman adımı gösterecek şekilde listelensin. Başlangıçta sağlıklı olanların oranı %99, hastaların oranı %1, iyileşmiş olanlar ise %0 olsun. Parametreler için $a = 0.6$ ve $b = 0.2$ kullanın (epeyce bulaşıcı, ama tipik iyileşme süresinin 5 zaman adımı olduğu bir hastalık).


SIR modelinde salgının kısa sürdüğü ve salgın süresince toplam nüfusun sabit kaldığı varsayılır. Yukarıdaki denklemlerin sağ taraflarını topladığınızda bazı terimlerin birbirini götürdüğünü ve $S_{t+1} + I_{t+1} + R_{t+1} = S_t + I_t + R_t = 1$ olacağını görebilirsiniz. Her zaman adımında $S_t + I_t + R_t$ toplamını da ekrana bastırın. Bu toplamın sabit kalmaması programınızda bir hata olduğunu göstergesidir.


Örnek çıktı:



```python
t     s     i     r   toplam

-- ----- ----- ----- --------

 0 0.990 0.010 0.000 1.000000

 1 0.984 0.014 0.002 1.000000

 2 0.976 0.019 0.005 1.000000

 3 0.964 0.027 0.009 1.000000

 4 0.949 0.037 0.014 1.000000

 5 0.928 0.051 0.021 1.000000

...

47 0.046 0.002 0.952 1.000000

48 0.046 0.001 0.952 1.000000

49 0.046 0.001 0.953 1.000000




```

Çeşitli başlangıç şartları, ve parametreler için çeşitli değerler deneyerek sistemin davranışına bakın. Hasta olanların oranı kaçıncı zaman adımında azami sayıya ulaşıyor? Salgın dindiğinde hiç hasta olmayanların oranı ne kadar? Bu sayılar parametrelerle nasıl değişiyor?


**Not.** Dinamik değişkenlerin güncellenmesi sırasında sağ tarafta hep eski (bir önceki zamandaki) değerlerin kullanılmasına dikkat etmek gerekiyor. Sözgelişi,



```
s = s - a*i*s

i = i + a*i*s - b*i    # hata

r = r + b*i            # hata

...




```

yazmak, ilk bakışta gözden kaçabilecek ciddi bir hataya yol açar. İkinci atamadaki `s` değişkeni aslında $S_{t}$ değerini değil, yenilenen $S_{t+1}$ değerini taşımaktadır. Aynı sorun üçüncü atamadaki `i` değişkeni için de geçerli. Bunu engellemenin iki yolu var. Birincisi, eski değerleri ayrı adlar altında saklamak ve döngünün sonunda güncelleme yapmak:



```
s = s_eski - a * i_eski * s_eski

i = i_eski + a* i_eski * s_eski - b * i_eski

r = r_eski + b * i_eski

...

s_eski = s

i_eski = i

r_eski = r

...


```

İkinci yol ise, Python’un çoklu atama özelliğini kullanarak, geçici değişken kullanmadan bütün değişkenleri tek bir atamada güncellemek:



```
s, i, r = s - a*i*s, i + a*i*s - b*i, r + b*i


```

Bu atamada önce eşit işaretinin sağ tarafının değeri (bir üçüz) bulunur. Sağ tarafta eski değerler kullanılır. Sonra bu üçüzün elemanları `s`, `i`, ve `r`‘ye sırayla atanır.