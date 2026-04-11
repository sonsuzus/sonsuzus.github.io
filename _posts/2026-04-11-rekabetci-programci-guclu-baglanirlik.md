---
layout: post
title: Rekabetçi Programcı Güçlü Bağlanırlık
math: true
excerpt_separator: "``"
categories:
  - Program
tags:
  - çizge
  - graph
  - yönlü-çizge
  - directed-graph
  - güçlü-bağlanırlık
  - strongly-connected
  - scc
  - kosaraju
  - 2sat
  - mantık
  - dfs
  - topolojik-sıralama
  - c
  - programlama
  - algoritma
  - olimpiyat
  - yarışma
  - kodlama
  - matematik
  - kitap
---

Yönlü bir çizgede kenarlar yalnızca tek yönlü geçilir. Bu nedenle çizge bağlı olsa bile her düğümden diğerine gidileceği garanti edilemez. Daha güçlü bir bağlanırlık kavramına ihtiyaç vardır.

Bir çizge, her düğümden diğer tüm düğümlere gidilebiliyorsa **güçlü bağlanılmış** (strongly connected) olarak adlandırılır. Güçlü bağlanılmamış bir çizgede ise bazı düğüm çiftleri arasında tek yönlü bir ulaşım bile mümkün olmayabilir.

**Güçlü bağlanılmış parçalar** (strongly connected components, SCC), çizgeyi olabildiğince büyük güçlü bağlanılmış bölümlere ayırır. Bu parçalar, orijinal çizgenin derin yapısını ortaya koyan asiklik bir **bileşen çizgesi** (component graph) oluşturur.
``
Örneğin bir çizgenin $A = \{1, 2\}$, $B = \{3, 6, 7\}$, $C = \{4\}$ ve $D = \{5\}$ şeklinde dört güçlü bağlanılmış parçası varsa, bileşen çizgesi bu dört düğüm üzerinde döngüsüz bir yönlü çizge oluşturur. Bu yapı döngü içermediği için 16. Bölümdeki topolojik sıralama ve dinamik programlama teknikleri doğrudan uygulanabilir.

## 17.1 Kosaraju'nun Algoritması

Kosaraju'nun Algoritması, yönlü bir çizgedeki tüm güçlü bağlanılmış parçaları $O(n + m)$ zamanda bulan verimli bir algoritmadır. İki ayrı DFS (derinlik öncelikli arama) kullanır.

### 1. Arama

İlk DFS, tüm düğümlerden geçerek her işlenmemiş düğümden bir arama başlatır. Her düğüm tamamen işlendiğinde bir listeye eklenir. Bu listedeki sıra, düğümlerin **bitiş zamanlarına** göre belirlenir.

Örneğin şu çizgede düğümler şu sırayla işlenip listeye eklenir:

| Düğüm | Bitiş Zamanı |
|:-----:|:------------:|
| 4     | 5            |
| 5     | 6            |
| 2     | 7            |
| 1     | 8            |
| 6     | 12           |
| 7     | 13           |
| 3     | 14           |

### 2. Arama

İkinci aşamada çizgedeki **tüm kenarlar ters çevrilir**. Bu, ikinci aramanın güçlü bağlanılmış parçaların dışına "sızmamasını" garanti eder.

Ardından birinci aramada oluşturulan listedeki düğümler **ters sırada** ziyaret edilir. İşlenmemiş her düğümden yeni bir parça oluşturulup DFS başlatılır; bu aramada bulunan tüm düğümler söz konusu parçaya eklenir.

Örnek çizgede önce 3. düğümden bir parça oluşturulur. Sonraki düğümler olan 7 ve 6 zaten bu parçaya ait olduğundan atlanır; yeni parça 1. düğümde başlar. En sonda 5 ve 4. düğümler işlenerek kalan parçalar tamamlanır.

Algoritmanın zaman karmaşıklığı $O(n + m)$'dir; iki DFS kullanılmasına karşın her biri lineer zamanda çalışır.

## 17.2 2SAT Problemi

Güçlü bağlanırlık, **2SAT** adı verilen önemli bir mantıksal tatmin problemiyle de doğrudan ilişkilidir. Problemde şu biçimde bir formül verilir:

$$(a_1 \lor b_1) \land (a_2 \lor b_2) \land \cdots \land (a_m \lor b_m)$$

