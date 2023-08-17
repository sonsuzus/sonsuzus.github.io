---
title:  C Programlama Örnekleri Özyineleme - Rekürsif 06
author: sonsuz
date: 2023-08-18 00:15:15 +0300
categories: [Program,C]
tags: [c,programlama,alıştırma,algoritma,örnek,fonksiyon,rekürsif]
---

## C Programlama Faktöriyel Hesaplama (Rekürsif fonksiyon)

```c
/*

Faktöriyel Hesaplama
// Özyinelemeli Fonksiyon (Recursive Function)

*/


#include <stdio.h>  
#include <locale.h>  


int faktoriyel(int sayi)
{
	if (sayi >= 1)
	{

		return sayi * faktoriyel(sayi - 1);
	
	/*
		ÖRNEK= 5!

				5 * faktoriyel(5)
					4 * faktoriyel(3)
						3*faktoriyel(2)
							2 * faktoriyel(1)
								1 *faktoriyel(0)
										1
	*/
	}

	else
		return 1;
}





int main()
{
	setlocale(LC_ALL, "Turkish");

	int sayi;


	printf("Bir tam sayı giriniz: ");
	scanf("%d", &sayi);

	printf("%d!= %d\n", sayi, faktoriyel(sayi));


	return 0;

	/*
	while (1) //Sonsuz Döngü de olsun. Program bitmesin.
	{
		printf("Bir tam sayı giriniz: ");
		scanf("%d", &sayi);
		printf("%d!= %d\n", sayi, faktoriyel(sayi));
	}
	return 0;
	*/


}

```

## C Programlama İki Sayının EBOB ve EKOK'unu Bulan Program (Rekürsif Fonksiyon)

```c
/*
İki Sayının EBOB ve EKOK'unu Bulan Program


En Büyük Ortak Bölenini (Ebob) Bulma
(Her ikisini de tam bölen tam sayıların en büyüğüdür)
C program to find GCD (HCF) of two numbers using recursion


En Küçük Ortak Kat (EKOK)Bulma
C program to find LCM of two numbers using recursion


// Özyinelemeli Fonksiyon (Recursive Function)
*/


#include <stdio.h>  
#include <locale.h>  


int ebob(int sayi1, int sayi2)
{
	if (sayi2 != 0)
	{
		return ebob(sayi2, sayi1 % sayi2);
	}

	else
	{
		return sayi1;
	}

}

int ekok(int sayi1, int sayi2)
{

	return (sayi1 * sayi2) / ebob(sayi1, sayi2);

}



int main()
{
	setlocale(LC_ALL, "Turkish");

	int sayi1, sayi2;
	int EBOB, EKOK;


	printf("İki Sayı Giriniz: \n");
	scanf("%d  %d", &sayi1, &sayi2);

	if (sayi1 > sayi2)
	{
		EBOB = ebob(sayi1, sayi2);
		EKOK = ekok(sayi1, sayi2);
	}
	else

		EBOB = ebob(sayi2, sayi1);
		EKOK = ekok(sayi2, sayi1);


	printf("EBOB(%d,%d)= %d", sayi1, sayi2, EBOB);
	printf("\nEKOK(%d,%d)= %d", sayi1, sayi2, EKOK);


	return 0;

}

```

## C Programlama Tam Sayının Üssünü Almak Özyinelemeli Fonksiyon (Rekürsif Fonksiyon)

```c
/*

Tam Sayının Üssünü Almak

// Özyinelemeli Fonksiyon (Recursive Function)

*/


#include <stdio.h>  
#include <locale.h>  


int fonk(int sayi1, int sayi2)
{
	if (sayi2 != 0)
	{
		return sayi1 * fonk(sayi1, sayi2 - 1);


	/*
		ÖRNEK= 2^3

		2*fonk(2,2)
			2*fonk(2,1)
				2*fonk(2,0)
					   1	
		
	*/

	}

	else

		return 1;


}



int main()
{
	setlocale(LC_ALL, "Turkish");

	int sayi1, sayi2;

	printf("Lütfen bir tam sayı giriniz: ");
	scanf("%d", &sayi1);

	printf("Lütfen üssünü giriniz: ");
	scanf("%d", &sayi2);

	int sonuc = fonk(sayi1, sayi2);

	printf("%d ^ %d = %d", sayi1, sayi2, sonuc);


	return 0;

}

```

