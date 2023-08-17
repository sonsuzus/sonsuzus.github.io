---
title:  C Programlama Alıştırmalar
author: sonsuz
date: 2023-08-01 23:20:15 +0300
categories: [Program,C]
tags: [c,programlama,alıştırma,algoritma]
---

#### İşaretsiz 2'lik sayı sisteminde _(unsigned binary system)_ 8 bitlik alanda aşağıdaki tam sayıları ifade ediniz:

* 255
* 15
* 48
* 65
* 129

### İşaretli ikilik sayı sisteminde *(signed binary system)*
 
* 1 byte'lık alanda yazılabilecek en küçük tamsayı nedir? 
* 1 byte'lık alanda yazılabilecek en büyük tamsayı nedir?
* 2 byte'lık alanda yazılabilecek en küçük tamsayı nedir?
* 2 byte'lık alanda yazılabilecek en büyük tamsayı nedir?
* 4 byte'lık alanda yazılabilecek en küçük tamsayı nedir?
* 4 byte'lık alanda yazılabilecek en büyük tamsayı nedir?
* 8 byte'lık alanda yazılabilecek en küçük tamsayı nedir? (Yaklaşık bir sayı yazabilirsiniz.)
* 8 byte'lık alanda yazılabilecek en büyük tamsayı nedir? (Yaklaşık bir sayı yazabilirsiniz.)

#### İşaretli 2'lik sayı sisteminde _(signed binary system)_ 8 bitlik alanda aşağıdaki tam sayıları ifade ediniz:

* -50
* -100
* 127
* 33
* -128
* -1

#### Aşağıdaki sayıların 2'ye tümleyenlerini _(two's complement)_ yazınız:

* 1001 0000
* 0000 0001
* 1111 0100
* 1111 1111
* 0101 1010

#### Aşağıda _10_'luk sayı sisteminde yazılmış tam sayıları _16_'lık sayı sisteminde ifade ediniz:

* 1024
* 170
* 255
* 178
* 65
* 48

#### Aşağıda tanımlanan sayıları _16_'lık sayı sisteminde ifade ediniz:

* İşaretli ikilik sayı sisteminde _2 byte_'lık alanda yazılabilecek en küçük tam sayı
* İşaretli ikilik sayı sisteminde _2 byte_'lık alanda yazılabilecek en büyük tam sayı
* İşaretli ikilik sayı sisteminde _2 byte_'lık alanda yazılan -1 değeri

#### İşaretsiz ikilik sayı sistemi için aşağıdaki cümlelerde işaretli yerleri doldurunuz:

* _1 byte_'lık alanda ifade edilebilecek en büyük tamsayı \___________  değeridir.
* _16_ bitlik bir sayının en yüksek anlamlı biti _(most significant bit)_ sayının \___________ bitidir.
* _8_ bitlik bir sayının en düşük anlamlı biti _(lest significant bit)_ sayının \___________ bitidir.
* İşaretsiz _(unsigned)_ bir tam sayının yalnızca tek bir biti ise o sayı _2_'nin  \___________.
* _15_ sayısının _1_'e tümleyeni _(one's complement)_  \___________ değeridir.
* Bir tamsayının _0_.biti _1_ ise o sayı \___________.

#### Aşağıdaki bildirimlerden geçersiz olanları işaretleyiniz: 

```c
int main(void)
{
	signed x1;
	unsigned double x2;
	long int long x3;
	bool x4;
	char int x5;
	x6 float;
	long double x7;
	unsigned short int x8;
	long unsigned x9;
	long float x10;
}
```

### Aşağıdaki bildirimlerden geçersiz olanları işaretleyiniz: 

```c
int main(void)
{
	int _6542;
	unsigned check;
	long long_distance;
	int 4thvalue;
	short too_short;
	signed binary;
	int register;
	double BURGER;
	int int_x;
}
```

#### Aşağıdaki cümlelerin doğru ya da yanlış olduğunu yazınız:

+ Otomatik ömürlü nesnelerin çöp değerleri _(garbage value)_ ile kullanılması tanımsız davranıştır.
+ Tam sayı ve gerçek sayı türlerinden statik ömürlü değişkenler ilk değer verilmeden tanımlansalar dahi hayata _0_ değeri ile başlarlar.
+ _long long_ türü en az _4 byte_ olmak zorundadır.
+ _char_ türünün işaretli ya da işaretsiz olması derleyiciye bağlıdır _(implementation defined)_
+ işaretli tamsayı türlerinde taşma tanımsız davranıştır _(undefined behavior)_.
+ işaretsiz tamsayı türlerinde taşma tanımsız davranıştır _(undefined behavior)_.
+ ```int x;``` biçiminde bildirilen _x_ değişkeni işaretli int türündendir.
+ _long_ türünden bir değişken _int_ türünden bir değişkene göre daha büyük tam sayıları tutabilir.
+ ```signed x;``` biçiminde bildirilen x değişkeni işaretli _char_ türündendir.

### Aşağıdaki bildirimlerden geçersiz olanları işaretleyiniz: 

```c
int x1 = 10;
int x2 = x1 + 20;

int main(void)
{
	int x3 = x1 + x2;
	static int x = x3;
}
```

#### _int_ türünün _2_ byte _long_ türünün _4_ byte olduğu bir derleyicide aşağıdaki sabitlerin türünü yazınız:

* 'A'
* 32767
* 32768
* 50000
* 0x7000
* 0xFFFF
* 50000U
* 10000U
* '\x1A'

#### Aşağıdaki sabitlerin _(constants)_ türlerini yazınız. Geçersiz olanları belirtiniz.

* 0.
* 0.F
* 34f
* 3E3
* 2.5e+2
* 45.3L
* 4.1l
* .5
* 3.2e-2f
* 67F

* _3_ sayıdan en büyüğünü hesaplayan _max3_ isimli bir fonksiyon tanımlayınız.

* _main_ fonksiyonu içinde standart giriş akımından _3_ tamsayı alınız.

* _max3_ isimli fonksiyona çağrı yaparak alınan _3_ tam sayıdan en büyüğünü standart çıkış akımına _(ekrana)_ yazdırınız:

* Aynı programı bu kez gerçek sayılar için yazınız.

### Örnek ekran çıktısı (1)

```
uc tamsayi girin:
12 56 8

12, 56 ve 8 sayilarinin en buyugu 56
```

### Örnek ekran çıktısı (2)

```
uc gercek sayi girin:
2.87 1.35 0.12

2.870000, 1.350000 ve 0.120000 sayilarinin en buyugu 2.870000
```

* _4_ sayıdan en büyüğünü hesaplayan _max4_ isimli bir fonksiyon tanımlayınız.

* _main_ fonksiyonu içinde standart giriş akımından _4_ tamsayı alınız.

