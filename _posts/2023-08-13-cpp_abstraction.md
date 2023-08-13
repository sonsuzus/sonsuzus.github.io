---
title:  C++ Soyutlama
author: sonsuz
date: 2023-08-13 19:13:09 +0300
categories: [Program,C++]
tags: [cpp,programlama,nesne,soyutlama,oop]
---



# Soyutlama

Soyutlama, kullanıcıya yalnızca ilgili ayrıntıların gösterilmesi ve ilgisiz ayrıntıların gizlenmesi olarak ifade edilebilir. C++'da kullanılan temel soyutlama sistemleri sınıflar, sınıflar yoluyla yapılan kalıtım ve şablonlardır.

Soyutlama, genellikle veri soyutlama amacıyla kullanılır. Veri soyutlama kullanımı için, içinde en az bir adet saf sanal fonksiyon bulunan soyut (abstract) bir sınıf oluşturulur. Bir sınıf içinde en az bir adet saf sanal fonksiyon tanımlanırsa, bu sınıf soyut (abstract) sınıf haline gelir. Bu soyut sınıf kendisinden türetilen alt sınıfların ortak değişkenlerini ve fonksiyonlarını içerir. Soyut bir sınıftan türetilen tüm sınıflarda sanal fonksiyon bildirimi yeniden yapılmalıdır. Eğer yapılmazsa, türetilen sınıflarda soyut sınıf olarak kabul edilir. Soyut sınıflar saf sanal fonksiyon dışında normal fonksiyonlar ve değişkenler içerebilir.

Soyut sınıfları kullanılarak geliştirilen yazılımlarda değişiklik yapmak gerektiğinde, soyut sınıflarda yer alan ve türetilen sınıflar tarafından kullanılan private erişim özelliğine değişkenlerin değiştirilmesi yeterli olmaktadır. Soyut sınıflarda bildirimi yapılan private değişkenler veri güvenliğini artırır ve program kodlarının daha pratik yazılmasını sağlar.
