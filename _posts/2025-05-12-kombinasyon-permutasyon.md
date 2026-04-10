---
layout: post
title: Permütasyon ve Kombinasyon Örnekleri
categories:
  - Bilgi
tags:
  - permütasyon
  - kombinasyon
  - matematik
  - olimpiyat
math: true
excerpt_separator: "``"
redirect_from:
  - /posts/kombinasyon-permutasyon/
---



Bu belge, permütasyon ve kombinasyon kavramlarını kısaca açıklamakta ve örnek sorularla pekiştirmektedir.

## Permütasyon (Sıralama)

Permütasyon, belirli bir kümenin elemanlarının **farklı sıralanışlarının** sayısını ifade eder. Sıralamanın önemli olduğu durumlarda permütasyon kullanılır.
``
$$n$$ elemanlı bir kümenin $$r$$ elemanlı permütasyonlarının sayısı $$P(n, r)$$ veya $$_nP_r$$ ile gösterilir ve şu formülle hesaplanır:

$$P(n, r) = \frac{n!}{(n-r)!}$$

Burada $$n!$$ (n faktöriyel), $$n \times (n-1) \times (n-2) \times \dots \times 1$$ anlamına gelir.

**Önemli Not:** Eğer kümenin tüm elemanları sıralanıyorsa ($$r=n$$), bu durumda $$P(n, n) = n!$$ olur.

### Tekrarlı Permütasyon

Eğer sıralanacak elemanlar arasında birbirinin aynı olanlar varsa, bu durumda tekrarlı permütasyon kullanılır. $$n$$ elemanın $$n_1$$ tanesi birinci türden, $$n_2$$ tanesi ikinci türden, ..., $$n_k$$ tanesi $$k$$. türden aynı ise (yani $$n_1 + n_2 + \dots + n_k = n$$), bu $$n$$ elemanın farklı sıralanışlarının sayısı:

$$\frac{n!}{n_1! \cdot n_2! \cdot \dots \cdot n_k!}$$

formülü ile hesaplanır.

### Örnek Sorular (Permütasyon)

**Soru 1:** A, B, C harfleri bir sıra üzerinde kaç farklı şekilde sıralanabilir?

**Çözüm:**
Burada 3 farklı harfimiz var ve hepsini sıralıyoruz ($$n=3, r=3$$).
$$P(3, 3) = 3! = 3 \times 2 \times 1 = 6$$
Farklı sıralanışlar: ABC, ACB, BAC, BCA, CAB, CBA.

**Soru 2:** 5 kişilik bir arkadaş grubu, 3 kişilik bir sıraya kaç farklı şekilde oturabilir?

**Çözüm:**
Burada 5 kişi arasından 3 kişiyi seçip sıralıyoruz ($$n=5, r=3$$).
$$P(5, 3) = \frac{5!}{(5-3)!} = \frac{5!}{2!} = \frac{5 \times 4 \times 3 \times 2 \times 1}{2 \times 1} = 5 \times 4 \times 3 = 60$$
Farklı şekilde oturabilirler.

**Soru 3:** "MATEMATİK" kelimesinin harfleri yer değiştirilerek anlamlı ya da anlamsız 9 harfli kaç farklı kelime yazılabilir?

**Çözüm:**
"MATEMATİK" kelimesinde toplam 9 harf bulunmaktadır.
Tekrar eden harfler:
- M: 2 tane
- A: 2 tane
- T: 2 tane
Diğer harfler (E, İ, K) birer tanedir.
Bu bir tekrarlı permütasyon problemidir.
Toplam sıralama sayısı = $$\frac{9!}{2! \cdot 2! \cdot 2! \cdot 1! \cdot 1! \cdot 1!} = \frac{9!}{2! \cdot 2! \cdot 2!} = \frac{362880}{2 \times 2 \times 2} = \frac{362880}{8} = 45360$$
Farklı kelime yazılabilir.

## Kombinasyon (Seçme)