* _max4_ isimli fonksiyona çağrı yaparak alınan _4_ tam sayıdan en büyüğünü standart çıkış akımına _(ekrana)_ yazdırınız:

### Örnek ekran çıktısı (1)

```
dört tamsayi girin:
12 56 91 8

12, 56, 91 ve 8 sayilarinin en buyugu 96
```

```c
#include <stdio.h>

int main(void)
{
	int x = -1;
	long y = -2;
	long long z = -3;

  //x, y ve z değişkenlerinin değerlerini standart output'a yazdıran tek bir printf çağrısı gerçekleştirin.
}

Aşağıdaki program derlenip çalıştırıldığında ekran çıktısı ne olur?
  
```c
#include <stdio.h>

int main(void)
{
	int x = 333;

	printf("%d", printf("%d", printf("%d", x)));
}

```

#### Aşağıdaki programın ekran çıktısı ne olur? 

__1. program__

```c
#include <stdio.h>
 
int main(void)
{
	int x = 1;
	int y = -1;
	int z = !--x - !++y;
 
	z += x += y;
 
	printf("%d%d%d", x, y, z);
 
	return 0;
}
```

#### Aşağıdaki programın ekran çıktısı ne olur? 

```c
#include <stdio.h>

int main(void)
{
	int x = 10;
	int y = 20;

	int a = x+++y;

	printf("%d\n", -x + y + a);
}
```

#### Aşağıdaki programın ekran çıktısı ne olur?

```c
#include <stdio.h>

int main(void)
{
	int x = 999;

	printf("%d\n", printf("%d", printf("%d", ++x)));
}
```

[Ödevin Cevabı](https://youtu.be/m-P5Lbk3-RY)

#### Aşağıdaki programın ekran çıktısı ne olur?

```c
#include <stdio.h>

int main(void)
{
	int x, y, z;

	x = 2, y = 1, z = 0;
	x = x && y || z;
	printf("%d\n", x);

	printf("%d\n", x || !y && z);

	x = y = 1;
	z = x++ - 1;
	printf("%d\n", x);
	printf("%d\n", z);

	z += -x++ + ++y;
	printf("%d\n", x);
	printf("%d\n", z);

	return 0;
}
```

#### Aşağıdaki programın ekran çıktısı ne olur?

```c
#include <stdio.h>

int main(void)
{
	int x = 2, y, z;

	x *= 3 + 2;
	printf("%d\n", x);

	x *= y = z = 4;
	printf("%d\n", x);

	x = y == z;
	printf("%d\n", x);

	x == (y = z);
	printf("%d\n", x);
}
```

[Ödevin Cevabı](https://youtu.be/U4Mz_mQNpS0)

#### Aşağıdaki programın ekran çıktısı ne olur?

```c
#include <stdio.h>

int main(void)
{
	int x = -3 + 4 * 5 - 6;

	printf("%d\n", x);

	x = 3 + 4 % 5 - 6;

	printf("%d\n", x);

	x = -3 * 4 % -6 / 5;

	printf("%d\n", x);

	x = (7 + 6) % 5 / 2;

	printf("%d\n", x);
}
```

#### Aşağıdaki programın ekran çıktısı ne olur?

```c
#include <stdio.h>

int main(void)
{
	int a = 0;

	if (-1 < a-- < 0)
		printf("%d", --a);
	else
		printf("%d", ++a);
}
```

#### Aşağıdaki programın ekran çıktısı ne olur?

```c
#include <stdio.h>

int main(void)
{
	int x = 1;

	if (++x > 2,5)
		printf("%d", ++x);
	else
		printf("%d", x++);
}
```

[Ödevin Cevabı](https://youtu.be/8bQH0DaVX14)

#### Aşağıdaki programın ekran çıktısı ne olur?

```c
#include <stdio.h>

void func(int x)
{
	++x;
	printf("%d ", x);
}

int main(void)
{
	int x = 10;

	func(++x);
	func(x++);

	printf("%d ", x);
}
```

[Ödevin Cevabı](https://youtu.be/RUAfuBdLWj0)

#### Aşağıdaki kod için şu sorulara yanıt vermeye çalışın:

* sentaks hatası var mı?
* tanımsız davranış *(undefined behavior)* var mı?
* ekran çıktısı ne olur?

```c
#include <stdio.h>

int main(void)
{
	int x = 4;
	int y = 10;

	printf("%d\n", (x++, ++x));
	printf("%d\n", (y *= x++, y + x));
}
```

#### Aşağıdaki kod için şu sorulara yanıt vermeye çalışın:

* sentaks hatası var mı?
* tanımsız davranış *(undefined behavior)* var mı?
* ekran çıktısı ne olur?

```c
#include <stdio.h>

double foo(double x)
{
	return x + 5,6;
}

int main(void)
{
	printf("%f\n", foo(3.));
}
```

[Ödevin Cevabı](https://youtu.be/RUAfuBdLWj0)

#### Aşağıdaki kod için şu sorulara yanıt vermeye çalışın:

* sentaks hatası var mı?
* tanımsız davranış *(undefined behavior)* var mı?
* ekran çıktısı ne olur?

```c
#include <stdio.h>

int main(void)
{
	int x = 0;
	int y = 1;

	printf("%d\n", !!x == !!y > x + 1);
	printf("%d\n", !!y > !y == !!x < !x);
	printf("%d\n", !x + !!x + y - !y - !!y);
}
```

#### Aşağıdaki kod için şu sorulara yanıt vermeye çalışın:

* sentaks hatası var mı?
* tanımsız davranış *(undefined behavior)* var mı?
* ekran çıktısı ne olur?

```c
#include <stdio.h>

int g = 3;

int f1(int x)
{
	return x * g++;
}

int f2(int x)
{
	return x * ++g;
}


int main(void)
{
	printf("%d\n", f2(f1(g)));
	printf("%d\n", f1(f2(g)));
}
```

#### Aşağıdaki C programını derleyip çalıştırın:

```c
#include <stdio.h>

int main(void)
{
	double d = 0.;
	int i;

	for (i = 0; i < 10; i++)
		d += .1;

	if (d == 1.)
		printf("d, 1. degerinde\n");
	else
		printf("d, 1. degerinde degil\n");

	return 0;
}
```

Program neden ekrana

```
d, 1. degerinde degil
```
yazısı çıkıyor? Açıklayınız.

#### Aşağıdaki C programı çalıştırıldığında bu programın çıktısı ne olur?

```c
#include <stdio.h>

#include <stdio.h>