## C Programlama İki Sayı Arasındaki Tam Sayıları Yazdırma (Rekürsif Fonksiyon Kullanarak)

```c
/*

İki Sayı Arasındaki Tam Sayıları Yazdırma

Program to print integers in a given range using recursion

// Özyinelemeli Fonksiyon (Recursive Function)

*/


#include <stdio.h>  
#include <locale.h>  


int fonk(int sayi1,int sayi2)
{
	
	if (sayi2 >= sayi1)
	{
		printf("%d ", sayi1);

		fonk(sayi1 + 1, sayi2);
	}

	else
		return 0;


}


int main()
{
	setlocale(LC_ALL, "Turkish");

	int sayi1, sayi2;

	printf("Lütfen bir tam sayı giriniz (AltSınır): ");
	scanf("%d", &sayi1);

	printf("\nLütfen bir tam sayı giriniz (Üst Sınır): ");
	scanf("%d", &sayi2);

	printf("\n%d ve %d arasındaki tam sayılar: \n", sayi1, sayi2);
	
	printf("\n");

    fonk(sayi1, sayi2);
	
	return 0;

}

```

## C Programlama İki Sayı Arasındaki Tam Sayıları Toplama 

```c
/*
İki Sayı Arasındaki Tam Sayıları Toplama 


C program to find sum of natural numbers in a given range using recursion

// Özyinelemeli Fonksiyon (Recursive Function)
*/


#include <stdio.h>  
#include <locale.h>  


int topla(int sayi1, int sayi2)
{

	if (sayi1 == sayi2)
	{
		return sayi1;
	}

	else
		return sayi1 + topla(sayi1 + 1, sayi2);


}


int main()
{
	setlocale(LC_ALL, "Turkish");

	int sayi1, sayi2;

	printf("Lütfen bir tam sayı giriniz (AltSınır): ");
	scanf("%d", &sayi1);

	printf("\nLütfen bir tam sayı giriniz (Üst Sınır): ");
	scanf("%d", &sayi2);

	printf("\n%d ve %d arasındaki tam sayıların toplamı: %d", sayi1, sayi2, topla(sayi1, sayi2));

	return 0;

}

```

## C Programlama İki Sayı Arasındaki Çift ve Tek Sayıları Yazdırma

```c
/*

İki Sayı Arasındaki Çift ve Tek Sayıları Yazdırma

Verilen aralıkta çift ve tek sayıların yazdırılması için C programı
C program to print even and odd numbers in given range using recursion

// Özyinelemeli Fonksiyon (Recursive Function)

*/


#include <stdio.h>  
#include <locale.h>  


int fonk(int sayi1,int sayi2)
{
	

	if (sayi2 >= sayi1)
	{
		if (sayi1 % 2 != 0)
		{
			
			printf("Tek : %d\n", sayi1);
			return fonk(sayi1 + 1, sayi2);



		}

		else if (sayi1 % 2 == 0)
		{
			
			printf("Çift: %d\n", sayi1);
			return fonk(sayi1 + 1, sayi2);
	
		}
	}

	else
		return 0;

}



int main()
{
	setlocale(LC_ALL, "Turkish");

	int sayi1, sayi2;

	printf("Lütfen bir tam sayı giriniz (AltSınır): ");
	scanf("%d", &sayi1);

	printf("\nLütfen bir tam sayı giriniz (Üst Sınır): ");
	scanf("%d", &sayi2);

	fonk(sayi1 + 1, sayi2);

	return 0;

}

```

## C Programlama Sayının Tersini Yazma (Rekürsif Fonksiyon ile)
 
