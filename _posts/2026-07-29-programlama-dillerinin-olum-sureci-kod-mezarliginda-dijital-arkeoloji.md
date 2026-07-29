---
layout: post
title: "Programlama Dillerinin Ölüm Süreci: Kod Mezarlığında Dijital Arkeoloji"
math: true
categories: 
  - Bilgi
tags: 
  - programlama dilleri
  - dijital arkeoloji
  - yazılım tarihi
---

Bir programlama dili nadiren tek bir gün içinde ölür. Genellikle önce yeni projelerden çekilir, sonra geliştiricilerini kaybeder, paket depoları sessizleşir ve en sonunda yalnızca eski bankacılık sistemlerinde ya da unutulmuş bir GitHub deposunda yaşamaya devam eder. Dolayısıyla bir dilin ölümünü anlamak, mezar taşındaki tarihi okumaktan çok geride bıraktığı dijital izleri incelemeye benzer.

``

## Ölüm, kullanımın sıfırlanması değildir

Bir dili “ölü” saymak için kullanım oranının sıfıra düşmesini beklersek neredeyse hiçbir dil ölmez. COBOL, 1959 doğumlu olmasına rağmen finans ve kamu altyapılarında çalışmayı sürdürüyor. Objective-C yeni mobil projelerde eski cazibesini kaybetti; fakat milyonlarca satırlık iOS kodunda hâlâ mevcut.

Bu nedenle üç farklı durumu ayırmak gerekir:

| Durum | Belirti | Tipik sonuç |
|---|---|---|
| Yaşayan | Yeni sürümler, paketler ve projeler vardır | Ekosistem büyür |
| Miras dili | Bakım sürer, yeni kullanım azalır | Kurumsal sistemlerde yaşar |
| Ölü dil | Resmî bakım ve üretken topluluk yoktur | Arşiv veya hobi nesnesine dönüşür |

Ölüm burada teknik değil, **sosyoteknik** bir kavramdır. Derleyici hâlâ çalışabilir; ancak onu geliştiren, öğreten ve yeni problemlere uyarlayan topluluk ortadan kalkmış olabilir.

## Dijital nabız nasıl ölçülür?

Bir dilin sağlığını tek bir popülerlik listesiyle ölçmek yanıltıcıdır. Arama motoru sorguları merakı, GitHub depoları açık kaynak faaliyetini, iş ilanları ise ekonomik talebi gösterir. Sağlıklı bir inceleme birkaç sinyali birleştirir:

- Son kararlı sürümün yaşı
- Aylık paket yayımlama sayısı
- Aktif katkıcı ve depo sayısı
- Stack Overflow soru eğilimi
- İş ilanları ve eğitim içerikleri
- Alternatif dillere gerçekleşen geliştirici göçü

Basit bir “yaşam skoru” şöyle modellenebilir:

$$L = 0.30R + 0.25C + 0.20P + 0.15J + 0.10E$$

Burada $R$ sürüm etkinliğini, $C$ katkıcı sayısını, $P$ paket hareketliliğini, $J$ iş talebini ve $E$ eğitim ekosistemini temsil eder. Her değişken $0$ ile $100$ arasında normalize edilir. Elbette katsayılar evrensel değildir; kurumsal dillerde iş talebi, akademik dillerde yayın ve eğitim etkinliği daha ağır basabilir.

## Topluluk göçü: Asıl ölüm ilanı

Geliştiriciler çoğu zaman dilden önce problemlerine sadıktır. Daha güvenli, hızlı veya kullanışlı bir alternatif ortaya çıktığında topluluk yavaşça göç eder. Perl’den Python ve Ruby’ye, Objective-C’den Swift’e, eski JavaScript araçlarından TypeScript tabanlı ekosistemlere geçiş bunun örnekleridir.

Göçün kritik işareti yalnızca kullanıcı kaybı değildir. Kütüphane yazarlarının yeni dili tercih etmesi daha önemlidir. Çünkü paketler gidince uygulama geliştirmek zorlaşır; uygulamalar azalınca iş ilanları düşer; iş azalınca yeni öğrenciler başka dillere yönelir. Böylece kendini besleyen bir çöküş döngüsü oluşur.

## Küçük bir arkeoloji aracı

Aşağıdaki Python kodu, yıllara göre yeni depo sayılarını inceleyerek doğrusal eğilimi hesaplar. Negatif eğim tek başına ölüm kanıtı değildir; fakat uzun süre devam ediyorsa güçlü bir uyarıdır.

```python
from statistics import linear_regression

repos = {
    2019: 840,
    2020: 760,
    2021: 610,
    2022: 470,
    2023: 350,
    2024: 240
}

years = list(repos.keys())
counts = list(repos.values())
slope, intercept = linear_regression(years, counts)

print(f'Yıllık değişim: {slope:.1f} depo')
if slope < -50:
    print('Uzun süreli topluluk daralması araştırılmalı.')
```

Gerçek bir araştırmada yıldız sayısı yerine aktif depolar, benzersiz katkıcılar ve arşivlenmiş proje oranı kullanılmalıdır. Bot etkinliği ve çatallanmış depolar da temizlenmelidir.

## Peki ne zaman resmen ölüdür?

Bir dil; resmî uygulaması terk edildiğinde, güvenlik sorunları giderilmediğinde, paket ekosistemi durduğunda ve topluluğu halef teknolojilere göç ettiğinde pratik olarak ölü kabul edilebilir. Yine de bu bir cenazeden çok dönüşümdür. Bazı diller fikirlerini haleflerine miras bırakır, bazıları retro meraklıları tarafından diriltilir. Dijital mezarlıklarda bile kod tamamen susmaz; yalnızca onu dinleyenlerin sayısı azalır.