int main(void)
{
	int x = 10;
	int y = 20;

	int a = x+++y;
	
	printf("%d\n", a);
	printf("%d\n", x);
	printf("%d\n", y);
}
```

__Sorunun yanıtı şu seçeneklerden biri de olabilir:__</br>
+ Sentaks hatası (derleme zamanı hatası)
+ Tanımsız davranış. _(undefined behavior)_
+ Derleyiciye göre değişir. _(unspecified behavior / implementation defined)_

[Ödevin Cevabı](https://www.youtube.com/watch?v=Xg3Gx5Uj7Mc)

Aşağıdaki C programı çalıştırıldığında bu programın çıktısı ne olur?

```c
#include <stdio.h>

void func(int x)
{
	++x;
	printf("%d", x);
}

int main(void)
{
	int x = 10;
	
	func(++x);
	func(x++);
	
	printf("%d", x);
}
```

__Sorunun yanıtı şu seçeneklerden biri de olabilir:__</br>
+ Sentaks hatası (derleme zamanı hatası)
+ Tanımsız davranış. _(undefined behavior)_
+ Derleyiciye göre değişir. _(unspecified behavior / implementation defined)_

Aşağıdaki C programı çalıştırıldığında bu programın çıktısı ne olur?

```c
#include <stdio.h>
 
int main(void)
{
	int x, y, z, t;
 
	x = y = z = t = 1;
	x = ++y > 1 || z++ > 1 && ++t > 1;
	printf("%d%d%d%d", x, y, z, t);
 
	return 0;
}
```

__Sorunun yanıtı şu seçeneklerden biri de olabilir:__</br>
+ Sentaks hatası (derleme zamanı hatası)
+ Tanımsız davranış. _(undefined behavior)_
+ Derleyiciye göre değişir. _(unspecified behavior / implementation defined)_

Aşağıdaki C programı çalıştırıldığında bu programın çıktısı ne olur?

```c
#include <stdio.h>
 
int main(void)
{
	int ival = 3;
	printf("%d", ival++ + ++ival);
}
```

__Sorunun yanıtı şu seçeneklerden biri de olabilir:__</br>
+ Sentaks hatası (derleme zamanı hatası).
+ Tanımsız davranış _(undefined behavior)_.
+ Derleyiciye göre değişir. _(unspecified behavior / implementation defined)_.

Aşağıdaki C programı çalıştırıldığında bu programın çıktısı ne olur?

```c
#include <stdio.h>
 
int main(void)
{
	int a = 11;
 
	if (10 < --a < 20)
		printf("%d", --a);
	else
		printf("%d", ++a);
}
```

__Sorunun yanıtı şu seçeneklerden biri de olabilir:__</br>
+ Sentaks hatası (derleme zamanı hatası)
+ Tanımsız davranış. _(undefined behavior)_
+ Derleyiciye göre değişir. _(unspecified behavior / implementation defined)_

[Ödevin Cevabı](https://youtu.be/3ZF3pD2BIYo)

Aşağıdaki C programı çalıştırıldığında bu programın çıktısı ne olur?

```c
#include <stdio.h>
 
int main(void)
{
	int x = 1;
	
	if (++x > 2,5)
		printf("%d", ++x);
	else
		printf("%d", x++);
}
```

__Sorunun yanıtı şu seçeneklerden biri de olabilir:__</br>
+ Sentaks hatası (derleme zamanı hatası)
+ Tanımsız davranış. _(undefined behavior)_
+ Derleyiciye göre değişir. _(unspecified behavior / implementation defined)_

#### Aşağıdaki C kodlarında kullanlan if deyimlerindeki hataları açıklayınız:

```c
double foo(void);
void bar(double);

int main(void)
{
	double dval = foo();

	if (dval > 3,4)
		bar(dval);
}
//////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////
double foo(void);
void bar(double);

int main(void)
{
	double dval = foo();

	if (dval > 4.5);
		bar(dval);
}
//////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////
int func(void);
void bar(int);

int main(void)
{
	int x = func();

	if (10 < x < 20)
		bar(x);
}
//////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////
int func(void);
void bar(int);

int main(void)
{
	int x = func();

	if (x != 7  || x != 23)
		bar(x);
}

```

[Ödevin Cevabı](https://youtu.be/_Rz4t9N_z2Q)

#### Aşağıdaki C programının ekran çıktısı ne olur?

```c
#include <stdio.h>

int main(void)
{
	int x = 5;

	while (x--);
		printf("%d ", x);
}
```

#### Aşağıdaki C programının ekran çıktısı ne olur?

```c
#include <stdio.h>

int main(void)
{
	int x = 0;

	while (x < 10) {
		if (x % 2 == 0) {
			printf("%d ", x);
			++x;
		}
		if (x % 3 != 0) {
			x += 2;
		}
		else {
			++x;
			printf("%d ", x);
		}
	}
}
```

#### 9 basamaklı en büyük Armstrong sayısını hesaplayan bir C programı yazınız.

#### Aşağıdaki C programı çalıştırıldığında bu programın çıktısı ne olur?

```c
#include<stdio.h>
 
int main(void)
{
	int num = 30;
	int ival = (num > 5 ? num <= 10 ? 10 : 20 : 50);
 
	printf("%d\n", ival);
}
```

__Sorunun yanıtı şu seçeneklerden biri de olabilir:__</br>
+ Sentaks hatası (derleme zamanı hatası)
+ Tanımsız davranış. _(undefined behavior)_
+ Derleyiciye göre değişir. _(unspecified behavior / implementation defined)_

### Aşağıdaki ifadaleri koşul operatörünü kullanarak yazınız:

**_y_ yıl değerini tutan değişken ve _int isleap(int)_ artık yıl test fonksiyonu olmak üzere**
+ Şubat ayının gün sayısı değerinde olan ifade
+ Yılın gün sayısı olan ifade

**_x_ ve _y_ işaretli int türden  değişkenler olmak üzere**
+ _x_ ve _y_'nin büyüğü _(max)_
+ _x_ ve _y_'nin küçüğü _(min)_
+ _x_'in mutlak değeri _(abs)_
+ _x_'in işaret değeri _(signum)_

#### Aşağıdaki C programında yorum satırı bulunan yere bir kod eklemeniz isteniyor:

```c
#include <stdio.h>

