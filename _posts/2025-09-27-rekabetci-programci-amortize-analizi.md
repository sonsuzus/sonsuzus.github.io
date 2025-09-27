---
layout: post
title: Rekabetçi Programcı Amortize Analizi
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
  - analiz
  - bellek
  - kodlama
  - matematik
  - kitap
  - amortize
---



Bir algoritmanın sadece yapısını inceleyerek (örneğin döngü sayılarına bakarak) zaman karmaşıklığını hesaplamak kolaydır. Fakat bazen bu üstünkörü analiz, algoritmanın gerçek verimliliğini doğru yansıtmaz.

**Amortize Analizi**, zaman karmaşıklığı farklı olan operasyonları içeren algoritmaları inceler. Buradaki fikir, tek tek operasyonların en kötü durumuna bakmak yerine, algoritmanın çalışması sürecinde bütün operasyonlar için harcanan toplam zamanı tahmin etmektir. Bazen bazı operasyonlar yavaş olsa da, toplamda bu yavaş operasyonlar sık gerçekleşmediği için ortalama performans verimli olabilir.

## 8.1 İki İşaretçi Methodu (Two Pointers Method)

İki işaretçi methodunda, dizinin elemanları üzerinden geçmek için iki işaretçi (pointer) kullanılır. Bu işaretçiler genellikle tek bir yöne doğru hareket ederler, bu da algoritmanın verimli çalışmasını sağlar.

### Altdizi (Subarray) Toplamı

**Problem:** `n` tane pozitif sayıdan oluşan bir dizide, toplamı `x` olan ardışık bir altdizi bulmak.

**Fikir:** Altdizinin başlangıcını ve sonunu gösteren iki işaretçi (`sol` ve `sağ`) tutulur. `sağ` işaretçi, toplam `x`'i geçmediği sürece ilerletilir. Toplam `x`'i geçerse, `sol` işaretçi ilerletilerek altdizi küçültülür. Eğer toplam tam olarak `x` olursa, bir çözüm bulunmuş olur.

 `[1, 3, 2, 5, 1, 1, 2, 3]` dizisinde toplamı 8 olan altdiziyi bulmak için iki işaretçi yönteminin adımları

Her iki işaretçi de dizi boyunca sadece ileri doğru hareket ettiği için toplamda en fazla `2n` adım atarlar. Bu yüzden algoritma $O(n)$ zamanda çalışır.

### 2SUM Problemi

**Problem:** `n` sayıdan oluşan bir dizide, toplamı `x` olan iki eleman bulmak.

**Fikir:**

1. Diziyi artan sırada sıralayın.
2. Bir işaretçiyi (`sol`) dizinin başına, diğerini (`sağ`) dizinin sonuna yerleştirin.
3. `array[sol] + array[sağ]` toplamını kontrol edin:
   - Toplam `x`'ten küçükse, daha büyük bir değere ihtiyacımız var demektir, bu yüzden `sol` işaretçisini bir sağa kaydırın.
   - Toplam `x`'ten büyükse, daha küçük bir değere ihtiyacımız var demektir, bu yüzden `sağ` işaretçisini bir sola kaydırın.
   - Toplam `x`'e eşitse, bir çözüm bulunmuştur.
4. İşaretçiler karşılaşana kadar devam edin.

Sıralama $O(n \log n)$, iki işaretçi ile arama ise $O(n)$ sürdüğü için toplam zaman karmaşıklığı $O(n \log n)$ olur. Daha zor bir problem olan **3SUM problemi** (toplamı `x` olan üç eleman bulmak), bu fikir genişletilerek $O(n^2)$ zamanda çözülebilir[^1].

## 8.2 En Yakın Küçük Elemanlar (Nearest Smaller Elements)

**Problem:** Bir dizideki her eleman için, o elemanın solunda bulunan ve kendisinden küçük olan en yakın elemanı bulmak.

**Fikir:** Dizinin solundan sağına doğru ilerlerken bir yığın (stack) kullanılır. Her eleman için:
1. Yığının tepesindeki eleman mevcut elemandan küçük olana kadar veya yığın boşalana kadar yığından eleman çıkarılır.
2. Eğer yığın boş değilse, tepedeki eleman aranan en yakın küçük elemandır.
3. Mevcut eleman yığına eklenir.

`[1, 3, 4, 2, 5, 3, 4, 2]` dizisi için yığının adım adım değişimi

Bir eleman yığına en fazla bir kez eklenip bir kez çıkarıldığı için, her eleman amortize olarak $O(1)$ yığın operasyonu gerektirir. Bu yüzden algoritmanın toplam zaman karmaşıklığı $O(n)$'dir.

## 8.3 Sürgülü Pencere Minimumu (Sliding Window Minimum)

**Problem:** Sabit `k` boyutundaki bir altdizinin (sürgülü pencere), dizi boyunca soldan sağa hareket ederken her pozisyondaki minimum elemanı bulmak.

**Fikir:** Bir `deque` (çift yönlü kuyruk) veri yapısı kullanılır. Bu `deque` her zaman pencere içindeki elemanların indislerini artan değer sırasında tutar. `deque`'in başındaki eleman her zaman o anki pencerenin minimumudur.
Her adımda pencere bir sağa kaydığında:

1. `deque`'in sonundan, yeni eklenecek elemandan daha büyük olan elemanlar çıkarılır.
2. Yeni elemanın indisi `deque`'in sonuna eklenir.
3. `deque`'in başındaki elemanın indisi pencerenin dışına çıkmışsa, baştan çıkarılır.


Her eleman `deque`'e en fazla bir kez eklenip bir kez çıkarıldığı için, bu algoritma da amortize olarak $O(n)$ zamanda çalışır.

[^1]: Uzun bir zaman boyunca 3SUM problemini $O(n^2)$ zamandan daha verimli bir şekilde çözmenin mümkün olmayacağı kabul edilmiştir. Fakat 2014'te bu durumun böyle olmadığı anlaşılmıştır.