---
layout: post
title: "Her On Yılın “Nihai Programlama Dili”: Bitmeyen Teknolojik İyimserlik Döngüsü"
math: true
categories: 
  - Bilgi
tags: 
  - programlama dilleri
  - teknoloji tarihi
  - yazılım kültürü
---

Yazılım dünyası belirli aralıklarla aynı heyecanı yeniden yaşar: Yeni bir programlama dili çıkar, eski dillerin bütün kusurlarını çözdüğü söylenir ve kısa süre içinde onun “geleceğin tek dili” olacağı ilan edilir. Fakat gelecek geldiğinde o dil ya belirli bir alana yerleşmiş, başka araçlarla birlikte kullanılmaya başlanmış ya da sessizce teknoloji tarihindeki yerini almıştır. Bu durum yalnızca pazarlama hevesi değil; yazılımın doğasından kaynaklanan döngüsel bir iyimserliktir.

``

## Dün de “gelecek” bugünkü kadar parlaktı

1950’lerde FORTRAN, makine kodunun zahmetini ortadan kaldırarak bilimsel programlamayı dönüştürdü. 1960’larda COBOL, iş dünyasının ortak dili olma iddiasıyla yükseldi. 1980’lerde nesne yönelimli programlama, karmaşıklığı sınıflar ve nesnelerle kontrol edecekti. 1990’larda Java’nın “bir kez yaz, her yerde çalıştır” sloganı platform bağımsızlığını vaat etti. 2010’larda Go sadeliği, Rust ise bellek güvenliğini merkeze aldı.

Bu dillerin hiçbiri başarısız değildir. Hatta bazıları olağanüstü başarılıdır. Yanlış olan, belirli bir dönemin baskın problemini çözmenin bütün gelecek problemlerini çözmek anlamına geldiğini düşünmektir.

| Dönem | Öne çıkan yaklaşım | Büyük vaat | Karşılaşılan gerçeklik |
|---|---|---|---|
| 1950–1960 | FORTRAN, COBOL | Donanım ayrıntılarından kurtulmak | Taşınabilirlik ve bakım sorunları |
| 1980–1990 | C++, Smalltalk | Karmaşıklığı nesnelerle yönetmek | Derin kalıtım ve sıkı bağımlılık |
| 1990–2000 | Java | Her platformda aynı program | Sanal makine maliyeti ve ekosistem yükü |
| 2010–2020 | Go, Rust | Basit eşzamanlılık veya güvenli sistemler | Öğrenme eğrisi ve alan bağımlılığı |
| 2020 sonrası | Yeni nesil diller ve yapay zekâ | Kodlama yükünü büyük ölçüde kaldırmak | Doğrulama, güvenlik ve bakım ihtiyacı |

## Neden tek bir dil yetmiyor?

Programlama dili tasarımı bir optimizasyon problemidir. Bir dilin sadelik, performans, güvenlik, taşınabilirlik ve ifade gücü gibi hedefleri aynı anda en üst düzeye çıkarması beklenir. Ancak pratikte bu hedefler arasında ödünleşim vardır. Bunu kabaca şöyle gösterebiliriz:

$$Q = w_sS + w_pP + w_gG + w_tT - C$$

Burada $S$ sadeliği, $P$ performansı, $G$ güvenliği, $T$ taşınabilirliği, $C$ ise öğrenme ve işletme maliyetini temsil eder. $w$ katsayıları projeye göre değişir. Bir oyun motorunda performansın ağırlığı yüksekken finans uygulamasında güvenlik, küçük bir otomasyon betiğinde ise geliştirme hızı daha önemli olabilir. Dolayısıyla evrensel “en iyi dil” yoktur; yalnızca belirli koşullar için uygun diller vardır.

Üstelik her soyutlama bir alt katmana dayanır. Basit görünen bir işlem bile çalışma zamanı, işletim sistemi ve donanımla ilişkilidir:

```python
from concurrent.futures import ThreadPoolExecutor

def hesapla(sayi):
    # İş yükünü temsil eden basit bir hesaplama yapar.
    return sayi * sayi

with ThreadPoolExecutor(max_workers=4) as havuz:
    sonuclar = list(havuz.map(hesapla, range(10)))

print(sonuclar)
```

Kod kısa ve okunaklıdır; fakat iş parçacığı zamanlaması, işlemci çekirdekleri, Python çalışma zamanı ve görev türü performansı etkiler. Dil ayrıntıları gizler, ancak onları yok etmez. Joel Spolsky’nin meşhur ifadesiyle bütün önemsiz olmayan soyutlamalar bir noktada “sızdırır”.

## Döngüsel iyimserliğin motoru

Yeni diller genellikle gerçek bir acıya tepki olarak doğar. Eski araçların sorunları görünür, yeni aracın sorunları ise henüz keşfedilmemiştir. Bu algı farkını şöyle özetleyebiliriz:

$$Algılanan\ Yenilik = Görünür\ Faydalar - Henüz\ Görülmeyen\ Maliyetler$$

Konferanslar, şirket yatırımları ve sosyal medya da bu farkı büyütür. Bir dil yalnızca teknik araç değil; topluluk, kariyer fırsatı ve kimlik hâline gelir. İnsanlar teknolojiyi değerlendirirken bazen sözdizimini değil, umutlarını savunur.

“Nihai dil” ilanlarının kaybolması ilerlemenin başarısız olduğu anlamına gelmez. Aksine her kuşak, önceki kuşağın fikirlerini yeniden işler. Rust sahiplik sistemini yaygınlaştırır, Kotlin null güvenliğini erişilebilir kılar, TypeScript dinamik ekosisteme statik denetim ekler. Kazanan tek bir dil değil, diller arasında taşınan fikirlerdir.

Bu yüzden yeni bir dil tanıtıldığında “Hepsinin yerini alacak mı?” yerine “Hangi ödünleşimi farklı yapıyor?” diye sormak daha sağlıklıdır. Geleceğin nihai dili muhtemelen hiç gelmeyecek; fakat onu ararken geliştirdiğimiz kavramlar yazılımı sürekli daha güvenli, anlaşılır ve üretken hâle getirecektir.
