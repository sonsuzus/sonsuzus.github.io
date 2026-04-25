---
layout: post
title: Rekabetçi Programcı Oyun Teorisi
math: true
excerpt_separator: "``"
categories:
  - Program
tags:
  - oyun-teorisi
  - game-theory
  - nim
  - sprague-grundy
  - grundy-sayısı
  - misère
  - kazanan-durum
  - kaybeden-durum
  - xor
  - mex
  - c
  - programlama
  - algoritma
  - olimpiyat
  - yarışma
  - kodlama
  - matematik
  - kitap
---

**Oyun teorisi**, rastgele eleman içermeyen iki kişilik oyunları analiz eder. Amaç; rakip ne yaparsa yapsın, eğer varsa oyunu kesinlikle kazandıracak bir strateji bulmaktır. Bu oyunlar **nim teorisi** ile analiz edilir.
``

## 25.1 Oyun Durumları

Örnek oyun: $n$ çubukluk bir öbek var; $A$ ve $B$ oyuncuları sırayla oynar, $A$ başlar. Her hamlede oyuncu 1, 2 veya 3 çubuk çıkarır; **son çubuğu çıkaran kazanır.**

$n = 10$ için örnek oynanış:

- A, 2 çıkarır → 8 kaldı
- B, 3 çıkarır → 5 kaldı
- A, 1 çıkarır → 4 kaldı
- B, 2 çıkarır → 2 kaldı
- A, 2 çıkarır → **A kazanır**

### Kazanan ve Kaybeden Durumlar

- **Kazanan durum (W):** Mevcut oyuncu optimal oynarsa kazanır.
- **Kaybeden durum (L):** Rakip optimal oynarsa mevcut oyuncu kaybeder.

**Temel kural:**
- Şu anki durumdan bir **kaybeden** duruma geçiş yapılabiliyorsa → **kazanan durum**
- Şu anki durumdan yalnızca **kazanan** durumlara geçilebiliyorsa → **kaybeden durum**

Başka hamle olmayan son durum her zaman **kaybedendir** (0 çubuk: hamle yok).

1–2–3 çubuk çıkarma oyununda 0–15 durumlarının sınıflandırması:

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
|---|---|---|---|---|---|---|---|---|---|----|----|----|----|----|----|
| L | W | W | W | L | W | W | W | L | W | W  | W  | L  | W  | W  | W  |

**Kalıp:** $k$ durumu, $4 \mid k$ ise kaybeden; aksi hâlde kazanandır. Optimal strateji her hamlede kalan çubuk sayısını 4'ün katı tutmaktır.

### Durum Çizgesi

