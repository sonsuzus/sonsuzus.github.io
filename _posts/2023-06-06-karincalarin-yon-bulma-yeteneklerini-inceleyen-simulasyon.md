---
title: Karıncaların yön bulma yeteneklerini inceleyen program
author: sonsuz
date: 2023-06-06 18:37:00 +0300
categories: [Proje]
tags: [simulasyon,c#,unity]
---

## Özet

C# programlama dili ve Unity oyun motoru kullanılarak hazırlanan simülasyon aracılığıyla karıncaların koloni ve besin kaynağı arasında feromon izlerini takip etmesi incelenmiştir.

## Giriş

Karıncalar, tek başlarına hayatta kalamayan, basit görevleri üstlenen canlılardır. Ancak pek çok adedi bir araya geldiğinde bir bütün olarak organizma gibi davranırlar. Karıncalar, feromon adı verilen kimyasallar aracılığıyla yönlerini bulurlar. Hem feromon salgılarlar, hem de feromona duyarlı canlılardır.

Karıncalar her an az miktarda feromon salgılarlar ve etrafta rastgele hareket ederek yiyecek ararlar. Karıncalar feromon algılamaları halinde, feromonun yoğunluğuna bağlı olarak feromona yönelebilir veya rastgele gezmeye devam edebilir. Yiyecek bulan bir karıncanın feromon salgılaması artar. Bu durum yiyeceğe ulaşmış karıncaların dönüş yolundayken feromon izini güçlendirmesine ve daha çok karıncanın izi takip ederek yiyeceğe ulaşmasına sebep olur. 

Bir iz, en çok karıncanın en kısa sürede geçişiyle en verimli haline ulaşır. Dolayısıyla  zaman içerisinde besin kaynağı ve koloni arasındaki yol, iki nokta arasındaki en kısa yol haline gelecektir.

## Amaç

Projenin amacı, karıncaların yol bulma yeteneklerini simüle etmek, bu simülasyona bağlı olarak bireylerin, ilaçlama şirketlerinin karınca istilasına karşı uygulayabilecekleri çözümler üzerine kolaylaştırmalar sağlamaktır.

## Yöntem

Simülasyon, Unity oyun motoru ve C# dili kullanılarak hazırlanmıştır. 

Simülasyon; karınca, besin, feromon objelerinin prefabrikleri ve karınca oluşma noktası, besin oluşma noktası, engel çerçevesinde çalışmaktadır. Feromonun kaybolma süresi simülasyonu kullanan kişi
tarafından değiştirilebilmektedir.

Karınca, sonlu durum makinesi (finite-state machine) modeline göre hazırlanmıştır. 

Mavi yarıçap : içerisindeki feromonlar karınca tarafından algılanamaz.
Kırmızı yarıçap : mesafesindeki feromonlar karınca tarafından algılanabilir.
Sarı doğru parçaları arasında kalan açı (yeşil yay) : karıncanın feromon ve besin algılayabileceği açıklığı gösterir.
Bu üç parametre de simülasyonu kullanan kişi tarafından değiştirilebilmektedir.


Simülasyon içerisindeki maksimum feromon sayısı, besin sayısı, karınca sayısı belirlenir. Karıncalara ve feromonlara ait parametreler ayarlanır (simülasyon başlangıç halinde referans değerlere sahiptir). Simülasyon başlatılır ve sonuçlar gözlemlenir.

## Gözlem ve Sonuç 

Karıncalar simülasyonun başlamasıyla rastgele biçimde etrafa yayıldılar. Besine ulaşan ilk karınca koloniye dönerek besin kaynağı-koloni arasındaki feromon izini oluşturdu. Onu takip eden diğer karıncalar izin güçlenmesini sağladı.

Zaman içerisinde, izden saparak besine daha kısa yoldan ulaşan karıncalar oldu. Başka karıncaların da eşlik etmesiyle birlikte kısa olan feromon izi daha da güçlendi. İlk ve uzun olan iz kayboldu.

Farklı bir engel eklenerek oluşturulan
başka bir simülasyonda karşılaşılan sonuç

## Öneriler

* Karınca kolonisini oluşturan kraliçenin ve erkek karıncanın genetik faktörü eklenebilir.
* Evlerin detaylı modellenebilmesi için tırmanılabilir, altından geçilebilir, geçilemez olacak şekilde mobilya-eşya eklemeleri yapılabilir.
* Simülasyon 3 boyutlu hazırlanabilir.
* Karıncaların karakteristikleri yaşlanmayla beraber değişim göstermektedir. Karıncalar için yaşam döngüsü eklenebilir.
* Karıncalar için tehditler eklenebilir (başka koloniler, zehir madde…)
