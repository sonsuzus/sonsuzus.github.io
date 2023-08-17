---
title:  C Programlama Örnekleri Veri Yapıları 08
author: sonsuz
date: 2023-08-18 00:45:15 +0300
categories: [Program,C]
tags: [c,programlama,alıştırma,algoritma,örnek,fonksiyon,data]
---

## C Program Tek Bağlı Liste (Singly Linked List) Uygulaması

```c
/* Tek Bağlı Liste (Singly Linked List) Uygulaması */


#include <stdio.h>
#include <locale.h> //Tüm Diller ve Karakter setleri bu kütüphane de yer alır. 



struct database {
	int number;
	struct database* next;
};

typedef struct database node;

node* head, * tmp;


/*-------------------------   1  -------------------------*/

void createList() //Liste Oluşturma Fonksiyonu
{
	int n, i;

	printf("Veri Sayısını Giriniz: ");
	scanf("%d", &n);

	for (i = 0; i < n; i++)
	{

		if (i == 0) {
			head = (node*)malloc(sizeof(node));
			tmp = head;
		}

		else {
			tmp->next = (node*)malloc(sizeof(node));
			tmp = tmp->next;
		}

		printf("%d. Veriyi Giriniz: ", i + 1);
		scanf("%d", &tmp->number);
	}

	tmp->next = NULL;

	printf("\n #Listeniz Oluşturuldu. Görmek İçin Ekrana Yazdırın\n");
}

/*-------------------------   2  -------------------------*/

void printList() //Listeyi Ekranda Gösteren Fonksiyon
{
	node* p;

	p = head;

	int i = 0;

	if (p == NULL) {

		printf("\n #Listede Bir Veri Yok\n");
		return;
	}

	printf("\n#Oluşturduğunuz Liste; \n");

	while (p != NULL)
	{
		printf("%d. Sayı: %d\n", i + 1, p->number);
		p = p->next;
		i++;
	}
	printf("\n");
}

/*-------------------------   3  -------------------------*/

void deleteNode() //Listede Silmek İstediğiniz Veriyi Silen Fonksiyon
{
	node* p, * q;

	int sayi;

	printf("Silmek İstediğiniz Veri(Sayıyı) Giriniz: ");
	scanf("%d", &sayi);

	p = head;
	q = head;


	if (p->number == sayi)
	{
		head = p->next;

		free(p);

		printf("\n #Veri Başarıyla Silindi\n"
			"\n  (Listenin İlk Düğümü Silindi)\n");
	}

	else
	{
		while (p->next != NULL && p->number != sayi)
		{
			q = p;
			p = p->next;
		}

		if (p->number == sayi)
		{
			q->next = p->next;
			free(p);
			printf("\n #Veri Başarıyla Silindi\n");
		}

		else if (p->next == NULL)
		{
			printf("\n #Silinecek Bir Veri Bulunamadı\n");
		}
	}

}

/*-------------------------   4  -------------------------*/

void addNode() //Listeye İstediğiniz Veriden önce Düğüm Ekleme
{
	node* p, * q;

	int sayi;

	tmp = (node*)malloc(sizeof(node));

	printf("Eklenecek Veriyi(Sayıyı) Giriniz: ");
	scanf("%d", &tmp->number);

	printf("Hangi Sayıdan Önce Ekrana Yazılsın? =  ");
	scanf("%d", &sayi);

	p = head;
	q = head;

	if (p->number == sayi)
	{
		tmp->next = p;
		head = tmp;
		printf("\n #Veri Listenin Başına Eklendi. Görmek İçin Ekrana Yazdırın\n");
	}
	else
	{
		while (p->next != NULL && p->number != sayi)
		{
			q = p;
			p = p->next;
		}

		if (p->number == sayi)
		{
			q->next = tmp;
			tmp->next = p;
			printf("\n #Veri Belirtilen Konuma Eklendi. Görmek İçin Ekrana Yazdırın\n");
		}

		else if (p->next == NULL)
		{
			p->next = tmp;
			tmp->next = NULL;
			printf("\n #Veri Listenin Sonuna Eklendi. Görmek İçin Ekrana Yazdırın\n");
		}
	}
}

/*-------------------------   5  -------------------------*/


void addNodeFirst() //Listenin Başına Düğüm Ekleme
{
	node* p;

	tmp = (node*)malloc(sizeof(node));

	printf("Eklenecek Veriyi(Sayıyı) Giriniz: ");
	scanf("%d", &tmp->number);

	p = head;

	tmp->next = p;
	head = tmp;

	printf("\n #Veri Listenin Başına Eklendi. Görmek İçin Ekrana Yazdırın\n");
}


/*-------------------------   6  -------------------------*/


void addNodeLast() //Listenin Sonuna Düğüm Ekleme
{
	node* p, * q;

	tmp = (node*)malloc(sizeof(node));

	printf("Eklenecek Veriyi(Sayıyı) Giriniz: ");
	scanf("%d", &tmp->number);

	p = head;

	while (p->next != NULL)
	{
		q = p;
		p = p->next;
	}

	p->next = tmp;
	tmp->next = NULL;

	printf("\n #Veri Listenin Sonuna Eklendi. Görmek İçin Ekrana Yazdırın\n");
}


/*-------------------------   7  -------------------------*/

void cnt() //Listedeki Eleman Sayısını Ekrana Yazdırma
{
	node* p;
	int sayac = 0;

	p = head;

	while (p != NULL)
	{
		sayac++;
		p = p->next;
	}

	printf("\n #Eleman Sayısı: %d\n", sayac);
}



/*-------------------------   8  -------------------------*/

void sondakiDugumuBasaAlma() {

	node* p, * q;

	p = head;
	q = NULL;

	while (p != NULL && p->next != NULL)
	{
		q = p;
		p = p->next;
	}

	q->next = NULL;
	p->next = head;
	head = p;

	printf("\n #Sondaki Düğüm Başa Alındı. Görmek İçin Ekrana Yazdırın\n");
}

/*-------------------------   9  -------------------------*/

void listeyiSil()
{
	node* p;

	if (head == NULL) {
		printf("\n #Listede Sayı Yok\n");
		return;
	}

	while (head != NULL) {
		p = head;
		head = head->next;
		free(p);
	}
	printf("\n #Liste Yok Edildi\n");
}


/*-------------------------  10  -------------------------*/


void yer_degistirme() // İstediğiniz İki Verinin Yerini Değiştirme
{
	node* prev1, * prev2, * node1, * node2, * temp;

	prev1 = NULL;
	prev2 = NULL;
	temp = NULL;
	node1 = head;
	node2 = head;

	int n1, n2;

	printf("Yer Değiştirmek İstediğiniz İki Tane Sayının Değerlerini Giriniz: \n");
	scanf("%d %d", &n1, &n2);


	// Listenin Boş Olup Olmadığını Kontrol Etme
	if (head == NULL) {
		return;
	}

	// Sayılar eşitse yer değişmeyecek  
	if (n1 == n2)
		return;

	//Arama Yapma (dugum1 için)
	while (node1 != NULL && node1->number != n1) {
		prev1 = node1;
		node1 = node1->next;
	}

	//Arama Yapma (dugum2 için)
	while (node2 != NULL && node2->number != n2) {
		prev2 = node2;
		node2 = node2->next;
	}

	if (node1 != NULL && node2 != NULL) {


		if (prev1 != NULL)
			prev1->next = node2;
		else
			head = node2;

		if (prev2 != NULL)
			prev2->next = node1;
		else
			head = node1;

		temp = node1->next;
		node1->next = node2->next;
		node2->next = temp;
	}
	else {
		printf("#Yer Değiştirme Yapılamıyor.\n");
	}
}


/*-------------------------  11  -------------------------*/

void en_buyuk_sayi()
{
	node* p;

	p = head;

	int enBuyuk = p->number;

	while (p != NULL)
	{
		if (p->number >= enBuyuk)
		{
			enBuyuk = p->number;
		}
		p = p->next;
	}

	printf("\nEn Büyük Sayı= %d\n", enBuyuk);
}

/*-------------------------  12  -------------------------*/

void en_kucuk_sayi()
{
	node* p;

	p = head;

	int enKucuk = p->number;

	while (p != NULL)
	{
		if (p->number <= enKucuk)
		{
			enKucuk = p->number;
		}
		p = p->next;
	}

	printf("\nEn Küçük Sayı= %d\n", enKucuk);
}


/*-------------------------  13  -------------------------*/

void ortalama()
{
	node* p;

	p = head;

	int ortalama, toplam = 0, i = 0;

	if (p == NULL)
	{
		printf("\nListede Sayı Yok\n");
	}

	else
	{
		while (p != NULL)
		{
			toplam += p->number;
			p = p->next;
			i++;
		}

		ortalama = toplam / i;

		printf("\nListenin Ortalaması= %d\n", ortalama);
	}
}

/*-------------------------  14  -------------------------*/

void reverselist()
{
	node* prevNode, * curNode;

	if (head != NULL)
	{
		prevNode = head;
		curNode = head->next;
		head = head->next; //curNode ve head aynı yerde oldu.

		prevNode->next = NULL; //ilk düğümü diğerlerinden ayırıyor. 

		while (head != NULL)
		{
			head = head->next;
			curNode->next = prevNode;

			prevNode = curNode;
			curNode = head;
		}

		head = prevNode;
	}

	printf("\n #Liste Ters Çevirildi. Görmek İçin Ekrana Yazdırın\n");


	/* Kaynak: https://codeforwin.org/2015/09/c-program-to-reverse-singly-linked-list.html */
}

/*-------------------------  15  -------------------------*/

void en_kucugu_cift_dugumlerden_cikar()
{
	node* p;

	p = head;

	int enKucuk = p->number;

	while (p != NULL)
	{
		if (p->number <= enKucuk)
		{
			enKucuk = p->number;
		}
		p = p->next;
	}

	p = head;

	while (p != NULL)
	{
		if ((p->number) % 2 == 0)
		{
			p->number -= enKucuk;
		}
		p = p->next;
	}

	printf("\nEn Küçük Sayı Tüm Çift Sayılardan Çıkarıldı. Görmek İçin Ekrana Yazdırın\n");


}

/*-------------------------  16  -------------------------*/

void en_buyugu_cift_dugumlerden_cikar()
{
	node* p;

	p = head;

	int enBuyuk = p->number;

	while (p != NULL)
	{
		if (p->number >= enBuyuk)
		{
			enBuyuk = p->number;
		}
		p = p->next;
	}

	p = head;

	while (p != NULL)
	{
		if ((p->number) % 2 == 0)
		{
			p->number -= enBuyuk;
		}
		p = p->next;
	}

	printf("\nEn Büyük Sayı Tüm Çift Sayılardan Çıkarıldı. Görmek İçin Ekrana Yazdırın\n");


}

/*-------------------------  17  -------------------------*/

void delete_same_node() //Aynı sayıları siliyor.
{
	node* p, * q, * r;

	p = head;

	while (p != NULL && p->next != NULL)
	{
		q = p;

		while (q->next != NULL)
		{
			if (p->number == q->next->number)
			{
				r = q->next;
				q->next = q->next->next;
				free(r);
			}

			else
				q = q->next;
		}
		p = p->next;
	}

	printf("\nGörmek İçin Ekrana Yazdırın\n");
}

/*-------------------------  18 -------------------------*/

void list_bilgi() {

	int i = 1;

	while (head != NULL) {

		printf("%d. Düğümün Adresi= %p \n", i, head);
		printf("%d. Düğümün Verisi= %d \n", i, head->number);
		printf("%d. Düğümün Bağlı Olduğu Dğümün Adresi= %p \n\n", i, head->next);
		head = head->next;
		i++;
	}

}



/*-------------------------  101 -------------------------*/


void question_01() {

	node* yenidugum;

	head = (node*)malloc(sizeof(node));

	if (head == NULL)
	{
		printf("YETERLİ HAFIZA YOK");
		exit(0);
	}

	head->next = NULL;
	tmp = head;


	int number;

	printf("Sayı Giriniz: ");
	scanf("%d", &number);


	if (number == -1)
	{
		printf("\nProgram Sonlandırıldı\n");
		exit(0);
	}

	else

		head->number = number;


	while (1)
	{
		printf("Sayı Giriniz: ");
		scanf("%d", &number);

		if (number == -1)
			break;


		if (number % 2 == 0)
		{

			yenidugum = (node*)malloc(sizeof(node));

			if (yenidugum == NULL)
			{
				printf("YETERLI HAFIZA YOK");
				exit(0);
			}

			yenidugum->number = number;
			yenidugum->next = NULL;

			head->next = yenidugum;
			head = yenidugum;
		}

		else
		{
			yenidugum = (node*)malloc(sizeof(node));

			if (yenidugum == NULL)
			{
				printf("YETERLI HAFIZA YOK");
				exit(0);
			}

			yenidugum->number = number;
			yenidugum->next = tmp;

			tmp = yenidugum;
		}

	}


	while (tmp != NULL)
	{
		printf("%d\n", tmp->number);

		tmp = tmp->next;

	}

}


/*-------------------------  MAIN  -------------------------*/

int main()
{
	setlocale(LC_ALL, "Turkish"); //Türkçe karakter yazdırmamızı sağlayan fonksiyon

	int sec = 0;

	while (sec != 100)
	{

		printf("*************************\n"
			"  0 - Programdan Çıkış Yap\n"
			"  1 - Listenizi Oluşturun\n"
			"  2 - Listeyi Ekrana Yazdırın\n"
			"  3 - Listede İstediğiniz Herhangi Bir Veriyi Silin\n"
			"  4 - Listeye Veri Ekleme (Seçilen Verinin Öncesine Ekler)\n"
			"  5 - Listenin Başına Veri Ekleme\n"
			"  6 - Listenin Sonuna Veri Ekleme\n"
			"  7 - Listedeki Verilerin Sayısı\n"
			"  8 - Listenin Sondaki Düğümü Başa Alma\n"
			"  9 - Listeyi Sil(Yok et)\n"
			" 10 - Listedeki Değerlerin Yerlerini Değiştirme\n"
			" 11 - Listedeki En Büyük Sayıyı Bulma\n"
			" 12 - Listedeki En Küçük Sayıyı Bulma\n"
			" 13 - Listedeki Değerlerin Ortalamasını Bulma\n"
			" 14 - Listedeki Değerleri Ters Çevirme\n"
			" 15 - Listedeki En Küçük Sayıyı Tüm Çift Sayılardan Çıkarma\n"
			" 16 - Listedeki En Büyük Sayıyı Tüm Çift Sayılardan Çıkarma\n"
			" 17 - Listede Aynı Değere Sahip Olan Düğümleri Silme\n"
			" 18 - Liste Elemanlarının Tüm Bilgileri\n"

			" \n*** EKSTRA***\n"
			" 101 - Klavyeden -1 girilene kadar verilen tek sayıları tek bağlı doğrusal bir listenin başına, verilen çift sayıları ise listenin sonuna ekle\n"
		

		);

		printf("\n Seçiminizi Yapınız:");
		scanf("%d", &sec);

		printf("\n");

		if (sec == 0) exit(0);
		else if (sec == 1) createList();
		else if (sec == 2) printList();
		else if (sec == 3) deleteNode();
		else if (sec == 4) addNode();
		else if (sec == 5) addNodeFirst();
		else if (sec == 6) addNodeLast();
		else if (sec == 7) cnt();
		else if (sec == 8) sondakiDugumuBasaAlma();
		else if (sec == 9) listeyiSil();
		else if (sec == 10) yer_degistirme();
		else if (sec == 11) en_buyuk_sayi();
		else if (sec == 12) en_kucuk_sayi();
		else if (sec == 13) ortalama();
		else if (sec == 14) reverselist();
		else if (sec == 15) en_kucugu_cift_dugumlerden_cikar();
		else if (sec == 16) en_buyugu_cift_dugumlerden_cikar();
		else if (sec == 17) delete_same_node();
		else if (sec == 18) list_bilgi();
		else if (sec == 101) question_01();



	}
}

```

