---
layout: post
title: "Prolog’da Aritmetik: is Operatörüyle Sembolleri Sonuca Dönüştürmek"
math: true
categories: 
  - Program
tags: 
  - prolog
  - aritmetik
  - mantıksal-programlama
---

Programlamada aritmetik deyince çoğu dilde `x = 2 + 3` yazıp sonucu bekleriz. Prolog ise biraz daha felsefi davranır: Önce sembolleri, terimleri ve ilişkileri düşünür; hesaplama ise özel olarak istendiğinde yapılır. İşte `is` operatörü tam bu noktada sahneye çıkar: Matematiksel formülü sadece sembolik bir yapı olarak tutmak yerine, gerçekten hesaplar ve kesin sonucu yeni bir değişkene bağlar.
``
Prolog’da `2 + 3` ifadesi ilk bakışta basit görünür. Fakat Prolog için bu ifade, otomatik olarak 5’e dönüşen bir işlem değil; `+(2, 3)` şeklinde okunabilecek bir terimdir. Yani sembolik bir ağaç gibi düşünebiliriz. Eğer hesaplama yapılmasını istiyorsak `is` kullanırız:

```prolog
X is 2 + 3.
% X = 5
```

Burada sağ taraf, yani `2 + 3`, önce değerlendirilir. Sonra elde edilen sonuç sol taraftaki değişkene bağlanır. Matematiksel olarak söylemek gerekirse:

$X = 2 + 3 \Rightarrow X = 5$

Ama Prolog’daki `=` operatörü ile bu aynı şey değildir. `=` birleştirme, yani unification yapar. Hesaplama yapmaz. Bu ayrım Prolog öğrenirken küçük ama çok kritik bir virajdır.

| İfade | Prolog’un Davranışı | Sonuç |
|---|---|---|
| `X = 2 + 3` | Sembolik terimi bağlar | `X = 2+3` |
| `X is 2 + 3` | Sağ tarafı hesaplar | `X = 5` |
| `5 is 2 + 3` | Sağ tarafı hesaplayıp karşılaştırır gibi birleştirir | doğru |
| `2 + 3 is 5` | Sol taraf hesaplanabilir değişken/ sayı gibi uygun değildir | genellikle hata |

Bunu bir mutfak benzetmesiyle düşünelim. `2 + 3` bir yemek tarifi olsun. `=` operatörü tarifi deftere yapıştırır. `is` ise mutfağa girer, malzemeleri toplar ve tabağa gerçek yemeği koyar. Tarif başka, yemek başka!

Aşağıdaki örnek, sembolik bağlama ile gerçek hesaplama arasındaki farkı gösterir:

```prolog
sembolik_ornek(X) :-
    X = 10 * 4 + 2.

hesapli_ornek(X) :-
    X is 10 * 4 + 2.
```

İlk kural çağrıldığında `X`, `10*4+2` terimine bağlanır. İkinci kuralda ise işlem önceliği uygulanır ve sonuç `42` olur. Yani:

$10 \times 4 + 2 = 42$

`is` operatörünün önemli bir şartı vardır: Sağ taraftaki ifade hesaplanabilir olmalıdır. Yani içinde değeri bilinmeyen bir değişken varsa Prolog hesaplama yapamaz.

```prolog
?- X is Y + 1.
% Hata: Y henüz bir sayıya bağlı değil
```

Doğru kullanımda önce `Y` bağlanmalıdır:

```prolog
?- Y = 4, X is Y + 1.
% Y = 4,
% X = 5
```

Bu davranış, Prolog’un soldan sağa hedef çözme mantığıyla ilgilidir. Prolog önce `Y = 4` hedefini çözer, sonra `X is Y + 1` ifadesinde artık `Y` değerini bildiği için hesaplama yapabilir.

Karşılaştırma işlemlerinde de dikkatli olmak gerekir. `is`, sonuç üretmek içindir; iki aritmetik ifadenin değerini karşılaştırmak için `=:=` kullanılır.

| Amaç | Kullanım | Örnek |
|---|---|---|
| Sonuç hesapla ve bağla | `is` | `X is 7 * 6` |
| Sembolik birleştirme yap | `=` | `X = 7 * 6` |
| Aritmetik eşitlik kontrol et | `=:=` | `2 + 3 =:= 5` |
| Aritmetik eşitsizlik kontrol et | `=\=` | `2 + 3 =\= 6` |

Küçük bir alan hesabı örneği yazalım:

```prolog
alan_dikdortgen(Genislik, Yukseklik, Alan) :-
    Alan is Genislik * Yukseklik.

cevre_dikdortgen(Genislik, Yukseklik, Cevre) :-
    Cevre is 2 * (Genislik + Yukseklik).
```

Bu kurallar şu şekilde çalışır:

```prolog
?- alan_dikdortgen(5, 8, A).
% A = 40

?- cevre_dikdortgen(5, 8, C).
% C = 26
```

Teorik olarak burada yaptığımız şey, bir bağıntının içinde deterministik bir hesaplama adımı tanımlamaktır. `alan_dikdortgen(5, 8, A)` ilişkisi, $A = 5 \times 8$ formülünü kullanır ve `A` değişkenini kesin sonuç olan 40’a bağlar.

Özetle: Prolog’da matematiksel formül yazmak, onun otomatik hesaplanacağı anlamına gelmez. `=` sembolik dünyada kalır; `is` ise hesaplama motorunu çalıştırır. Eğer formülün gerçekten değerlendirilmesini ve sonucun yeni bir değişkene atanmasını istiyorsanız, doğru araç `is` operatörüdür. Prolog’un büyüsü de burada başlar: Sembollerle düşünür, gerektiğinde sayılarla hesaplar.
