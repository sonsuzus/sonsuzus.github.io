---
title:  C Programlama Örnekleri Girdi/Çıktı Değişken ve İşlemler 00
author: sonsuz
date: 2023-08-17 23:26:15 +0300
categories: [Program,C]
tags: [c,programlama,alıştırma,algoritma,örnek]
---


## Giriş

```c
/* Burası yorum satırıdır */

// #include [Başlığı(Header)] <kütüphane>

#include <stdio.h> //Her C programında olması gerekir.  //stdio.h: [STandarD Input/Output(Standart Girdi/Çıktı)]                   

#include <locale.h>  //Tüm Diller ve Karakter setleri bu kütüphane de yer alır. 

/*  main() fonksiyonu her C programında bulunması gereken bir fonksiyondur */


int main()
{
    printf("Hello world!\n");
     
    setlocale(LC_ALL,"Turkish"); //Türkçe karakter yazdırmamızı sağlayan fonksiyon
 
    printf("Merhaba Dünya\n");
   
    printf("İĞÜÇÖŞ iğüçöş");
	
    return; // Geriye değer gönderme işlemi yapar.
}

```

## Bazı Tanımlar

```c
#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

/*
Karakterler


\0 > sonlandırıcı karakter (null character) 
\a > çan sesi (alert) 
\b > geri boşluk (back space) 
\t > 1 tane tab kadar boşluk bırakır. (horizontal TAB) 
\n > Bir alt satıra geçer(new line) 
\v > düşey tab (vertical tab) 
\f > sayfa ileri (form feed) 
\r > satır başı (carriage return) 

*/


/*
Veri Tipleri
   char-> int -> float -> double


   - char    : Karakter(Character): Alfabedeki büyük küçük harfler, özel semboller //1 byte (-128'den 127'ye kadar) STANDART ASCII TABLOSU

	 unsigned char > İşaretsiz char Türü

   - int     : Tamsayı(İnteger): Tamsayı değişken ve sabitleri tanımlamak için kullanılır. //4 byte

	 [signed] short [int] > İşaretli Kısa Tamsayı Türü    // 2 byte (-32.768 - 32.767)
	 [signed] long  [int] > İşaretli Uzun Tamsayı Türü    // 4 byte (-2.147.483.648 - 2.147.483.647)
	 unsigned short [int] > İşaretsiz Kısa Tamsayı Türü   // 2 byte
 	 unsigned long  [int] > İşaretsiz Uzun Tamsayı Türü	  // 4 byte

   - float   : Küsüratlı Sayılar: Virgüllü kısmıyla ifade eder. //4 byte

   - double  : Daha Hassas Küsüratlı Sayılar: Float türünden 2 kat daha duyarlıdır. //8 byte
	   
	 long double

*/


/*
Yer ve Tür Belirleyiciler
   Yer Belirleyicileri
	- auto
	- register
	- static
	- extern
   Tür Belirleyicileri
	- const       > Bir değişken ile tanımlandığında ve ilk değer atandığında, bu değişken içeriği hiç değişmez.
	ÖRN: const pi = 3.14;
		 const double pi = 3.1416;

	- volatile


*/


int main()

{
	setlocale(LC_ALL, "Turkish");

	int tamsayi;

	char karakter;

	char karakterDizisi[50];

	float kesirlisayi1;

	double kesirlisayi2;

	/* scanf veri alır, printf veri gönderir*/

	printf("Lütfen bir tam sayı giriniz: ");
	scanf("%d", &tamsayi);

	printf("Lütfen bir karakter giriniz: ");
	scanf(" %c", &karakter);

	/* scanf(" %c" ,&karakter);
	Program içerisinde kullanıcıdan birden fazla tipte değer almak istediğimizde derleyicinin kafasının karışmaması 
	için karakter alırken bir boşluk kullanarak karakter değerini kullanıcıdan almalıyız.
	 */

	printf("Lütfen bir karakter dizini giriniz: ");
	scanf("%s", &karakterDizisi);  	
	// scanf("%s" ,&karakterDizisi),  scanf("%s" ,karakterDizisi), scanf("%s" ,karakterDizisi[0]) 

	printf("Lütfen bir kesirli sayı giriniz: "); // Program bizden kesirli bir sayı değeri girmemizi istediğinde virgül kullanarak girmeliyiz.
	scanf("%f", &kesirlisayi1);

	printf("Lütfen bir daha hassas küsüratlı bir sayı giriniz: ");
	scanf("%lf", &kesirlisayi2);


	/* printf ("Sabit metin bilgisi", değişken ismi)*/
	printf("\n\n");

	printf("Girilen Tam Sayı: %d\n", tamsayi);
	printf("Girilen Karakter: %c\n", karakter);
	printf("Girilen Karakter Dizisi: %s\n", karakterDizisi);
	printf("Girilen Kesirli Sayı: %f\n", kesirlisayi1);
	printf("Girilen Hassas Küsüratlı Sayı: %lf\n", kesirlisayi2);




	int x = 15;
	float y = 15;
	double z = 15;

	printf("\n\n");
	printf("int / float= %f\n", x / y);
	printf("int / float= %lf\n", x / z);
	printf("float / double= %f\n", y / z);


	int t = 3;
	printf("\n\n");
	printf("%f\n", (float)x);
	printf("%.1f", (float)x);

}

```