int main(void)
{
	int x, y, z;

	printf("uc tamsayi giriniz: ");
	scanf("%d%d%d", &x, &y, &z);
	/* code  */

}
```

#### Yazdığınız kod çalıştırıldığında girilen sayıları ekrana şu formatta yazdırmalı:

```
girdi           çıktı
=====        ============
30 10 20     10 < 20 < 30
7 5 7        5 < 7 = 7
2 2 2        2 = 2 = 2
9 6 6        6 = 6 < 9
```

#### Arkadaş Sayılar *(amicable numbers / friendly numbers)*

*x* ve *y* pozitif tamsayılar olmak üzere, eğer *x* sayısının çarpanları toplamı *y* sayısına, ve aynı zamanda *y* sayısının çarpanları toplamı *x* sayısına eşit ise, bu sayılar *“arkadaştır”*.
Örneğin *220* ve *284* arkadaş sayılardır:

```
220 => 1 + 2 + 4 + 5 + 10 + 11 + 20 + 22 + 44 + 55 + 110 = 284
284 => 1 + 2 + 4 + 71 + 142 = 220
```
Kendisine gönderilen iki tamsayının arkadaş olup olmadıklarını sınayan, __are_friends__ isimli işlevi tanımlayın:
```
int are_friends(int number1, int number2);
```
Yazdığınız işlevi aşağıdaki arkadaş sayı çiftleri ile test edebilirsiniz:
```
220 284                         
1184 1210
2620 2924
5020 5564
6232 6368
10744 10856
12285 14595
17296 18416
63020 76084
66928 66992
67095 71145
69615 87633
79750 88730
100485 124155
122265 139815
122368 123152
141664 153176
142310 168730
171856 176336
176272 180848
185368 203432
196724 202444
```

#### Collatz sanısı (Collatz conjecture)

1937 yılında *Lothar Collatz*  sıfırdan büyük her tamsayı için aşağıdaki problemi ortaya koydu:

*n* bir tamsayı olmak üzere her yeni n değeri için aşağıdaki kurallar uygulanacak
*n*,  1 değerine eşit ise işlemler sonlandırılıyor.
*n* çift ise yeni *n* değeri olarak *n / 2* alınıyor.
*n* tek ise yeni *n* değeri olarak *3 * n + 1* değeri alınıyor.

__Collatz__ sanısı matematikçilerin tüm çabalarına karşın halen kanıtlanmış değildir.

Kendisine gelen işaretsiz _long long_ türden bir tamsayı için bu serideki tüm sayıları (sayının kendisi ve 1 dahil olmak üzere) standart çıkış akımına yazdıran

```c
unsigned int display_collatz(unsigned long long val);
```
işlevini kodlayın.

İşlevin geri dönüş değeri standart çıkış akımına kaç sayı yazıldığı bilgisidir.

Aşağıda _72543_ tamsayısı için oluşturulan serinin _188_ terimi yer alıyor:

```
72543 217630 108815 326446 163223 489670 244835 734506 367253 1101760 
550880 275440 137720 68860 34430 17215 51646 25823 77470 38735 116206 
58103 174310 87155 261466 130733 392200 196100 98050 49025 147076 73538 
36769 110308 55154 27577 82732 41366 20683 62050 31025 93076 46538 23269 
69808 34904 17452 8726 4363 13090 6545 19636 9818 4909 14728 7364 3682 
1841 5524 2762 1381 4144 2072 1036 518 259 778 389 1168 584 292 146 73 
220 110 55 166 83 250 125 376 188 94 47 142 71 214 107 322 161 484 242 
121 364 182 91 274 137 412 206 103 310 155 466 233 700 350 175 526 263 
790 395 1186 593 1780 890 445 1336 668 334 167 502 251 754 377 1132 566 
283 850 425 1276 638 319 958 479 1438 719 2158 1079 3238 1619 4858 2429 
7288 3644 1822 911 2734 1367 4102 2051 6154 3077 9232 4616 2308 1154 577 
1732 866 433 1300 650 325 976 488 244 122 61 184 92 46 23 70 35 106 53 
160 80 40 20 10 5 16 8 4 2 1
```

#### Bir tamsayının süper asal *(super prime)* olup olmadığını test eden is_superprime isimli işlevin kodunu yazınız:

```c
int is_superprime(int val);
```

**Süper asal nedir?**

Bu sayılara "asal indeksli asal sayılar" *(prime indexed primes)* da denilmektedir. Tüm asal sayıların *1* değerinden başlayarak indekslendiğini düşünelim:

```
1. asal sayı 2
2. asal sayı 3
3. asal sayı 5
4. asal sayı 7
5. asal sayı 11
6. asal sayı 13
7. asal sayı 17

```

Eğer bir asal sayının indeksi de *(yani kaçıncı asal sayı olduğunu gösteren tamsayı da )* asal ise bu asal sayı bir süper asaldır. Örneğin yukarıdaki tabloda yer alan 3 *(2 indeksli)*, 5 *(3 indeksli)*, 11 *(5 indeksli)* ve 17 *(7 indeksli)* süper asal sayılardır.

Yazdığınız işlev kodunu aşağıdaki süper asal sayılarla test edebilirsiniz:
```
3, 5, 11, 17, 31, 41, 59, 67, 83, 109, 127, 157, 179, 191, 211, 241, 277, 
283, 331, 353, 367, 401, 431, 461, 509, 547, 563, 587, 599, 617, 709, 739, 
773, 797, 859, 877, 919, 967, 991
```

#### Aşağıdaki C programı çalıştırıldığında bu programın çıktısı ne olur?

```c
#include <stdio.h>

int main()
{
	int i = 1;
	do
	{
		printf("%d\n", i);
		i++;
		if (i < 15)
			continue;
	} while (0);

	return 0;
}
```

**Sorunun yanıtı şu seçeneklerden biri de olabilir:**

+ Sentaks hatası _(syntax error)_
+ Tanımsız davranış "(undefined behavior)*
+ Derleyiciye göre değişir. *(implementation defined - implementation specified).*

Tüm zamanların en ilginç matematikçilerinden biri olan *Ramanujan* hastanedeyken ünlü matematikçi *Hardy* onu hastanede ziyarete gider. Hardy gelirken bindiği taksinin plaka numarasının ilginç olmayan bir sayı olan *1729* olduğunu söyler. *Ramanujan* buna itiraz eder ve *1729* sayısının iki pozitif kübün toplamı olarak, iki değişik şekilde yazılabilecek en küçük sayı olduğunu açıklar:

```
1729 = 9^3 + 10^3 = 1^3 + 12^3
```

N bir pozitif tamsayı ve a, b, c, d birbirinden farklı tamsayılar olmak üzere eğer

```
N = a^3 + b^3 = c^3 + d^3
```

eşitliğini sağlayacak a, b, c ve d tamsayıları var ise N bir *Hardy-Ramanujan* sayısıdır. Örneğin *1729* bir *Hardy-Ramanujan* sayısıdır.

Bir C kodu yazarak *100000*'den küçük olan tüm *Hardy-Ramanujan* sayılarını bulunuz.

**Aşağıdaki koda tek bir karakter ekleyeceksiniz ya da koddan tek bir karakteri değiştireceksiniz. Yapılan değişiklikten sonra oluşan C programı derlenip çalıştırıldığında standart çıkış akımına 5 kez**

```
necati
```

yazacak.

Sorunun en az *3* farklı yanıtı olduğunu söylemeliyim. *3* yanıtı da bulmanız gerekiyor.

```c
#include <stdio.h>

