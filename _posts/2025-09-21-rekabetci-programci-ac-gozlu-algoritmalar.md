---
layout: post
title: Rekabetçi Programcı Açgözlü Algoritmalar (Greedy Algorithms)
math: true 
categories: 
  - Program
tags: 
  - search
  - arama
  - c
  - programlama
  - algoritma
  - olimpiyat
  - dizi
  - yarışma
  - değişken
  - açgözlü
  - greedy
  - bellek
  - kodlama
  - matematik
  - kitap
---

Açgözlü algoritma, her zaman o anki en iyi gözüken kararı vererek çözüme ulaşan bir yaklaşımdır. Açgözlü bir algoritma asla daha önce verdiği kararları geri almaz ve doğrudan son sonucu oluşturur. Bu yüzden açgözlü algoritmalar genellikle verimlidir. Açgözlü bir algoritma oluşturmanın zorluğu, her zaman en iyi (optimal) cevabı verecek bir açgözlü strateji bulmaktır. Yapılan küçük optimal kararların, genel olarak da optimal olması gerekir. Genellikle bir açgözlü algoritmanın doğru çalıştığını kanıtlamak zordur.

## 6.1 Para Problemi (Coin problem)

Elimizdeki madeni paraları kullanarak `n` miktarında bir para üstü vermemiz isteniyor. Elimizdeki paraların değerleri `coins = {c_1, c_2, ..., c_k}`'dir ve her parayı istediğimiz kadar kullanabiliriz. Amaç, toplam için gereken minimum sayıda madeni para kullanmaktır.

Örneğin, `{1, 2, 5, 10, 20, 50, 100, 200}` paralarıyla `n = 520` oluşturmak için en az 4 para gerekir: `200 + 200 + 100 + 20`.

### Açgözlü Algoritma

Basit bir açgözlü algoritma, gereken miktar toplanana kadar her zaman seçilebilecek en büyük değerli parayı seçmektir. Bu strateji, standart Euro madeni paraları gibi sistemlerde işe yarar.

### Genel Durum

Ancak genel durumda, sahip olduğumuz paralar rastgele değerlerde olabilir ve bu açgözlü algoritma her zaman optimal çözümü vermeyebilir. Örneğin, elimizdeki paralar `{1, 3, 4}` ise ve istenen toplam 6 ise, açgözlü algoritma `4 + 1 + 1` (3 adet para) çözümünü verirken, en iyi çözüm `3 + 3`'tür (2 adet para).

Para problemi için her zaman çalışan genel bir açgözlü algoritma bilinmemektedir[^1].

## 6.2 Zaman Planlaması (Scheduling)

Çoğu zaman planlama sorusu açgözlü algoritmalar ile çözülebilir. Klasik bir problem, başlangıç ve bitiş zamanları bilinen `n` tane etkinlikten, birbiriyle çakışmayacak şekilde en fazla sayıda etkinliği seçmektir.

| Etkinlik | Başlama Zamanı | Bitiş Zamanı |
|----------|----------------|--------------|
| A        | 1              | 3            |
| B        | 2              | 5            |
| C        | 3              | 9            |
| D        | 6              | 8            |

Bu durumda en fazla iki etkinlik seçilebilir, örneğin B ve D.

Farklı açgözlü stratejiler denenebilir:

1.  **En kısa etkinliği seç:** Bu strateji her zaman çalışmaz. Kısa bir etkinlik, daha uzun süren iki etkinliğin seçilmesini engelleyebilir.
2.  **En erken başlayan etkinliği seç:** Bu da her zaman çalışmaz. Erken başlayan uzun bir etkinlik, daha sonraki birçok etkinliği engelleyebilir.
3.  **En erken biten etkinliği seç:** **Bu strateji her zaman doğru çalışır.** Her adımda, mevcut etkinliklerle çakışmayan ve bitiş zamanı en erken olan etkinliği seçmek, kalan zamanı maksimize ettiği için optimal bir çözüm üretir.

## 6.3 Görevler ve Son Teslimler (Tasks and Deadlines)

Süresi ve son teslim tarihi bilinen `n` tane görevimiz olduğunu düşünelim. Amacımız görevleri yapmak için bir sıra oluşturmak. Her görev için $d - x$ puan kazanıyoruz, burada `d` görevin son teslim tarihi ve `x` görevi bitirdiğimiz zamandır. En fazla alabileceğimiz toplam puan kaçtır?

İlginç bir şekilde, bu sorunun optimal çözümü son teslim tarihlerine bağlı değildir. Doğru açgözlü strateji, görevleri **sürelerine göre artan bir şekilde sıralamaktır**. Bunun nedeni, eğer daha uzun süren bir görevi daha kısa süren bir görevden önce yaparsak, bu iki görevin yerini değiştirdiğimizde toplam puanın her zaman artması veya aynı kalmasıdır. Daha kısa görevleri önce bitirmek, sonraki tüm görevlerin bitiş zamanını öne çeker ve toplam puanı iyileştirir.

## 6.4 Toplamları Küçültmek (Minimizing Sums)

Bize `n` tane $a_1, a_2, ..., a_n$ sayısı verildiğinde, $\sum_{i=1}^{n} \lvert a_i - x\rvert ^c$ toplamını en küçük yapacak `x` değerini bulma problemi.

### c = 1 Durumu

$\sum \lvert a_i - x\rvert $ toplamını minimize etmek için en iyi `x` değeri, sayıların **medyanı**dır. Sayılar sıralandıktan sonra ortadaki eleman medyandır.

### c = 2 Durumu

$\sum (a_i - x)^2$ toplamını minimize etmek için en iyi `x` değeri, sayıların **aritmetik ortalaması**dır ($(\sum a_i) / n$).

## 6.5 Veri Sıkıştırma (Data Compression)

Bir metni sıkıştırmak için her karaktere bir bit dizisi (kod) atanabilir. Daha sık geçen karakterlere daha kısa kodlar, daha az geçenlere daha uzun kodlar atayarak metnin toplam uzunluğu azaltılabilir.

### Huffman Kodlaması

Huffman Kodlaması, bir metni sıkıştırmak için en optimal kodu (prefix code) üreten bir açgözlü algoritmadır[^2].

Algoritma, karakterlerin metindeki frekanslarına (geçme sıklıklarına) dayalı bir ikili ağaç (binary tree) oluşturur.

1.  Her karakteri, frekansı kadar ağırlığa sahip bir düğüm olarak başlat.
2.  Her adımda, en düşük ağırlığa sahip iki düğümü seç ve bunları yeni bir ebeveyn düğüm altında birleştir. Yeni düğümün ağırlığı, birleştirilen iki düğümün ağırlıkları toplamıdır.
3.  Tek bir kök düğüm kalana kadar bu işleme devam et.

Oluşturulan ağaçta, kökten bir karakterin yaprağına giden yol o karakterin kodunu verir (sola gitmek '0', sağa gitmek '1').

Bu yöntemle, sık geçen 'A' karakteri gibi karakterler kısa kodlar alırken, az geçen 'B' ve 'D' gibi karakterler daha uzun kodlar alır, bu da optimal sıkıştırmayı sağlar.

[^1]: Bu bölümde yapılan açgözlü algoritmanın elimizdeki paralar için doğru olup olmadığını polinom zamanda (polynomial time) kontrol etmek mümkündür.
[^2]: D. A. Huffman bu metodu üniversite dersinde bir soruyu çözerken bulmuştur ve bu algoritmayı 1952'de yayınlamıştır.