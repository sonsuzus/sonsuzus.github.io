---
title:  C Programlama Örnekleri 04
author: sonsuz
date: 2023-08-17 23:56:15 +0300
categories: [Program,C]
tags: [c,programlama,alıştırma,algoritma,örnek]
---

## C Programlama ile Şans Oyunu

```c
/*
Şans Oyunu : Craps
•	İki zar atılır.
•	Zarların toplam hesaplanır.
•	İlk atışta 7 veya 11 gelirse oyuncu kazanır.
•	İlk atışta 2, 3 veya 12 gelirse oyuncu kaybeder.
•	İlk atışta 4, 5, 6, 8, 9 ve 10 gelirse bu oyuncunun puanı oluyor.
•	Oyuncu 7 atmadan önce kendi puanını tutturmalıdır.

*/


#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <locale.h>


int zaratma(void)
{
	int ilkzar, ikincizar, toplam;

	ilkzar = 1 + (rand() % 6);

	ikincizar = 1 + (rand() % 6);

	printf("İlk Zar: %d \n", ilkzar);
	printf("İkinci Zar: %d \n", ikincizar);

	toplam = ilkzar + ikincizar;
	printf("Oyuncunun Puanı: %d + %d = %d \n", ilkzar, ikincizar, toplam);
	printf("\n");


	return toplam;

}



int main()
{
	setlocale(LC_ALL, "Turkish");

	int atis, puan, sonuc;


	srand(time(NULL)); //Rastgele Sayı Üretimi


	atis = zaratma();


	if (atis == 7 || atis == 11)
	{
		sonuc = 1;
		printf("OYUNCU KAZANDI\n");
	}

	else if (atis == 2 || atis == 3 || atis == 12)
	{
		sonuc = 2;
		printf("OYUNCU KAYBETTİ\n");
	}


	else     //else if (atis == 4 || atis == 5 || atis == 6 || atis == 8 || atis == 9 || atis == 10)
	{
		sonuc = 3;

	}

	while (sonuc == 3)
	{

		puan = zaratma();

		if (puan == atis)

		{
			sonuc = 1;
			printf("OYUNCU KAZANDI\n");
		}

		else if (puan == 7)

		{
			sonuc = 2;
			printf("OYUNCU KAYBETTİ\n");
		}

	}
	return 0;

}

```

## Tam Sayının Üssünü Almak

```c
/* Tam Sayının Üssünü Almak

C program to find power of a number using function

Write a C program to input a number from user and find power of given number.

// Fonksiyon Kullanımı

*/

#include <stdio.h>    
#include <locale.h>  


int fonk(int x, int y)
{
	int i;

	int sonuc = 1;

	for (i = 0; i < y; i++)
	{
		sonuc *= x;
	}

	return sonuc;
}

int main()
{

	setlocale(LC_ALL, "Turkish");

	int x, y;

	printf("Lütfen bir tam sayı giriniz: ");
	scanf("%d", &x);

	printf("\n");

	printf("Lütfen üssünü giriniz: ");
	scanf("%d", &y);

	printf("\nSonuç: %d\n", fonk(x, y));

}

```

## Fonksiyon ile Dizinin En Büyük ve En Küçük Elemanını Bulma

```c
/* Dizinin En Büyük ve En Küçük Elemanını Bulma

// Dizi ve İşlevi
// Fonksiyon ile

*/

#include <stdio.h>
#include <locale.h> 
#define SIZE 100

void fonksiyon(int dizi[], int N)
{

	int min = 0, max = 0;
	int i;

	max = dizi[0];
	min = dizi[0];

	for (i = 1; i < N; i++)
	{
		if (dizi[i] > max)
		{
			max = dizi[i];
		}
		if (dizi[i] < min)
		{
			min = dizi[i];
		}
	}

	printf("\nEn Büyük Sayı = %d\n", max);
	printf("\nEn Küçük Sayı = %d\n", min);
}


int main()
{
	setlocale(LC_ALL, "Turkish");

	int dizi[SIZE], N;
	int i;

	printf("Dizinin Boyutunu Giriniz: ");
	scanf("%d", &N);

	printf("\n");

	for (i = 0; i < N; i++)
	{
		printf("%.2d. Elemanı Giriniz: ", i + 1);
		scanf("%d", &dizi[i]);
	}

	fonksiyon(dizi, N);
	return 0;
}

```

