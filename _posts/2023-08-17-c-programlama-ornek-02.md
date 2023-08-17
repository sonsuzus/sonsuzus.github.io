---
title:  C Programlama Örnekleri 02
author: sonsuz
date: 2023-08-17 23:40:15 +0300
categories: [Program,C]
tags: [c,programlama,alıştırma,algoritma,örnek]
---

## Tek Sayıların Toplamı

```c
/* Tek Sayıların Toplamı

// While Kullanımı

Klavyeden çift sayı girilene kadar girilmiş olan tek sayıların toplamını hesaplayıp yazdıran programı C dili ile yazınız*/


#include <stdio.h>  
#include <locale.h>  


int main()
{
	setlocale(LC_ALL, "Turkish");
		
    int sayi, toplam=0;
    
    printf("Bir sayı giriniz: ");
    
    scanf("%d", &sayi);

   
    while (sayi%2!=0)
    {
        toplam+=sayi;
        printf("Bir Sayı Giriniz: ");
        scanf("%d", &sayi);
    }
    
	printf("Tek Sayıların Toplamı = %d", toplam);
    return 0;
 }

```

## En Büyük ve En Küçük Sayıyı Bulma

```c
/* En Büyük ve En Küçük Sayıyı Bulma

//While Kullanımı

Kullanıcı klavyeden -1 girene kadar girilmiş olan sayıların en büyüğü ile en küçüğünü ekrana yazdıran program*/

#include <stdio.h>
#include <locale.h>  

int main()
{
	setlocale(LC_ALL, "Turkish");

	float sayi, max, min;
	printf("Sayı Giriniz: ");
	scanf("%f", &sayi);

	min = sayi;
	max = sayi;

	while (sayi != -1)
	{

		if (sayi > max)
			max = sayi;

		if (sayi < min)
			min = sayi;

		printf("Sayı Giriniz: ");
		scanf("%f", &sayi);

	}
	printf("En Büyük Sayı: %.2f\n", max);
	printf("En Küçük Sayı: %.2f", min);

}

```

## Girilen Değerlerin Ortalamasını Hesaplama

```c
/* Girilen Değerlerin Ortalamasını Hesaplama

//For Kullanımı

SIZE (#define SIZE İstediğin Sayı) elemanlı bir dizideki değerleri toplayıp ortalamasını yazan program. */

#include <stdio.h>
#include <locale.h>  
#define SIZE 3

int main()
{
	setlocale(LC_ALL, "Turkish");

	int i;
	float a[SIZE], ort, toplam;
	toplam = 0;

	for (i = 0; i < SIZE; i++)

	{
		printf("Sayı Giriniz: ");
		scanf("%f", &a[i]);
		toplam = toplam + a[i];
	}


	ort = toplam / SIZE;
	printf("Ortalama=%.2f", ort);

	return 0;
}

```

## Bir Sayı Diğer Sayının Katı Mıdır?

```c
/*  Bir Sayı Diğer Sayının Katı Mıdır? */

#include <stdio.h>
#include <locale.h>

int main()

{

	setlocale(LC_ALL, "Turkish");

	int buyukSayi, kucukSayi;

	printf("Lutfen once büyük sayıyı sonra küçük sayıyı giriniz...\n");

	scanf("%d %d", &buyukSayi, &kucukSayi);


	if (buyukSayi % kucukSayi == 0)
	{

		printf("Katıdır\n");

	}

	else
	{

		printf("Katı Değildir\n");

	}

	return 0;
}

```

## Girilen Sayıyı Tersten Yazan Program

```c
/*Girilen Sayıyı Tersten Yazan Program

// While Kullanımı
*/

#include <stdio.h>
#include <locale.h>

int main()
{

	setlocale(LC_ALL, "Turkish");

	int sayi, ters = 0, basamak;

	printf("Tam Sayı Giriniz:  ");
	scanf("%d", &sayi);

	while (sayi != 0)
	{

		basamak = sayi % 10;
		ters = ters * 10 + basamak;
		sayi /= 10;

	}

	printf("Sayının Tersi:  %d", ters);
	return 0;
}

```

## İki Sayının EBOB'unu Bulan Program

```c
/* İki Sayının EBOB'unu Bulan Program */

#include <stdio.h>
#include <locale.h>

int main()

{

	setlocale(LC_ALL, "Turkish");

	int x, y, min;

	int i, ebob = 1;

	printf("Birinci Sayıyı Giriniz:");
	scanf("%d", &x);

	printf("Ikinci Sayıyı Giriniz:");
	scanf("%d", &y);

	if (x < y)
		min = x;
	min = y;

	for (i = 2; i <= min; i++)

	{
		if (x % i == 0 && y % i == 0)
			ebob = i;
	}

	printf("EBOB(%d,%d) = %d", x, y, ebob);


	return 0;
}

```