int main()
{
	int n = 5;

	for (int i = 0; i < n; i--)
		printf("necati\n");

	return 0;
}
```

1'den büyük asal olmayan bir tamsayının rakamlarının toplamı, sayı asal çarpanlarına ayrılarak yazıldığında bu yazımda yer alan tüm asal sayıların rakamlarının toplamına eşit ise bu sayı bir **Smith Sayısı** denir.

Örneğin:

```
728 = 2 * 2 * 2 * 7 * 13  
7 + 2 + 8 = 2 + 2 + 2 + 7 + 1 + 3
```

olduğundan *728* bir **Smith** sayısıdır.

Peki neden bu sayılara **Smith** sayıları deniyor.  Lehigh Universitesi*'nden *Albert Wilansky* kayın biraderi *Harold Smith*'in telefon numarasının bu özelliğe sahip olduğunu fark edince bu tür sayılara *Smith* sayısı demiş. *(WikiPedia‘nın yalancısıyım)*
Kayınço’nun numarası *493 7775*.

```
493 7775 = 3 × 5 × 5 × 65837, 
4 + 9 + 3 + 7 + 7 + 7 + 5 = 42
3 + 5 + 5 + 6 + 5 + 8 + 3 + 7 = 42
```

*1000*'den küçük *Smith* sayıları şunlardır:

```
4, 22, 27, 58, 85, 94, 121, 166, 202, 265, 274, 319, 346,
355, 378, 382, 391, 438, 454, 483, 517,526, 535, 562, 576,
588, 627, 634, 636, 645, 648, 654, 663, 666, 690, 706, 728, 
729, 762, 778, 825, 852, 861, 895, 913, 915, 922, 958, 985
```

***1* ile *10000* arasındaki tüm *Smith* sayılarını bularak ekrana yazdıran bir *C* programı yazınız.**

#### Bir tamsayının basamaksal kökünü *(digital root)* bulan *get_digital_root* isimli işlevi tanımlayınız:

```c
int get_digital_root(int val);
```

Bir tamsayının basamaksal kökü tüm basamaklarının toplanması ile elde edilen tamsayıdır. Basamakları toplama, tek basamaklı bir sayı elde edilene kadar sürdürülür. Örneğin *34879* sayısının basamaksal kökü *4*'tür:

```
34879 -> 3 + 4 + 8 + 7 + 9 = 31
31 -> 3 + 1 = 4
```

##### Sayma sayılarında *10*’luk sayı sisteminde yalnızca _4_ tane *`factorion`* sayı var. 

İyi ama __factorion sayı__ ne demek? 
Basamaklarının faktöriyelleri toplamı kendisine eşit olan sayıya *factorion* deniyor. 
Örneğin _abc_ tamsayısı eğer bir *`factorion`* ise

```
abc = a! + b! + c!
```

Eşitliğinin doğru olması gerekiyor. İlk iki *`factorion`* sayının _1_ ve _2_ olduğu açık. 
Diğer iki _factorion_ sayıyı da bir _C_ programı yazarak siz bulun. 
Bir ipucu olarak her iki sayının da _100.000_‘den küçük olduğunu söyleyelim.

#### Aşağıdaki C programı çalıştırıldığında bu programın çıktısı ne olur?

**Sorunun yanıtı şu seçeneklerden biri de olabilir:**
+ Sentaks hatası *(syntax error)*
+ Tanımsız davranış *(undefined behavior)*
+ Derleyiciye göre değişir.* (implementation defined/specified)*

```c
#include<stdio.h>

int main(void)
{
	int i, k;
	
	for (i = 1, k = 1; k; printf("%d%d", i, k))
		k = i++ <= 3;	
}
```

#### Aşağıdaki C programı çalıştırıldığında bu programın çıktısı ne olur?

**Sorunun yanıtı şu seçeneklerden biri de olabilir:**

+ Sentaks hatası *(syntax error)*
+ Tanımsız davranış *(undefined behavior)*
+ Derleyiciye göre değişir. *(implementation defined/specified)*

```c
#include <stdio.h>

int main(void)
{
	int x = 1;

	while (x-- >= 1)
		while (x-- >= 0);
			printf("%d", x);
}
```

#### Kendisine gönderilen bir tamsayının 10‘luk sayı sisteminde Harshad sayısı olup olmadığını test eden _is_harshad_ isimli işlevi tanımlayınız.

```c
int is_harshad(int val);
```

İşleve gönderilen değer 10’luk sayı sisteminde bir `Harshad` sayısı ise işlev sıfır dışı bir değere değil ise işlev sıfır değerine geri döner.

**Tanımladığınız işlevi kullanarak ilk 100 Harshad sayısını standart çıkış akımına yazdıran bir C programı yazınız.**

#### Harshad sayısı nedir?

Eğlence matematiğinde `Harshad Sayı (veya Niven Sayı)` rakamları toplamına tam bölünebilen tamsayılara denir. Harshad özelliğini sağlayan sayma tabanına n dersek sayılar `n-Harshad (ya da n-Niven)` olarak da söylenirler. Hindistanlı matematikçi `D. R. Kaprekar` tarafından tanımlanmışlardır. `"Harshad"` kelimesi Sanskritçe harṣa (eğlence) + da (vermek), kelimelerinin bileşiminden *"eğlenceli"* anlamındadır. `“Niven Sayı”` tabiri ise `Ivan M. Niven` tarafından 1977 yılında sayma teorisi ile ilgili yayınlanmış olan makaleye dayandırılmıştır.

**Örnekler:**
18 sayısı 10 tabanında (sayma sisteminde) `Harshad` sayıdır. Çünkü rakamları olan 1 ve 8‘in toplamı 9‘dur (1+8=9), ve 18 sayısı 9‘a tam bölünür. (18/9=2 ve 2 bir tamsayıdır)

`1729` sayısı `10`'luk sayma sisteminde bir `Harshad` sayıdır çünkü rakamları toplamı olan `19`‘a tam bölünür 
`1729 = 19 * 91`

`19` sayısı 10'luk sayma sisteminde bir `Harshad` sayı değildir, çünkü rakamları toplamı 10‘dur (1+9=10) ve (19/10=1.9 ve 1.9 tam sayı olmadığından) `19 10`‘a tam bölünmez.

10'luk sayma sisteminde `Harshard` sayıları dizisi şöyledir:

`1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 18, 20, 21, 24, 27, 30, 36, 40, 42, 45, 48, 50, 54, 60, 63, 70, 72, 80, 81, 84, 90, 100, 102, 108, 110, 111, 112, 114, 117, 120, 126, 132, 133, 135, 140, 144, 150, 152, 153, 156, 162, 171, 180, 190, 192, 195, 198, 200...`

**`Kaynak : wikipedia`**

#### Aşağıdaki C programı derlenip çalıştırıldığında ekrana ne yazdırılır?

```c
#include <stdio.h>