Daha karmaşık oyunlarda (örneğin $k$. durumda $k$'yi bölen kadar çubuk alınabilir) durum çizgesi kurulur: düğümler durumları, kenarlar geçişleri gösterir. 1–9 durumları için:

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|
| L | W | L | W | L | W | L | W | L |

Bu oyunda tüm tek sayılı durumlar kaybedendir.

## 25.2 Nim Oyunu

**Nim**, oyun teorisinin temel taşıdır; çünkü çoğu oyun aynı stratejiyle analiz edilebilir.

**Kurallar:**
- $n$ öbek vardır, $k$. öbekte $x_k$ çubuk bulunur.
- Sıradaki oyuncu bir öbek seçer ve istediği kadar çubuk çıkarır.
- Son çubuğu çıkaran kazanır.
- Durum $[0, 0, \ldots, 0]$ kaybedendir.

### Analiz: Nim Toplamı

Herhangi bir nim durumu **nim toplamı** ile sınıflandırılır:

$$s = x_1 \oplus x_2 \oplus \cdots \oplus x_n$$

$\oplus$ XOR operatörüdür. **Nim toplamı 0 olan durum kaybedendir; diğerleri kazanandır.**

Örnek: $[10, 12, 5]$ durumunda $s = 10 \oplus 12 \oplus 5 = 3 \neq 0$ → kazanan durum.

**Neden işe yarar?**

- **Kaybeden durumlar:** $[0,0,\ldots,0]$'ın nim toplamı 0'dır. Herhangi bir $x_k$'yı değiştirmek nim toplamını 0'dan farklı yapar → kazanan duruma geçilir.
- **Kazanan durumlar:** $x_k \oplus s < x_k$ olan bir $k$ her zaman mevcuttur (nim toplamının en soldaki bitine karşılık gelen öbek). Bu öbeği $x_k \oplus s$ büyüklüğüne düşürmek nim toplamını 0 yapar → kaybeden duruma geçilir.

**Örnek hamle:** $[10, 12, 5]$, nim toplamı $s = 3$:

$$10 = 1010_2, \quad 12 = 1100_2, \quad 5 = 0101_2, \quad s = 0011_2$$

$s$'nin en soldaki biti 10'un 2. bitine denk gelir. Yeni öbek boyutu: $10 \oplus 3 = 9$.
Hamle: 10'lu öbekten 1 çubuk çıkar → $[9, 12, 5]$, nim toplamı $9 \oplus 12 \oplus 5 = 0$ → **kaybeden durum**.

### Misère Nim

**Misère** versiyonunda son çubuğu alan **kaybeder**. Strateji:

- Tüm öbeklerde en fazla 1 çubuk kalana dek **standart nim** gibi oyna.
- Bu eşiğe gelindiğinde taktiği değiştir:
  - **Standart nim'de** tek çubuklu öbek sayısını **çift** tut.
  - **Misère'de** tek çubuklu öbek sayısını **tek** tut.

Bu eşik durumu her zaman **kazanan** bir durumdur (birden fazla çubuklu tek öbek mevcuttur, nim toplamı 0 değildir).

## 25.3 Sprague–Grundy Teoremi

**Sprague–Grundy Teoremi**, nim stratejisini aşağıdaki şartları sağlayan tüm oyunlara genelleştirir (Sprague 1935, Grundy 1939 — bağımsız olarak):

- İki oyuncu sırayla hamle yapar.
- Olası hamleler kimin sırasında olduğuna bağlı değildir.
- Hamle yapamayan oyuncu kaybeder.
- Oyun sonlu durumda biter.
- Oyuncuların tam bilgisi vardır; rastgelelik yoktur.

**Temel fikir:** Her oyun durumuna bir **Grundy sayısı** atanır. Bu sayı bir nim öbeğindeki çubuk sayısına karşılık gelir; böylece oyun standart nim gibi oynanabilir.

### Grundy Sayısı (mex)

Bir durumun Grundy sayısı:

$$G = \text{mex}(\{g_1, g_2, \ldots, g_n\})$$

$g_1, g_2, \ldots, g_n$ gidilebilecek durumların Grundy sayıları; **mex** ise kümede bulunmayan en küçük negatif olmayan tam sayıdır.

Örnek: $\text{mex}(\{0, 1, 3\}) = 2$. Hamle olmayan durumda $\text{mex}(\emptyset) = 0$.

**Özellikler:**
- Grundy sayısı **0** → kaybeden durum
- Grundy sayısı **pozitif** → kazanan durum
- Grundy sayısı $x > 0$ olan durumdan $0, 1, \ldots, x-1$ Grundy sayılı tüm durumlara gidilebilir

**Labirent oyunu örneği:** Oyuncular figürü sol veya yukarı hareket ettiriyor; son hamleyi yapan kazanıyor. Sol alt köşenin Grundy sayısı 2 → kazanan durum. Kaybeden duruma ya iki adım yukarı ya dört adım sola gidilerek varılır.

> Standart nim'den farklı olarak Grundy sayısı daha büyük bir duruma geçmek mümkündür; fakat rakip her zaman bu hamleyi nötrleyebilir.

### Alt Oyunlar

Oyun birden fazla bağımsız alt oyundan oluşuyorsa ve her hamlede yalnızca bir alt oyunda hareket ediliyorsa, **tüm oyunun Grundy sayısı alt oyunların Grundy sayılarının nim toplamıdır:**

$$G = G_1 \oplus G_2 \oplus \cdots \oplus G_k$$

**Örnek:** 3 labirentten oluşan oyun; başlangıç Grundy sayıları 2, 3, 3 ise:

$$G = 2 \oplus 3 \oplus 3 = 2 \neq 0 \implies \text{kazanan durum}$$

Optimal hamle: ilk labirentte iki adım yukarı git → $0 \oplus 3 \oplus 3 = 0$ (kaybeden durum).

### Grundy'nin Oyunu

Bazen bir hamle oyunu bağımsız **alt oyunlara böler**. Bu durumda:

$$G = \text{mex}(\{g_1, g_2, \ldots, g_n\}), \quad g_k = a_{k,1} \oplus a_{k,2} \oplus \cdots \oplus a_{k,m}$$

**Grundy'nin Oyunu:** Tek bir öbek var; her hamlede oyuncu seçtiği öbeği **farklı büyüklükte** iki boş olmayan öbeğe böler. Son hamleyi yapan kazanır.

$f(n)$, $n$ çubuklu öbeğin Grundy sayısı olsun. Örneğin $n = 8$:

$$f(8) = \text{mex}(\{f(1) \oplus f(7),\ f(2) \oplus f(6),\ f(3) \oplus f(5)\})$$

1 ve 2 çubuklu öbekler bölünemez; dolayısıyla $f(1) = f(2) = 0$. İlk Grundy sayıları:

| $n$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|-----|---|---|---|---|---|---|---|---|
| $f(n)$ | 0 | 0 | 1 | 0 | 2 | 1 | 0 | 2 |

$f(8) = 2 \neq 0$ → kazanan durum. Kazanan hamle: $1 + 7$ olarak böl, çünkü $f(1) \oplus f(7) = 0 \oplus 0 = 0$.

---

> **Kaynak:** *Rekabetçi Programcı* (Competitive Programmer's Handbook — Antti Laaksonen), Bölüm 25.
