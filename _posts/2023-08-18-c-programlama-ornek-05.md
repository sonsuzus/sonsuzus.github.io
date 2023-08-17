---
title:  C Programlama Örnekleri String İşlemleri 05
author: sonsuz
date: 2023-08-18 00:01:15 +0300
categories: [Program,C]
tags: [c,programlama,alıştırma,algoritma,örnek]
---

## C programlama ile Her Harfin Tekrar Sayısını Bulma

```c
/* Her Harfin Tekrar Sayısını Bulma (1)

//String (Karakter Tutan Diziler)

//While ile

Klavyeden girilen bir metnin içerisinde her harfin tekrar sayısını bularak ekrana yazdıran C kodu

ASCII Değerleri A=65,a=97,enter=13

*/

#include <stdio.h>
#include <locale.h> 
#define SIZE 150

int main()
{
	setlocale(LC_ALL, "Turkish");

	char metin[256];
	int i=0,j;
	int sayac[SIZE] = { 0 };

	printf("Metin Giriniz: ");
	gets(metin);

	while (metin[i] != NULL)
	{
		sayac[metin[i] - 65]++;
		i++;
	}

	for (j = 0; j < SIZE; j++)
	{
		if (sayac[j] != 0)
			printf("%d tane %c harfi vardir.\n", sayac[j], j + 65);
	}

	getch();

	return 0;
}

```

## Metni Tersten Yazdırma Programı

```c
/* Metni Tersten Yazdırma Programı

//String (Karakter Tutan Diziler)
//For ile
//Fonksiyonla yazımı

Klavyeden girilen metni tersten ekrana yazdıran C programı */

#include <stdio.h>
#include <locale.h> 
#define SIZE 100

int uzunlukbulma(char metin[])
{

	int i = 0; // karakter sayısını alacak


	while (1) // Sonsuz Döngü
	{
		if (metin[i] == '\0') // '\0' simgesi NULL(bos) karakter
		{
			break; //NULL gelince sonsuz döngüden çıkıyoruz
		}

		i++;

	}

	return i; //Metnin uzunluğunu verir.

	/* Alternatif
	while(metin[i] != '\0')  //Null görene kadar dönmeye devam eder.
		{
			i++;
		}
			return i;
	*/

}


int main()
{
	setlocale(LC_ALL, "Turkish");

	char metin[SIZE];

	printf("Metin giriniz: ");
	gets(metin);    // alternatif: scanf("%s", metin);

	int uzunluk = uzunlukbulma(metin);

	int sayac = 0;


	printf("\nMetnin Tersi: ");
	
	for (sayac = uzunluk - 1; sayac >= 0; sayac--)
	{
		putchar(metin[sayac]); // printf("%c", metin[sayac]) //Belirtilen karakteri ekrana yazar.
	}

	printf("\n");

}

```

## Kelimelerin Baş Harflerini Yazdırma

```c
/* Kelimelerin Baş Harflerini Yazdırma

//String (Karakter Tutan Diziler)
//While ile

Klavyeden girilen cümlede yer alan kelimelerin baş harflerini ekrana yazdıran programı C dilinde yazınız.

 >ASCII KOD< 
 32 = Space

 */

#include <stdio.h>
#include <locale.h>  
#define SIZE 256

int main()
{
	setlocale(LC_ALL, "Turkish");

	char cumle[SIZE];

	printf("Cümlenizi Giriniz: ");
	gets(cumle);

	int i = 1;
	int sayac = 0;

	printf("%c", cumle[0]); // alternatif: putchar(cumle[0])

	while (cumle[i] != '\0') // '\0' simgesi NULL(bos) karakter
	{
		if ((cumle[i] == 32) && (cumle[i + 1] != 32))
		{
			putchar(cumle[i + 1]);  // alternatif: printf("%c", cumle[i + 1]);
		}

		i++;
	}

	return 0;
}

```

## Büyük/Küçük Harf Değiştirme