#define  NECO    100
#define  ZERO    0
#define  NONO     


int main()
{
#if NECO
	printf("A");
#endif 

#if ZERO
	printf("B");
#endif 

#if YOKO
	printf("C");
#endif 

#ifdef NECO
	printf("D");
#endif 

#ifdef ZERO
	printf("E");
#endif 

#ifdef NONO
	printf("F");
#endif 

#ifdef YOKO
	printf("G");
#endif 

#ifndef NECO
	printf("H");
#endif 

#ifndef ZERO
	printf("I");
#endif 

#ifndef NONO
	printf("J");
#endif 

#ifndef YOKO
	printf("K");
#endif 

#if YOKO > -1
	printf("L");
#endif 

#if TOKO == YOKO
	printf("M");
#endif 

}
```

**Sorunun yanıtı şu seçeneklerden biri de olabilir:**
+ Sentaks hatası *(syntax error)*
+ Tanımsız davranış *(undefined behavior)*
+ Derleyiciye göre değişir.* (implementation defined/specified)*

#### Aşağıda belirtilen işlevsel makroları `(functional - function-like macros)` tanımlayınız:

+ standart *isupper* işlevinin yerine geçecek *is_upper* isimli makro

+ standart *toupper* işlevinin yerine geçecek *to_upper* isimli makro

+ 3 sayıdan en büyüğünü hesaplayan *max3* isimli makro

+ 4 sayıdan en büyüğünü hesaplayan *max4* isimli makro

+ `clamp` isimli makro:	*clamp(val, low, high)* ifadesinin değeri 
	+ `val <= low ise low`
	+ `val >= high ise high`
	+ `aksi halde val olmalı`

+ _is_triangle_ isimli makro: </br>
```
is_triangle(a, b, c)
```

ifadesinin değeri
+ eğer `a b c` kenar uzunlukları geçerli bir üçgen oluşturuyor ise _1_
+ eğer `a b c` kenar uzunlukları geçerli bir üçgen oluşturmuyor _0_ ise olmalı.
	
#### Aşağıdaki C programı derlenip çalıştırıldığında ekran çıktısı ne olur?

```c
#include <stdio.h>

#define  NEC	100

void func(void);

int main()
{
	func();
#ifdef  NEC
#undef  NEC
#endif

}

void func(void)
{
#if defined NEC
	printf("NEC = %d\n", NEC);
#else
	printf("NEC tanimsiz\n");
#endif
}
```

**Sorunun yanıtı şu seçeneklerden biri de olabilir:**
+ Sentaks hatası *(syntax error)*
+ Tanımsız davranış *(undefined behavior)*
+ Derleyiciye göre değişir. _(implementation defined/specified)_

#### Bu sorumuz koşullu derlemeye _(conditional compiling)_ yönelik. Aşağıdaki _C_ programı çalıştırıldığında ekran çıktısı ne olur?

```c
#include <stdio.h>

int main()
{
	int x =  -1;

#if x > -1
	printf("A");
#else
	printf("B");
#endif
}
```

__Sorunun yanıtı şu seçeneklerden biri de olabilir:__</br>
+ Sentaks hatası (derleme zamanı hatası)
+ Tanımsız davranış. _(undefined behavior)_
+ Derleyiciye göre değişir. _(unspecified behavior / implementation defined)_

#### Aşağıdaki _C_ programı çalıştırıldığında ekran çıktısı ne olur?

```c
#include <stdio.h>

#define SIZE	100
#define ROWSIZE	SIZE
#undef  SIZE
#define SIZE	76


int main(void)
{
	printf("%d\n", ROWSIZE);
}
```

__Sorunun yanıtı şu seçeneklerden biri de olabilir:__</br>
+ Sentaks hatası (derleme zamanı hatası)
+ Tanımsız davranış. _(undefined behavior)_
+ Derleyiciye göre değişir. _(unspecified behavior / implementation defined)_

#### Aşağıdaki C programı çalıştırıldığında bu programın çıktısı ne olur?

**Sorunun yanıtı şu seçeneklerden biri de olabilir:**
+ Sentaks hatası _(syntax error)_
+ Tanımsız davranış *(undefined behavior)*
+ Derleyiciye göre değişir. *(implementation defined/specified)*

```c
#include <stdio.h>

int g = 34;

int main()
{
	unsigned int n = sizeof g++ - sizeof ++g + g++;
	printf("%u\n", n);
}
```

#### Aşağıdaki C programı çalıştırıldığında bu programın çıktısı ne olur?

```
#include <stdio.h>

int main()
{
	int x = 3;
	int y = 5;
	int z = x + sizeof(++x) - sizeof(++y);

	printf("%d\n", x + y + z);

	return 0;
}
```
+ Sorunun yanıtı şu seçeneklerden biri de olabilir:
+ Sentaks hatası (derleme zamanı hatası)
+ Tanımsız davranış. _(undefined behavior)_
+ Derleyiciye göre değişir. _(unspecified behavior / implementation defined)_

_T_ bir tür olmak üzere

```
sizeof(T)
```

ifadesi ile aynı değeri üretecek _sizeof_ işlecini _(operatörünü)_ kullanmayan bir ifade oluşturun:

+ Oluşturduğunuz ifadenin türü _size_t_ olmalı
+ Oluşturduğunuz ifade tanımsız davranış _(undefined behavior)_ oluşturmamalı.

#### Aşağıdaki programın ekran çıktısı ne olur?

```c
#include<stdio.h>

#define asize(a)	(sizeof(a) / sizeof(*a))

int a[] = {1, 2, 3, 4, 5};

int main()
{
	for (int k = -1; k <= asize(a) - 2; ++k)
		printf("%d\n", a[k + 1]);
}
```

__Sorunun yanıtı şu seçeneklerden biri de olabilir:__</br>
+ Sentaks hatası (derleme zamanı hatası)
+ Tanımsız davranış. _(undefined behavior)_
+ Derleyiciye göre değişir. _(unspecified behavior / implementation defined)_

#### Bir tamsayı dizisi içinde en çok tekrar eden değeri (mod) hesaplayarak ekrana yazdıran bir C kodu yazınız. 
Bu nitelikte birden fazla öğe varsa dizide ilk geçen değer bulunacak. Ekran çıktısı şu şekilde olmalı:

`4 7 6 7 3 2 9 7 4 9 7 1`

**mod = _7_ ve _4_ kez tekrar ediyor**

`3 4 8 4 9 4 6 7 3 2 2 2` 

**mod = `4` ve `3` kez tekrar ediyor**

#### Aşağıdaki test kodunu kullanabilirsiniz:

```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define     SIZE      1000