```c
/*
Sayının Tersini Yazma

Girilen Sayı Değerinini tersten yazan program
C program to find reverse of a number using recursion

// Özyinelemeli Fonksiyon (Recursive Function)

*/


#include <stdio.h>  
#include <locale.h>  


int ters = 0;
int basamak;



int tersinialma(int sayi)
{

	if (sayi)
	{
		basamak = sayi % 10;
		ters = ters * 10 + basamak;
		tersinialma(sayi /10);
	}

	else
		return ters;

}


int main()
{
	setlocale(LC_ALL, "Turkish");

	int sayi;


	printf("Lütfen bir tam sayı giriniz: ");
	scanf("%d", &sayi);


	printf("\nSayının Tersi: %d", tersinialma(sayi));

	return 0;

}

```

## C Programlama Metni Tersten Yazdırma Programı (Rekürsif Fonksiyon)

```c
/*

Metni Tersten Yazdırma Programı


// Özyinelemeli Fonksiyon (Recursive Function)

*/


#include <stdio.h>  
#include <locale.h>  



int ters() 

{
	char metin; 
	scanf("%c", &metin);  

	if (metin != '\n')
	{
	

		ters();  

		printf("%c", metin);

	}
}


int main()
{
	setlocale(LC_ALL, "Turkish");


	printf("Lütfen Metninizi Giriniz: \n");

	ters();

	
	return 0;

}

/*
int ters() fonksiyonu kullanıcı tarafından girilen ilk harfi metin değişkeninde saklar.

Değişken '\ n' dışında bir karakterse, ters () işlevi yeniden çağrılır.

ters () ikinci kez çağrıldığında, kullanıcı tarafından girilen ikinci harf tekrar metin 'e kaydedilir.
Ancak, ikinci fonksiyondaki metin değişkeni birincisiyle aynı değildir. Her ikisi de bellekte farklı yer tutarlar.


'\ n' girdiğinde, en son işlevi ters () işlevi  en son karakteri basar printf("%c", metin) nedeniyle
ve ikinci ters () işlevine geri döner.


Yine, ikinci son ters () işlevi, ikinci son karakteri basar ve 
üçüncü son ters () işlevine geri döner.

Bu süreç devam ediyor ve son çıktı ters metin olacak.

KAYNAK: https://www.programiz.com/c-programming/examples/reverse-sentence-recursion

*/

```

## C Programlama Girilen Sayının Palindromik Olup Olmadığını Bulmak

```c
/*

Girilen Sayının Palindromik Olup Olmadığını Bulmak
(Palindrom, tersten okunuşu da aynı olan cümle, sözcük ve sayılara denilmektedir.)

C program to check palindrome number using recursion

// Özyinelemeli Fonksiyon (Recursive Function)

*/


#include <stdio.h>  
#include <locale.h>  

int palindrome(int sayi);
int tersinialma(int sayi);

int ters = 0;
int basamak;


int main()
{
	setlocale(LC_ALL, "Turkish");

	int sayi;


	printf("Lütfen bir tam sayı giriniz: ");
	scanf("%d", &sayi);


	if (palindrome(sayi) == 1)
	{
		printf("%d sayısı palindromik bir sayıdır.\n", sayi);
	}
	else
	{
		printf("%d sayısı palindromik bir sayı değildir.\n", sayi);
	}

	return 0;


}


int palindrome(int sayi)
{
	if (sayi == tersinialma(sayi))
	{
		return 1;
	}

	return 0;

}


int tersinialma(int sayi)
{

	if (sayi)
	{
		basamak = sayi % 10;
		ters = ters * 10 + basamak;
		tersinialma(sayi / 10);
	}

	else
		return ters;

}

```

## C Programlama Girilen Metnin(String) Palindromik Olup Olmadığını Bulmak

