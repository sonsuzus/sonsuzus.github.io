---
title:  C Programlama Örnekleri 07
author: sonsuz
date: 2023-08-18 00:30:15 +0300
categories: [Program,C]
tags: [c,programlama,alıştırma,algoritma,örnek,fonksiyon,bellek,sistem,işaretçi,pointer]
---

## C Programlama Dinamik olarak ayrılan bir hafıza bölgesine 1 ile 100 arasında rastgele oluşturulan 10 tane tam sayıyı yazan program

```c
/*
Dinamik olarak ayrılan bir hafıza bölgesine 1 ile 100 arasında rastgele oluşturulan
10 tane tam sayıyı yazan program

//Dinamik bellek ayırma yöntemi kullanımı
*/


#include <locale.h>  
#include <stdio.h>  
#include <stdlib.h>
#include <time.h>



int main()
{
	setlocale(LC_ALL, "Turkish");

	srand(time(NULL)); //Rastgele Sayı Üretimi

	int* p;

	int i;

	p = malloc(10 * sizeof(int));

	for (i = 0; i < 10; i++)
	{
		*(p + i) = 1 + (rand() % 100);

		printf("%2d. Eleman= %d\n", i + 1, *(p + i));

	}

}
```

## C Programlama Dizideki Elemanları Tersten Yazma (Pointer)

```c
/*
Dizideki Elemanları Tersten Yazma (Pointer)
Verilen dizi içerisinde yer alan sayıları pointer kullanarak ters şekilde sıralayan programı C dilinde yazınız.
*/


#include <stdio.h>  
#include <locale.h>  
#define SIZE 100

void main ()
{
	setlocale(LC_ALL, "Turkish");

	int dizi[SIZE];
	int i, N;
	int* ptr;



	printf("Dizinin Boyutunu Giriniz: ");
	scanf("%d", &N);

	printf("\nDizideki %d Elemanın Değerlerini Giriniz \n",N);

	ptr = &dizi[0]; // ptr, dizi[0] dizisinin adresini saklar


	for (i = 1; i <= N; i++)
	{
		printf("\n%d. Elemanı Giriniz: ", i);

		scanf("%d", ptr); //değerin adresini alır.

		ptr++; //Adresi artırır. Adres 4 byte artar. 

	}



	printf("\n--------------------------\n");

	printf("\nDizideki Elemanların Tersi\n");

	ptr = &dizi[N - 1];

	for (i = N; i > 0; i--)
	{
		printf("\n%d. Eleman= %d \n", i, *ptr); //*ptr dizideki değerleri verir.

		ptr--; //Adresi azaltır. Adres 4 byte azalır.
	}

}

```

## C Programlama Diziyi Artan Şekilde Yazma (pointer)

```c
/*
Diziyi Artan Şekilde Yazma

//Pointer Kullanımı

*/


#include <stdio.h>
#include <locale.h>  
#define SIZE 100

void main()
{
	setlocale(LC_ALL, "Turkish");

	int N;

	int dizi[SIZE];

	int i, j, k;

	int* ptr;


	printf("Dizinin Boyutunu Giriniz: ");
	scanf("%d", &N);

	printf("\nDizideki %d Elemanın Değerlerini Giriniz \n", N);

	ptr = &dizi[0]; // ptr, dizi[0] dizisinin adresini saklar

	for (i = 0; i < N; i++)
	{
		printf("\n%d. Elemanı Giriniz: ", i + 1);

		scanf("%d", ptr + i);

		/*
		Dizi, işaretçi değişkeni dizinin temel adresini gösteren işaretçiler yardımıyla getirilebilir.
		Bu nedenle, işaretçileri kullanarak diziyi sıralamak için,
		dizinin öğelerine (pointer + indeks) biçimini kullanarak erişmemiz gerekir.

		*/
	}

	for (i = 0; i < N; i++)
	{
		for (j = i + 1; j < N; j++)
		{
			if (*(ptr + i) > * (ptr + j))
			{
				k = *(ptr + i);
				*(ptr + i) = *(ptr + j);
				*(ptr + j) = k;
			}

		}
	}

	printf("\nKüçükten Büyüğe Sıralanmış Hali\n");


	for (i = 0; i < N; i++)
	{
		printf("\n%d. Eleman= %d \n", i + 1, *(ptr + i));

	}

}

```

## C Programlama Dizideki Metnin Tüm Permütasyonlarını Yazma