## C Programlama Çift Bağlı Liste (Double Linked List) Uygulaması

```c
/* Çift Bağlı Liste (Double Linked List) Uygulaması */

#include <stdio.h>
#include <locale.h> //Tüm Diller ve Karakter setleri bu kütüphane de yer alır. 

struct database {
	int number;
	struct database* next;
	struct database* prev;
};

typedef struct database node;

node* head, * end, * tmp;


/*-------------------------   1  -------------------------*/

void createList() //Liste Oluşturma Fonksiyonu
{
	int n, i;

	printf("Veri Sayısını Giriniz: ");
	scanf("%d", &n);

	for (i = 0; i < n; i++)
	{
		if (i == 0) {
			head = (node*)malloc(sizeof(node));
			tmp = head;
			end = head;
		}
		else {
			tmp->next = (node*)malloc(sizeof(node));
			tmp = tmp->next;
		}
		printf("%d. Sayıyı Giriniz: ", i + 1);
		scanf("%d", &tmp->number);
		tmp->prev = end;
		tmp->next = NULL;
		end->next = tmp;
		end = tmp;

	}

	printf("\n #Listeniz Oluşturuldu. Görmek İçin Ekrana Yazdırın\n");


	/*
	Oluşturulan listede;
	head = ilk düğüm
	end  = son düğüm
	tmp  = boş düğüm
						oldu.

	*/
}

/*-------------------------   2  -------------------------*/

void printList() //Listeyi Ekranda Gösteren Fonksiyon
{
	node* p;

	p = head;

	int i = 0;

	if (p == NULL) {

		printf("\n #Listede Bir Veri Yok\n");
		return;
	}

	printf("\n#Oluşturduğunuz Liste; \n");

	while (p != NULL)
	{
		printf("%d. Sayı: %d\n", i + 1, p->number);
		p = p->next;
		i++;
	}

	printf("\n");
}

/*-------------------------   3  -------------------------*/

void deleteNode() //Listede Silmek İstediğiniz Veriyi Silen Fonksiyon
{
	node* p, * q;

	int sayi;

	printf("Silmek İstediğiniz Veri(Sayıyı) Giriniz: ");
	scanf("%d", &sayi);

	p = head;
	q = NULL;

	if (head->number == sayi)
	{

		if (head == NULL)
		{
			printf(" #Silme İşlemi Yapılamıyor.\n");
		}
		else
		{
			head = head->next;
			head->prev = NULL;

			free(p);

			printf("\n #Veri Başarıyla Silindi\n"
				"\n     (Listenin Baştaki (İlk Düğümü) Silindi)\n");
		}
	}
	else
	{
		while (p->next != NULL && p->number != sayi)
		{
			q = p;
			p = p->next;
		}

		if (p == end)
		{
			if (end == NULL)
			{
				printf(" #Silme İşlemi Yapılamıyor.\n");
			}
			else
			{
				end = end->prev;
				end->next = NULL;

				free(p);

				printf("\n #Veri Başarıyla Silindi\n"
					"\n     (Listenin Sonundaki (Son Düğümü) Silindi)\n");
			}
		}

		else if (p != end)
		{
			p->prev->next = p->next;
			p->next->prev = p->prev;

			free(p);

			printf("\n #Veri Başarıyla Silindi\n");
		}
	}
}

/*-------------------------   4  -------------------------*/

void addNode() //Listeye İstediğiniz Veriden önce Düğüm Ekleme
{
	node* p, * q;

	int sayi;

	tmp = (node*)malloc(sizeof(node));

	printf("Eklenecek Veriyi(Sayıyı) Giriniz: ");
	scanf("%d", &tmp->number);

	printf("Hangi Sayıdan Önce Ekrana Yazılsın? =  ");
	scanf("%d", &sayi);

	p = head;
	q = head;

	if (p->number == sayi)
	{
		tmp->next = p;
		head = tmp;
		printf("\n #Veri Listenin Başına Eklendi. Görmek İçin Ekrana Yazdırın\n");
	}
	else
	{
		while (p->next != NULL && p->number != sayi)
		{
			q = p;
			p = p->next;
		}

		if (p->number == sayi)
		{
			q->next = tmp;
			tmp->next = p;
			printf("\n #Veri Belirtilen Konuma Eklendi. Görmek İçin Ekrana Yazdırın\n");
		}

		else if (p->next == NULL)
		{
			p->next = tmp;
			tmp->next = NULL;
			printf("\n #Veri Listenin Sonuna Eklendi. Görmek İçin Ekrana Yazdırın\n");
		}
	}
}

/*-------------------------   5  -------------------------*/


void addNodeFirst() //Listenin Başına Düğüm Ekleme
{
	node* p;

	tmp = (node*)malloc(sizeof(node));

	printf("Eklenecek Veriyi(Sayıyı) Giriniz: ");
	scanf("%d", &tmp->number);

	p = head;

	tmp->next = p;
	tmp->prev = NULL;
	p->prev = tmp;
	head = tmp;

	printf("\n #Veri Listenin Başına Eklendi. Görmek İçin Ekrana Yazdırın\n");

}

/*-------------------------   6  -------------------------*/

void addNodeLast() //Listenin Sonuna Düğüm Ekleme
{
	node* p, * q;

	tmp = (node*)malloc(sizeof(node));

	printf("Eklenecek Veriyi(Sayıyı) Giriniz: ");
	scanf("%d", &tmp->number);

	p = head;

	while (p->next != NULL)
	{
		q = p;
		p = p->next;
	}

	p->next = tmp;
	tmp->next = NULL;
	tmp->prev = p;
	p->next = tmp;

	printf("\n #Veri Listenin Sonuna Eklendi. Görmek İçin Ekrana Yazdırın\n");
}

/*-------------------------   7  -------------------------*/

void cnt() //Listedeki Eleman Sayısını Ekrana Yazdırma
{
	node* p;
	int sayac = 0;

	p = head;

	while (p != NULL)
	{
		sayac++;
		p = p->next;
	}

	printf("\n #Eleman Sayısı: %d\n", sayac);
}

/*-------------------------   8  -------------------------*/

void listeyiSil()
{
	node* p;

	if (head == NULL) {
		printf("\n #Listede Sayı Yok\n");
		return;
	}

	while (head != NULL) {
		p = head;
		head = head->next;
		free(p);
	}
	printf("\n #Liste Yok Edildi\n");
}


/*-------------------------   9  -------------------------*/

void addthen() //head listesinin n. düğümün hemen ardından tmp düğümü ekleme
{
	node* p;

	tmp = (node*)malloc(sizeof(node));

	printf("Eklenecek Sayıyı Giriniz: ");
	scanf("%d", &tmp->number);

	int n;

	printf("Hangi Düğümden Sonra Eklensin: ");
	scanf("%d", &n);

	p = head;

	int i = 1;

	while (i < n) {
		head = head->next;
		i++;
	}

	tmp->prev = head;
	tmp->next = head->next;
	head->next = tmp;
	head = p;

}



/*-------------------------   10  -------------------------*/

void palindrom()
{
	/*(Palindrom, tersten okunuşu da aynı olan cümle, sözcük ve sayılara denilmektedir.)*/

	node* p, * q;


	if (head == NULL)
		return 1;

	p = head;
	q = NULL;

	while (p->next != NULL)
	{
		q = p;
		p = p->next;
	}

	while (head != p)
	{
		if (head->number != p->number)
		{
			printf(" Palindrom değildir\n");
			return 0;
		}

		head = head->next;
		p = q; //p=p->prev;
	}

	printf(" Palindromdur\n");
	return 1;
}

/*-------------------------  MAIN  -------------------------*/

int main()
{
	setlocale(LC_ALL, "Turkish"); //Türkçe karakter yazdırmamızı sağlayan fonksiyon

	int sec = 0;

	while (sec != 100)
	{

		printf("*************************\n"
			"  0 - Programdan Çıkış Yap\n"
			"  1 - Listenizi Oluşturun\n"
			"  2 - Listeyi Ekrana Yazdırın\n"
			"  3 - Listede İstediğiniz Herhangi Bir Veriyi Silin\n"
			"  4 - Listeye Veri Ekleme (Seçilen Verinin Öncesine Ekler)\n"
			"  5 - Listenin Başına Veri Ekleme\n"
			"  6 - Listenin Sonuna Veri Ekleme\n"
			"  7 - Listedeki Verilerin Sayısı\n"
			"  8 - Listeyi Sil(Yok et)\n"
			"  9 - Listede Araya Eleman Ekleme\n"
			" 10 - Liste Palindrom Mudur?\n"


		);

		printf("\n Seçiminizi Yapınız:");
		scanf("%d", &sec);

		printf("\n");

		if (sec == 0) exit(0);
		else if (sec == 1) createList();
		else if (sec == 2) printList();
		else if (sec == 3) deleteNode();
		else if (sec == 4) addNode();
		else if (sec == 5) addNodeFirst();
		else if (sec == 6) addNodeLast();
		else if (sec == 7) cnt();
		else if (sec == 8) listeyiSil();
		else if (sec == 9) addthen();
		else if (sec == 10) palindrom();
	}
}

```