Kombinasyon, belirli bir kümenin elemanlarından **sıralama gözetmeksizin** yapılan seçimlerin sayısını ifade eder. Seçim sırasının önemli olmadığı durumlarda kombinasyon kullanılır.

$$n$$ elemanlı bir kümenin $$r$$ elemanlı kombinasyonlarının sayısı $$C(n, r)$$ veya $$\binom{n}{r}$$ ile gösterilir ve şu formülle hesaplanır:

$$C(n, r) = \binom{n}{r} = \frac{n!}{r! \cdot (n-r)!}$$

**Önemli Not:** Kombinasyonda $$C(n, r) = C(n, n-r)$$ eşitliği geçerlidir. Ayrıca $$C(n, 0) = 1$$ ve $$C(n, n) = 1$$'dir.

### Örnek Sorular (Kombinasyon)

**Soru 1:** 5 kişilik bir gruptan 3 kişilik bir ekip kaç farklı şekilde seçilebilir?

**Çözüm:**
Burada 5 kişi arasından 3 kişi seçiyoruz ve seçilen kişilerin kendi aralarındaki sıralaması önemli değil ($$n=5, r=3$$).
$$C(5, 3) = \binom{5}{3} = \frac{5!}{3! \cdot (5-3)!} = \frac{5!}{3! \cdot 2!} = \frac{5 \times 4 \times 3!}{3! \times 2 \times 1} = \frac{5 \times 4}{2} = 10$$
Farklı şekilde ekip seçilebilir.

**Soru 2:** Bir kutuda bulunan 4 farklı kırmızı ve 3 farklı mavi bilye arasından, 2 kırmızı ve 1 mavi bilye kaç farklı şekilde seçilebilir?

**Çözüm:**
Bu problemde iki ayrı seçim işlemi vardır: kırmızı bilyelerin seçimi ve mavi bilyelerin seçimi.
- 4 kırmızı bilyeden 2 kırmızı bilye seçimi: $$C(4, 2) = \binom{4}{2} = \frac{4!}{2! \cdot (4-2)!} = \frac{4!}{2! \cdot 2!} = \frac{4 \times 3}{2 \times 1} = 6$$
- 3 mavi bilyeden 1 mavi bilye seçimi: $$C(3, 1) = \binom{3}{1} = \frac{3!}{1! \cdot (3-1)!} = \frac{3!}{1! \cdot 2!} = \frac{3}{1} = 3$$

Bu iki seçim birbirinden bağımsız olduğu için çarpma kuralı uygulanır:
Toplam farklı seçim sayısı = $$C(4, 2) \times C(3, 1) = 6 \times 3 = 18$$
Farklı şekilde bilye seçilebilir.

**Soru 3:** 10 soruluk bir sınavda bir öğrencinin ilk 4 sorudan en az 3 tanesini cevaplaması koşuluyla toplam 7 soru seçmesi gerekmektedir. Bu öğrenci kaç farklı şekilde soru seçimi yapabilir?

**Çözüm:**
Öğrenci toplam 7 soru seçecektir. İlk 4 sorudan en az 3'ünü cevaplama koşulu iki durumu içerir:

* **Durum 1:** İlk 4 sorudan 3 tanesini seçer ve kalan 6 sorudan (10 - 4 = 6) 4 tanesini seçer (toplam 3 + 4 = 7 soru).
    * İlk 4 sorudan 3 soru seçimi: $$C(4, 3) = \binom{4}{3} = 4$$
    * Kalan 6 sorudan 4 soru seçimi: $$C(6, 4) = \binom{6}{4} = \frac{6!}{4! \cdot 2!} = \frac{6 \times 5}{2 \times 1} = 15$$
    * Bu durum için seçim sayısı: $$4 \times 15 = 60$$

* **Durum 2:** İlk 4 sorudan 4 tanesini seçer ve kalan 6 sorudan 3 tanesini seçer (toplam 4 + 3 = 7 soru).
    * İlk 4 sorudan 4 soru seçimi: $$C(4, 4) = \binom{4}{4} = 1$$
    * Kalan 6 sorudan 3 soru seçimi: $$C(6, 3) = \binom{6}{3} = \frac{6!}{3! \cdot 3!} = \frac{6 \times 5 \times 4}{3 \times 2 \times 1} = 20$$
    * Bu durum için seçim sayısı: $$1 \times 20 = 20$$

