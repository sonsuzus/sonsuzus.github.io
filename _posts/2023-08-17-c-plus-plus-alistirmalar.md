---
title:  C++ Alıştırmalar
author: sonsuz
date: 2023-08-17 19:20:15 +0300
categories: [Program,C++]
tags: [cpp,programlama,alıştırma,algoritma]
---


#### Aşağıdaki kaynak koddaki her bir sentaks hatasını

+ C dilinin kurallarına göre
+ C++ dilinin kurallarına 

#### belirleyiniz. Her bir sentaks hatasının nedenini açıklayınız:

```c
#include <stdlib.h>

enum Color {Blue, Red, Yellow};
enum Fruit { Apple, Melon, Mango};

foo(int, int);
int func();

double sum(a, b)
double a, b;
{
	return a + b;
}

int f(int x, int)
{
	return x * x;
}

int g1 = func();
const int g2;

int main()
{
	const int ci1;
	const int ci2 = func();
	const c3 = 123;
	char *p1 = "necati";
	int i1 = 12.5;
	int i2 = Red;

	enum Color color1 = 2;
	enum Color color2 = 19;
	enum Color color3 = Mango;
  
	char str[3] = "ali";
	enum Color color = Red;
	++color;
	Fruit f = Mango;
	const int cx = 10;
	int ival = 56;
	func(ival);
	int *ptr = &cx;
	char *cptr = &ival;
	const int *p2 = &ival;
	int *p3 = malloc(10 * sizeof(int));
	int *p4 = 0;
	int *p5 = NULL;
}
```

#### Aşağıdaki kod hakkında yorum yapmanız isteniyor:

```c
#include <stdio.h>

int nec = 0;

int main()
{
	struct nec {
		char str[64];
	};
	printf("sizeof(nec) = %zu\n", sizeof(nec));
}

```

#### Bu kod C dilinin kurallarına göre derlenirse ne olur? C++ dilinin kurallarına göre derlenirse ne olur? Açıklayınız.

#### C dili tekrarı için sorulmaktadır:

Aşağıdaki kodda C ve C++ dillerinin kurallarına göre sentaks hatası oluşturan deyimleri *(statements)* işaretleyiniz ve sentaks hatalarının nedenlerini açıklayınız. Her bir gösterici *(pointer)* değişkeni niteleyen ingilizce terimleri yazınız. Soruya bir derleyici, *IDE* ya da yardımcı bira araç kullanmadan yanıt veriniz.

```c
int main()
{
	int x = 10;
	int y = 20;
	
	int * const p1 = &x;
	const int *p2 = &x;
	int const *p3 = &x;
	const int* const p4 = &x;

	*p1 = 40;
	p1 = &y;

	*p2 = 40;
	p2 = &y;

	*p3 = 40;
	p3 = &y;
	
	*p4 = 40;
	p4 = &y;
}
```

#### C dili tekrarı için sorulmaktadır:

Aşağıdaki kodda C ve C++ dillerinin kurallarına göre sentaks hatası oluşturan deyimleri *(statements)* işaretleyiniz ve sentaks hatalarının nedenlerini açıklayınız. Her bir gösterici *(pointer)* değişkeni niteleyen ingilizce terimleri yazınız. Soruya bir derleyici, *IDE* ya da yardımcı bira araç kullanmadan yanıt veriniz.

```c
int main()
{
	int x = 10;
	int y = 20;
	
	int * const p1 = &x;
	const int *p2 = &x;
	int const *p3 = &x;
	const int* const p4 = &x;

	*p1 = 40;
	p1 = &y;

	*p2 = 40;
	p2 = &y;

	*p3 = 40;
	p3 = &y;
	
	*p4 = 40;
	p4 = &y;
}
```

Aşağıdaki kaynak kod

+ C dilinin kurallarına göre derlenip çalıştırıldığında ne olur?
+ C++ dilinin kurallarına göre derlenip çalıştırıldığında ne olur?
+ **#include <stdbool.h>** Önişlemci komutu koda eklenerek C dilinin kurallarına göre derlenip çalıştırıldığında ne olur?
   
```c
#include <stdio.h>

int main()
{
#if true
	printf("dogru\n");
#else
	printf("yanlis\n");
#endif

}
```

#### Aşağıdaki C++ programı derlenip çalıştırıldığında standart çıkış akımına ne yazar?

```c++
int foo(int *p, int *q)
{
	*p = 1;
	*q = 2;
	
	return *p + *q;
}

char str[] = "0123";

#include <iostream>

int main()
{
	using namespace std;

	int a = 3;
	int b = 4;
	int c = foo(&a, &a);
	cout << c;
	(c == a + b ? a : b) = 5;
	cout << a << b;
	int i = 0;
	str[i] = i[str + 2];
	cout << str;
	
} 
```

#### Aşağıdaki C++ programı hakkında yorum yapınız:

+ sentaks hatası
+ tanımsız davranış
+ derleyiciye göre değişir
+ ekrana şunu yazar: 

```c++
#include <iostream> 

typedef long long mylong;

void func(unsigned myllong) 
{
	std::cout << '1';
}

void func(unsigned long long) 
{
	std::cout << '2';
}

int main() 
{
	func(0ULL);
}
```

#### Aşağıdaki kodda yapılan referans tanımlamalarından geçersiz olanları işaretleyin ve geçersizlik nedenlerini açıklayın:

```c++
int &f1();
int f2();

int main()
{
	int x = 10;
	int y = 35;
	const int primes[]{ 2, 3, 5, 7, 11, 13, 17, 19, 23, 29 };
	int a[]{ 1, 2, 4 };
	int &r1;
	int &r2(++x);
	int &r3{ 10 };
	const int &r4{ int() };
	const int &r5{ int{} };
	int &r6 = +y;
	int &r7 = (x, y);
	int &r8 = x > 10 ? x : y;
	int &r9 = f1();
	int &r10 = f2();
	int &r11 = primes[5];
	int const &r12 = *primes;
	const int &r13{ x };
	int *&r14 = a;
	int(&r15)[] = a;
	int(&r16)[3] = a;
}
```

#### Aşağıdaki C++ programı hakkında yorum yapınız:

+ sentaks hatası
+ tanımsız davranış
+ derleyiciye göre değişir
+ ekrana şunu yazar: 

```c++
#include <iostream>

int foo(int &x, int &y) 
{
	x = 3;
	y = 4;
	return x + y;
}

int main() 
{
	int x = 1;
	int y = 2;
	int z = foo(x, x);

	std::cout << x << y << z;
}

```

#### Aşağıdaki C++ programı hakkında yorum yapınız:

+ sentaks hatası
+ tanımsız davranış
+ derleyiciye göre değişir
+ ekrana şunu yazar: 

```c++
#include <iostream>

int main() 
{
	int ival = 1;
	const int &r = ival > 0 ? ival : 1;
	ival = 5;
	std::cout << ival << r;
}
```

#### Aşağıdaki C++ programı hakkında yorum yapınız:

+ sentaks hatası
+ tanımsız davranış
+ derleyiciye göre değişir
+ ekrana şunu yazar: 

```c++
#include<iostream>

void func(int& ra, const int& rb) 
{
	std::cout << rb;
	ra = 1;
	std::cout << rb;
}

int main() 
{
	int ival = 0;

	func(ival, ival);
}

```

#### Aşağıdaki C++ programı hakkında yorum yapınız:

+ sentaks hatası
+ tanımsız davranış
+ derleyiciye göre değişir
+ ekrana şunu yazar: 

```c++
#include <iostream>

int main()
{
	int x{ 1 }, y{ };

	const int &r1 = x > 0 ? x : y++;
	const int &r2 = x > 0 ? x : ++y;
	x = 5;
	std::cout << r1 << r2;
}

```

##### Aşağıdaki her bir kod hakkında yorum yapınız:

```c++
int &func(int x)
{
	return x;
}

int main()
{
	int y = 20;
	func(y) = 50;
}
```

```c++
#include <iostream>

int main()
{
	const int x = 20;
	auto y = x;
	++y;

	std::cout << y << " " << x << "\n";

}
```

```c++
include <iostream>

int main()
{
	int x = 10;
	int &r1 = x;
	auto r2 = x;
	auto &r3 = r2;

	r2 += 5;
	r3 += 20;
	++x;

	std::cout << r1 + r2 + r3 << "\n";
}
```

```c++
int main()
{
	int x = 10;
	const int &cr = x;
	auto &r = cr;

	++r;
}
```

```c++
#include <iostream>

int main()
{
	int a[] = { 0, 1, 2, 3, 4, 5 };
	auto r1 = a;
	auto &r2 = a;

	++r2[3];
	std::cout << (r1[3] == r2[3]) << "\n";
}
```

```c++
#include <iostream>

int main()
{
	int a[] = { 10, 20, 30, 40 };
	auto p = a;
	auto &r = p;
	++r;
	++p;

	std::cout << *r << "\n";
}
```