## C Programlama İkili Arama Ağacı (Binary Search Tree BTREE)

```c
/* İkili Arama Ağacı (Binary Search Tree BTREE) */

#include <stdio.h>
#include <locale.h> //Tüm Diller ve Karakter setleri bu kütüphane de yer alır. 


struct node {
	int data;
	struct node* left;  //Sol çocuğa işaretçi
	struct node* right; // Sağ çocuğa işaretçi
};

typedef struct node BTREE;

BTREE* myroot = NULL;
BTREE* tmp;

//Fonksiyon Prototipleri
BTREE* newNode(int);
int      isBSTorNot(BTREE*);
BTREE* insert(BTREE*, int);
void     preorder(BTREE*);
void     inorder(BTREE*);
void     postorder(BTREE*);
int      size(BTREE*);
BTREE* searchtree(BTREE*, int);
int      heightofTree(BTREE*);
void     mirror(BTREE*);
void     createmyroot();
int      minValue(BTREE*);
int      maxValue(BTREE*);
BTREE* deleteNode(BTREE*, int);
int      pathTotal(BTREE*, int);
void     createmyroot();




BTREE* newNode(int data) {

	BTREE* p;

	p = (BTREE*)malloc(sizeof(BTREE)); //Bellekten yer alıyor

	p->data = data;
	p->left = NULL;
	p->right = NULL;

	return p; // Bu adresi geri dönderiyor.

}

int isBSTorNot(BTREE* root) { //İkili Arama Ağacı Kontrolü

	if (root == NULL)
		return 1;

	if (root->left != NULL && root->left->data > root->data)
		return 0;

	if (root->right != NULL && root->right->data < root->data)
		return 0;

	if (!isBSTorNot(root->left) || !isBSTorNot(root->right))
		return 0;

	return 1;
}


BTREE* insert(BTREE* root, int data) // İkili Ağaca Veri Ekleme
{
	if (root != NULL) {

		if (data < root->data)
			root->left = insert(root->left, data); //Küçükse sola ekleme

		else
			root->right = insert(root->right, data); //Büyük ve eşitse sağa ekleme
	}

	else
		root = newNode(data);
	/* Eğer root boşsa (Herhangi bir eleman yoksa) newnode(data)gönderiyor.
	   BTREE* newNode(int data) döndüreln adresi root a atıyor.
	*/

	return root;
}


void preorder(BTREE* root) { // Önce Kök

	// KÖK - SOL - SAĞ (Root-Left-Right) 

	if (root != NULL) {

		printf("%5d ", root->data);

		preorder(root->left);
		preorder(root->right);
	}
}

void inorder(BTREE* root) {  // Kök Ortada

	// SOL - KÖK - SAĞ (Left-Root-Right)

	if (root != NULL) {

		inorder(root->left);

		printf("%5d ", root->data);

		inorder(root->right);
	}
}

void postorder(BTREE* root) {  // Kök Sonda

	// SOL - SAĞ - KÖK (Left-Right-Root)

	if (root != NULL) {

		postorder(root->left);
		postorder(root->right);

		printf("%5d ", root->data);
	}
}

int size(BTREE* root) { // Düğüm Sayılarını Veren Fonksiyon

	if (root == NULL)
		return 0;

	else
		return size(root->left) + 1 + size(root->right);

}

int heightofTree(BTREE* root) { // Bir Ağacın Yüksekliğini Bulmak (Kökün Yüksekliği)

	if (root == NULL)
		return -1;

	else {

		int leftHeight, rightHeight;

		leftHeight = heightofTree(root->left);

		rightHeight = heightofTree(root->right);

		if (rightHeight > leftHeight)
			return rightHeight + 1;

		else
			return leftHeight + 1;
	}
}


BTREE* searchtree(BTREE* node, int data) { // İstenilen Veriyi Bulmak

	if (node != NULL)

		if (node->data == data)
			return node;

		else if (node->data > data)
			searchtree(node->left, data);

		else
			searchtree(node->right, data);

	else
		return NULL;
}



void mirror(BTREE* root) {
	/*
	İkili Bir Ağacın sol çocukları ile sağ çocukların yerini değiştiren fonksiyon. (Ayna Görüntüsü)

	*/
	if (root == NULL)
		return;

	else {
		BTREE* temp;

		mirror(root->left);
		mirror(root->right);

		temp = root->left; // Yer değiştirme işlemi yapıyor.

		root->left = root->right;
		root->right = temp;
	}
}

int minValue(BTREE* root) { // Ağaçtaki Tüm Verilerden En Küçük Olan Değer
	if (root == NULL)
		return 0;

	while (root->left != NULL)
		root = root->left;

	return(root->data);
}

int maxValue(BTREE* root) { // Ağaçtaki Tüm Verilerden En Büyük Olan Değer

	if (root == NULL)
		return 0;

	while (root->right != NULL)
		root = root->right;

	return(root->data);
}

BTREE* deleteNode(BTREE* root, int num) {

	BTREE* p, * q;

	if (root == NULL) //Ağaç yoksa
		return NULL;


	if (num < root->data) // Silinecek sayı, ebeveyninin verisinden küçükse
		root->left = deleteNode(root->left, num); // Sol Alt Ağaca Geçiliyor.

	else if (num > root->data) // Silinecek sayı, ebeveyninin verisinden büyükse
		root->right = deleteNode(root->right, num); // Sağ Alt Ağaca Geçiliyor.

	else
	{
		// Silinecek olan düğümün çocuğu yok ise
		if (root->left == root->right)
		{
			free(root);
			return NULL;
		}

		// Silinecek olan düğümün 1 çocuğu var ise
		if (root->left == NULL)
		{
			p = root->right;
			free(root);
			return p;
		}

		else if (root->right == NULL) {
			p = root->left;
			free(root);
			return p;
		}

		// Silinecek olan düğümün 2 çocuğu var ise

		else {
			p = q = root->right;
			while (p->left != NULL)
				p = p->left;
			p->left = root->left;
			free(root);
			return q;
		}
	}
}

int pathTotal(BTREE* root, int sum) {
	/*

	Girilin bir int değeri, kökten itibaren yaprak dahil olmak üzere o yol üzerindeki verilerin toplamına eşit mi?

	*/
	int pathSum;

	if (root == NULL) //Ağaç yok ise
		return (sum == 0);

	else {

		pathSum = sum - root->data;

		return(pathTotal(root->left, pathSum) || pathTotal(root->left, pathSum));
	}
}

void createmyroot() {

	int n = 0;
	int i = 0;

	printf("Ağaca Veri Eklemek İçin Sayı Giriniz (-1 Girilene kadar) \n");

	do {

		printf(" %d. Sayıyı Giriniz: ", i + 1);
		scanf("%d", &n);

		if (n != -1)
			myroot = insert(myroot, n);

		i++;

	} while (n != -1);

}

int main()
{
	setlocale(LC_ALL, "Turkish"); //Türkçe karakter yazdırmamızı sağlayan fonksiyon

	int sec = 0;
	int node;

	while (sec != 100)
	{
		printf(
			"\n ****************************************************\n"
			"   1 - Ağaç Oluştur / Ağaç Varsa Veri Ekle\n"
			"   2 - İkili Bir Ağaç mı?\n"
			"   3 - Preorder?\n"
			"   4 - Inorder?\n"
			"   5 - Postorder?\n"
			"   6 - Ağaçtan İstediğiniz Veriyi Bulma\n"
			"   7 - Ağacın Yüksekliği (Kökün Yüksekliği) Nedir?\n"
			"   8 - Ağacın En Küçük Değeri Nedir?\n"
			"   9 - Ağacın En Büyük Değeri Nedir?\n"
			"  10 - Ağacın Düğümlerinin Sayısı Nedir?\n"
			"  11 - Ağaçtan Veri Silmek\n"
			"  12 - Sol Çocukları ile Sağ Çocukların Yerini Değiştir\n"
			"  13 - Girdiğiniz Değer Herhangi Bir Yol Üzerindeki Değerler Toplamına Eşit mi?\n"
			"  14 - ÇIKIŞ? \n"
		);

		printf("\n\n Seçiminizi Yapınız: ");
		scanf("%d", &sec);

		printf("\n");

		if (sec == 1) createmyroot();

		else if (sec == 2) {
			if (isBSTorNot((myroot)))
				printf("\n -- İkili Arama Ağacıdır.\n");
			else
				printf("\n -- İkili Arama Ağacı Değildir!\n");
		}

		else if (sec == 3) preorder(myroot);
		else if (sec == 4) inorder(myroot);
		else if (sec == 5) postorder(myroot);
		else if (sec == 6) {
			printf("\nAranacak Veriyi Giriniz: ");
			scanf("%d", &node);

			tmp = searchtree(myroot, node);

			if (tmp)
			{
				printf("Düğüm Bulundu= %d\n", tmp->data);
			}
			else
			{
				printf("Ağaçta Böyle Bir Veri YOK\n");
			}
		}

		else if (sec == 7) {
			printf("Ağacın Yüksekliği: %d\n", heightofTree(myroot));
		}

		else if (sec == 8) printf("%d", minValue(myroot));
		else if (sec == 9) printf("%d", maxValue(myroot));
		else if (sec == 10) printf("%d", size(myroot));
		else if (sec == 11) {

			printf("\nSilinecek Veriyi Giriniz: ");
			scanf("%d", &node);

			tmp = deleteNode(myroot, node);

			if (tmp)
			{
				printf("Düğüm Silindi");
			}
			else
			{
				printf("Ağaçta Böyle Bir Veri YOK\n");
			}
		}

		else if (sec == 12) mirror(myroot);

		else if (sec == 13) {

			printf("\n Veriyi Giriniz: ");
			scanf("%d", &node);

			tmp = pathTotal(myroot, node);

			if (tmp)
			{
				printf("\n-- Yoldaki Değerlerin Toplamı Girdiğiniz Değere EŞİT --\n");
			}
			else
			{
				printf("\n-- Yoldaki Değerlerin Toplamı Girdiğiniz Değere Eşit DEĞİL! -- \n");
			}
		}
		else if (sec == 14) exit(0);
	}
}

```

