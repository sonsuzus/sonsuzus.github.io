---
title:  C Programlama Örnekleri Dosya İşlemleri 09
author: sonsuz
date: 2023-08-18 00:50:15 +0300
categories: [Program,C]
tags: [c,programlama,alıştırma,algoritma,örnek,fonksiyon,data,dosya]
---

## C Program Dosya Güncelleme

```c
/* Dosya Güncelleme

Dosyada bilgileri tutulan öğrencilerden final notu 55 ile 59 arasında olan
tüm öğrencilerin notuna 5 puan ekleyerek dosyayı güncelleyen(update) program kodu

// Rastgele Erişimli Dosya

*/
#include <stdio.h>
#include <locale.h>

struct ogrenci
{
	int numara;
	char ad[20];
	float final_notu;
};


void main()
{
	setlocale(LC_ALL, "Turkish");

	struct ogrenci bilgi;

	int i = 1;

	FILE* myPtr;

	if ((myPtr = fopen("student.dat", "r+")) == NULL)
		printf("Dosya Açılamadı\n");

	/*
	r+ -> Dosya hem okuma hem de yazma için açılır.
		  Dosya yok ise açılamaz.
	*/

	else
	{
		fread(&bilgi, sizeof(struct ogrenci), 1, myPtr); //İlk Kaydı Okur

	/*fread: Dosyadan belirtilen kadar bayt okuyup hafızaya atar.

	fread(bellek, boyutu, sayısı, dosya_gosterici);

		bellek= dosyadan okutulacak yazdırılacak verinin geçici olarak
				bellekte saklanacağı alan
		boyutu= okutulacak alanı uzunluğu
		sayısı= verinin tekrarlanma sayısı
	*/
		while (!feof(myPtr)) //Dosyanın sonuna gelene kadar devam et.

	/*
	feof(Dosya İşaretçisi):  Dosyanın sonunu gösterir.
	*/
		{
			if (bilgi.final_notu >= 55 && bilgi.final_notu <= 59)
			{
				bilgi.final_notu += 5;

				fseek(myPtr, (i - 1) * sizeof(struct ogrenci), SEEK_SET);

				/* fseek: Dosyadaki konumu belirtilen işaretçinin konumunu ayarlar.

				fseek(dosya_gostericisi,offset,symbolic_constant)

					offset= dosyadaki konumu gösteren işaretçi
					symbolic_constant= dosyanın neresinden okumaya başlayacağını gösterir.

						SEEK_SET - başından başla
						SEEK_CUR - mevcut bulunan konumdan başla
						SEEK_END - dosyanın sonundan başla
				*/

				fwrite(&bilgi, sizeof(struct ogrenci), 1, myPtr);
				
				/*fwrite: bellekteki görüntüsü ile dosyaya yazar.

				fwrite(bellek, boyutu, sayısı, dosya_gosterici);

					bellek= dosyadan okutulacak yazdırılacak verinin geçici olarak
							bellekte saklanacağı alan
					boyutu= okutulacak alanı uzunluğu
					sayısı= verinin tekrarlanma sayısı
				*/

			}

			i++; //Bir sonraki kayıt için indisi artırır.

		//Sıradaki kaydı oku.
			fseek(myPtr, (i - 1) * sizeof(struct ogrenci), SEEK_SET);
			fread(&bilgi, sizeof(struct ogrenci), 1, myPtr);

		}


		printf("Hesaplar Güncellendi");


	}


	fclose(myPtr);  //Açılmış olan dosyayı kapatır.
}

```

## C Programlama Dosyadan Dosyaya Kopyalama

```c
/* Dosyadan Dosyaya Kopyalama

Sıralı erişimli "notlar.txt" isimli bir dosyada öğrenci no(int), ad ve not(float) bilgisi tutulmaktadır. 
Bu dosyada yer alan kayıtlar arasında ismi "Ahmet" olan ve notu 60 ve üzerinde olan öğrencileri 
"basari.dat" isimli rastgele erişimli bir dosyaya yazarak aktaran kod

// Sıralı Erişimli Dosya -> Rastgele Erişimli Dosya


*/


#include <stdio.h>
#include <string.h>
#include <locale.h>


struct ogrenci
{
	int no;
	char ad[20];
	float not;
};


int main(void)
{
	setlocale(LC_ALL, "Turkish");

	FILE* ptr1, * ptr2;

	struct ogrenci kayit;

	ptr1 = fopen("notlar.txt", "r");
	ptr2 = fopen("basari.dat", "w");

	if (ptr1 != NULL && ptr2 != NULL)
	{
		fscanf(ptr1, "%d %s %f", &kayit.no, kayit.ad, &kayit.not);
	
	/* fscanf: Dosyadan okuma yapan bir işlevdir.
	fscanf(dosya_gostericisi, "%d %s %f", &myInt, myString, &myFloat)
	
	*/
		
		while (!feof(ptr1)) //Dosyanın sonuna gelene kadar devam et.

	/*
	feof(Dosya İşaretçisi):  Dosyanın sonunu gösterir.
	*/
		{
			if (strcmp(kayit.ad, "Ahmet") == 0 && kayit.no >= 60)
				fwrite(&kayit, sizeof(struct ogrenci), 1, ptr2);
			fscanf(ptr1, "%d %s %f", &kayit.no, kayit.ad, &kayit.not);
		}

		fclose(ptr1);
		fclose(ptr2);
		//fclose: Açılmış olan bir dosyayı kapatır.
	}

}

/*

strcmp= birinci yazı ile ikinci yazı birbirine eşit ise 0 değeridir.

*/

```