Burada her $a_i$ ve $b_i$ ya bir mantıksal değişken ($x_1, x_2, \ldots, x_n$) ya da onun karşıtıdır ($\lnot x_1, \lnot x_2, \ldots, \lnot x_n$). Görev, formülü doğru yapacak bir değer ataması bulmak ya da böyle bir atamanın mümkün olmadığını göstermektir.

### Örnek 1 (Çözülebilir)

$$L_1 = (x_2 \lor \lnot x_1) \land (\lnot x_1 \lor \lnot x_2) \land (x_1 \lor x_3) \land (\lnot x_2 \lor \lnot x_3) \land (x_1 \lor x_4)$$

Bu formül aşağıdaki atama ile sağlanır:

$$x_1 = \text{false},\quad x_2 = \text{false},\quad x_3 = \text{true},\quad x_4 = \text{true}$$

### Örnek 2 (Çözülemez)

$$L_2 = (x_1 \lor x_2) \land (x_1 \lor \lnot x_2) \land (\lnot x_1 \lor x_3) \land (\lnot x_1 \lor \lnot x_3)$$

$x_1$ için ne değer verilirse verilsin bir çelişki ortaya çıkar: $x_1 = \text{false}$ ise hem $x_2$ hem $\lnot x_2$ doğru olmalıdır (imkânsız); $x_1 = \text{true}$ ise hem $x_3$ hem $\lnot x_3$ doğru olmalıdır (imkânsız).

### Çizge Modeli

2SAT problemi bir çizgeye dönüştürülür. Düğümler $x_i$ ve $\lnot x_i$ değişkenlerini, kenarlar ise değişkenler arası çıkarımları temsil eder. Her $(a_i \lor b_i)$ çifti iki kenar üretir:

$$\lnot a_i \to b_i \qquad \text{ve} \qquad \lnot b_i \to a_i$$

Bu, "$a_i$ yanlışsa $b_i$ doğru olmalı, ya da tam tersi" mantığını ifade eder.

$L_1$ için oluşan çizgede $x_i$ ve $\lnot x_i$ hiçbir zaman aynı güçlü bağlanılmış parçada bulunmaz; dolayısıyla bir çözüm mevcuttur. $L_2$ için ise tüm düğümler aynı güçlü bağlanılmış parçaya aittir; dolayısıyla çözüm **yoktur**.

**Genel kural:** Formülün bir çözümü vardır ancak ve ancak hiçbir $x_i$ ile $\lnot x_i$ aynı güçlü bağlanılmış parçada bulunmuyorsa.

### Çözümü Bulmak

Çözüm mevcutsa değişken değerleri **ters topolojik sıraya** göre belirlenir. Her adımda, başka işlenmemiş parçalara kenarı olmayan bir parça seçilir:

- Parçadaki değişkenlere henüz değer verilmemişse parçanın konumuna göre değer atanır.
- Değer zaten atanmışsa değiştirilmez.

Bu işlem tüm değişkenlere birer değer verilinceye kadar sürer.

Örneğin $L_1$ için bileşenler $A = \{\lnot x_4\}$, $B = \{x_1, x_2, \lnot x_3\}$, $C = \{\lnot x_1, \lnot x_2, x_3\}$ ve $D = \{x_4\}$ olarak bulunur. Ters topolojik sırayla önce $D$ işlenir ve $x_4 = \text{true}$ olur. Ardından $C$ işlenir ve $x_1 = \text{false}$, $x_2 = \text{false}$, $x_3 = \text{true}$ atanır. Tüm değişkenler atandığından $A$ ve $B$ parçaları değişkenleri değiştirmez.

Bu yöntemin doğruluğunu şöyle anlayabiliriz: eğer $x_i$ düğümünden $x_j$ düğümüne, oradan da $\lnot x_j$ düğümüne bir yol varsa $x_i$ asla doğru olamaz; çünkü bu durumda $\lnot x_j$ düğümünden $\lnot x_i$ düğümüne de bir yol bulunur ve bu zincirleme çelişki $x_i$'yi zorla yanlış yapar.

> **Not:** 3SAT probleminde her parça $(a_i \lor b_i \lor c_i)$ biçimindedir. Bu problem NP-Hard'dır; yani verimli bilinen bir çözüm algoritması yoktur.
