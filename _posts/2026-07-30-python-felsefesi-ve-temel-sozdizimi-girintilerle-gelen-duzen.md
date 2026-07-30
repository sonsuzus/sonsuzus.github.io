---
layout: post
title: "Python Felsefesi ve Temel Sözdizimi: Girintilerle Gelen Düzen"
math: true
categories: 
  - Bilgi
tags: 
  - Python
  - Sözdizimi
  - Temiz Kod
---

Python öğrenmeye başladığınızda ilk şaşkınlık genellikle şudur: “Süslü parantezler nerede?” Cevap basit ama önemlidir: Python, kod bloklarını `{}` karakterleriyle değil, girintiyle tanımlar. Bu tercih yalnızca farklı bir sözdizimi oluşturmaz; programcıyı düzenli, sade ve okunabilir kod yazmaya yönlendiren bilinçli bir tasarım felsefesini temsil eder.

``

## Python felsefesi: Kod insanlar içindir

Python’ın yaklaşımı, Tim Peters tarafından yazılan **The Zen of Python** ilkelerinde özetlenir. Bu ilkeleri görmek için Python yorumlayıcısında aşağıdaki komut çalıştırılabilir:

```python
import this
```

Karşımıza çıkan metindeki en ünlü ifadelerden biri şudur: **“Readability counts.”**, yani “Okunabilirlik önemlidir.” Python’a göre kod yalnızca bilgisayarın çalıştıracağı komutlardan ibaret değildir. Aynı zamanda başka geliştiricilerin ve gelecekteki hâlimizin okuyacağı teknik bir anlatıdır.

Bu düşünceyi basitçe şöyle modelleyebiliriz:

$$Kod\ Kalitesi = Doğruluk + Okunabilirlik + Sürdürülebilirlik$$

Program doğru sonuç üretse bile anlaşılması çok zorsa bakım maliyeti yükselir. Python, görsel düzeni sözdiziminin bir parçası yaparak bu sorunu azaltmaya çalışır.

## Girinti nasıl blok oluşturur?

C, Java ve JavaScript gibi dillerde bir bloğun başlangıcı ve sonu süslü parantezlerle belirtilir. Python’da ise aynı hizadaki satırlar aynı bloğa aittir.

| Özellik | Süslü parantezli diller | Python |
|---|---|---|
| Blok başlangıcı | `{` karakteri | Girinti artışı |
| Blok sonu | `}` karakteri | Önceki girinti seviyesine dönüş |
| Görsel düzen | Çalışmayı etkilemeyebilir | Sözdiziminin zorunlu parçasıdır |
| Yaygın standart | Değişken olabilir | Genellikle dört boşluk |

Aşağıdaki örnekte `if` satırından sonra gelen iki komut aynı girinti seviyesindedir ve koşul bloğuna dahildir:

```python
sicaklik = 28

if sicaklik > 25:
    print('Hava sıcak.')
    print('Su içmeyi unutma!')

print('Program tamamlandı.')
```

Koşul doğruysa girintili iki satır çalışır. Son satır sola döndüğü için `if` bloğunun dışındadır ve koşuldan bağımsız olarak yürütülür. Buradaki iki nokta `:`, yeni bir kod bloğunun başlayacağını haber verir.

## Girinti seviyelerinin mantığı

Her iç içe blok, bir önceki seviyeye göre daha fazla girintilenir. Girinti düzeyi $n$, standart olarak kullanılan boşluk sayısı da $4$ ise satırın toplam girintisi yaklaşık olarak şöyle düşünülebilir:

$$Girinti(n) = 4n$$

Örneğin bir döngünün içindeki koşul ikinci seviyededir ve sekiz boşluk kullanır:

```python
sayilar = [3, 8, 11, 14]

for sayi in sayilar:
    if sayi % 2 == 0:
        print(f'{sayi} çift sayıdır.')
    else:
        print(f'{sayi} tek sayıdır.')
```

Bu kod, listedeki sayıları dolaşır ve `%` operatörüyle kalanı kontrol eder. Girintiler sayesinde döngü, koşul ve alternatif dal gözle kolayca ayırt edilir.

## Boşluk mu, sekme mi?

Python teknik olarak sekmelerle girintiye izin verse de **PEP 8**, her seviye için dört boşluk kullanılmasını önerir. Boşluk ve sekmeyi aynı dosyada karıştırmak `TabError` hatasına veya editörler arasında farklı görünümlere yol açabilir.

| Tercih | Avantaj | Risk |
|---|---|---|
| Dört boşluk | Tutarlı ve PEP 8 uyumlu | Elle yazarken daha fazla tuşlama |
| Sekme | Tek tuşla girinti | Görünüm ayara göre değişebilir |
| Karışık kullanım | Belirgin avantajı yok | Hata ve hizalama problemi |

Modern editörler Tab tuşuna basıldığında otomatik olarak dört boşluk ekleyebilir. Böylece hem hız hem tutarlılık elde edilir.

## Okunabilirliğin pratik sonucu

Python’ın girinti zorunluluğu ilk başta katı görünebilir; aslında ekip içinde ortak bir görsel dil oluşturur. Gereksiz parantezler azalır, blokların kapsamı hızla anlaşılır ve kötü biçimlendirilmiş kod daha yazılmadan engellenir. Kısacası girinti, Python’da dekorasyon değil anlamdır. Bu yaklaşımı benimsediğinizde yalnızca çalışan programlar değil, başkalarının keyifle okuyabileceği temiz ve sürdürülebilir yazılımlar üretmeye başlarsınız.
