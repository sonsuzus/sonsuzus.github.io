---
layout: post
title: "Birim Testleri ve Profil Analizi: Koduna Dedektif Gibi Yaklaş"
math: true
categories: 
  - Bilgi
tags: 
  - unit-testing
  - pytest
  - profiling
  - performans
  - yazılım-kalitesi
---

Kod yazmak bazen Lego yapmak gibidir: Parçalar tek tek güzel görünür ama kuleyi kaldırınca ortadan ikiye ayrılıyorsa bir yerde hata vardır. Birim testleri, bu Lego parçalarının tek başına sağlam olup olmadığını kontrol eder. Profil analizi ise aynı parçaların ne kadar hızlı, ne kadar bellekle ve hangi maliyetle çalıştığını gösterir. Yani biri doğruluk dedektifi, diğeri performans dedektifidir.
``
Birim testinin temel fikri basittir: Büyük bir sistemi küçük davranışlara ayırır, her davranışı izole biçimde sınarız. Bir fonksiyonun beklenen çıktıyı üretip üretmediğini test etmek, yazılımın matematiksel olarak daha güvenilir hale gelmesine yardım eder. Elbette testler mutlak ispat değildir; fakat doğru seçilmiş örnekler, sınır durumları ve hata senaryolarıyla güven düzeyini ciddi biçimde artırır.

Bir fonksiyonu $f(x)$ gibi düşünelim. Test yazarken aslında belirli girdiler için şu önermeyi kontrol ederiz: $f(girdi) = beklenen\_çıktı$. Örneğin indirim hesaplayan bir fonksiyonda $f(100, 0.2) = 80$ olmalıdır. Eğer bu önerme bozulursa test kırmızıya döner ve bize şunu söyler: Kodun davranışı ile beklentin aynı evrende yaşamıyor.

| Kavram | Ne Kontrol Eder? | Tipik Soru |
|---|---|---|
| Birim testi | Doğruluk | Fonksiyon doğru sonucu veriyor mu? |
| Entegrasyon testi | Parçalar arası uyum | Modüller birlikte çalışıyor mu? |
| Profil analizi | Performans | Zaman ve bellek nerede harcanıyor? |
| Benchmark | Karşılaştırmalı hız | A yöntemi mi B yöntemi mi hızlı? |

Birim testlerinde yaygın desen Arrange-Act-Assert üçlüsüdür. Önce ortamı hazırlarız, sonra fonksiyonu çalıştırırız, en sonunda sonucu doğrularız. Python ve pytest ile küçük ama anlamlı bir örnek görelim:

```python
def calculate_discount(price, rate):
    if price < 0:
        raise ValueError('price cannot be negative')
    if not 0 <= rate <= 1:
        raise ValueError('rate must be between 0 and 1')
    return price * (1 - rate)


def test_calculate_discount_normal_case():
    # Arrange
    price = 100
    rate = 0.25

    # Act
    result = calculate_discount(price, rate)

    # Assert
    assert result == 75


def test_calculate_discount_rejects_negative_price():
    import pytest
    with pytest.raises(ValueError):
        calculate_discount(-10, 0.2)
```

Bu testler sadece normal senaryoyu değil, hata senaryosunu da kontrol eder. İyi test yazmanın püf noktası, mutlu yol kadar mutsuz yolları da düşünmektir. Çünkü kullanıcılar her zaman bizim hayal ettiğimiz gibi davranmaz; bazen eksi fiyat girerler, bazen yüzde 400 indirim isterler, bazen de sistemin sabrını sınarlar.

Test kapsamı konuşulurken sıkça coverage oranı gündeme gelir. Diyelim ki projenizde 100 satır çalıştırılabilir kod var ve testler 85 satırı çalıştırıyor. Kapsam yaklaşık $Coverage = \frac{85}{100} \times 100 = 85\%$ olur. Ancak dikkat: Yüksek coverage, kaliteli test anlamına her zaman gelmez. Bir satırı çalıştırmak başka, onun doğru davrandığını doğrulamak başkadır.

| İyi Test | Kötü Test |
|---|---|
| Tek davranışı sınar | Her şeyi aynı anda test eder |
| Okunabilir isim taşır | test1, test2 gibi belirsizdir |
| Sınır durumlarını içerir | Sadece kolay örnekleri dener |
| Deterministiktir | Bazen geçer bazen kalır |

Gelelim profil analizine. Kod doğru olabilir ama yavaşsa kullanıcı yine mutsuz olur. Python’da cProfile, hangi fonksiyonun kaç kez çağrıldığını ve toplamda ne kadar süre harcadığını gösterir:

```python
import cProfile

def slow_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

if __name__ == '__main__':
    data = range(10_000_000)
    cProfile.run('slow_sum(data)')
```

Bu çıktı bize darboğazları gösterir. Performans analizinde önemli olan tahminle değil ölçümle hareket etmektir. Çünkü geliştiricinin iç sesi çoğu zaman dramatiktir: “Kesin şu döngü yavaş!” Profil aracı ise sakin bir şekilde “Hayır dostum, asıl sorun veritabanı çağrısında” diyebilir.

Birim testleri ve profil araçları birlikte kullanıldığında güvenli refactoring mümkün olur. Önce testlerle davranışı sabitlersin, sonra profille yavaş noktaları bulursun, ardından kodu iyileştirirsin. Son adımda testleri tekrar çalıştırırsın. Eğer testler yeşilse ve profil daha iyiyse, kodun hem doğru hem de daha fit hale gelmiştir.

Özetle, test yazmak zaman kaybı değil, gelecekteki panik anlarına yapılan yatırımdır. Profil analizi de optimizasyonu falcılıktan çıkarıp mühendisliğe dönüştürür. Koduna küçük bir laboratuvar kur: testlerle doğrula, profille ölç, sonra gönül rahatlığıyla geliştir.