## C Programlama Bilgiyi Ekrana Basma

```c
/* Bilgiyi Ekrana Basma

Dosyada bilgileri tutulan öğrencilerden en yüksek ikinci final notuna
sahip öğrencinin numara,ad ve notunu bilgilerini ekranan basan kod

//  Rastgele Erişimli Dosya


*/


#include <stdio.h>
#include <locale.h>


struct ogrenci
{
	int numara;
	char ad[40];
	float not;
};


void ikinciMax(FILE*okuPtr)
{

	struct ogrenci bilgi, max1, max2;

	fread(&bilgi, sizeof(struct ogrenci), 1, okuPtr); //İlk Kaydı okur.

/* fread: Dosyadan belirtilen kadar bayt okuyup hafızaya atar.
	fread(bellek, boyutu, sayısı, dosya_gosterici);

		bellek= dosyadan okutulacak yazdırılacak verinin geçici olarak
				bellekte saklanacağı alan
		boyutu= okutulacak alanı uzunluğu
		sayısı= verinin tekrarlanma sayısı
*/

	max1 = bilgi;
	max2 = bilgi;

	while (!feof(okuPtr)) //Dosyanın sonuna gelene kadar devam et.

/*
	feof(Dosya İşaretçisi):  Dosyanın sonunu gösterir.
*/
	{
		if (bilgi.not> max1.not)
		{
			max2 = max1;
			max1 = bilgi;
		}

		else if (bilgi.not> max2.not)
			max2 = bilgi;

		fread(&bilgi, sizeof(struct ogrenci), 1, okuPtr);

	}

	printf("İkinci En Büyük Final Notu Olan Öğrenci\n");
	printf("%d\t%s\t%2.f\n", max2.numara, max2.ad, max2.not);


}


int main(void)
{
	setlocale(LC_ALL, "Turkish");

	FILE* myPtr;

	if ((myPtr = fopen("student.dat", "r")) == NULL)
		printf("Dosya Açılamadı\n");

	else
		ikinciMax(myPtr);
}

```

## C Programlama Bilgiyi Ekrana Basma (2)

```c
/* Bilgiyi Ekrana Basma (2)

Dosyada bilgileri tutulan öğrencilerden en düşük ikinci final notuna
sahip öğrencinin numara,ad ve notunu bilgilerini ekranan basan kod

//  Rastgele Erişimli Dosya


*/


#include <stdio.h>
#include <locale.h>


struct ogrenci
{
	int numara;
	char ad[40];
	float not;
};


void ikinciMin(FILE*okuPtr)
{

	struct ogrenci bilgi, min1, min2;

	fread(&bilgi, sizeof(struct ogrenci), 1, okuPtr); //İlk Kaydı okur.

/* fread: Dosyadan belirtilen kadar bayt okuyup hafızaya atar.
	fread(bellek, boyutu, sayısı, dosya_gosterici);

		bellek= dosyadan okutulacak yazdırılacak verinin geçici olarak
				bellekte saklanacağı alan
		boyutu= okutulacak alanı uzunluğu
		sayısı= verinin tekrarlanma sayısı
*/

	min1 = bilgi;
	min2 = bilgi;

	while (!feof(okuPtr)) //Dosyanın sonuna gelene kadar devam et.

/*
	feof(Dosya İşaretçisi):  Dosyanın sonunu gösterir.
*/
	{
		if (bilgi.not<min1.not)
		{
			min2 = min1;
			min1 = bilgi;
		}

		else if (bilgi.not < min2.not)
			min2 = bilgi;

		fread(&bilgi, sizeof(struct ogrenci), 1, okuPtr);

	}

	printf("İkinci En Düşük Final Notu Olan Öğrenci\n");
	printf("%d\t%s\t%2.f\n", min2.numara, min2.ad, min2.not);


}


int main(void)
{
	setlocale(LC_ALL, "Turkish");

	FILE* myPtr;

	if ((myPtr = fopen("student.dat", "r")) == NULL)
		printf("Dosya Açılamadı\n");

	else
		ikinciMin(myPtr);
}

```