int main(void)
{

	int a[SIZE];

	srand((unsigned)time(0));

	for (int i = 0; i < SIZE; ++i) {
		a[i] = rand() % 500;
		if (i && i % 20 == 0)
			printf("\n");
		printf("%3d ", a[i]);
	}
	///kod
}
```

İlk kez __Edsger Dijkstra__ tarafından sorulan bu algoritmaya 3 renkten oluşması nedeniyle `Hollanda Bayrağı Algoritması` deniyor. Yalnızca 0, 1, 2 değerlerinden oluşan bir diziniz var:

```
int a[] = {1, 2, 2, 0, 1, 0, 1, 0, 0, 1, 1, 2, 1, 0, 1, 2, 0, 0, 1, 0};
```

#### Bu diziyi `O(n)` karmaşıklığında bir algoritma ile sıralamanız gerekiyor. Aşağıdaki test kodunu kullanabilirsiniz:

```c
#include <stdio.h>

int main(void)
{
	int a[] = { 1, 2, 2, 0, 1, 0, 1, 0, 0, 1, 1, 2, 1, 0, 1, 2, 0, 0, 1, 0 };

	/*
		kodunuz
	*/

	for (size_t i = 0; i < sizeof(a) / sizeof(*a); ++i)
		printf("%d", a[i]);

	//00000000111111112222
}
```

#### Bir dizinin öğelerinin ardışık _(consecutive)_ tamsayılardan oluşup oluşmadığını sınayan bir C kodu yazınız:

```
int a1[] = {74, 70, 73, 71, 83, 77, 84, 81, 82, 78, 86, 72, 79, 88, 76, 87, 75, 89, 80, 85}; //evet
int a2[] = {43, 44, 48, 40, 50, 47, 45, 42, 52, 49, 54, 46, 51, 41, 53}; //evet
int a3[] = {9, 0, 7, 6, 8, 5, 4, 3, 2, 7}; //hayir
```

+ Problemi ilave bir dizi kullanarak ve ilave bir dizi kullanmadan ayrı ayrı çözmeye çalışın.
+ Her iki algoritmanın karmaşıklığını _big O_ notasyonu ile belirtin.

#### _Partisyon_ (bölümleme) işlemi bir veri yapısını, bir koşulu sağlayanlar ve sağlamayanlar olarak ikiye ayırma işlemidir.
Bu iş *O(n)* karmaşıklığında bir algoritma ile gerçekleştirilebilir. Öğeleri *int* türden olan bir diziyi tekler başta çiftler sonda olmak üzere ikiye ayırınız:

```c
#include <stdio.h>

#define     SIZE  100

int main(void)
{
	int a[SIZE] = {
	1, 320, 552,   3, 989, 899, 604, 291, 279, 513, 800, 137, 857, 908,  71, 929, 272,  10, 643, 674,
	972,  58, 111, 430, 806, 834, 991, 351, 970, 212, 724, 840, 357, 147, 116, 514, 824, 865, 753, 702,
	334, 874, 176, 811, 250, 526, 214,  48, 757, 810, 438, 428, 359,  81,  38, 812, 891, 434, 595, 509,
	176, 530, 665, 179, 188, 739, 272, 513, 492,  68, 211, 490, 810, 171, 682, 983, 343, 560, 179,  89,
	761, 956, 717, 546, 350, 811, 197,  47, 905, 693, 789, 497,  20, 387,  81, 501, 223, 104, 955, 688, };

	//kod buraya yazilacak

	for (int i = 0; i < SIZE; ++i) {
		if (i && i % 20 == 0)
			printf("\n");
		printf("%3d ", a[i]);
	}
}
```

#### Küçükten büyüğe sıralanmış, her öğesi birbirinden farklı _(distinct)_ olan negatif bir tamsayı içermeyen bir tamsayı dizisi var. Bu dizide yer almayan en küçük tamsayıyı bulunuz. Örnekler:

```
girdi : 0 1 2 3 5 8 12
çıktı : 4

girdi : 1 3 4 5 6 7 20
çıktı : 0

girdi : 0 1 2 3 4
çıktı : 5
```

#### Aşağıdaki test kodunu kullanabilirsiniz:

```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define   SIZE      100

int icmp(const void *vp1, const void *vp2)
{
	return *(const int *)vp1 > *(const int *)vp2 ? 1  :
         *(const int *)vp1 < *(const int *)vp2 ? -1 : 0;
}

int main(void)
{
	int a[SIZE];

	srand((unsigned)time(NULL));


	for (int i = 0, idx = 0; idx < SIZE; ++i) {
		if (rand() % (SIZE / 4) != 0)
			a[idx++] = i;
	}

	for (int i = 0; i < SIZE; ++i) {
		if (i != 0 && i % 20 == 0)
			printf("\n");
		printf("%3d ", a[i]);
	}
	printf("\n\n");

	//kodu buraya yazin
}
```

#### _n_ elemanlı bir dizi var. Bu dizide *1 – n* arasında tüm değerler yer alıyor. Ancak bir değerden *2* tane var. Yinelenen değeri bulan bir C kodu yazınız:

Örnek:

```c
n = 10
int a[10] = {9, 8, 1, 3, 4, 2, 7, 8, 5, 6};
Yinelenen değer 8
```

#### Yazdığınız kodu aşağıdaki kod ile test edebilirsiniz:

```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define   SIZE      100

int main(void)
{
	int a[SIZE];
	
	srand((unsigned)time(NULL));
	int val = rand() % (SIZE - 1) + 1;
	a[0] = val;

	for (int i = 1; i < SIZE; ++i) {
		a[i] = i;
	}

	for (int i = 0; i < 5 * SIZE; ++i) {
		int idx1 = rand() % SIZE;
		int idx2 = rand() % SIZE;
		if (idx1 != idx2) {
			int temp = a[idx1];
			a[idx1] = a[idx2];
			a[idx2] = temp;
		}
	}

	for (int i = 0; i < SIZE; ++i) {
		if (i % 20 == 0)
			printf("\n");
		printf("%3d ", a[i]);
	}

	printf("\ntekrar eden sayi : %d\n", val);

	//a dizisi icinde tekrar eden sayiyi bulacak kodu buraya yazınız:

}
```

#### Aşağıdaki C programı çalıştırıldığında bu programın çıktısı ne olur?

**Sorunun yanıtı şu seçeneklerden biri de olabilir:**
+ Sentaks hatası _(syntax error)_
+ Tanımsız davranış _(undefined behavior)_
+ Derleyiciye göre değişir. _(implementation defined/specified)_

```c
#include <stdio.h>

int main(void)
{
	int a[] = { 0, 1, 2, 3};

	printf("%d\n", (a[0], a[0, 1], a[0, 1, 2], a[0, 1, 2, 3]));
}
```

#### Bir tamsayı dizisinde eşsiz _(unique)_ olan değerleri standart çıkış akımına yazdırın. 
Aşağıda sizin için bir test kodu var:

```c
#include <time.h>
#include <stdlib.h>
#include <stdio.h>