```c
/* Büyük/Küçük Harf Değiştirme (1)

Büyük Harfleri Küçük, Küçük Harfleri Büyük Harf Yapan Program

//String (Karakter Tutan Diziler)
//While ile yazılan program

Klavyeden girilen bir ifadede yer alan büyük harfleri küçük harflere,
küçük harfleri büyük harflere hazır bir fonksiyon kullanmadan çeviren ve sonucu
ekrana yazdıran C programını yazınız.

(Örneğin İfade “BuGün hAVa güzel” ise Sonuç “bUgÜN HavA GÜZEL” olmalıdır).

 >ASCII KOD<
 65  = A
 90  = Z
 97  = a
 122 = z

 */

#include <stdio.h>
#include <locale.h> 


int main()
{
	setlocale(LC_ALL, "Turkish");

	char ifade[256];
	
	printf("Cümleyi Giriniz: ");
	gets(ifade);

	int i = 0;

	int fark = 'a' - 'A';

	while (ifade[i] != '\0') // '\0' simgesi NULL(bos) karakter
	{
		if (ifade[i] >= 'A' && ifade[i] <= 'Z')
		{
			ifade[i] += fark;
		}
		else if (ifade[i] >= 'a' && ifade[i] <= 'z')
		{
			ifade[i] -= fark;

		}
		
		printf("%c", ifade[i]); //alternatif: putchar(ifade[i])
		
		i++;
	}

	return 0;
}

```

## C Programlama ile Büyük/Küçük Harf Değiştirme

```c
/* Büyük/Küçük Harf Değiştirme (2)

Büyük Harfleri Küçük, Küçük Harfleri Büyük Harf Yapan Program


// String (Karakter Tutan Diziler)
// For ile yazılan program

Klavyeden girilen bir ifadede yer alan büyük harfleri küçük harflere,
küçük harfleri büyük harflere hazır bir fonksiyon kullanmadan çeviren ve sonucu
ekrana yazdıran C programını yazınız. (Örneğin İfade “BuGün hAVa güzel” ise Sonuç “bUgÜN HavA GÜZEL” olmalıdır).
*/

#include <stdio.h>
#include <locale.h> 

int main()
{
	setlocale(LC_ALL, "Turkish");
	char ifade[256];
	printf("ifadeyi giriniz: ");
	gets(ifade);

	int i;

	//While ile yapmak daha doğru olur.
	for (i = 0; i < 256; i++)
	{
		if ((ifade[i] >= 65) && (ifade[i] <= 90)) //harf buyukse
			ifade[i] = ifade[i] + 32;
		else if ((ifade[i] >= 97) && (ifade[i] <= 122)) //harf buyukse
			ifade[i] = ifade[i] - 32;
		else if (ifade[i] == '\0') //ifade bittiyse
			break;
	}

	printf("\n");

	puts(ifade);

	return 0;
}

```

## Kaç Tane Karakter Var Hesaplama

```c
/* Kaç Tane Karakter Var Hesaplama

//String (Karakter Tutan Diziler)

Klavyeden girilen bir string içerisinde kelimelerden kaç tane "e" (İstediğini Yapabilirsin) karakteri geçtigini bulan c programı
*/


#include <stdio.h>
#include <locale.h> 

int main()
{
	setlocale(LC_ALL, "Turkish");

	char karakter[256];
	printf("Karakteri giriniz: ");
	gets(karakter);

	int i = 0;
	int sayac = 0;

	while (karakter[i] != '\0')
	{
		if (karakter[i] == 'e') //İstediğin karakteri yazabilirsin.
			sayac++;
		i++;
	}
	printf("\n%s ifadesinde %d tane karakter var", karakter, sayac);

	return 0;

}

```

## Metnin Karakter Uzunluğunu Bulma

```c
/*Metnin Karakter Uzunluğunu Bulma

//String (Karakter Tutan Diziler)

Klavyeden girilen metnin karakter uzunluğu bulan C programı (Boşluklarda sayılır)
*/

#include <stdio.h>
#include <locale.h> 

void main() //Void yazıldığında fonksiyon geriye bir deger gondermez.
		//int main() yazmak istiyorsan sonuna return eklemen gerekir.
{

	setlocale(LC_ALL, "Turkish");

	char metin[256];
	int sayac = 0;
	printf("Metni Giriniz: ");
	gets(metin);

	while (metin[sayac] != '\0')
		sayac++;
	printf("Girilen metin %d karakterden oluşur.", sayac);

}

```