```c
/*
Dizideki Metnin Tüm Permütasyonlarını Yazma

//Pointer Kullanımı


*/



#include <stdio.h>  
#include <locale.h>  
#define SIZE 100



int uzunlukbulma(char metin[])
{
/*

strlen() fonksiyonun işlevini yapar.
(strlen fonksiyonu başlangıç adresini aldığı yazının uzunluğu ile geri döner.)

*/
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

int yerdegistirme(char *metin1, char *metin2)
{
	char k;

	k = *metin1;
	*metin1 = *metin2;
	*metin2 = k;

	return k;

}



void permutasyon(char* ptr,int x, int y)
{
	int i;

	if (x == y)
	{
		printf("%s\n", ptr);
	}
	else
	{
		for (i = x; i < y; i++)
		{
			yerdegistirme((ptr + x), (ptr + i));

			permutasyon(ptr, x + 1, y);

			yerdegistirme((ptr + x), (ptr + i));
		}
	}


}



int main()
	{
		setlocale(LC_ALL, "Turkish");


		char metin[SIZE];

		printf("Metin giriniz: ");
		gets(metin);    // alternatif: scanf("%s", metin);


		int uzunluk = uzunlukbulma(metin);


		permutasyon(metin, 0, uzunluk);


}

```

## C Programlama Dizinin En Büyük Elemanını Bulma

```c
/*
Dizinin En Büyük Elemanını Bulma

//Dinamik bellek ayırma yöntemi kullanımı

*/


#include <stdio.h>  
#include <locale.h>  
#include <stdlib.h>



int main()
{
	setlocale(LC_ALL, "Turkish");


	int i, n;

	int* ptr;


	printf("Dizinin Boyutunu Giriniz: ");
	scanf("%d", &n);

	ptr = (int*)calloc(n,sizeof(int));

	if (ptr == NULL)
	{
		printf("Yeterli Hafıza Alanı Yok!");
	
	}


	for (i = 0; i < n; i++)
	{
		printf("%d. Elemanı Giriniz: ", i + 1);
		scanf("%d", ptr + i);

	}

	for (i = 0; i < n; i++)
	{
		if (*ptr < *(ptr + i))
		{

			*ptr = *(ptr + i);

		}

	}

	printf("Dizinin En Büyük Elemanı = %d\n", *ptr);

	return 0;

}

```

## C Programlama Metni Tersten Yazdırma

```c
/*
Metni Tersten Yazdırma

//Pointer Kullanımı

*/

#include <stdio.h>  
#include <locale.h>  
#define SIZE 20

int main()
{
	setlocale(LC_ALL, "Turkish");


	char metin[SIZE];
	char tersi[SIZE];

	char* ptr_1 = metin;
	char* ptr_2 = tersi;

	int i = 0;

	printf("Metin giriniz: ");
	gets(metin);    // alternatif: scanf("%s", metin);


	while (*ptr_1)
	{

		ptr_1++;
		i++;

	}

	while (i >= 0)
	{
		ptr_1--;
		*ptr_2 = *ptr_1;
		ptr_2++;
		--i;
	}


	*ptr_1 = '\0';

	printf("Metnin Tersi: %s", tersi);

	return 0;

}

```

## C Programlama Rastgele Oluşan Dizideki Rakamları Tek Ve Çift Olarak Ayırma

```c
/*
Rastgele Oluşan Dizideki Rakamları Tek Ve Çift Olarak Ayırma
Dinamik bellek ayırma yöntemi kullanılarak 20 elemanlı bir dizi oluşturulacak.
Bu dizinin elemanları 1 ile 9 arasındaki sayıları rastgele değerlerle program dolduracak.
Oluşturulan dizideki rakamların tekleri bir diziye çiftleri ayrı bir diziye yerleştirerek çıktı oluşturulacak.
*/


#include <stdio.h>
#include <stdlib.h>
#include <locale.h> 
#include <time.h>


int main(void)
{
	setlocale(LC_ALL, "Turkish");

	srand(time(NULL)); //Rastgele Sayı Üretimi

	int i;

	int cift_sayac = 0;

	int tek_sayac = 0;

	int* dizi;  //Ana dizi için bir pointer

	int* cift;  //Çift sayılar için bir dizi

	int* tek;   //Tek Sayılar için bir dizi


	if ((dizi = malloc(20 * sizeof (int))) == NULL)
	{
		printf("YETERLI HAFIZA YOK");
	}

	cift = realloc(dizi, 20 * sizeof(int));


	if ((tek = malloc(20 * sizeof ( int))) == NULL)
	{
		printf("YETERLI HAFIZA YOK");
	}


	dizi = &dizi[0]; //Pointer ile dizi aynı isimle koyarak ekstra bir dizi tanımlamamıza gerek olmuyor.


	for (i = 0; i < 20; ++i)
	{

		dizi[i] = 1 + (rand() % 9);

		printf("%.2d. Eleman= %d\n", i + 1, dizi[i]);


		if (dizi[i] % 2 == 0) //Çift Kontrolü
		{
			cift[cift_sayac] = dizi[i];
			cift_sayac++;
		}

		else //diğerleri de tek oluyor.
		{
			tek[tek_sayac] = dizi[i];
			tek_sayac++;
		}
	}


	printf("\nÇİFT SAYILAR\n");

	for (i = 0; i < cift_sayac; i++)
	{
		printf("%d  ", cift[i]);
	}

	printf("\n");


	printf("\nTEK SAYILAR\n");

	for (i = 0; i < tek_sayac; i++)
	{
		printf("%d  ", tek[i]);
	}

	printf("\n");

	free(dizi);
	free(tek);

}

```