## C Programlama Yer Değiştirme

```c
/* Yer Değiştirme */

#include <stdio.h>
#include <locale.h>
#define MAX_SIZE 25

struct student {
	int  schoolnumber;
	char name[MAX_SIZE];
	char surname[MAX_SIZE];

};

void display(FILE*);

int main()
{
	setlocale(LC_ALL, "Turkish");

	struct student school;

	int  i;
	int  students;

	printf("Öğrenci Sayısını Giriniz: ");
	scanf("%d", &students);

	printf("\n");

	FILE* fptr;


	if ((fptr = fopen("student.txt", "w")) == NULL)
		printf("Dosya Açılamadı\n");

	else
	{
		rewind(fptr);

		//fprintf(fptr, "%-28s%-30s%10s\n", "Öğrencinin Okul Numarası", "Öğrencinin Soyadı", "Öğrencinin Adı");


		for (i = 0; i < students; ++i)
		{
			printf("%d. Öğrenci\n", i + 1);

			printf("Öğrencinin Okul Numarası:");
			scanf("%d", &school.schoolnumber);

			printf("Öğrencinin Adı:");
			scanf("%s", &school.name);

			printf("Öğrencinin Soyadı:");
			scanf("%s", &school.surname);


			printf("\n");


			fprintf(fptr, "%-10d%-16s%-16s\n", school.schoolnumber, school.name, school.surname);
		}

		fclose(fptr);
	}


	printf("\nÖğrenci Bilgileri Dosyaya Yazıldı\n");

	display(fptr);

	printf("\nYer Değiştirme Yapıldı\n");

	fclose(fptr);
}


void display(FILE* fptr)
{
	struct student tmp1 = {0,"",""};
	struct student tmp2 = {0,"",""};

	if ((fptr = fopen("student.txt", "r+")) == NULL)
		printf("Dosya Açılamadı\n");

	else
	{

		fseek(fptr, (0) * sizeof(struct student), SEEK_SET);


		fread(&tmp1, sizeof(struct student), 1, fptr);


		fseek(fptr, (2) * sizeof(struct student), SEEK_SET);


		fread(&tmp2, sizeof(struct student), 1, fptr);



		fseek(fptr, (0) * sizeof(struct student), SEEK_SET);


		fwrite(&tmp2, sizeof(struct student), 1, fptr);


		fseek(fptr, (2) * sizeof(struct student), SEEK_SET);


		fwrite(&tmp1, sizeof(struct student), 1, fptr);

	}
}

```

## C Programlama Dosya Örnek Uygulama

