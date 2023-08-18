---
title:  Python Paket kurulumları (pip)
author: sonsuz
date: 2023-08-18 13:15:45 +0300
categories: [Program,Python]
tags: [python,programlama,paket,kütüphane,modül,pip]
---

## Paket programları yükleme

Bir sanal ortamı oluşturup aktif hale getirdikten sonra, Python ortamında çalışan paket programları yükleyebiliriz. Python ortamında yüklenebilecek [paket programların listesi](https://pypi.org/) (Python Package Index) adresinde yer almaktadır.

Python kurulumunu yaptığımızda bazı paket programlar otomatik olarak yüklenir. Bunlardan birisi de paket program yüklememizi sağlayan pip kütüphanesidir. Aşağıdaki komutları sırasıyla çalıştırdığımızda, env01 sanal ortamındaki script dizinine geçip, pip paketine ait komut ve seçenekleri görebiliriz:

```sh
cd C:\Users\Mehmet\AppData\Local\Programs\Python\Python39 # Python kurulum dizinine geçiş
cd envs\env01\Scripts # Sanal ortam script dizinine geçiş

activate # Sanal ortamı aktif hale getirme

pip # Python komutu


```

Windows işletim sisteminde komut istemini (cmd) açarak aşağıdaki komutları sırasıyla çalıştıralım:

![](python/paket001.png)

Sanal ortam içinde requests adlı paketi kurmak için aşağıda gösterilen komutu kullanabiliriz:

```sh
pip install requests # Python komutu


```

![](python/paket002.png)

Bu komutu kullandığımızda, requests program paketi ile birlikte bu paketin kullanılması için gerekli olan certifi, chardet, idna ve urllib paketleri de birlikte kurulur.

Kurulum tamamlandığında, orjinal Python programı içinde yer alan paketlerin içinde bulunduğu dizin yapısı aşağıdaki şeklin sol tarafında, env01 sanal kütühanesi içinde kurulu paketlerin içinde bulunduğu dizin yapısı ise aşağıdaki şeklin sağ tarafında gösterilmektedir. Dizin yapısında görüldüğü gibi, yapılan kurulum işlemi sadece env01 sanal ortamı içindeki paketleri etkilemiştir. Pembe ve mavi renkli çerçeve ile gösterilen paketler kurulumu yapılan paketleri göstermektedir.

![](python/paket003.png)

## Paket programların sürümünü yükseltme

Sanal ortam içinde kurulu olan herhangi bir paketin sürümünü yükseltmek için, aşağıda gösterilen komutu yapısını kullanabiliriz:

```sh
pip install --upgrade paket-adı # Python komut yapısı

pip install --upgrade requests # Örnek Python komutu


```

## Paket programların belirli bir sürümünü kurma

Sanal ortam içinde herhangi bir paketin belirli bir sürümünü kurmak için, aşağıda gösterilen komutu yapısını kullanabiliriz:

```sh
pip install paket-adı==x.xx.x # Python komut yapısı

pip install requests==2.18.4 # Örnek Python komutu


```

## Kurulu olan paket programları listeleme

Sanal ortam içinde kurulu paket programları listelemek için, aşağıda gösterilen komutu yapısını kullanabiliriz:

```sh
pip list # Python komut yapısı


```

![](python/paket004.png)

## Kurulu olan bir paket program hakkında bilgi alma

Sanal ortam içinde kurulu herhangi bir paket hakkında bilgi almak için, aşağıda gösterilen komutu yapısını kullanabiliriz:

```sh
pip show paket-adı # Python komut yapısı

pip show requests # Örnek Python komutu


```

![](python/paket005.png)

Yukarıdaki komut requests program paketi hakkında bilgi almamızı, paketin çalışması için hangi paketlere ihtiyaç duyulduğunu ve paketin hangi paketlerin çalışması için gerekli olduğunu gösterir.

## Paket programları kaldırma

Sanal ortam içinde herhangi bir paketi kaldırmak için, aşağıda gösterilen komutu yapısını kullanabiliriz:

```sh
pip uninstall paket-adı # Python komut yapısı

pip uninstall requests # Örnek Python komutu


```

## PIP paket kurulum kütüphanesinin kendisini güncelleme

Sanal ortam içinde PIP paket kurulum kütüphanesinin kendisini güncellemek için, aşağıda gösterilen komutu yapısını kullanabiliriz:

```sh
python -m pip install --upgrade pip


```