## Metnin Kelime Sayısını Bulan Program

```c
/*  Metnin Kelime Sayısını Bulan Program

//String (Karakter Tutan Diziler)
//While ile

Klavyeden girilen metnin kelime sayısını bulan C programı
*/

#include <stdio.h>
#include <locale.h> 

int main()
{
	setlocale(LC_ALL, "Turkish");

	char ifade[256];
	printf("ifadeyi giriniz: ");
	gets(ifade);

	int i = 0;
	int sayac = 0;

	while (ifade[i] == 32)
		i++;

	while (1)
	{
		if ((ifade[i] == 32) && (ifade[i - 1] != 32))
			sayac++;
		else if ((ifade[i] == '\0') && (ifade[i - 1] != 32))
		{

			sayac++;
			break;
		}
		i++;
	}

	printf("%s ifadesinde %d tane kelime var.\n", ifade, sayac);


	return 0;
}

```

## Metin İçerisinde Karakter Değiştirme

```c
/* Metin İçerisinde Karakter Değiştirme

//String (Karakter Tutan Diziler)

Klavyeden girilen bir cümle içerisinde yer alan tüm ‘a’ karakterlerini ‘A’ ile değiştiren
ve değiştirilmiş metin ile kaç karakter değiştirildiğini ekrana yazdıran programı C dili ile kodlayınız. */

#include <stdio.h>
#include <locale.h>

int main()
{
	setlocale(LC_ALL, "Turkish");

	char cumle[256];
	printf("Bir Cümle Giriniz: ");
	gets(cumle);

	int i = 0;
	int sayac = 0;

	while (cumle[i] != '\0')
	{
		if (cumle[i] == 'a') // if(cumle[i]==97)  
		{
			cumle[i] = 'A'; //cumle[i] = 65;
			sayac++;
		}
		i++;

	}
	printf("\nDeğiştirilen Cümle = %s\t %d tane a A'ye cevrildi\n", cumle, sayac);

	return 0;
}

```

## Büyük/Küçük Harf Sayısını Bulma

```c
/* Büyük/Küçük Harf Sayısını Bulma

//String (Karakter Tutan Diziler)


Klavyeden girilen metin içerisindeki küçük ve büyük harf sayısını bulan C programı


*/

#include <stdio.h>
#include <locale.h>

void main()
{
	setlocale(LC_ALL, "Turkish");

	char metin[100];

	int sayac = 0, kucuk_harf = 0, buyuk_harf= 0;

	printf("Metin giriniz: ");
	gets(metin);

	while (metin[sayac] != '\0')
	{
		char karakter = metin[sayac];
		
		if (karakter >= 'a' && karakter <= 'z')
			
			kucuk_harf++;
		
		else if (karakter >= 'A' && karakter <= 'Z')
			
			buyuk_harf++;
		
		sayac++;
	}

	printf("\nMetnin içerisinde %d küçük ve %d büyük harf bulunuyor.\n", kucuk_harf, buyuk_harf);

}

```

## Kelimenin İlk Harfini Büyük Yapma

```c
/* Kelimenin İlk Harfini Büyük Yapma

//String (Karakter Tutan Diziler)


Klavyeden girilen metnin içerisindeki kelimelerin sadece ilk harfini büyük yazan C programı

Örnek= merhaba dünya -> Merhaba Dünya
*/

#include <stdio.h>
#include <locale.h>

int main()
{
	setlocale(LC_ALL, "Turkish");

	char metin[256];

	int i=0;

	int durum=1;
		
	printf("Metin Giriniz:");
	gets(metin);
		
	while (metin[i] != 0)
	{
		if (durum)
		{
			if (metin[i] >= 'a' && metin[i] <= 'z')
				
				metin[i] -= 32;
				durum = 0;
		}
		
		else
		{
			if (metin[i] >= 'A' && metin[i] <= 'Z')
				
				metin[i] += 32;
		}
			
		if (metin[i] == ' ' || metin[i] == '.')
			
			durum = 1;
			
		i++;
	}
		
	printf("%s", metin);
	
	return 0;

}

```