```c++
#include <iostream>

int &func(int &r)
{
	++r;
	return r;
}

int main()
{
	int x = 10;
	auto f = func;
	auto y = f(x);
	auto &r = f(x);
	r += 400;
	y += 50;

	std::cout << "x = " << x << "\n";

}
```

```c++
#include <iostream>

int main()
{
	int x = 10;
	int *ptr = &x;

	auto r1 = x;
	auto r2 = *ptr;
	auto r3 = r2;
	auto &r4 = ptr;
	auto &r5 = *ptr;

	r1 += 3;
	r2 += 13;
	r3 += 20;
	*r4 += r2;
	++r5;

	std::cout << "x = " << x << "\n";

}
```

#### Sentaks hatası olan satırları belirtiniz:

```c++

auto a;
int &b;
auto c = 10;
int &d = c;
const auto &e = 20;
int &f = ++c;
int &g = c + 5;
int &&h = c % 2;
int func(); int &&j = func();
int &foo(); int &&m = foo();
int ival = 10; int &&rval = ival + 10; int &p = rval;

```

#### Aşağıdaki kodlarda (varsa) sentaks hatalarını işaretleyiniz ve sentaks hatalarının nedenlerini belirtiniz:

```c++
void f1()
{
	const int x = 10;
	auto a = x;
	auto &b = x;
	decltype(x) c = 0;

	++a;
	++b;
	++c;
}


void f2()
{
	int x = 10;
	int y = 20;
	const int *p = &x;
	int *const cp = &x;

	auto a = p;
	auto b = cp;

	a = &y;
	*a = 20;
	b = &y;
	*b = 56;
}


void f3()
{
	int x = 10;
	int *p = &x;
	int **pp = &p;

	decltype(p) a;
	decltype(*p) b;
	decltype(+*p) c;
	decltype(pp) d;
	decltype(*pp) e;
	decltype(**pp) f;
}

void f4()
{
	int arr[]{ 1, 2, 3, 4 };
	decltype(arr)a;
	auto b{ arr };
	auto &c{ arr };

	++a;
	++b;
	++c;
	++*a;
	++*b;
	++*c;
}

void f5()
{
	auto x = 10;
	auto y = &x;
	auto z = &y;

	y = *z;
	x = **z;
	y = 0;
	z = 0;	
}

void f6()
{
	const int x = 10;
	const int &r = x;
	auto a = r;
	decltype(a) b;
	++a;
	++b;
	decltype(*&x) c;
}
```

#### Aşağıdaki C++ programı hakkında yorum yapınız:

+ sentaks hatası
+ tanımsız davranış
+ derleyiciye göre değişir
+ ekrana şunu yazar: 

```c++
#include <iostream>

int main()
{
	int x = 5;
	decltype((x)) y{ x };
	decltype(y *= 2) z = x;
	decltype(y--) t = x;
	int &rx{ x };
	auto ax{ rx };

	++y;
	z *= 2;
	t *= 5;
	ax += 10;

	std::cout << "x = " << x << "\n";
}
```

```c++
#include <iostream>

int main()
{
	int x = 10;
	int *ptr = &x;

	auto r1 = x;
	auto r2 = *ptr;
	auto r3 = r2;
	auto &r4 = ptr;
	auto &r5 = *ptr;

	r1 += 3;
	r2 += 13;
	r3 += 20;
	*r4 += r2;
	++r5;

	std::cout << "x = " << x << "\n";

}
```

#### Aşağıdaki C++ programı hakkında yorum yapınız

+ sentaks hatası var ise, hatayı ve hatanın nedenini belirtiniz.
+ tanımsız davranış var ise nedenini belirtiniz.
+ standart çıkış akımına ne yazdırılacağını belirtiniz.

```c++
#include <iostream>

int main()
{
	const int x = 20;
	auto y = x;
	++y;

	std::cout << y << " " << x << "\n";
}
```

#### Aşağıdaki C++ programı hakkında yorum yapınız:

+ sentaks hatası
+ tanımsız davranış
+ derleyiciye göre değişir
+ ekrana şunu yazar: 

```c++
#include <iostream>

int main()
{
	int a[] = { 10, 20, 30, 40 };
	auto p = a;
	auto &r = p;
	++r;
	++p;

	std::cout << *r << "\n";
	
}
```

#### Aşağıdaki C++ programı hakkında yorum yapınız

+ sentaks hatası var ise, hatayı ve hatanın nedenini belirtiniz.
+ tanımsız davranış var ise nedenini belirtiniz.
+ standart çıkış akımına ne yazdırılacağını belirtiniz.

```c++
#include <iostream>

int main()
{
	int x = 10;
	const int &cr = x;
	auto &r = cr;
	++r;

	std::cout << "x = " << x << "\n";
}
```

#### Aşağıdaki bildirimlerden sentaks hatası içerenleri işaretleyiniz. Sentaks hatasının nedenini açıklayınız:

```c++
void f1(int, int = 10, int);
```

```c++
void f2(const char *= "error");
```

```c++
int g{};
void f3(int &r = g);
```

```c++
void f4(int x = 10, int y = x);
```

```c++
void f5(int, int, int = 10);
void f5(int, int, int = 10);
```

```c++
int f6(int x = 10, int y = 20)
{
	return x * x + y - 5;
}
```

```c++
int f7(int, int, int);
int f7(int, int, int = 10);
int f7(int, int = 20, int);
```

```c++
int f8(int = 0);
int f9(int = f8());
int f10(int = f9());
```

```c++
int f11(int = 1);

int f11(int x = 1)
{
	return x + 5;
}
```

#### Aşağıdaki programın çıktısı ne olur? Açıklayınız:

```c++
#include <iostream>

int foo()
{
	static int x{};
	
	return ++x;
}

void func(int i = foo())
{
	std::cout << i;
}

int main()
{
	func();
	func();
	func();
}
```

#### C++17 standartlarına göre aşağıdaki C++ programı çalıştırıldığında bu programın çıktısı ne olur?

```c++
#include <iostream>
 
void f(int) 
{
	std::cout << "int";
}
 
void f(long)
{
	std::cout << "long";
}
 
void f(double)
{ 
	std::cout << "double";
}
 
int main()
{
	f(sizeof(int));
 
	return 0;
}
```

__Sorunun yanıtı şu seçeneklerden biri de olabilir:__

+ Sentaks hatası *(syntax error)*
+ Tanımsız davranış *(undefined behavior)*
+ Derleyiciye göre değişir *(implementation defined)*

#### C++17 standartlarına göre aşağıdaki C++ programı çalıştırıldığında bu programın çıktısı ne olur?

```c++
#include <iostream>
 
void func(char* &) { std::cout << 'A'; }
void func(char* &&) { std::cout << 'B'; }
 
int main()
{
	char c{ 'c' };
	func(&c);
}
```

__Sorunun yanıtı şu seçeneklerden biri de olabilir:__

+ Sentaks hatası *(syntax error)*
+ Tanımsız davranış *(undefined behavior)*
+ Derleyiciye göre değişir *(implementation defined)*

#### Aşağıdaki kodların her biri için şu soruya yanıt vermeniz gerekiyor:

+ Sentaks hatası var mı?
+ İşlev yüklemesi var mı?

```c++
class A {
public:
	void func(int);
private:
	void func(int);
};
```

```c++
class B {
public:
	void func(int, int);
private:
	void func(int);
};
```

```c++
class C {
public:
	void func(int);
};

void func(C *ptr, int);
```

```c++
class D {
public:
	void func(int) = delete;
	void func(unsigned int) = delete;
	void func(double) = delete;
};
```

```c++
class E {
public:
	void func()const;
	void func();
};
```

```c++
class F {
public:
	F& func();
	const F& func();
};
```

```c++
class A;
class B;

class G {
public:
	void func(A);
	void func(B);
};
```

#### Aşağıdaki C++ programı hakkında yorum yapınız:

+ sentaks hatası
+ tanımsız davranış
+ derleyiciye göre değişir
+ ekrana şunu yazar: 

```c++
#include <iostream>
#include <string>

void f(const std::string &) { std::cout << 1; }
void f(const void *) { std::cout << 2; }
void f(int = 0, ...) { std::cout << 3; }

int main() 
{
	f("necati");
	const char *pstr = "bar";
	f(pstr);
}
```

#### Aşağıdaki kodda yapılan işlev çağrılarının durumunu belirtin. Geçerli mi değil mi? Geçerli ise çağrılan işlev hangisidir?

```c++
void func(int);  	//1
void func(double); 	//2
void func(long);  	//3
void func(bool); 	//4

void foo()
{
	int x = 10;

	func('A');
	func(2.3F);
	func(4u);
	func(10 > 5);
	func(&x);
	func(nullptr);
}
```

#### Aşağıdaki kodda yapılan işlev çağrılarının durumunu belirtin. Geçerli mi değil mi? Geçerli ise çağrılan işlev hangisidir?

```c++
void func(void *);  //1
void func(bool); //2

void foo()
{
	double x = 1.0;

	func(0);
	func(nullptr);
	func(&x);
	func(x);
}
```