## Fonksiyon ile Girilen Sayıyı Tersten Yazan Program

```c
/* Girilen Sayıyı Tersten Yazan Program

//Fonksiyon Kullanımı

*/

#include <stdio.h>
#include <locale.h>

int tersinialma(int sayi)
{
	int ters = 0, basamak;

	while (sayi != 0)
	{

		basamak = sayi % 10;
		ters = ters * 10 + basamak;
		sayi /= 10;

	}

	return ters;
}

int main()
{

	setlocale(LC_ALL, "Turkish");

	int sayi;

	printf("Tam Sayı Giriniz: ");
	scanf("%d", &sayi);

	printf("\nSayının Tersi: %d\n", tersinialma(sayi));

	return 0;
}

```

## İki Sayı Arasındaki Asal Sayıları Bulma

```c
#include <stdio.h>
#include <locale.h>

/* İki Sayı Arasındaki Asal Sayıları Bulma


C Program to Display Prime Numbers Between Intervals Using Function
Example to print all prime numbers between two numbers (entered by the user) by making a user-defined function.

//Fonksiyon Kullanımı


*/

int func(int sayi);


int main()
{
	setlocale(LC_ALL, "Turkish");

	int sayi1, sayi2;
	int i, j;

	printf("İki pozitif tam sayı giriniz: \n");
	scanf("%d %d", &sayi1, &sayi2);

	printf("\n");
	printf("İki sayı arasındaki asal sayılar: \n");

	for (i = sayi1 + 1; i < sayi2; ++i)
	{
		j = func(i);
		if (j == 1)
			printf("%d\n", i);
	}

	return 0;
}

int func(int sayi)
{
	int k, j = 1;

	for (k = 2; k <= sayi / 2; ++k)
	{
		if (sayi % k == 0)
		{
			j = 0;
			break;
		}
	}
	return j;
}

```

## Diziyi Artan ve Azalan Şekilde Yazma

```c
/*

Diziyi Artan ve Azalan Şekilde Yazma

C Fonksiyonu kullanarak bir diziyi artan ve azalan düzende Sıralama Programı


C Program to Sort an array in ascending and descending order using function
Code for Sorting of array elements using a function in C Programming

//Fonksiyon Kullanımı

*/


#include <stdio.h>  
#include <locale.h>  
#define MAX_SIZE 100


int diziyisirala(int dizi[], int N)
{
	int i, j, k;

	for (i = 0; i < N; i++)
	{
		for (j = i + 1; j < N; j++)
		{
			if (dizi[i] > dizi[j])
			{
				k = dizi[i];
				dizi[i] = dizi[j];
				dizi[j] = k;
			}

		}
	}

}

int diziyisirala2(int dizi[], int N)
{
	int i, j, k;

	for (i = 0; i < N; i++)
	{
		for (j = i + 1; j < N; j++)
		{
			if (dizi[i] < dizi[j])
			{
				k = dizi[i];
				dizi[i] = dizi[j];
				dizi[j] = k;
			}

		}
	}

}


int main()
{
	setlocale(LC_ALL, "Turkish");

	int dizi[MAX_SIZE];
	int i, N;


	printf("Dizinin Boyutunu Giriniz: ");
	scanf("%d", &N);


	for (i = 0; i < N; i++)
	{
		printf("%d. Elemanı Giriniz: ", i + 1);
		scanf("%d", &dizi[i]);
	}


	printf("\n\n");

	printf("Girilen Dizi\n");
	for (i = 0; i < N; i++)
	{
		printf("%d ", dizi[i]);
	}



	printf("\n\n");


	diziyisirala(dizi, N);

	printf("Küçükten Büyüğe Sıralanmış Hali:\n");

	for (i = 0; i < N; i++)
	{
		printf("%d ", dizi[i]);
	}

	printf("\n\n");


	diziyisirala2(dizi, N);

	printf("Büyükten Küçüğe Sıralanmış Hali:\n");

	for (i = 0; i < N; i++)
	{
		printf("%d ", dizi[i]);
	}

	printf("\n\n");


	return 0;
}

```