```c
/*

Girilen Metnin(String) Palindromik Olup Olmadığını Bulmak

(Palindrom, tersten okunuşu da aynı olan cümle, sözcük ve sayılara denilmektedir.)

// Özyinelemeli Fonksiyon (Recursive Function)
*/

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



int palindrome(char metin[], int uzunluk)
{
	if (uzunluk <= 0)
	{
		return 1;   //Uzunluk eğer sıfıra kadar gelebildiyse 1' döndürüyoruz.
	}

	else if (metin[0] == metin[uzunluk - 1])
	{
		return palindrome(metin + 1, uzunluk - 2);
	}

	else
	{
		return 0; //Yukarıdaki if ler doğru olmazsa sıfır döndürüyoruz.

	}

}



int main()
{
	setlocale(LC_ALL, "Turkish");


	char metin[SIZE];

	printf("Metin giriniz: ");
	gets(metin);    // alternatif: scanf("%s", metin);


	int uzunluk = uzunlukbulma(metin);

	/*
	Tersini Yazdırma

	int sayac = 0;


	printf("\nMetnin Tersi: ");

	for (sayac = uzunluk - 1; sayac >= 0; sayac--)

		putchar(metin[sayac]); // printf("%c", metin[sayac]) //Belirtilen karakteri ekrana yazar.

	*/


	int sonuc = palindrome(metin, uzunluk);

	if (sonuc == 1)  //Eğer sonuç 1 ise palindromdur.
	{
		printf("\n '%s' ifadesi palindromdur\n", metin);
	}

	else if (sonuc == 0) //Eğer sonuç 2 ise palindrom değildir.
	{
		printf("\n '%s' ifadesi polindrom değildir.\n", metin);
	}


}

/*

Örnek:KAZAK kelimesi

metin[0]: K
metin[1]: A
metin[2]: Z
metin[3]: A
metin[4]: K


****	uzunlukbulma(char metin[]) fonksiyonu; Bu kelimenin uzunluğunu bulacak. 
strlen() fonksiyonun işlevini yapar.
(strlen fonksiyonu başlangıç adresini aldığı yazının uzunluğu ile geri döner.)


****	palindrome(char metin[], int uzunluk) fonksiyonu; 

	if (5 <= 0) 'YANLIŞ'
	{
		return 1;   
	}

	else if (metin[0] == metin[4])  (  (metin[0]: KK)== (metin[4]: K) ) 'DOĞRU'
	{
		return palindrome(metin + 1, 5 - 2); başa geri dönüyor
	}

		if (3 <= 0) 'YANLIŞ'
		{
			return 1;   
		}	

		else if (metin[0] == metin[2]) ( (metin[1]: A) ==  (metin[3]: A) ) 'DOĞRU'

		{

			return palindrome(metin + 1, 3 - 2); başa geri dönüyor

		}
			
			if (1 <= 0) 'YANLIŞ'
			{
				return 1;
			}

			else if (metin[0] == metin[0])  ( (metin[2]: Z) == (metin[2]: Z) )  'DOĞRU'

			{

				return palindrome(metin + 1, 1 - 2 ); başa geri dönüyor

			}

				
				if (-1 <= 0) 'DOĞRU'

				{
					return 1; 
				}


**** int sonuc = palindrome(metin, uzunluk);

	if (sonuc == 1)  'DOĞRU'
	{
		printf("\n '%s' ifadesi palindromdur\n", metin);
	}


*/

```

## C Programlama Basamak Değerlerinin Toplamı (Rekürsif Fonksiyon)

```c
/*

Basamak Değerlerinin Toplamı

C program to find sum of digits using recursion

// Özyinelemeli Fonksiyon (Recursive Function)

*/


#include <stdio.h>  
#include <locale.h>  




int basamakdegerleritoplamı(int sayi)
{
	if (sayi == 0)
		return 0;
	else
		return (sayi % 10) + basamakdegerleritoplamı(sayi / 10);

	/*
	
	Örnek= 125 Sayısı

		5+basamakdegerleritoplamı(12)
			2+basamakdegerleritoplamı(1)
				1+basamakdegerleritoplamı(0)
	
	
	*/

}


int main()
{
	setlocale(LC_ALL, "Turkish");

	int sayi;


	printf("Lütfen bir tam sayı giriniz: ");
	scanf("%d", &sayi);


	printf("\nBasamak Değerleri Toplamı = %d\n", basamakdegerleritoplamı(sayi));

	return 0;

}

```