#### C++17 standartlarına göre aşağıdaki C++ programı çalıştırıldığında bu programın çıktısı ne olur?

```c++
#include <iostream>
 
void func(int)
{
	std::cout << "int";
}
 
void func(float)
{
	std::cout << "float";
}
 
 
int main()
{
	func(2.5);
}
```

__Sorunun yanıtı şu seçeneklerden biri de olabilir:__

+ Sentaks hatası *(syntax error)*
+ Tanımsız davranış *(undefined behavior)*
+ Derleyiciye göre değişir *(implementation defined)*

#### Aşağıdaki kodda yapılan işlev çağrılarının durumunu belirtin. Geçerli mi değil mi? Geçerli ise çağrılan işlev hangisidir?

```c++
void func(char *p);  //1
void func(const char *p); //2

void foo()
{
	char str[] = "Herb Sutter";
	const char cstr[] = "Stephan Lavavej";
	char *const p1 = str;
	const char *p2 = str;
	func(nullptr);
	func("Bjarne Stroustrup");
	func(str);
	func(cstr);
	func(p1);
	func(p2);
}
```

#### Aşağıdaki kodda yapılan işlev çağrılarının durumunu belirtin. Geçerli mi değil mi? Geçerli ise çağrılan işlev hangisidir?

```c++
enum Color {Blue, Green, Red};

void func(Color);
void func(unsigned int);

void foo()
{
	func(12);
}
```

#### Aşağıdaki kodda yapılan işlev çağrılarının durumunu belirtin. Geçerli mi değil mi? Geçerli ise çağrılan işlev hangisidir?

```c++
void func(int &);
void func(int &&);
void func(const int &);

int f1();
int& f2();

void foo()
{
	int x = 10;
	const int cx = 20;

	func(x);
	func(cx);
	func(x + 5);
	func(f1());
	func(f2());
}
```

#### Aşağıdaki kodlardan herbirinde function overloading ("işlev yüklemesi") olup olmadığını belirtin. Her bir kod için açıklama yapın:

```c++
void func(int);

void foo()
{
	extern func(int, int);
}
```

```c++
int func(double);
double func(double);
```

```c++
int f(double);
int f(double = 0.);
```

```c++
int g(int);
int g(const int);
```

```c++
int g(int *p);
int g(int* const p);
```

```c++
int f(int *p);
int f(const int *p);
```

```c++
void func(int &);
void func(const int &);
```

```c++
void g(int);
void g(int &);
```

```c++
void foo(int &);
void foo(int &&);
```

```c++
void f(const double &);
void f(double &&);
```

```c++
typedef int Word;

void f(Word);
void f(int);
```

```c++
enum Color {gray, red, blue};
void g(Color);
void g(int);
```

```c++
#include <cstdint>

void func(int32_t);
void func(int);
```

```c++
int f(bool);
int f(int);
```

```c++
void foo(char16_t);
void foo(int);
```

```c++
void func(char);
void func(signed char);
```

```c++
void f(char);
void f(unsigned char);
```

```c++
void foo(int(*)(int));
void foo(int(&)(int));
```

```c++
void g(int[10]);
void g(int *p);
```

```c++
void foo(int(&)[10]);
void foo(int(&)[20]);
```

#### C++17 standartlarına göre aşağıdaki C++ programı çalıştırıldığında bu programın çıktısı ne olur? Her bir fonksiyon çağrısı için ayrı cevap verilecek

```c++
#include <iostream>
 
void display(char const *ptr)
{
	std::cout << ptr;
}
 
void display(unsigned int uval)
{
	std::cout << uval;
}
 
int main()
{
	display("abc");
	display(0);
	display('A');
}
```

__Sorunun yanıtı şu seçeneklerden biri de olabilir:__

+ Sentaks hatası *(syntax error)*
+ Tanımsız davranış *(undefined behavior)*
+ Derleyiciye göre değişir *(implementation defined)*



#### C++17 standartlarına göre aşağıdaki C++ programı çalıştırıldığında bu programın çıktısı ne olur?

```c++
#include <iostream>
 
void f(int) 
{
	std::cout << "int";
}
 
void f(long)
{
	std::cout << "long";
}
 
void f(double)
{ 
	std::cout << "double";
}
 
int main()
{
	f(sizeof(int));
 
	return 0;
}
```

__Sorunun yanıtı şu seçeneklerden biri de olabilir:__

+ Sentaks hatası *(syntax error)*
+ Tanımsız davranış *(undefined behavior)*
+ Derleyiciye göre değişir *(implementation defined)*



#### Aşağıdaki sınıf tanımlamalarında (varsa) sentaks hatalarını belirtin. Her bir sentaks hatasının nedenini/nedenlerini açıklayın.

```c++
class A{
public:
	void func();
	void func()const;
};

void func();

//===================================================

class B {
public:
	void foo(int);
private:
	void foo(int);
};

//===================================================

class C {
public:
	void foo(int);
private:
	void foo(double);
};

//===================================================

class D {
public:
	void foo(int);
private:
	int foo;
};

//===================================================

class E {
public:
	void foo();
};

void foo(int);

void E::foo()
{
	foo(12);
}

//===================================================

class F {
public:
	void foo(int x)
	{
		bar(x);
		F::bar(x);
		this->bar(x);
	}

	void bar(int)
	{
		//...
	}
};


```



#### Aşağıdaki kodda bir sentaks hatası varsa belirtin ve sentaks hatasının nedenini açıklayın.

```c++
class A {
	void func(int);
public:
	void func(unsigned);
};


int main()
{
	A ax;
	ax.func('A');
}

```

#### Aşağıdaki C++ kodu hakkında yorum yapınız:

```c++
int foo(int);

class A {
public:
	A(int x, int y) : my(x + y), mx(foo(my)) {}
private:
	int mx, my;
};
```

#### Aşağıdaki programda tanımsız davranış oluşturan kodları işaretleyin. Her bir tanımsız davranışın nedenini açıklayın:

```c++
#include <iostream>

class A {
public:
	void print()const
	{
		std::cout << mx << '\n';
	}
private:
	int mx;
};

A ga;

int main()
{
	A a1;
	A a2{};
	static A a3;

	ga.print();
	a1.print();
	a2.print();
	a3.print();
}

```

#### C++17 standartlarına göre aşağıdaki C++ programı çalıştırıldığında bu programın çıktısı ne olur?

```c++
#include <iostream>
 
class Myclass {
public:
	Myclass(int x) : x(x) 
	{
		std::cout << x;
	}
	
	~Myclass() 
	{ 
		std::cout << x + 3;
	}
 
private:
	int x;
};
 
int main() 
{
	const Myclass &c = Myclass(1);
	Myclass(2);
}
```

__Sorunun yanıtı şu seçeneklerden biri de olabilir:__

+ Sentaks hatası *(syntax error)*
+ Tanımsız davranış *(undefined behavior)*
+ Derleyiciye göre değişir *(implementation defined)*

#### C++17 standartlarına göre aşağıdaki C++ programı çalıştırıldığında bu programın çıktısı ne olur?

```c++
#include <initializer_list>
#include <iostream>
 
class Myclass {
public:
	Myclass() 
	{
		std::cout << "default ctor.\n";
	}
 
	Myclass(int)
	{
		std::cout << "ctor with int param\n";
	}
 
	Myclass(std::initializer_list<int>)
	{
		std::cout << "ctor with init_list param\n";
	}
};
 
int main() 
{
	Myclass m1;
	Myclass m2{};
	Myclass m3{ 1 };
	Myclass m4{ 1, 2 };
}
```

__Sorunun yanıtı şu seçeneklerden biri de olabilir:__

+ Sentaks hatası *(syntax error)*
+ Tanımsız davranış *(undefined behavior)*
+ Derleyiciye göre değişir *(implementation defined)*

#### Aşağıdaki kodda bulunan sentaks hatalarını işaretleyiniz:

```c++
class A {
public:
	explicit A(int);
	//
};

void f1(A);
void f2(A &);
void f3(const A &);
A f4() { return 1; }

int main()
{
	A a1{ 12 };
	A a2(24);
	A a3 = 35;
	A a4 = static_cast<A>(45);
	f1(1);
	f2(2);
	f3(3);
}
```

#### C++17 standartlarına göre aşağıdaki C++ programı çalıştırıldığında bu programın çıktısı ne olur?

```c++
#include <iostream>
 
class Myclass  {
public:
	Myclass() 
	{ 
		std::cout << "Myclass"; 
	}
};
 
int main() 
{
	Myclass m1();
	Myclass *m2(); 
}
```

__Sorunun yanıtı şu seçeneklerden biri de olabilir:__

+ Sentaks hatası *(syntax error)*
+ Tanımsız davranış *(undefined behavior)*
+ Derleyiciye göre değişir *(implementation defined)*

#### Aşağıdaki C++ programı hakkında yorum yapınız:

+ sentaks hatası
+ tanımsız davranış
+ derleyiciye göre değişir
+ ekrana şunu yazar: 