Bu iki durum birbirinden ayrı olduğu için toplama kuralı uygulanır:
Toplam farklı seçim sayısı = $$60 + 20 = 80$$
Öğrenci 80 farklı şekilde soru seçimi yapabilir.

## Permütasyon ve Kombinasyon Arasındaki Fark

Temel fark, **sıralamanın önemli olup olmamasıdır**:

* **Permütasyon:** Elemanların **sıralanışı** önemlidir. "ABC" ile "CBA" farklı permütasyonlardır.
* **Kombinasyon:** Elemanların **seçim sırası** önemli değildir. {A, B, C} kümesinden yapılan seçimde {A, B} ile {B, A} aynı kombinasyondur (aynı elemanlar seçilmiştir).

Genellikle, bir problemde "kaç farklı şekilde sıralanabilir?", "kaç farklı düzenleme yapılabilir?" gibi ifadeler permütasyonu işaret ederken; "kaç farklı şekilde seçilebilir?", "kaç farklı grup oluşturulabilir?" gibi ifadeler kombinasyonu işaret eder.

## Sonlu Matematik - Bölüm 1, Kısım 2: Permütasyon ve Kombinasyon Örnek Çözümleri

Bu belge, "Sonlu Matematik - Olimpiyat Soruları ve Çözümleri" kaynağının 1. Bölümü'nde yer alan "Permütasyon ve Kombinasyon" konularına ilişkin seçilmiş bazı örnek problemlerin ve kaynağın 3. Bölümündeki ayrıntılı çözümlerinin sunulmasını amaçlamaktadır. Kaynakta bahsedilen temel sayma prensipleri (toplama ve çarpma ilkeleri) ile permütasyon ve kombinasyon kavramları bu problemler üzerinden pekiştirilmektedir [1].

Permütasyon, nesnelerin sıralanmasıyla ilgilenirken (sıralama önemlidir), kombinasyon nesnelerin seçilmesiyle ilgilenir (sıralama önemli değildir) [2, 3].

## Örnek Problemler ve Çözümleri

### Problem 1: Dairesel Permütasyon Kısıtlaması

**Problem:** 5 erkek, 3 kız yuvarlak bir masa etrafına c) kızlar yan yana oturmayacak şekilde kaç farklı şekilde oturtulabilir? [4]

**Çözüm:**
Kızların yan yana oturmaması koşulunu sağlamak için, önce erkekleri yuvarlak masa etrafına oturturuz.
5 erkek yuvarlak masa etrafına **(5-1)!** farklı şekilde oturtulabilir [4].
$$ (5-1)! = 4! = 4 \times 3 \times 2 \times 1 = 24 $$
Erkekler oturduktan sonra aralarında 5 boşluk oluşur (iki kız yan yana gelmeyecek şekilde bu boşluklar kullanılmalıdır) [5].
E _ E _ E _ E _ E _
Bu 5 boş yere 3 kızın oturması gerekmektedir. Bu, 5 yerden 3'ünü seçip kızları bu yerlere sıralamak anlamına gelir. Bu işlemin sayısı **P(5, 3)** veya **5 · 4 · 3** ile bulunur [5].
$$ P(5, 3) = \frac{5!}{(5-3)!} = \frac{120}{2} = 60 $$
Veya çarpma ilkesine göre: ilk kız için 5 yer, ikinci kız için kalan 4 yer, üçüncü kız için kalan 3 yer vardır: $5 \times 4 \times 3 = 60$ [5].
Son olarak, çarpma ilkesine göre erkeklerin oturma düzeni ile kızların oturma düzeninin çarpımı toplam farklı oturma sayısını verir [5].
$$ \text{Toplam farklı sıralama sayısı} = (\text{Erkeklerin dairesel sıralaması}) \times (\text{Kızların boşluklara sıralaması}) $$
$$ \text{Toplam} = 4! \times (5 \times 4 \times 3) = 24 \times 60 = 1440 $$
Sonuç olarak kızlar yan yana gelmeyecek şekilde 1440 farklı şekilde yuvarlak masaya oturtulabilir [5].