## C Programlama N adet Fibonacci Sayısı Yazdıran Program

```c
/*
N adet Fibonacci Sayısı Yazdıran Program
// Özyinelemeli Fonksiyon (Recursive Function)
*/


#include <stdio.h>  
#include <locale.h>  


int fibonacci(int x)
{
	if (x == 0 || x == 1)
	{
		return x;
	}
	else
		return fibonacci(x - 1) + fibonacci(x - 2);
}


int main()
{
	setlocale(LC_ALL, "Turkish");

	int sayi, i;

	printf("Kaç tane Fibonacci sayısı yazılsın?: ");
	scanf("%d", &sayi);

	for (i = 1; i <= sayi; i++)
	{
		printf("%d\n", fibonacci(i));
	}

	return 0;

}

/*


i=1 fibonacci(1)

i=2 fibonacci(1)+fibonacci(0)

i=3 fibonacci(2)+fibonacci(1)


*/

```

## C Programlama Örnek Dizideki Elemanlar Toplamı

```c
/*
Dizideki Elemanlar Toplamı


C program to find sum of array elements using recursion

// Özyinelemeli Fonksiyon (Recursive Function)
*/


#include <stdio.h>  
#include <locale.h>  
#define MAX_SIZE 100

int topla(int dizi[], int x, int y)  //topla(dizi, 0, N); x=0, y=N <<< Başlangıç
{
	if (x >= y)
		return 0;
	else
		return (dizi[x] + topla(dizi, x + 1, y));
}



int main()
{
	setlocale(LC_ALL, "Turkish");
	
	int dizi[MAX_SIZE];
	int i,N;
	int sonuc;
	
	printf("Dizinin Boyutunu Giriniz: ");
	scanf("%d", &N);


	for (i = 0; i < N; i++)
	{
		printf("%d. Elemanı Giriniz: ", i + 1);
		scanf("%d", &dizi[i]);

	}

	sonuc = topla(dizi, 0, N);

	printf("Dizideki Elemanların Toplamı: %d", sonuc);

	return 0;

}

```

## C Programlama Örnek Dizideki Elemanların Ortalaması

```c
/*
Dizideki Elemanların Ortalaması


C program that finds the average of the numbers in a given array with the recursive function

// Özyinelemeli Fonksiyon (Recursive Function)
*/


#include <stdio.h>  
#include <locale.h>  
#define MAX_SIZE 100

int topla(int dizi[], int x, int y)  //topla(dizi, 0, N); x=0, y=N <<< Başlangıç
{
	if (x >= y)
		return 0;
	else
		return (dizi[x] + topla(dizi, x + 1, y));
}



int main()
{
	setlocale(LC_ALL, "Turkish");

	int dizi[MAX_SIZE];
	int i, N;
	int sonuc;

	printf("Dizinin Boyutunu Giriniz: ");
	scanf("%d", &N);


	for (i = 0; i < N; i++)
	{
		printf("%d. Elemanı Giriniz: ", i + 1);
		scanf("%d", &dizi[i]);

	}

	sonuc = topla(dizi, 0, N);

	printf("Dizideki Elemanların Ortalaması: %d", sonuc/N);

	return 0;

}

```

## C Programlama Örnek Dizinin En Büyük Elemanını Bulma 

```c
/*
 Dizinin En Büyük Elemanını Bulma 

// Dizi ve İşlevi


C program to find maximum  elements in array using recursion

// Özyinelemeli Fonksiyon (Recursive Function)
*/


#include <stdio.h>  
#include <locale.h>  
#define MAX_SIZE 100



int enbuyuksayi(int dizi[], int ilk_elemani, int son_elemani)
{
	int max;

	if (ilk_elemani == son_elemani)
		return dizi[ilk_elemani];

	else
	{
		max = enbuyuksayi(dizi, ilk_elemani + 1, son_elemani);

		if (dizi[ilk_elemani] >= max)

			return dizi[ilk_elemani];
		else
			return max;
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

	printf("Dizinin En Büyük Elemanı = %d\n", enbuyuksayi(dizi, 0, N));


	return 0;

}
```