```c++
#include <iostream>

class Myclass {
public:
	explicit Myclass(int) 
	{
		std::cout << "i";
	};
	Myclass(char) 
	{
		std::cout << "c";
	};
};

int main() 
{
	Myclass c1{ 7 };
	Myclass c2 = 7;
}

```

#### Aşağıdaki C++ programı hakkında yorum yapınız:

+ sentaks hatası
+ tanımsız davranış
+ derleyiciye göre değişir
+ ekrana şunu yazar: 

```c++
#include <iostream>

class Nec {
public:
	Nec(int i) : i(i) { std::cout << i; }
	~Nec() { std::cout << i + 4; }

private:
	int i;
};

int main() {
	Nec&& nec = Nec{ 0 };
	Nec{ 1 };
	Nec{ 2 };
}
```

#### Aşağıdaki C++ programı hakkında yorum yapınız:

+ sentaks hatası
+ tanımsız davranış
+ derleyiciye göre değişir
+ ekrana şunu yazar: 

```c++
#include <iostream>

class F;

class C {
public:
	C() { std::cout << "C"; }
	friend C F::createC();
};

class F {
public:
	F() { std::cout << "F"; }

	C createC() { return C(); }
};

int main() {
	F f;
	C c = f.createC();
}

```

#### Aşağıdaki C++ programı hakkında yorum yapınız:

+ sentaks hatası
+ tanımsız davranış
+ derleyiciye göre değişir
+ ekrana şunu yazar: 

```c++
#include <iostream>

using namespace std;

class Nec {
public:
	Nec() { cout << "c"; }
	~Nec() { cout << "d"; }
};

int n = 2;

int main() {
erg:
	Nec nec;
	if (n--)
		goto erg;
}
```

#### Aşağıdaki C++ programı derlenip çalıştırıldığında ekran çıktısı ne olur?

```c++
#include <iostream>

class Myclass {
public:
	Myclass()
	{
		static int x{};
		std::cout << x++ << " ";
	}
	
};

int main()
{
	Myclass a[100];
}
```

#### Aşağıdaki bildirimlerden sentaks hatası olanları belirtiniz.

```c++
class Nec {
	Nec operator+();  //1
	Nec operator+(Nec); //2
	bool operator bool()const; //3
	static bool operator<(const Nec&); // 4
	int operator()(int)const; //5
	double operator()(int, int = 1)const; //6
	bool operator>(const Nec&, const Nec&); //7
	friend bool operator==(const Nec&); //8
	int* operator->(int(*)(int)); //9
	int operator.()const; //10
};

int operator[](Nec&, int); //11
Nec( operator=(Nec&, int); //12
int operator+(int, int); //13
```

#### C++17 standartlarına göre aşağıdaki C++ programı çalıştırıldığında bu programın çıktısı ne olur?

```c++
class Nec {
public:
	Nec(int x) : mx{ x } {}
	operator bool() const { return mx >= 0; }
private:
	int mx;
};

#include <iostream>

int main()
{
	Nec n1{ 0 }, n2{ 2 };
	std::cout << n1 + n2 << (n1 == n2);
}

```

__Sorunun yanıtı şu seçeneklerden biri de olabilir:__

+ Sentaks hatası *(syntax error)*
+ Tanımsız davranış *(undefined behavior)*
+ Derleyiciye göre değişir *(implementation defined)*

#### //1 ile işaretlenen deyimdeki fonksiyonları isimleriyle çağırın.

```c++
class Nec {
public:
	Nec& operator=(int);
	Nec operator>>(int);
};

Nec operator+(const Nec&, const Nec&);
bool operator>(const Nec&, const Nec&);

int main()
{
	Nec n1, n2, n3, n4;
	//...
	n1 = (n2 + n3) >> 5 > n4; //1

}
```

#### //1 ile işaretlenen satırda yazılan deyimde yapılan tüm fonksiyonları isimleriyle çağırın.

```c++
struct A {
	void foo();
};

struct B {
	A* operator->();
};

struct C {
	B operator->();
};

int main()
{
	C c;

	c->foo(); //1
}
```

#### Aşağıdaki C++ programı derlenip çalıştırıldığında ekran çıktısı ne olur?

```c++
#include <iostream>

class Myclass {
public:
	Myclass()
	{
		static int x{};
		std::cout << x++ << " ";
	}
	
};

int main()
{
	Myclass a[100];
}
```

#### Aşağıda tanımlanan Nec isimli sınıfla ilgili olarak aşağıdaki saptamaların her birinin doğru ya da yanlış olduğunu belirtiniz.

```c++
class Nec {
public:
private:
	const int mx;
};
```

+ _Nec_ sınıfının tanımında sentaks hatası vardır.   
+ _Nec_ sınıfının _default constructor_'ı _"not declared"_ durumdadır.
+ _Nec_ sınıfının _default constructor_'ı derleyici tarafından _delete_ edilmiştir.
+ _Nec_ sınıfının _default constructor_'ı derleyici tarafından _default_ edilmiştir.

#### C++17 standartlarına göre aşağıdaki C++ programı çalıştırıldığında bu programın çıktısı ne olur?

```c++
#include <iostream>
 
class Nec {
public:
	Nec() { std::cout << "A"; }
	Nec(const Nec&) { std::cout << "B"; }
	Nec(Nec&&) { std::cout << "C"; }
	~Nec() { std::cout << "D"; }
};
 
Nec func()
{
	return Nec{};
}
 
int main()
{
	func();
}
```

__Sorunun yanıtı şu seçeneklerden biri de olabilir:__

+ Sentaks hatası *(syntax error)*
+ Tanımsız davranış *(undefined behavior)*
+ Derleyiciye göre değişir *(implementation defined)*

#### C++11 standartlarına göre aşağıdaki C++ programı çalıştırıldığında bu programın çıktısı ne olur?

```c++
#include <iostream>
 
class Myclass {
public:
	Myclass() { std::cout << "1"; }
	Myclass(const Myclass &m) { std::cout << "2"; }
	void func() { std::cout << "3"; }
};
 
int main() 
{
	Myclass a[2];
 
	for (auto x : a) {
		x.func();
	}
}
```

__Sorunun yanıtı şu seçeneklerden biri de olabilir:__

+ Sentaks hatası *(syntax error)*
+ Tanımsız davranış *(undefined behavior)*
+ Derleyiciye göre değişir *(implementation defined)*

#### Aşağıdaki C++ programı hakkında yorum yapınız:

+ sentaks hatası
+ tanımsız davranış
+ derleyiciye göre değişir
+ ekrana şunu yazar: 

```c++
#include <iostream>

struct Nec {
	Nec() { std::cout << "A"; }
	Nec(const Nec&) { std::cout << "B"; }
	Nec(Nec &&) { std::cout << "C"; }
	~Nec() { std::cout << "D"; }
	void foo() { std::cout << "E"; }
} nec;

int main() 
{
	Nec(nec);
	nec.foo();
}
```

#### C++11 standartlarına göre aşağıdaki C++ programı çalıştırıldığında bu programın çıktısı ne olur?

```c++
#include <iostream>
#include <exception>
 
int g = 0;
 
class Member {
public:
	Member() 
	{
		std::cout << 'm';
		if (g++ == 0) {
			throw std::exception();
		}
	}
	~Member()
	{
		std::cout << 'M';
	}
};
 
class Owner {
public:
	Owner()
	{
		std::cout << 'o';
	}
	
	~Owner()
	{
		std::cout << 'O';
	}
	
	Member m;
};
 
void foo()
{
	static Owner owner;
}
 
int main()
{
	try {
		foo();
	}
	catch (std::exception &) {
		std::cout << 'c';
		foo();
	}
}
```

__Sorunun yanıtı şu seçeneklerden biri de olabilir:__

+ Sentaks hatası *(syntax error)*
+ Tanımsız davranış *(undefined behavior)*
+ Derleyiciye göre değişir *(implementation defined)*

#### C++17 standartlarına göre aşağıdaki C++ programı çalıştırıldığında bu programın çıktısı ne olur?

```c++
#include <iostream>
 
struct A {
	A() 
	{
		std::cout << "1";
	}
 
	A(const A &x) 
	{
		std::cout << "2";
	}
	
	const A &operator=(const A &x)
	{
		std::cout << "3";
		return *this;
	}
};
 
int main()
{
	A x;
	A y(x);
	A z = y;
	z = x;
}
```

__Sorunun yanıtı şu seçeneklerden biri de olabilir:__

+ Sentaks hatası *(syntax error)*
+ Tanımsız davranış *(undefined behavior)*
+ Derleyiciye göre değişir *(implementation defined)*

#### C++17 standartlarına göre aşağıdaki C++ programı çalıştırıldığında bu programın çıktısı ne olur?

```c++
#include <iostream>
#include <vector>
 
struct A
{
	A()
	{
		std::cout << "d";
	}
	
	A(const A&)
	{
		std::cout << "c";
	}
};
 
int main()
{
	std::vector<A> avec(4);
}
```


