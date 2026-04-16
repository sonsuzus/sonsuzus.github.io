---
layout: post
title: Rekabetçi Programcı Akışlar ve Kesimler
math: true
excerpt_separator: "``"
categories:
  - Program
tags:
  - çizge
  - graph
  - maksimum-akış
  - maximum-flow
  - minimum-kesim
  - minimum-cut
  - ford-fulkerson
  - edmonds-karp
  - iki-parçalı-eşleşme
  - bipartite-matching
  - hall-teoremi
  - könig-teoremi
  - dilworth-teoremi
  - yol-kaplaması
  - c
  - programlama
  - algoritma
  - olimpiyat
  - yarışma
  - kodlama
  - matematik
  - kitap
---

Bu bölümde iki temel soru üzerine yoğunlaşıyoruz:

- **Maksimum akış (maximum flow):** Kaynak düğümden musluk düğüme gönderilebilecek en fazla akış miktarı nedir?
- **Minimum kesim (minimum cut):** Kaynak ile musluğu ayıran, toplam ağırlığı en küçük olan kenar kümesi hangisidir?

Her iki problem için girdi; **kaynak** (kendisine gelen kenar bulunmayan) ve **musluk** (kendisinden çıkan kenar bulunmayan) olmak üzere iki özel düğüm içeren, yönlü ve ağırlıklı bir çizgedir.

Bu iki sorunun cevabı her zaman birbirine eşittir. Maksimum akış ile minimum kesim sanki paranın iki yüzüdür; Ford-Fulkerson Algoritması hem maksimum akışı hem de minimum kesimi aynı anda çözer.
``

## 20.1 Ford–Fulkerson Algoritması

**Ford–Fulkerson Algoritması**, bir çizgedeki maksimum akışı bulan temel algoritmadır. Boş bir akışla başlar ve her adımda kaynaktan musluğa ek akış taşıyabilecek bir yol arar. Yol bulunamadığında maksimum akışa ulaşılmış olur.

### Ters Kenar Gösterimi

Algoritma çizgeyi özel bir biçimde temsil eder: her kenar için zıt yönde bir **ters kenar** eklenir. Bir kenarın ağırlığı o kenardan taşınabilecek kalan kapasiteyi gösterir. Başlangıçta orijinal kenarların ağırlığı tam kapasitelerine eşitken ters kenarların ağırlığı $0$'dır.

### Algoritmanın İşleyişi

Her turda algoritma, kaynaktan musluğa tüm kenarları pozitif ağırlıklı bir yol seçer. Yoldaki minimum kenar ağırlığı $x$ bulunur ve akış $x$ birim artırılır:

- Yol üzerindeki her kenarın ağırlığı $x$ azalır.
- Yol üzerindeki her ters kenarın ağırlığı $x$ artar.

Ters kenarların ağırlığını artırmak, önceki akış kararlarının geri alınabilmesini sağlar; bu sayede başka bir yolun daha yararlı olduğu durumda akış yeniden yönlendirilebilir.

### Örnek

Aşağıdaki çizgede kaynak 1. düğüm, musluk 6. düğümdür. Tüm kenar kapasiteleri gösterilmiştir. Algoritma şu turları izleyebilir:

| Tur | Seçilen Yol | Eklenen Akış |
|:---:|:-----------:|:------------:|
| 1 | $1 \to 2 \to 3 \to 6$ | 2 |
| 2 | $1 \to 2 \to 4 \to 5 \to 6$ | 3 |
| 3 | $1 \to 2 \to 3 \to 6$ | 2 |
| 4 | $1 \to 4 \to 5 \to 6$ | ... |