## Harf/Rakam/Özel Karakter Sayılarını Bulma

```c
/* Harf/Rakam/Özel Karakter Sayılarını Bulma

//String (Karakter Tutan Diziler)

Klavyeden girilen metin içerisinde harf, rakam ve özel karakterlerin sayısını bulan C Programı

 >ASCII KOD<
 48  = 0
 57  = 9 
 65  = A
 90  = Z
 97  = a
 122 = z

 */

#include <stdio.h>
#include <locale.h>
#define SIZE 256

int main()
{
	setlocale(LC_ALL, "Turkish");

	char metin[SIZE];

	int i = 0;

	int harf = 0, rakam = 0, ozel = 0;

	printf("Metin giriniz: ");
	gets(metin);

	while (metin[i] != 0)
	{
		char karakter = metin[i];

		if ((karakter >= 'a' && karakter <= 'z') || (karakter >= 'A' && karakter <= 'Z'))
			harf++;

		else if (karakter >= '0' && karakter <= '9')
			rakam++;

		else
			ozel++;

		i++;
	}

	printf("\nHarf Sayısı= %d \nRakamların Sayısı= %d \nÖzel Karakterlerin Sayısı= %d\n", harf, rakam, ozel);

	return 0;
}

```

## Metin de Aranan Kelimenin Olup Olmadığına Bakma

```c
/* Metin de Aranan Kelimenin Olup Olmadığına Bakma

//String (Karakter Tutan Diziler)

*/

#include <stdio.h>
#include <locale.h>

int main()
{
	setlocale(LC_ALL, "Turkish");

	char metin[256];

	char arama[256];

	int sayac_1 = 0, sayac_2 = 0;

	int durum = 0;

	printf("Metin Giriniz: ");
	gets(metin); //alternatif: scanf("%s", metin);

	printf("\nMetinde Aranması Gereken Kelime: ");
	gets(arama);

	while (metin[sayac_1] != 0)
	{
		sayac_2 = 0;

		if (metin[sayac_1] == arama[sayac_2])
		{
			while (metin[sayac_1 + sayac_2] == arama[sayac_2])
				sayac_2++;

			if (arama[sayac_2] == '\0')
				durum = 1;
		}

		if (durum == 1) 
			break;
		
		sayac_1++;
	}
	
	if (durum)
		
		printf("\nAranan kelime, metin içerisinde bulunuyor.\n");
	else
		
		printf("\nAranan kelime, metin içerisinde bulunmuyor.\n");
	
	return 0;
}

```

## Metnin Her Kelimesinin Harf Sayısını Bulma

```c
/* Metnin Her Kelimesinin Harf Sayısını Bulma

//String (Karakter Tutan Diziler)

*/

#include <stdio.h>
#include <locale.h>
#define SIZE 256



int uzunlukbulma(char metin[])
{
	int i = 0;

	while(metin[i] != '\0')  //Null görene kadar dönmeye devam eder.
		{
			i++;
		}
			return i;

}


int main()
{
	setlocale(LC_ALL, "Turkish");


	char metin[SIZE];
	char ifade[SIZE] = { 0 };

	int i, sayac = 0;

	printf("Metin giriniz: ");
	gets(metin);    // alternatif: scanf("%s", metin);

	int uzunluk = uzunlukbulma(metin);


	for (i = 0; i < uzunluk; i++)
	{
		if (metin[i] == ' ')
		{
			sayac++;
		}

		else
		{
			ifade[sayac]++;
		}
	}

	for (i = 0; i <= sayac; i++)
	{
		printf("\n%d. Kelime: %d harf var.\n", i+1, ifade[i]);
	}

	return 0;
}

```

## C Programlama ile Büyük Ünlü Uyumu