__Sorunun yanıtı şu seçeneklerden biri de olabilir:__

+ Sentaks hatası *(syntax error)*
+ Tanımsız davranış *(undefined behavior)*
+ Derleyiciye göre değişir *(implementation defined)*

#### C++17 standartlarına göre aşağıdaki C++ programı çalıştırıldığında bu programın çıktısı ne olur?


```c++
#include <iostream>
 
struct A {
	A() { std::cout << "a"; }
	~A() { std::cout << "A"; }
};
 
struct B {
	B() { std::cout << "b"; }
	~B() { std::cout << "B"; }
};
 
struct C {
	C() { std::cout << "c"; }
	~C() { std::cout << "C"; }
};
 
struct D {
	D() { std::cout << "d"; }
	~D() { std::cout << "D"; }
};
 
A a;
 
void f1() { static C c; }
void f2() { D d; }
 
int main()
{
	B b;
	f1();
	f2();
}
```

__Sorunun yanıtı şu seçeneklerden biri de olabilir:__

+ Sentaks hatası *(syntax error)*
+ Tanımsız davranış *(undefined behavior)*
+ Derleyiciye göre değişir *(implementation defined)*

#### C++17 standartlarına göre aşağıdaki C++ programı çalıştırıldığında bu programın çıktısı ne olur?


```c++
#include <iostream>
 
class A {
public:
	A() { std::cout << "A"; }
};
 
class B {
public:
	B(const A &r)
	{
		std::cout << "B"; 
	}
	
	void func() 
	{
		std::cout << "func";
	}
};
 
int main()
{
	B b(A());
	b.func();
}
```

__Sorunun yanıtı şu seçeneklerden biri de olabilir:__

+ Sentaks hatası *(syntax error)*
+ Tanımsız davranış *(undefined behavior)*
+ Derleyiciye göre değişir *(implementation defined)*

#### Aşağıdaki C++ programı hakkında yorum yapınız:

+ sentaks hatası
+ tanımsız davranış
+ derleyiciye göre değişir
+ ekrana şunu yazar: 

```c++
#include <iostream>

struct Nec
{
	Nec() { std::cout << "1"; }
	Nec(const Nec&) { std::cout << "2"; }
	~Nec() { std::cout << "3"; }
};

Nec func()
{
	return Nec();
}

int main()
{
	func();
}

```

#### Aşağıdaki C++ programı hakkında yorum yapınız:

+ sentaks hatası
+ tanımsız davranış
+ derleyiciye göre değişir
+ ekrana şunu yazar: 

```c++
#include <iostream>
#include <utility>

struct Nec {
	Nec() { std::cout << "1"; }
	Nec(Nec &) { std::cout << "2"; }
	Nec(const Nec &) { std::cout << "3"; }
	Nec(Nec &&) { std::cout << "4"; }
	~Nec() { std::cout << "5"; }
};

struct A {
	mutable Nec x;
	A() = default;
	A(const A &) = default;
};

int main() 
{
	A a1;
	A a2 = std::move(a1);
}
```

#### Aşağıda tanımlanan Nec isimli sınıfla ilgili olarak aşağıdaki saptamaların her birinin doğru ya da yanlış olduğunu belirtiniz.


```c++
int gp{};

class Myclass {
public:
private:
	const int mx{ 20 };
	int& r{ gp };
};
```

+ _Nec_ sınıfının tanımında sentaks hatası vardır.   
+ _Nec_ sınıfının _default constructor_'ı _"not declared"_ durumdadır.
+ _Nec_ sınıfının _default constructor_'ı derleyici tarafından _delete_ edilmiştir.
+ _Nec_ sınıfının _default constructor_'ı derleyici tarafından _default_ edilmiştir.

#### Aşağıdaki bildirimlerden sentaks hatası oluşturanları belirtiniz:

```c++
#include <string>

int func(int);

class Myclass {
	static int x = 10; 
	const static bool flag = true;
	const static unsigned char buffer[100] = {0};
	constexpr static int y = 20;
	constexpr static int a[]{ 1, 2, 3, 4, 5 };
	const static double dval = 12.5;
	inline static double d = 3.4;
	inline static std::string name{ "necati" };
	const static enum Color { Blue, Magenta, Red }Scolor = Red;
	inline static int ival = func(12);
};
```

#### _Nec_ sınıfının _foo_ isimli üye fonksiyonu içinde sentaks hatası oluşturan deyimleri _(statements)_ işaretleyin. 

```c++
class Nec {

	void foo()
	{
		m_val = 10; //1
		m_s = 20; //2
		this->m_s = 30; //3
		bar(); //4
		baz(); //5
		this->bar(); //6
		this->baz();  //7
		void (*fp1)() = &bar; //8
		void (*fp2)() = &baz; //9
		Nec::m_s++; //10
		Nec::baz(); //11
	}

	void bar();

	static void baz();

	static int m_s;
	int m_val;

};
```

#### _Nec_ sınıfının _foo_ isimli üye fonksiyonu içinde sentaks hatası oluşturan deyimleri _(statements)_ işaretleyin. 

```c++
class Nec {

	void foo() const
	{
		bar(); // 1
		baz(); // 2
		++m_val;
		++m_s; // 3
	}

	void bar();

	static void baz();

	static int m_s;
	int m_val;

};
```

#### _Nec_ sınıfının tanımımnda sentaks hatası oluşturan bildirimleri işaretleyiniz.

```c++
class Erg;

class Nec {
	static class Date sdate;
	static int foo();
	static int a[];
	Nec nx;
	static Nec nec;
	static Erg erg;
};
```

#### _Nec_ sınıfının _foo_ üye fonksiyonu içinde sentaks hatası oluşturan kodları işaretleyin.

```c++
class Nec {
	static void foo()
	{
		Nec nec;
		nec.mval = 10; //1
		nec.sval = 10; //2
		nec.bar(); //3
		nec.baz(); //4
		bar(); //5
		baz();  //6
		sval = 10; //7
		auto x = mval; //8
	}

	static void bar();
	void baz();
	static int sval;
	int mval;
};
```

#### C++17 standartlarına göre aşağıdaki C++ programı çalıştırıldığında bu programın çıktısı ne olur?

```c++
#include<iostream>
 
int func()
{
	return 0;
}
 
class Myclass
{
public:
	static int i;
	static int func()
	{
		return 1;
	}
};
 
int Myclass::i = func();
 
int main()
{
	std::cout << Myclass::i;
}
```

__Sorunun yanıtı şu seçeneklerden biri de olabilir:__

+ Sentaks hatası *(syntax error)*
+ Tanımsız davranış *(undefined behavior)*
+ Derleyiciye göre değişir *(implementation defined)*

#### _Nec_ sınıfının tanımımnda sentaks hatası oluşturan bildirimleri işaretleyiniz.


```c++
#include <string>

class Nec {
	int i1 = 20;
	int i2(30);
	int i3{ 20 };
	constexpr static double dval{ 3.0 };
	static const pi{ 3.14159 };
	static const int x = 83246;
	inline static std::string str{ "necati" };
	const static int primes[] = { 2, 3, 5, 7, 9, 13 };
	inline static int i4 = i1;
};
```

#### Aşağıdaki C++ kodunda bir sentaks hatası/hataları olup olmadığını belirtiniz. Varsa, her bir sentaks hatasının nedenini açıklayınız:

```c++
void f();

namespace A {
	void g();
}

namespace X {
	using ::f; 
	using A::g; 
}

void h()
{
	X::f(); 
	X::g(); 
}
```

#### Aşağıdaki C++ kodunda bir sentaks hatası/hataları olup olmadığını belirtiniz. Eğer varsa, her bir sentaks hatasının nedenini açıklayınız. Her bir fonksiyon çağrısı için hangi fonksiyonun çağrıldığını belirtiniz.


```c++
namespace A {
	struct X {};
	struct Y {};
	void f(int);
	void g(X);
}

namespace B {
	void f(int i)
	{
		f(i);
	}

	void g(A::X x)
	{
		g(x);
	}

	void h(A::Y y)
	{
		h(y);
	}
}
```

#### Aşağıdaki C++ kodunda (varsa) sentaks hatası olan yerleri belirtiniz. Her bir sentaks hatasının nedenini açıklayınız. `main` fonksiyonu içindeki `using` bildiriminin `main` fonksiyonunun üstündeki global isim alanına `(global namespace)` taşınması durumunda yine sentaks hatası olan (varsa) yerleri belirtiniz ve her bir sentaks hatasının nedenini açıklayınız.

```c++
#include <iostream>

namespace Nec {
	void func(int)
	{
		std::cout << "void Nec::func(int)\n";
	}

	void func(double)
	{
		std::cout << "void Nec::func(double)\n";
	}
}

int func()
{
	std::cout << "int func()\n";
	return 1;
}

// using Nec::func; //2
int main()
{
	using Nec::func; //1

	func();
	func(12);
	func(2.5);
}
```

