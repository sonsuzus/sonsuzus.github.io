# C/C++ Programlama

C Programlama oldukça eski fakat hala güncelliğini ve gücünü koruyan bir programlama dilidir. Bilgisayarın donanımını kontrol edebildiği için işletim sistemleri dahil bir çok uygulama ve oyun bu programlama dili ile geliştirilir. C programlama derken elbette C++ programlamıyı da içine almaktadır. En azından bu sayfada. 

Her programlama dilinde olduğu gibi ekrana bir merhaba yazdırarak başlayalım.

```
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

```
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

```
#include<stdioh.>
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

```
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

{% include footer.html %}

{% include analytics.html %}
