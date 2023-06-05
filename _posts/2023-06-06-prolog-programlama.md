---
title: Prolog Programlama
author: sonsuz
date: 2023-06-06 02:04:00 +0300
categories: [Program]
tags: [dil,programlama,prolog,mantık]
---


Prolog, Yapay zekâ uygulamalarında kullanılan dördüncü nesil bilgisayar dili ailesinden olan bir mantık programlama dilidir.

1970'li yılların başlarında Fransa'nın Aix-Marseille Üniversitesi'nde Alain Colmerauer ve çalışma grubu tarafından icat edilmiştir. Fransızca "Programmation en Logique" kelimesinden gelmektir. Mantığın doğrudan doğruya bir bilgisayar dili olarak kullanılabilmesini sağlamak amacıyla yapılan çalışmalar da 1980 yıllarının başlarında da yoğunluk kazanmıştır. 1981 yılında Japonlar beşinci nesil bilgisayar projesini açıklamalarıyla da konuya olan ilgi büyük bir ölçüde artmıştır. Prolog üzerine çeşitli amaç ve seviyelerde birçok kitap yayınlanmış ve dilin bir standardı oluşmuştur.

Bilgisayarın belirli bir problemi çözebilmesi için kendisine problemle ve çözüm yoluyla ilgili bilgi verilmesi gereklidir. Programlama dilleri aracılığıyla insan bilgisayarlarla iletişim kurabilir. Prolog mantıksal ve sembolik düşünmeye uygun yapısıyla, problemin tanımlanması ve çözümü için gerekli yöntemlerin geliştirilmesi aşamalarında insanoğluna yardımcı olan bir araçtır.

Bir örnek verecek olursak Sokrat bir insandır ve Tüm insanlar ölümlüdür cümlelerinden, Sokrat ölümlüdür sonucuna varırız. Şimdi bu basit mantık probleminin bir prolog programı olarak nasıl ifade edilebileceğini görelim. Problem önce dilin iki öğesi olan, gerçekler ve kurallar aracılığıyla tanımlanır. Gerçekler, matematiksel aksiyomlar gibi, bir veya daha fazla nesne arasında bulunan bir ilişkiyi veya bir nesneyle ilgili bir özelliği, deklare etmek için yazılan Prolog tümceleridir. Prolog tümceleri mantıktaki Horn cümlelerini ifade eder.

erkek(ahmet).

Yukarıda bulunan ifade bir fact olarak tanımlanmaktadır. Doğal dilde bunu ‘Ahmet bir erkektir.’ diye tanımlayabiliriz. Burada bulunan ‘erkek’ ifadesi bir predicate olarak isimlendirilmektedir. Bu predicate bize içinde bulunan argüman/argümanlar arasında ki ilişkiyi göstermektedir. Prolog programlama dilinde bulunan bütün clause ifadeleri . ile bitmektedir. Yukarıda yazdığımız prolog uzantılı dosyamızı programımıza yükledikten sonra,şöyle bir soru sorarsak.

?- erkek(ahmet).

Sorduğumuz soru şöyle olmaktadır. ‘Ahmet erkek midir’ Aldığımız cevap true. olacaktır. Bu fact önceden programımızda tanımlamış olduğumuzdan bize true cevabını verecektir.

?- erkek(can).

Sorduğumuz soru şöyle olmaktadır ‘Can erkek midir ?’ Aldığımız cevap ise false. olacaktır. Bu fact önceden programımızda tanımlanmış olmadığından dolayı false cevabını verecektir.

Prolog programlama dilinde değişkenleri büyük harfler ile göstermekteyiz. Örnek vermek gerekirse X,_23,Can gibi ifadeler prolog içinde bir değişken ifade etmektedir. Yazdığımız programda aşağıda ki gibi bir soru sorarsak

?- erkek(X).

Bu soru ‘X erkek midir ?’ elimizde her hangi belirli bir değer olmadığından bütün erkek ilişkisinde tanımlanan argümanlar bizim X değerimiz olabilir,kısacası bu soruyu prolog programına şöyle sormaktayız ‘Hangi değerler X olabilir’ cevap olarak

X = ahmet.

ifadesini almış oluruz,Prolog programlama dilinde fact kavramı çok önemlidir,bizim koşulsuz biçimde bir ilişki tanımlamamızı sağlamaktadırlar.


Programımızda istersek daha farklı ilişkiler tanımlayabiliriz.

anne(merve,zehra).

Yukarıda bulunan fact erkek ilişkisi yerine 1 argüman yerine 2 argüman almakta doğal dilde ise şöyle ifade edilebilir.

“Merve Zehranın annesidir.”

## 8 Vezir yerleştiren program

```prolog
% render solutions nicely.
:- use_rendering(chess).

%%	n_queens(?N, ?Cols) is nondet.
%
%	@param The k-th element of Cols is the column number of the
%	queen in row k.
%	@author Markus Triska

:- use_module(library(clpfd)).

n_queens(N, Qs) :-
	length(Qs, N),
	Qs ins 1..N,
	safe_queens(Qs).

safe_queens([]).
safe_queens([Q|Qs]) :-
	safe_queens(Qs, Q, 1),
	safe_queens(Qs).

safe_queens([], _, _).
safe_queens([Q|Qs], Q0, D0) :-
	Q0 #\= Q,
	abs(Q0 - Q) #\= D0,
	D1 #= D0 + 1,
	safe_queens(Qs, Q0, D1).


/** <examples>

?- n_queens(8, Qs), labeling([ff], Qs).
?- n_queens(24, Qs), labeling([ff], Qs).
?- n_queens(100, Qs), labeling([ff], Qs).

*/
```