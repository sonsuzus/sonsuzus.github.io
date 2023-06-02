# Markdown Kullanımı Türkçe

## Markdown Nedir, Ne Amaçla Kullanılır?

Markdown, yazılarımızı düz metin olarak yazmamıza imkan veren işaretleme/biçimlendirme dilidir (_markup language_).  Markdown'ın temel amacı, metnimizi kolayca hazırlamak ve düz metin haliyle bile metnin rahatça okunmasını sağlamaktır. 

## Örneklerle Sözdizim (_syntax_) kuralları

[Başlık](#Başlık)

[Vurgulama](#Vurgulama)

[Maddeleme ve Sıralama](#Maddeleme-ve-Sıralama)

[Bağlantı](#Bağlantı)

[Tablo](#Tablo)

[Resim](#Resim)

[Kod](#Kod)

[Alıntı](#Alıntı)


### Başlık

```
# 1. Başlık
## 2. Alt Başlık
### 3. Alt Başlık
```

# 1. Başlık
## 2. Alt Başlık
### 3. Alt Başlık

### Vurgulama

```
**kalın** __kalın__

*italik* _italik_

**_kalın ve italik_**
```

**kalın** __kalın__

*italik* _italik_

**_kalın ve italik_**

### Maddeleme ve Sıralama

*Maddeleme:*

```
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

```
1. Birinci
2. İkinci
```
1. Birinci
2. İkinci


### Bağlantı

```
[Bağlantı](https://github.com/sonsuzus)

[Başlıklı Bağlantı](https://github.com/sonsuzus "GitHub Sayfam")
```

[Bağlantı](https://github.com/sonsuzus)

[Başlıklı Bağlantı](https://github.com/sonsuzus "GitHub Sayfam")


```
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
```
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


### Resim/Görsel
```
Resim: 
![alt yazı][resim]

[resim]: https://www.freeiconspng.com/uploads/github-logo-icon-0.png"Resim Başlığı"
```


Resim: 
![alt yazı][resim]

[resim]: https://www.freeiconspng.com/uploads/github-logo-icon-0.png "Resim Başlığı"

### Kod

#### Yazı İçinde Kod
```
asdf asdf adf `kod` asdf asdf.
```

asdf asdf adf `kod` asdf asdf.

#### Kod Bloğu
\```\
asdf

\```

```
asdf
```

### Alıntı
```
> Alıntı 1

>> Alıntı 2

>>> Alıntı 3
```
> Alıntı 1

>> Alıntı 2

>>> Alıntı 3

{% include footer.html %}

{% include analytics.html %}