#define  SIZE 20

int main(void)
{
	int a[SIZE];
	
	srand((unsigned)time(NULL));

	for (int i = 0; i < SIZE; ++i) {
		a[i] = rand() % SIZE;
		printf("%d ", a[i]);
	}
	
	printf("\n");

	/*
		sizin kodunuz
	*/
}
```

Yukarıdaki kodda, _a_ dizisinin öğelerine rastgele değerler yerleştiriliyor ve bu dizinin öğeleri standart _printf_ işlevi ile kullanıcı ekranına yazdırılıyor. Dizi öğeleri aşağıdaki gibi olsun:

```
16 7 7 6 6 13 16 19 6 15 5 2 11 7 5 13 5 9 6 13
```

Bu durumda yazdığınız kod çalıştırıldığında ekrana şu değerleri yazmalı:

```
19 15 2 11 9
```

Kodunuzda ikinci bir dizi tanımlanmamalı.

Aşağıdaki kodda __SIZE__ tane öğeye sahip bir tamsayı dizisine rastgele değerler veriliyor:

```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define			SIZE		20

int main(void)
{
	int a[SIZE];

	srand((unsigned)time(0));
	for (int i = 0; i < 20; ++i) {
		a[i] = rand() % 20 + 1;
		printf("%d ", a[i]);
	}
	printf("\n");
}
```

Bu dizinin elemanlarının değerlerini kullanarak bir histogram oluşturacak C programını yazmanız isteniyor. Örnek bir ekran çıktısı aşağıdaki gibi olmalı:<br>

![image](https://github.com/necatiergin/c_kursu_odevleri/blob/master/resimler/histogram.JPG)

İçinde en az bir tane negatif tamsayı olan bir tam sayı dizisi var. Bu dizinin tüm ardışık alt dizileri içinde en büyük kümülatif toplam değerini (maximum subsequence) bulmamız gerekiyor:

Örneğin

```
3  4 -8  1  7 -2
```

dizisinde en büyük toplam değerini veren alt dizi 

```
1 7
```

ve hesaplanacak toplam değeri : 

```
8
```

Aşağıda tanımlanan a dizisinin en büyük alt dizi toplamını hesaplayan bir C programı yazınız:

```c
#define			SIZE		100

int a[SIZE] = {
		-258, 225, -350, 323, 6, 829, 804, 732, -346, 289,
		-793, -588, 665, -681, 154, 274, -43, 877, -977, -23,
		530, 385, -514, 154, -373, 62, 790, -174, 184, 375,
		-171, 519, -354, -237, 482, -697, 717, -532, -752, 217,
		-89, -908, -382, 617, -122, 584, 617, -664, -566, 18,
		138, -496, -552, 829, 191, -478, -48, -122, 440, -686,
		256, 372, -987, 36, -872, 171, -953, 500, -603, 613,
		311, -267, -616, -384, -574, -771, -482, -881, -747, 356,
		584, 33, -135, -717, -326, 530, -328, -767, -50, 846,
		894, -499, 48, -265, -327, 574, 670, -642, -932, 84,
	};
}
```

* Kodda ikinci bir dizi kullanmayacaksınız.
* Oluşturduğuz algoritma O(n) karmaşıklığında olmalı

#### Kendisine gün, ay ve yıl olarak gönderilen tarihin yılın kaçıncı günü olduğunu hesaplayan _day_of_year_ isimli işlevi tanımlayın:

```c
int day_of_year(int day, int mon, int year);
```

+ İşlevin geri dönüş değeri _day/month/year_ tarihinin year yılının kaçıncı günü olduğu bilgisi.
+ Artık yılları _(leap years)_ göz önüne almayı unutmayınız.

#### Kendisine gönderien tamsayıdan daha küçük ilk asal sayıyı bulan closest_prime isimli işlevi tanımlayınız:

```
int closest_prime(int value);
```

+ İşlevin geri dönüş değeri value değerinden küçük en büyük asal sayı olacaktır.
+ Eğer böyle bir asal sayı yok ise işlev hata değeri olarak `-1` değerini döndürür.

#### Aşağıdaki C programı çalıştırıldığında bu programın çıktısı ne olur?

**Sorunun yanıtı şu seçeneklerden biri de olabilir:**
+ Sentaks hatası *(syntax error)*
+ Tanımsız davranış *(undefined behavior)*
+ Derleyiciye göre değişir. *(implementation defined/specified)*

```c
#include <stdio.h>

int main(void)
{
	int n = 3;
	int i = 0;

	switch (n % 2) {
	case 0:
	do {
			++i;
	case 1: ++i;
	} while (--n > 0);}

	printf("%d\n", i);
}
```

#### Aşağıdaki C programı çalıştırıldığında bu programın çıktısı ne olur?

```c
#include<stdio.h>

int main(void)
{
	int x = 1;
	switch (x)
	{
	case '1': printf("1\n"); break;
	case '2': printf("2\n"); break;
	defualt : printf("0\n");
	}
}
```
__Sorunun yanıtı şu seçeneklerden biri de olabilir:__</br>
+ Sentaks hatası (derleme zamanı hatası)
+ Tanımsız davranış. _(undefined behavior)_
+ Derleyiciye göre değişir. _(unspecified behavior / implementation defined)_

#### Standart _rand_ işlevine çağrı yaparak değeri rastgele olarak aşağıdaki sayılardan biri olacak bir ifade yazınız.

```
7 11 15 19
```

#### Yazdığınız ifadeyi aşağıdaki kodla test edebilirsiniz:

```c
#include <stdio.h>

int main(void)
{
	//EXP yerine ifadenizi yaziniz
	for (;;) {
		printf("%d\n", EXP);
		getchar();
	}
}
```

#### 	Aşağıdaki deyimlerin C dilinde geçerli olup olmadığını yazınız. 	Her bir sentaks hatasının nedenini açıklayınız:

```c
int main(void)
{
	int x = 10;
	int y = 10;
	int* p = &x;
	int* q = &y;

	&x = &y;
	x = *p;
	*p = *q;
	p = &y;
	p = q;
	&x++;
	++* p;
	&++x;
	&y = p;
}
```

#### Aşağıdaki deyimlerin C dilinde geçerli olup olmadığını yazınız. Her bir sentaks hatasının nedenini açıklayınız:

```c
int main(void)
{
	int a[] = { 1, 3, 5 };
	int b[] = { 2, 4, 6 };
	int* p = a;

	a = b;
	++a;
	p = b;
	*p = *a;
	*a = *b;
	++* a;
	++* p;
	(*p)++;
	a = p;
}
```

