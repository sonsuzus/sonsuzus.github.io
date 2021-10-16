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

C programlama dilinde bir değişkeni kullanmadan önce tanımlamamız gerekir. Buna göre bellekten yer ayırmaktadır. Basit programlarla (algoritma)[https://sonsuzus.github.io/algoritma-programlama] örneklerimizi yapmaya başlayalım.

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

{% include footer.html %}

{% include analytics.html %}
