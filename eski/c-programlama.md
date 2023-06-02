# C/C++ Programlama

C Programlama oldukça eski fakat hala güncelliğini ve gücünü koruyan bir programlama dilidir. Bilgisayarın donanımını kontrol edebildiği için işletim sistemleri dahil bir çok uygulama ve oyun bu programlama dili ile geliştirilir. C programlama derken elbette C++ programlamıyı da içine almaktadır. En azından bu sayfada. 

Her programlama dilinde olduğu gibi ekrana bir merhaba yazdırarak başlayalım.

```c
#include<stdio.h>

int main()
{
  printf("Merhaba");
  return 0;
}
```

#include ile başlayan satır kütüphane eklemek içindir. Standart giriş çıkış kütüphanesi stdio.h olarak bulunmaktadır. printf fonksiyonunu içinde barındırır.

C/C++ programlama dilinde her şey fonksiyonlardan oluşur. Buna ana program da dahildir. main() fonksiyonu programın ilk çalıştığı yeri gösterir. Fonksiyonların arasından önce main fonksiyonunu arar ve program oradan başlar. int main() olması dönen değerin ifadesidir. return 0 ile sisteme bir tamsayı değer döndürürüz. { ve } ise kod bloklarıdır. Kodlarımızı bloklamak için bu simgeleri kullanırız.

