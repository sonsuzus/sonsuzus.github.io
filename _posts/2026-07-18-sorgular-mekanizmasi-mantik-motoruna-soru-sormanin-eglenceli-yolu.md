---
layout: post
title: "Sorgular Mekanizması: Mantık Motoruna Soru Sormanın Eğlenceli Yolu"
math: true
categories: 
  - Bilgi
tags: 
  - mantıksal programlama
  - sorgular
  - Prolog
  - kural motoru
---

Bir bilgi tabanınız olduğunu düşünün: içinde gerçekler, kurallar ve biraz da dedektiflik kokan ilişkiler var. Sorgular mekanizması, bu yapıya dışarıdan soru sormamızı sağlar: Bu sonuç doğru mu, yanlış mı, yoksa sistemin bildikleriyle kanıtlanamıyor mu? Kısacası sorgu, mantık motoruna yöneltilen kontrollü bir mercek gibidir; veriyi ezberlemek yerine, sonuç çıkarmayı otomatikleştirir.
``
Sorgular özellikle mantıksal programlama, uzman sistemler, kural motorları ve bilgi grafikleri gibi alanlarda çok kullanılır. Temel fikir şudur: önce sisteme bazı gerçekler verilir, sonra bu gerçeklerden yeni bilgiler türetebilecek kurallar tanımlanır. Ardından kullanıcı, sisteme bir önerme yöneltir. Sistem de bu önermenin bilgi tabanı tarafından desteklenip desteklenmediğini araştırır.

Teorik olarak bir sorgu, bir mantıksal ifadenin bilgi tabanından türetilip türetilemeyeceğini sorar. Bunu şöyle yazabiliriz: $KB \models q$. Burada $KB$ bilgi tabanını, $q$ ise sorguyu temsil eder. İfade şu anlama gelir: Bilgi tabanı doğru kabul edildiğinde, sorgu da zorunlu olarak doğru mudur? Eğer sistem bunu kanıtlayabiliyorsa sonuç true, kanıtlayamıyorsa çoğu mantıksal programlama sisteminde false döner.

| Kavram | Anlamı | Mini Örnek |
|---|---|---|
| Gerçek | Doğrudan bilinen bilgi | parent(ayse, mehmet) |
| Kural | Yeni bilgi üretme şablonu | grandparent(X, Z) :- parent(X, Y), parent(Y, Z) |
| Sorgu | Sisteme sorulan mantıksal soru | grandparent(ayse, zeynep)? |
| Çıkarım | Kurallarla sonuca ulaşma süreci | Ayşe, Zeynep'in büyükannesi mi? |

Basit bir Prolog benzeri örnek üzerinden gidelim:

```prolog
parent(ayse, mehmet).
parent(mehmet, zeynep).

grandparent(X, Z) :- parent(X, Y), parent(Y, Z).

?- grandparent(ayse, zeynep).
```

Bu kodda ilk iki satır gerçektir. Üçüncü satır ise bir kuraldır: X, Y'nin ebeveyni ve Y de Z'nin ebeveyni ise X, Z'nin büyükanne veya büyükbabasıdır. Sorgu çalıştırıldığında sistem değişkenleri eşleştirir, yani unification yapar. $X = ayse$, $Y = mehmet$, $Z = zeynep$ değerleriyle kural sağlandığı için cevap true olur.

Sorgu motorunun çalışma mantığı genellikle geriye doğru zincirleme ile açıklanır. Motor, hedef sonucu kanıtlamak için şu soruyu sorar: Bu hedef hangi alt hedeflere bağlı? Sonra alt hedefleri tek tek çözmeye çalışır. Bir bakıma final sorusundan başlayıp ipuçlarını geriye doğru takip eden bir dedektif gibi davranır.

| Yaklaşım | Nereden Başlar? | Ne Zaman Kullanışlı? |
|---|---|---|
| Geriye doğru zincirleme | Sorgudan | Belirli bir sorunun cevabı aranırken |
| İleri doğru zincirleme | Gerçeklerden | Tüm olası sonuçlar önceden çıkarılacaksa |
| SQL sorgusu | Tablolardan | Yapısal veri filtrelenecekse |
| Mantıksal sorgu | Kurallar ve gerçeklerden | İlişkisel çıkarım gerekiyorsa |

Buradaki önemli ayrım şudur: SQL genellikle var olan satırları filtrelerken, mantıksal sorgular var olmayan ama türetilebilen bilgileri de bulabilir. Örneğin tabloda doğrudan büyükebeveyn bilgisi bulunmayabilir; ama ebeveyn ilişkilerinden bu bilgi hesaplanabilir. Yani sorgu motoru yalnızca arama yapmaz, akıl yürütür.

Küçük bir Python benzeri taslakla bu fikri sezgisel olarak görebiliriz:

```python
facts = {
    ('parent', 'ayse', 'mehmet'),
    ('parent', 'mehmet', 'zeynep')
}

def is_grandparent(x, z):
    for relation, a, y in facts:
        if relation == 'parent' and a == x:
            if ('parent', y, z) in facts:
                return True
    return False

print(is_grandparent('ayse', 'zeynep'))
```

Bu örnek, kural motorunun yaptığı işi sadeleştirerek gösterir. Gerçekler kümesi içinde uygun ara kişi aranır. Eğer $parent(x, y)$ ve $parent(y, z)$ aynı anda sağlanıyorsa, $grandparent(x, z)$ sonucu true kabul edilir.

Elbette gerçek sistemlerde işler biraz daha karmaşıktır. Değişken bağlama, geri izleme, çakışan kurallar, sonsuz döngüler ve kapalı dünya varsayımı gibi konular devreye girer. Kapalı dünya varsayımı özellikle önemlidir: Sistem bir bilgiyi kanıtlayamıyorsa onu yanlış kabul eder. Bu, günlük hayattaki bilmiyorum ile aynı şey değildir. Mantıksal sistem açısından kanıt yoksa cevap çoğu zaman false olur.

Sonuç olarak sorgular mekanizması, kural ve gerçeklerden oluşan bir bilgi tabanını pasif bir veri yığını olmaktan çıkarır. Ona soru sorabilir, ilişkileri test edebilir ve yeni sonuçları otomatik olarak keşfedebiliriz. İyi tasarlanmış sorgular, yazılımınıza küçük ama çalışkan bir mantık asistanı eklemek gibidir: az konuşur, çok çıkarım yapar.
