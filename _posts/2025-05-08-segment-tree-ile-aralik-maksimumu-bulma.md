---
layout: post
title: Segment Ağacı ile Aralık Maksimumu Bulma
categories:
  - Program
tags:
  - cpp
  - sıralama
  - segment ağacı
  - aralık sorgusu
  - algoritma
---

Bu kod, bir dizi üzerinde aralık maksimumu sorgularını verimli bir şekilde gerçekleştirmek için bir Segment Ağacı kullanır. Segment Ağacı, bir dizi üzerinde tanımlanmış bir ağaç yapısıdır ve her düğüm, dizinin bir alt aralığını temsil eder. Bu sayede, belirli bir aralıktaki maksimum değeri bulma işlemi, dizinin tamamını taramak yerine ağaç üzerinde daha az sayıda düğümü ziyaret ederek gerçekleştirilebilir.

Bu kodda, Segment Ağacı kullanılarak, verilen bir dizideki belirli bir aralıktaki en büyük elemanı bulmak için `query` fonksiyonu ve bir elemanın değerini güncellemek için `update` fonksiyonu uygulanmaktadır. `build` fonksiyonu ise Segment Ağacını oluşturmak için kullanılır.

Aşağıdaki C++ kodu, Segment Ağacı kullanarak bir dizideki aralık maksimumunu bulmayı sağlar:

```c++
//Segment tree ile aralık maksimumu bulma
#include <bits/stdc++.h>

using namespace std;

int tree[100005*4],a[100005],n,t;

void build(int node,int start,int end){
	if(start==end){tree[node]=a[start];return ;}//yaprak düğüm(leaf) ulaştığımda node'un değerini belirlemek kolay oluyor.
	int mid=(start+end)/2;
	build(node*2,start,mid),build(node*2+1,mid+1,end);//sola ve sağa dallanıyoruz.
	tree[node]=max(tree[node*2],tree[node*2+1]);//node'un değeri soldan ve sağdan gelen değerlerin maksimumuna eşittir.
}

void update(int node,int start,int end,int x,int v){
	if(start>end || start>x || end<x)return ;//istenmeyen bir aralığa ulaştığımda daha fazla dallanmamak için 'kesiyorum'.
	if(start==x && end==x){
		tree[node]=v;//güncellemek istediğim indise ulaştığımda değerini v'ye eşitlerim.
		return ;
	}
	int mid=(start+end)/2;
	update(node*2,start,mid,x,v);//sola dallanıyoruz.
	update(node*2+1,mid+1,end,x,v);//sağa dallanıyoruz.
	tree[node]=max(tree[node*2],tree[node*2+1]);//bir node'un değeri soldan ve sağdan gelen değerlerin maksimumuna eşittir.
}

int query(int node,int start,int end,int l,int r){
	if(start>end || start>r || end<l)return -INT_MAX;//istenmeyen bir aralığa geldiğimiz için etkisiz elemanı döndürüyoruz.
	if(start>=l && end<=r)return tree[node];//istenen aralıkta node'un değerini döndürüyoruz.
	int mid=(start+end)/2;
	return max(query(node*2,start,mid,l,r),query(node*2+1,mid+1,end,l,r));//soldan ve sağdan gelen maksimumu cevap olarak döndürüyoruz.
}

int main(){
	scanf("%d",&n);
	for(int i=1;i<=n;i++)scanf("%d",&a[i]);
	scanf("%d",&t);//t tane sorgu gelecek
	while(t--){
		int tur;
		scanf("%d",&tur);//sorgunun türünü belirliyoruz.
		if(tur==1){
			int x,d;
			scanf("%d %d",&x,&d);//dizinin x. elemanını d'ye eşitle. (a[x]=d)
			update(1,1,n,x,d);
		}
		else{
			int l,r;
			scanf("%d %d",&l,&r);//dizinin l. elemanından r. elemanına kadarki maksimumu bul.
			printf("%d\n",query(1,1,n,l,r));
		}
	}
}
```