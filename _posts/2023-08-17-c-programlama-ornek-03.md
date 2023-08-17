---
title:  C Programlama Örnekleri 03
author: sonsuz
date: 2023-08-17 23:54:15 +0300
categories: [Program,C]
tags: [c,programlama,alıştırma,algoritma,örnek]
---

## Dizideki Elemanların Ortalaması

```c
/* Dizideki Elemanların Ortalaması


*/

#include <stdio.h>
#include <locale.h>
#define MAX_SIZE 100



int main()

{
	setlocale(LC_ALL, "Turkish");

	float dizi[MAX_SIZE];
	int i, N;
	float toplam=0;

	printf("Dizinin Boyutunu Giriniz: ");
	scanf("%d", &N);

	for (i = 0; i < N; i++)
	{
		printf("%.2d. Elemanı Giriniz: ", i + 1);
		scanf("%f", &dizi[i]);

		toplam += dizi[i];
	}

	printf("\nGirilen Elemanların Ortalaması= %f\n", toplam / N);
	
	return 0;

}

```

## Dizinin En Büyük ve En Küçük Elemanını Bulma

```c
/* Dizinin En Büyük ve En Küçük Elemanını Bulma */

#include <stdio.h>
#include <locale.h>
#define SIZE 100 


int main()
{
	setlocale(LC_ALL, "Turkish");

	int dizi[SIZE];
	int i,N;
	int max=0, min=0;

	printf("Dizinin Boyutunu Giriniz: ");
	scanf("%d", &N);

	printf("\n");

	for (i = 0; i < N; i++)
	{
		printf("%.2d. Elemanı Giriniz: ", i + 1);
		scanf("%d", &dizi[i]);
	}

	max = dizi[0];
	min = dizi[0];

	for (i = 1; i < N; i++)
	{
		if (dizi[i] > max)
		{
			max = dizi[i];
		}
		else if (dizi[i] < min)
		{
			min = dizi[i];
		}
	}

	printf("\nEn Büyük Sayı = %d\n", max);
	printf("\nEn Küçük Sayı = %d\n", min);

	return 0;
}

```

## Dizi İçerisinde Sayı Arama ve o Sayıdan kaç tane olduğunu Yazan Program

```c
/* Dizi İçerisinde Sayı Arama ve o Sayıdan kaç tane olduğunu Yazan Program

Klavyeden girilen SIZE elemanlı dizi içerisinde klavyeden girilen sayının frekansını bulan C programı

*/

#include <stdio.h>
#include <locale.h>
#define SIZE 100

int main()
{
	setlocale(LC_ALL, "Turkish");

	int dizi[SIZE],N;
	int x;
	int frekans = 0;
	int i, toplam = 0;
	
	printf("Dizinin Boyutunu Giriniz: ");
	scanf("%d", &N);

	printf("\n");

	printf("Aranacak Sayı: ");
	scanf("%d", &x);

	printf("\n");


	for (i = 0; i < N; i++)
	{
		printf("%.2d. Elemanı Giriniz: ", i + 1);
		scanf("%d", &dizi[i]);
		if (dizi[i] == x)
			frekans++;
	}


	printf("\nDizi içerisinde %d adet, %d sayısı vardır.\n", frekans, x);
	
	return 0;
}

```