#### `main' işlevi içinde yapılan çağrılardan hangileri geçerlidir? Geçerli olan çağrılar karşılığında hangi fonksiyon(lar) çağrılır? 
Sentaks hatası olan durumlarda sentaks hatası nedeni nedir?

```c++
#include <iostream>

namespace A {
	void func(int)
	{
		std::cout << "void A::func(int)\n";
	}
	//...
}

namespace B {
	void func(double)
	{
		std::cout << "void B::func(double)\n";
	}
	//...
}

void func(int)
{
	std::cout << "void ::func(int)\n";
}

using namespace A;
using namespace B;

int main()
{
	::func(1);
	func(1);
	func(4.5);
  func(9.L);
}
```

#### Aşağıdaki `C++` programında bir sentaks hatası var mı? Varsa sentaks hatasının nedeni/nedenleri nedir? Sentaks hatası yok ise ekrana ne yazdırılır?

```c++
#include <iostream>

namespace Nec {
	struct X{};
	void func(X) { std::cout << "A"; }
}

class Myclass {
public:
	void func(Nec::X) { std::cout << "B";}
	
	void foo()
	{
		Nec::X ax;
		func(ax); 
	}
};

int main()
{
	Myclass mx;
	mx.foo();
}

```

#### Aşağıdaki C++ kodunda main fonksiyonu içinde yapılan func çağrısı geçerli midir? Açıklama yapınız.

```c++
#include <vector>
#include <iostream>

namespace A {
	class B{};
	void func(std::vector<B>) 
	{
		std::cout << "A::func(std::vector<A::B>)\n";
	}
}

int main()
{
	std::vector<A::B> x;

	func(x); 
}
```

#### Aşağıdaki C++ programı hakkında yorum yapınız:

+ sentaks hatası
+ tanımsız davranış
+ derleyiciye göre değişir
+ ekrana şunu yazar: 

```c++
#include <iostream>

namespace A {
	class Nec {};
	void func(const Nec&) 
	{
		std::cout << "1";
	}
}

namespace B {
	void func(const A::Nec&) 
	{
		std::cout << "2";
	}
}

int main() {
	func(A::Nec());
}
```

#### Aşağıdaki kodda sentaks hatası olan yerleri belirleyiniz ve her bir sentaks hatasının nedenini açıklayınız:

```c++
namespace A {
	namespace B {
		class Bclass {	};
	}
	using namespace B;

	inline namespace C {
		class Cclass {	};
	}
	
	void func(B::Bclass);
	void foo(C::Cclass);
}

int main()
{
	A::Bclass bx;
	A::Cclass cx;

	func(bx);
	func(cx);
}
```

#### Mark the syntax errors, if any, in the following code sections.

```c++
#include <cstddef>

class A {
	size_type mx;
public:
	using size_type = std::size_t;
};
```

```c++
#include <cstddef>

class B {
	void func()
	{
		size_type n{};
		//...
	}
public:
	using size_type = std::size_t;
};
```

```c++
#include <cstddef>

class C {
	size_type func()
	{
		return 1u;
	}
public:
	using size_type = std::size_t;
};
```

```c++
include <cstddef>

class D {
	void func(size_type x)
	{
		//...
	}
public:
	using size_type = std::size_t;
};
```

```c++
#include <cstddef>

class E {
	using size_type = std::size_t;
	void func(size_type x);
};

void E::func(size_type x)
{
	//...
}
```

```c++
#include <cstddef>

class F {
	F::size_type mval;
public:
	using size_type = std::size_t;
};
```

```c++
#include <cstddef>

class G {
	using size_type = std::size_t;
	size_type bar();
};

size_type G::bar()
{
	//...
	return 1u;
}
```

#### Mark the syntax errors, if any, in the following code sections.

```c++
class A {
	class B {
		void foo();
	};
	
	void bar()
	{
		mb.foo();
	}
	B mb;
};
```

```c++
class A {
	class B {
		void bar()
		{
			auto sz1 = sizeof(mx);
			auto sz2 = sizeof(A::mx);
			foo();
			A::foo();
			//...
		}
	};
	int mx;
	static void foo(){}
};
```

#### Aşağıdaki kodda bulunan her bir sentaks hatasını işaretleyin ve sentaks hatasının nedenini belirtin:

```c++
int x = 0;
int y = 0;

class Encloser {	
	int x;
	static int s;  
	static NestedType sn;
public:
	
	class Nested {		
		void func(int ival)
		{
			x = ival; 
			int a = sizeof x; 

			s = ival;   
			::x = ival; 
			y = ival;   
		}
	public:
		void foo(Encloser* p, int i)
		{
			p->x = i;
			NestedType nsx;
		}
	};
	typedef Nested NestedType;
	void encfunc(NestedType n)
	{
		n.foo(this, x);
		n.func(x);
	}
};

```

#### Mark the syntax errors, if any, in the following code sections

```c++
class A {
private:
	class B {};
public:
	static B foo();
};

int main()
{
	auto bx = A::foo();
}
```

#### Mark the syntax errors, if any, in the following code sections

```c++
namespace nec {
	class A {
	public:
		class B {};
	};

	void foo(A::B);
}

int main()
{
	nec::A::B bx;
	foo(bx);
}
```

#### Bir std::string nesnesi üzerinde aşağıdaki silme işlemlerini gerçekleştirmeniz gerekiyor:

01. Yazının ilk karakterini silin.
02. Yazının son karakterini silin.
03. Yazının ilk ve son karakterleri dışında tüm karakterlerini silin.
04. Yazının ikinci karakterini silin.
05. Yazının sondan ikinci karakterini silin.
06. idx yazının geçerli bir indeksi olmak üzere yazının *idx* indisli karakterini silin.
07. Yazıdaki ilk *a* karakterini silin.
08. Yazıdaki son *a* karakterini silin.
19. Yazıdaki tüm *a* karakterlerini silin.
10. Yazıdaki ilk *a* karakteri ile başlayan ve son *a* karakteri ile biten yazıyı silin.
11. Yazıdaki ilk *a* karakterinden önce gelen ve sonra gelen *2* karakteri silin.
12. Yazıda bulunan ilk *"kan"* yazısını silin
13. Yazıda bulunan son *"kan"* yazısını silin
14. Yazıda bulunan tüm *"kan"* yazılarını silin
15. Yazıda bulunan ilk rakam karakterini silin
16. Yazıda bulunan son rakam karakterini silin
17. Yazıdaki tüm rakam karakterlerini silin.
18. Yazının uzunluğu 1'den büyükse ve yazının ilk karakteri ile son karakteri aynı ise bunları silin.
19. Yazının uzunluğu 5'ten büyükse ve yazının ilk *3* karakteri ile son *3* karakteri aynı ise bunları silin.
20. Yazıdaki ardışık eşit karakterlerden sadece bir tane kalacak şekilde silme işlemi yapın. *(unique)*
21. Yazıdaki tüm boşluk *(whitespace)* karakterlerini silin.

**Aşağıdaki test kodunu kullanabilirsiniz:**

```c++
#include <string>
#include <iostream>

void print(const std::string &s)
{
	std::cout << "'" << s << "' [" << s.length() << "]\n";
}

int main()
{
	std::string s;

	std::cout << "bir yazi giriniz: ";
	std::getline(std::cin, s);
	print(s);
	///kod
	print(s);
}

```

#### *filename* isimli *std::string* nesnesi bir dosyanın ismini tutuyor. Aşağıdaki işlemleri gerçekleştirecek kodları yazınız.

+ Dosyanın uzantısı yok ise uzantısı *.jpg* olsun.  *(hasan) -> (hasan.jpg)*
+ Dosyanın uzantısı *".gif"* ise uzantısını *".png"* olarak değiştirin.  *(necati.gif) -> (necati.png)*
+ Dosyanın uzantısı *".xls"* ise uzantısını silin. *(aleyna.xls) -> (aleyna)*

#### Aşağıdaki işlevleri tanımlayınız ve kendi yazacağınız test kodu (kodları) ile test ediniz:

```c++
std::string opposite_case(const std::string &s);
```

işlev parametresi ile aldığı yazıdaki 
 + küçük harflerin yerinde aynı karakterlerin büyüğü olan
 + büyük harflerin yerinde aynı karakterlerin küçüğü olan

bir string döndürecek.

```c++
std::string remove_chars(const std::string &source, const std::string &scars);

```

İşlevin geri dönüş değeri olan *string*'in değeri source *string*'i içinden *scars* stringinin karakterlerinin silinmiş hali olacak.
<br>Örnek (parantezler yazılara dahil değil)

*source*           : (ankaranin tasina bak gozlerimin yasina bak) <br>
*scars*            : (kain ) <br>
*geri dönüş değeri*: (rtsbgozlermysb)

```c++
std::string trim(const std::string &source);
```

işlevin geri dönüş değeri olan string source stringinin başındaki ve sonundaki boşluk karakterlerinin silinmiş hali olacak:

```
(     necati ergin     )  ->  (necati ergin)
```

parantezler yazıya ait değil.

#### Bir stringin başka bir *string*'in sola döndürülmüş hali olup olmadığını sınayan