### Problem 2: Koşullu Komisyon Seçimi

**Problem (Çözüm Açıklamasına Göre Yeniden İfade Edilmiştir):** 4 erkek ve 6 bayandan oluşan bir gruptan 6 kişilik bir komisyon oluşturulacaktır. Komisyonda erkek sayısı 2 veya 3 olabilir. Bu komisyon kaç farklı şekilde oluşturulabilir? [6]

**Çözüm:**
Komisyondaki erkek sayısına göre durumları ayıralım:
1.  **Komisyonda tam 2 erkek varsa:**
    4 erkek arasından 2 erkek seçilir: $\binom{4}{2}$ farklı yolla.
    6 kişilik komisyonda 2 erkek olduğuna göre, geriye kalan $6 - 2 = 4$ kişi bayan olmalıdır. 6 bayan arasından 4 bayan seçilir: $\binom{6}{4}$ farklı yolla [6].
    Bu durumda komisyon $\binom{4}{2} \times \binom{6}{4}$ farklı yolla oluşturulur.
    $$ \binom{4}{2} = \frac{4!}{2!2!} = \frac{24}{4} = 6 $$
    $$ \binom{6}{4} = \binom{6}{2} = \frac{6!}{4!2!} = \frac{720}{24 \times 2} = 15 $$
    Seçim sayısı: $6 \times 15 = 90$. Ancak kaynak çözümde bu durumu daha alt başlıklara ayırmış gibi görünmektedir: "erkeklerin sayısı ya 2 ya da 3 olabilir. 2 ise, bayanların sayısı 4, 5 veya 6 olabilir." [6]. Bu ifade, komisyon büyüklüğünün *sabit* 6 kişi olduğunu varsayarsak çelişkilidir. Eğer problem "erkek sayısı en az 2 ve en fazla 3 olabilir VE bayan sayısı en az 4 olabilir VE toplam üye sayısı 6 olabilir" şeklinde yorumlanırsa, tek geçerli durum erkek=2, bayan=4 olur. Kaynağın çözümü "2 ise, bayanların sayısı 4, 5 veya 6 olabilir" ifadesiyle başlamakta ve $\binom{4}{2} [ \binom{6}{4} + \binom{6}{5} + \binom{6}{6} ]$ terimini içermektedir [6]. Bu, komisyonun toplam 6 kişiden oluştuğu ancak erkek sayısı 2 iken bayan sayısının 4, 5 veya 6 olabileceği *farklı* problemlerin toplamını hesaplıyormuş gibi durmaktadır.
    Kaynak çözümünün ifadesine göre gidelim:
    *   Erkek sayısı 2 ise: Bayan sayısı 4, 5 veya 6 olabilir [6].
        - 2 erkek (4'ten) ve 4 bayan (6'dan): $\binom{4}{2} \binom{6}{4}$
        - 2 erkek (4'ten) ve 5 bayan (6'dan): $\binom{4}{2} \binom{6}{5}$
        - 2 erkek (4'ten) ve 6 bayan (6'dan): $\binom{4}{2} \binom{6}{6}$
        Bu durumların toplamı: $\binom{4}{2} (\binom{6}{4} + \binom{6}{5} + \binom{6}{6})$ [6].
        Hesaplama: $6 \times (15 + 6 + 1) = 6 \times 22 = 132$.