## Alan Genişliği

```c
/* Alan Genişliği Ayırarak Yazdırma

%d   > Tamsayı Belirleyici 
	  (int) onluk sayı sisteminde yazar.

%ld  > Uzun Tamsayı Belirleyici
	  (long) onluk sayı sisteminde yazar.

%f   > Ondalık Sayı Belirleyici
	  (float,double) onluk sayı sisteminde yazar.

%lf  > Uzun Ondalık Sayı Belirleyici
	  (double,long) onluk sayı sisteminde yazar.

%e   > Üstel Biçim Belirleyici
      Gerçek sayıları üstel biçimde yazar.

%u   > İşaretsiz Tamsayı Belirleyici
	  (unsigned int) onluk sayı sisteminde yazar.

%x   > İşaretsiz Hexadesimal (Onaltılık) Belirleyici
      (unsigned int) onaltılık sayı sisteminde yazar.

%o   > İşaretsiz Oktal (Sekizlik) Belirleyici
	  (unsigned int) sekizlik sayı sisteminde yazar.

%g   > Durume göre %f veya %e kullanılan Belirleyici
	  Kısa olan şekli tercih ederler

%c   > Karakter Belirleyici


%s   > Metin Belirleyici


*/


#include <stdio.h>
#include <locale.h>

int main()
{
	setlocale(LC_ALL, "Turkish");


	printf("	%%d Kullanımı\n");
	printf("\n");


	printf("Output:%d\n", 7);
	/* Aynısı gibi yazar.*/

	printf("Output:%6d\n", 7);
	/* 6 karakterli bir alan içerisinde yazdırır. Yani 5 karakterlik yer atlayarak değeri yazar.*/

	printf("Output:%06d\n", 7);
	/* Aynı tam sayı değeri 6 karakterlik bir alan içerisine yazar ama boşluk olan yerler sıfır ile doldurur.*/

	printf("Output:%-10d\n", 75);
	/* (-) işareti sola dayalı yazdırır.*/

					printf("\n********************************\n");

	printf("	%%f Kullanımı\n");
	printf("\n");


	printf("Output:%.8f\n", 1.234);
	/* Virgülden sonrasındaki sayıyı yazdıktan sonra 8 karakterlik olması için boşluklar sıfırla tamamlanır.*/

	printf("Output:%2.3f\n", 45.58678);
	/* Tam sayı bölümü 2, desimal bölümü (Virgülden sonrası) ise 3 karakter yazdırır. Yuvarlama yapar.*/

	printf("Output:%2.3f\n", 45.58);
	/* Tam sayı bölümü 2, desimal bölümü ise 3 karakter yazdırır.*/

	printf("Output:%5.3f\n", 45.58);
	/* Tam sayı bölümü 5, desimal bölümü ise 3 karakter yazdırır.*/

	printf("Output:%-15.3f\n", 45.58);
	/* Sola dayalı tam sayı bölümü aynı, desimal bölümü ise 3 karakter yazdırır.*/

					printf("\n********************************\n");

	printf("	%%e Kullanımı\n");
	printf("\n");


	printf("Output:%+.3e\n", -123.456789);
	/* Sayısını üssel gösterimle 3 hane hassasiyetli olarak (+ -) işareti ile birlikte yazdırır.*/

	printf("Output:%.2e\n", 225.68);
	printf("Output:%20.2e\n", 225.68);
	printf("Output:%-20.2e\n", 225.68);
	
					printf("\n********************************\n");


	

	unsigned int u = 57054;
	printf("Output (%%u) = %u\n", u); /* u değerini onluk sistemde yazar */
	printf("Output (%%o) = %o\n", u); /* u değerini sekizlik sistemde yazar */
	printf("Output (%%x) = %x\n", u); /* u değerini onaltılık sistemde yazar */
	
					printf("\n********************************\n");

	long int lo = 23467;
	unsigned long int unlo = 65242;
	printf("Output (%%ld) = %ld\n", lo);   /* onluk sistemde yazar */
	printf("Output (%%lu) = %lu\n", unlo); /* onluk sistemde yazar */
	printf("Output (%%lx) = %lo\n", unlo); /* sekizlik sistemde yazar */
	printf("Output (%%lx) = %lx\n", unlo); /* onaltılık sistemde yazar */

					printf("\n********************************\n");

	
	printf("Output (%%s) = %s\n", "This is a string");

	printf("Output (%%g) = %g\n", 123456.789);
}

```

