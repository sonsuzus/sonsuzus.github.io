---
layout: post
title: Segment Ağacı ile Inversion Sayma
categories:
  - Program
tags:
  - c++
  - sıralama
  - segment ağacı
  - inversion sayısı
  - algoritma
---

Bu kod, bir dizideki inversion sayısını hesaplamak için Segment Ağacı kullanır. Inversion, bir dizideki sıralı olmayan çiftlerin sayısıdır. Bu, dizinin ne kadar "sıralı olmadığı"nın bir ölçüsüdür.

Segment Ağacı, bir dizi üzerinde aralık sorgularını verimli bir şekilde gerçekleştirmek için kullanılan bir veri yapısıdır. Bu kodda, Segment Ağacı, dizideki her bir elemanın "sıkıştırılmış" değerini kullanarak, o elemandan daha büyük elemanların sayısını takip etmek için kullanılır. Bu sayede, her bir eleman için yapılan sorgularla toplam inversion sayısı bulunur.

Aşağıdaki C++ kodu, Segment Ağacı kullanarak bir dizideki inversion sayısını hesaplar:
```c++
//Segment tree ile inversion sayma
#include <bits/stdc++.h>

using namespace std;

int a[100005],kopya[100005];
long long tree[100005*4];

void update(int node,int start,int end,int x){
	if(start>end || start>x || end<x)return ;//güncellemek istediğim aralığın (elemanın) tamamen dışındaysam
	if(start==x && end==x){//güncellemek istediğim indise ulaşmışsam
		tree[node]++;//x elemanından 1 tane daha geldiği için değeri 1 arttırıyoruz.
		return;//daha fazla dallanmasını istemiyoruz
	}
	int mid=(start+end)/2;
	update(node*2,start,mid,x),update(node*2+1,mid+1,end,x);//sola ve sağa dallanıyorum.
	tree[node]=tree[node*2]+tree[node*2+1];//bir node'un değeri sol ve sag çocuklarının toplamına eşittir.
}

long long query(int node,int start,int end,int l,int r){
	if(start>end || start>r || end<l)return 0;//İstediğim aralığın tamamen dışında isem 0 tane istenen değer vardır(istenen değer yoktur.)
	if(start>=l && end<=r)return tree[node];//İstediğim aralığın tamamen içindeysem bu node'un değerini dönerim.
	int mid=(start+end)/2;
	return query(node*2,start,mid,l,r)+query(node*2+1,mid+1,end,l,r);//Soldan ve sağdan gelen değerlerin toplamı fonksiyonun şuanki durumunun cevabıdır.
}

int main(){
	int n;
	scanf("%d",&n);
	int a[n+2];
	int b[n+2];
	for(int i=1;i<=n;i++){
		scanf("%d",&a[i]);
		kopya[i]=a[i];//dizimizi klonluyoruz
	}
	sort(kopya+1,kopya+n+1);//burada klonlanan diziyi sıralıyoruz (stl fonksiyon kullandık.)
	int dizi[n+2];
	int index=0;
	for(int i=1;i<=n;i++){
		if(i==1 || kopya[i]!=kopya[i-1])dizi[++index]=kopya[i];//burada klonlanan dizideki bütün elemanların farklı olmasını sağlıyoruz.
	}
	for(int i=1;i<=n;i++){
		int sol=1;
		int sag=index;
		while(sol<sag){//binary search ile sıkıştırılmış indisini tespit etmeye çalışıyoruz.
			int orta=(sol+sag)/2;
			if(dizi[orta]>=a[i])sag=orta;
			else sol=orta+1;
		}
		a[i]=sag;//binary searchde bulduğumuz değer elemanımızın sıkıştırılmış değeri olur.
	}
	long long cevap=0;
	for(int i=1;i<=n;i++){
		cevap+=query(1,1,index,a[i]+1,index);//elemanımızdan büyük kaç sayı varsa inversion sayımızı o kadar arttırıyoruz.
		update(1,1,index,a[i]);//bir tane daha a[i] elemanı geldiği için değerini 1 arttırıyoruz.
	}
	cout<<cevap<<endl;
}
```