## C Programlama örnek

```c
#include <stdio.h>  


void main()
{

	int* m, ** p, *** k, myArray[5] = { 2,4,6,8,10 };

	m = &myArray[2]; //m artık MyArray[2] adresini tutuyor.

	p = &m;

	k = &p;

	printf("%p\n", **k); // MyArray[2] adresini verir.

	printf("%d\n", *(**(k)+2)); // MyArray[2] deydi 8 bayt giderse MyArray[4] dizisinin değerini verir.

	m = myArray; //m=&myArray[0] m dizinin ilk elemanın adresidir.

	printf("%d\n", *(*(p)+1)); //Output=4 

	**(p) += 7.26;

	m += 3; // m artık dizi[3] de başlıyor.

	printf("%d\n", *(*(p)-3)); //Output=9

	printf("%p\n", **k); // MyArray[3] adresini verir.

}

```

## C Programlama örnek 2

```c
#include <stdio.h>

int fun(int x, int y)
{
	if (x == y)
		return x;

	if (x > y)
	{
		printf("\n%d, %d\n", x, y);

		return fun(x - y, y);
	}

	return fun(x, y - x);
}

int main()
{
	int sayilar[] = { 132,48,55,47,-6 };

	int* ptr = &sayilar[3]; //ptr[0]=*(ptr+0)=sayilar[3] 


	/*  int* ptr;

	ptr= &sayilar[3];   */

	int sonuc = fun(sayilar[0], (*ptr) + 1);

	printf("\nfun(%d,%d) = %d\n", ptr[-3], *(ptr)+1, sonuc);

	return 0;
}

```

## C Programlama pointer örnek

```c
#include <stdio.h>
#include <locale.h> 


void main()
{
	double* m, ** k, myArray[5] = { 1.0,2.0,3.0,4.0,5.0 };

	m = myArray; //m=&myArray[0] m dizinin ilk elemanın adresidir.

	printf("%.1f\n", *(m + 1)); // Output=2.0

	*(m + 3) += 3.86; // myArray[3]= *(m+3) =7.86

	m += 2; // m artık dizi[2] de başlıyor.

	printf("%.1f\n", *(m + 1)); //Output=7.9

	m = &myArray[3]; //m artık MyArray[3] adresini tutuyor.

	k = &m;  

	printf("%.1f\n", *(*(k)-1)); //myArray[2] değerini verir.

	printf("%p\n", *k); //myArray[3]'ün adresini verir.

	m = m - 1;

	printf("%p", m); //myArray[2] adresini verir.
}

```

## C Programlama pointer işlemleri

```c
#include <stdio.h>


int x=0;

void main()
{
	int *ptr=&x; 
	/*
	aynı anlamda
	int *ptr;
	
	ptr=&x;
	*/
	
	printf("%p\n", ptr);
	
	x++;
	
	printf("%p\n", ptr);
}


/*Aynı Adres değerini verir.*/



```

## C Programlama dizi ve pointer

```c
#include <stdio.h>  


void main()
{

	double* m, ** k, myArray[5] = { 2.0,4.0,6.0,8.0,10.0 };


	m = &myArray[1];

	k = &m;

	
	printf("%p\n", *k); //myArray[1] adresini verir.

	printf("%.1f\n", *(*(k)+2)); //myArray[3] değerini verir. Output=8.0

	m = myArray;

	printf("%.1f\n", *(m + 1));  //Output=4.0

	*(m + 3) += 7.26;

	m += 2;

	printf("%.1f\n", *(m + 1)); //Output=15.30

	m -= 2;

	printf("%p\n", m); // myArray[0] adresini verir.
}

```