C programlama dilinde bir değişkeni kullanmadan önce tanımlamamız gerekir. Buna göre bellekten yer ayırmaktadır. Basit programlarla [algoritma](https://sonsuzus.github.io/algoritma-programlama) örneklerimizi yapmaya başlayalım.

Kullanıcıya yaşı sorulur ve doğum tarihi hesaplanır.

```c
#include<stdio.h>

int main()
{
  int yas;
  printf("Yasinizi giriniz: ");
  scanf("%d",&yas); //değişkenin adresine yazdırıyoruz, tam sayılar için %d ile alınıyor.
  printf("dogum yiliniz %d",2021-yas); // printf içinde işlem yapabiliriz elbette çift tırnak dışında
  return 1;
}
```

Burada scanf ile verileri okumaya yarayan stdio.h içinde bulunan bir fonksiyon kullanıyoruz. C de veriler değişkenlerin bellek adreslerine yazıldığı için değişkenin önüne & getirmeyi unutmayınız.

Kullanıcıya iki tam sayı sorulur ve arasında dört işlem yaptırılıp ekrana yazdırılır.

```c
#include<stdio.h>
int main()
{
  int sayi1,sayi2,toplam,fark,bolum,carpim; // değişkenlerimizi tanımlıyoruz
  printf("ilk tam sayiyi giriniz: ");
  scanf("%d",&sayi1); 
  printf("ikinci tam sayiyi giriniz: ");
  scanf("%d",&sayi2);
  toplam = sayi1 + sayi2;
  fark = sayi1 - sayi1;
  carpim = sayi1 * sayi2;
  bolum = sayi1 / sayi2;
  printf("%d + %d = %d \n",sayi1,sayi2,toplam); // \n alt satıra geçirmeye yarıyor
  printf("%d - %d = %d \n",sayi1,sayi2,fark);
  printf("%d * %d = %d \n",sayi1,sayi2,carpim);
  printf("%d / %d = %d",sayi1,sayi2,bolum);
  return 0;
}
```

Yine sayıları okuturken & adres bilgisine yazdırıyoruz. C de dört işlem diğer programlama dillerinde olduğu gibi numlock bölümündeki simgeler kullanılır. 

Yeni sorumuzla devam edelim.

Kullanıcıya havanın sıcaklığı santigrat cinsinden sorulur ve fahrenayta çevrilir.

Bunun formülü f=c\*1.8+32 dir.

```c
#include<stdio.h>

int main()
{
  float fahr,cel; 
  printf("Celsius cinsinden sicakligi giriniz: ");
  scanf("%f",&cel);
  fahr = cel*1.8+32;
  printf("%f santigrat %f fahrenayt demektir",cel,fahr);
  return 0;
}
```

Burada yeni bir değişken tipi yani float dikkatinizi çekmiştir. Noktalıklı sayılar için kullanılır. Bellekten daha fazla yer ayırmaktadır. Okuturken ve yazdırırken kullanılan formatı %f şeklindedir.

Yeni sorumuz da şu olsun. Kullanıcıya çap sorulur ve dairenin çevresi ve alanı hesaplanır.

```c
#include <stdio.h>

int main()
{
    float R, r, cevre, alan, pi = 3.14;
    printf("Lütfen dairenin capini giriniz: ");
    scanf("%f",&R);
    r = R/2.0; 
    cevre = 2 * pi * r;
    alan = pi * r * r;
    printf("%f capli dairenin cevresi: %f ve alani: %f dir.\n",R,cevre,alan);
    return 1;
}
```

Sorularımıza devam edelim. Yine benzer bir soru. Kullanıcıya eşkenar üçgenin bir kenarı sorulur gelen yanıta göre eşkenar üçgenin alanı hesaplanır.

```c
#include <stdio.h>

int main()
{
    float a, kok3 = 1.732, alan;
    printf("Eskenar ucgenin bir kenarini giriniz: ");
    scanf("%f",&a);
    alan = (kok3 / 4.0) * (a*a);
    printf("Bir kenari %f olan ucgenin alani: %f dir.\n",a,alan);
}
```

Dolar ve euro hesaplayan sorumuz ise şu şekilde. Kullanıcıya elindeki türk parası miktarı sorulur, gelen yanıta göre ne kadar dolar ve euro alacağı söylenir.

```c
#include <stdio.h>

int main(){
    float dolar,euro,tl;
    printf("Elinizdeki tl miktarinini girin: ");
    scanf("%f",&tl);
    dolar = tl / 13.65;
    euro = tl / 15.50;
    printf("Elinizdeki %f tl ile %f dolar veya %f euro alabilirsiniz.",tl,dolar,euro);
}
```

Yeni sorumuz sıralama sorusu. Elbette döngülerle daha güzel sıralamalar yapılır ama şimdilik sadece iflerle sıralama yapalım. Kullanıcıdan üç sayı istenir ve büyükten küçüğe yazdırılır.

```c
#include <stdio.h>

int main()
{
    int a, b, c;
    printf("Birinci sayiyi giriniz: ");
    scanf("%d",&a);
    printf("Ikinci sayiyi giriniz: ");
    scanf("%d",&b);
    printf("Ucuncu sayiyi giriniz: ");
    scanf("%d",&c);
    if(a>=b && b>=c) printf("%d > %d > %d",a,b,c);
    if(a>=c && c>=b) printf("%d > %d > %d",a,c,b);
    if(b>=c && c>=a) printf("%d > %d > %d",b,c,a);
    if(b>=a && a>=c) printf("%d > %d > %d",b,a,c);
    if(c>=a && a>=b) printf("%d > %d > %d",c,a,b);
    if(c>=b && b>=a) printf("%d > %d > %d",c,b,a);
}
```

```c
#include <stdio.h>

int main()
{
    int sayi,enkucuk=1000000,enbuyuk=-10000000;
    do
    {
        printf("Bir sayi giriniz: ");
        scanf("%d",&sayi);
        if(sayi<enkucuk && sayi!=0) enkucuk=sayi;
        if(sayi>enbuyuk && sayi!=0) enbuyuk=sayi;
        printf("Simdiye kadar girilen en kucuk sayi: %d \nSimdiye kadar girilen en buyuk sayi: %d\n",enkucuk,enbuyuk);
    } while (sayi!=0);
    return 0;
}
```

```c
#include <stdio.h>
/*2 ile 2022 arasinda tam kare ve küp olan sayilar kaç tanedir */

int karemi(int sayi)
{
    int i;
    for(i=1;i<sayi;i++)
    {
        if(i*i==sayi) return 1;
    }
    return 0;
}

int kupmu(int sayi)
{
    int i;
    for(i=1;i<sayi;i++)
    {
        if(i*i*i==sayi) return 1;
    }
    return 0;
}

int main()
{
    int sayi,adet=0;
    for(sayi=2;sayi<=2022;sayi++)
    {
        if(karemi(sayi)==1 || kupmu(sayi)==1)
        {
            printf("%d - ",sayi);
            adet++;
        }
    }
    printf("\n2 - 2022 arasinda %d adet kare veya kup sayi vardir.",adet);
}
```

{% include footer.html %}

{% include analytics.html %}
