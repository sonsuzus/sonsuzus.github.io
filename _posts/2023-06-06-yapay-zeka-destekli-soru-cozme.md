---
title: Yapay zeka destekli soru çözme uygulaması
author: sonsuz
date: 2023-06-06 18:11:00 +0300
categories: [Proje]
tags: [yapayzeka,uygulama,c]
---

## Amaç
Uygulama, öğrencilere yapay zeka destekli koçluk vererek günlük soru çözme miktarlarını
belirleyip bunları haftanın günlerine bölerek öğrencileri soru çözmeye motive eder. Ayrıca,
uygulama öğrencilere özelleştirilmiş öğrenme planları sunarak eksik oldukları konuları
belirlemelerine yardımcı olur. Yapay zeka destekli koçluk sistemi, öğrencilerin güçlü ve zayıf
yönlerini analiz eder ve onlara en etkili öğrenme stratejilerini sağlar. Bu sayede öğrenciler,
soru çözme miktarlarını ve çalışma sürelerini optimize ederek daha verimli bir şekilde
ilerlerler.

Uygulama tamamen açık kaynak kodlu bir biçimde yapılmıştır, bunun birden fazla sebebi
bulunmaktadır fakat benim için bunu yapmamın en önemli sebebi her zaman gelişime açık
olmasıdır.

## Öğrenci Arayüzü

Genel uygulamanın arayüzü, Visual Studio 2019 kullanılarak tasarlanmıştır. Öğrenci
arayüzü, kullanıcının soruları çözebilmesi için gerekli butonlar, metin kutuları ve diğer
kontrolleri içerir. Öğrenciler soru çözmeye başlamadan önce yapay zekanın yardımı ile
oluşturulan takvime göre yönlendirilerek testi çözmeye başlar. Testin soruları eğitimci
platformu tarafından girilen sorular arasından seçilir ve öğrencinin önüne sunulur.

## Eğitimci Arayüzü

Bu platform, yarışmacıların cevaplayacağı soruların yüklendiği, yarışmacı platformundan
bağımsız olan ve sadece eğitimcilerin kullanabildiği bir sistem olarak geliştirilmiştir. Bu
platformda yarışmacıların cevaplayacağı soruların tüm bilgilerine ulaşabilir, düzeltme
yapabilir veya yenisini ekleyebilirsiniz.

Her eğitimcinin kendine ve branşına özel bir uygulama ve giriş bilgisi bulunur. Eğitimcinin
kendisi hariç kimse izinsiz giriş yapamaz ve soruların güvenliği bozulmaz.

## Database

Yapmış olduğum platform Microsoft SQL Server destekli yapılmıştır, bu sayede tüm sorular
ve bilgiler kolay ve güvenli bi şekilde saklanır. Bu database IP adresi ve password ile
korunmaktadır. Yani dışarıdan bi giriş imkansızdır. Çoğu uygulama bu tarz güvenlik
açıklarına dikkat etmez fakat ben uygulamamda birincil şifreleme yöntemlerinden biri olan
Şifreleme ile Veri Koruma (Transparent Data Encryption - TDE) kullanarak verilerimin
güvenliğini sağladım. Database içerisinde her bir branş için ayrı table bulunmakta ve
bunların her birinin içerisinde neredeyse sınırsız soru kapasitesi bulunmaktadır.

## Sonuç Olarak;

Uygulama halihazırda işlevsel ve gayet düzgün şekilde çalışsa da açık kaynak kod desteği
ile birden çok geliştirici ve topluluk ile çok daha geliştirilebilir. Ayrıca soru yükleme işlemi
devam ettikçe uygulamada her seferinde daha daha fazla soruyla karşılaşacak olan öğrenci
başarısının gelişimini mutlaka zamanla görecektir.

Yazar: Yüksel Ege Erol