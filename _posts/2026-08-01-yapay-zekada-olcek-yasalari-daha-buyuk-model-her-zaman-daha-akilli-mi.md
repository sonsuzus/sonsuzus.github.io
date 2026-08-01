---
layout: post
title: "Yapay Zekâda Ölçek Yasaları: Daha Büyük Model Her Zaman Daha Akıllı mı?"
math: true
categories: 
  - Bilgi
tags: 
  - yapay zekâ
  - ölçek yasaları
  - büyük dil modelleri
---

Bir dil modeline daha fazla parametre eklemek, ona otomatik olarak daha fazla “zekâ” mı kazandırır? Son yıllardaki dev modeller bu fikri destekliyor gibi görünse de gerçek tablo daha renkli: Boyut önemli, fakat veri kalitesi, eğitim bütçesi, mimari ve modelin nasıl kullanıldığı da en az boyut kadar belirleyici.
``

## Ölçek yasası nedir?

Ölçek yasaları, bir modelin hata oranının model boyutu, veri miktarı ve hesaplama bütçesi arttıkça nasıl değiştiğini açıklayan deneysel ilişkilerdir. Dil modellerinde kayıp değerinin yaklaşık olarak bir kuvvet yasasına uyduğu gözlemlenir:

$$L(N) \approx L_{\infty} + aN^{-\alpha}$$

Burada $L(N)$, $N$ parametreli modelin kaybını; $L_{\infty}$ erişilebilecek teorik alt sınırı; $a$ ve $\alpha$ ise deneylerden öğrenilen sabitleri temsil eder. Denklemdeki kritik ayrıntı, getirinin giderek azalmasıdır. Parametre sayısını iki katına çıkarmak performansı iyileştirebilir, ancak modeli iki kat “akıllı” yapmaz.

Benzer ilişkiler veri miktarı $D$ ve eğitim hesaplaması $C$ için de kurulabilir:

$$L \propto N^{-\alpha}D^{-\beta}C^{-\gamma}$$

Bu formül bir sihirli değnek değil, mühendislik pusulasıdır. Hangi kaynağa yatırım yapılırsa daha fazla kazanç elde edileceğini tahmin etmeye yardımcı olur.

## Boyut tek başına neden yetmez?

Dev bir modeli yetersiz veriyle eğitmek, büyük bir kütüphaneyi aynı kitabın milyonlarca kopyasıyla doldurmaya benzer. Raflar etkileyicidir; bilgi çeşitliliği değildir. Chinchilla yaklaşımı olarak bilinen bulgular, belirli bir hesaplama bütçesinde daha küçük bir modeli daha fazla ve kaliteli veriyle eğitmenin, aşırı büyük fakat eksik eğitilmiş bir modeli geçebileceğini göstermiştir.

| Etken | Artırıldığında olası kazanç | Temel sınır |
|---|---|---|
| Parametre sayısı | Daha karmaşık örüntüler | Maliyet ve azalan getiri |
| Veri miktarı | Daha geniş bilgi kapsamı | Tekrar, telif ve gürültü |
| Veri kalitesi | Daha güvenilir cevaplar | Seçim ve temizleme zorluğu |
| Eğitim hesaplaması | Daha iyi optimizasyon | Enerji ve donanım maliyeti |
| Çıkarım hesaplaması | Daha güçlü akıl yürütme | Gecikme ve kullanım ücreti |

## Yetenek gerçekten “ortaya” mı çıkıyor?

Bazı yeteneklerin belirli bir ölçekte aniden belirdiği söylenir. Buna *emergent abilities*, yani beliren yetenekler denir. Küçük model bir görevi yapamazken büyük model bir anda başarılı görünür. Ancak bu sıçrama bazen ölçüm yönteminden kaynaklanır. Başarı yalnızca “doğru” veya “yanlış” olarak puanlanırsa kademeli gelişim, keskin bir eşik gibi görünebilir.

Dolayısıyla ölçek, yeni yeteneklerin oluşmasını kolaylaştırabilir; fakat her sıçramayı gizemli bir zekâ patlaması olarak yorumlamak doğru değildir. Kullanılan test, istem biçimi ve puanlama yöntemi sonucu ciddi biçimde etkiler.

## Basit bir ölçek hesabı

Aşağıdaki Python kodu, kuvvet yasasını kullanarak farklı model boyutları için tahmini kaybı hesaplar:

```python
import math

def tahmini_kayip(parametre, alt_sinir=1.2, a=3.0, alfa=0.08):
    """Parametre sayısından yaklaşık eğitim kaybı üretir."""
    return alt_sinir + a * math.pow(parametre, -alfa)

boyutlar = [1e8, 1e9, 1e10, 1e11]

for boyut in boyutlar:
    kayip = tahmini_kayip(boyut)
    print(f"{boyut / 1e9:6.1f} milyar parametre -> {kayip:.3f}")
```

Kod gerçek bir modelin performansını kesin olarak tahmin etmez; azalan getiriyi görünür kılan basitleştirilmiş bir deneydir. Katsayılar model ailesine ve veri kümesine göre ölçülmelidir.

## Büyük olmakla akıllı olmak arasındaki mesafe

Daha büyük modeller genellikle daha iyi dil üretir, daha fazla bilgiyi sıkıştırır ve örneklerden daha esnek biçimde öğrenir. Buna rağmen halüsinasyon, güncellik, nedensel akıl yürütme ve güvenilirlik sorunları yalnızca parametre eklenerek çözülmez. İyi veri, araç kullanımı, bilgi getirme sistemleri, ince ayar ve insan geri bildirimi çoğu zaman daha ekonomik ilerleme sağlar.

Sonuç olarak ölçek güçlü bir kaldıraçtır, zekânın tek ölçüsü değildir. En başarılı sistem, mutlaka en büyük model değil; boyut, veri, hesaplama ve kullanım maliyeti arasındaki dengeyi en iyi kuran modeldir.
