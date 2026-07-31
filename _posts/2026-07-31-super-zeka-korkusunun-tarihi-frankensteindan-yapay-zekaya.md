---
layout: post
title: "Süper Zekâ Korkusunun Tarihi: Frankenstein’dan Yapay Zekâya"
math: true
categories: 
  - Bilgi
tags: 
  - yapay zekâ
  - teknoloji tarihi
  - Frankenstein kompleksi
---

İnsanlık, yaptığı aletlerin işini kolaylaştırmasını ister; fakat aynı aletler bağımsız hareket etmeye başladığında huzursuz olur. Bir çekiç tehdit sayılmazken düşünen, karar veren veya sahibine itiraz eden bir makine neden korkutucudur? Süper zekâ tartışmalarının arkasında yalnızca teknik riskler değil, yüzyıllardır tekrarlanan kültürel bir hikâye vardır: Yaratıcının, kontrolünü kaybettiği yaratığıyla yüzleşmesi.

``

## Frankenstein kompleksi nedir?

Mary Shelley’nin 1818’de yayımlanan *Frankenstein* romanında Victor Frankenstein, cansız maddeden yaşam üretir; ancak sonucuyla karşılaşınca sorumluluk almak yerine kaçar. Roman sıklıkla “kötü canavar” öyküsü gibi hatırlansa da asıl mesele, yaratıcının kibri ve ihmalidir. Korkunun kaynağı teknoloji kadar onu amaçsız ve sevgisiz bırakan insandır.

“Frankenstein kompleksi” ifadesini daha sonra bilimkurgu yazarı Isaac Asimov popülerleştirdi. Kavram, insan yapımı varlıkların sonunda insanlara başkaldıracağı yönündeki otomatik beklentiyi anlatır. Asimov’un Üç Robot Yasası da bu korkuya verilmiş kurgusal bir mühendislik cevabıydı: Makineye en baştan güvenlik sınırları koymak.

Bu anlatının kökleri Frankenstein’dan da eskidir. Golem efsanesinde koruma amacıyla yaratılan varlık kontrolden çıkar. Sanayi Devrimi’nde makineler işçilerin geçim kaynaklarını tehdit eder. Karel Čapek’in 1920 tarihli *R.U.R.* oyununda “robot” sözcüğü doğar ve yapay işçiler isyan eder. HAL 9000, Skynet ve benzeri karakterler aynı kalıbın farklı kostümleridir.

| Dönem veya eser | İnsan yapımı güç | Temel korku |
|---|---|---|
| Golem anlatıları | Büyüyle canlandırılan varlık | Emrin yanlış uygulanması |
| *Frankenstein* | Bilimsel yaşam | Yaratıcının sorumluluğunu kaybetmesi |
| Sanayi Devrimi | Otomasyon | İş ve toplumsal statü kaybı |
| *R.U.R.* | Yapay işçiler | İsyan ve insanın gereksizleşmesi |
| Modern yapay zekâ | Öğrenen algoritmalar | Amaçların insan değerlerinden sapması |

## Korkunun matematiksel çekirdeği

Süper zekâ endişesi basitçe “makineler kötü olacak” iddiası değildir. Daha güçlü sav, çok yetenekli bir sistemin yanlış tanımlanmış hedefi olağanüstü verimlilikle gerçekleştirebileceğidir. Basitleştirilmiş risk hesabı şöyle yazılabilir:

$$R = P(K) \times Z$$

Burada $P(K)$ kontrol kaybı olasılığını, $Z$ ise gerçekleşmesi hâlindeki zararı temsil eder. Olasılık düşük olsa bile zarar çok büyükse toplam risk önemsenebilir. Buna karşılık yalnızca zararı hayal edip olasılığı, mevcut önlemleri ve teknolojinin faydasını yok saymak da sağlıklı değildir.

Bir sistemin hedefi ile insanın gerçek niyeti arasındaki farkı ise kabaca şöyle düşünebiliriz:

$$Uyum\ Hatası = |H_{insan} - H_{model}|$$

Bu matematik gerçek dünyayı eksiksiz açıklamaz; yalnızca “zekâ” ile “doğru amaç” kavramlarının aynı şey olmadığını gösterir. Çok iyi satranç oynayan bir motor, neden satranç oynadığını bilmez.

Aşağıdaki Python örneği, farklı senaryoların beklenen kaybını karşılaştıran küçük bir düşünce aracıdır:

```python
senaryolar = {
    'dar kapsamlı hata': (0.20, 10),
    'yaygın otomasyon hatası': (0.05, 500),
    'kontrol kaybı': (0.001, 100_000)
}

for ad, (olasilik, zarar) in senaryolar.items():
    beklenen_kayip = olasilik * zarar
    print(f'{ad}: {beklenen_kayip:.1f}')
```

Kod, her senaryo için olasılık ile zararı çarpar. Değerler bilimsel tahmin değildir; düşük olasılıklı fakat yüksek etkili olayların neden tartışıldığını görünür kılan temsili sayılardır.

## Neden aynı hikâyeyi tekrarlıyoruz?

Çünkü teknoloji yalnızca araçlarımızı değil, insanın özel olduğuna dair inançlarımızı da sarsar. Makine güç kazandığında kaslarımızı, hesap yaptığında zihnimizi, sanat ürettiğinde yaratıcılığımızı sorgularız. Ayrıca karmaşık sistemleri insanlaştırmaya yatkınız: Bir algoritmanın hatasını “ihanet”, beklenmedik çıktısını “niyet” olarak okuyabiliriz.

Yine de Frankenstein kompleksini bütünüyle irrasyonel saymak hatalıdır. Tarih, denetimsiz teknolojilerin çevresel, ekonomik ve askerî zararlar doğurabildiğini gösteriyor. Alınacak ders “yaratma” demek değil; hedefleri dikkatle tanımlamak, sistemleri sınamak, bağımsız denetim kurmak ve sorumluluğu makineye devretmemektir.

Belki de asıl korkmamız gereken, bilinç kazanıp bize saldıran bir süper zekâdan önce, güçlü fakat ne yaptığını anlamayan sistemleri aceleyle kullanan insanlardır. Frankenstein’ın kalıcı uyarısı da budur: Yaratığın varlığı kadar, yaratıcının davranışı önemlidir.
