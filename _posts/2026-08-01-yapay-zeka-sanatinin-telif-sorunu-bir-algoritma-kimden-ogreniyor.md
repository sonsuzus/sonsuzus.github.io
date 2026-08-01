---
layout: post
title: "Yapay Zekâ Sanatının Telif Sorunu: Bir Algoritma Kimden “Öğreniyor”?"
math: true
categories: 
  - Bilgi
tags: 
  - yapay zekâ
  - telif hakkı
  - dijital sanat
---

Bir ressam binlerce tablo görüp kendi üslubunu geliştirirse buna eğitim deriz. Bir yapay zekâ aynı tablolarla eğitildiğinde ise sorular değişir: Öğreniyor mu, kopyalıyor mu, yoksa devasa bir istatistik makinesini mi çalıştırıyor? Üretken yapay zekâ sanatı, özgünlüğü yalnızca estetik açıdan değil; hukuk, emek ve yaratıcılık bakımından da yeniden düşünmemizi gerektiriyor.
``

## Model gerçekte ne öğreniyor?

Bir görüntü modeli, eğitim eserlerini küçük bir albüm gibi içinde saklamak zorunda değildir. Genellikle görseller ile metinler arasındaki örüntüleri parametrelerine dağıtır. Basitleştirilmiş hâliyle model, verilen metne uygun görüntünün olasılığını öğrenmeye çalışır:

$$\theta^* = \arg\min_\theta \sum_{i=1}^{n} L(f_\theta(x_i), y_i)$$

Burada $x_i$ eğitim girdisini, $y_i$ hedefi, $L$ hata ölçüsünü ve $\theta$ milyarlarca model parametresini temsil eder. Eğitim sonucunda belirli bir tablonun piksellerinden çok; renk, kompozisyon, biçim ve kavram ilişkileri ağırlıklara yansır.

Ancak “model yalnızca örüntü öğrenir” demek tartışmayı bitirmez. Aşırı öğrenme veya ezberleme gerçekleşirse model, eğitim verisine şaşırtıcı derecede benzeyen çıktılar üretebilir. Dolayısıyla öğrenme ile kopyalama arasında keskin bir duvar değil, benzerlik derecelerinden oluşan sisli bir bölge vardır.

| Durum | İnsan sanatçı | Yapay zekâ modeli |
|---|---|---|
| Kaynaktan etkilenme | Hafıza ve yorum aracılığıyla | İstatistiksel parametreler aracılığıyla |
| Niyet | Genellikle bilinçli | Bilinç veya amaç yok |
| Eser seçimi | Sanatçı karar verir | Veri setini geliştirici seçer |
| Sorumluluk | Sanatçıya yüklenebilir | Kullanıcı, geliştirici ve platform arasında dağılır |
| Birebir benzerlik | İhlal riski doğurabilir | Aynı risk, ezberleme yoluyla oluşabilir |

## Hukuk hangi noktada devreye giriyor?

Telif hukuku çoğu ülkede fikirleri, tarzları veya genel teknikleri değil; özgün eserlerdeki somut ifade biçimini korur. “Empresyonist bir gün batımı” fikri tek başına korunmazken belirli bir tablonun ayırt edici kompozisyonunun kopyalanması sorun yaratabilir.

Yapay zekâ tartışmasının iki ayrı aşaması bulunur:

1. **Eğitim girdisi:** Telifli eserlerin izin alınmadan veri setine eklenmesi hukuka uygun mudur?
2. **Üretilen çıktı:** Sonuç, mevcut bir eserin korunan unsurlarına esaslı biçimde benziyor mu?

Yanıt ülkeye göre değişir. Bazı hukuk sistemlerinde metin ve veri madenciliği istisnaları bulunurken bazılarında adil kullanım, lisans veya hak sahibinin itiraz imkânı tartışılır. Ayrıca tamamen makine tarafından oluşturulan bir çıktının telif sahibi olup olamayacağı belirsizdir. Birçok yaklaşım, koruma için anlamlı insan yaratıcılığı arar. İyi yazılmış bir komut tek başına her zaman yeterli görülmeyebilir; kapsamlı seçme, düzenleme ve rötuş ise insan katkısını güçlendirebilir.

## Özgünlük matematiksel olarak ölçülebilir mi?

Benzerlik denetimi yararlı olsa da hukuki hüküm vermez. Örneğin iki görselin özellik vektörleri arasındaki kosinüs benzerliği şöyle hesaplanabilir:

$$S(A,B)=\frac{A\cdot B}{\|A\|\|B\|}$$

Aşağıdaki örnek, iki özellik vektörünü karşılaştıran basit bir denetim aracıdır:

```python
import numpy as np

def cosine_similarity(a, b):
    a, b = np.array(a), np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

reference = [0.2, 0.8, 0.4]
generated = [0.3, 0.7, 0.5]
print(cosine_similarity(reference, generated))
```

Sonucun yüksek olması görsel yakınlığa işaret eder; fakat bağlamı, parodiyi, ortak sanat geleneğini veya korunan ifade unsurlarını tek başına değerlendiremez. Mahkeme salonu henüz bir NumPy fonksiyonuyla yönetilmiyor!

## Felsefi düğüm: Yaratıcılık kimin?

Romantik görüş, sanat eserini bireysel dehanın benzersiz ürünü sayar. Daha ilişkisel bir yaklaşım ise her eserin geçmiş eserler, kültür ve araçlarla kurulan diyaloğun sonucu olduğunu savunur. Yapay zekâ bu ikinci yaklaşımı görünür kılar; fakat eğitim verisini sağlayan sanatçıların emeğini görünmezleştirme riski taşır.

Bu nedenle özgünlüğü “hiçbir şeye benzememek” şeklinde değil; kaynaklarla şeffaf, dönüştürücü ve sorumlu bir ilişki kurmak olarak tanımlamak daha işlevseldir. Lisanslı veri setleri, sanatçıların veri dışı kalma seçenekleri, kaynak açıklaması ve gelir paylaşımı teknik ilerlemeyi durdurmaz. Aksine, algoritmanın öğrendiği insanların masada kaldığı daha adil bir sanat ekosistemi oluşturur.