2.  **Komisyonda tam 3 erkek varsa:**
    4 erkek arasından 3 erkek seçilir: $\binom{4}{3}$ farklı yolla [6].
    6 kişilik komisyonda 3 erkek olduğuna göre, geriye kalan $6 - 3 = 3$ kişi bayan olmalıdır. Ancak kaynak çözüm "3 ise bayanların 6 ’sını da komisyona almak zorundayız" ifadesini kullanmaktadır [6]. Bu da ya problem metninin eksik aktarıldığını ya da 6 kişilik komisyon kısıtının sadece ilk durum için geçerli olduğunu düşündürmektedir. Kaynağın formülüne sadık kalalım:
    *   Erkek sayısı 3 ise: Bayanların 6'sını da komisyona almak zorundayız [6].
        - 3 erkek (4'ten) ve 6 bayan (6'dan): $\binom{4}{3} \binom{6}{6}$
        Hesaplama: $\binom{4}{3} = \binom{4}{1} = 4$ [Dış kaynak]. $\binom{6}{6} = 1$.
        Seçim sayısı: $4 \times 1 = 4$.

Toplam farklı yollar, bu durumların birleşimi olduğu için toplama ilkesi kullanılır [6]:
$$ \text{Toplam Seçim Sayısı} = \binom{4}{2} (\binom{6}{4} + \binom{6}{5} + \binom{6}{6}) + \binom{4}{3} \cdot \binom{6}{6} $$
$$ \text{Toplam} = 132 + 4 = 136 $$
Kaynak çözüm de bu toplamı 136 olarak vermektedir [6]. Problem ifadesindeki muğlaklığa rağmen, çözüm adımları ve sonucu kaynakla uyumludur.

### Problem 3: İki Adımda Yer Değiştirme Dizilişleri

**Problem:** Her adımda tam olarak iki sayının yerleri değiştirilmek üzere, {1, 2, 3, 4, 5, 6, 7} dizilişinden iki adımda elde edilebilecek farklı dizilişlerin sayısı nedir? (UMO-2001) [7]
Seçenekler: a) 88 b) 100 c) 120 d) 176 e) 441 [7]

**Çözüm:**
Kaynak çözüm 3 durum olabileceğini belirtir [8]. Her adım bir transpozisyondur (iki elemanın yer değiştirmesi). İki adımda $\tau_1$ ve $\tau_2$ gibi iki transpozisyon uygulanır. Elde edilen son diziliş $\tau_2 \tau_1$ permütasyonuna karşılık gelir. İki transpozisyonun çarpımı şu permütasyon tiplerinden birini verir:
1.  **Birim Permütasyon (Identity):** Eğer $\tau_1 = \tau_2$ ise (aynı iki eleman iki kere yer değiştirirse). Örn: (1 2)(1 2).
2.  **Bir 3-döngü (3-cycle):** Eğer $\tau_1$ ve $\tau_2$ tam olarak bir elemanı ortak kullanıyorsa. Örn: (1 2)(2 3) = (1 2 3).
3.  **İki Ayrı Transpozisyonun Çarpımı (Double Transposition):** Eğer $\tau_1$ ve $\tau_2$ hiç ortak eleman kullanmıyorsa. Örn: (1 2)(3 4). Bu, 4 elemanın yer değiştirdiği bir permütasyondur.

