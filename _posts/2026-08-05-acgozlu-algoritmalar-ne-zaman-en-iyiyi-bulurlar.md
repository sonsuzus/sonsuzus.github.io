---
layout: post
title: "Açgözlü Algoritmalar: Ne Zaman En İyiyi Bulurlar?"
math: true
categories: 
  - Bilgi
tags: 
  - açgözlü algoritmalar
  - aktivite seçimi
  - algoritma analizi
---

Açgözlü algoritmalar, her adımda o an için en cazip seçeneği tercih eder. Geleceği ayrıntılı biçimde hesaplamaz, geçmiş kararlarını da değiştirmezler. Bu yaklaşım biraz “önce en güzel kurabiyeyi kap, gerisini sonra düşünürüz” tavrına benzer. Şaşırtıcı biçimde bazı problemlerde bu basit strateji gerçekten optimal sonucu verirken, bazılarında bizi kurabiye kırıntılarıyla baş başa bırakır.

``

## Açgözlü yaklaşımın temel mantığı

Bir optimizasyon problemi, belirli kısıtlar altında bir amaç fonksiyonunu en küçük veya en büyük yapmayı hedefler. Açgözlü algoritma ise çözümü adım adım kurar ve her aşamada yerel olarak en iyi görünen kararı verir.

Bir çözüm $S$ ve seçilebilecek adaylar kümesi $C$ olsun. Algoritma her adımda yaklaşık olarak şu seçimi yapar:

$$x^* = \arg\max_{x \in C} kazanç(x)$$

Ancak yerel maksimumun küresel maksimuma eşit olması garanti değildir. Açgözlü yöntemin optimal olması için problemde genellikle iki önemli özellik aranır:

1. **Açgözlü seçim özelliği:** Yerel olarak en iyi seçim, en az bir optimal çözümün parçası olmalıdır.
2. **Optimal alt yapı:** Optimal çözümün içinde kalan alt problemler de optimal biçimde çözülmelidir.

| Özellik | Sorduğumuz soru | Anlamı |
|---|---|---|
| Açgözlü seçim | İlk yerel seçim güvenli mi? | Bu seçim optimal çözüme dönüştürülebilir. |
| Optimal alt yapı | Kalan problem bağımsız mı? | Kalan kısmın optimal çözümü kullanılabilir. |
| Geri dönmeme | Karar değiştirilecek mi? | Açgözlü algoritma seçimini kalıcı yapar. |

## Optimal olduğunu nasıl kanıtlarız?

En yaygın yöntemlerden biri **değiş tokuş argümanıdır**. Önce herhangi bir optimal çözüm düşünülür. Eğer bu çözüm açgözlü seçimi içermiyorsa, çözümdeki başka bir seçim açgözlü seçimle değiştirilir. Değişiklik çözümün geçerliliğini ve değerini bozmuyorsa, açgözlü seçimi içeren bir optimal çözüm bulunduğu kanıtlanır.

İkinci adımda problem küçültülür. İlk güvenli seçim yapıldıktan sonra kalan bölümün aynı yapıda bir alt problem olduğu gösterilir. Böylece tümevarım kullanılarak algoritmanın tamamının optimal olduğu sonucuna ulaşılır.

## Klasik örnek: Aktivite seçimi

Her aktivitenin başlangıç zamanı $s_i$ ve bitiş zamanı $f_i$ olsun. Amaç, zamanları çakışmayan en fazla sayıda aktiviteyi seçmektir. Doğru açgözlü kural şudur: **En erken biten uygun aktiviteyi seç.**

Neden en kısa süreni veya en erken başlayanı seçmiyoruz?

| Strateji | Optimal mi? | Sorun |
|---|---:|---|
| En erken biteni seç | Evet | Gelecek aktiviteler için en fazla alanı bırakır. |
| En erken başlayanı seç | Hayır | Çok geç biten bir aktivite seçilebilir. |
| En kısa süreliyi seç | Hayır | Konumu kötü olduğu için iki aktiviteyi engelleyebilir. |

Örneğin aktiviteler $(1,4)$, $(3,5)$, $(0,6)$, $(5,7)$ ve $(8,9)$ ise önce $(1,4)$ seçilir. Ardından başlangıcı 4 veya daha büyük olanlar arasından $(5,7)$, sonra $(8,9)$ alınır. Sonuç üç aktivitedir.

```python
def aktivite_sec(aktiviteler):
    # Aktiviteleri bitiş zamanına göre sıralar.
    aktiviteler.sort(key=lambda aktivite: aktivite[1])

    secilenler = []
    son_bitis = float("-inf")

    for baslangic, bitis in aktiviteler:
        # Önceki aktivite bittiyse bu seçim güvenlidir.
        if baslangic >= son_bitis:
            secilenler.append((baslangic, bitis))
            son_bitis = bitis

    return secilenler
```

Sıralama $O(n \log n)$, tarama ise $O(n)$ sürdüğünden toplam karmaşıklık $O(n \log n)$ olur. Veriler zaten bitiş zamanına göre sıralıysa süre $O(n)$ seviyesine iner.

## Açgözlülüğün tökezlediği yerler

Para üstü probleminde standart madeni paralarla en büyük değeri seçmek işe yarayabilir. Fakat para değerleri $\{1,3,4\}$ ve hedef $6$ olduğunda açgözlü yöntem $4+1+1$ ile üç para kullanır; optimal çözüm $3+3$ ile iki paradır. Demek ki hızlı ve sezgisel görünmek kanıt yerine geçmez.

Kısacası bir açgözlü algoritmaya güvenmeden önce güvenli seçimi tanımlayın, değiş tokuş argümanını kurun ve kalan problemin optimal alt yapıya sahip olduğunu gösterin. Bu üçlü sağlanıyorsa açgözlü yaklaşım yalnızca hızlı değil, matematiksel olarak da iştah açıcıdır.
