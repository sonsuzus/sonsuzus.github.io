---
title:  Sayı kartları Sorusu ve Çözümü
author: sonsuz
date: 2023-06-09 19:16:13 +0300
categories: [Blog]
tags: [zeka sorusu,mantık,sayı,matematik]
---

Üzerinde birden onikiye kadar sayıları yazılı olduğu oniki tane kartımız var. Bu kartla Anaximander, Boethius, Confucius ve Diogenes arasında eşit olarak paylaştırılıyor, yani her biri üç tane kart alıyor. Sonra sırayla aralarında şöyle bir konuşma geçiyor.


Anaximander: Benim kartların birinde 8 var.


Beothius: Kartlarımın hepsinde asal sayılar var.


Confucius: Benim sayılarımın hiçbiri asal değil. Ayrıca üçünün de ortak bir asal çarpanı var.


Diogenes: O zaman her birinizin hangi kartlara sahip olduğunu biliyorum.


Herkes doğruyu söylemişse Anaximander’in kartlarında hangi sayılar vardır?


## Çözüm

Anaximander’in kartlarından birinde 8 sayısı var.


Boethius’un kartlarında sadece asal sayılar varmış. Yani 2, 3, 5, 7, 11. 


Confucius’un kartlarında da asal olmayan ve ortak bir asal çarpanı olan üç sayı varmış. Bunlar da 4, 6, 9, 10 ve 12 olabilir. 1’in asal çarpanı olmadığı için listede yok. 8 sayısı Anaximander’in kartlarında ve 2 sayısı da asal olduğundan Confucius’un kartlarında olamaz. 


Bu bilgilere bakan Diogenes kimde hangi sayıların olduğunu bulabiliyor. 


Şimdi bu bilgilere biraz daha bakalım. Boethius’un kartlarında üç tane asal olduğuna göre kalan iki asal Anaximander’de ve Diogenes’te olmalı, çünkü Confucius’ta hiç asal yok. Peki bu asalların dağılımı nasıl olmalı ki Diogenes kendi kartlarına baktığında kimde hangi sayıların olduğunu görebiliyor? 


Dikkat edersek asallarla ilgili Boethius’tan başka bilgi veren yok. Yani eğer Anaximander’de asal sayı varsa, Diogenes hangi asal sayıların Boethius’ta hangi asal sayının veya asal sayıların Anaximander’de olduğunu bilemez. O zaman kalan iki asal sayı da Diogenes de olmalı. Bu şekilde Diogenes Boethius’un üç sayısını da bilebilir. 


Şimdi kalan sayılara bakalım. 8 sayısı Anaximander’deydi. O zaman 1, 4, 6, 9, 10, 12 sayıları kaldı. 1 sayısı kimde olmalı?


1 sayısı eğer Diogenes’te olsa, o zaman Diogenes 4, 6, 9, 10 ve 12 sayılarının hangi üçünün Confucius’ta, hangi ikisinin de Anaximander’de olduğunu bulamaz. Olasılıklara bakalım:


Anaximander: 4, 10 Confucius: 6, 9, 12 (ortak asal çarpan 3)


Anaximander: 9, 12 Confucius: 4, 6, 10 (ortak asal çarpan 2)


ve daha başka dağılımlar da bulunabilir. 


Demek ki 1 sayısı Diogenes’te olamaz. 1 sayısı Anaximander’de.


Artık dağıtmamız gereken beş sayı kaldı. 4, 6, 9, 10, 12. Bu sayıların biri Anaximander’de, üçü Confucius’ta, sonuncusu da Diogenes’te. Hangi dağılımda Diogenes herkesin sayılarını bilebilir?


Bunun için şöyle bir tablo yapayım:




|  |  |  |
| --- | --- | --- |
| Anaximander | Confucius | Diogenes |
| 10 ya da 9 | (6, 9, 12) ya da (6, 10, 12) | 4 |
| 9 | 4, 10, 12 | 6 |
| 12, 6, 4 ya da 10 | (4, 6, 10) ya da (4, 10, 12) ya da (6, 10, 12) ya da (4, 6, 12) | 9 |
| 4 ya da 9 | (6, 9, 12) ya da ((4, 6, 12) | 10 |
| 9 | (4, 6, 10) | 12 |


Bu tabloyu Diogenes sütunundan okumaya başlayalım. Eğer Diogenes’te 4, 9 ya da 10 sayılarından biri varsa kalan sayıların dağılımı birden fazla şekilde yapılabiliyor. Bu durumda Diogenes diğerlerinin sayılarını bilemez. Buna karşın Diogenes’in sayıları 6 ya da 12 ise kalan sayıların dağılımı tek şekilde yapılabiliyor. Bu dağılımların ikisinde de Anaximander 9 sayısına sahip oluyor.


Sonuçta Diogenes herkesin sayılarını biliyor ama biz problemi çözünce Diogenes’in hiçbir sayısını bilemiyoruz. Elindeki sayıları bilebileceğimiz tek kişi de **Anaximander** ve soruda da onun sayıları sorulmuş. **1, 8, 9**.


Anaximander de diğerlerinin sayılarını bilemez, ne asal sayıların ne de asal olmayan sayıların dağılımı hakkında bir bilgiye sahip değil. 


Boethius kalan iki asal sayının Diogenes’te olduğunu bulabilir ama Diogenes’in son sayısını bulamaz. 


Aynı şekilde Confucius da Diogenes’in asal olmayan sayısını bilir ama asalların nasıl dağıldığını bulamaz.