```c
/* Dosya Örnek Uygulama

 Öğrencilere ait numara, isim, vize ve final notunun tutulduğu “notlar.txt” isimli dosya üzerinde işlemler yapabileceğiniz bir C programı yazınız. Buna göre programın menüsü şu şekilde olacaktır:,
 1- Dosya oluştur / veri gir
 2- Dosyadan oku / listele
 3- Geçme notu 60 üstü olanları listele
 4- Dosyada geçme notu 60 ve üstü olanları “gecenler.txt”, düşük olanları ise “kalanlar.txt”  dosyasına yazdır.
 5- Dosya boyutunu ekrana yazdır.
Not: Her bir menü seçeneği bir fonksiyon ile yapılıcaktır.

*/

#include <stdio.h>
#include <locale.h>


struct ogrenci {
	int okul_no;
	char isim[40];
	int vize_notu;
	int final_notu;


};

void dosyaOlustur()
{
	struct ogrenci okul;

	int i;
	int ogrenci_sayisi;

	printf("Öğrenci Sayısını Giriniz: ");
	scanf("%d", &ogrenci_sayisi);

	printf("\n");

	FILE* fptr;

	if ((fptr = fopen("notlar.txt", "w")) == NULL)
		printf("Dosya Açılamadı\n");

	else
	{
		for (i = 0; i < ogrenci_sayisi; ++i)
		{
			printf("%d. Öğrenci\n", i + 1);

			printf("Öğrencinin Okul Numarası:");
			scanf("%d", &okul.okul_no);

			printf("Öğrencinin Adı:");
			scanf("%s", okul.isim);

			printf("Öğrencinin Vize Notu:");
			scanf("%d", &okul.vize_notu);

			printf("Öğrencinin Final Notu:");
			scanf("%d", &okul.final_notu);

			printf("\n");

			fprintf(fptr, "%d\t%s\t%d\t%d\n", okul.okul_no, okul.isim, okul.vize_notu, okul.final_notu);

		}

		fclose(fptr);
	}


	printf("\nÖğrenci Notları Dosyaya Yazıldı\n");

}

void dosyaOku()
{
	struct ogrenci okul;

	FILE* fptr;


	if ((fptr = fopen("notlar.txt", "r")) == NULL)
		printf("Dosya Açılamadı\n");

	else
	{
		fscanf(fptr, "%d%s%d%d", &okul.okul_no, okul.isim, &okul.vize_notu, &okul.final_notu);


		while (!feof(fptr))
		{

			printf("%d\t%s\t%d\t%d\n", okul.okul_no, okul.isim, okul.vize_notu, okul.final_notu);

			fscanf(fptr, "%d%s%d%d", &okul.okul_no, okul.isim, &okul.vize_notu, &okul.final_notu);
		}


	}

	fclose(fptr);
}

void listele()
{
	struct ogrenci okul;

	FILE* fptr;

	int gecme_notu;



	if ((fptr = fopen("notlar.txt", "r")) == NULL)
		printf("Dosya Açılamadı\n");

	else
	{
		fscanf(fptr, "%d%s%d%d", &okul.okul_no, okul.isim, &okul.vize_notu, &okul.final_notu);

		gecme_notu = (okul.vize_notu * 0.4) + (okul.final_notu * 0.6);

		while (!feof(fptr))
		{

			if (gecme_notu >= 60)
			{
				printf("%d\t%s\t%d\t%d\n", okul.okul_no, okul.isim, okul.vize_notu, okul.final_notu);
			}

			fscanf(fptr, "%d%s%d%d", &okul.okul_no, okul.isim, &okul.vize_notu, &okul.final_notu);

			gecme_notu = (okul.vize_notu * 0.4) + (okul.final_notu * 0.6);

		}

	}



	fclose(fptr);
}

void dosyaKopyalama()
{
	struct ogrenci okul;

	FILE* fptr = fopen("notlar.txt", "r");
	FILE* kalan = fopen("kalanlar.txt", "w");
	FILE* gecen = fopen("gecenler.txt", "w");

	int gecme_notu;


	if (fptr == NULL)
		printf("Dosya Açılamadı\n");

	else
	{
		fscanf(fptr, "%d%s%d%d", &okul.okul_no, okul.isim, &okul.vize_notu, &okul.final_notu);

		gecme_notu = (okul.vize_notu * 0.4) + (okul.final_notu * 0.6);

		while (!feof(fptr))
		{
			if (gecme_notu >= 60)
			{
				fprintf(gecen, "%d\t%s\t%d\t%d\n", okul.okul_no, okul.isim, okul.vize_notu, okul.final_notu);
			}

			else
			{
				fprintf(kalan, "%d\t%s\t%d\t%d\n", okul.okul_no, okul.isim, okul.vize_notu, okul.final_notu);
			}

			fscanf(fptr, "%d%s%d%d", &okul.okul_no, okul.isim, &okul.vize_notu, &okul.final_notu);
			gecme_notu = (okul.vize_notu * 0.4) + (okul.final_notu * 0.6);
		}

	}

	printf("\nGeçenler ve Kalanlar İçin Ayrı Dosyalar Oluşturuldu.\n");


	fclose(kalan);
	fclose(gecen);
	fclose(fptr);
}

void dosyaBoyutu()
{
	int i = 0;
	char k;

	FILE* fptr = fopen("notlar.txt", "r");

	if (fptr == NULL)
		printf("Dosya Açılamadı\n");

	else
	{

		k = fgetc(fptr);

		while (!feof(fptr))
		{
			i++;
			k = fgetc(fptr);
		}


	}

	printf("Dosyanın Boyutu: %d Byte\n", i);
	fclose(fptr);
}



int main()
{
	setlocale(LC_ALL, "Turkish");

	int sec = 6;

	while (sec != 7)
	{
		printf("\n1 - Dosya Oluştur\n"
			"2 - Dosyayı Oku\n"
			"3 - Dersi Geçen Öğrencilerin Listesi\n"
			"4 - Geçenler Ayrı Dosyaya Kalanları Ayrı Dosyaya Yazdır\n"
			"5 - Dosya Boyutunu Ekrana Yazdır\n"
			"6 - Çıkış\n");

		printf("Seçiminizi Yapınız:");
		scanf("%d", &sec);

		printf("\n");

		if (sec == 1) dosyaOlustur();
		else if (sec == 2) dosyaOku();
		else if (sec == 3) listele();
		else if (sec == 4) dosyaKopyalama();
		else if (sec == 5) dosyaBoyutu();
		else if (sec == 6) exit(0);
	}
}

```
