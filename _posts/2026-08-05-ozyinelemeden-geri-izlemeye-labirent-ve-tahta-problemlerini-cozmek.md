---
layout: post
title: "Özyinelemeden Geri İzlemeye: Labirent ve Tahta Problemlerini Çözmek"
math: true
categories: 
  - Bilgi
tags: 
  - özyineleme
  - geri izleme
  - algoritmalar
---

Bir labirentin girişinde durduğunuzu düşünün: Her kavşakta bir yön seçiyor, çıkmaza girerseniz son karar noktasına dönüyorsunuz. Özyinelemeli düşünme ve geri izleme tam olarak böyle çalışır. Büyük bir problemi daha küçük benzer problemlere ayırır, olası seçimleri dener ve başarısız seçimlerden vazgeçerek çözümü sistematik biçimde arar.
``
## Özyinelemeli düşünmek ne demektir?

Özyineleme, bir fonksiyonun problemi küçülterek kendisini çağırmasıdır. Sağlıklı bir özyinelemeli çözümün iki temel parçası bulunur:

1. **Temel durum:** Çağrıların duracağı en küçük problem.
2. **Özyinelemeli durum:** Problemi daha küçük bir örneğe dönüştüren adım.

Örneğin faktöriyel şu bağıntıyla tanımlanır:

$$n! = n \cdot (n-1)!$$

Temel durum ise $0! = 1$ olur. Kod karşılığı oldukça doğaldır:

```python
def faktoriyel(n):
    if n == 0:          # Temel durum
        return 1
    return n * faktoriyel(n - 1)
```

Buradaki kritik fikir, fonksiyonun sonsuza kadar çağrılmamasıdır. Her çağrı problemi temel duruma yaklaştırmalıdır. Aksi hâlde çağrı yığını büyür ve program sonunda hata verir.

## Özyineleme ile geri izleme arasındaki fark

Geri izleme, çoğunlukla özyineleme kullanır; ancak her özyinelemeli algoritma geri izleme değildir. Geri izlemede bir seçim yapılır, sonuç araştırılır ve seçim başarısızsa durum eski hâline getirilir.

| Yaklaşım | Temel hareket | Önceki duruma dönüş | Örnek |
|---|---|---|---|
| Özyineleme | Problemi küçültür | Her zaman gerekli değildir | Faktöriyel |
| Geri izleme | Seç, araştır, geri al | Çözüm bulunamazsa gerekir | Sudoku |
| Kaba kuvvet | Tüm olasılıkları dener | Genellikle sistemsizdir | Tüm kombinasyonlar |
| Dinamik programlama | Sonuçları saklar | Aynı hesabı tekrar etmez | Fibonacci |

Geri izlemenin özeti şu üç komuttur: **Seç, keşfet, seçimi geri al.** Bu son adım unutulursa algoritma, önceki yolun izlerini sonraki denemelere taşır.

## Labirentte yol bulma

Bir hücreden yukarı, aşağı, sağa veya sola gidebildiğimizi varsayalım. Duvarlara ve daha önce ziyaret edilen hücrelere giremeyiz. Aşağıdaki fonksiyon, çıkışa ulaştığında `True` döndürür:

```python
def yolu_bul(labirent, satir, sutun, cikis, ziyaret):
    if (satir, sutun) == cikis:
        return True

    if (satir, sutun) in ziyaret:
        return False

    if labirent[satir][sutun] == "#":
        return False

    ziyaret.add((satir, sutun))

    for ds, dt in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        yeni_s, yeni_t = satir + ds, sutun + dt
        if 0 <= yeni_s < len(labirent) and 0 <= yeni_t < len(labirent[0]):
            if yolu_bul(labirent, yeni_s, yeni_t, cikis, ziyaret):
                return True

    ziyaret.remove((satir, sutun))  # Geri izleme
    return False
```

`ziyaret` kümesi döngüleri önler. Hücreden çıkışa ulaşılamazsa hücre kümeden silinir; böylece farklı bir yol aynı hücreyi başka bağlamda deneyebilir. Yalnızca herhangi bir yolu arıyorsak hücreyi silmemek de mümkündür. Ancak tüm yolları üretmek istediğimizde geri alma adımı zorunludur.

## Tahta doldurma: N-Vezir problemi

N-Vezir probleminde $N \times N$ tahtaya, birbirini tehdit etmeyen $N$ vezir yerleştirilir. Her satıra bir vezir koyup yalnızca güvenli sütunları denemek, arama alanını ciddi ölçüde küçültür.

```python
def vezirleri_yerlestir(n, satir=0, sutunlar=set(), capraz1=set(), capraz2=set()):
    if satir == n:
        return True

    for sutun in range(n):
        if sutun in sutunlar or satir - sutun in capraz1 or satir + sutun in capraz2:
            continue

        sutunlar.add(sutun)
        capraz1.add(satir - sutun)
        capraz2.add(satir + sutun)

        if vezirleri_yerlestir(n, satir + 1, sutunlar, capraz1, capraz2):
            return True

        sutunlar.remove(sutun)
        capraz1.remove(satir - sutun)
        capraz2.remove(satir + sutun)

    return False
```

Saf denemede olasılık sayısı yaklaşık $N^N$ olabilir. Geçersiz dalları erkenden budamak ise gereksiz çağrıları engeller. Bu nedenle iyi bir geri izleme çözümünün sırrı yalnızca geri dönmek değil, **ne zaman devam etmemek gerektiğini** erkenden bilmektir.

Özyinelemeli düşünürken önce temel durumu, ardından seçimi ve son olarak geri alma işlemini yazmak yararlıdır. Labirent, Sudoku, N-Vezir ve kelime bulmacaları farklı görünse de aynı macerayı anlatır: Bir kapıyı aç, içeri bak; hazine yoksa kapıyı kapat ve diğerini dene.