## Matematiksel İşlemler

```c
/* Matematiksel İşlemler */

#include <stdio.h>    
#include <stdlib.h>
#include <locale.h>  

/*  ATAMA OPERATÖRLERİ
x += y   >  x = x+y
x -= y   >  x = x-y
x *= y   >  x = x*y
x /= y   >  x = x/y
x %= y   >  x = x%y

*/

/*  Arttırma ve Eksiltme Operatörleri

++x  > x = x+1     önce arttırılır, sonra atanır
--x  > x = x-1     önce eksiltilir, sonra atanır

x++  >             önce atanır, sonra arttırılır
x--  >             önce atanır, sonra azaltılır


*/


int main()
{

	setlocale(LC_ALL, "Turkish");

	int x, y;



	printf("Lütfen bir tam sayı giriniz: \n");
	scanf("%d", &x);


	y = x++;  //atanır sonra arttırılır.

	printf("x= %d, y= %d\n", x, y);



	printf("Lütfen bir tam sayı giriniz: \n");
	scanf("%d", &x);

	y = ++x; //önce arttırılır, sonra atanır

	printf("x= %d, y= %d\n", x, y);



	printf("Lütfen bir tam sayı giriniz: \n");
	scanf("%d", &x);

	x += 5;

	printf("x= %d", x);


	return 0;

}

```

## Operatörler

```c
/*
Mantıksal Operatörler

-- Operatör -- Anlamı -- C Sembol -- C Örnek Kod -- Sonuç
	AND        Ve	     &&	       a && b           >> Her ikiside doğru ise 1(True), her ikiside yanlış ise 0(False)
	OR	      Veya	     ||        a || b           >> Herhangi birisi doğru ise 1(True), her ikiside yanlış ise 0(False)
	NOT	      Değil       !          !a	            >> Doğru ise 0(False), Yanlış ise 1(True)


*/


/*
Operatörlerde Öncelik Sırası

Öncelikli Operatör            ()			 soldan sağa

Aritmetik Operatörler         ! ++ --		 SAĞDAN SOLA
							  /  * %		 soldan sağa
							  + -			 soldan sağa

Karşılaştırma Operatörler     > >= < <=		 soldan sağa
(İlişkisel)					  == !=		     soldan sağa

Mantıksal Operatörler         &&			 soldan sağa
							  ||			 soldan sağa

Atama Operatörü               =				 SAĞDAN SOLA

*/


#include <stdio.h>
#include <locale.h>


void main()

{
	setlocale(LC_ALL, "Turkish");

	int a = 5, b = 8, c = 3, d, e, f, g;

	d = a * b / c % a;
	printf("%d\n", d);

	e = (a < 5) || (++b > 4);
	printf("%d\n", !e);

	printf("%d\n", a || c && b % c && e);

	f = a * 2 % (b + 1) - c / (a + b);
	printf("%d\n", f);

	g = (f / e * a - b++ * --c) / -3;
	printf("%d\n", g);

	printf("\n\n");

	int x = 4, y = 7, z = 5, p, r, s, m;

	p = x * y / z % x;
	printf("%d\n", p);

	r = (x < 5) || (++y > 4);
	printf("%d\n", !r);

	printf("%d\n", x || z && y % z && r);

	s = x * 2 % (y + 1) - z / (x + y);
	printf("%d\n", s);

	m = (s / r * x - y++ * --z) / -3;
	printf("%d", m);

}

```