## C Programlama Örnek Decimal Sayıyı Binary Sayıya Çevirme

```c
/*

Decimal Sayıyı Binary Sayıya Çevirme


Verilen bir sayısının decimal’den binary’e dönüşümünü rekürsif fonksiyonla hesaplayan programı yazınız?
Write a C program for decimal to binary conversion with the recursive function?

// Özyinelemeli Fonksiyon (Recursive Function)
*/


#include <stdio.h>  
#include <locale.h>  


int binary(int sayi)
{
	if (sayi == 0)
	{
		return 0;
	}


	binary(sayi / 2);
	printf("%d", sayi % 2);


}


int main()
{
	setlocale(LC_ALL, "Turkish");

	int sayi;

	printf("Onluk Tabanında Olan Bir Sayı Giriniz: ");
	scanf("%d", &sayi);

	binary(sayi);

	return 0;

}

/*


•	Onlu (Desimal, 10 Tabanlı, Decimal) Sayı Sistemi
Günlük hayatta kullandığımız sayı sistemi 10 tabanına göredir. Yani bu sistemde 0-1-2-3-4-5-6-7-8-9 sayıları mevcuttur. Kullanılan bu sayı sistemine de Onlu Sayı Sistemi veya Desimal Sistem denilmektedir.

•	İkili (Binary, 2 Tabanlı) Sayı Sistemi
İkili sayı sisteminde sadece 1 ve 0′ lar bulunur. Bu sayı sistemi 2 tabanında olduğu için İkili Sayı Sistemi veya Binary Sistem olarak isimlendirilmektedir.


//Desimal sayı binary sayıya çevrilirken binary sayının tabanı olan 2'ye bölünür.
Kalanlar bir kenara yazılarak tersten ikilik sayı olarak yazılır.



*/




/*
Örnek 45 sayısı girildiğinde

	printf("Modu Alınacak Sayı= %d\n", sayi);

45,22,11,5,2,1 sayılarını alt alta yazıyor.


	binary(sayi / 2); Sayi==0 Olana kadar bulunan sayıları 2 ye bölmeye devam ediyor. 

	printf("%d", sayi % 2); //Bulunan sayıların ayrı ayrı modları alınıp yanyana yazılınca sonuç çıkıyor.

*/


```

## C Programlama Örnek Girilen Sayının Asal Sayı Olup Olmadığını Kontrol Etmek

```c
/*

Girilen Sayının Asal Sayı Olup Olmadığını Kontrol Etmek

// Özyinelemeli Fonksiyon (Recursive Function)
*/


#include <stdio.h>  
#include <locale.h>  


int asal(int sayi, int x)
{
	if (x == 1)
	{
		return 1;
	}
	else
	{
		if (sayi % x == 0)
		{
			return 0;
		}
		else
		{
			return asal(sayi, x - 1);
		}
	}
}


int main()
{
	setlocale(LC_ALL, "Turkish");

	int sayi;

	printf("Lütfen bir tam sayı giriniz: ");
	scanf("%d", &sayi);

	int kontrol = asal(sayi,sayi/ 2);


	if (kontrol == 1)
	{
		printf("\nASAL SAYIDIR");
		printf("\n");
	}
	else
	{
		printf("\nASAL SAYI DEĞİLDİR");
		printf("\n");
	}
	return 0;

}
```

## C Programlama Örnek Pascal Üçgeni Oluşturma