Kaynaktan musluğa pozitif ağırlıklı yol kalmadığında algoritma durur ve maksimum akış **7** olarak bulunur. Çözümdeki akış dağılımı $v/k$ (kapasite $k$'dan $v$ akış geçiyor) biçiminde gösterilir:

$$1 \xrightarrow{3/5} 2, \quad 1 \xrightarrow{4/4} 4, \quad 2 \xrightarrow{3/3} 3, \quad \ldots$$

### Yol Seçim Stratejileri

Ford-Fulkerson algoritması yolun *nasıl* seçileceğini belirtmez; yalnızca pozitif kenarlı bir yol bulunduğu sürece akışı artırmayı garantiler. Yol seçimi verimliliği doğrudan etkiler:

- **Derinlik öncelikli arama (DFS):** Kolay implementasyon, ama en kötü durumda her yol akışı 1 birim artırır.
- **Edmonds–Karp Algoritması:** Her turda kenar sayısı en az olan yolu seçmek için genişlik öncelikli arama (BFS) kullanır. Zaman karmaşıklığı $O(m^2 n)$'dir.
- **Ölçekleme Algoritması:** DFS kullanır; ancak yalnızca ağırlığı belirli bir eşiği aşan kenarlardan geçen yolları arar. Eşik değeri başta yüksek tutulur, yol bulunamadıkça ikiye bölünür. Zaman karmaşıklığı $O(m^2 \log c)$'dir ($c$ başlangıç eşiği).

Pratikte ölçekleme algoritması DFS tabanlı olduğu için daha kolay koda dökülebilir; her iki algoritma da yarışma problemleri için yeterince verimlidir.

### Minimum Kesimi Bulmak

Ford-Fulkerson tamamlandığında minimum kesim de elde edilmiş olur. Algoritma bittikten sonra:

- **$A$ grubu:** Kaynak düğümden pozitif ağırlıklı kenarlarla erişilebilen düğümler.
- **$B$ grubu:** Geri kalan tüm düğümler (musluk dahil).

Minimum kesim, orijinal çizgede $A$'dan $B$'ye geçen kenarlardır; bu kenarların tüm kapasitesi maksimum akış tarafından tam doldurulmuştur.

**Neden maksimum akış = minimum kesim?**

Bir akış, çizgedeki herhangi bir kesimin toplam ağırlığından büyük olamaz; çünkü akış kaynaktan musluğa ulaşmak için her kesimi geçmek zorundadır. Öte yandan Ford-Fulkerson, mümkün olan en büyük akışı üretir. Bu ikisi eşitlendiğinde akış maksimum, kesim ise minimum olur.

## 20.2 Ayrık Yollar

Pek çok çizge problemi maksimum akış problemine dönüştürülerek çözülebilir.

### Kenar Ayrık Yollar

Kaynaktan musluğa kadar olan, her kenarın yalnızca bir yolda kullanıldığı **kenar ayrık yolların** maksimum sayısını bulmak istiyoruz.

Çözüm doğrudur: tüm kenar kapasitelerini 1 olarak atarsak maksimum akış değeri, maksimum kenar ayrık yol sayısına eşittir. Maksimum akış hesaplandıktan sonra yollar açgözlü biçimde izlenebilir.

### Düğüm Ayrık Yollar

Kaynak ve musluk hariç her düğümün en fazla bir yolda geçtiği **düğüm ayrık yolların** maksimum sayısını bulmak için standart bir dönüşüm uygulanır: her düğüm $v$ ikiye bölünür:

- $v_{\text{giriş}}$: orijinal düğüme gelen tüm kenarları alır.
- $v_{\text{çıkış}}$: orijinal düğümden çıkan tüm kenarları verir.
- $v_{\text{giriş}} \to v_{\text{çıkış}}$ kapasitesi 1 olan bir kenarla bağlanır.

Bu dönüşüm, her düğümden en fazla 1 birim akış geçmesini zorlar; böylece maksimum akış, maksimum düğüm ayrık yol sayısına eşit olur.

## 20.3 Maksimum Eşleşme

**Maksimum eşleşme** (maximum matching) problemi, yönsüz bir çizgede her düğümün en fazla bir çifte ait olduğu, en büyük düğüm çifti kümesini bulmaktır. Genel çizgeler için polinom algoritmalar mevcuttur; ancak bunlar karmaşık ve yarışmalarda nadiren uygulanır. **İki parçalı çizgelerde** ise problem maksimum akışa indirgenerek kolaylıkla çözülür.

### İki Parçalı Eşleşme

İki parçalı çizgede düğümler sol ($L$) ve sağ ($R$) olmak üzere iki gruba ayrılır; kenarlar yalnızca $L$'den $R$'ye gider. Maksimum akış modeli şöyle kurulur:

1. Kaynak düğüm eklenir; kaynaktan tüm sol düğümlere kapasite 1'lik kenar çekilir.
2. Musluk düğüm eklenir; tüm sağ düğümlerden musluğa kapasite 1'lik kenar çekilir.
3. Orijinal çizgedeki her kenar kapasite 1 ile tutulur.

Bu yapıdaki maksimum akış değeri, iki parçalı çizgenin maksimum eşleşme büyüklüğüne eşittir.

### Hall'ın Teoremi

Hall'ın Teoremi, tüm sol (veya sağ) düğümleri kapsayan bir eşleşmenin var olup olmadığını belirler. $X$ sol düğümlerden oluşan herhangi bir alt küme, $f(X)$ ise $X$'in komşularının kümesi olsun. Tüm sol düğümleri kapsayan bir eşleşme vardır ancak ve ancak:

$$\forall X \subseteq L : |X| \leq |f(X)|$$

Başka bir deyişle, sol tarafın hiçbir alt kümesi sağ taraftaki komşularından daha kalabalık olmamalıdır. Bu koşul bozulduğunda, $X$ grubu neden mükemmel eşleşmenin imkânsız olduğunu doğrudan gösterir.

### König'in Teoremi

**Minimum düğüm kaplaması** (minimum vertex cover), çizgedeki her kenarın en az bir ucunun içinde bulunduğu en küçük düğüm kümesidir. Genel çizgede bu NP-hard'dır; ancak iki parçalı çizgede König'in Teoremi devreye girer:

$$\text{minimum düğüm kaplaması} = \text{maksimum eşleşme}$$

Dolayısıyla maksimum akış algoritması, minimum düğüm kaplamasını da doğrudan verir.

**Maksimum bağımsız küme** ise minimum düğüm kaplamasının tamamlayıcısıdır: birbirine kenarla bağlı iki düğümün aynı anda içinde bulunmadığı en büyük düğüm kümesi. İki parçalı çizgede büyüklüğü şöyle hesaplanır:

$$\text{maksimum bağımsız küme} = n - \text{maksimum eşleşme}$$

## 20.4 Yol Kaplaması

**Yol kaplaması**, çizgedeki her düğümün en az bir yola ait olduğu bir yol kümesidir. Yönlü asiklik çizgelerde minimum yol kaplaması, iki parçalı bir eşleşme çizgesi üzerinden maksimum akış ile çözülür.

### Düğüm Ayrık Yol Kaplaması

Her düğümün tam olarak bir yola ait olduğu kaplamayı bulmak için dönüşüm şöyle yapılır:

- Orijinal çizgenin her düğümü $v$, sol $v_L$ ve sağ $v_R$ olmak üzere ikiye bölünür.
- Orijinal çizgede $a \to b$ kenarı varsa eşleşme çizgesine $a_L \to b_R$ kenarı eklenir.
- Kaynak tüm sol düğümlere, tüm sağ düğümler musluğa bağlanır.

Eşleşme çizgesindeki maksimum eşleşmenin büyüklüğü $c$ ise minimum düğüm ayrık yol kaplamasının büyüklüğü:

$$n - c$$

olur; $n$ orijinal çizgedeki düğüm sayısıdır. Her eşleşme kenarı, orijinal çizgedeki bir "ardışık bağlantıyı" temsil eder; eşleşmeye giremeyen düğümler kendi başına birer tek elemanlı yol oluşturur.

### Genel Yol Kaplaması

Bir düğümün birden fazla yolda yer alabildiği genel yol kaplamasında minimum boyut, minimum düğüm ayrık yol kaplamasından küçük olabilir. Dönüşüm hemen hemen aynıdır; tek fark: orijinal çizgede $a$'dan $b$'ye herhangi bir yol (birden fazla kenardan oluşan) varsa eşleşme çizgesine $a_L \to b_R$ kenarı eklenir. Bu şekilde oluşturulan yollar, birden fazla adım atlayarak düğümleri birleştirebilir.

### Dilworth'un Teoremi

Bir **anti zincir**, yönlü asiklik çizgede hiçbir düğümden diğerine ulaşılamayan düğüm kümesidir. Dilworth'un Teoremi şunu söyler:

$$\text{minimum genel yol kaplaması} = \text{maksimum anti zincir büyüklüğü}$$

Bu teorem, maksimum akış yoluyla minimum yol kaplaması hesaplandığında aynı zamanda maksimum anti zincir büyüklüğünün de elde edildiğini garanti eder.
