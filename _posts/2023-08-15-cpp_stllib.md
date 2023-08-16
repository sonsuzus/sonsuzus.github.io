---
title:  C++ Standart şablon kütüphanesi (STL)
author: sonsuz
date: 2023-08-15 22:41:46 +0300
categories: [Program,C++]
tags: [cpp,programlama,stl,kütüphane]
---


## STL hakkında

Standart şablon kütüphanesi (Standart Templates Library - STL), hazır sınıf ve fonksiyon şablonları içerir. Bu şablonlar kullandıkları vektör, liste, kuyruk ve yığın gibi yaygın algoritma ve veri yapılarına erişim için fonksiyonlar tanımlar. STL şablon sınıflarından oluşturulduğundan, algoritmalar ve veri yapıları neredeyse her tür veriye uygulanabilir.

STL, birbiriyle bağlantılı olarak çalışan dört temel unsurdan oluşur:

* Konteynerler (Containers)
* Algoritmalar
* Tekrarlayıcılar (Iterators)
* Fonksiyonlar

## Konteynerler (Containers)

Konteynerler kütüphanesi, kuyruklar, listeler ve yığınlar gibi ortak veri yapılarının kolayca kullanılmasını sağlayan, genel bir sınıf şablonları ve algoritmalardan oluşur. Her biri farklı bir işlem grubu sağlamak üzere tasarlanmış üç konteyner sınıfı vardır:

* Sıralı konteynerler (Sequence containers)
* İlişkisel konteynerler (Associative containers)
* Sırasız İlişkisel konteynerler (Unordered associative containers)

Konteyner, elemanları için ayrılan depolama alanını yönetir ve doğrudan veya tekrarlayıcılar (iterators) yolulya elemanlarına erişim sağlamak için üye fonksiyonlar içerir.

Verilerin depolanmasında kullanılan konteynerlerin listesi aşağıdaki tabloda gösterilmektedir:

| Konteyner | Açıklama |
| --- | --- |
| bitset | Bir seri bit değeridir. |
| deque | Çift uçlu bir kuyruktur. |
| list | Linear bir listedir. |
| map | Her bir anahtarın tek bir değer ile eşleştiği anahtar/değer ikililerini depolar. |
| multimap | Her bir anahtarın iki veya daha fazla değer ile eşleştiği anahtar/değer ikililerini depolar. |
| multiset | Her bir elemanın benzersiz olması gerekmeyen bir set tanımlar. |
| priority\_queue | Öncelikli bir kuyruğu ifade eder. |
| queue | Bir kuyruğu ifade eder. |
| set | İçindeki her bir elemanın benzersiz olduğu bir gruptur. |
| stack | Bir yığını ifade eder. |
| vector | Dinamik bir dizidir. |

## Algoritmalar

Algoritmalar konteynerler içeriğinde yer alan verilere ilk değer verme, sıralama ve arama gibi işlemler yapabilirler.

## Tekrarlayıcılar (Iterators)

Tekrarlayıcılar, aşağı yukarı işaretçiler gibi davranan nesnelerdir. Bir konteyner içinde yer alan verilere sırasıyla erişim için tekrarlayıcıları kullanabiliriz. Tekrarlayıcıların beş farklı türü vardır:

| Tekrarlayıcı | Erişim yetkisi |
| --- | --- |
| Rastgele erişim | Değerleri depolar ve okur. Elemanlara rastgele erişilebilir. |
| Çift yönlü | Değerleri depolar ve okur. İleri ve geri hareket eder. |
| İleri | Değerleri depolar ve okur. Sadece ileri hareket eder. |
| Giriş | Değerleri okur fakat depolamaz. Sadece ileri hareket eder. |
| Çıkış | Değerleri depolar fakat okumaz. Sadece ileri hareket eder. |

İşaretçiler gibi kullanılan tekrarlayıcıları, artırabilir, azaltabilir ve \* işlemcisi ile kullanabiliriz. Yineleyiciler, çeşitli konteynerler tarafından tanımlanan yineleyici türü kullanılarak bildirilir. Tekrarlayıcıların bildirimi farklı konteynerler tarafından iterator ifadesi kullanılarak yapılır.

STL ile, ters tekrarlayıcıları da kullanabiliriz. destekler. Ters tekrarlayıcılar, bir dizi boyunca ters yönde hareket eden çift yönlü veya rastgele erişimli tekrarlayıcılardır. Bu nedenle, bir ters tekrarlayıcı bir dizinin sonunu gösterirse, bu tekrarlayıcının artırılması dizinin sondan bir önceki elemanını göstermesini sağlar.

## Fonksiyonlar

Konteynerler, algoritmalar ve tekrarlayıcıların yanı sıra karşılaştırma fonksiyonları ve fonksiyon nesneleri yer almaktadır.

`<functional>` başlık dosyası içindeki şablonlar, operator() tanımlayan nesneleri oluşturmamıza yardımcı olur. Bunlar fonksiyon nesneleri olarak adlandırılır ve birçok yerde fonksiyon işaretçileri yerine kullanılabilirler. `<functional>` başlık dosyasında içinde bildirilmiş önceden tanımlanmış birkaç fonksiyon nesnesi aşağıda gösterilmektedir:

En yaygın kullanılan fonksiyon nesnesi olan less, bir nesnenin diğerinden daha küçük olduğunu belirler. Fonksiyon nesneleri, STL algoritmalarında gerçek fonksiyon işaretçilerinin yerine kullanılabilir. Fonksiyon işaretçileri yerine fonksiyon nesnelerini kullanmak, STL'nin daha verimli kod üretmesini sağlar.