```c
/*
Pascal Üçgeni Oluşturma

// Özyinelemeli Fonksiyon (Recursive Function)

*/

#include <stdio.h>
#include <locale.h>  
#define MAX_SIZE 50

int fun(int i, int j) {

	if (i == j || j == 0)
		return 1;

	else
		return fun(i - 1, j) + fun(i - 1, j - 1);
}

int main() {

	setlocale(LC_ALL, "Turkish");

	int N, i, j, A[MAX_SIZE][MAX_SIZE];

	printf("Satır Sayısı İçin\n"
		   "Lütfen Bir Değer Giriniz: ");
	scanf("%d", &N);

	printf("\n");

	for (i = 0;i < N;i++) {

		for (j = 0;j <= i;j++) {
			A[i][j] = fun(i, j);
		}
	}

	for (i = 0;i < N;i++) {

		for (j = 0;j <= i;j++) {

			printf("%-6d", A[i][j]);

		}
		printf("\n");
	}
}
```

## C Programlama Örnek

```c
#include<stdio.h> 

void fun(int x)
{
    if (x > 0)
    {
        fun(--x);
        printf("%d\t", x);
        fun(--x);
    }
}

int main()
{
    int a = 4;
    fun(a);
    getchar();
    return 0;
}




/*

P(): Yazdır

fun(4) = fun(3) + P(3) + fun(2) <<< Buna Göre takip edilecek. 


fun(3) = fun(2) + P(2) + fun(1)
fun(2) = fun(1) + P(1) + fun(0)
fun(1) = fun(0) + P(0) + fun(-1)

Output: 0 1 2 0 3 0 1

fun(3) = 0 1 2 0
fun(2) = 0 1


*/

```

## C Programlama Örnek

```c
#include <stdio.h> 

void fun(int n)
{
	if (n > 0)
	{
		fun(n - 1);
		printf("%d ", n);
		fun(n - 1);
	}
}

int main()
{
	fun(4);
	return 0;
}

/*
P(): Yazdır

f(4) = f(3) P(4) f(3)    <<< Buna Göre takip edilecek. 

f(3) = f(2) P(3) f(2)
f(2) = f(1) P(2) f(1)
f(1) = f(0) P(1) f(0)



f(3) = 1 2 1 3 1 2 1
P(4) = 4



Output= 1 2 1 3 1 2 1 4 1 2 1 3 1 2 1

*/

```

## C Programlama Örnek

```c
#include<stdio.h> 

void fun(int x)
{
	if (x < 1)
	{
		return;
	}

	fun(x - 1);

	fun(x - 3);

	printf("%d\t", x);

}

int main()
{
	int a = 4;

	fun(a);

	getchar();
	
	return 0;
}
```

## C Programlama Örnek

```c
#include <stdio.h>
#include <locale.h> //Tüm Diller ve Karakter setleri bu kütüphane de yer alır. 


void calculate(int a) {

	printf("%3d", a);

	if (a < 9)
		calculate(a + 1);
	
	printf("%3d", a);
}


void calculate_2(int a) {

	printf("%3d", a);

	if (a > 9)
		calculate_2(a - 1);

	printf("%3d", a);
}


main()
{
	setlocale(LC_ALL, "Turkish"); //Türkçe karakter yazdırmamızı sağlayan fonksiyon

	printf("\ncalculate(1)   : ");

	calculate(1);

	printf("\n\ncalculate_2(20): ");

	calculate_2(20);
}

```

## C Programlama Örnek

```c
#include <stdio.h>
#include <locale.h> //Tüm Diller ve Karakter setleri bu kütüphane de yer alır. 


struct complex {

	int real;
	int im;

};

struct complex sum(struct complex s1, struct complex s2) {

	struct complex result;

	result.real = s1.real + s2.real;
	result.im = s1.im + s2.im;

	return result;
}


main()
{
	setlocale(LC_ALL, "Turkish"); //Türkçe karakter yazdırmamızı sağlayan fonksiyon

	struct complex a1, a2, a3;

	a1.real = 5;
	a1.im = 3;

	a2.real = 15;
	a2.im = 30;

	a3 = sum(a1, a2);

	printf("Sonuç: %d+i%d\n", a3.real, a3.im);

}

```