Kaynak çözüm bu durumları sayarak toplam farklı diziliş sayısını bulur. Kaynak çözümdeki terimlerin karşılığı şu şekildedir:
1.  **4 sayının yeri değiştiği durum (İki ayrı transpozisyonun çarpımı):** Bu, 7 elemandan 4'ünü seçip, bu 4'ünü iki ayrı çift halinde yer değiştirmekle elde edilir. 7 elemandan 4'ünü $\binom{7}{4}$ yolla seçeriz. Seçilen 4 elemanı ikişerli iki gruba ayırmanın $\frac{\binom{4}{2}}{2} = 3$ yolu vardır (örn: {a,b,c,d} -> (a,b),(c,d); (a,c),(b,d); (a,d),(b,c)). Bu çiftlerin transpozisyonu (ab)(cd) veya (cd)(ab) permütasyonunu verir. Ancak kaynak çözümün formülü $\frac{\binom{7}{2} \binom{5}{2}}{2}$ şeklindedir [8]. Bu ifade, 7 elemandan ilk yer değiştirecek çifti $\binom{7}{2}$ yolla, kalan 5 elemandan ikinci yer değiştirecek çifti $\binom{5}{2}$ yolla seçmek ve yer değiştiren çiftlerin sırası önemli olmadığı için 2'ye bölmek anlamına gelir. Bu da aynı sonucu verir: $\frac{21 \times 10}{2} = 105$ farklı permütasyon [8].
2.  **3 sayının yeri değiştiği durum (3-döngü):** Bu, 7 elemandan 3'ünü seçip bu 3 elemanı bir 3-döngü şeklinde sıralamakla elde edilir. 7 elemandan 3'ünü $\binom{7}{3}$ yolla seçeriz ($ \binom{7}{3} = \frac{7 \times 6 \times 5}{3 \times 2 \times 1} = 35 $). Seçilen 3 elemanla 2 farklı 3-döngü oluşturulabilir ((abc) ve (acb)). Bu 3-döngüler, iki transpozisyonun çarpımı olarak elde edilebilir (örn: (abc) = (ac)(ab)). Kaynak çözümdeki terim $\binom{7}{3} \cdot 2$ şeklindedir [8]. Bu, 3 eleman seçim sayısı çarpı bu elemanlarla oluşturulabilecek 3-döngü sayısıdır. $35 \times 2 = 70$ farklı permütasyon.
3.  **2 sayının yeri değiştiği durum (Transpozisyon):** Kaynak çözümün son terimi $\binom{7}{2}$ şeklindedir [8]. $\binom{7}{2} = 21$. Bu, 7 elemandan 2'sini seçerek oluşturulabilecek transpozisyon sayısıdır. Bir transpozisyon, bir adımda elde edilir. İki adımda nasıl bir transpozisyon elde edildiği çözümde açıkça belirtilmemiştir. Ya bu terim, ikinci adımın ilk adımın tersi olmadığı, ancak net sonucun bir transpozisyon olduğu durumları saymaktadır (ki bu yalnızca 3-döngü veya birim permütasyon yoluyla olabilir), ya da Problem 1'deki çözümde olduğu gibi, farklı "durumları" sayarken permütasyon türlerini değil, olasılıkları veya işlem sıralarını hesaba katmaktadır. Ancak problem "farklı dizilişlerin sayısını" sormaktadır, bu da permütasyon sayısını ima eder. Eğer bu terim, birinci adımda $a \leftrightarrow b$ yer değiştirmesi yapılıp, ikinci adımda da $a \leftrightarrow b$ yer değiştirmesi dışında *başka* bir yer değiştirme yapıldığında net sonucun bir transpozisyon olma durumlarını sayıyorsa, bu transpozisyonlar zaten 3-döngü veya 4-elemanlı permütasyonlar içine dahil olur.

Kaynak çözümünün formülü şöyledir:
$$ \text{Toplam Farklı Diziliş} = \frac{\binom{7}{2} \binom{5}{2}}{2} + \binom{7}{3} \cdot 2 + \binom{7}{2} $$
$$ \text{Toplam} = 105 + 70 + 21 = 196 $$
Kaynak çözüm bu üç terimin toplamını 196 olarak vermiştir [8]. Ancak, problemde verilen seçenekler arasında 196 bulunmamaktadır [7]. Mantıksal olarak, iki transpozisyonun çarpımı ya birim permütasyondur (1 farklı diziliş), ya bir 3-döngüdür (70 farklı diziliş), ya da iki ayrı transpozisyonun çarpımıdır (105 farklı diziliş). Bu durumda toplam farklı diziliş sayısı $1 + 70 + 105 = 176$ olmalıdır, ki bu da seçenekler arasında d) şıkkına karşılık gelir [7]. Kaynak çözümündeki son $+21$ teriminin kaynağı ve anlamı, sağlanan metin parçalarına göre net değildir ve nihai sonuç seçeneklerden biriyle uyuşmamaktadır. Yine de, kaynağın sunduğu çözümü buraya aktardım.