```c++
#include <string>

bool is_lest_rotate(const std::string &s1, const std::string &s2);

```

#### işlevini tanımlayınız.

#### İşlev eğer *s2* stringi *s1* stringinin sola döndürülmesiyle elde edilebiliyorsa *true* değere aksi halde *false* değere geri dönmeli.

#### Aşağıdaki listede ingilizce sözcüklerin ortak bir özelliği var: Bu sözcüklerden bazı karakterler silindiğinde geriye benim ismim kalıyor. Böyle bir özelliği test eden bir işlev yazabilir misiniz?

```c++
bool is_reachable_to(const std::string &r1, const std::string &r2);
```

+ İşlevin birinci parametresi kaynak (uygunluğu test edilecek) *string*.
+ İşlevin ikinci parametresi silme işleminden sonra geriye kalması gereken *string*.
+ İşlevin geri dönüş değeri birinci yazıdan karakter silme yoluyla ikinci yazının elde edilip *(true)* elde edilemeyeceği *(false)* bilgisi.

```
anemoclastic             anencephalotrophia       antelocation             anteoccupation           
anticommercialistic      antidemocratic           antidemocratical         antidemocratically       
antiecclesiastic         antiecclesiastical       antiecclesiastically     antiecclesiasticism      
antieducation            antieducational          antieducationalist       antieducationally        
antieducationist         antiejaculation          antimechanistic          antimechanistically      
antimechanization        antimedication           antimedicative           antispeculation          
aquopentamminecobaltic   beneficiating            beneficiation            bronchiectatic           
cockneyfication          consecrating             consecration             consecrations            
consecrative             contrectation            counteraccusation        counterassociation       
countercathexis          counterclassification    counterclassifications   countercondemnation      
counterdeclaration       counterexcommunication   counterindication        counterindoctrination    
countermachination       countervindication       deconsecrating           deconsecration           
deintellectualization    disinsectization         encephalomyocarditis     endopericarditis         
enterotoxication         generification           gynaecocratic            gynaecomastia            
gynecocratic             gynecocratical           gynecomastia             gynecomastism            
gynecopathic             gynecratic               hendecatoic              inaffectation            
inappreciation           inappreciative           inappreciatively         inappreciativeness       
indemnification          indemnifications         indescribabilities       ineducation              
inescation               inexpectation            influenceabilities       insectation              
intellectation           intellectualisation      intellectualistic        intellectualistically    
intellectualities        intellectualization      intellectualizations     intensification          
intensifications         interapplication         interassociation         intercalating            
intercalation            intercalations           intercalative            intercarotid             
intercartilaginous       intercausative           intercirculating         intercirculation         
intercivilization        intercolonization        intercolumnation         intercolumniation        
intercombination         intercommunicating       intercommunication       intercommunicational     
intercommunications      intercommunicative       intercontradiction       intercorrelating         
intercorrelation         intercorrelations        intercreating            intercrystallization     
intercursation           interesterification      interincorporation       interindicating          
interjaculating          interlocating            interlocation            interlucation            
intermodification        interoscillating         interosculating          interosculation          
interplication           interpunctuation         interramification        interreticulation        
interscholastic          interstratification      intersusceptation        intertrochanteric        
intraecclesiastical      linecasting              lymphangiectatic         magnetification          
meningoencephalitic      meningoencephalitis      necation                 necessitating            
necessitatingly          necessitation            necessitative            necromantic              
necromantical            necromantically          necrotization            neoconservative          
neuropsychiatric         neuropsychiatrically     neuropsychiatrist        neuropsychopathic        
neurovaccination         newscasting              nomenclative             nomenclatorial           
nomenclatorship          nomenclaturist           nonaffectation           nonappreciation          
nonappreciative          nonappreciatively        nonappreciativeness      nonauthentication        
nonbureaucratic          nonbureaucratically      noncertification         nonconsecration          
nondecalcification       nondecatoic              nondeceleration          nondeclaration           
nondeclarative           nondeclaratively         nondecoration            nondecorative            
nondedication            nondedicative            nondefalcation           nondemocratic            
nondemocratical          nondemocratically        nondenunciating          nondenunciation          
nondenunciative          nondeprecating           nondeprecatingly         nondeprecative           
nondeprecatively         nondeprecatorily         nondepreciating          nondepreciation          
nondepreciative          nondepreciatively        nondesecration           nondiversification       
nondomesticating         nonecclesiastic          nonecclesiastical        nonecclesiastically      
nonecstatic              nonecstatically          noneducation             noneducational           
noneducationally         noneducative             nonelectrification       nonelucidating           
nonelucidation           nonelucidative           nonemancipation          nonemancipative          
nonenunciation           nonenunciative           nonequivocating          noneradicative           
nonevacuation            nonevocative             nonexcavation            nonexcitative            
nonexculpation           nonexemplification       nonexemplificatior       nonexpectation           
nonexplicative           nonextrication           nonidentification        nonmechanistic           
nonmedicative            nonmercantile            nonobjectification       nonpersonification       
nonprecipitation         nonprecipitative         nonpredicative           nonpredicatively         
nonreciprocating         nonrecitation            nonrecitative            nonreclamation           
nonrecommendation        nonreconciliation        nonrecuperatiness        nonrecuperation          
nonrecuperative          nonrecuperativeness      nonrenunciation          nonreplication           
nonrespectabilities      nonresuscitation         nonresuscitative         nonretractation          
nonrevocation            nonsensification         nonspecification         nonspeculation           
nonspeculative           nonspeculatively         nonspeculativeness       nonsubjectification      
nontheocratic            nontheocratical          nontheocratically        nonverification          
overintellectualization  overintensification      panecclesiastical        pentadecatoic            
phoneticization          phoneticogrammatical     pneumoencephalitis       preconseccrating         
preconsecrating          preconsecration          preindemnification       prenecessitating         
reconsecrating           reconsecration           reconsecrations          telangiectatic           
transpeciation           transrectification       unaffectation            unappreciating           
unappreciation           unappreciative           unappreciatively         unappreciativeness       
unbureaucratic           unbureaucratically       unconsecration           unconsecrative           
undecatoic               undeclarative            undecorative             undeification            
undemocratic             undemocratically         undemocratisation        undemocratise            
undemocratised           undemocratising          undemocratization        undemocratize            
undemocratized           undemocratizing          undeprecating            undeprecatingly          
undeprecative            undeprecatively          undepreciative           undercapitalization      
undercapitalize          undercapitalized         undercapitalizing        undercaptain             
undercoating             undercoatings            undereducation           underparticipation       
undomestication          unecclesiastic           unecclesiastical         unecclesiastically       
unecstatic               unecstatically           uneducative              unelucidating            
unelucidative            unemancipative           unemasculative           unenunciative            
unequivocating           uneradicative            uneucharistical          unevocative              
unexacerbating           unexcogitative           unexcruciating           unexplicative            
unfelicitating           ungesticulating          ungesticulative          unmechanistic            
unmedicative             unmercantile             unmerchantlike           unnecessitating          
unpeculating             unprecautioned           unprecipitative          unprecipitatively        
unpredicative            unpredicatively          unprevaricating          unrecanting              
unreciprocating          unrecitative             unrecreating             unrecreational           
unrecriminative          unrecuperatiness         unrecuperative           unrecuperativeness       
unrenunciative           unresuscitating          unresuscitative          unspeculating            
unspeculative            unspeculatively          unverificative
```

#### Bir std::string nesnesi üzerinde aşağıdaki ekleme (insert) işlemlerini gerçekleştirmeniz gerekiyor:

01. Yazının başına 'X' karakterini ekleyin.
02. Yazının sonuna 'X' karakterini ekleyin.
03. Yazıya 'W' karakterini yazının 3 indeksli karakteri olacak biçimde ekleyin. 
04. Yazının başına "kendi isminizi" ekleyin.
05. Yazının sonuna "kendi isminizi" ekleyin.
06. Yazının sonuna yazının uzunluğunu ekleyin: necati ----> necati6
07. Yazıda bulunan rakam karakterlerinden bir tane daha ekleyin:   a4b71p9eak23t ----> a44b7711p99eak2233t


**Aşağıdaki test kodunu kullanabilirsiniz:**

```c++
#include <string>
#include <iostream>

void print(const std::string &s)
{
	std::cout << "'" << s << "' [" << s.length() << "]\n";
}

int main()
{
	std::string s;

	std::cout << "bir yazi giriniz: ";
	std::getline(std::cin, s);
	print(s);
	///kod
	print(s);
}

```

#### Aşağıdaki fonksiyonlardan tanımsız davranış olanları işaretleyiniz ve neden tanımsız davranış oluşturduklarını açıklayınız. (Bu soru David Mazieri'nin bir makalesinden alınmıştır.)