## C Programlama AVL Ağacı (AVL Tree) - Dengeli İkili Arama Ağacı

```c
/* AVL Ağacı (AVL Tree)

- Dengeli İkili Arama Ağacı

*/

#include <stdio.h>
#include <locale.h> //Tüm Diller ve Karakter setleri bu kütüphane de yer alır. 


struct node {
	int data;
	struct node* left;  // Sol çocuğa işaretçi
	struct node* right; // Sağ çocuğa işaretçi
	int height;
};

typedef struct node AVLTREE;

AVLTREE* myroot = NULL;
AVLTREE* tmp;



//Fonksiyon Prototipleri

int height(AVLTREE*);
int balance(AVLTREE*);
int maxNumber(int, int);
AVLTREE* newNode(int);
AVLTREE* rightRotate(AVLTREE*);
AVLTREE* leftRotate(AVLTREE*);
AVLTREE* leftRightRotate(AVLTREE*);
AVLTREE* rightLeftRotate(AVLTREE*);
AVLTREE* insert(AVLTREE*, int);
void     preorder(AVLTREE*);
void     inorder(AVLTREE*);
void     postorder(AVLTREE*);
int      size(AVLTREE*);
AVLTREE* searchtree(AVLTREE*, int);
int      heightofTree(AVLTREE*);
int      minValue(AVLTREE*);
int      maxValue(AVLTREE*);
void     createmyroot();
AVLTREE* deleteNode(AVLTREE*, int);


int height(AVLTREE* n) // işaretlenen Düğümün Yüksekliği
{
	if (n == NULL)
		return 0;

	return n->height;
}

int maxNumber(int x, int y) { // İki Sayıdan En Büyüğü

	return (x > y) ? x : y;

	/*
	int maxValue(int x, int y) {

		if(x>=y)
			return x;
		else
			return y;

	}*/
}


/*
- AVL ağacındaki bir düğümün denge faktörü, sol alt ağacın yüksekliği ile o düğümün sağ alt ağacının yüksekliği arasındaki farktır.
- AVL ağaçlarınının sol ve sağ alt ağaçlar arasındaki yükseklik farkı en fazla 1'dir. (İç Ağaçlarda dahil)
*/

int balance(AVLTREE* n)
{
	if (n == NULL)
		return 0;

	return height(n->left) - height(n->right);
}



AVLTREE* newNode(int data) {

	AVLTREE* p;

	p = (AVLTREE*)malloc(sizeof(AVLTREE)); // Bellekten yer alıyor

	p->data = data;
	p->left = NULL;
	p->right = NULL;

	p->height = 1;

	return p; // Bu adresi geri dönderiyor.

}

/* Tek Döndürme (Single Rotation)

1- Sağa Döndürme (Right Rotate)
2- Sola Döndürme (Left  Rotate)
*/

AVLTREE* rightRotate(AVLTREE* node) {

	AVLTREE* temp = node->left;

	node->left = temp->right;

	temp->right = node;

	node->height = maxNumber(height(node->left), height(node->right)) + 1;

	temp->height = maxNumber(height(temp->left), height(temp->right)) + 1;

	return temp;
}

AVLTREE* leftRotate(AVLTREE* node) {

	AVLTREE* temp = node->right;

	node->right = temp->left;

	temp->left = node;

	node->height = maxNumber(height(node->left), height(node->right)) + 1;

	temp->height = maxNumber(height(temp->left), height(temp->right)) + 1;

	return temp;
}

AVLTREE* leftRightRotate(AVLTREE* node) {

	node->left = leftRotate(node->left);

	return rightRotate(node);
}


AVLTREE* rightLeftRotate(AVLTREE* node) {

	node->right = rightRotate(node->left);

	return leftRotate(node);
}


AVLTREE* insert(AVLTREE* node, int data) {

	if (node == NULL)
		return(newNode(data));


	if (data < node->data)
		node->left = insert(node->left, data);

	else if (data > node->data)
		node->right = insert(node->right, data);

	else
		return node;

	node->height = 1 + maxNumber(height(node->left), height(node->right));


	int blnc = balance(node);

	if (blnc > 1 && data < node->left->data)
		return rightRotate(node);

	if (blnc < -1 && data > node->right->data)
		return leftRotate(node);

	if (blnc > 1 && data > node->left->data)
		return leftRightRotate(node);

	if (blnc < -1 && data < node->right->data)
		return rightLeftRotate(node);

	return node;
}



void preorder(AVLTREE* root) { // Önce Kök

	// KÖK - SOL - SAĞ (Root-Left-Right) 

	if (root != NULL) {

		printf("%5d ", root->data);

		preorder(root->left);
		preorder(root->right);
	}
}

void inorder(AVLTREE* root) {  // Kök Ortada

	// SOL - KÖK - SAĞ (Left-Root-Right)

	if (root != NULL) {

		inorder(root->left);

		printf("%5d ", root->data);

		inorder(root->right);
	}
}

void postorder(AVLTREE* root) {  // Kök Sonda

	// SOL - SAĞ - KÖK (Left-Right-Root)

	if (root != NULL) {

		postorder(root->left);
		postorder(root->right);

		printf("%5d ", root->data);
	}
}

int size(AVLTREE* root) { // Düğüm Sayılarını Veren Fonksiyon

	if (root == NULL)
		return 0;

	else
		return size(root->left) + 1 + size(root->right);

}

AVLTREE* minValueNode(AVLTREE* node)
{
	AVLTREE* current = node;
	while (current->left != NULL)
		current = current->left;
	return current;
}

int minValue(AVLTREE* root) { // Ağaçtaki Tüm Verilerden En Küçük Olan Değer
	if (root == NULL)
		return 0;

	while (root->left != NULL)
		root = root->left;

	return(root->data);
}

int maxValue(AVLTREE* root) { // Ağaçtaki Tüm Verilerden En Büyük Olan Değer

	if (root == NULL)
		return 0;

	while (root->right != NULL)
		root = root->right;

	return(root->data);
}


int heightofTree(AVLTREE* root) { // Bir Ağacın Yüksekliğini Bulmak (Kökün Yüksekliği)

	if (root == NULL)
		return -1;

	else {

		int leftHeight, rightHeight;

		leftHeight  = heightofTree(root->left);

		rightHeight = heightofTree(root->right);

		if (rightHeight > leftHeight)
			return rightHeight + 1;

		else
			return leftHeight + 1;
	}

}

AVLTREE* searchtree(AVLTREE* node, int data) { // İstenilen Veriyi Bulmak

	if (node != NULL)

		if (node->data == data)
			return node;

		else if (node->data > data)
			searchtree(node->left, data);

		else
			searchtree(node->right, data);

	else
		return NULL;
}

AVLTREE* deleteNode(AVLTREE* root, int data) {

	/*1. Kısım: İkili Arama Ağacı silme işlemi ile aynı yapılır*/

	if (root == NULL)
	return root;

	if (data < root->data)
		root->left = deleteNode(root->left, data);

	else if (data > root->data)
		root->right = deleteNode(root->right, data);

	else
	{
		if ((root->left == NULL) || (root->right == NULL))
		{
			AVLTREE* temp = root->left ? root->left : root->right;
			if (temp == NULL)
			{
				temp = root;
				root = NULL;
			}
			else
				*root = *temp;

			free(temp);
		}
		else
		{
			AVLTREE* temp = minValueNode(root->right);
			root->data = temp->data;
			root->right = deleteNode(root->right, temp->data);
		}
	}


	/* 2. Kısım: AVL Ağacı Olması İçin Döndürme İşlemleri Yapılır*/

	if (root == NULL)
		return root;

	root->height = 1 + maxNumber(height(root->left), height(root->right));


	int blnc = balance(root);

	if (blnc > 1 && balance(root->left) >= 0)
		return rightRotate(root);

	if (blnc > 1 && balance(root->left) < 0)
		return leftRightRotate(root);

	if (blnc < -1 && balance(root->right) <= 0)
		return leftRotate(root);

	if (blnc < -1 && balance(root->right) > 0)
		return rightLeftRotate(root);

	return root;
}




void createmyroot() {

	int n = 0;
	int i = 0;

	printf("Ağaca Veri Eklemek İçin Sayı Giriniz (-1 Girilene kadar) \n");

	do {

		printf(" %d. Sayıyı Giriniz: ", i + 1);
		scanf("%d", &n);

		if (n != -1)
			myroot = insert(myroot, n);

		i++;

	} while (n != -1);

}



int main() {

	setlocale(LC_ALL, "Turkish"); //Türkçe karakter yazdırmamızı sağlayan fonksiyon

	int sec = 0;
	int node;


	while (sec != 100)
	{

		printf(
			"\n ****************************************************\n"
			"   1 - Ağaç Oluştur / Ağaç Varsa Veri Ekle\n"
			"   2 - Preorder?\n"
			"   3 - Inorder?\n"
			"   4 - Postorder?\n"
			"   5 - Ağaçtan İstediğiniz Veriyi Bulma\n"
			"   6 - Ağacın Yüksekliği (Kökün Yüksekliği) Nedir?\n"
			"   7 - Ağacın En Küçük Değeri Nedir?\n"
			"   8 - Ağacın En Büyük Değeri Nedir?\n"
			"   9 - Ağacın Düğümlerinin Sayısı Nedir?\n"
			"  10 - Ağaçtan Veri Silmek\n"


		);

		printf("\n\n Seçiminizi Yapınız: ");
		scanf("%d", &sec);

		printf("\n");

		if (sec == 1) createmyroot();

		else if (sec == 2) preorder(myroot);
		else if (sec == 3) inorder(myroot);
		else if (sec == 4) postorder(myroot);
		else if (sec == 5) {
			printf("\nAranacak Veriyi Giriniz: ");
			scanf("%d", &node);

			tmp = searchtree(myroot, node);

			if (tmp)
			{
				printf("Düğüm Bulundu= %d\n", tmp->data);
			}
			else
			{
				printf("Ağaçta Böyle Bir Veri YOK\n");
			}

		}

		else if (sec == 6) {
			printf("Ağacın Yüksekliği: %d\n", heightofTree(myroot));
		}

		else if (sec == 7) printf("%d", minValue(myroot));
		else if (sec == 8) printf("%d", maxValue(myroot));
		else if (sec == 9) printf("%d", size(myroot));
		else if (sec == 10) {

			printf("\nSilinecek Veriyi Giriniz: ");
			scanf("%d", &node);

			tmp = deleteNode(myroot, node);

			if (tmp)
			{
				printf("Düğüm Silindi");
			}
			else
			{
				printf("Ağaçta Böyle Bir Veri YOK\n");
			}
		}
	}
}

```
