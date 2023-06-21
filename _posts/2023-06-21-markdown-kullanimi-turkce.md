---
title: Markdown kullanım kılavuzu
author: sonsuz
date: 2023-06-22 00:02:00 +0300
categories: [Program,Rehber]
tags: [kılavuz,markdown,yardım,rehber,yazı]
---

## Markdown Kullanımı Türkçe

## Markdown Nedir, Ne Amaçla Kullanılır?

Markdown, yazılarımızı düz metin olarak yazmamıza imkan veren işaretleme/biçimlendirme dilidir (_markup language_).  Markdown'ın temel amacı, metnimizi kolayca hazırlamak ve düz metin haliyle bile metnin rahatça okunmasını sağlamaktır. 

## Örneklerle Sözdizim (_syntax_) kuralları

[Başlık](#başlık)

[Vurgulama](#vurgulama)

[Maddeleme ve Sıralama](#maddeleme-ve-sıralama)

[Bağlantı](#bağlantı)

[Tablo](#tablo)

[Resim](#resim)

[Kod](#kod)

[Alıntı](#alıntı)

### Başlık

```md
# 1. Başlık
## 2. Alt Başlık
### 3. Alt Başlık
```

# 1. Başlık

## 2. Alt Başlık

### 3. Alt Başlık

### Vurgulama

```md
**kalın** __kalın__

*italik* _italik_

**_kalın ve italik_**
```

**kalın** __kalın__

*italik* _italik_

**_kalın ve italik_**

### Maddeleme ve Sıralama

*Maddeleme:*

```md
- Maddde 1
- Madde 2
- Madde 3
  * Alt madde a
  * Alt madde b
    - Fıkra i
    - Fıkra ii
```

- Maddde 1
- Madde 2
- Madde 3
  * Alt madde a
  * Alt madde b
    - Fıkra i
    - Fıkra ii

*Sıralama:*

```md
1. Birinci
2. İkinci
```
1. Birinci
2. İkinci

### Bağlantı

```md
[Bağlantı](https://github.com/sonsuzus)

[Başlıklı Bağlantı](https://github.com/sonsuzus "GitHub Sayfam")
```

[Bağlantı](https://github.com/sonsuzus)

[Başlıklı Bağlantı](https://github.com/sonsuzus "GitHub Sayfam")

```md
[Referans 1][1]
[Referans 2][2]

YazıYazıYazıYazıYazıYazıYazıYazıYazıYazı
YazıYazıYazıYazıYazıYazıYazıYazı.

Referanslar sayfanın en sonuna yazılabilir. Sayfada gozukmez.

[1]: https://github.com/sonsuzus
[2]: https://github.com/
```

[Referans 1][1]

[Referans 2][2]

YazıYazıYazıYazıYazıYazıYazıYazıYazıYazı
YazıYazıYazıYazıYazıYazıYazıYazı.

[1]: https://github.com/sonsuzus
[2]: https://github.com/

### Tablo

```md
|   | Fiyat   | Adet  |
| --|:-------:| -----:|
| A | 1000TL  | 1     |
| B | 100TL   | 10    |
| C | 1TL     | 1000  |

```

|   | Fiyat   | Adet  |
| --|:-------:| -----:|
| A | 1000TL  | 1     |
| B | 100TL   | 10    |
| C | 1TL     | 1000  |

### Resim

#### Aynı Satıra Yazarak

```md
![alt yazı][resim adresi]

![Proje](son.jpg "GitHub")
```
 
![Proje](son.jpg)

#### Referans İle

```md
![Proje][resim]

[resim]: son.jpg "Resim Başlığı"
```
 
![Proje][resim]

[resim]: son.jpg "Resim Başlığı"

#### Resimin Boyutunu Değiştirerek (HTML Kullanarak)

```html
<img src="https://sonsuzus.github.io/img/son.jpg" alt="alt yazı" width="320">
```
 
<img src="https://sonsuzus.github.io/img/son.jpg" alt="Proje" width="320">

### Kod

#### Yazı İçinde Kod

```md
asdf asdf adf `kod` asdf asdf.
```

asdf asdf adf `kod` asdf asdf.

#### Kod Bloğu

\```\
asdf

\```

```md
asdf
```

### Alıntı

```md
> Alıntı 1

>> Alıntı 2

>>> Alıntı 3
```

> Alıntı 1

>> Alıntı 2

>>> Alıntı 3