```c++
decltype(auto)
fn_A(int i)
{
	return i;
}

decltype(auto)
fn_B(int i)
{
	return (i);
}

decltype(auto)
fn_C(int i)
{
	return (i + 1);
}

decltype(auto)
fn_D(int i)
{
	return i++;
}
decltype(auto)
fn_E(int i)
{
	return ++i;
}

decltype(auto)
fn_F(int i)
{
	return (i >= 0 ? i : 0);
}

decltype(auto)
fn_G(int i, int j)
{
	return i >= j ? i : j;
}

struct S {
	int i = 0;
};

decltype(auto)
fn_H()
{
	return (S{});
}
decltype(auto)
fn_I()
{
	return (S{}.i);
}
```



#### main fonksiyonu içinde yapılan fonksiyon çağrılarından hangileri geçerlidir. Geçerli olan fonksiyon çağrılarında hangi fonksiyonlar çağrılır?

```c++
#include <string>
#include <string_view>
#include <iostream>

void foo(const std::string&)
{
	std::cout << "string\n";
}

void foo(std::string_view)
{
	std::cout << "string_view\n";
}

std::string bar() 
{
	return {};
}

int main()
{
	using namespace std::literals;

	foo("necati");
	foo("necati"s);
	foo("necati"sv);
	foo({});
	foo(bar());
}
```

#### Aşağıda tanımlanan get_reverse isimli fonksiyon hakkında  bir yorum yapmanız isteniyor. Fonksiyonda bir sorun var mı? Varsa sorunu açıklayınız:

```c++
#include <iostream>
#include <string_view>
#include <algorithm>

std::string_view get_reverse(std::string str)
{
	reverse(begin(str), end(str));

	return str;
}

int main()
{
	auto s = get_reverse("necati ergin");

	std::cout << s << '\n';
}
```

#### Aşağıdaki kodda bir tanısmsız davranış söz konusu mu? Yorum yapınız:

```c++
#include <string_view>
#include <iostream>

int main()
{
	std::string str{ "necati ergin" };

	std::string_view sw{ str };
	str.append(500, 'A');
	std::cout << "[" << sw << "]\n";
}
```

# Date sınıfı

Aşağıda ismi `Date` olan bir sınıfın tanımlandığı başlık dosyası yer almaktadır. 
Bu ödevde `Date` sınıfının kodlarını yazmanız isteniyor.

`Date` sınıfı türünden bir nesnenin değeri bir tarihtir. Örnek: `15 Şubat 1998` <br>
Aşağıdaki açıklamalar kodda bulunan yorum satırlarına ilişkindir:

1. Sınıfın hizmet verdiği en küçük yıl değeri
2. `random_date` işlevinin üreteceği tarih için en küçük yıl değeri.
3. `random_date` işlevinin üreteceği tarih için en büyük yıl değeri.
4.  Haftanın günü için `enum class` türü.
5. Varsayılan kurucu işlev: `Date` nesnesini `01-01-1900` tarihi ile oluşturmalı.
6. `Date` nesnesini gün, ay, yıl değeri ile oluşturacak kurucu işlev.
7. `Date` nesnesini formatlanmış  yazıdan alacağı tarih değeri ile oluşturacak. Format: `gg/aa/yil`
8. `Date` nesnesini `"calender time"` değerinden dönüştüreceği tarih değeri ile oluşturmalı.
9. Ayın gününü döndürüyor.
10. Ay değerini döndürüyor. `(Ocak 1, Şubat 2, ...)`
11. Tarihin yıl değerini döndürüyor
12. Yılın gününü döndürüyor `(01 Ocak ---> 1   31 Aralık---> 365 ya da 366`
13. Haftanın gününü döndürüyor.
14. Tarihin ayın günü değerini değiştiriyor.
15. Tarihin ayını değiştiriyor
16. Tarihin yılını değiştiriyor.
17. Tarihi değiştiriyor.
18. Tarihten gün çıkartan `const` üye operatör işlevi. Geri dönüş değeri elde edilen tarih olacak.
19. Tarihi gelen gün kadar arttıran üye operatör işlevi. Geri dönüş değeri `*this` olmalı.
20. Tarihi gelen gün kadar eksilten üye operatör işlevi. Geri dönüş değeri `*this` olmalı.
21. Önek `++` operatörünü yükleyen işlev. (İşlevin referans döndürdüğüne dikkat ediniz). 
22. Sonek `++` operatörünü yükleyen işlev. (İşlevin referans döndürmediğine dikkat ediniz). 
23. Önek `--` operatörünü yükleyen işlev. (İşlevin referans döndürdüğüne dikkat ediniz). 
24. Sonek `--` operatörünü yükleyen işlev. (İşlevin referans döndürmediğine dikkat ediniz). 
25. Rastgele bir tarih döndüren sınıfın `static` üye işlevi.
26. Artık yıl testi yapan sınıfın `static` üye işlevi.
27. `Date` nesnelerinin karşılaştırılmasını sağlayacak global operatör işlevleri.
28. İki tarih arasındaki gün farkını döndüren global operatör işlevi.
29. Gelen tarihten `n` gün sonrasını döndüren global operatör işlevleri.
30. İçsel `(nested) enum class Weekday` için arttırma ve eksiltme işlevleri.
31. Date nesnelerinin değerlerini çıkış akımlarına yazdıracak global operatör işlevi `(inserter)`.
Formatlama şöyle olmalı:  `31 Ekim 2019 Persembe`.
32. `Date` nesnelerine giriş akımlarından aldığı karakterlerden oluşturulacak değeri yerleştiren global operatör işlevi `(extractor)`
Formatlama: `gg/aa/yyyy` (ayıraç olarak istenilen bir karakter kullanılabilir.

#### Diğer notlar:
* Dilediğiniz global işlevleri `"friend"` yapabilirsiniz.
* Sınıfın `private` arayüzünü dilediğiniz gibi oluşturabilirsiniz.
* Gerekli görürseniz sınıfın `public` arayüzüne eklemeler yapabilirsiniz.
* Gerekli görürseniz sınıfın `public` arayüzünde değişiklikler yapabilirsiniz.
* Sınıfın `public` öğelerinin isimlerini istediğiniz şekilde değiştirebilirsiniz.
* Dilediğiniz işlevleri `"constexpr"` yapabilirsiniz.
* Bu ödevde `"exception handling"` araçlarını kullanmayacağız. (`exception handling` konusunu gördükten sonra kodlarda değişiklik yapacağız.) Fonksiyonlara gönderilen argümanların uygun ve doğru değerler olduğunu varsayabilirsiniz. 
* Kod tekrarından mümkün olduğu kadar kaçınmalısınız.
* `const` doğruluğuna `(const correctness)` çok dikkat etmelisiniz. `(const olması gereken tüm varlıklar const olmalı)`
* Gereksiz yorum satırlarından mümkün olduğu kadar kaçınmalısınız.
* Yazdığınız kodların doğru çalışıp çalışmadığını sınamak için test kodları yazmalısınız.
* Derleyicinizin uygun bir `switch`'ini kullanarak mantıksal uyarı iletilerinin hata `(error)` olarak değerlendirilmesini sağlayınız.
* Gerekli olduğunu düşündüğünüz yerlerde [[nodiscard]] attribute'unu kullanmalısınız.


```c++
#ifndef DATE_H
#define DATE_H
#include <iosfwd>
#include <ctime>

namespace project {
class Date {
public:
	static constexpr int year_base = 1900;  //1
	static constexpr int random_min_year = 1940;  //2
	static constexpr int random_max_year = 2020;  //3
	enum class Weekday {Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday}; //4
	Date(); //5 
	Date(int d, int m, int y);  //6
	explicit Date(const char *p);  //7
	explicit Date(std::time_t timer); //8
	int get_month_day()const; //9
	int get_month()const; //10
	int get_year()const; //11
	int get_year_day()const; //12
	Weekday get_week_day()const; //13

	Date& set_month_day(int day); //14
	Date& set_month(int month); //15
	Date& set_year(int year); //16
        Date& set(int day, int mon, int year); //17
	Date operator-(int day)const; //18
	Date& operator+=(int day); //19
	Date& operator-=(int day); //20
	Date& operator++(); //21
	Date operator++(int); //22
	Date& operator--(); //23
	Date operator--(int); //24
	
	friend bool operator<(const Date &, const Date &); //27
	friend bool operator==(const Date &, const Date &); //27
	static Date random_date(); //25
	static constexpr bool isleap(int y); //26
	
	friend std::ostream &operator<<(std::ostream &os, const Date &date); //31
	friend std::istream &operator>>(std::istream &is, Date &date); //32
};

bool operator<=(const Date &, const Date &); //27
bool operator>(const Date &, const Date &); //27
bool operator>=(const Date &, const Date &); //27
bool operator!=(const Date &, const Date &); //27

int operator-(const Date &d1, const Date &d2); //28
Date operator+(const Date &date, int n); //29
Date operator+(int n, const Date &); //29
Date::Weekday& operator++(Date::Weekday &r); //30
Date::Weekday operator++(Date::Weekday &r, int); //30
Date::Weekday& operator--(Date::Weekday &r); //30
Date::Weekday operator--(Date::Weekday &r, int); //30}

#endif
```