## C Programlama ile Rastgele Sıralama Oluşturma

```c
/*
Rastgele sırada sunum yapılması için bir program yazılması gerekmektedir. 
Sunum listesi bir dizide saklanmalıdır. rastgeleSıralamaOlustur isimli bir fonksiyonu diziyi ve 
dizinin boyutunu parametre olarak alacak şekilde yazınız. Lütfen programın tamamını kodlayınız.


In order to make a presentation in random order, a program must be written. 
The presentation list should be stored in an array. Write a function called generateRandomOrder 
which takes an array and size of the array as a parameter. Please write the entire program.


*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <locale.h>
#define SIZE 100


int rastgeleSiralamaOlustur(int dizi[], int x)

{
	int i, j = 0, random;

	for (i = 0; i < x; i++)
	{
		random = 1 + rand() % x;

		for (j = 0; j <= i; j++)
		{
			if (i == j) //Eğer üretilen sayı önceki değerlerden farklıysa
			{
				dizi[i] = random;
			}
			else if (random == dizi[j]) // Eğer üretilen sayı dizide ise
			{
				i--;
				break;
			}

		}

	}

}


int main()
{
	setlocale(LC_ALL, "Turkish");

	srand(time(NULL)); ////Rastgele Sayı Üretimi

	int ogrenci_sayisi;

	printf("Öğrenci Sayısını Giriniz: ");
	scanf("%d", &ogrenci_sayisi);

	int dizi[SIZE];

	rastgeleSiralamaOlustur(dizi, ogrenci_sayisi);

	int i = 0;

	for (i = 0; i < ogrenci_sayisi; i++)
		printf("%d. Sırada Sunacak Kişi - Listedeki %d. Öğrenci\n", i + 1, dizi[i]);

	return 0;

}

```

## C Programlama ile Vücut Kitle İndeksi Bulma

```c
/*

Boy ve kilo bilgisini alarak vücut kitle indeksini hesaplayan kitleIndeks isimli bir fonksiyon yazınız. 
Bu fonksiyon aşağıda verilen tabloya göre değer döndürmektedir. 

Yazdığınız fonksiyonu main fonksiyonunda çağırarak kullanın ve bir program yazınız. Programın örnek çalışması şekilde verildiği gibi olmalıdır. 
Vücut kitle indeksi hesabı aşağıda verilmiştir.


Write a function named bodyIndex that computes body mass index by taking height and weight information. Write a program that calls the function in the main. 
The sample output of the program should be as it is given.


*/


#include <stdio.h>  
#include <locale.h>  


int kitleindeks(float boy, float kilo)
{

	float indeks;

	indeks = kilo / (boy * boy);

	if (indeks <= 18)
	{
		return 1;
	}

	else if (indeks <= 25)
	{
		
		return 2;
	}

	else if (indeks <= 30)
	{
		
		return 3;
	}

	else
	{
		return 4;
	}
}


int main()
{

	setlocale(LC_ALL, "Turkish");

	float boy=0, kilo=0;

	printf("Boyunuzu ve Kilonuzu Giriniz: "); //boyu metre cinsinden kiloyu da kg cinsinden giriniz.
	scanf("%f %f", &boy, &kilo);


	int sonuc = kitleindeks(boy, kilo);

	if(sonuc==1)
		printf("ZAYIF");

	else if(sonuc==2)
		printf("NORMAL");

	else if(sonuc==3)
		printf("KİLOLU");

	else
		printf("OBEZ");		

}

```
