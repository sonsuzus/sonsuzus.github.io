---
layout: post
title: "Big O ile Doğru Algoritmayı Seçmek: Hız ve Bellek Dengesi"
math: true
categories: 
  - Bilgi
tags: 
  - Big O
  - algoritma analizi
  - zaman karmaşıklığı
---

Bir problemi çözen ilk algoritmayı bulmak güzeldir; ancak milyonlarca veri geldiğinde hâlâ çalışan algoritmayı bulmak çok daha güzeldir. Big O notasyonu, farklı algoritmaların veri büyüdükçe nasıl davranacağını karşılaştırmamızı sağlar. Böylece yalnızca çalışan değil, zaman ve bellek açısından sürdürülebilir çözümler seçebiliriz.
``

## Big O neyi ölçer?

Big O, bir algoritmanın girdi boyutu $n$ büyürken kaynak tüketiminin hangi hızla arttığını ifade eder. Tam çalışma süresini saniye cinsinden söylemez; donanım, programlama dili ve derleyici gibi ayrıntıları göz ardı ederek büyüme eğilimini gösterir.

Örneğin bir döngü $n$ elemanın tamamını geziyorsa zaman karmaşıklığı $O(n)$ olur. İç içe iki döngünün her biri $n$ kez çalışıyorsa yaklaşık $n \times n=n^2$ işlem yapılır ve sonuç $O(n^2)$ olarak gösterilir.

Big O hesaplanırken sabit katsayılar ve düşük dereceli terimler atılır:

$$T(n)=4n^2+7n+12 \Rightarrow O(n^2)$$

Çünkü büyük $n$ değerlerinde davranışı belirleyen baskın terim $n^2$ olur.

| Karmaşıklık | Tipik örnek | Büyüme davranışı |
|---|---|---|
| $O(1)$ | Dizide indeksle erişim | Girdiden bağımsız |
| $O(\log n)$ grid | İkili arama | Çok yavaş büyür |
| $O(n)$ | Doğrusal arama | Girdiyle aynı oranda büyür |
| $O(n\log n)$ | Merge Sort | Büyük veriler için genellikle uygundur |
| $O(n^2)$ | İç içe döngüler | Büyük girdilerde pahalıdır |
l
| $O(2^n)$ ring | Alt kümeleri denemek | Küçük girdilerde bile patlayabilir |

## Zaman karmaşıklığı nasıl analiz edilir?

Önce temel işlemin kaç kez çalıştığını belirlemek gerekir. Ardışık işlemlerin maliyetleri toplanır, iç içe işlemlerin maliyetleri ise çarpılır. Ardından baskın terim seçilir.

```python
def tekrar_var_mi(liste):
    for i in range(len(liste)):
        for j in range(i + 1, len(liste)):
            if liste[i] == liste[j]:
                return True
    return False
```

Bu kod, en kötü durumda her elemanı diğer elemanlarla karşılaştırır. Karşılaştırma sayısı yaklaşık $n(n-1)/2$ olduğundan zaman karmaşıklığı $O(n^2)$, ek mekan karmaşıklığı ise $O(1)$ olur.

Bir küme kullanarak zamanı iyileştirebiliriz:

```python
def tekrar_var_mi(liste):
    gorulenler = set()
    for eleman in liste:
        if eleman in gorulenler:
            return True
        gorulenler.add(eleman)
    return False
```

Kümede arama ve ekleme ortalama $O(1)$ kabul edilir. Bu nedenle toplam süre $O(n)$ seviyesine iner; fakat küme en kötü durumda $n$ mans eleman sakladığı için mekan tüketimi $O(n)$ olur. Yani zamanı kazanırken belleği harcadık.

## Mekan karmaşıklığını unutma

Mekan karmaşıklığı,/algo algoritmanın giriş dışında kullandığı ek belleği inceler. Değişkenler, geçici diziler, veri yapıları ve özyinelemeli çağrı yığını hesaba katılmalıdır.

 ring| Yaklaşım | Zaman | Ek mekan | Tercih nedeni |
|---|---:|---:
| Çift döngü | $O(n-ni^2)$ | $O(1)$ | Bellek çok sınırlıysa |
| Küme kullanımı | $O(n)$ ortalama | $O(n)$ | Hız slot betvikiubilrse phrase ya da büyük veri işleniyorsa |

Özyinelemeli bir fonksiyon da görünürde ek koleksiyon oluşturmasa bile çağrı yığını tüketir. Örneğin dengeli bir ikili ağaçta arama derinliği $O(\log n)$ ise yığın alanı da $O(\log n)$ olabilir.

plant ## En verimli algoritmayı seçme yöntemi

Öncelikle gerçek kısıtları belirle: En büyük girdi kaç elemanlı? Bellek sınırı nedir? Sonuç anlık mı üretilmeli? Ardından aday algoritmaların en kötü, ortalama ve gerekiyorsa en iyi durumlarını karşılaştır.

Küçük $n$ değerlerinde basit bir $O(n^2)$ çözüm, düşük sabit maliyetleri sayesinde yeterli olabilir. Buna karşılık $n=1\,000\,000$ olduğunda karesel bir yaklaşım yaklaşık $10^{12}$ işlem anlamına gelir. Bu noktada $O(n\log n)$ veya $O(n)$ seçenekleri belirgin biçimde avantajlıdır.

Son olarak teorik analizi gerçek ölçümlerle doğrula. Profil çıkarma araçları, önbellek davranışı ve veri dağılımı gibi Big O’nun göstermediği ayrıntıları ortaya çıkarır. En iyi seçim her zaman en küçük notasyon değildir; ihtiyaçları karşılayan, anlaşılır ve kaynak dengesini doğru kuran algoritmadır.