```c
/* Büyük Ünlü Uyumu

//String (Karakter Tutan Diziler)

*/

#include <stdio.h>
#include <locale.h>



int uzunlukbulma(char metin[])
{
	int i = 0;

	while (metin[i] != '\0')  //Null görene kadar dönmeye devam eder.
	{
		i++;
	}
	return i;

}

int main()
{
	setlocale(LC_ALL, "Turkish");

	char metin[100];

	int kalin = 0, ince = 0;

	printf("Metin Giriniz: ");
	gets(metin);

	int uzunluk = uzunlukbulma(metin);

	for (int i = 0; i < uzunluk; i++)
	{
		
		if (metin[i] == 'a' || metin[i] == 'ı' || metin[i] == 'o' || metin[i] == 'u')
			kalin++;

		if (metin[i] == 'e' || metin[i] == 'i' || metin[i] == 'ö' || metin[i] == 'ü')
			ince++;

	}

	if (kalin != 0 && ince != 0)
		printf("\nBüyük Ünlü Uyumuna Uymaz\n");

	else
		printf("\nBüyük Ünlü Uyumuna Uyar\n");

	return 0;

}

```

## Her Harfin Tekrar Sayısını Bulma (2)

```c
/* Her Harfin Tekrar Sayısını Bulma (2)

//String (Karakter Tutan Diziler)

//Fonksiyon ile yazımı

//While ile

Klavyeden girilen bir metnin içerisinde her harfin tekrar sayısını bularak ekrana yazdıran C kodu

ASCII Değerleri A=65,a=97,enter=13
*/

#include <stdio.h>
#include <locale.h> 
#define SIZE 150


void fonksiyon(char x[], int sayac[])
{
	int i = 0;
	
	while (x[i] != '\0')
	{
		if (x[i] >= 'a' && x[i] <= 'z')
			
			sayac[x[i] - 'a']++;

		else if (x[i] >= 'A' && x[i] <= 'Z')
			
			sayac[x[i] - 'A']++;
		
		i++;
	}
}

int main()
{
	setlocale(LC_ALL, "Turkish");

	char metin[256];
	int i;
	int sayac[SIZE] = { 0 };

	printf("Metin Giriniz: ");
	gets(metin);

	fonksiyon(metin, sayac);

	for (i = 0; i < SIZE; i++)
	{
		if (sayac[i] != 0)
			printf("%d tane %c harfi vardir.\n", sayac[i], i + 65);
	}
	
	getch();
		
	return 0;
}

```

## Her Satırda Bir Harf Ekleyerek Kelimeyi Yazma

```c
/* Her Satırda Bir Harf Ekleyerek Kelimeyi Yazma

//String (Karakter Tutan Diziler)

//While ile

Klavyeden girilen bir kelimenin harflerini her bir satıda bir harf ekleyerek ekrana yazdıran C Kodu

ÖRNEK:

Kelimeyi Giriniz: Hello

H
He
Hel
Hell
Hello

*/

#include <stdio.h>
#include <locale.h> 
#define SIZE 150

int main()
{
	setlocale(LC_ALL, "Turkish");

	char kelime[SIZE];

	int i = 0, j;
		  
	printf("Kelimeyi Giriniz: ");
	gets(kelime);

	while (kelime[i] != NULL)
	{
		for(j = 0; j <= i; j++)
		{
			putchar(kelime[j]);
		}

		printf("\n");

		i++;
	}

	getch();
}

```

## Örüntü Bulma

```c
/* Örüntü Bulma

//String (Karakter Tutan Diziler)

Klavyeden girilen bir karakter dizisinde kaç tane “ak” örüntüsünün olduğunu bulma

*/

#include <stdio.h>
#include <locale.h>



int uzunlukbulma(char metin[])
{
	int i = 0;

	while (metin[i] != '\0')  //Null görene kadar dönmeye devam eder.
	{
		i++;
	}
	return i;

}

int main()
{
	setlocale(LC_ALL, "Turkish");

	char metin[100];

	int sayac = 0,i;

	printf("Metin Giriniz: ");
	gets(metin);

	int uzunluk = uzunlukbulma(metin);

	for (i = 0; i < uzunluk; i++)
	{
		if (metin[i] == 'a' && metin[i + 1] == 'k')
		{
			sayac++;
		}
	}

	printf("\n%d tane 'ak' vardır.\n", sayac);

	return 0;

}

```
