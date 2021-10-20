# Algoritma

Bir işin veya programın yapılması için adımlara bölünmüş halidir. Aslında hayatımızın her noktasında algoritmaları kullanırız farkında olmadan. Yemek yapmaktan araba kullanmaya kadar hepsi birer algoritma içerir. Bu başlığımızda algoritma kurma yöntemlerini inceleyeceğiz. Takıldığınız konuları [discussions](https://github.com/sonsuzus/sonsuzus.github.io/discussions) bölümünde sorabilirsiniz.

## Programlama soruları

Bu bölümde programlama ile ilgili sorular sorulacaktır. Çözümlerine ilgili programlama sayfalarından ulaşabilirsiniz.

Kullanıcıya yaşı sorulur ve doğum tarihi hesaplanır.

Kullanıcıya iki tam sayı sorulur ve arasında dört işlem yaptırılıp ekrana yazdırılır.

Kullanıcıya havanın sıcaklığı santigrat cinsinden sorulur ve fahrenayta çevrilir.

Kullanıcıya çap sorulur ve dairenin çevresi ve alanı hesaplanır.

Kullanıcıya eşkenar üçgenin bir kenarı sorulur gelen yanıta göre eşkenar üçgenin alanı hesaplanır.

Kullanıcıya elindeki türk parası miktarı sorulur, gelen yanıta göre ne kadar dolar ve euro alacağı söylenir.

Kullanıcıdan üç sayı istenir ve büyükten küçüğe yazdırılır.

Kullanıcıdan tek harflik cinsiyet bilgisi istenir buna göre bir cümle kurulur.

Kullanıcıdan elindeki Türk Lirası miktarı sorulur. Gelen yanıta göre ne kadar japon yeni alabileceği söylenir.

Kullanıcıya kürenin çapı sorulur, gelen yanıta göre hacmi hesaplanır.

Kullanıcıya notu sorulur. 50 den büyükse geçtin, 50 den küçükse kaldın yazdırılır.

Suyun sıcaklığı sorulur, 0 dan küçükse katı, 0-100 arasında sıvı, 100 den büyükse gaz yazdırılır.

Kullanıcıdan bir sayı girmesi istenir. Bu sayı tek mi çift mi yazdırılır.

Kullanıcıya kişinin cinsiyeti ve yaşı sorulur. Ona göre hediye önerilir.

Kullanıcıya 3 adet tamsayı kenar girmesi istenir. Girilen kenarlara göre üçgen olup olmadığı, üçgense ne tür bir üçgen olduğu yazdırılması istenir.

Kullanıcıya beş tane cümlenin doğru mu yanlış mı olduğu sorulur sırayla ve notu açıklanır. (doğru için d, yanlış için y, not 100 üzerinden)

1 den 100 e kadar sayılar yazdırılır. (döngü)

1 ile 100 arasında 3 veya 7 ye tam bölünen sayılar yazdırılır.

Kullanıcıdan tek sayılar için T çift sayılar için C tüm sayılar için B girmesi istenir. İstediği şekilde sayılar 100 e kadar yazdırılır.

Kullanıcıdan belirsiz sayıda not girilip ortalaması hesaplanır. Not girişini durdurmak için 0 a basılır.

Durunun kodu

```
#include<stdio.h>

int main;

int a;
printf("Ucgen olusturmaya hos geldiniz. 1. sayiyi giriniz: ");
scanf(a,b,c, "%d");
int b;
printf("2. sayiyi giriniz: ");
int c;
printf("3. sayiyi giriniz: ");
if (a+b+c==180)
    ("Bu sayilarla bir ucgen olusturulabilir.");
        if (a+b+c!=180)
        printf("Bu sayilarla bir ucgen olusturulamaz.");
else if (a==60 && b==60 && c==60)
    ("Bu sayilarla bir eskenar ucgen olusturulabilir.");
else if (a==90 && b==45 && c==45 || a==45 && b==90 && c==45 || a==45 && b==45 && c==90)
    ("Bu sayilarla bir dik acili ucgen olusturulabilir.");
else if (a==b && b!=c || a==c && c!=b || b==c && b!=a)
    ("Bu sayilarla bir ikizkenar ucgen olusturulabilir.");
else
    printf("Bu sayilarla bir cesikenar ucgen olusturulabilir.");

remain=0
```


{% include footer.html %}

{% include analytics.html %}
