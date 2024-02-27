---
title:  Ballerina Programlama
author: sonsuz
date: 2024-02-28 01:00:15 +0300
categories: [Program]
tags: [ballerina,programlama,ilginç,yazılım,dil]
---

Ballerina aslında Java ve Go ile benzerlik gösteren bir dildir. Java ile dilin hedefleri ve amacı açısından, Go ile de eş zamanlı programlama hızlı derleme gibi özellikleri açısından benzerdir.

## Ballerina dilinde GİRİŞ ve ÇIKIŞ;

```ballerina
io:println(“Lütfen bir sayı girin:”);
string userInput = io:readLn();
```

`io:readln()` komutu ile giriş, `io:println()` komutu ile çıkış işlemi gerçekleşebilir.

## Ballerina dilinde DEĞİŞKENLER;

Ballerina dilinde değişkenler “var” ifadesi ile tanımlanır. Tip belirlenmiş ve belirlenmemiş 2 tanımlama yöntemi vardır. 

Örnekler;

Tip Belirtilmemiş: var isim : “Yuksel”;

Bu örnekte isim değişkeni otomatik olarak string değeri olarak alınacaktır.

Tip Belirtilmiş: var string isim : “Yuksel”;

Bu örnekte de belirtmiş olduk hiçbir fark yok aralarında.

*Değişken isimleri sayı ile başlayamaz*

## Ballerina dilinde DÖNGÜLER;

“while” döngüsü: Normal dillerdeki while ile aynı mantıkta çalışır, kullanım şekli:

```ballerina
int sayi=0;
while(sayi<5){
io:println(“Sayi:” +sayi);
sayi=sayi+1;
}
```

“foreach” döngüsü:

```ballerina
 int[] sayilar = [1,2,3,4,5];
foreach int sayi in sayilar {
	io:println(“Sayi:” +sayi);
}
```

## Ballerina dilinde KOŞULLAR;

“if” Koşulu:

```ballerina
int x=10;
If(x>0)  {
Io:println(“Pozitif sayı”);
}
```

“else if” Koşulu:

```ballerina
int y=-5;
If(y>0){
	io:println(“Pozitif sayı”);
}else if (y<0){
	Io:println(“Negatif sayı”);
}
```

“else” Koşulu;

```ballerina
If(y>0){
	io:println(“Pozitif sayı”);
}else if (y<0){
	Io:println(“Negatif sayı”);
}
else{
	io:println(“Sayı sıfıra eşit”);
}
```
