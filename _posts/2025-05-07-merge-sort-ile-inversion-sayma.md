---
layout: post
title: Merge Sort ile Inversion Sayma
categories:
  - Program
tags:
  - cpp
  - sıralama
  - merge sort
  - inversion sayısı
  - algoritma
---

Bu kod, Merge Sort algoritmasını kullanarak bir dizideki inversion sayısını hesaplar. Inversion, bir dizideki sıralı olmayan çiftlerin sayısıdır. Başka bir deyişle, bir dizideki i ve j indisleri için, eğer i < j ve a[i] > a[j] ise, bu bir inversion'dır. Inversion sayısı, bir dizinin ne kadar "sıralı olmadığı"nın bir ölçüsüdür; sıralı bir dizide inversion sayısı 0'dır.

Merge Sort, böl ve yönet yaklaşımını kullanan, verimli bir sıralama algoritmasıdır. Diziyi ardışık olarak iki alt diziye böler, her bir alt diziyi sıralar ve sonra sıralı alt dizileri birleştirir. Bu birleştirme işlemi sırasında, alt dizilerdeki elemanların göreli sırasını takip ederek inversion sayılarını hesaplayabiliriz. Özellikle, sol alt dizideki bir eleman sağ alt dizideki bir elemandan büyükse, bu bir inversion anlamına gelir ve bu durumdaki inversion sayısı, sol alt dizideki kalan elemanların sayısı kadardır.

Aşağıdaki C++ kodu, Merge Sort algoritmasını kullanarak bir dizideki inversion sayısını hesaplar.
```c++
//Merge Sort ile inversion sayma
#include <bits/stdc++.h>

using namespace std;

int n,a[500005],tmp[500005];
long long cevap;

void merge_sort(int sol,int sag){
	if(sol==sag){//eğer bir elemanlı bir aralık kaldıysa daha fazla dallanmamalıyız.
		return ;
	}
	int orta=(sol+sag)/2;
	merge_sort(sol,orta);//sol tarafa dallanıyoruz.
	merge_sort(orta+1,sag);//sağ tarafa dallanıyoruz.
	int p1=sol;
	int p2=orta+1;
	//[sol,orta] ,  [orta+1,sag]
	int index=0;
	while(p1<=orta && p2<=sag){//iki dizinin de yukarıya çıkartılacak elemanı olduğu sürece
		if(a[p1]<=a[p2]){//sol taraftaki eleman daha küçük veya eşitse
			tmp[++index]=a[p1++];//sol taraftaki elemanı diziye ekle
			cevap+=p2-(orta+1);//inversion sayısını sağ taraftaki şuanki elemanımızdan küçük eleman sayısınca arttır.
		}
		else{
			tmp[++index]=a[p2++];//sol taraftaki elemanı diziye ekle
		}
	}
	while(p1<=orta){//sağ taraftaki elemanların hepsi bitmiş soldaki kalanları ekliyoruz
		cevap+=p2-(orta+1);
		tmp[++index]=a[p1++];
	}
	while(p2<=sag){//sol taraftaki elemanların hepsi bitmiş sağda kalanları ekliyoruz
		tmp[++index]=a[p2++];
	}
	for(int i=sol;i<=sag;i++){//dizimizin aralıktaki elemanları sıralanmış haline getiriyoruz.
		a[i]=tmp[i-sol+1];
	}
}

int main(){
	scanf("%d",&n);
	for(int i=1;i<=n;i++){
		scanf("%d",&a[i]);
	}
	merge_sort(1,n);//dizinin tamamını sıralamak ve iversionları saymak için bütün dizide merge_sort fonksiyonunu çağırıyoruz. 
	printf("%lld\n",cevap);
	return 0;
}
```