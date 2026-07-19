---
layout: post
title: "Geriye İzleme (Backtracking): Çıkmaz Sokaklardan Zekice Dönmek"
math: true
categories: 
  - Bilgi
tags: 
  - algoritma
  - backtracking
  - veri-yapıları
---

Bir labirentte yürüdüğünü düşün: Önünde üç yol var, birini seçiyorsun, ilerliyorsun ve duvara çarpıyorsun. Panik yok! Son karar noktasına geri dönüp denenmemiş diğer yolu seçiyorsun. İşte geriye izleme, yani backtracking, bilgisayarın bu “hmm olmadı, başka kapı deneyelim” refleksidir. Özellikle bulmaca çözme, rota arama, kombinasyon üretme ve kısıt sağlama problemlerinde sistematik şekilde alternatifleri dener.
``
Backtracking’in kalbinde “seç, ilerle, kontrol et, gerekirse geri al” döngüsü vardır. Algoritma bir çözüm adayını parça parça inşa eder. Her adımda mevcut durumun hedefe götürme ihtimali kontrol edilir. Eğer durum kurallara aykırıysa veya artık çözüm üretme şansı yoksa, algoritma o dalı terk eder. Buna budama (pruning) denir. Budama, gereksiz yolları erkenden keserek aramayı hızlandırır.

Teorik olarak backtracking, derinlik öncelikli arama (DFS) mantığına çok benzer. Fakat klasik DFS sadece graf üzerinde dolaşırken, backtracking genellikle “karar ağacı” üzerinde aday çözümler üretir. Her düğüm bir kısmi çözümü, her kenar ise yeni bir seçimi temsil eder. Eğer dallanma faktörü $b$ ve maksimum derinlik $d$ ise kaba kuvvetle arama maliyeti yaklaşık $O(b^d)$ olabilir. Bu yüzden akıllı kontrol fonksiyonları çok önemlidir.

| Kavram | Ne Anlama Gelir? | Backtracking’de Rolü |
|---|---|---|
| Durum | O ana kadar yapılan seçimler | Kısmi çözümü temsil eder |
| Seçenek | Bir sonraki hamle | Yeni dallar oluşturur |
| Kısıt | Uyulması gereken kural | Geçersiz yolları eler |
| Geri alma | Son seçimi iptal etme | Alternatifleri denemeyi sağlar |
| Budama | Umutsuz dalı kesme | Performansı artırır |

Basit bir formül gibi düşünürsek algoritmanın davranışı şöyle özetlenebilir: $Çözüm = Seçim + Kısıt\ Kontrolü + Geri\ Alma$. Yani yalnızca denemek değil, denediğini akıllıca geri sarmak önemlidir. Bu yüzden backtracking, “kaba kuvvetin gözlük takmış hali” olarak düşünülebilir.

En meşhur örneklerden biri N-Queens problemidir. Ama daha basit bir örnekle başlayalım: Verilen sayılardan toplamı hedef değere eşit olan bir alt küme bulmak. Aşağıdaki Python kodu, her sayıyı “al” veya “alma” kararlarıyla ilerler; çıkmaza girince önceki adıma döner.

```python
def subset_sum(nums, target):
    result = []

    def backtrack(index, current, total):
        # Hedefe ulaşıldıysa çözümü kaydet
        if total == target:
            result.append(current.copy())
            return

        # Liste bitti veya toplam hedefi geçtiyse bu dalı bırak
        if index == len(nums) or total > target:
            return

        # 1. seçenek: mevcut sayıyı al
        current.append(nums[index])
        backtrack(index + 1, current, total + nums[index])

        # Geri alma: son eklenen sayıyı çıkar
        current.pop()

        # 2. seçenek: mevcut sayıyı alma
        backtrack(index + 1, current, total)

    backtrack(0, [], 0)
    return result

print(subset_sum([2, 3, 5, 7], 10))
```

Bu kodda `current.append(...)` bir karar vermektir. `current.pop()` ise o kararı geri almaktır. Bu ikili, backtracking’in sahnedeki dansıdır: bir adım ileri, gerekirse bir adım geri. Eğer `total > target` olursa algoritma o yolu sürdürmez; çünkü pozitif sayılarla hedefe geri inme şansı yoktur. İşte bu küçük kontrol ciddi performans kazandırır.

Backtracking ile dinamik programlama sık karıştırılır. İkisi de “zor problemi küçük parçalara bölme” fikrini sever, ama yaklaşımları farklıdır.

| Özellik | Backtracking | Dinamik Programlama |
|---|---|---|
| Temel fikir | Alternatifleri dene, geçersizse geri dön | Alt problemlerin sonuçlarını sakla |
| Kullanım | Kombinasyon, permütasyon, bulmaca | Optimizasyon, tekrar eden alt problemler |
| Bellek kullanımı | Genellikle daha düşük | Tablo nedeniyle daha yüksek olabilir |
| Performans | Budamaya çok bağlı | Tekrarları önlediği için düzenli |

Backtracking’in kullanıldığı popüler alanlar arasında Sudoku çözümü, 8 vezir problemi, labirent rotası bulma, şifre kombinasyonu denemeleri, graf renklendirme ve kısıt tatmin problemleri vardır. Mesela Sudoku’da her boş hücreye 1’den 9’a kadar sayı denenir; satır, sütun veya kutu kuralı bozulursa sayı geri alınır. Bilgisayar sabırlı bir bulmaca çözücüye dönüşür.

Elbette backtracking her derde deva değildir. Seçenek sayısı çok büyükse ve iyi budama yoksa algoritma yavaşlayabilir. Bu durumda sezgisel sıralama, erken kontrol, memoization veya problemi matematiksel olarak daraltma gibi teknikler eklenir. Örneğin önce en kısıtlı hücreyi seçmek, Sudoku’da arama ağacını dramatik şekilde küçültebilir.

Sonuç olarak geriye izleme, yazılım dünyasının “denedim, olmadı, akıllıca geri döndüm” stratejisidir. Onu güçlü yapan şey sadece tüm yolları denemesi değil; yanlış yollardan zamanında vazgeçmesidir. Eğer bir problem “bir sürü ihtimal var ama kurallar geçersizleri elememi sağlıyor” diyorsa, backtracking büyük ihtimalle kapıda bekleyen kahramandır.
