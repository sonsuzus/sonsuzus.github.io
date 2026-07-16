---
layout: post
title: "C++ ile Genetik Algoritmalar: Evrimi Kodla, Çözümü Seç"
math: true
categories: 
  - Program
tags: 
  - C++
  - Genetik Algoritma
  - Optimizasyon
---

Bir problemi çözmeye çalışırken bazen “en iyi” cevabı doğrudan hesaplamak zordur; özellikle seçenek sayısı devasa ise klasik yöntemler yorulabilir. İşte genetik algoritmalar burada sahneye çıkar: Doğadaki seçilim, çaprazlama ve mutasyon fikrini taklit ederek veri havuzundaki aday çözümleri nesilden nesle iyileştirir. C++ ise performansı ve bellek kontrolü sayesinde bu evrimsel deneyi hızlıca çalıştırmak için harika bir araçtır.

``

Genetik algoritmanın temel fikri şudur: Elimizde bir **popülasyon** vardır. Popülasyondaki her birey, olası bir çözümü temsil eder. Bu bireylere çoğu zaman **kromozom** denir. Kromozom; bit dizisi, sayı vektörü, rota listesi veya başka bir veri yapısı olabilir. Her kromozomun başarısı bir **uygunluk fonksiyonu** ile ölçülür. Amaç, uygunluğu yüksek bireyleri seçip melezlemek ve zamanla daha iyi çözümler üretmektir.

Matematiksel olarak bir optimizasyon probleminde amaç genellikle şu biçimdedir:

$$\max_{x \in S} f(x)$$

Burada $S$ çözüm uzayı, $x$ aday çözüm, $f(x)$ ise uygunluk değeridir. Genetik algoritma, $S$ içinde tek tek tüm noktaları gezmek yerine “umut vadeden bölgeleri” keşfetmeye çalışır. Biraz dedektif, biraz çiftçi, biraz da çılgın bilim insanı gibi davranır.

| Kavram | Doğadaki Karşılığı | Algoritmadaki Anlamı |
|---|---|---|
| Popülasyon | Canlı topluluğu | Aday çözümler kümesi |
| Kromozom | Genetik yapı | Çözüm temsili |
| Uygunluk | Hayatta kalma başarısı | Amaç fonksiyonu skoru |
| Çaprazlama | Üreme | İki çözümden yeni çözüm üretme |
| Mutasyon | Gen değişimi | Rastgele küçük değişiklik |

Basit bir örnek düşünelim: 0 ve 1’lerden oluşan 20 bitlik bir dizide mümkün olduğunca çok 1 elde etmek istiyoruz. Bu, eğitim amaçlı “OneMax” problemidir. Uygunluk fonksiyonu, kromozomdaki 1 sayısıdır. Yani $f(x)=\sum x_i$. Kulağa kolay geliyor ama aynı yapı, daha zor problemlerde rota optimizasyonu, çizelgeleme veya parametre ayarlama için de kullanılabilir.

Aşağıdaki C++ kodu orta düzey bir iskelet sunar. Popülasyon oluşturur, uygunluk hesaplar, turnuva seçimi yapar, çaprazlama ve mutasyon uygular:

```cpp
#include <bits/stdc++.h>
using namespace std;

const int GENE_LENGTH = 20;
const int POP_SIZE = 50;
const int GENERATIONS = 100;
const double MUTATION_RATE = 0.02;

mt19937 rng(random_device{}());

using Chromosome = vector<int>;

int fitness(const Chromosome& c) {
    return accumulate(c.begin(), c.end(), 0);
}

Chromosome randomChromosome() {
    uniform_int_distribution<int> bit(0, 1);
    Chromosome c(GENE_LENGTH);
    for (int& gene : c) gene = bit(rng);
    return c;
}

Chromosome tournamentSelect(const vector<Chromosome>& pop) {
    uniform_int_distribution<int> dist(0, POP_SIZE - 1);
    Chromosome a = pop[dist(rng)];
    Chromosome b = pop[dist(rng)];
    return fitness(a) > fitness(b) ? a : b;
}

Chromosome crossover(const Chromosome& p1, const Chromosome& p2) {
    uniform_int_distribution<int> pointDist(1, GENE_LENGTH - 2);
    int point = pointDist(rng);
    Chromosome child(GENE_LENGTH);
    for (int i = 0; i < GENE_LENGTH; i++)
        child[i] = (i < point) ? p1[i] : p2[i];
    return child;
}

void mutate(Chromosome& c) {
    uniform_real_distribution<double> prob(0.0, 1.0);
    for (int& gene : c)
        if (prob(rng) < MUTATION_RATE) gene = 1 - gene;
}
```

Bu parçalar ana döngüde birleştirilir: Eski popülasyondan ebeveyn seçilir, çocuk üretilir, mutasyon uygulanır ve yeni nesil oluşturulur. Her nesilde en iyi bireyi izlemek, algoritmanın gerçekten evrimleşip evrimleşmediğini görmemizi sağlar.

| Parametre | Düşük Değer Etkisi | Yüksek Değer Etkisi |
|---|---|---|
| Popülasyon boyutu | Hızlı ama dar arama | Yavaş ama çeşitli arama |
| Mutasyon oranı | Yerel takılma riski | Rastgeleliğe fazla kayma |
| Nesil sayısı | Erken durma | Daha iyi yakınsama şansı |
| Çaprazlama oranı | Az kombinasyon | Daha fazla keşif |

Genetik algoritmalarda sihirli tek bir ayar yoktur. Mutasyon oranı çok düşükse popülasyon birbirine benzer hale gelir; çok yüksekse öğrenilmiş iyi özellikler sürekli bozulur. Bu denge, **keşif** ve **sömürü** arasındaki klasik optimizasyon dansıdır. Keşif yeni bölgeleri aramak, sömürü ise bulunan iyi bölgeleri iyileştirmektir.

C++ tarafında dikkat edilmesi gereken önemli noktalardan biri kopyalama maliyetidir. Büyük kromozomlarda `vector` kopyalamak pahalı olabilir; gerekirse referans, taşıma semantiği veya özel veri yapıları kullanılabilir. Ayrıca rastgele sayı üretiminde `rand()` yerine `std::mt19937` tercih etmek daha sağlıklı sonuçlar verir.

Sonuç olarak genetik algoritmalar, kesin cevabı garanti eden sihirli değnekler değildir; ama karmaşık ve geniş arama uzaylarında oldukça pratik sezgisel yöntemlerdir. C++ ile birleştiğinde hızlı deneyler yapabilir, farklı uygunluk fonksiyonları deneyebilir ve algoritmanın küçük dijital canlılar gibi gelişmesini izleyebilirsiniz. Kısacası: Eğer probleminiz “çok fazla seçenek, çok az sabır” diyorsa, evrimi biraz koda dökmenin zamanı gelmiş olabilir.
